# GUTS — CURRENT STATE
Updated: 2026-09-30
Working branch: `prepage-refresh-2026-09-28`
Do not modify `main` during current experimentation.

## Production safety
- Production `main` remains frozen and untouched.
- Pre-integration rollback branch: `ten-book-pre-integration-backup-2026-09-30`.
- Current integrated working-branch commit: `c3f390ee20ba1b6beab11f0476fe857ec7922a30`.

## Frozen engine
Do not reopen without a specific observed defect:
- H2 PUSH / GUT PULL
- READY / ARMED / CLEAN
- Worker/KV transport
- exact `$$$` substitution
- selected-chapter opener protection
- 6-second dwell
- PAID persistence
- leave-no-trace behaviour
- existing Reader page-turn mechanics

## Ten-book expansion
Prepared and integrated on the working branch:
- Brodie
- Chandler
- Flann O’Brien
- Keys of the Kingdom
- Kon-Tiki
- Parker
- Peake
- Ripley
- Perelman
- Ubu

Corpus locations:
- `PERFORMANCE10/`
- `public/PERFORMANCE10/`

Batch records:
- `docs/corpus/TEN_BOOK_BUILD_REPORT_2026-09-30.md`
- `docs/corpus/TEN_BOOK_MANIFEST_v5.json`
- `docs/corpus/TEN_BOOK_QA_v5.json`

Ten new covers are present in repo root and `public/`.

One-shot importer completed successfully and is quarantined at:
`LEGACY_DO_NOT_DEPLOY/workflows/ten_book_import_once_2026-09-30.yml`

## Current air-lock method
The earlier synthetic "CREATE THE CHAPTER" concept did not become the active implementation for this batch.

Current practical classification:
- P = person/focal consciousness available
- NP = no person / scenic or authorial description
- D = dialogue/dramatic form
- C = anonymous cutaway escape hatch where needed

Rules:
- preserve genuine text order around insertion;
- avoid unnecessarily highlighting the force as a lexical object;
- use C only when useful;
- engineer awkward pages rather than silently excluding them;
- chapter/division pruning must be deliberate and documented.

## Keys
Source supplied as scan/OCR EPUB. Six major divisions retained:
- Beginning of the End
- Strange Vocation
- An Unsuccessful Curate
- The China Incident
- The Return
- End of the Beginning

OCR is imperfect but usable. One badly mangled source leaf was preserved rather than reconstructed.

## Shelf state
Target expanded shelf: **18 unique books total**.

The old visible carousel artwork still contains only the original 9 thumbnails.

A temporary working-branch code change renders covers dynamically for loop mechanics. This is not the intended final design.

## Carousel — OPEN
Missing prerequisite: the expanded baked carousel graphic.

Agreed artwork:
- one long strip;
- 18 unique thumbnails once each;
- normal gaps internally;
- half-gap at each outer edge so tiling creates one normal seam gap.

Agreed runtime:
- repeat strip internally as a buffer;
- begin in the middle copy;
- silently recenter by one strip-width near either edge;
- apparent endless spin in both directions;
- 18 tappable zones per cycle.

## NEXT ACTION

**YOUR JOB — Stanley**
Tomorrow, create and upload the expanded `Carousel.jpg` with 18 unique covers, normal internal gaps, and half-gap at each end.

**MY JOB — Kryten**
After upload:
1. replace the old carousel artwork;
2. restore the intended graphic-based carousel;
3. map all 18 clickable areas;
4. implement and verify endless bidirectional looping;
5. verify old and new books open correctly;
6. hand to Stanley for phone QA;
7. update canonical release state after PASS.

## 3058 OUT bootstrap protocol
When Stanley says **3058 out** in an established project thread:
1. Write/update a dated checkpoint under `docs/checkpoints/`.
2. Update this `docs/CURRENT_STATE.md` if canonical state changed.
3. Verify both GitHub writes.
4. Only after verification reply:
   `Thread details stored on GitHub`
   `Latitude 90° North out.`

If verification fails, report the failure and do not claim storage succeeded.
