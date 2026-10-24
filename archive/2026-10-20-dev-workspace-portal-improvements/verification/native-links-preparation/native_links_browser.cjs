"use strict";
const assert = require("node:assert/strict");
const {chromium, expect} = require("@playwright/test");
const baseURL = process.argv[2];
(async () => {
  const browser = await chromium.launch({headless:true, channel:"chromium", args:["--ignore-certificate-errors"]});
  try {
    const context = await browser.newContext({ignoreHTTPSErrors:true, viewport:{width:1440,height:850}});
    const page = await context.newPage(), errors = [];
    page.on("pageerror", error => errors.push(error.message));
    const transcript = await (await context.request.get(baseURL + "/fixture/presentation")).json();
    await page.route("**/api/sessions/example/**", route => {
      const operation = new URL(route.request().url()).pathname.split("/").at(-1);
      if (["page","thread"].includes(operation)) return route.fulfill({json:transcript});
      return route.continue();
    });
    await page.goto(baseURL + "/example/");
    const link = page.locator("#transcript a").filter({hasText:"Plan"});
    await expect(link).toHaveCount(1);
    await expect(link).toHaveAttribute("href", "/files/example?artifact=plan.md#L1");
    await expect(link).toHaveAttribute("target", "_blank");
    const rel = (await link.getAttribute("rel")).split(/\s+/);
    assert(rel.includes("noopener") && rel.includes("noreferrer"));
    const expected = new URL(await link.getAttribute("href"), baseURL).href;
    const originalURL = page.url(), originalPages = context.pages().length;

    // Retain the actual event and inspect it after dispatch, including any
    // later bubbling listener's cancellation. Do not synthesize an event.
    await page.evaluate(() => document.addEventListener("contextmenu", event => {
      if (event.target.closest('#transcript a[href="/files/example?artifact=plan.md#L1"]')) window.nativeLinkContextEvent = event;
    }, {capture:true}));
    await link.click({button:"right"});
    const menuEvent = await page.evaluate(() => {
      const event = window.nativeLinkContextEvent;
      return event ? {trusted:event.isTrusted, canceled:event.defaultPrevented, button:event.button,
        href:event.target.closest("a").href} : null;
    });
    assert.deepEqual(menuEvent, {trusted:true,canceled:false,button:2,href:expected});
    assert.equal(page.url(), originalURL); assert.equal(context.pages().length, originalPages);
    await page.keyboard.press("Escape");

    const completed = [];
    const openViewer = async (name, action) => {
      const [viewer] = await Promise.all([context.waitForEvent("page"), action()]);
      await viewer.waitForURL(expected);
      await expect(viewer.locator("#source-file-title")).toHaveText("plan.md");
      await expect(viewer.locator("#source-file-copy-content")).toBeEnabled();
      await expect(viewer.locator("#source-file-content")).toContainText("# Plan");
      assert.equal(new URL(viewer.url()).hash, "#L1");
      assert.equal(await viewer.evaluate(() => window.opener), null);
      assert.equal(page.url(), originalURL);
      completed.push({action:name,url:viewer.url(),originalUnchanged:true});
      await viewer.close(); await page.bringToFront();
    };
    await openViewer("standard click", () => link.click());
    await openViewer("Ctrl-click (Linux)", () => link.click({modifiers:["Control"]}));
    await link.focus(); await expect(link).toBeFocused();
    await openViewer("keyboard Enter", () => link.press("Enter"));
    assert.deepEqual(errors, []);
    console.log(JSON.stringify({contextmenu:menuEvent,completed,
      nativeMenuItemSelection:"UNTESTED: headless browser exposes the contextmenu event, not OS menu item selection"}));
  } finally { await browser.close(); }
})().catch(error => {console.error(error);process.exitCode=1;});
