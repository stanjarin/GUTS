# GUTS — NEXT EWE BRIEF
## 22 September 2026 — corrected authoritative resume point

**Do not follow the older README section saying literal `$$$` is a GUTS bug. That diagnosis was wrong-app archaeology and is superseded by the correction appended to README.**

## VERIFIED CURRENT STATE

Production is live at `https://gutenbrg.com`. Single-user production bridge is now **END-TO-END PASSED**:

**NoBo H2 → authenticated Cloudflare ARM push → KV → GUTS spectator pull → GOPHERS displayed correctly.**

Stanley personally tested the full chain. There was no PIN prompt at the covert submit and GUTS showed GOPHERS correctly, not `$$$`.

## What the $$$ incident actually was

Stanley had been looking at **NoBo performer pages**, not the GUTS spectator reader. NoBo's persistent BROWSE mode deliberately returned raw `force_paragraphs`, exposing the `$$$` socket.

NoBo repairs:
- `6dbd25797e121d58b0414cd963f0c9b5225d9671` — ARM automatically exits BROWSE mode.
- `c52447a4ac11fe46f9a3fb149381c078f37ae966` — guarded/local H2 result binding fixes the subsequent iOS “Image unavailable” failure.
- `0731e17ce939ababebe9b1e4480504a89cb073c2` — hidden MORE panel now has **ARM AUTH ON/OFF** de-authorisation control.

PIN1 preactivation persists in NoBo localStorage. **ARM AUTH ON** has been visibly confirmed by Stanley. OFF removes `guts-arm-pin`; next H2 SEARCH requests and verifies PIN1 again.

## Wrong-tram GUTS debris

Do not describe these as fixes for the NoBo symptom:
- `a7d984846dbd4ee667085b93caa8a5cc47214bec` added a GUTS unresolved-socket runtime diagnostic. It can now be removed as cleanup.
- `2fe079b83a1e893e0715cd03375bdad73303dfb2` explicitly bound `ASSETS` in Wrangler. It is compatible with `env.ASSETS.fetch()`, but was non-causal to the reported `$$$` issue.

## Facts not to reopen

- Nine books / 5,435 pages passed socket QA.
- H2 PUSHES — GUT PULLS.
- Chapter opener protection remains visual + dwell.
- Single-user path is current priority; multi-performer is PARKED.
- Never restore unauthenticated write routes.
- PIN variables/secrets remain out of repo; `keep_vars = true` is already deployed.
- NoBo H2 UI is reused, not redesigned.
- Cloudflare is production host/state; GitHub Pages is development.

## NEXT WORK — LEAVE NO TRACE

Stanley's Shed principle: **Leave it as you found it / Leave No Trace.** Before GUTS, real Gutenberg is there; during the effect GUTS temporarily bends the environment; afterward ordinary spectator discovery should return to real Gutenberg.

Implement carefully:
- In **REHEARSAL/outside SHOW**, an ordinary outsider visiting/revisiting `gutenbrg.com` should quietly end up at the **real Project Gutenberg**, rather than a revealing 404.
- Short-URL/history revisits outside SHOW should likewise lead into real Gutenberg behavior.
- In **SHOW**, GUTS operates normally.
- Preserve authorised performer/development access where needed and avoid redirect loops.
- Practical PIN2 SHOW/REHEARSAL control remains to finish.

## Workflow

Stanley = user; Kryten = assistant. Be concise and exact. Do the work when Stanley says “go.” Never use `!H` or `007`; Stanley owns those. Never Arial; visual doctrine is Helvetica. Do not touch signed-off corpus/mechanics without evidence. Do not expose secret values. Do not call Resources “fake.” Carousel.png is canonical.

## Immediate next action

**KRYTEN:** clean up the obsolete GUTS diagnostic if appropriate, then implement/test LEAVE NO TRACE REHEARSAL→real Project Gutenberg camouflage and finish the practical PIN2 display control without disturbing the now-proven bridge.
