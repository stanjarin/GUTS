# 10 October 2026 — Top-airlock experimental edition APPROVED AND FROZEN

## Authority and boundaries
- User actual-phone verdict: **"Perfect. Well, perfect enough."** after Kon-Tiki repair.
- Immutable content/runtime commit: `1ae4abe1e1f3ce83c996d932fa5bdcbb8fc95601`.
- Frozen rollback branch: `freeze-top-airlock-approved-2026-10-10` (same SHA).
- Development/preview branch: `experiment-top-airlock-2026-10-10`; stop editing approved code without a new observed defect.
- Preview: https://stanjarin.github.io/GUTS/top-airlock/?browse=1
- Main and Cloudflare production source remain at `06086d6c1290692d283a6a855cc12cf8a4485143`; NoBo unchanged.

## Approved design STANdard
"It should need less machinery, not more. We must resist rebuilding the elaborate system we've just made unnecessary."

The 18 book-specific approved airlocks stay verbatim. Each prepared page, including chapter openings, places airlock as first **prose** paragraph; legitimate headings/subtitles before it; remainder starts a fresh sentence. User accepts rough Gutenberg source and mild linguistic awkwardness as prototype. Kon-Tiki specifically suppresses giant subheading slabs on its eight chapter-opening pages, including extra second slab on chapter 7, and normalises initial all-caps source words.

## Evidence
- 18 books / 4,858 pages browser inventory: 4,858 visible airlocks, 0 missing, 0 invalid following sentence starts: Actions run `38035001251`.
- 18-book browser smoke test: run `38036671495`.
- Kon-Tiki eight chapter openings QA: `38040653664`.
- Latest approved preview deployment: `38040688382` SUCCESS.
- User actual-phone QA: first all-books principle works beautifully, Kon-Tiki corrected and accepted.

## Integration reconnaissance — READ ONLY
- Production NoBo already commands GUTS with READY / ARMED + force word; GUTS locally handles 6s dwell, PAID and reset. Do not rebuild protocol.
- Production Reader `visible(p)` presently protects selected chapter opener; production `dwell()` also excludes that opener. The experimental Reader changes the display rule and has a partial change to dwell; do not promote without verifying actual remote ARMED, substitution, selected first page, 6s dwell, PAID and RSET end-to-end.
- Experimental preview uses `<base href="/GUTS/top-airlock/">`, unlike live production's `<base href="/">`. Never copy directly into production without adapting the base/deployment route.
- GitHub Pages browse preview doesn't prove the authenticated Worker API or local PAID flow; it substitutes literal `$$$` in browse mode by design.
- Need only Reader delta and deployment path checks, not corpus re-pagination, retention/pump/short-page repair.
- No production changes authorised yet. Investigate isolated end-to-end test route before any merge or promotion.

## Next action
Specify a minimum-surface, isolated NoBo→GUTS full-chain rehearsal plan using existing controls and Word/KV; seek approval prior to any production promotion. Retain frozen rollback intact.


## Isolated Reader protocol rehearsal — 10 October (same day)
- Test workflow: `rehearse-nobo-top-airlock.yml`; PASS [Actions 38041746845](https://github.com/stanjarin/GUTS/actions/runs/38041746845).
- Browser served local copy of experimental Reader; NoBo command payloads simulated in-browser and `/api/state` intercepted to prevent any live Worker/KV traffic.
- Ripley chapter 1 opening tested: READY (clear) → ARMED + GOPHERS (substitute) → 6s dwell (qualified) → depart (PAID) → paid-page persistence → newer READY clears.
- This is **not** proof that the live NoBo app, pre-page handoff, auth cookie, Cloudflare API and Worker routing function against the experimental Github Pages preview; its absolute `/api/state` does not go to production and must not be silently repointed.
- Frozen approved code commit remains `1ae4abe1e1f3ce83c996d932fa5bdcbb8fc95601`; current experiment branch carries *tests/docs only* since that freeze. Main and NoBo unchanged.
- Next step: design a genuine isolated Worker/KV-backed or explicitly approved rehearsal endpoint for phone-to-phone handoff, without touching production domains. Prefer existing machinery and minimal changes; do not conflate simulation with full live integration.
