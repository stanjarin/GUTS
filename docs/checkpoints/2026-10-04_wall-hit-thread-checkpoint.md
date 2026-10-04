# GUTS wall-hit thread checkpoint — 4 Oct 2026

## Trigger
Stanley identified that the 2 Oct airlock-placement sweep had validated **unformatted word depth**, not actual rendered placement. This reopened the prepared-corpus visual QA question without reopening frozen runtime/state machinery.

## Key reasoning established in this thread

1. **Rendered wrapping, not raw word count, governs airlock vertical placement.**
2. Cross-device width variation is the major source of reflow; phone height is secondary.
3. Ordinary white space below text on taller phones is acceptable and not itself suspicious.
4. The Reader should preserve one standard typographic geometry across normal phones.
5. Approved Design STANdard for Reader text:
   - Georgia
   - 15 CSS px
   - line-height 1.45
   - fixed text measure **329 CSS px**
   - centred
   - wider phones gain side white space rather than wider lines
   - old/narrow fringe devices do not govern the design; zoom/fallback may handle them
6. Fixed text width and fixed font size are separate controls; both are intentionally locked.
7. Hardware pixel density/display resolution does not govern layout; CSS geometry does.
8. The useful audit unit is **rendered line/vertical position before `$$$`**, not raw characters or words.

## Work completed

Created work branch:
`fixed-measure-audit-2026-10-04`

Base:
`guts-browse-2026-10-03` @ `e0fe14f390d95122d5bf5d3bc70f8a562ef1f609`

Branch-only Reader update applied to:
- `index.html`
- `public/index.html`
- `public/project_library/books/browse/index.html`

Verified identical Reader blob:
`d893eed842cb827eda0bf4df0279047dcf63efb4`

No corpus files changed.

## Formatted audit completed

Canonical report on work branch:
`docs/checkpoints/2026-10-04_fixed-measure-formatted-airlock-audit.md`

Scope:
- 18 active books
- 4,858 prepared pages
- REPORT ONLY
- no corpus repair

Diagnostic result:
- TOO HIGH (<120px): 830
- LOW (>450px): 219
- below 540px reference: 187
- prepared chapter-opening sockets inventoried: 463
- maximal RETENTION runs within 32px rendered band: 217

Major findings:
- Runyon, Ulysses, Chandler, Jeeves and Parker have many high placements.
- Keys of the Kingdom is the major low-placement outlier.
- Rendered retention runs remain widespread despite the prior word-depth PASS.
- The old 2 Oct word-count law is therefore insufficient for visual camouflage.

## Safety

No production corpus repair was performed.
No Worker/state/protocol/opener/dwell/PAID machinery changed.
No NoBo change was made.
Production runtime remains protected.

## Fresh-ewe instruction

Read:
1. `GUTS_WORKFLOW_CONSTITUTION.md`
2. `GUTS_HANDOVER_2026-10-04.md`
3. `GUTS_CURRENT_STATE.md`
4. `docs/CURRENT_STATE.md`
5. the formatted audit report on `fixed-measure-audit-2026-10-04`
6. latest NoBo handover/README

Then:
- verify the work branch and three-reader parity;
- do **not** rerun the old word-count sweep;
- do **not** repair corpus yet;
- review the diagnostic thresholds / representative examples with Stanley;
- only after Stanley says GO, repair prepared-layer placement using rendered geometry;
- re-audit;
- finish with representative actual-phone visual QA before any promotion/freeze.
