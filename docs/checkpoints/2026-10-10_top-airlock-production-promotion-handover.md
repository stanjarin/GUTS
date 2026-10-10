# GUTS — 10 October 2026, live Reader promotion / handover

## STATUS: Reader promoted to Main, Cloudflare live deployment still requires verification
- **GUTS Main**: `837a0ce22773d8db9dafb0991d981007694b6263` — PR #7 merged, top-of-page Reader only.
- **Pre-promotion Main / rollback**: `06086d6c1290692d283a6a855cc12cf8a4485143`, immutable named branch `backup-pre-top-airlock-promotion-2026-10-10`. Preserve it.
- **User-approved experimental Reader**: frozen at `1ae4abe1e1f3ce83c996d932fa5bdcbb8fc95601`, branch `freeze-top-airlock-approved-2026-10-10`; GitHub Pages visual preview `https://stanjarin.github.io/GUTS/top-airlock/?browse=1`.
- User's actual-phone verdict: **"Perfect. Well, perfect enough."** The universal top-of-page airlock principle works beautifully. Do not reopen cosmetic repairs.
- Only changed files in production PR #7: `index.html`, `public/index.html`, `public/project_library/books/browse/index.html`. Same Reader mirrors. Base adjusted to `/` for production. **No Worker code, NoBo, KV, corpus or domains changed.**
- Premerge QA PASS: GitHub Actions `38043537147`. Tested all 18 books / 4,858 prepared pages: 0 missing top airlocks / 0 invalid next-sentence starts; simulated READY → ARMED word substitution on chapter 1 opener → 6-second dwell → PAID persistence → RESET passed.
- Separate isolated protocol rehearsal PASS `38041746845`, though this does *not* verify real NoBo phone command handoff.
- 18 book airlocks unchanged verbatim. Opener titles above first prose airlock. Kon-Tiki first-page slab headings suppressed, uppercase first prose word normalised, split chapter 7 slab suppressed. Gutenberg OCR flaws and occasional wording like "Then" deliberately accepted as prototype.
- **Guiding DESIGN STANdard:** "It should need less machinery, not more. We must resist rebuilding the elaborate system we've just made unnecessary." User explicitly wants minimum sensible engineering and no sprawl.

## Current unresolved deployment verification
- User sent `b46625ab`, apparently copied from Cloudflare. GitHub repo API cannot find a commit with that SHA; may be Cloudflare deployment ID, not evidence of wrong deployment.
- **DO NOT ask user again to navigate through Cloudflare or repeat instructions to get there.** The prior thread kept doing this and user observed the thread deteriorating. Ask for just the Cloudflare screenshot/details only if strictly necessary, but prefer read-only verification via tools.
- Need confirm Cloudflare latest `guts` deployment is **Success/Active** and source commit `837a0ce`; GitHub PR merge alone does not prove live deployment. The Worker aliases (`ebooks.fyi`, `www3.library.gutenbrg.com`, etc.) use one production Worker. Do not confuse deployment ID and source commit.
- If source commit verified deployed, user can use **NoBo BR+ first** as lowest-friction visual check for literal `$$$` on top of Reader; then normal NoBo ARM/RESET for actual performance rehearsal. **BR+ does not test ARMED or PAID.** Important user/assistant joke: accidental rhyme **"BR+. Much less fuss."**
- If live Reader can't be verified yet, clearly state uncertainty; don't invent Cloudflare state.
- Performance test: RESET → ARM distinctive word GOPHERS → normal `ebooks.fyi` GUTS route → selected chapter/page including opener shows injected word first prose paragraph → six-second dwell/departure PAID persists → NoBo RESET clears.

## Communication
- User age 74, artist/designer, wants brief direct `My job:` / `Your job:` when operational. Don't endlessly demand GO once given. No sheep jokes. They call assistant Kryten.
- Explicit user request: "This thread might be dying. Create handover now." This checkpoint is the handover. Provide a paste-ready new-thread greeting after verifying file and Main.
- Constitutional authority: `GUTS_WORKFLOW_CONSTITUTION.md`, `OPERATIONS_START_HERE.md`, `GUTS_CURRENT_STATE.md`, `docs/CURRENT_STATE.md`. Constitution "Read broadly, act narrowly." Production main is now `837a0ce` until docs-only handover commits change its head.
- Next stage is **VERIFY CLOUDFLARE ACTIVE DEPLOYMENT, THEN BR+ PHONE QA, THEN ARMED END-TO-END**. No more speculative side Workers or extra architecture. Preserve rollback.
