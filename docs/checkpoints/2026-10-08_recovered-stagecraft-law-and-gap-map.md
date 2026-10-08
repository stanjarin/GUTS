# GUTS recovered stagecraft law and implementation gap map — 8 October 2026

STATUS: historical-rule reconciliation, NOT a new factory brief and NOT repair authorisation.
Sources: 5 Oct formatted-placement repair, 7 Oct Jeeves phone-PASS freeze, 7 Oct factory stagecraft law, 8 Oct systemic gate audit, 8 Oct handover, and the live `tools/factory_book.py`.

## Pre-existing governing objective
GUTS books are theatrical ebook props for at most about ten minutes of spectator scrutiny. Plausibility on the actual phone outranks literary polish, machine metrics and generic publisher standards. Gutenberg appearance is camouflage, not a claim that all texts came from Gutenberg. Leave ordinary source/OCR ugliness alone unless conspicuous or method-revealing; identify gross OCR splats and ridiculously short pages for targeted review. Before Monday ASM, no broad rebuilding.

## Pre-existing mechanics and stagecraft
1. NoBo commands; GUTS executes. Keep READY/ARMED, local PAID, SHW/HIDD and PIN separate, and leave production untouched pending explicit QA/promotion.
2. `$$$` is a self-contained airlock paragraph; it is the FIRST NEW PARA after the head carry-over. Never splice into a genuine sentence. This is essential for the approved spoken instruction 'jump to the first NEW paragraph.'
3. Page tops should begin in the middle of a sentence carried from the preceding page, except an explicitly accepted phone-visible exception.
4. Socket paragraph top varies by at least FOUR actual rendered text lines on adjacent prepared pages; target rotation is 8/12/16/10/14 lines. Compare final assembled Reader appearance, not words, pixel estimates or isolated carry paragraphs.
5. Visible retention matters principally in the upper attention zone. Repetition low down can be acceptable; the deliberately low-attention DOUBLE-UP at bottom of page N / top of N+1 was phone-approved.
6. When short dialogue produces multiple 'new paragraphs' before the socket or prevents sufficient stagger, RUN ON / COMPACT the consecutive dialogue in the prepared layer while retaining verbatim words and order; strip only artificial helper labels. Never invent padding words.
7. All filler comes from prose already in the SAME BOOK. Use locally available prose, same chapter, nearby chapters, other locations within book in that preference order. Legitimate plasticine operations: shift prepared boundaries, rejoin/split paragraphs, borrow verbatim and DOUBLE-UP. No automatic wholesale repagination.
8. Genuine `paragraphs` were frozen as an engineering/source-identity safety constraint during the approved factory pilot; they are not aesthetically sacred. Relaxing that constraint would require a separate explicit change because page/source identity and performance are coupled. The user has NOT authorised rewriting genuine arrays in this pass.
9. Chapter openers socket-free; preserve exactly one socket on eligible prepared pages; protect clean state, root/public parity and full protocol.
10. Factory structural PASS never equals spectator phone PASS. Freeze wins after actual-phone acceptance.

## Recovered implementation gaps (not new design principles)
- Factory `JS_MEASURE_MANY` scores isolated carry-over paragraphs; assembled final page/airlock start position is not independently used for four-line spacing gate.
- Final four-line checks remeasure `g[0]` in isolation. `JS_PAGE_METRICS` already exists but isn't used to enforce the final assembly gate.
- Retention windows are recorded but not a PASS blocker, and upper/lower attention-zone significance isn't considered.
- The factory assumes `force_paragraphs=[g[0],air]+g[1:]` proves FIRST NEW PARA. It does not independently test real page output or dialog-driven apparent paragraph starts.
- The approved dialogue-run-on technique is not a dedicated guaranteed fallback for the final first-new-para failure.
- DOUBLE-UP is applied AFTER spacing measurement; final appearance isn't independently revalidated.
- Structural PASS omits some reported warnings; use explicit warning classification and phone QA rather than treating counts as zero.

## Recovery versus proposed work
Already invented and proved in Jeeves: dialogue compaction, DOUBLE-UP, book-internal borrowing, line staggering, visual phone authority. DO NOT reinvent these or manufacture new prose.

First necessary engineering action, after this reconciliation: add READ-ONLY FINAL-STAGED-READER VALIDATION using existing factory and Reader assets. Test on Ulysses ch1 to reproduce the observed fault; then check wider batch. Only after that, use the existing repair methods narrowly. No write to production, staging, NoBo, or corpus in this reconciliation.

## Monday scope
Limit repairs to method-exposing / illusion-breaking defects. RSP/OCR are ranked triage candidates, not grounds for indiscriminate restoration.
