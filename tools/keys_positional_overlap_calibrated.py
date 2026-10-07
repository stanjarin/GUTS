#!/usr/bin/env python3
import json,re
from pathlib import Path
from playwright.sync_api import sync_playwright

BOOK=Path("PERFORMANCE10/keys_performance.json")
REPORT=Path("docs/checkpoints/2026-10-07_keys-positional-overlap-calibrated.md")
N=10
SAME_ZONE_PX=96
STRONG_DISPLACEMENT_PX=174

CSS="""
*{box-sizing:border-box}
html,body{margin:0;background:#fbf8ef;color:#29261f;font-family:Georgia,serif}
.page{width:100%;padding:25px 15px 58px;font:15px/1.45 Georgia,serif;color:#29261f;background:#fbf8ef}
.page p{width:329px;max-width:100%;margin:0 auto .72em}
.page p:first-child{margin-top:2px}
.page p+p{text-indent:1.5em}
.w{display:inline}
"""

def words(s): return re.findall(r"\S+",str(s))
def clean(t): return re.sub(r"^\W+|\W+$","",str(t),flags=re.UNICODE).lower()
def paras(p): return [str(x) for x in (p.get("force_paragraphs") or p.get("paragraphs") or []) if "$$" not in str(x)]
def flat(ps):
    out=[]
    for para in ps:
        for tok in words(para):
            c=clean(tok)
            if c: out.append(c)
    return out
def overlaps(a,b,n=N):
    amap={}
    for i in range(max(0,len(a)-n+1)): amap.setdefault(tuple(a[i:i+n]),[]).append(i)
    out=[]
    for j in range(max(0,len(b)-n+1)):
        g=tuple(b[j:j+n])
        for i in amap.get(g,[]): out.append((i,j,g))
    return out

JS=r"""payload=>{
 const page=document.querySelector('.page'); page.innerHTML=''; let g=0; const out=[];
 for(const para of payload.paras){
   const p=document.createElement('p');
   for(const tok of para.trim().split(/\s+/).filter(Boolean)){
     const s=document.createElement('span'); s.className='w'; s.textContent=tok; s.dataset.g=String(g++);
     p.appendChild(s); p.appendChild(document.createTextNode(' '));
   }
   page.appendChild(p);
 }
 for(const s of page.querySelectorAll('.w')){
   const r=s.getBoundingClientRect(); out.push({i:Number(s.dataset.g),top:r.top});
 }
 return out;
}"""

def pos(pg,ps): return {x["i"]:x["top"] for x in pg.evaluate(JS,{"paras":ps})}

book=json.loads(BOOK.read_text())
rows=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    pg=browser.new_page(viewport={"width":414,"height":736},device_scale_factor=1)
    pg.set_content(f"<!doctype html><style>{CSS}</style><div class='page'></div>")
    for ci,ch in enumerate(book.get("chapters",[]),1):
        pages=ch.get("pages",[])
        for pi in range(len(pages)-1):
            pa,pb=paras(pages[pi]),paras(pages[pi+1])
            hits=overlaps(flat(pa),flat(pb))
            if not hits: continue
            posa,posb=pos(pg,pa),pos(pg,pb)
            vals=[]
            for ia,ib,g in hits:
                if ia in posa and ib in posb:
                    ya,yb=posa[ia],posb[ib]
                    vals.append((abs(ya-yb),ya-yb,ya,yb," ".join(g)))
            if not vals: continue
            vals.sort(key=lambda x:x[0])
            mind,dir_delta,ya,yb,phrase=vals[0]
            same=any(v[0]<=SAME_ZONE_PX for v in vals)
            strong=all(v[0]>=STRONG_DISPLACEMENT_PX for v in vals)
            downup=any(v[1]>=STRONG_DISPLACEMENT_PX for v in vals)
            rows.append(dict(ch=ci,left=pi+1,right=pi+2,left_y=round(ya,1),right_y=round(yb,1),
                             delta=round(mind,1),same=same,strong=strong,downup=downup,phrase=phrase))
    browser.close()

same=[r for r in rows if r["same"]]
strong=[r for r in rows if r["strong"]]
review=[r for r in rows if not r["same"] and not r["strong"]]
downup=[r for r in rows if r["downup"]]

lines=[
"# Keys positional overlap audit — calibrated 7 Oct 2026","",
"Read-only. No prose or corpus changed.","",
f"- repeated adjacent page pairs: **{len(rows)}**",
f"- same-zone risk pairs (nearest repeat <= {SAME_ZONE_PX}px): **{len(same)}**",
f"- strongly displaced camouflage pairs (all repeats >= {STRONG_DISPLACEMENT_PX}px): **{len(strong)}**",
f"- intermediate / phone-review pairs: **{len(review)}**",
f"- pairs containing strong down-to-up displacement: **{len(downup)}**","",
"Machine meaning: same-zone is suspicious; strong displacement is camouflage; intermediate is for phone judgement.","",
"## Same-zone risks"
]
for r in same:
    lines.append(f"- ch{r['ch']} p{r['left']}/p{r['right']} — {r['left_y']}px to {r['right_y']}px (delta {r['delta']}px) — {r['phrase']}")
if not same: lines.append("- none")
lines+=["","## Strong displacement / camouflage"]
for r in strong:
    tag=" down-to-up" if r["downup"] else ""
    lines.append(f"- ch{r['ch']} p{r['left']}/p{r['right']} — nearest delta {r['delta']}px{tag}")
if not strong: lines.append("- none")
lines+=["","## Intermediate — phone review"]
for r in review:
    lines.append(f"- ch{r['ch']} p{r['left']}/p{r['right']} — nearest delta {r['delta']}px")
if not review: lines.append("- none")
REPORT.write_text("\n".join(lines)+"\n")
print("\n".join(lines))
