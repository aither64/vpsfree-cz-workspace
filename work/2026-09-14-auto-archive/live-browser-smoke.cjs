"use strict";
const fs = require("node:fs");
const path = require("node:path");
const tls = require("node:tls");
const {X509Certificate, createHash} = require("node:crypto");
const {chromium, expect} = require("@playwright/test");

(async () => {
  const host = "vpsfree-cz.workspace.aitherdev.int.vpsfree.cz";
  const slug = "2026-09-14-auto-archive";
  const leaf = await new Promise((resolve, reject) => {
    const socket = tls.connect({host, servername: host, port: 443,
      ca: fs.readFileSync("/var/lib/dev-workspaces/public/ca.pem")}, () => {
      resolve(new X509Certificate(socket.getPeerCertificate().raw));
      socket.end();
    });
    socket.on("error", reject);
  });
  const pin = createHash("sha256").update(leaf.publicKey.export({type: "spki", format: "der"})).digest("base64");
  const browser = await chromium.launch({headless: true, channel: "chromium",
    args: ["--ignore-certificate-errors-spki-list=" + pin]});
  try {
    const page = await browser.newPage({httpCredentials: {username: "aither",
      password: fs.readFileSync("/var/lib/dev-workspaces/password/password", "utf8").trim()}});
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    await page.route("**/*", route => {
      if (!["GET", "HEAD"].includes(route.request().method())) return route.abort();
      return route.continue();
    });
    const response = await page.goto(`https://${host}/${slug}/`);
    expect(response.status()).toBe(200);
    await page.locator("#auto-archive-panel summary").click();
    await expect(page.locator("#auto-archive-status")).toContainText("conversation identity");
    const ownStatus = await page.locator("#auto-archive-status").innerText();
    // A shell-only initiative has no activity identity. Inspect a normal session
    // read-only; hold/release writes are covered by isolated contract tests.
    const observedSlug = process.env.AUTO_ARCHIVE_OBSERVED_SESSION;
    expect(observedSlug).toMatch(/^20[0-9-]+[a-z0-9-]+$/);
    await page.goto(`https://${host}/${observedSlug}/`);
    await page.locator("#auto-archive-panel summary").click();
    await expect(page.locator("#auto-archive-hold")).toBeEnabled();
    expect(errors).toEqual([]);
    const result = {url: page.url(), tlsVerified: true, readOnly: true,
      ownShellSessionStatus: ownStatus, pageErrors: errors,
      status: await page.locator("#auto-archive-status").innerText()};
    fs.writeFileSync(path.join(__dirname, "live-browser-results.json"), JSON.stringify(result, null, 2) + "\n");
    await page.locator("#auto-archive-panel").screenshot({path: path.join(__dirname, "auto-archive-portal.png")});
    console.log(JSON.stringify(result));
  } finally {
    await browser.close();
  }
})().catch(error => {console.error(error); process.exitCode = 1;});
