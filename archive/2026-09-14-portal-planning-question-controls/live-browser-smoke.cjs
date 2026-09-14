"use strict";
const fs = require("node:fs");
const path = require("node:path");
const tls = require("node:tls");
const {X509Certificate, createHash} = require("node:crypto");
const {chromium, expect} = require("@playwright/test");
(async () => {
  const host = "vpsfree-cz.workspace.aitherdev.int.vpsfree.cz";
  // Validate the live leaf against the local CA before pinning it in Chromium.
  // The server omits the root CA, so Chromium cannot match that CA's SPKI.
  const leaf = await new Promise((resolve, reject) => {
    const socket = tls.connect({host, servername: host, port: 443, ca: fs.readFileSync("/var/lib/dev-workspaces/public/ca.pem")}, () => {
      resolve(new X509Certificate(socket.getPeerCertificate().raw));
      socket.end();
    });
    socket.on("error", reject);
  });
  const pin = createHash("sha256").update(leaf.publicKey.export({type: "spki", format: "der"})).digest("base64");
  const browser = await chromium.launch({headless: true, channel: "chromium", args: ["--ignore-certificate-errors-spki-list=" + pin]});
  try {
    const page = await browser.newPage({httpCredentials: {username: "aither", password: fs.readFileSync("/var/lib/dev-workspaces/password/password", "utf8").trim()}});
    const errors = [], mutations = [], assets = [];
    page.on("pageerror", e => errors.push(e.message));
    page.on("response", response => {
      const pathname = new URL(response.url()).pathname;
      if (pathname.startsWith("/static/") || pathname.startsWith("/codex/assets/")) assets.push({path: pathname, status: response.status()});
    });
    await page.route("**/*", route => {
      if (!["GET", "HEAD"].includes(route.request().method())) {
        mutations.push({method: route.request().method(), path: new URL(route.request().url()).pathname});
        return route.abort();
      }
      return route.continue();
    });
    const slug = path.basename(__dirname);
    const response = await page.goto("https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/" + slug + "/");
    expect(response.status()).toBe(200);
    await expect(page.locator("#handoff")).toBeVisible();
    await expect(page.locator("h1")).toHaveText(slug);
    await page.locator("#session-tab-repositories").click();
    await expect(page.locator("#repositories")).toBeVisible();
    await page.locator("#session-tab-handoff").click();
    await expect(page.locator("#handoff")).toBeVisible();
    expect(errors).toEqual([]);
    expect(mutations).toEqual([]);
    expect(assets.length).toBeGreaterThan(2);
    expect(assets.every(asset => asset.status === 200)).toBe(true);
    const results = {url: page.url(), status: response.status(), caVerifiedLeafPublicKey: true, pageErrors: errors, attemptedMutations: mutations, assets, tabs: "Handoff and Repositories passed", scope: "Read-only owned initiative page; question behavior is covered by the committed renderer fixture and exact deployed asset hashes."};
    fs.writeFileSync(path.join(__dirname, "live-browser-results.json"), JSON.stringify(results, null, 2) + "\n");
    console.log(JSON.stringify(results, null, 2));
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
