# GUTS review-stage JSON overrides

**Scope: GitHub Pages staging only, never `main`, `ebooks.fyi`, or live NoBo.**

Staging workflow: `.github/workflows/stable-staging-2026-10-08.yml`
Source branch: `factory-autopilot-2026-10-07`
Review URL: https://stanjarin.github.io/GUTS/?browse=1

## Where to upload edited JSON from CP EDIT

In GitHub, choose branch `factory-autopilot-2026-10-07`, upload the CP-edited JSON under **this folder**, preserving the relative path it has in the web Reader:

- Ripley: `staging-overrides/PERFORMANCE10/ripley_performance.json`
- Joyce: `staging-overrides/PERFORMANCE35/jj_035.json` (confirmed against Reader metadata)
- Other books: `staging-overrides/PERFORMANCE10/<filename>.json` or `staging-overrides/PERFORMANCE35/<filename>.json`, exactly matching the Reader's `file` field.

The staging build copies the base `public/` tree, original factory artifacts, recovered artifacts, newest five artifacts (including Ripley HOLD), **then finally `staging-overrides/`**.

An override placed at `staging-overrides/PERFORMANCE10/ripley_performance.json` therefore publishes as `/GUTS/PERFORMANCE10/ripley_performance.json` on staging. Do **not** upload edited JSON only to `public/PERFORMANCE10` or `PERFORMANCE10` and assume it wins; subsequent artifact overlay would replace it.

Changes to `staging-overrides/**` on this branch automatically request a fresh staging build. Confirm Actions deployment success before phone testing and refresh with cache bypass as needed. Old saved browser state may need reset.

## QA and release
- Staging availability is not machine QA PASS and is not production approval.
- Ripley from recovery run 37864168324 is HOLD (ch 1 pp 5-6), included for human visual review.
- Joyce is restored for human phone review; prior QA concerns are not waived.
- Authoritative `main`/live NoBo unaffected. Never auto-promote.
- Upload edited JSON files one by one and record phone PASS / EDIT / HOLD; machine checks must be rerun on the edited candidate before promotion.
