#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from playwright.sync_api import sync_playwright

DEFAULT_CSS = """
*{box-sizing:border-box}
html,body{margin:0;background:#fff;color:#171717;font-family:Georgia,"Times New Roman",serif}
.page{width:100%;height:100%;padding:34px 30px 54px;overflow:hidden;background:#fff}
.page p{font-size:17px;line-height:1.48;text-align:left;margin:0 0 .75em;text-indent:1.5em}
.page p:first-of-type{text-indent:0}
.page p+p{text-indent:1.5em}
"""

JS_MEASURE = r"""
() => {
  const page = document.querySelector('.page') || document.body;
  const paras = [...page.querySelectorAll('p')];
  const lines = [];
  let globalLine = 0;
  for (let pi=0; pi<paras.length; pi++) {
    const p = paras[pi];
    const text = p.textContent || '';
    const words = [...text.matchAll(/\S+/g)];
    const buckets = [];
    for (const m of words) {
      const range = document.createRange();
      const node = p.firstChild;
      if (!node || node.nodeType !== Node.TEXT_NODE) continue;
      range.setStart(node, m.index);
      range.setEnd(node, m.index + m[0].length);
      const rect = range.getBoundingClientRect();
      let b = buckets.find(x => Math.abs(x.top - rect.top) < 0.8);
      if (!b) {
        b = {top:rect.top,bottom:rect.bottom,left:rect.left,right:rect.right,words:[]};
        buckets.push(b);
      }
      b.words.push({text:m[0],left:rect.left,right:rect.right});
      b.left = Math.min(b.left, rect.left);
      b.right = Math.max(b.right, rect.right);
      b.bottom = Math.max(b.bottom, rect.bottom);
    }
    buckets.sort((a,b)=>a.top-b.top);
    for (let li=0; li<buckets.length; li++) {
      globalLine++;
      const b=buckets[li];
      lines.push({
        line:globalLine, paragraph:pi+1, line_in_paragraph:li+1,
        text:b.words.map(w=>w.text).join(' '),
        top:b.top,bottom:b.bottom,left:b.left,right:b.right
      });
    }
  }
  const marker = '$$$';
  let markerInfo = null;
  for (let pi=0; pi<paras.length; pi++) {
    const p=paras[pi], node=p.firstChild;
    if (!node || node.nodeType !== Node.TEXT_NODE) continue;
    const i=node.data.indexOf(marker);
    if (i>=0) {
      const r=document.createRange();
      r.setStart(node,i); r.setEnd(node,i+marker.length);
      const x=r.getBoundingClientRect();
      const line=lines.find(L => Math.abs(L.top-x.top)<0.8 && L.paragraph===pi+1);
      markerInfo={
        paragraph:pi+1,
        line:line?line.line:null,
        line_in_paragraph:line?line.line_in_paragraph:null,
        top:x.top,bottom:x.bottom,left:x.left,right:x.right
      };
      break;
    }
  }
  const pr=page.getBoundingClientRect();
  return {
    viewport:{width:innerWidth,height:innerHeight,devicePixelRatio},
    page:{left:pr.left,top:pr.top,width:pr.width,height:pr.height},
    lines,marker:markerInfo
  };
}
"""

def html_for(cfg):
    paras = cfg.get('paragraphs', [])
    body = ''.join(
        '<p>'+p.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')+'</p>'
        for p in paras
    )
    css = DEFAULT_CSS + '\n' + cfg.get('css','')
    return (
        '<!doctype html><html><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">'
        f'<style>{css}</style></head><body><main class="page">{body}</main></body></html>'
    )

def main():
    ap=argparse.ArgumentParser(description='Render a fixed-layout reader page and report exact browser line boxes.')
    ap.add_argument('input', help='JSON input file')
    ap.add_argument('--out', default='render-out', help='output directory')
    ap.add_argument('--engine', choices=['chromium','webkit','firefox'], default='chromium')
    ap.add_argument('--executable', help='browser executable path when Playwright bundle is absent')
    args=ap.parse_args()

    cfg=json.loads(Path(args.input).read_text())
    vp=cfg.get('viewport', {'width':414,'height':736})
    out=Path(args.out)
    out.mkdir(parents=True,exist_ok=True)

    html=html_for(cfg)
    (out/'page.html').write_text(html)

    with sync_playwright() as p:
        bt=getattr(p,args.engine)
        kw={'headless':True}
        if args.executable:
            kw['executable_path']=args.executable
        browser=bt.launch(**kw)
        page=browser.new_page(
            viewport={'width':int(vp['width']),'height':int(vp['height'])},
            device_scale_factor=float(vp.get('device_scale_factor',1))
        )
        page.set_content(html, wait_until='load')
        page.screenshot(path=str(out/'page.png'), full_page=False)
        metrics=page.evaluate(JS_MEASURE)

        expected=cfg.get('expected_lines') or []
        actual=[x['text'] for x in metrics.get('lines',[])]
        mismatches=[]
        for i,e in enumerate(expected):
            a=actual[i] if i < len(actual) else None
            if a != e:
                mismatches.append({'line':i+1,'expected':e,'actual':a})
        metrics['calibration']={
            'expected_count':len(expected),
            'matched':len(expected)-len(mismatches),
            'exact':bool(expected) and not mismatches,
            'mismatches':mismatches
        }

        (out/'metrics.json').write_text(json.dumps(metrics,indent=2,ensure_ascii=False))
        browser.close()

    print(json.dumps({
        'screenshot':str(out/'page.png'),
        'metrics':str(out/'metrics.json'),
        'marker':metrics.get('marker'),
        'line_count':len(metrics.get('lines',[])),
        'calibration':metrics.get('calibration')
    },ensure_ascii=False))

if __name__=='__main__':
    main()
