# GUTS fixed-measure formatted airlock audit — 4 Oct 2026

Scope: all 18 active GUTS books / 4,858 prepared pages. REPORT ONLY. No corpus repair.

## Reader standard under test
Implemented branch-only on `fixed-measure-audit-2026-10-04`, based on `guts-browse-2026-10-03`.

- Georgia
- 15 CSS px
- line-height 1.45
- fixed text measure 329 CSS px
- text measure centred
- current iPhone 8 appearance preserved: 23 px effective side margin at 375 px viewport
- at 360 px viewport the same 329 px measure fits with ~15.5 px side margins
- narrower fringe devices may reflow / rely on user zoom; they do not govern the design

Implementation detail:
- Reader page horizontal padding changed from 23 px to 15 px.
- Reader paragraphs are capped at 329 px and centred.
- At 375 px viewport this yields the same 329 px text measure as before.
- Wider normal phones no longer widen/reflow the book text.

No corpus files were changed.

## Audit model
The audit uses the fixed 329 px measure and production typography to estimate formatted line wrapping and vertical socket start.

Important: this is a format-aware line-wrap simulation from the actual corpus and production CSS, not a literal Safari screenshot/raster capture. Georgia glyph widths are modelled, so a few pixels may vary by browser/font renderer. Gross placement and repeated-band findings are not marginal.

## Report thresholds
These thresholds are AUDIT FLAGS, not yet repair law.

- TOO HIGH: socket starts above 120 px from text-page top.
- LOW: socket starts below 450 px.
- BELOW I8 FIRST-SCREEN REFERENCE: socket starts below 540 px.
- RETENTION: 3+ consecutive prepared pages in one chapter with socket starts contained within a 32 px band (about 1.5 rendered lines).
- OPENER SOCKET: prepared page 1 contains a socket. Runtime selected-chapter opener protection remains law; this is an edge-case inventory, not automatically a defect.

## Whole-corpus result
- prepared pages audited: **4,858**
- TOO HIGH flags: **830**
- LOW flags: **219**
- BELOW I8 FIRST-SCREEN reference: **187**
- prepared chapter-opening sockets: **463**
- maximal RETENTION runs: **217**

The old word-count audit therefore does not predict formatted placement reliably enough.

## Book-by-book summary

| Book | Prepared pages | Too high | Low >450 | Below 540 | Opener sockets | Retention runs |
|---|---:|---:|---:|---:|---:|---:|
| House at Pooh Corner | 82 | 27 | 1 | 1 | 10 | 2 |
| Right Ho, Jeeves! | 228 | 68 | 0 | 0 | 23 | 10 |
| A Farewell to Arms | 215 | 50 | 7 | 2 | 41 | 5 |
| Huckleberry Finn | 270 | 51 | 9 | 3 | 43 | 7 |
| On Broadway | 742 | 165 | 0 | 0 | 47 | 46 |
| Murder at the Vicarage | 72 | 17 | 0 | 0 | 32 | 0 |
| Ulysses | 725 | 157 | 7 | 1 | 18 | 43 |
| My Life and Hard Times | 55 | 11 | 0 | 0 | 10 | 2 |
| Prime of Miss Jean Brodie | 113 | 39 | 0 | 0 | 6 | 6 |
| Farewell, My Lovely | 248 | 90 | 0 | 0 | 39 | 13 |
| Keys of the Kingdom | 329 | 0 | 187 | 179 | 6 | 0 |
| Kon-Tiki Expedition | 222 | 21 | 0 | 0 | 8 | 6 |
| Here Lies | 227 | 67 | 0 | 0 | 24 | 8 |
| Gormenghast | 608 | 2 | 3 | 1 | 61 | 59 |
| Best of S. J. Perelman | 257 | 9 | 2 | 0 | 49 | 5 |
| Third Policeman | 210 | 49 | 2 | 0 | 12 | 5 |
| Talented Mr. Ripley | 225 | 7 | 1 | 0 | 29 | 0 |
| King Ubu | 30 | 0 | 0 | 0 | 5 | 0 |

## Clear formatted examples

Retention examples:
- Jeeves, chapter 22, pages 14–16: ~81 px on all three.
- Farewell, chapter 35, pages 5–7: ~81 px on all three.
- Chandler, chapter 37, pages 2–7: six-page run clustered ~81–103 px.
- Runyon, chapter 11, pages 4–9: six-page run clustered ~81–103 px.
- Ulysses contains multiple runs of 3–7 pages in narrow formatted bands.
- Peake contains many repeated lower-page bands, commonly around ~255–320 px.

Low-placement concentration:
- Keys of the Kingdom is the major outlier: 187/329 below 450 px and 179/329 below the iPhone-8 first-screen reference of 540 px.
- Other books have relatively few extreme low placements.

High-placement concentration:
- Runyon 165, Ulysses 157, Chandler 90, Jeeves 68, Parker 67 are the largest high-placement counts.

## Interpretation
1. The fixed 329 px text measure materially solves the cross-device width/reflow problem for normal portrait phones.
2. The old 12-word / 28-48-68-38-58 word-depth rules are not sufficient as visual-placement law.
3. Top proximity is a genuine formatted problem in several books.
4. Retention of vision remains a genuine formatted problem despite the earlier machine PASS.
5. Keys is a different pathology: sockets are generally too deep, not too high.
6. Variable phone height is secondary. Ordinary white space below text is not treated as a defect.
7. No repair thresholds should be promoted until Stanley reviews this report / representative visual examples.

## Safety / state
- No corpus edits.
- No Reader/state/Worker/protocol changes other than the branch-only fixed text measure.
- `main` untouched.
- Existing runtime/opener/dwell/PAID behaviour untouched.
- Existing GUTS browse QA work retained as branch base.
