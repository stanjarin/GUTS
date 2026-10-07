# GUTS thread checkpoint — 7 Oct 2026 — factory autopilot

## Scope

Durable continuation checkpoint for the GUTS factory thread.

## Naming convention

In GUTS-building / engineering threads, call the machinery **GUTS**.

Reserve **NoBo NoFo** for the performance/effect vocabulary. Do not blur the two in engineering discussion unless needed for cross-system context.

## Keys result

Keys was used as a stress-test book.

Phone judgement:
- the three stubborn adjacent-retention pairs were visually acceptable;
- broader repetition/retention existed mostly in the lower half / below the normal attention zone and did not perceptually jump;
- machine sentence-start warnings did not correspond to a meaningful phone-visible defect in the sampled pages;
- OCR bloops, embedded KEYS titles, short pages and miscellaneous Gutenberg editorial uglies are explicitly deferred.

Operational conclusion:
**KEYS — provisional phone PASS / editorial uglies deferred.**

Key lesson:
**retention is positional and attention-zone dependent, not merely textual duplication.**

Gutenberg-origin formatting/OCR defects are not factory blockers unless they reveal the method.

Checkpoint:
`docs/checkpoints/2026-10-07_keys-phone-judgement.md`

## UBU result

UBU single-book factory run produced:
- 25 forceable prepared pages repaired;
- 30 pages changed;
- 23 exact target hits;
- 0 unresolved pages;
- 0 spacing violations;
- 0 retention-window flags;
- 0 source/hash/parity failures;
- 0 page-head mid-sentence failures;
- 0 opener failures;
- 2 raw adjacent textual overlaps:
  - ch4 p2/p3
  - ch5 p5/p6

Stanley phone-inspected both and judged them visually acceptable.

Important procedural simplification discussed:
**“Just jump to the first new paragraph.”**

This makes page-top carry-over text scenery rather than the operational target. A page beginning with a complete sentence is not automatically method-revealing if the spectator is directed to the first new paragraph. Treat this as a performance/procedural simplification to test before globally rewriting factory law.

## Factory architecture breakthrough

The stop-start human activation loop was identified as the real bottleneck.

Old loop:
GitHub stops → Stanley wakes ChatGPT → ChatGPT inspects → ChatGPT triggers next job → repeat.

New architecture:
**event-driven factory autopilot with a human gate only where human judgement is genuinely required.**

Current safe branch:
`factory-autopilot-2026-10-07`

Design:
- run remaining books in parallel using a GitHub Actions matrix;
- each book runs the generic single-book factory engine independently;
- retain per-book candidate + QA report;
- consolidate all outputs automatically;
- deploy one combined temporary phone preview automatically;
- stop only at consolidated Stanley phone QA.

Production `main`, `ebooks.fyi`, and the frozen live system remain untouched.

## Parallel factory run

Generic engine:
`tools/factory_book.py`

Workflow:
`.github/workflows/factory-autopilot-2026-10-07.yml`

Jeeves is frozen and excluded.
Keys and UBU were already phone-reviewed and are excluded from regeneration.

The remaining 15 books are running in parallel.

Known fast completions observed during this thread included:
- AAM
- Brodie
- AC
- JT

Later, 12 were reported complete with 5 laggards still running:
- Runyon
- Joyce
- Kon-Tiki
- Peake
- Ripley

The point of the parallel architecture is that total elapsed time is governed mainly by the slowest books, not the sum of all per-book runtimes.

## GitHub Actions warning

All jobs show a yellow Node 20 deprecation warning for standard GitHub Actions such as checkout/setup/upload-artifact being forced onto Node 24.

This is platform plumbing noise, not a GUTS defect, and is not currently a blocker.

## Human / machine authority

Keep the current hierarchy:
1. canonical genuine source / paragraphs;
2. prepared force layer;
3. actual phone appearance;
4. machine diagnostics.

Machine metrics narrow suspects.
Phone appearance decides visual acceptability.

## Immediate next action

Do not manually prod individual books.

Let the current factory autopilot run continue to completion.

When the consolidated preview is ready, Stanley performs one human phone-QA pass on the surfaced suspects.

Do not touch production main.
