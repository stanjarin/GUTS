# GUTS — AUTHORITATIVE HANDOVER
## Known-good baseline: 0.32

**READ THIS FILE BEFORE PROPOSING OR CHANGING ANYTHING.**

This is the cockpit card for the current GUTS / Project Gutenberg camouflage build. It does not replace larger project documentation. If chat recollection conflicts with this file about the current implementation state, inspect the live repo/code before acting.

## 1. CURRENT KNOWN-GOOD STATE

Version **0.32** is the handover baseline. Stanley tested the three targeted 0.32 changes on the actual phone and reported: **PASS ALL 3**.

Those three PASS items are:

1. All four Pre-Page choices work, including **Staff Picks**.
2. The redundant **Project Gutenberg** material exposed beneath the carousel on a wrong-direction swipe is hidden/removed from view. Do not restore it; Stanley judged it redundant and over-proving.
3. Reader page turning now responds to a real horizontal finger drag: page follows the finger, sufficient distance/velocity completes the turn, insufficient drag springs back. Vertical scrolling remains available. Edge tap-to-turn remains as fallback.

Other already-passed items to preserve:

- Deep Landing artwork is in place.
- Suggestions overlay is positioned correctly (+4 px from the earlier position).
- Carousel is user-spun, not auto-spun, with iOS-like horizontal behaviour.
- Back navigation functions.
- Visible TEST/development furniture is gone from the spectator screen.
- Landing-only discreet build number is visible; current number is **0.32**, with no `v`.

**Do not casually refactor these passed behaviours.**

## 2. IMMEDIATE NEXT WORK

Next task: **Contents + Reader VISUAL pass.**

The earlier 0.30 attempt at a broad Poet pass was judged a failure wherever Stanley could not see/understand a meaningful visual change. Therefore future visual changes must be concrete and visibly judgeable on the phone.

Do not reopen working plumbing merely because aesthetics are being changed.

## 3. BABY'S FIRST LESSON — ARCHITECTURE

### The three places

1. **P phone** — Performer-side control/input role. This is where the covert force/state originates.
2. **GitHub** — source repository. Current spectator build repo is `stanjarin/GUTS`.
3. **Cloudflare** — deployment/runtime layer serving the spectator-facing site and `/api/state` state endpoint. A GitHub commit is not proof that Stanley's phone has received the deployment; the visible Landing build number is the quick deployment check.

### The five spectator-facing players

1. **P phone** — covert performer control/state.
2. **Gutenberg** — the fake/camouflaged Project Gutenberg experience built in GUTS.
3. **Real Gutenberg** — genuine destination used for the eventual clean exit/leafing strategy.
4. **Pre-Page** — initial Gutenberg-looking gateway with four choices/hotspots.
5. **Sp phone** — spectator's phone, where the fake Gutenberg experience is used.

### Spectator flow

**Pre-Page → Landing/Carousel → selected large Cover → Contents → Reader pages → eventual clean exit to real Gutenberg.**

Landing uses static artwork plus live HTML overlays: carousel, Suggestions and build stamp.

## 4. CURRENT IMPORTANT FILES / ASSETS

Main runtime:

- `index.html`

Landing/gateway assets currently referenced by runtime:

- `Pre-Page.jpg`
- `LANDING PAGE.jpg`
- `Carousel.jpg`
- `Suggestions.png`

Large selected-book covers:

- `THURBER.jpg`
- `JEEVES.jpg`
- `HEMINGWAY.jpg`
- `POOH.jpg`
- `HUCK.jpg`
- `PARKER.jpg`
- `RUNYON.jpg`
- `CHRISTIE.jpg`
- `JOYCE.jpg`

Primed local book data currently referenced includes:

- `PRIMED/AAM_GUTS_PRIME2.json`
- `PRIMED/DP_GUTS_PRIME2.json`
- `PRIMED/DR_GUTS_PRIME2.json`
- `PRIMED/AC_GUTS_PRIME2.json`
- `PRIMED/JJ_GUTS_PRIME2.json`

Some legacy book JSON is currently fetched from `stanjarin/NoBoNoFo` raw GitHub URLs. **Inspect current `index.html` before changing data paths.**

## 5. FORCE / STATE MACHINERY — PRESERVE

Current runtime has performer/spectator state machinery using phases including:

- READY
- ARMED
- PAID
- CLEAN

The spectator polls `/api/state` and stores relevant session state. The force word is inserted into prepared `force_paragraphs`/socket material. Dwell/payoff behaviour and the protected selected chapter opener are part of the machinery.

This machinery descends from the already-developed NoBo NoFo state system. **Do not redesign or reopen it during cosmetic work without a demonstrated failure.**

The broader NoBo principle remains: No Book. No Force. Spectator invents/read-aloud material; performer covertly obtains/selects a distinctive short word; spectator freely chooses book/chapter/page/flick; prepared destinations allow the word to appear; after discovery other sockets clean while the discovered occurrence persists for that session; eventual fake-to-real exit provides a clean genuine-book state.

## 6. MOTION — WHAT WORKED / WHAT FAILED

### Failed approach

0.30 used the Web Animations API (`element.animate(...)`) with relatively subtle movement and a `prefers-reduced-motion` escape. On the actual phone the intended motions were effectively absent. Do not resurrect that implementation as though it were known-good.

### Working tap navigation slides

0.31 changed tap-triggered navigation to full-screen CSS `translate3d()` slides. Stanley reported the swipe/slide animation looked good when triggered by tap. Preserve this mechanism for tap-based navigation such as Cover → Contents and Contents → chapter unless there is a specific reason to change it.

### Working reader swipe

0.32 added touch-driven reader page movement. This is now explicitly **PASS** on Stanley's phone. Preserve it.

Important distinction:

- Cover → Contents / Contents → chapter: tap-triggered full-screen slide is appropriate.
- Reader next/previous: must physically follow horizontal finger drag, then complete or spring back.

## 7. PRE-PAGE HOTSPOTS — HISTORY

Do not assume evenly spaced hotspot geometry from the artwork. Earlier blanket positioning produced only 2/4 and then 3/4 working choices. In 0.32 **Staff Picks was independently repositioned/enlarged and all four passed**.

Do not re-normalise the four hotspot coordinates just because asymmetric CSS looks untidy.

## 8. LANDING / CAROUSEL RULES

- Real Gutenberg-style carousel should sit static until the user touches/spins it.
- It should behave like a familiar horizontal iOS carousel with natural bounceback/scroll feel.
- Suggestions floats above it and has already been moved down by 4 px to clear the carousel background correctly.
- Landing artwork is intentionally deep to allow casual vertical overscroll into plausible Gutenberg/social/footer material.
- No white should reveal above the Landing on upward/top overscroll.
- The material immediately beneath the carousel that exposed another Project Gutenberg element was judged redundant/over-proving and is masked in 0.32. Preserve that result.
- This effect is designed for a **phone**, not a tablet. Do not optimise the performance UI around iPad/tablet use unless Stanley explicitly changes that premise.

## 9. DEVELOPMENT DISCIPLINE

1. **Inspect the current repository/file before editing. Never patch from memory.**
2. Treat **0.32 as known-good baseline** until Stanley reports otherwise.
3. Make small, targeted changes rather than broad speculative rewrites.
4. Preserve things Stanley has explicitly passed.
5. A commit is not a PASS. Stanley's actual phone is the authority.
6. Keep the discreet Landing-only version stamp current: number only (`0.33`, etc.), no visible `v` or descriptive suffix.
7. State exactly what changed and ask Stanley to test only the relevant behaviours.
8. For visual work use **BEFORE → visibly AFTER** thinking. If Stanley cannot notice or understand the intended improvement, regard it as a fail rather than defending it as subtle.
9. Do not expose performer/debug/TEST furniture to Sp.
10. Do not disturb force/state machinery during Poet/cosmetic work without evidence it is implicated.

## 10. GITHUB / ASSET PRACTICALITIES

The available GitHub connector can edit UTF-8 text/code files such as `index.html` directly. Binary artwork replacement has previously required Stanley to upload/replace the JPG/PNG in GitHub himself; after he says it is up, verify the changed file/SHA before proceeding.

When Stanley uploads a replacement asset, keep the agreed filename exact unless there is a deliberate migration.

## 11. RECENT VERSION HISTORY

- **0.29** — revised deep Landing work; Suggestions moved; top Landing behaviour work; discreet version stamp subsequently restored.
- **0.30** — attempted broad Poet pass. Landing/Suggestions and TEST removal succeeded, but many intended motion/visual changes failed or were imperceptible.
- **0.31** — changed animation architecture to full-screen CSS `translate3d()` slides; three Pre-Page choices worked, Staff Picks still failed; tap-triggered slide looked good.
- **0.32** — independently fixed Staff Picks; hid redundant Project Gutenberg exposure beneath carousel; added true touch-drag reader page turning. **Stanley: PASS ALL 3. CURRENT KNOWN-GOOD BASELINE.**

## 12. FIRST ACTION FOR A NEW CHAT

Before suggesting code or asking Stanley to repeat project history:

1. Read this file.
2. Fetch current `index.html` from `stanjarin/GUTS`.
3. Confirm the runtime still identifies itself as 0.32 (or note any later repo state).
4. Then continue with **Contents + Reader visual pass**, unless Stanley gives a different instruction.

Do not make Stanley reconstruct this state from memory.