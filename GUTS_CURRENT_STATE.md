# GUTS — CURRENT STATE

**Authoritative checkpoint: 27 September 2026 — emergency handover**

Read `GUTS_HANDOVER_2026-09-27.md` first and `GUTS_OHS_RECOVERY.md` before any write/deploy action.

## Branch / production truth

- Production branch: `main` — **DO NOT MODIFY during this audit**.
- Verified `main` head at handover: `b662978d1de67304cc96ad78e3c224f2d2b75533` — `Install authoritative Contents tables`.
- Working branch: `contents-repair`.
- `contents-repair` was created from that current main.
- First branch checkpoint commit: `c7b75c6f365cf5a7723256aa8ad84c05976e6a5a` — `Checkpoint GUTS at thread wall`.
- Frozen rollback baseline also exists: `GUTS-035-KNOWN-GOOD`.
- **Corpus provenance/integrity audit has NOT begun.**
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

## Next action — audit first

Before any further Contents patching, map:

`original/source -> PRIMED/PERFORMANCE35 -> chapters retained/omitted -> renumbering/mapping -> page/opening alignment -> $$$ sockets/force_paragraphs preserved`

Priority order:

1. Christie.
2. Runyon.
3. Joyce.
4. Verify Pooh and Thurber.
5. Jeeves / Farewell / Huck.
6. Parker last / special case.

The previous cosmetic Contents plan is now subordinate to this provenance audit. Do not renumber/hide/relabel around unknown structural damage.

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

**Status: MAIN SAFE / CONTENTS-REPAIR ISOLATED / DOCUMENTATION FIRST / CORPUS AUDIT NOT STARTED.**