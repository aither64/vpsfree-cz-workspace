# Actual provider verification

Disposable fixture provenance: exact committed runtime e414ed3 archives, only
browser test Go/CJS adaptations. Registered source remained clean. Private keys,
endpoint capabilities and subscription IDs never enter logs. Profiles/temp
fixture state belong only to this test. OS display on macOS is not established.

Initial headless run and diagnostic run each completed with no provider delivery;
zero process status meant completed diagnostics only. Diagnostic distinguished
Chromium registration refusal (unsupported endpoint host, valid key/expiry and
origin/admission) from Firefox native getSubscription AbortError. Installed
Playwright Firefox playwright.cfg explicitly sets dom.push.serverURL empty and
connection.enabled false, so it could not establish native provider compatibility.

Headed native run restores Mozilla's wss://push.services.mozilla.com/ connection
in a new disposable profile and uses owned Xvfb. It completed68.499s with Xvfb/test
reaped, browser profiles closed/removed. Exact artifacts:
push-provider-probe/native/run/results.json and runner-summary.json.

- Firefox148.0.2: real updates.push.services.mozilla.com subscription, registration
  and delayed test accepted. Every portal tab closed; about:blank remained active.
  Real provider result provider_accepted; real worker IndexedDB test receipt1
  after window (before0). This proves zero-tab provider-to-worker delivery.
  getNotifications returned0 in Xvfb, so no browser record or OS display claim.
  Shipped Disable succeeded; registrations/pending/local subscription all zero.
- Chromium147.0.7727.15: actual native subscription endpoint host jmt17.google.com.
  HTTPS/keys/null expiry valid; server refused400 unsupported_endpoint. No server
  registration or pending delivery persisted. Shipped Disable also refused while
  trying to recover registration, so local unsubscribe did not complete; allocated
  profile closed/removed. No provider/worker delivery claimed.

Official Chromium main source inspected by lead:
https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/push_messaging/push_messaging_constants.cc
https://chromium.googlesource.com/chromium/src/+/refs/heads/main/components/push_messaging/push_messaging_utils.cc
Constants declare jmt17.google.com as the staging GCM push endpoint. Utility
selects staging for channels other than STABLE (unless Webpush-path feature uses
the fcm.googleapis.com preprod route). Architect assigned to verify exact version
and decide the smallest provider/cleanup amendment. No wildcard acceptance or
product edit made. Two unadmitted activation jobs canceled pending this decision;
foreign integration-performance review hold continues. No own live activation.

## Final amended native run at b8a6be26

Exact committed runtime b8a6be26a75347dcc9ec0fd1330dff886e47c93f, fresh archive and approved fixture-only adaptation. Command: bash push-provider-probe/native-b8a6be26a753/run.sh. Linux headed Xvfb, owned exact display process; 86.6 seconds, runner/Go exit0. Separate result interpretation below; exit0 alone is not delivery proof.

- Chromium147.0.7727.15: real jmt17.google.com subscription/registration accepted. Delayed shipped Test action; all portal tabs closed for18seconds with about:blank active. Provider accepted, worker test receipt0→1, browser notification/test record0→1. This proves native zero-tab provider-to-worker delivery and a browser notification record.
- Firefox148.0.2: real Mozilla subscription/registration accepted under normal push prefs. Same zero-tab window; provider accepted, worker test receipt0→1. Browser notification record remained0 under Xvfb, so the harness labels delivery_incomplete. Worker delivery is proved; physical/macOS display remains unproved. No application defect inferred from absent virtual-display record.
- Both engines: shipped Disable confirmed server registrations/outbox0 and local subscription absent. Own profiles closed/removed. Runner reaped its exact Go and Xvfb children. No product session/state, reservation or live deployment touched.

Artifacts: push-provider-probe/native-b8a6be26a753/run/results.json, runner-summary.json, go-test.log/status, timestamps and full source/provenance checksums. No synthetic push, endpoint rewriting or guard bypass. No OS/macOS display or actual click claim; synthetic worker click/auth contracts are separate earlier evidence.
