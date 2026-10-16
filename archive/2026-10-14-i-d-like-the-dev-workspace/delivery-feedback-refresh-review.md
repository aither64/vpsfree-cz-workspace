# Final affected review: refresh observation ownership

No findings. The new completed committed refresh-ownership correction satisfies its affected source-review gate at exact4ed9af55. The original browser failure is not causally explained, and no new browser, packaged, provider or physical-display verification is established by this review.

Reviewer: retained independent reviewer0, GPT-6.1 Sol/xhigh/read_only; saved settings unchanged. Reverified bound current/session, both absent DEV_SESSION identity variables, and live same-session roster17/thread/settings. Read mandatory-change-review and all four lane references; read/reused applicable unchanged workspace/runtime guidance, documentation and handoff instructions. Direct read-only inspection, no nested agents, source/artifact writes, tests/builds, network/provider/host/queue/reservation/lifecycle operations.

## Exact scope and evidence binding

Affected range:
5a07708ea80a2649265c3ef268b8379daaec47bb ->
4ed9af55127743b7564cb4dd01d10c9f7fee5120.

Amended fifth012f6184faa62b7d476555058f1473adcd908528, followed by unchanged-content status-removal sixth4ed9af55. HEAD and merge base match the packet; runtime remained clean at final recheck. Final tree3c0747c55490b7a9cddb6131f9991ea89f422875 matches the supplied quick-tested tree.

Independently verified:
- all31 new manifest hashes and all167 preserved evidence hashes;
- change, final-delta, owning-delivery, sixth and whole-branch patches byte-for-byte against Git;
- all three changed SHA256 values and all13 protected path equalities against5a;
- retained reviewed5a/50fba refs;
- sixth stable patch-ID1fea1a8447c111f44efc6e4f65ce5694c8b04a72 at old and new heads.

New delta is exactly three paths, +241/-19: static/browser-notifications.js, attention_browser_test.cjs and notifications_browser_test.cjs. No API, Go fixture, worker/store, template, product copy, transport, dependency, private/server/browser format or persisted field change accompanies it.

## General and affected risk conclusions

refresh now captures generation and registration identity, stages worker/subscription observations locally and checks ownership before issuing its status GET and before publishing results. Both success and failure writes to subscription/known/registered/status state and buttons are guarded. Newest-refresh ordering, action-start invalidation, pagehide and cross-tab revocation prevent stale observations from overwriting the newer owner, including after the action finishes.

Refresh triggers during explicit actions are ignored. Revoked observations remain retired under the old identity until explicit Enable; this does not erase the saved-ID/current-digest cleanup obligations. Refresh itself performs no subscription mutation. Refresh-launched workerReadiness writes carry the same current guard across update/capability awaits. Resume is launched only from a current observation, and its existing post-await poll-generation/registration/page/action/pending guards remain.

Reviewed the affected touchpoints with Enable, Disable and Test. Existing registration failure remains incomplete rather than being turned into success. The new code stages reads without replacing action-owned subscription objects; both server deletion obligations and independent local cleanup remain intact. Exact Test retirement, compare-delete and delayed-resume protections remain unchanged from the lead's recorded narrow-remedy disposition. No confirmation rerun of those three earlier fixes or unchanged notification/provider/processgroup lanes was performed.

The five new deterministic ordering contracts exercise old GET success/rejection after Enable, absent/existing local subscriptions, delayed local reads, activation/visible triggers during actions, reversed refresh completion, completion after Disable/Test/revocation/pagehide and genuine failed registration. These are meaningful checks of the new ownership boundary.

## Fixture diagnostics, architecture and proportionality

The actual-browser fixture retains its deliberately existing local fake subscription, original assertions and worker activation. It explicitly waits for /register and requires2xx; neither the Go fixture nor authentication/origin/profile/store checks are relaxed.

Failure diagnostics record fixed event ordering/request numbers, HTTP status, query-ID categories, projected response booleans and bounded controller/state categories. They omit raw IDs, URLs/queries, endpoints, keys, response bodies, arbitrary errors and browser storage dumps. Snapshot and trace-collection waits are bounded; retained rows are capped48 and emitted trace is capped8KiB with dropped counts. The actual helper's canary/overflow contract exercises the privacy and bound projections without launching a browser. Successful fixture runs do not emit the failure trace.

A local generation/current closure fits the existing client ownership model; no generic observation framework, alternate registration implementation or new persistence layer is introduced. The fixture diagnostics are proportionate to the preserved run's missing request/order evidence. Product guidance remains accurate because supported user behavior and visible copy do not change; temporary failure evidence and investigation rationale appropriately remain in session records.

## Complete history and consolidation

Complete own range:
832d9f1a6a21337dd44063ddf39f7a88cfc95450 ->
4ed9af55127743b7564cb4dd01d10c9f7fee5120.

Reviewed complete commit parents/messages/series, range-diff and final cumulative inventory/patch, retaining earlier source-review conclusions for unchanged objects. Exactly six logical commits, no merges:
1. 96717cdeb5f733391846a95d78c117068ce77de8 — attention/Web Push with inseparable imports/module/vendorHash.
2. bb9e6291bec10227c961c36559fba406938f1eaa — bounded provider diagnostics.
3. 6e1d9a191724d376cad2a71f234f0e4d1c01f36f — descendant-exit test-observer correction.
4. 867682c3df251fbe6941ff9a667539ae1af790ec — requested menu/layout correction.
5. 012f6184faa62b7d476555058f1473adcd908528 — owning delivery feedback, with narrow remedies and this refresh correction consolidated.
6. 4ed9af55127743b7564cb4dd01d10c9f7fee5120 — separate requested status-row removal.

Whole final diff:42 paths, +5073/-106. First four objects are unchanged. Sixth has identical content/stable patch-ID despite fixture line-offset/blob-header changes. The transient fixup is absent from final ancestry; superseded5a/50fba and earlier failed/evidence versions remain retained outside the final series.

No obsolete unapplied approach, follow-up fixup series or repeated runtime dependency/channel/generated update stream remains. Source/import/module/vendorHash remain together in the first owning commit. Later requested UI and delivery changes follow the supported deployed6e1 boundary; their separation remains justified. No further source consolidation is required.

Protected initial-registration ancestry92b2576d through sensitive-session273a08c/ba8669b, admission3d60ced, sharding69399c5 and integration832d9f1 remains intact. Those upstream capabilities are supported baseline, not obsolete own history.

## Migration and composition limits

No migrations or persistent/private format conversions in the complete own runtime range. This correction adds only document-local ownership state. Previously reviewed initial private notification schema1, optional IDBv1 test metadata, version1 queued payloads, strict optional creation preference/old omitted receipts, capable bundled-reader pairing and forward-only recovery remain unchanged.

Deployed/consumed6e1 is a supported product-state boundary. Preserve its private keys/subscriptions/outbox, cleanup obligations and protected upstream journal/capability lineage. The amended fifth/sixth are unpublished/undeployed; no transitional migration or new DB/server/browser format is introduced. Earlier predeployment no-consumption statements remain historical.

Directly inspected consumers remain workspace0a9d232e74209da2c2f53358e5f2807f34074055 and configuration45fa9962df83b9bec65523ae6ee7d19b63bb03ea, both selecting exact6e1 with matching prior complete lock identity. No4ed downstream selection is supplied or certified.

Read the130c2248 configuration planning addendum. Its stable input reaches aitherdev and the configuration dev shell; unchanged confctl/runtime pins do not prove shell or host closure equality. The new declared environment is preparation evidence, not activation. Actual rebased bases, generated selections, effective package graph, hooks/checks and complete consumer histories still require the promised final composition inventory/review. This source review does not certify that future composition.

## Verification and remaining gates

Supplied quick evidence records32 named Node passes, zero failures/cancellations/skips, duration1987.159282ms (command2.123s), plus three changed syntax checks and diff PASS. Final tree equality binds the tested source through consolidation. No browser was launched for the trace contract; no unchanged Go/live check was rerun. I ran none of these checks.

The sealed first5a browser run remains FAILED: Enable expected Enabled but observed incomplete, command17s/test9.74s. It captured no HTTP/order/controller evidence sufficient to identify the actual cause. The missing refresh guard is independently demonstrated by source and forced orderings; this does not prove that ordering caused that failed run.

A fresh exact-head finite browser check with the new diagnostics remains pending; stop on failure and preserve its boundary evidence. Final packaged/native checks, downstream composition/preparation and authorized activation are separate outstanding gates. Olda5 and any newly prepared4ed native bundles are unrun preparation, not delivery evidence.

Physical Firefox/macOS non-display and actual click/authentication acceptance remain unresolved. Provider acceptance, worker receipt, display API resolution and browser records cannot establish physical appearance. Original provider and processgroup failure causes remain unknown; corrected or later passing checks cannot retroactively explain them.

Lead should persist this report as delivery-feedback-refresh-review.md. No source finding prevents the lead's planned finite post-review browser check. No publication, deployment, merge, reservation release or lifecycle approval is granted. Keep session and reservation1956d2a0 open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
