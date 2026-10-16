# Background integration design and verification brief

Lead owns design and edits; no retained roster is configured. The requested feature is substantive and uses xhigh design/implementation policy. Local operator is trusted; preserve checks for mistakes, concurrency, state integrity and remote clients.

## Interfaces and state

Add --background to integrate and integration-resume and add integration-pause. Existing calls and schema-1 requests stay unchanged. Background journals use schema 2 with continuation state, revision observation and notification sequence. Read schema-1 manual journals without migration. Package metadata advertises journalSchema 2; new readers accept 1 and 2, predecessors reject schema-2 retained journals. Ledger, snapshots, adapter and attempt envelopes stay schema 1.

Use existing durable step requestIds and ledger receipts to associate jobs/reservations with background runs; do not add routing fields to operation records. Publish the step identity before submitting, so routing works even when the submit reply or journal update is lost. Suppress per-operation native events for background-owned operations, including machine grants; final/actionable run events use the existing native outbox. Reserve bounded recovery capacity for each unfinished background run.

The scheduler discovers background journals for each verified owner and launches at most one per-run systemd transient worker. A worker advances once outside scheduler/admission locks. Waiting runs are redispatched only when the ledger revision changes; the existing five-second scheduler tick recovers missed wakeups and exited workers. No agent, browser or attached CLI is needed. Save continuation observations before exit and wake the scheduler on publication. Slow preparation never runs in the scheduler.

Persist intervention on non-transient errors; conflict semantics, stale machine artifacts, changed scope and uncertain effects remain lead work. Retry the internal AdmissionBusy contention signal (CLI exit 75); failed external commands remain actionable even when their CLI status is 75; generation handover leaves a runnable run for the selected compatible runtime. Reuse the exact run/step/job identities. No blind activation replay.

Pause is an independently durable owner-bound marker, accepted without waiting for the run lock; it prevents the next admitted step. Resume removes it under the run lock. Background step and admission guards recheck selected generation, owner identity/fence, suspension and pause. Archive/delete fence pending work and preserve deployed recovery ownership. Revival does not silently resume paused/held background work.

## Completion and notifications

Run events are written before their notification sequence is saved so a crash can retry the deterministic event identity. Worker finalization is rediscovered on delivery acknowledgment. Publish completion notification before allowing lifecycle complete, and never wait for that same event in pre-completion finish checks. Preserve settled prior deliveries and all existing integration/release proofs. Completed operational work may still hold a machine for review.

## Documentation, rollout and verification

Own behavior/compatibility in runtime integration and coordination guides. Workspace docs replace active waits with background-submit/end-turn guidance. Operations shows compact background run progress and reasons. vpsfree-cz-configuration remains the deployment owner for the aitherdev system; application stays in user profile. Pin the same reviewed runtime in both input graphs and verify the exact final configuration artifact.

Quick checks: focused Ruby integration/coordinator suites, Ruby syntax, Go metadata/coordination tests and browser contracts. Final committed review must cover whole-branch history, state schemas and no database migrations, notification routing/crash races, capacity, lifecycle, generation handover and scope. Only then run packaged/systemd/native tests and build configuration. Verify two contending sessions need zero model calls during waiting and one deduplicated action/review wake.

## Current deployment constraint

This tracking-only initiative has no native owner. The preceding attempted session has an unresolved initial-request refusal, preserved in plan/state. Implement and test with isolated fixtures; do not submit live deployment without a valid retained conversation owner.
