# Final affected review: automatic notification-worker activation

One Advisory finding; no Blocking or Important findings. The committed activation change satisfies the affected source-review gate, subject to recording the Advisory disposition. The prepared real-browser lifecycle regression remains unrun.

## Finding

Advisory — Canceling readiness can leave an indefinite “Updating” message.
Lanes: general correctness; affected async/UI risk.
Commit: e208027f006937693839e3612807db31a7ce0134.
File: portal/internal/web/static/browser-notifications.js:14,47,52–81,87–104,337–361.

When Test or Disable invalidates an outstanding readiness check, cancellation correctly clears its timer/listeners (or capability ports). The generation check then prevents that canceled task from publishing a terminal result, but the action does not replace the earlier “Updating browser notifications…” text. If no later visibility/controller event starts a new refresh, that message remains after the ten-second check has ended. The same sequence is possible when an already-current worker's capability reply is pending; a new worker transition is not required. Current cancellation tests assert cleanup/no stale overwrite but retain the progress text.

Have the current action owner replace canceled progress with an honest unconfirmed/limited result, or arrange one bounded current check after the action. Do not let the stale task publish or add an update loop. A focused contract can cancel an in-progress check with Test/Disable, advance past its deadline and assert no lingering “Updating” state. This is a presentation issue, not evidence that installation or push delivery fails; it does not block the planned lifecycle fixture.

## Identity, scope and evidence

Retained independent reviewer0, GPT-6.1 Sol/xhigh/read_only, settings unchanged. Reverified bound current, both absent DEV_SESSION identity variables and live same-session roster17/thread/settings. Applied mandatory-change-review and all four lane references plus applicable workspace/runtime guidance; these references are unchanged from the completed retained reviews. No nested agents, writes, tests/builds, network/provider/host/queue/reservation/lifecycle operations.

Exact affected range:
4ed9af55127743b7564cb4dd01d10c9f7fee5120 ->
e208027f006937693839e3612807db31a7ce0134.

Exact complete own range:
832d9f1a6a21337dd44063ddf39f7a88cfc95450 ->
e208027f006937693839e3612807db31a7ce0134.

HEAD matches; tree was clean at entry and final recheck. Independently verified all22 notification-activation-artifacts.sha256 entries, affected/whole patches byte-for-byte against Git, complete full-message series and whole stat. Ten affected paths, +311/-51; complete final diff42 paths, +5333/-106. Client/worker/store SHA256 values match the inventory. Twelve protected server/store/transport/receipt/module/vendorHash/lock/observer blobs are unchanged from4ed. The first six commit objects are preserved exactly.

Read the final worker-update packet, complete implementer inventory, final copy patch, narrowed design addendum, current state/rollout context, changed source, module contracts and prepared actual-browser fixture. Earlier source reviews retain their unchanged boundaries; no confirmation rerun of old notification/provider/processgroup lanes was performed.

## Activation, architecture and accepted scope

The user's requirement is new/refreshed controls using the successor while other tabs remain open. Old-tab notification semantics and retrofitting loaded scripts are explicitly outside acceptance; no additional compatibility mechanism is required here.

The worker adds only install waitUntil(skipWaiting), retaining activate waitUntil(clients.claim). It has no fetch handler/page cache and adds no navigation/reload/close, subscription reset, push replay/cancel or persistent-state operation. Existing push waitUntil(display), session tags/ACKs and click behavior remain unchanged. Automatic takeover therefore fits the chosen scope without replacing document assets or drafts.

The client fetches through the existing root registration and shares one update promise per document. It waits for no installing/waiting predecessor and for this document's activated controller to equal registration.active before probing the existing capability. An old active capability or serviceWorker.ready alone cannot certify a known pending successor. A fetched successor's own install handler handles an already-waiting predecessor that has no activation-message handler; no new worker command or protocol is introduced.

Readiness uses a ten-second overall deadline, bounded existing capability probe and state/update/controller listeners. Terminal, timeout and invalidation paths clear owned observers/timers/ports. Refresh/action/page/revocation generation guards prevent old readiness results from overwriting newer owners. Failed/hung update checks remain limited; a new/refreshed document can try again. Apart from the Advisory progress text, this is a local, proportionate lifecycle observation rather than a framework.

First registration/permission/subscription still belongs to explicit Enable. Opening controls without a registration does not register one. Update does not unregister/resubscribe/reset keys or browser/server state. Existing Test correlation, retirement/compare-delete and fixed old-ID/digest cleanup obligations remain intact. New v3 client selections in both templates retain shared-store v2 and no index initializer.

Both owning guides replace the tab-closing update advice with automatic takeover and honest current-controller readiness. Main-agent final copy approval and its requested wording correction are reflected in the committed source. Physical appearance remains separate from worker/API evidence.

## Prepared regression and quick-check evidence

The real Go fixture adds a finite fixture-only old/old-waiting/current response switch at the same worker URL. It does not expose a production test endpoint or relax real notification API authorization/origin/store behavior. Old active and waiting scripts have neither skipWaiting nor activation-message support.

The CJS lifecycle scenario runs in both Chromium and Firefox, keeps an old-controlled conversation page/draft/sentinel open, creates a waiting predecessor, then serves the actual successor to new controls. It checks controller takeover, absence of a waiting/installing worker, capability support and retained original page/draft. Lifecycle registration/update/control remain native. Chromium additionally uses Playwright worker evaluation for correlated synthetic Test/display; Firefox makes no worker-evaluation or delivery claim. Existing menu/layout/hidden Settings/no-load-mutation and bounded diagnostic coverage remains.

Supplied quick receipts:37 named actual-module Node passes, zero failures/cancellations/skips, duration2069.115726ms (command2.235s); two focused Go template/page passes, package0.085s (command7.566s), compiling the changed Go fixture; four syntax checks and diff PASS. New contracts cover install/claim, waiting transition/current controller, shared outstanding fetch, failure/nonresponse/deadline cleanup and stale readiness invalidation. I reran none. Native browser execution is explicitly UNRUN, so prepared fixture assertions are not observed lifecycle proof.

## Complete history, repeated streams and migration provenance

Exactly seven logical own commits, no merges:
1. 96717cdeb5f733391846a95d78c117068ce77de8 — attention/Web Push with inseparable imports/module/vendorHash.
2. bb9e6291bec10227c961c36559fba406938f1eaa — bounded provider diagnostics.
3. 6e1d9a191724d376cad2a71f234f0e4d1c01f36f — descendant-exit test observer.
4. 867682c3df251fbe6941ff9a667539ae1af790ec — menu/layout.
5. 012f6184faa62b7d476555058f1473adcd908528 — correlated feedback and consolidated remedies.
6. 4ed9af55127743b7564cb4dd01d10c9f7fee5120 — requested status-row removal.
7. e208027f006937693839e3612807db31a7ce0134 — separately requested automatic activation after consumed4ed.

No obsolete unapplied own approach, fixup/follow-up series or repeated runtime dependency/channel/generated-update stream remains. The seventh commit is justified independently by the new postdeployment requirement; preserving deployed4ed history is appropriate. The source/import/module/vendorHash boundary remains inseparable in the first commit. Protected initial-registration/sensitive-session/admission/sharding/integration ancestry remains intact.

No migrations or persistent/private format conversions in the complete own range. The seventh adds no API, worker protocol/payload format, dependency, vendorHash, schema or database version/object-store change. Private notificationv1, IDBv1 optional Test metadata, payloadv1, strict optional preference/old omitted receipts, capable-helper pairing and upstream journal/capability fencing remain supported. Subscriptions, VAPID keys, IDs and cleanup selectors are preserved; recover forward through a compatible package.

Both6e1 and4ed are deployed/consumed state boundaries. Current deployed consumers750ab33c/c90e56d5 select4ed. Their exact source/refs/receipts and earlier failed evidence remain preserved. New e208 is unpublished/undeployed per packet, and no e208 consumer composition is supplied or certified. Later own pin streams still require consolidation and final mechanical history/composition conclusions; publication/deployment alone do not justify retaining superseded pins.

## Residual limits and handoff

After recording the Advisory disposition, no Blocking/Important source finding prevents one finite exact-head browser lifecycle check. Do not represent preparation or quick module contracts as that check's result. Later packaged/CI, final consumer pins/composition, exact preparation and authorized activation remain separate gates.

Deployed4ed native evidence now includes correlated Firefox display rejection UnknownError/no record, while Chromium resolved/recorded. That safe category does not establish an application or macOS cause. This activation change does not repair or explain that separate rejection, physical Firefox/macOS non-display, original failed fixture/provider/processgroup causes, or click/authentication acceptance. Provider/worker/API/browser records cannot prove physical appearance.

Lead should persist this as notification-activation-review.md. This review grants no publication, deployment, default merge, release, reservation-release or lifecycle approval. Keep reservation1956d2a0 and session open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
