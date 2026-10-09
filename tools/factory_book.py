#!/usr/bin/env python3
import argparse, copy, hashlib, json, re, subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

TARGETS=[8,12,16,10,14]
CSS="""
*{box-sizing:border-box}
html,body{margin:0;background:#fbf8ef;color:#29261f;font-family:Georgia,serif}
.page{width:100%;padding:25px 15px 58px;font:15px/1.45 Georgia,serif;color:#29261f;background:#fbf8ef}
.page p{width:329px;max-width:100%;margin:0 auto .72em}
.page p:first-child{margin-top:2px}
.page p+p{text-indent:1.5em}
"""
CORPORA=[]

JS_MEASURE_MANY=r"""carries => {
  const p=document.querySelector('.page');
  const out=[];
  for(const carry of carries){
    p.innerHTML='';
    const a=document.createElement('p'); a.textContent=carry; p.appendChild(a);
    const range=document.createRange(); range.selectNodeContents(a);
    const rects=[...range.getClientRects()].filter(r=>r.width>0&&r.height>0);
    const tops=[];
    for(const r of rects) if(!tops.some(t=>Math.abs(t-r.top)<0.75)) tops.push(r.top);
    out.push(tops.length+1);
  }
  return out;
}"""

def words(s): return re.findall(r"\S+", str(s))
def wc(s): return len(words(s))
def norm_tokens(paras): return words(" ".join(str(x) for x in paras))
def split_sentences(s):
    out=re.split(r'(?<=[.!?])\s+(?=[“‘"\'A-Z0-9])',str(s).strip())
    return [x.strip() for x in out if x.strip()]

JS_PAGE_METRICS=r"""payload => {
  const page=document.querySelector('.page');
  page.innerHTML='';
  const nodes=[];
  for(const txt of payload.paras){
    const p=document.createElement('p'); p.textContent=txt; page.appendChild(p); nodes.push(p);
  }
  const all=[];
  nodes.forEach((node,idx)=>{
    const r=document.createRange(); r.selectNodeContents(node);
    for(const x of [...r.getClientRects()].filter(x=>x.width>0&&x.height>0)){
      all.push({idx,top:x.top,bottom:x.bottom,width:x.width});
    }
  });
  const last=all.length?all[all.length-1]:null;
  const air=all.filter(x=>x.idx===payload.air_index);
  return {
    bottom:last?last.bottom:null,
    lastTop:last?last.top:null,
    lastWidth:last?last.width:null,
    airTop:air.length?air[0].top:null
  };
}"""

OVERLAP_N=10
DOUBLE_UP_TRIGGER_BOTTOM=600
DOUBLE_UP_TARGET_BOTTOM=715

def clean_tok(t):
    return re.sub(r"^\W+|\W+$","",str(t),flags=re.UNICODE).lower()

def clean_words(s):
    return [x for x in (clean_tok(t) for t in words(s)) if x]

def has_ngram_overlap(a,b,n=OVERLAP_N):
    aa=clean_words(a); bb=clean_words(b)
    if len(aa)<n or len(bb)<n: return False
    seen={tuple(aa[i:i+n]) for i in range(len(aa)-n+1)}
    return any(tuple(bb[j:j+n]) in seen for j in range(len(bb)-n+1))

def strip_adjacent_duplicate_head(cur_genuine, prev_source, next_source, stats):
    """Remove only clearly repeated leading prepared paragraphs before rebuilding."""
    out=list(cur_genuine)
    neighbours=" ".join(list(prev_source or [])+list(next_source or []))
    removed=0
    while out and has_ngram_overlap(out[0],neighbours):
        out.pop(0); removed+=1
    if removed: stats["duplicate_heads_stripped"]+=removed
    return out

def page_non_air_paras(p):
    fp=list(p.get("force_paragraphs") or p.get("paragraphs") or [])
    return [str(x) for x in fp if "$$" not in str(x)]

def page_prepared_text(p, trim_double=True):
    toks=words(" ".join(page_non_air_paras(p)))
    if trim_double:
        n=int(p.get("double_up_words") or 0)
        if n>0 and n<=len(toks): toks=toks[:-n]
    return " ".join(toks)

_HEAD_INDEX_CACHE = {}

def head_is_mid_sentence(book, head):
    """Index canonical source once per book; reused by borrowed-fill candidates."""
    key=id(book)
    entry=_HEAD_INDEX_CACHE.get(key)
    if entry is None:
        raw=[]
        for ch in book.get("chapters",[]):
            for p in ch.get("pages",[]):
                raw.extend(words(" ".join(p.get("paragraphs",[]))))
        clean=[clean_tok(x) for x in raw]
        starts=set()
        for i in range(1,len(clean)-3):
            if not is_terminal_token(raw[i-1]):
                starts.add(tuple(clean[i:i+4]))
        entry=starts
        _HEAD_INDEX_CACHE[key]=entry
    h=clean_words(head)[:4]
    return len(h)==4 and tuple(h) in entry

def apply_double_up(pages, page, stats):
    """
    DOUBLE-UP: if a prepared page is visibly stunted, extend its final paragraph
    with genuine following words until text runs below the phone window. The
    next page remains at its original break, so the added tail repeats there.
    """
    for i in range(1,len(pages)-1):
        q=pages[i]
        fp=list(q.get("force_paragraphs") or [])
        if not fp: continue
        ai=next((j for j,x in enumerate(fp) if "$$" in str(x)), -1)
        metrics=page.evaluate(JS_PAGE_METRICS,{"paras":fp,"air_index":ai})
        if metrics.get("bottom") is None: continue
        short_page=metrics["bottom"] < DOUBLE_UP_TRIGGER_BOTTOM
        ugly_tail=(metrics.get("lastWidth") or 999)<110
        # Both conditions are required. A merely short page is legitimate;
        # DOUBLE-UP is reserved for the conspicuous "tiny last line + early end"
        # specimen Stanley identified.
        if not (short_page and ugly_tail): continue
        donor=words(" ".join(pages[i+1].get("paragraphs",[])))
        if not donor: continue
        last=max((j for j,x in enumerate(fp) if "$$" not in str(x)), default=-1)
        if last<0: continue
        added=[]
        for tok in donor[:72]:
            added.append(tok)
            fp[last]=str(fp[last]).rstrip()+" "+tok
            if len(added)%6==0:
                m=page.evaluate(JS_PAGE_METRICS,{"paras":fp,"air_index":ai})
                if (m.get("bottom") or 0)>=DOUBLE_UP_TARGET_BOTTOM:
                    break
        if added:
            q["force_paragraphs"]=fp
            q["double_up_words"]=len(added)
            stats["double_up_pages"]+=1
            stats["double_up_words"]+=len(added)

def adjacency_and_head_qa(book, stats, failures):
    for ci,ch in enumerate(book.get("chapters",[])):
        pages=ch.get("pages",[])
        for pi,p in enumerate(pages):
            if pi==0:
                if any("$$" in str(x) for x in p.get("force_paragraphs",[])):
                    stats["opener_socket_failures"]+=1
                    failures.append(f"{book.get('id','?')} ch{ci+1} p1: chapter opener exposes socket")
                continue
            fp=list(p.get("force_paragraphs") or [])
            non=[str(x) for x in fp if "$$" not in str(x)]
            if non and not head_is_mid_sentence(book,non[0]):
                stats["mid_sentence_failures"]+=1
                # Phone-review diagnostic only: Keys established that a machine sentence-start flag is not itself a structural failure.
            if pi>0:
                a=page_prepared_text(pages[pi-1],trim_double=True)
                b=page_prepared_text(p,trim_double=True)
                if has_ngram_overlap(a,b):
                    stats["adjacent_overlap_failures"]+=1
                    # Phone-review diagnostic only: textual overlap is not itself a visual-retention failure.

def para_hash(book):
    payload=json.dumps([[p.get("paragraphs",[]) for p in c.get("pages",[])] for c in book.get("chapters",[])],
                       ensure_ascii=False,separators=(",",":"))
    return hashlib.sha256(payload.encode()).hexdigest()
def extract_page(p):
    fp=list(p.get("force_paragraphs") or [])
    airs=[(i,x) for i,x in enumerate(fp) if "$$" in str(x)]
    if len(airs)!=1: return None
    ai,air=airs[0]
    # Deterministic rebuild: canonical paragraphs are always the prose starting
    # point. Never feed a previous factory's plasticine output back in.
    genuine=[str(x) for x in p.get("paragraphs",[]) if str(x).strip()]
    return {"genuine":genuine,"air":air,"old_ai":ai}

def is_terminal_token(tok):
    t=str(tok).strip()
    if not t: return False
    bare=re.sub(r"[”\\\"’')\\]]+$","",t)
    low=bare.lower()
    if low in {"mr.","mrs.","ms.","dr.","prof.","sr.","jr.","st.","vs.","etc.","e.g.","i.e.","no.","nos.","fig.","ch."}:
        return False
    if re.fullmatch(r"[A-Za-z]\\.",bare):
        return False
    return bool(re.search(r"[.!?][”\\\"’')\\]]*$",t))

def candidate_splits(genuine, measure_many, target, prev_line, history, protect_first=True):
    """
    Hard local law:
    - next page begins inside a sentence;
    - the airlock follows a proper completed sentence.
    No global stitching or OCR repair is attempted.
    """
    if not genuine:
        return [], "NO_GENUINE_DONOR"
    floor=1 if protect_first else 0
    available=len(genuine)-floor
    if available<=0:
        return [], "NO_AVAILABLE_DONOR"

    raw=[]
    for k in range(1,available+1):
        # Prepared-layer paragraph boundaries are flexible camouflage.
        # Join as many donor paragraphs as needed to create a legal pump block;
        # genuine word order remains inviolable.
        donor=" ".join(str(x).strip() for x in genuine[-k:] if str(x).strip()).strip()
        toks=words(donor)
        if len(toks)<18: continue
        prefix_words=sum(wc(x) for x in genuine[:-k])
        lo=max(4,36-prefix_words)
        hi=len(toks)-6
        for cut in range(lo,hi+1):
            if is_terminal_token(toks[cut-1]):
                continue
            ends=[]
            for end in range(cut+4,min(len(toks),cut+320)+1):
                if is_terminal_token(toks[end-1]):
                    ends.append(end)
                    if len(ends)>=12:
                        break
            for end in ends:
                head=" ".join(toks[:cut]).strip()
                carry=" ".join(toks[cut:end]).strip()
                remainder=" ".join(toks[end:]).strip()
                if prefix_words+wc(head)<45: continue
                raw.append({"k":k,"head":head,"carry":carry,"remainder":remainder})

    if not raw:
        return [], "NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT"

    lines=measure_many([x["carry"] for x in raw])
    cands=[]
    for x,line in zip(raw,lines):
        if line is None: continue
        if prev_line is not None and abs(line-prev_line)<4:
            # Keep the hard spacing law, but permit a second-pass search below
            # to choose a different legal target rather than declaring defeat.
            continue
        if len(history)>=2 and history[-2] is not None and history[-1] is not None:
            vals=[history[-2],history[-1],line]
            if max(vals)-min(vals)<=4:
                continue
        score=abs(line-target)*10+abs(wc(x["carry"])-80)/24+x["k"]*.03
        cands.append((score,x["k"],x["head"],x["carry"],x["remainder"],line))
    cands.sort(key=lambda x:x[0])
    if not cands:
        return [], "SPACING_OR_RETENTION_CONFLICT"
    return cands, "OK"

def candidate_boundary_slide(genuine, measure_many, target, prev_line, history):
    """
    Plasticine fallback: slide the prepared page boundary forward into the
    current page. Move an opening prefix back onto the previous page so the
    current page begins mid-sentence, then carry through to the next genuine
    sentence ending before the airlock.
    """
    if not genuine:
        return [], "NO_CURRENT_TEXT_FOR_BOUNDARY_SLIDE"
    raw=[]
    max_join=len(genuine)
    for k in range(1,max_join+1):
        donor=" ".join(str(x).strip() for x in genuine[:k] if str(x).strip()).strip()
        toks=words(donor)
        if len(toks)<10:
            continue
        for cut in range(2,len(toks)-4):
            if is_terminal_token(toks[cut-1]):
                continue
            ends=[]
            for end in range(cut+6,min(len(toks),cut+260)+1):
                if is_terminal_token(toks[end-1]):
                    ends.append(end)
                    if len(ends)>=8:
                        break
            for end in ends:
                prefix=" ".join(toks[:cut]).strip()
                carry=" ".join(toks[cut:end]).strip()
                remainder=" ".join(toks[end:]).strip()
                raw.append({"k":k,"prefix":prefix,"carry":carry,"remainder":remainder})
    if not raw:
        return [], "NO_BOUNDARY_SLIDE_SPLIT"
    lines=measure_many([x["carry"] for x in raw])
    cands=[]
    for x,line in zip(raw,lines):
        if line is None:
            continue
        if prev_line is not None and abs(line-prev_line)<4:
            continue
        if len(history)>=2 and history[-2] is not None and history[-1] is not None:
            vals=[history[-2],history[-1],line]
            if max(vals)-min(vals)<=4:
                continue
        score=abs(line-target)*10+abs(wc(x["carry"])-80)/24+x["k"]*.03
        cands.append((score,x["k"],x["prefix"],x["carry"],x["remainder"],line))
    cands.sort(key=lambda x:x[0])
    if not cands:
        return [], "BOUNDARY_SLIDE_SPACING_CONFLICT"
    return cands, "OK"

def candidate_emergency_slide(genuine, measure_many, target, prev_line, history):
    """
    Last-resort plasticine pass for pathological pages.
    Treat the current prepared page as one continuous token stream, ignore its
    paragraph boundaries entirely, and slide the boundary at any non-terminal
    token so the visible page begins mid-sentence and reaches a clean terminal
    before the airlock. Genuine token order is still preserved.
    """
    donor=" ".join(str(x).strip() for x in genuine if str(x).strip()).strip()
    toks=words(donor)
    if len(toks)<6:
        return [], "NO_EMERGENCY_DONOR"
    raw=[]
    def loose_terminal(tok):
        t=str(tok).strip()
        return bool(re.search(r"[.!?][”\"’')\\]]*$", t))
    for cut in range(1,len(toks)-2):
        if loose_terminal(toks[cut-1]):
            continue
        for end in range(cut+2,min(len(toks),cut+400)+1):
            if not loose_terminal(toks[end-1]):
                continue
            prefix=" ".join(toks[:cut]).strip()
            carry=" ".join(toks[cut:end]).strip()
            remainder=" ".join(toks[end:]).strip()
            raw.append({"prefix":prefix,"carry":carry,"remainder":remainder})
            if len(raw)>=2500:
                break
        if len(raw)>=2500:
            break
    if not raw:
        return [], "NO_EMERGENCY_SPLIT"
    measured=measure_many([x["carry"] for x in raw])
    cands=[]
    for x,line in zip(raw,measured):
        if line is None:
            continue
        if prev_line is not None and abs(line-prev_line)<4:
            continue
        if len(history)>=2 and history[-2] is not None and history[-1] is not None:
            vals=[history[-2],history[-1],line]
            if max(vals)-min(vals)<=4:
                continue
        score=abs(line-target)*10+abs(wc(x["carry"])-80)/24
        cands.append((score,x["prefix"],x["carry"],x["remainder"],line))
    cands.sort(key=lambda x:x[0])
    if not cands:
        return [], "EMERGENCY_SPACING_CONFLICT"
    return cands, "OK"

def candidate_borrowed_fill(book, chapter_index, page_index, measure_many, target, prev_line, history):
    """
    Final factory fallback. Borrow stylistically native prose from elsewhere in
    the same book to manufacture a convincing prepared-page head when all local
    plasticine options fail. Source/genuine corpus remains untouched; borrowed
    material exists only in the prepared force layer and is explicitly reported.
    Preference order: same chapter -> nearby chapters -> anywhere in same book.
    """
    pools=[]
    chapters=book.get("chapters",[])
    # 1) same chapter, excluding current page
    same=[]
    if 0 <= chapter_index < len(chapters):
        for j,p in enumerate(chapters[chapter_index].get("pages",[])):
            if j in {page_index-1,page_index,page_index+1}: continue
            same += [str(x).strip() for x in p.get("paragraphs",[]) if str(x).strip()]
    pools.append(("SAME_CHAPTER", same))

    # 2) nearby chapters
    near=[]
    for dist in range(1,4):
        for ci in (chapter_index-dist, chapter_index+dist):
            if 0 <= ci < len(chapters):
                for p in chapters[ci].get("pages",[]):
                    near += [str(x).strip() for x in p.get("paragraphs",[]) if str(x).strip()]
    pools.append(("NEARBY_CHAPTER", near))

    # 3) whole book
    whole=[]
    for ci,ch in enumerate(chapters):
        if ci==chapter_index: continue
        for p in ch.get("pages",[]):
            whole += [str(x).strip() for x in p.get("paragraphs",[]) if str(x).strip()]
    pools.append(("SAME_BOOK", whole))

    def loose_terminal(tok):
        t=str(tok).strip()
        return bool(re.search(r"[.!?][”\"’')\\]]*$", t))

    for source_class, paras in pools:
        toks=words(" ".join(paras))
        if len(toks)<20:
            continue
        raw=[]
        # Search bounded windows so the fallback remains deterministic and fast.
        max_start=max(1, min(len(toks)-12, 12000))
        for start in range(0,max_start,7):
            for cut in range(start+2,min(start+80,len(toks)-6)):
                if loose_terminal(toks[cut-1]):
                    continue
                for end in range(cut+4,min(len(toks),cut+180)+1):
                    if not loose_terminal(toks[end-1]):
                        continue
                    carry=" ".join(toks[cut:end]).strip()
                    raw.append((carry, start, cut, end))
                    if len(raw)>=1200:
                        break
                if len(raw)>=1200:
                    break
            if len(raw)>=1200:
                break
        if not raw:
            continue
        # Reject non-native or adjacent-overlap prose before expensive Chromium measurements.
        prev_src=" ".join(chapters[chapter_index].get("pages",[])[page_index-1].get("paragraphs",[])) if page_index>0 else ""
        next_src=" ".join(chapters[chapter_index].get("pages",[])[page_index+1].get("paragraphs",[])) if page_index+1<len(chapters[chapter_index].get("pages",[])) else ""
        raw=[x for x in raw if not has_ngram_overlap(x[0],prev_src) and not has_ngram_overlap(x[0],next_src) and head_is_mid_sentence(book,x[0])]
        if not raw: continue
        measured=measure_many([x[0] for x in raw])
        cands=[]
        prev_src=" ".join(chapters[chapter_index].get("pages",[])[page_index-1].get("paragraphs",[])) if page_index>0 else ""
        next_src=" ".join(chapters[chapter_index].get("pages",[])[page_index+1].get("paragraphs",[])) if page_index+1<len(chapters[chapter_index].get("pages",[])) else ""
        for (carry,start,cut,end),line in zip(raw,measured):
            if line is None:
                continue
            if has_ngram_overlap(carry,prev_src) or has_ngram_overlap(carry,next_src):
                continue
            if not head_is_mid_sentence(book,carry):
                continue
            if prev_line is not None and abs(line-prev_line)<4:
                continue
            if len(history)>=2 and history[-2] is not None and history[-1] is not None:
                vals=[history[-2],history[-1],line]
                if max(vals)-min(vals)<=4:
                    continue
            score=abs(line-target)*10+abs(wc(carry)-80)/24
            cands.append((score,carry,line,source_class,start,cut,end))
        cands.sort(key=lambda x:x[0])
        if cands:
            return cands, "OK"
    return [], "NO_BORROWED_FILL_CANDIDATE"

def rebuild_page(orig, genuine, air, forceable):
    q=copy.deepcopy(orig)
    if not forceable:
        return q
    if not genuine:
        return q
    q["force_paragraphs"]=[genuine[0],air]+genuine[1:]
    q["airlock_index"]=1
    q["pre_airlock_words"]=wc(genuine[0])
    return q

def repair_book(book,page,stats,failures,unresolved_details,borrowed_details):
    before_hash=para_hash(book)
    before_stream=[]
    after_stream=[]
    for ci,ch in enumerate(book.get("chapters",[])):
        pages=ch.get("pages",[])
        if not pages: continue
        prepared=[]
        original_genuine=[]
        chapter_ok=True
        for pi,p in enumerate(pages):
            e=extract_page(p)
            if not e and pi==0:
                # Approved chapter openers are deliberately socket-free.
                if "$$" not in " ".join(str(x) for x in p.get("force_paragraphs",[])):
                    e={"genuine":list(p.get("paragraphs",[])),"air":None,"old_ai":None}
            if not e:
                failures.append(f"{book.get('id','?')} ch{ci+1} p{pi+1}: socket count !=1")
                chapter_ok=False; break
            prepared.append(e)
            original_genuine.append(list(e["genuine"]))
            # Prepared force text is intentionally plasticine; canonical paragraphs are source truth.
            before_stream += norm_tokens(p.get("paragraphs",[]))
        if not chapter_ok:
            stats["chapters_skipped"]+=1
            continue

        lines=[]
        unresolved=[False]*len(prepared)
        legality=[None]*len(prepared)

        for pi in range(1,len(prepared)):
            target=TARGETS[(pi-1)%len(TARGETS)]
            prev=prepared[pi-1]
            cur=prepared[pi]
            cur["genuine"]=strip_adjacent_duplicate_head(
                cur["genuine"],
                pages[pi-1].get("paragraphs",[]),
                pages[pi+1].get("paragraphs",[]) if pi+1<len(pages) else [],
                stats
            )
            # Immediately after a genuine chapter opener, do not manufacture the
            # next head from prose the spectator has just seen on that opener.
            if pi==1:
                cands,reason=[],"CHAPTER_OPENER_VISUAL_RETENTION_GUARD"
            else:
                cands,reason=candidate_splits(
                    prev["genuine"],
                    lambda arr:page.evaluate(JS_MEASURE_MANY,arr),
                    target,
                    lines[-1] if lines else None,
                    lines,
                    protect_first=(pi-1)>0
                )
            if not cands:
                slide,slide_reason=candidate_boundary_slide(
                    cur["genuine"],
                    lambda arr:page.evaluate(JS_MEASURE_MANY,arr),
                    target,
                    lines[-1] if lines else None,
                    lines
                )
                if slide:
                    _,k,prefix,carry,remainder,line=slide[0]
                    prev["genuine"]=prev["genuine"]+[prefix]
                    tail=cur["genuine"][k:]
                    injected=[carry]
                    if remainder:
                        injected.append(remainder)
                    cur["genuine"]=injected+tail
                    reason="BOUNDARY_SLIDE"
                    stats["boundary_slides"]+=1
                else:
                    emergency,emergency_reason=candidate_emergency_slide(
                        cur["genuine"],
                        lambda arr:page.evaluate(JS_MEASURE_MANY,arr),
                        target,
                        lines[-1] if lines else None,
                        lines
                    )
                    if emergency:
                        _,prefix,carry,remainder,line=emergency[0]
                        prev["genuine"]=prev["genuine"]+[prefix]
                        cur["genuine"]=[carry]+([remainder] if remainder else [])
                        reason="EMERGENCY_PLASTICINE"
                        stats["emergency_slides"]+=1
                    else:
                        borrowed,borrow_reason=candidate_borrowed_fill(
                            book,
                            ci,
                            pi,
                            lambda arr:page.evaluate(JS_MEASURE_MANY,arr),
                            target,
                            lines[-1] if lines else None,
                            lines
                        )
                        if borrowed:
                            _,carry,line,source_class,start,cut,end=borrowed[0]
                            # Borrowed prose is prepared-layer camouflage only.
                            # Genuine paragraphs and source token stream remain untouched.
                            cur["genuine"]=[carry]+cur["genuine"]
                            reason="BORROWED_FILL_"+source_class
                            stats["borrowed_fill_pages"]+=1
                            borrowed_details.append({
                                "book":book.get("id","?"),
                                "chapter":ci+1,
                                "page":pi+1,
                                "source_class":source_class,
                                "target":target,
                                "line":line
                            })
                        else:
                            unresolved[pi]=True
                            stats["unresolved_pages"]+=1
                            unresolved_details.append({
                                "book":book.get("id","?"),
                                "chapter":ci+1,
                                "page":pi+1,
                                "target":target,
                                "reason":reason+" / "+slide_reason+" / "+emergency_reason+" / "+borrow_reason,
                                "previous_line":lines[-1] if lines else None
                            })
                            lines.append(None)
                            continue
            else:
                _,k,head,carry,remainder,line=cands[0]
                prev["genuine"]=prev["genuine"][:-k]+[head]
                injected=[carry]
                if remainder:
                    injected.append(remainder)
                cur["genuine"]=injected+cur["genuine"]
            legality[pi]=(True, is_terminal_token(words(carry)[-1]) if words(carry) else False)
            lines.append(line)
            stats["forceable_pages"]+=1
            stats["line_abs_error"]+=abs(line-target)
            if line==target: stats["exact_hits"]+=1
            elif abs(line-target)==1: stats["within1"]+=1
            elif abs(line-target)==2: stats["within2"]+=1
            else: stats["beyond2"]+=1

        final_lines=[]
        for pi,p in enumerate(pages):
            q=copy.deepcopy(p)
            g=prepared[pi]["genuine"]
            if pi==0:
                # Chapter openers are always socket-free in the prepared layer.
                q["force_paragraphs"]=list(g)
                q.pop("airlock_index",None)
                q.pop("pre_airlock_words",None)
                final_lines.append(None)
            elif not unresolved[pi] and g:
                q["force_paragraphs"]=[g[0],prepared[pi]["air"]]+g[1:]
                q["airlock_index"]=1
                q["pre_airlock_words"]=wc(g[0])
                final_lines.append(page.evaluate(JS_MEASURE_MANY,[g[0]])[0])
                if not legality[pi] or not legality[pi][0]:
                    stats["mid_sentence_failures"]+=1
                if not legality[pi] or not legality[pi][1]:
                    stats["airlock_left_terminal_failures"]+=1
            else:
                if g!=original_genuine[pi] and g:
                    oldai=prepared[pi]["old_ai"]
                    ai=max(0,min(oldai,len(g)))
                    fp=list(g); fp.insert(ai,prepared[pi]["air"])
                    q["force_paragraphs"]=fp
                    q["airlock_index"]=ai
                final_lines.append(None)

            if q.get("force_paragraphs")!=p.get("force_paragraphs"):
                stats["pages_changed"]+=1
            pages[pi]=q
            after_stream += norm_tokens(q.get("paragraphs",[]))

        apply_double_up(pages,page,stats)

        for i in range(1,len(final_lines)):
            a,b=final_lines[i-1],final_lines[i]
            if a is None or b is None: continue
            if abs(b-a)<4:
                stats["spacing_violations"]+=1
        for i in range(2,len(final_lines)):
            tri=final_lines[i-2:i+1]
            if any(x is None for x in tri): continue
            if max(tri)-min(tri)<=4:
                stats["retention_windows"]+=1

    if before_stream!=after_stream:
        failures.append(f"{book.get('id','?')}: canonical source token order mismatch after repair")
        stats["token_mismatches"]+=1
    if para_hash(book)!=before_hash:
        failures.append(f"{book.get('id','?')}: genuine paragraphs changed")
        stats["genuine_hash_mismatches"]+=1
    adjacency_and_head_qa(book,stats,failures)
    return book

def process_copy(path,page,write,allstats,failures,unresolved_details,borrowed_details):
    book=json.loads(path.read_text())
    stats={k:0 for k in ["forceable_pages","pages_changed","exact_hits","within1","within2","beyond2",
                         "spacing_violations","retention_windows","unresolved_pages","chapters_skipped",
                         "token_mismatches","genuine_hash_mismatches","mid_sentence_failures","airlock_left_terminal_failures","boundary_slides","emergency_slides","borrowed_fill_pages","line_abs_error","duplicate_heads_stripped","adjacent_overlap_failures","opener_socket_failures","double_up_pages","double_up_words"]}
    repaired=repair_book(book,page,stats,failures,unresolved_details,borrowed_details)
    if write: path.write_text(json.dumps(repaired,ensure_ascii=False,separators=(",",":")))
    for k,v in stats.items(): allstats[k]+=v
    return stats

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--write",action="store_true")
    ap.add_argument("--corpus",required=True)
    ap.add_argument("--report")
    args=ap.parse_args()
    global CORPORA
    CORPORA=[args.corpus]
    if not args.report:
        stem=Path(args.corpus).stem
        args.report=f"docs/checkpoints/2026-10-07_autopilot_{stem}.md"
    authorities=[]
    for rel in CORPORA:
        pub=Path("public")/rel
        root=Path(rel)
        if pub.exists(): authorities.append((rel,pub,root if root.exists() else None))
        elif root.exists(): authorities.append((rel,root,None))
    failures=[]
    unresolved_details=[]
    borrowed_details=[]
    totals={k:0 for k in ["forceable_pages","pages_changed","exact_hits","within1","within2","beyond2",
                         "spacing_violations","retention_windows","unresolved_pages","chapters_skipped",
                         "token_mismatches","genuine_hash_mismatches","mid_sentence_failures","airlock_left_terminal_failures","boundary_slides","emergency_slides","borrowed_fill_pages","line_abs_error","duplicate_heads_stripped","adjacent_overlap_failures","opener_socket_failures","double_up_pages","double_up_words"]}
    per=[]
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        pg=browser.new_page(viewport={"width":414,"height":736},device_scale_factor=1)
        pg.set_content(f"<!doctype html><style>{CSS}</style><div class='page'></div>")
        for rel,path,mirror in authorities:
            st=process_copy(path,pg,args.write,totals,failures,unresolved_details,borrowed_details)
            per.append((str(path),st))
            if args.write and mirror is not None:
                mirror.parent.mkdir(parents=True,exist_ok=True)
                mirror.write_bytes(path.read_bytes())
        browser.close()

    # parity check for root/public copies where both exist
    parity=[]
    for rel in CORPORA:
        a=Path(rel); b=Path("public")/rel
        if a.exists() and b.exists():
            same=a.read_bytes()==b.read_bytes()
            parity.append((rel,same))
            if not same: failures.append(f"{rel}: root/public parity FAIL")

    passed=not failures and totals["unresolved_pages"]==0 and totals["spacing_violations"]==0 and totals["airlock_left_terminal_failures"]==0 and totals["opener_socket_failures"]==0
    avg=(totals["line_abs_error"]/totals["forceable_pages"]) if totals["forceable_pages"] else 0
    lines=[
      f"# Factory autopilot — {Path(args.corpus).stem} — 7 Oct 2026","",
      "**Single-book branch automation. Production main untouched.**","",
      "Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; pathological pages may use an **emergency plasticine token-stream slide** while preserving genuine token order; if that still fails, the factory may use **flagged borrowed-fill camouflage from elsewhere in the same book** (same chapter preferred, then nearby chapters, then same book); socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.","",
      "Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.","",
      "## Compact QA",
      f"- forceable prepared pages repaired: **{totals['forceable_pages']}**",
      f"- pages whose force layer changed: **{totals['pages_changed']}**",
      f"- exact target hits: **{totals['exact_hits']}**",
      f"- ±1 line: **{totals['within1']}**",
      f"- ±2 lines: **{totals['within2']}**",
      f"- >2 lines: **{totals['beyond2']}**",
      f"- mean absolute target error: **{avg:.2f} lines**",
      f"- adjacent <4-line spacing violations: **{totals['spacing_violations']}**",
      f"- 3-page retention windows within 4-line band: **{totals['retention_windows']}**",
      f"- unresolved prepared pages: **{totals['unresolved_pages']}**",
      f"- skipped chapters: **{totals['chapters_skipped']}**",
      f"- genuine paragraph hash mismatches: **{totals['genuine_hash_mismatches']}**",
      f"- canonical source token-order mismatches: **{totals['token_mismatches']}**",
      f"- page-head mid-sentence failures: **{totals['mid_sentence_failures']}**",
      f"- local prepared-boundary slides used: **{totals['boundary_slides']}**",
      f"- emergency plasticine slides used: **{totals['emergency_slides']}**",
      f"- borrowed-fill prepared pages used: **{totals['borrowed_fill_pages']}**",
      f"- airlock-left sentence-completion failures: **{totals['airlock_left_terminal_failures']}**",
      f"- adjacent prose-overlap failures: **{totals['adjacent_overlap_failures']}**",
      f"- chapter-opener socket failures: **{totals['opener_socket_failures']}**",
      f"- duplicate prepared heads stripped before rebuild: **{totals['duplicate_heads_stripped']}**",
      f"- DOUBLE-UP pages: **{totals['double_up_pages']}** ({totals['double_up_words']} repeated packing words)",
      f"- root/public corpus parity failures: **{sum(1 for _,ok in parity if not ok)}**","",
      f"## Machine verdict: **{'PASS' if passed else 'HOLD'}**",""
    ]
    if unresolved_details:
        from collections import Counter
        counts=Counter(x["reason"] for x in unresolved_details)
        lines+=["## Unresolved classification"]
        for reason,count in sorted(counts.items()):
            lines.append(f"- {reason}: **{count}**")
        lines+=["","## Unresolved locations"]
        for x in unresolved_details:
            lines.append(f"- ch{x['chapter']} p{x['page']} — {x['reason']} — target {x['target']} — previous line {x['previous_line']}")
        lines+=[""]
    if borrowed_details:
        lines+=["## Borrowed-fill exceptions"]
        for x in borrowed_details:
            lines.append(f"- ch{x['chapter']} p{x['page']} — {x['source_class']} — target {x['target']} — rendered line {x['line']}")
        lines+=[""]
    if failures:
        lines+=["## Failures"]+[f"- {x}" for x in failures[:80]]
    else:
        lines+=["No machine-QA invariant failures detected. Borrowed-fill camouflage is permitted only when explicitly flagged; canonical source paragraphs remain the authority.","","Next action: autopilot continues. Human intervention is required only for consolidated structural exceptions or final phone QA."]
    rp=Path(args.report); rp.parent.mkdir(parents=True,exist_ok=True); rp.write_text("\n".join(lines)+"\n")
    print("\n".join(lines[:30]))
    if not passed: raise SystemExit(2)

if __name__=="__main__": main()
