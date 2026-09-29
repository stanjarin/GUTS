> **29-Sep current-state warning:** this is a forensic audit map, not the live resume point. Later full rebuild/QA superseded several retained-chapter counts below. For current truth read `GUTS_HANDOVER_2026-09-29.md` and `GUTS_CURRENT_STATE.md` first.

# GUTS — SYSTEM AUDIT / MAP

**Canonical machine map — 27 September 2026**  
**Working branch:** `contents-repair`  
**Clean pre-hardening snapshot:** `contents-repair-backup-2026-09-27` at `9e6a3f713c1343e4bfb361a447fe70a884b9a55b`  
**Production `main`: untouched** at `b662978d1de67304cc96ad78e3c224f2d2b75533`

## Read-everything rule

At every handover, **read everything before acting**:
- all GUTS documentation, code, workflows, configs and relevant data;
- all NoBo documentation/code/data as cross-system context.

Then apply scope correctly:

**For GUTS, NoBo is operationally relevant only through the H2G2 covert arming mechanism.**

Do not let unrelated NoBo book/corpus state become a GUTS repair or release dependency.

## Audit scope completed

Complete machine read performed:
- GUTS: 101 text/code/data files, 236,902 logical lines.
- NoBo: 25 text/code/data files, 130,227 logical lines.
- all JSON/webmanifest payloads parsed;
- all standalone JavaScript and inline HTML scripts syntax-checked;
- binary artwork/checker PDFs inventoried as artifacts rather than line-oriented code.

Raw evidence:
- `SYSTEM_AUDIT_RAW_2026-09-27.md`
- `NOBO_SOCKET_FORENSIC_2026-09-27.md`
- `CONTENTS_CORPUS_FORENSIC_AUDIT_2026-09-27.md`
- `RUNYON_JOYCE_REBUILD_QA.md`
- `HARDENING_QA_2026-09-27.md`

## Authority order

1. `GUTS_CURRENT_STATE.md`
2. this file
3. `GUTS_OHS_RECOVERY.md`
4. `HARDENING_QA_2026-09-27.md`
5. `CONTENTS_CORPUS_FORENSIC_AUDIT_2026-09-27.md`
6. `RUNYON_JOYCE_REBUILD_QA.md`
7. `GUTS_HANDOVER_2026-09-27.md`
8. current code/data

Older briefs/checkpoints remain historical evidence only.

## Architecture

### Performer side

`NoBo H2G2 covert input -> POST https://gutenbrg.com/api/performer/state -> Cloudflare Worker/KV`

NoBo H2G2 is the only NoBo dependency material to GUTS.

### Cloudflare

Current Worker:
- `src/worker.js`

Config:
- `wrangler.jsonc`

Assets served from:
- `./public`

Core global routes:
- `GET/POST /api/state`
- `POST /api/performer/state`

Session/alias routes also exist and are documented in the detailed handover.

### Spectator Reader

Current Reader baseline:
- GUTS 0.35
- metadata `v0.35-performance-reader`
- root `index.html` and served `public/index.html` are byte-identical

State behaviour preserved:
- READY / ARMED / CLEAN remote state
- local PAID
- 6-second dwell
- selected-chapter opener protection
- paid-page persistence

## Corpus state

- Pooh: 10 chapters / 82 pages — sound.
- Thurber: 10 retained sections / 55 pages — sound.
- Jeeves: 23 chapters / 228 pages — sound.
- Huck: 42 retained chapters / 268 pages — sound; source Ch43 intentionally omitted.
- Farewell: 34 retained chapters / 202 pages — sound; source Ch1, 8, 17, 22, 26, 32 and 39 intentionally omitted.
- Christie: 11 retained source chapters / 36 pages — source Ch5, 6, 11, 12, 22, 23, 24, 25, 26, 30 and 32.
- Runyon: repaired to 47 genuine stories / 742 pages.
- Joyce: repaired to 18 genuine episodes / 725 pages.
- Parker: parked/non-runner.

Every active performance page passes:
- one canonical `$$$` marker in `force_paragraphs`;
- no marker in genuine `paragraphs`;
- root/public corpus identity.

## Hardening completed

### Exact socket substitution

The Reader previously used an incorrect `$$` substitution.

It now uses exact canonical `$$$` substitution on `contents-repair`.

Production `main` remains unchanged and therefore still contains the old production code until an approved release.

### Contents / visible-heading truth

- Thurber authoritative Contents reduced from 11 labels to the 10 retained sections.
- Christie authoritative Contents now explicitly lists its retained source chapter numbers.
- Christie no longer rewrites retained source chapter headings into false sequential Roman numbering.
- Farewell authoritative Contents explicitly lists its 34 retained source chapter numbers.
- Farewell is excluded from sequential Roman rewriting so source-number gaps remain truthful.
- Runyon/Pooh/Joyce authoritative tables remain aligned with their repaired/verified structures.

### Workflow quarantine

Removed from active `.github/workflows` and preserved under `LEGACY_DO_NOT_DEPLOY/workflows`:
- `contents_fix_v2.yml`
- `one_shot_contents_words.yml`
- `guts035_build.yml`

These could otherwise overwrite current Contents or recreate the old Runyon/Joyce structure.

Completed temporary audit/QA workflows were also archived after use.

## Hardening QA

`HARDENING_QA_2026-09-27.md` records PASS for:
- root/public Reader identity;
- exact `$$$` substitution;
- truthful Thurber/Christie/Farewell Contents;
- Christie retained source numbering;
- all eight active corpus chapter/page/socket checks;
- root/public corpus identity;
- stale active workflow absence;
- Reader JavaScript syntax.

## Safety / rollback

Three separate safety anchors now exist:
1. production `main` — untouched live baseline;
2. `GUTS-035-KNOWN-GOOD` — older frozen rollback baseline;
3. `contents-repair-backup-2026-09-27` — exact pre-hardening snapshot of the fully audited/repaired branch.

Do not force-update or delete any of them during current QA.

## Release gate

Machine hardening is complete.

Remaining gate before any release:
1. actual-phone visible QA of the repaired/hardened candidate;
2. compare release candidate against frozen `main`;
3. only then decide whether to merge/release.

**Do not touch `main` merely to make testing easier.**
