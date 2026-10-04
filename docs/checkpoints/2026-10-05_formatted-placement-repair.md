# GUTS formatted placement repair — 5 Oct 2026

**Authorisation:** backup, then execute directly to main; Stanley phone-checks afterwards.

## Rollback
`rollback-pre-formatted-repair-2026-10-05` @ `64dfc21877abff262f91b15a845dbb9db4660d9c`

## Reader STANdard promoted
- Georgia 15 CSS px
- line-height 1.45
- fixed 329 CSS px text measure
- centred

Only the fixed-measure CSS was ported into the current main Reader copies. No older runtime code was copied from the audit branch.

## Repair law
- Keep existing placement when it is not clearly defective.
- Repair socket starts above 120px or below 450px.
- Aim repaired sockets into 135–420px.
- Treat 3 consecutive prepared pages within a 32px rendered band as retention.
- Prefer a safe alternative more than 48px away from the recent repeated band.
- Rotate target heights instead of converging on one altitude.
- If paragraph boundaries cannot give a safe position, split the prepared `force_paragraphs` layer at a genuine sentence boundary.
- Genuine `paragraphs` are untouched.
- Socket prose itself is untouched.

## QA
All **4,858** prepared pages were processed.

- placement changes: **1,272**
- prepared sentence-boundary splits: **766**
- malformed or multi-socket pages: **0**
- implementation-estimator HIGH: **908 → 8**
- LOW >450: **208 → 2**
- below 540: **179 → 0**
- retention runs: **208 → 5**
- every active root/public corpus pair points to the same blob SHA

The canonical 4 Oct audit remains the authoritative pre-repair reference: **830 high / 219 low / 187 below 540 / 217 retention runs**. Its Georgia glyph-width model is not numerically identical to the conservative implementation estimator used for the execution pass, so the two pre-count sets must not be conflated.

## Safety
- exact pre-repair main is frozen at the rollback branch;
- genuine corpus arrays unchanged;
- no protocol/state/Worker/dwell/PAID/opener logic touched;
- current main Reader received only the approved fixed-measure CSS;
- root/public parity is explicit in the commit tree.

## Next action
**Stanley actual-phone visual QA.** If the result is wrong, roll back. If it is right, freeze this layer.
