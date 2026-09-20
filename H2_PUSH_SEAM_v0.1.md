# GUTS H2 PUSH SEAM v0.1

Status: design locked from the current NoBo NoFo H2G2 implementation. NoBo source remains untouched.

## Existing covert action

In NoBo NoFo `index.html`, H2G2's Search overlay captures the performer's covert word in `#secretSearch`.

On form submit, `submit()`:
1. trims the covert input;
2. rejects blank input and the camouflage word `improbability`;
3. calls `armMagic(w)`;
4. replaces the visible field with `improbability`;
5. blurs the keyboard;
6. shows the innocent search results.

That submit event is the correct GUTS transport seam. The performer handling need not change.

## GUTS change

For GUTS, replace the local-only arming action at that seam with a transport helper:

```js
async function pushRemoteState(phase, word=""){
  const r=await fetch("/api/state",{
    method:"POST",
    headers:{
      "content-type":"application/json",
      "authorization":"Bearer "+PERFORMER_SECRET
    },
    body:JSON.stringify({phase,word})
  });
  if(!r.ok) throw Error("push failed "+r.status);
  return r.json();
}
```

The H2 submit sequence becomes conceptually:

```js
const w=inp.value.trim();
if(!w || w.toLowerCase()==="improbability")return;
await pushRemoteState("ARMED",w);
inp.value="improbability";
inp.blur();
showResults();
```

Thus the visible H2G2 choreography remains the same. The network action occurs at the same instant that NoBo currently calls `armMagic(w)`.

## Security boundary

The production performer secret MUST NOT be embedded in the public spectator GUTS JavaScript.

Therefore H2 must ultimately be a performer-only surface, separate from the public spectator bundle, or use another authenticated performer-only route. The current NoBo public GitHub Pages build must NOT be modified to contain the Cloudflare secret.

For Stanley's single-performer v0.1, deployment can use a private performer H2 surface whose POST reaches the same Cloudflare Worker. Exact secret provisioning waits until the Cloudflare account is verified and the Worker exists.

## Cleanup/reset

The same helper supports:
- `pushRemoteState("CLEAN")`
- `pushRemoteState("READY")`

No PAID state is pushed. PAID remains spectator-local.

## Implementation rule

Do not alter NoBo's H2 visual/search choreography merely to add transport. Keep the seam narrow: covert submit -> authenticated POST -> existing innocent H2 result screen.

H2 PUSHES — GUT PULLS.
