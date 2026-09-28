# GUTS WORKFLOW CONSTITUTION

**Purpose:** stop regressions by separating layers, freezing wins, and requiring human-visible QA before moving downstream.

## 1. Read everything, then act narrowly

At every handover:
- read all GUTS documentation, code, workflows, configs and relevant data;
- read all NoBo material for context;
- remember that for GUTS, NoBo is operationally relevant only through **H2G2 arming**.

Do not begin by changing anything.

## 2. Work in this order only

1. **SOURCE TRUTH**
2. **CORPUS**
3. **READER**
4. **ARMING**
5. **DEPLOYMENT**
6. **COSMETICS**

A downstream layer must not silently rewrite an upstream layer.

## 3. Freeze wins

Once a layer or book passes:
- machine QA; and
- Stanley’s actual-phone visual QA;

it is **FROZEN**.

Do not globally regenerate, renumber, repaginate, relabel or “improve” frozen material unless a specific observed defect requires it.

## 4. Human-visible truth outranks structural neatness

A corpus is not “sound” merely because:
- JSON parses;
- chapter arrays exist;
- sockets count correctly;
- root/public copies match.

The spectator-facing test is decisive:

**Does this look and behave like the real book a spectator expects to see?**

Wrong chapter starts, missing chapters, bare-number Contents, false numbering or implausible openings are failures even when the files are internally consistent.

## 5. No destructive performance pruning

Never remove genuine chapters merely because they are:
- short;
- fewer than a target page count;
- inconvenient for pagination;
- cosmetically uneven.

Performance preparation may change pagination and add force material, but must preserve the complete intended source structure unless Stanley explicitly approves an editorial cut.

## 6. One authority per layer

Avoid overlapping sources of truth.

For each layer, identify one current authority:
- source master;
- generated corpus;
- Reader;
- Worker/state;
- deployment target.

Historical workflows, old generated reports and one-shot patches are evidence only unless explicitly promoted.

## 7. Automation is disposable

One-shot repair/build workflows:
- must be branch-only;
- must not write to `main`;
- must be quarantined immediately after successful use;
- must never remain active where a later push can replay old assumptions.

Automation must not outlive the problem it solved.

## 8. Every major change gets a clean rollback point

Before a risky change:
- freeze the current good state at an immutable commit and preferably a named backup branch;
- record the SHA in canonical docs;
- do not modify or delete that rollback point during the same repair pass.

## 9. QA gate for every layer

For each layer:

**A. Machine QA**
- syntax/parsing;
- counts;
- identity checks;
- invariants;
- no accidental overwrite.

**B. Stanley phone QA**
- visible Contents;
- genuine chapter starts;
- navigation;
- reader feel;
- actual spectator-facing behaviour.

Only after both pass does the layer become frozen.

## 10. No multi-layer repair passes

Do not combine:
- corpus rebuild;
- Reader redesign;
- state-machine changes;
- deployment changes;
- cosmetics

in one pass.

One problem class at a time.

## 11. Current freeze map

### Passed and frozen unless a specific defect appears
- Pooh
- Thurber
- Runyon
- Joyce

### Passed and frozen at corpus level
- Jeeves
- Huck
- Farewell
- Christie

All eight active books are now corpus-frozen. Reader presentation remains a separate downstream layer.

### Parked
- Parker

### Machinery already signed off and not to be reopened casually
- H2 PUSH / GUT PULL architecture
- Worker/KV transport
- READY / ARMED / CLEAN
- local PAID/dwell persistence
- selected-chapter opener protection

## 12. Production rule

`main` remains production truth until the complete release candidate passes:
- corpus QA;
- Reader QA;
- arming QA;
- deployment QA;
- actual-phone QA.

Do not touch `main` merely to make testing easier.

## 13. Mandatory status format

Every project status/handover must state:
- what is frozen;
- what is still open;
- what changed;
- current rollback point;
- **NEXT ACTION**.

## Current next action

Phone-QA the repaired main Reader presentation for all eight active books.

Do **not** regenerate or alter any corpus while doing Reader QA.
