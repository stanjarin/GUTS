# GUTS

GUTS is the spectator-phone development branch of the NoBo NoFo concept.

## Current state — 21 September 2026

The nine-book corpus, force machinery, spectator reader, local performance-state engine and Cloudflare transport seam are built and mechanically QA'd.

Current reader/engine: **v0.23-cloudflare-pull-seam**.

Production deployment is now moving from GitHub Pages development to Cloudflare and the production domain **gutenbrg.com**.

## Library

Nine books, **5,435 reader pages** total:

### Six PRIME2 books

- A. A. Milne — *The House at Pooh Corner* — 203 pages
- Agatha Christie — *The Murder at the Vicarage* — 176 pages
- Dorothy Parker — *Men I’m Not Married To* — 28 pages
- Damon Runyon — *On Broadway* — 1,583 pages
- James Joyce — *Ulysses* — 1,878 pages
- James Thurber — *My Life and Hard Times* — 138 pages

### Three inherited NoBo NoFo books

- P. G. Wodehouse — *Right Ho, Jeeves!* — 379 pages
- Ernest Hemingway — *A Farewell to Arms* — 464 pages
- Mark Twain — *Adventures of Huckleberry Finn* — 586 pages

Mechanical QA: every reader page has force-paragraph data and exactly one canonical `$$$` socket. Zero bad marker pages.

## Force doctrine

The canonical marker is `$$$`.

The force target is paragraph-based. Performance instruction:

> “Now read the first paragraph. No, sorry, the first new paragraph.”

Each page is mechanically primed, but the selected chapter-opening page is protected in the reader: it remains visually clean and cannot qualify for dwell/PAID. The protections are deliberately independent.

Once the force word has been discovered, the selected occurrence persists for that performance session while other sockets remain clean.

## Reader / performance state

The current spectator-phone reader preserves the proven NoBo state logic while keeping the spectator-facing surface clean.

Core phases:

- READY
- ARMED
- PAID
- CLEAN

Desktop Firefox live test passed the protected-opener and payoff sequence:

1. chapter opener clean
2. next eligible page shows the force word
3. dwell qualifies the payoff
4. subsequent page clean
5. returning to payoff page retains the word
6. CLEAN restores pristine text

Development TEST/admin furniture remains intentionally visible for now. Cosmetic polishing is deferred until transport and production hosting are proven.

## Transport doctrine

**H2 PUSHES — GUT PULLS.**

The performer and spectator phones do not communicate directly.

- Performer H2G2 surface pushes the force word to Cloudflare.
- Cloudflare remembers the tiny shared performance state.
- Spectator GUTS browser pulls that state.
- No HTML mutation or redeployment occurs during performance.

Conceptual shared state:

```json
{"state":"ARMED","word":"GOPHERS"}
```

Cloudflare KV is the chosen state store.

The spectator reader has the Cloudflare GET pull seam in v0.23. GitHub Pages development tolerates the absence of `/api/state` harmlessly.

## Cloudflare bridge

Backend files:

- `cloudflare/src/worker.js`
- `cloudflare/wrangler.toml`
- `cloudflare/README.md`
- `CLOUDFLARE_BRIDGE_v0.1.md`
- `H2_PUSH_SEAM_v0.1.md`

Worker API:

- GET `/api/state`
- POST `/api/state`
- KV key: `current`
- Bearer secret: `GUTS_PUSH_SECRET`
- accepted remote phases: READY / ARMED / CLEAN
- ARMED requires a word, maximum 120 characters
- server owns revision and updatedAt
- responses use no-store caching

The H2 push seam is `armMagic(w)` in the NoBo NoFo performer interface. Production will replace/bridge that seam with an authenticated remote push.

**Security rule:** never embed `GUTS_PUSH_SECRET` in public spectator JavaScript or a public GitHub Pages performer surface. The production performer push must be private/authenticated or use a secure server route.

## Production hosting

Development: GitHub Pages.

Production target: Cloudflare + **gutenbrg.com**.

Cloudflare's job is deliberately narrow:

**HOST WEBSITE + REMEMBER WORD.**

The new Cloudflare zone has been rebuilt with the required DNS records and the registrar nameservers have been changed to the new Cloudflare assignment. As of 21 September 2026, delegation propagation is still pending. Do not delete the old Cloudflare zone until the new zone is confirmed Active and the domain resolves correctly.

After propagation:

1. confirm the new zone is Active
2. verify apex and www resolution
3. deploy the real GUTS Worker and KV binding
4. set the push secret securely
5. test H2 push → Cloudflare → GUTS pull end to end
6. deploy static production assets/routes

## Spectator entry / camouflage

The intended spoken route is a saved old Safari bookmark whose visible bookmark title includes the short URL. The performer apparently remembers having a Gutenberg shortcut, finds it among genuine old bookmarks, and reads it aloud.

Current short route:

`is.gd/shortcuts`

The performer intended to send the spectator directly to Gutenberg. Instead the old bookmark lands on a mildly institutional educational **Resources** gateway.

Performance beat:

> “Hang on, I’ve got a shortcut…”
>
> Resources page appears.
>
> “Oh. … OK, that’ll do. Tap any of those.”

The apparent imperfection is intentional camouflage: the route feels remembered rather than prepared.

Only **one** Gutenberg bookmark is required. The premise is that an old saved portal still works, but not quite as directly as remembered.

### Resources gateway

Current visual logic:

- anonymous/wordless crest: implies an already-known institutional context rather than introducing an organisation
- ochre/baby-shit-coloured **Resources** identity: visual bridge toward the following Gutenberg-style page
- heading: **From Project Gutenberg, free books in the public domain**
- deliberately nonessential explanatory subhead: **The world’s great literature available to everyone at no cost or subscription.**
- prompt: **Make a start here:**
- four deliberately old-fashioned blue underlined links:
  - Recent additions
  - Popular titles
  - Reader recommendations
  - Staff picks

The gateway is a conduit to books **from** Project Gutenberg; it does not claim to be Project Gutenberg.

All four links should behave as genuine independent links/touch targets even if they ultimately converge on the same GUTS destination.

Link-state colour doctrine:

- untouched: `#0000EE` — classic browser-link blue
- touch/down: `#FF0000`
- activated/visited: `#551A8B` — classic visited-link purple

If native `:visited` is used, do not give all four links an identical href if independent activated state is required; visited state is URL-based.

## Gutenberg-style landing page

The next page presents the nine-book library in a Gutenberg-like visual language while remaining compatible with the educational gateway framing.

The moving cover field is the canonical `Carousel.png`: background tint + covers + captions move horizontally as one strip.

**Suggestions** is a separate static transparent overlay above the moving carousel.

Important geometry distinction:

- elevation/z-axis: Suggestions is ABOVE the carousel
- page/x-y layout: Suggestions occupies the same physical carousel area while the carousel passes underneath it

Do not rebuild `Carousel.png` from individual cover exports.

## Fixed-art geometry

For rigid portrait phone artwork, current master geometry is:

- MASTER: **2048 × 4210**
- ESSENTIAL: **1804 × 3640**, centred
- approximate sacrificial bleed: 122 px left/right, 285 px top/bottom

Critical art should remain slightly inside the essential boundary where practical.

CSS crop doctrine:

```css
object-fit: cover;
object-position: center center;
```

No device-dependent top bias is intended. Taller/narrower screens lose sides symmetrically; shorter/wider screens lose top/bottom symmetrically.

Phone artwork is intentionally rigid/unresponsive. Tablet and desktop presentation should preserve the phone-shaped composition centrally with gutters rather than expanding the art to fill the device.

Fake web pages may scroll; single-cover/fixed-art screens use the safe/bleed discipline above.

## Asset doctrine

- opaque full-screen cover art: JPEG, typically quality 90–95
- transparency: PNG
- `Carousel.png` remains the canonical complete moving strip
- `Suggestions.png` should be transparent and retain its full positioning canvas; do not trim transparent pixels
- individual covers are exported at 2048 × 4210 with critical content inside the essential area

Binary visual assets are batch-uploaded manually when required; repository wiring follows after upload.

## Development discipline

- Do not reopen already signed-off state mechanics merely because editorial or cosmetic work changes.
- Do not redesign the H2 PUSH / GUT PULL architecture without a demonstrated reason.
- Keep production secrets out of public code.
- Preserve genuine source wording/order in the corpus.
- Treat chapter-opener protection as two independent safeguards: visual eligibility and dwell eligibility.
- Prefer exact, mechanical QA over assumptions.
- Cosmetic polish follows functional transport proof.

## Immediate next stage

Wait for the new Cloudflare nameserver delegation to propagate.

Then verify the production domain and complete the real Worker/KV/secret deployment before wiring the final spectator-facing assets.

