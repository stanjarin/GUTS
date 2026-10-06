# Jeeves factory pilot — 6 Oct 2026

**Jeeves-only branch automation. Production main and all other books untouched.**

Law: every forceable prepared page begins **mid-sentence**; the airlock appears only after a **proper completed sentence**; socket-start targets cycle **8 / 12 / 16 / 10 / 14**; unrelated Gutenberg paragraph oddities are left alone.

Renderer used for machine pass: Chromium at the fixed Reader geometry (329 CSS px, Georgia 15px/1.45). Actual iPhone Safari remains the phone-QA authority.

## Compact QA
- forceable prepared pages repaired: **183**
- pages whose force layer changed: **210**
- exact target hits: **160**
- ±1 line: **3**
- ±2 lines: **2**
- >2 lines: **18**
- mean absolute target error: **0.69 lines**
- adjacent <4-line spacing violations: **0**
- 3-page retention windows within 4-line band: **0**
- unresolved prepared pages: **22**
- skipped chapters: **0**
- genuine paragraph hash mismatches: **0**
- genuine token-order mismatches: **0**
- page-head mid-sentence failures: **0**
- airlock-left sentence-completion failures: **0**
- root/public corpus parity failures: **0**

## Machine verdict: **HOLD**

## Unresolved classification
- NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT: **21**
- SPACING_OR_RETENTION_CONFLICT: **1**

## Unresolved locations
- ch1 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch1 p3 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 12 — previous line None
- ch3 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch4 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch6 p9 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 16 — previous line 12
- ch7 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch8 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch9 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch11 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch11 p11 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 14 — previous line 10
- ch12 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch14 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch16 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch17 p5 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 10 — previous line 5
- ch17 p9 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 16 — previous line 12
- ch21 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch21 p3 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 12 — previous line None
- ch22 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None
- ch22 p3 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 12 — previous line None
- ch22 p14 — SPACING_OR_RETENTION_CONFLICT — target 16 — previous line 4
- ch22 p15 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 10 — previous line None
- ch23 p2 — NO_LEGAL_MID_SENTENCE_TO_TERMINAL_SPLIT — target 8 — previous line None

No machine-QA invariant failures detected.

Next action: Builder diagnoses unresolved classes and revises factory; Stanley phone QA only after a clean candidate exists.
