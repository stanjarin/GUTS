# IF CHATGPT DIES, READ THIS

**GUTS disaster-recovery / human handover — 24 September 2026**

This file exists so the project can continue without the ChatGPT conversation history. **Read this first, then README.md and the named project documents below before changing code.**

## What GUTS is

GUTS is the spectator-phone descendant of NoBo NoFo. The spectator uses **their own phone** and apparently wanders through a Gutenberg/free-books route, chooses a book, chapter and page, then encounters an impossible word in the text. The engineering must disappear in performance.

Production spectator site: `https://gutenbrg.com`

Current short spectator route used in performance: `https://tinyurl.com/ebooks-0`

GitHub repository: `stanjarin/GUTS`

Performer repository: `stanjarin/NoBoNoFo`

## Current build

Current `index.html` identifies itself as:

**v0.26-carousel-motion**

Latest carousel-motion commit at time of this handover:

`207e1849e85c4ba348b24ecb26cfacbde49e84cd`

The production site was successfully serving the real visual-asset chain on an actual phone on 23 September 2026. The v0.26 carousel also moves, but too slowly and still needs finesse.

## Current spectator path

Intended visible chain:

**Resources Pre-Page → Gutenberg-style Landing → moving Carousel / Suggestions → selected full-size book cover → Contents → chapter → reader → force payoff**

The Resources page is intentionally a slightly wrong old institutional shortcut. The performer can apparently give the Resources URL by accident: “Oh wait, that ain’t— ah, it’ll do. Tap one of those.”

The fake/GUTS route is ephemeral camouflage. At the appropriate exit the spectator can end up at real Project Gutenberg, leaving no obvious fake site behind.

Performance target is **phones**. Tablet presentation is not a design requirement. Desktop is principally for development/QA.

## Real visual assets now in repository root

Gateway / landing:

- `Pre-Page.jpg`
- `LANDING PAGE.jpg`
- `Carousel.jpg`
- `Suggestions.png`

Full-size selected-book covers:

- `THURBER.jpg`
- `JEEVES.jpg`
- `HEMINGWAY.jpg`
- `POOH.jpg`
- `HUCK.jpg`
- `PARKER.jpg`
- `RUNYON.jpg`
- `CHRISTIE.jpg`
- `JOYCE.jpg`

**Do not reconstruct these from HTML/CSS if the artwork already exists.** They are Stanley’s production artwork. Revisions should normally be simple asset swaps while preserving filenames/geometry where practical.

`.assetsignore` must explicitly admit any root visual asset that Cloudflare is expected to publish. Merely uploading a file to GitHub does not guarantee Cloudflare serves it.

## Nine books / corpus

The nine books are:

1. James Thurber — *My Life and Hard Times*
2. P. G. Wodehouse — *Right Ho, Jeeves!*
3. Ernest Hemingway — *A Farewell to Arms*
4. A. A. Milne — *The House at Pooh Corner*
5. Mark Twain — *Adventures of Huckleberry Finn*
6. Dorothy Parker — *Men I’m Not Married To*
7. Damon Runyon — *On Broadway*
8. Agatha Christie — *The Murder at the Vicarage*
9. James Joyce — *Ulysses*

Corpus data lives under `PRIMED/`. It has already undergone mechanical socket QA. **Do not rewrite or regenerate the corpus merely to fix UI/runtime bugs.**

## Force architecture — preserve this

Canonical socket marker: `$$$`.

Doctrine:

**H2 PUSHES — GUT PULLS.**

- Performer uses the existing NoBo NoFo H2G2 covert word-entry surface.
- Performer side securely pushes ARMED + word to Cloudflare.
- Cloudflare KV remembers the tiny performance state.
- Spectator GUTS browser pulls it.
- Reader substitutes the force word into the selected canonical socket.
- No performance-time HTML redeploy/mutation is required.

Core local phases are READY / ARMED / PAID / CLEAN.

The selected chapter-opening page is deliberately protected. Payoff/dwell/persistence machinery was proven before the current visual-asset work. **Do not reopen signed-off state machinery merely because a cosmetic/UI change is being made.**

Cloudflare Worker/state details and security rules are documented in:

- `README.md`
- `ENGINE_v0.1.md`
- `CLOUDFLARE_BRIDGE_v0.1.md`
- `H2_PUSH_SEAM_v0.1.md`
- `cloudflare/README.md`

Never put actual PINs or `GUTS_PUSH_SECRET` into public source or documentation.

## Cloudflare production pieces

Production domain: `gutenbrg.com`

Worker: `guts`

KV binding: `GUTS_STATE`

Expected runtime binding names include:

- `GUTS_PUSH_SECRET`
- `GUTS_ARM_PIN`
- `GUTS_SITE_PIN`

`keep_vars = true` was added previously because dashboard PIN bindings had disappeared after deployments. Preserve that protection unless there is a demonstrated reason to change it.

Cloudflare’s job is deliberately narrow:

**HOST WEBSITE + REMEMBER WORD.**

Do not redesign the transport architecture for elegance.

## Current known-good visual state

As of the evening of 23 September 2026, actual-phone testing confirmed:

- Resources/Pre-Page displays.
- Landing artwork displays.
- Carousel artwork displays.
- Visible book hit zones select the corresponding books.
- Selected book opens its correct large cover.
- Tapping the large cover proceeds to Contents.
- v0.26 carousel moves horizontally and reverses, but movement is **too slow**.

The carousel currently measures its actual rendered strip width against the actual viewport/window before animating. This replaced an earlier CSS-only travel calculation that rendered correctly but did not visibly move.

## Exact resume point — morning 24 September 2026

Known UI defects / next work:

1. **Resources Pre-Page:** only the **first** of the four apparent links currently works on the phone. Diagnose the hit-zone geometry/overlay for links 2–4. All four should be independent live touch targets even though they converge on the same landing destination.
2. **Carousel speed:** v0.26 works but is S--L--O--W. Current motion duration is 24 seconds end-to-end. A first candidate is roughly **12 seconds**, but finesse this from the actual phone rather than treating 12 as sacred.
3. **Full dress rehearsal:** after the two UI fixes, perform one complete real-phone run including H2 covert word entry → ARMED → `[WORD]`/`$$$` payoff → dwell → PAID persistence/cleanup. Do not repeatedly reopen the already-proven state chain before the UI is ready.
4. Then finesse transitions, cover slide, spacing/crop and other cosmetics from actual-phone evidence.

## Things not to “improve” casually

- Do not replace the existing NoBo performer PWA.
- Do not rebuild the H2 PUSH / GUT PULL architecture.
- Do not touch corpus wording/order to solve presentation bugs.
- Do not remove chapter-opener protection.
- Do not expose secrets/PINs publicly.
- Do not redesign the fake Gutenberg material into something polished. Some Gutenberg brutality/inconsistency is intentional camouflage.
- Do not rebuild `Carousel.jpg` from individual covers. It is the canonical moving strip artwork.
- `Suggestions.png` is a separate transparent full-format overlay and sits above the moving carousel.
- Do not optimise for tablets. The performance object is a spectator’s phone.
- Prefer a small targeted patch over a broad refactor. **Working weirdness beats elegant destruction.**

## Essential reading order for a replacement developer / AI

1. `IF_CHATGPT_DIES_READ_THIS.md` — this file
2. `README.md` — canonical architecture/state history; note that older sections may be superseded by later continuation checkpoints
3. `GUTS_PERFORMANCE_FLOW_POV_v1.md` — performance logic/POV
4. `ENGINE_v0.1.md`
5. `CLOUDFLARE_BRIDGE_v0.1.md`
6. `H2_PUSH_SEAM_v0.1.md`
7. `cloudflare/README.md`
8. Current `index.html`

Then inspect git history before changing anything.

## Recovery procedure if ChatGPT is unavailable

1. Download/clone `stanjarin/GUTS` to a Mac and keep an untouched backup.
2. Preserve access to the Cloudflare account/domain/Worker/KV configuration. GitHub documents the architecture but does not itself contain the live secret values/state.
3. Give the complete repo to a competent web developer or coding AI and require them to read the files above first.
4. Establish that production `gutenbrg.com` still serves the known-good build before deploying changes.
5. Make one targeted change at a time; commit it; let Cloudflare deploy; test on the actual spectator phone.
6. If something breaks, return to the last known-good Git commit rather than reconstructing the project.

## Philosophy

The spectator should see almost none of the engineering. They invent a sentence/word context, use their own phone, wander through apparently ordinary free books, make free choices, stop somewhere, and encounter the impossibility.

The thousands of pages, sockets, state machine, H2 input, Cloudflare Worker/KV, camouflage and deployment plumbing exist precisely so that **none of the hard work is visible**.
