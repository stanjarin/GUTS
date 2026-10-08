# GUTS independent final-page validation — 8 October 2026

STATUS: READ-ONLY validation; does not alter books, staging, NoBo, production, or factory machinery.
Input: the 15 artifact-source ZIPs retained by GitHub Actions runs 37565443433 and 37592243640.
Method: Chromium using factory CSS (Georgia 15px/1.45, 329px measure) and all final force_paragraphs; DOM Range text rects. 21.75 CSS px text line height. Evaluate first-new-paragraph index and actual final airlock paragraph top, not isolated carry-only length.

RESULTS
- 15 factory books, 3,842 prepared pages inspected (excluding chapter openers and absent sockets).
- 42 first-new-paragraph failures (airlock paragraph index >1): ALL in Ulysses.
- 47 upper-page adjacent stagger failures (final airlock top delta < 4 line heights while both airlocks in upper zone <=330px): 46 Ulysses, 1 The Talented Mr. Ripley.
- Ulysses Chapter 1 particularly: pages 6, 7, 11, 13, 15, 18 contain extra paragraph(s) preceding airlock; many consecutive early pages have actual stagger less than four lines.

IMPORTANT LIMITATIONS
- DOM model uses factory CSS and final page paragraph content, not a full deployed staging iPhone Safari session. Actual phone remains final authority.
- Upper-zone threshold 330px is a triage threshold, NOT a newly authorised visual law.
- Pairwise violation counts omit chapter-opener sockets and cannot prove absence of 3-page conspicuous retention elsewhere.
- Existing three phone-reviewed established books were not in this 15-artifact inspection.
- No repair has occurred; diagnostic FAIL is not a repair mandate.
- All padding must use actual existing same-book prose; never invent prose. Dialogue compaction, boundary slides, DOUBLE-UP already exist as approved techniques.

CAUSAL CODE EVIDENCE
- factory_book.py isolates candidate carry text in JS_MEASURE_MANY, then selects stagger on proxy length.
- final calculation also isolates g[0] rather than measuring airlock in complete output.
- retention windows counted but omitted from machine PASS.
- fallback paths can create g[0],g[1],... with airlock later than first paragraph, and code accepts this via final assembly.
- existing dialogue compaction lacks a final independently enforced first-new-paragraph gate.

NEXT
Convert the local diagnostic into a safe-branch automated, failing final-page QA gate before any repeat factory build. Confirm tests on Ulysses ch1 (known FAIL) and accepted Jeeves reference (known PASS); enforce first-new-para, final rendered line stagger, top retention with classified exception/phone decision. Then narrowly fix known failures with existing techniques, preserving freeze policy. No mass rewrite before Monday.

MY JOB: Integrate the gate safely and rerun validation without rewriting stage props.
YOUR JOB: No phone QA until a corrected candidate exists.
