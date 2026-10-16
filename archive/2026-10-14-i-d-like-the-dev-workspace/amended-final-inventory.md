# Amended final source and composition inventory

Runtime provider/API review: provider-disable-review.md. Direct narrow remedy verification: provider-disable-dispositions.md and provider-disable-replacement-inventory.md. Earlier full runtime and composition reports remain preserved. This packet requests final mechanical pin/history/migration conclusions; no full source confirmation review is requested.


## dev-workspace

Base: `ba8669b14536f72b559abc912bba8eac430111e4`; head: `b8a6be26a75347dcc9ec0fd1330dff886e47c93f`; clean. Merge base: `ba8669b14536f72b559abc912bba8eac430111e4`. Local published feature ref: `b8a6be26a75347dcc9ec0fd1330dff886e47c93f`.

Final diff: [dev-workspace-amended-final.diff](dev-workspace-amended-final.diff), SHA256 `29690f24053238a6f45e22eeadb06098e9acadeba293f019964eae7f51c38287`.

Complete own series:
```text
commit b8a6be26a75347dcc9ec0fd1330dff886e47c93f
Author:     Jakub Skokan <jakub.skokan@havefun.cz>
AuthorDate: Wed Oct 14 23:50:14 2026 +0200
Commit:     Jakub Skokan <jakub.skokan@havefun.cz>
CommitDate: Thu Oct 15 02:43:27 2026 +0200

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
    
    Accept Chromium's exact upstream staging provider for non-stable channels.
    Disable independently removes the browser subscription and origin-scoped
    server registration; retain one deletion selector across uncertain cleanup.
    A lost registration ID uses the exact endpoint digest without registering
    again. The additive deletion API preserves ID clients and private schema 1.
    
    Retire old registration identities before replacing saved IDs. Bind
    uncertain replacement cleanup to the current endpoint digest and retain any
    old ID separately. Disable confirms both fixed server obligations and local
    absence before reporting completion.
```

Final inventory:
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


## workspace

Base: `d22b5341cc3f74336c557c0725d5b01975d2777e`; head: `e6aaa9c76ff3a0cb1d9dacca876c496e7e639b3f`; clean. Merge base: `d22b5341cc3f74336c557c0725d5b01975d2777e`. Local published feature ref: `e6aaa9c76ff3a0cb1d9dacca876c496e7e639b3f`.

Final diff: [workspace-amended-final.diff](workspace-amended-final.diff), SHA256 `4f3faa09530abe791cfdc2f556b6a738f0742a01e76e098298e021aff4fa748d`.

Complete own series:
```text
commit e6aaa9c76ff3a0cb1d9dacca876c496e7e639b3f
Author:     Jakub Skokan <jakub.skokan@havefun.cz>
AuthorDate: Thu Oct 15 00:20:58 2026 +0200
Commit:     Jakub Skokan <jakub.skokan@havefun.cz>
CommitDate: Thu Oct 15 02:45:36 2026 +0200

    inputs: select session attention and background notification runtime
    
    Pin the reviewed portal runtime for aitherdev application deployment.
    Preserve the selected extension, dependency follows and unrelated inputs;
    the matching host contract is selected through configuration's existing
    channel. The application remains in its workspace user profile.
```

Final inventory:
```text
flake.lock | 8 ++++----
 flake.nix  | 2 +-
 2 files changed, 5 insertions(+), 5 deletions(-)
```


## vpsfree-cz-configuration

Base: `661236f0b2cdebecafeaa0dd50bccc8634f898b2`; head: `c4fb5da44733cb9a83e61428afe604a034b1946b`; clean. Merge base: `661236f0b2cdebecafeaa0dd50bccc8634f898b2`. Local published feature ref: `c4fb5da44733cb9a83e61428afe604a034b1946b`.

Final diff: [vpsfree-cz-configuration-amended-final.diff](vpsfree-cz-configuration-amended-final.diff), SHA256 `993cf183926fc95bacf8ca631caf072a4613a119a3ea02d4df42cf97b68f80f3`.

Complete own series:
```text
commit c4fb5da44733cb9a83e61428afe604a034b1946b
Author:     Jakub Skokan <jakub.skokan@havefun.cz>
AuthorDate: Thu Oct 15 00:20:23 2026 +0200
Commit:     Jakub Skokan <jakub.skokan@havefun.cz>
CommitDate: Thu Oct 15 02:45:50 2026 +0200

    inputs: set devWorkspace to b8a6be26
    
    devWorkspace: ba8669b1 -> b8a6be26
    git log for ba8669b14536f72b559abc912bba8eac430111e4..b8a6be26a75347dcc9ec0fd1330dff886e47c93f
    > b8a6be2 portal: show session attention and deliver background Web Push
```

Final inventory:
```text
flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```


## Consolidation, composition and state provenance

Each own feature stream has exactly one final commit. Runtime source imports/module metadata/vendorHash remain bundled for source-derived Nix vendoring. Old unpublished amendment heads and earlier published feature heads are absent from the final owning ancestry. Workspace's previous pin was patch-equivalently rebased over d22b5341 tracking-only upstream advance; no substantive workspace baseline changed. Configuration uses confctl-generated selection with intentionally corrected cumulative ba8669b..b8a6be2 changelog, one final pin. Earlier sensitive-session selection commits remain protected upstream history.

No migrations: no DB, lifecycle, roster, runtime-contract or Codex pin changes. Initial private notification schema1 has no released/deployed predecessor or externally consumed product state. Optional strict receipt bool keeps old omitted receipts and capable paired readers; flagged receipts require forward recovery. Browser cleanup receipt remains the same bounded origin-local ID/digest key plus existing saved registration ID; no generic list or new server format. Disposable probes are not supported product-state predecessors. No own deployment, merge or lifecycle action has occurred.

Both effective selected locked runtime identities match b8a6be26a75347dcc9ec0fd1330dff886e47c93f. Workspace only selected runtime node and its direct nested URL changed; configuration only devWorkspace node changed. Extension3f0777ff, siblings, follows and selected-node edges retained. Deployment-contract checker PASS. Config normal hooks PASS, generated message width warning only. Runtime final quick checks PASS15 Node plus Go Attention/Notifications0.443s(member),0.414s(lead); syntax/diff PASS. Native fixture remains preparation-only; real Chromium/Firefox template/CSP/root-worker integration at final head PASS under Luna watcher; final packaged/CI evidence is pending. These are distinct from physical/macOS OS display.

Review unchanged API/provider boundary conclusions at1a57 plus direct four-path requested remedy atb8a6. Requested reviewer: same retained reviewer0, GPT-6.1 Sol/xhigh/read_only; history/composition duties and explicit no-migration conclusion. No source edits or long checks. No authorization for master merge, release/reservation cleanup or lifecycle action.
