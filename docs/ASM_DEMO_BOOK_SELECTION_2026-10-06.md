# ASM Demo Book Selection — 6 October 2026

Purpose: choose the safest single book to perfect and freeze for the ASM demonstration on Monday 12 October 2026.

This is a cheap structural comparison only. No corpus was modified.

## Selection criteria

Priority:
1. legal raw donor availability under the new boundary law;
2. conventional punctuation / sentence completion;
3. low structural/OCR pathology;
4. manageable whole-book size before Monday;
5. enough prepared pages to demonstrate convincing freedom.

"Raw boundary eligibility" means the donor text contains at least one structurally legal mid-sentence cut followed later by a proper sentence completion, before rendered-line/spacing optimisation is considered.

## Strongest candidates

| Book | Pages | Forceable after chapter openers | Raw boundary eligibility | Paragraphs ending terminally | Lowercase paragraph starts | Notes |
|---|---:|---:|---:|---:|---:|---|
| **My Life and Hard Times — Thurber** | **55** | **45** | **100%** | **92.4%** | **0** | Smallest clean conventional-prose candidate; ideal Monday reference book |
| The Prime of Miss Jean Brodie | 113 | 107 | 100% | 90.7% | 41 | Compact but more prepared-boundary oddity |
| The Third Policeman | 210 | 198 | 100% | 97.6% | 1 | Extremely clean; larger whole-book job |
| Here Lies — Dorothy Parker | 227 | 203 | 100% | 97.0% | 0 | Very clean; roughly 4x Thurber workload |
| The Talented Mr. Ripley | 225 | 196 | 100% | 95.8% | 10 | Clean conventional prose; larger |
| Farewell, My Lovely | 248 | 209 | 100% | 96.7% | 0 | Clean conventional prose; larger |
| Right Ho, Jeeves | 228 | 205 | 100% | 91.4% | 124 | Legally promising but more existing split structure |

## Rejected as Monday first choice

- **King Ubu** is only 30 pages and structurally clean, but dramatic/script form is not the best reference implementation for ordinary book prose.
- **The Murder at the Vicarage** is only 72 pages, but 29 of 32 chapters are three pages or fewer in the current corpus, creating disproportionate chapter-edge/opener complications.
- **Ulysses** already shows raw boundary failures and extensive pathological structure.
- **Gormenghast** is large and has known difficult structure.
- **Kon-Tiki / Pooh / Perelman** show substantially more irregular paragraph-boundary structure than the leading candidates.
- **Runyon** is far too large for the Monday reference-book objective.

## Decision

**Book Zero / ASM demonstration candidate: James Thurber, _My Life and Hard Times_.**

Reasons:
- only 55 pages;
- 45 forceable post-opener pages;
- 100% raw donor eligibility under the new boundary law;
- zero lowercase paragraph starts in the current genuine corpus;
- conventional prose and punctuation;
- enough pages/chapters to demonstrate free-looking choice;
- small enough to permit whole-book machine QA plus meaningful phone QA before Monday.

Runner-up if Thurber reveals an unexpected rendered-layout defect:
**The Third Policeman**.

## Important limitation

This selection pass proves textual/structural suitability only. It does **not** claim the 55-page book already passes rendered-line placement, retention, page-head or airlock phone QA.

Next:
1. create protected Thurber demo branch from current main;
2. implement/finalise the one-book deterministic build there;
3. run whole-book machine QA;
4. Stanley phone QA;
5. freeze the demo SHA.
