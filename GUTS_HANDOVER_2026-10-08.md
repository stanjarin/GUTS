# GUTS HANDOVER — 8 OCT 2026

## READ FIRST
1. `GUTS_WORKFLOW_CONSTITUTION.md`
2. this file
3. `GUTS_CURRENT_STATE.md`
4. `docs/CURRENT_STATE.md`
5. latest relevant NoBo handover / README

Principle: **Read broadly, act narrowly.**

## Current operational truth

Safe working branch: `factory-autopilot-2026-10-07`.

Production `main` remains the older frozen live release. It is rollback-safe production truth, not the freshest GUTS corpus.

Factory work is complete across the library.

Original autopilot run:
- `37565443433`
- ten books completed successfully there;
- five original laggard jobs were later cancelled;
- ignore that run operationally except as artifact source.

Optimized laggard recovery:
- `37592243640`
- SUCCESS
- recovered Runyon, Ripley, Kon-Tiki, Peake, Joyce
- Joyce was extremely slow but did progress and finish.

Factory judgment from Stanley's phone review:
- **principle mainly OK**
- many visible warts remain
- **short pages are the worst recurring visible wart**
- do NOT launch another broad repair campaign before Monday
- plausible Project Gutenberg ugliness is acceptable camouflage
- only method-revealing / illusion-breaking defects justify immediate repair.

## Stable staging

The disposable Cloudflare preview expired and must no longer be treated as the durable QA address.

A persistent GitHub Pages staging deployment was created from the consolidated factory artifacts.

Workflow:
- `.github/workflows/stable-staging-2026-10-08.yml`

Successful run:
- `37707029293`, attempt 2 — SUCCESS

Stable staging URL:
- `https://stanjarin.github.io/GUTS/?browse=1`

GitHub Pages source was changed in repository Settings from **Deploy from a branch** to **GitHub Actions** so the staging workflow could deploy.

The workflow assembles:
- ten finished artifacts from run `37565443433`
- five recovered laggard artifacts from run `37592243640`
- existing branch/public state for the remaining established books

Production `main`, `ebooks.fyi`, and live NoBo were not changed by staging.

## NoBo relationship

Canonical architecture remains:

**NoBo commands. GUTS executes.**

But **NoBo production still routes to the older production GUTS at `ebooks.fyi`**.

The new factory-built corpus is currently on stable staging only.

Therefore:
- direct QA/rehearsal of new corpus: use stable staging URL
- full performance-chain testing through NoBo: still reaches old production until an explicit repoint/promotion decision is made.

Do not assume NoBo reaches staging.

## Monday strategy

Monday ASM demo is now the priority.

Keep the full library open; do not reduce to one safe book.

Project Gutenberg framing gives cover for ordinary OCR/formatting ugliness.

Working threshold:
- method-revealing / illusion-breaking → fix
- plausible Gutenberg roughness → leave

Recent performance workaround:
- if a page top looks awkward, Stanley can say **“jump to the first NEW paragraph.”**

Do not reopen global sentence-start, overlap, retention, pagination, Reader, protocol, or corpus surgery without a specific observed phone defect.

## Presentation notes

Monday theme is spooky/supernatural.

Stanley's framing direction:
- Karen: vodou / Marie Laveau / Tarot
- Stanley: James Randi / agnostic rather than atheist
- distinction: **improbable, not impossible**
- domestic-harmony bridge into improbability
- climax gag: finger wiggle + **“OOooh… spooky!!”**

Do not write the script for Stanley unless asked.

## Immediate next action

1. Verify stable staging on Stanley's phone.
2. Rehearse presentation and handling.
3. Decide explicitly whether to repoint NoBo to staging / promote factory corpus before Monday.
4. Do **not** touch production merely to make staging convenient.
5. If a genuine method-revealing defect appears during rehearsal, repair narrowly and re-QA only that defect.

## Identity note for incoming ewe

You are **Kryten wearing a sheepskin coat**.
Do not confuse costume with species.
**Avoid mirrors.**
