# Current generic sysctl CI failure

Terminal receipt: exact846bb run39767770407, attempt1, completed with
`failure` at2026-10-23T01:14:16Z. All11 jobs are terminal:8success/3failure.
The failed jobs are product119793311317 (124 tests passed, six failed),
AMD-scale-aged-v6 119793311395 (CPU127 scheduler-hotplug warning), and
AMD-scale-aged-v5 119793311416 (CPU114 RCU stalls). Final `amd-fresh` and `amd`
jobs passed. Workflow wall time11:03:56Z–01:14:16Z is14h10m20s, including
allocation waits; it is not one test's runtime.

The source was already merged into `staging` at17:19:40Z under the explicit
product-six/v6 exception. The later v5 RCU failure was separately reported
and is outside that earlier exception. No green-CI or causal-exclusion claim
is made. Root-cause/test-value investigation belongs to the separately
assigned session; no repair, rerun, revert or further monitoring is selected.

Authoritative metadata captured01:14:27Z is retained in
`generic-sysctl-ci-39767770407-terminal-{run,jobs,artifacts}.json`. Terminal
retrieval supplied full logs for all three failed jobs under
`generic-sysctl-ci-39767770407-terminal-failure-*/job.log` and native artifacts
under `generic-sysctl-ci-39767770407-terminal-artifact-*/files/`; earlier first
evidence remains intact. Watch exit1 ended01:14:20Z; watcher CLI/tool exit0.
The01:16:30Z local receipt `generic-sysctl-ci-39767770407-no-active-observer.json`
confirms former watch PIDs absent and zero matching active watch processes.
The sole watcher has returned. Branches, worktrees and session remain open.

## Earlier failure and approval checkpoints

Subsequent user steering accepted these observed six product failures and
AMD-scale-aged-v6 warning as nonblocking for merging846bb. This does not change
the failed test results or establish causal exclusion. Root-cause and test-value
investigation moves to a new lead-created session; this lane retains current
CI observation/Git only. Integration still waits for lead's final freshness
release, with distinct new failures reportable. No blind rerun is selected.

Exact head `846bb469505789ba0b2a405fa5905ba6d8253006`, run
[39767770407](https://github.com/vpsfreecz/vpsadminos/actions/runs/39767770407),
attempt1. Product job `119793311317` failed after3h6m41s; the sole watcher
reported it at the scheduled refresh, relayed14:42:27Z. Overall CI still has
unfinished AMD jobs. Conditional `vpsadminos` → `staging` integration is blocked;
no repository claim, merge, source repair or rerun was selected.

The native suite completed338 scripts in130 tests:124 passed, six failed,
8782.07s. This is executed guest failure, not a prebuild failure. The current
CI `system/sysctl` test itself passed in89.08s at13:26:05–13:27:34Z, with
native `expected_success`; the separately accepted focused local run passed
all8 examples with exact exit0. Neither passing check makes the whole CI green.

## First errors

The following five cases failed `assert_retained` at
`tests/suite/upgrade/common.nix:1534` after successful userspace activation:

| Test | Expected boot dataset suffix | Actual | Init PID before/after |
| --- | --- | --- | --- |
| upgrade/from-6.12-guests | impermanence-4febac | tank/ct/niximpermanent | 6191 |
| upgrade/from-6.12-guests-v1 | impermanence-bd3a1e | tank/ct/niximpermanent | 6280 |
| upgrade/from-6.12-inherited-guests | impermanence-931fb2 | tank/ct/niximpermanent | 6158 |
| upgrade/from-6.18-guests | impermanence-798605 | tank/ct/niximpermanent | 7370 |
| upgrade/from-6.18-guests-v1 | impermanence-7b3ada | tank/ct/niximpermanent | 6802 |

Each expected full name is `tank/ct/niximpermanent.<suffix>`.
`RSpec::Expectations::ExpectationNotMetError` reports the saved clone versus
the base dataset. Containers remain reported running with the same init PID.
The current generation switch exits0; kernel release, boot ID and booted-system
stay unchanged while current-system becomes the exact846bb generation.

Sixth case `upgrade/from-6.18-nested-podman` fails earlier in setup:

```text
OsVm::TimeoutError: Timeout occurred while waiting for container "nestedpodman" to come online
```

It runs1237.2s before the exception. `ct start` succeeds at13:29:13–17Z,
then the online probe repeatedly reports `Temporary failure in name resolution`;
curl/wget are absent. The900s readiness deadline expires13:44:17Z. The guest
shell contains no switch-to-configuration command before the error. Source
`common.nix:1246` places this wait in pinned-predecessor workload creation,
before current generation activation. Implementer0's
[bounded local diagnosis](generic-sysctl-ci-nested-podman.md) records dhcpcd
`ps_managersandbox: seccomp: Permission denied` at13:29:18Z, failed ifup and
no guest IPv4/default route. The exact denial/filter/syscall origin is unknown;
no networking repair is selected.

## Generic-service execution evidence and limits

All five dataset cases have post-switch `runsv sysctl` and `svlogd` for
`/var/log/sysctl`, with the oneShot reported down. In the first case,
`machine-failure-diagnostics.log:1282` records the supervisor and log process;
line1974 reports down43s. The other cases report down37s,68s,99s,101s.
This proves the new service is present under supervision, not that procps
succeeded or that its application caused the dataset mismatch.

The switch output ends “runit will start new services”; newly introduced
services start asynchronously via runsv, so the absence of an explicit
`sv start sysctl` line does not exclude application. Uploaded console “Applying
55/60” lines belong to predecessor early boot. These uploads list the sysctl
log directory but do not include its current contents, the applied/done stamp,
custom-check outcome, attempt count or post-switch sysctl value readback.
Precise application timing, success/failure and final values are unresolved.
Negative log searches are not execution proof.

The same five dataset failures existed in the preserved
[b81c CI analysis](os-hardlockup-ci-failure-analysis.md), before this generic
service existed. This establishes historical occurrence, not exclusion of
current contribution. The old boot-argument-only nonexecution argument cannot
be reused to exclude this runtime service. Architect0's
[causal synthesis](design.md#current-product-ci-causal-boundary) confirms zero
source change between b81c and846bb in the upgrade common fixture, container
export, run configuration loader, runit wrapper and switcher. This narrows the
directly changed code but does not prove runtime exclusion. No demonstrated
feature-caused first error or
justified panic/sysctl repair has been identified; actual runtime YAML and
mounted ephemeral root are not captured, so their state and precise loader
root cause remain unresolved. Useful later evidence would combine pre/post
run-configuration bytes and actual mount source with timed service output,
completion and value readbacks. That diagnostic execution is not selected;
there is no basis to claim harmless reporting, data loss or baseline equivalence.

The nested-podman first error occurs on the predecessor before feature
activation; current sysctl/panic changes are excluded from that executed
failure path. This does not certify a general DNS/network root cause or justify
an unrelated suite repair. No new evaluation, VM or remote query was used in
these diagnosis lanes.

## AMD scale-aged v6 qualification failure

Second failed job `119793311395` is
`kernel/livepatch-qualification@amd-scale-aged-v6`. The watcher captured its
first artifacts at15:53:37–47Z; parent relayed the failure16:02:21Z. This is
an executed qualification health assertion after exercise, not a build/setup
or livepatch activation timeout. At15:41:35Z, `test-runner.log:107` rejects
dmesg matching the no-kernel-fault pattern. The matching event is:

```text
[14636.489093] Dying CPU not properly vacated!
[14636.489185] WARNING: CPU: 127 PID: 789 at kernel/sched/core.c:8333 sched_cpu_dying.cold+0xe/0xda
```

Console149–150 and failure-diagnostics635–636 record the warning.
It occurs during the first CPU127 offline exercise at15:24:42–51Z, before
the corrected livepatch insertion at15:26:09–15:38:46Z. The test then records
one successful activation in757.998s under its1800s ceiling, expected transition
and callback counts, and a second successful offline/online exercise at
15:38:56–15:39:11Z. The later dmesg assertion catches the earlier warning.
Successful commands do not make the warning benign or establish its cause.

The adjacent dump reports `CPU127 enqueued tasks (2 total)` but names only
PID789 `migration/127`. Architect0's exact local source interpretation is a
real hotplug invariant violation: the callback warns when runnable count is
not1 or pinned tasks remain. The stopper context is expected here and does
not identify the offending task. The dump supplies count2 but no second PID or
pinned-state proof. This is not a hard/soft-lockup detector report or a kernel
panic. No callback owner, corruption claim or kernel fix follows from it.
[Architect source synthesis](design.md#amd-livepatch-hotplug-warning-boundary)
records the exact callback condition and its continue/return0 behavior. The
local predecessor source versions have identical scheduler/CPU files; this is
source continuity, not runtime nonregression proof. Establishing a sysctl
chain would need excess-task/hotplug timing and actual boot/service/stress
values. Those data are missing and no additional diagnostic run is selected.

The guest boots current846bb OS
`/nix/store/36lyy591m13v8kd5jwa2vyv1hn2gd9vr-vpsadminos-system-vpsadminos-26.05.git.846bb46`
with frozen6.12.95.6 kernel; this is not the predecessor-OS boundary of the
Podman failure. Source `tests/suite/kernel/livepatch-6.12.95-common.nix:409,504`
imports the frozen boot kernel configuration into the current empty machine.
The producing kernel source is `a2384967b90f24d2470c9eb15f0e66d938df7e08`,
with original binary/toolchain identity retained by
`os/packages/linux/boot-6.12.95.nix`. The first warning precedes corrected v7
execution but occurs with the v6 predecessor loaded. Architect0 owns narrow
scheduler-source interpretation before selecting any repair.

The command line includes the qualification trace flags and lacks the panic
boot arguments. Postfailure process/service diagnostics show current
`runsv sysctl`, its logger and down15666s (lines1666,1688,3328). This establishes
current generic service reachability at boot; uploaded service output, stamps
and managed-value readbacks remain missing. Generic boot-state contribution is
not excluded. No OS switch occurs in this scenario. Stress intentionally sets
several sysctls after boot; neither that fact nor a negative log search proves
which earlier managed values applied.

Evidence is retained under
`generic-sysctl-ci-39767770407-600s-failure-119793311395/artifacts/os-test-logs-39767770407-1-livepatch-amd-scale-aged-v6/`.
Native `unexpected_failure` follows one example lasting15606.9s; total runner
elapsed15706.7s. Per-job log retrieval refused while the workflow is active;
artifact retrieval exited0. No rerun, source edit, kernel repair or new check is
selected. At this pre-exception checkpoint CI was unsuccessful and integration blocked.

## Later AMD scale-aged v5 failure

After the accepted-exception merge, the same watcher reported a distinct third
failed job: `119793311416`, AMD-scale-aged-v5. Its first native artifacts were
captured20:44:01–13Z under
`generic-sysctl-ci-39767770407-600s-detail-failure-119793311416/artifacts/os-test-logs-39767770407-1-livepatch-amd-scale-aged-v5/`.
The example failed at20:35:17Z after16629.89s, at the dmesg no-fault assertion.
The exact matching events in `test-runner.log:138,189` are RCU stalls:

```text
[14822.947301] rcu: INFO: rcu_preempt self-detected stall on CPU
[14823.741817] rcu: INFO: rcu_preempt detected expedited stalls on CPUs/tasks: { 114-.... } 21202 jiffies s: 84857 root: 0x80/.
```

This is not the v6 scheduler-warning signature. Initial relay called the
generic regex match a warning before extracting these exact lines; that relay
was promptly corrected. The artifacts downloaded successfully; per-job log
retrieval remains unavailable until overall completion. No causal relation,
repair or rerun is selected here. Root-cause/test-value investigation belongs
to the separately assigned session; this lane retains current CI observation.
The new failure was reported explicitly and was not silently included in the
earlier user waiver or described as green.

## Preserved evidence and continuing owner

First evidence root:
`generic-sysctl-ci-39767770407-600s-failure-119793311317/`.
Its `artifacts/os-test-logs-39767770407-1-native/` contains the native
`test.log` and all case logs/results. All six failed directory names are
recoverable from their `test-result.txt` and suite summary; no prior evidence
was overwritten. The watcher's artifact download exited0. Its per-job `gh run
view --log` exited1 with empty log; that retrieval gap is retained in
`job.exit`/`job.stderr` rather than treated as no failure.

Same native watcher `01a1634c-0553-7530-ba30-b19cfc2307d0` retained this run
through terminal completion on the600s cadence. Its final
`generic-sysctl-ci-39767770407-600s-detail.{log,exit,ended}` and terminal metadata
govern overall status. No second observer, workflow, retry or CI cancellation
was launched. Complete conclusions and first evidence are preserved; no active
observer remains, as recorded above.
