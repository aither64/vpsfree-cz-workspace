"use strict";
try {
// PREPARED ONLY. Explicit GETs; page JavaScript and service workers stay disabled.
const fs = require("node:fs"), path = require("node:path");
const {createHash} = require("node:crypto"), {execFileSync} = require("node:child_process");
const {chromium} = require("@playwright/test");
const dir = __dirname, cfg = JSON.parse(fs.readFileSync(path.join(dir, "candidate.json")));
const phase = process.argv[2];
let diagnosticStage = "bootstrap";
const requireThat = value => {
  if (!value) {
    const error = Error("check_failed"); error.diagnosticCheck = "assertion";
    Error.captureStackTrace(error, requireThat); throw error;
  }
};
const namingReasons = new Set(["argument_observation_bound", "candidate_catalog_hash_mismatch", "catalog_argument_bound", "catalog_argument_mismatch", "catalog_argument_not_config", "catalog_observation_bound", "children_observation_bound", "expected_package_and_unit_required", "naming_executable_changed", "native_candidate_observation_bound", "observation_unavailable", "portal_executable_mismatch", "portal_main_pid_unavailable", "process_observation_bound", "process_relation_changed", "process_relation_unavailable", "task_observation_bound", "unique_owned_naming_child_not_observed"]);
const diagnosticFailure = (error, stage = diagnosticStage) => {
  const match = String(error?.stack || "").match(/continuity-diagnostic[.]cjs:(\d+):(\d+)/);
  const check = error?.diagnosticCheck;
  return {state:"failed",phase,reason:"read_only_continuity_not_confirmed",stage,
    check:check === "assertion" || check === "command" ||
      typeof check === "string" && check.startsWith("naming_") && namingReasons.has(check.slice(7)) ? check : "operation",
    source:"continuity-diagnostic.cjs",line:match ? Number(match[1]) : null};
};
requireThat(["before", "after"].includes(phase));
const receiptDir = path.resolve(process.argv[3] || "");
requireThat(receiptDir.startsWith(dir + "/attempts/"));
const digest = value => createHash("sha256").update(value).digest("hex");
const canonical = value => Array.isArray(value) ? value.map(canonical) : value && typeof value === "object" ?
  Object.fromEntries(Object.keys(value).sort().map(key => [key, canonical(value[key])])) : value;
const hashJSON = value => digest(JSON.stringify(canonical(value)));
const run = (cmd, args) => {
  try { return execFileSync(cmd, args, {encoding:"utf8", timeout:15000, maxBuffer:4*1024*1024, stdio:["ignore","pipe","pipe"]}).trim(); }
  catch (error) {
    error.diagnosticCheck = "command"; Error.captureStackTrace(error, run);
    if (cmd === "python3" && args[0] === path.join(dir, "naming-readiness.py")) {
      try {
        const child = JSON.parse(String(error.stdout || ""));
        if (child.ready === false && namingReasons.has(child.reason)) error.diagnosticCheck = "naming_" + child.reason;
      } catch (_) {}
    }
    throw error;
  }
};
const save = (name, value) => fs.writeFileSync(path.join(receiptDir, name), JSON.stringify(value, null, 2) + "\n", {mode:0o600, flag:"wx"});
const expectedPackage = phase === "before" ? cfg.selected : cfg.candidate;
const profile = "/home/aither/.local/state/dev-workspaces/profile";
let browser, context;
const processIdentity = unit => {
  requireThat(run("systemctl", ["--user", "is-active", unit]) === "active");
  const pid = run("systemctl", ["--user", "show", unit, "--property=MainPID", "--value"]);
  requireThat(/^[1-9][0-9]*$/.test(pid));
  const exe = fs.realpathSync("/proc/" + pid + "/exe");
  const stat = fs.readFileSync("/proc/" + pid + "/stat", "utf8");
  const start = stat.slice(stat.lastIndexOf(")") + 2).split(" ")[19];
  requireThat(/^[0-9]+$/.test(start));
  return {fingerprint:hashJSON([pid, start, exe]), executable:exe};
};
async function main() {
  diagnosticStage = "binding";
  requireThat(run("dev-session", ["current"]) === cfg.slug);
  requireThat((process.env.DEV_SESSION_SLUG === undefined && process.env.DEV_SESSION_WORKSPACE === undefined) ||
    (process.env.DEV_SESSION_SLUG === cfg.slug && process.env.DEV_SESSION_WORKSPACE === cfg.workspace));
  diagnosticStage = "profile_and_source_heads";
  requireThat(fs.realpathSync(profile) === expectedPackage);
  for (const [repo,head] of Object.entries(cfg.sources)) {
    requireThat(run("git", ["-C", path.join(cfg.sourceRoot,repo), "rev-parse", "HEAD"]) === head);
    requireThat(run("git", ["-C", path.join(cfg.sourceRoot,repo), "status", "--porcelain"]) === "");
  }
  diagnosticStage = "system_identity";
  const system = fs.realpathSync("/run/current-system"), systemProfile = fs.realpathSync("/nix/var/nix/profiles/system");
  requireThat(system === cfg.system && systemProfile === cfg.system);
  for (const base of ["/run/current-system", "/nix/var/nix/profiles/system"]) {
    requireThat(JSON.parse(fs.readFileSync(base + "/etc/confctl/configuration-info.json")).revision === cfg.systemConfiguration);
    requireThat(JSON.parse(fs.readFileSync(base + "/etc/confctl/inputs-info.json")).devWorkspace.rev === cfg.systemRuntime);
  }
  diagnosticStage = "services";
  requireThat(run("systemctl", ["is-active", "nginx.service"]) === "active");
  for (const unit of ["workspace-router.service", "workspace-coordinator.service", "workspace-portal@vpsfree-cz.service"])
    requireThat(run("systemctl", ["--user", "is-active", unit]) === "active");
  diagnosticStage = "native_and_tmux_identity";
  const native = processIdentity("workspace-codex@vpsfree-cz.service"), tmux = processIdentity("workspace-tmux@vpsfree-cz.service");
  requireThat(native.executable === fs.realpathSync(expectedPackage + "/libexec/codex/libexec/codex/bin/codex"));
  diagnosticStage = "workspace_registry";
  const registration = JSON.parse(fs.readFileSync("/home/aither/.config/dev-workspaces/registry.json"));
  requireThat(registration.schema === 1 && Array.isArray(registration.workspaces));
  const matches = registration.workspaces.filter(row => row.root === cfg.workspace);
  requireThat(matches.length === 1 && matches[0].name === "vpsfree-cz");
  const hostname = "vpsfree-cz.workspace.aitherdev.int.vpsfree.cz";
  requireThat(matches[0].hostname === hostname);
  const baseURL = "https://" + hostname, own = "/api/sessions/" + cfg.slug;
  diagnosticStage = "router_health";
  requireThat(JSON.parse(run("curl", ["--fail", "--silent", "--show-error", "--max-time", "10", "--unix-socket", "/run/dev-workspaces/router.sock", "-H", "Host: " + hostname, "http://localhost/healthz"])).ok === true);
  diagnosticStage = "unauthenticated_tls_health";
  requireThat(run("curl", ["--silent", "--show-error", "--max-time", "10", "--cacert", "/var/lib/dev-workspaces/public/ca.pem", "--output", "/dev/null", "--write-out", "%{http_code}", baseURL + "/healthz"]) === "401");
  diagnosticStage = "own_manifest_socket";
  // Decode and validate the own manifest with this phase's installed parser.
  const manifest = JSON.parse(run("/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby", ["-e", `
    load ARGV.fetch(0)
    runner = DevSession::Runner.new(workspace: ARGV.fetch(1), require_runtime: false)
    manifest = runner.send(:load_portal_manifest, ARGV.fetch(2), required: true, expected_slug: ARGV.fetch(3))
    codex = manifest.fetch('codex')
    print JSON.generate({slug: manifest.fetch('slug'), rootThread: codex.fetch('thread_id'), socket: codex.fetch('socket_path')})
  `, path.join(expectedPackage, "libexec/workspace-portal/.dev-session-wrapped"), cfg.workspace,
    path.join(cfg.tracking, "portal.yml"), cfg.slug]));
  const {rootThread, socket} = manifest;
  requireThat(manifest.slug === cfg.slug && typeof rootThread === "string" && rootThread.length > 0 &&
    typeof socket === "string" && path.isAbsolute(socket));
  const socketStat = fs.statSync(socket); requireThat(socketStat.isSocket());
  diagnosticStage = "credential_in_memory";
  let password;
  try {
    password = execFileSync("ssh", ["-o","BatchMode=yes","-o","StrictHostKeyChecking=yes","-o","IdentitiesOnly=yes","-o","ConnectTimeout=10","-i","/home/aither/.ssh/id_ed25519","root@172.16.106.40","cat -- /var/lib/dev-workspaces/password/password"],
      {encoding:"utf8",timeout:15000,maxBuffer:16384,stdio:["ignore","pipe","pipe"]}).trim();
    requireThat(password.length > 0);
  } catch (_) {throw Error("credential_read_unavailable");}
  diagnosticStage = "browser_context";
  browser = await chromium.launch({headless:true,channel:"chromium"});
  context = await browser.newContext({ignoreHTTPSErrors:true,javaScriptEnabled:false,serviceWorkers:"block",
    httpCredentials:{username:"aither",password},viewport:{width:1440,height:850}});
  password = undefined;
  // No index-status/session enumeration, streams, controller, attention, push or writes.
  const allowed = url => url.origin === baseURL && (url.pathname === "/healthz" ||
    url.pathname === "/notification-worker.js" ||
    url.pathname === "/" + cfg.slug + "/" || url.pathname === "/files/" + cfg.slug ||
    [own+"/team",own+"/thread/page",own+"/queue",own+"/files",own+"/file",own+"/file/download"].includes(url.pathname) ||
    url.pathname.startsWith("/static/") || url.pathname.startsWith("/codex/assets/"));
  await context.route("**/*", route => {
    const request=route.request();
    if (request.method() !== "GET" || !allowed(new URL(request.url()))) return route.abort();
    return route.continue();
  });
  const get = async resource => {
    const url = new URL(resource, baseURL); requireThat(allowed(url));
    const response = await context.request.get(url.href, {timeout:40000,maxRedirects:0});
    requireThat(response.status() === 200); return response;
  };
  diagnosticStage = "authenticated_health";
  requireThat((await (await get("/healthz")).json()).ok === true);
  diagnosticStage = "own_session_page";
  const page = await context.newPage(); requireThat((await page.goto(baseURL+"/"+cfg.slug+"/",{timeout:40000})).status() === 200);
  requireThat(await page.locator("body").getAttribute("data-session") === cfg.slug);
  requireThat(await page.locator("body").getAttribute("data-root-thread-id") === rootThread);
  const conversation = await page.locator("body").getAttribute("data-conversation-id"); requireThat(conversation);
  diagnosticStage = "own_roster";
  const roster = (await (await get(own+"/team")).json()).roster;
  requireThat(roster.slug === cfg.slug && roster.rootThreadId === rootThread && Array.isArray(roster.members));
  for (const member of ["implementer2","implementer3"]) requireThat(roster.members.some(row => row.address === member && row.state === "ready"));
  diagnosticStage = "own_transcript";
  const transcript = await (await get(own+"/thread/page")).json();
  requireThat(transcript.threadId === rootThread && Array.isArray(transcript.entries));
  // Saved lead settings belong to the validated roster; page enrichment is optional.
  requireThat(typeof roster.leadModel === "string" && roster.leadModel.length > 0 &&
    typeof roster.leadEffort === "string" && roster.leadEffort.length > 0);
  diagnosticStage = "own_queue";
  const queue = await (await get(own+"/queue")).json(); requireThat(Array.isArray(queue));
  // Only exposed same-thread attempt identities, never global ledger or text.
  const attempts = {queued:queue.map(row => ({client:digest(row.clientUserMessageId),id:digest(row.id)})),
    visible:[...new Set((transcript.entries||[]).filter(row=>row.clientUserMessageId).map(row=>digest(row.clientUserMessageId)))]};
  const snapshot = {capturedAt:new Date().toISOString(),profilePackage:expectedPackage,profileLink:fs.readlinkSync(profile),
    system,systemProfile,systemConfiguration:cfg.systemConfiguration,systemRuntime:cfg.systemRuntime,
    hostContract:"equivalent; mixed source revisions",native,tmux,socket:hashJSON([socket,socketStat.dev,socketStat.ino]),
    identity:{root:digest(rootThread),conversation:digest(conversation),roster:hashJSON(roster),
      model:roster.leadModel,effort:roster.leadEffort},memberCount:roster.members.length,attempts};
  diagnosticStage = "source_assets";
  const source = path.join(cfg.sourceRoot,"dev-workspace"), shared = path.join(cfg.sourceRoot,"codex-web");
  const sourceBytes = (repo,revision,relative) => execFileSync("git",["-C",repo,"show",revision+":"+relative],
    {timeout:15000,maxBuffer:8*1024*1024,stdio:["ignore","pipe","pipe"]});
  const bHead=phase === "before" ? cfg.systemRuntime : cfg.sources["dev-workspace"];
  const aHead=phase === "before" ? cfg.oldShared : cfg.sources["codex-web"];
  const assets = [["/static/app.js",source,bHead,"portal/internal/web/static/app.js"],
    ["/static/style.css",source,bHead,"portal/internal/web/static/style.css"],
    ["/static/browser-notifications.js",source,bHead,"portal/internal/web/static/browser-notifications.js"],
    ["/static/session-attention-store.js",source,bHead,"portal/internal/web/static/session-attention-store.js"],
    ["/notification-worker.js",source,bHead,"portal/internal/web/static/notification-worker.js"]];
  for (const name of ["conversation.js","conversation.css","citations.js","uploads.js","refresh.js","sync.js","questions.js"])
    assets.push(["/codex/assets/"+name,shared,aHead,"conversation/assets/"+name]);
  let assetIndex = 0;
  for (const [url,repo,head,file] of assets) {
    diagnosticStage = "asset_" + assetIndex++;
    requireThat(digest(await (await get(url)).body()) === digest(sourceBytes(repo,head,file)));
  }
  diagnosticStage = "catalog";
  const catalog=JSON.parse(fs.readFileSync(path.join(expectedPackage,"share/dev-workspace/agent-teams.json")));
  requireThat(catalog.default_team === "delegated" && catalog.default_development_team === "delegated");
  requireThat(catalog.capacity.required_native_child_threads === 8);
  for (let n=2;n<=6;n++) {
    const id=n===2?"delegated":"delegated_"+n; requireThat(catalog.teams[id].initial_member_counts.implementer === n);
    requireThat(catalog.teams[id].max_open_agents === n+2);
  }
  // This already-registered shell script is text only and never executed.
  diagnosticStage = "passive_file_preview";
  const query="?artifact="+encodeURIComponent(cfg.passiveScript);
  const expected=fs.readFileSync(path.join(cfg.tracking,cfg.passiveScript));
  const preview=await (await get(own+"/file"+query)).json();
  requireThat(!preview.content.binary && !preview.content.limited && digest(preview.content.text) === digest(expected));
  diagnosticStage = "passive_file_download";
  const download=await get(own+"/file/download"+query);
  requireThat(download.headers()["content-type"].startsWith("application/octet-stream"));
  requireThat(download.headers()["content-disposition"].startsWith("attachment;"));
  requireThat(digest(await download.body()) === digest(expected));
  diagnosticStage = "passive_source_viewer";
  const viewer=await context.newPage();
  requireThat((await viewer.goto(baseURL+"/files/"+cfg.slug+query,{timeout:40000})).status() === 200);
  requireThat(await viewer.locator("#source-file").getAttribute("data-slug") === cfg.slug);
  diagnosticStage = "after_continuity";
  if (phase === "after") {
    const before=JSON.parse(fs.readFileSync(path.join(receiptDir,"continuity-before.json")));
    requireThat(hashJSON(snapshot.identity) === hashJSON(before.identity));
    requireThat(hashJSON(native) === hashJSON(before.native) && hashJSON(tmux) === hashJSON(before.tmux));
    requireThat(snapshot.socket === before.socket && snapshot.memberCount === before.memberCount);
    const observed=new Set([...attempts.queued.map(row=>row.client),...attempts.visible]);
    requireThat(before.attempts.queued.every(row=>observed.has(row.client)));
    const files=(await (await get(own+"/files")).json()).files;
    requireThat(Array.isArray(files) && files.some(row=>row.path === cfg.passiveScript && row.registered));
    for (const src of ["/static/app.js?v=55","/static/session-attention-store.js?v=4","/static/browser-notifications.js?v=6"])
      requireThat(await page.locator('script[src="'+src+'"]').count() === 1);
    requireThat(await page.locator('[data-transcript-filter="team"]').count() === 1);
    requireThat(await page.locator("#message-submission-status").count() === 1);
    snapshot.filesCount=files.length;
  }
  diagnosticStage = "naming_readiness";
  const naming=JSON.parse(run("python3",[path.join(dir,"naming-readiness.py"),"--package",expectedPackage,"--unit","workspace-portal@vpsfree-cz.service"]));
  requireThat(naming.ready === true && naming.naming_turn_verified === false);
  diagnosticStage = "process_recheck";
  requireThat(hashJSON(native) === hashJSON(processIdentity("workspace-codex@vpsfree-cz.service")));
  requireThat(hashJSON(tmux) === hashJSON(processIdentity("workspace-tmux@vpsfree-cz.service")));
  diagnosticStage = "write_diagnostic_receipt";
  snapshot.capturedAt=new Date().toISOString();
  snapshot.naming=naming; snapshot.state="passed";
  save("continuity-"+phase+".json",snapshot);
  console.log(JSON.stringify({state:"passed",phase,health:true,assets:true,catalog:true,passiveScript:true,
    rosterMembers:roster.members.length,updatedRoster:true,nativeContinuity:phase === "after",namingReadinessOnly:true}));
}
main().catch(error=>{console.error(JSON.stringify(diagnosticFailure(error)));process.exitCode=1;})
  .finally(async()=>{try{await context?.close();}catch(error){console.error(JSON.stringify(diagnosticFailure(error,"cleanup_context")));process.exitCode=1;}try{await browser?.close();}catch(error){console.error(JSON.stringify(diagnosticFailure(error,"cleanup_browser")));process.exitCode=1;}});

} catch (error) {
  const match = String(error?.stack || "").match(/continuity-diagnostic[.]cjs:(\d+):(\d+)/);
  console.error(JSON.stringify({state:"failed",phase:["before","after"].includes(process.argv[2]) ? process.argv[2] : "invalid",
    reason:"read_only_continuity_not_confirmed",stage:"bootstrap",check:"initialization",
    source:"continuity-diagnostic.cjs",line:match ? Number(match[1]) : null}));
  process.exitCode = 1;
}
