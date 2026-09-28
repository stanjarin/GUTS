# GUTS — CURRENT STATE

**Authoritative checkpoint: 27 September 2026 — post-hardening**

## Safety anchors

- Production `main`: `b662978d1de67304cc96ad78e3c224f2d2b75533` — untouched.
- Working branch: `contents-repair`.
- Clean pre-hardening snapshot: `contents-repair-backup-2026-09-27` at `9e6a3f713c1343e4bfb361a447fe70a884b9a55b`.
- Frozen known-good rollback: `GUTS-035-KNOWN-GOOD`.

## Governing workflow

Read `GUTS_WORKFLOW_CONSTITUTION.md` **before all other project documents**. It governs sequencing, freeze rules, rollback discipline and QA.

## Mandatory handover rule

**READ EVERYTHING before acting.**

Read all GUTS material and all NoBo material. After reading it, remember that for GUTS the only operational NoBo dependency is **H2G2 covert arming**.

## Current Reader/corpus state

- Runyon repaired: 47 genuine stories / 742 pages.
- Joyce repaired: 18 genuine episodes / 725 pages.
- Pooh, Thurber, Jeeves, Huck and Farewell structurally sound.
- Christie is a deliberate 11-source-chapter performance edition, not unexplained corruption.
- Parker remains parked.

## Hardening completed on contents-repair

- exact canonical `$$$` substitution fixed;
- Thurber stale unreachable Contents label removed;
- Christie Contents/source numbering made truthful;
- Farewell retained source numbering made explicit/truthful;
- stale Contents/build writer workflows quarantined;
- root/public Reader synchronised;
- active performance corpus root/public copies synchronised.

## Mechanical QA

`HARDENING_QA_2026-09-27.md`: **PASS**

It verifies:
- exact `$$$` substitution;
- Reader JavaScript syntax;
- truthful Thurber/Christie/Farewell Contents;
- chapter counts for all eight active books;
- exactly one socket per active performance page;
- no socket markers in genuine prose;
- root/public identity;
- stale writer workflows absent from active workflow directory.

## Signed-off machinery — do not reopen casually

- H2 PUSH / GUT PULL.
- Worker/KV transport.
- READY / ARMED / CLEAN.
- local PAID/dwell persistence.
- selected-chapter opener protection.
- existing Reader navigation/transitions.

## Read next

1. `GUTS_NOBO_SYSTEM_AUDIT_MAP_2026-09-27.md`
2. `GUTS_OHS_RECOVERY.md`
3. `HARDENING_QA_2026-09-27.md`
4. `CONTENTS_CORPUS_FORENSIC_AUDIT_2026-09-27.md`
5. `RUNYON_JOYCE_REBUILD_QA.md`
6. `GUTS_HANDOVER_2026-09-27.md`

## Next action

**Actual-phone visible QA of the hardened candidate without altering production main.**

After that, compare the release candidate against frozen `main` and decide whether it is fit to release.

**Status: MAIN SAFE / CLEAN BACKUP FROZEN / HARDENING COMPLETE / MACHINE QA PASS / PHONE QA NEXT.**


## 2026-09-28 corpus freeze / Reader repair

Phone corpus QA passed for Jeeves, Huck, Farewell and Christie using the isolated four-book QA page. Huck OCR defects are logged as a separate source-quality issue; Christie's doubled heading on that stripped QA page was presentation-only.

All eight active books are now **corpus-frozen**: Pooh, Thurber, Runyon, Joyce, Jeeves, Huck, Farewell, Christie.

Reader-only repair then applied on `contents-repair`:
- rebuilt-four Contents now derive descriptive labels from genuine opening prose instead of stale authoritative chapter arrays;
- first reader page of Jeeves, Huck, Farewell and Christie now displays one canonical chapter heading;
- an existing Christie source heading is replaced rather than duplicated;
- root and public Reader copies verified identical;
- exact `$$$` socket substitution remains intact.

NEXT ACTION: phone-QA the real Reader presentation only. Do not touch corpus generation.


## 2026-09-28 all-eight Reader phone QA PASS

Stanley tested the uniquely named repaired Reader preview on iPhone Safari Private.

Result: **ALL EIGHT ACTIVE BOOKS PASS** at Reader presentation level:
- Pooh
- Thurber
- Runyon
- Joyce
- Jeeves
- Huck
- Farewell
- Christie

This confirms:
- rebuilt four-book corpora remain sound in the real Reader;
- Contents presentation is acceptable;
- chapter-opening presentation is acceptable;
- no visible regression observed in the previously frozen four.

Known side issues remain separate:
- Huck OCR defects are source-quality cleanup only;
- TinyURL/live deployment is still serving the old production state;
- landing-page grey-block defect remains logged separately.

Current uniquely named Reader QA commit:
- `63b97344612ff480b88e64015e7f84393ccbd342`
- `public/READER_QA_2026-09-28.html`

NEXT ACTION: freeze this Reader state, then test live H2G2 → GUTS arming/deployment against a controlled candidate without altering corpus or Reader presentation.


## 2026-09-28 landing/carousel source repair PASS

Stanley phone- and desktop-tested the branch preview after restoring the pre-0.32 carousel presentation model.

Root cause chain:
- 0.31 had no carousel mask.
- 0.32 introduced an unrelated white carousel background plus `.carousel-mask`.
- 0.33 deliberately resized that mask, preserving the compromised structure.
- later builds inherited it.
- the replacement `LANDING PAGE.jpg` was ruled out: old and replacement are both 2048 × 8000 and pixel-aligned through the carousel zone.

Clean repair on `contents-repair`:
- removed `.carousel-mask` CSS;
- removed carousel-mask markup;
- removed `background:#fff` from `.carousel-window`;
- retained native touch scrolling and current hit-map logic;
- retained exact `$$$` substitution;
- root/public Reader files verified identical.

Stanley result: **A-OK on phone and desktop.**

Rollback anchor created immediately before clean repair:
- `visually-good-backup-2026-09-28`
- commit `a188dbfea75317ea0663adf00b4fd5c22ebcb6b5`

Current clean repaired branch tip after the three file edits:
- `e6f56f27a3b8a9775e4bcc3a5cfa666c9cfbcb9f`

Landing/carousel layer is now **FROZEN**.

NEXT ACTION: test **H2G2 → GUTS arming only** against the branch preview. Do not alter corpus, Reader presentation, or landing/carousel.


## 2026-09-28 H2G2 → GUTS arming PASS

Stanley armed **GOPHERS** through NoBo H2G2.

Verified transport:
- H2G2 posts to `https://gutenbrg.com/api/performer/state`.
- production and branch preview read the same KV state.
- after ARM, both endpoints reported:
  - phase: ARMED
  - word: GOPHERS
  - revision: 27

A visible `GOPHERS$` anomaly appeared when testing through the stable branch alias. Investigation ruled out:
- H2G2 input corruption;
- KV corruption;
- malformed `$$$$` sockets;
- stale repository Reader code;
- stale deployed Reader code;
- stale deployed Thurber JSON;
- service-worker/PWA caching.

Current deployed Reader HTML and Thurber JSON were byte-identical to repository versions, with exact `split('$$$')` substitution and exact `$$$` sockets.

Testing the unique Cloudflare version URL:
- `https://666e831b-guts.stanjarin.workers.dev`
produced **GOPHERS clean**.

Conclusion:
- H2G2 → Worker/KV → GUTS arming path is **PASS**.
- the `GOPHERS$` symptom was caused by Safari/stable-preview-alias cache serving an older Reader document.
- no corpus or Reader-source repair is required for this issue.

Arming layer is now **FROZEN**.

NEXT ACTION: deliberately CLEAN remote state, then test the final READY / ARMED / PAID / CLEAN performance path on the fresh build URL before release/deployment decisions.


## 2026-09-28 full performance state-chain PASS

Stanley completed the controlled live test using a fresh Cloudflare version URL and a new arm word.

Sequence tested:
1. deliberately forced remote CLEAN by clearing stored ARM authorisation and re-entering the ARM PIN through NoBo H2G2;
2. armed a new word through H2G2;
3. spectator entered GUTS on the unique branch build;
4. chose a book and chapter;
5. selected chapter opener remained pristine;
6. prepared page displayed the armed word;
7. page was held for the required dwell interval;
8. departure converted the local state to PAID;
9. revisiting the paid page preserved the armed-word payoff only on that paid page;
10. cleanup path remained functional.

Stanley result: **PASS**.

This confirms the complete live performance chain:
**CLEAN → ARMED → protected opener → prepared payoff → 6s dwell → PAID persistence → CLEAN**

Previously observed `GOPHERS$` was isolated to Safari caching an older Reader document at the stable preview alias. Unique Cloudflare version URL produced the correct clean result. For QA, prefer unique version URLs when verifying newly deployed Reader code.

The following layers are now frozen:
- corpus;
- Reader presentation;
- landing/carousel;
- H2G2 → Worker/KV arming;
- full READY/ARMED/PAID/CLEAN performance state chain.

NEXT ACTION: compare the frozen release candidate against production `main`, remove/quarantine temporary diagnostic workflows and reports that are no longer needed, and prepare a release/deployment checklist without altering frozen runtime behavior.


## 2026-09-28 release-candidate preparation

Pre-release cleanup completed without changing frozen runtime behaviour.

Completed:
- compared `contents-repair` against `main`: branch was ahead, 0 commits behind;
- quarantined all temporary 28-Sep diagnostic workflows;
- quarantined obsolete active 0.35 writer/audit workflows;
- moved transient diagnostic reports under `LEGACY_DO_NOT_DEPLOY/diagnostics/`;
- created `GUTS_RELEASE_CHECKLIST_2026-09-28.md`.

No corpus, Reader, landing/carousel, Worker/KV or state-machine behaviour was altered by this cleanup.

NEXT ACTION: verify repository hygiene, freeze the exact approved tip as a named release-candidate branch, then await Stanley's explicit approval before any merge to `main`.
