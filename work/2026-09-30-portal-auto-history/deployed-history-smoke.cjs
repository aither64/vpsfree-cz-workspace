"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const {chromium} = require(process.env.PLAYWRIGHT_MODULE);

const baseURL = process.env.PORTAL_BASE_URL;
const passwordFile = process.env.PORTAL_PASSWORD_FILE;
const executablePath = process.env.CHROMIUM_EXECUTABLE;
const sessionSlug = process.env.PORTAL_SESSION_SLUG || "2026-09-27-newadmin-integration";

if (!baseURL || !passwordFile || !executablePath) {
  throw new Error("Set PORTAL_BASE_URL, PORTAL_PASSWORD_FILE and CHROMIUM_EXECUTABLE");
}

(async () => {
  const browser = await chromium.launch({headless: true, executablePath, args: ["--no-sandbox"]});
  try {
    const context = await browser.newContext({
      viewport: {width: 1600, height: 1000},
      ignoreHTTPSErrors: true,
      httpCredentials: {
        username: "aither",
        password: fs.readFileSync(passwordFile, "utf8").trim(),
      },
    });
    const page = await context.newPage();
    const pageErrors = [];
    let cursorReads = 0;
    page.on("pageerror", error => pageErrors.push(error.message));
    page.on("response", response => {
      const url = new URL(response.url());
      if (url.pathname.endsWith("/thread/page") && url.searchParams.has("cursor")) cursorReads++;
    });

    await page.goto(`${baseURL}/${encodeURIComponent(sessionSlug)}/#codex`, {
      waitUntil: "domcontentloaded",
      timeout: 30_000,
    });
    await page.locator("#transcript .message").first().waitFor({timeout: 30_000});
    await page.waitForFunction(() => document.querySelector("#codex-status")?.textContent.trim() !== "Connecting", null,
      {timeout: 30_000});
    assert.equal(await page.locator("#load-older").count(), 0, "persistent Load older control must be absent");

    await page.locator("#transcript").hover();
    await page.waitForTimeout(150);
    const initialMessages = await page.locator("#transcript .message").count();
    const geometry = await page.locator("#transcript").evaluate(node => {
      node.scrollTop = 260;
      return {clientHeight: node.clientHeight, scrollHeight: node.scrollHeight, scrollTop: node.scrollTop};
    });
    assert(geometry.scrollHeight > geometry.clientHeight + 260, "target conversation must provide a scrollable first page");
    assert.equal(geometry.scrollTop, 260, "history smoke must begin above the automatic-load threshold");
    await page.waitForTimeout(50);
    assert.equal(cursorReads, 0, "programmatic positioning must not request history");

    const olderResponse = page.waitForResponse(response => {
      const url = new URL(response.url());
      return url.pathname.endsWith("/thread/page") && url.searchParams.has("cursor");
    }, {timeout: 30_000});
    await page.mouse.wheel(0, -120);
    const response = await olderResponse;
    assert(response.ok(), `older-page response failed with HTTP ${response.status()}`);
    await page.waitForTimeout(500);
    assert.equal(cursorReads, 1, "one upward action must request exactly one older page");
    assert((await page.locator("#transcript .message").count()) >= initialMessages,
      "loading history must not remove visible messages");
    assert.deepEqual(pageErrors, []);

    console.log(JSON.stringify({
      passed: true,
      sessionSlug,
      initialMessages,
      finalMessages: await page.locator("#transcript .message").count(),
      cursorReads,
      loadOlderControls: await page.locator("#load-older").count(),
    }));
  } finally {
    await browser.close();
  }
})().catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
