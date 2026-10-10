# 10 Oct 2026 — Real NoBo → top-airlock GUTS handoff boundary

## Verified read-only
- Approved experimental Reader frozen at `1ae4abe1e1f3ce83c996d932fa5bdcbb8fc95601`.
- Source `wrangler.jsonc` Main deploys Worker name `guts`, static assets `public/`, KV binding `GUTS_STATE` namespace ID `85ae7131c91e492abb79aca57d6817a6`.
- Current Worker `src/worker.js` supports existing `GET /api/state`, authenticated `POST /api/state`, and existing performer/session/alias endpoints; no new protocol is needed.
- NoBo Main targets `https://ebooks.fyi`; current performance path reaches same live GUTS Worker via `www3.library.gutenbrg.com`.
- Experimental preview at `https://stanjarin.github.io/GUTS/top-airlock/?browse=1` is **static** and deliberately uses `<base href="/GUTS/top-airlock/">`. Reader calls absolute `/api/state`, which there would resolve to GitHub Pages, not Cloudflare, in genuine non-browse mode.
- Existing browser simulation of READY → ARMED → six-second dwell → PAID → READY passed at GitHub Actions `38041746845`. This is not a cross-service verification.
- GitHub repository has Cloudflare auto-deploy integration for Main, but available current tools do not expose the Cloudflare account, create an isolated Worker, bind isolated KV or invoke NoBo's actual app on a phone.

## Minimal isolated integration
1. Create a **separate temporary Cloudflare Worker**, not an alias of production `guts`, with a **distinct KV namespace**, using the existing Worker and frozen Reader (Reader base path adapted from GitHub Pages to root). Preserve production secrets; use isolated rehearsal credentials.
2. Make its URL available, then test the Worker+Reader `GET/POST /api/state` against that separate namespace.
3. For a genuine NoBo-to-preview phone rehearsal, route a **temporary NoBo test copy** to the temporary Worker URL; preserve NoBo Main and production endpoint.
4. On actual phone test RSET → READY → ARM named word → pick book/chapter → stop on opener/normal page → six-second dwell → PAID → reset. Revert/retire test infrastructure after success.
5. **Do not** point a GitHub Pages page at production `/api/state`, reuse production KV, or deploy to `main` before approval.

## Status
- Integration path determined.
- No production source, NoBo, Cloudflare deployment, KV or domains changed.
- Real live preview Worker **not yet created** because Cloudflare deployment/account tooling or authorisation for separate Worker/KV is not currently accessible here.
- Next operator/user action: provision a distinct Cloudflare preview Worker and KV or connect a deployment integration that can; keep production `guts` intact.
