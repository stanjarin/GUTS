# Jeeves factory pilot — 6 Oct 2026

**Jeeves-only branch automation. Production main and all other books untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; pathological pages may use an **emergency plasticine token-stream slide** while preserving genuine token order; if that still fails, the factory may use **flagged borrowed-fill camouflage from elsewhere in the same book** (same chapter preferred, then nearby chapters, then same book); socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **323**
- pages whose force layer changed: **329**
- exact target hits: **273**
- ±1 line: **4**
- ±2 lines: **5**
- >2 lines: **41**
- mean absolute target error: **0.77 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **0**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- canonical source token-order mismatches: **0**
- page-head mid-sentence failures: **17**
- local prepared-boundary slides used: **43**
- emergency plasticine slides used: **0**
- borrowed-fill prepared pages used: **16**
- airlock-left sentence-completion failures: **0**
- adjacent prose-overlap failures: **7**
- chapter-opener socket failures: **0**
- duplicate prepared heads stripped before rebuild: **0**
- DOUBLE-UP pages: **20** (1422 repeated packing words)
- root/public corpus parity failures: **0**

## Machine verdict: **HOLD**

## Borrowed-fill exceptions
- ch2 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch3 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch4 p2 — SAME_CHAPTER — target 8 — rendered line 15
- ch4 p3 — SAME_CHAPTER — target 12 — rendered line 19
- ch4 p4 — SAME_CHAPTER — target 16 — rendered line 14
- ch4 p19 — SAME_CHAPTER — target 16 — rendered line 16
- ch4 p32 — SAME_CHAPTER — target 8 — rendered line 18
- ch4 p113 — SAME_CHAPTER — target 12 — rendered line 15
- ch4 p137 — SAME_CHAPTER — target 8 — rendered line 18
- ch4 p138 — SAME_CHAPTER — target 12 — rendered line 22
- ch4 p139 — SAME_CHAPTER — target 16 — rendered line 16
- ch4 p141 — SAME_CHAPTER — target 14 — rendered line 15
- ch4 p143 — SAME_CHAPTER — target 12 — rendered line 15
- ch4 p144 — SAME_CHAPTER — target 16 — rendered line 19
- ch4 p146 — SAME_CHAPTER — target 14 — rendered line 15
- ch4 p147 — SAME_CHAPTER — target 8 — rendered line 19

## Failures
- keys ch1 p4: prepared page begins at sentence start
- keys ch1 p5: prepared page begins at sentence start
- keys ch1 p6: prepared page begins at sentence start
- keys ch2 p2/p3: distinctive adjacent prose overlap
- keys ch2 p18: prepared page begins at sentence start
- keys ch2 p33: prepared page begins at sentence start
- keys ch2 p46: prepared page begins at sentence start
- keys ch2 p79: prepared page begins at sentence start
- keys ch3 p11: prepared page begins at sentence start
- keys ch4 p2/p3: distinctive adjacent prose overlap
- keys ch4 p3/p4: distinctive adjacent prose overlap
- keys ch4 p58: prepared page begins at sentence start
- keys ch4 p63: prepared page begins at sentence start
- keys ch4 p67: prepared page begins at sentence start
- keys ch4 p70: prepared page begins at sentence start
- keys ch4 p81: prepared page begins at sentence start
- keys ch4 p84: prepared page begins at sentence start
- keys ch4 p137/p138: distinctive adjacent prose overlap
- keys ch4 p138/p139: distinctive adjacent prose overlap
- keys ch4 p143/p144: distinctive adjacent prose overlap
- keys ch4 p146/p147: distinctive adjacent prose overlap
- keys ch4 p157: prepared page begins at sentence start
- keys ch4 p173: prepared page begins at sentence start
- keys ch6 p5: prepared page begins at sentence start
