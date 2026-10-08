'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const {chromium, expect} = require('@playwright/test');
const base = 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz';
const root = '/home/aither/workspace/ai/vpsfree.cz';
const slug = '2026-10-07-workspace-file-links';
const password = fs.readFileSync('/var/lib/dev-workspaces/password/password', 'utf8').trim();

(async () => {
  const browser = await chromium.launch({headless: true, channel: 'chromium'});
  try {
    // The independent Python probe verifies the host against its development CA.
    const context = await browser.newContext({ignoreHTTPSErrors: true,
      httpCredentials: {username: 'aither', password},
      permissions: ['clipboard-read', 'clipboard-write'], viewport: {width: 1280, height: 900}});
    const page = await context.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    const response = await page.goto(base + root + '/docs/agent-instructions/lifecycle.md:93');
    assert.equal(response.status(), 200);
    assert.equal(new URL(page.url()).pathname, '/workspace-files');
    assert.equal(new URL(page.url()).hash, '#L93');
    await expect(page.locator('#source-file-version')).toHaveText('Current workspace · includes uncommitted edits');
    await expect(page.locator('.review-line-numbers a[aria-current="line"]')).toHaveText('93');
    await expect(page.locator('.review-linked-line')).toHaveText(fs.readFileSync(root + '/docs/agent-instructions/lifecycle.md', 'utf8').split('\n')[92]);
    await expect(page.locator('.cm-content')).toHaveAttribute('contenteditable', 'false');
    await expect(page.locator('#source-file-notice')).toBeHidden();
    await page.getByRole('button', {name: 'Copy link', exact: true}).click();
    assert.equal(await page.evaluate(() => navigator.clipboard.readText()), page.url());
    // CodeMirror marks its visible gutter aria-hidden; still verify a real clickable link.
    await page.getByRole('link', {name: 'Line 94', exact: true, includeHidden: true}).click();
    await expect(page.locator('.review-line-numbers a[aria-current="line"]')).toHaveText('94');
    assert.equal(new URL(page.url()).hash, '#L94');
    await page.evaluate(() => {location.hash = '#L999999';});
    await expect(page.locator('#source-file-notice')).toHaveText('Line 999999 is not present in this version of the file.');
    await expect(page.locator('.review-linked-line')).toHaveCount(0);
    await page.evaluate(() => {location.hash = '#L93';});
    await expect(page.locator('.review-linked-line')).toHaveCount(1);
    await page.screenshot({path: root + '/work/' + slug + '/shared-file-viewer.png'});

    await page.goto(base + root + '/AGENTS.md:1');
    await expect(page.locator('#source-file-title')).toHaveText('AGENTS.md');
    await expect(page.locator('.review-line-numbers a[aria-current="line"]')).toHaveText('1');
    await page.goto(base + root + '/work/' + slug + '/plan.md:1');
    await expect(page.locator('#source-file-version')).toHaveText('Current session artifact');
    await expect(page.locator('.review-line-numbers a[aria-current="line"]')).toHaveText('1');

    // Exercise preview notices through the real page/editor without host fixtures.
    for (const content of [{kind: 'file', bytes: 600000, limited: true},
                           {kind: 'file', bytes: 2, binary: true}]) {
      await page.route('**/api/workspace/file?*', route => route.fulfill({json: {
        path: 'fixture', source: 'workspace', content}}));
      await page.goto(base + '/workspace-files?path=AGENTS.md');
      await expect(page.locator('#source-file-notice')).toContainText(content.limited ? 'Preview omitted:' : 'cannot be displayed as UTF-8 text');
      await expect(page.locator('.cm-editor')).toHaveCount(0);
      await page.unroute('**/api/workspace/file?*');
    }
    assert.deepEqual(errors, []);
    const result = {passed: true, real_editor: true, shared_line: 93, gutter_navigation: 94,
      read_only: true, clipboard: true, missing_line_notice: true, root_agents: true,
      session_artifact: true, preview_notices: true, page_errors: errors,
      browser_tls_exception: 'development certificate; separately verified against CA by verify-live.py'};
    fs.writeFileSync(root + '/work/' + slug + '/live-browser-verification.json', JSON.stringify(result, null, 2) + '\n');
    console.log(JSON.stringify(result));
  } finally {
    await browser.close();
  }
})().catch(error => {console.error(error.message); process.exitCode = 1;});
