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
CORPORA=[
"PERFORMANCE35/aam_035.json","PERFORMANCE35/jeeves_035.json","PERFORMANCE35/farewell_035.json",
"PERFORMANCE35/huck_035.json","PERFORMANCE35/dr_035.json","PERFORMANCE35/ac_035.json",
"PERFORMANCE35/jj_035.json","PERFORMANCE35/jt_035.json",
"PERFORMANCE10/brodie_performance.json","PERFORMANCE10/chandler_performance.json",
"PERFORMANCE10/keys_performance.json","PERFORMANCE10/kontiki_performance.json",
"PERFORMANCE10/parker_performance.json","PERFORMANCE10/peake_performance.json",
"PERFORMANCE10/perelman_performance.json","PERFORMANCE10/policeman_performance.json",
"PERFORMANCE10/ripley_performance.json","PERFORMANCE10/ubu_performance.json"]

JS_MEASURE=r"""carry => {
  const p=document.querySelector('.page');
  p.innerHTML='';
  const a=document.createElement('p'); a.textContent=carry; p.appendChild(a);
  const b=document.createElement('p'); b.textContent='Then $$$ came to him.'; p.appendChild(b);
  const ps=[...p.querySelectorAll('p')]; let global=0;
  for(let pi=0;pi<ps.length;pi++){
    const n=ps[pi].firstChild;if(!n)continue;
    const tops=[];
    for(let i=0;i<n.data.length;i++){
      if(/\s/.test(n.data[i]))continue;
      const r=document.createRange();r.setStart(n,i);r.setEnd(n,i+1);
      const top=r.getBoundingClientRect().top;
      if(!tops.some(x=>Math.abs(x-top)<0.75)) tops.push(top);
    }
    tops.sort((x,y)=>x-y);
    for(let li=0;li<tops.length;li++){
      global++;
      if(pi===1&&li===0) return global;
    }
  }
  return null;
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

def candidate_splits(genuine, measure, target, prev_line, history):
    cands=[]
    max_tail=min(5,len(genuine))
    for k in range(1,max_tail+1):
        donor=" ".join(genuine[-k:]).strip()
        ss=split_sentences(donor)
        if len(ss)<2: continue
        prefix_paras=genuine[:-k]
        prefix_words=sum(wc(x) for x in prefix_paras)
        for cut in range(1,len(ss)):
            head=" ".join(ss[:cut]).strip()
            carry=" ".join(ss[cut:]).strip()
            if wc(head)<12 or wc(carry)<12: continue
            if wc(carry)>180: continue
            remain=prefix_words+wc(head)
            if remain<120: continue
            line=measure(carry)
            if line is None: continue
            spacing_bad = prev_line is not None and abs(line-prev_line)<4
            window_bad=False
            if len(history)>=2:
                vals=[history[-2],history[-1],line]
                if max(vals)-min(vals)<=4: window_bad=True
            score=(200 if window_bad else 0)+(80 if spacing_bad else 0)+abs(line-target)*10+abs(wc(carry)-80)/20+k*.05
            cands.append((score,k,head,carry,line,spacing_bad,window_bad))
    cands.sort(key=lambda x:x[0])
    return cands

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

def repair_book(book,page,stats,failures):
    before_hash=para_hash(book)
    before_stream=[]
    after_stream=[]
    for ci,ch in enumerate(book.get("chapters",[])):
        pages=ch.get("pages",[])
        if not pages: continue
        prepared=[]
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
            before_stream += norm_tokens(e["genuine"])
        if not chapter_ok:
            stats["chapters_skipped"]+=1
            continue

        lines=[]
        unresolved=[]
        for pi in range(1,len(prepared)):
            target=TARGETS[(pi-1)%len(TARGETS)]
            prev=prepared[pi-1]
            cur=prepared[pi]
            cands=candidate_splits(prev["genuine"],lambda s:page.evaluate(JS_MEASURE,s),target,lines[-1] if lines else None,lines)
            if not cands:
                unresolved.append(pi)
                stats["unresolved_pages"]+=1
                continue
            _,k,head,carry,line,spacing_bad,window_bad=cands[0]
            prev["genuine"]=prev["genuine"][:-k]+[head]
            cur["genuine"]=[carry]+cur["genuine"]
            lines.append(line)
            stats["forceable_pages"]+=1
            stats["line_abs_error"]+=abs(line-target)
            if line==target: stats["exact_hits"]+=1
            elif abs(line-target)==1: stats["within1"]+=1
            elif abs(line-target)==2: stats["within2"]+=1
            else: stats["beyond2"]+=1
            if spacing_bad: stats["spacing_violations"]+=1
            if window_bad: stats["retention_windows"]+=1

        for pi,p in enumerate(pages):
            forceable=(pi>0 and pi not in unresolved)
            newp=rebuild_page(p,prepared[pi]["genuine"],prepared[pi]["air"],forceable)
            if newp.get("force_paragraphs")!=p.get("force_paragraphs"):
                stats["pages_changed"]+=1
            pages[pi]=newp
            after_stream += norm_tokens([x for x in newp.get("force_paragraphs",[]) if "$$$" not in str(x)])

    if before_stream!=after_stream:
        failures.append(f"{book.get('id','?')}: chapter-stream token order mismatch after repair")
        stats["token_mismatches"]+=1
    if para_hash(book)!=before_hash:
        failures.append(f"{book.get('id','?')}: genuine paragraphs changed")
        stats["genuine_hash_mismatches"]+=1
    return book

def process_copy(path,page,write,allstats,failures):
    book=json.loads(path.read_text())
    stats={k:0 for k in ["forceable_pages","pages_changed","exact_hits","within1","within2","beyond2",
                         "spacing_violations","retention_windows","unresolved_pages","chapters_skipped",
                         "token_mismatches","genuine_hash_mismatches","line_abs_error"]}
    repaired=repair_book(book,page,stats,failures)
    if write: path.write_text(json.dumps(repaired,ensure_ascii=False,separators=(",",":")))
    for k,v in stats.items(): allstats[k]+=v
    return stats

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--write",action="store_true")
    ap.add_argument("--report",default="docs/checkpoints/2026-10-05_line-pump-corpus-repair.md")
    args=ap.parse_args()
    roots=[]
    for prefix in [Path("public"),Path(".")]:
        found=[prefix/x for x in CORPORA if (prefix/x).exists()]
        if found: roots.append((prefix,found))
    failures=[]
    totals={k:0 for k in ["forceable_pages","pages_changed","exact_hits","within1","within2","beyond2",
                         "spacing_violations","retention_windows","unresolved_pages","chapters_skipped",
                         "token_mismatches","genuine_hash_mismatches","line_abs_error"]}
    per=[]
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        pg=browser.new_page(viewport={"width":414,"height":736},device_scale_factor=1)
        pg.set_content(f"<!doctype html><style>{CSS}</style><div class='page'></div>")
        for prefix,files in roots:
            for path in files:
                st=process_copy(path,pg,args.write,totals,failures)
                per.append((str(path),st))
        browser.close()

    # parity check for root/public copies where both exist
    parity=[]
    for rel in CORPORA:
        a=Path(rel); b=Path("public")/rel
        if a.exists() and b.exists():
            same=a.read_bytes()==b.read_bytes()
            parity.append((rel,same))
            if not same: failures.append(f"{rel}: root/public parity FAIL")

    passed=not failures and totals["unresolved_pages"]==0 and totals["spacing_violations"]==0 and totals["retention_windows"]==0
    avg=(totals["line_abs_error"]/totals["forceable_pages"]) if totals["forceable_pages"] else 0
    lines=[
      "# Rendered-line corpus pump repair — 5 Oct 2026","",
      "**Branch-only automation. Production main untouched.**","",
      "Law: every forceable prepared page begins with carry-over from the previous page; socket-start targets cycle **8 / 12 / 16 / 10 / 14**; genuine words/order are invariant; prepared paragraph boundaries are flexible.","",
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
      f"- root/public corpus parity failures: **{sum(1 for _,ok in parity if not ok)}**","",
      f"## Machine verdict: **{'PASS' if passed else 'HOLD'}**",""
    ]
    if failures:
        lines+=["## Failures"]+[f"- {x}" for x in failures[:80]]
    else:
        lines+=["No machine-QA invariant failures detected.","","Next action: Stanley performs a small actual-phone spot-check before any promotion discussion."]
    rp=Path(args.report); rp.parent.mkdir(parents=True,exist_ok=True); rp.write_text("\n".join(lines)+"\n")
    print("\n".join(lines[:30]))
    if not passed: raise SystemExit(2)

if __name__=="__main__": main()
