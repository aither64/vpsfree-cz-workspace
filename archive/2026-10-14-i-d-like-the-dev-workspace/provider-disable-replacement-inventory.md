# Frozen replacement-cleanup remedy inventory

Exact frozen head: `b8a6be26a75347dcc9ec0fd1330dff886e47c93f`. Registered worktree clean. Push held.
Final upstream base/sole parent: `ba8669b14536f72b559abc912bba8eac430111e4`.
Previous affected-review head: `1a57ae9a038516fd4e435591ea3853de098fa8fb`.

## Complete branch series and paths

```text
b8a6be26a75347dcc9ec0fd1330dff886e47c93f portal: show session attention and deliver background Web Push
```

```text
A	docs/browser-notifications-operations.md
A	docs/browser-notifications.md
M	docs/workspace-portal.md
M	libexec/dev-session
M	libexec/workspace-host
M	nix/workspace-portal.nix
M	portal/go.mod
M	portal/go.sum
A	portal/internal/web/attention.go
A	portal/internal/web/attention_browser_test.cjs
A	portal/internal/web/attention_test.go
M	portal/internal/web/browser_contract_test.cjs
M	portal/internal/web/creation.go
M	portal/internal/web/creation_store.go
A	portal/internal/web/notifications.go
A	portal/internal/web/notifications_browser_test.cjs
A	portal/internal/web/notifications_browser_test.go
A	portal/internal/web/notifications_store.go
A	portal/internal/web/notifications_test.go
A	portal/internal/web/notifications_transport.go
M	portal/internal/web/preparation.go
M	portal/internal/web/preparation_store.go
M	portal/internal/web/preparation_test.go
M	portal/internal/web/server.go
M	portal/internal/web/static/app.js
A	portal/internal/web/static/browser-notifications.js
A	portal/internal/web/static/notification-worker.js
M	portal/internal/web/static/preparation.js
A	portal/internal/web/static/session-attention-store.js
A	portal/internal/web/static/session-attention.js
M	portal/internal/web/templates/index.html
A	portal/internal/web/templates/notifications.html
M	portal/internal/web/templates/session.html
M	portal/internal/web/uploads.go
M	test/dev_session/agent_team_creation_test.rb
M	test/workspace_host/agent_team_registration_test.rb
```

```text
 docs/browser-notifications-operations.md           | 105 ++++
 docs/browser-notifications.md                      | 127 +++++
 docs/workspace-portal.md                           |   9 +
 libexec/dev-session                                |   5 +-
 libexec/workspace-host                             |   2 +
 nix/workspace-portal.nix                           |   7 +-
 portal/go.mod                                      |   3 +
 portal/go.sum                                      |  74 ++-
 portal/internal/web/attention.go                   | 236 +++++++++
 portal/internal/web/attention_browser_test.cjs     | 399 +++++++++++++++
 portal/internal/web/attention_test.go              | 253 ++++++++++
 portal/internal/web/browser_contract_test.cjs      |   2 +-
 portal/internal/web/creation.go                    |   4 +
 portal/internal/web/creation_store.go              |  45 +-
 portal/internal/web/notifications.go               | 542 +++++++++++++++++++++
 portal/internal/web/notifications_browser_test.cjs |  52 ++
 portal/internal/web/notifications_browser_test.go  |  60 +++
 portal/internal/web/notifications_store.go         | 218 +++++++++
 portal/internal/web/notifications_test.go          | 532 ++++++++++++++++++++
 portal/internal/web/notifications_transport.go     | 106 ++++
 portal/internal/web/preparation.go                 |   9 +-
 portal/internal/web/preparation_store.go           |  21 +-
 portal/internal/web/preparation_test.go            |   2 +-
 portal/internal/web/server.go                      |  75 ++-
 portal/internal/web/static/app.js                  |  11 +-
 .../internal/web/static/browser-notifications.js   | 180 +++++++
 portal/internal/web/static/notification-worker.js  |  80 +++
 portal/internal/web/static/preparation.js          |  11 +-
 .../internal/web/static/session-attention-store.js |  32 ++
 portal/internal/web/static/session-attention.js    | 103 ++++
 portal/internal/web/templates/index.html           |   7 +-
 portal/internal/web/templates/notifications.html   |   8 +
 portal/internal/web/templates/session.html         |  17 +-
 portal/internal/web/uploads.go                     |   3 +
 test/dev_session/agent_team_creation_test.rb       |  31 ++
 .../workspace_host/agent_team_registration_test.rb |  42 ++
 36 files changed, 3349 insertions(+), 64 deletions(-)
```

The own branch is still one feature commit. The old unmerged/undeployed heads
were amended, preserving no obsolete functional or dependency/hash boundary.
Source imports, module declarations and source-derived Nix vendoring remain in
the same owning commit. This remedy changes no Go/API/provider code, external
imports, modules, vendorHash, flake inputs or Codex pin. The validated vendor hash
remains `sha256-iyydGWryLmh8P+YxQcQ2SqGIj1Lds+WBDgsKQV4uFqA=`.

## Exact remedy from affected-review head

```text
M	docs/browser-notifications-operations.md
M	docs/browser-notifications.md
M	portal/internal/web/attention_browser_test.cjs
M	portal/internal/web/static/browser-notifications.js
```

[Exact narrow patch](provider-disable-replacement-remedy.patch), SHA-256
`8306e0b6fdd5a1115fe405ae6a2ac636d429fb244248da68048fc709441a0f66`.

A current subscription is always bound to its endpoint digest, independently
of a saved ID that may refer to an earlier subscription. Disable confirms these
fixed two server obligations independently, retains any failed selector across
reload and verifies local absence before reporting fully disabled. Existing
ID-only selector receipts avoid duplicate requests. No general selector list or
queue is introduced.

Enable with a confirmed different registration ID retires the prior saved ID
before overwriting it. Failure or a lost deletion response leaves the prior ID
and current digest for explicit Disable retry. A successful old-ID deletion
allows saving the new ID normally. No automatic load cleanup or unsubscribe is
added to Enable. All UI strings reuse previously approved copy.

## Finding disposition and verification

The Important finding in [provider-disable-review.md](provider-disable-review.md)
is fixed within the accepted narrow recommendation. The lead also explicitly
accepted the closely related successful-replacement path. Main-agent final copy
passes approved the complete current two-doc diff, including the exact retirement
paragraph, before amendment. No confirmation review or long/provider operation
was started by the implementer.

[Final focused evidence](provider-disable-replacement-quick.log),
[status](provider-disable-replacement-quick.status): PASS. Cached declared Nix
environment, Go 1.26.6, GOMODCACHE=/tmp/session-webpush-mod,
GOCACHE=/tmp/session-attention-go-build, GOFLAGS=-mod=readonly, GOPROXY=off;
PORTAL_BROWSER_TEST absent:

```sh
# Registered runtime worktree:
node --check portal/internal/web/static/browser-notifications.js
node portal/internal/web/attention_browser_test.cjs
# portal/:
go test -mod=readonly ./internal/web -run '^Test(Attention|Notifications)' -count=1
# Runtime worktree:
git diff --check
```

All 15 actual-module Node contracts pass, including the prior 13 behaviors,
stale saved ID plus lost replacement response, each selector deletion failure,
reload/retry, server registration/outbox truth, and confirmed replacement with
normal/failed/lost old-ID retirement. Go passes in 0.443 seconds (7.207 seconds
including compilation). Only focused quick checks ran; no browser/provider test
or long suite was launched. Repository hook declarations remain absent; no hook
was bypassed.

## Formats and migration provenance

No migrations. Private notification schema remains initial version 1; there is
no server conversion, index or schema amendment. Optional strict creation-receipt
booleans and capable-helper pairing remain as previously reviewed. The same
bounded origin-local cleanup key holds one ID/digest selector; the existing
registration-ID key independently retains the prior ID until deletion is
confirmed. No new local key or selector-list format is introduced by this remedy.

Per lead direction, the feature and predecessor own heads remain unmerged and
undeployed, with no real product private state to migrate. Disposable probe
state/profiles were isolated test evidence, not a supported product predecessor.
Old probe copies and runs remain immutable evidence. The prepared final-native
fixture at 1a57ae9a is superseded as current-source evidence and is preserved;
a fresh exact-head native fixture is prepared separately, without executing it.

Remaining: direct lead remedy verification, lead-owned publication/composition
refresh and authorized long/native verification. Push stays held. No merge,
deployment, reservation or session lifecycle action was performed.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
