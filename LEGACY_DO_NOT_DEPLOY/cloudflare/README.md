# GUTS Cloudflare backend

Deploy-ready backend for the single-performer GUTS transport.

## Contract

- `GET /api/state` is public and returns the tiny current state record with `Cache-Control: no-store`.
- `POST /api/state` requires `Authorization: Bearer <GUTS_PUSH_SECRET>`.
- Allowed pushed phases: `READY`, `ARMED`, `CLEAN`.
- `ARMED` requires a non-empty `word`.
- The Worker owns `revision` and `updatedAt`; callers do not.
- State is stored at one KV key, `current`.
- PAID, selected page/chapter, dwell and navigation are never stored remotely.

Example state:

```json
{"phase":"ARMED","word":"GOPHERS","revision":17,"updatedAt":1789876800000}
```

## Cloudflare setup later

1. Create a Cloudflare account and put `gutenbrg.com` on Cloudflare.
2. Create a Workers KV namespace and bind it to the Worker as `GUTS_STATE`.
3. Replace the placeholder namespace ID in `wrangler.toml`.
4. Create the encrypted Worker secret `GUTS_PUSH_SECRET`.
5. Deploy the Worker/site so `/api/state` is same-origin with the spectator GUTS site.
6. Test GET, authenticated POST, revision increment, ARMED pull, PAID protection and CLEAN.

No secret belongs in GitHub or spectator JavaScript.
