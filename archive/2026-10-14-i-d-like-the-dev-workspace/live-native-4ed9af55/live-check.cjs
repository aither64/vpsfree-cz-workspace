"use strict";
// Live acceptance only after lead-authorized activation. No raw errors, auth,
// subscription material, transcript data or private server state are logged.
const fs = require("node:fs"), os = require("node:os"), path = require("node:path");
const cp = require("node:child_process"), crypto = require("node:crypto");
const expected = JSON.parse(fs.readFileSync(path.join(__dirname, "expected.json"), "utf8"));
const tracking = path.dirname(__dirname), resultPath = process.env.LIVE_NOTIFICATION_RESULT;
const report = {sourceRevision: expected.sourceRevision, headless: false, platform: process.platform,
  syntheticPush: false, providerResultCorrelated: false, osDisplayVerified: false, macOSDisplayVerified: false, phase: "preflight", browsers: []};
const codes = new Set(["result_path_missing", "preparation_unavailable", "preparation_revision_mismatch", "selected_profile_mismatch",
  "remote_read_unavailable", "credentials_unavailable", "served_asset_mismatch", "portal_identity_mismatch"]);
const fail = code => {const error = new Error(); error.probeCode = code; throw error;};
const safeError = error => ["Error", "TimeoutError", "AbortError", "NotAllowedError", "NotSupportedError", "SecurityError", "InvalidStateError", "InvalidAccessError", "NetworkError", "UnknownError", "OperationError", "QuotaExceededError", "TypeError"].includes(error?.name) ? error.name : "Error";
const safeResult = result => ["", "provider_accepted", "retrying", "provider_refused", "expired", "delivery_failed"].includes(result) ? result : "unknown";
function save() {
  if (!resultPath) return;
  try {fs.writeFileSync(resultPath, JSON.stringify(report, null, 2) + "\n", {mode: 0o600});}
  catch (_) {report.outputWriteFailed = true;}
}
function remoteRead(command) {
  try {
    return cp.execFileSync("ssh", ["-o", "BatchMode=yes", "-o", "ConnectTimeout=8", "-o", "LogLevel=ERROR",
      "root@172.16.106.40", command], {encoding: "utf8", timeout: 15000, maxBuffer: 8192, stdio: ["ignore", "pipe", "pipe"]}).trim();
  } catch (_) {fail("remote_read_unavailable");}
}
function preparedPackage() {
  let preparation;
  try {
    const file = fs.realpathSync(process.env.LIVE_PROFILE_PREPARED || path.join(tracking, "profile-prepared.json"));
    if (!file.startsWith(tracking + path.sep) || fs.statSync(file).size > 4 * 1024 * 1024) fail("preparation_unavailable");
    preparation = JSON.parse(fs.readFileSync(file, "utf8"));
  } catch (_) {fail("preparation_unavailable");}
  const operation = preparation.operation;
  const runtimes = operation?.coverage?.filter(entry => entry.repository === "dev-workspace") || [];
  if (runtimes.length !== 1 || runtimes[0].revision !== expected.sourceRevision) fail("preparation_revision_mismatch");
  if (!/^\/nix\/store\/[a-z0-9]{32}-[^/\s]{1,200}$/.test(operation.candidatePackage)) fail("preparation_unavailable");
  return operation.candidatePackage;
}
function selectedMatches(candidate) {
  return remoteRead("readlink -f /home/aither/.local/state/dev-workspaces/profile") === candidate;
}
async function servedAssetsMatch(context) {
  for (const [route, digest] of Object.entries(expected.assets)) {
    const response = await context.request.get(expected.origin + route, {timeout: 12000});
    if (response.status() !== 200 || crypto.createHash("sha256").update(await response.body()).digest("hex") !== digest) return false;
  }
  return true;
}
async function openControls(context) {
  const page = await context.newPage();
  await page.goto(expected.origin + "/");
  const indexMatches = await page.evaluate(origin => location.origin === origin && location.pathname === "/", expected.origin);
  if (!indexMatches) fail("portal_identity_mismatch");
  await page.getByRole("button", {name: "Workspace menu", exact: true}).click();
  await page.getByRole("link", {name: "Browser notifications", exact: true}).click();
  await page.waitForURL(expected.origin + expected.notificationsPath);
  const matches = await page.evaluate(({origin, notificationsPath}) => location.origin === origin && location.pathname === notificationsPath,
    {origin: expected.origin, notificationsPath: expected.notificationsPath});
  if (!matches) fail("portal_identity_mismatch");
  await page.locator("#browser-notifications").waitFor({state: "visible"});
  return page;
}
async function controlStatus(page) {
  return page.evaluate(() => {
    const text = document.querySelector("[data-notification-status]")?.textContent || "";
    if (text.startsWith("Disabled on this browser.")) return "disabled";
    if (text === "Browser subscription removed; server cleanup is still pending. Retry Disable.") return "server_pending";
    if (text === "Disabling is incomplete. Retry Disable.") return "disable_incomplete";
    if (text === "Browser setup is incomplete. Disable it or enable notifications again.") return "setup_incomplete";
    if (text.startsWith("Registration failed:")) return "registration_failed";
    if (text.startsWith("Notifications are blocked")) return "permission_denied";
    if (text.startsWith("This browser build does not support")) return "unsupported";
    if (text.startsWith("Enabled on this browser")) return "enabled";
    return "other";
  });
}
function exactTestDescriptor(value) {
  return value && typeof value.id === "string" && /^[0-9a-f]{64}$/.test(value.id) &&
    typeof value.identity === "string" && /^test-[0-9a-f]{64}$/.test(value.identity) &&
    Number.isSafeInteger(value.revision) && value.revision > 0 && Number.isSafeInteger(value.expiresAt) &&
    value.expiresAt > Date.now() && value.expiresAt <= Date.now() + 70000 ?
    {id: value.id, identity: value.identity, revision: value.revision, expiresAt: value.expiresAt} : null;
}
async function deliveryEvidence(page, descriptor = null) {
  const value = await page.evaluate(async descriptor => {
    const id = localStorage.getItem("workspace-browser-notifications.v1") || "";
    let settingsHTTPStatus = null, state = null;
    const controller = new AbortController(), deadline = setTimeout(() => controller.abort(), 8000);
    try {
      const response = await fetch(`/api/browser-notifications?registrationId=${encodeURIComponent(id)}`, {cache: "no-store", credentials: "same-origin", signal: controller.signal});
      settingsHTTPStatus = response.status;
      if (response.ok) state = await response.json();
    } catch (_) {} finally {clearTimeout(deadline);}
    const tag = descriptor ? `test-${descriptor.identity}-${descriptor.id}` : null;
    let notifications = null, notificationDeadline;
    try {
      notifications = await Promise.race([(async () => {
        const registration = await navigator.serviceWorker.getRegistration("/");
        return registration ? registration.getNotifications() : [];
      })(), new Promise(resolve => {notificationDeadline = setTimeout(() => resolve(null), 1500);})]);
    } catch (_) {} finally {clearTimeout(notificationDeadline);}
    const local = descriptor ? await new Promise(resolve => {
      let db, settled = false;
      const finish = value => {if (settled) return; settled = true; clearTimeout(timer); db?.close(); resolve(value);};
      const timer = setTimeout(() => finish({read: "unavailable"}), 1500);
      const open = indexedDB.open("workspace-session-attention");
      // Never create a schema while collecting evidence.
      open.onupgradeneeded = () => {open.transaction.abort(); finish({read: "absent"});};
      open.onerror = open.onblocked = () => finish({read: "unavailable"});
      open.onsuccess = () => {
        db = open.result;
        if (settled) {db.close(); return;}
        if (!db.objectStoreNames.contains("sessions")) {finish({read: "absent"}); return;}
        const read = db.transaction("sessions", "readonly").objectStore("sessions").get(descriptor.identity);
        read.onerror = () => finish({read: "unavailable"});
        read.onsuccess = () => {
          const outcome = read.result?.testOutcome;
          const correlated = Boolean(outcome && outcome.identity === descriptor.identity && outcome.id === descriptor.id &&
            outcome.revision === descriptor.revision && outcome.expiresAt === descriptor.expiresAt);
          const display = correlated && ["resolved", "rejected"].includes(outcome.display) ? outcome.display : "unknown";
          const errorCategory = display === "rejected" && ["NotAllowedError", "NotSupportedError", "SecurityError", "InvalidStateError", "TypeError", "AbortError"].includes(outcome.error) ? outcome.error : display === "rejected" ? "UnknownError" : "none";
          finish({read: read.result ? "found" : "absent", correlated, received: correlated && outcome.received === true, display, errorCategory,
            workerBrowserRecord: correlated && ["present", "absent", "unavailable"].includes(outcome.browserRecord) ? outcome.browserRecord : "unavailable"});
        };
      };
    }) : {read: "not_requested"};
    const matching = descriptor && notifications ? notifications.filter(notification => notification.tag === tag).length : null;
    return {settingsHTTPStatus, registered: Boolean(state?.registered), result: state?.result || "", providerResultCorrelated: false,
      workerRecordRead: local.read, outcomeCorrelated: Boolean(local.correlated), received: Boolean(local.received), display: local.display || "unknown",
      displayErrorCategory: local.errorCategory || "none", workerBrowserRecord: local.workerBrowserRecord || "unavailable",
      browserRecord: matching === null ? "unavailable" : matching > 0 ? "present" : "absent", matchingTestNotifications: matching,
      notifications: notifications?.length ?? null,
      testNotifications: notifications ? notifications.filter(notification => notification.body === "Browser notification test").length : null};
  }, descriptor);
  value.result = safeResult(value.result);
  return value;
}
async function cleanup(context, row) {
  if (!row.enableAttempted) {row.cleanup = "not_needed"; return;}
  row.cleanup = "incomplete";
  let page;
  try {
    page = context.pages().find(candidate => candidate.url().startsWith(expected.origin + expected.notificationsPath));
    if (!page) page = await openControls(context);
    await page.waitForFunction(() => Boolean(document.querySelector("[data-notification-status]")?.textContent.trim()));
    await page.locator("[data-notification-disable]").waitFor({state: "visible"});
    const button = page.locator("[data-notification-disable]");
    if (await button.isEnabled()) {
      await button.click();
      await page.waitForFunction(() => document.querySelector("[data-notification-status]")?.textContent.startsWith("Disabled on this browser."), null, {timeout: 15000});
      row.serverAbsenceConfirmedByShippedDisable = true;
    }
  } catch (error) {row.cleanupError = safeError(error);}
  if (!page || page.isClosed()) return;
  try {row.cleanupStatus = await controlStatus(page);} catch (error) {row.cleanupStatusError = safeError(error);}
  try {
    row.localSubscriptionRemaining = await page.evaluate(async () => {
      const registration = await navigator.serviceWorker.getRegistration("/");
      const subscription = await registration?.pushManager.getSubscription();
      if (registration) (await registration.getNotifications()).forEach(notification => notification.close());
      return Boolean(subscription);
    });
  } catch (error) {row.localCleanupError = safeError(error);}
  if (row.serverAbsenceConfirmedByShippedDisable && row.localSubscriptionRemaining === false && row.cleanupStatus === "disabled") row.cleanup = "complete";
}
(async () => {
  if (!resultPath) fail("result_path_missing");
  save();
  const candidate = preparedPackage();
  report.preparationRevisionMatches = true;
  if (!selectedMatches(candidate)) fail("selected_profile_mismatch");
  report.selectedPackageMatches = true;
  let username, password;
  try {
    username = remoteRead("cut -d: -f1 /var/lib/dev-workspaces/auth/htpasswd");
    password = remoteRead("cat /var/lib/dev-workspaces/password/password");
    if (!username || username.length > 256 || /[\r\n\0]/.test(username) || !password || password.length > 4096 || /[\r\n\0]/.test(password)) fail("credentials_unavailable");
  } catch (_) {fail("credentials_unavailable");}
  const {chromium, firefox} = require("@playwright/test");
  for (const engine of [chromium, firefox]) {
    const row = {browser: engine.name(), phase: "launch", providerAccepted: false, workerReceiptVerified: false,
      browserNotificationRecordVerified: false, zeroPortalTabsVerified: false, osDisplayVerified: false};
    report.browsers.push(row); save();
    const profile = fs.mkdtempSync(path.join(os.tmpdir(), `session-live-4ed9af55-${engine.name()}-`));
    let context;
    try {
      if (!selectedMatches(candidate)) fail("selected_profile_mismatch");
      context = await engine.launchPersistentContext(profile, {headless: false, ignoreHTTPSErrors: true,
        httpCredentials: {username, password, origin: expected.origin}, ...(engine === chromium ? {channel: "chromium",
          ignoreDefaultArgs: ["--disable-background-networking"], args: ["--ignore-certificate-errors", "--allow-insecure-localhost"]} :
        {firefoxUserPrefs: {"dom.push.serverURL": "wss://push.services.mozilla.com/", "dom.push.connection.enabled": true}})});
      context.setDefaultTimeout(12000); context.setDefaultNavigationTimeout(20000);
      row.version = context.browser()?.version() || "unreported";
      row.servedAssetsMatch = await servedAssetsMatch(context);
      if (!row.servedAssetsMatch) fail("served_asset_mismatch");
      await context.grantPermissions(["notifications"], {origin: expected.origin});
      let page = await openControls(context);
      row.apiSupport = await page.evaluate(() => ({secureContext: isSecureContext, serviceWorker: "serviceWorker" in navigator,
        push: "PushManager" in globalThis, notifications: "Notification" in globalThis,
        permission: ["default", "granted", "denied"].includes(globalThis.Notification?.permission) ? Notification.permission : "unavailable"}));
      if (!(row.apiSupport.secureContext && row.apiSupport.serviceWorker && row.apiSupport.push && row.apiSupport.notifications)) {row.phase = "browser_unsupported"; continue;}
      if (row.apiSupport.permission !== "granted") {row.phase = "permission_unavailable"; continue;}
      if (preparedPackage() !== candidate) fail("preparation_revision_mismatch");
      if (!selectedMatches(candidate)) fail("selected_profile_mismatch");
      if (!await servedAssetsMatch(context)) fail("served_asset_mismatch");
      row.phase = "enable"; save(); row.enableAttempted = true;
      await page.locator("[data-notification-enable]").click();
      await page.waitForFunction(() => {
        const text = document.querySelector("[data-notification-status]")?.textContent || "";
        const button = document.querySelector("[data-notification-test]");
        return (button && !button.disabled) || text.startsWith("Registration failed:") ||
          text.startsWith("Browser setup is incomplete.") || text.startsWith("Notifications are blocked") || text.startsWith("Disabling is incomplete.");
      }, null, {timeout: 45000});
      if (!await page.locator("[data-notification-test]").isEnabled()) {row.phase = "registration_incomplete"; row.controlStatus = await controlStatus(page); continue;}
      row.before = await deliveryEvidence(page);
      if (preparedPackage() !== candidate) fail("preparation_revision_mismatch");
      if (!selectedMatches(candidate)) fail("selected_profile_mismatch");
      if (!await servedAssetsMatch(context)) fail("served_asset_mismatch");
      row.phase = "test"; save();
      const [response] = await Promise.all([
        page.waitForResponse(response => response.request().method() === "POST" &&
          response.url() === expected.origin + "/api/browser-notifications/test", {timeout: 15000}),
        page.locator("[data-notification-test]").click(),
      ]);
      row.testHTTPStatus = response.status();
      const reply = await response.json();
      row.queueAccepted = response.status() === 200 && reply.ok === true;
      // Descriptor values remain in memory and in the browser; never in output.
      const descriptor = exactTestDescriptor(reply.test);
      row.testDescriptorValid = Boolean(descriptor) && await page.evaluate(value => value.identity ===
        `test-${localStorage.getItem("workspace-browser-notifications.v1") || ""}`, descriptor);
      if (!row.queueAccepted || !row.testDescriptorValid) {row.phase = "test_uncorrelated"; continue;}
      await page.waitForFunction(() => document.querySelector("[data-notification-status]")?.textContent.startsWith("A test notification will be sent in 10 seconds."));
      const blank = await context.newPage(); await blank.goto("about:blank");
      for (const open of context.pages()) if (new URL(open.url()).origin === expected.origin) await open.close();
      row.portalTabsDuringWait = context.pages().filter(open => new URL(open.url()).origin === expected.origin).length;
      row.zeroPortalTabsVerified = row.portalTabsDuringWait === 0 && blank.url() === "about:blank";
      await blank.bringToFront(); row.phase = "zero_tab_wait"; save(); await blank.waitForTimeout(18000);
      page = await openControls(context);
      row.after = await deliveryEvidence(page, descriptor);
      row.preparationStillMatches = preparedPackage() === candidate;
      row.selectedPackageStillMatches = selectedMatches(candidate);
      row.servedAssetsStillMatch = await servedAssetsMatch(context);
      row.providerAccepted = row.after.result === "provider_accepted";
      row.providerResultCorrelated = false;
      row.workerReceiptVerified = row.after.outcomeCorrelated && row.after.received;
      row.displayAPIOutcome = row.after.display;
      row.displayAPIErrorCategory = row.after.displayErrorCategory;
      row.correlatedPostDisplayEvidenceVerified = row.after.outcomeCorrelated && ["resolved", "rejected"].includes(row.after.display);
      row.browserNotificationRecordVerified = row.after.browserRecord === "present";
      row.phase = !row.preparationStillMatches || !row.selectedPackageStillMatches || !row.servedAssetsStillMatch ? "revision_changed" :
        row.after.display === "rejected" ? "display_rejected" : row.workerReceiptVerified && row.after.display === "resolved" && row.zeroPortalTabsVerified ?
          "display_request_resolved" : "delivery_incomplete";
    } catch (error) {row.phase = "incomplete"; row.error = safeError(error); if (codes.has(error.probeCode)) row.reason = error.probeCode;}
    finally {
      if (context) {
        await cleanup(context, row);
        try {await context.close(); row.browserClosed = true;} catch (error) {row.browserClosed = false; row.closeError = safeError(error);}
      }
      const canRemove = (!context && !row.enableAttempted) || (row.browserClosed && ["complete", "not_needed"].includes(row.cleanup));
      if (canRemove) {
        try {fs.rmSync(profile, {recursive: true, force: true}); row.profileRemoved = true;} catch (error) {row.profileRemoved = false; row.profileError = safeError(error);}
      } else {
        row.profileRemoved = false; row.profileRetainedForRecovery = true;
        const recovery = path.join(path.dirname(resultPath), "recovery-profiles.json");
        try {
          const entries = fs.existsSync(recovery) ? JSON.parse(fs.readFileSync(recovery, "utf8")) : [];
          entries.push({browser: engine.name(), profileDirectory: profile});
          fs.writeFileSync(recovery, JSON.stringify(entries, null, 2) + "\n", {mode: 0o600});
        } catch (_) {row.recoveryManifestUnavailable = true;}
      }
      save();
    }
  }
  username = ""; password = "";
  report.phase = "diagnostics_completed"; save(); console.log(JSON.stringify(report));
})().catch(error => {report.phase = "refused_or_incomplete"; report.error = safeError(error); if (codes.has(error.probeCode)) report.reason = error.probeCode; save(); console.log(JSON.stringify(report)); process.exitCode = 1;});
