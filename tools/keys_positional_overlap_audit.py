#!/usr/bin/env python3
import json,re
from pathlib import Path
from playwright.sync_api import sync_playwright

BOOK=Path("PERFORMANCE10/keys_performance.json")
REPORT=Path("docs/checkpoints/2026-10-07_keys-positional-overlap-audit.md")
N=10
SAME_ZONE_PX=96
TOP_ZONE_MAX=180
BOTTOM_ZONE_MIN=500

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
                # report the first occurrence pair with the smallest positional difference,
                # plus whether any occurrence is genuinely same-zone.
                best=None; dangerous=False; bottom_top=False
                for ia,ib,g in hits:
                    ya=posa.get(ia); yb=posb.get(ib)
                    if ya is None or yb is None: continue
                    d=abs(ya-yb)
                    same=d<=SAME_ZONE_PX
                    bt=(ya>=BOTTOM_ZONE_MIN and yb<=TOP_ZONE_MAX)
                    if same: dangerous=True
                    if bt: bottom_top=True
                    cand=(d,ia,ib,ya,yb," ".join(g))
                    if best is None or cand[0]<best[0]: best=cand
                if best is None: continue
                d,ia,ib,ya,yb,phrase=best
                rows.append({
                    "chapter":ci,"left":pi+1,"right":pi+2,
                    "left_y":round(ya,1),"right_y":round(yb,1),"delta":round(d,1),
                    "dangerous":dangerous,"bottom_top":bottom_top,"phrase":phrase
                })
        browser.close()

    danger=[r for r in rows if r["dangerous"]]
    benign=[r for r in rows if not r["dangerous"]]
    bt=[r for r in rows if r["bottom_top"]]
    lines=[
      "# Keys positional overlap audit — 7 Oct 2026","",
      "Read-only audit. No prose or corpus files changed.","",
      f"- adjacent page pairs with a repeated {N}-word run anywhere: **{len(rows)}**",
      f"- same-zone positional overlaps (≤ {SAME_ZONE_PX}px): **{len(danger)}**",
      f"- non-same-zone textual overlaps: **{len(benign)}**",
      f"- bottom→top overlaps detected (left ≥ {BOTTOM_ZONE_MIN}px, right ≤ {TOP_ZONE_MAX}px): **{len(bt)}**","",
      "Interpretation: only the same-zone count is a retention-risk flag. Bottom→top duplication is expected camouflage and is not itself a failure.","",
      "## Same-zone risks"
    ]
    if danger:
        for r in danger:
            lines.append(f"- ch{r['chapter']} p{r['left']}/p{r['right']} — {r['left_y']}px → {r['right_y']}px (Δ {r['delta']}px) — “{r['phrase']}”")
    else:
        lines.append("- none")
    lines += ["","## Benign positional duplicates"]
    if benign:
        for r in benign:
            tag=" bottom→top" if r["bottom_top"] else ""
            lines.append(f"- ch{r['chapter']} p{r['left']}/p{r['right']} — {r['left_y']}px → {r['right_y']}px (Δ {r['delta']}px){tag}")
    else:
        lines.append("- none")
    REPORT.write_text("\n".join(lines)+"\n")
    print("\n".join(lines))

if __name__=="__main__":
    main()
