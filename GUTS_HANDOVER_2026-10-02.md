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

## 8. What is still open

The protocol itself is no longer the debugging job.

The remaining functional work is **promotion/deployment**:

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
