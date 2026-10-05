#!/usr/bin/env python3
"""
Cheap fixed-reader copyfit surrogate.

Purpose:
  Predict vertical airlock/socket start from paragraph text without browser rendering.

Calibrated 2026-10-05 against actual iPhone 8 Plus GUTS screenshots:
  effective full-line capacity ~= 46 characters
  font size 18px
  line-height 1.45
  paragraph bottom margin .82em
  page top padding 22px

Diagnostic only. Never mutates corpus.
"""
import argparse, json
from pathlib import Path

DEFAULTS = {
    "chars_per_line": 46,
    "font_px": 18.0,
    "line_height": 1.45,
    "paragraph_margin_em": 0.82,
    "top_padding_px": 22.0,
    "high_px": 120.0,
    "low_px": 450.0,
}

def greedy_lines(text, cap):
    total = 0
    for hard in str(text).splitlines() or [""]:
        words = hard.strip().split()
        if not words:
            total += 1
            continue
        lines, used = 0, 0
        for word in words:
            need = len(word) + (1 if used else 0)
            if used and used + need > cap:
                lines += 1
                used = len(word)
            else:
                used += need
        total += lines + (1 if used else 0)
    return total

def analyse_page(page, cfg):
    fps = page.get("force_paragraphs") or []
    ai = page.get("airlock_index")
    if ai is None or ai < 0 or ai >= len(fps):
        return {"status": "NO_AIRLOCK"}

    cap = int(cfg["chars_per_line"])
    line_px = float(cfg["font_px"]) * float(cfg["line_height"])
    margin_px = float(cfg["font_px"]) * float(cfg["paragraph_margin_em"])
    y = float(cfg["top_padding_px"])

    prior = fps[:ai]
    prior_lines = []
    for p in prior:
        n = greedy_lines(p, cap)
        prior_lines.append(n)
        y += n * line_px + margin_px

    if y < float(cfg["high_px"]):
        band = "HIGH"
    elif y > float(cfg["low_px"]):
        band = "LOW"
    else:
        band = "OK"

    air = fps[ai]
    return {
        "status": "OK",
        "socket_start_px": round(y, 1),
        "band": band,
        "airlock_index": ai,
        "prior_paragraphs": len(prior),
        "prior_lines": prior_lines,
        "airlock_lines": greedy_lines(air, cap),
        "contains_dollars": "$$$" in air,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page_json", help="JSON object containing force_paragraphs + airlock_index")
    ap.add_argument("--chars", type=int, default=DEFAULTS["chars_per_line"])
    args = ap.parse_args()
    page = json.loads(Path(args.page_json).read_text())
    cfg = dict(DEFAULTS)
    cfg["chars_per_line"] = args.chars
    print(json.dumps(analyse_page(page, cfg), indent=2))

if __name__ == "__main__":
    main()
