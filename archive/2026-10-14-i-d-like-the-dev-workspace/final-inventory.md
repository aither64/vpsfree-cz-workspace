# Final runtime and deployment composition inventory

Runtime substantive final review: reviewer0 Sol/xhigh, all four lanes, ba8669b..a7000a2. All six findings directly remediated/verified by lead under the narrow-fix policy; see review.md and review-dispositions.md. This packet requests final complete-history/migration/composition conclusions, not a full source re-review.

## dev-workspace

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace`
- Initial registered base: `92b2576d82a850fa4e24f889a8ff592a1e7f3e42`
- Current fetched review/feature base: `ba8669b14536f72b559abc912bba8eac430111e4`
- Exact final head: `e414ed31806d2b91620d5e5fad8b5b5ee56e07ac`
- Merge base: `ba8669b14536f72b559abc912bba8eac430111e4`
- Tracked worktree status: `clean`
- Final diff: [dev-workspace-consolidated-final.diff](dev-workspace-consolidated-final.diff), SHA256 `51ac2686e712b9a9daed6267e2b59ee645fae48e1a9aa984df829c86e3cfa7b0`

### Complete own feature series

```text
e414ed31806d2b91620d5e5fad8b5b5ee56e07ac
portal: show session attention and deliver background Web Push

Surface unseen blocking requests, successful settled lead responses and
persistent machine reservations in the session title. Visible focused
visits acknowledge browser-local attention without changing conversations
or coordinator ownership. Retained documents refuse changed session roots
or incarnations, and relevant unread events survive observer restarts.

Observe sessions on the server and persist event baselines with a bounded
outbox. Send standard encrypted Web Push through checked provider transport
and display it through a root service worker when no portal tabs are open.
Keep browser subscription actions explicit and session mute server-side;
retain private VAPID material through package changes.

Package webpush-go with its source imports: Nix vendoring derives the module
closure from source usage, so dependency declarations and the vendor hash
are inseparable from the observer and sender that introduce those imports.

New private notification state starts at schema 1. Creation preferences are
optional strict booleans: old omitted receipts remain valid, while newly
flagged receipts require the capable bundled helper and forward recovery.
Lifecycle journals, roster formats and Codex protocol pins remain intact.

```

### Complete initial registration base-to-head ancestry

```text
273a08c sessions: keep sensitive session records local
ba8669b portal: clarify sensitive session controls and status
e414ed3 portal: show session attention and deliver background Web Push
```

### Final diff inventory

```text
 docs/browser-notifications-operations.md           |  70 +++
 docs/browser-notifications.md                      | 122 +++++
 docs/workspace-portal.md                           |   9 +
 libexec/dev-session                                |   5 +-
 libexec/workspace-host                             |   2 +
 nix/workspace-portal.nix                           |   7 +-
 portal/go.mod                                      |   3 +
 portal/go.sum                                      |  74 ++-
 portal/internal/web/attention.go                   | 236 ++++++++++
 portal/internal/web/attention_browser_test.cjs     | 207 +++++++++
 portal/internal/web/attention_test.go              | 253 +++++++++++
 portal/internal/web/browser_contract_test.cjs      |   2 +-
 portal/internal/web/creation.go                    |   4 +
 portal/internal/web/creation_store.go              |  45 +-
 portal/internal/web/notifications.go               | 505 +++++++++++++++++++++
 portal/internal/web/notifications_browser_test.cjs |  51 +++
 portal/internal/web/notifications_browser_test.go  |  60 +++
 portal/internal/web/notifications_store.go         | 218 +++++++++
 portal/internal/web/notifications_test.go          | 436 ++++++++++++++++++
 portal/internal/web/notifications_transport.go     | 103 +++++
 portal/internal/web/preparation.go                 |   9 +-
 portal/internal/web/preparation_store.go           |  21 +-
 portal/internal/web/preparation_test.go            |   2 +-
 portal/internal/web/server.go                      |  75 ++-
 portal/internal/web/static/app.js                  |  11 +-
 .../internal/web/static/browser-notifications.js   | 103 +++++
 portal/internal/web/static/notification-worker.js  |  80 ++++
 portal/internal/web/static/preparation.js          |  11 +-
 .../internal/web/static/session-attention-store.js |  32 ++
 portal/internal/web/static/session-attention.js    | 103 +++++
 portal/internal/web/templates/index.html           |   7 +-
 portal/internal/web/templates/notifications.html   |   8 +
 portal/internal/web/templates/session.html         |  17 +-
 portal/internal/web/uploads.go                     |   3 +
 test/dev_session/agent_team_creation_test.rb       |  31 ++
 .../workspace_host/agent_team_registration_test.rb |  42 ++
 36 files changed, 2903 insertions(+), 64 deletions(-)
```

## workspace

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/workspace`
- Initial registered base: `6415d3ac2fa5bbd67994bfb25fc2c1f12c270a38`
- Current fetched review/feature base: `e9202f88e94cf5dddd86174df5388fa015a74245`
- Exact final head: `988752b7e082a3829fee2b274739c2daa71458a9`
- Merge base: `e9202f88e94cf5dddd86174df5388fa015a74245`
- Tracked worktree status: `clean`
- Final diff: [workspace-consolidated-final.diff](workspace-consolidated-final.diff), SHA256 `d60dc02284629784dd6ddd550fb6686a575ef00431a72d77c90ce5e9882126c8`

### Complete own feature series

```text
988752b7e082a3829fee2b274739c2daa71458a9
inputs: select session attention and background notification runtime

Pin the reviewed portal runtime for aitherdev application deployment.
Preserve the selected extension, dependency follows and unrelated inputs;
the matching host contract is selected through configuration's existing
channel. The application remains in its workspace user profile.

```

### Complete initial registration base-to-head ancestry

```text
f45cf41e tracking: plan portal session attention indicators
18ccec1e tracking: plan session slug quality and naming recovery
31a49933 sessions: document local sensitive tracking exceptions
2f28b46e inputs: select sensitive-session review deployment
e9202f88 tracking: record portal attention implementation and final review
988752b7 inputs: select session attention and background notification runtime
```

### Final diff inventory

```text
 flake.lock | 8 ++++----
 flake.nix  | 2 +-
 2 files changed, 5 insertions(+), 5 deletions(-)
```

## vpsfree-cz-configuration

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/vpsfree-cz-configuration`
- Initial registered base: `ac00192849f682eed847a152a91978a399f0105e`
- Current fetched review/feature base: `661236f0b2cdebecafeaa0dd50bccc8634f898b2`
- Exact final head: `0a1649033f729642d3e6f486e4825095096ccea2`
- Merge base: `661236f0b2cdebecafeaa0dd50bccc8634f898b2`
- Tracked worktree status: `clean`
- Final diff: [vpsfree-cz-configuration-consolidated-final.diff](vpsfree-cz-configuration-consolidated-final.diff), SHA256 `d7efa7b8bc74a3902a0dee1c298746c6bd7f85f0b60a79d82242d01826ddac0f`

### Complete own feature series

```text
0a1649033f729642d3e6f486e4825095096ccea2
inputs: set devWorkspace to e414ed31

devWorkspace: ba8669b1 -> e414ed31
git log for ba8669b14536f72b559abc912bba8eac430111e4..e414ed31806d2b91620d5e5fad8b5b5ee56e07ac
> e414ed3 portal: show session attention and deliver background Web Push

```

### Complete initial registration base-to-head ancestry

```text
661236f0 inputs: set devWorkspace to ba8669b1
0a164903 inputs: set devWorkspace to e414ed31
```

### Final diff inventory

```text
 flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```

## Consolidation, compatibility and scope

The runtime has exactly one feature commit. Original unpublished dependency
0bddd694 and feature a7000a2 were consolidated with their narrow fixes. Nix vendor
closure follows source imports; declarations/imports/vendorHash are inseparable.
No superseded intermediate boundary remains. The final forced vendoring hash is
sha256-iyydGWryLmh8P+YxQcQ2SqGIj1Lds+WBDgsKQV4uFqA=.

Workspace has one logical nested runtime update; configuration has one generated
dev-workspace/devWorkspace channel update. Both select the same exact runtime.
No repeated update streams or retained intermediate pins. Existing upstream
sensitive behavior and tracking commits are ancestry, not additional feature
iterations. Workspace flake.lock changes only its dev-workspace node; extension,
siblings and follows are unchanged. Configuration changes only devWorkspace's
locked revision/hash/timestamp through confctl, retaining its generated message
and passing Overcommit. Deployment contract checker passes at e414ed31.

No database, lifecycle, roster or runtime-contract migrations. Private notification
schema1 is initial with no predecessor, never released/deployed/externally
consumed. Source was published only after remedies. Optional receipt boolean
supports old omitted/true/false with strict validation; paired capable Go/Ruby
readers and forward-only recovery preserve the reviewed compatibility boundary.
No obsolete schema/migration or compatibility shim remains. No codex-web pin
change (5f15b9293f9b1eef7469a34d7b2044c743160283).

Feature/operations docs live in runtime docs/browser-notifications.md and
browser-notifications-operations.md, linked from docs/workspace-portal.md.
Site procedure in configuration docs/operations/workspace-coordination-aitherdev.md
was read and remains accurate; this individual rollout lives in rollout.md.

User authorized implementation, verification and aitherdev deployment, not any
master merge or lifecycle action. No deployment yet. Runtime long integration
started only after completed review and direct remedy verification; Linux
synthetic worker/provider evidence cannot prove Firefox/macOS OS display.

## Final assertion-only refresh

Runtime e91f22f..e414ed3 changes exactly two test assertions, no product behavior
or format/dependency changes. Lead verified exact Go tests PASS1.222s and member
broader Creation/Preparation/SessionPreparation/Sensitive PASS44.017s. First
long check and CI failures investigated (verification.md); real browser/CSP and
zero-tab synthetic push had passed. New runtime/pin refs force-published with
exact leases, superseded CI already complete. Workspace pin amended; generated
configuration stream squashed and its cumulative generated changelog corrected
to the final base-to-head range. Normal Overcommit passed; no intermediate
unmerged pins remain. Earlier baseline pin updates are already merged upstream,
so they are protected ancestry, not repeated unmerged update streams. No
deployment/release/consumer boundary introduced.
