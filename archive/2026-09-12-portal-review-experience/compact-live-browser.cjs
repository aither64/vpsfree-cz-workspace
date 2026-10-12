// Read-only live acceptance. Run only after the exact approved runtime revision is deployed.
const {chromium} = require(process.env.PLAYWRIGHT_MODULE || '/tmp/portal-compact-playwright');
const fs = require('node:fs');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');

const base = 'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz';
const slug = '2026-09-12-portal-review-experience';
const output = process.env.REVIEW_BROWSER_OUTPUT;
const expectedHead = process.env.EXPECTED_RUNTIME_HEAD;
const longCommit = 'd3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2';
const repository = crypto.createHash('sha256').update('dev-workspace').digest('hex').slice(0, 32);
const checks = [], pageErrors = [], cspViolations = [], urls = {};
const started = Date.now();
const api = (operation, values = {}) => {
  const query = new URLSearchParams({repository, ...values});
  return base + '/api/sessions/' + slug + '/repository-' + operation + '?' + query;
};
const fileSelector = id => '.repository-file[data-file-id="' + id + '"]';
const sectionSelector = id => '.repository-file-section[data-file-id="' + id + '"]';
const waitForScrollableDetails = page => page.waitForFunction(() => {
  const pane = document.querySelector('.repository-file-scroll');
  const details = document.querySelector('.repository-comparison-details');
  return document.querySelectorAll('.repository-file-section .review-code-view').length >= 1 &&
    pane.scrollHeight > pane.clientHeight + details.offsetHeight + 1 &&
    ![...pane.querySelectorAll('.review-syntax-status')].some(node => node.textContent === 'Highlighting…');
});

const parentURL = (source, commit) => {
  const next = new URL(source);
  for (const name of ['file', 'view', 'version']) next.searchParams.delete(name);
  next.searchParams.set('commit', commit);
  next.hash = '';
  return next;
};

(async () => {
  assert(output, 'Set REVIEW_BROWSER_OUTPUT to the owned evidence directory');
  assert(/^[0-9a-f]{7,40}$/.test(expectedHead), 'EXPECTED_RUNTIME_HEAD must be a full or abbreviated SHA');
  fs.mkdirSync(output, {recursive: true});
  const browser = await chromium.launch({
    executablePath: process.env.CHROMIUM_EXECUTABLE || '/tmp/portal-compact-chromium/bin/chromium',
    headless: true, args: ['--no-sandbox'],
  });
  let observedHead, savedBase, selectedPath, statuses, scrollGeometry, retainedEditors = [];
  const editorRequests = [];
  try {
    const context = await browser.newContext({viewport: {width: 1600, height: 1000}, ignoreHTTPSErrors: true,
      httpCredentials: {username: 'aither', password: fs.readFileSync('/var/lib/dev-workspaces/password/password', 'utf8').trim()}});
    context.setDefaultTimeout(30000);
    await context.grantPermissions(['clipboard-read', 'clipboard-write'], {origin: base});
    context.on('page', page => page.on('pageerror', error => pageErrors.push(error.message)));
    context.on('request', request => { if (/review-editor|review-syntax/.test(request.url())) editorRequests.push(request.url()); });
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
    assert.equal(editorRequests.length, 0, 'Repository overview eagerly loaded comparison editor assets');
    await card.locator('[data-review-branch]').click();
    await page.locator('.repository-comparison-stats').waitFor();
    await page.locator('.repository-file-tree').first().waitFor();
    const review = new URL(page.url()).searchParams.get('review');
    const comparison = await get('comparison', {review});
    urls.branchDetails = page.url();
    assert.equal(new URL(page.url()).searchParams.has('file'), false, 'Branch opening inserted an automatic file selection');
    assert(await page.locator('.repository-file-scroll').evaluate(node => node.scrollTop < 2), 'Branch opening skipped comparison details');
    assert.equal(await page.locator('.repository-file-scroll > .repository-comparison-details .repository-comparison-stats').count(), 1);
    assert.equal(await page.locator('.repository-review-heading .repository-comparison-stats').count(), 0);
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
      assert(values.length >= 2, 'Expected comparison totals and file-header statistics');
      assert(values.every(value => value.color === color && value.text.startsWith(prefix)), 'Statistics lost their color or sign');
    }
    const navigator = page.locator('.repository-file-list');
    assert.equal(await navigator.locator('.repository-file-counts, .repository-additions, .repository-deletions, .codex-copy-button').count(), 0,
      'Navigator still contains line statistics or copy controls');
    assert.equal(await navigator.locator(':scope > p').count(), 0, 'Navigator still repeats comparison totals');
    const rows = await navigator.locator('.repository-file-row').evaluateAll(nodes => nodes.map(node => {
      const name = node.querySelector('.repository-file-path');
      const status = node.querySelector('.repository-file-status');
      const style = getComputedStyle(name);
      const rect = name.getBoundingClientRect(), statusRect = status.getBoundingClientRect();
      return {whiteSpace: style.whiteSpace, overflow: style.overflow, textOverflow: style.textOverflow,
        height: rect.height, lineHeight: Number.parseFloat(style.lineHeight), top: rect.top, statusTop: statusRect.top};
    }));
    assert(rows.every(row => row.whiteSpace === 'nowrap' && row.overflow === 'hidden' && row.textOverflow === 'ellipsis'),
      'File names must use one-line ellipsis truncation');
    assert(rows.every(row => !Number.isFinite(row.lineHeight) || row.height <= row.lineHeight + 1), 'A filename spans two lines');
    assert(rows.every(row => Math.abs(row.top - row.statusTop) <= 4), 'Filename and status are not on the same row');
    const summaries = navigator.locator('.repository-directory > summary');
    const icons = await summaries.evaluateAll(nodes => nodes.map(node => {
      const visible = [...node.querySelectorAll('svg')].filter(icon => {
        const style = getComputedStyle(icon); return style.display !== 'none' && style.visibility !== 'hidden';
      });
      return {count: visible.length, hidden: visible.map(icon => icon.getAttribute('aria-hidden')), color: visible.map(icon => getComputedStyle(icon).color),
        summaryColor: getComputedStyle(node).color};
    }));
    assert(icons.every(icon => icon.count === 1 && icon.hidden[0] === 'true' && icon.color[0] === icon.summaryColor),
      'Every directory must show one decorative, theme-colored folder icon');
    checks.push('branch opens at scrolling comparison details without an automatic file route', 'live branch with expanded nested tree',
      'single-line accessible colored statuses and filename ellipsis', 'navigator has no statistics or copy controls',
      'decorative theme-colored directory icons', 'colored comparison and file-header statistics');

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
    await section.getByRole('button', {name: 'Copy file path', exact: true}).click();
    assert.equal(await page.evaluate(() => navigator.clipboard.readText()), file.path);
    assert.equal(page.url(), beforeCopy, 'Header path copy navigated');
    urls.branch = page.url();
    await page.screenshot({path: output + '/repository-compact-desktop.png'});
    checks.push('syntax colors retained', 'repository-relative path copied through native clipboard from file header');

    const summary = directory.locator(':scope > summary');
    const visibleFolder = () => summary.locator('svg:visible').evaluate(node => [...node.querySelectorAll('path')]
      .filter(path => getComputedStyle(path).display !== 'none' && getComputedStyle(path).visibility !== 'hidden')
      .map(path => path.getAttribute('d')).join('|'));
    const openFolder = await visibleFolder();
    await summary.focus();
    await page.keyboard.press('Enter');
    assert.equal(await directory.getAttribute('open'), null);
    const closedFolder = await visibleFolder();
    assert.notEqual(closedFolder, openFolder, 'Closed directory kept its open-folder appearance');
    assert.equal(await nav.isVisible(), false);
    assert.equal(await section.isVisible(), true, 'Collapsing navigation hid the diff');
    await page.getByRole('button', {name: 'Unified', exact: true}).click();
    assert.equal(await directory.getAttribute('open'), null, 'Layout change expanded a collapsed directory');
    await summary.focus();
    await page.keyboard.press('Space');
    assert.equal(await directory.evaluate(node => node.open), true);
    assert.equal(await visibleFolder(), openFolder, 'Reopening did not restore the open-folder icon');
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
    checks.push('directory collapse, changing folder icons and native Enter/Space controls', 'collapse preserved during layout changes', 'Back/Forward reveals selected file ancestors');

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
        await page.screenshot({path: output + '/repository-compact-full-file-back.png'});
      }
      await back.click();
      assert.equal(page.url(), backURL.href);
      await section.locator('.cm-editor').first().waitFor();
      assert.equal(await back.isVisible(), false);
      const anchoredDiff = new URL(backURL.href); anchoredDiff.hash = version + '-L' + line;
      await page.goto(anchoredDiff.href, {waitUntil: 'domcontentloaded'});
      const anchor = section.locator('.cm-gutters a[href$="#' + version + '-L' + line + '"]').first();
      await anchor.waitFor();
      await page.waitForFunction(({id, side, line}) => {
        const pane = document.querySelector('.repository-file-scroll').getBoundingClientRect();
        const anchor = document.querySelector('.repository-file-section[data-file-id="' + id + '"] .cm-gutters a[href$="#' + side + '-L' + line + '"]');
        if (!anchor) return false;
        const rect = anchor.getBoundingClientRect();
        return rect.top >= pane.top - 1 && rect.bottom <= pane.bottom + 1;
      }, {id: file.id, side: version, line});
      assert.equal(page.url(), anchoredDiff.href, 'Cold diff line route changed');
    }
    checks.push('explicit cold unified and split diff line links reveal their lines', 'Before/unified and After/split cold full-file links', 'back arrow position and exact frozen diff routes');

    await page.getByRole('button', {name: 'Unified', exact: true}).click();
    const headURL = parentURL(page.url(), observedHead);
    const headData = await get('comparison', {review, commit: observedHead});
    await page.goto(headURL.href, {waitUntil: 'domcontentloaded'});
    await page.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, headData.commit.message);
    assert(headData.commit.parents.length > 0, 'Expected a non-root runtime head');
    assert.equal(new URL(page.url()).searchParams.has('file'), false, 'Commit opening inserted an automatic file selection');
    assert(await page.locator('.repository-file-scroll').evaluate(node => node.scrollTop < 2), 'Commit opening skipped its message');
    assert.equal(await page.locator('.repository-review-heading .repository-commit-full-message, .repository-review-heading .repository-commit-detail-identity, .repository-review-heading .repository-commit-parents').count(), 0);
    assert.equal(await page.locator('.repository-file-scroll > .repository-comparison-details .repository-commit-full-message').count(), 1);
    const toolbar = page.locator('.repository-review-heading');
    for (const label of ['← Repositories', 'Copy comparison link', 'Split', 'Unified']) {
      assert.equal(await toolbar.getByRole('button', {name: label, exact: true}).count(), 1, 'Toolbar lost ' + label);
    }
    checks.push('commit opens with complete message at the top of the diff pane', 'compact persistent toolbar contains only navigation and identity controls');
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
      assert(await page.locator('.repository-file-scroll').evaluate(node => node.scrollTop < 2), 'Parent opening skipped its message');
      return expectedPage;
    };
    const parent = await followParent(headData.commit.parents[0]);
    urls.parent = page.url();
    await page.screenshot({path: output + '/repository-compact-parent-commit.png'});
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
    const longData = await get('comparison', {review, commit: longCommit});
    assert(longData.commit.message.split('\n').length >= 18, 'Historical commit is not long enough to exercise message scrolling');
    const longURL = parentURL(page.url(), longCommit);
    await page.goto(longURL.href, {waitUntil: 'domcontentloaded'});
    await page.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, longData.commit.message);
    const scroll = page.locator('.repository-file-scroll');
    await waitForScrollableDetails(page);
    const beforeScroll = await page.evaluate(() => {
      const details = document.querySelector('.repository-comparison-details'), message = details.querySelector('.repository-commit-full-message');
      const pane = document.querySelector('.repository-file-scroll'), toolbar = document.querySelector('.repository-review-heading');
      const style = getComputedStyle(message);
      return {messageHeight: message.getBoundingClientRect().height, messageScrollHeight: message.scrollHeight,
        messageClientHeight: message.clientHeight, maxHeight: style.maxHeight, overflowY: style.overflowY,
        paneHeight: pane.clientHeight, detailsHeight: details.offsetHeight, toolbarTop: toolbar.getBoundingClientRect().top,
        toolbarHeight: toolbar.getBoundingClientRect().height, scrollTop: pane.scrollTop};
    });
    assert.equal(beforeScroll.maxHeight, 'none', 'Full commit message still has a height cap');
    assert(!['scroll', 'auto'].includes(beforeScroll.overflowY), 'Full commit message still has an independent scrollbar');
    assert(beforeScroll.messageScrollHeight <= beforeScroll.messageClientHeight + 2, 'Message content is clipped');
    assert(beforeScroll.scrollTop < 2, 'Long commit opening did not start at its message');
    assert(beforeScroll.toolbarHeight < 120, 'Desktop toolbar is not compact');
    await page.screenshot({path: output + '/repository-compact-long-message.png'});
    const paneBox = await scroll.boundingBox();
    await page.mouse.move(paneBox.x + paneBox.width / 2, paneBox.y + paneBox.height / 2);
    await page.mouse.wheel(0, beforeScroll.detailsHeight + 250);
    await page.waitForFunction(() => {
      const details = document.querySelector('.repository-comparison-details').getBoundingClientRect();
      const pane = document.querySelector('.repository-file-scroll').getBoundingClientRect();
      return details.bottom <= pane.top + 1;
    });
    const afterScroll = await page.evaluate(() => ({
      toolbarTop: document.querySelector('.repository-review-heading').getBoundingClientRect().top,
      toolbarHeight: document.querySelector('.repository-review-heading').getBoundingClientRect().height,
      scrollTop: document.querySelector('.repository-file-scroll').scrollTop,
      detailsBottom: document.querySelector('.repository-comparison-details').getBoundingClientRect().bottom,
      paneTop: document.querySelector('.repository-file-scroll').getBoundingClientRect().top,
    }));
    assert(Math.abs(beforeScroll.toolbarTop - afterScroll.toolbarTop) < 1, 'Scrolling the commit moved its toolbar');
    assert.equal(beforeScroll.toolbarHeight, afterScroll.toolbarHeight);
    assert(afterScroll.scrollTop > beforeScroll.detailsHeight, 'Diff pane did not scroll past all comparison details');
    scrollGeometry = {commit: longCommit, messageLines: longData.commit.message.split('\n').length, before: beforeScroll, after: afterScroll};
    urls.longCommit = longURL.href;
    await page.screenshot({path: output + '/repository-compact-scrolled-diff.png'});
    checks.push('long real commit message has no independent cap or scrollbar', 'mouse-wheel scrolling moves all details away while compact toolbar stays visible');

    await page.goto(urls.branchDetails, {waitUntil: 'domcontentloaded'});
    await page.locator('.repository-file-tree').first().waitFor();
    const visit = comparison.files.filter(item => item.oldMode !== '160000' && item.newMode !== '160000').slice(0, 11);
    assert(visit.length > 8, 'Live branch needs more than eight files to exercise editor retention');
    for (const item of visit) {
      await page.locator(fileSelector(item.id)).click();
      await page.locator(sectionSelector(item.id)).locator('.review-code-view').first().waitFor();
      await page.waitForFunction(() => document.querySelectorAll('.review-code-view').length <= 8);
      const retained = await page.locator('.review-code-view').count();
      retainedEditors.push({file: item.path, retained});
      assert(retained > 0 && retained <= 8, 'Comparison exceeded its eight-file retained editor limit');
    }
    assert(editorRequests.some(url => /review-editor/.test(url)), 'No lazy editor request was observed');
    checks.push('editor assets load only after a comparison opens', 'eight-file editor retention bound during live file navigation');

    await page.setViewportSize({width: 390, height: 844});
    await page.goto(urls.branch, {waitUntil: 'domcontentloaded'});
    await page.locator('.repository-file-tree').first().waitFor();
    await section.locator('.cm-editor').first().waitFor();
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), 'Mobile document overflows horizontally');
    assert.equal(await page.locator('[contenteditable="true"]').count(), 0);
    await page.waitForFunction(id => ![...document.querySelectorAll('.repository-file-section[data-file-id=\"' + id + '\"] .review-syntax-status')].some(node => node.textContent === 'Highlighting…'), file.id);
    await page.screenshot({path: output + '/repository-compact-mobile.png'});
    const mobileGeometry = await page.evaluate(() => {
      const tree = document.querySelector('.repository-file-list').getBoundingClientRect();
      const pane = document.querySelector('.repository-file-scroll').getBoundingClientRect();
      return {treeBottom: tree.bottom, paneTop: pane.top};
    });
    assert(mobileGeometry.treeBottom <= mobileGeometry.paneTop + 1, 'Mobile navigator is not stacked above the diff');
    assert.equal(await page.locator('.repository-file-list .codex-copy-button, .repository-file-list .repository-file-counts').count(), 0);
    await page.goto(longURL.href, {waitUntil: 'domcontentloaded'});
    await page.waitForFunction(message => document.querySelector('.repository-commit-full-message')?.textContent === message, longData.commit.message);
    assert(await page.locator('.repository-file-scroll').evaluate(node => node.scrollTop < 2), 'Mobile commit skipped its message');
    assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), 'Mobile commit message overflows horizontally');
    const mobileScroll = page.locator('.repository-file-scroll');
    await waitForScrollableDetails(page);
    const mobileBox = await mobileScroll.boundingBox();
    const mobileDetails = await page.locator('.repository-comparison-details').evaluate(node => node.offsetHeight);
    await page.mouse.move(mobileBox.x + mobileBox.width / 2, mobileBox.y + mobileBox.height / 2);
    await page.mouse.wheel(0, mobileDetails + 150);
    await page.waitForFunction(() => document.querySelector('.repository-comparison-details').getBoundingClientRect().bottom <= document.querySelector('.repository-file-scroll').getBoundingClientRect().top + 1);
    assert(await page.locator('.repository-review-heading').isVisible());
    await page.screenshot({path: output + '/repository-compact-mobile-scrolled.png'});
    checks.push('390px mobile tree and read-only editors', 'mobile commit details scroll away below the persistent toolbar');
    assert.deepEqual(pageErrors, []);
    assert.deepEqual(cspViolations, []);
    checks.push('zero page errors or CSP violations across navigations');
    const result = {passed: true, elapsedSeconds: (Date.now() - started) / 1000, expectedHead, observedHead, savedBase, selectedPath,
      observedStatuses: [...new Set(statuses.map(status => status.text))].sort(), scrollGeometry, retainedEditors, checks, urls,
      limitations: ['TLS trust is checked separately; the browser context ignores certificate errors.',
        'No live Git refs or conversation state were changed; edge-case statuses and merge/root fixtures are covered by component and Go tests.']};
    fs.writeFileSync(output + '/compact-live-browser-results.json', JSON.stringify(result, null, 2) + '\n');
    console.log(JSON.stringify({passed: true, elapsedSeconds: result.elapsedSeconds, checks: checks.length, observedHead, output}));
  } catch (error) {
    fs.writeFileSync(output + '/compact-live-browser-results.json', JSON.stringify({passed: false, elapsedSeconds: (Date.now() - started) / 1000,
      expectedHead, observedHead, savedBase, selectedPath, checks, urls, error: error.message, pageErrors, cspViolations}, null, 2) + '\n');
    throw error;
  } finally {
    await browser.close();
  }
})().catch(error => {console.error(error); process.exitCode = 1;});
