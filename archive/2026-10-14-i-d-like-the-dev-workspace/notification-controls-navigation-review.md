# Final affected review: retained navigation-counter boundary

No findings. The committed fixture-only correction satisfies its affected review gate at197782df. The actual browser check remains unrun; no integration or readiness claim follows.

Retained independent reviewer0, GPT-6.1 Sol/xhigh/read_only, unchanged settings. Reverified bound current/session, both absent DEV_SESSION identity variables and live roster17/thread/settings. Read mandatory-change-review and assigned general, architecture/repetition and scope references; reused applicable unchanged workspace/runtime guidance and prior product/risk/popover/checkbox conclusions without confirmation reruns. No nested agents, writes, tests/builds/browser/network/check polling/provider/host/queue/reservation/lifecycle actions.

## Exact scope and correctness

Affected range:
55af728332471ef16a9587723c6964c563227748 ->
197782df20a0776842fb914ba2a2caa674b45186.

HEAD/tree5a93f2b1c8f65ec80f7f3e157ee85760adaa71f6 match the freeze; worktree remained clean. Only notifications_browser_test.cjs changes, +9/-1. Every other tracked blob is identical to55af.

At lines152–160, the fixture requires zero unexpected retained navigations immediately before its intentional Settings click. It arms a finite5000ms event wait before clicking, restricted to the retained main frame and exact fixture #settings destination, awaits both event and click, then requires exactly one transition and the active Settings section/hash. Only then is the counter reset.

This correctly separates setup from the later measurement. The existing Settings anchor has href="#settings"; its application listener selects the panel without suppressing native fragment navigation. The fixture therefore accounts explicitly for its own transition instead of broadly discarding accumulated events. Any preceding or extra transition fails before reset. The complete suffix after this boundary is byte-identical, including final zero-navigation, draft/sentinel, page-count/URL, sound/storage, subscription, controller, correlation and click assertions. No sleep, existing timeout increase, worker-handle change or product refocusing mechanism is introduced. Scope and ownership are proportionate.

## Evidence and history

All10 current manifest hashes, both retained refs and all25 sealed preservation hashes match. Verified exact patch, fixture blob/hash, complete nine-commit subject series and unchanged suffix against Git.

The complete832d9f1a6a21337dd44063ddf39f7a88cfc95450..197782df range retains nine coherent commits and no merges. See verified notification-controls-navigation-series.txt. First seven deployed objects remain unchanged. The correction is consolidated into owning eighth2f6c2730; ninth197782df is replayed with unchanged stable patch-ID936d8a9b985a4f827b1ad03f85b0be742140cd62. Superseded55af/97eb and prior evidence remain retained. Cumulative final diff:42 paths,+6012/-107.

No obsolete unapplied own history, redundant fixup/follow-up series or repeated runtime dependency/channel/generated-update stream remains. Source/import/module/vendorHash remain inseparable in the first feature commit. Protected sensitive-session/admission/sharding/integration ancestry and supported consumed6e1/4ed/469 boundaries remain intact.

No migrations or persistent/private format conversions. This correction changes no product/API/payload/dependency state. Already-reviewed optional IDBv1 sound data, private notificationv1, receipt/readers, cleanup obligations and upstream journals/capabilities remain unchanged. Preserve keys/subscriptions/outbox/receipts/coordination state and compatible forward recovery. No197 consumer composition is certified; final pins/history review and preparation remain separate.

## Verification limits and handoff

Supplied exact197 quick receipts pass fixture syntax,53 existing Node contracts (zero fail/cancel/skip;6570.782876ms) and working/range diff checks. I reran none.

The separate55af diagnostic locates238:92 for its run; it captures neither raw count nor navigation history. Ordinary55af and earlier ordinary failure causes remain unlocated. Source establishes the counter-boundary defect independently; future success cannot retroactively reconstruct those failures.

No finding blocks one finite exact-head Chromium/Firefox fixture. Fullflake remains held until it passes. Native sound suppression, keyboard-save focus continuity and real Firefox/macOS notification-click selection remain separate acceptance limits.

Lead should persist this as notification-controls-navigation-review.md. No publication, deployment, merge, release, reservation-release or lifecycle approval is granted. Keep session and reservation1956d2a0 open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
