# Factory autopilot — jt_035 — 7 Oct 2026

**Single-book branch automation. Production main untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; pathological pages may use an **emergency plasticine token-stream slide** while preserving genuine token order; if that still fails, the factory may use **flagged borrowed-fill camouflage from elsewhere in the same book** (same chapter preferred, then nearby chapters, then same book); socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **45**
- pages whose force layer changed: **55**
- exact target hits: **39**
- ±1 line: **1**
- ±2 lines: **0**
- >2 lines: **5**
- mean absolute target error: **1.16 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **0**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- canonical source token-order mismatches: **0**
- page-head mid-sentence failures: **0**
- local prepared-boundary slides used: **19**
- emergency plasticine slides used: **0**
- borrowed-fill prepared pages used: **6**
- airlock-left sentence-completion failures: **0**
- adjacent prose-overlap failures: **2**
- chapter-opener socket failures: **0**
- duplicate prepared heads stripped before rebuild: **0**
- DOUBLE-UP pages: **3** (198 repeated packing words)
- root/public corpus parity failures: **0**

## Machine verdict: **PASS**

## Borrowed-fill exceptions
- ch1 p2 — NEARBY_CHAPTER — target 8 — rendered line 8
- ch1 p3 — NEARBY_CHAPTER — target 12 — rendered line 12
- ch8 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch8 p4 — SAME_CHAPTER — target 16 — rendered line 16
- ch10 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch10 p5 — SAME_CHAPTER — target 10 — rendered line 10

No machine-QA invariant failures detected. Borrowed-fill camouflage is permitted only when explicitly flagged; canonical source paragraphs remain the authority.

Next action: autopilot continues. Human intervention is required only for consolidated structural exceptions or final phone QA.
