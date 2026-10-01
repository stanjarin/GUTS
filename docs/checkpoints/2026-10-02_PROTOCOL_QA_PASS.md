# GUTS CHECKPOINT — 2026-10-02 — PROTOCOL QA PASS

## State
- GUTS branch: `protocol-cleanup-2026-10-01`
- NoBo branch: `controls-refresh-2026-10-01`
- GUTS main untouched at `aef68707b1ad031eab16ae1efbecce5733630186`
- NoBo main untouched at `93d4ade5fee65d9931c5c6ad1b1b25cad8c18235`

## Phone QA PASS
- [WORD] across books: PASS
- HIDD ↔ SHW preserves [WORD]: PASS
- refresh/new request preserves [WORD]: PASS
- 6+ second dwell and departure → PAID: PASS
- PAID persistence: PASS
- RSET/READY clears [WORD]: PASS

## Canonical protocol
- remote magic: READY / ARMED only
- local execution: PAID
- visibility: SHW / HIDD, independent
- auth: non-mutating validation
- CLEAN removed from live NoBo↔GUTS path

## Next
Promotion only: freeze rollback points, promote both tested branches, repoint NoBo to production GUTS, verify `ebooks.fyi`, final smoke test.
