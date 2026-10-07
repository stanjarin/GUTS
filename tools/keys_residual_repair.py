#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
sys.path.insert(0,"tools")
import keys_factory_scope as k

ROOT=Path("PERFORMANCE10/keys_performance.json")
PUB=Path("public/PERFORMANCE10/keys_performance.json")
OUT=Path("docs/checkpoints/2026-10-07_keys-residual-repair-report.md")
TARGETS={(1,4),(1,5),(1,6),(2,3),(2,18),(2,33),(2,46),(2,79),(3,11),
(4,3),(4,4),(4,58),(4,63),(4,67),(4,70),(4,81),(4,84),(4,138),(4,139),
(4,144),(4,147),(4,157),(4,173),(6,5)}

def slide(book,c,p):
    pages=book["chapters"][c-1]["pages"]; cur=pages[p-1]; prev=pages[p-2]
    fp=list(cur.get("force_paragraphs") or [])
    airs=[i for i,x in enumerate(fp) if "$$" in str(x)]
    if len(airs)!=1: return "bad socket"
    air=fp[airs[0]]
    toks=k.words(" ".join(cur.get("paragraphs",[])))
    if len(toks)<20: return "too little canonical text"
    cut=None; end=None
    for i in range(4,min(18,len(toks)-8)):
        if not k.is_terminal_token(toks[i-1]):
            cut=i; break
    if cut is None: return "no mid-sentence cut"
    for j in range(cut+6,min(len(toks),cut+140)):
        if k.is_terminal_token(toks[j]):
            end=j+1; break
    if end is None: return "no terminal after cut"
    prefix=" ".join(toks[:cut]); head=" ".join(toks[cut:end]); tail=" ".join(toks[end:])
    pfp=list(prev.get("force_paragraphs") or prev.get("paragraphs") or [])
    last=max((i for i,x in enumerate(pfp) if "$$" not in str(x)),default=-1)
    if last>=0: pfp[last]=str(pfp[last]).rstrip()+" "+prefix
    prev["force_paragraphs"]=pfp
    cur["force_paragraphs"]=[head,air]+([tail] if tail else [])
    cur["airlock_index"]=1; cur["pre_airlock_words"]=len(k.words(head))
    cur["residual_repair"]="targeted boundary slide"
    return None

book=json.loads(ROOT.read_text())
errs=[]
for c,p in sorted(TARGETS):
    e=slide(book,c,p)
    if e: errs.append(f"ch{c} p{p}: {e}")
stats={x:0 for x in ["opener_socket_failures","mid_sentence_failures","adjacent_overlap_failures"]}
fails=[]
k.adjacency_and_head_qa(book,stats,fails)
errs+=fails
verdict="PASS" if not errs else "HOLD"
lines=["# Keys residual repair — 7 Oct 2026","",
f"- targeted pages: **{len(TARGETS)}**",
f"- remaining sentence-start failures: **{stats['mid_sentence_failures']}**",
f"- remaining adjacent-overlap failures: **{stats['adjacent_overlap_failures']}**",
f"- opener socket failures: **{stats['opener_socket_failures']}**","",
f"## Machine verdict: **{verdict}**"]
if errs: lines+=["","## Remaining failures"]+[f"- {x}" for x in errs]
OUT.write_text("\n".join(lines)+"\n")
if verdict=="PASS":
    payload=json.dumps(book,ensure_ascii=False,separators=(",",":"))
    ROOT.write_text(payload); PUB.write_text(payload)
print("\n".join(lines))
raise SystemExit(0 if verdict=="PASS" else 1)
