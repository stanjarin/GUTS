# GUTS CLOUDFLARE BRIDGE v0.2 — SESSION ARCHITECTURE

Status: canonical transport contract. Supersedes the single-global-state assumption in v0.1.

## Doctrine

**H2 PUSHES — GUT PULLS.**

Cloudflare = **HOST WEBSITE + REMEMBER SESSION STATE**.

Multiple performers may operate simultaneously. No performer may overwrite another performer's force word.

## Session isolation

Each performance uses an opaque random session ID, for example:

```
8f2d7c6a4b...
```

KV keys are namespaced:

```
session:<opaque-id>
```

Each record remains microscopic:

```json
{
  "phase": "READY",
  "word": "",
  "revision": 0,
  "updatedAt": 0
}
```

Remote phases: READY / ARMED / CLEAN.

PAID, paid-page key, dwell, selected chapter and reader navigation remain local to the spectator browser.

## Pairing rule

The spectator must never type or see a session number.

The public gateway associates the arriving spectator browser with the correct opaque session and stores that association in an HttpOnly cookie. Subsequent GUTS state pulls use the cookie; the force word and session ID do not appear in visible book URLs.

The handoff is carried by the existing short-link gateway choreography, not by a visible pairing step.

### Short-link slot handoff

In SHOW mode the performer claims a short-lived **arrival slot** for an isolated session immediately before inviting Sp to type the existing public shortcut. The public Resources gateway consumes the next valid arrival slot and binds that browser to the session with an HttpOnly cookie. The browser then continues through the ordinary Resources page and clean book URL.

The spectator therefore still types only the familiar short URL. No session number, performer ID, PIN, force word, QR code or pairing screen is shown.

The arrival slot must:
- contain only an opaque session ID
- expire quickly
- be consumed once
- never contain the force word
- fail closed if no valid slot exists
- be suitable for a later multi-performer allocation scheme rather than a single global "next visitor" assumption.

For Stanley's first production proof, do **not** silently implement a global next-arrival slot: that would reintroduce the exact simultaneous-performer collision v0.2 is intended to remove. The allocator must have a deterministic discriminator before multi-performer is declared complete.

## Performer authentication

PIN 1 authenticates ARM/CLEAN operations. The PIN itself is a Cloudflare encrypted secret and is never committed to GitHub.

A successful performer request acts only on the supplied opaque session ID.

PIN 2 controls site mode: REHEARSAL / SHOW.

## Site modes

REHEARSAL: only a browser authorised by PIN 2 may see spectator static assets; others receive 404.

SHOW: spectator gateway is public.

SHOW -> REHEARSAL also CLEANs active session state.

## Compatibility

The current production single-session endpoints remain untouched until the session handoff is implemented and tested. Today's proven GUTS production path therefore continues to work while v0.2 is built alongside it.

## Migration sequence

1. Define isolated session records and opaque IDs.
2. Add session-aware performer endpoints.
3. Add invisible spectator-session handoff.
4. Teach GUTS pull to use its bound session.
5. Test two simultaneous sessions with different words.
6. Only then retire the legacy global state path.

## Non-negotiables

- no force word in spectator URL
- no PIN or master secret in public JavaScript
- no per-performance GitHub deploy
- no global force record in final multi-performer architecture
- no reopening the signed-off local READY -> ARMED -> PAID -> CLEAN engine
