# Final delivery feedback and status-removal review

Two Important findings and one Advisory; no Blocking finding. Fix or explicitly record decisions on the Important findings before long/browser integration checks.

Retained independent reviewer0, GPT-6.1 Sol/xhigh/read_only, settings unchanged. Reverified bound current from the assigned tracking directory, both absent DEV_SESSION identity variables and live same-session roster17/thread/settings. Applied mandatory-change-review and all four lane references plus applicable workspace/runtime guidance. Direct read-only inspection; no nested agents, writes, tests/builds, network/provider/host/queue/reservation/lifecycle operations.

## Findings

1. Important — A failed new Test request leaves the previous test able to report success for the current interaction.
Lanes: general correctness; risk/correlation.
Commit: 43c6461e3f5ce900f72df7b2aa9593584884b04e.
File: portal/internal/web/static/browser-notifications.js:267–285, pollTest:65–94.

The click handler stops the previous wait only after a successful /test reply (line272). Queue A, click Test again, then fail the second request or lose its successful server reply: the catch changes only the main status. pendingTest, its saved descriptor and polling/message path still belong to A. A later A receipt can say “This test reached the browser and the browser accepted the display request”; pollTest also replaces the new request error with “Enabled on this browser.” The newest click has no known descriptor, so this presents an older event as its diagnostic result and violates exact-click correlation.

Retire the prior check when a new explicit Test attempt begins, before awaiting the request. Keep a failed/lost new reply unknown and prevent automatic resumption of the retired check. Clear persisted state only if it still matches the retired descriptor (finding2). Add a focused contract with A pending, a rejected/lost second reply and a later A outcome/message; the second interaction must not advance to A's success or erase its own uncertainty. Current contracts do not cover this path.

2. Important — An older tab can delete a newer tab's persisted pending check.
Lanes: general correctness; architecture/state ownership; risk/persistence.
Commit: 43c6461e3f5ce900f72df7b2aa9593584884b04e.
File: portal/internal/web/static/browser-notifications.js:20–25; Enable caller:183.

cancelTest captures only identity and unconditionally deletes value.testPending in the shared transaction. Tab A can still hold descriptor A while tab B has saved newer B for the same registration. Before A's next poll notices B, Enable in A invokes cancelTest and removes B. A same-ID Enable can leave the subscription/registration intact. B continues in memory, but closing/reopening B no longer resumes its check: resumeTest reads only testPending, even if the worker later saves B's outcome. This bypasses saveTest's newer-revision protection.

Capture the complete canceled descriptor and compare all four fields against the transaction's current testPending before deleting. A stale document must not remove another event's descriptor. Add a shared-store two-document contract: A pending, B newer saved, A canceled, then B reopened; B's descriptor/resumability must survive. No server/API/schema expansion is needed.

3. Advisory — A delayed resume read can overwrite a newly started or canceled check.
Lanes: general correctness; architecture/async ownership.
Commit: 43c6461e3f5ce900f72df7b2aa9593584884b04e.
File: portal/internal/web/static/browser-notifications.js:96–103.

resumeTest checks pendingTest/pageClosed/registration only before awaiting IDB. If a new Test reply installs B while the older resume read is outstanding, its continuation can assign saved A over B; polling can then report another test replaced the check and stop B's wait. An intervening cancellation can likewise be undone in memory. Recheck registration, page state, absence of a newer pendingTest and an invalidation generation after the read, before assigning. Cover this with a deferred-read contract, without a new abstraction.

Findings are from source/control-flow inspection; no reproduction tests were run.

## Exact scope and evidence

Affected range:
867682c3df251fbe6941ff9a667539ae1af790ec ->
a5e41580d6dbeae9cbb468c707c22106f159066c.

Delivery commit43c6461e3f5ce900f72df7b2aa9593584884b04e and status-removal commita5e41580 are separate completed changes. Runtime HEAD/parents match the freeze; tree was clean at inspection and final recheck. Independently verified all48 manifest hashes, all four affected/status-removal/combined/whole-branch patches byte-for-byte against Git, all11 final blob SHA256/Git identities and all10 protected unchanged blob checks. Combined affected delta:11 paths, +526/-23. Sixth alone:2 paths, +1/-2.

Retained ui-feedback-review.md applies to exact867. First four commit objects are unchanged; earlier notification/provider/diagnostic/processgroup reviews retain their unchanged boundaries. No confirmation source rerun was performed.

## Other affected conclusions

The existing successful /test reply adds only the exact queued event's id, identity, revision and expiresAt. Authentication/origin/scoping and admission remain unchanged. notifications.go changes only descriptor capture/reply assembly; sender/observer, transport/SSRF guards and private server store remain unchanged. No endpoint or subscription key is exposed. Go coverage binds all four fields to the outbox event and checks descriptor privacy.

The shared attention store owns normalization, exact matching, safe error categories and monotonic outcomes. Optional closed pending/latest fields reuse IndexedDB v1 and its existing record bound. No parallel store, server receipt service or generalized schema mechanism is introduced. Apart from the ownership races, this is proportionate to the demonstrated diagnostic gap.

The worker separates receipt, display resolution/rejection and browser-record present/absent/unavailable. Bounded diagnostic writes/reads cannot indefinitely prevent display attempts; arbitrary error text is excluded. Fresh test-event tags and bounded same-identity older-test closure preserve session tags/ACKs. Provider status remains explicitly registration-wide and cannot certify a test. Display API resolution/browser records are not physical-display or click proof.

Version1 queued payloads remain accepted. Older workers/pre-display records do not fabricate terminal outcomes; absent server/helper/worker capabilities remain limited/unknown. Worker update/capability checks do not unregister, resubscribe, reset keys or force skipWaiting. Both document consumers load the shared v2 store before the client. Fixed old-ID/digest deletion obligations and independent local/server cleanup remain unchanged.

Native menu placement, spacing, hidden Settings initialization and absent index/load-time subscription mutations remain intact. Sixth removes only p#session-attention-status and changes its existing browser assertion to count0. Observer writes are null-guarded; title/presence/Reservations behavior is unchanged. No additional finding in the deletion.

The owning feature/operations guides accurately separate queue, provider result, receipt, display API, browser record, physical appearance and click. Compatibility/recovery guidance is retained; lead's main-agent copy approval is recorded. Temporary failure/rollout evidence stays in session records.

## Complete history, consolidation and migration provenance

Complete own range:
832d9f1a6a21337dd44063ddf39f7a88cfc95450 ->
a5e41580d6dbeae9cbb468c707c22106f159066c.

Inspected complete parents/messages/series and cumulative final inventory/patch, retaining already reviewed unchanged boundaries. Exactly six logical owning commits, no merges:
1. 96717cdeb5f733391846a95d78c117068ce77de8 — attention/Web Push; inseparable source imports/module declarations/vendorHash.
2. bb9e6291bec10227c961c36559fba406938f1eaa — bounded provider diagnostics.
3. 6e1d9a191724d376cad2a71f234f0e4d1c01f36f — pre-existing descendant-exit test observer correction.
4. 867682c3df251fbe6941ff9a667539ae1af790ec — requested menu/layout correction.
5. 43c6461e3f5ce900f72df7b2aa9593584884b04e — correlated delivery feedback.
6. a5e41580d6dbeae9cbb468c707c22106f159066c — separate requested status-row deletion.

Whole final diff:42 paths, +4727/-106. No obsolete unapplied design/fixup series or repeated runtime dependency/channel/generated update stream remains. Module/vendorHash updates occur together only in the first commit. Later UI/diagnostic/status commits address independently requested behavior after the supported deployed6e1 boundary, rather than retaining abandoned feature iterations. Narrow review fixes should normally be folded into the unpublished fifth owning commit.

Initial-registration ancestry92b2576d through sensitive-session273a08c/ba8669b, admission3d60ced, sharding69399c5 and integration832d9f1 remains intact. Protected upstream journal/capability history must remain.

No migrations or persistent/private format conversions in the complete own range. Initial private notification schema1, strict optional creation boolean and old omitted receipts retain their reviewed lineage. Optional testPending/testOutcome fields need no DB upgrade; old readers preserve/ignore optional metadata and new readers treat absent detailed outcomes as unknown. Deployed6e1 is now a supported consumed boundary, evidenced by acceptance/deployment/identity records; older no-consumption statements are historical. Preserve its private keys/subscriptions/outbox, cleanup obligations, capable bundled receipt readers and upstream integration journals/capability fencing. Recovery remains forward-only through a compatible package.

Fifth/sixth are unpublished/undeployed. No new dependency, vendorHash, server/DB/lifecycle format or migration is introduced by them. No transitional migration remains.

Directly inspected current consumers: workspace0a9d232e74209da2c2f53358e5f2807f34074055 and configuration45fa9962df83b9bec65523ae6ee7d19b63bb03ea still select exact6e1 with matching prior complete locked identities. No a5e41580 downstream composition is supplied or certified; future generated selections retain their final history/composition gate.

## Verification and remaining gates

Inspected supplied logs/status: fifth22 named Node passes (original15+7),22 focused Go passes plus intentional actual-browser skip, five syntax passes and diff checks; sixth3 focused Go/template passes, changed fixture syntax and diff checks. These are supplied precommit-identical-tree receipts, not reviewer executions. The three finding sequences lack coverage.

Prepared actual-browser fixture is UNRUN; final-head long/native checks remain pending. Synthetic/stub display assertions cannot establish provider delivery or physical OS appearance. Firefox/macOS non-display remains unresolved; preserved6e1 Firefox provider acceptance/pre-display worker receipt with zero browser records remains an unresolved observation. Physical/macOS display and click/authentication acceptance are separate gates.

Original provider and bb9 processgroup causes remain unproved; later corrected/passing checks cannot retroactively explain either failure.

Lead should persist this as delivery-feedback-review.md and reconcile findings before proceeding. Preserve active/open session, deployed state and reservation1956d2a0. This report grants no publication, merge, deployment, reservation-release or lifecycle approval.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/
