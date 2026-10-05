# GUTS Strategic Plan — 6 October 2026

## Purpose

GUTS has outgrown the workflow in which ChatGPT manually carries large amounts of corpus work through one conversation.

The project now needs two parallel objectives:

1. **A reliable one-book demonstration for the ASM meeting on Monday 12 October 2026.**
2. **A durable completion architecture for the full 18-book system.**

The central strategic change is:

> **ChatGPT designs, supervises and diagnoses. Deterministic tooling does bulk corpus work.**

GitHub is not merely storage. GitHub branches, Actions, scripts, artifacts and reports become the heavy-lifting factory. Cloudflare remains the live runtime / routing / state layer. ChatGPT must not be the freight engine.

---

# I. Non-negotiable principles

## 1. Source truth is immutable

The genuine book text is source truth.

Bulk repair may alter only the prepared / force layer unless Stanley explicitly approves an editorial change.

For every build:
- genuine paragraph hash must remain unchanged;
- genuine token order must remain unchanged;
- no genuine words may be inserted, removed or reordered.

## 2. One final factory, not serial patch campaigns

Do not continue the pattern:

> repair A → discover B → patch B → discover C → patch C

Instead:

> source truth → one deterministic build engine → candidate corpus → machine QA → phone QA → promotion

If a new law is discovered, update the factory specification and rebuild from source truth. Do not stack repair campaigns on repaired output unless explicitly required.

## 3. ChatGPT must never be the bulk processor

ChatGPT may:
- define laws;
- write / revise scripts;
- inspect small representative samples;
- interpret QA reports;
- diagnose exception classes;
- decide which narrow change comes next.

ChatGPT should not:
- ingest thousands of pages into conversation;
- manually classify comma-number populations;
- carry long-running corpus state in thread memory;
- be relied on to finish a multi-thousand-page operation before a wall hit.

All comma-scale jobs belong in deterministic external tooling.

## 4. Every major operation must survive the death of the ewe

A new ChatGPT thread must be able to resume from:
- one specification file;
- one current-state file;
- one build report;
- one exception manifest;
- exact branch / SHA anchors.

Conversation continuity is helpful, never critical.

## 5. Human-visible truth outranks elegant machinery

Machine QA proves invariants.

Stanley's actual iPhone remains authority for:
- camouflage;
- visual rhythm;
- Reader feel;
- believable page heads;
- believable airlock placement;
- performance behaviour.

---

# II. Final prepared-page laws

These laws are the current target specification and must be made explicit before the full factory run.

## A. Page-head law

Every forceable prepared page begins with genuine prose carried from the previous page.

The page head must begin **mid-sentence**, not at a fresh sentence or fresh paragraph.

Purpose: the top of a prepared page must not look deliberately constructed.

## B. Airlock-boundary law

The airlock may be inserted only after a genuine completed sentence.

Do not globally repair Gutenberg OCR or paragraph oddities merely to beautify the book.

Asymmetric rule:

> **The airlock boundary must be clean. Everything else may remain gloriously Gutenberg.**

## C. Genuine-text law

The genuine token stream is inviolable.

Prepared paragraph boundaries may be rearranged for camouflage, but genuine word order may not change.

## D. Rendered-line placement law

Authoritative Reader geometry:
- Georgia;
- 15 CSS px;
- line-height 1.45;
- fixed 329 CSS px text measure.

Working socket-start target cycle:

**8 → 12 → 16 → 10 → 14 → repeat**

Exact target is desirable, not sacred.

Where exact placement is impossible:
- choose nearest legal line;
- avoid repeating the immediately preceding socket line where possible;
- aim for at least four rendered lines separation.

## E. Retention law

Any run of three prepared pages whose socket starts fall within a four-line band is a retention defect and should be broken where legally possible.

## F. Existing frozen performance laws

Do not disturb without a specific observed defect:
- exact $$$ substitution;
- selected-chapter opener protection;
- READY / ARMED remote protocol;
- 6-second dwell;
- local PAID persistence;
- SHW / HIDD orthogonality;
- NoBo commands / GUTS executes;
- current production routing and domain behaviour.

---

# III. Architecture — who does what

## Stanley

Authority for:
- design intent;
- acceptable deception;
- visual PASS / FAIL;
- performance practicality;
- final promotion approval.

Stanley should not be asked to inspect thousands of pages.

## ChatGPT

Role:
- architect;
- diagnostician;
- code author;
- exception analyst;
- QA interpreter;
- release foreman.

Normal working unit:
- small samples;
- compact manifests;
- machine reports;
- exact exceptions.

## GitHub

Role:
- source control;
- branch isolation;
- rollback;
- deterministic build execution through GitHub Actions;
- machine QA;
- artifact / report generation;
- persistent project state.

GitHub becomes the factory floor.

## Cloudflare

Role:
- production delivery;
- routing;
- Worker / KV state;
- NoBo ↔ GUTS runtime transport.

Cloudflare should not become the corpus factory unless a later requirement specifically demands it.

## Porkbun

Role:
- domain registration / ownership.

No corpus or application logic belongs there.

---

# IV. Track A — Monday ASM demo

## Objective

By Monday 12 October 2026, have **one book that is genuinely finished and frozen** for demonstration.

Stanley may openly explain that GUTS is still under development and ask the group to choose the designated demonstration title.

This is a prototype demonstration, not a claim that all 18 books are complete.

## A1. Select the demo book

Choose by engineering suitability, not sentiment.

Desired characteristics:
- conventional prose and punctuation;
- clean Gutenberg source;
- sufficient chapter length;
- few pathological OCR splits;
- no unusual typographic structures;
- enough prepared pages to demonstrate convincing freedom;
- low unresolved rate under the final boundary laws.

Likely candidate:
- **Right Ho, Jeeves**

But selection should be confirmed by a cheap machine comparison, not assumption.

The comparison should process metadata / counts only and return a tiny table:
- prepared pages;
- pages legally solvable;
- unresolved count / percentage;
- chapter-edge complications;
- obvious pathology count.

No full corpus content should enter ChatGPT.

## A2. Create a protected demo branch

Once selected:

- branch from known production / source anchor;
- isolate the chosen book only;
- freeze all unrelated Reader, NoBo, Cloudflare and corpus material;
- record exact starting SHA.

No experiment outside the chosen book belongs on this branch.

## A3. Make the demo book the reference implementation

Run the final laws against the entire chosen book.

Goal:
- every forceable page begins mid-sentence;
- every airlock follows a completed genuine sentence;
- rendered placement obeys target / spacing law where possible;
- zero unapproved unresolved pages;
- genuine corpus invariants PASS.

If exceptional pages cannot satisfy every soft placement rule, prefer deception laws over numerical elegance.

Hard priority:
1. genuine text integrity;
2. mid-sentence page head;
3. completed-sentence airlock boundary;
4. one clean socket;
5. plausible rendered placement;
6. stagger / retention optimisation.

## A4. Machine QA gate

Demo candidate must report:
- pages processed;
- pages changed;
- unresolved pages;
- genuine hash mismatches;
- genuine token-order mismatches;
- page-head failures;
- airlock-boundary failures;
- socket count failures;
- retention / spacing residuals;
- root/public parity.

Hard gate:
- zero genuine mismatches;
- zero page-head boundary failures;
- zero airlock-boundary failures;
- zero malformed socket pages.

No promotion if a hard gate fails.

## A5. Stanley phone QA

Use a fixed torture sample from the demo book:
- early page;
- middle page;
- late page;
- short donor;
- long donor;
- awkward punctuation;
- chapter edge if applicable;
- several consecutive prepared pages to judge rhythm.

Stanley marks simple PASS / FAIL.

If failures occur, fix the factory law, not the individual page unless the page is explicitly documented as an exception.

## A6. Freeze the ASM demo release

After PASS:
- tag / branch exact demo SHA;
- record rollback;
- write a one-page ASM demo checklist;
- make no further corpus changes to that book before Monday unless a demonstrated defect appears.

The demo release is operationally frozen even while the full project continues elsewhere.

---

# V. Track B — full GUTS completion

Track B must not jeopardise Track A before Monday.

## B1. Write the factory specification

Before another large repair run, define in one canonical document:
- all hard laws;
- all soft preferences;
- precedence when laws conflict;
- what constitutes unresolved;
- what is allowed to change;
- what must never change;
- required machine QA outputs;
- promotion criteria.

This specification is the contract.

## B2. Build one deterministic corpus engine

The engine should:

1. load immutable source truth;
2. construct prepared pages under the final laws;
3. render / measure using the canonical geometry;
4. validate every hard invariant;
5. write candidate corpus only to a work branch or artifact;
6. produce a compact summary report;
7. produce a separate exception manifest;
8. return PASS / HOLD / FAIL.

No automatic write to main.

## B3. Design reports for ChatGPT-scale consumption

The main report should be small.

Example:

- books: 18
- prepared pages: 4,858
- solved: 4,721
- unresolved: 137
- genuine mismatches: 0
- head-law failures: 0
- airlock-boundary failures: 0
- socket failures: 0
- spacing residuals: 19
- retention residuals: 7
- verdict: HOLD

The exception manifest may contain the full list externally.

ChatGPT receives:
- counts by cause;
- books / chapters affected;
- representative samples only.

## B4. Classify unresolved cases mechanically

Do not ask ChatGPT to read 1,964 unresolved pages.

The engine itself should assign reason codes such as:
- NO_LEGAL_MID_SENTENCE_CUT;
- NO_TERMINAL_SENTENCE_AFTER_CUT;
- DONOR_TOO_SHORT;
- CHAPTER_EDGE;
- OPENER_PROTECTION;
- SPACING_CONFLICT;
- RETENTION_CONFLICT;
- SOCKET_CONSTRAINT;
- OTHER.

Then produce counts.

Only dominant classes need human diagnosis.

## B5. Resolve blockers by precedence, not improvisation

When laws conflict, hard deception / integrity laws win.

Suggested precedence:
1. genuine text integrity;
2. page-head mid-sentence;
3. clean completed-sentence airlock boundary;
4. one valid socket;
5. chapter / opener protection;
6. legal rendered placement;
7. four-line staggering;
8. retention optimisation;
9. exact cycle target.

A lower rule may be relaxed only if documented and machine-reported.

## B6. Scale in stages

Never jump directly from five samples to all 18 books.

Use:
- **Stage 1:** 5-page functional sample;
- **Stage 2:** one entire reference book;
- **Stage 3:** small mixed-book proving batch;
- **Stage 4:** all 18 books on work branch;
- **Stage 5:** machine QA;
- **Stage 6:** Stanley phone torture suite;
- **Stage 7:** promotion;
- **Stage 8:** production smoke test.

Each stage must pass before the next.

## B7. Permanent phone torture suite

Create a fixed set of representative stress pages / chapters covering:
- conventional prose;
- dialogue;
- OCR oddity;
- Joyce;
- Peake;
- short chapter;
- chapter opening;
- long paragraph;
- near-bottom socket;
- several consecutive pages for retention rhythm.

Use the same suite for every release candidate.

Do not invent a fresh QA sample after every change unless the defect demands one.

## B8. Promotion

Before full promotion:
- immutable rollback branch / tag;
- candidate branch SHA recorded;
- machine report PASS;
- phone torture suite PASS;
- root/public parity verified.

Promotion should be one deliberate release event, not accumulated incidental commits.

After promotion:
- verify public domains;
- run complete NoBo → GUTS performance chain;
- record release SHA;
- freeze.

---

# VI. Stop rules — preventing another ChatGPT bridge collapse

Any one of these means stop and change method:

- task involves hundreds / thousands of page-level decisions inside chat;
- tool output must dump large corpus text into conversation;
- a run is silent for an implausibly long period;
- a repair requires repeated giant repository scans;
- ChatGPT needs to remember unpersisted intermediate state;
- the only evidence of success is a hand-built fixture;
- machine QA assertion is tautological rather than independently measured;
- a repair run writes output even though its QA is HOLD;
- production must be modified merely to make testing convenient.

When a stop rule triggers:
1. persist state;
2. reduce the problem;
3. move bulk computation to deterministic tooling;
4. resume from compact evidence.

---

# VII. Definition of DONE

GUTS is finished when:

1. final factory specification is frozen;
2. deterministic build engine exists in repository;
3. all 18 books build from source truth;
4. hard invariant failures = 0;
5. unresolved cases = 0, or each remaining exception is explicitly approved and documented;
6. machine placement / retention QA meets approved thresholds;
7. fixed Stanley phone torture suite PASSES;
8. NoBo ↔ GUTS full performance chain PASSES on production;
9. production domains verified;
10. rollback anchors recorded;
11. release SHA recorded;
12. current-state / handover documents updated;
13. production is frozen.

After this point, new ideas are new-version work, not reasons to reopen the finished release.

---

# VIII. Immediate order of battle

## Before Monday

1. Do **not** attack the 1,964 unresolved pages globally.
2. Select the safest demo book by cheap machine metrics.
3. Create protected demo branch.
4. Use that one book to finish / validate the final factory behaviour.
5. Machine-QA the whole demo book.
6. Stanley phone-QA the demo book.
7. Freeze ASM demo release.

## After demo book is secure

8. Finalise full factory specification.
9. Build / harden permanent GitHub Actions corpus pipeline.
10. Add reason-coded exception reporting.
11. Prove on a mixed-book batch.
12. Run all 18 books externally.
13. Diagnose only exception classes / representative cases in ChatGPT.
14. Full machine gate.
15. Stanley fixed phone torture suite.
16. Promote once.
17. Production smoke test.
18. Freeze release.

---

# Strategic summary

The project no longer asks:

> **What do we fix next?**

It asks:

> **What machinery will take the known source truth to the finished system reproducibly, while making ChatGPT failure irrelevant?**

Monday's one-book release is the first production proof of that machinery.

The full 18-book release is the same process at freight scale.
