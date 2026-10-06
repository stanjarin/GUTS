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

No machine-QA invariant failures detected.

Next action: Stanley performs actual-phone QA on the Jeeves candidate before any promotion discussion.
