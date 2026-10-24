# I-B1 narrow remediation plan

Status: preparation only. Application source, tests and commits remain held until the final exact-B85eb review completes and the lead releases implementation.

Baseline B85eb687a597df116690d6481ca2ec5d4ea94f0cd / tree be3753a029d646d170c93cf1aba6cfafa6db4925. Existing final packet, verified final.bundle, immutable Nix source and published feature ref remain retained. On release, create a dedicated immutable85eb preservation ref before source edits and keep remediation evidence separate from the original packet.

## Exact scope

- portal/internal/web/turn_retry_activity.go: reconcile count quality in the existing read-only retryActivityView, optionally through a small private pure helper.
- portal/internal/web/turn_retry_activity_test.go: focused pure-view table and real Handler/root+member fault regressions, reusing the actual managed-client/private-wire fixture.

No changes to controller, writer, state schema, action tuples, provider interface, public DTO, policies, quota, manual delivery, acceptance/Stop acknowledgment or A/pin/assets/docs. Existing docs already require partial/unavailable checkpoint-gap evidence; no new visible copy is proposed.

## Read-only rule

For the same chain, preserve the stored confirmed count and quality when continuity is proved. Downgrade an exact count to unavailable (null confirmedStarts) when a supported known gap exists:

1. The authoritative Pending has ResultTurn, but its UUID differs from checkpoint.LastConfirmed: native acceptance was saved without the corresponding count checkpoint.
2. checkpoint.PendingID differs from checkpoint.LastConfirmed, and that pending identity is now absent or replaced in the ledger: an uncheckpointed attempt was retired/replaced and its count continuity cannot be certified.

Treat a missing checkpoint through the existing unavailable fallback. Preserve already partial/unavailable quality; never upgrade or add counts from Attempt, quota, polls or presentation. An accepted/caught-up checkpoint remains exact. A scheduled/uncertain same UUID without a known acceptance gap retains its existing count; unknown remains represented separately by the authoritative Uncertain() flag. Keep chain identity, phase/outcome, timing rules, action tokens and native recovery unchanged.

The helper/view must not mutate State, Policy or Summary or persist anything. Both GET and action responses already use this view, so failed Stop checkpoint acknowledgment receives the same honest quality without making its save mandatory.

## Focused cases

New TestRetryActivityViewCheckpointContinuity table:

- exact0/scheduledP -> accepted ResultTurnP with stale LastConfirmed: unavailable count, unconfirmed0;
- failed Stop summary after acceptance: terminal/stopped with unavailable count, original Chain/Pending/action identity retained;
- known manual retirement with stale pending checkpoint: unavailable count;
- replaced uncheckpointed Pending: unavailable count;
- caught-up accepted LastConfirmedP, current scheduled/unknownP, and already partial/unavailable controls: no false degradation/upgrade or synthetic count;
- byte-identical State/Policy/Summary before/after view.

New TestRetryActivityActualHTTPCheckpointGaps, root and retained member, with real Server.Handler and real managed client/private native wire:

- save exact accepted receipt in the retry ledger while optional sidecar checkpoint fails and its old readable summary remains; GET the production root /api/sessions/{slug}/retry/activity or member /codex/conversations/{id}/retry/activity and verify unavailable count/unconfirmed0;
- Stop with an unwritable optional checkpoint: acknowledgment still succeeds, owning tuple/cancellation persists, response and later GET never claim stale exact count;
- retire the accepted pending tuple through the existing authoritative manual cancellation transition while the old summary remains; real HTTP GET reflects the continuity gap;
- repeated GET leaves sidecar/ledger bytes and file identity unchanged, creates no native start/quota movement; original exact receipt/token recovery remains usable.

Reuse/factor the existing actual unknown-intent private-wire fixture in the same test file if needed; do not relax its strict native methods, delivery assertions, or add a fake-only substitute.

## Exact proposed quick commands after release only

CWD /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace

Normal:

    nix develop --no-update-lock-file --command go -C portal test -mod=readonly ./internal/web -run '^(TestRetryActivityViewCheckpointContinuity|TestRetryActivityActualHTTPCheckpointGaps|TestRetryActivityActualHTTPRootMemberActionsIdentityAndNoDispatch|TestRetryActivityActualHTTPStopsOwnUnknownBeforeOrdinaryGate|TestRetryActivityStopAcknowledgesLedgerWithUnavailableSummary)$' -count=1 -timeout=45s

Race: identical selector with -race after -mod=readonly. Existing activity cases were bounded at1.648s normal, broader policy/activity at11.231s race. These remain focused quick checks; any unexpected duration/failure will be reported, not retried blindly. No pressure, accepted-fork integration, browser, native, full, build, CI or live operation is included.

After implementation: format/diff check, focused normal/race receipts, owning remediation commit and ordinary SSH publication, exact new head/tree with85eb delta and all unrelated blobs equal. Lead step9 inspects the requested narrow finding fix. Route any required contract/scope expansion to lead before changing it.
