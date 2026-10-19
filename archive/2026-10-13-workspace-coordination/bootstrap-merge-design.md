# Bounded integration of the retained bootstrap owner

Design proposal, 2026-10-13. Author: delegated GPT-6 Astra/xhigh designer.
The lead owns implementation, review, deployment and integration. This document
authorizes no operation. The current creation-fix rollout remains immutable.

## Decision

Use a dated, source-only, supervised integration helper for this installation.
It can load the exact selected package's Host and Engine and drive one ordinary
merge job at a time. A permanent bootstrap CLI privilege is unnecessary for the
known installation-only gap.

This is a **new reviewed maintenance route**, not an already supported public CLI.
Its support boundary is the frozen helper, selected runtime package, exact owner,
workspace, reservation and reviewed repository inventory. Document and test that
boundary. Do not present arbitrary Ruby calls into a private library as an
ordinary recovery procedure.

Keep the ordinary `--bootstrap-owner` allowlist unchanged. Do not change the
scheduler to admit queued bootstrap work. Do not create a conversation, transfer
ownership, acquire/release a machine reservation, deploy, or execute Git mutation
commands in the helper. The installed merge worker owns all actual integration.

The helper is substantive operational code, not tracking-only prose. Put a
maintainable implementation, focused fixtures and a dated procedure in the
workspace feature worktree, for example `bin/bootstrap-merge-2026-10-13`,
`test/bootstrap_merge_2026_10_13_test.rb` and
`docs/maintenance/bootstrap-merge-2026-10-13.md`. Do not add it to Nix exports,
the installed CLI, portal or automatic workers; do not use the shared-master
tracking exception to commit functional code. The owning workspace head will
change and needs the normal final review/integration gate. No runtime, extension
or configuration repin is intrinsically needed. Verify that the workspace's
evaluated application derivation remains identical before claiming that no
application redeployment is necessary. Its flake constructs the package from
inputs and explicit site/team/coordination configuration, rather than packaging
the whole workspace checkout. A source-only helper should therefore leave it
unchanged; this is a check, not assumed validation.

If the new workspace head descends from the deployed workspace head, completion
can use ordinary ancestry for that source. Adding this source-only commit does
not itself require a deployed-head replacement mapping. Rewriting previously
deployed history still requires the existing reviewed-lineage procedure.

An ephemeral uncommitted `ruby -e` workaround would not meet these requirements.

## Evidence and alternatives

The inspected runtime is the owned feature source at a10af6c4:

- `WorkspaceCoordinationHost#coordination_session_command` explicitly refuses
  new preparation/approval/submission through `--bootstrap-owner`.
- `Engine#existing_bootstrap_owner` verifies a retained, active, threadless,
  unfenced incarnation without creating an owner.
- `with_coordination_session_admission` supplies the selected-generation,
  session lock, lifecycle-journal and ready-creation checks.
- `prepare_merge`, `mutate('approve')`, `mutate('submit')`, `claim`,
  `dispatch`, `reconcile_attempts` and `dispatch_reconciliation` already
  support ordinary merge records belonging to a bootstrap owner.
- The worker rechecks approval and owner, serializes repository/common-Git
  resources, preserves hooks, performs the fast-forward/push and proves ancestry.
  It already handles shared workspace master separately from project targets.
- `run_coordinator` skips bootstrap owners. The existing `wait_bootstrap`
  performs synchronous owner-wide dispatch and inline recovery; it is not the
  right helper to reuse for a one-merge maintenance operation.

Thus the missing part is supervised admission, not a new execution or recovery
engine. Reusing the original deployment bootstrap would unnecessarily authorize
machine/profile activation. Adopting the owner into a new conversation would
change ownership and leave its old reservation unresolved. Direct Git operations
would bypass claims. Broadening normal bootstrap submit/approve or scheduler
admission would introduce lasting behavior beyond the demonstrated need.

A permanent `coordination-bootstrap-merge` command is the fallback only if the
helper cannot satisfy the exact scope/exclusion requirements below, or if this
becomes a recurring supported user operation. In that case put this same narrow
composition in `workspace-coordination-host.rb`; do not extend general bootstrap
privileges or introduce another worker format. It requires runtime tests and
docs, a new published runtime head, composed workspace/configuration pins,
review, package/system verification and a subsequent deployment before use.
That is additional work after the currently frozen rollout, not part of it.

## Frozen scope and prerequisite

Bind the helper's reviewed plan to:

- Workspace `/home/aither/workspace/ai/vpsfree.cz`, registered name from the
  real registry, session `2026-10-13-workspace-coordination`.
- Owner `55e83d75-cb96-417a-9308-11d3caf22dcd`.
- Existing reservation `d114323d-806c-479f-b7a4-8c1a08afb45b`, owned by that
  owner and in `deployed_review`.
- Exactly `dev-workspace`, `vpsfree-dev-workspace`, `workspace` and
  `vpsfree-cz-configuration`, each targeting `refs/heads/master`.
- Exact final feature heads, current review/evidence hashes, canonical catalog
  and remotes, selected package path and current profile token. The helper's own
  workspace commit changes the workspace head; freeze it only after its final
  review and comparison capture. The other presently reviewed heads are
  a10af6c4, c697acc7 and fbbda8e9; use full hashes in machine inputs.
- The actual user instruction, with source/reference:
  “ok, after you'll deploy the fix, you can merge the changes”.

Execution requires the lead's frozen evidence that the creation fix was
successfully deployed and accepted. A quote alone does not prove that condition.
Verify those checksummed evidence files before initial admission. Existing
user approval covers only its stated repository/target set; follow the Git
procedure for any material scope change and final branch-history checks.

Capture comparisons and verify publication before preparing each merge. The
shared root's newly published baseline is 90005ea3a7a170b23699c38933b111b046ce43f8
at design time; fetch and check it again at execution. Old local project master
refs that are ancestors of remote master are valid input to `prepare_merge`;
do not reset or rewrite them as a prerequisite.

Use serial execution, preferably runtime, extension, configuration, then
workspace. The final workspace operation remains an ordinary approved
fast-forward on the shared root, preserving unrelated files and index changes.
No cross-repository atomicity is promised. Record each succeeded job/head before
continuing.

## Caller, lifecycle and generation admission

Load `libexec/workspace-host` from the exact selected installed package with
the package's Ruby/environment. Do not load a worktree implementation, monkeypatch
Host/Engine/Worker, set fixture mode, or enable `@bootstrap_token`. The loaded
Host computes `package_root` from its own installed file. Give the helper a name
that does not contain `workspace-host`, because that loaded source otherwise
runs its CLI entry point.

Select the actual registry entry; check the frozen workspace/name, profile,
package, catalog and invocation environment rather than accepting arbitrary
state-root/profile/registry overrides. Ambient session identity, when present,
must match the frozen identity. A threadless owner intentionally has no native
session conversation; the exact retained-owner selector is its authority.

At initial admission, preparation publication, approval/submission and **every
new claim**, enter the installed `with_coordination_session_admission`, then:

1. Call `engine.current_generation!` as well as the Host generation guard.
   The engine's captured token detects a switch/rollback between separate lock
   acquisitions even when the package path is the same.
2. Call `existing_bootstrap_owner` with the exact UUID and slug.
3. Check the held reservation and frozen repository/target obligations. New
   work refuses released/blocked reservations, suspension, changed incarnation,
   lifecycle fences/journals, changed registration or changed catalog.
4. Enforce the supervised-owner exclusion described below.

Preparation's Git fetches, source retention and hook environment builds run
outside these locks, using `prepare_merge`. Reenter admission and revalidate the
returned snapshot before publishing it. Do not hold transition/session/ledger
locks over worker waits, network reconciliation or hook preparation.

## One-job scope and the necessary supervised window

The installed `claim(owner_id:)` filters by owner, **not by job**. It cannot be
treated as an exact-job API. Require the completed rollout's driver/worker units
to have exited, no other nonterminal job for this bootstrap owner, and an
explicitly recorded maintenance window in which the lead starts no other
bootstrap deployment or integration for this owner. Use a helper process lock
to serialize this helper's executions; unrelated sessions remain eligible.

On retry, the sole nonterminal owner job may be the saved exact merge. Recheck
this inventory under ordinary session admission before claiming, and require
the result to be either no job or precisely that job. Never dispatch a returned
unexpected job or quietly expand the operation's scope.

The process lock alone does not exclude the existing candidate-only deployment
bootstrap, which does not hold session admission across all of its engine
calls. The operational exclusion is therefore a real prerequisite, not a claim
of automatic mutual exclusion. A trusted lead can satisfy it for this one
quiescent retained owner. If concurrent bootstrap submissions must be supported,
stop this route and implement an installed exact-job claim filter instead;
do not copy/replace `claim` or edit other jobs to make owner-wide selection fit.

## Preparation and exact retries

Use two stages with separate request identities. All new authority uses the
existing Store request receipts; immutable payloads use `save_artifact`.
Do not introduce a bespoke journal, receipt validator or direct ledger editing.

The preparation request has `schema: 1`, caller-generated `requestId: P`,
one frozen repository selection, evidence and actual user-instruction source.
The frozen plan supplies the exact owner/reservation, target, expected reviewed
head and package bindings. Bound input through the existing request reader and
strict key checks.

1. Under admission, look up the ordinary request receipt for
   `[ownerId, "bootstrap-merge-prepare-2026-10-13", request]`.
   An exact existing receipt returns its retained result before capacity/build
   work; altered input under P refuses.
2. Otherwise run `prepare_merge` outside admission and verify its target,
   feature head, catalog and generation against the frozen plan.
3. Save a small immutable bundle through `save_artifact`: kind, owner and plan
   binding, original preparation input, exact returned snapshot, normal approval
   source/scope, and stable distinct IDs A and E for approval and submission.
   Derive A/E from P, owner and explicit versioned labels, or generate them once
   in this bundle. Do not regenerate them during execution.
4. Under revalidated admission, publish only a bounded receipt containing the
   bundle ID and returned execution request via `Store#request` inside
   `Store#transaction`. The execution request is
   `{schema: 1, requestId: E, artifact: BUNDLE_ID}`.
   Reload the winning receipt if concurrent identical preparation raced.
   Large snapshots belong in the artifact, not a 16 KiB receipt.

A crash before publication may leave unused retained sources/artifacts; no merge
was admitted. Retry P and retain them. After publication an exact preparation
retry returns the same bundle and E, never a newly prepared replacement.
A changed baseline/head requires new review/evidence as appropriate and a new P;
never overwrite the old bundle. If any prior attempt has uncertain effects,
reconcile it before preparing a replacement for that target.

## Approval, submission and execution retries

Resolve the immutable bundle and compare all bindings, including E. Reject caller
substitution of another snapshot, target, source quote, kind or request ID.

Under admission, call the ordinary `mutate` methods:

- `approve`, request A: kind `merge`, one exact repository/target scope,
  stored actual `source`, and `reviewedSnapshot: snapshot.id`; omit
  `iterationScope`.
- `submit`, request E: kind `merge`, empty dependencies, returned approval ID,
  `reservationId: null`, and the exact stored snapshot.

The submit receipt is the canonical execution receipt. No separate outer
“accepted” receipt is necessary. The bundle and its fixed A/E prevent repeating
the merge with a fresh identity. Both calls retain the existing capacity checks.
A failure between approval and submit leaves an inert approval; retry reuses it.
A lost response after submit reuses E and the original job.

Crucially, **do not eagerly rerun `snapshot` validation before calling the
receipt-aware mutations on an execution retry**. A successful worker changes the
target checkout/local refs, and the old snapshot is expected to be stale then.
The existing mutations return exact retained receipts before live snapshot
validation; preserve that ordering. Still validate the immutable artifact,
owner, caller and generation. A first submit without a receipt performs all
normal snapshot validation. Conflicting reuse of A/E fails through Store.

The synchronous driver records/prints the exact job ID before waiting. It reads
the saved job's current state, consumes existing result receipts through
`reconcile_attempts`, and claims only under the admission/exclusion above.
Dispatch the returned exact job through `dispatch` outside locks. Thereafter
never dispatch a claimed/running/reconciling attempt again.

For recovery, call `dispatch_reconciliation` for the original attempt outside
locks. That reuses the independent reconciliation service, worker lock, running
unit checks and retry delay; do not perform Git probes or reimplement outcome
classification in the helper. Busy resources wait without taking another
session's reservation; the lead continues the skill's bounded visible monitoring.

Return success only when the exact job is `succeeded`, with job/attempt IDs,
repository, target, feature head and observed remote proof. `needs_refresh`
means stop for reviewed refresh; failed/canceled means stop; ambiguous recovery
retains the claim and reports the original job, rather than creating a new one.
Interruption cancels only the waiting driver, not accepted work.

The dated helper has no refresh action. For an unclaimed `needs_refresh` job,
use the already supported exact-owner `cancel` command with its current revision
and a fresh cancellation request ID, then prepare a new P after the required
rebase/review. A failed job with proved no effect is already terminal. Never
cancel or replace a claimed or ambiguous attempt to evade recovery.

## Recovery and compatibility limits

No schema, owner/job/approval/reservation shape, worker envelope, deployment
history, package contract, API/client or NixOS/vpsAdminOS protocol changes are
needed. The extra opaque preparation receipt and generic immutable artifact are
accepted by current Store validation. Older packages can read ordinary merge
jobs and consume/reconcile their attempts; they do not need to understand the
helper. They still skip claiming unstarted bootstrap jobs.

If the helper dies before a claim, retry the same E to resume admission. If it
dies after dispatch, the independent worker continues. If it dies after claim
but before a durable attempt request, retain the claim for operator recovery,
as the existing guide requires; absence of a request is not permission to
redispatch. Failed/lost push replies use the existing exact remote-ancestry
reconciliation. A local fast-forward with an unproved remote effect remains
held; the helper neither pushes it again nor resets it.

A package/generation change stops new helper admission. Already admitted workers
and ordinary `--bootstrap-owner ... reconcile` retain their existing recovery
semantics. Do not relax generation checks so the dated helper works against an
unreviewed successor. Package rollback remains subject to the existing supported
coordination contract; no pre-contract package is made eligible.

All merges leave the original reservation, history and deployment ownership
unchanged. `finish`, exact final/deployed-head proofs, independently reviewed
replacement lineage where needed, and explicit review/deployment completion
remain separate. This task grants no release, archive, delete or reboot.

## Verification and documentation

Quick disposable tests should prove:

- Wrong package/token/owner/workspace/incarnation, lifecycle/creation blockers,
  reservation mismatch, broadened repo/target/kind, missing deployment condition,
  altered bundle/source/evidence and concurrent owner work all refuse.
- Preparation receipt retries preserve the exact bundle; changed P input fails.
  Execute retries after approval-only and after completed merge reuse A/E/job,
  including a changed target checkout. Concurrent exact retries create one job.
- Ordinary public bootstrap prepare/approve/submit remain unavailable.
- Capacity refuses new work without damaging retained state; accepted receipt
  retries and existing recovery still work.
- The real installed Engine/Worker on private Git fixtures integrates a project
  and a shared-root workspace, preserves unrelated shared files/index, honors
  hooks, retains feature refs and leaves reservation/notification state alone.
- Stale remote/local target and changed feature evidence fail before mutation.
  Other-owner claims preserve FIFO/resource exclusion.

After committed-helper final review, a fresh verification watcher runs the
uncertain-duration private systemd fixture: kill the driver after dispatch,
settle the original worker; stop a worker and recover via the independent
reconciler; stall that probe and prove unrelated work remains usable. Include
the claim-without-request refusal. Load retained ordinary records with the
selected predecessor reader as a compatibility check; no new decoder should be
required. Do not use real default-branch pushes as a test.

The dated procedure documents supported package/helper identities, the owner
exclusion, two-stage requests, exact retry commands, known interrupted-claim
limit, and separate finish/release. Keep exact rollout success and request/job
IDs in this initiative's rollout/state artifacts. Update final branch inventory
and review evidence for the workspace helper commit; prove unchanged application
derivation before retaining the current deployment as sufficient. Publish/capture
the final workspace comparison under the normal Git procedure.

The inspected code supports this design; these checks and the helper itself
have not been implemented or executed by the designer. The lead should register
this design artifact and fold its decision into the main design/state record.

