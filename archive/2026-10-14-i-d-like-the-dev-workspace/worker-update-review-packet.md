# Worker activation correction review packet

FINAL: source committed, clean, quick checks PASS.

User: “i don't care about the other tabs or backward compatibility of the
notifications. i just want the notifications to work on new/refreshed tabs”.

Acceptance: a new/refreshed controls document updates/uses the successor worker
while existing portal tabs remain open. No closing/reloading tabs or subscription
reset. Old-tab notification semantics are explicitly outside the acceptance
requirement. Existing permission, subscription, keys, private session state and
cleanup obligations are retained. Actual OS/macOS display remains distinct.

Bound session2026-10-14-i-d-like-the-dev-workspace, workspace
/home/aither/workspace/ai/vpsfree.cz. Design/state/plan under this tracking root.
Architect0 owns design, implementer0 owns code, lead owns copy/operations.

Affected source starts at deployed4ed9af55127743b7564cb4dd01d10c9f7fee5120;
complete own source base832d9f1a6a21337dd44063ddf39f7a88cfc95450. The first six
objects are supported and preserved. New seventh owning commit is independently
requested worker activation behavior with its tests/guides, not a rewrite of
deployed4ed. Earlier reviewed affected boundaries retain their exact scope.

No migrations, DB upgrades, API/private state/protocol payload/dependency/vendorHash
changes are intended. IDBv1 and payloadv1 persist. Preserve original privatev1
and optional receipt lineage plus upstream integration journals/capabilities.
Both6e1 and4ed were deployed/consumed; their exact source, predecessor consumer
refs, receipts and all failure evidence must remain. Consumer pin updates later
consolidate to one final own runtime selection per consumer. No separate new
notification-format compatibility framework is requested or justified.

Overall risk high for worker lifecycle/activation and mixed loaded documents,
without imposing old-tab notification behavior against explicit user scope.
Use retained reviewer0 Sol/xhigh/read_only, all four mandatory review lanes
(general/history; architecture; scope; risk). Inspect final committed source,
complete base-to-head series/final diff and migration/stream provenance. No
confirmation rerun of unchanged earlier notification/provider/processgroup lanes.
No reviewer tests/build/network/host/operations required. Do not launch nested
reviewers. This report must not grant deployment, merge, release or lifecycle
authority.

Review automatic install skipWaiting+activate claim, bounded readiness and
freshness guards, no stale async status mutation, listener/timer cleanup, truthful
copy and prepared old-controller/multiple-open-tab actual browser regression.
Worker does not fetch/cache portal content, so activation must not navigate or
replace page state. The fixture must test real native lifecycle; synthetic push
and display remain labelled and cannot establish physical OS acceptance.

Final head e208027f006937693839e3612807db31a7ce0134 over deployed4ed9af55.
Ten paths +311/-51, including two guides, worker/client, two template cachev3
includes, module contracts and real-browser fixture supporting changes. Main
read/approved actual notification-activation-copy.patch with the one completed
plain-language guide correction; queued Test now suggests another tab or app.
37 named Node contracts PASS, no skips/failures; focused Go page/template2 PASS
and changed4 JS syntax/diff PASS. See notification-activation-quick-results.json
and per-check logs/status (browser fixture prepared, not executed).
Whole inventory worker-update-series.txt, worker-update-whole.diff and
worker-update-stat.txt. Affected source worker-update-source.diff. Exactly seven
logical runtime commits, no merges. First six source objects preserved. Source
modules/vendorHash and API/state remain unchanged by this seventh change.
Real fixture now tests native lifecycle/current controller in BOTH engines;
only Chromium uses Playwright worker evaluation for synthetic Test outcome.
Firefox has no synthetic delivery claim. No product test API added.

Source owner generic runtime; actual consumers workspace nested
vpsfree-dev-workspace/dev-workspace override and configuration devWorkspace.
Extension767dfd58 and upstream protected baselines stay unchanged.
Current deployed consumers750ab33c/c90e56d5 select4ed; future final selections
need their own complete mechanical composition/history conclusion.
