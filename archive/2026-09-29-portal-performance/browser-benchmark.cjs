const {chromium} = require(process.env.PLAYWRIGHT_MODULE);
const fs = require('node:fs');

const baseURL = process.env.PORTAL_BASE_URL;
const passwordFile = process.env.PORTAL_PASSWORD_FILE;
const chromiumExecutable = process.env.CHROMIUM_EXECUTABLE;
const sessionSlug = process.env.PORTAL_SESSION_SLUG || '2026-09-27-newadmin-integration';
const runCount = Number(process.env.PORTAL_BENCHMARK_RUNS || '30');
const maxUsableMs = Number(process.env.PORTAL_BENCHMARK_MAX_MS || '2000');

if (!baseURL || !passwordFile || !chromiumExecutable || !Number.isInteger(runCount) || runCount < 1 ||
    !Number.isFinite(maxUsableMs) || maxUsableMs <= 0) {
  throw new Error('Set PORTAL_BASE_URL, PORTAL_PASSWORD_FILE, CHROMIUM_EXECUTABLE and positive benchmark limits');
}

const percentile = (values, percentage) => {
  const ordered = [...values].sort((left, right) => left - right);
  return ordered[Math.ceil(ordered.length * percentage) - 1];
};

(async () => {
  const browser = await chromium.launch({
    executablePath: chromiumExecutable,
    headless: true,
    args: ['--no-sandbox'],
  });
  try {
    const context = await browser.newContext({
      viewport: {width: 1600, height: 1000},
      ignoreHTTPSErrors: true,
      httpCredentials: {
        username: 'aither',
        password: fs.readFileSync(passwordFile, 'utf8').trim(),
      },
    });
    const samples = [];
    for (let run = 1; run <= runCount; run++) {
      const page = await context.newPage();
      const start = Date.now();
      const responses = {page: 0, legacy: 0, errors: 0};
      const pageErrors = [];
      page.on('pageerror', error => pageErrors.push(error.message.slice(0, 160)));
      page.on('response', response => {
        const pathname = new URL(response.url()).pathname;
        if (pathname.endsWith('/thread/page')) responses.page++;
        if (pathname.endsWith('/thread')) responses.legacy++;
        if (response.status() >= 400) responses.errors++;
      });
      const sample = {run};
      try {
        await page.goto(`${baseURL}/${encodeURIComponent(sessionSlug)}/#codex`, {
          waitUntil: 'domcontentloaded',
          timeout: 30000,
        });
        await page.locator('#transcript .message').first().waitFor({timeout: 30000});
        await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
        sample.recentPaintMs = Date.now() - start;
        await page.waitForFunction(() => {
          const composer = document.querySelector('#message-form textarea');
          const status = document.querySelector('#codex-status');
          return composer && !composer.disabled && status && status.textContent.trim() !== 'Connecting';
        }, null, {timeout: 30000});
        sample.controlsReadyMs = Date.now() - start;
        sample.usableMs = Math.max(sample.recentPaintMs, sample.controlsReadyMs);
        sample.messageCount = await page.locator('#transcript .message').count();
      } catch (error) {
        sample.failedMs = Date.now() - start;
        sample.error = error.message.split('\n')[0].slice(0, 160);
        sample.connectionState = (await page.locator('#conversation-connection').textContent().catch(() => '')).trim().slice(0, 160);
        sample.transcriptState = (await page.locator('#transcript .empty').textContent().catch(() => '')).trim().slice(0, 160);
      }
      sample.pageErrors = pageErrors;
      Object.assign(sample, responses);
      samples.push(sample);
      console.log(JSON.stringify(sample));
      await page.close();
    }
    const successful = samples.filter(sample => sample.usableMs !== undefined);
    const p95UsableMs = successful.length === runCount ? percentile(successful.map(sample => sample.usableMs), 0.95) : null;
    const passed = p95UsableMs !== null && p95UsableMs <= maxUsableMs;
    console.log(JSON.stringify({
      browserVersion: browser.version(),
      viewport: '1600x1000',
      sessionSlug,
      cachePolicy: 'one context, new page per run',
      runs: runCount,
      failures: runCount - successful.length,
      maxUsableMs,
      passed,
      p95UsableMs,
      p95RecentPaintMs: successful.length === runCount ? percentile(successful.map(sample => sample.recentPaintMs), 0.95) : null,
      totalPageResponses: samples.reduce((count, sample) => count + sample.page, 0),
      totalLegacyResponses: samples.reduce((count, sample) => count + sample.legacy, 0),
      totalErrorResponses: samples.reduce((count, sample) => count + sample.errors, 0),
    }));
    if (!passed) process.exitCode = 1;
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
