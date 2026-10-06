# 18-book factory repair brief — stagecraft law from Jeeves pilot

**Date:** 7 Oct 2026  
**Status:** approved working policy for the Motherlode factory  
**Reference demo:** Jeeves phone-QA PASS

## Objective

Transform prepared pages so they survive casual real-phone inspection during performance while preserving canonical source truth.

The factory is not a literary restoration project. It is performance machinery.

## Authority hierarchy

1. canonical genuine source / `paragraphs` — immutable;
2. prepared layer / `force_paragraphs` — editable camouflage layer;
3. actual rendered phone appearance — decisive QA authority;
4. machine metrics — diagnostics and gates, not aesthetic truth.

## Page-pump law

Every prepared page should begin in the middle of a genuine-looking sentence carried from the previous page. A clean sentence start at the top is a defect unless explicitly accepted by Stanley.

Airlock `$$$` appears later at varied rendered depth.

Chapter-opening prepared pages remain socket-free.

## Placement / retention

Use the current fixed Reader geometry:
- Georgia 15 CSS px;
- line-height 1.45;
- fixed 329 CSS px centred measure.

Vary airlock paragraph start height. Avoid visually obvious repetition across nearby pages. Machine spacing rules are guidance; Stanley phone QA decides whether a page actually calls attention to itself.

## Adjacent-page camouflage

Distinctive prose visibly repeated from one ordinary page into the next is a retention defect.

Exception: deliberate DOUBLE-UP at the bottom of a visually short page is legal because the repeated material is placed where spectators are unlikely to compare it against the following page top.

## Ridiculously Short Page rule — DOUBLE-UP

When a prepared page N is visually too short:

1. leave its existing prepared content intact;
2. append genuine prose copied from the beginning of page N+1;
3. append enough to make page N look normally occupied;
4. **do not move the break point of N+1**;
5. therefore N+1 still begins with the copied prose;
6. record the borrow/overlap explicitly in machine metadata/reporting.

Do not globally repaginate merely to solve a local short page.

The Jeeves pilot demonstrated that this overlap is visually acceptable on actual phone QA.

## Dialogue compaction

Short alternating dialogue may be run together in the prepared layer where individual one-line paragraphs create conspicuous vertical patterns or defeat placement.

Artificial helper labels must not remain visible if they advertise the surgery.

For Jeeves, `SELF:` and `JEEVES:` are deliberately stripped at render time. Equivalent helper labels in other books should be removed or rendered invisibly only when they are machinery rather than genuine text.

## Borrowed filler

If local genuine prose is insufficient:
1. same page/adjacent continuation first;
2. same chapter next;
3. nearby chapter only as fallback;
4. preserve source truth;
5. flag every nonlocal borrow in the report.

Avoid borrowing from immediate neighbours when that would create obvious ordinary adjacent-page repetition.

## Machine gates

At minimum report:
- unresolved prepared pages;
- top-of-page sentence-start failures;
- chapter-opener socket failures;
- ordinary adjacent-prose overlap failures;
- airlock placement/spacing;
- retained source identity;
- root/public parity;
- DOUBLE-UP pages and word counts;
- borrowed-fill pages and source locations.

A machine PASS does not freeze the result. Stanley actual-phone QA is required.

## Freeze rule

Once a book receives machine PASS plus Stanley phone PASS, freeze it.

Do not rerun broad repair over a frozen book unless a specific observed defect requires it.

## Production isolation

The 18-book factory runs on branch/Actions machinery only.

Production `main`, `ebooks.fyi`, and the current show system stay usable throughout processing. Nothing becomes production until deliberate promotion after QA.

## Reference anchor

Jeeves phone-QA reference candidate before documentation-only freeze commits:

`07cd1fb8b72b957fdd22d6acea2f904a63e0adf3`

Cloudflare reference preview:

`https://b55e014a-guts.stanjarin.workers.dev/?browse=1`
