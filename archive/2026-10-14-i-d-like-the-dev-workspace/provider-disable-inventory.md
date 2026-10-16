# Provider and Disable amendment inventory

Current frozen runtime head: `1a57ae9a038516fd4e435591ea3853de098fa8fb`. Registered worktree is clean.
Base: `ba8669b14536f72b559abc912bba8eac430111e4`. Previous published feature head: `e414ed31806d2b91620d5e5fad8b5b5ee56e07ac`.
One owning feature commit remains; no merge or push was performed.

## Whole branch series

```text
1a57ae9a038516fd4e435591ea3853de098fa8fb portal: show session attention and deliver background Web Push
```

The dependency declarations, source imports and Nix vendor hash remain in this
single feature commit because Nix vendoring follows source imports. This
amendment adds only standard-library SHA-256 usage; go.mod, go.sum, vendorHash,
flake inputs and Codex protocol pins are unchanged from the previous head.

No migrations. The initial private notification schema remains version 1;
no product state from this feature has been merged, released or deployed in
this initiative. Earlier real-provider probes used private disposable fixtures
and fresh profiles, then removed those fixtures. They are verification evidence,
not a supported persisted product-state predecessor. The browser now retains
one origin-local bounded cleanup selector under the existing storage-key family;
it contains an ID or digest, never endpoint/key data. Existing ID-only deletion
clients remain supported. No new server private schema/index is introduced.
The final affected provider/API security review is still owned by the lead.

## Amendment paths

```text
M	docs/browser-notifications-operations.md
M	docs/browser-notifications.md
M	portal/internal/web/attention_browser_test.cjs
M	portal/internal/web/notifications.go
M	portal/internal/web/notifications_browser_test.cjs
M	portal/internal/web/notifications_test.go
M	portal/internal/web/notifications_transport.go
M	portal/internal/web/static/browser-notifications.js
```

Exact amendment diff: [provider-disable-amendment.patch](provider-disable-amendment.patch)
SHA-256: `7e878b6d7e8246e561c4a4c2e1d29851a9c39082d18741666bf12491d27f9f30`.

## Complete base-to-head paths

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

## Complete base-to-head diffstat

```text
 docs/browser-notifications-operations.md           |  98 ++++
 docs/browser-notifications.md                      | 125 +++++
 docs/workspace-portal.md                           |   9 +
 libexec/dev-session                                |   5 +-
 libexec/workspace-host                             |   2 +
 nix/workspace-portal.nix                           |   7 +-
 portal/go.mod                                      |   3 +
 portal/go.sum                                      |  74 ++-
 portal/internal/web/attention.go                   | 236 +++++++++
 portal/internal/web/attention_browser_test.cjs     | 311 ++++++++++++
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
 .../internal/web/static/browser-notifications.js   | 158 ++++++
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
 36 files changed, 3230 insertions(+), 64 deletions(-)
```

## Verification and copy pass

Main-agent final copy approval arrived before this amendment commit, covering
the owning notification docs, official Chromium references and all UI strings.
No additional visible wording was introduced. Repository instructions and flake
declare no hook framework; no executable pre-commit hook was present, and no
hook was bypassed.

[Focused quick evidence](provider-disable-quick.log),
[status](provider-disable-quick.status): PASS. In the cached declared Nix
environment, with GOMODCACHE=/tmp/session-webpush-mod,
GOCACHE=/tmp/session-attention-go-build, GOFLAGS=-mod=readonly and GOPROXY=off:

```sh
# From the registered runtime worktree:
node --check portal/internal/web/static/browser-notifications.js
node --check portal/internal/web/notifications_browser_test.cjs
node portal/internal/web/attention_browser_test.cjs
# From portal/, with PORTAL_BROWSER_TEST absent:
go test -mod=readonly ./internal/web -run '^Test(Attention|Notifications)' -count=1
# From the runtime worktree:
gofmt -l portal/internal/web/notifications.go portal/internal/web/notifications_transport.go portal/internal/web/notifications_test.go
git diff --check
```

All 13 browser contracts pass, including lost registration reply/ID, offline and
denied deletion with successful local removal, reload/explicit retry, retained
known IDs, normal removal, false unsubscribe with verified absence, local failure
and uncertain local absence. The Go filter passes in 0.416 seconds (7.205 seconds
including compilation), covering strict selectors, origin/registration/outbox
scope, idempotence, current package admission and exact provider/deceptive-host
validation with existing transport guards. No real browser/provider or long suite
was launched. A first targeted Go command was accidentally started from the
repository root and found no module; the same check then passed from portal/.

Remaining: lead direct verification, affected retained independent API/provider
review, then lead-owned publication and longer/provider verification. Push is
held. Deployment/lifecycle/reservation ownership remains with the lead. Browser
storage failure can prevent persisting a cleanup selector; in-memory retry is
retained and local unsubscribe is still attempted, as documented.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
