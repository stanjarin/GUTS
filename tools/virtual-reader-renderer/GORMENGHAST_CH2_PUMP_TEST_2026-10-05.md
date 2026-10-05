# Gormenghast Ch 2 line-pump prototype — 2026-10-05

Branch-only diagnostic. No corpus or production mutation.

The controller was run locally in Chromium against the GUTS fixed-width reader CSS. This is **not** authoritative for iPhone Safari; it proves the steering mechanism, not final device equivalence.

Targets: **8 / 12 / 16**

Observed prototype choices:
- p1 synthetic carry: target 8 -> local browser line 7 (nearest legal sentence split; error 1)
- p2 boundary run: target 12 -> local browser line 12 (exact)
- p3 fat run: target 16 -> local browser line 15 (nearest legal sentence split; error 1)

Crucial result: the controller now chooses the **carry suffix by rendered line count**. The carried suffix is the first paragraph of the next page; the $$$ airlock follows it. Therefore the same mechanism controls both hard requirements:

1. prepared page begins part-way through an existing paragraph;
2. socket start is steered to the line-stagger target.

The p3 test deliberately uses a run-on donor across genuine paragraph boundaries, confirming the intended “big fat paragraph” escape hatch while preserving genuine words and order.

Next validation must be on actual iPhone Safari.