# GUTS — working parlour

> **CURRENT OPERATIONAL HANDOVER (9 Oct 2026): Read [OPERATIONS_START_HERE.md](OPERATIONS_START_HERE.md) FIRST.** It supersedes historical startup pointers below. Cloudflare auto-deploys GUTS Main; the next job is the read-only above-the-fold retention flight-simulator pilot.

**One working branch:** [main](https://github.com/stanjarin/GUTS/tree/main).

**18 books:** `public/PERFORMANCE10/` (10) and `public/PERFORMANCE35/` (8). They are JSON corpus files, not two grades of book. The Reader points to these locations.

**Reader:** `public/index.html` (and the mirrored `index.html`, `public/project_library/books/browse/index.html`); assets and covers in `public/`.

**NoBo ↔ GUTS:** `src/worker.js` with `wrangler.jsonc`. NoBo controls SHOW/HIDE, GUTS executes. Changes to this repository alone **do not certify or deploy** a new Cloudflare release.

**Edit a book:** In CP EDIT, export its JSON, then update the matching filepath under `public/PERFORMANCE10/` or `public/PERFORMANCE35/` on main. Keep the root-level `PERFORMANCE10/` or `PERFORMANCE35/` mirror identical until the processing machinery is retired. Review on the phone; don't treat automated factory QA as spectator approval.

**Current review state:** 18 Reader entries, Joyce enabled. Ripley is available but remains a machine QA HOLD (chapter 1, pages 5–6). Editorial phone review of all 18 outstanding. No automatic production promotion.

## Safety and archive

- **Full Main snapshot immediately before parlour cleanup:** [archive-full-main-before-parlour-cleanup-2026-10-09](https://github.com/stanjarin/GUTS/tree/archive-full-main-before-parlour-cleanup-2026-10-09).
- **Verified earlier production backup:** [backup-production-main-2026-10-09](https://github.com/stanjarin/GUTS/tree/backup-production-main-2026-10-09).
- Read `GUTS_WORKFLOW_CONSTITUTION.md`, `GUTS_CURRENT_STATE.md`, and `docs/CURRENT_STATE.md` for engineering invariants and actual release state.
- Historical notes, old workbooks, tests and build materials are preserved in the full archive branch. Historical `LEGACY_DO_NOT_DEPLOY/` and `FORMAT1/` content was retired from Main and remains in the full archive branch.

**Principle:** Working files stay at their expected paths; archives and documentation never get to dictate runtime. One backup, one working Main.
