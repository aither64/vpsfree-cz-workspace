'use strict';
// Read-only final activation fence. Credentials stay in memory and origin-scoped.
const fs = require('node:fs'), cp = require('node:child_process'), crypto = require('node:crypto');
const root = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace';
const checkout = '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace';
const revision = '469757183ba9491d642b56e91658dc64e390647b';
const origin = 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz';
const read = command => cp.execFileSync('ssh',['-o','BatchMode=yes','-o','ConnectTimeout=8','-o','LogLevel=ERROR','root@172.16.106.40',command],{encoding:'utf8',timeout:15000,maxBuffer:8192,stdio:['ignore','pipe','pipe']}).trim();
(async () => {
 const {request} = require('@playwright/test');
 const proof=JSON.parse(fs.readFileSync(root+'/profile-prepared-46975718.json'));
 if(proof.operation.coverage.find(x=>x.repository==='dev-workspace')?.revision!==revision)throw Error();
 const candidate=proof.operation.candidatePackage;
 if(read('readlink -f /home/aither/.local/state/dev-workspaces/profile')!==candidate)throw Error();
 const context=await request.newContext({ignoreHTTPSErrors:true,httpCredentials:{username:read('cut -d: -f1 /var/lib/dev-workspaces/auth/htpasswd'),password:read('cat /var/lib/dev-workspaces/password/password'),origin}});
 try {
  const assets={};
  for (const [url,file] of [['/static/browser-notifications.js','portal/internal/web/static/browser-notifications.js'],['/notification-worker.js','portal/internal/web/static/notification-worker.js']]) {
   const expected=crypto.createHash('sha256').update(cp.execFileSync('git',['-C',checkout,'show',revision+':'+file],{maxBuffer:1048576})).digest('hex');
   const reply=await context.get(origin+url,{timeout:15000});
   const actual=crypto.createHash('sha256').update(await reply.body()).digest('hex');
   if(reply.status()!==200||actual!==expected)throw Error();
   assets[url]={status:reply.status(),sha256:actual};
  }
  const reply=await context.get(origin+'/browser-notifications',{timeout:15000}); const html=await reply.text();
  if(reply.status()!==200||!html.includes('/static/browser-notifications.js?v=3'))throw Error();
  const report={schema:1,revision,candidatePackage:candidate,selectedProfileMatches:true,assets,controlsHTTPStatus:200,currentClientV3:true,readOnly:true,permissionOrSubscriptionMutation:false};
  fs.writeFileSync(root+'/worker-update-served-proof.json',JSON.stringify(report,null,2)+'\n',{flag:'wx',mode:0o600});
  console.log('Live selected package, served client/worker and current page cache version match.');
 }finally{await context.dispose();}
})().catch(()=>{console.error('Final served-asset proof failed; no raw diagnostics emitted.');process.exitCode=1;});
