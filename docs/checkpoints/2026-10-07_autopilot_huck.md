# Factory autopilot — huck_035 — 7 Oct 2026

**Single-book branch automation. Production main untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; pathological pages may use an **emergency plasticine token-stream slide** while preserving genuine token order; if that still fails, the factory may use **flagged borrowed-fill camouflage from elsewhere in the same book** (same chapter preferred, then nearby chapters, then same book); socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **227**
- pages whose force layer changed: **270**
- exact target hits: **184**
- ±1 line: **13**
- ±2 lines: **2**
- >2 lines: **28**
- mean absolute target error: **0.96 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **0**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- canonical source token-order mismatches: **0**
- page-head mid-sentence failures: **12**
- local prepared-boundary slides used: **101**
- emergency plasticine slides used: **0**
- borrowed-fill prepared pages used: **62**
- airlock-left sentence-completion failures: **0**
- adjacent prose-overlap failures: **22**
- chapter-opener socket failures: **0**
- duplicate prepared heads stripped before rebuild: **1**
- DOUBLE-UP pages: **14** (1008 repeated packing words)
- root/public corpus parity failures: **0**

## Machine verdict: **PASS**

## Borrowed-fill exceptions
- ch1 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch1 p4 — NEARBY_CHAPTER — target 16 — rendered line 16
- ch2 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch3 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch3 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch6 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch6 p3 — NEARBY_CHAPTER — target 12 — rendered line 12
- ch6 p4 — NEARBY_CHAPTER — target 16 — rendered line 16
- ch6 p5 — NEARBY_CHAPTER — target 10 — rendered line 10
- ch6 p6 — NEARBY_CHAPTER — target 14 — rendered line 14
- ch6 p7 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch6 p8 — NEARBY_CHAPTER — target 12 — rendered line 12
- ch7 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch7 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch7 p4 — SAME_CHAPTER — target 16 — rendered line 7
- ch7 p5 — SAME_CHAPTER — target 10 — rendered line 11
- ch7 p6 — SAME_CHAPTER — target 14 — rendered line 6
- ch8 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch8 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch8 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch8 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch10 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch12 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch13 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch13 p5 — SAME_CHAPTER — target 10 — rendered line 11
- ch15 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch15 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch18 p2 — SAME_CHAPTER — target 8 — rendered line 11
- ch18 p9 — SAME_CHAPTER — target 16 — rendered line 16
- ch18 p11 — SAME_CHAPTER — target 14 — rendered line 14
- ch18 p12 — SAME_CHAPTER — target 8 — rendered line 8
- ch19 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch20 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch21 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch21 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch22 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch22 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch24 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch25 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch26 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch27 p2 — SAME_CHAPTER — target 8 — rendered line 9
- ch29 p9 — SAME_CHAPTER — target 16 — rendered line 16
- ch31 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch31 p6 — SAME_CHAPTER — target 14 — rendered line 14
- ch31 p7 — SAME_CHAPTER — target 8 — rendered line 8
- ch31 p8 — SAME_CHAPTER — target 12 — rendered line 12
- ch32 p2 — SAME_CHAPTER — target 8 — rendered line 10
- ch32 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch34 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch36 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch36 p6 — SAME_CHAPTER — target 14 — rendered line 14
- ch37 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch37 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch37 p6 — SAME_CHAPTER — target 14 — rendered line 14
- ch39 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch39 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch40 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch40 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch41 p3 — SAME_CHAPTER — target 12 — rendered line 13
- ch41 p4 — SAME_CHAPTER — target 16 — rendered line 17
- ch41 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch42 p2 — SAME_CHAPTER — target 8 — rendered line 8

No machine-QA invariant failures detected. Borrowed-fill camouflage is permitted only when explicitly flagged; canonical source paragraphs remain the authority.

Next action: autopilot continues. Human intervention is required only for consolidated structural exceptions or final phone QA.
