#!/usr/bin/env python3
"""
Rendered-line carry pump controller — diagnostic prototype.

Given a donor run of genuine prose, tries legal sentence-boundary splits.
The suffix becomes the carry at the top of the next prepared page; the
airlock follows it. The browser counts actual rendered lines and the
controller selects the split whose airlock start is nearest the target.

No corpus mutation. Genuine words/order are never changed.
"""
import argparse, json, re
from pathlib import Path
from playwright.sync_api import sync_playwright

DEFAULT_CSS = """
*{box-sizing:border-box}
html,body{margin:0;background:#fbf8ef;color:#29261f;font-family:Georgia,"Times New Roman",serif}
.page{width:100%;height:100%;padding:25px 15px 58px;overflow:hidden;background:#fbf8ef;font:15px/1.45 Georgia,serif;color:#29261f}
.page p{width:329px;max-width:100%;margin:0 auto .72em;text-align:left}
.page p:first-child{margin-top:2px;text-indent:0}
.page p+p{text-indent:1.5em}
"""

JS_LINE_COUNT = r"""() => {
  const paras=[...document.querySelectorAll('.page p')];
  const lines=[]; let global=0;
  for(let pi=0;pi<paras.length;pi++){
    const p=paras[pi], node=p.firstChild;
    if(!node || node.nodeType!==Node.TEXT_NODE) continue;
    const text=node.data, tops=[];
    for(let i=0;i<text.length;i++){
      if(/\s/.test(text[i])) continue;
      const r=document.createRange(); r.setStart(node,i); r.setEnd(node,i+1);
      const top=r.getBoundingClientRect().top;
      if(!tops.some(x=>Math.abs(x-top)<0.8)) tops.push(top);
    }
    tops.sort((a,b)=>a-b);
    for(let li=0;li<tops.length;li++)
      lines.push({line:++global,paragraph:pi+1,line_in_paragraph:li+1,top:tops[li]});
  }
  const ai=paras.findIndex(p=>p.textContent.includes('$$$'));
  const first=ai>=0 ? lines.find(x=>x.paragraph===ai+1 && x.line_in_paragraph===1) : null;
  return {line_count:global,airlock_start_line:first?first.line:null};
}"""

def split_sentences(text):
    parts=re.split(r'(?<=[.!?])\s+(?=[“‘"\'A-Z0-9])', text.strip())
    return [p.strip() for p in parts if p.strip()]

def wc(s):
    return len(re.findall(r"\S+",s))

def html_for(carry,airlock,css):
    esc=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    return (
      '<!doctype html><html><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">'
      f'<style>{css}</style></head><body><main class="page">'
      f'<p>{esc(carry)}</p><p>{esc(airlock)}</p></main></body></html>'
    )

def best_split(page,donor,airlock,target,css,min_head=12,min_carry=12):
    ss=split_sentences(donor)
    candidates=[]
    for cut in range(1,len(ss)):
        head=' '.join(ss[:cut]).strip()
        carry=' '.join(ss[cut:]).strip()
        if wc(head)<min_head or wc(carry)<min_carry:
            continue
        page.set_content(html_for(carry,airlock,css),wait_until='load')
        m=page.evaluate(JS_LINE_COUNT)
        line=m['airlock_start_line']
        if line is None:
            continue
        candidates.append({
          'cut_after_sentence':cut,
          'head_words':wc(head),
          'carry_words':wc(carry),
          'airlock_start_line':line,
          'error':abs(line-target),
          'head':head,
          'carry':carry
        })
    if not candidates:
        return None,[]
    candidates.sort(key=lambda x:(x['error'],abs(x['carry_words']-80),x['cut_after_sentence']))
    return candidates[0],candidates

def main():
    ap=argparse.ArgumentParser(description='Steer a carry split by rendered airlock line.')
    ap.add_argument('input')
    ap.add_argument('--engine',choices=['webkit','chromium','firefox'],default='webkit')
    ap.add_argument('--executable',help='Optional browser executable path.')
    ap.add_argument('--out')
    args=ap.parse_args()

    cfg=json.loads(Path(args.input).read_text())
    css=cfg.get('css',DEFAULT_CSS)
    vp=cfg.get('viewport',{'width':414,'height':736})
    results=[]

    with sync_playwright() as p:
        kw={'headless':True}
        if args.executable:
            kw['executable_path']=args.executable
        browser=getattr(p,args.engine).launch(**kw)
        page=browser.new_page(
          viewport={'width':int(vp['width']),'height':int(vp['height'])},
          device_scale_factor=float(vp.get('device_scale_factor',1))
        )
        for item in cfg['tests']:
            best,cands=best_split(
              page,item['donor'],item['airlock'],int(item['target_line']),css,
              int(item.get('min_head_words',12)),int(item.get('min_carry_words',12))
            )
            results.append({
              'name':item.get('name'),
              'target_line':item['target_line'],
              'best':best,
              'candidate_count':len(cands)
            })
        browser.close()

    out={'engine':args.engine,'viewport':vp,'results':results}
    payload=json.dumps(out,indent=2,ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(payload)
    print(payload)

if __name__=='__main__':
    main()
