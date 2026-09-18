# GUTS FORMAT 1 — NINE-BOOK MANIFEST

## Six new books
- AAM — A. A. Milne — The House at Pooh Corner
- AC — Agatha Christie — The Murder at the Vicarage
- DP — Dorothy Parker — Men I’m Not Married To
- DR — Damon Runyon — On Broadway
- JJ — James Joyce — Ulysses
- JT — James Thurber — My Life and Hard Times

## Three inherited and normalized from NoBo NoFo
- EH — Ernest Hemingway — A Farewell to Arms
- MT — Mark Twain — Adventures of Huckleberry Finn
- PGW — P. G. Wodehouse — Right Ho, Jeeves

The inherited books were taken from the NoBo NoFo field-refinement-v5 corpus.
Existing NoBo force_paragraphs and $$$ machinery were deliberately discarded before GUTS normalization.

All nine are now represented as GUTS FORMAT 1 paged text/JSON. The original six retain their checker PDFs. The inherited three were normalized directly in GitHub and therefore do not yet have binary checker PDFs.

Next engineering stage: nine-book socket/force-paragraph generation and GUTS reader integration.
