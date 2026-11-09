# Independent final review

## Findings

### Important R1: interrupted cutover cannot reach recovery through normal portal paths

Commit: `c74544517d1d77a7c18c1eb6e9fd933f4d7aa85f`.
Primary location: `portal/internal/turnretry/store.go:150`.

A crash after publishing a schema-3 marker and before publishing its database is
an explicitly supported migration state. `Store.Load` turns its missing database
into the plain error `retry evidence migration requires locked recovery`.
`Store.Lock`/`Inspect` can recover it, but important callers return that error
before obtaining either lock:

- `workspacecodex.Client.CancelAutomaticRetry`, `turn_retry.go:37`, runs before
  ordinary browser mutations in `web/server.go:4046`.
- `web.reconcileTurnRetry`, `turn_retry.go:322`, runs before every full scheduler
  step (`turn_retry.go:203`).
- `turnretry.Controller.ReconcileOnly`, `controller.go:54`, repeats the same
  read-before-lock guard.
- `web.retryIdleCandidate`, `turn_retry_idle.go:189`, returns the load error;
  `stepTurnRetrySettled` returns that error instead of taking its full path.

Consequently, restarting the portal after an interruption in this window can
leave both ordinary browser changes and automatic recovery refusing indefinitely.
The store-level migration test reaches recovery by calling `Lock` directly, so
it does not cover this application-level failure. State remains recoverable;
this is an availability and recovery-contract defect, not evidence loss.

Make the recoverable marker distinguishable and route it through an authorized
locked existing-record operation. Keep passive reads non-mutating, genuinely
absent state absent, malformed state refused, and a completed marker with a
missing database failed closed. Add application-level regressions for both
`source: empty` and `source: legacy`, including a retained uncertain automatic
UUID, through browser cancellation and the scheduler/reconciliation entry points.

### Important R2: cold team delivery still reports failure for optional binding bookkeeping

Commit: `c74544517d1d77a7c18c1eb6e9fd933f4d7aa85f`.
Primary location: `portal/internal/workspacecodex/turn_retry.go:383`, with
`turn_retry.go:476` and `recovery.go:84` as the remaining consumer path.

The warm send path now logs `recordRetryBinding` failures and preserves an
accepted generic receipt. The cold team-assignment path still propagates the
same optional failure. `sendWithRecovery` first successfully calls the generic
`QueueWithPolicy`, then calls `ActivateThreadWithSettings`. Because
`sendWithOptions` supplies `retryTransactionKey`, the held-transaction branch
performs the native activation successfully and then returns
`c.recordRetryBinding(...)` directly at line 480. A transient provider read or
retry-evidence save failure there makes `sendWithRecovery` return an empty
receipt and an error at `recovery.go:88`, although the original message is
already durably queued and may already execute during activation. It also skips
the subsequent recovery-state update.

This leaves a current, documented consumer outside the stated guarantee that
accepted delivery cannot become a failure because optional retry bookkeeping
failed. It is a remaining integration gap rather than a newly introduced native
delivery mechanism; the underlying callback predates this branch.

Handle optional retry-binding failure separately from native activation failure
in this held delivery context, preserving the original queue receipt and the
ordinary recovery permission update. Do not hide a native activation or
recovery-authority failure. Add a cold root/member send regression that injects
only the post-activation binding failure and verifies the same queue/message
identity, successful acknowledgement, correct recovery state, and no repeated
native dispatch on replay.

## Scope and proportionality

The implementation matches the authorized SQLite/shared-settings and asynchronous
proof solution. The approximately 1,559 additions/673 deletions include the owned
storage mechanism, conversion, delivery wrappers, consumers, tests and lasting
documentation. This is justified by the requested removal of aggregate evidence
as a delivery admission condition; I found no speculative framework or attempt
to resist the trusted local operator. Remote authorization and execution proof
remain separate from optional evidence collection.

`turnretry` appropriately owns persistence and the state machine;
`workspacecodex` owns native proof/delivery integration. The SQL view retains
unloaded rows, rejects stale revisions, deduplicates settings and includes its
revision in idle hints. Cancellation still precedes dispatch, and unknown native
identities are retained. The separate interrupt commit uses matching pre/post
turn identity and a terminal post-observation; pending interruption and turnover
remain unsettled. No additional finding in that commit.

## Complete history and repeated-update conclusion

Reviewed the complete committed series and final diff from
`240a53dafabf24b6718195b88bee012a4ead8698` to
`79a1cc869b1c9631ac4ca8070f1a082793f7f149`:

1. `c74544517d1d77a7c18c1eb6e9fd933f4d7aa85f` — delivery/evidence storage,
   conversion, affected consumers, diagnostics, tests and documentation.
2. `79a1cc869b1c9631ac4ca8070f1a082793f7f149` — immediate confirmed interruption
   settlement and its tests/documentation.

The first commit's support changes serve its single replacement of bounded
aggregate admission with durable indexed evidence and asynchronous proof. The
interrupt behavior is independently reviewable in the second commit. No
superseded approach, fixup-only commit, obsolete migration or unused
branch-iteration compatibility layer remains in this series.

There are no repeated dependency, channel, input, lockfile or generated-artifact
update streams. `modernc.org/sqlite` moves from indirect to direct at the same
already pinned version. Codex, codex-web and other dependency revisions are
unchanged; no consolidation is required.

## Migration and compatibility conclusion

Inventory: one direct migration from supported JSON schemas 1/2 to a schema-3
identity/cutover marker plus SQLite state, snapshots and shared settings. There
is no intermediate branch schema. The packet records that this migration has
never been merged, released, deployed or externally consumed; only disposable
fixtures have used it. The source and tests agree with that lineage.

The backup-before-marker and database-before-ready ordering, preserved original
scope/epochs/pending tuples, and refusal to restore a completed store from a stale
backup are appropriate. The lineage itself is sound, with application recovery
reachability incomplete as R1 describes. No existence guards accommodate an
unreleased intermediate schema.

Old strict readers reject the marker. The new package checker requires exact
integer `turnRetryEvidenceSQLite: 1` while preserving predecessor capability
keys. This supports the first forward upgrade and prevents selection of an
incompatible reader once retry records exist. Software recovery must remain
forward to a compatible package; an older reader cannot consume new SQLite
state. Native submission and session-policy schemas remain unchanged.

Discovered consumers inspected include browser scheduling/idle status, manual
browser cancellation, workspacecodex send/queue/team and cold-recovery wrappers,
lifecycle `CancelSession`, package preparation/activation compatibility and
native creation-test readers. The pinned codex-web API supplies the required
typed outcomes and exact generic receipts without a companion dependency change.

## Evidence, limits and disposition

Reviewed the packet, plan/design/state, repository instructions, applicable
workspace procedures, the mandatory review skill and all four lane references;
inspected code, complete commit history, final diffs, affected tests and owning
documentation. The repository worktree was clean at review start. No source
edits, tests, builds, live runtime inspection or other-session inspection were
performed. This report is the only file written.

Focused-check successes are lead-supplied evidence from the packet; this review
does not claim an independent rerun. Broad Go/browser/package/native checks are
still pending. Existing tests cover volume, restart, exact replay, store-level
cutover, revision conflict, receipt save failure and interruption. They do not
cover R1's caller reachability or R2's cold post-activation failure.

I also inspected the lead-raised optional-capture/legacy-proof concern. A
reason-only `holdRetryEvidence` does not itself invalidate the legacy shortcut.
I did not establish a production native lifecycle that both retains a legacy
proven snapshot for an unhandled active turn and subsequently appends input to
that same turn: normal proof creation occurs for terminal failures and saves
their handled watermark. I therefore have not promoted that concern to a
confirmed finding. A focused regression documenting the supported legacy case
would clarify the boundary; any newly supported path must remain conservative.

Reviewer identity: `/root/final_review`, a fresh independent standalone fallback,
outside the threadless initiative roster. Configured model/effort:
`gpt-6.1-sol` / `xhigh`, as supplied by the launcher assignment. All four lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility. Risk:
high because persisted-state conversion, uncertain delivery and forward recovery
are affected. No nested agents were used.

No Blocking findings. Address the two Important findings, or record explicit
decisions under the mandatory review procedure, before long integration checks.
This report grants no integration or deployment approval.
