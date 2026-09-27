# IF CHATGPT DIES, READ THIS

**Recovery entry point — refreshed 27 Sep 2026**

Do not reconstruct GUTS from chat memory. The repository now contains the authority.

## FIRST: DO NO HARM

Production `main` is safe. During the current Contents/corpus investigation, **do not alter it**.

Working branch: `contents-repair`.

At emergency handover:

- `main` head = `b662978d1de67304cc96ad78e3c224f2d2b75533` (`Install authoritative Contents tables`)
- `contents-repair` existed and had been checkpointed
- corpus provenance/integrity audit had **not begun**
- no corpus repair had been made after branching

Frozen rollback baseline: `GUTS-035-KNOWN-GOOD`.

## READ IN THIS ORDER

1. `GUTS_EMERGENCY_HANDOVER_2026-09-27.md`
2. `GUTS_CURRENT_STATE.md`
3. `GUTS_OHS_RECOVERY.md`
4. `GUTS_THREAD_WALL_CHECKPOINT_2026-09-27.md`
5. `CONTENTS_EDITORIAL_PLAN.md`
6. `GUTS_HANDOVER_2026-09-27.md` — detailed architecture/manual
7. `BABYS_FIRST_GUTS.md`
8. `GUTS_PERFORMANCE_FLOW_POV_v1.md`

The former contents of this file described an older v0.26-era resume point and are obsolete.

## CURRENT EMERGENCY

A Contents cleanup uncovered evidence that the transformed corpus itself may be discontinuous. `PERFORMANCE35/ac_035.json` (Christie) begins with a `Chapter 5` chapter object. Stop cosmetic patching until provenance is mapped.

Next production task after documentation:

**Audit Christie source/original -> PRIMED -> PERFORMANCE35 -> retained/omitted chapters -> mapping -> opening alignment -> `$$$`/force data.**

Then Runyon and Joyce opening alignment; verify Pooh/Thurber; then Jeeves/Farewell/Huck. Parker is parked.

## MACHINE MAP

- GUTS source/workshop: `stanjarin/GUTS`
- performer NoBo/H2G2: `stanjarin/NoBoNoFo`
- production domain: `gutenbrg.com`
- Cloudflare Worker: `guts`
- KV binding: `GUTS_STATE`
- current static asset root: `./public`
- current Worker source: `src/worker.js`
- current deployment config: `wrangler.jsonc`
- current Reader baseline: GUTS 0.35 / `v0.35-performance-reader`

Doctrine: **H2 PUSHES — GUT PULLS.**

Do not copy secret/PIN values into GitHub. Do not replace runtime secrets during a routine redeploy/recovery.

## IF PRODUCTION IS BROKEN

Do not guess. Compare `main` to `GUTS-035-KNOWN-GOOD`, inspect Cloudflare **View all deployments**, verify what `public/index.html` contains, and preserve Worker/KV bindings. The full procedure is in `GUTS_OHS_RECOVERY.md` and `GUTS_HANDOVER_2026-09-27.md`.

## IF THE CONTENTS REPAIR IS BROKEN

Do not patch the patch. Record the bad branch commit, compare it with the previous `contents-repair` state and with `main`, restore only the affected branch material, and re-run mechanical checks. Production should remain untouched.

**The repository is the memory. Read first; turn screws second.**