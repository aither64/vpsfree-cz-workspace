"use strict";
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const {chromium, firefox} = require("@playwright/test");
const base = process.argv[2];
const resultPath = process.env.PROVIDER_PROBE_RESULT_FILE;
const origin = new URL(base).origin;
const safeResult = value => ["", "provider_accepted", "retrying", "provider_refused", "expired", "delivery_failed"].includes(value) ? value : "unknown";
const safeError = error => ["TimeoutError", "Error", "AbortError", "NotAllowedError", "NotSupportedError", "SecurityError"].includes(error?.name) ? error.name : "Error";
const report = {sourceRevision: "e414ed31806d2b91620d5e5fad8b5b5ee56e07ac", platform: process.platform, headless: true,
  providerTransport: "shipped_guardedPushClient_unmocked", syntheticPush: false, osDisplayVerified: false, macOSDisplayVerified: false, browsers: []};
const incomplete = "Browser setup is incomplete. Disable it or enable notifications again.";
function save() {
  if (resultPath) fs.writeFileSync(resultPath, JSON.stringify(report, null, 2) + "\n", {mode: 0o600});
}
async function summary(page) {
  return page.evaluate(async () => {
    const response = await fetch("/fixture/summary", {cache: "no-store"});
    const value = await response.json();
    return {registrations: value.registrations, pending: value.pending};
  });
}
async function deliveryEvidence(page) {
  return page.evaluate(async () => {
    const id = localStorage.getItem("workspace-browser-notifications.v1") || "";
    const response = await fetch(`/api/browser-notifications?registrationId=${encodeURIComponent(id)}`, {cache: "no-store"});
    const state = await response.json();
    const registration = await navigator.serviceWorker.getRegistration("/");
    const notifications = registration ? await registration.getNotifications() : [];
    // Read counts only; endpoint capabilities, keys, IDs and payloads never leave
    // this disposable browser profile or enter the result file.
    const receiptCount = await new Promise(resolve => {
      const open = indexedDB.open("workspace-session-attention", 1);
      open.onerror = () => resolve(null);
      open.onsuccess = () => {
        const db = open.result;
        if (!db.objectStoreNames.contains("sessions")) {db.close(); resolve(0); return;}
        const tx = db.transaction("sessions", "readonly");
        const read = tx.objectStore("sessions").getAll();
        read.onerror = () => {db.close(); resolve(null);};
        read.onsuccess = () => {const count = read.result.filter(record => record.event?.kind === "test").length; db.close(); resolve(count);};
      };
    });
    return {registered: Boolean(state.registered), result: state.result || "", workerTestRecords: receiptCount,
      notifications: notifications.length, testNotifications: notifications.filter(notification => notification.body === "Browser notification test").length};
  });
}
async function cleanup(context, row) {
  row.cleanup = "incomplete";
  try {
    let page = context.pages().find(page => page.url().startsWith(origin + "/"));
    if (!page) {page = await context.newPage(); await page.goto(`${base}/example/#settings`);}
    const button = page.locator("[data-notification-disable]");
    await page.waitForTimeout(1000);
    if (await button.isEnabled()) {
      await button.click();
      await page.waitForFunction(() => document.querySelector("[data-notification-status]")?.textContent.startsWith("Disabled on this browser."), null, {timeout: 12000});
    }
    row.localSubscriptionRemaining = await page.evaluate(async () => {
      const registration = await navigator.serviceWorker.getRegistration("/");
      const subscription = await registration?.pushManager.getSubscription();
      if (registration) (await registration.getNotifications()).forEach(notification => notification.close());
      return Boolean(subscription);
    });
    row.storeAfterCleanup = await summary(page);
    row.cleanup = !row.localSubscriptionRemaining && row.storeAfterCleanup.registrations === 0 ? "complete" : "incomplete";
  } catch (error) {row.cleanupError = safeError(error);}
}
(async () => {
  save();
  for (const engine of [chromium, firefox]) {
    const row = {browser: engine.name(), phase: "launch", providerAccepted: false, workerReceiptVerified: false,
      browserNotificationRecordVerified: false, zeroPortalTabsVerified: false, osDisplayVerified: false};
    report.browsers.push(row); save();
    const profile = fs.mkdtempSync(path.join(os.tmpdir(), `session-provider-probe-${engine.name()}-`));
    let context;
    try {
      context = await engine.launchPersistentContext(profile, {headless: true, ignoreHTTPSErrors: true,
        ...(engine === chromium ? {channel: "chromium", ignoreDefaultArgs: ["--disable-background-networking"],
          args: ["--ignore-certificate-errors", "--allow-insecure-localhost"]} : {})});
      context.setDefaultTimeout(12000);
      context.setDefaultNavigationTimeout(20000);
      row.version = context.browser()?.version() || "unreported";
      try {await context.grantPermissions(["notifications"], {origin}); row.permissionSetup = "granted";}
      catch (error) {row.permissionSetup = "unavailable"; row.permissionError = safeError(error); row.phase = "permission_setup_unavailable"; continue;}
      const page = await context.newPage();
      page.setDefaultTimeout(12000);
      await page.goto(`${base}/example/#settings`);
      row.apiSupport = await page.evaluate(() => ({secureContext: isSecureContext, serviceWorker: "serviceWorker" in navigator,
        push: "PushManager" in globalThis, notifications: "Notification" in globalThis, permission: globalThis.Notification?.permission || "unavailable"}));
      if (!(row.apiSupport.secureContext && row.apiSupport.serviceWorker && row.apiSupport.push && row.apiSupport.notifications)) {row.phase = "browser_unsupported"; continue;}
      row.phase = "register"; save();
      await page.locator("[data-notification-enable]").click();
      try {
        await page.waitForFunction(incompleteText => {
          const text = document.querySelector("[data-notification-status]")?.textContent || "";
          return text.startsWith("Enabled on this browser") || text.startsWith("Registration failed:") || text === incompleteText || text.startsWith("Notifications are blocked");
        }, incomplete, {timeout: 45000});
      } catch (error) {row.phase = "registration_incomplete"; row.registrationError = safeError(error); continue;}
      const enabled = await page.evaluate(() => document.querySelector("[data-notification-status]")?.textContent.startsWith("Enabled on this browser"));
      if (!enabled) {
        row.phase = "registration_unavailable";
        row.registrationStatus = await page.evaluate(incompleteText => {
          const text = document.querySelector("[data-notification-status]")?.textContent || "";
          return text === incompleteText ? "local_incomplete" : text.startsWith("Notifications are blocked") ? "permission_denied" :
            text.startsWith("Registration failed:") ? "registration_failed" : "unavailable";
        }, incomplete);
        continue;
      }
      row.registration = "enabled";
      row.before = await deliveryEvidence(page); row.before.result = safeResult(row.before.result);
      await page.locator("[data-notification-test]").click();
      await page.waitForFunction(() => document.querySelector("[data-notification-status]")?.textContent.startsWith("A test notification will be sent in 10 seconds."));
      row.phase = "test_queued"; save();
      const blank = await context.newPage(); await blank.goto("about:blank");
      for (const open of context.pages()) if (open.url().startsWith(origin + "/")) await open.close();
      row.portalTabsDuringWait = context.pages().filter(open => open.url().startsWith(origin + "/")).length;
      row.zeroPortalTabsVerified = row.portalTabsDuringWait === 0 && blank.url() === "about:blank";
      await blank.bringToFront();
      await blank.waitForTimeout(18000);
      const reopened = await context.newPage(); await reopened.goto(`${base}/example/#settings`);
      row.after = await deliveryEvidence(reopened); row.after.result = safeResult(row.after.result);
      row.providerAccepted = row.after.result === "provider_accepted";
      row.workerReceiptVerified = Number.isInteger(row.after.workerTestRecords) && row.after.workerTestRecords > (row.before.workerTestRecords || 0);
      row.browserNotificationRecordVerified = row.after.testNotifications > row.before.testNotifications;
      row.phase = row.providerAccepted && row.workerReceiptVerified && row.browserNotificationRecordVerified ? "delivery_evidence_observed" : "delivery_incomplete";
    } catch (error) {row.phase = "harness_incomplete"; row.error = safeError(error);}
    finally {
      if (context) {
        await cleanup(context, row);
        try {await context.close(); row.browserClosed = true;}
        catch (error) {row.browserClosed = false; row.closeError = safeError(error);}
      }
      // Explicit cleanup is limited to this fixture's freshly allocated profile.
      if (!context || row.browserClosed) {
        try {fs.rmSync(profile, {recursive: true, force: true}); row.profileRemoved = true;}
        catch (error) {row.profileRemoved = false; row.profileError = safeError(error);}
      } else {row.profileRemoved = false;}
      save();
    }
  }
  console.log(JSON.stringify(report));
})().catch(error => {report.harnessError = safeError(error); save(); console.log(JSON.stringify(report)); process.exitCode = 1;});
