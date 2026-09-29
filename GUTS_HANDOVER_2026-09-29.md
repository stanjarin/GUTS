# GUTS — HANDOVER / START HERE

**Checkpoint: 29 September 2026**

This is the current resume point for Stanley, a replacement developer, or a fresh AI.

## 0. Read broadly, act narrowly

Before changing anything:
1. read `GUTS_WORKFLOW_CONSTITUTION.md`;
2. read this handover;
3. read `GUTS_CURRENT_STATE.md`;
4. read the rest of the GUTS documentation/code/config relevant to the task;
5. read NoBo material for cross-system context.

Then scope correctly:

**For GUTS, NoBo is operationally relevant only through H2G2 covert arming.**

Do not let unrelated NoBo corpus/book state become a GUTS dependency.

## 1. Production truth

Production `main`:
`aef68707b1ad031eab16ae1efbecce5733630186`

That release passed production smoke QA.

Current cosmetic/work branch:
`prepage-refresh-2026-09-28`

Approved runtime checkpoint before this documentation-only handover pass:
`d5bec8a6d202042b922e49858124478036b10afd`

Do not use `main` as the artwork workbench.

## 2. Frozen machinery

Do not reopen without a specific observed defect:
- all eight active book corpora;
- Reader presentation;
- exact canonical `$$$` substitution;
- landing/carousel;
- H2 PUSH / GUT PULL;
- Worker/KV transport;
- READY / ARMED / CLEAN;
- selected-chapter opener protection;
- 6-second dwell;
- PAID persistence;
- complete performance chain.

Verified chain:
**CLEAN → ARMED → protected opener → prepared payoff → 6s dwell → PAID persistence → CLEAN**

Parker remains parked/non-runner.

## 3. Cache / preview trap

Safari and stable branch-preview aliases can serve stale material.

Known false alarms:
- `GOPHERS$`
- transient giant grey landing slab

Both were investigated and isolated away from current source truth.

Rule:
**find the event/root cause before patching.**
Do not rewrite frozen source just because a stable preview looks stale.

## 4. Current Pre-Page

Stanley replaced the old Gutenberg-explicit gateway with a generic Resources/public-domain-books page.

Visible copy includes:
- Resources
- Browse free public-domain books and ebooks
- Recent additions
- Popular titles
- Reader recommendations
- Staff picks
- explanatory copy below

All four visible links go to the same place, so one transparent hotspot covers the whole block.

### Artwork system recovered
- standard fixed-page master: **2048 × 4210 px**
- essential/safe area: **1804 × 3640 px**
- long landing artwork may extend below that, e.g. **2048 × 8000 px**

Key lesson:
the safe guides are **survival boundaries**, not huge-margin guides. Meaningful composition should nearly fill them.

### Pre-Page renderer pilot
`object-fit: cover` was tested and rejected for long scrolling art because it cropped vertically.

Passing implementation:
- width 112%
- max-width none
- height auto
- margin-left -6%
- normal vertical scrolling
- one enlarged hotspot over all four links

Stanley phone verdict:
**PASS & PASS** for framing and hotspot.

## 5. Current domains

Owned:
- **ebooks.fyi** — intended primary spectator-facing domain
- **ebks.fyi** — spare

Plan:
attach `ebooks.fyi` directly to the existing Cloudflare Worker so it remains visible in the address bar.

Do not use a redirect that exposes `gutenbrg.com`.

H2G2 may continue pushing to:
`https://gutenbrg.com/api/performer/state`

## 6. Private control simplification still pending

Stanley wants the private control values renamed to:
- ARM → **Arm**
- SHOW → **Show**

Not yet done.

Do not expose actual secret bindings in repo.

## 7. Next work

### STANLEY'S JOB
Clean the dirty backgrounds on the book covers.

### KRYTEN'S JOB
When one revised cover arrives:
1. wire only that cover on `prepage-refresh-2026-09-28`;
2. test the same width-overscale/crop principle;
3. phone-QA it;
4. only then consider rolling the treatment across all covers.

Later:
- replace Parker with a title having many genuine chapter pages;
- perhaps add several books;
- clean visible chapter-numbering inconsistencies;
- attach `ebooks.fyi`;
- privately simplify ARM/SHOW control values.

## 8. Collaboration rules

- concise, exact;
- every status ends with a concrete **NEXT ACTION**;
- use **MY JOB / YOUR JOB**;
- distinguish source defects from cache/display anomalies;
- investigate root cause before patching symptoms;
- preserve frozen layers;
- do not use `!H`; Stanley owns it;
- `!HACK` is Kryten's acknowledgement/self-Heel shorthand, used sparingly.

## NEXT ACTION

**Stanley revises one cover. Kryten then runs a single-cover cosmetic/crop pilot on the existing work branch.**
