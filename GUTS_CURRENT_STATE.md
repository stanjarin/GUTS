# GUTS — CURRENT STATE

**Authoritative checkpoint: 29 September 2026**

## Safety / production anchors

- Production `main`: `aef68707b1ad031eab16ae1efbecce5733630186`
- Frozen release candidate: `release-candidate-2026-09-28` at the same runtime state
- Frozen rollback branches:
  - `GUTS-035-KNOWN-GOOD`
  - `contents-repair-backup-2026-09-27`
  - `visually-good-backup-2026-09-28`
- Current cosmetic/work branch: `prepage-refresh-2026-09-28`
- Approved runtime checkpoint before this docs-only pass: `d5bec8a6d202042b922e49858124478036b10afd`

## Governing rule

Read `GUTS_WORKFLOW_CONSTITUTION.md` first.

At handover: **READ EVERYTHING before acting.** Read all GUTS and all NoBo material, then scope correctly:

**NoBo dependency for GUTS = H2G2 covert arming only.**

## Frozen / passed

### Corpus
All eight active books passed corpus QA and real Reader phone QA:
- Pooh
- Thurber
- Runyon
- Joyce
- Jeeves
- Huck
- Farewell
- Christie

Parker remains parked/non-runner.

### Reader / mechanics
Passed and frozen:
- exact `$$$` substitution
- chapter opener protection
- 6-second dwell
- local PAID persistence
- READY / ARMED / CLEAN remote state
- H2 PUSH / GUT PULL
- Worker/KV bridge
- landing/carousel repair
- complete live performance chain

Full verified chain:

**CLEAN → ARMED → protected opener → prepared payoff → 6s dwell → PAID persistence → CLEAN**

### Production release
The frozen release candidate was fast-forwarded to `main`.

Production smoke test passed.

A transient grey landing slab on the custom/stable route was isolated as a browser/alias/cache/resource-loading effect. Source assets were byte-identical to the known-good build. Do not alter landing source merely to chase this symptom.

## Current Pre-Page branch work

Branch: `prepage-refresh-2026-09-28`

New generic Resources artwork replaces the old Gutenberg-explicit Pre-Page.

Approved design:
- enlarged Resources heading
- “Browse free public-domain books and ebooks”
- four visible links:
  - Recent additions
  - Popular titles
  - Reader recommendations
  - Staff picks
- lower explanatory copy
- one transparent hotspot spans the full four-link block

### Float/crop pilot — PASS
The original fixed-page art system was recovered:
- standard master: **2048 × 4210 px**
- essential/safe area: **1804 × 3640 px**
- long landing art may extend below this, e.g. **2048 × 8000 px**

Important design lesson:
- meaningful composition should sit close to the safe guides;
- excess canvas outside the guides is sacrificial crop allowance;
- do not use `object-fit: cover` on long scrolling artwork.

Current passing Pre-Page renderer:
- artwork width: **112%**
- horizontal crop via **margin-left: -6%**
- height remains auto
- normal vertical scrolling
- one enlarged hotspot covers all four links

Stanley phone result: **PASS & PASS** for framing and hotspot.

## Spectator-facing domain plan

Purchased:
- **ebooks.fyi** — intended primary spectator domain
- **ebks.fyi** — spare

The plan is to attach `ebooks.fyi` as a Cloudflare custom domain to the existing Worker so it remains in the address bar. Do not use a redirect that exposes `gutenbrg.com`.

Current H2G2 arming may continue to POST to `gutenbrg.com/api/performer/state`.

## Secret rename still pending

Privately change, when ready:
- ARM PIN/secret → **Arm**
- SHOW/site PIN/secret → **Show**

Do not place secret values in repo documentation beyond this user-approved naming intent; actual bindings remain private in Cloudflare.

## Cover system — PASSED AND FROZEN (29 Sep 2026)

Eight modern covers now use the responsive cover renderer. Parker remains deliberately on the old treatment as a placeholder/control specimen.

Frozen behaviour:
- ordinary portrait phones are width-led at **112vw**;
- the first view is vertically centred;
- vertical scrolling remains available; do **not** restore a hard vertical `overflow:hidden` crop;
- wide portrait screens at **600 CSS px and above** are height-led at **100dvh**, centred with white side space;
- landscape gets **no warning screen and no special redesign**; ordinary user behaviour is allowed to solve it;
- modern covers auto-advance to Contents after **1400 ms**;
- old NoBo reference delay was **1500 ms**;
- tapping the cover advances immediately and cancels the timer;
- no separate cover-swipe mechanism is required;
- Parker remains manual and untouched.

Stanley phone sweep: **PASS** across the eight modern covers. First-load Jeeves briefly decoded late, then behaved normally once cached; no source change was required.

Do not reopen this cover behaviour unless a specific observed defect appears.

## Open work / next actions

1. Replace Parker later, when wanted, with a genuine multi-chapter title.
2. Add further books later if desired.
3. Resolve remaining visible chapter-number consistency issues without touching frozen corpus structure.
4. Attach `ebooks.fyi` when the branch work is ready for deployment.
5. Privately simplify ARM/SHOW control values when ready.

## Mandatory handover phrase

**Read broadly, act narrowly.**

**NEXT ACTION: leave the passed cover system alone and move to the next explicitly chosen item.**
