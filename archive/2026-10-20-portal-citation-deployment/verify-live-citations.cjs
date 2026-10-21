const {chromium} = require(process.env.PLAYWRIGHT_MODULE);
const assert = require('node:assert/strict');
const fs = require('node:fs');

(async () => {
  const browser = await chromium.launch({headless: true, executablePath: process.env.CHROMIUM,
    args: ['--no-sandbox']});
  // This development host uses an internal certificate authority unavailable to
  // the test browser. HTTPS transport and the actual hostname remain in use.
  const context = await browser.newContext({ignoreHTTPSErrors: true,
    httpCredentials: {username: 'aither', password: fs.readFileSync('/var/lib/dev-workspaces/password/password', 'utf8').trim()},
    permissions: ['clipboard-read', 'clipboard-write']});
  const page = await context.newPage();
  const blockedWrites = [], errors = [], pages = [];
  await page.route('**/*', route => {
    if (!['GET', 'HEAD'].includes(route.request().method())) {
      blockedWrites.push({method: route.request().method(), url: route.request().url()});
      return route.abort();
    }
    return route.continue();
  });
  page.on('pageerror', error => errors.push(error.message));
  page.on('response', response => {
    if (response.url().includes('/thread/page')) pages.push({url: response.url(), status: response.status()});
  });
  const url = 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/';
  try {
    const response = await page.goto(url, {waitUntil: 'domcontentloaded'});
    assert.equal(response.status(), 200);
    await page.waitForSelector('#transcript .message', {timeout: 60000});
    const message = page.locator('#transcript .message').filter({hasText: 'Yes—you need a'});
    for (let attempt = 0; attempt < 30 && await message.count() === 0; attempt++) {
      const loaded = page.waitForResponse(response => response.url().includes('/thread/page?cursor=') &&
        response.status() === 200, {timeout: 30000});
      await page.locator('#transcript').evaluate(node => {
        node.scrollTop = 0;
      });
      await page.locator('#transcript').hover();
      await page.mouse.wheel(0, -800);
      await (await loaded).finished();
      await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
    }
    assert.equal(await message.count(), 1, 'original response present in paged history');
    await page.waitForFunction(() => {
      const row = [...document.querySelectorAll('#transcript .message')].find(node => node.textContent.includes('Yes—you need a'));
      return row && !row.textContent.includes('\ue200cite') &&
        [...row.querySelectorAll('a')].some(a => a.textContent === '[1]');
    }, null, {timeout: 60000});
    const links = await message.locator('a').evaluateAll(nodes => nodes.filter(node => /^\[\d+\]$/.test(node.textContent))
      .map(node => ({text: node.textContent, href: node.href, title: node.title})));
    assert(links.some(link => link.href === 'https://pypi.org/help/' && link.title));
    assert(links.some(link => link.href === 'https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/' && link.title));
    assert(await message.locator('table').count() > 0, 'Markdown table preserved');
    assert(await message.locator('code').filter({hasText: 'haveapi-client'}).count() > 0, 'literal code preserved');
    await message.getByRole('button', {name: 'Copy message', exact: true}).click();
    const copied = await page.evaluate(() => navigator.clipboard.readText());
    assert(!copied.includes('\ue200cite'));
    assert(copied.includes('https://pypi.org/help/'));
    assert(copied.includes('https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/'));
    assert(copied.includes('`haveapi-client`'));
    const moduleResult = await page.evaluate(async () => {
      const {citationCopyText} = await import('/codex/assets/citations.js?v=1');
      return citationCopyText({text: '`\ue200cite\ue202literal\ue201`'});
    });
    assert.equal(moduleResult, '`\ue200cite\ue202literal\ue201`');
    for (const request of blockedWrites) {
      assert.equal(request.method, 'POST');
      assert.equal(new URL(request.url).pathname,
        '/api/sessions/2026-10-19-dynamic-python-api-client/queue/reconcile',
        'unexpected write request blocked during read-only verification');
    }
    assert.deepEqual(errors, [], 'browser runtime errors');
    const result = {result: 'passed', url, links, pagedReads: pages.length,
      olderPagesRead: pages.some(entry => entry.url.includes('cursor=')), copiedMarkdownLinks: true,
      tableAndCodePreserved: true, actualWriteRequests: 0, blockedWrites, browserErrors: errors,
      certificateValidation: 'internal development certificate trust bypassed in browser only'};
    fs.writeFileSync(process.env.CITATION_RESULT, JSON.stringify(result, null, 2) + '\n');
    console.log(JSON.stringify(result));
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
