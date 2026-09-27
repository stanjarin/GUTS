GUTS THREAD-WALL CHECKPOINT — 27 Sep 2026

DO NOT alter production main during audit. Working branch `contents-repair` was created from current main.

CURRENT TEST RESULTS
- Pooh: Contents clean.
- Thurber: Contents clean.
- Runyon: Contents titles correct; selections can open on non-story-start pages. Needs opening alignment audit.
- Joyce: Contents titles correct; selections can open on non-episode-start pages. Needs opening alignment audit.
- Christie: broken/discontinuous Contents (observed 5, 6, 11, 12, 22, 23, 24, 25...).
- Parker: parked/non-runner for now.

CRITICAL DISCOVERY
`PERFORMANCE35/ac_035.json` itself begins with a `Chapter 5` chapter object and is discontinuous. This is therefore not merely a display-label problem. Stanley has originals. Do not claim originals were destroyed; current PERFORMANCE35 is the suspect transformed corpus.

NEXT ACTION
Stop editorial patching. Audit corpus provenance/integrity before more repairs:
original/source -> PRIMED/PERFORMANCE35 -> chapters retained/omitted -> renumbering/mapping -> page/opening alignment -> insert sockets preserved.
Priority: Christie first; then Runyon, Joyce; verify Pooh/Thurber; then Jeeves/Farewell/Huck; Parker last/special case.

LIVE META
`aam` House at Pooh Corner -> PERFORMANCE35/aam_035.json
`jeeves` Right Ho, Jeeves! -> PERFORMANCE35/jeeves_035.json
`farewell` A Farewell to Arms -> PERFORMANCE35/farewell_035.json
`huck` Huckleberry Finn -> PERFORMANCE35/huck_035.json
`dp` Men I’m Not Married To -> PRIMED/DP_GUTS_PRIME2.json
`dr` On Broadway -> PERFORMANCE35/dr_035.json
`ac` Murder at the Vicarage -> PERFORMANCE35/ac_035.json
`jj` Ulysses -> PERFORMANCE35/jj_035.json
`jt` My Life and Hard Times -> PERFORMANCE35/jt_035.json
Display order: jt, jeeves, farewell, aam, huck, dp, dr, ac, jj.

RELEASE DISCIPLINE
Keep known-good MAIN THANG intact. Work on branch/copy. Test complete replacement. At release, archive/rename old known-good as *_old, then make checked new bird live.

GITHUB/CLOUDFLARE
Normal large one-line index update calls were repeatedly blocked by connector checks; do not redesign the app merely because of that. Blob/tree route worked for Git objects. Workflow route eventually succeeded for Contents patch. Cloudflare root-directory build problem was repaired earlier. Current main reader identifies v0.35-performance-reader.

EDITORIAL PRINCIPLES
Use authoritative real titles. Do not invent prose headings where real titles exist. Do not leave unusable selectable entries merely as clean/non-payoff choices. Hiding unusable entries and renumbering may be valid only after mapping is understood. Christie had previously appeared fixed; locate known-good historical mapping before inventing another.

COMMUNICATION
Sparse comms. `go` = assistant acts. Do not ask Stanley to say go unless permission is actually needed. Prefer `Found it` over irrelevant implementation detail. Always provide/action the next concrete step, not status-only reports.

NEW CHAT START
Continue GUTS from this checkpoint. Do NOT touch main. Start by auditing corpus provenance/integrity on `contents-repair`, beginning with `PERFORMANCE35/ac_035.json` against the best available original/source.