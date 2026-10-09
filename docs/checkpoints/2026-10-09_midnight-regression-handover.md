# GUTS / NoBo — 9 October 2026, midnight checkpoint

## Governing objective
Monday ASM demonstration is a **working prototype**, not release certification. Acknowledge pagination defects honestly; show a simple reliable NoBo → ebooks.fyi → GUTS effect. Retention of vision remains a **major visually obvious fault**, not trivial cosmetics. Avoid reopening huge factory audits, approximate simulators, or adding QA machinery to the performance path.

## Unresolved regression — FIRST JOB
Stanley reports that the prepared `$$$` insertion is no longer reliably the **first NEW paragraph** on the page, including Keys; a recent phone screenshot displayed it in the **fourth paragraph**. This rule reportedly worked previously. Treat this as a regression investigation, not a request to repaginate.

Source history: GUTS commit `bddc02d391f7` on 9 Oct consolidated/replaced all 18 JSONs. Compared Jean Brodie against 5 Oct `99a4d422dc69`: old 113 prepared pages with socket at paragraph 2 on 57 pages and paragraph 3+ on 56; current 113 pages, 107 socket pages all paragraph 2 (six chapter openers without socket). Reader mirrors currently share blob `6118a035...`, root/public Brodie JSON share `ea5e003...`. Hence an observed fourth-paragraph socket is **inconsistent with the current Main Brodie corpus**; whether the photographed page was Brodie and the precise served version still require checking. Do NOT conclude the 9 Oct consolidation caused this without deployed artifact evidence.

**Next decisive check:** Stanley supplies Cloudflare → Workers & Pages → guts → Deployments screenshot showing active deployment and source commit. Kryten compares against GUTS Main `5cd303dbd54a077c28188207493af7cf376870e0`, investigates actual live Reader and JSON / phone cache, and corrects only a proven cause. Cloudflare automatic GitHub Main deployment and five aliases are established in OPERATIONS_START_HERE.md; do not rediscover or rebuild it.

## NoBo QA shortcut
NoBo Main promoted to `07d85da4662444e3d73e8cd02c28fdbba7c9fd2d`: in control panel BR+ reveals **GUTS ↗** which navigates to camouflage Reader with `?browse=1`. Rollback branch `backup-pre-browse-handoff-2026-10-09` at `8626df947ca1771dcc4ce5eb4a4ed7cfe863e058`; working branch `browse-handoff-2026-10-09`. JavaScript syntax and GitHub read-back passed. Phone testing saw workers.dev in-app browser and fourth-paragraph socket; do not assume shortcut caused data regression. BR− is normal performance, BR+ inspection; READY separate from SHW/HIDD.

## Retention investigation
Old 5 Oct placement estimator was not preserved as reusable code. Historical criterion: 3 consecutive pages within 32px band, while current concern is consecutive above-fold two-page positions fewer than four rendered lines apart. Jean Brodie observed Ch3 pp27–28 ~3 lines (likely fail), Ch2 pp17–18 ~3 lines (likely fail), Ch3 pp12–13 5 lines (pass), Ch4 pp17–18 4 lines (pass). Character-difference scouting is not a reliable release QA. Simulator was abandoned as misleading; do not rebuild it ahead of Monday.

## Protocol
Read OPERATIONS_START_HERE.md FIRST. Read broadly, act narrowly; execute actions already authorised. Stanley says **SAGO** as a reminder to request GO; GO authorises work and is not a cue for verbal plans. Always state exact next executable action and who does it when blocked. No announcements of inaction, no reiterating Stanley's arguments, minimise bandwidth. At project-thread **3058 out**, checkpoint to GitHub, update current state if changed, verify; closing phrase preference: “Have you ejected WD3? / Latitude 90° North out.”

## Tomorrow
1. Obtain Cloudflare active deployment screenshot/commit and check served assets vs Main.
2. Determine why first-NEW-paragraph insertion appears to have regressed, without speculative repairs.
3. Once identified, smallest backed-up, tested correction and phone acceptance.
4. One end-to-end normal BR− NoBo performance rehearsal, freeze Monday prototype.
