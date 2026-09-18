# Recovery review: architecture and repetition

Reviewed with gpt-6-astra at xhigh, as explicitly selected by the user. No
subagents were used. The review covers vpsadmin
`014fbc78422f3660b295add7a50f35cc7acdf0c8..268f7d09b9e3ca59d2b8f286e6666f72f9f7a9ff`
and vpsfree-maintenance-tasks
`6eea682ede8d8e2634b2d41e5b11cf0f02231bc6..c77ff3742f623afd23c0be26c0f6ddbc026f1ba4`.

## Findings

### Blocking A1: the installed launcher never enters the repair CLI

Maintenance commit `c77ff3742f623afd23c0be26c0f6ddbc026f1ba4`,
`2026-09-14-repair-kernel-history-bounds/repair_kernel_history_bounds.rb:83`.
The executable selects `vpsadmin-api-ruby` in its shebang, but only calls the
CLI when `$0 == __FILE__`. The actual owning launcher at the reviewed vpsAdmin
revision, `nixos/modules/vpsadmin/api-runners.nix:44`, adds the installed API
load path and then calls `load script` at line 47. It does not change `$0`.
Consequently `$0` remains the generated Ruby runner path while `__FILE__` is
the maintenance script, and the guard is false.

Concrete failure: on an updated API host, every documented direct invocation
(`./repair_kernel_history_bounds.rb`, `--apply`, and even `--help`) defines the
module and exits successfully without previewing, repairing, or reporting any
totals. No database operation is reached. An operator can mistake the successful
exit for a completed invocation.

The consumer validation misses this boundary:
`spec/runner_spec.rb:104` invokes `RbConfig.ruby` directly on the script, which
sets `$0` to the maintenance script and makes the test pass.

Reproduced without accessing a database, using the reviewed vpsAdmin API Nix
shell and the real maintenance script. Direct Ruby execution with `--help`
produced 483 bytes; execution through `ruby -e 'load ARGV.shift' SCRIPT --help`,
matching the installed launcher's relevant behavior, produced zero bytes and
exit status 0.

Keep the fix local to the dated task: separate its importable Runner/CLI code
from the executable and invoke the CLI unconditionally from the executable, or
use an equivalent entrypoint compatible with the existing loader. Add a
subprocess check through the launcher's `load` semantics, covering help and
disposable-database preview/apply. Changing the generic installed launcher is
unnecessary for this task.

### Advisory A2: the borrowed batch default contradicts the declared task contract

Maintenance commit `c77ff3742f623afd23c0be26c0f6ddbc026f1ba4`,
`repair_kernel_history_bounds.rb:11` and `node_repair.rb:18`, within the dated
task directory. Both defaults come from
`VpsAdmin::API::Operations::Node::HistoryBackfill::DEFAULT_BATCH_SIZE`, whose
actual value is **10,000** in
`vpsadmin/api/lib/vpsadmin/api/operations/node/history_backfill.rb:2` at both
reviewed feature commits. The CLI help at line 52, README, accepted follow-up,
and review packet all promise **1,000**.

Concrete failure: omitting `--batch-size` processes evidence batches ten times
larger than advertised. Future tuning of the unrelated raw-status history
backfill can silently change this dated repair again while its help stays
unchanged. The existing help test checks the literal text, not the effective
default used by the Runner.

Make the intended default explicit and consistent. Given the accepted 1,000
requirement, a task-owned default reused by Runner, NodeRepair and help is
appropriate. If 10,000 is intentionally selected instead, record that decision
and correct the operational documentation. This does not presently make a
repair unsafe or unbounded.

No other Blocking or Important architecture/repetition finding was identified.

## Boundary and ownership assessment

- `KernelEvidence::StableState` owns stable boot/release/effective-patch
  comparison. Actual implementation consumers are the permanent recorder and
  this maintenance task; both import that provider. Provider specs cover boot
  identity, incomplete/transitioning reports, enrichment changes and legacy
  inventories hiding active patches. Task specs exercise the shared predicate
  against retained immutable evidence. No equivalent repair remains in the API.
- `SnapshotReader.comparison` supplies the actual supervisor ingestion consumer
  with current, checkpoint or retained-event evidence and its original time.
  The checkpoint uses the existing normalized `Report.to_h`/`from_hash`
  contract, rather than introducing another component serializer. Checkpoint
  capture, valid event recording, current replacement and checkpoint deletion
  are within the existing node lock and transaction.
- The private checkpoint is a separate one-row-per-node model with a unique
  index and cascading node foreign key. Public evidence/component resources
  select `NodeKernelEvidence` and its children, and no checkpoint resource is
  registered. The API regression verifies that adding a checkpoint changes
  neither those rows nor endpoint inventory. Repair proof selection explicitly
  queries event snapshots, so private checkpoints cannot become historical
  repair evidence.
- The dated task owns all-node selection, repeatable filters, fixed candidate
  membership, output and per-node orchestration. `NodeRepair` owns proof
  selection and revalidation. It compares the target, predecessor and supporting
  evidence again under the node lock, including stored-digest checks for
  normalized child-row drift, before updating only the lower bound normally.
  This is an appropriate task-local boundary; it does not need a generic repair
  framework.
- Supervisor regressions cover unchanged confirmations, malformed/repeated/
  missing/stale reports, restarts, failed recovery writes, new boots, role
  changes, newer retained events after older writers, and component histories.
  The synthetic integration extension drives the real ingestion path and
  supervisor restart without changing host patch state.

## Verification and residual limits

Read workspace and both project AGENTS.md files, the review skill and
architecture reference, plan/state/packet/rollout, both vpsAdmin commits,
maintenance implementation/tests, current provider consumers and installed
launcher. Inspected public resource selection and revision calculation.
Ran only the focused no-database launcher reproduction above; did not rerun
the reported database suites or begin integration testing. Project worktrees
remain clean. No code, production, state.md, instructions or session lifecycle
were changed.

The final configuration and KB pins are explicitly deferred to a later review.
Mixed older writers can still discard observations that they never checkpoint;
the implementation can prefer a newer retained event but cannot reconstruct
already lost reports. Historical repair also depends on retained immutable
evidence. Those limits are already documented and do not require a broader
abstraction in this change.
