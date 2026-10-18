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

## Deployment ownership

Startup is resolved. This initiative has its own ready managed owner and native notification destination, recorded in state.md. Deployment uses that owner and its existing queued reservation; it does not adopt the original initiative or another machine holder.

## Compatible first upgrade with retained manual runs

The completed older initiative left a schema-1 manual run pending. Treating that journal as completed, removing it, or mutating its owner is outside this initiative. Correct our new package capability advertisement instead. No foreign session state or machine ownership changes.

Keep package.json integration exactly {journalSchema: 1, certificationSchema: 1}, the existing manual ABI understood by strict predecessor package readers. Install a separate share/dev-workspace/integration-contract.json with schema 1, journalSchemas [1,2], certificationSchema 1. The new Ruby Store validates the optional schema-1 contract and requires its unique positive-integer journal read set to include the legacy schema 1 and every retained schema. Additional declared reader versions are compatible when the required retained version is included. A predecessor package lacking the file supports only schema 1. Missing or malformed support for a retained schema-2 journal refuses selection, including completed schema-2 journals. The sidecar does not change ledger, journal, snapshot, adapter, or native formats and does not advertise a package.json shape rejected by older Go loaders. Remove the unnecessary unmerged Go allowance for package.json journalSchema 2; no deployed package used that metadata.

This permits ordinary old-to-new profile activation with pending manual runs: the predecessor accepts its unchanged legacy descriptor, and the new executor can resume both journal schemas. Pending old runs remain pending for their owner and are never automatically retried by background continuation. System then profile ordering, reservation/approval guards and forward-only recovery remain unchanged. No bridge generation or foreign repair is required. The former drain instruction is replaced in owning runtime docs.

Verify the exact old Store against a candidate carrying the new sidecar with a real pending manual journal fixture; verify new Store accepts a dual-reader target, refuses legacy-only/malformed contracts for active and completed schema-2 journals, and still accepts legacy targets for schema-1 state. Keep strict Go legacy metadata validation and packaged contract checks. Rebase onto archive runtime 59833652 preserving tracking sync and its package recovery metadata. Resolve only the archive recovery fixture dependency list by including both helpers. Run focused quick checks, commit the completed deliverable and independently review affected compatibility/composition lanes before longer package, systemd, native and consumer builds. Repin published exact final runtime in both consumers through their normal Nix/confctl routes and consolidate each unconsumed pin stream. Existing user authorization continues to cover the same three repository/master targets after live deployment and verification; no new repository or machine action is introduced.

## Review remediation: recovery progress

The reviewer reproduced a lost batch reply followed by completed jobs before continuation restarts. Replay can advance only the integration journal without changing the ledger; marking that observation waiting can strand the run. After a successful continuation pass, keep the run runnable when its phase changes or a retained pending refresh is consumed. A following pass can observe the new phase/jobs before sleeping on the ledger. Unchanged waiting phases still park at their observed ledger revision. This is a direct crash-recovery correction inside the reviewed background contract, without new states or external behavior. Add a regression with real fixture operation completion, replayed submit receipt and scheduler dispatch, preserving job identity and one final notice.
