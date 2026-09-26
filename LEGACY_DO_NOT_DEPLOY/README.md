# LEGACY / JUNK DRAWER — DO NOT DEPLOY

This directory contains files confirmed obsolete for current GUTS 0.35 production but retained for archaeology/recovery context.

Current production authority remains at repo root: `wrangler.jsonc`, `src/worker.js`, `public/`, `GUTS_HANDOVER_2026-09-27.md`, and `GUTS_CURRENT_STATE.md`.

## Retired Cloudflare deployment tree

Moved here after confirming current production uses root `wrangler.jsonc` + root `src/worker.js` + `./public` assets and finding no current code reference to the old `cloudflare/wrangler.toml` path.

- `cloudflare/wrangler.toml` — older deployment config; notably preserved PIN/secret bindings with `keep_vars = true`, but serves a different asset root and is not the current production config.
- `cloudflare/src/worker.js` — older duplicate/reference Worker tree superseded by root `src/worker.js`.
- `cloudflare/README.md` — older backend contract, superseded by the current Worker and handover.

## Retired one-shot workflows

These were completed repair workflows that trigger only when their own workflow file is pushed. They are preserved here so they cannot be mistaken for current runnable tooling:

- `workflows/guts034.yml` — obsolete 0.34 patch.
- `workflows/guts035_carousel_fix.yml` — completed one-shot carousel repair; current carousel passed phone QA.
- `workflows/guts035_restore_parker.yml` — completed one-shot restoration/Parker-placeholder repair; Parker's current placeholder status is documented separately.
- `workflows/guts035_structure_fix.yml` — completed one-shot Joyce/Runyon structure repair; its resulting corpus/report remains in PERFORMANCE35.

## Deliberately NOT moved

When classification was uncertain or the file could still be useful for current build/recovery work, it was left in place. In particular:

- `.github/workflows/guts035_build.yml` — retained; current PERFORMANCE35 build machinery may be useful for replacement/additional books.
- `.github/workflows/guts035_audit.yml` — retained; current audit machinery may be useful for corpus QA.
- `.github/workflows/guts035_deploy.yml` — retained; intentionally converted to manual/recovery-only synchronisation tooling.
- old project documentation/source/build directories were left in place where their future recovery/editorial value was not conclusively disposable.

Rule for this drawer: **history only; never deploy/run directly from here.**
