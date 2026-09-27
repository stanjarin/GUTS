# GUTS — CURRENT STATE

**Authoritative checkpoint: 27 September 2026 — emergency handover**

Read `GUTS_EMERGENCY_HANDOVER_2026-09-27.md` first, then this file, and `GUTS_OHS_RECOVERY.md` before any write/deploy action. `GUTS_HANDOVER_2026-09-27.md` remains the detailed architecture manual beneath the later emergency overlay.

## Branch / production truth

- Production branch: `main` — **DO NOT MODIFY during this audit**.
- Verified `main` head at handover: `b662978d1de67304cc96ad78e3c224f2d2b75533` — `Install authoritative Contents tables`.
- Working branch: `contents-repair`.
- `contents-repair` was created from that current main.
- First branch checkpoint commit: `c7b75c6f365cf5a7723256aa8ad84c05976e6a5a` — `Checkpoint GUTS at thread wall`.
- Frozen rollback baseline also exists: `GUTS-035-KNOWN-GOOD`.
- **Eight-book corpus provenance/integrity audit COMPLETED.** See `CONTENTS_CORPUS_FORENSIC_AUDIT_2026-09-27.md`.
- **No production corpus repair has been made since the branch was created.**

## Production baseline

- Spectator Reader: GUTS 0.35.
- Domain: `gutenbrg.com`.
- Reader metadata: `v0.35-performance-reader`.
- Cloudflare serves `./public` via root `wrangler.jsonc`; Worker source is root `src/worker.js`.
- Compact actual-phone QA of the 0.35 visible Reader previously passed: Landing, carousel/bounce, book → Contents → chapter, page movement both ways, return to Landing.
- Landing overscroll material, cover → Contents slide, and page-flick slide are already implemented.

## What triggered the stop

The intended Contents cleanup ceased when inspection showed the problem is deeper than display labels.

`PERFORMANCE35/ac_035.json` (Agatha Christie, *The Murder at the Vicarage*) itself begins with a `Chapter 5` chapter object and is discontinuous. This means the transformed performance corpus is suspect; the originals are not thereby presumed damaged or lost.

Observed state at stop point:

- **Pooh:** Contents clean.
- **Thurber:** Contents clean.
- **Runyon:** Contents titles correct, but selections can open on non-story-start pages; opening alignment needs audit.
- **Joyce:** Contents titles correct, but selections can open on non-episode-start pages; opening alignment needs audit.
- **Christie:** broken/discontinuous Contents and suspect transformed corpus.
- **Parker:** parked/non-runner; do not spend repair time on it now.

## Forensic audit result

The eight active performance titles are now separated into three classes:

- **Structurally sound:** Pooh, Thurber, Jeeves.
- **Structurally sound with deliberate source-chapter cuts:** Huck, Farewell, Christie.
- **Broken opening/group mapping from later equal-chunk regrouping:** Runyon, Joyce.

Christie's discontinuity is now explained: the 0.35 builder deliberately retained source Chapters 5, 6, 11, 12, 22, 23, 24, 25, 26, 30 and 32 under its performance-depth rules. The retained destinations still begin at genuine chapter openings. Christie therefore needs an editorial/product decision, not forensic reconstruction.

A deeper prepared-page scan then proved that many genuine Runyon story titles and Joyce episode markers sit inside the existing prepared pages. Therefore a grouping-only repair could not produce true opening pages without splitting prepared pages and disturbing socket geometry.

Runyon and Joyce were consequently rebuilt **from the untouched PRIME sources only**, using the established 0.35 pagination/air-lock algorithm and the genuine source boundaries:
- Runyon: **47 genuine stories / 742 pages**.
- Joyce: **18 genuine episodes / 725 pages**. Episode XI (Sirens) is recovered at its genuine opening text because the PRIME extraction lacks an explicit "EPISODE XI" label there.
- every rebuilt chapter/episode opens at its genuine source opening;
- genuine token order is preserved;
- every rebuilt page has exactly one `$# GUTS — CURRENT STATE

**Authoritative checkpoint: 27 September 2026 — emergency handover**

Read `GUTS_EMERGENCY_HANDOVER_2026-09-27.md` first, then this file, and `GUTS_OHS_RECOVERY.md` before any write/deploy action. `GUTS_HANDOVER_2026-09-27.md` remains the detailed architecture manual beneath the later emergency overlay.

## Branch / production truth

- Production branch: `main` — **DO NOT MODIFY during this audit**.
- Verified `main` head at handover: `b662978d1de67304cc96ad78e3c224f2d2b75533` — `Install authoritative Contents tables`.
- Working branch: `contents-repair`.
- `contents-repair` was created from that current main.
- First branch checkpoint commit: `c7b75c6f365cf5a7723256aa8ad84c05976e6a5a` — `Checkpoint GUTS at thread wall`.
- Frozen rollback baseline also exists: `GUTS-035-KNOWN-GOOD`.
- **Eight-book corpus provenance/integrity audit COMPLETED.** See `CONTENTS_CORPUS_FORENSIC_AUDIT_2026-09-27.md`.
- **No production corpus repair has been made since the branch was created.**

## Production baseline

- Spectator Reader: GUTS 0.35.
- Domain: `gutenbrg.com`.
- Reader metadata: `v0.35-performance-reader`.
- Cloudflare serves `./public` via root `wrangler.jsonc`; Worker source is root `src/worker.js`.
- Compact actual-phone QA of the 0.35 visible Reader previously passed: Landing, carousel/bounce, book → Contents → chapter, page movement both ways, return to Landing.
- Landing overscroll material, cover → Contents slide, and page-flick slide are already implemented.

## What triggered the stop

The intended Contents cleanup ceased when inspection showed the problem is deeper than display labels.

`PERFORMANCE35/ac_035.json` (Agatha Christie, *The Murder at the Vicarage*) itself begins with a `Chapter 5` chapter object and is discontinuous. This means the transformed performance corpus is suspect; the originals are not thereby presumed damaged or lost.

Observed state at stop point:

- **Pooh:** Contents clean.
- **Thurber:** Contents clean.
- **Runyon:** Contents titles correct, but selections can open on non-story-start pages; opening alignment needs audit.
- **Joyce:** Contents titles correct, but selections can open on non-episode-start pages; opening alignment needs audit.
- **Christie:** broken/discontinuous Contents and suspect transformed corpus.
- **Parker:** parked/non-runner; do not spend repair time on it now.

## Forensic audit result

The eight active performance titles are now separated into three classes:

- **Structurally sound:** Pooh, Thurber, Jeeves.
- **Structurally sound with deliberate source-chapter cuts:** Huck, Farewell, Christie.
- **Broken opening/group mapping from later equal-chunk regrouping:** Runyon, Joyce.

Christie's discontinuity is now explained: the 0.35 builder deliberately retained source Chapters 5, 6, 11, 12, 22, 23, 24, 25, 26, 30 and 32 under its performance-depth rules. The retained destinations still begin at genuine chapter openings. Christie therefore needs an editorial/product decision, not forensic reconstruction.

 in `force_paragraphs` and none in genuine `paragraphs`.

See `RUNYON_JOYCE_REBUILD_QA.md`.

**Next work:** visible branch QA of Runyon and Joyce Contents → opening pages, then resolve Christie's deliberate 11-chapter edited-edition presentation. Parker remains parked.

## Live metadata mapping

- `aam` — *The House at Pooh Corner* — `PERFORMANCE35/aam_035.json`
- `jeeves` — *Right Ho, Jeeves!* — `PERFORMANCE35/jeeves_035.json`
- `farewell` — *A Farewell to Arms* — `PERFORMANCE35/farewell_035.json`
- `huck` — *Huckleberry Finn* — `PERFORMANCE35/huck_035.json`
- `dp` — *Men I’m Not Married To* — `PRIMED/DP_GUTS_PRIME2.json`
- `dr` — *On Broadway* — `PERFORMANCE35/dr_035.json`
- `ac` — *Murder at the Vicarage* — `PERFORMANCE35/ac_035.json`
- `jj` — *Ulysses* — `PERFORMANCE35/jj_035.json`
- `jt` — *My Life and Hard Times* — `PERFORMANCE35/jt_035.json`

Display order: `jt, jeeves, farewell, aam, huck, dp, dr, ac, jj`.

## Signed-off machinery — do not reopen casually

- H2 PUSH / GUT PULL architecture.
- Cloudflare Worker/KV production seam.
- READY / ARMED / CLEAN remote transport.
- local payoff/PAID, dwell and persistence behaviour.
- Reader 0.35 visible baseline and existing transitions.

A corpus/Contents problem is not evidence that the state engine is broken.

## Release discipline

Nothing from `contents-repair` goes to `main` until the full replacement is audited and compactly phone-tested. At release, preserve the old known-good material as rollback history; never destroy the known-good bird while testing the new one.

**Status: MAIN SAFE / CONTENTS-REPAIR ISOLATED / RUNYON + JOYCE STRUCTURAL REBUILD COMPLETE + MECHANICALLY QA'D / NOT RELEASED.**