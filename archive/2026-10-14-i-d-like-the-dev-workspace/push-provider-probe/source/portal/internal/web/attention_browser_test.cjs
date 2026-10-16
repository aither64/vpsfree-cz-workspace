const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = name => fs.readFileSync(path.join(__dirname, 'static', name), 'utf8');
const identity = 'a'.repeat(64), id = 'b'.repeat(64);
const event = (revision = 1, kind = 'input') => ({version: 1, identity, id, revision, kind, slug: 'example', member: 'implementer0', route: '/example/?member=implementer0#codex', expiresAt: Date.now() + 60000});

test('title priority and exact persistent reservation count', () => {
  const context = {}; vm.runInNewContext(source('session-attention.js'), context);
  const {title, reservations} = context.workspaceSessionAttention;
  assert.equal(title('api-cleanup · Workspace', event(), [], 0), '? api-cleanup · Workspace');
  assert.equal(title('api-cleanup · Workspace', event(1, 'done'), [], 1), '✓ R api-cleanup · Workspace');
  assert.equal(title('api-cleanup · Workspace', event(), [], 2), '? R2 api-cleanup · Workspace');
  assert.equal(title('api-cleanup · Workspace', event(), [id], 2), 'R2 api-cleanup · Workspace');
  assert.equal(reservations({reservationHolders: [{slug: 'example', observationIdentity: identity, machines: [
    {machine: 'one', state: 'deployed_review'}, {machine: 'one', state: 'recovery_hold'}, {machine: 'two', state: 'recovery_hold'}, {machine: 'three', state: 'requested'}]},
    {slug: 'example', observationIdentity: 'wrong', machines: [{machine: 'foreign', state: 'deployed_review'}]}]}, 'example', identity), 2);
  assert.throws(() => reservations({}, 'example', identity));
});

function workerHarness() {
  const listeners = {}, notifications = [], windows = [], records = new Map(), calls = [];
  let status = {fresh: true, enabled: true, identity, event: event(), revision: 1}, inaccessible = false;
  const context = {URL, AbortController, setTimeout, clearTimeout, Date,
    importScripts: value => assert.equal(value, '/static/session-attention-store.js'),
    workspaceAttentionStore: {update: async (key, change) => {
      const record = change(records.get(key) || {identity: key, seen: [], revision: 0, event: null}); records.set(key, record); return record;
    }},
    fetch: async (url, options) => { calls.push({url, options}); return {ok: !inaccessible, status: inaccessible ? 401 : 200, json: async () => status}; },
    self: {location: {origin: 'https://workspace.example'}, registration: {
      showNotification: async (title, options) => notifications.push({title, ...options}), getNotifications: async () => [],
    }, clients: {matchAll: async () => windows, openWindow: async url => calls.push({openWindow: url}), claim: async () => {}},
    addEventListener: (name, listener) => listeners[name] = listener},
  };
  vm.runInNewContext(source('notification-worker.js'), context);
  return {notifications, calls, records, context,
    status: value => status = value, inaccessible: () => inaccessible = true,
    push: async payload => { let pending; listeners.push({data: {json: () => payload}, waitUntil: promise => pending = promise}); await pending; },
    click: async (route, boundIdentity) => { let pending; listeners.notificationclick({notification: {data: {route, identity: boundIdentity}, close() {}}, waitUntil: promise => pending = promise}); await pending; },
  };
}

test('worker displays with zero tabs, coalesces duplicate and reordered delivery', async () => {
  const h = workerHarness();
  await h.push(event());
  assert.equal(h.notifications[0].body, 'implementer0: Your answer is needed');
  assert.equal(h.notifications[0].renotify, false);
  h.status({fresh: true, enabled: true, identity, event: {...event(2, 'done'), id: 'c'.repeat(64)}, revision: 2});
  await h.push({...event(2, 'done'), id: 'c'.repeat(64)});
  await h.push(event());
  assert.equal(h.notifications.at(-1).body, 'Session update available');
  assert.equal(h.notifications.at(-1).tag, h.notifications[0].tag);
  assert.equal(h.records.get(identity).revision, 2);
  assert.equal(h.notifications.length, 3, 'every delivered valid push is user-visible');
});

test('worker protects auth/mute/freshness races and safe click navigation', async () => {
  const h = workerHarness();
  h.status({fresh: true, enabled: false, identity, event: event(), revision: 1});
  await h.push(event()); assert.equal(h.notifications.at(-1).body, 'Session update available');
  h.inaccessible(); await h.push(event()); assert.equal(h.notifications.at(-1).title, 'Workspace update');
  await h.push({version: 99}); assert.equal(h.notifications.at(-1).title, 'Workspace update');
  await h.click('https://attacker.example/example/'); assert.equal(h.calls.filter(c => c.openWindow).length, 0);
  await h.click('//attacker.example/example/'); assert.equal(h.calls.filter(c => c.openWindow).length, 0);
  await h.click('/example/?member=implementer0#codex'); assert.equal(h.calls.at(-1).openWindow, 'https://workspace.example/example/?member=implementer0#codex');
  assert.ok(h.calls.filter(c => c.url).every(c => c.options.cache === 'no-store' && c.options.credentials === 'same-origin'));
  assert.equal(source('notification-worker.js').includes('caches.'), false, 'no authenticated cache');
});

test('worker handles bounded digit-containing member roles', async () => {
  const h = workerHarness(), member = 'gpt6reviewer0';
  const payload = {...event(), member, route: `/example/?member=${member}#codex`};
  h.status({fresh: true, enabled: true, identity, event: payload, revision: 1});
  await h.push(payload);
  assert.equal(h.notifications.at(-1).body, `${member}: Your answer is needed`);
  assert.equal(h.notifications.at(-1).data.route, payload.route);
  await h.click(payload.route, identity);
  const destination = new URL(h.calls.at(-1).openWindow);
  assert.equal(destination.searchParams.get('member'), member);
  assert.equal(destination.searchParams.get('attentionIdentity'), identity);
  await h.click(`/example/?member=${'a'.repeat(33)}0#codex`);
  assert.equal(h.calls.filter(call => call.openWindow).length, 1, 'oversized role is refused');
});

test('browser permission is only requested after explicit enable click', async () => {
  const controls = Object.fromEntries(['status', 'enable', 'disable', 'test'].map(name => [name, {disabled: false, addEventListener(type, callback) { this[type] = callback; }}]));
  let prompts = 0;
  const storage = new Map();
  const panel = {querySelector: selector => controls[selector.match(/notification-(\w+)/)[1]]};
  const context = {document: {getElementById: () => panel}, navigator: {serviceWorker: {getRegistration: async () => null}},
    Notification: {permission: 'default', requestPermission: async () => { prompts++; return 'denied'; }},
    isSecureContext: true, PushManager: function() {}, AbortController, setTimeout, clearTimeout,
    localStorage: {getItem: key => storage.get(key) || null},
    fetch: async () => ({ok: true, json: async () => ({available: true, registered: false})}),
  };
  vm.runInNewContext(source('browser-notifications.js'), context);
  for (let i = 0; i < 8; i++) await Promise.resolve();
  assert.equal(prompts, 0);
  await controls.enable.click();
  assert.equal(prompts, 1); assert.match(controls.status.textContent, /blocked/);
});

test('new-session muted choice survives exact request retry', async () => {
  const context = {URLSearchParams}; vm.runInNewContext(source('preparation.js'), context);
  const storage = new Map();
  const saved = {getItem: key => storage.get(key) || null, setItem: (key, value) => storage.set(key, value), removeItem: key => storage.delete(key)};
  const bodies = [];
  const fields = {name: 'example', goal: 'work', date: '2026-10-14', model: '', effort: '', team: '', catalogDigest: '', browserNotificationsEnabled: false};
  const draft = context.sessionPreparation.createRequestDraft({storage: saved, fields, randomUUID: () => '11111111-1111-4111-8111-111111111111', fetch: async (url, options = {}) => {
    if (options.body) bodies.push(options.body); throw new Error('network lost');
  }});
  await assert.rejects(draft.submit([], false));
  assert.equal(new URLSearchParams(bodies[0]).get('browserNotificationsEnabled'), 'false');
  assert.equal(draft.draft.browserNotificationsEnabled, false);
  const recovered = context.sessionPreparation.createRequestDraft({storage: saved, fields: {...fields, browserNotificationsEnabled: true}, fetch: async (url, options = {}) => {
    if (!options.body) return {status: 404}; bodies.push(options.body); throw new Error('network lost');
  }});
  await assert.rejects(recovered.submit([], false)); assert.equal(bodies[1], bodies[0]);
});

test('visible focus acknowledges only observed events and keeps stale reservations', async () => {
  const listeners = {}, timers = [], records = new Map(); let focus = false, failReservations = false;
  let current = event();
  const document = {body: {dataset: {session: 'example', selectedMember: 'implementer0', sessionObservation: identity, rootThreadId: 'thread-1'}}, title: 'example · Workspace', visibilityState: 'visible',
    hasFocus: () => focus, getElementById: () => null, addEventListener: (name, callback) => listeners[name] = callback};
  const context = {document, window: {addEventListener: (name, callback) => listeners[name] = callback},
    URL, AbortController, setTimeout: callback => { timers.push(callback); return timers.length; }, clearTimeout() {},
    navigator: {}, workspaceAttentionStore: {update: async (key, change = value => value) => {
      const next = change(records.get(key) || {identity: key, seen: [], revision: 0}); records.set(key, next); return next;
    }}, fetch: async url => {
      if (url.endsWith('/attention')) return {ok: true, json: async () => ({version: 1, identity, rootThread: 'thread-1', event: current, revision: current?.revision || 1, fresh: true, enabled: true})};
      if (failReservations) throw new Error('coordinator unavailable');
      return {ok: true, json: async () => ({reservationHolders: [{slug: 'example', observationIdentity: identity, machines: [{machine: 'one', state: 'recovery_hold'}]}]})};
    },
  };
  const settle = async () => { for (let i = 0; i < 30; i++) await Promise.resolve(); };
  vm.runInNewContext(source('session-attention.js'), context); await settle();
  assert.equal(document.title, '? R example · Workspace'); assert.deepEqual(records.get(identity).seen, []);
  focus = true; listeners.focus(); await settle(); assert.equal(document.title, 'R example · Workspace');
  assert.ok(records.get(identity).seen.includes(id));
  focus = false; current = {...event(2), id: 'c'.repeat(64)}; failReservations = true;
  timers.at(-1)(); await settle();
  assert.equal(document.title, '? R example · Workspace');
  assert.equal(records.get(identity).seen.includes(current.id), false, 'event after blur was not acknowledged');
  document.visibilityState = 'hidden'; focus = true; listeners.focus(); await settle();
  assert.equal(records.get(identity).seen.includes(current.id), false, 'focus alone cannot acknowledge a hidden page');
});

test('retained focused document refuses replaced directory or changed root', async () => {
  for (const next of [{identity: 'c'.repeat(64), rootThread: 'thread-1'}, {identity, rootThread: 'new-root'}]) {
    const listeners = {}, reads = [], records = new Map(), status = {}, control = {disabled: false, addEventListener(name, callback) {this[name] = callback;}};
    let presence = 0;
    const document = {body: {dataset: {session: 'example', sessionObservation: identity, rootThreadId: 'thread-1'}}, title: 'example · Workspace',
      visibilityState: 'visible', hasFocus: () => true, addEventListener: (name, action) => listeners[name] = action,
      getElementById: name => name === 'session-attention-status' ? status : control};
    const context = {document, window: {addEventListener: (name, action) => listeners[name] = action},
      navigator: {}, AbortController, setTimeout: () => 1, clearTimeout() {},
      workspaceAttentionStore: {update: async (key, change = value => value) => { const value = change({identity: key, seen: [], revision: 0}); records.set(key, value); return value; }},
      workspaceBrowserNotifications: {presence: async () => presence++},
      fetch: async (url, options = {}) => {reads.push({url, options}); return {ok: true, json: async () => ({version: 1, ...next, fresh: true, enabled: true, event: {...event(), identity: next.identity}, revision: 1})};},
    };
    vm.runInNewContext(source('session-attention.js'), context);
    for (let i = 0; i < 20; i++) await Promise.resolve();
    assert.equal(status.textContent, 'This session changed. Reload this page to continue.');
    assert.equal(control.disabled, true); assert.equal(records.size, 0); assert.equal(presence, 0);
    await control.change(); listeners.focus(); listeners.pageshow();
    for (let i = 0; i < 20; i++) await Promise.resolve();
    assert.equal(reads.length, 1, 'mismatch stops later reads/settings');
    assert.equal(records.size, 0, 'replacement was never acknowledged');
  }
});

test('lost registration reply and push-key mismatch expose disable recovery', async () => {
  for (const scenario of ["lost-reply", "key-mismatch", "lost-storage"]) {
    const keyMismatch = scenario === "key-mismatch";
    const controls = Object.fromEntries(['status', 'enable', 'disable', 'test'].map(name => [name, {disabled: false, addEventListener(type, callback) {this[type] = callback;}}]));
    const calls = [], storage = new Map(); let subscribed = scenario !== "lost-reply", registered = scenario === "lost-storage", loseReply = scenario === "lost-reply", unsubscribed = 0;
    const subscription = {options: keyMismatch ? {applicationServerKey: new Uint8Array([1]).buffer} : {},
      toJSON: () => ({endpoint: 'https://fcm.googleapis.com/private-endpoint', keys: {p256dh: 'public', auth: 'auth'}, expirationTime: null}),
      unsubscribe: async () => {unsubscribed++; subscribed = false; return true;}};
    const registration = {pushManager: {getSubscription: async () => subscribed ? subscription : null,
      subscribe: async () => {subscribed = true; return subscription;}}};
    const context = {document: {getElementById: () => ({querySelector: selector => controls[selector.match(/notification-(\w+)/)[1]]})},
      navigator: {serviceWorker: {getRegistration: async () => registration, register: async () => registration, ready: Promise.resolve(registration)}},
      Notification: {permission: 'granted', requestPermission: async () => 'granted'}, PushManager: function() {}, isSecureContext: true,
      AbortController, setTimeout, clearTimeout, atob, Uint8Array,
      localStorage: {getItem: key => storage.get(key) || null, setItem: (key, value) => storage.set(key, value), removeItem: key => storage.delete(key)},
      fetch: async (url, options = {}) => {
        const body = options.body && JSON.parse(options.body); calls.push({url, body});
        if (url.endsWith('/register')) {registered = true; if (loseReply) {loseReply = false; throw Error('lost reply');} return {ok: true, json: async () => ({registrationId: 'browser-id'})};}
        if (url.endsWith('/disable')) {assert.equal(body.registrationId, 'browser-id'); registered = false; return {ok: true, json: async () => ({ok: true})};}
        return {ok: true, json: async () => ({available: true, publicKey: 'Ag', registered: false})};
      },
    };
    vm.runInNewContext(source('browser-notifications.js'), context);
    for (let i = 0; i < 20; i++) await Promise.resolve();
    if (scenario !== "lost-storage") await controls.enable.click();
    assert.equal(controls.status.textContent, 'Browser setup is incomplete. Disable it or enable notifications again.');
    assert.equal(controls.disable.disabled, false); assert.equal(subscribed, true);
    await controls.disable.click();
    assert.equal(unsubscribed, 1); assert.equal(registered, false);
    assert.match(controls.status.textContent, /^Disabled on this browser/);
    assert.equal(calls.filter(call => call.url.endsWith('/register')).length, scenario === "lost-reply" ? 2 : 1);
  }
});
