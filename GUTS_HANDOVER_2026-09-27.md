# GUTS — HANDOVER / START HERE

**Handover checkpoint: 27 September 2026**

This is the current engineering handover for GUTS. It is intended to let Stanley, a replacement developer, or a fresh AI resume without reconstructing the project from chat history.

## 0. Authority and reading order

Read in this order before changing code:

1. `GUTS_HANDOVER_2026-09-27.md` — this file.
2. `GUTS_CURRENT_STATE.md` — concise current production truth.
3. `BABYS_FIRST_GUTS.md` — Stanley-level map of the system.
4. `GUTS_PERFORMANCE_FLOW_POV_v1.md` — performance logic and spectator POV.
5. Current `index.html` and `public/index.html`.
6. Current `src/worker.js` and root `wrangler.jsonc`.
7. `PERFORMANCE35/BUILD_REPORT.md`, `PERFORMANCE35/AUDIT.md`, `PERFORMANCE35/STRUCTURE_REPORT.md`.
8. Historical engineering references as needed: `README.md`, `ENGINE_v0.1.md`, `CLOUDFLARE_BRIDGE_v0.1.md`, `H2_PUSH_SEAM_v0.1.md`, and `LEGACY_DO_NOT_DEPLOY/cloudflare/README.md`.

Older files are history, not automatically current truth. In particular `IF_CHATGPT_DIES_READ_THIS.md` is a valuable 24 September handover but its v0.26 resume point is obsolete. `CURRENT_STATE.md` and old README checkpoints may likewise describe earlier builds.

## 1. Current verified production state

- Spectator Reader: **GUTS 0.35**.
- Production domain: `gutenbrg.com`.
- Worker name: `guts`.
- KV binding: `GUTS_STATE`.
- Current Reader metadata identifies `v0.35-performance-reader`.
- Visible footer/build stamp reads **0.35**.
- Stanley performed compact actual-phone QA after final cleanup and reported all visible tests passed: Landing, carousel/bounce, book → Contents → chapter, page movement both ways, return to Landing.
- Landing overscroll material, cover → Contents slide, and page-flick slide are already implemented and working. Do not resurrect them as TODOs.
- Final diagnostic cleanup is complete.

### Frozen rollback baseline

Branch: `GUTS-035-KNOWN-GOOD`

Preserve it. Git history and Cloudflare deployment/version history are additional rollback paths.

## 2. What GUTS is

GUTS = **Gutenberg Utility Title System**. It is the spectator-own-phone descendant/extension of NoBo NoFo.

The performer secretly supplies a chosen word. The spectator uses their own phone and apparently wanders through an ordinary Gutenberg/free-books route, chooses a book and chapter/page, and encounters that word in plausible book text.

Engineering doctrine:

**H2 PUSHES — GUT PULLS.**

The P phone pushes tiny state to Cloudflare. The spectator Reader pulls it. There is no direct P-phone-to-Sp-phone link.

## 3. System map

### P phone / performer side

Performer UI/code lives primarily in separate repository:

`stanjarin/NoBoNoFo`

The existing NoBo/H2G2 covert input is the performer surface. Do not replace it merely because GUTS is being developed.

### GitHub

`stanjarin/GUTS` is the GUTS source/workshop/archive. It contains Reader code, corpus/build products, artwork, Worker source/config, workflows, and documentation.

GitHub is not the live secret messenger during performance.

### Cloudflare

Cloudflare does two core jobs:

**HOST WEBSITE + REMEMBER WORD.**

The Worker handles API/state/session/mode routes and then serves static assets through the `ASSETS` binding.

### Spectator route

Conceptual visible chain:

Resources Pre-Page → GUTENBRG Landing → carousel / choose book → full cover → Contents → chapter/reader → payoff → real Gutenberg when required.

`gutenbrg.com` is ours. `gutenberg.org` is real Project Gutenberg.

The short spectator route historically/currently documented is `tinyurl.com/ebooks-0`; verify the redirect before changing or printing it anywhere permanent.

## 4. Current production files and paths

### Reader/static source

Root `index.html` is a source/canonical Reader copy used by build tooling.

**Cloudflare production currently serves `./public`**, as declared in root `wrangler.jsonc`. Therefore `public/index.html` is the served Reader copy.

This distinction caused the September 0.35 stamp incident. A workflow changed root `index.html` while Cloudflare served `public/index.html`.

**Rule: never assume changing root `index.html` changes production. Keep root and `public/index.html` intentionally synchronised when a Reader change is meant to ship.**

The retained `.github/workflows/guts035_deploy.yml` is manual/recovery-only and now checks the 0.35 marker/stamp and synchronises the served copy rather than blindly manufacturing a build.

### Worker

Current production Worker source in the root deployment path:

`src/worker.js`

Current root deployment config:

`wrangler.jsonc`

Root config uses:

- Worker `guts`
- main `./src/worker.js`
- assets `./public`
- binding `ASSETS`
- `run_worker_first: true`
- KV binding `GUTS_STATE`

### Legacy Cloudflare material — quarantined

The former root `cloudflare/` directory has been moved intact to `LEGACY_DO_NOT_DEPLOY/cloudflare/`.

It contains older/reference Worker deployment material including `LEGACY_DO_NOT_DEPLOY/cloudflare/wrangler.toml` and `LEGACY_DO_NOT_DEPLOY/cloudflare/src/`.

Important: that legacy config serves `..`, not `./public`, and explicitly contains `keep_vars = true` plus required-secret documentation. It is **not the current production deployment path and must not be deployed accidentally**. Current production uses root `wrangler.jsonc` and root `src/worker.js`.

The old `LEGACY_DO_NOT_DEPLOY/cloudflare/README.md` describes an earlier single-global-state contract and says PAID is local. Current root Worker has since grown session/alias/rehearsal routes; inspect `src/worker.js` rather than treating the old README as exhaustive.

Completed one-shot 0.34/0.35 repair workflows have likewise been moved under `LEGACY_DO_NOT_DEPLOY/.github/workflows/`. See `LEGACY_DO_NOT_DEPLOY/README.md` before using anything in the quarantine directory.

## 5. Runtime bindings / secrets

Known runtime names:

- `GUTS_STATE` — KV namespace binding.
- `GUTS_PUSH_SECRET` — encrypted secret for authenticated `/api/state` push.
- `GUTS_ARM_PIN` — performer/session/alias arming PIN variable/secret binding.
- `GUTS_SITE_PIN` — rehearsal/site-mode PIN variable/secret binding.

Actual values belong only in Cloudflare/private configuration. Never put them in GitHub docs, Reader JavaScript, screenshots intended for public distribution, or handover text.

The KV namespace ID is present in deployment config; secret values are not.

## 6. Current Worker contract — verified from `src/worker.js`

The Worker currently supports both the original global-state seam and newer session/alias machinery.

### Global state

KV key `current` stores `{phase, word, revision, updatedAt}`.

`GET /api/state` — public current global state.

`POST /api/state` — authenticated with `Authorization: Bearer GUTS_PUSH_SECRET`; accepts READY / ARMED / CLEAN. ARMED requires a word.

`POST /api/performer/state` — performer-origin route restricted by CORS to `https://stanjarin.github.io`; PIN-protected by `GUTS_ARM_PIN`; accepts ARMED / CLEAN.

### Session/alias state

Session KV keys are `session:<id>` with 86400-second TTL.

Alias KV keys are `alias:<alias>`.

Current allowed aliases in Worker source are `shortcuts` and `test-p2`.

Relevant routes:

- `POST /api/alias/bootstrap`
- `POST /api/alias/state`
- `/entry/<alias>`
- `POST /api/session/create`
- `GET /api/session/state`
- `POST /api/performer/session`
- `GET /api/join?t=<ticket>`

Spectator session identity is stored in HttpOnly cookie `guts_session`.

Do not casually unify/remove the global and session paths because both may support established performer/rehearsal/test flows.

### SHOW / REHEARSAL

KV key `site-mode` stores SHOW or REHEARSAL.

`/performer/rehearsal` provides a PIN-gated rehearsal entry.

`/api/performer/mode` provides performer mode GET/POST and uses `GUTS_SITE_PIN`.

When site mode is REHEARSAL, a browser without the `guts_rehearsal=1` cookie is redirected to real `https://www.gutenberg.org/`, preserving path/query where applicable. An authorised rehearsal browser receives the GUTS assets.

This is camouflage/access behaviour. Do not simplify it without understanding the performance consequence.

## 7. Local Reader state / payoff doctrine

The remote transport deliberately stays small. Historical/current architecture distinguishes remote READY/ARMED/CLEAN from local Reader payoff behaviour such as PAID, selected page/chapter, dwell and persistence.

Canonical socket marker: `$$$`.

The prepared Reader substitutes the armed word into the appropriate force paragraph/socket. Chapter-opening protection, dwell and payoff persistence were signed off earlier. Do not reopen them merely because a UI, corpus, artwork or deployment issue appears.

Before altering state behaviour, read `GUTS_PERFORMANCE_FLOW_POV_v1.md`, current Reader JavaScript, and the relevant later README checkpoints.

## 8. PERFORMANCE35 corpus

`PERFORMANCE35/` is the current 0.35 performance corpus/build area.

The 0.35 build report verifies eight performance-built titles and deliberately excludes Parker.

Built titles represented in the report:

- A. A. Milne — *The House at Pooh Corner*
- Agatha Christie — *The Murder at the Vicarage*
- Damon Runyon — *On Broadway*
- James Joyce — *Ulysses*
- James Thurber — *My Life and Hard Times*
- P. G. Wodehouse — *Right Ho, Jeeves!*
- Mark Twain — *Adventures of Huckleberry Finn*
- Ernest Hemingway — *A Farewell to Arms*

The build report's QA invariants include:

- source masters not modified
- no invented/repeated genuine prose
- chapters under the build threshold cut
- retained chapters at least three pages
- one air-lock in each prepared page's `force_paragraphs`
- air-lock after genuine opening/carry material
- staggered carry split lengths

Use the actual current builder/audit files and reports rather than reproducing these rules from memory when adding a title.

## 9. Parker and library expansion

Dorothy Parker / `dp` / *Men I’m Not Married To* is **intentionally a placeholder**.

Do not repair or PERFORMANCE35-build Parker. The title has unsuitable extremely short / one-line chapter structures for the plausible GUTS page/book model.

Eventual action: replace Parker with a structurally suitable Gutenberg title.

The library is not architecturally fixed at nine books. Stanley may expand the choice to **about 12 books**, which is considered ample.

For a new title, expect work in these categories:

1. choose a legally/source-suitable Gutenberg title with usable chapter structure
2. ingest/retain source master
3. apply the established PERFORMANCE35 pagination/air-lock/socket process
4. inspect Contents/chapter plausibility
5. add metadata/data mapping
6. make/add full cover artwork and carousel representation
7. update carousel hit mapping/selection mapping
8. include required static/corpus assets in the production `public` bundle
9. run mechanical audit before visible QA
10. deploy in a small pass and test on phone

Core Worker/KV/state architecture should not need redesign merely to add books. Around 12 books, presentation/carousel geometry is the likely practical constraint, not the magic transport.

## 10. Artwork / UI assets

Stanley's visual artwork is production material, not disposable scaffolding. Existing named assets include Pre-Page, Landing, Carousel, Suggestions and full-size book covers. Inspect current root/public trees before recreating anything.

Historical handover explicitly warns: do not reconstruct canonical artwork from HTML/CSS when the finished image asset exists.

Current signed-off UI includes:

- Landing
- carousel with touch/bounce behaviour
- cover selection/hit mapping
- cover → Contents slide
- Contents → reader
- page-flick slide
- extra harmless Landing material for casual overscroll

Do not “polish” deliberate Gutenberg ugliness merely because it looks inconsistent. Camouflage includes plausible institutional/web clunk.

## 11. Deployment and Cloudflare rules

### September 0.35 stamp incident

0.35 was live but the visible build stamp still said 0.34. The Reader's internal metadata was already `v0.35-performance-reader`; only the badge lied.

Durable diagnostic rule:

**When a visible version number disagrees with expectation, first determine what code generates that visible number. Do not immediately blame DNS/cache/Worker propagation.**

### Root/public trap

Cloudflare currently serves `public`. A workflow that updates only root `index.html` can leave production unchanged or labels out of sync.

### Reading Cloudflare deployments

Cloudflare Overview may show a stale/misleading traffic percentage. During the incident it showed 0% while **View all deployments** showed the same version at 100% and active.

If they disagree, use **View all deployments** as the traffic authority.

Whenever Stanley is asked to inspect Cloudflare, give him the **exact human-readable deployment/commit description/name tag** to look for. Do not send him hunting by SHA or “latest”.

### Deployment discipline

- Prefer targeted commits.
- Use multi-pass work for risky changes.
- Internally inspect between passes.
- Bring Stanley in only for compact final phone QA unless his device is genuinely needed earlier.
- Never require a full state-chain retest solely because a cosmetic/diagnostic file changed.
- Never make multiple unrelated production changes merely to save a deployment.

## 12. GitHub workflows — caution

Active `.github/workflows/` contains the workflows retained as current/recovery/build/audit tooling. Completed one-shot repair workflows removed from the active workflow directory are preserved under `LEGACY_DO_NOT_DEPLOY/.github/workflows/` for provenance only.

Do not assume any workflow is safe to run merely because it exists. Read it first and determine whether it is current production/recovery tooling or a builder/auditor.

The retained `guts035_deploy.yml` was deliberately converted to manual/recovery-only after the stamp incident.

Anything under `LEGACY_DO_NOT_DEPLOY/` is quarantined historical material and must not be deployed or restored to an active path without deliberate review.

## 13. Known stale documentation / contradictions

A replacement developer must know these exist:

- `IF_CHATGPT_DIES_READ_THIS.md` says current build v0.26 and lists UI defects that have since been fixed. Historical only after this handover.
- Older `CURRENT_STATE.md`/README sections contain earlier checkpoints. Later authority wins.
- `LEGACY_DO_NOT_DEPLOY/cloudflare/README.md` describes an earlier simpler backend contract; current root Worker has additional session/alias/rehearsal machinery.
- `LEGACY_DO_NOT_DEPLOY/cloudflare/wrangler.toml` and root `wrangler.jsonc` describe different asset roots. The former is quarantined historical configuration; current production uses the clean `public` bundle via root `wrangler.jsonc`.

Do not “resolve” these contradictions by deleting history. Use this handover/current-state pair to disambiguate them.

## 14. Secrets, accounts and things Git cannot preserve

A repo clone is not the whole machine. Continuity also requires authorised access to:

- Cloudflare account controlling `gutenbrg.com`
- Worker `guts`
- KV namespace bound as `GUTS_STATE`
- runtime PIN/secret values
- domain/DNS configuration
- GitHub account/repositories
- performer NoBo PWA/repository
- the short-link account if the TinyURL destination ever needs alteration

Do not copy secret values into this handover. A human successor should obtain them through the authorised account/password-management route.

## 15. Recovery procedure

If ChatGPT/history is unavailable:

1. Clone/download `stanjarin/GUTS` and preserve an untouched copy.
2. Read this handover and `GUTS_CURRENT_STATE.md` before touching code.
3. Confirm production `gutenbrg.com` still behaves as 0.35 on a phone.
4. Confirm Cloudflare Worker/KV/runtime bindings exist; do not overwrite secrets while “redeploying”.
5. Use `GUTS-035-KNOWN-GOOD` as the rollback reference if current main is suspect.
6. Compare current main with that branch rather than reconstructing from memory.
7. Make one narrow change or one coherent pass at a time.
8. Verify build/deployment internally.
9. Give Stanley the exact Cloudflare description/name tag if he must inspect deployment status.
10. Finish with a compact actual-phone QA appropriate to what changed.

If a new change breaks production, rollback to known-good history. Do not rebuild GUTS from scratch unless the repository itself is irrecoverable.

## 16. Things not to improve casually

- NoBo performer PWA / H2G2 covert input
- H2 PUSH / GUT PULL architecture
- signed-off READY/ARMED/PAID/CLEAN behaviour
- chapter-opener/payoff protection
- corpus wording/pagination/socket machinery
- deliberate Gutenberg camouflage/ugliness
- production artwork
- rollback branch

## 17. Immediate future work

There is no outstanding emergency repair after 0.35.

Likely future work is deliberate product development, especially:

- replace Parker with a suitable title
- possibly expand the library toward roughly 12 books
- create corresponding covers/carousel art and mappings
- continue editorial/visual refinement only where Stanley identifies an actual need

Do not manufacture work from stale TODO lists.

## 18. Legacy quarantine

`LEGACY_DO_NOT_DEPLOY/` is the repository junk drawer for material deliberately removed from active production paths while preserving provenance/recovery history.

Its contents are not current instructions. Read `LEGACY_DO_NOT_DEPLOY/README.md` before touching them. Nothing inside that directory should be deployed, copied back into an active path, or treated as production authority merely because it once was.

---

**Current recovery sentence:** GUTS 0.35 is the verified phone-tested production baseline; root `wrangler.jsonc` + root `src/worker.js` + `public/` are the active Cloudflare deployment path; `GUTS-035-KNOWN-GOOD` is the frozen rollback branch; obsolete alternate Cloudflare material and completed one-shot repair workflows live under `LEGACY_DO_NOT_DEPLOY/`; preserve signed-off magic/state/corpus behaviour and make future changes narrowly.