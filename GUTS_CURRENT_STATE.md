# GUTS — CURRENT STATE

**Authoritative checkpoint: 27 September 2026 — post exhaustive GUTS + NoBo audit**

Read this file first, then:
1. `GUTS_NOBO_SYSTEM_AUDIT_MAP_2026-09-27.md`
2. `GUTS_OHS_RECOVERY.md`
3. `CONTENTS_CORPUS_FORENSIC_AUDIT_2026-09-27.md`
4. `RUNYON_JOYCE_REBUILD_QA.md`
5. `GUTS_HANDOVER_2026-09-27.md` for detailed architectural history

## Branch / production truth

- Production `main`: **DO NOT MODIFY casually**.
- Verified production head: `b662978d1de67304cc96ad78e3c224f2d2b75533` — `Install authoritative Contents tables`.
- Working branch: `contents-repair`.
- Frozen rollback branch: `GUTS-035-KNOWN-GOOD`.
- Production Reader: GUTS 0.35 / `v0.35-performance-reader`.
- Cloudflare serves `./public`; Worker is root `src/worker.js`.
- Root/public Reader and active corpus copies are currently synchronised on the branch.

## Exhaustive audit complete

GUTS was read in full at the text/code/data level:
- 101 text/code/data files / 236,902 logical lines;
- all JSON/webmanifest parsed;
- all JavaScript/inline HTML scripts syntax-checked successfully.

NoBo was cross-checked comprehensively, but for GUTS **only the H2G2 covert arming route is relevant**. Other NoBo books/corpus issues are out of GUTS scope.

See `GUTS_NOBO_SYSTEM_AUDIT_MAP_2026-09-27.md`.

## Corpus state

- Pooh: sound.
- Thurber: structurally sound; Contents table has one stale/unreachable extra terminal label.
- Jeeves: sound.
- Huck: sound; source Ch43 deliberately omitted.
- Farewell: structurally sound; seven source chapters deliberately omitted; visible numbering presentation still needs truthing.
- Christie: structurally sound reduced edition retaining source chapters 5, 6, 11, 12, 22–26, 30, 32; visible numbering presentation still needs a deliberate editorial decision.
- Runyon: **repaired on this branch** — 47 genuine stories / 742 pages.
- Joyce: **repaired on this branch** — 18 genuine episodes / 725 pages.
- Parker: parked/non-runner.

Runyon/Joyce rebuild QA:
- genuine token order PASS;
- genuine opening alignment PASS;
- exactly one canonical `$$$` marker per prepared page PASS.

## Critical newly found Reader defect

GUTS currently substitutes:

`split('$$')`

but the canonical corpus marker is:

`$$$`

NoBo correctly replaces `$$$` exactly. GUTS must be corrected on `contents-repair` before release.

This defect exists in frozen production `main` too; **do not patch main directly**.

## Workflow hazards

Before any merge/release, review/quarantine:
- `.github/workflows/contents_fix_v2.yml`
- `.github/workflows/one_shot_contents_words.yml`
- `.github/workflows/guts035_build.yml`

The first two can write on pushes to `main`; the builder can recreate the old Runyon/Joyce structural problem.

## Signed-off machinery — do not reopen casually

- H2 PUSH / GUT PULL architecture.
- Worker/KV transport.
- READY / ARMED / CLEAN remote state.
- local PAID/dwell persistence.
- selected-chapter opener protection.
- current visible Reader navigation/transitions baseline.

A corpus/Contents defect is not evidence that those systems are broken.

## Next action

Perform a **branch-only hardening pass**:

1. fix GUTS exact `$$$` substitution;
2. truth Christie, Farewell and Thurber Contents/visible headings;
3. quarantine stale active write workflows;
4. run full mechanical QA again;
5. then actual-phone QA.

**Status: MAIN SAFE / EXHAUSTIVE AUDIT COMPLETE / RUNYON + JOYCE REPAIRED ON BRANCH / RELEASE BLOCKED BY KNOWN HARDENING ITEMS.**
