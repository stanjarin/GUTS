# GUTS wall-hit checkpoint — 5 Oct 2026

## Status at wall

Current `main`:
`99a4d422dc69ae6ba07e81f4ee25f07e2e081273`
— **Repair formatted airlock placement under fixed Reader measure**

Exact pre-repair rollback:
`rollback-pre-formatted-repair-2026-10-05` @
`64dfc21877abff262f91b15a845dbb9db4660d9c`

The formatted placement repair is already promoted to `main`.

## Promoted Reader STANdard

- Georgia 15 CSS px
- line-height 1.45
- fixed 329 CSS px text measure
- centred

## Repair result already canonical

All 4,858 prepared pages processed.

- placement changes: 1,272
- prepared sentence-boundary splits: 766
- malformed/multi-socket pages: 0
- implementation-estimator HIGH: 908 → 8
- LOW >450: 208 → 2
- below 540: 179 → 0
- retention runs: 208 → 5
- genuine `paragraphs` untouched
- root/public corpus parity passed

Repair law remains:
- repair above 120px or below 450px;
- aim repaired sockets into 135–420px;
- break 3-page retention bands within 32px where possible;
- permit sentence-boundary splits in prepared `force_paragraphs` only;
- vary target heights.

## Residual-location recovery attempted in wall-hit thread

Stanley asked for the exact locations of the remaining **8 high / 2 low / 5 retention** cases.

The original repair checkpoint stored the totals, but **did not store the location list**.

A narrow read-only recovery was started against current `main`. No corpus/runtime files were edited.

### Strong high candidates recovered before wall

Five zero-prose / socket-first pages were found:
- Ulysses — ch 16 *Eumaeus* — p 21
- Ulysses — ch 17 *Ithaca* — p 13
- Ulysses — ch 17 *Ithaca* — p 28
- Gormenghast — ch 19 — p 11
- Gormenghast — ch 29 — p 13

Very shallow Ulysses candidates:
- Ulysses — ch 16 *Eumaeus* — p 35
- Ulysses — ch 13 *Nausicaa* — p 18
- Ulysses — ch 16 *Eumaeus* — p 46

A further borderline high candidate appeared under the approximate reconstruction:
- Gormenghast — ch 48 — p 1

**Important:** the exact implementation estimator was not persisted as a reusable script. The wall-hit reconstruction used the current corpus plus an approximate Georgia width model and had not yet been perfectly calibrated when the session hit the wall. Therefore the eight-item high set above is **provisional**, not yet canonical.

### Low cases — strong candidates

The two clear low outliers recovered are both in Ulysses, ch 17 *Ithaca*:
- p 43 — extremely deep pre-socket paragraph
- p 33 — long moon/woman paragraph before socket

These match the expected residual count of two under the narrow reconstruction, but should still be re-confirmed with the exact/faithful estimator before being called canonical.

### Retention runs

The five residual retention runs were **not safely identified before wall-hit**.

A final calibration pass intended only to isolate those five runs timed out. Do not guess them from the partial output.

## Safety / next action

No changes were made during residual-location recovery.

Fresh ewe should:
1. read constitution + 5 Oct handover/current state;
2. treat the formatted repair on `main` as the current production state;
3. **do not rerun the old word-count sweep**;
4. **do not repair anything** merely to locate residuals;
5. recover/reproduce the implementation placement estimator as faithfully and cheaply as possible;
6. return only the exact **8 high / 2 low / 5 retention** locations;
7. then Stanley can actual-phone check those residuals and representative repaired pages;
8. if phone QA passes, freeze formatted placement;
9. if it fails materially, rollback remains available.

NoBo commands. GUTS executes. Read broadly. Act narrowly. Freeze wins.
