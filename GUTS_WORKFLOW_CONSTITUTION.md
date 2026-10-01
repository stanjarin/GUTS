# GUTS WORKFLOW CONSTITUTION

**Purpose:** prevent regressions by separating layers, freezing wins, and requiring machine + phone QA before promotion.

## 1. Read everything, then act narrowly

At every handover:
- read this constitution;
- read the latest dated handover;
- read `GUTS_CURRENT_STATE.md` and `docs/CURRENT_STATE.md`;
- read relevant GUTS code/config/docs;
- read relevant NoBo handover/README for the cross-system control contract.

Do not begin by changing anything.

## 2. Work in this order only

1. SOURCE TRUTH
2. CORPUS
3. READER
4. ARMING / STATE
5. DEPLOYMENT
6. COSMETICS

A downstream layer must not silently rewrite an upstream layer.

## 3. Freeze wins

Once a layer passes:
- machine QA; and
- Stanley’s actual-phone QA;

it is **FROZEN**.

Do not globally regenerate, renumber, repaginate, relabel or “improve” frozen material unless a specific observed defect requires it.

## 4. Human-visible truth outranks structural neatness

A corpus or interface is not “sound” merely because files parse and counts match.

The spectator-facing test is decisive:

**Does this look and behave like the real thing a spectator expects to see?**

## 5. No destructive performance pruning

Never remove genuine chapters merely because they are short, awkward, inconvenient for pagination, or cosmetically uneven.

Any deliberate editorial cut must be explicitly approved and documented.

## 6. One authority per layer

For each layer identify one authority:
- source master;
- generated corpus;
- Reader;
- Worker/state;
- deployment target.

Historical workflows, old generated reports and one-shot patches are evidence only unless explicitly promoted.

## 7. Automation is disposable

One-shot repair/build workflows:
- branch-only;
- never write to `main`;
- quarantine after use;
- never remain active where a later push can replay old assumptions.

## 8. Every major change gets a rollback point

Before risky promotion/deployment:
- freeze the current good state at an immutable commit;
- preferably create a named backup branch;
- record the SHA in canonical docs;
- do not alter/delete that rollback point during the same pass.

## 9. QA gate

Every layer requires:

**Machine QA**
- syntax/parsing;
- counts/invariants;
- identity/parity checks;
- no accidental overwrite.

**Stanley phone QA**
- visible behaviour;
- navigation;
- reader feel;
- actual performance chain.

Only after both pass does the layer freeze.

## 10. No mixed repair campaigns

Do not combine unrelated:
- corpus rebuild;
- Reader redesign;
- state-machine repair;
- deployment changes;
- cosmetics.

One problem class at a time.

## 11. Canonical control architecture

**NoBo commands. GUTS executes.**

Three independent axes:

### MAGIC
- READY
- ARMED
- local PAID

Remote NoBo↔GUTS protocol is **READY / ARMED only**.

### VISIBILITY
- SHW
- HIDD

Visibility changes must not alter magic state.

### AUTH
- valid / invalid

Validation must not alter magic state.

CLEAN is historical and is not part of the current live protocol.

## 12. Current freeze map — 2 Oct 2026

Passed/frozen unless a specific observed defect appears:
- 18-book corpus/shelf;
- Reader presentation;
- exact `$$$` substitution;
- selected-chapter opener protection;
- 6-second dwell;
- local PAID persistence;
- H2 PUSH / GUT PULL;
- Worker/KV transport;
- READY / ARMED remote protocol;
- non-mutating ARM validation;
- SHW/HIDD orthogonality;
- landing/pre-page;
- carousel;
- cover behaviour;
- complete phone-tested chain:
  **RSET → READY → ARM → GUTS → dwell → PAID → RSET → cleared**.

Deferred only:
- production promotion;
- production domain attachment/verification;
- final smoke test;
- cosmetics/editorial items in `docs/COSMETICS_LATER.md`.

## 13. Production rule

`main` remains production truth until a tested release is deliberately promoted.

Do not touch `main` merely to make testing easier.

Before promotion:
- create rollback points;
- record SHAs;
- promote only QA-passed work;
- verify each repo after promotion;
- run final production phone smoke QA.

## 14. Mandatory handover/status content

Every handover must state:
- what is frozen;
- what is open;
- what changed;
- current rollback/branch anchors;
- exact next action.

## Current next action

**Promotion/deployment only.**

Create rollback points, promote the QA-passed GUTS/NoBo branches, repoint NoBo to production GUTS, verify `ebooks.fyi`, run one final phone smoke test, then freeze the release.
