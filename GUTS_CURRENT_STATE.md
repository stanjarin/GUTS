# GUTS — CURRENT STATE

**Authoritative checkpoint: 2 October 2026**

## Read first

1. `GUTS_WORKFLOW_CONSTITUTION.md`
2. `GUTS_HANDOVER_2026-10-02.md`
3. this file
4. `docs/CURRENT_STATE.md`
5. relevant NoBo handover/README

Principle: **Read broadly, act narrowly.**

## Production anchors

- GUTS production `main`: `aef68707b1ad031eab16ae1efbecce5733630186`
- Current QA-passed GUTS branch: `protocol-cleanup-2026-10-01`
- Paired QA-passed NoBo branch: `controls-refresh-2026-10-01`
- NoBo production `main`: `93d4ade5fee65d9931c5c6ad1b1b25cad8c18235`

Promotion completed on GitHub on 2 October 2026. External domain verification and the final phone smoke test remain pending.

## Canonical architecture

**NoBo commands. GUTS executes.**

Independent axes:
- MAGIC: READY → ARMED → local PAID
- VISIBILITY: SHW ↔ HIDD
- AUTH: valid / invalid

Visibility/auth actions must not mutate magic state.

### Remote state
Live remote protocol is only:
- READY
- ARMED (+ word)

CLEAN is historical and not part of the current live NoBo↔GUTS protocol.

### GUTS local execution
Frozen/passed behaviour:
- exact `$$$` substitution;
- selected chapter opener protection;
- 6-second dwell;
- local PAID/frozen page;
- remote READY clears local ARMED/PAID on a newer revision;
- remote ARMED does not overwrite a PAID reader until reset.

## Protocol cleanup — PASSED

On `protocol-cleanup-2026-10-01`:
- non-mutating ARM PIN validation endpoint added;
- performer state accepts READY/ARMED only;
- SHW/HIDD mode mutation is independent of magic state;
- rehearsal authorisation is cookie/auth only;
- default mode when absent is REHEARSAL/HIDD;
- reader root/public copies consume READY/ARMED only;
- machine checks passed.

## Phone QA — PASSED 2 Oct 2026

Actual iPhone results:
- [WORD] survives all books;
- [WORD] survives HIDD ↔ SHW;
- [WORD] survives refresh/new GUTS request;
- prepared page + 6+ seconds + departure reaches PAID;
- PAID persists correctly;
- NoBo RSET sends READY;
- after RSET, [WORD] is gone from prepared pages.

Full passed chain:

**RSET → READY → ARM [WORD] → GUTS pull → prepared page → 6s dwell → PAID → persistence → RSET/READY → cleared**

## PIN vocabulary

Existing user-facing names:
- ARM PIN = `arm`
- SHOW PIN = `show`

Do not introduce a third PIN term.

## Test deployment

NoBo:
`https://stanjarin.github.io/NoBoNoFo/`

GUTS protocol preview:
`https://protocol-cleanup-2026-10-01-guts.stanjarin.workers.dev/`

Rehearsal auth:
`https://protocol-cleanup-2026-10-01-guts.stanjarin.workers.dev/performer/rehearsal`

NoBo QA branch deliberately points to this GUTS preview until promotion.

## Frozen visual/corpus state

Do not reopen without a specific observed defect:
- 18-book shelf/corpus;
- 18-cover baked carousel and endless loop behaviour;
- landing/pre-page artwork;
- Reader/nav;
- page flicks;
- chapter/cover behaviour;
- exact force substitution;
- opener protection;
- 6-second dwell;
- PAID;
- current cover treatment;
- deliberate ugly cover back-arrow overlap (STET).

Deferred cosmetic work remains in `docs/COSMETICS_LATER.md`.

## Domain plan

Primary intended production spectator domain:
`ebooks.fyi`

Spare:
`ebks.fyi`

Attach as a Cloudflare custom domain to the production Worker. Avoid a visible redirect exposing `gutenbrg.com`.

## Open work

The protocol is no longer an open debugging problem.

Completed on GitHub:
1. rollback branches created and recorded;
2. GUTS tested work promoted to `main`;
3. NoBo tested work promoted to `main`;
4. NoBo production controller repointed to `https://ebooks.fyi`.

Still pending:
1. externally verify that `ebooks.fyi` is attached to the production GUTS Worker and serving the promoted build;
2. run one final production phone smoke test:
   **RSET → ARM → GUTS → PAID → RSET**;
3. freeze release.

## NEXT ACTION

**Fresh ewe:** GitHub promotion is complete. Verify `ebooks.fyi`, then request only the final phone smoke test. Do not reopen corpus/Reader/cosmetics.

**Stanley:** final phone smoke test only after production-domain verification.

## Promotion anchors — 2 October 2026

- phone-QA frozen GUTS anchor: `qa-pass-2026-10-02` @ `59b6e1015cc7ff8bc51bedbd1a874d974b6710b5`
- pre-promotion GUTS rollback: `rollback-pre-promotion-2026-10-02` @ `aef68707b1ad031eab16ae1efbecce5733630186`
- promotion scope remains deployment only; frozen corpus/Reader/cosmetics are not reopened.
