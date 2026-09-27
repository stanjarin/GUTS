# GUTS Contents / Corpus Repair Plan

**Status: AUDIT FIRST. Editorial patching is paused.**

## Governing rule

Every visible/selectable Contents destination must ultimately be performance-capable **and** must open at a defensible story/chapter/episode start. But we do not repair display labels around an unexplained transformed corpus.

The earlier plan treated this as primarily spectator-facing Contents regularisation. That assumption is no longer safe: `PERFORMANCE35/ac_035.json` itself is discontinuous and begins with a `Chapter 5` object.

## Phase 0 — safety

- Work only on `contents-repair`.
- Do not modify, merge to, deploy from, or force-update `main`.
- Preserve `GUTS-035-KNOWN-GOOD`.
- Do not run an existing workflow until its target/ref and mutation behaviour have been read.
- Do not touch state machinery while investigating corpus structure.

## Phase 1 — provenance/integrity audit

For each affected title establish, with evidence:

`best original/source -> PRIMED input -> PERFORMANCE35 transform -> retained/omitted chapters -> source-to-display mapping -> opening page alignment -> $$$/force_paragraph preservation`

Record chapter counts, source IDs/titles, transformed IDs/titles, first-page coordinates, and any omissions. Distinguish deliberate performance cuts from accidental loss.

### Priority

1. **Christie** — first and mandatory. Find the best available original/source and compare it with `PRIMED/AC_GUTS_PRIME2.json` and `PERFORMANCE35/ac_035.json`. Determine exactly where Chapters 1–4 and later gaps went and whether a known-good historical mapping exists.
2. **Runyon** — titles look right, but selectable destinations may open mid-story. Audit story-start mapping.
3. **Joyce** — titles look right, but selectable destinations may open mid-episode. Audit episode-start mapping.
4. **Pooh / Thurber** — currently look clean; verify rather than assume.
5. **Jeeves / Farewell / Huck** — verify inherited/current mapping and opening alignment.
6. **Parker** — parked/special case; do not let it block the main repair.

## Phase 2 — repair design

Only after the mapping is understood decide whether each title needs:

- restoration from an upstream source;
- corrected retained-chapter mapping;
- opening-page realignment;
- spectator-facing display renumbering;
- genuine title/subtitle cleanup;
- hiding a genuinely unusable destination;
- no change.

Use authoritative real titles where they exist. Do not invent prose headings to conceal structural uncertainty.

## Phase 3 — mechanical verification

Before visible QA, verify at minimum:

- every displayed destination resolves;
- every displayed destination is performance-capable;
- selected destination opens at the intended chapter/story/episode start;
- genuine prose order is preserved;
- no accidental source chapters disappeared beyond documented performance cuts;
- `$$$` / `force_paragraphs` remain valid on prepared pages;
- opener protection and payoff coordinates remain coherent;
- root and `public` copies are intentionally synchronised if production assets are eventually changed.

## Phase 4 — spectator/editorial cleanup

After structural correctness is proved:

- renumber retained chapters consecutively for display where appropriate;
- use genuine chapter/story/episode titles where available;
- remove malformed extraction fragments;
- do not expose clean/dead choices;
- retain underlying IDs where possible if they are part of proven payoff mapping.

## Phase 5 — release

No release until the complete candidate replacement is checked on `contents-repair`. Then perform a compact actual-phone QA. Only after that should a deliberate release/merge be considered.

## Known observations at handover

- Pooh: Contents clean.
- Thurber: Contents clean.
- Runyon: titles correct; opening alignment suspect.
- Joyce: titles correct; opening alignment suspect.
- Christie: broken/discontinuous Contents; transformed corpus itself suspect.
- Parker: parked.

**Next concrete job after documentation is complete: Christie provenance audit. Not a cosmetic Contents patch.**