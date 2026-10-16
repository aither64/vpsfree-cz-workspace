# Registration diagnostic probe

Prepared only; no diagnostic provider/browser run by implementer0. The first
probe, its source copy and `../run/` evidence remain unchanged. Its exit status
was zero, but neither browser reached delivery. Chromium reported an incomplete
local subscription; Firefox reported registration failure. That evidence alone
does not identify a product defect or a headless-browser limitation.

This separate disposable copy again starts from committed runtime
`e414ed31806d2b91620d5e5fad8b5b5ee56e07ac`. Only the Go/CJS notification browser
fixture files change. No registered source, branch or product behavior is edited.

## Exact lead watcher command

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/push-provider-probe/diagnostic/run.sh
```

Run once through a fresh dev-session-monitor watcher or its visible fallback.
The runner retains the declared tools/caches and refuses an existing `run/`.
Read `run/results.json`, `run/go-test.log` and `run/status`; exit zero only means
the diagnostic sequence completed. Do not rerun blindly. Return evidence to the
lead before making any product change.

## Added observations

The Go fixture forwards the shipped register, disable and test handlers. A
response-writer wrapper retains at most 4096 response bytes in memory and maps
only known constant product errors to fixed categories. The bytes themselves
are never exposed. It records HTTP status, action, unchanged host-profile and
provider admission, exact host/origin matches, before/after registration counts
and the store failure flag. A mutex protects at most 24 diagnostic records.
The read-only fixture summary exposes those sanitized records and counts.

The browser listens for statuses on the four fixed notification API routes.
Transparent wrappers call the real service-worker registration,
`PushManager.subscribe` and `getSubscription` with the original receiver and
arguments, preserve native fulfillment/rejection, and record only stage,
outcome and allowlisted error name/category. A successful subscription is
inspected for validation booleans: provider allowlist, HTTPS/port/path shape,
key lengths/padding and expiration type/future status. No endpoint, key or
expiration value is retained in diagnostics. Storage wrappers record whether
the registration ID was saved and read back successfully, without recording
its value. Cleanup captures these observations and server counts even if the
shipped Disable action fails.

The original probe's actual transport, ten-second Test action, eighteen-second
zero-portal-tab delivery window, fresh browser profiles and scoped cleanup are
retained. The shipped service worker, encryption, guarded push transport,
registration validation and `showNotification` remain unchanged. There is no
synthetic fallback or activity reconciliation. No macOS or OS display claim is
made from Linux/headless evidence.

## Static trace and interpretation

`browserNotificationsAPI` first checks the current package/provider admission,
then exact host and POST origin. It decodes an 8192-byte request with unknown
fields rejected and one JSON value required. The request uses
`expirationTime: *int64`; native browser expiration shape is now observed
without changing it. Validation then checks the exact provider endpoint,
uncompressed P-256 public key, 16-byte authentication secret and expiry before
atomically saving the registration. The shipped browser sends only endpoint
and keys inside subscription, plus the separate expiration field. It saves the
returned ID only after the register API succeeds.

Use the diagnostic records to distinguish these cases:

- Native subscribe rejects and no register request: inspect its fixed error
  category. A granted Notifications permission alone does not establish a
  working Push service.
- Register returns non-2xx: use the server category and admission/origin/shape
  booleans. Do not weaken guards to make the probe pass.
- Register succeeds and the store count increases, but storage save/readback
  fails: this is a browser registration-state failure after server admission.
- Local subscription exists but register was rejected: Disable re-registers
  through the same existing contract, so the same refusal may prevent cleanup.
  The diagnostic fixture/profile cleanup remains isolated from real sessions.

No product defect is confirmed by the initial result. Any confirmed product
issue must go to the lead before changing the frozen application.

`adaptation.patch` compares against the committed fixture;
`diagnostic-increment.patch` compares against the first disposable adaptation.
`source-sha256.txt` pins every copied source file. Preparation evidence is in
`preparation-checks.log/status`; compilation selects no tests and launches no
server or browser.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
