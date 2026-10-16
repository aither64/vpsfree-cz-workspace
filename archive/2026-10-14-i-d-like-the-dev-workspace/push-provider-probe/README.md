# Disposable provider probe

Prepared against committed runtime
`e414ed31806d2b91620d5e5fad8b5b5ee56e07ac`. The registered runtime worktree and
branch remain unchanged. This is a verification fixture, not a product patch.
The actual provider/browser operation has **not been run** by implementer0.

The source copy came from `git archive` of that exact commit. Only
`portal/internal/web/notifications_browser_test.go` and
`portal/internal/web/notifications_browser_test.cjs` differ. See
`adaptation.patch`, `provenance.json` and the complete `source-sha256.txt`
manifest. The prepared Go/CJS files are also retained beside the copy.

## Lead watcher command

Run once with the lead's fresh verification watcher under the
dev-session-monitor skill, or its visible fallback. The member shell cannot
listen on TCP, so it has only performed the preparation checks below.

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/push-provider-probe/run.sh
```

The runner uses the cached declared Nix environment, Go module/build caches and
pinned Playwright Chromium/Firefox bundle. It verifies the copied source
manifest and refuses to overwrite an existing `run/`. It writes the exact Go
exit status to `run/status`, sanitized output to `run/go-test.log`, and
progressive evidence to `run/results.json`. Start/finish timestamps are saved
beside them. No Nix daemon operation or dependency download is requested.

Watch only this command. Do not retry, modify source, deploy or operate any real
session. A subscription failure is an incomplete diagnostic outcome, not a
request to manufacture a subscription or push. Return the exit status and
sanitized per-browser evidence to the lead. A zero exit status means the probe
finished recording outcomes; inspect the evidence fields before claiming
delivery. A browser close/profile cleanup failure also remains explicit in the
result. Retain the artifacts.

## What the adaptation exercises

The fixture uses its existing temporary workspace, private notification store,
VAPID keys, APIs and shipped `guardedPushClient`. A one-second ticker invokes
only `n.sendNext` to service the explicit Test action. It never starts activity
reconciliation. The isolated attention response contains the fixture identity
and no event. Coordination reports no reservations. A read-only summary exposes
only registration/outbox counts.

Each engine gets a newly created persistent disposable browser profile. The
harness grants the browser notification permission, then clicks the shipped
Enable button. `pushManager.subscribe`, encryption, provider transport, worker
code and `showNotification` are unmocked. Chromium retains background networking
and permits the fixture's local test certificate. Firefox uses Playwright's
supported permission grant; unavailable permission or subscription is recorded
without substituting a fake path.

After successful registration the harness clicks Send test notification through
the shipped UI, verifies the ten-second queued message, closes every portal tab
and keeps an `about:blank` tab active. It waits eighteen seconds, reopens the
portal and records independent evidence:

- `providerAccepted`: the shipped API reports `provider_accepted`.
- `workerReceiptVerified`: real IndexedDB test-event records increased.
- `browserNotificationRecordVerified`: real `getNotifications()` test records
  increased. The harness does not override that method or `showNotification`.
- `zeroPortalTabsVerified`: all origin pages were closed during the wait while
  the browser remained running with `about:blank` active.

These are Linux/headless observations. OS display, macOS display, notification
click behavior and delivery while a fully quit browser are not established by
this probe. Provider acceptance alone does not prove worker receipt or display.
Reopening occurs only after the zero-tab delivery window.

## Data and cleanup

Subscription endpoints, keys, registration IDs and payloads never enter the
output artifacts. Errors are reduced to fixed error names and result codes;
protocol debug logging is unset. Fixture state remains in Go test temporary
directories and browser data in newly allocated temporary profiles.

Cleanup uses the shipped Disable action for this fixture's registration,
checks that its subscription is absent and server registrations are zero,
closes its test notifications, then closes the browser and removes only that
newly allocated profile. If closing fails, the profile is retained and the
failure is recorded. Go cleans its own fixture directories on return. No real
session, host, machine reservation, lifecycle or production registration is
accessed.

## Preparation checks

See `preparation-checks.log` and `preparation-checks.status`. The checks validate
shell/JavaScript syntax, Go formatting and compilation with no tests selected.
They do not start the TLS fixture or launch a browser.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
