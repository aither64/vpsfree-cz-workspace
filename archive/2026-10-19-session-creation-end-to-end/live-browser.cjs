// Operational acceptance of the deployed forms and real model exchanges.
// This script creates only dedicated fixtures and never deletes any session.
"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const {randomUUID} = require("node:crypto");
const {execFileSync} = require("node:child_process");
const {chromium} = require(process.env.PLAYWRIGHT_MODULE);
const [action, label, optionsJSON = "{}"] = process.argv.slice(2);
const options = JSON.parse(optionsJSON);
const origin = "https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz";
const evidence = __dirname;
const file = path.join(evidence, `live-${label}.json`);
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
const instruction = marker => `This is an authorized disposable session-creation acceptance fixture. Do not edit files, run tools, delegate, or perform lifecycle actions. Respond with exactly ${marker} and nothing else. Remain idle after responding; an external browser owns verification.`;

(async () => {
  assert(["create", "fork", "plan", "finish"].includes(action));
  assert(/^[a-z0-9-]+$/.test(label));
  const password = execFileSync("ssh", ["-o", "BatchMode=yes", "-o", "ConnectTimeout=10",
    "root@172.16.106.40", "cat /var/lib/dev-workspaces/password/password"],
    {encoding: "utf8", timeout: 15000}).trim();
  const browser = await chromium.launch({executablePath: process.env.CHROMIUM_EXECUTABLE,
    headless: true, args: ["--no-sandbox", "--disable-dev-shm-usage"]});
  const context = await browser.newContext({ignoreHTTPSErrors: true,
    httpCredentials: {username: "aither", password}});
  const page = await context.newPage(), errors = [];
  page.on("pageerror", error => errors.push(error.message));
  let record, phase = action;
  const save = () => fs.writeFileSync(file, JSON.stringify(record, null, 2) + "\n");
  const get = async endpoint => {
    const response = await context.request.get(origin + endpoint);
    assert(response.ok(), `${endpoint}: ${response.status()}`);
    return response.json();
  };
  const statusPath = () => record.requestId ? `/api/session-creations/${record.requestId}` :
    `/api/sessions/${record.slug}/creation`;
  async function ready() {
    phase = "creation completion";
    const deadline = Date.now() + 300000;
    while (Date.now() < deadline) {
      const status = await get(statusPath());
      assert.equal(status.receiptId, record.receiptId);
      if (["ready", "failed", "paused", "conflict", "gone", "cancelled"].includes(status.state)) {
        Object.assign(record, status); save();
        assert.equal(status.state, "ready", JSON.stringify(status));
        return;
      }
      await sleep(500);
    }
    throw Error("creation completion deadline exceeded");
  }
  async function open(destination, slug) {
    const [hydrated] = await Promise.all([
      page.waitForResponse(r => r.request().method() === "GET" &&
        [`/api/sessions/${slug}/thread`, `/api/sessions/${slug}/thread/page`].includes(new URL(r.url()).pathname)),
      page.goto(origin + destination),
    ]);
    assert(hydrated.ok());
  }
  async function settings(form) {
    await form.locator("[name=provider]:not([disabled])").waitFor();
    await form.locator("[name=provider]").selectOption(options.provider || "");
    if (await form.locator("[name=team]").count()) {
      await form.locator("[name=team]").selectOption(options.team || "solo");
    }
    await form.locator("[name=model]:not([disabled])").waitFor();
    const available = await form.locator("[name=model] option").evaluateAll(nodes => nodes.map(n => n.value));
    assert(available.includes("gpt-6.1-sol"));
    await form.locator("[name=model]").selectOption("gpt-6.1-sol");
    await form.locator("[name=effort]").selectOption("high");
  }
  async function responseFor(marker) {
    const deadline = Date.now() + 180000;
    while (Date.now() < deadline) {
      const thread = await get(`/api/sessions/${record.slug}/thread`);
      const users = (thread.entries || []).filter(e => e.kind === "userMessage" && e.text?.includes(marker));
      assert(users.length <= 1, `duplicate user item for ${marker}`);
      if (users.length === 1) {
        const answer = thread.entries.find(e => e.kind === "agentMessage" &&
          e.turnId === users[0].turnId && e.turnStatus === "completed" && e.text.trim() === marker);
        if (answer) return {thread, turnId: users[0].turnId, status: answer.turnStatus};
        const failed = thread.entries.find(e => e.turnId === users[0].turnId && ["failed", "interrupted"].includes(e.turnStatus));
        assert(!failed, JSON.stringify(failed));
      }
      await sleep(500);
    }
    throw Error(`completed same-turn reply missing for ${marker}`);
  }
  async function usable() {
    await ready();
    record.destination = record.requestId ? record.canonicalUrl : record.url;
    assert.equal(record.destination, `/${record.slug}/`);
    if (![origin + record.url, origin + record.destination].includes(page.url())) {
      await page.goto(origin + record.url, {waitUntil: "commit"});
    }
    await page.waitForURL(origin + record.destination);
    await page.locator("body[data-thread-id]:not([data-thread-id=''])").waitFor();
    record.threadId = await page.locator("body").getAttribute("data-thread-id");
    assert(record.threadId); save();
    await open(record.destination, record.slug);
    if (record.kind !== "fork") record.initial = await responseFor(record.initialMarker);
    phase = "follow-up";
    record.followupMarker = `LIVE_FOLLOWUP_${randomUUID()}`; save();
    const before = await get(`/api/sessions/${record.slug}/thread`);
    assert(!before.entries.some(e => e.text?.includes(record.followupMarker)));
    await page.locator("#message-form textarea[name=message]").fill(instruction(record.followupMarker));
    await page.locator("#message-send:not([disabled])").waitFor();
    await page.locator("#message-send").click();
    record.followup = await responseFor(record.followupMarker);
    assert.equal(record.followup.thread.model, "gpt-6.1-sol");
    assert.equal(record.followup.thread.reasoningEffort, "high");
    assert.deepEqual(errors, []);
    record.verifiedAt = new Date().toISOString(); save();
    await page.reload();
    assert.equal(await page.locator("body").getAttribute("data-thread-id"), record.threadId);
    await ready();
  }
  try {
    if (action === "finish") {
      record = JSON.parse(fs.readFileSync(file));
      await usable();
    } else if (action === "create") {
      await page.goto(origin);
      const form = page.locator("#new-session-form");
      await form.locator("details summary").click();
      await settings(form);
      const initialMarker = `LIVE_INITIAL_${randomUUID()}`;
      await form.locator("[name=goal]").fill(instruction(initialMarker));
      if (!options.auto) await form.locator("[name=name]").fill(`creation-live-${label}`);
      const [accepted] = await Promise.all([
        page.waitForResponse(r => r.request().method() === "POST" && new URL(r.url()).pathname === "/sessions"),
        form.locator("button[type=submit]:not([disabled])").click(),
      ]);
      assert.equal(accepted.status(), 202);
      const requestId = new URLSearchParams(accepted.request().postData()).get("clientRequestId");
      record = {...await get(`/api/session-creations/${requestId}`), options, kind: "new", initialMarker};
      assert.equal(record.requestId, requestId); save();
      await usable();
    } else {
      const source = JSON.parse(fs.readFileSync(path.join(evidence, `live-${options.source}.json`)));
      assert(source.verifiedAt && source.threadId);
      await open(source.destination, source.slug);
      const initialMarker = `LIVE_PLAN_INITIAL_${randomUUID()}`;
      if (action === "plan") {
        await page.locator("#codex-mode").getByRole("button", {name: "Plan", exact: true}).click();
        await page.locator("#message-form textarea").fill(
          `Produce a proposed plan with a single implementation step: ${instruction(initialMarker)} Do not implement it yet. Put the plan in a proposed_plan block so I can approve it.`);
        await page.locator("#message-send:not([disabled])").click();
        await page.locator("#plan-implement-new").waitFor({state: "visible", timeout: 180000});
        await page.locator("#plan-implement-new").click();
      } else await page.locator("#fork-open:not([disabled])").click();
      const form = page.locator(action === "fork" ? "#fork-form" : "#plan-session-form");
      await settings(form);
      await form.locator("[name=name]").fill(`creation-live-${label}`);
      const [accepted] = await Promise.all([
        page.waitForResponse(r => r.request().method() === "POST" && new URL(r.url()).pathname ===
          `/api/sessions/${source.slug}/${action === "fork" ? "fork" : "implement-plan"}`),
        form.locator("button[type=submit]").click(),
      ]);
      assert.equal(accepted.status(), 202);
      const submitted = JSON.parse(accepted.request().postData());
      const slug = `${submitted.creationDate}-${submitted.name}`;
      record = {...await get(`/api/sessions/${slug}/creation`), options, submitted, kind: action, initialMarker,
        source: {slug: source.slug, threadId: source.threadId}}; save();
      await usable();
      assert.notEqual(record.threadId, source.threadId);
      const preserved = await get(`/api/sessions/${source.slug}/thread`);
      assert(preserved.entries.some(e => e.kind === "agentMessage" && e.text.trim() === source.followupMarker));
      record.sourcePreserved = true; save();
    }
    console.log(JSON.stringify({action, label, requestId: record.requestId, receiptId: record.receiptId,
      slug: record.slug, threadId: record.threadId, state: record.state, verifiedAt: record.verifiedAt}));
  } catch (error) {
    if (record) save();
    console.error(JSON.stringify({phase, errors, record: record && {slug: record.slug,
      requestId: record.requestId, receiptId: record.receiptId, state: record.state}}));
    throw error;
  } finally { await browser.close(); }
})().catch(error => {console.error(error); process.exitCode = 1;});
