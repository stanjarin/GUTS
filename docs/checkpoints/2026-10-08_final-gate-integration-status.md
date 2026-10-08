# GUTS final-page QA integration — 8 Oct 2026

## Changes implemented on SAFE BRANCH ONLY
- New read-only `tools/factory_final_page_gate.py` renders complete prepared-page paragraphs with factory Chromium CSS and independently measures airlock top.
- Reports violations of FIRST NEW PARA (airlock must be at paragraph index 1), upper-attention-zone four-line stagger, short-page screen candidates, and OCR pattern suspects.
- `--strict` exits failure for first-new-paragraph, socket-count, and unreviewed upper stagger violations.
- Updated `.github/workflows/factory-autopilot-2026-10-07.yml` to call independent gate for each candidate and retain JSON findings.
- Workflow now also fails on the factory engine's recorded nonzero exit code, instead of concealing it behind the wrapper's `exit 0`.

## Evidence before integration
Previous 18-book independent screening: 4,395 eligible prepared pages; 42 first-new-paragraph failures (all Ulysses); 50 upper stagger flags (46 Ulysses, 3 Keys, 1 Ripley); 729 broad short-page candidates. OCR pattern counts from earlier 15-book only inspection are NOT a verified 18-book OCR verdict.

## Important limits / not yet done
- New GitHub gate script and YAML are committed and read back, BUT the revised GitHub Actions job has NOT been dispatched or executed; do NOT claim end-to-end new gate PASS.
- Short-page and OCR detectors are TRIAGE, NOT automatic repair or blocker conditions.
- 330px upper attention-zone / 600px bottom are inspection heuristics, not aesthetic law; phone can accept an exception after review.
- No book repair, no staging deploy, no production change. The 18-book staging URL still serves prior artifacts.
- Do not rerun 15-book heavy factory automatically just to exercise new gate; first prove the gate on isolated Ulysses and Jeeves fixtures, then decide narrow scope.
- Do not create new filler. Use only same-book words. Existing run-on dialogue and DOUBLE-UP remain the remedies.

## NEXT
1. Execute new gate independently on Ulysses ch1 and accepted Jeeves reference; establish expected HOLD/PASS, correct false positives.
2. Produce ranked RSP/OCR audit with sampled text and source attribution for credible method-threatening defects.
3. Repair only confirmed failures, revalidate, then actual-phone QA and explicit staging/promotion decision before Monday.

MY JOB: Make the new independent gate run and verify it with controlled fixtures, followed by RSP/OCR triage.
YOUR JOB: Assk ze questions. 
