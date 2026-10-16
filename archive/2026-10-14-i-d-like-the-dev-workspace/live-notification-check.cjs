'use strict';
// Disposable browser profiles only. Never print auth or subscription material.
const fs = require('node:fs');
const cp = require('node:child_process');
const {chromium, firefox, expect} = require('@playwright/test');
const origin = 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz';
const path = '/2026-10-14-i-d-like-the-dev-workspace/#settings';
const username = cp.execFileSync('ssh', ['-o', 'BatchMode=yes', 'root@172.16.106.40', "cut -d: -f1 /var/lib/dev-workspaces/auth/htpasswd"], {encoding:'utf8'}).trim();
const password = cp.execFileSync('ssh', ['-o', 'BatchMode=yes', 'root@172.16.106.40', 'cat /var/lib/dev-workspaces/password/password'], {encoding:'utf8'}).trim();
if (!username || username.includes('\n') || !password) throw Error('Portal credentials unavailable');
const results = [];
(async () => {
 for (const engine of [chromium, firefox]) {
  const report = {browser: engine.name(), osDisplay: 'not observed on macOS', stage:'launch'};
  let browser, context;
  try {
   browser = await engine.launch({headless:true, ...(engine === chromium ? {channel:'chromium', args:['--ignore-certificate-errors'], ignoreDefaultArgs:['--disable-background-networking']} : {})});
   context = await browser.newContext({ignoreHTTPSErrors:true, httpCredentials:{username,password}});
   await context.grantPermissions(['notifications'], {origin});
   let page = await context.newPage();
   report.stage='load'; await page.goto(origin+path);
   await expect(page.locator('#browser-notifications')).toBeVisible();
   report.title = await page.title();
   report.stage='subscribe'; await page.locator('[data-notification-enable]').click();
   await expect(page.locator('[data-notification-test]')).toBeEnabled({timeout:35000});
   report.subscribed = true;
   report.stage='send-test'; await page.locator('[data-notification-test]').click();
   await expect(page.locator('[data-notification-status]')).toContainText('10 seconds');
   const elsewhere = await context.newPage(); await elsewhere.goto('about:blank'); await elsewhere.bringToFront();
   await page.close();
   report.portalTabsDuringWait=context.pages().filter(p=>p.url().startsWith(origin)).length;
   report.stage='background-delivery';
   await new Promise(resolve=>setTimeout(resolve,18000));
   page=await context.newPage(); await page.goto(origin+path);
   const state = await page.evaluate(async () => {
    const id=localStorage.getItem('workspace-browser-notifications.v1') || '';
    const state=await (await fetch('/api/browser-notifications?registrationId='+encodeURIComponent(id),{cache:'no-store'})).json();
    const registration=await navigator.serviceWorker.getRegistration('/');
    const notifications=registration ? await registration.getNotifications() : [];
    return {providerResult:state.result, visibleNotificationCount:notifications.length,
      testNotificationPresent:notifications.some(n=>n.body==='Browser notification test')};
   });
   Object.assign(report,state); report.stage='complete';
  } catch (error) {
   report.result='incomplete'; report.error=error.name;
   if (context) for (const page of context.pages()) {
    if (page.url().startsWith(origin)) report.controlStatus=await page.locator('[data-notification-status]').textContent().catch(()=> 'unavailable');
   }
  } finally {
   if (context) {
    try {
     const page=await context.newPage(); await page.goto(origin+path);
     const disable=page.locator('[data-notification-disable]');
     await expect(page.locator('#browser-notifications')).toBeVisible();
     // Let initial subscription inspection settle before choosing cleanup.
     await page.waitForFunction(()=>document.querySelector('[data-notification-status]').textContent.trim().length>0);
     if (await disable.isEnabled()) {
      await disable.click(); await expect(page.locator('[data-notification-status]')).toContainText('Disabled on this browser');
     }
     report.disposableSubscriptionRemoved=true;
    } catch (error) {report.cleanup='incomplete'; report.cleanupError=error.name;}
    await context.close();
   }
   if (browser) await browser.close();
   results.push(report); console.log(JSON.stringify(report));
  }
 }
 fs.writeFileSync(__dirname+'/live-notification-check.json',JSON.stringify(results,null,2)+'\n');
})().catch(error=>{console.error('Live notification check could not complete:',error.name);process.exitCode=1;});
