# GUTS TEN-BOOK PERFORMANCE CORPUS v5

Corpus-stage package only. Reader, Worker, Cloudflare, and production `main` were not modified.

## Batch result

- **The Prime of Miss Jean Brodie** — 6 divisions; 113 prepared pages; QA PASS.
- **Farewell, My Lovely** — 39 divisions; 248 prepared pages; QA PASS.
- **The Keys of the Kingdom** — 6 divisions; 329 prepared pages; QA PASS.
- **The Kon-Tiki Expedition** — 8 divisions; 222 prepared pages; QA PASS.
- **Here Lies: Collected Stories of Dorothy Parker** — 24 divisions; 227 prepared pages; QA PASS.
- **Gormenghast** — 61 divisions; 608 prepared pages; QA PASS.
- **The Best of S. J. Perelman** — 49 divisions; 257 prepared pages; QA PASS.
- **The Third Policeman** — 12 divisions; 210 prepared pages; QA PASS.
- **The Talented Mr. Ripley** — 29 divisions; 225 prepared pages; QA PASS.
- **King Ubu (Ubu Roi)** — 5 divisions; 30 prepared pages; QA PASS.

## Keys
- Source: user-supplied `Keys of the kingdom.epub`.
- Six source divisions preserved from the source Contents.
- OCR text lightly normalized and repaginated at sentence boundaries; no attempt was made to silently rewrite uncertain OCR into guessed prose.
- Blank/section-title scan leaves omitted; substantive OCR text is repaginated continuously, so corrupt scan boundaries do not become bad Reader pages.
- One source defect remains documented: scan leaf 163 contains only a short OCR fragment in the supplied EPUB; it is preserved in sequence rather than invented.
- Airlock: `Quite suddenly he thought of “$$$”. Why it should have come to him then he could not imagine. He let the thought linger for a moment, then put it from him.`

## QA invariants
- exactly one `$$$` in each prepared force page;
- no `$$$` in genuine/source paragraphs;
- payload is quoted;
- genuine paragraphs remain in source order around the airlock;
- airlock is not the first paragraph of a prepared page;

**BATCH QA: PASS**
