"use strict";
const fs = require("node:fs"), cp = require("node:child_process"), crypto = require("node:crypto");
const {chromium} = require("/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules/@playwright/test");
const record = "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace";
const origin = "https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz", slug = "2026-10-14-i-d-like-the-dev-workspace";
const report = {sourceRevision: "6e1d9a191724d376cad2a71f234f0e4d1c01f36f", notificationOptInAttempted: false, settingsChanged: false};
function remote(command) {return cp.execFileSync("ssh", ["-o", "BatchMode=yes", "-o", "ConnectTimeout=8", "-o", "LogLevel=ERROR", "root@172.16.106.40", command], {encoding: "utf8", timeout: 15000, maxBuffer: 8192, stdio: ["ignore", "pipe", "pipe"]}).trim();}
(async () => {
  let browser;
  try {
    report.selectedPackageMatches = remote("readlink -f /home/aither/.local/state/dev-workspaces/profile") === "/nix/store/910f16dvr6wl65mb74mlrg623qs82s6q-dev-workspace-0.2.0";
    if (!report.selectedPackageMatches) throw new Error();
    const username = remote("cut -d: -f1 /var/lib/dev-workspaces/auth/htpasswd"), password = remote("cat /var/lib/dev-workspaces/password/password");
    browser = await chromium.launch({headless: true, channel: "chromium"});
    const context = await browser.newContext({ignoreHTTPSErrors: true, httpCredentials: {username, password, origin}});
    const page = await context.newPage();
    await page.goto(origin + "/" + slug + "/#settings", {timeout: 20000});
    await page.waitForFunction(() => !document.querySelector("#session-notifications-enabled")?.disabled && /(?:^| )R(?: |$)/.test(document.title), null, {timeout: 15000});
    Object.assign(report, await page.evaluate(slug => ({sessionIdentityMatches: document.body.dataset.session === slug,
      reservationTitleMarker: /(?:^| )R(?: |$)/.test(document.title), sessionPreferenceEnabled: !document.querySelector("#session-notifications-enabled").disabled,
      browserControlsPresent: Boolean(document.querySelector("#browser-notifications"))}), slug));
    const asset = await context.request.get(origin + "/static/session-attention.js", {timeout: 12000});
    const expected = cp.execFileSync("git", ["-C", record + "/../../worktrees/" + slug + "/dev-workspace", "show", report.sourceRevision + ":portal/internal/web/static/session-attention.js"]);
    report.servedAttentionAssetMatches = asset.status() === 200 && crypto.createHash("sha256").update(await asset.body()).digest("hex") === crypto.createHash("sha256").update(expected).digest("hex");
    await page.goto(origin + "/", {timeout: 20000});
    report.creationPreferenceDefaultEnabled = await page.locator('input[name="browserNotificationsEnabled"]').isChecked();
    report.passed = ["sessionIdentityMatches", "reservationTitleMarker", "sessionPreferenceEnabled", "browserControlsPresent", "servedAttentionAssetMatches", "creationPreferenceDefaultEnabled"].every(key => report[key] === true);
  } catch (_) {report.passed = false; report.error = "smoke_incomplete";}
  finally {
    if (browser) await browser.close().catch(() => {report.browserCloseUncertain = true;});
    fs.writeFileSync(record + "/deployed-ui-smoke-6e1d9a19.json", JSON.stringify(report, null, 2) + "\n", {mode: 0o600});
  }
  process.exitCode = report.passed ? 0 : 1;
})();
