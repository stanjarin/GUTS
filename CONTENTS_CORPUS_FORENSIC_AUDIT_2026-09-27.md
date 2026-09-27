# GUTS — CONTENTS / CORPUS FORENSIC AUDIT

**Date:** 27 September 2026  
**Scope:** eight active performance titles; Parker excluded/parked.  
**Branch:** `contents-repair` only.  
**Production `main`: untouched.**

## Executive finding

There is **not one common Contents failure**.

Three distinct states exist:

1. **Clean / structurally aligned:** Pooh, Thurber, Jeeves.
2. **Structurally aligned but deliberately source-discontinuous because short chapters were cut:** Farewell, Huck, Christie.
3. **Opening alignment broken by a later structural regrouping step:** Runyon, Joyce.

No evidence found that the original/source masters were destroyed. The 0.35 builder explicitly preserved source masters and generated separate PERFORMANCE35 files.

## Book findings

### AAM — The House at Pooh Corner — CLEAN
Source grouping has ten genuine chapters. PERFORMANCE35 retains all ten, each prepared chapter begins at its genuine chapter opening, and the current authoritative Contents table supplies the genuine Milne chapter titles.

Result: **no corpus repair indicated.**

### JT — My Life and Hard Times — CLEAN
The PRIME2 source contains a Preface, nine essay/chapter titles, separate two-word CHAPTER markers, and a terminal Note. The 0.35 builder correctly discarded the isolated two-word markers as false structural groups and retained the Preface plus nine genuine essay sections. Current Contents maps those ten retained sections correctly.

Result: **no corpus repair indicated.**

### Jeeves — Right Ho, Jeeves! — CLEAN / VERIFY ONLY
The 0.35 builder processed the inherited NoBo master chapter-by-chapter, retained all 23 chapters, and repaginated *within each chapter*. No later commit changed `PERFORMANCE35/jeeves_035.json`.

Result: chapter-opening alignment is preserved by construction. **No repair indicated; compact visible verification only.**

### Huck — Adventures of Huckleberry Finn — STRUCTURALLY ALIGNED, ONE SOURCE CHAPTER CUT
The 0.35 builder processed the inherited master chapter-by-chapter and retained 42 of 43 chapters. Source Chapter 43 was cut for insufficient performance depth. No later commit changed `PERFORMANCE35/huck_035.json`.

Result: every surviving destination begins at a genuine retained chapter opening. Display numbering may be treated as an edited 42-chapter edition, but the underlying corpus is aligned. **No corpus repair indicated.**

### Farewell — A Farewell to Arms — STRUCTURALLY ALIGNED, SOURCE GAPS BY DESIGN
The 0.35 builder retained 34 of 41 source chapters and cut source Chapters 1, 8, 17, 22, 26, 32 and 39 for performance-depth reasons. It repaginated each retained chapter separately. No later commit changed `PERFORMANCE35/farewell_035.json`.

Result: surviving entries begin at genuine retained chapter openings, but source chapter identity is discontinuous. Consecutive spectator-facing numbering is an editorial-edition choice, not evidence of corruption. **No corpus repair indicated.**

### AC — The Murder at the Vicarage — DISCONTINUITY IS BUILDER POLICY, NOT MYSTERY CORRUPTION
PRIME2 contains the complete 32-chapter sequence. The 0.35 performance builder deliberately retained only chapters capable of producing at least three performance-depth pages.

Retained source chapters are:

**5, 6, 11, 12, 22, 23, 24, 25, 26, 30, 32**

The current PERFORMANCE35 file therefore correctly reflects what that builder produced. Its discontinuity is real, but it is **not unexplained source loss**.

All retained Christie entries still begin at their genuine source chapter openings and retain prepared sockets.

Result: Christie needs an **editorial/product decision**, not forensic reconstruction:
- accept an edited 11-destination edition and renumber/display it coherently; or
- rebuild Christie under different chapter-depth rules if all/most source chapters are required.

Do not patch labels while pretending the PERFORMANCE35 corpus contains Chapters 1–11 of the original.

### DR — On Broadway — BROKEN OPENING ALIGNMENT
Initial 0.35 build produced four very large detected performance groups over 744 prepared pages. A later “structure repair” then:
1. flattened all prepared pages out of those groups;
2. divided the 744 pages into **18 near-equal chunks** of 41–42 pages;
3. labelled them Story 1–18;
4. later overlaid genuine Runyon story names in the Reader Contents.

That regrouping explicitly ignored original story boundaries. Therefore a genuine story title can currently open on an arbitrary mid-story page.

Important: the repair did **not** alter prose, pagination, air-locks or sockets; it altered chapter/group boundaries only.

Result: **structural mapping must be repaired** by restoring genuine story-opening boundaries over the already-prepared pages. Do not repaginate unless proven necessary.

### JJ — Ulysses — BROKEN OPENING ALIGNMENT
Initial 0.35 build collapsed Ulysses into one oversized 726-page performance group because the PRIME2/build heading detection did not preserve the 18 episodes as separate built groups.

A later “structure repair” then:
1. flattened the 726 prepared pages;
2. split them into **18 near-equal chunks** of 40–41 pages;
3. labelled them Episode 1–18;
4. later overlaid the genuine 18 episode names.

Equal page division is not episode mapping. Hence current named Contents entries can land mid-episode.

Again, prose, prepared pages, air-locks and sockets were left untouched; the broken layer is the grouping/boundary map.

Result: **structural mapping must be repaired** by locating the genuine 18 episode openings in the prepared page stream and setting group boundaries there. Do not repaginate unless evidence forces it.

## Current safe repair order

1. **Runyon:** recover genuine story-start boundaries over existing prepared pages.
2. **Joyce:** recover genuine episode-start boundaries over existing prepared pages.
3. **Christie:** make explicit editorial decision about the deliberately reduced 11-chapter performance edition.
4. Re-verify Pooh, Thurber, Jeeves, Huck and Farewell mechanically after any shared Reader/Contents changes.
5. Parker remains out of scope.

## Safety conclusions

- Do **not** rebuild all eight books.
- Do **not** apply a Christie-derived fix globally.
- Do **not** repaginate Runyon/Joyce merely to fix their Contents boundaries.
- Do **not** reopen state/Cloudflare/payoff machinery.
- Preserve every existing prepared page and its `force_paragraphs` / `$$$` socket unless a specific page-level defect is independently proven.
- Continue only on `contents-repair`; `main` remains the production rollback truth.

## Evidence trail

Primary evidence used:
- `PERFORMANCE35/BUILD_REPORT.md`
- `PERFORMANCE35/AUDIT.md`
- `PERFORMANCE35/STRUCTURE_REPORT.md`
- `PRIMED/QA_PRIME2.md`
- `INHERITED_MASTERS.md`
- `.github/workflows/guts035_build.yml`
- historical Joyce/Runyon structure-repair commits/workflow
- current `index.html` Contents mapping
- direct PRIME2-to-PERFORMANCE35 structural inspection for Pooh, Christie and Thurber
- Git comparison from the initial PERFORMANCE35 build to current `contents-repair`, confirming only Runyon and Joyce performance JSONs were subsequently structurally modified.

**AUDIT RESULT: two genuine mapping repairs (Runyon, Joyce); one editorial decision (Christie); five structurally sound books (Pooh, Thurber, Jeeves, Huck, Farewell).**
