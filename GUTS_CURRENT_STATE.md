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

- GUTS production runtime anchor: `4e6c5c4835fb858ba10409962af694657d921d77` (`release-2026-10-02-production-pass`)
- Current QA-passed GUTS branch: `protocol-cleanup-2026-10-01`
- Paired QA-passed NoBo branch: `controls-refresh-2026-10-01`
- NoBo production runtime anchor: `6dcd4b33429788f413f6fd80e503f08553eda0cd` (`release-2026-10-02-production-pass`)

Production promotion, domain attachment, and final phone smoke QA all PASSED on 2 October 2026. Release is frozen.

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

## Production deployment

NoBo:
`https://stanjarin.github.io/NoBoNoFo/`

GUTS spectator domain:
`https://ebooks.fyi`

`ebooks.fyi` is connected to Cloudflare and attached to the production `guts` Worker.

The temporary protocol-preview URL is retained only as historical QA evidence; production NoBo now points to `https://ebooks.fyi`.

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

## Domain state

Primary production spectator domain:
`ebooks.fyi` — **LIVE / PASSED**

Spare:
`ebks.fyi`

`ebooks.fyi` is delegated to Cloudflare and attached directly as a custom domain to the production GUTS Worker. No visible redirect exposes `gutenbrg.com`.

## Release status

**PRODUCTION RELEASE PASSED / FROZEN — 2 October 2026**

Completed:
1. rollback branches created and recorded;
2. GUTS tested work promoted to `main`;
3. NoBo tested work promoted to `main`;
4. NoBo production controller repointed to `https://ebooks.fyi`;
5. `ebooks.fyi` delegated to Cloudflare and attached to production GUTS;
6. live production domain verified;
7. final actual-phone smoke test PASSED:
   **RSET → ARM → GUTS → prepared page → 6+ sec → PAID persistence → RSET → cleared**.

## NEXT ACTION

No functional work is open. Return only to explicitly deferred cosmetics/editorial work when desired. Do not reopen frozen corpus, Reader, protocol, state architecture, covers, carousel, or deployment without a specific observed defect.

## Promotion anchors — 2 October 2026

- phone-QA frozen GUTS anchor: `qa-pass-2026-10-02` @ `59b6e1015cc7ff8bc51bedbd1a874d974b6710b5`
- pre-promotion GUTS rollback: `rollback-pre-promotion-2026-10-02` @ `aef68707b1ad031eab16ae1efbecce5733630186`
- promotion scope remains deployment only; frozen corpus/Reader/cosmetics are not reopened.


## Final production pass — 2 October 2026

Stanley reported **“All systems nominal!”** after the final production phone smoke test against `https://ebooks.fyi`.

Frozen production runtime anchors:
- GUTS: `release-2026-10-02-production-pass` @ `4e6c5c4835fb858ba10409962af694657d921d77`
- NoBo: `release-2026-10-02-production-pass` @ `6dcd4b33429788f413f6fd80e503f08553eda0cd`

The release is closed.

## Airlock placement + retention sweep — 2 Oct 2026

A full 18-book prepared-corpus sweep was completed on `airlock-sweep-2026-10-02`.

- 4,858 prepared pages scanned;
- 552 PLACEMENT defects and 12 RETENTION defects identified before repair;
- 567 prepared pages changed;
- genuine `paragraphs` unchanged;
- no Reader/state/cover/chapter/repagination changes;
- post-repair machine QA: 0 placement flags, 0 retention flags, 0 socket failures/leaks, 0 genuine token-order mismatches, root/public parity PASS.

Rollback: `rollback-pre-airlock-sweep-2026-10-02` @ `6113a1a7bac25f389ddb5444dca4d7b4c775b459`.

Promotion was explicitly authorised after machine QA. Phone/visual spot-check remains pending; do not call this layer newly phone-frozen until that check is done.


## Immediate handover state — wall-hit, 2 Oct 2026

Latest prepared-corpus work:
- full 18-book AIRLOCK PLACEMENT + RETENTION sweep is complete, promoted and machine-QA PASSED;
- rollback: `rollback-pre-airlock-sweep-2026-10-02` @ `6113a1a7bac25f389ddb5444dca4d7b4c775b459`;
- detailed checkpoint: `docs/checkpoints/2026-10-02_airlock-placement-retention-sweep.md`;
- no runtime/Reader/state/cover/chapter/repagination change;
- **visual/phone spot-check of repaired prepared pages remains pending**.

Current public journey:
- `https://ebooks.fyi` = HTTPS entry / Resources pre-page;
- `https://www3.library.gutenbrg.com/project_library/books/browse/` = HTTPS GUTS library/carousel/Reader;
- Safari may collapse the long path to `www3.library.gutenbrg.com`; accepted.

Carousel first-arrival start is now **Jean Brodie**; return-to-jump-point remains intact.

Paired NoBo now has the back-room Corpus Workshop via reader EDIT or Library MORE → DATA. Read the latest NoBo handover before workshop changes.

**NEXT ACTION:** representative phone/visual spot-check of repaired GUTS airlock placement/retention. Do not rerun the sweep.
