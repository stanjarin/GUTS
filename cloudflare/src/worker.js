const STATE_KEY = "current";

function json(data, status=200){
  return new Response(JSON.stringify(data),{
    status,
    headers:{"content-type":"application/json; charset=utf-8","cache-control":"no-store"}
  });
}
async function readState(env){
  const saved=await env.GUTS_STATE.get(STATE_KEY,"json");
  return saved || {phase:"READY",word:"",revision:0,updatedAt:0};
}
export default {
  async fetch(request,env){
    const url=new URL(request.url);
    if(url.pathname!=="/api/state") return env.ASSETS ? env.ASSETS.fetch(request) : new Response("Not found",{status:404});
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
    const current=await readState(env);
    const next={phase,word,revision:Number(current.revision||0)+1,updatedAt:Date.now()};
    await env.GUTS_STATE.put(STATE_KEY,JSON.stringify(next));
    return json(next);
  }
};