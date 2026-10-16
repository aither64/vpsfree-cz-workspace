(() => {
  "use strict";
  const key = "workspace-browser-notifications.v1";
  const panel = document.getElementById("browser-notifications");
  if (!panel) return;
  const status = panel.querySelector("[data-notification-status]"), enable = panel.querySelector("[data-notification-enable]"),
    disable = panel.querySelector("[data-notification-disable]"), test = panel.querySelector("[data-notification-test]");
  const supported = globalThis.isSecureContext && "serviceWorker" in navigator && "PushManager" in globalThis && "Notification" in globalThis;
  let registrationId = "", busy = false, registered = false, localSubscription = null;
  const incomplete = "Browser setup is incomplete. Disable it or enable notifications again.";
  try { registrationId = localStorage.getItem(key) || ""; } catch (_) {}
  const api = async (path, body) => {
    const controller = new AbortController(), deadline = setTimeout(() => controller.abort(), 8000);
    try {
      const response = await fetch(`/api/browser-notifications${path}`, {cache: "no-store", credentials: "same-origin", signal: controller.signal,
        ...(body ? {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(body)} : {})});
      const value = await response.json(); if (!response.ok) throw new Error(value.error || "Browser notifications are unavailable."); return value;
    } finally { clearTimeout(deadline); }
  };
  const buttons = () => {
    enable.disabled = busy || !supported || Notification.permission === "denied";
    disable.disabled = busy || !supported || (!localSubscription && !registrationId);
    test.disabled = busy || !registered;
  };
  async function refresh() {
    if (!supported) { status.textContent = "This browser build does not support background Web Push. Use a browser with Push API support."; buttons(); return; }
    try {
      const local = await navigator.serviceWorker.getRegistration("/");
      localSubscription = await local?.pushManager.getSubscription();
      const state = await api(`?registrationId=${encodeURIComponent(registrationId)}`);
      registered = Boolean(state.registered && localSubscription && Notification.permission === "granted");
      status.textContent = localSubscription && !registered ? incomplete : Notification.permission === "denied" ? "Notifications are blocked. Change this site's notification permission in your browser settings." :
        !state.available ? "Notification delivery is disabled on the server." : state.result === "expired" ? "The browser subscription expired. Enable notifications again." : registered ?
        ({expired: "The browser subscription expired. Enable notifications again.", retrying: "The provider is unavailable. Delivery will retry.", delivery_failed: "Delivery failed. Send a test notification to check it.", provider_refused: "The provider refused delivery. Enable notifications again.", provider_accepted: "The push service accepted the last notification. Check this browser to confirm it appeared."})[state.result] || "Enabled on this browser." : "Disabled on this browser.";
    } catch (error) { registered = false; status.textContent = localSubscription ? incomplete : error.message; }
    buttons();
  }
  enable.addEventListener("click", async () => {
    if (busy || !supported || Notification.permission === "denied") return;
    busy = true; buttons();
    try {
      const permission = await Notification.requestPermission();
      if (permission !== "granted") throw new Error(permission === "denied" ? "Notifications are blocked. Change this site's notification permission in your browser settings." : "Notification permission was not granted.");
      const state = await api("");
      if (!state.available) throw new Error("Notification delivery is disabled on the server.");
      const registration = await navigator.serviceWorker.register("/notification-worker.js", {scope: "/", updateViaCache: "none"});
      await navigator.serviceWorker.ready;
      let subscription = await registration.pushManager.getSubscription();
      localSubscription = subscription;
      const applicationServerKey = Uint8Array.from(atob(state.publicKey.replace(/-/g, "+").replace(/_/g, "/")), char => char.charCodeAt(0));
      if (subscription && subscription.options.applicationServerKey &&
          [...new Uint8Array(subscription.options.applicationServerKey)].join() !== [...applicationServerKey].join()) {
        throw new Error("The server's push key changed. Disable this browser subscription, then enable it again.");
      }
      subscription ||= await registration.pushManager.subscribe({userVisibleOnly: true, applicationServerKey});
      localSubscription = subscription;
      const value = subscription.toJSON();
      const saved = await api("/register", {subscription: {endpoint: value.endpoint, keys: value.keys}, expirationTime: value.expirationTime ?? null});
      registrationId = saved.registrationId;
      localStorage.setItem(key, registrationId);
      if (localStorage.getItem(key) !== registrationId) throw new Error("Browser registration could not be saved. Try enabling notifications again.");
      registered = true; status.textContent = "Enabled on this browser. Send a test notification to check delivery.";
    } catch (error) { registered = false; status.textContent = localSubscription ? incomplete : `Registration failed: ${error.message}`; }
    finally { busy = false; buttons(); }
  });
  disable.addEventListener("click", async () => {
    if (busy) return;
    busy = true; buttons();
    try {
      const registration = await navigator.serviceWorker.getRegistration("/");
      const subscription = await registration?.pushManager.getSubscription() || localSubscription;
      if (!registrationId && subscription) {
        // A lost register acknowledgement/storage key is recovered through the
        // same origin-bound, endpoint-idempotent registration, then removed.
        const value = subscription.toJSON();
        const saved = await api("/register", {subscription: {endpoint: value.endpoint, keys: value.keys}, expirationTime: value.expirationTime ?? null});
        registrationId = saved.registrationId;
      }
      if (registrationId) await api("/disable", {registrationId});
      registered = false;
      if (subscription && !await subscription.unsubscribe()) throw new Error("The server registration was removed, but browser unsubscribe failed. Retry Disable.");
      localSubscription = null; localStorage.removeItem(key); registrationId = ""; registered = false;
      status.textContent = "Disabled on this browser. Site permission remains in your browser settings.";
    } catch (error) { status.textContent = `Disabling is incomplete: ${error.message}`; }
    finally { busy = false; buttons(); }
  });
  test.addEventListener("click", async () => {
    if (busy || !registered) return;
    busy = true; buttons();
    try { await api("/test", {registrationId}); status.textContent = "A test notification will be sent in 10 seconds. Close portal tabs or switch windows to check background delivery."; }
    catch (error) { status.textContent = error.message; }
    finally { busy = false; buttons(); }
  });
  globalThis.workspaceBrowserNotifications = {
    async presence(snapshot, focused, seen) {
      if (!focused || !registrationId || !registered) return;
      const eventId = snapshot.event && seen.includes(snapshot.event.id) ? snapshot.event.id : "";
      try { await fetch(`/api/sessions/${document.body.dataset.session}/attention`, {method: "POST", headers: {"Content-Type": "application/json"},
        body: JSON.stringify({identity: snapshot.identity, registrationId, eventId})}); } catch (_) {}
    },
  };
  void refresh();
})();
