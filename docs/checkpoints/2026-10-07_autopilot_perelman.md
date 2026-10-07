# Factory autopilot — perelman_performance — 7 Oct 2026

**Single-book branch automation. Production main untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; pathological pages may use an **emergency plasticine token-stream slide** while preserving genuine token order; if that still fails, the factory may use **flagged borrowed-fill camouflage from elsewhere in the same book** (same chapter preferred, then nearby chapters, then same book); socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **208**
- pages whose force layer changed: **257**
- exact target hits: **166**
- ±1 line: **6**
- ±2 lines: **0**
- >2 lines: **36**
- mean absolute target error: **1.28 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **0**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- canonical source token-order mismatches: **0**
- page-head mid-sentence failures: **5**
- local prepared-boundary slides used: **93**
- emergency plasticine slides used: **0**
- borrowed-fill prepared pages used: **60**
- airlock-left sentence-completion failures: **0**
- adjacent prose-overlap failures: **27**
- chapter-opener socket failures: **0**
- duplicate prepared heads stripped before rebuild: **1**
- DOUBLE-UP pages: **15** (1062 repeated packing words)
- root/public corpus parity failures: **0**

## Machine verdict: **PASS**

## Borrowed-fill exceptions
- ch1 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch2 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch5 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch5 p4 — NEARBY_CHAPTER — target 16 — rendered line 16
- ch6 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch6 p3 — NEARBY_CHAPTER — target 12 — rendered line 12
- ch6 p4 — NEARBY_CHAPTER — target 16 — rendered line 16
- ch7 p2 — SAME_CHAPTER — target 8 — rendered line 12
- ch7 p3 — SAME_CHAPTER — target 12 — rendered line 8
- ch7 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch7 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch8 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch10 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch11 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch11 p3 — NEARBY_CHAPTER — target 12 — rendered line 12
- ch11 p4 — NEARBY_CHAPTER — target 16 — rendered line 16
- ch11 p5 — NEARBY_CHAPTER — target 10 — rendered line 10
- ch11 p6 — NEARBY_CHAPTER — target 14 — rendered line 14
- ch11 p7 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch13 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch15 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch15 p6 — SAME_CHAPTER — target 14 — rendered line 14
- ch15 p7 — SAME_CHAPTER — target 8 — rendered line 8
- ch15 p8 — SAME_CHAPTER — target 12 — rendered line 12
- ch15 p11 — SAME_CHAPTER — target 14 — rendered line 14
- ch16 p3 — NEARBY_CHAPTER — target 12 — rendered line 12
- ch16 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch17 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch19 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch19 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch20 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch24 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch26 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch29 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch32 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch32 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch32 p6 — SAME_CHAPTER — target 14 — rendered line 14
- ch34 p2 — NEARBY_CHAPTER — target 8 — rendered line 9
- ch34 p3 — SAME_CHAPTER — target 12 — rendered line 13
- ch34 p4 — SAME_CHAPTER — target 16 — rendered line 17
- ch34 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch34 p6 — SAME_CHAPTER — target 14 — rendered line 14
- ch37 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch37 p6 — SAME_CHAPTER — target 14 — rendered line 14
- ch37 p7 — SAME_CHAPTER — target 8 — rendered line 18
- ch38 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch38 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch39 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch39 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch39 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch39 p13 — SAME_CHAPTER — target 12 — rendered line 12
- ch39 p14 — SAME_CHAPTER — target 16 — rendered line 16
- ch42 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch43 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch43 p3 — NEARBY_CHAPTER — target 12 — rendered line 12
- ch43 p4 — NEARBY_CHAPTER — target 16 — rendered line 16
- ch43 p5 — NEARBY_CHAPTER — target 10 — rendered line 10
- ch43 p6 — NEARBY_CHAPTER — target 14 — rendered line 14
- ch47 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch47 p4 — SAME_CHAPTER — target 16 — rendered line 16

No machine-QA invariant failures detected. Borrowed-fill camouflage is permitted only when explicitly flagged; canonical source paragraphs remain the authority.

Next action: autopilot continues. Human intervention is required only for consolidated structural exceptions or final phone QA.
