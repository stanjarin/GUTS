# Jeeves factory pilot — 6 Oct 2026

**Jeeves-only branch automation. Production main and all other books untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; prepared-layer paragraphs may be **joined or locally rebalanced across page boundaries** when needed; socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **194**
- pages whose force layer changed: **220**
- exact target hits: **165**
- ±1 line: **6**
- ±2 lines: **0**
- >2 lines: **23**
- mean absolute target error: **0.76 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **11**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- genuine token-order mismatches: **0**
- page-head mid-sentence failures: **0**
- local prepared-boundary slides used: **13**
- airlock-left sentence-completion failures: **0**
- root/public corpus parity failures: **0**

## Machine verdict: **HOLD**

## Unresolved classification
- NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / BOUNDARY_SLIDE_SPACING_CONFLICT: **1**
- NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT: **8**
- SPACING_OR_RETENTION_CONFLICT / BOUNDARY_SLIDE_SPACING_CONFLICT: **1**
- SPACING_OR_RETENTION_CONFLICT / NO_BOUNDARY_SLIDE_SPLIT: **1**

## Unresolved locations
- ch1 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 8 — previous line None
- ch1 p3 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 12 — previous line None
- ch3 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 8 — previous line None
- ch7 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 8 — previous line None
- ch12 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 8 — previous line None
- ch14 p3 — SPACING_OR_RETENTION_CONFLICT / BOUNDARY_SLIDE_SPACING_CONFLICT — target 12 — previous line 4
- ch21 p3 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / BOUNDARY_SLIDE_SPACING_CONFLICT — target 12 — previous line 4
- ch22 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 8 — previous line None
- ch22 p3 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 12 — previous line None
- ch22 p14 — SPACING_OR_RETENTION_CONFLICT / NO_BOUNDARY_SLIDE_SPLIT — target 16 — previous line 4
- ch22 p15 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT / NO_BOUNDARY_SLIDE_SPLIT — target 10 — previous line None

No machine-QA invariant failures detected.

Next action: Builder diagnoses unresolved classes and revises factory; Stanley phone QA only after a clean candidate exists.
