# GUTS — HANDOVER / START HERE

**Checkpoint: 2 October 2026, after phone QA PASS**

## 0. Read broadly, act narrowly

Before changing anything:
1. read `GUTS_WORKFLOW_CONSTITUTION.md`;
2. read this handover;
3. read `GUTS_CURRENT_STATE.md`;
4. read `docs/CURRENT_STATE.md`;
5. read relevant GUTS code/config/docs;
6. read the NoBo handover/README for the cross-system control contract.

Do not begin by editing.

## 1. Production safety

Production `main` is still untouched at:

`aef68707b1ad031eab16ae1efbecce5733630186`

Current QA-passed GUTS branch:

`protocol-cleanup-2026-10-01`

Current branch head at handover:

`5078c5e2cab2c741b9ae4e3b2ccf4aeb49d62b5a`

Current paired NoBo branch:

`controls-refresh-2026-10-01`

NoBo branch head at handover:

`02295e21e354e69da08d1dda55686a09dfecfeb3`

Do not use either `main` as a workbench before promotion is deliberately executed.

## 2. Current authority / architecture

Canonical rule:

**NoBo commands. GUTS executes.**

Three concerns are now orthogonal:

- **MAGIC:** READY → ARMED → local PAID
- **VISIBILITY:** SHW ↔ HIDD
- **AUTH:** PIN valid / invalid

Changing visibility must never mutate magic state.

### Live remote protocol

Remote GUTS magic state accepts only:
- READY
- ARMED (+ word)

CLEAN is no longer part of the live NoBo↔GUTS protocol.

### Local reader behaviour

GUTS reader still owns:
- selected-chapter opener protection;
- prepared `$$$` substitution;
- 6-second dwell;
- local PAID/freeze behaviour.

Remote READY on a newer revision clears local ARMED/PAID state.
Remote ARMED does not overwrite an already-PAID reader until RSET/READY occurs.

## 3. Protocol cleanup completed

On `protocol-cleanup-2026-10-01`:

- `/api/performer/validate` validates ARM PIN without mutating state;
- `/api/performer/state` accepts READY / ARMED only;
- `/api/performer/mode` changes site mode only;
- `/performer/rehearsal` authorises that browser only; it no longer changes mode or magic state;
- absent site-mode KV defaults to REHEARSAL/HIDD;
- GUTS root/public reader copies consume READY / ARMED only;
- root/public reader parity was machine-checked;
- no live CLEAN branch remains in the worker/reader protocol path.

Existing private names:
- ARM PIN value currently used by Stanley: `arm`
- SHOW PIN value currently used by Stanley: `show`

Do not invent a third “site PIN” term. In conversation/UI use **ARM PIN** and **SHOW PIN**.

## 4. Phone QA — PASSED

Actual iPhone QA passed after the coordinated NoBo/GUTS cleanup:

- [WORD] survives navigation across all books;
- [WORD] survives HIDD ↔ SHW;
- [WORD] survives a fresh GUTS request/refresh;
- prepared page + 6+ second dwell + departure reaches PAID;
- PAID persistence behaves correctly;
- NoBo RSET sends READY;
- after RSET, [WORD] is gone from prepared pages;
- landing in real Gutenberg after RSET was correctly explained by HIDD still being active, not by loss of state.

Full passed functional chain:

**RSET → READY → ARM [WORD] → GUTS pull → prepared page → 6s dwell → PAID → persistence → RSET/READY → cleared**

This is now the functional truth to preserve.

## 5. Current test URLs

NoBo test:
`https://stanjarin.github.io/NoBoNoFo/`

GUTS protocol branch preview:
`https://protocol-cleanup-2026-10-01-guts.stanjarin.workers.dev/`

GUTS rehearsal authorisation:
`https://protocol-cleanup-2026-10-01-guts.stanjarin.workers.dev/performer/rehearsal`

NoBo test branch deliberately points at the GUTS protocol-cleanup preview for QA.

## 6. Production domain / deployment state

Intended spectator-facing production domain remains:

`ebooks.fyi`

Spare:
`ebks.fyi`

Do not expose `gutenbrg.com` to spectators as a visible redirect target.

The exact final production base URL in NoBo must be changed only during promotion/deployment, after rollback points are created.

## 7. Frozen visual/corpus state

Do not disturb the already passed GUTS visual/corpus work while promoting protocol changes.

Preserve:
- 18-book shelf;
- baked 18-cover carousel;
- current landing art;
- current Reader;
- current page-turn mechanics;
- current chapter/cover behaviour;
- selected opener protection;
- 6-second dwell;
- local PAID;
- existing corpus and air-lock text;
- deliberate ugly modern-cover back-arrow overlap (STET);
- deferred cosmetics list in `docs/COSMETICS_LATER.md`.

This handover is about **promotion of passed plumbing**, not reopening corpus or cosmetics.

## 8. Release closure

**Production release PASSED / FROZEN — 2 October 2026.**

The protocol is not an open debugging job. Promotion/deployment is complete.

Historical promotion plan was:

1. create immutable rollback points for both current QA-passed branches;
2. promote the tested GUTS changes to GUTS `main`;
3. promote the tested NoBo changes to NoBo `main`;
4. repoint NoBo from the temporary GUTS branch-preview base to the chosen production GUTS address;
5. attach/verify `ebooks.fyi` on the production GUTS Worker;
6. run one final production smoke test:
   **RSET → ARM → GUTS → PAID → RSET**;
7. only after that freeze the release and return to deferred cosmetics/editorial work.

## 9. Promotion discipline

Before touching either `main`:
- verify current branch SHAs;
- create named rollback branches/checkpoints;
- record them in canonical docs;
- make no unrelated edits;
- promote one repo at a time;
- verify after each promotion;
- then run the production smoke test.

If any production smoke test fails, revert to the named rollback point rather than improvising on `main`.

## 10. NEXT ACTION

**MY JOB — fresh ewe**
1. read this handover and canonical state;
2. create rollback points;
3. promote the QA-passed branches carefully;
4. repoint NoBo to production GUTS;
5. verify `ebooks.fyi`;
6. guide Stanley through one final smoke test.

**STANLEY'S JOB**
Only the final phone smoke test when asked. No need to repeat the long QA campaign already passed.


## 11. FINAL PRODUCTION PASS — 2 October 2026

Completed and verified:
- GUTS promoted to production;
- NoBo promoted to production;
- NoBo production target = `https://ebooks.fyi`;
- `ebooks.fyi` connected to Cloudflare and attached to the production GUTS Worker;
- live production domain verified;
- actual-phone smoke test PASSED:
  **RSET → ARM → GUTS → prepared page → 6+ sec → PAID persistence → RSET → cleared**.

Stanley’s final report: **“All systems nominal!”**

Frozen runtime anchors:
- GUTS `release-2026-10-02-production-pass` @ `4e6c5c4835fb858ba10409962af694657d921d77`
- NoBo `release-2026-10-02-production-pass` @ `6dcd4b33429788f413f6fd80e503f08553eda0cd`

No functional work is open.

---

# LATEST IMMEDIATE HANDOVER UPDATE — 2 October 2026, wall-hit

**THIS SECTION OVERRIDES EARLIER “NEXT ACTION”, branch, domain and frozen-corpus wording above.**

## Current production / branch truth

- GUTS `main` and `airlock-sweep-2026-10-02` are currently identical at:
  `8a79206da91fe5216c695401d6d3319ba24d32b4`
- pre-sweep rollback:
  `rollback-pre-airlock-sweep-2026-10-02` @ `6113a1a7bac25f389ddb5444dca4d7b4c775b459`
- the older frozen runtime anchor `release-2026-10-02-production-pass` remains historical evidence of the previously phone-passed runtime.
- No Reader/state/Worker code was changed by the airlock sweep.

## Public surface truth

Current public journey:
1. `https://ebooks.fyi` — HTTPS entry / Resources pre-page.
2. tap through to GUTS at:
   `https://www3.library.gutenbrg.com/project_library/books/browse/`
   — HTTPS Gutenberg-facing landing/carousel/Reader.
3. Safari compact address bar may display only `www3.library.gutenbrg.com`; Stanley explicitly accepted this.

NoBo remains:
`https://stanjarin.github.io/NoBoNoFo/`

NoBo API/control base remains `https://ebooks.fyi`; this is intentional.

## Carousel cosmetic completed today

GUTS first-arrival carousel start was changed from Thurber to **Jean Brodie**.
Return-to-jump-point behaviour is preserved.
Runtime/carousel mechanics otherwise unchanged.

## NoBo Corpus Workshop created today

NoBo now contains a back-room **CORPUS WORKSHOP**:
- Book open → **EDIT** → workshop on current book/chapter/page.
- Library → long-press **MORE** → **DATA** → workshop fallback.
- axes: **GUTS / NoBo** × **AIRLOCK / CORPUS**.
- AIRLOCK shows the complete genuine page with **⟦ AIRLOCK HERE ⟧** and edits the prepared socket paragraph.
- CORPUS edits genuine page text/chapter heading.
- **DONE / CANCEL** work in both modes.
- local working copy only; **IMPORT / EXPORT BOOK / RESET BOOK**.
- no direct GitHub write-back from the browser workshop.
- Pages branch `controls-refresh-2026-10-01` was fast-forwarded to current NoBo `main` so the live Pages URL serves the workshop.

NoBo rollback before workshop:
`rollback-pre-corpus-workshop-2026-10-02`.

## GUTS AIRLOCK PLACEMENT + RETENTION SWEEP — COMPLETED / MACHINE-QA PASSED

Stanley authorised a single-pass audit + repair + validation + promotion.

Scope:
- all 18 active GUTS books;
- prepared layer only;
- no repagination;
- no chapter restructuring;
- no Reader/state/covers changes;
- genuine `paragraphs` remain untouched.

Canonical repair logic:
- PLACEMENT defect: airlock at top, fewer than 12 genuine words before it, or heading-only material before it.
- RETENTION defect: run of 3+ consecutive eligible pages with pre-airlock depth within an 8-word band.
- historical carry targets used as repair compass:
  **28 / 48 / 68 / 38 / 58 words**.
- existing paragraph boundaries preferred.
- where necessary, only `force_paragraphs` was split at a sentence boundary.
- selected-chapter page-1 opener protection remains runtime law: the selected opener is genuine and does not arm/dwell.

Audit before repair:
- prepared pages scanned: **4,858**
- PLACEMENT flags: **552**
- RETENTION flags: **12**

Repair:
- prepared pages changed: **567**
- prepared-only sentence splits: **301**

Whole-corpus post-repair machine QA:
- 18/18 books parsed;
- PLACEMENT flags: **0**
- RETENTION flags: **0**
- bad/missing/multiple sockets: **0**
- `$$$` leaks into genuine text: **0**
- genuine token-order mismatches: **0**
- root/public corpus parity failures: **0**

Canonical detail:
`docs/checkpoints/2026-10-02_airlock-placement-retention-sweep.md`

## IMPORTANT: what remains unverified

The airlock sweep is **machine-QA PASSED and promoted**, but **new production phone/visual spot-check is still pending**.

Do **not** call the repaired prepared-corpus layer newly phone-frozen until Stanley visually checks a representative sample on the actual phone.

The previous runtime/state phone QA remains valid because runtime code was not changed.

## Exact next action for fresh ewe

1. Read Constitution + this latest handover update + `GUTS_CURRENT_STATE.md` + `docs/CURRENT_STATE.md`.
2. Read NoBo latest handover for Corpus Workshop state.
3. **Do not rerun or regenerate the airlock sweep.**
4. Guide Stanley through a small representative visual spot-check of repaired prepared pages / retention using the current live GUTS path.
5. If visual behaviour passes, record the repaired corpus as phone/visual PASS and freeze it.
6. If a defect appears, repair that specific defect only; rollback exists at `rollback-pre-airlock-sweep-2026-10-02`.

Wall-hit state is safe and recoverable.
