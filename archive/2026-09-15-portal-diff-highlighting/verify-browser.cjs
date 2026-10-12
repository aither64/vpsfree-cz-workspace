// Read-only acceptance of the immutable reported comparison, with verified TLS.
const fs = require('node:fs');
const path = require('node:path');
const tls = require('node:tls');
const {X509Certificate, createHash} = require('node:crypto');
const assert = require('node:assert/strict');
const {chromium, expect} = require('@playwright/test');
(async () => {
  const host = 'vpsfree-cz.workspace.aitherdev.int.vpsfree.cz';
  const leaf = await new Promise((resolve, reject) => {
    const socket = tls.connect({host, servername: host, port: 443, ca: fs.readFileSync('/var/lib/dev-workspaces/public/ca.pem')}, () => {
      resolve(new X509Certificate(socket.getPeerCertificate().raw)); socket.end();
    });
    socket.on('error', reject);
  });
  const pin = createHash('sha256').update(leaf.publicKey.export({type: 'spki', format: 'der'})).digest('base64');
  const browser = await chromium.launch({headless: true, channel: 'chromium', args: ['--ignore-certificate-errors-spki-list=' + pin]});
  const candidate = process.env.REVIEW_EDITOR_CANDIDATE;
  const outputDirectory = process.env.REVIEW_OUTPUT_DIRECTORY || __dirname;
  const results = {candidateAssetOverride: Boolean(candidate), tlsVerified: true, layouts: [], pageErrors: [], failedAssets: [], attemptedMutations: []};
  try {
    for (const layout of ['unified', 'split']) {
      const page = await browser.newPage({viewport: {width: 1920, height: 1200}, httpCredentials: {
        username: 'aither', password: fs.readFileSync('/var/lib/dev-workspaces/password/password', 'utf8').trim(),
      }});
      page.on('pageerror', e => results.pageErrors.push(e.message));
      page.on('response', response => {
        const pathname = new URL(response.url()).pathname;
        if ((pathname.startsWith('/static/') || pathname.startsWith('/codex/assets/')) && response.status() !== 200) {
          results.failedAssets.push({path: pathname, status: response.status()});
        }
      });
      await page.route('**/*', route => {
        if (!['GET', 'HEAD'].includes(route.request().method())) {
          results.attemptedMutations.push({method: route.request().method(), path: new URL(route.request().url()).pathname});
          return route.abort();
        }
        if (candidate && new URL(route.request().url()).pathname === '/static/review-editor.js') {
          return route.fulfill({path: candidate, contentType: 'text/javascript'});
        }
        return route.continue();
      });
      const url = `https://${host}/2026-09-15-abuse-uceprotect/?tab=repositories&repository=f7e4ad2503a24e7ccdccd7895eec0012&review=459a908f223e248f9e827131190441f8&file=a82b2be05b24ddefa6bdeb1ac4ba00dd&view=diff&layout=${layout}#old-L106`;
      const response = await page.goto(url);
      assert.equal(response.status(), 200);
      const deleted = '      return [] if addr_str.nil? || time.nil?';
      const added = '      body_ips = entries.map { |entry| entry[:ip] }.compact.uniq';
      const line = page.locator('.cm-line.review-deleted-line').filter({hasText: deleted.trim()});
      await expect(line).toBeVisible({timeout: 30000});
      await expect(page.locator('.review-syntax-status')).toHaveCount(0, {timeout: 30000});
      const marks = await page.evaluate(({deleted, added}) => {
        return [deleted, added].map(text => {
          const row = [...document.querySelectorAll('.cm-line')].find(el => el.textContent === text);
          if (!row) throw new Error('Expected source line not rendered: ' + text);
          const walker = document.createTreeWalker(row, NodeFilter.SHOW_TEXT);
          const groups = []; let offset = 0;
          while (walker.nextNode()) {
            const node = walker.currentNode, end = offset + node.textContent.length;
            if (node.parentElement.closest('.review-added-text, .review-deleted-text')) {
              if (groups.at(-1)?.to === offset) groups.at(-1).to = end;
              else groups.push({from: offset, to: end});
            }
            offset = end;
          }
          return {text, groups: groups.map(g => ({...g, text: text.slice(g.from, g.to)}))};
        });
      }, {deleted, added});
      for (const mark of marks) {
        assert.equal(mark.groups.length, 1, 'Expected one continuous highlight');
        assert.equal(mark.groups[0].text.trim(), mark.text.trim());
      }
      const file = page.locator('[data-file-id="a82b2be05b24ddefa6bdeb1ac4ba00dd"]').filter({has: page.locator('.repository-editor')});
      await expect(file).toContainText('+206');
      await expect(file).toContainText('−75');
      await expect(page.locator('a[aria-current="line"][data-side="old"][data-line="106"]')).toBeVisible();
      await page.screenshot({path: path.join(outputDirectory, `fixed-${layout}.png`)});
      results.layouts.push({layout, url: page.url(), status: response.status(), marks, fileCounts: {additions: 206, deletions: 75}, syntaxReady: true, lineLink: 'old-L106'});
      await page.close();
    }
    assert.deepEqual(results.pageErrors, []);
    assert.deepEqual(results.failedAssets, []);
    assert.ok(results.attemptedMutations.every(request => request.method === 'POST' &&
      request.path === '/api/sessions/2026-09-15-abuse-uceprotect/queue/reconcile'), 'Unexpected mutation attempt');
    results.backgroundQueueReconciliationBlocked = true;
    fs.writeFileSync(path.join(outputDirectory, 'browser-results.json'), JSON.stringify(results, null, 2) + '\n');
    console.log(JSON.stringify(results, null, 2));
  } finally { await browser.close(); }
})().catch(error => {console.error(error); process.exitCode = 1;});
