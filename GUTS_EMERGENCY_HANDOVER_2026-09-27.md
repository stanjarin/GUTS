# GUTS — EMERGENCY HANDOVER OVERLAY — 27 Sep 2026

**THIS IS THE FIRST FILE TO READ DURING THE CONTENTS/CORPUS EMERGENCY.**

It overlays, but does not erase, `GUTS_HANDOVER_2026-09-27.md`. The older handover remains the detailed architecture manual; this file records the later thread-wall state and prevents a fresh ewe/developer from following an earlier next-step assumption.

## Non-negotiable branch state

- Production `main`: **untouched**.
- `main` head verified at handover: `b662978d1de67304cc96ad78e3c224f2d2b75533` — `Install authoritative Contents tables`.
- Working branch: `contents-repair`.
- `contents-repair` was created from current main.
- First branch checkpoint: `c7b75c6f365cf5a7723256aa8ad84c05976e6a5a` — `Checkpoint GUTS at thread wall`.
- The corpus provenance/integrity audit **had not begun** at handover.
- No corpus repair had been made on the branch after creation; documentation is the first job.

## Why the thread stopped

The Contents cleanup exposed a structural warning: `PERFORMANCE35/ac_035.json` itself begins with `Chapter 5` and is discontinuous. That makes further cosmetic renumbering unsafe until corpus provenance is understood.

Do not infer that Stanley's originals were destroyed. The suspect layer is the transformed PERFORMANCE35/current corpus and its mapping.

## Bench observations

- Pooh — clean Contents.
- Thurber — clean Contents.
- Runyon — correct titles, but opening alignment suspect.
- Joyce — correct titles, but opening alignment suspect.
- Christie — discontinuous/broken Contents and suspect transformed corpus.
- Parker — parked/non-runner.

## Next production job after documentation

Start **Christie provenance/integrity audit** on `contents-repair`:

`best source/original -> PRIMED/AC_GUTS_PRIME2.json -> PERFORMANCE35/ac_035.json -> retained/omitted chapters -> mapping/renumbering -> opening alignment -> $$$/force_paragraph preservation`

Look for a known-good historical Christie mapping before inventing a new one.

Then audit Runyon and Joyce opening alignment; verify Pooh/Thurber; then Jeeves/Farewell/Huck. Parker last.

## Read next

1. `GUTS_CURRENT_STATE.md`
2. `GUTS_OHS_RECOVERY.md`
3. `GUTS_THREAD_WALL_CHECKPOINT_2026-09-27.md`
4. `CONTENTS_EDITORIAL_PLAN.md`
5. `GUTS_HANDOVER_2026-09-27.md` for full architecture and recovery detail
6. `BABYS_FIRST_GUTS.md` for the human map
7. `GUTS_PERFORMANCE_FLOW_POV_v1.md` before state/payoff work

## Communication / working discipline

Sparse comms. `go` means act. Do not ask Stanley to say go unless permission is genuinely needed. Locate first, answer second. Prefer a concrete finding and next action over implementation theatre.

**MAIN SAFE. BRANCH ISOLATED. DOCUMENTATION FIRST. AUDIT NEXT.**