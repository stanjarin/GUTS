#!/usr/bin/env python3
import copy, html, importlib.util, json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
ENGINE_PATH = ROOT / "tools" / "line_pump_boundary_repair.py"
OUT = ROOT / "public" / "project_library" / "books" / "browse" / "boundary-law-live-sample.html"

spec = importlib.util.spec_from_file_location("boundary_engine", ENGINE_PATH)
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)

TARGETS = [
    ("Peake Ch2 p2", ROOT / "PERFORMANCE10" / "peake_performance.json", 1, 1, 8),
    ("Peake Ch2 p3", ROOT / "PERFORMANCE10" / "peake_performance.json", 1, 2, 12),
    ("Ulysses Ithaca p11", ROOT / "PERFORMANCE35" / "jj_035.json", 16, 10, 14),
    ("Ulysses Ithaca p12", ROOT / "PERFORMANCE35" / "jj_035.json", 16, 11, 8),
    ("Ulysses Ithaca p13", ROOT / "PERFORMANCE35" / "jj_035.json", 16, 12, 12),
]

def fresh_stats():
    return {k:0 for k in [
        "forceable_pages","pages_changed","exact_hits","within1","within2","beyond2",
        "spacing_violations","retention_windows","unresolved_pages","chapters_skipped",
        "token_mismatches","genuine_hash_mismatches","mid_sentence_failures",
        "airlock_left_terminal_failures","line_abs_error"
    ]}

def load_repaired(path, page):
    book = json.loads(path.read_text())
    failures = []
    stats = fresh_stats()
    repaired = engine.repair_book(copy.deepcopy(book), page, stats, failures)
    return repaired, stats, failures

def sample_page(book, ci, pi):
    p = book["chapters"][ci]["pages"][pi]
    fp = list(p.get("force_paragraphs") or [])
    if sum("$$$" in str(x) for x in fp) != 1:
        raise RuntimeError(f"sample ch{ci+1} p{pi+1}: expected exactly one $$$")
    return fp

def make_html(samples):
    payload = json.dumps(samples, ensure_ascii=False)
    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>GUTS boundary-law live repair sample</title>
<style>
*{{box-sizing:border-box}}
html,body{{margin:0;background:#fbf8ef;color:#29261f;font-family:Georgia,serif}}
.top{{position:sticky;top:0;z-index:5;background:#f3efe4;border-bottom:1px solid #b8ae99;padding:9px 12px;font:13px -apple-system,BlinkMacSystemFont,sans-serif}}
.status{{padding:10px 15px 8px;font:13px/1.35 -apple-system,BlinkMacSystemFont,sans-serif}}
.results{{display:flex;gap:6px;padding:0 15px 10px;flex-wrap:wrap}}
.chip{{border:1px solid #b8ae99;border-radius:7px;padding:6px 8px;background:#fffdf7;font:12px/1.2 -apple-system,BlinkMacSystemFont,sans-serif}}
.controls{{display:flex;gap:7px;padding:0 15px 10px;flex-wrap:wrap}}
button{{font:13px -apple-system,BlinkMacSystemFont,sans-serif;padding:8px 11px;border:1px solid #9c927d;border-radius:7px;background:#fffdf7;color:#29261f}}
.page{{width:100%;padding:25px 15px 58px;font:15px/1.45 Georgia,serif;color:#29261f;background:#fbf8ef}}
.page p{{width:329px;max-width:100%;margin:0 auto .72em}}
.page p:first-child{{margin-top:2px}}
.page p+p{{text-indent:1.5em}}
.detail{{padding:0 15px 20px;font:12px/1.4 -apple-system,BlinkMacSystemFont,sans-serif;color:#5f594d}}
</style>
</head>
<body>
<div class="top">GUTS · LIVE boundary-law output · branch-only</div>
<div class="status" id="status">These five pages are extracted after the repair engine runs in memory. No copied fixture prose.</div>
<div class="results" id="results"></div>
<div class="controls" id="controls"></div>
<div class="page" id="page"></div>
<div class="detail" id="detail"></div>
<script>
const SAMPLES={payload};
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function lineRows(el){{
  const ps=[...el.querySelectorAll('p')], rows=[]; let global=0;
  ps.forEach((p,pi)=>{{
    const n=p.firstChild;if(!n)return;
    const tops=[];
    for(let i=0;i<n.data.length;i++){{
      if(/\s/.test(n.data[i]))continue;
      const r=document.createRange();r.setStart(n,i);r.setEnd(n,i+1);
      const top=r.getBoundingClientRect().top;
      if(!tops.some(t=>Math.abs(t-top)<0.75))tops.push(top);
    }}
    tops.sort((a,b)=>a-b).forEach((top,li)=>rows.push({{line:++global,para:pi+1,paraLine:li+1,top}}));
  }});
  return rows;
}}
function measure(s){{
  const box=document.createElement('div'); box.className='page'; box.style.position='fixed'; box.style.left='-10000px';
  box.innerHTML=s.paras.map(x=>'<p>'+esc(x)+'</p>').join('');
  document.body.appendChild(box);
  const rows=lineRows(box);
  const ai=s.paras.findIndex(x=>x.includes('$$$'))+1;
  const first=rows.find(x=>x.para===ai&&x.paraLine===1);
  box.remove();
  return first?first.line:null;
}}
const actual=SAMPLES.map(measure);
function show(i){{
  const s=SAMPLES[i];
  document.getElementById('page').innerHTML=s.paras.map(x=>'<p>'+esc(x)+'</p>').join('');
  document.getElementById('detail').textContent=s.label+' · target '+s.target+' · Safari airlock line '+actual[i]+' · generated directly from repaired in-memory page';
  scrollTo(0,0);
}}
document.getElementById('results').innerHTML=SAMPLES.map((s,i)=>'<div class="chip">'+s.label+'<br>'+s.target+' → <b>'+actual[i]+'</b></div>').join('');
document.getElementById('controls').innerHTML=SAMPLES.map((s,i)=>'<button onclick="show('+i+')">'+(i+1)+'</button>').join('');
show(0);
</script>
</body>
</html>"""

def main():
    needed = {}
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width":414,"height":736}, device_scale_factor=1)
        page.set_content(f"<!doctype html><style>{engine.CSS}</style><div class='page'></div>")
        for _, path, _, _, _ in TARGETS:
            if path not in needed:
                repaired, stats, failures = load_repaired(path, page)
                needed[path] = repaired
                print(f"{path.name}: forceable={stats['forceable_pages']} unresolved={stats['unresolved_pages']} failures={len(failures)}")
        browser.close()

    samples=[]
    for label,path,ci,pi,target in TARGETS:
        paras=sample_page(needed[path],ci,pi)
        samples.append({"label":label,"target":target,"paras":paras})
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(make_html(samples))
    print(f"WROTE {OUT}")

if __name__ == "__main__":
    main()
