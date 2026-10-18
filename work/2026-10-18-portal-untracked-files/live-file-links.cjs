"use strict";
const assert = require("node:assert/strict");
const crypto = require("node:crypto");
const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const {chromium} = require(process.env.PLAYWRIGHT_MODULE);
const workspace = "/home/aither/workspace/ai/vpsfree.cz";
const slug = "2026-10-18-portal-untracked-files";
const records = path.join(workspace, "work", slug);
const socketPath = "/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock";
const fixtureRoots = [workspace, path.join(records), path.join(workspace, "worktrees", slug, "workspace")];
const created = [];
const directories = [];
const results = [];
let browser, server;
const hash = text => crypto.createHash("sha256").update(text).digest("hex");
(async () => {
  for (const root of fixtureRoots) {
    const directory = path.join(root, ".portal-file-link-acceptance");
    fs.mkdirSync(directory);
    directories.push(directory);
    for (const [name, text] of [[".gitignore", "/ignored.md\n"], ["visible.md", "# Portal untracked acceptance\nSynthetic visible fixture.\n"], ["ignored.md", "Synthetic ignored fixture.\n"]]) {
      const namePath = path.join(directory, name);
      fs.writeFileSync(namePath, text, {flag: "wx"});
      created.push({path: namePath, text});
    }
  }
  server = http.createServer((request, response) => {
    if (!["GET", "HEAD"].includes(request.method)) {
      response.writeHead(405); response.end(); return;
    }
    const upstream = http.request({socketPath, path: request.url, method: request.method, headers: {...request.headers, host: "localhost"}}, result => {
      response.writeHead(result.statusCode, result.headers);
      result.pipe(response);
    });
    upstream.on("error", () => { response.writeHead(502); response.end("Portal proxy failed"); });
    request.pipe(upstream);
  });
  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  browser = await chromium.launch({executablePath: process.env.CHROMIUM_EXECUTABLE, headless: true, args: ["--no-sandbox", "--disable-dev-shm-usage"]});
  const context = await browser.newContext({viewport: {width: 1280, height: 800}, permissions: ["clipboard-read", "clipboard-write"]});
  const page = await context.newPage();
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  const rustPlan = path.join(workspace, "work", "2026-10-17-confctl-rust-rewrite-plan", "design.md");
  const targets = [{path: rustPlan, source: "artifact"}, ...directories.map((directory, index) => ({path: path.join(directory, "visible.md"), source: ["workspace", "artifact", "worktree"][index]}))];
  for (const [index, target] of targets.entries()) {
    await page.goto(base + encodeURI(target.path) + ":1", {waitUntil: "networkidle"});
    await page.waitForSelector("#source-file-content .cm-editor");
    assert.equal(new URL(page.url()).hash, "#L1");
    assert.equal(await page.locator("#source-file-notice").isHidden(), true);
    const url = new URL(page.url());
    const api = url.pathname === "/workspace-files" ? "/api/workspace/file" : `/api/sessions/${url.pathname.split("/").pop()}/file`;
    const response = await fetch(base + api + url.search);
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("cache-control"), "no-store");
    const file = await response.json();
    assert.equal(file.source, target.source);
    assert.equal(file.content.text, fs.readFileSync(target.path, "utf8"));
    assert.match(await page.locator("#source-file-version").textContent(), /Current/);
    if (index === 0) {
      assert.equal(await page.locator("#source-file-title").textContent(), "design.md");
      await page.screenshot({path: path.join(records, "live-rust-plan.png"), fullPage: false});
      await page.locator("#source-file-copy").click();
      assert.equal(await page.evaluate(() => navigator.clipboard.readText()), page.url());
    }
    results.push({path: target.path, status: response.status, source: file.source, sha256: hash(file.content.text), viewer: true, lineAnchor: true});
  }
  for (const [index, directory] of directories.entries()) {
    await page.goto(base + encodeURI(path.join(directory, "ignored.md")), {waitUntil: "networkidle"});
    await page.waitForFunction(() => document.getElementById("source-file-notice")?.textContent.includes("This file is unavailable"));
    assert.equal(await page.locator("#source-file-content .cm-editor").count(), 0);
    const url = new URL(page.url());
    const api = url.pathname === "/workspace-files" ? "/api/workspace/file" : `/api/sessions/${url.pathname.split("/").pop()}/file`;
    const response = await fetch(base + api + url.search);
    assert.equal(response.status, 404);
    results.push({root: fixtureRoots[index], ignoredStatus: response.status, viewerDenied: true});
  }
  assert.deepEqual(errors, []);
  const result = {result: "passed", originalLink: rustPlan, checkedAt: new Date().toISOString(), checks: results};
  fs.writeFileSync(path.join(records, "live-file-links-result.json"), JSON.stringify(result, null, 2) + "\n");
  console.log(JSON.stringify(result));
})().catch(error => { console.error(error.stack); process.exitCode = 1; }).finally(async () => {
  if (browser) await browser.close();
  if (server) await new Promise(resolve => server.close(resolve));
  for (const file of created.reverse()) {
    if (fs.existsSync(file.path) && fs.readFileSync(file.path, "utf8") === file.text) fs.unlinkSync(file.path);
  }
  for (const directory of directories.reverse()) {
    if (fs.existsSync(directory) && fs.readdirSync(directory).length === 0) fs.rmdirSync(directory);
  }
});
