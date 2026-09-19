# GUTS CLOUDFLARE BRIDGE v0.1

Status: canonical transport contract for the current single-performer GUTS build.

## Doctrine

**H2 PUSHES — GUT PULLS.**

H2G2 remains the covert performer input. Per-performance HTML is never rewritten, uploaded, rebuilt, or redeployed.

Flow:

```
P phone / H2G2
      |
      | PUSH { phase, word, revision }
      v
Cloudflare tiny shared state
      ^
      | PULL
      |
Sp phone / GUTS
```

Cloudflare = **HOST WEBSITE + REMEMBER WORD**.

## Runtime state

For Stanley's present single-performer implementation, one mutable record is sufficient:

```json
{
  "phase": "READY",
  "word": "",
  "revision": 0,
  "updatedAt": 0
}
```

Allowed remote phases initially: `READY`, `ARMED`, `CLEAN`.

`PAID`, the paid page key, dwell qualification, selected chapter, and reader navigation remain **local to the spectator browser**. They are performance-engine state, not transport state.

## Endpoints

### GET /api/state

GUTS pulls the current tiny record.

Response must be JSON, `Cache-Control: no-store`, same-origin in production.

### POST /api/state

H2 pushes a complete new record. Payload:

```json
{ "phase": "ARMED", "word": "GOPHERS" }
```

or:

```json
{ "phase": "CLEAN", "word": "" }
```

or RESET:

```json
{ "phase": "READY", "word": "" }
```

The Worker increments `revision` and stamps `updatedAt`.

POST must require a performer secret/authentication mechanism. The secret must never be shipped in spectator JavaScript.

## GUTS pull rule

On entry/load, GUTS calls `GET /api/state`.

- Remote `ARMED` + non-empty word: initialise local engine as `ARMED` with that word.
- Remote `READY`: initialise/retain pristine READY only when there is no active local performance.
- Remote `CLEAN`: clean force material locally.
- Once local GUTS has reached `PAID`, an unchanged remote ARMED record must **not** re-arm or destroy the paid-page state.

Use `revision` to make applying remote state idempotent.

Initial implementation can pull once on page load because choreography is **arm first → spectator enters second**. Polling is not required for v0.1.

## What does NOT happen

- no HTML mutation on the server per performance
- no GitHub commit/deploy per force
- no propagation wait
- no force word in spectator URL
- no Inject-style visitor claiming/pairing in Stanley v0.1
- no remote storage of chapter/page/dwell/paid-page details
- no Cloudflare commercial multi-performer/session architecture yet

## Existing engine boundary

Current `index.html` v0.22-opener-fix already owns:

READY → ARMED → PAID → CLEAN

six-second dwell, protected selected chapter opener, payoff persistence, cleanup, RESET, and `$$$` injection.

The bridge must feed that engine; it must not replace or reopen it.

## Development seam

Until the Cloudflare Worker exists, the visible TEST/admin control remains the local transport simulator. Cloudflare integration should be introduced behind small functions such as:

```js
async function pullRemoteState() { /* GET /api/state */ }
async function pushRemoteState(next) { /* H2 side only */ }
```

Do not entangle network transport with page visibility/dwell/payoff logic.

## Deferred commercial problem

A commercial multi-performer product will require independent performer/session isolation and authentication. That is deliberately outside this single-performer bridge and must not be solved by adopting Inject's Auto Pair architecture.
