# Start diagnostics, July comparison and shutdown/import proposal

Published vpsadminos feature branch `2026-11-13-osctld-start-recovery-errors`,
head `25101c51e893c480f083c1812f07d3b1d3788a62`, base/observed remote staging
`c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`. No default-branch integration,
production changes or deployment. Session remains active and open.

## Implemented

`Container#start_block_reason` identifies the first existing blocker: staged,
error state, container recovery taint, network-interface taint or inactive pool.
It shares one decision with the Boolean predicate and preserves precedence and
the guard before force/no-op/start effects. Taint errors include available
recorded interface identity and a safely quoted pool/ID cleanup command with
stopped/resource-inspection prerequisites. They do not invent historical causes
or probe/mutate resources. Normal Restart and custom Boot use the common error.
Foreground start/restart/boot end the inherited console connection, reap its
child and restore the terminal before reporting the original error.

The existing osctl manual explains recorded versus live identity, diagnostic
limits, active `recover state` effects and conditional recovery. A full tainted
cleanup still requires fresh stopped/no-init proof; absent-link acknowledgement
still requires both name and index absent for veth and recorded IFB, plus owner
checks. Live/reused links refuse. No auto-clearing taint, force safety bypass,
blind link deletion/adoption or hand-edited daemon metadata was added.

No YAML/runtime schema, hook protocol, API error envelope or CLI option change.
Node-by-node userspace update and ordinary rollback remain compatible. External
scripts parsing the old free-form literal may need adjustment. Async queue/raw
console behavior and Boot's earlier effects retain their existing boundaries.

## July branch comparison

Exact OS July `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44` and admin July
`807e9d7f1277217d3cf2d49b7c4b2525dc441c10` were read only; refs and fresh SSH
remote heads matched. No old-session record/ref/worktree/team was changed or
contacted. Full source/test citations and variant matrix: [july-comparison.md](july-comparison.md).

July improves already-admitted lifecycle concurrency: durable accepted intent,
generations, callback/reconciliation leases and cleanup before replacement.
It still does not solve this full incident class:

- `CtPostStop` and `VethDown` still reject before CT DB publication; reducer
  leases cannot help when lookup fails. Hooks have no retry/spool during blackout.
- `Recovery#recover_stopped_run` uses the saved `run_conf.reboot?`. An unseen
  guest reboot target cannot be reconstructed from stopped state; accepted/saved
  reboot and separate newer intents are different, supported cases.
- July's Veth behavior is name based and lacks the deployed tuple/taint gates.
  It cannot prove safe handling of c0ad0ad's retained/reused host-link ownership.
- Tests cover accepted halt/reboot, reboot-plus-start and daemon restart during
  driven operations, but the inspected cases do not combine guest target loss,
  prepublication import and deployed kernel-link identity safety. No July tests
  were rerun; historical green workflows remain recorded evidence only.

Current-source late publication supports the incident hypothesis, but exact hook
responses and the shutdown initiator were not captured. No production query or
runtime reproduction was performed. See [race-evidence.md](race-evidence.md).

## Proposed race solution, not implemented

[Architect design](design.md) recommends a narrow per-run terminal target record
written before socket delivery, bound to root-authoritative owner/run/host-boot
launch registration, plus per-CT import readiness and exact-run attachment/
retirement serialization. Import reconciles retained outcomes and unfinished
cleanup; reboot gets one successor reservation only after cleanup and pool
readiness. A newer explicit stop wins. Stopped state alone never implies a
reboot. Existing host-link identity/ownership refusals remain; uncertain cleanup
leaves the intent visibly pending instead of silently treating reboot as halt.

Earlier DB publication alone misses downtime and attachment races. Readiness
alone is a useful partial fix but cannot recover lost targets. Bounded hook
retry retains intent only while its process survives. Importing July is much
broader and still leaves the target/admission gaps.

Future release must prove atomic writer authority, immutable managed/direct LXC
launch binding, crash recovery, legacy-hook coverage, explicit-stop precedence
and rollback fencing. No fleet-synchronous update is needed: adopt node by node,
but already-running old hooks require a newly bound run or proven live handover
for full coverage. Pending new-format outcomes cannot safely be ignored by an
old daemon on downgrade. Deterministic import-phase, crash, duplicate/stale,
wrong-owner/boot/run, link-reuse/IFB, stop/reboot and old/new combination cases
are specified in the design. Broader execution requires a new authorized scope.

## Verification and readiness

Independent reviewer0 (retained Sol/xhigh) reviewed the full branch/history under
all four lanes: [report](review-result.md), [packet and narrow-fix receipt](review.md).
Important foreground inherited-socket hang was reproduced by all three real
fork tests on old code, then fixed and directly inspected under the review
skill's narrow-remediation rule. Advisory commit-message validation context was
also fixed. Final series remains one logical commit, no migrations, superseded
approaches or repeated pin streams. Manual placement and safety preservation
passed independent review.

Quick evidence: 236 daemon examples; final affected client/CLI/Console 49
examples; real fork regressions fail on original/pass on fixed code; man render,
RuboCop, mandatory hooks and empty affected metadata refresh pass. Details and
logs: [state.md](state.md).

Longer verification remains active, so final readiness is pending. The exact-head
packaged OS build, RSpec and RuboCop passed. The local VM has passed the relevant
host-link recovery case (replacement refusal, guarded absence acknowledgement,
cleanup and subsequent start) plus its first six cases; its unchanged repeated
and pooled cleanup cases still run. The whole suite has no terminal result yet.
Broader automatic CI includes queued test/livepatch jobs. No full-suite pass is
claimed. Runtime monitor `96bc2e32-43ad-48bd-b351-d7080dd66443` owns the exact
local command and durable result delivery to this lead; source session 71405,
utility thread `01a1d729-2160-7340-b724-0fc36d97ac2c`. On its report the lead must
interpret the result, inspect failures before any retry, then finish exact-head
CI observation with a fresh utility if still running and update readiness. This
is an active managed continuation, not a request for the user to chase checks.
No merge, deployment or session lifecycle operation is authorized.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-osctld-start-recovery-errors/)
