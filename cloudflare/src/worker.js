const STATE_KEY = "current";
const MODE_KEY = "site-mode";
const SESSION_COOKIE = "guts_session";

function json(data,status=200,extra={}){
  return new Response(JSON.stringify(data),{status,headers:{"content-type":"application/json; charset=utf-8","cache-control":"no-store",...extra}});
}
function cookie(request,name){
  const raw=request.headers.get("cookie")||"";
  for(const bit of raw.split(";")){
    const [k,...v]=bit.trim().split("=");
    if(k===name)return decodeURIComponent(v.join("="));
  }
  return "";
}
async function readState(env){
  const saved=await env.GUTS_STATE.get(STATE_KEY,"json");
  return saved || {phase:"READY",word:"",revision:0,updatedAt:0};
}
async function writeState(env,phase,word=""){
  const current=await readState(env);
  const next={phase,word,revision:Number(current.revision||0)+1,updatedAt:Date.now()};
  await env.GUTS_STATE.put(STATE_KEY,JSON.stringify(next));
  return next;
}
async function readMode(env){
  return (await env.GUTS_STATE.get(MODE_KEY)) || "SHOW";
}
function pinOK(got,want){ return !!want && String(got||"")===String(want); }
function sessionKey(id){ return `session:${id}`; }
function aliasKey(alias){ return `alias:${alias}`; }
function validAlias(alias){ return /^[a-z0-9-]{3,48}$/.test(String(alias||"")); }
function validSession(id){ return /^[A-Za-z0-9_-]{16,96}$/.test(String(id||"")); }
async function readSession(env,id){
  const saved=await env.GUTS_STATE.get(sessionKey(id),"json");
  return saved || {phase:"READY",word:"",revision:0,updatedAt:0};
}
async function writeSession(env,id,phase,word=""){
  const current=await readSession(env,id);
  const next={phase,word,revision:Number(current.revision||0)+1,updatedAt:Date.now()};
  await env.GUTS_STATE.put(sessionKey(id),JSON.stringify(next),{expirationTtl:86400});
  return next;
}

export default {
  async fetch(request,env){
    const url=new URL(request.url);

    // v0.2 isolated-session transport. Built alongside the proven legacy path.
    // Permanent performer alias -> current isolated performance session.
    // "shortcuts" is Stanley/P1. "test-p2" is temporary QA/P2.
    if(url.pathname==="/api/alias/bootstrap"){
      if(request.method!=="POST") return new Response("Method not allowed",{status:405});
      let body; try{body=await request.json()}catch{return json({error:"invalid_json"},400)}
      if(!pinOK(body?.pin,env.GUTS_ARM_PIN)) return json({error:"unauthorized"},401);
      const alias=String(body?.alias||"").toLowerCase();
      if(!validAlias(alias) || !["shortcuts","test-p2"].includes(alias)) return json({error:"invalid_alias"},400);
      let id=await env.GUTS_STATE.get(aliasKey(alias));
      if(!validSession(id)){
        id=crypto.randomUUID().replaceAll("-","");
        await writeSession(env,id,"READY","");
        await env.GUTS_STATE.put(aliasKey(alias),id);
      }
      return json({alias,session:id,state:await readSession(env,id)});
    }
    if(url.pathname==="/api/alias/state"){
      if(request.method!=="POST") return new Response("Method not allowed",{status:405});
      let body; try{body=await request.json()}catch{return json({error:"invalid_json"},400)}
      if(!pinOK(body?.pin,env.GUTS_ARM_PIN)) return json({error:"unauthorized"},401);
      const alias=String(body?.alias||"").toLowerCase();
      const id=await env.GUTS_STATE.get(aliasKey(alias));
      if(!validSession(id)) return json({error:"unknown_alias"},404);
      const phase=String(body?.phase||"").toUpperCase();
      if(!["ARMED","CLEAN"].includes(phase)) return json({error:"invalid_phase"},400);
      const word=phase==="ARMED"?String(body?.word||"").trim():"";
      if(phase==="ARMED"&&!word) return json({error:"armed_requires_word"},400);
      if(word.length>120) return json({error:"word_too_long"},400);
      return json({alias,state:await writeSession(env,id,phase,word)});
    }
    if(url.pathname.startsWith("/entry/")){
      const alias=url.pathname.slice(7).replace(/\/$/,"").toLowerCase();
      if(!validAlias(alias)) return new Response("404 Not Found",{status:404});
      const id=await env.GUTS_STATE.get(aliasKey(alias));
      if(!validSession(id)) return new Response("404 Not Found",{status:404});
      return new Response(null,{status:302,headers:{
        "location":"/project_library/books/browse/",
        "set-cookie":`${SESSION_COOKIE}=${encodeURIComponent(id)}; Path=/; Max-Age=86400; Secure; HttpOnly; SameSite=Lax`,
        "cache-control":"no-store"
      }});
    }

    if(url.pathname==="/api/session/create"){
      if(request.method!=="POST") return new Response("Method not allowed",{status:405});
      let body; try{body=await request.json()}catch{return json({error:"invalid_json"},400)}
      if(!pinOK(body?.pin,env.GUTS_ARM_PIN)) return json({error:"unauthorized"},401);
      const id=crypto.randomUUID().replaceAll("-","");
      const state=await writeSession(env,id,"READY","");
      return json({session:id,state});
    }
    if(url.pathname==="/api/session/state"){
      const id=cookie(request,SESSION_COOKIE);
      if(!validSession(id)) return json({error:"no_session"},404);
      if(request.method!=="GET") return new Response("Method not allowed",{status:405});
      return json(await readSession(env,id));
    }
    if(url.pathname==="/api/performer/session"){
      if(request.method!=="POST") return new Response("Method not allowed",{status:405});
      let body; try{body=await request.json()}catch{return json({error:"invalid_json"},400)}
      if(!pinOK(body?.pin,env.GUTS_ARM_PIN)) return json({error:"unauthorized"},401);
      const id=String(body?.session||"");
      if(!validSession(id)) return json({error:"invalid_session"},400);
      const phase=String(body?.phase||"").toUpperCase();
      if(!["ARMED","CLEAN"].includes(phase)) return json({error:"invalid_phase"},400);
      const word=phase==="ARMED"?String(body?.word||"").trim():"";
      if(phase==="ARMED"&&!word) return json({error:"armed_requires_word"},400);
      if(word.length>120) return json({error:"word_too_long"},400);
      return json(await writeSession(env,id,phase,word));
    }
    // Invisible spectator handoff: opaque ticket is consumed once, then removed from the visible URL.
    if(url.pathname==="/api/join"){
      const ticket=String(url.searchParams.get("t")||"");
      if(!validSession(ticket)) return new Response("404 Not Found",{status:404});
      const existing=await env.GUTS_STATE.get(sessionKey(ticket));
      if(!existing) return new Response("404 Not Found",{status:404});
      const clean="/project_library/books/browse/";
      return new Response(null,{status:302,headers:{
        "location":clean,
        "set-cookie":`${SESSION_COOKIE}=${encodeURIComponent(ticket)}; Path=/; Max-Age=86400; Secure; HttpOnly; SameSite=Lax`,
        "cache-control":"no-store"
      }});
    }

    // Existing public state pull + master-secret maintenance POST.
    if(url.pathname==="/api/state"){
      if(request.method==="GET") return json(await readState(env));
      if(request.method!=="POST") return new Response("Method not allowed",{status:405,headers:{"allow":"GET, POST"}});
      const auth=request.headers.get("authorization")||"";
      if(!env.GUTS_PUSH_SECRET || auth!==`Bearer ${env.GUTS_PUSH_SECRET}`) return json({error:"unauthorized"},401);
      let body; try{body=await request.json()}catch{return json({error:"invalid_json"},400)}
      const phase=String(body?.phase||"").toUpperCase();
      if(!["READY","ARMED","CLEAN"].includes(phase)) return json({error:"invalid_phase"},400);
      const word=phase==="ARMED"?String(body?.word||"").trim():"";
      if(phase==="ARMED"&&!word) return json({error:"armed_requires_word"},400);
      if(word.length>120) return json({error:"word_too_long"},400);
      return json(await writeState(env,phase,word));
    }

    // PIN 1: performer ARM/CLEAN. Allow only the NoBo GitHub Pages performer UI cross-origin.
    if(url.pathname==="/api/performer/state"){
      const origin=request.headers.get("origin")||"";
      const allowedOrigin="https://stanjarin.github.io";
      const cors=origin===allowedOrigin?{
        "access-control-allow-origin":allowedOrigin,
        "access-control-allow-methods":"POST, OPTIONS",
        "access-control-allow-headers":"content-type",
        "vary":"Origin"
      }:{};
      if(request.method==="OPTIONS"){
        if(origin!==allowedOrigin) return new Response(null,{status:403});
        return new Response(null,{status:204,headers:cors});
      }
      if(request.method!=="POST") return new Response("Method not allowed",{status:405,headers:cors});
      let body; try{body=await request.json()}catch{return json({error:"invalid_json"},400,cors)}
      if(!pinOK(body?.pin,env.GUTS_ARM_PIN)) return json({error:"unauthorized"},401,cors);
      const phase=String(body?.phase||"").toUpperCase();
      if(!["ARMED","CLEAN"].includes(phase)) return json({error:"invalid_phase"},400,cors);
      const word=phase==="ARMED"?String(body?.word||"").trim():"";
      if(phase==="ARMED"&&!word) return json({error:"armed_requires_word"},400,cors);
      if(word.length>120) return json({error:"word_too_long"},400,cors);
      return json(await writeState(env,phase,word),200,cors);
    }

    // PIN 2: switch spectator visibility. REHEARSAL authorises this browser via HttpOnly cookie.
    if(url.pathname==="/api/performer/mode"){
      const origin=request.headers.get("origin")||"";
      const allowedOrigin="https://stanjarin.github.io";
      const cors=origin===allowedOrigin?{
        "access-control-allow-origin":allowedOrigin,
        "access-control-allow-methods":"GET, POST, OPTIONS",
        "access-control-allow-headers":"content-type",
        "access-control-allow-credentials":"true",
        "vary":"Origin"
      }:{};
      if(request.method==="OPTIONS"){
        if(origin!==allowedOrigin) return new Response(null,{status:403});
        return new Response(null,{status:204,headers:cors});
      }
      if(request.method==="GET") return json({mode:await readMode(env)},200,cors);
      if(request.method!=="POST") return new Response("Method not allowed",{status:405,headers:cors});
      let body; try{body=await request.json()}catch{return json({error:"invalid_json"},400,cors)}
      if(!pinOK(body?.pin,env.GUTS_SITE_PIN)) return json({error:"unauthorized"},401,cors);
      const mode=String(body?.mode||"").toUpperCase();
      if(!["REHEARSAL","SHOW"].includes(mode)) return json({error:"invalid_mode"},400,cors);
      await env.GUTS_STATE.put(MODE_KEY,mode);
      let state=await readState(env);
      if(mode==="REHEARSAL") state=await writeState(env,"CLEAN","");
      const headers={...cors};
      if(mode==="REHEARSAL") headers["set-cookie"]="guts_rehearsal=1; Path=/; Max-Age=2592000; Secure; HttpOnly; SameSite=None";
      else headers["set-cookie"]="guts_rehearsal=; Path=/; Max-Age=0; Secure; HttpOnly; SameSite=None";
      return json({mode,state},200,headers);
    }

    // In REHEARSAL only the browser authorised by PIN 2 can see static GUTS.
    const mode=await readMode(env);
    // Rehearsal authorisation belongs only to the performer browser. A stale cookie
    // must not let a former spectator/development browser survive SHOW -> REHEARSAL.\n    const rehearsalAuthorised=cookie(request,"guts_rehearsal")==="1";
      if(mode==="REHEARSAL" && !rehearsalAuthorised) {
      // LEAVE NO TRACE: to an ordinary outsider/revisiting spectator, Gutenbrg has vanished.
      // Preserve path/search where practical so a history revisit lands in the real Gutenberg world.
      const real=new URL("https://www.gutenberg.org/");
      if(url.pathname!=="/") real.pathname=url.pathname;
      real.search=url.search;
      return new Response(null,{status:302,headers:{"location":real.toString(),"cache-control":"no-store"}});
    }
    return env.ASSETS ? env.ASSETS.fetch(request) : new Response("Not found",{status:404});
  }
};