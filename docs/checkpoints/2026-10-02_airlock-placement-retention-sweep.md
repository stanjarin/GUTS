# GUTS airlock placement + retention sweep — 2026-10-02

Scope: all 18 active GUTS books. Prepared corpus layer only.

Rollback:
- `rollback-pre-airlock-sweep-2026-10-02`
- base `6113a1a7bac25f389ddb5444dca4d7b4c775b459`

Repair rules:
- genuine `paragraphs` untouched;
- existing airlock sentence preserved;
- exactly one `$$$` socket per prepared page;
- PLACEMENT defect = airlock at top, fewer than 12 genuine words before it, or heading-only material before it;
- RETENTION defect = run of 3+ consecutive pages whose pre-airlock depth sits within an 8-word band;
- historical carry targets 28 / 48 / 68 / 38 / 58 words used as the repair compass;
- existing paragraph boundaries preferred;
- where necessary, only the prepared display layer is split at a sentence boundary;
- selected-chapter opener protection in the Reader is unchanged;
- no Reader/state/covers/chapters/repagination changes.

Audit/repair:
- prepared pages scanned: 4,858
- initial PLACEMENT flags: 552
- initial RETENTION flags: 12
- prepared pages changed: 567
- prepared-only sentence splits: 301

Whole-corpus machine QA after repair:
- books: 18/18
- PLACEMENT flags: 0
- RETENTION flags: 0
- bad/multiple/missing sockets: 0
- `$$$` leaks into genuine text: 0
- genuine token-order mismatches: 0
- root/public corpus parity failures: 0

Promotion:
- authorised by Stanley as a one-pass audit + repair + machine-QA promotion.
- production phone/visual spot-check remains advisable; this pass did not alter runtime code.
