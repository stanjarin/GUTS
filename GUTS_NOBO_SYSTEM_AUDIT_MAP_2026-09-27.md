# GUTS + NoBo — SYSTEM AUDIT / MAP

**Audit date:** 27 September 2026  
**GUTS branch audited:** `contents-repair`  
**NoBo branch audited:** `main`  
**Production GUTS `main`: NOT MODIFIED**

## Audit scope

This is the canonical machine-level map produced after a complete repository read.

- GUTS: 134 repository files inventoried; 101 text/code/data files read in full; 49,807,562 text/code/data bytes; 236,902 logical lines.
- NoBo: 40 repository files inventoried; 25 text/code/data files read in full; 19,945,674 text/code/data bytes; 130,227 logical lines.
- Every JSON/webmanifest payload parsed successfully.
- Every standalone JavaScript file and every inline HTML script block passed `node --check`.
- Binary images and checker PDFs were inventoried as artifacts rather than treated as line-oriented source. The text companion/source files were read in full where present.

Raw machine evidence:
- `SYSTEM_AUDIT_RAW_2026-09-27.md`
- `NOBO_SOCKET_FORENSIC_2026-09-27.md`
- `CONTENTS_CORPUS_FORENSIC_AUDIT_2026-09-27.md`
- `RUNYON_JOYCE_REBUILD_QA.md`

## Authority hierarchy

For current work, use this order:

1. `GUTS_CURRENT_STATE.md`
2. this file: `GUTS_NOBO_SYSTEM_AUDIT_MAP_2026-09-27.md`
3. `GUTS_OHS_RECOVERY.md`
4. `CONTENTS_CORPUS_FORENSIC_AUDIT_2026-09-27.md`
5. `RUNYON_JOYCE_REBUILD_QA.md`
6. `GUTS_HANDOVER_2026-09-27.md` for detailed architecture
7. code/data themselves

Older briefs, generated reports and checkpoint notes are historical evidence unless explicitly promoted above.

## Production / branch truth

- GUTS production `main` remains frozen at `b662978d1de67304cc96ad78e3c224f2d2b75533` — `Install authoritative Contents tables`.
- Working branch: `contents-repair`.
- Frozen rollback branch: `GUTS-035-KNOWN-GOOD`.
- Cloudflare serves `./public`.
- Root `index.html` and `public/index.html` are currently byte-identical.
- Root/public copies of all active PRIMED and PERFORMANCE35 corpus files checked by the audit are byte-identical.
- Inherited NoBo masters `jeeves.json`, `huck.json`, and `farewell.json` stored in GUTS are byte-identical to NoBo `main`.

## Architecture

### Performer / NoBo

Current NoBo `main` is build `v6.18S`.

The performer-side path is:

`NoBo H2G2 covert input -> POST https://gutenbrg.com/api/performer/state -> Cloudflare Worker/KV`

NoBo:
- uses the canonical `$$$` replacement exactly;
- preserves selected-chapter opener protection;
- uses a 6-second dwell;
- transitions ARMED -> PAID on departure from the qualified page;
- preserves only the paid page while PAID;
- supports CLEAN;
- contains the performer controls for GUTS state/mode.

### Cloudflare

Current Worker is root `src/worker.js`; config is root `wrangler.jsonc`.

Important routes:
- global: `/api/state`, `/api/performer/state`
- sessions: `/api/session/create`, `/api/session/state`, `/api/performer/session`, `/api/join`
- aliases: `/api/alias/bootstrap`, `/api/alias/state`, `/entry/<alias>`
- mode: `/performer/rehearsal`, `/api/performer/mode`

Important runtime facts:
- KV binding: `GUTS_STATE`
- global key: `current`
- site-mode key: `site-mode`
- session cookie: `guts_session`
- session TTL: 86400 seconds
- allowed aliases currently: `shortcuts`, `test-p2`
- performer CORS origin: `https://stanjarin.github.io`
- REHEARSAL sends unauthorised browsers to real Gutenberg while preserving path/query
- secret values are not stored in repository source

### Spectator / GUTS

Current Reader metadata remains `v0.35-performance-reader`.

Runtime:
- polls `/api/state` every 2.5 seconds;
- stores local magic state in sessionStorage;
- has selected-chapter opener protection;
- uses a 6-second dwell;
- pays on departure;
- renders `force_paragraphs` only when ARMED or on the exact PAID page.

## Critical defect found — socket substitution

The corpus standard everywhere is `$$$`.

NoBo correctly does:

`replaceAll("$$$", word)`

GUTS currently does:

`String(s).split('$$').join(magic.force)`

This is present in both current GUTS `main` and `contents-repair`.

With a canonical `$$$` marker, the GUTS expression replaces the first two dollar signs and leaves the third one behind. This is a real Reader defect and must be fixed on the working branch before release.

Do not repair production `main` directly.

## Corpus state

### Sound / aligned

- Pooh: 10 genuine chapters / 82 performance pages.
- Thurber: 10 retained structural sections / 55 performance pages.
- Jeeves: 23 chapters / 228 performance pages.
- Huck: 42 retained chapters / 268 performance pages; source Chapter 43 was deliberately omitted by the 0.35 builder.
- Farewell: 34 retained chapters / 202 performance pages; source Chapters 1, 8, 17, 22, 26, 32 and 39 were deliberately omitted.

### Christie

PRIME source contains the complete 32-chapter sequence.

The 0.35 builder deliberately retained only:

**5, 6, 11, 12, 22, 23, 24, 25, 26, 30, 32**

The retained text is structurally sound. The problem is product/editorial presentation, not unexplained corruption.

Current Reader also creates an additional presentation contradiction: the Contents can expose source chapter numbers while `displayParas()` rewrites first-page CHAPTER headings to sequential Roman numerals. This must be resolved deliberately.

### Runyon — repaired on contents-repair

Rebuilt from untouched PRIME source:
- 47 genuine stories
- 742 pages
- genuine token order preserved
- each story opens at its genuine opening
- exactly one `$$$` marker in each prepared page

### Joyce — repaired on contents-repair

Rebuilt from untouched PRIME source:
- 18 genuine episodes
- 725 pages
- genuine token order preserved
- each episode opens at its genuine opening
- exactly one `$$$` marker in each prepared page

Episode XI / Sirens is located by its genuine opening prose because the PRIME extraction does not contain an explicit EPISODE XI label.

### Parker

Still parked/non-runner. Do not spend repair time on it until a replacement/source decision is made.

## Contents / visible-heading issues still open

- Runyon: rebuilt structure now matches all 47 authoritative Contents titles.
- Joyce: rebuilt structure now matches all 18 authoritative episode titles.
- Pooh: authoritative 10-title table matches its 10 chapters.
- Thurber: Reader has 11 authoritative labels but PERFORMANCE35 currently has 10 retained sections. The terminal `A Note at the End` was cut by the builder, so the 11th label is unreachable; table should be made truthful.
- Christie: retained source chapter numbers conflict with sequential Roman-number rewriting on the first page.
- Farewell: retained source chapters are discontinuous; first-page chapter rewriting sequentialises them while stored titles retain source numbers.
- Huck/Jeeves: no equivalent discontinuity problem in their retained sequence, but visible QA remains required.

## NoBo corpus truth

The current NoBo book corpus contains **7,157 page objects**, not 9,761.

Current marker structure:
- Bloomfield: 1 marker per page.
- Farewell: 1 per page.
- H2G2: 1 per page.
- HST: 124 pages with one marker; Chapter 1 page 1 has none.
- Huck: 1 per page.
- Jeeves: 1 per page.
- Jobs: 1 per page.
- Keef: 1 per page.
- Sot-Weed: 66 chapter-opening pages have no marker; 1,767 follower pages each contain three `$$$` occurrences in one prepared sentence.

Those HST/Sot-Weed exceptions correspond to the documented older chapter-lead repair/reversion history and are not evidence of current GUTS corruption.

The current NoBo root `README.md` claim that 9,761 pages were checked, every page has a socket, and there are 9,762 sockets does **not** describe the present checked-in corpus and must be treated as stale historical documentation.

## Active-workflow hazards

The following active GUTS workflows are unsafe to carry blindly into a release:

### `contents_fix_v2.yml`
- runs on pushes to `main` as well as manual dispatch;
- writes Reader files and pushes commits;
- contains old Contents patch logic.

### `one_shot_contents_words.yml`
- runs on every push to `main`;
- writes the same Reader files;
- contains an older competing Contents table, including a 32-entry Christie assumption.

Both should be quarantined before any branch is merged to `main`.

### `guts035_build.yml`
Its build logic is the old builder that originally mis-grouped Runyon/Joyce. Running it again can recreate the structural problem and overwrite the repaired branch corpus. It must be quarantined or rewritten before release.

### `guts035_audit.yml`
Useful historical audit machinery but self-triggered by editing its workflow file and writes generated files. Keep only if deliberately retained as controlled tooling.

### `guts035_deploy.yml`
Manual-only Reader root/public synchroniser. It does not deploy the repaired corpus by itself. It is comparatively safe but should still be reviewed as part of release hardening.

## Documentation integrity

The full audit found:
- `GUTS_CURRENT_STATE.md` was corrupted by a branch-only automated text replacement during this thread. It is being replaced in full, not patched.
- `PERFORMANCE35/STRUCTURE_REPORT.md` describes the now-superseded equal-chunk Runyon/Joyce structure.
- `PERFORMANCE35/BUILD_REPORT.md` describes the original 0.35 builder output, not the repaired current Runyon/Joyce branch state.
- `GUTS_HANDOVER_2026-09-27.md`, emergency/checkpoint briefs and older NEXT-EWE files contain historically correct states that predate the completed 47-story/18-episode repair.
- historical files should remain available for archaeology, but must not outrank the authority hierarchy at the top of this document.

## Release rule

Before anything reaches `main`:

1. fix the exact `$$$` substitution bug on `contents-repair`;
2. resolve Christie/Farewell/Thurber Contents-visible-heading truth;
3. quarantine or rewrite dangerous active workflows;
4. run machine corpus/state QA;
5. run compact actual-phone Reader QA;
6. compare the release candidate against frozen `main`;
7. only then merge/release.

**Production `main` remains the untouched rollback truth until that gate is passed.**
