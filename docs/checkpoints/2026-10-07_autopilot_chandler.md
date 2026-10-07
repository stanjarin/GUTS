# Factory autopilot — chandler_performance — 7 Oct 2026

**Single-book branch automation. Production main untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; pathological pages may use an **emergency plasticine token-stream slide** while preserving genuine token order; if that still fails, the factory may use **flagged borrowed-fill camouflage from elsewhere in the same book** (same chapter preferred, then nearby chapters, then same book); socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **209**
- pages whose force layer changed: **248**
- exact target hits: **177**
- ±1 line: **3**
- ±2 lines: **4**
- >2 lines: **25**
- mean absolute target error: **0.85 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **0**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- canonical source token-order mismatches: **0**
- page-head mid-sentence failures: **0**
- local prepared-boundary slides used: **55**
- emergency plasticine slides used: **0**
- borrowed-fill prepared pages used: **13**
- airlock-left sentence-completion failures: **0**
- adjacent prose-overlap failures: **3**
- chapter-opener socket failures: **0**
- duplicate prepared heads stripped before rebuild: **0**
- DOUBLE-UP pages: **9** (642 repeated packing words)
- root/public corpus parity failures: **0**

## Machine verdict: **PASS**

## Borrowed-fill exceptions
- ch1 p2 — NEARBY_CHAPTER — target 8 — rendered line 10
- ch8 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch10 p2 — SAME_CHAPTER — target 8 — rendered line 10
- ch10 p3 — SAME_CHAPTER — target 12 — rendered line 14
- ch10 p4 — SAME_CHAPTER — target 16 — rendered line 9
- ch18 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch20 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch23 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch23 p6 — SAME_CHAPTER — target 14 — rendered line 15
- ch24 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch24 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch24 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch32 p2 — SAME_CHAPTER — target 8 — rendered line 8

No machine-QA invariant failures detected. Borrowed-fill camouflage is permitted only when explicitly flagged; canonical source paragraphs remain the authority.

Next action: autopilot continues. Human intervention is required only for consolidated structural exceptions or final phone QA.
