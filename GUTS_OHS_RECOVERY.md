# GUTS — OH&S / RECOVERY RAILS

**Operational safety sheet — 27 Sep 2026**

This is software OH&S: the rules intended to stop a repair from injuring the known-good production machine.

## RED RULES

1. **Do not touch `main` during the corpus audit.** Work only on `contents-repair`.
2. **Do not deploy from `contents-repair` while investigating.** A branch is not a rehearsal licence for production.
3. **Do not run a workflow by name alone.** Read its triggers, checkout ref, write target, commit/push target and deploy step first.
4. **Do not force-update any safety branch.** Preserve `GUTS-035-KNOWN-GOOD` and current `main` history.
5. **Do not repair symptoms before locating the layer that caused them.** Contents label, chapter mapping, transformed corpus, source corpus, Reader routing and Worker state are different layers.
6. **Do not reopen signed-off state machinery because a corpus/title/opening problem exists.** READY/ARMED/CLEAN transport and local PAID/dwell/persistence are separate.
7. **Do not overwrite source/original material.** Repairs create a new checked derivative; originals remain evidence.
8. **Do not put Cloudflare secrets/PIN values in GitHub.** Preserve bindings; never manufacture replacements during recovery.
9. **Do not assume root `index.html` is what production serves.** Current Cloudflare config serves `./public`; root/public drift has already caused a false diagnosis once.
10. **Do not let connector/tool friction redesign the app.** If a large write route is blocked, change the engineering route, not the proven architecture.

## CURRENT SAFETY ANCHORS

- Production `main` head at emergency handover: `b662978d1de67304cc96ad78e3c224f2d2b75533`.
- Working branch: `contents-repair`.
- First branch checkpoint: `c7b75c6f365cf5a7723256aa8ad84c05976e6a5a`.
- Frozen rollback branch: `GUTS-035-KNOWN-GOOD`.
- Production Reader baseline: GUTS 0.35 / `v0.35-performance-reader`.
- Domain: `gutenbrg.com`.

## BEFORE ANY WRITE

Confirm all four:

- target branch is `contents-repair`;
- file/layer is actually implicated by evidence;
- an upstream/original copy exists or the current blob/commit is recoverable;
- the write cannot trigger a production deploy.

If any answer is unknown, inspect first.

## CORPUS REPAIR METHOD

For each title, make an evidence table before mutation:

- source/original identity and chapter/story count;
- PRIMED identity/count;
- PERFORMANCE35 identity/count;
- retained versus omitted sections and why;
- source ID/title -> transformed ID/title -> displayed label;
- intended opening page versus actual opening page;
- prepared-page / `force_paragraphs` / `$$$` status.

Only then choose the smallest repair that restores a coherent performance edition.

## RECOVERY IF A BRANCH WRITE GOES WRONG

1. Stop. Do not make a second compensating guess.
2. Record the bad commit SHA and affected paths.
3. Compare against the previous `contents-repair` commit and against `main`.
4. Restore/revert only the affected branch material.
5. Re-run mechanical checks before continuing.
6. `main` should still be untouched; verify that explicitly.

## RECOVERY IF PRODUCTION APPEARS WRONG

1. Do not immediately redeploy.
2. Verify what `main` points to.
3. Verify what Cloudflare is actually serving and which deployment is at 100% under **View all deployments**.
4. Verify Reader metadata and the code that generates any visible version stamp.
5. Compare root `index.html` with `public/index.html`.
6. Compare production candidate with `GUTS-035-KNOWN-GOOD`.
7. Preserve runtime bindings/secrets while rolling back.

## RELEASE GATE

A candidate repair is not releasable until:

- provenance/mapping is documented;
- mechanical corpus checks pass;
- all displayed destinations are valid and performance-capable;
- opening alignment is correct;
- socket/force data is intact;
- served `public` assets are intentionally synchronised;
- compact actual-phone QA passes;
- rollback point is named and preserved.

## HUMAN FACTOR

When Stanley is asked to inspect Cloudflare, provide the exact human-readable deployment/commit description to look for. Do not send him hunting by SHA alone.

Keep testing demands proportional. Do not ask for a full ARMED → PAID chain solely because documentation, labels or unrelated cosmetics changed.

**Rule of thumb: preserve the bird that flies; dissect the copy on the bench.**