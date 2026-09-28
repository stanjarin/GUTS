# GUTS RELEASE CANDIDATE CHECKLIST — 28 September 2026

Status: **PREPARED — NOT YET MERGED TO PRODUCTION MAIN**

## Authority

Read in this order:
1. `GUTS_WORKFLOW_CONSTITUTION.md`
2. `GUTS_CURRENT_STATE.md`
3. this checklist
4. supporting audit/recovery documents only as needed

Rule: **read broadly, act narrowly.**

## Production anchor

- Production branch: `main`
- Production anchor before this repair campaign: `b662978d1de67304cc96ad78e3c224f2d2b75533`
- Release work branch: `contents-repair`
- `contents-repair` is ahead of `main` and was 0 commits behind at pre-release comparison.
- Existing rollback anchors remain:
  - `contents-repair-backup-2026-09-27`
  - `visually-good-backup-2026-09-28`
  - `GUTS-035-KNOWN-GOOD`

## Frozen layers — DO NOT EDIT DURING RELEASE

- corpus
- Reader presentation
- landing/carousel
- H2G2 covert arming path
- Worker/KV transport
- READY / ARMED / PAID / CLEAN state machinery
- selected-chapter opener protection
- 6-second dwell and PAID persistence

## Human QA already passed

- all eight active books: corpus + real Reader phone QA
- landing/carousel: phone + desktop A-OK
- H2G2 → Worker/KV → GUTS: PASS
- complete performance chain:
  **CLEAN → ARMED → protected opener → prepared payoff → 6s dwell → PAID persistence → CLEAN**
- unique Cloudflare version URL produced clean force-word substitution

## Cache caveat

Safari may retain an older Reader when using the stable branch-preview alias.

For deployment QA, use the unique Cloudflare version URL first. Only after that passes should the stable alias/custom domain be judged. A visible trailing-dollar symptom (`GOPHERS$`) was proven to be stale alias/browser cache, not current source, corpus, KV, or deployed version content.

## Repository hygiene before release

Completed:
- temporary 28-Sep diagnostic workflows moved under `LEGACY_DO_NOT_DEPLOY/workflows/`
- obsolete 0.35 writer/audit workflows removed from active `.github/workflows/`
- transient diagnostic reports moved under `LEGACY_DO_NOT_DEPLOY/diagnostics/`
- no frozen runtime behaviour changed during cleanup

Before merge:
- confirm `.github/workflows/` contains no active writer workflow
- confirm root `index.html` and `public/index.html` are byte-identical
- confirm exact socket injector remains `split('$$$').join(magic.force)`
- confirm active performance pages contain exactly one canonical `$$$` socket per prepared page
- confirm Cloudflare branch build succeeds

## Release procedure

1. Freeze a named release-candidate branch at the exact approved `contents-repair` tip.
2. Compare release candidate against `main`; inspect runtime/code/data differences only.
3. Do **not** regenerate corpus or run old build workflows.
4. Merge the frozen release candidate to `main` only after explicit Stanley approval.
5. Wait for Cloudflare production build to finish successfully.
6. Capture the unique production version URL.
7. On that unique URL, smoke-test:
   - landing and carousel;
   - one book/Contents/Reader path;
   - CLEAN;
   - H2G2 ARM with a fresh word;
   - protected opener;
   - payoff page;
   - 6+ second dwell;
   - PAID persistence;
   - CLEAN.
8. Test `https://gutenbrg.com` separately after unique-version QA.
9. If custom-domain Safari appears stale, do not modify source merely to chase cache. Compare against the unique build first.
10. If any genuine regression appears, stop and roll back to the frozen RC/known-good anchor; do not patch multiple layers at once.

## Explicitly not part of this release

- Huck OCR cleanup
- Parker resurrection
- new corpus generation
- NoBo corpus/editorial changes
- multi-performer/session architecture expansion
- cosmetic experimentation beyond the already-approved landing/carousel repair

## Release gate

Production merge requires one explicit decision only:

**Stanley approves the frozen RC for merge to `main`.**

Until then, `main` remains untouched.
