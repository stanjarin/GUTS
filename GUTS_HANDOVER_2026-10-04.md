# GUTS — HANDOVER / START HERE

**Checkpoint: 4 October 2026 — fixed-measure formatted-airlock audit complete; wall-hit handover**

## 0. Read broadly, act narrowly

Before changing anything:
1. read `GUTS_WORKFLOW_CONSTITUTION.md`;
2. read this handover;
3. read `GUTS_CURRENT_STATE.md`;
4. read `docs/CURRENT_STATE.md`;
5. read `docs/checkpoints/2026-10-04_fixed-measure-formatted-airlock-audit.md` from branch `fixed-measure-audit-2026-10-04`;
6. read the latest NoBo handover / README for the cross-system contract.

**NoBo commands. GUTS executes.**

Do not begin by editing.

## 1. Production safety

No production corpus repair was performed on 4 Oct.

Before this docs-only handover work, GUTS `main` runtime/content head was:
`ea75ce37e3f931fd6b8aaeb2226d037f3d3618ef`

The 4 Oct fixed-measure/audit work is isolated on:

`fixed-measure-audit-2026-10-04`

That branch was based on:

`guts-browse-2026-10-03`

whose base/head at branch-off was:
`e0fe14f390d95122d5bf5d3bc70f8a562ef1f609`

Do not promote the fixed-measure Reader or repair corpus until the report is reviewed and Stanley explicitly authorises the next step.

## 2. Why the old airlock PASS was reopened

The 2 Oct sweep audited airlock position structurally by **word depth**:
- minimum genuine words before socket;
- carry targets 28 / 48 / 68 / 38 / 58;
- retention based on word-depth bands.

That pass was mechanically sound for those rules, but Stanley identified the missing visual variable:

**formatted line wrapping governs actual vertical placement.**

The old word-count PASS therefore does not prove visual placement.

## 3. New Design STANdard for Reader geometry

Stanley approved preserving the current iPhone-8 Reader typography as the cross-device standard:

- Georgia
- 15 CSS px
- line-height 1.45
- **fixed text measure 329 CSS px**
- centred on normal portrait phones
- wider phones get wider white side margins rather than wider text/reflow
- display pixel density/resolution is irrelevant to layout because CSS pixels govern geometry
- old/narrow fringe phones do not govern the design; pinch/zoom or narrow fallback may handle them
- variable phone height is secondary; ordinary white below short text is not a defect

Key distinction:
**fixed width does not itself fix font size. We deliberately fix both width and typography.**

## 4. Branch-only implementation completed

On `fixed-measure-audit-2026-10-04`, the three Reader copies were changed identically:

- `index.html`
- `public/index.html`
- `public/project_library/books/browse/index.html`

Verified blob for all three after the change:
`d893eed842cb827eda0bf4df0279047dcf63efb4`

Verified branch CSS includes:
- Georgia 15px / 1.45
- paragraph width 329px
- max-width 100%
- centred text measure

At 375px viewport, this preserves the existing 329px text measure.
At wider normal phones, text no longer widens/reflows.

No corpus files were changed.

## 5. New formatted audit — COMPLETE, REPORT ONLY

Canonical report:

`docs/checkpoints/2026-10-04_fixed-measure-formatted-airlock-audit.md`

on branch:

`fixed-measure-audit-2026-10-04`

Scope:
- all 18 active GUTS books
- all 4,858 prepared pages
- fixed 329px text measure
- production typography
- format-aware line-wrap / vertical socket estimate
- **no repair**

Audit flags used for report:
- TOO HIGH: socket starts above 120px from text-page top
- LOW: socket starts below 450px
- BELOW I8 FIRST-SCREEN reference: below 540px
- RETENTION: 3+ consecutive prepared pages in one chapter whose socket starts stay within a 32px band (~1.5 rendered lines)
- OPENER SOCKET: prepared page 1 contains a socket; inventory only because selected-chapter opener protection remains runtime law

Whole-corpus result:
- prepared pages: **4,858**
- TOO HIGH: **830**
- LOW >450: **219**
- BELOW 540: **187**
- prepared chapter-opening sockets: **463**
- maximal RETENTION runs: **217**

Important concentrations:
- Runyon: 165 TOO HIGH
- Ulysses: 157 TOO HIGH
- Chandler: 90 TOO HIGH
- Jeeves: 68 TOO HIGH
- Parker: 67 TOO HIGH
- Keys of the Kingdom: 187 LOW >450; 179 below 540
- Peake: many repeated lower-page retention bands

Clear formatted retention examples include:
- Jeeves ch 22 pp 14–16: ~81px three times
- Farewell ch 35 pp 5–7: ~81px three times
- Chandler ch 37 pp 2–7: six-page run ~81–103px
- Runyon ch 11 pp 4–9: six-page run ~81–103px

## 6. Interpretation

The fixed 329px measure makes cross-device width behaviour tractable.

The old word-depth rules are no longer sufficient as visual-placement law.

Two genuine formatted pathologies now exist:
1. **top proximity / repeated high placement**;
2. **retention of vision in rendered line bands**.

Keys of the Kingdom is a separate low-placement outlier.

Do not treat the report thresholds as final repair law yet. They are diagnostic flags.

## 7. What is still frozen

Do not reopen without a specific defect:
- state architecture / READY / ARMED / local PAID
- Worker/KV transport
- exact `$$$` substitution
- selected-chapter opener protection
- 6-second dwell
- cover / carousel / landing behaviour
- existing production domain journey
- NoBo control contract

The 4 Oct work did not change any of those.

## 8. NoBo / BR+ context

Operationally:
- NoBo remains controller + workshop.
- BR+ launches the GUTS browse/evaluation route.
- DATA edits GUTS or NoBo locally in the Corpus Workshop.
- DONE saves local workshop copy only.
- EXPORT BOOK does not make a book live.
- To make a corrected book live later, replace the proper GUTS corpus JSON, preserve root/public parity, machine-QA, then BR+ verify.

No NoBo change was made in this 4 Oct pass.

## 9. EXACT NEXT ACTION — FRESH EWE

1. Read the files listed in section 0.
2. Confirm branch `fixed-measure-audit-2026-10-04` still contains the three identical Reader copies and the 4 Oct audit report.
3. **Do not rerun the old 2 Oct word-count sweep.**
4. **Do not repair corpus yet.**
5. Present / review the formatted audit with Stanley and settle the actual visual safe bands / repair law.
6. Once Stanley says GO, repair prepared-layer placement only, against rendered-line geometry rather than raw word count.
7. Re-run the fixed-measure formatted audit.
8. Then do a small actual-phone visual QA sample before promotion/freeze.

The wall-hit state is safe and recoverable.
