# GUTS + NoBo — OPERATIONS START HERE
**Verified against GitHub main on 9 October 2026. Read this FIRST in every new thread.**
This is the CURRENT OPERATING MANUAL, not a historical development narrative.

## The five facts an incoming assistant must know without rediscovery
1. **GUTS source:** https://github.com/stanjarin/GUTS — working branch **main**. **NoBo source:** https://github.com/stanjarin/NoBoNoFo — working branch **main**. Do not confuse with NoBoNoFo-QA or old staging branches.
2. **YES, CLOUDFLARE IS ALREADY CONNECTED TO GITHUB MAIN AND AUTOMATICALLY BUILDS/DEPLOYS THE PRODUCTION GUTS WORKER.** User directly showed Cloudflare > Workers & Pages > guts > Overview / Deployments; latest four-hotspot commit `d9813d0` had successful green build. Stop telling user that GitHub cannot deploy Cloudflare or proposing a new workflow. Source commit is NOT enough to guarantee live success; verify latest Cloudflare build when necessary.
3. **Cloudflare Worker `guts` serves `ebooks.fyi`, `www3.library.gutenbrg.com`, `www3.gutenbrg.com`, `gutenbrg.com`, and `guts.stanjarin.workers.dev`.** Domains are aliases on the same Worker, NOT separate source branches or separate book versions. Assets binding `ASSETS`; KV binding `GUTS_STATE`. `wrangler.jsonc`: `src/worker.js`, assets from `public/`, Worker-first.
4. **One current 18-book Reader on GUTS main.** Reader code identical/mirrored in `public/index.html`, `index.html`, `public/project_library/books/browse/index.html`. Its book metadata points to 10 JSONs under `public/PERFORMANCE10/` and 8 under `public/PERFORMANCE35/`. Corresponding root-level PERFORMANCE folders are mirrors for historical processing and must stay in sync for edits. The labels 10/35 are legacy folder names, not quality categories. Joyce restored, Ripley present but its machine recovery result had HOLD around chapter 1 pages 5–6. All books visible on user's phone.
5. **The full phone-tested performance path works.** NoBo → `ebooks.fyi` pre-page → four separate hotspots → `www3.library.gutenbrg.com/project_library/books/browse/` → GUTS. NoBo SHW serves GUTS. NoBo HIDD serves THE SAME pre-page on `ebooks.fyi`, then any hotspot goes to genuine `www.gutenberg.org`. User personally verified both SHW and HIDD on phone 9 Oct; BR+ browsing and literal `$$$` substitution worked. NoBo commands; GUTS executes.

## Actual control behavior — DO NOT REINVENT
- NoBo main source `index.html` has `const GUTS_BASE="https://ebooks.fyi";`; build `v6.20P` in source, phone UI may show `v6.20Q` (investigate caching rather than presume deployed source identity).
- SHW/HIDD are visibility states `SHOW` / `REHEARSAL` on GUTS Worker. ARM and READY are separate magic states. BR−/BR+ is a *local NoBo browse-mode toggle* and does NOT contain a direct navigation or workers.dev URL in current NoBo main. If BR+ visible, user expects literal `$$$` rather than armed substitution and no 6-second PAID dwell.
- `workers.dev` is a Cloudflare alias on the SAME Worker. A phone once showed it; another entry showed the correct `www3.library.gutenbrg.com` camouflage address. No hard-coded `workers.dev` was found in current GUTS Reader or NoBo main. Do not infer a stray branch/ant tunnel without evidence.
- In HIDD, Worker allows `ebooks.fyi/` and `ebooks.fyi/Pre-Page.jpg` for ordinary visitors, redirects all other routes to genuine Gutenberg. An authorised rehearsal cookie may bypass HIDD; do not conflate that with BR+.
- Known pre-page hotspots are four independent hit regions, all same link in SHW and all route to genuine Gutenberg in HIDD. Artwork labels: Recent additions; Popular titles; Reader recommendations; Staff picks. NO remapping to four sites.
- Credentials: two performer PIN functions SHOW and ARM, not a third "site" PIN. DO NOT put secret values in documents or chat. Pending nonurgent issue https://github.com/stanjarin/GUTS/issues/5 is to accept capital initial without breaking lowercase.

## Backup and deployment safety
- Pre-consolidation Main immutable backup `backup-production-main-2026-10-09` anchored `e5856d8bdd53f08218febe8c2ac039e77edc7bce`.
- Full before-cleanup archive `archive-full-main-before-parlour-cleanup-2026-10-09`.
- Pre HIDD-prepage Worker edit backup `backup-pre-hidd-prepage-2026-10-09`.
- Current GUTS main at manual authoring time `7d2dab2b4c5a3d6c9937f0fb3123dd26e2606d4e` (verify live branch SHA on entry; docs updates advance it). NoBo main `e582c042a3938b806a25b35d7d728e60198430a0`.
- GUTS commit that added HIDD-prepage Worker routing `7d2dab2b`; Cloudflare automatic connection confirmed by user's deployment screenshots for earlier hotspot changes. User confirmed HIDD prepage → real Gutenberg worked after this commit.
- Preserve bindings, KV, worker domain attachment, and NoBo protocol. Check Cloudflare dashboard build on changed main; phone QA remains final acceptance. Reuse verified backups, don't proliferate scaffolding.
- Repo cleaned: obsolete FORMAT1 and LEGACY_DO_NOT_DEPLOY are now stored on archive branch; Main keeps functional paths plus remaining historical notes.

## EXACT NEXT JOB — 9 OCT: Read-only visual flight simulator pilot
**Problem:** User cannot inspect ~4,858 prepared pages manually; preliminary phone browsing reveals retention-of-vision faults: literal `$$$` on consecutive pages in almost the same VERTICAL visible position, especially ABOVE THE FOLD. This is NOT repeated prose or browser page persistence.
**Only QA priority:** above-the-fold consecutive-page positional retention. Gutenberg's imperfect OCR, shorter pages, other typographic roughness are acceptable. Four-rendered-line minimum stagger between visible socket positions was the earlier target, but prior word-depth audits did not correspond to actual rendered placement.
**Plan:** investigate whether actual GUTS Reader can be rendered in a browser with iPhone 8 Plus-equivalent viewport, Georgia/fixed-measure CSS, source pages and browse socket behavior. Make ONE book pilot (Jean Brodie is a candidate). Capture screenshots/positions of adjacent `$$$` pages; calibrate against user-observed bad pairs BEFORE scanning all 18. Return compact flagged page-pair screenshots; never run automated repair or giant report factory by default. Avoid large corpus dumps and bandwidth overruns.
**At handover:** This pilot has NOT been implemented. Do not describe it as complete. Begin by inspecting the current Reader and sample corpus and establishing a faithful rendering harness; collect one known offender if needed.
**Observed oddity:** Jean Brodie showed no `$$$` at first; toggling BR− then BR+ restored sockets and entered GUTS using workers.dev alias. This may indicate phone session refresh; source audit did not prove BR+ initiates navigation.
**Separate sidetrack:** Internet Archive 'Collection ... | Crawling' popups likely JDownloader running on user's older Mac; user quit it to see if popups stop. Not part of GUTS.

## Communication contract
- User prefers concise, direct, lightly wry discussion, no excessive persona sign-offs or repetitive sheep/robot shtick.
- **DON'T ANNOUNCE INACTION** ("no changes made", "I haven't touched main" etc.) unless essential for safety. Report findings, changes and next steps. This is a user-stated durable bandwidth rule.
- **My Job / Your Job** at genuine operational handoff is useful; do not repeatedly ask GO to perform already authorised work. Never imply background work.
- User's 3058-out checkpoint rule: create dated GitHub checkpoint, update CURRENT_STATE if canonical state changed, verify writes; final wording preference from prior context is “Have you ejected WD3? / Latitude 90° North out.” Never claim saved if unverified.
- New assistant must **READ** this file, GUTS_README and current-state, relevant NoBo actual source, and VERIFY Github deployment facts *before proposing architectural changes*. Historical docs are archives, not current authority.

## Startup acceptance drill (before taking action)
Report briefly and concretely: ① two repo names/main heads; ② Cloudflare automatic main→guts production deploy and aliases; ③ SHW vs HIDD pre-page behavior; ④ meaning of BR+ and `$$$`; ⑤ where the 18 JSONs are; ⑥ precise pending flight-simulator pilot; ⑦ unresolved vs verified facts. Then perform the pilot when instructed. **Do not spend an hour rediscovering Cloudflare.**
