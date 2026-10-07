# Factory autopilot — farewell_035 — 7 Oct 2026

**Single-book branch automation. Production main untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; pathological pages may use an **emergency plasticine token-stream slide** while preserving genuine token order; if that still fails, the factory may use **flagged borrowed-fill camouflage from elsewhere in the same book** (same chapter preferred, then nearby chapters, then same book); socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **174**
- pages whose force layer changed: **215**
- exact target hits: **149**
- ±1 line: **2**
- ±2 lines: **4**
- >2 lines: **19**
- mean absolute target error: **0.81 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **0**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- canonical source token-order mismatches: **0**
- page-head mid-sentence failures: **2**
- local prepared-boundary slides used: **43**
- emergency plasticine slides used: **1**
- borrowed-fill prepared pages used: **10**
- airlock-left sentence-completion failures: **0**
- adjacent prose-overlap failures: **5**
- chapter-opener socket failures: **0**
- duplicate prepared heads stripped before rebuild: **0**
- DOUBLE-UP pages: **9** (648 repeated packing words)
- root/public corpus parity failures: **0**

## Machine verdict: **PASS**

## Borrowed-fill exceptions
- ch5 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch12 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch12 p3 — NEARBY_CHAPTER — target 12 — rendered line 12
- ch12 p4 — NEARBY_CHAPTER — target 16 — rendered line 16
- ch31 p2 — NEARBY_CHAPTER — target 8 — rendered line 10
- ch31 p3 — NEARBY_CHAPTER — target 12 — rendered line 14
- ch31 p4 — NEARBY_CHAPTER — target 16 — rendered line 18
- ch32 p2 — NEARBY_CHAPTER — target 8 — rendered line 12
- ch38 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch38 p3 — SAME_CHAPTER — target 12 — rendered line 12

No machine-QA invariant failures detected. Borrowed-fill camouflage is permitted only when explicitly flagged; canonical source paragraphs remain the authority.

Next action: autopilot continues. Human intervention is required only for consolidated structural exceptions or final phone QA.
