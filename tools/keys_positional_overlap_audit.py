#!/usr/bin/env python3
import json,re
from pathlib import Path
from playwright.sync_api import sync_playwright

BOOK=Path("PERFORMANCE10/keys_performance.json")
REPORT=Path("docs/checkpoints/2026-10-07_keys-positional-overlap-audit.md")
N=10
SAME_ZONE_PX=96
STRONG_DISPLACEMENT_PX=174  # about eight rendered lines at 21.75px

CSS="""
*{box-sizing:border-box}
html,body{margin:0;background:#fbf8ef;color:#29261f;font-family:Georgia,serif}
.page{width:100%;padding:25px 15px 58px;font:15px/1.45 Georgia,serif;color:#29261f;background:#fbf8ef}
.page p{width:329px;max-width:100%;margin:0 auto .72em}
.page p:first-child{margin-top:2px}
.page p+p{text-indent:1.5em}
.w{display:inline}
"""

def raw_words(s):
    return re.findall(r"\S+",str(s))

def clean_tok(t):
    return re.sub(r"^\W+|\W+$","",str(t),flags=re.UNICODE).lower()

def page_paras(p):
    return [str(x) for x in (p.get("force_paragraphs") or p.get("paragraphs") or []) if "$$" not in str(x)]

def flat_clean(paras):
    out=[]
    for para in paras:
        for tok in raw_words(para):
            c=clean_tok(tok)
            if c: out.append(c)
    return out

def overlap_hits(a,b,n=N):
    if len(a)<n or len(b)<n: return []
    amap={}
    for i in range(len(a)-n+1):
        amap.setdefault(tuple(a[i:i+n]),[]).append(i)
    hits=[]
    seen=set()
    for j in range(len(b)-n+1):
        g=tuple(b[j:j+n])
        if g in amap:
            for i in amap[g]:
                key=(i,j,g)
                if key not in seen:
                    seen.add(key); hits.append((i,j,g))
    return hits

JS_RENDER=r"""payload=>{
 const page=document.querySelector('.page'); page.innerHTML='';
 let g=0; const positions=[];
 for(const para of payload.paras){
   const p=document.createElement('p');
   const toks=para.trim().split(/\s+/).filter(Boolean);
   toks.forEach((tok,i)=>{
     const span=document.createElement('span'); span.className='w'; span.textContent=tok; span.dataset.g=String(g++);
     p.appendChild(span);
     if(i<toks.length-1) p.appendChild(document.createTextNode(' '));
   });
   page.appendChild(p);
 }
 for(const s of page.querySelectorAll('.w')){
   const r=s.getBoundingClientRect();
   positions.push({i:Number(s.dataset.g),top:r.top,bottom:r.bottom});
 }
 return positions;
}"""

def pos_map(pg,paras):
    arr=pg.evaluate(JS_RENDER,{"paras":paras})
    return {x["i"]:x["top"] for x in arr}

def main():
    book=json.loads(BOOK.read_text())
    rows=[]
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        pg=browser.new_page(viewport={"width":414,"height":736},device_scale_factor=1)
        pg.set_content(f"<!doctype html><style>{CSS}</style><div class='page'></div>")
        for ci,ch in enumerate(book.get("chapters",[]),1):
            pages=ch.get("pages",[])
            for pi in range(len(pages)-1):
                pa=page_paras(pages[pi]); pb=page_paras(pages[pi+1])
                ca=flat_clean(pa); cb=flat_clean(pb)
                hits=overlap_hits(ca,cb)
                if not hits: continue
                posa=pos_map(pg,pa); posb=pos_map(pg,pb)
                occ=[]
                for ia,ib,g in hits:
                    ya=posa.get(ia); yb=posb.get(ib)
                    if ya is None or yb is None: continue
                    occ.append((abs(ya-yb),ya-yb,ya,yb," ".join(g)))
                if not occ: continue
                occ.sort(key=lambda x:x[0])
                mind,dir_delta,ya,yb,phrase=occ[0]
                same=any(x[0]<=SAME_ZONE_PX for x in occ)
                strong=all(x[0]>=STRONG_DISPLACEMENT_PX for x in occ)
                down_up=any(x[1]>=STRONG_DISPLACEMENT_PX for x in occ)
                up_down=any(x[1]<=-STRONG_DISPLACEMENT_PX for x in occ)
                rows.append({
                    "chapter":ci,"left":pi+1,"right":pi+2,
                    "left_y":round(ya,1),"right_y":round(yb,1),"delta":round(mind,1),
                    "same_zone":same,"strong_displacement":strong,
                    "down_up":down_up,"up_down":up_down,"phrase":phrase
                })
        browser.close()

    same=[r for r in rows if r["same_zone"]]
    strong=[r for r in rows if r["strong_displacement"]]
    review=[r for r in rows if not r["same_zone"] and not r["strong_displacement"]]
    downup=[r for r in rows if r["down_up"]]
    lines=[
      "# Keys positional overlap audit — calibrated 7 Oct 2026","",
      "Read-only audit. No prose or corpus files changed.","",
      f"- adjacent page pairs with a repeated {N}-word run anywhere: **{len(rows)}**",
      f"- same-zone risk pairs (nearest repeat ≤ {SAME_ZONE_PX}px): **{len(same)}**",
      f"- strongly displaced pairs (all repeats ≥ {STRONG_DISPLACEMENT_PX}px): **{len(strong)}**",
      f"- intermediate / phone-review pairs: **{len(review)}**",
      f"- pairs containing a strong down→up displacement: **{len(downup)}**","",
      "Interpretation: textual duplication alone is not a failure. Same-zone recurrence is the machine risk signal; strong displacement is camouflage. The middle band is deliberately left for phone judgement.","",
      "## Same-zone risks"
    ]
    if same:
        for r in same:
            lines.append(f"- ch{r['chapter']} p{r['left']}/p{r['right']} — {r['left_y']}px → {r['right_y']}px (Δ {r['delta']}px) — “{r['phrase']}”")
    else:
        lines.append("- none")
    lines += ["","## Strongly displaced / camouflage"]
    if strong:
        for r in strong:
            tag=" down→up" if r["down_up"] else (" up→down" if r["up_down"] else "")
            lines.append(f"- ch{r['chapter']} p{r['left']}/p{r['right']} — nearest Δ {r['delta']}px{tag}")
    else:
        lines.append("- none")
    lines += ["","## Intermediate — phone review"]
    if review:
        for r in review:
            lines.append(f"- ch{r['chapter']} p{r['left']}/p{r['right']} — nearest Δ {r['delta']}px")
    else:
        lines.append("- none")
    REPORT.write_text("\n".join(lines)+"\n")
    print("\n".join(lines))

if __name__=="__main__":
    main()
