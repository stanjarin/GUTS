# GUTS

GUTS is the spectator-phone development branch of the NoBo NoFo concept.

## Current state — 22 September 2026

The nine-book corpus, force machinery, spectator reader, local performance-state engine and Cloudflare transport seam are built and mechanically QA'd.

Current reader/engine: **v0.23-cloudflare-pull-seam**.

**Production deployment is LIVE on Cloudflare at `https://gutenbrg.com`.** The Worker, static spectator site, KV state store and custom production domain are connected and the first end-to-end remote force test has passed.

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

Production: Cloudflare + **gutenbrg.com** — **LIVE 22 September 2026**.

Cloudflare's job is deliberately narrow:

**HOST WEBSITE + REMEMBER WORD.**

The new Cloudflare zone is Active on the new account and registrar delegation is complete. The obsolete GoDaddy apex A records (`13.248.243.5` and `76.223.105.230`) were removed, and the root custom domain `gutenbrg.com` is now attached directly to the GUTS Worker. Static assets and `/api/state` are served by the same Worker deployment.

Production proof completed 22 September 2026:

1. real GUTS Worker deployed from GitHub with root directory `/cloudflare`
2. `GUTS_STATE` KV namespace bound successfully
3. encrypted `GUTS_PUSH_SECRET` deployed in Cloudflare
4. authenticated POST armed the live state with `GOPHERS`
5. independent GET returned `ARMED`, `GOPHERS`, revision `1`
6. actual spectator GUTS site pulled the remote state and injected `GOPHERS` into the book corpus
7. `gutenbrg.com` custom domain connected and confirmed serving GUTS successfully

This proves the production chain: **authenticated PUSH → Worker → KV → spectator PULL → corpus payoff.**

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

The Cloudflare production transport and domain are proven. Next development work can proceed from this known-good production baseline: complete the performer-side H2 authenticated push path and wire the final spectator-facing visual assets/gateway without reopening the signed-off transport architecture.


---

## CONTINUATION CHECKPOINT — 22 September 2026 (authoritative handover)

This section supersedes stale “immediate next stage” wording above. **Do not reconstruct the current state from old chat. Start here.**

### Production status

Production is live at `https://gutenbrg.com`.

Proven production chain earlier today:

**authenticated PUSH → Worker → KV → spectator PULL → injected force word → dwell → PAID persistence**

A real phone test previously succeeded with `GOPHERS`: ARMED, approximately six-second dwell, leave page, PAID, only payoff page retained GOPHERS and other sockets cleaned.

Cloudflare zone/domain:
- registrar: GoDaddy
- Cloudflare nameservers: `carlos.ns.cloudflare.com`, `wanda.ns.cloudflare.com`
- obsolete GoDaddy apex A records removed: `13.248.243.5`, `76.223.105.230`
- `gutenbrg.com` serves the GUTS Worker/static assets
- KV namespace: `GUTS_STATE`
- KV namespace ID: `85ae7131c91e492abb79aca57d6817a6`
- Worker: `guts`
- public workers.dev route: `https://guts.stanjarin.workers.dev`
- old disposable test Worker `sparkling-term-874e.stanjarin.workers.dev` still exists; do not delete unless explicitly requested.

Runtime bindings currently expected in Cloudflare:
- `GUTS_PUSH_SECRET` — Secret
- `GUTS_ARM_PIN` — currently a dashboard Variable; current value known to Stanley
- `GUTS_SITE_PIN` — currently a dashboard Variable; current value known to Stanley

**Never put actual secret/PIN values in this README or public source.**

### Binding persistence fix

The ARM/SITE PIN dashboard bindings disappeared after earlier Wrangler/GitHub deployments. They were recreated manually.

Commit `ecaf19c57d96398b0686c5c21718cd3839b724d7` — **Preserve dashboard PIN bindings across Wrangler deploys** — added:
- `keep_vars = true`
- declarations that the three runtime secret/binding names are required

After that deployment became Active, Stanley tested NoBo H2 preactivation and reported: **PIN worked**. This is the first proof that the current PIN binding/preservation path is functioning.

### Performer NoBo / H2 bridge

Performer UI is the existing NoBo NoFo PWA; do not rebuild it.

NoBo repository: `stanjarin/NoBoNoFo`.

The seam is the existing H2G2 covert word entry. Historical local call was `armMagic(w)`; current bridge first securely pushes ARMED to GUTS, then retains the local NoBo behavior.

Relevant NoBo commits:
- `d32ad00` — Wire H2G2 covert input to secure GUTS ARM endpoint
- `b31a4ee` is GUTS-side CORS support, not NoBo
- `ac7c002` — move ARM PIN entry to preactivation before covert word submit
- `232c128` — persist preactivated ARM PIN in `localStorage` across PWA launches
- `bc1a6c7` — verify ARM PIN during preactivation by sending CLEAN before storing it

Current intended choreography:
1. Before performance, enter H2G2 SEARCH.
2. If no stored PIN, prompt says **ARM PIN**.
3. PIN is verified immediately via `POST https://gutenbrg.com/api/performer/state` with phase CLEAN.
4. Only a successful PIN is stored in NoBo PWA `localStorage`.
5. During the covert H2 word submit there must be **no PIN prompt** and no security business; stored PIN silently sends ARMED + word.
6. A rejected PIN is removed from localStorage.

Visible NoBo version label may still say **6.18S**; that does not prove the bridge code is stale.

CORS history:
- initial cross-origin JSON POST from GitHub Pages failed because OPTIONS/CORS was absent
- `b31a4ee1327729c074eaae34dc2bc5e36e866988` added exact-origin CORS/preflight for `https://stanjarin.github.io`
- `86659e2bd42aedf9f6422d6b1403df746add564f` added CORS headers to error responses, turning generic Safari “Load failed” into useful “PIN rejected”
- later Cloudflare Settings revealed PIN bindings had disappeared; they were recreated
- after persistence fix, **PIN now works**

### Current blocking bug — literal $$$ after successful PIN

**THIS IS THE EXACT RESUME POINT.**

Latest Stanley report after PIN success:

> “Pin worked but pages show, literally, $$$”

The reader is selecting force paragraphs but displaying the literal socket marker rather than the force word.

Inspection of current `index.html` found:
- remote ARMED handling sets `magic.force = String(remote.word).trim()`
- `visible(p)` selects `p.force_paragraphs` when ARMED (except protected chapter opener)
- injection happens before HTML escaping/render:
  `function inject(s){return magic.force?s.replaceAll("$$$",magic.force):s}`
- reader render calls `visible(p)`, then `esc(x)`
- therefore literal `$$$` proves the force paragraph is being selected, but substitution is not occurring as expected.

A first hardening attempt changed the socket substitution from `replaceAll` to literal split/join:
`function inject(s){return magic.force?String(s).split("$$$").join(magic.force):s}`

Commit:
`5438466909372d5c597f1850909cb7b71d810e37` — **Harden force-word socket substitution**

Stanley retested after that change and reported:

> **“Still seeing $$$.”**

Therefore **do not repeat the replaceAll/split-join theory. It is disproven.**

Next investigation must determine why `forceHere` can apparently choose force paragraphs while `inject()` receives no usable `magic.force`, or whether another render/state path is replacing/clearing `magic.force` between remote pull and page rendering. Instrument/inspect actual runtime state before changing corpus or state machinery.

**Do not touch the corpus.** All 5,435 pages previously passed mechanical socket QA and a real production test previously injected GOPHERS successfully.

Potentially relevant current pull logic:
- `pullRemoteState()` GETs `/api/state`
- `applyRemoteState(remote)` ignores revisions `<= sessionStorage[REMOTE_KEY]`
- ARMED + word sets local ARMED unless local phase is PAID
- CLEAN clears force
- READY resets only from READY/CLEAN
- remote revision is recorded after handling
Be alert to stale revision/local-state interactions. Do not assume this is the cause without evidence.

### Worker controls / security

Current single-user routes:
- `GET /api/state` — public state pull
- `POST /api/state` — master-secret protected
- `POST /api/performer/state` — PIN1 protected, ARMED/CLEAN
- `GET /api/performer/mode` — current mode
- `POST /api/performer/mode` — PIN2 protected, REHEARSAL/SHOW
- SHOW→REHEARSAL writes CLEAN
- REHEARSAL currently gates static assets by performer cookie

Known security/logic caveat still to fix later:
`GET /api/state` and `GET /api/performer/mode` are evaluated before the static REHEARSAL gate and remain publicly readable.

An unsafe unauthenticated performer write endpoint was briefly added and immediately removed in commit `7599b9a15316c8eb346718fc5d6cd40fc48d4a56`. **Never reintroduce unauthenticated writes.**

Zero Trust/Access was considered but its “free” setup demanded payment details. Stanley declined. Do not resume that path unless explicitly requested.

### The Shed idea — PARKED until literal-$$$ bug is solved

New idea from Stanley, not yet implemented:

In **REHEARSAL**, instead of outsiders receiving a 404 from `gutenbrg.com`, invisibly/quietly send them to the **real Project Gutenberg**. This is better camouflage because a mistyped/revisited “Gutenberg” address simply produces the expected real site.

Likewise, when someone later revisits the short URL from browser history, **all Resources options should lead to real Project Gutenberg** outside SHOW.

In **SHOW**, our Gutenbrg experience intercepts the journey as designed.

This should replace the current 404 camouflage once the current force-word bug is fixed. Preserve the existing performer-authorised rehearsal behavior as needed; work out redirect routing carefully rather than creating loops.

### REHEARSAL / SHOW doctrine

Two states only:
- **REHEARSAL** — between shows/development; performer-authorised access remains possible, outsiders should ultimately escape to real Gutenberg (new parked requirement)
- **SHOW** — spectator-facing GUTS public

No third CLOSED state unless Stanley changes the design.

PIN2/display toggle is pre/post-show, never part of the covert moment. Backend exists; practical control UI is not yet finished.

### Multi-performer work — PARKED

Do not resume unless Stanley explicitly asks.

Partial architecture exists alongside single-user and must not break it:
- opaque sessions, KV `session:<id>`
- session cookie `guts_session`
- session create/state routes
- permanent alias prototype
- P1 prototype alias `shortcuts`
- P2 QA alias `test-p2`

Relevant commits:
- `e74b54e` — session architecture spec
- `207d973` — isolated session transport
- `c29f97a` — short-link handoff constraints
- `da63c67` — permanent performer aliases for P1/P2 QA

Production custom-domain route proved alias code existed even when Cloudflare workers.dev HTTP tester misleadingly returned 404. Resume point if ever unparked: bootstrap P1/P2 on production, ARM different words, prove isolation.

Commercial doctrine: each purchaser eventually gets a permanent innocent alias/short URL; aliases are never recycled.

### Spectator entry and visual work — not current priority

Spoken prototype remains:
**“Look, quickest way is to just go to is.gd/shortcuts.”**

Resources gateway concept is locked:
- vague institutional/educational gateway, not Project Gutenberg identity
- wordless crest
- ochre “Resources”
- heading: “From Project Gutenberg, free books in the public domain”
- explanatory institutional waffle
- “Make a start here:”
- four classic links: Recent additions / Popular titles / Reader recommendations / Staff picks
- performance line on unexpected gateway: **“Oh. … OK, that'll do. Tap any of those.”**

Gutenberg-style landing follows. Canonical moving art is `Carousel.png`; Suggestions is a separate static transparent overlay ABOVE it while carousel moves underneath. Do not rebuild the carousel.

Typography doctrine: **Helvetica. No Arial. Ever.** Current development CSS may still contain Arial; fix during visual/Arts & Crafts pass, not by destabilising current debugging.

### Immediate order from this checkpoint

1. **Solve literal `$$$` bug using runtime evidence.**
2. Re-prove phone ARMED → force word → dwell → PAID → CLEAN.
3. Implement/test The Shed REHEARSAL→real Project Gutenberg camouflage.
4. Finish practical PIN2 SHOW/REHEARSAL control.
5. Return to Resources/assets/page-flip/visual Arts & Crafts.
6. Multi-performer remains parked.



## CORRECTION / VERIFIED END-TO-END STATE — 22 September 2026

The earlier checkpoint section describing literal `$$$` as a GUTS spectator-reader bug was a **wrong-app diagnosis**. Stanley was looking at the **NoBo performer app**, not GUTS. Do not resume GUTS runtime debugging from that stale section.

### Actual cause and repairs

In NoBo, persistent BROWSE mode deliberately returned raw `force_paragraphs`, so literal `$$$` was visible and normal injection was bypassed. Fixed in NoBo commit:
- `6dbd25797e121d58b0414cd963f0c9b5225d9671` — Exit socket browse mode when arming performance.

A subsequent H2 result-page “Image unavailable” failure was repaired by binding the result click handler through the local results container with a null guard:
- `c52447a4ac11fe46f9a3fb149381c078f37ae966` — Guard H2 result binding on iOS.

ARM authorisation is now persistent in NoBo localStorage and a deliberate de-authorise control was added to the hidden MORE maintenance panel:
- `0731e17ce939ababebe9b1e4480504a89cb073c2` — Add ARM authorisation off control.
- The panel shows **ARM AUTH ON** when `guts-arm-pin` is stored. Pressing it removes that localStorage item; the next H2 SEARCH preactivation asks for and verifies PIN1 again.

### FULL BRIDGE — PASSED

Stanley performed the complete production test successfully:

**NoBo H2 → PIN-authenticated Cloudflare ARM push → KV → GUTS spectator pull → GOPHERS displayed correctly.**

Observed conditions:
- no PIN interruption during the covert H2 submit;
- no literal `$$$`;
- force word displayed once and correctly in GUTS;
- therefore the single-user production bridge is now **END-TO-END PASSED**.

### Wrong-tram debris in GUTS

During the mistaken GUTS diagnosis two changes were made that were **not causal fixes** for the reported `$$$` symptom:
- `a7d984846dbd4ee667085b93caa8a5cc47214bec` — runtime unresolved-socket diagnostic remains in GUTS and may be removed as cleanup.
- `2fe079b83a1e893e0715cd03375bdad73303dfb2` — explicit `ASSETS` binding in Wrangler. This aligns with `env.ASSETS.fetch()` but was not the solution to the NoBo symptom.

### Current priority

The force bridge is no longer blocking. Next functional work is the parked **LEAVE NO TRACE** camouflage: outside SHOW / in REHEARSAL, ordinary outsider revisits should resolve harmlessly to the real Project Gutenberg rather than expose a GUTS 404. Preserve authorised performer/development access and avoid redirect loops. PIN2 practical SHOW/REHEARSAL control remains to be finished after/with that work.


## TWO-REPO SYSTEM MAP

GUTS is now one operational system spanning **two sibling GitHub repositories**:

```text
stanjarin ›
├── GUTS ›
│   ├── README.md
│   ├── NEXT_EWE_BRIEF_2026-09-22.md
│   ├── GUTS_PERFORMANCE_FLOW_POV_v1.md
│   ├── cloudflare ›
│   ├── PRIMED ›
│   └── index.html
│
└── NoBoNoFo ›
    └── index.html   ← performer-side H2G2 + PIN/ARM machinery
```

**Division of responsibility:**
- **NoBoNoFo** = P-side interface. H2G2 covert input, ARM PIN preactivation/persistence/de-authorisation, authenticated ARM push.
- **GUTS** = Sp-side experience plus Cloudflare Worker/KV transport, display state, library/reader and production hosting.

Do **not** look for performer/H2 implementation inside the GUTS repo. When debugging the P-side half of the production bridge, inspect `stanjarin/NoBoNoFo`. When debugging spectator display, Worker/KV, corpus or production routing, inspect `stanjarin/GUTS`.
