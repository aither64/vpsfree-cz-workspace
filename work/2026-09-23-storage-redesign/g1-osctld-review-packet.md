# G1 osctld activity status review packet

## Final checkpoint, 2026-09-25

The reviewed feature commit was amended for two VM-fixture-only corrections
and one export-spec fake correction, then published at
`dcad075a171244cc17d67d625ab89c402d11781e`. Reviewer0's initial
four-lane review and both affected-lane reruns found no Blocking or Important
issue; the reruns confirmed that the runtime diff is unchanged.
The focused osctld unit selection passed 26/0. The registered
`osctld/storage-activity` VM test passed all three real UNIX-command examples
at the runtime-equivalent preceding head. The corrected export spec passed
10/0; normal Nixfmt/RuboCop hooks passed. The remainder of this
packet records the original pre-integration review scope and evidence.

Review the committed vpsAdminOS feature change at
`8e44a5124439b1f3048ffc56b1717614a5360358..d43bab508d4cf766243ad89558ea042afea7d414`
in `worktrees/2026-09-23-storage-redesign/vpsadminos`. The branch is
`2026-09-23-storage-redesign`, based on the exact vpsAdmin flake-pinned
vpsAdminOS revision. The owning plan and current state are
`work/2026-09-23-storage-redesign/{plan,state}.md`; the G1 design is in
`storage-integrity-design.md`. Review the full one-commit diff and its
message, not only the final source tree.

## Outcome and boundary

The first G1 slice adds a generic, read-only osctld
`pool_storage_activity` command for exactly one zpool. It reports a bounded
version-1 `gc_trash_v1` sample with daemon boot identity, pool import
identity, monotonic daemon-lifetime generation, pending/running GC and trash
counts, registered run-dataset count, worker liveness and sticky unknown or
overflow conditions. The tracker observes enqueue through completion,
timer prunes, synchronous trash moves and pool lifecycle. An absent,
stopping, unproved or older pool/daemon must never be described as idle.

This is one commit because the tracker, its GC/trash/lifecycle hooks, command,
unit coverage, VM command fixture and interface documentation form one
provider-side protocol. vpsAdmin/NodeCtld consumption is deliberately a later
commit. vpsAdmin currently pins the base revision, so this new command is
not deployed or called by that application. New osctld with an old consumer
is inert; an old osctld will make the later consumer report unknown. No
schema, on-disk format, write fence, strict dispatch, `repair_ready`, verified
scope, reconciliation APPLY, vpsAdmin input pin, node rollout or production
action changes in this commit.

The public interface owner is vpsAdminOS osctld, not vpsAdmin. The immediate
generic caller is the osctld UNIX command protocol; a later signed NodeCtld
adapter will call it. The existing `osctl` CLI and pinned vpsAdmin revision
remain unchanged. The implementation is intended to work without vpsAdmin.
The eventual consumer must deduplicate managed roots by zpool and map missing
or invalid samples to unknown. Storage-only nodes may lack an osctld-imported
zpool; this slice does not decide a not-applicable policy.

## Evidence and open gates

- Focused Nix osctld selection after final spec edits: 26 examples, 0
  failures, seed 28084. It covers tracker cardinality/unknown/generation,
  GC/trash enqueue, timer, synchronous work and command validation. The
  initial fixture run failed 26/3 because worker tests lacked a logger and
  one kill test raced the worker entering its ensure; those test fixtures
  were corrected without changing runtime policy.
- Ruby syntax passed for changed files; targeted RuboCop passed. The normal
  commit hook passed Nixfmt and RuboCop; staged diff --check passed.
- `tests/suite/osctld/storage-activity.nix` is registered in
  `tests/all-tests.nix` and exercises the real UNIX command. It has **not**
  yet been run; the mandatory review precedes that long VM test.
- The local native-extension build left `libosctl/tmp/` untracked and outside
  the commit. No other source changes are pending.

Risk classification: **High** because this is a privileged host-daemon
protocol and a future cross-project safety signal. Review all four lanes:
general, architecture/repetition, scope/proportionality, and
risk/compatibility. Retained independent reviewer0 is the lowest-index ready
review-purpose member, saved GPT-6 Sol/xhigh, read-only. The reviewer should
inspect repository and workspace instructions, all lane references, the
committed diff, adjacent workers/queue/Pool export paths, tests, documentation
and the actual vpsAdmin/vpsAdminOS pin relationship. Report Blocking,
Important and Advisory findings with evidence. Do not edit or start the VM
test. The lead will reconcile findings and decide the next verification step.

Known limits: `gc_trash_v1` does not prove NodeCtld all-queue activity,
supervised child-process exit, general osctld commands, future work absence,
or independent root/osctld writes. GC export leaves its old worker behavior
unchanged; any lingering worker must make the sample unknown. No change in
this review may be described as a full node-quiescence barrier or permission
for repair.
