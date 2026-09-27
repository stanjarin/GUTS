# GUTS

**Gutenberg Utility Title System** — spectator-own-phone development descended from NoBo NoFo.

## EMERGENCY CURRENT STATE — 27 Sep 2026

**DO NOT TOUCH `main`.** Production `main` is the known live baseline and currently points at commit `b662978d1de67304cc96ad78e3c224f2d2b75533` (`Install authoritative Contents tables`).

All investigation and repair work is confined to branch:

`contents-repair`

That branch was created from current `main`. The only work performed after branching was documentation/checkpoint work. **The corpus provenance/integrity audit has not begun and no production corpus repair has been made on this branch.**

### Why work stopped

A Contents cleanup exposed a deeper problem. `PERFORMANCE35/ac_035.json` (Christie) itself begins with a `Chapter 5` chapter object and is discontinuous. Therefore the defect is not safely classifiable as a display-label problem. The transformed PERFORMANCE35 corpus must be audited against its upstream/source material before further editorial patching.

Known bench observations at the stop point:

- Pooh: Contents clean.
- Thurber: Contents clean.
- Runyon: titles correct; some selections can open on non-story-start pages.
- Joyce: titles correct; some selections can open on non-episode-start pages.
- Christie: broken/discontinuous Contents; corpus itself is suspect.
- Parker: parked/non-runner for now.

### Next production action — NOT YET STARTED

Audit provenance/integrity on `contents-repair`, beginning with Christie:

`original/source -> PRIMED -> PERFORMANCE35 -> retained/omitted chapters -> numbering/mapping -> opening alignment -> $$$/force_paragraph preservation`

Do **not** resume cosmetic renumbering until that mapping is understood.

## Canonical reading order

1. `GUTS_HANDOVER_2026-09-27.md`
2. `GUTS_CURRENT_STATE.md`
3. `GUTS_OHS_RECOVERY.md`
4. `GUTS_THREAD_WALL_CHECKPOINT_2026-09-27.md`
5. `CONTENTS_EDITORIAL_PLAN.md`
6. `BABYS_FIRST_GUTS.md`
7. `GUTS_PERFORMANCE_FLOW_POV_v1.md`
8. current code/data only after the above

`CURRENT_STATE.md` is retained as a compatibility pointer to the authoritative current-state file. `IF_CHATGPT_DIES_READ_THIS.md` is the recovery entry point and points back to this canonical set.

Older README/checkpoint material, legacy Cloudflare files, and one-shot workflows are history unless the canonical docs explicitly call them current.

## Production architecture in one paragraph

Performer NoBo/H2G2 pushes tiny state to Cloudflare; the spectator Reader on `gutenbrg.com` pulls it. **H2 PUSHES — GUT PULLS.** Current production Reader is 0.35; Cloudflare serves `./public` through root `wrangler.jsonc` and root `src/worker.js`. Remote READY/ARMED/CLEAN transport and local Reader payoff/PAID behaviour are established machinery and are not to be redesigned as part of the Contents/corpus repair.

## Safety baseline

Frozen rollback branch: `GUTS-035-KNOWN-GOOD`.

Current live `main` must remain untouched while `contents-repair` is being investigated. No workflow, deploy, merge, branch-force, or corpus mutation may target `main` during the audit.

For the full recovery/safety rules, read `GUTS_OHS_RECOVERY.md` before turning another screw.