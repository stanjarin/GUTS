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
CORPORA=["PERFORMANCE35/jeeves_035.json"]

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
def para_hash(book):
    payload=json.dumps([[p.get("paragraphs",[]) for p in c.get("pages",[])] for c in book.get("chapters",[])],
                       ensure_ascii=False,separators=(",",":"))
    return hashlib.sha256(payload.encode()).hexdigest()
def extract_page(p):
    fp=list(p.get("force_paragraphs") or [])
    airs=[(i,x) for i,x in enumerate(fp) if "$$$" in str(x)]
    if len(airs)!=1: return None
    ai,air=airs[0]
    genuine=[x for i,x in enumerate(fp) if i!=ai]
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
            for end in range(cut+6,min(len(toks),cut+260)+1):
                if is_terminal_token(toks[end-1]):
                    ends.append(end)
                    if len(ends)>=8:
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
    max_join=min(4,len(genuine))
    for k in range(1,max_join+1):
        donor=" ".join(str(x).strip() for x in genuine[:k] if str(x).strip()).strip()
        toks=words(donor)
        if len(toks)<14:
            continue
        for cut in range(4,len(toks)-6):
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

def repair_book(book,page,stats,failures,unresolved_details):
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
            if not e:
                failures.append(f"{book.get('id','?')} ch{ci+1} p{pi+1}: socket count !=1")
                chapter_ok=False; break
            if norm_tokens(e["genuine"])!=norm_tokens(p.get("paragraphs",[])):
                failures.append(f"{book.get('id','?')} ch{ci+1} p{pi+1}: prepared/genuine page token mismatch")
                chapter_ok=False; break
            prepared.append(e)
            original_genuine.append(list(e["genuine"]))
            before_stream += norm_tokens(e["genuine"])
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
                    unresolved[pi]=True
                    stats["unresolved_pages"]+=1
                    unresolved_details.append({
                        "book":book.get("id","?"),
                        "chapter":ci+1,
                        "page":pi+1,
                        "target":target,
                        "reason":reason+" / "+slide_reason,
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
            if pi>0 and not unresolved[pi] and g:
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
            after_stream += norm_tokens([x for x in q.get("force_paragraphs",[]) if "$$$" not in str(x)])

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
        failures.append(f"{book.get('id','?')}: chapter-stream token order mismatch after repair")
        stats["token_mismatches"]+=1
    if para_hash(book)!=before_hash:
        failures.append(f"{book.get('id','?')}: genuine paragraphs changed")
        stats["genuine_hash_mismatches"]+=1
    return book

def process_copy(path,page,write,allstats,failures,unresolved_details):
    book=json.loads(path.read_text())
    stats={k:0 for k in ["forceable_pages","pages_changed","exact_hits","within1","within2","beyond2",
                         "spacing_violations","retention_windows","unresolved_pages","chapters_skipped",
                         "token_mismatches","genuine_hash_mismatches","mid_sentence_failures","airlock_left_terminal_failures","boundary_slides","line_abs_error"]}
    repaired=repair_book(book,page,stats,failures,unresolved_details)
    if write: path.write_text(json.dumps(repaired,ensure_ascii=False,separators=(",",":")))
    for k,v in stats.items(): allstats[k]+=v
    return stats

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--write",action="store_true")
    ap.add_argument("--report",default="docs/checkpoints/2026-10-06_jeeves-factory-pilot-report.md")
    args=ap.parse_args()
    authorities=[]
    for rel in CORPORA:
        pub=Path("public")/rel
        root=Path(rel)
        if pub.exists(): authorities.append((rel,pub,root if root.exists() else None))
        elif root.exists(): authorities.append((rel,root,None))
    failures=[]
    unresolved_details=[]
    totals={k:0 for k in ["forceable_pages","pages_changed","exact_hits","within1","within2","beyond2",
                         "spacing_violations","retention_windows","unresolved_pages","chapters_skipped",
                         "token_mismatches","genuine_hash_mismatches","mid_sentence_failures","airlock_left_terminal_failures","boundary_slides","line_abs_error"]}
    per=[]
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        pg=browser.new_page(viewport={"width":414,"height":736},device_scale_factor=1)
        pg.set_content(f"<!doctype html><style>{CSS}</style><div class='page'></div>")
        for rel,path,mirror in authorities:
            st=process_copy(path,pg,args.write,totals,failures,unresolved_details)
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

    passed=not failures and totals["unresolved_pages"]==0 and totals["spacing_violations"]==0 and totals["retention_windows"]==0 and totals["mid_sentence_failures"]==0 and totals["airlock_left_terminal_failures"]==0
    avg=(totals["line_abs_error"]/totals["forceable_pages"]) if totals["forceable_pages"] else 0
    lines=[
      "# Jeeves factory pilot — 6 Oct 2026","",
      "**Jeeves-only branch automation. Production main and all other books untouched.**","",
      "Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.","",
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
      f"- genuine token-order mismatches: **{totals['token_mismatches']}**",
      f"- page-head mid-sentence failures: **{totals['mid_sentence_failures']}**",
      f"- local prepared-boundary slides used: **{totals['boundary_slides']}**",
      f"- airlock-left sentence-completion failures: **{totals['airlock_left_terminal_failures']}**",
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
    if failures:
        lines+=["## Failures"]+[f"- {x}" for x in failures[:80]]
    else:
        lines+=["No machine-QA invariant failures detected.","","Next action: Builder diagnoses unresolved classes and revises factory; Stanley phone QA only after a clean candidate exists."]
    rp=Path(args.report); rp.parent.mkdir(parents=True,exist_ok=True); rp.write_text("\n".join(lines)+"\n")
    print("\n".join(lines[:30]))
    if not passed: raise SystemExit(2)

if __name__=="__main__": main()
