# GUTS — 10 October 2026 — production phone PASS and handover

Production Reader merge PR #7: 837a0ce. Main before documentation: a2d9d5b. Preserved exact production snapshot in branch backup-production-phone-pass-2026-10-10 at a2d9d5b. Existing pre-promotion rollback backup-pre-top-airlock-promotion-2026-10-10 at 06086d6 remains protected.

Cloudflare dashboard showed deployment a16602c9 Active/Ready at 100% traffic; PR #7 deployment b46625ab Ready. These are Cloudflare IDs, not Git commits. User's iPhone independently confirmed production Reader behavior.

Initial direct Reader URL tests lacked $$$ and seemed OLD because they did not include ?browse=1. Correct production URL https://www3.library.gutenbrg.com/project_library/books/browse/?browse=1 revealed $$$ in first paragraph: PHONE PASS.

Normal performance: home-screen NoBo, H2G2 ARM GOPHERS, spectator enters ebooks.fyi, chooses book/chapter/page; GOPHERS substituted correctly. Six-second dwell and PAID persistence PASS. NoBo RESET did NOT change still-open Reader screen without refresh; after refresh to library and returning to Jean Brodie, GOPHERS absent: PASS. No claim of instant synchronization.

Machine QA 38043537147 passed 18 books/4,858 prepared pages; only selected paths received actual phone acceptance. Production Reader and corpus FROZEN. No speculative code, Worker, cache, or KV modifications. Monday ASM performer rehearsal next.

## Welcome to the new Kryten
Read GUTS_WORKFLOW_CONSTITUTION.md, OPERATIONS_START_HERE.md, GUTS_CURRENT_STATE.md, docs/CURRENT_STATE.md, this checkpoint, and docs/checkpoints/2026-10-10_top-airlock-production-promotion-handover.md. Current live Reader is confirmed, backup at a2d9d5b, old rollback 06086d6. Never mistake direct URL without ?browse=1 for BR+ test. Normal spectator performance uses home-screen NoBo H2G2 ARM and ebooks.fyi without experimental URLs. Frozen working system. Read broadly, act narrowly. Design STANdard: less machinery, not more.

Git Main archaeology queried 10 October: GUTS 498 reachable commits (from 18 September), NoBo 147 (from 27 August), each a recoverable tracked-files snapshot, not a separate physical complete backup. Git contains committed book JSON, Reader and committed assets, not external KV, secrets, or browser state.

My Job: preserve working system and help rehearse Monday's presentation.
Your Job: perform the normal NoBo routine; no additional technical action needed.
