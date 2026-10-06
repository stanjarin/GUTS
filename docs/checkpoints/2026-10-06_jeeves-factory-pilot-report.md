# Jeeves factory pilot — 6 Oct 2026

**Jeeves-only branch automation. Production main and all other books untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **202**
- pages whose force layer changed: **226**
- exact target hits: **173**
- ±1 line: **4**
- ±2 lines: **0**
- >2 lines: **25**
- mean absolute target error: **0.85 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **3**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- genuine token-order mismatches: **0**
- page-head mid-sentence failures: **0**
- local prepared-boundary slides used: **21**
- airlock-left sentence-completion failures: **0**
- root/public corpus parity failures: **0**

## Machine verdict: **HOLD**

## Unresolved classification
- NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT: **2**
- SPACING_OR_RETENTION_CONFLICT / NO_BOUNDARY_SLIDE_SPLIT: **1**

## Unresolved locations
- ch1 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 8 — previous line None
- ch22 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 8 — previous line None
- ch22 p14 — SPACING_OR_RETENTION_CONFLICT / NO_BOUNDARY_SLIDE_SPLIT — target 16 — previous line 4

No machine-QA invariant failures detected.

Next action: Builder diagnoses unresolved classes and revises factory; Stanley phone QA only after a clean candidate exists.
