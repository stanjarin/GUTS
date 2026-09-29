# GUTS RELEASE CHECKLIST — 28/29 September 2026

Status: **RELEASE COMPLETED / PRODUCTION PASS**

## Production

Production `main`:
`aef68707b1ad031eab16ae1efbecce5733630186`

The frozen release candidate was fast-forwarded to `main`.

Production smoke test passed:
- landing/carousel
- book → Contents → Reader
- live performance state chain

## Frozen runtime layers

- corpus
- Reader presentation
- landing/carousel
- H2G2 covert arming
- Worker/KV transport
- READY / ARMED / PAID / CLEAN
- selected-chapter opener protection
- 6-second dwell
- PAID persistence

Do not regenerate or re-architect these layers during cosmetic work.

## Cache caveat

Stable branch aliases and Safari can serve stale resources.

Known examples:
- `GOPHERS$` on a stale preview alias
- transient grey landing slab

In both cases current source/deployed assets were clean.

Rule:
**compare source/build evidence before editing frozen runtime to chase a visual cache symptom.**

## Post-release cosmetic branch

Current branch:
`prepage-refresh-2026-09-28`

Approved runtime checkpoint before 29-Sep docs-only commits:
`d5bec8a6d202042b922e49858124478036b10afd`

Current branch purpose:
- new generic Resources Pre-Page
- artwork float/crop experiments
- future cover cosmetic cleanup

Production `main` is not to be used as the artwork workbench.

## Pre-Page pilot — PASS

Passing long-page model:
- width overscale to 112%
- horizontal offset -6%
- height auto
- normal vertical scrolling
- one hotspot spanning all four links

Do not use viewport `object-fit: cover` for the long Pre-Page.

## Artwork master

- fixed-page master: 2048 × 4210
- essential/safe: 1804 × 3640
- long landing master may extend to 2048 × 8000

## Next release gate

No new production release is currently authorised.

Before the next merge to `main`:
1. finish cosmetic branch work;
2. phone-QA one cover pilot;
3. roll out only after the pilot passes;
4. verify root/public identity;
5. verify frozen runtime invariants remain unchanged;
6. create/freeze a new release candidate;
7. merge only after Stanley explicitly approves.

**NEXT ACTION: revise and test one book cover as the next isolated cosmetic pilot.**
