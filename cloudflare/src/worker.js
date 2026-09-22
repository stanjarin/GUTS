const STATE_KEY = "current";
const MODE_KEY = "site-mode";

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

export default {
  async fetch(request,env){
    const url=new URL(request.url);

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

    // PIN 1: performer ARM/CLEAN. PIN is supplied at runtime, never shipped in public source.
    if(url.pathname==="/api/performer/state"){
      if(request.method!=="POST") return new Response("Method not allowed",{status:405});
      let body; try{body=await request.json()}catch{return json({error:"invalid_json"},400)}
      if(!pinOK(body?.pin,env.GUTS_ARM_PIN)) return json({error:"unauthorized"},401);
      const phase=String(body?.phase||"").toUpperCase();
      if(!["ARMED","CLEAN"].includes(phase)) return json({error:"invalid_phase"},400);
      const word=phase==="ARMED"?String(body?.word||"").trim():"";
      if(phase==="ARMED"&&!word) return json({error:"armed_requires_word"},400);
      if(word.length>120) return json({error:"word_too_long"},400);
      return json(await writeState(env,phase,word));
    }

    // PIN 2: switch spectator visibility. REHEARSAL authorises this browser via HttpOnly cookie.
    if(url.pathname==="/api/performer/mode"){
      if(request.method==="GET") return json({mode:await readMode(env)});
      if(request.method!=="POST") return new Response("Method not allowed",{status:405});
      let body; try{body=await request.json()}catch{return json({error:"invalid_json"},400)}
      if(!pinOK(body?.pin,env.GUTS_SITE_PIN)) return json({error:"unauthorized"},401);
      const mode=String(body?.mode||"").toUpperCase();
      if(!["REHEARSAL","SHOW"].includes(mode)) return json({error:"invalid_mode"},400);
      await env.GUTS_STATE.put(MODE_KEY,mode);
      let state=await readState(env);
      if(mode==="REHEARSAL") state=await writeState(env,"CLEAN","");
      const headers={};
      if(mode==="REHEARSAL") headers["set-cookie"]="guts_rehearsal=1; Path=/; Max-Age=2592000; Secure; HttpOnly; SameSite=Strict";
      return json({mode,state},200,headers);
    }

    // In REHEARSAL only the browser authorised by PIN 2 can see static GUTS.
    const mode=await readMode(env);
    if(mode==="REHEARSAL" && cookie(request,"guts_rehearsal")!=="1") return new Response("404 Not Found",{status:404,headers:{"cache-control":"no-store"}});
    return env.ASSETS ? env.ASSETS.fetch(request) : new Response("Not found",{status:404});
  }
};