# GUTS checkpoint — 2026-09-30

## Thread focus
Ten-book expansion, air-lock architecture, new covers, Keys source recovery, ten-book performance corpus build, GitHub integration, and discovery that the expanded carousel still requires a new baked graphic.

## Current production safety
- Production `main` remains untouched.
- All current work is on `prepage-refresh-2026-09-28`.
- Pre-integration rollback branch created:
  `ten-book-pre-integration-backup-2026-09-30`
- Current integrated working-branch commit:
  `c3f390ee20ba1b6beab11f0476fe857ec7922a30`
- Importer workflow completed successfully and quarantined itself under:
  `LEGACY_DO_NOT_DEPLOY/workflows/ten_book_import_once_2026-09-30.yml`

## Ten new covers
Stanley created and uploaded these ten 2048 × 4210 covers:
- BRODIE.jpg
- CHANDLER.jpg
- FLANN.jpg
- KEYS.jpg
- KON-TIKI.jpg
- PARKER.jpg
- PEAKE.jpg
- RIPLEY.jpg
- SJP.jpg
- UBU.jpg

They are present in repo root and copied into `public/`.

## Ten-book corpus batch
Prepared performance corpora now exist for:
1. Muriel Spark — *The Prime of Miss Jean Brodie*
2. Raymond Chandler — *Farewell, My Lovely*
3. Flann O’Brien — *The Third Policeman*
4. A. J. Cronin — *The Keys of the Kingdom*
5. Thor Heyerdahl — *The Kon-Tiki Expedition*
6. Dorothy Parker — *Here Lies: Collected Stories*
7. Mervyn Peake — *Gormenghast*
8. Patricia Highsmith — *The Talented Mr. Ripley*
9. S. J. Perelman — *The Best of S. J. Perelman*
10. Alfred Jarry — *Ubu Roi*

Canonical integrated locations:
- `PERFORMANCE10/*_performance.json`
- `public/PERFORMANCE10/*_performance.json`

Support records:
- `docs/corpus/TEN_BOOK_BUILD_REPORT_2026-09-30.md`
- `docs/corpus/TEN_BOOK_MANIFEST_v5.json`
- `docs/corpus/TEN_BOOK_QA_v5.json`

Machine QA passed during importer execution.

## Keys
Stanley supplied `Keys of the kingdom.epub` (~61 MB).

Recovered source structure:
- Beginning of the End
- Strange Vocation
- An Unsuccessful Curate
- The China Incident
- The Return
- End of the Beginning

The EPUB is scan/OCR based. OCR is imperfect but usable. One source leaf contains only a severely mangled fragment; the build preserves the surviving text rather than inventing Cronin.

Keys is now represented by:
`PERFORMANCE10/keys_performance.json`

## Air-lock direction actually used in the ten-book batch
The earlier "CREATE THE CHAPTER" synthetic-chapter idea did not become the active implementation in this pass.

Current practical architecture:
- classify page/story state as P / NP / D / C when needed;
- use character/narrator thought where a person is legitimately available;
- use dialogue for dramatic form where appropriate;
- use a short anonymous CUTAWAY only as an escape hatch when no legitimate consciousness is available;
- keep payload quoted where the chosen prose requires it;
- avoid explicitly spotlighting the force as "the word" where possible;
- preserve genuine prose order around the insertion;
- engineer awkward pages rather than silently excluding them;
- deliberate chapter/division cuts remain a documented performance-editorial decision, not an accidental deletion.

## Current shelf count
Existing active shelf before expansion: 8 genuine runners plus Parker placeholder/control = 9 visible books.

New batch adds 10 prepared titles, but new Parker replaces the old Parker slot.

Target visible shelf after proper carousel artwork:
**18 unique books total.**

## Critical carousel correction
The old visible carousel is a baked graphic:
`Carousel.jpg`

It currently contains only the original 9 thumbnails.

During integration, branch code was temporarily changed to render individual cover images dynamically and repeat them for looping. That is mechanically wired but is **not the intended visual design**.

Stanley correctly identified the missing prerequisite:
**the expanded baked carousel artwork does not yet exist.**

Therefore:
- refreshing the old deployed page cannot show the new titles;
- the new books cannot appear in the intended carousel until Stanley supplies the new long graphic;
- do not treat the current dynamic-cover carousel rewrite as finished design.

## Infinite carousel design agreed
Stanley will create one long graphic containing the **18 unique covers once each**.

Spacing rule:
- normal full gaps between internal thumbnails;
- **half-space at each outer end**;
- when tiled, the two half-spaces meet to form one normal gap at the seam.

Runtime looping plan:
- repeat the one-strip graphic internally three times as a buffer;
- start in the middle copy;
- silently shift scroll position by exactly one strip-width near either end;
- spectator experience remains endlessly spinnable in both directions;
- map 18 tap zones per cycle to the corresponding books.

Three copies are only the implementation buffer; visible behaviour is infinite.

## Next action
Tomorrow:

**YOUR JOB — Stanley**
Create the new long `Carousel.jpg`:
- 18 unique thumbnails once each;
- normal gaps internally;
- half-gap at each end;
- same visual house style as the current Gutenberg carousel.

**MY JOB — Kryten**
After upload:
1. replace the old carousel artwork on the working branch;
2. restore the intended graphic-based carousel instead of the temporary dynamic-cover renderer;
3. map all 18 tappable zones;
4. implement/verify seamless endless looping in both directions;
5. verify old + new books open correctly;
6. phone-QA with Stanley;
7. only after PASS update canonical release state.

## 3058 OUT protocol
When Stanley says **3058 out** in an established project thread:
1. Write/update a dated checkpoint under `docs/checkpoints/`.
2. Update `docs/CURRENT_STATE.md` if canonical state changed.
3. Verify both GitHub writes.
4. Only after verification reply:
   `Thread details stored on GitHub`
   `Latitude 90° North out.`

If verification fails, report the failure instead.
