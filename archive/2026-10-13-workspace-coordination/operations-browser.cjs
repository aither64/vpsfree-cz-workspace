const fs = require('node:fs');
const http = require('node:http');
const assert = require('node:assert/strict');
const {chromium} = require('/nix/store/5cwkzbaxg65vbbnjvz05w8jm9m9kbam7-playwright-test-1.61.1/lib/node_modules/@playwright/test');
const tracking = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-13-workspace-coordination';
const hostname = 'vpsfree-cz.workspace.aitherdev.int.vpsfree.cz';
const base = `https://${hostname}`;
(async () => {
 const browser = await chromium.launch({headless:true, executablePath:'/nix/store/q1n69vfpd7bf1fsks84ra1yza4j1lb16-playwright-chromium-headless-shell/chrome-headless-shell-linux64/chrome-headless-shell'});
 try {
  const context = await browser.newContext({viewport:{width:1280,height:900},serviceWorkers:'block'});
  // Read the real authenticated router backend as its trusted local operator.
  // Route only GETs from this host; no credentials or public listener is needed.
  await context.route('**/*', async route => {
   const request=route.request(), url=new URL(request.url());
   if(url.hostname!==hostname || request.method()!=='GET') return route.abort();
   const response=await new Promise((resolve,reject)=>{
    const req=http.request({socketPath:'/run/dev-workspaces/router.sock',path:url.pathname+url.search,method:'GET',headers:{host:hostname}},res=>{
     const chunks=[];let bytes=0;res.on('data',chunk=>{bytes+=chunk.length;if(bytes>10*1024*1024) req.destroy(new Error('response too large'));else chunks.push(chunk)});
     res.on('end',()=>resolve({status:res.statusCode,headers:Object.fromEntries(Object.entries(res.headers).filter(([key])=>!['transfer-encoding','content-length'].includes(key))),body:Buffer.concat(chunks)}));
    });req.on('error',reject);req.end();
   });await route.fulfill(response);
  });
  const page=await context.newPage(),errors=[];
  page.on('pageerror',error=>errors.push(error.message));
  await page.goto(base+'/');
  const card=page.locator('[data-session-slug="2026-10-13-workspace-coordination"]');
  const badge=card.locator('[data-session-reservation]');
  await badge.waitFor({state:'visible',timeout:15000});
  assert.equal(await badge.textContent(),'Machine reserved');
  assert.match(await badge.getAttribute('title'),/vpsfree:aitherdev.*review/);
  const identity=await card.getAttribute('data-session-observation');
  const status=await page.evaluate(async()=>await (await fetch('/api/coordination')).json());
  const holder=status.workspaces.flatMap(w=>w.reservationHolders).find(h=>h.slug==='2026-10-13-workspace-coordination');
  assert.equal(identity,holder.observationIdentity);
  await page.getByRole('button',{name:'Workspace menu'}).click();
  assert.deepEqual(await page.locator('#sidebar-menu a').allTextContents(),['Automatic archival','Operations']);
  await card.scrollIntoViewIfNeeded();
  await page.screenshot({path:tracking+'/operations-session-badge.png'});
  await page.locator('#sidebar-menu a[href="/operations"]').click();
  await page.getByRole('heading',{name:'Operations',exact:true}).waitFor();
  await page.waitForFunction(()=>document.querySelector('[data-coordination]').textContent.includes('Reserved through review'));
  const text=await page.locator('[data-coordination]').textContent();
  assert.match(text,/vpsfree:aitherdev/);assert.match(text,/Completed/);
  assert.equal(await page.locator('[data-coordination-warning]').isVisible(),false);
  await page.screenshot({path:tracking+'/operations-page.png'});
  assert.deepEqual(errors,[]);
  fs.writeFileSync(tracking+'/operations-browser-result.json',JSON.stringify({outcome:'passed',transport:'Read-only Chromium requests to actual private router socket',checks:{menuBesideAutomaticArchival:true,pageAndCompletedJobs:true,reviewReservationBadge:true,rubyGoObservationIdentityMatches:true,noPageErrors:true},observationIdentity:identity,holder},null,2)+'\n');
 } finally {await browser.close()}
})().catch(error=>{console.error(error);process.exitCode=1});
