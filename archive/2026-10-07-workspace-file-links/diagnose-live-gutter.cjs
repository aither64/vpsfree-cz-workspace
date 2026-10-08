const fs = require('node:fs');
const {chromium, expect} = require('@playwright/test');
const record = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-07-workspace-file-links';
(async () => {
  const browser = await chromium.launch({headless:true,channel:'chromium'});
  try {
    const context = await browser.newContext({ignoreHTTPSErrors:true,httpCredentials:{username:'aither',password:fs.readFileSync('/var/lib/dev-workspaces/password/password','utf8').trim()},viewport:{width:1280,height:900}});
    const page = await context.newPage();
    await page.goto('https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/lifecycle.md:93');
    await expect(page.locator('.review-line-numbers a[aria-current="line"]')).toHaveText('93');
    const result = {
      visibleRoleCount:await page.getByRole('link',{name:'Line 94',exact:true}).count(),
      includingHiddenRoleCount:await page.getByRole('link',{name:'Line 94',exact:true,includeHidden:true}).count(),
      links:await page.locator('.review-line-numbers a').evaluateAll(links => links.filter(a => ['93','94'].includes(a.dataset.line)).map(a => ({text:a.textContent,ariaLabel:a.getAttribute('aria-label'),href:a.getAttribute('href'),gutterAriaHidden:a.closest('.cm-gutters')?.getAttribute('aria-hidden'),display:getComputedStyle(a).display,bounds:a.getBoundingClientRect().toJSON()})))
    };
    fs.writeFileSync(record+'/live-browser-diagnostic.json',JSON.stringify(result,null,2)+'\n');
    console.log(JSON.stringify(result));
    await page.screenshot({path:record+'/live-browser-diagnostic.png'});
  } finally {await browser.close();}
})().catch(e => {console.error(e.message);process.exitCode=1;});
