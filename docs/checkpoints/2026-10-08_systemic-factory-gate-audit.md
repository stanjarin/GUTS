# GUTS systemic factory-gate audit — 8 October 2026

## Scope
Read-only diagnosis of the factory program and its GitHub Actions PASS machinery. No corpus, Reader, production, NoBo or staging modification.

## Evidence
Source: `tools/factory_book.py` on `factory-autopilot-2026-10-07`.
Workflow: `.github/workflows/factory-autopilot-2026-10-07.yml`.
Approved law: `docs/GUTS_FACTORY_STAGECRAFT_LAW_2026-10-07.md`.
Phone observation: Ulysses chapter 1 shows repeated upper-page airlock positioning and FIRST NEW PARA difficulty caused by dialogue.

## Confirmed systemic mechanisms
1. Candidate placement measures isolated carry prose via `JS_MEASURE_MANY` (lines 16–30), returning `tops.length+1`. `candidate_splits` and fallback methods choose positions from those estimates. The full-page measurement helper `JS_PAGE_METRICS` exists (lines 39–61) but is not used in the final stagger PASS loop.
2. `final_lines` are recomputed as `JS_MEASURE_MANY([g[0]])[0]` (around line 608), not actual airlock top from the fully rendered assembled page with all paragraph spacing and Reader structure.
3. Three-page `retention_windows` are counted (lines 634–638) but NOT required to equal zero in `passed` (line 704). Their visual upper-page importance also is not modelled.
4. `mid_sentence_failures` and `adjacent_overlap_failures` are reported, but are not included in the final structural gate; some exceptions may legitimately require human QA, but they must be explicitly classified rather than silently passing.
5. First-new-paragraph is an output construction assumption (`force_paragraphs=[g[0],air]+g[1:]` at ~605) without an independent end-to-end finished Reader check of rendered paragraph boundaries or user navigation.
6. `apply_double_up` is run after preparation and initial measurement (line 627). No final full-page post-DOUBLE-UP visual acceptance check is performed.
7. Dialogue compaction is permitted in the approved stagecraft law, but the current gate has no dedicated rendered FIRST NEW PARA compliance test or dialogue exception QA.

## Conclusion
The current PASS is **structural, not a complete visual-stagecraft PASS**. A book can meet the internal spacing proxy while still exhibiting visible repetition or the FIRST NEW PARA failure reported by Stanley. This is a systemic test-gap, not evidence that all books are broken.

## Proposed correction (not yet executed)
- Introduce a READ-ONLY final-page audit using the actual Reader layout and final staged `force_paragraphs`, after all DOUBLE-UP operations.
- Count actual rendered text lines to the airlock and validate consecutive 4-line staggering; apply attention-zone retention test near the top, not blanket lower-page penalties.
- Independently validate FIRST NEW PARA on finished output, including dialogue paragraphs; classify deliberate exceptions.
- Report ridiculous-short-page actual occupied lines/height and high-confidence OCR evidence, with book/chapter/page and source-vs-prepared attribution.
- Split `MACHINE STRUCTURAL PASS` from `STAGECRAFT PHONE QA PENDING` rather than presenting structural PASS as final audience-facing success.
- Run this diagnostic first on Ulysses chapter 1, then on the 15 factory artifacts, without rebuilding or writing prepared books.
- Only after a reproduced, passing diagnostic should a separate, narrow repair proposal be considered.

## Operational freeze
Do not change production `main`, `ebooks.fyi`, NoBo, staging site or corpus. The Monday ASM rehearsal remains priority.
