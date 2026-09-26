# GUTS — CURRENT STATE

**Authoritative checkpoint: 27 September 2026**

**For a fresh developer/AI or disaster recovery, read `GUTS_HANDOVER_2026-09-27.md` first, then this file.** The handover contains the full architecture, production paths, Worker routes, corpus/library rules, recovery procedure, stale-document warnings and account dependencies.

This file supersedes stale TODO/current-state material in older README sections and chat history.

## Current production state

- Current spectator Reader: **GUTS 0.35**.
- Production domain: `gutenbrg.com`.
- GUTS 0.35 is working in production and has passed Stanley's compact visible phone QA.
- Visible build stamp correctly reads **0.35**.
- Landing page, carousel/bounce, book → Contents → chapter, page movement in both directions, and return to Landing all passed.
- The previously planned cosmetic work (landing-page overscroll material, cover → Contents slide, page-flick slide behaviour) is **already implemented and working**. Do not put it back on the TODO list.

## Frozen safety baseline

GitHub branch:

`GUTS-035-KNOWN-GOOD`

This is the safety/rollback marker made before final cleanup. Preserve it.

Normal Git history and Cloudflare deployment/version history provide additional rollback paths.

## 26–27 September deployment/stamp incident — resolved

The apparent failure to get 0.35 live was ultimately a display-label bug, not a stale Reader deployment.

The live 0.35 HTML contained the correct metadata marker:

`v0.35-performance-reader`

but its visible footer/build stamp was hard-coded as:

`0.34`

Therefore 0.35 was live while presenting a false 0.34 name badge.

### Durable lesson

When a visible version/build number disagrees with the expected deployment, first establish **what code generates that visible number** before diagnosing DNS, caching, Worker routing, assets, or deployment propagation.

Do not use the visible stamp alone as proof of which corpus/Reader is live.

## Cleanup completed

Temporary diagnostics used during the investigation were removed after 0.35 was proven:

- static `GUTS-ASSET-035` diagnostic removed
- temporary `/__guts_version` Worker diagnostic removed
- one-shot 0.35 stamp-repair workflow removed
- repository audit found no remaining `__guts_version`, `GUTS-ASSET-035`, or lying `buildstamp">0.34` occurrences

Stanley then performed the compact phone QA and reported all tests passed.

## Deployment workflow lesson/fix

The earlier 0.35 deployment workflow modified root `index.html`, while Cloudflare serves the `public` tree. That separation made it possible for source and served Reader copies/version labels to drift.

The retained 0.35 workflow was converted to a **manual/recovery-only** workflow. It now:

- requires an existing `v0.35-performance-reader` marker
- refuses an unknown Reader state rather than manufacturing one
- enforces the visible 0.35 build stamp
- synchronises root `index.html` to `public/index.html`
- commits only if a synchronisation change is actually required

Do not reintroduce a workflow that updates only root `index.html` while production serves `public/index.html`.

## Cloudflare deployment-reading rule

Cloudflare Overview can show stale/misleading traffic percentages. During the stamp repair, Overview showed a new version at 0% while **View all deployments** showed that same version at 100% and active.

When checking a deployment, use **View all deployments** as the authoritative traffic view if Overview disagrees.

When asking Stanley to inspect Cloudflare, always give him the **exact human-readable Cloudflare/Git commit description/name tag to look for**, not merely a SHA, version ID, or “latest deployment.”

## Parker placeholder / library expansion

Dorothy Parker / `dp` (*Men I’m Not Married To*) is **intentionally a placeholder** in the current 0.35 library. Do not spend development time repairing or PERFORMANCE35-building Parker.

Reason: the title contains unsuitable extremely short / one-line chapter structures, which do not fit the plausible GUTS book/page performance model. Parker is therefore a marked seat awaiting a different Gutenberg title.

The eventual task is to **replace Parker with a structurally suitable title**, not to fix Parker.

The library is also intentionally allowed to grow rather than remaining locked at nine books. Stanley may broaden spectator choice to **up to about 12 books**, which is considered ample. New books should use the established PERFORMANCE35 production treatment and common GUTS state/transport architecture; they do not require a new magic/state system merely because the library grows.

Practical expansion work per title includes suitable source selection, chapter/Contents structure, PERFORMANCE35 pagination and socket/force-paragraph preparation, cover/carousel entry and hit target, and mechanical QA. If library growth creates a limit, expect the first constraint to be landing/carousel presentation rather than the core ARMED/CLEAN/PAID or Cloudflare/KV architecture.

## Signed-off / do not reopen casually

- 0.35 visible Reader baseline
- landing/carousel presentation
- cover → Contents transition
- page-flick transition
- Cloudflare production domain/Worker/static hosting path
- established GUTS transport/state architecture
- corpus merely because a UI/deployment issue appears

Functional/state machinery was not deliberately changed during the final visible cleanup. Do not demand a full ARMED → PAID state-chain retest solely because cosmetic/diagnostic files were removed.

## Resume discipline

Before doing new GUTS work:

1. Read `GUTS_HANDOVER_2026-09-27.md`, then this file.
2. Treat `GUTS-035-KNOWN-GOOD` as the rollback baseline.
3. Determine the actual next outstanding item from current code/project notes; do not resurrect old TODO items from chat.
4. Use multi-pass changes for risky work, with internal inspection between passes and Stanley brought in only for the compact final visible test unless his phone is genuinely required earlier.
5. Preserve exact deployment name tags in handoff/testing instructions.

## Status at checkpoint

**GUTS 0.35: WORKING / CLEANUP COMPLETE / USER VISIBLE QA PASSED.**

No further housekeeping is required merely to finish the 0.35 cleanup episode.
