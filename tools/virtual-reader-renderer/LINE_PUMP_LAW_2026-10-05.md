# Line-based airlock pump — proposed replacement law (2026-10-05)

Status: **diagnostic design only**. No corpus mutation. No Reader production change.

## Finding

The current retention machinery is fundamentally word-based. Actual iPhone Safari evidence from Gormenghast Ch 2:

- p1 stored pre-airlock depth: 81 words -> airlock paragraph starts on rendered line 10
- p2 stored pre-airlock depth: 103 words -> rendered line 13
- p3 stored pre-airlock depth: 100 words -> rendered line 13

So different word depths can collapse to the same rendered line. Retention must therefore be judged and driven in **rendered line units**.

## Replacement principle

**The browser is the ruler.**

For every prepared page, after layout:

1. Count the real Safari/WebKit line boxes before the airlock.
2. Record the rendered line on which the airlock paragraph begins.
3. Stagger against the **previous prepared page's rendered airlock-start line**, not its word count.
4. Never accept the same airlock-start line on two consecutive prepared pages when a legal alternative exists.
5. Prefer a separation of at least **4 rendered lines** from the immediately previous prepared page where a legal placement permits.
6. Treat a run of 3 prepared pages whose socket-start lines fall within a **4-line band** as RETENTION and force the next legal page outside that band.
7. Preserve genuine text and paragraph order. Prepared-layer sentence splitting is allowed only where already permitted by the existing corpus rules.
8. **Every prepared page must begin mid-paragraph.** The previous page creates the carry fragment. Fresh non-$$ paragraph starts are defects. Prepared paragraph boundaries may be run together or split at sensible sentence boundaries, but genuine words and order are inviolable.

## Initial target cycle

Use a five-step line target cycle as a compass, not a mandate:

**8 / 12 / 16 / 10 / 14**

This deliberately spans the usable vertical field while avoiding adjacent repeats. If the exact target is unavailable because of paragraph/sentence boundaries, choose the nearest legal rendered line subject to:

- no consecutive repeat;
- ideally >=4-line separation from previous page;
- no 3-page cluster inside a 4-line band;
- every prepared page begins with genuine carry-over from an already-started paragraph.

## Why these targets

They are typographic rather than pixel/word targets and sit comfortably inside the established central field on the current iPhone baseline. They also retain the old five-step stagger idea while replacing the broken unit of measure.

## Validation gate

Before any corpus-wide repair:

- test this law on one known retention run (Gormenghast Ch 2 pp1-3);
- then on one Ulysses run;
- actual iPhone Safari line probe is authoritative;
- only after both behave correctly should a branch-only corpus repair be generated.

## Hard safety rule

**The line pump may measure and propose on a branch. It may not write to production main without explicit promotion approval.**
