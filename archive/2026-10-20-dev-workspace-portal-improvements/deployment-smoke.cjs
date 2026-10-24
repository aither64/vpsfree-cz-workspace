"use strict";
// Prepared read-only candidate. Never mounts the conversation controller.
const fs = require("node:fs"), path = require("node:path"), assert = require("node:assert/strict");
const {createHash} = require("node:crypto"), {execFileSync} = require("node:child_process");
const {chromium} = require("@playwright/test");
const required = name => {assert(process.env[name], `Set ${name}`); return process.env[name];};
const workspace = "/home/aither/workspace/ai/vpsfree.cz", slug = "2026-10-20-dev-workspace-portal-improvements";
for (const [key,value] of Object.entries({DEV_SESSION_SLUG:slug, DEV_SESSION_WORKSPACE:workspace}))
  assert(!process.env[key] || process.env[key] === value, `${key} mismatch`);
const mode = process.argv[2], snapshotFile = process.argv[3];
assert(["before","after"].includes(mode) && snapshotFile, "Use before|after SNAPSHOT.json");
const packageRoot = required("PORTAL_SMOKE_PACKAGE"), sourceRoot = required("PORTAL_SMOKE_SOURCE");
const expectedHead = required("PORTAL_SMOKE_HEAD"), authUser = required("PORTAL_SMOKE_AUTH_USER");
const selected = fs.realpathSync(path.join(process.env.HOME,".local/state/dev-workspaces/profile"));
assert.equal(selected, fs.realpathSync(packageRoot));
assert.equal(execFileSync("git",["-C",sourceRoot,"rev-parse","HEAD"],{encoding:"utf8"}).trim(), expectedHead);
assert.equal(execFileSync("git",["-C",sourceRoot,"status","--porcelain"],{encoding:"utf8"}).trim(), "");
const registry=JSON.parse(fs.readFileSync(path.join(process.env.HOME,".config/dev-workspaces/registry.json")));
const binding=registry.workspaces.find(row=>row.root===workspace); assert(binding);
const baseURL="https://"+binding.hostname, sessionPath="/"+slug+"/";
const manifest=fs.readFileSync(path.join(workspace,"work",slug,"portal.yml"),"utf8");
const rootThread=/^  thread_id: ([^\s]+)$/m.exec(manifest)?.[1]; assert(rootThread);
const digest = data => createHash("sha256").update(data).digest("hex");
const canonical = value => Array.isArray(value) ? value.map(canonical) : value && typeof value==="object" ? Object.fromEntries(Object.keys(value).sort().map(k=>[k,canonical(value[k])])) : value;
(async()=>{
  // Certificate trust is checked separately by CA-verified curl in the plan.
  const browser=await chromium.launch({headless:true,channel:"chromium"});
  try {
    const configuredPasswordFile="/var/lib/dev-workspaces/password/password";
    const passwordFile=process.env.PORTAL_SMOKE_PASSWORD_FILE || configuredPasswordFile;
    const readMode=process.env.PORTAL_SMOKE_PASSWORD_READ_MODE || "direct";
    assert(["direct","sudo","ssh"].includes(readMode), "Select direct, sudo or ssh password read mode");
    let password;
    if(readMode==="ssh") {
      assert.equal(passwordFile,configuredPasswordFile,"SSH mode requires the configured password path");
      try {
        password=execFileSync("ssh",["-o","BatchMode=yes","-o","StrictHostKeyChecking=yes","-o","IdentitiesOnly=yes","-o","ConnectTimeout=10","-i","/home/aither/.ssh/id_ed25519","root@172.16.106.40","cat -- /var/lib/dev-workspaces/password/password"],{encoding:"utf8",stdio:["ignore","pipe","pipe"]}).trim();
      } catch (_) {throw new Error("Configured portal credential is unavailable through explicit SSH mode");}
    } else if(readMode==="sudo") {
      assert.equal(passwordFile,configuredPasswordFile,"Sudo mode requires the configured password path");
      try {
        password=execFileSync("sudo",["-n","cat","--",passwordFile],{encoding:"utf8",stdio:["ignore","pipe","pipe"]}).trim();
      } catch (_) {throw new Error("Configured portal credential is unavailable through explicit sudo mode");}
    } else {
      try {password=fs.readFileSync(passwordFile,"utf8").trim();}
      catch (_) {throw new Error("Portal credential is unavailable through direct mode");}
    }
    const context=await browser.newContext({ignoreHTTPSErrors:true,javaScriptEnabled:false,
      httpCredentials:{username:authUser,password},viewport:{width:1440,height:850}});
    const get=async url=>{const r=await context.request.get(baseURL+url,{timeout:40000,maxRedirects:0});assert.equal(r.status(),200,`GET ${url} status`);return r;};
    assert.deepEqual(await (await get("/healthz")).json(),{ok:true});
    const index=await context.newPage();await index.goto(baseURL+"/",{timeout:40000});
    const indexStatus=await (await get("/api/index-status?progress=1")).json();
    const session=await context.newPage();await session.goto(baseURL+sessionPath,{timeout:40000});
    assert.equal(await session.locator("body").getAttribute("data-session"),slug);
    assert.equal(await session.locator("body").getAttribute("data-root-thread-id"),rootThread);
    const conversationID=await session.locator("body").getAttribute("data-conversation-id");assert(conversationID);
    const roster=(await (await get(`/api/sessions/${slug}/team`)).json()).roster;
    assert.equal(roster.rootThreadId,rootThread);assert.equal(roster.slug,slug);
    const page=await (await get(`/api/sessions/${slug}/thread/page`)).json();assert.equal(page.threadId,rootThread);
    const snapshot={slug,rootThread,conversationID,rosterHash:digest(JSON.stringify(canonical(roster))),
      model:page.model || "",reasoningEffort:page.reasoningEffort || ""};
    const result={mode,packageRoot,head:expectedHead,health:true,rootThread,entriesRead:page.entries?.length || 0,
      indexLoading:indexStatus.loading===true,rosterHash:snapshot.rosterHash,assets:[]};
    if(mode==="before") fs.writeFileSync(snapshotFile,JSON.stringify(snapshot,null,2)+"\n",{mode:0o600,flag:"wx"});
    else {
      assert.deepEqual(snapshot,JSON.parse(fs.readFileSync(snapshotFile,"utf8")),"Retained identity/settings/roster changed");
      const catalog=JSON.parse(fs.readFileSync(path.join(packageRoot,"share/dev-workspace/agent-teams.json")));
      assert.equal(catalog.default_team,"delegated");assert.equal(catalog.default_development_team,"delegated");
      const select=index.locator('select[name="team"]');assert.equal(await select.inputValue(),"delegated");
      for(let n=2;n<=6;n++) {
        const id=n===2?"delegated":`delegated_${n}`;
        assert.equal(catalog.teams[id].initial_member_counts.implementer,n);
        const label=await select.locator(`option[value="${id}"]`).textContent();assert(label.includes(`Full team (${n} implementers)`));
      }
      const assets=[['/static/app.js',path.join(sourceRoot,'portal/internal/web/static/app.js')],
        ['/static/style.css',path.join(sourceRoot,'portal/internal/web/static/style.css')]];
      const shared=path.join(required("PORTAL_SMOKE_SHARED_SOURCE"),'conversation/assets');
      for(const name of ['conversation.js','conversation.css','citations.js','uploads.js','refresh.js','sync.js','questions.js']) assets.push(['/codex/assets/'+name,path.join(shared,name)]);
      for(const [url,file] of assets) {const actual=await (await get(url)).body();assert.equal(digest(actual),digest(fs.readFileSync(file)),`Served asset ${url}`);result.assets.push({url,sha256:digest(actual)});}
      assert.equal(await session.locator('[data-transcript-filter="team"]').count(),1);
      assert.equal(await session.locator('#message-submission-status').count(),1);
      assert(await session.locator('script[src="/static/app.js?v=50"]').count());
      const moduleText=(await (await get('/codex/assets/conversation.js')).body()).toString('utf8');
      for(const symbol of ['submissionFailurePresentation','transcriptEntryPresentation','transcriptEntryVisible','citationCopyText']) assert(moduleText.includes(symbol));
      result.catalogDefaultsAndCounts=true;result.continuity=true;
    }
    console.log(JSON.stringify(result)); // No transcript, instructions, password or ledger dump.
    await context.close();
  } finally {await browser.close();}
})().catch(error=>{console.error(error.message);process.exitCode=1;});
