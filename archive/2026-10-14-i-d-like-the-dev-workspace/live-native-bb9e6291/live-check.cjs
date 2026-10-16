"use strict";
// Live acceptance only after lead-authorized activation. No raw errors, auth,
// subscription material, transcript data or private server state are logged.
const fs = require("node:fs"), os = require("node:os"), path = require("node:path");
const cp = require("node:child_process"), crypto = require("node:crypto");
const expected = JSON.parse(fs.readFileSync(path.join(__dirname, "expected.json"), "utf8"));
const tracking = path.dirname(__dirname), resultPath = process.env.LIVE_NOTIFICATION_RESULT;
const report = {sourceRevision: expected.sourceRevision, headless: false, platform: process.platform,
  syntheticPush: false, osDisplayVerified: false, macOSDisplayVerified: false, phase: "preflight", browsers: []};
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
async function openSettings(context) {
  const page = await context.newPage();
  await page.goto(expected.origin + expected.settingsPath);
  const matches = await page.evaluate(({origin, slug, settingsPath}) => location.origin === origin &&
    location.pathname === settingsPath.split("#")[0] && document.body.dataset.session === slug,
  {origin: expected.origin, slug: expected.sessionSlug, settingsPath: expected.settingsPath});
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
async function deliveryEvidence(page) {
  const value = await page.evaluate(async () => {
    const id = localStorage.getItem("workspace-browser-notifications.v1") || "";
    const response = await fetch(`/api/browser-notifications?registrationId=${encodeURIComponent(id)}`, {cache: "no-store", credentials: "same-origin"});
    const state = response.ok ? await response.json() : null;
    const registration = await navigator.serviceWorker.getRegistration("/");
    const notifications = registration ? await registration.getNotifications() : [];
    const workerTestRecords = await new Promise(resolve => {
      const open = indexedDB.open("workspace-session-attention");
      // Reading evidence must not create an empty database ahead of the app.
      open.onupgradeneeded = () => {open.transaction.abort(); open.result.close(); resolve(0);};
      open.onerror = () => resolve(null);
      open.onsuccess = () => {
        const db = open.result;
        if (!db.objectStoreNames.contains("sessions")) {db.close(); resolve(0); return;}
        const read = db.transaction("sessions", "readonly").objectStore("sessions").getAll();
        read.onerror = () => {db.close(); resolve(null);};
        read.onsuccess = () => {const count = read.result.filter(record => record.event?.kind === "test").length; db.close(); resolve(count);};
      };
    });
    return {settingsHTTPStatus: response.status, registered: Boolean(state?.registered), result: state?.result || "",
      workerTestRecords, notifications: notifications.length,
      testNotifications: notifications.filter(notification => notification.body === "Browser notification test").length};
  });
  value.result = safeResult(value.result);
  return value;
}
async function cleanup(context, row) {
  if (!row.enableAttempted) {row.cleanup = "not_needed"; return;}
  row.cleanup = "incomplete";
  let page;
  try {
    page = context.pages().find(candidate => candidate.url().startsWith(expected.origin + expected.settingsPath.split("#")[0]));
    if (!page) page = await openSettings(context);
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
    const profile = fs.mkdtempSync(path.join(os.tmpdir(), `session-live-bb9e6291-${engine.name()}-`));
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
      let page = await openSettings(context);
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
      await page.locator("[data-notification-test]").click();
      await page.waitForFunction(() => document.querySelector("[data-notification-status]")?.textContent.startsWith("A test notification will be sent in 10 seconds."));
      const blank = await context.newPage(); await blank.goto("about:blank");
      for (const open of context.pages()) if (new URL(open.url()).origin === expected.origin) await open.close();
      row.portalTabsDuringWait = context.pages().filter(open => new URL(open.url()).origin === expected.origin).length;
      row.zeroPortalTabsVerified = row.portalTabsDuringWait === 0 && blank.url() === "about:blank";
      await blank.bringToFront(); row.phase = "zero_tab_wait"; save(); await blank.waitForTimeout(18000);
      page = await openSettings(context);
      row.after = await deliveryEvidence(page);
      row.preparationStillMatches = preparedPackage() === candidate;
      row.selectedPackageStillMatches = selectedMatches(candidate);
      row.servedAssetsStillMatch = await servedAssetsMatch(context);
      row.providerAccepted = row.after.result === "provider_accepted";
      row.workerReceiptVerified = Number.isInteger(row.before.workerTestRecords) && Number.isInteger(row.after.workerTestRecords) && row.after.workerTestRecords > row.before.workerTestRecords;
      row.browserNotificationRecordVerified = row.after.testNotifications > row.before.testNotifications;
      row.phase = !row.preparationStillMatches || !row.selectedPackageStillMatches || !row.servedAssetsStillMatch ? "revision_changed" :
        row.providerAccepted && row.workerReceiptVerified && row.zeroPortalTabsVerified ? "provider_worker_observed" : "delivery_incomplete";
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
