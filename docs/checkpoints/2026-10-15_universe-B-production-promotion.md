## Final acceptance — 15 October 2026
Stanley reports **ALL A-OK** after testing the live production chain on his iPhone. **PRODUCTION PHONE PASS**. Cloudflare screenshot shows Main production ready, including promotion and subsequent docs builds. Universe B is now the accepted production Reader. Universe A backup `backup-universe-A-pre-six-second-promotion-2026-10-15` retained. No additional Reader or NoBo changes.

# Universe B Reader production promotion — 15 October 2026

Status: GitHub Main MERGED; Cloudflare live deployment and actual-phone smoke test PENDING confirmation.

Approved by Stanley after Jeeves actual-phone PASS on the delayed 6-second reveal, page-slide, rapid flick stability and boundary bounce.

## State
- Production promotion: PR #8 merged, commit `31241a6cf343a7b7340910cb128f2bc1c75aa14d`.
- Preserved Universe A snapshot: branch `backup-universe-A-pre-six-second-promotion-2026-10-15` (created from pre-merge Main). Verified Reader blob `033c341cbda93c9cec8c7c59aa4f848fd5fe9c4f`.
- Experimental B source head: `fc8b63dc215ec1dede691b7f73e9254844d9efdb`.
- Promotion changed only three mirrored Reader HTML files: `index.html`, `public/index.html`, `public/project_library/books/browse/index.html`. GitHub Main read-back confirmed identical copies and delayed slide Reader code.
- No changes to NoBo, Worker source, corpus, or Pre-Page.
- Reader B: ARM stores word, Watcher starts on first actual page flick, restarts on navigation, 6-second stable dwell inserts top airlock and commits PAID, independent smooth 210ms page slide and 18px elastic no-go bounce at first-page backwards boundary.
- Jeeves actual-phone QA PASSED. Other 17 books have the extended logic but do not have individual phone acceptance. Production end-to-end smoke QA not yet complete.

## Remaining critical acceptance
1. Verify Cloudflare successful deploy sourced from Main merge `31241a6c` (do not infer from GitHub merge).
2. On phone, normal NoBo RESET → SHW → fresh ARM; open `ebooks.fyi` → Pre-Page hotspot → live disguised GUTS Reader.
3. Open book Ch 1 P1, wait >6 seconds without flick — no word. Flick once, wait 6 seconds — word appears, PAID persists; other pages clean. Test rapid flick, HIDD/RESET as appropriate.
4. If regression, restore Universe A from the named snapshot, not from an old ad hoc commit.
