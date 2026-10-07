## UBU factory scope — 7 Oct 2026

**UBU-only branch automation. Production main untouched. Keys candidate inherited but not regenerated.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; pathological pages may use an **emergency plasticine token-stream slide** while preserving genuine token order; if that still fails, the factory may use **flagged borrowed-fill camouflage from elsewhere in the same book** (same chapter preferred, then nearby chapters, then same book); socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **25**
- pages whose force layer changed: **30**
- exact target hits: **23**
- ±1 line: **0**
- ±2 lines: **0**
- >2 lines: **2**
- mean absolute target error: **0.52 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **0**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- canonical source token-order mismatches: **0**
- page-head mid-sentence failures: **0**
- local prepared-boundary slides used: **12**
- emergency plasticine slides used: **0**
- borrowed-fill prepared pages used: **8**
- airlock-left sentence-completion failures: **0**
- adjacent prose-overlap failures: **2**
- chapter-opener socket failures: **0**
- duplicate prepared heads stripped before rebuild: **0**
- DOUBLE-UP pages: **2** (144 repeated packing words)
- root/public corpus parity failures: **0**

## Machine verdict: **HOLD**

## Borrowed-fill exceptions
- ch1 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch1 p3 — SAME_CHAPTER — target 12 — rendered line 12
- ch4 p2 — SAME_CHAPTER — target 8 — rendered line 8
- ch4 p6 — SAME_CHAPTER — target 14 — rendered line 14
- ch4 p8 — SAME_CHAPTER — target 12 — rendered line 12
- ch5 p3 — NEARBY_CHAPTER — target 12 — rendered line 12
- ch5 p5 — SAME_CHAPTER — target 10 — rendered line 10
- ch5 p6 — SAME_CHAPTER — target 14 — rendered line 14

## Failures
- ubu ch4 p2/p3: distinctive adjacent prose overlap
- ubu ch5 p5/p6: distinctive adjacent prose overlap
