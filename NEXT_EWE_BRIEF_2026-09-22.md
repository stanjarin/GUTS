# GUTS — NEXT EWE BRIEF
## 22 September 2026 — start here, do not archaeology first

Read `README.md`, especially **CONTINUATION CHECKPOINT — 22 September 2026 (authoritative handover)**. It contains the full production/security/H2/session/camouflage state and commit trail.

## Exact current problem

Stanley has just successfully passed the new NoBo H2 **ARM PIN** preactivation on his phone. That proves the current NoBo bridge reaches the active Cloudflare Worker and the restored `GUTS_ARM_PIN` binding works.

But the spectator GUTS reader now displays literal **`$$$`** in force paragraphs instead of the selected force word.

The original injection:
`magic.force ? s.replaceAll("$$$", magic.force) : s`

was changed to:
`magic.force ? String(s).split("$$$").join(magic.force) : s`

in commit `5438466909372d5c597f1850909cb7b71d810e37`.

**Stanley retested: still literal $$$**.

Therefore do NOT repeat that fix and do NOT edit the corpus. The corpus is mechanically good and previously produced a successful real-phone GOPHERS payoff.

Next job: obtain runtime evidence for `magic.phase`, `magic.force`, remote state/revision, `forceHere`, and the actual paragraph string at render time. Determine where the word is being lost/cleared or whether the wrong state/render instance is involved. Fix only what the evidence identifies.

## Facts not to reopen

- Production: `https://gutenbrg.com`
- Worker + static assets + KV on same Cloudflare deployment.
- Nine books / 5,435 pages, socket QA passed.
- Chapter opener protection is two safeguards: visual + dwell.
- H2 PUSHES — GUT PULLS.
- Single-user production path is current priority.
- Multi-performer work exists but is PARKED.
- Unsafe unauthenticated write route was removed; never restore it.
- Zero Trust path parked after payment-method demand.
- NoBo H2 UI is reused; do not redesign it.
- PIN1 is preactivated before performance and persists in PWA localStorage; no PIN prompt at covert word submit.
- Current dashboard bindings: `GUTS_PUSH_SECRET`, `GUTS_ARM_PIN`, `GUTS_SITE_PIN`; values stay out of repo.
- `keep_vars = true` persistence fix is commit `ecaf19c57d96398b0686c5c21718cd3839b724d7`.
- PIN now works after that fix.

## Parked Shed improvement

After the $$$ bug is solved: in REHEARSAL, outsiders should no longer get 404. Quietly route them to the **real Project Gutenberg**. Revisits via the short URL/history should likewise have all Resources options go to real Gutenberg outside SHOW. In SHOW, our Gutenbrg experience operates normally. This is camouflage, not a new forcing mechanism.

## Style / workflow constraints

Stanley = user. Assistant = Kryten.
Do not use `!H` or `007`; Stanley owns those.
Be concise, exact, and do the work when Stanley says “go.”
When an action is pending, explicitly identify **NEXT ACTION — KRYTEN** or **NEXT ACTION — STANLEY**.
Do not claim checks that were not performed.
Do not use Arial; visual doctrine is Helvetica.
Do not touch signed-off mechanics/corpus without evidence.
Do not expose secret values.
Do not call the Resources gateway “fake.”
Do not reconstruct Carousel.png; it is canonical combined art.
When Stanley says “3058 out.” reply exactly:
Latitude 90° North out.
Have you STORED?

## Immediate next action

**KRYTEN:** debug literal `$$$` with runtime evidence, then make the smallest repair.
