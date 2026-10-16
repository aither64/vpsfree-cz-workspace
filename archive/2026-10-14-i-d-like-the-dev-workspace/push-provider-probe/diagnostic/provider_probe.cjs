"use strict";
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const {chromium, firefox} = require("@playwright/test");
const base = process.argv[2];
const resultPath = process.env.PROVIDER_PROBE_RESULT_FILE;
const origin = new URL(base).origin;
const safeResult = value => ["", "provider_accepted", "retrying", "provider_refused", "expired", "delivery_failed"].includes(value) ? value : "unknown";
const safeError = error => ["TimeoutError", "Error", "AbortError", "NotAllowedError", "NotSupportedError", "SecurityError", "InvalidStateError", "InvalidAccessError", "NetworkError", "UnknownError", "OperationError", "QuotaExceededError", "TypeError", "RangeError", "NotFoundError", "NotReadableError", "InvalidModificationError"].includes(error?.name) ? error.name : "Error";
const report = {sourceRevision: "e414ed31806d2b91620d5e5fad8b5b5ee56e07ac", platform: process.platform, headless: true,
  providerTransport: "shipped_guardedPushClient_unmocked", syntheticPush: false, osDisplayVerified: false, macOSDisplayVerified: false, browsers: []};
const incomplete = "Browser setup is incomplete. Disable it or enable notifications again.";
function save() {
  if (resultPath) fs.writeFileSync(resultPath, JSON.stringify(report, null, 2) + "\n", {mode: 0o600});
}
// Transparent diagnostics: every native method receives its original arguments
// and returns its real result or rejection. No capability or key enters state.
async function installDiagnostics(context, row) {
  row.apiHTTP = [];
  context.on("response", response => {
    const url = new URL(response.url());
    const action = ({"/api/browser-notifications": "state", "/api/browser-notifications/register": "register",
      "/api/browser-notifications/disable": "disable", "/api/browser-notifications/test": "test"})[url.pathname];
    if (url.origin === origin && action && row.apiHTTP.length < 24) row.apiHTTP.push({action, status: response.status()});
  });
  await context.addInitScript(targetOrigin => {
    if (location.origin !== targetOrigin) return;
    const state = globalThis.__providerProbeDiagnostics = {steps: [], storage: {getCalls: 0, setCalls: 0}};
    const allowedNames = ["Error", "AbortError", "NotAllowedError", "NotSupportedError", "SecurityError", "InvalidStateError", "InvalidAccessError", "NetworkError", "UnknownError", "OperationError", "QuotaExceededError", "TypeError", "RangeError", "NotFoundError", "NotReadableError", "InvalidModificationError"];
    const classify = error => {
      const name = allowedNames.includes(error?.name) ? error.name : "Error";
      const category = ({NotAllowedError: "permission", SecurityError: "security", NetworkError: "network",
        NotSupportedError: "unsupported", InvalidStateError: "state", InvalidAccessError: "argument",
        AbortError: "aborted", OperationError: "operation", QuotaExceededError: "quota", TypeError: "argument", RangeError: "argument",
        NotFoundError: "not_found", NotReadableError: "not_readable", InvalidModificationError: "state"})[name] || "unclassified";
      // Recognize only fixed browser messages, never return the message itself.
      const known = new Map([["Registration failed - push service error", "push_service_error"],
        ["Registration failed - push service not available", "push_service_unavailable"],
        ["Error retrieving push subscription", "push_subscription_lookup"]]).get(error?.message);
      return {name, category: known || category};
    };
    const shape = subscription => {
      if (!subscription) return {present: false};
      try {
        const value = subscription.toJSON(), url = new URL(value.endpoint);
        const decodeLength = text => {
          if (typeof text !== "string" || text.length > 256) return -1;
          try {return atob(text.replace(/-/g, "+").replace(/_/g, "/")).length;} catch (_) {return -1;}
        };
        const expires = value.expirationTime;
        return {present: true, endpointHttps: url.protocol === "https:", endpointHostAllowed: ["fcm.googleapis.com", "updates.push.services.mozilla.com"].includes(url.hostname),
          endpointWithinLimit: value.endpoint.length <= 2048, endpointPortAllowed: !url.port || url.port === "443",
          endpointPathPresent: Boolean(url.pathname), endpointHasCredentials: Boolean(url.username || url.password), endpointHasFragment: Boolean(url.hash),
          publicKeyBytesValid: decodeLength(value.keys?.p256dh) === 65, authKeyBytesValid: decodeLength(value.keys?.auth) === 16,
          publicKeyUnpadded: typeof value.keys?.p256dh === "string" && !value.keys.p256dh.includes("="),
          authKeyUnpadded: typeof value.keys?.auth === "string" && !value.keys.auth.includes("="),
          keyFieldsKnown: value.keys && Object.keys(value.keys).every(key => ["auth", "p256dh"].includes(key)),
          expirationKind: expires === undefined ? "absent" : expires === null ? "null" : Number.isSafeInteger(expires) ? "integer" : typeof expires === "number" ? "fractional_or_unsafe_number" : "other",
          expirationFuture: expires == null || (typeof expires === "number" && expires > Date.now())};
      } catch (error) {return {present: true, inspectionError: classify(error)};}
    };
    const add = record => {if (state.steps.length < 24) state.steps.push(record);};
    const wrap = (prototype, method, onSuccess) => {
      const original = prototype?.[method];
      if (typeof original !== "function") return;
      prototype[method] = function(...args) {
        const record = {stage: method, outcome: "pending"}; add(record);
        if (method === "subscribe") record.options = {userVisibleOnly: args[0]?.userVisibleOnly === true,
          publicKeyByteLengthValid: args[0]?.applicationServerKey?.byteLength === 65};
        let promise;
        try {promise = Reflect.apply(original, this, args);}
        catch (error) {record.outcome = "rejected"; record.error = classify(error); throw error;}
        return Promise.resolve(promise).then(value => {
          record.outcome = "resolved";
          if (onSuccess) {try {record.subscription = shape(value);} catch (_) {record.inspectionUnavailable = true;}}
          return value;
        }, error => {record.outcome = "rejected"; record.error = classify(error); throw error;});
      };
    };
    try {
      wrap(globalThis.ServiceWorkerContainer?.prototype, "register", false);
      wrap(globalThis.PushManager?.prototype, "subscribe", true);
      wrap(globalThis.PushManager?.prototype, "getSubscription", true);
      const key = "workspace-browser-notifications.v1", get = Storage.prototype.getItem, set = Storage.prototype.setItem;
      let savedValue;
      Storage.prototype.getItem = function(name) {
        if (name !== key) return Reflect.apply(get, this, [name]);
        state.storage.getCalls++;
        try {
          const value = Reflect.apply(get, this, [name]);
          state.storage.idPresent = Boolean(value);
          if (savedValue !== undefined) state.storage.readbackMatched = value === savedValue;
          return value;
        } catch (error) {state.storage.getError = classify(error); throw error;}
      };
      Storage.prototype.setItem = function(name, value) {
        if (name !== key) return Reflect.apply(set, this, [name, value]);
        state.storage.setCalls++;
        try {const result = Reflect.apply(set, this, [name, value]); savedValue = value; state.storage.setSucceeded = true; return result;}
        catch (error) {state.storage.setError = classify(error); throw error;}
      };
      state.installed = true;
    } catch (error) {state.installError = classify(error);}
  }, origin);
}
async function browserDiagnostics(page) {
  return page.evaluate(() => globalThis.__providerProbeDiagnostics || {installed: false});
}
async function summary(page) {
  return page.evaluate(async () => {
    const response = await fetch("/fixture/summary", {cache: "no-store"});
    const value = await response.json();
    return {registrations: value.registrations, pending: value.pending, httpDiagnosticCount: value.httpDiagnosticCount,
      httpDiagnostics: value.httpDiagnostics};
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
  let page;
  try {
    page = context.pages().find(page => page.url().startsWith(origin + "/"));
    if (!page) {page = await context.newPage(); await page.goto(`${base}/example/#settings`);}
    const button = page.locator("[data-notification-disable]");
    await page.waitForTimeout(1000);
    if (await button.isEnabled()) {
      await button.click();
      await page.waitForFunction(() => document.querySelector("[data-notification-status]")?.textContent.startsWith("Disabled on this browser."), null, {timeout: 12000});
    }
  } catch (error) {row.cleanupError = safeError(error);}
  if (!page || page.isClosed()) return;
  try {
    row.localSubscriptionRemaining = await page.evaluate(async () => {
      const registration = await navigator.serviceWorker.getRegistration("/");
      const subscription = await registration?.pushManager.getSubscription();
      if (registration) (await registration.getNotifications()).forEach(notification => notification.close());
      return Boolean(subscription);
    });
  } catch (error) {row.subscriptionCleanupError = safeError(error);}
  try {row.storeAfterCleanup = await summary(page);} catch (error) {row.summaryCleanupError = safeError(error);}
  try {row.browserAfterCleanup = await browserDiagnostics(page);} catch (error) {row.diagnosticCleanupError = safeError(error);}
  row.cleanup = row.localSubscriptionRemaining === false && row.storeAfterCleanup?.registrations === 0 ? "complete" : "incomplete";
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
      await installDiagnostics(context, row);
      row.version = context.browser()?.version() || "unreported";
      try {await context.grantPermissions(["notifications"], {origin}); row.permissionSetup = "granted";}
      catch (error) {row.permissionSetup = "unavailable"; row.permissionError = safeError(error); row.phase = "permission_setup_unavailable"; continue;}
      const page = await context.newPage();
      page.setDefaultTimeout(12000);
      await page.goto(`${base}/example/#settings`);
      row.serverBefore = await summary(page);
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
      } catch (error) {
        row.phase = "registration_incomplete"; row.registrationError = safeError(error);
        row.browserAfterRegistration = await browserDiagnostics(page); row.serverAfterRegistration = await summary(page);
        continue;
      }
      row.browserAfterRegistration = await browserDiagnostics(page);
      row.serverAfterRegistration = await summary(page);
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
