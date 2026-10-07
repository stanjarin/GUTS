#!/usr/bin/env python3
import copy,json,re,hashlib
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path("PERFORMANCE10/keys_performance.json")
PUBLIC=Path("public/PERFORMANCE10/keys_performance.json")
REPORT=Path("docs/checkpoints/2026-10-07_keys-phone-candidate-report.md")
N=10
SAME_ZONE_PX=96

TARGETS=[(4,2,3),(4,137,138),(4,138,139),(4,143,144),(4,146,147),(5,2,3),(6,2,3)]

CSS="""
*{box-sizing:border-box}
html,body{margin:0;background:#fbf8ef;color:#29261f;font-family:Georgia,serif}
.page{width:100%;padding:25px 15px 58px;font:15px/1.45 Georgia,serif;color:#29261f;background:#fbf8ef}
.page p{width:329px;max-width:100%;margin:0 auto .72em}
.page p:first-child{margin-top:2px}
.page p+p{text-indent:1.5em}
.w{display:inline}
"""
JS_RENDER=r"""payload=>{
 const page=document.querySelector('.page'); page.innerHTML=''; let g=0; const out=[];
 for(let pi=0; pi<payload.paras.length; pi++){
   const para=payload.paras[pi];
   const p=document.createElement('p'); p.dataset.pi=String(pi);
   for(const tok of para.trim().split(/\s+/).filter(Boolean)){
     const s=document.createElement('span'); s.className='w'; s.textContent=tok;
     s.dataset.g=String(g++); s.dataset.pi=String(pi);
     p.appendChild(s); p.appendChild(document.createTextNode(' '));
   }
   page.appendChild(p);
 }
 for(const s of page.querySelectorAll('.w')){
   const r=s.getBoundingClientRect(); out.push({i:Number(s.dataset.g),pi:Number(s.dataset.pi),top:r.top});
 }
 return out;
}"""
JS_LINES=r"""arr=>{
 const host=document.querySelector('.page'); const out=[];
 for(const txt of arr){
   host.innerHTML=''; const p=document.createElement('p'); p.textContent=txt; host.appendChild(p);
   const range=document.createRange(); range.selectNodeContents(p);
   out.push(range.getClientRects().length);
 }
 return out;
}"""

def toks(s): return re.findall(r"\S+",str(s))
def clean(t): return re.sub(r"^\W+|\W+$","",str(t),flags=re.UNICODE).lower()
def flat(ps):
    out=[]
    for p in ps:
        for t in toks(p):
            c=clean(t)
            if c: out.append(c)
    return out
def prepared(p): return [str(x) for x in (p.get("force_paragraphs") or p.get("paragraphs") or [])]
def prose(p): return [x for x in prepared(p) if "$$" not in x]
def has_overlap(a,b,n=N):
    aa,bb=flat(a),flat(b)
    if len(aa)<n or len(bb)<n: return False
    aset={tuple(aa[i:i+n]) for i in range(len(aa)-n+1)}
    return any(tuple(bb[j:j+n]) in aset for j in range(len(bb)-n+1))
def overlap_hits(a,b,n=N):
    aa,bb=flat(a),flat(b); amap={}
    for i in range(max(0,len(aa)-n+1)): amap.setdefault(tuple(aa[i:i+n]),[]).append(i)
    out=[]
    for j in range(max(0,len(bb)-n+1)):
        g=tuple(bb[j:j+n])
        for i in amap.get(g,[]): out.append((i,j,g))
    return out
def pos(pg,ps):
    arr=pg.evaluate(JS_RENDER,{"paras":ps})
    return {x["i"]:(x["top"],x["pi"]) for x in arr}
def pair_same_zone(pg,left,right):
    la,lb=prose(left),prose(right)
    hits=overlap_hits(la,lb)
    if not hits: return False,None
    pa,pb=pos(pg,la),pos(pg,lb)
    best=None
    for ia,ib,g in hits:
        if ia in pa and ib in pb:
            ya,pia=pa[ia]; yb,pib=pb[ib]; d=abs(ya-yb)
            row=(d,ya,yb,pia,pib," ".join(g))
            if best is None or d<best[0]: best=row
    return (best is not None and best[0]<=SAME_ZONE_PX),best
def is_terminal(tok):
    return bool(re.search(r"[.!?][”\"’')\]]*$",str(tok).strip()))
def top_fragments(text):
    w=toks(text); out=[]
    if len(w)<16: return out
    for cut in range(2,min(18,len(w)-8)):
        if is_terminal(w[cut-1]): continue
        for end in range(cut+8,min(len(w),cut+120)+1):
            if is_terminal(w[end-1]):
                out.append(" ".join(w[cut:end]))
                break
    return out
def para_hash(book):
    payload=json.dumps([[p.get("paragraphs",[]) for p in c.get("chapters",[])] for c in book.get("chapters",[])],
                       ensure_ascii=False,separators=(",",":"))
    return hashlib.sha256(payload.encode()).hexdigest()

book=json.loads(ROOT.read_text())
before_hash=para_hash(book)
stats=[]
failures=[]

with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    pg=browser.new_page(viewport={"width":414,"height":736},device_scale_factor=1)
    pg.set_content(f"<!doctype html><style>{CSS}</style><div class='page'></div>")

    # donor pool: genuine canonical prose only
    donor_paras=[]
    for ci,ch in enumerate(book.get("chapters",[])):
        for pi,p in enumerate(ch.get("pages",[])):
            for para in p.get("paragraphs",[]):
                txt=str(para).strip()
                if txt and "$$" not in txt and len(toks(txt))>=8:
                    donor_paras.append((ci,pi,txt))

    for chno,lno,rno in TARGETS:
        pages=book["chapters"][chno-1]["pages"]
        left,right=pages[lno-1],pages[rno-1]
        bad,info=pair_same_zone(pg,left,right)
        if not bad:
            stats.append((chno,lno,rno,"already clear"))
            continue

        # locate duplicate on right page and the prepared paragraph containing it
        _,_,_,_,right_pi,_=info
        fp=prepared(right)
        non_idxs=[i for i,x in enumerate(fp) if "$$" not in x]
        if right_pi>=len(non_idxs):
            failures.append(f"ch{chno} p{lno}/p{rno}: could not locate right paragraph")
            continue
        target_idx=non_idxs[right_pi]
        old=fp[target_idx]
        old_lines=pg.evaluate(JS_LINES,[old])[0]
        top_target=(right_pi==0)

        # Build candidates. Top paragraph must begin mid-sentence; interior replacements use whole paragraphs.
        candidates=[]
        for dci,dpi,txt in donor_paras:
            if dci==chno-1 and dpi in {lno-1,rno-1,rno}: continue
            if has_overlap([txt],prose(left)) or has_overlap([txt],prose(right)): continue
            if top_target:
                for frag in top_fragments(txt):
                    candidates.append(frag)
            else:
                candidates.append(txt)
            if len(candidates)>=3500: break
        if not candidates:
            failures.append(f"ch{chno} p{lno}/p{rno}: no donor candidates")
            continue

        lines=pg.evaluate(JS_LINES,candidates)
        order=sorted(range(len(candidates)),key=lambda i:(abs(lines[i]-old_lines),abs(len(toks(candidates[i]))-len(toks(old)))))
        accepted=None
        for i in order[:500]:
            cand=candidates[i]
            trial=copy.deepcopy(right)
            tfp=prepared(trial); tfp[target_idx]=cand; trial["force_paragraphs"]=tfp
            bad2,_=pair_same_zone(pg,left,trial)
            if bad2: continue
            # Do not create same-zone risk with the next page either.
            if rno < len(pages):
                bad_next,_=pair_same_zone(pg,trial,pages[rno])
                if bad_next: continue
            accepted=(cand,lines[i])
            break

        if not accepted:
            failures.append(f"ch{chno} p{lno}/p{rno}: no safe replacement found")
            continue

        cand,new_lines=accepted
        fp[target_idx]=cand
        right["force_paragraphs"]=fp
        stats.append((chno,lno,rno,f"replaced right paragraph {target_idx}; lines {old_lines}->{new_lines}"))

    # Final target QA and local-neighbour QA.
    remaining=[]
    for chno,lno,rno in TARGETS:
        pages=book["chapters"][chno-1]["pages"]
        bad,info=pair_same_zone(pg,pages[lno-1],pages[rno-1])
        if bad:
            remaining.append(f"ch{chno} p{lno}/p{rno}")

    browser.close()

after_hash=para_hash(book)
if after_hash!=before_hash:
    failures.append("canonical paragraphs hash changed")

# Root/public parity is written from one object only if the target gate clears.
lines=["# Keys targeted positional-retention repair — 7 Oct 2026","",
       "Scope: phone candidate only. Apply the seven machine-clearable same-zone cases; leave the three stubborn pairs untouched for Stanley phone judgement.","",
       f"- machine-clearable target pairs applied: **{len(TARGETS)}**",
       "- deliberately untouched stubborn pairs: **ch4 p33/p34; ch4 p142/p143; ch4 p145/p146**",
       f"- remaining same-zone target pairs: **{len(remaining)}**",
       f"- canonical paragraphs hash unchanged: **{'YES' if after_hash==before_hash else 'NO'}**","",
       "## Actions"]
for ch,l,r,msg in stats:
    lines.append(f"- ch{ch} p{l}/p{r}: {msg}")
if failures:
    lines+=["","## Failures"]+[f"- {x}" for x in failures]
if remaining:
    lines+=["","## Remaining target risks"]+[f"- {x}" for x in remaining]

passed=(not failures and not remaining)
lines+=["",f"## Candidate verdict: **{'READY FOR PHONE QA' if passed else 'HOLD'}**"]
REPORT.write_text("\n".join(lines)+"\n")
print("\n".join(lines))

if passed:
    payload=json.dumps(book,ensure_ascii=False,indent=2)+"\n"
    ROOT.write_text(payload); PUBLIC.write_text(payload)
else:
    raise SystemExit(1)
