# GUTS — HANDOVER / START HERE

**Checkpoint: 5 October 2026 — formatted repair promoted; residual-location recovery wall-hit**

## READ FIRST — BEFORE TOUCHING ANYTHING

1. `GUTS_WORKFLOW_CONSTITUTION.md`
2. this handover: `GUTS_HANDOVER_2026-10-05.md`
3. `GUTS_CURRENT_STATE.md`
4. `docs/CURRENT_STATE.md`
5. `docs/checkpoints/2026-10-05_formatted-placement-repair.md`
6. `docs/checkpoints/2026-10-05_wall-hit-residual-location-recovery.md`
7. latest NoBo handover / README

**NoBo commands. GUTS executes. Read broadly. Act narrowly. Freeze wins.**

## Current canonical state

Formatted runtime/content repair anchor:
`99a4d422dc69ae6ba07e81f4ee25f07e2e081273`

The formatted repair is already on main. Later 5 Oct commits are documentation-only handover/current-state writes; do not mistake the newer docs head for another corpus/runtime change. Do not revert or re-repair casually.

Exact rollback:
`rollback-pre-formatted-repair-2026-10-05` @
`64dfc21877abff262f91b15a845dbb9db4660d9c`

Reader STANdard now on main:
**Georgia 15 CSS px / 1.45 line-height / fixed 329 CSS px centred text measure.**

Repair result:
- 4,858 prepared pages processed
- 1,272 placements changed
- 766 prepared sentence-boundary splits
- 0 malformed/multi-socket pages
- HIGH 908 → 8
- LOW 208 → 2
- below-540 179 → 0
- retention runs 208 → 5

Genuine `paragraphs` were untouched.

## What the previous ewe was doing when the wall hit

Stanley asked: **where exactly are the remaining 8 high, 2 low and 5 retention cases?**

The totals exist in the 5 Oct repair checkpoint, but the exact location list was not persisted.

A narrow read-only recovery against current main was started. It deliberately avoided giant diffs and any mutation.

Strong/provisional high candidates recovered:
- Ulysses ch16 *Eumaeus* p21
- Ulysses ch17 *Ithaca* p13
- Ulysses ch17 *Ithaca* p28
- Gormenghast ch19 p11
- Gormenghast ch29 p13
- Ulysses ch16 *Eumaeus* p35
- Ulysses ch13 *Nausicaa* p18
- Ulysses ch16 *Eumaeus* p46

Borderline candidate under the approximate reconstructed model:
- Gormenghast ch48 p1

Strong/provisional low candidates:
- Ulysses ch17 *Ithaca* p43
- Ulysses ch17 *Ithaca* p33

The **five retention runs remain unresolved**. The final calibration pass timed out.

Important: the exact implementation estimator was not found as a saved script. The provisional location recovery used the corpus plus a reconstructed Georgia-width model. Therefore do **not** promote the provisional list to canonical until reproduced faithfully.

## EXACT NEXT ACTION

Do **not** edit.

Do **not** rerun the old 2 Oct word-count sweep.

Do a narrow, read-only residual-location recovery from current `main`, returning only:
- the exact 8 HIGH locations;
- the exact 2 LOW locations;
- the exact 5 RETENTION runs.

Keep bandwidth low. Do not dump corpus text or giant diffs into chat.

After that, Stanley performs actual-phone visual QA. If accepted, freeze formatted placement. If rejected materially, rollback exists.


## SECOND WALL-HIT — practical scouting handover

Stanley clarified that the residual-location exercise is for **phone scouting**, not for mathematical completeness.

For HIGH scouting, the useful chapter map is now sufficient:
- Ulysses ch13 *Nausicaa*
- Ulysses ch16 *Eumaeus*
- Ulysses ch17 *Ithaca*
- Gormenghast ch19
- Gormenghast ch29

The two strong LOW cases are both Ulysses ch17 *Ithaca*.

Do not burn bandwidth resolving the borderline Gormenghast ch48 high candidate unless phone QA reveals a real defect.

The conversation then wall-hit while Stanley was asking for the equivalent **books + chapters only** for the five residual RETENTION runs.

Newest checkpoint:
`docs/checkpoints/2026-10-05_wall-hit-scouting-handover.md`

### EXACT NEXT ACTION

Read-only only.

Return just the **books and chapters containing the five residual RETENTION runs**.

Do not seek exact page runs unless trivial.
Do not edit corpus/runtime.
Do not rerun the old word-count sweep.
Keep output tiny.

After that Stanley will scout those chapters and the HIGH/LOW chapter set on the actual phone.


## CORE DESIGN LAW — PAGE PUMP

This is the governing illusion and outranks later implementation shorthand:

- **Every prepared page must begin mid-paragraph**, carrying genuine prose forward from the previous page. A fresh non-$$$ paragraph at page top is a defect because it exposes the preparation logic.
- Genuine prose words and order are inviolable.
- Prepared-layer paragraph boundaries are flexible camouflage: paragraphs may be run together or split at sensible sentence boundaries if needed, provided genuine word order is preserved.
- The previous page is the **pump** that creates the carry fragment for the next page.
- The $$$ airlock must appear later at a deliberately varied **rendered line depth**.
- Retention is therefore a **line-position** problem, not a word-count or pixel-model problem.
- Browser-rendered lines on the real target device are authoritative. Word-depth targets such as 28/48/68/38/58 are historical implementation aids only and must not override the design law.
- The intended chain is: **previous page creates carry → carry fixes next-page head → line pump shapes pre-socket depth → $$$ lands at a varied line.**

For future handovers: carry this section forward verbatim or link to it; do not bulk-reload historical audits unless a defect requires them.
