#!/usr/bin/env python3
"""Read-only post-assembly stagecraft gate. Never rewrites corpus files."""
import argparse, json, re
from pathlib import Path
from playwright.sync_api import sync_playwright

CSS = """*{box-sizing:border-box}html,body{margin:0;background:#fbf8ef;color:#29261f;font-family:Georgia,serif}.page{width:100%;padding:25px 15px 58px;font:15px/1.45 Georgia,serif;color:#29261f;background:#fbf8ef}.page p{width:329px;max-width:100%;margin:0 auto .72em}.page p:first-child{margin-top:2px}.page p+p{text-indent:1.5em}"""
JS = """({paras,ai})=>{const e=document.querySelector('.page');e.replaceChildren();let arr=[];for(const s of paras){let p=document.createElement('p');p.textContent=s;e.appendChild(p);let r=document.createRange();r.selectNodeContents(p);let rects=[...r.getClientRects()].filter(x=>x.width>0&&x.height>0);let tops=[];for(const x of rects)if(!tops.some(y=>Math.abs(y-x.top)<.75))tops.push(x.top);arr.push({top:tops[0]??null,bottom:rects.length?rects.at(-1).bottom:null,lines:tops.length})}return {airTop:arr[ai]?.top??null,bottom:arr.filter(x=>x.bottom!==null).at(-1)?.bottom??null,precedingLines:arr.slice(0,ai).reduce((s,x)=>s+x.lines,0)}}"""
def inspect(paths,upper=330,short=600):
    out=[]; line_height=15*1.45
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        page=browser.new_page(viewport={"width":390,"height":844})
        page.set_content('<html><head><style>'+CSS+'</style></head><body><div class="page"></div></body></html>')
        for path in paths:
            book=json.loads(Path(path).read_text())
            title=book.get("title") or book.get("id") or Path(path).stem
            for ci,ch in enumerate(book.get("chapters",[]),1):
                prev=None
                for pi,p in enumerate(ch.get("pages",[]),1):
                    f=p.get("force_paragraphs") or []
                    air=[i for i,s in enumerate(f) if "$$$" in str(s)]
                    if not air: prev=None; continue
                    row={"book":title,"chapter":ci,"page":pi,"source":str(path),"airlockCount":len(air)}
                    if len(air)!=1:row["severity"]="FATAL";row["issue"]="socket count";out.append(row);prev=None;continue
                    ai=air[0]
                    m=page.evaluate(JS,{"paras":f,"ai":ai})
                    row.update({"airlockIndex":ai,"airTop":m["airTop"],"bottom":m["bottom"],"precedingLines":m["precedingLines"],"firstNewParaFail":ai!=1,"shortCandidate":m["bottom"] is not None and m["bottom"]<short})
                    if prev is not None and m["airTop"] is not None and prev["airTop"] is not None:
                        d=(m["airTop"]-prev["airTop"])/line_height
                        row["deltaRenderedLines"]=round(d,2)
                        row["upperStaggerFlag"]=abs(d)<4 and m["airTop"]<=upper and prev["airTop"]<=upper
                    else:row["upperStaggerFlag"]=False
                    # OCR triage only: these patterns are not proof of bad OCR.
                    joined=" ".join(str(s) for s in f)
                    row["ocrSuspect"]=bool(re.search(r"(?:�|\\uFFFD|[!?.,;:]{4,}|[A-Za-z]-\\s+[a-z])",joined))
                    if row["firstNewParaFail"] or row["upperStaggerFlag"] or row["shortCandidate"] or row["ocrSuspect"]:out.append(row)
                    prev={"airTop":m["airTop"]}
        browser.close()
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("corpora",nargs="+",type=Path)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--strict",action="store_true",help="Exit nonzero for structural first-new-paragraph or socket failures")
    args=ap.parse_args()
    entries=inspect(args.corpora)
    stats={"books":len(args.corpora),"firstNewParaFailures":sum(x.get("firstNewParaFail",False) for x in entries),
           "upperStaggerFlags":sum(x.get("upperStaggerFlag",False) for x in entries),
           "shortCandidates":sum(x.get("shortCandidate",False) for x in entries),
           "ocrSuspects":sum(x.get("ocrSuspect",False) for x in entries),
           "socketFailures":sum(x.get("issue")=="socket count" for x in entries)}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps({"summary":stats,"suspects":entries},ensure_ascii=False,indent=2))
    print(json.dumps(stats))
    if args.strict and (stats["firstNewParaFailures"] or stats["socketFailures"]):raise SystemExit(1)
if __name__=="__main__":main()
