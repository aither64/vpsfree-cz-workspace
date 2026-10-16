# In-place notification worker activation: committed review inventory

Final clean runtime `e208027f006937693839e3612807db31a7ce0134`.
One NEW separate owning commit over deployed
`4ed9af55127743b7564cb4dd01d10c9f7fee5120`; no prior commit rewritten.
HOLD source publication/pins/long/browser/provider/native/host operations for
lead-owned committed affected independent review.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>

## Behavior and accepted boundary

Lead accepted architect design.md section "In-place notification-worker
activation, narrowed user requirement". New/refreshed controls update the existing
root worker. The successor installs with waitUntil(skipWaiting) and activates
with existing waitUntil(clients.claim). No tab is closed/reloaded and drafts stay
in the document. Old tabs need not retain earlier notification semantics; no
protocol/version registry, legacy activation command or fetch/cache handler added.

The client shares one update check per document, observes installing/waiting/
state/controller transitions for up to10s and confirms this document's controller
is the activated registration.active with no waiting/installing successor before
the existing bounded capability probe. An old active reply or ready promise
cannot certify a known pending successor. Listeners/timers are cleaned on terminal
state, timeout or refresh/action/page invalidation. Failed/hung updates remain
unconfirmed; refresh can check again in a new document. Existing refresh,
Test-cancellation, cleanup and current-registration ownership remain intact.

Explicit Enable still owns first registration/permission/subscription. Updating
does not unregister/resubscribe/reset keys, state or permissions. Per-session mute,
leases, sender/transport/retry/expiry and notification display contracts are
unchanged. Physical Firefox/macOS display rejection is a separate unresolved
boundary; this fix is not causal proof or a display repair claim.

## Source, copy and cache

Exact10changed paths:

- `docs/browser-notifications-operations.md`.
- `docs/browser-notifications.md`.
- `portal/internal/web/attention_browser_test.cjs`.
- `portal/internal/web/notifications_browser_test.cjs`.
- `portal/internal/web/notifications_browser_test.go`.
- `portal/internal/web/notifications_test.go`.
- `portal/internal/web/static/browser-notifications.js`.
- `portal/internal/web/static/notification-worker.js`.
- `portal/internal/web/templates/notifications.html`.
- `portal/internal/web/templates/session.html`.

The two template client includes now select browser-notifications.js?v=3;
shared store stays v2. The focused template expectation follows that selection.
Root worker URL/scope unchanged. No index panel/client restored.

Main lead directly applied vpsfree-writing/Humanizer to actual
notification-activation-copy.patch, approved all strings/docs with one exact
wording correction ("for the updated worker to control it"), now applied in
notification-activation-copy-final.patch. Queued Test keeps its first sentence
and now asks switching to another tab/app. Update copy never asks closing tabs.
Two owning guides explain automatic takeover, finite honest readiness and the
narrowed old-document contract. No new unapproved copy/control was added.

## Quick evidence and browser fixture (UNRUN)

Cached declared Node24.19.0/Go1.26.6, readonly module cache with GOPROXY=off.
notification-activation-quick-results.json and per-check log/status record:

- node portal/internal/web/attention_browser_test.cjs:37namedPASS,0failures/skips,
  command2.235s. Original attention/correlation/cleanup/refresh contracts retained.
- focused Go NotificationsPageIsSeparateFromIndex and
  SessionPageUsesPersistentSidebarAndSectionPanels:PASS, command7.566s including
  compilation of the changed actual-browser Go fixture. Browser test not run.
- changed client/worker/unit/browser JS syntax and git diff --check:PASS.

New module cases prove install/claim calls, waiting/installing->current-controller
activation, update failure/nonresponse/deadline/listener cleanup, no stale
readiness after refresh/action/page retirement, no mutation on update and sharing
an outstanding fetch before trusting an old controller. Test harness event targets
now support multiple native lifecycle listeners; forced refresh races remain real
contracts rather than overwritten fake callbacks.

Prepared actual-browser fixture adds a finite fixture-only old/old-waiting/current
worker response switch at the same root URL. No production API/helper changed.
It retains an old controlling conversation page and unsent-draft/sentinel while
serving the actual successor to a second controls page. Chromium AND Firefox
assert takeover, current-controller capability, both tabs open, no automatic
navigation/reload and preserved draft. Only Chromium uses Playwright worker
inspection and synthetic push/display for a correlated Test outcome. Firefox
claims lifecycle/controller capability only; Playwright worker enumeration is
not used there. Existing menu/spacing/hidden Settings/no-load-mutation and bounded
failure traces remain. No real browser was launched; final fixture requires
committed independent review before one exact-head watcher run.

Future lead command, only after review/finding reconciliation, from runtime:

```sh
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/runtime-dev-env.sh
export GOMODCACHE=/tmp/session-webpush-mod GOCACHE=/tmp/session-portal-go-cache GOPROXY=off
export NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules
export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers
PORTAL_BROWSER_TEST=1 go -C portal test -mod=readonly -count=1 -v ./internal/web -run '^TestNotificationsBrowser$'
```

Use a fresh watcher/fallback for this uncertain browser operation; no launch now.
No unchanged live checks, provider/native/network/SSH/HTTPS/credentials/host/Nix
daemon/queue/reservation/lifecycle operation occurred. No old probe or bundle
retargeted. Original failed-run and physical causes remain unproved.

## History, migration and deployment provenance

Full own series over integrated832d9f1:

```
96717cdeb5f733391846a95d78c117068ce77de8 portal: show session attention and deliver background Web Push
bb9e6291bec10227c961c36559fba406938f1eaa provider: retain bounded failure context before compensation
6e1d9a191724d376cad2a71f234f0e4d1c01f36f processgroup: make descendant exit assertions identity-aware
867682c3df251fbe6941ff9a667539ae1af790ec portal: move browser notifications into the workspace menu
012f6184faa62b7d476555058f1473adcd908528 portal: report correlated browser notification test outcomes
4ed9af55127743b7564cb4dd01d10c9f7fee5120 portal: remove the redundant session attention status row
e208027f006937693839e3612807db31a7ce0134 portal: activate notification workers while tabs stay open
```

The six preceding deployed/consumed commits are retained verbatim. This seventh
commit is a separate supported-behavior change, not a redundant follow-up pin.
No dependency/pin stream or migration introduced. notification-activation.patch
is the exact deployed-parent->new-head binary-capable diff, with SHA256 in the
artifact manifest. No intermediate fixes or obsolete approaches retained.

No server/private snapshot, database version/object store, receipt, API, payload,
provider subscription, VAPID or cleanup selector format changed. Existing IDBv1
optional Test fields and payloadv1 stay readable. Old loaded scripts can keep old
copy/semantics, but new/refreshed controls use current assets and fetch the new
successor even when an older waiting worker has no activation handler. Existing
capable-helper/forward-only receipt pairing and upstream capability-journal
lineage are unchanged. No downgrade/reset path is introduced. Modules/vendorHash,
server notification code, shared attention store, title observer and index are
Git-byte-unchanged from4ed.

Normal <=80-column body-file git commit, no hook bypass. Exact session/env and
saved ready workspace_write roster17 verified; applicable instructions and
documentation/handoff skills reused. Lead owns independent review, state/artifacts,
pins/publication and finite activation/verification. Session stays open.

## Diffstat and asset hashes

```
 docs/browser-notifications-operations.md           |  11 +-
 docs/browser-notifications.md                      |  15 +--
 portal/internal/web/attention_browser_test.cjs     | 112 +++++++++++++++++++--
 portal/internal/web/notifications_browser_test.cjs |  87 +++++++++++++++-
 portal/internal/web/notifications_browser_test.go  |  32 ++++++
 portal/internal/web/notifications_test.go          |   4 +-
 .../internal/web/static/browser-notifications.js   |  96 +++++++++++++-----
 portal/internal/web/static/notification-worker.js  |   1 +
 portal/internal/web/templates/notifications.html   |   2 +-
 portal/internal/web/templates/session.html         |   2 +-
 10 files changed, 311 insertions(+), 51 deletions(-)
```

- client SHA256: `9aec6ea0f3b6bf28eef642e1601ab5be0fd6d2e260119cc1c917b73b19666150`.
- worker SHA256: `49cb7a2be1cf8ec75a5332673a1fce87a0c67d55356a7a609a74ad855b01ede9`.
- shared store (unchanged): `0a8069fb721ae79e29f871010dd9b6af264fa69aec5dd97f391bbe5946b1aae5`.
