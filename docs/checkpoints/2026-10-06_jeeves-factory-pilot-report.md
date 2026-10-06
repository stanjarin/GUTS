# Jeeves factory pilot — 6 Oct 2026

**Jeeves-only branch automation. Production main and all other books untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; pathological pages may use an **emergency plasticine token-stream slide** while preserving genuine token order; if that still fails, the factory may use **flagged borrowed-fill camouflage from elsewhere in the same book** (same chapter preferred, then nearby chapters, then same book); socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **205**
- pages whose force layer changed: **228**
- exact target hits: **90**
- ±1 line: **15**
- ±2 lines: **8**
- >2 lines: **92**
- mean absolute target error: **3.35 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **0**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- canonical source token-order mismatches: **0**
- page-head mid-sentence failures: **3**
- local prepared-boundary slides used: **91**
- emergency plasticine slides used: **2**
- borrowed-fill prepared pages used: **24**
- airlock-left sentence-completion failures: **0**
- adjacent prose-overlap failures: **8**
- chapter-opener socket failures: **0**
- duplicate prepared heads stripped before rebuild: **314**
- DOUBLE-UP pages: **144** (16806 repeated packing words)
- root/public corpus parity failures: **0**

## Machine verdict: **HOLD**

## Borrowed-fill exceptions
- ch1 p2 — SAME_CHAPTER — target 8 — rendered line 3
- ch1 p5 — SAME_CHAPTER — target 10 — rendered line 16
- ch1 p6 — SAME_CHAPTER — target 14 — rendered line 20
- ch5 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch7 p6 — SAME_CHAPTER — target 14 — rendered line 14
- ch8 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch10 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch10 p6 — SAME_CHAPTER — target 14 — rendered line 15
- ch10 p9 — SAME_CHAPTER — target 16 — rendered line 16
- ch11 p8 — SAME_CHAPTER — target 12 — rendered line 12
- ch11 p10 — SAME_CHAPTER — target 10 — rendered line 11
- ch15 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch17 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch17 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch17 p7 — SAME_CHAPTER — target 8 — rendered line 8
- ch17 p13 — SAME_CHAPTER — target 12 — rendered line 12
- ch17 p17 — SAME_CHAPTER — target 8 — rendered line 8
- ch20 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch20 p4 — SAME_CHAPTER — target 16 — rendered line 14
- ch20 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch22 p2 — SAME_CHAPTER — target 8 — rendered line 15
- ch22 p8 — SAME_CHAPTER — target 12 — rendered line 15
- ch22 p10 — SAME_CHAPTER — target 10 — rendered line 15
- ch22 p16 — SAME_CHAPTER — target 14 — rendered line 15

## Failures
- jeeves ch1 p1/p2: distinctive adjacent prose overlap
- jeeves ch1 p5/p6: distinctive adjacent prose overlap
- jeeves ch5 p1/p2: distinctive adjacent prose overlap
- jeeves ch8 p6: prepared page begins at sentence start
- jeeves ch9 p7: prepared page begins at sentence start
- jeeves ch17 p1/p2: distinctive adjacent prose overlap
- jeeves ch17 p2/p3: distinctive adjacent prose overlap
- jeeves ch20 p1/p2: distinctive adjacent prose overlap
- jeeves ch20 p4/p5: distinctive adjacent prose overlap
- jeeves ch20 p6: prepared page begins at sentence start
- jeeves ch22 p2/p3: distinctive adjacent prose overlap
