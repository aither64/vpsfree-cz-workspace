const {chromium} = require(process.env.PLAYWRIGHT_MODULE || '/nix/store/2xc3ahwfjaa3k3wpn4gslgws25swsyd7-playwright-core-1.59.1');
const fs = require('node:fs');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');

const base = 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz';
const slug = '2026-09-12-portal-review-experience';
const output = process.env.REVIEW_BROWSER_OUTPUT;
const expectedHead = process.env.EXPECTED_RUNTIME_HEAD || 'cbe617d';
const repository = crypto.createHash('sha256').update('dev-workspace').digest('hex').slice(0, 32);
const checks = [], pageErrors = [], cspViolations = [], urls = {};
const started = Date.now();
const api = (operation, values = {}) => {
  const query = new URLSearchParams({repository, ...values});
  return base + '/api/sessions/' + slug + '/repository-' + operation + '?' + query;
};
const fileSelector = id => '.repository-file[data-file-id="' + id + '"]';
const sectionSelector = id => '.repository-file-section[data-file-id="' + id + '"]';
const parentURL = (source, commit) => {
  const next = new URL(source);
  for (const name of ['file', 'version']) next.searchParams.delete(name);
  next.searchParams.set('commit', commit);
  next.searchParams.set('view', 'diff');
  next.hash = '';
  return next;
};

(async () => {
  assert(output, 'Set REVIEW_BROWSER_OUTPUT to the owned evidence directory');
  assert(/^[0-9a-f]{7,40}$/.test(expectedHead), 'EXPECTED_RUNTIME_HEAD must be a full or abbreviated SHA');
  fs.mkdirSync(output, {recursive: true});
  const browser = await chromium.launch({
    executablePath: process.env.CHROMIUM_EXECUTABLE || '/nix/store/789yhb4v2kq51jwl4acmmjvxs7mfrlhv-chromium-152.0.7977.75/bin/chromium',
    headless: true, args: ['--no-sandbox'],
  });
  let observedHead, savedBase, selectedPath, statuses;
  try {
    const context = await browser.newContext({viewport: {width: 1600, height: 1000}, ignoreHTTPSErrors: true,
      httpCredentials: {username: 'aither', password: fs.readFileSync('/var/lib/dev-workspaces/password/password', 'utf8').trim()}});
    context.setDefaultTimeout(30000);
    await context.grantPermissions(['clipboard-read', 'clipboard-write'], {origin: base});
    context.on('page', page => page.on('pageerror', error => pageErrors.push(error.message)));
    await context.exposeBinding('recordReviewCSP', (_, directive) => cspViolations.push(directive));
    await context.addInitScript(() => document.addEventListener('securitypolicyviolation', event => {
      void window.recordReviewCSP(event.violatedDirective);
    }));
    const page = await context.newPage();
    const get = async (operation, values) => {
      const response = await context.request.get(api(operation, values));
      assert.equal(response.status(), 200, operation + ' request failed');
      return response.json();
    };
    const state = await get('state');
    observedHead = state.head;
    assert(observedHead.startsWith(expectedHead), 'Repository head does not match EXPECTED_RUNTIME_HEAD: ' + observedHead);
    await page.goto(base + '/' + slug + '/?tab=repositories', {waitUntil: 'domcontentloaded'});
    const card = page.locator('[data-repository-id="' + repository + '"]');
    await card.locator('.repository-commit-subject').first().waitFor();
    await card.locator('[data-review-branch]').click();
    await page.locator('.repository-comparison-stats').waitFor();
    await page.locator('.repository-file-tree').first().waitFor();
    const review = new URL(page.url()).searchParams.get('review');
    const comparison = await get('comparison', {review});
    savedBase = comparison.pair.base;
    assert.equal(comparison.pair.head, observedHead);
    assert((await page.locator('.repository-directory').count()) >= 3, 'Expected nested directories in the live branch');
    assert(await page.locator('.repository-directory').evaluateAll(directories => directories.every(directory => directory.open)), 'A new comparison must start expanded');
    statuses = await page.locator('.repository-file-list .repository-file-status').evaluateAll(nodes => nodes.map(node => ({
      text: node.textContent, label: node.getAttribute('aria-label'), title: node.title, color: getComputedStyle(node).color,
    })));
    const expectedColors = {A: 'rgb(126, 231, 135)', M: 'rgb(210, 168, 255)', D: 'rgb(255, 161, 152)',
      R: 'rgb(121, 192, 255)', C: 'rgb(121, 192, 255)', T: 'rgb(227, 179, 65)', '?': 'rgb(227, 179, 65)'};
    for (const status of statuses) {
      assert(/^[AMDRCT?]$/.test(status.text), 'Status must be one letter');
      assert(status.label && status.title === status.label, 'Status must retain a descriptive accessible label');
      assert.equal(status.color, expectedColors[status.text]);
    }
    for (const [selector, color, prefix] of [
      ['.repository-additions', 'rgb(126, 231, 135)', '+'], ['.repository-deletions', 'rgb(255, 161, 152)', '−'],
    ]) {
      const values = await page.locator('.repository-comparison ' + selector).evaluateAll(nodes => nodes.map(node => ({text: node.textContent, color: getComputedStyle(node).color})));
      assert(values.length >= 3, 'Expected totals, tree, and file-header statistics');
      assert(values.every(value => value.color === color && value.text.startsWith(prefix)), 'Statistics lost their color or sign');
    }
    checks.push('live branch with expanded nested tree', 'compact accessible colored statuses', 'colored totals/tree/file statistics');

    const preferred = ['portal/internal/web/static/repository-review.js', 'portal/internal/web/server.go', 'portal/internal/repository/review.go'];
    const file = preferred.map(path => comparison.files.find(file => file.path === path && file.oldMode !== '000000' && file.newMode !== '000000')).find(Boolean);
    assert(file, 'Expected an existing syntax-highlighted portal source file in the comparison');
    selectedPath = file.path;
    const nav = page.locator(fileSelector(file.id));
    const section = page.locator(sectionSelector(file.id));
    const directoryPath = file.path.split('/').slice(0, -1).join('/');
    const directory = page.locator('.repository-directory[data-directory-path=' + JSON.stringify(directoryPath) + ']');
    await nav.click();
    await section.locator('.cm-editor').first().waitFor();
    await page.waitForFunction(id => new Set([...document.querySelectorAll('.repository-file-section[data-file-id="' + id + '"] [class*="review-token-"]')].map(node => getComputedStyle(node).color)).size >= 3, file.id);
    assert.equal(await nav.locator('.repository-file-path').textContent(), file.path.split('/').pop());
    const beforeCopy = page.url();
    await nav.locator('..').getByRole('button', {name: 'Copy file path', exact: true}).click();
    assert.equal(await page.evaluate(() => navigator.clipboard.readText()), file.path);
    assert.equal(page.url(), beforeCopy, 'Tree path copy navigated');
    await section.getByRole('button', {name: 'Copy file path', exact: true}).click();
    assert.equal(await page.evaluate(() => navigator.clipboard.readText()), file.path);
    assert.equal(page.url(), beforeCopy, 'Header path copy navigated');
    urls.branch = page.url();
    await page.screenshot({path: output + '/repository-tree-desktop.png'});
    checks.push('syntax colors retained', 'repository-relative path copied through native clipboard from tree and header');

    const summary = directory.locator(':scope > summary');
    await summary.focus();
    await page.keyboard.press('Enter');
    assert.equal(await directory.getAttribute('open'), null);
    assert.equal(await nav.isVisible(), false);
    assert.equal(await section.isVisible(), true, 'Collapsing navigation hid the diff');
    await page.getByRole('button', {name: 'Unified', exact: true}).click();
    assert.equal(await directory.getAttribute('open'), null, 'Layout change expanded a collapsed directory');
    await summary.focus();
    await page.keyboard.press('Space');
    assert.equal(await directory.evaluate(node => node.open), true);
    assert.equal(await nav.isVisible(), true);
    await summary.click();
    const outside = comparison.files.find(item => item.path.includes('/') && !item.path.startsWith(directoryPath + '/'));
    assert(outside, 'Expected a file outside the selected directory for history navigation');
    await page.locator(fileSelector(outside.id)).click();
    await page.goBack();
    await page.waitForFunction(({id, path}) => new URL(location.href).searchParams.get('file') === id &&
      [...document.querySelectorAll('.repository-directory')].find(node => node.dataset.directoryPath === path)?.open, {id: file.id, path: directoryPath});
    assert.equal(await nav.isVisible(), true);
    await page.goForward();
    await page.waitForFunction(id => new URL(location.href).searchParams.get('file') === id, outside.id);
    await page.goBack();
    await page.waitForFunction(id => new URL(location.href).searchParams.get('file') === id, file.id);
    checks.push('directory collapse and native Enter/Space controls', 'collapse preserved during layout changes', 'Back/Forward reveals selected file ancestors');

    const contents = await get('comparison', {review, file: file.id});
    for (const [layout, version, versionLabel, blob] of [
      ['unified', 'old', 'Before', contents.preview.content.before], ['split', 'new', 'After', contents.preview.content.after],
    ]) {
      await page.getByRole('button', {name: layout === 'split' ? 'Split' : 'Unified', exact: true}).click();
      await section.getByRole('link', {name: 'View file', exact: true}).click();
      await section.getByRole('button', {name: versionLabel, exact: true}).click();
      const full = new URL(page.url());
      assert.equal(full.searchParams.get('view'), 'file');
      assert.equal(full.searchParams.get('version'), version);
      const lines = blob.text.split('\n').length - (blob.text.endsWith('\n') ? 1 : 0);
      const line = Math.min(5, lines);
      assert(line > 0, 'Expected nonempty source for both file versions');
      full.hash = version + '-L' + line;
      await page.goto(full.href, {waitUntil: 'domcontentloaded'});
      await section.locator('.cm-gutters a[href$="#' + version + '-L' + line + '"]').first().waitFor();
      assert(await page.locator('.repository-directory').evaluateAll(directories => directories.every(directory => directory.open)), 'Reload did not start expanded');
      const back = section.getByRole('link', {name: 'Back to diff', exact: true});
      assert.equal(await back.getAttribute('title'), 'Back to diff');
      assert.equal(await section.locator('.repository-file-heading').evaluate(node => node.firstElementChild.classList.contains('repository-back-to-diff')), true);
      const backURL = new URL(await back.getAttribute('href'));
      assert.equal(backURL.searchParams.get('repository'), repository);
      assert.equal(backURL.searchParams.get('review'), review);
      assert.equal(backURL.searchParams.get('file'), file.id);
      assert.equal(backURL.searchParams.get('view'), 'diff');
      assert.equal(backURL.searchParams.get('layout'), layout);
      assert.equal(backURL.searchParams.has('version'), false);
      assert.equal(backURL.hash, '');
      if (version === 'old') {
        urls.fullFile = full.href;
        await back.scrollIntoViewIfNeeded();
        await page.screenshot({path: output + '/repository-tree-full-file-back.png'});
      }
      await back.click();
      assert.equal(page.url(), backURL.href);
      await section.locator('.cm-editor').first().waitFor();
      assert.equal(await back.isVisible(), false);
    }
    checks.push('Before/unified and After/split cold full-file links', 'back arrow position and exact frozen diff routes');

    await page.getByRole('button', {name: 'Unified', exact: true}).click();
    const headURL = parentURL(page.url(), observedHead);
    const headData = await get('comparison', {review, commit: observedHead});
    await page.goto(headURL.href, {waitUntil: 'domcontentloaded'});
    await page.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, headData.commit.message);
    assert(headData.commit.parents.length > 0, 'Expected a non-root runtime head');
    let checkedParentTab = false;
    const followParent = async expected => {
      const link = page.locator('.repository-parent-link').first();
      await link.waitFor();
      const href = new URL(await link.getAttribute('href'));
      assert.equal(href.searchParams.get('commit'), expected);
      assert.equal(href.searchParams.get('review'), review);
      assert.equal(href.searchParams.get('layout'), 'unified');
      for (const key of ['file', 'view', 'version']) assert.equal(href.searchParams.has(key), false);
      assert.equal(href.hash, '');
      const expectedPage = await get('comparison', {review, commit: expected});
      if (!checkedParentTab) {
        const [tab] = await Promise.all([context.waitForEvent('page'), link.click({modifiers: ['Control']})]);
        await tab.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, expectedPage.commit.message);
        assert.equal(new URL(tab.url()).searchParams.get('commit'), expected);
        assert.equal(new URL(tab.url()).searchParams.get('review'), review);
        assert.equal(new URL(page.url()).searchParams.get('commit'), headData.commit.sha);
        await tab.close(); checkedParentTab = true;
        checks.push('Control-click opens the parent in a separate tab');
      }
      await link.click();
      await page.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, expectedPage.commit.message);
      assert.equal(await page.locator('.repository-commit-detail-identity code').textContent(), expected);
      assert.equal(new URL(page.url()).searchParams.get('review'), review);
      assert.equal(new URL(page.url()).searchParams.get('layout'), 'unified');
      assert.equal(await page.locator('.repository-file-list .repository-file').count(), expectedPage.stats.files);
      return expectedPage;
    };
    const parent = await followParent(headData.commit.parents[0]);
    urls.parent = page.url();
    await page.screenshot({path: output + '/repository-tree-parent-commit.png'});
    await page.reload({waitUntil: 'domcontentloaded'});
    await page.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, parent.commit.message);
    await page.goBack();
    await page.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, headData.commit.message);
    await page.goForward();
    await page.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, parent.commit.message);
    checks.push('real parent commit link with full standard commit page', 'parent reload and Back/Forward');
    const baseData = await get('comparison', {review, commit: savedBase});
    const baseURL = parentURL(page.url(), savedBase);
    await page.goto(baseURL.href, {waitUntil: 'domcontentloaded'});
    await page.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, baseData.commit.message);
    if (baseData.commit.parents.length) {
      await followParent(baseData.commit.parents[0]);
      urls.beforeBase = page.url();
      checks.push('parent navigation across the saved comparison base');
    } else {
      assert.equal(await page.locator('.repository-commit-parents').textContent(), 'No parent');
      assert.equal(await page.locator('.repository-parent-link').count(), 0);
      checks.push('saved comparison base is a root commit and correctly shows No parent');
    }
    await page.setViewportSize({width: 390, height: 844});
    await page.goto(urls.branch, {waitUntil: 'domcontentloaded'});
    await page.locator('.repository-file-tree').first().waitFor();
    await section.locator('.cm-editor').first().waitFor();
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), 'Mobile document overflows horizontally');
    assert.equal(await page.locator('[contenteditable="true"]').count(), 0);
    await page.waitForFunction(id => ![...document.querySelectorAll('.repository-file-section[data-file-id=\"' + id + '\"] .review-syntax-status')].some(node => node.textContent === 'Highlighting…'), file.id);
    await page.screenshot({path: output + '/repository-tree-mobile.png'});
    checks.push('390px mobile tree and read-only editors');
    assert.deepEqual(pageErrors, []);
    assert.deepEqual(cspViolations, []);
    checks.push('zero page errors or CSP violations across navigations');
    const result = {passed: true, elapsedSeconds: (Date.now() - started) / 1000, expectedHead, observedHead, savedBase, selectedPath,
      observedStatuses: [...new Set(statuses.map(status => status.text))].sort(), checks, urls,
      limitations: ['TLS trust is checked separately; the browser context ignores certificate errors.',
        'No live Git refs or conversation state were changed; edge-case statuses and merge/root fixtures are covered by component and Go tests.']};
    fs.writeFileSync(output + '/tree-live-browser-results.json', JSON.stringify(result, null, 2) + '\n');
    console.log(JSON.stringify({passed: true, elapsedSeconds: result.elapsedSeconds, checks: checks.length, observedHead, output}));
  } catch (error) {
    fs.writeFileSync(output + '/tree-live-browser-results.json', JSON.stringify({passed: false, elapsedSeconds: (Date.now() - started) / 1000,
      expectedHead, observedHead, savedBase, selectedPath, checks, urls, error: error.message, pageErrors, cspViolations}, null, 2) + '\n');
    throw error;
  } finally {
    await browser.close();
  }
})().catch(error => {console.error(error); process.exitCode = 1;});
