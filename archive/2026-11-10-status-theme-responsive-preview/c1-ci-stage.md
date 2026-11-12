# C1: bounded CI stage diagnosis

Owner: implementer1; read-only diagnosis on 2026-11-10, 14:12:46–14:14:35 UTC.
Session/environment identity and live retained Sol/xhigh/workspace_write verified.
No source, Git, service, runner or machine mutations; no checks, builds, retries,
cancellation or duplicate watcher. Terminal observation remains with runtime
operation `8a076f1f`.

## Current stage

One GitHub snapshot at approximately 14:13 UTC:

- Repository: `vpsfreecz/vpsf-status`, Integration Tests.
- Head: `6188366420342fdcf5b5f73c76dc0ccffede80b8`.
- [Run 42829260041](https://github.com/vpsfreecz/vpsf-status/actions/runs/42829260041),
  attempt 1: **queued**, no conclusion.
- Job `129874673120`, “Run ci-tagged integration tests”: **queued**, `steps: []`,
  no completion time.
- Run created, startedAt and updated timestamps all `2026-11-10T13:57:10Z`.
  The API's run startedAt does not establish job execution: the job remains queued
  with no steps. About 16 minutes had elapsed since creation at this snapshot.

Command: `gh run view 42829260041 --repo vpsfreecz/vpsf-status --json
attempt,headSha,status,conclusion,createdAt,startedAt,updatedAt,jobs,url`.
There is no current per-test/build stage to inspect while this job is queued.
Next observable milestone is self-hosted runner assignment and setup/checkout,
then selection of the `status-page` suite.

## Prior run: progress and diagnostic limit

Prior head: `9958b0375eb4d7c655cdc505a76e46ec95301cd4`.
Run `42816255766`, attempt 1, job `129830005698`: intentionally cancelled,
not a completed application test result. Job duration was 1h27m50s.
Evidence: [saved report](ci-9958b03/report.txt) and
[full Actions log](ci-9958b03/run-42816255766.log).

- 12:30:30–12:30:55 UTC: visible Nix builds of test-runner dependencies and the
  test-runner repository-source derivation.
- 12:30:59 UTC, log lines 164–172: selected `status-page`; reserved three machines,
  17.5 GiB memory and 14 CPUs; reported `[1/1] Running test 'status-page'`.
  Resource allocation succeeded; this was not waiting in the runner's resource queue.
- 12:35:59–13:55:59 UTC, lines 173–189: five-minute aggregate heartbeats,
  “Status: passing; 0 succeeded ... 1 running, 0 remaining”. These show a live
  test-runner, not successful assertions or advancing build/test phases.
- 13:57:43 UTC: cancellation. Evaluation then reports zero completed tests.
  Cleanup lists an orphan `nix-build` process; this supports that a build child
  existed at cancellation, but does not identify its derivation, progress or cause.

The saved Actions log contains no per-test builder/VM/assertion output after
selection. The saved report says full-log upload was skipped; a one-time
`gh api repos/vpsfreecz/vpsf-status/actions/runs/42816255766/artifacts` check
confirmed `total_count: 0`. No per-test artifacts are available through that run.

## Interpretation and recommendation

The workflow uses `self-hosted`, then `./test-runner.sh test -f --jobs auto -t ci
--state-dir /tmp/os-test-runner | tee test.log`. Its Run tests timeout is 320
minutes; job timeout is 360. These are limits, not expected durations.
`tests/suite/status-page.nix` is a three-machine integration suite with cluster
setup, JSON/metrics checks, reachability recovery, outages and advisories. A
“running” aggregate status does not distinguish Nix image/package preparation,
machine startup, setup waits or an individual assertion.

Current result: **runner queue wait**. Runner availability and queue cause were
not established. No ETA can be inferred. Keep the existing watcher as terminal
owner; do not rerun or cancel because of these aggregate heartbeats. If the
replacement again stays inside Run tests without a concrete phase, the useful
next diagnostic is the exact runner's `/tmp/os-test-runner` per-test build and
machine logs, including the active derivation or first setup/assertion wait.
This requires a separately scoped access/diagnosis decision; broader CI changes
are outside C1. The cancelled run supplies neither an application pass nor an
application failure.

This single bounded inspection finished within the five-minute allocation.

## C3: current final-head diagnostic access, 2026-11-10 15:07–15:09 UTC

Owner architect0; exact session/environment and retained Astra/xhigh/workspace_write
verified. Read-only bounded investigation; terminal observation remains with
runtime watcher `923dcf5b-0cad-478f-87df-6e7bd5633014`. No rerun, cancellation,
runner modification, source edit, build/test launch or machine claim.

Current exact head is `2d448fd21e8ea5ec3b2a1322bb170d35617470ce`,
[run 42837407366](https://github.com/vpsfreecz/vpsf-status/actions/runs/42837407366),
attempt 1, job `129903183487`. Actions job metadata establishes:

- Runner assigned: `gh-runner1.int.vpsadminos.org`, runner ID `10650`, group
  `vpsadminos runners` (ID `3`). Job began at 14:46:00 UTC.
- Setup, runner setup, checkout and gcroot reset completed successfully.
  `Run tests` began at 14:46:20 UTC and remains `in_progress` at inspection,
  approximately 22 minutes later. This is no longer a runner queue wait.
- Result evaluation, log summary and artifact upload remain pending. No test
  conclusion, derivation, VM stage or assertion is exposed by job metadata.
  Run `updated_at=14:46:00Z` is not a build-progress or stall indicator.

Accessible diagnostics and exact limits:

1. `gh run view ... --json ...` and
   `gh api repos/vpsfreecz/vpsf-status/actions/jobs/129903183487` give the step
   and runner facts above, but no per-test stage.
2. `gh run view 42837407366 --repo vpsfreecz/vpsf-status --job 129903183487 --log`
   refuses while the job is in progress. The direct job `/logs` endpoint returned
   HTTP 404 `BlobNotFound` at 15:08:07 UTC. No current log content was available.
3. Run `/artifacts` reports zero artifacts. Check-suite `116012518957` contains
   the running job with null output title, summary and text.
4. One noninteractive SSH attempt to the API-identified runner, using the existing
   configured user `aither`, strict existing-host-key verification and an 8-second
   connection limit, failed with `Permission denied (publickey,password,keyboard-interactive)`.
   No remote command ran; no other account, credential or access path was tried.

The final-head workflow still executes `./test-runner.sh ... --state-dir
/tmp/os-test-runner | tee test.log`; `test-runner.sh` delegates to
`nix run .#test-runner`. Build, image preparation and VM/assertion execution are
therefore indistinguishable through the currently accessible aggregate step.
Only advancement through setup into `Run tests` is proven. There is no evidence
here establishing whether the current long step is advancing, stuck, or waiting
on a particular dependency; previous-run heartbeat evidence cannot answer it.

Shortest useful next read-only diagnostic: an operator with existing access to
this exact runner can supply the active job's `test.log`, latest per-test
build/machine log tails and timestamps under `/tmp/os-test-runner`, and the current
child process/derivation for job `129903183487`, confirming that they belong to
this head/attempt. No restart or rerun is needed to collect them. Otherwise the
existing watcher continues until GitHub exposes completed logs. C3 stops here
within its five-minute bound; available interfaces cannot resolve the inner stage.

## C4: fresh access check and pinned output ownership, 2026-11-10 16:05–16:07 UTC

Owner architect0; identity/retained settings verified, capacity accepted. One
fresh Actions snapshot, bounded canonical-source reads and one documented SSH
access attempt; no duplicate watcher or execution mutation. Conditional final-CI
integration approval remains unsatisfied by an unfinished run.

Fresh job `129903183487` remains on runner `gh-runner1.int.vpsadminos.org`, exact
head `2d448fd21e8ea5ec3b2a1322bb170d35617470ce`, attempt 1. `Run tests` is still
active from 14:46:20 UTC, about 79 minutes at this snapshot. Later steps remain
pending. Direct `/logs` returned HTTP 404 `BlobNotFound` at 16:05:35 UTC; artifacts
remain zero and check output title/summary/text remain null. No externally visible
phase advancement since C3 is established; this is not proof that work has stalled.

New source evidence narrows the missing diagnostic:

- Final-head `flake.lock` pins vpsAdminOS
  `837baf04054c6ee0e71d288b8870ac42a6990c38`. At this exact revision,
  `test-runner/lib/test-runner/executor.rb:536–570` forks the test evaluator and
  redirects its stdout/stderr to the per-test `test-runner.log` before construction
  and execution. The evaluator constructor calls `TestConfig.build`, so this log
  also covers preparation before VM/test execution, not only assertions.
- `executor.rb:576–600` enables its periodic “last output” diagnostic only in
  verbose mode. The status workflow's invocation omits that mode. Aggregate
  progress can therefore continue while detailed work is recorded elsewhere;
  missing detailed console lines alone cannot identify which stage is responsible.
- `executor.rb:709–727` derives the status-page log path as
  `/tmp/os-test-runner/os-test-status-page-040d34e0/test-runner.log`. This path is
  calculated from pinned source and test name; its current existence/content has
  **not** been inspected remotely.
- Canonical `vpsadminos-org-configuration` local `origin/master`
  `ca96c95a1fee04793468785d8323a759615b2b4e` (2026-10-24) identifies the runner,
  its `github-runner` service user, and `environments/base.nix` enables SSH with
  root authorized admin/builder keys. This is repository configuration evidence,
  not proof of the runner's deployed configuration or of available credentials.
  No alternate read-only log service was found in these targeted definitions.

The previously denied `aither` SSH attempt was not repeated. One attempt through
the documented root interface used existing credentials, BatchMode, strict host
verification and an 8-second connect limit. It also failed authentication with
`Permission denied (publickey,password,keyboard-interactive)` at approximately
16:06:37 UTC. No remote command ran. No credential/key content was inspected or
changed; the service account was not treated as an SSH access account.

Shortest actionable next read is now precise: an operator already authorized on
`gh-runner1.int.vpsadminos.org` should confirm active job/head, then supply `stat`
and the latest approximately 80 lines of the exact per-test log above, plus its
current child process/derivation and relevant machine-log tail if the evaluator
has started VMs. This will distinguish Nix preparation from boot/setup/assertion
waits without rerunning anything. If no such access is supplied, the existing
watcher can only wait for completion and downloadable logs. Current-stage root
cause, advancement and ETA remain unproven. C4 ends within its five-minute bound;
repeating unchanged API/denied-access probes is not a useful next investigation.

## C5: baseline, faithful local command and observed preparation

Architect0 investigation began 16:18 UTC on 2026-11-10; source remained clean at
`2d448fd21e8ea5ec3b2a1322bb170d35617470ce`. Lead owns the local run and cancellation;
architect performed only source, own-log and owned-process reads. No app changes.

### Meaningful successful baseline

[Run 40127557047](https://github.com/vpsfreecz/vpsf-status/actions/runs/40127557047),
attempt 1, head `018b700f06cf216a125a70ac9bfedddaabf07b92`, ran on
`gh-runner3.int.vpsadminos.org`, not current CI's runner1. On 2026-10-24:
Run tests took 315 seconds (19:56:50–20:02:05 UTC), status-page itself 308.49s,
and all seven examples succeeded. First example completed at 20:00:47 UTC,
about 231s after test selection.
The baseline raw log was read into `/tmp/vpsf-status-c5-baseline-40127557047.log`.

Baseline-to-final diff leaves workflow, runner invocation, test suite/extensions,
flake wiring, pinned vpsAdmin and vpsAdminOS source unchanged. Relevant input
differences are inherited default-branch Go dependencies/vendor hash and
`nixpkgs_2`: `ee48b147c18c7de1e6ec97dc74792be42724bed1` →
`ac588ef1c914865dad517b337ea0eb9694a4021c`. These predate this UI branch;
`e560b43..2d448fd` changes none of those test/build-input files. The newer package
set changes dependent VM derivations even with identical suite/source; warm-cache
baseline timing is not a guarantee for the new closure or another runner.

Current exact inputs: vpsAdmin `3f9b68adb97b7f43df929a85fc172d9d11e15211`;
vpsAdminOS/test-runner `837baf04054c6ee0e71d288b8870ac42a6990c38`; root nixpkgs
follows `vpsadminos/nixpkgs`, resolving the `ac588ef...` node. Full input graph is
the final commit's `flake.lock`, SHA256
`58ebaf0b13ffe439d7d05289ff1a22bde3f91d0d46cb188aea25243c7927d005`.

Own cancelled run `42816255766` selected status-page at 12:30:59, emitted no
completed-example events for about 87 minutes, and cancellation cleanup reported
a surviving `nix-build` child (saved log lines 172–190, 315–319). This is a concrete
build/preparation clue, not proof of the current CI derivation or its cause.

### Local command contract, delivered before launch

CWD: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-10-status-theme-responsive-preview/vpsf-status`.

```sh
./test-runner.sh test -f --jobs auto -t ci --verbose \
  --state-dir /tmp/os-test-2026-11-10-status-theme-responsive-preview-c5
```

This preserves the full CI selection and default command timeouts, adding only
the verified command-local verbose option and an isolated state directory. Capture
both output streams with `pipefail` into the owning session log. Do not reproduce
CI's broad gcroot deletion or shared `/tmp/os-test-runner` removal. No alternate
test config or `TEST_RUNNER_REPO_ROOT` override; use the repository's pinned
`nix run .#test-runner` wrapper, not ambient Ruby. No second test invocation.

One selected test, three VMs, 17.5 GiB RAM, 17.5 GiB shared memory, 14 vCPUs.
Lead verified KVM read/write, approximately 63 GiB available memory and 93 GiB
free disk. `/dev/shm` read showed about 40 GiB free before launch; default resource
reserve is 8 GiB. Keep the test's configured socket/user networking; no devcluster
or bridge override. Fixed socket mcast port is 22131; investigate conflict only
if owned-run evidence identifies one. No such conflict was observed here.

Read `/tmp/os-test-2026-11-10-status-theme-responsive-preview-c5/os-test-status-page-040d34e0/test-runner.log`
as soon as it exists; verbose last-output heartbeats alone still wait five minutes.
Stop/escalate immediately on an unexpected local kernel compilation. Diagnose any
failure or sustained log/CPU/I/O stall before another run; do not retry blindly.
At 15 minutes without the first example, classify the exact build/setup wait from
this log and processes before extending observation. This is a diagnostic checkpoint,
not permission to shorten a legitimate configured assertion timeout.

### Observed local advancement and kernel-cache risk

Lead launched once (exec session 92567, runner PID 2197015). At 16:20:24 the exact
expected resource reservation succeeded. At 16:21:17 evaluator PID 2206216 was
waiting on child `nix-build` PID 2206219, mode `testJson`, output `config.json`,
before evaluator VM execution. Runtime runner:
`/nix/store/9lqp326mnrj1f3s6pjyjf08fcdxh6svm-test-runner`; captured source:
`/nix/store/6i0z5czb2hsrirqg1z3dz5c5q3hwhz0a-source`.
In a five-second read-only sample, child CPU advanced 74.99→79.11 seconds,
RSS 1.87→2.12 million kB, and the log grew from zero to 2978 bytes while building
the vpsAdmin source derivation. Local preparation was advancing, not idle.

The following plan then reported 759 derivations to build and 483 paths to fetch
(830.6 MiB download, 2.7 GiB unpacked), including many generated units/configs,
Ruby dependencies, vpsAdmin packages, disk images and complete VM systems.
These counts do not mean 759 expensive compilations. NixOS Linux 6.18.62 and
modules were fetched from cache.nixos.org. Separately, the plan includes two
vpsAdminOS Linux 6.12.95 derivations, requiring immediate kernel-start vigilance:

| Derivation | Output / dev output |
| --- | --- |
| `/nix/store/945vand1sz7ikdrafvqbc9h1xph6laks-linux-6.12.95.drv` | `/nix/store/p33nnz0i06wlzrwjz841vywmis03iyn7-linux-6.12.95` / `/nix/store/5a3v7w8w1aw79azs2r3f1xizv1dx5xn9-linux-6.12.95-dev` |
| `/nix/store/7gybyyg75k8w7a9jnhwmgaig2qlzkvr4-linux-6.12.95.drv` | `/nix/store/kwb292shzp8hhjqhfwvdn93fi82cyfy7-linux-6.12.95` / `/nix/store/fdm6xb93d9pq3x03s27pgq3gvlpp5198-linux-6.12.95-dev` |

Both use source `/nix/store/4jcdch0myxf11872ncmp4cgh91mg546r-a2384967b90f24d2470c9eb15f0e66d938df7e08.tar.gz`.
Build-plan inclusion proves no accepted substitute at planning time, not whether
cache publication is missing, the configured cache is unavailable, or dependencies
changed the store identity. Those alternatives require exact output cache queries
and derivation-input comparison; no kernel exception has been established.
Lead additionally observed build-user-ID contention at 16:23; this can delay
individual derivations but does not yet account for the remote 90-minute run.

Pinned runner exposes no native cancel subcommand or custom signal trap. Ordinary
SIGINT is the Ruby interruption path; interrupting only the root risks leaving
forked evaluator/build processes. Observed runner/evaluator/build shared PGID/SID
2197013. Lead must revalidate exact owned group membership before terminal/group
interrupt, join the existing exec and reconcile survivors/Nix command effects.
VM cleanup is in `TestEvaluator#do_run` ensure, but constructor `TestConfig.build`
occurs before that block. No process was signalled by architect0.

C5 conclusion: no branch/test defect identified. There is now direct local proof
of substantial Nix preparation and cache misses; the inherited nixpkgs change is
a concrete source of changed VM identities. This supports investigating build/cache
delay, without claiming the remote cause or exempting final CI. Lead owns ongoing
local observation. A further bounded package should query these two exact kernel
outputs in configured caches and compare dependency/config identities; it must not
start another build or weaken checks. C5 source/evidence work ends here.

## C6: exact kernel cache miss and inherited input drift

Read-only investigation began 16:25:23 UTC on 2026-11-10. Session/environment
and architect0's retained Astra/xhigh/workspace_write binding were verified.
Final source remains `2d448fd21e8ea5ec3b2a1322bb170d35617470ce`.
Lead reports local run 92567 stopped at 16:25 when linux-config `31jmrq...`
started: group SIGINT, joined exit 130, no survivors, no realized config.json
and no VMs started. Architect did not signal or poll the run.

The four exact kernel out/dev paths listed under C5 were each queried once via
narinfo at the configured caches. Both cache.vpsadminos.org and cache.nixos.org
returned HTTP 404 for all four. cache.numtide.com returned HTTP 403 for all four,
which establishes inaccessible output there, not absence. Relevant cache signing
keys are configured. No build, store copy or cache retry was performed.

The two derivations are intentional variants, not duplicate identical builds:
`945vand...` is the plain kernel used for builtin configuration; `7gybyyg...`
adds builtin ZFS through `j6jj1i7k9bss399xvm2x720116lkk784-zfs-builtin-2.3-vpsadminos-6.12.95.drv`.
Their configs are respectively `31jmrqlk359khswcnfhjkkgxg48sk904` and
`44v4wg6jnvpzm25n5f7wswnx4yrzb9af` linux-config derivations. Both use the same
kernel source and current gcc-wrapper-15.3.0 toolchain.
At OS `837baf04054c6ee0e71d288b8870ac42a6990c38`,
`os/modules/config/kernel.nix` selects builtin ZFS by default and separately
defines kernelForBuiltinsConfig; `os/packages/linux/packages.nix` constructs
both with injected `pkgs.callPackage`. Changing pkgs changes kernel identities.

The OS revision's own `flake.lock` resolves its root nixpkgs to
`ee48b147c18c7de1e6ec97dc74792be42724bed1` (nixos-26.05), matching the successful
C5 baseline. Final vpsf-status instead resolves that OS input to
`ac588ef1c914865dad517b337ea0eb9694a4021c`. Its dependency updater's
`confctl inputs update --forward-only nixpkgs` advances the root follow into
the OS package set. This inherited input drift changes the kernel toolchain
despite unchanged OS source. `flake.nix` also passes root nixpkgs.outPath into
both mkTests and mkTestsMeta, so changing follows alone would be insufficient.

The pinned OS `.github/workflows/kernels.yml` builds its own locked composition,
on a daily schedule and selected kernel-source changes, and publishes closures
to the OS cache. It does not declare workflow_dispatch. One Actions query for
the exact OS head returned only an input-update run, not a kernel run; this is
not exhaustive historical publication evidence. There is no evidence that the
current downstream-overridden derivations are expected upstream outputs merely
awaiting publication. A local kernel-build exception is therefore unproven.

Minimal correction candidate: retain modern app nixpkgs/Go 1.26 independently,
restore the OS-pinned package composition for integration, and align both
tests and testsMeta pkgsPath. Keep OS/vpsAdmin source and assertions unchanged.
Do not globally roll back the app's package set. Before a full rerun, evaluate
the complete test config derivation and both kernel out/dev identities without
building, then confirm their cache availability. Original-composition cache
availability and compatibility with the modern app still require that check.
Alternatively, deliberately retaining the mixed graph needs an authorized
upstream publication of these exact variants/composition; a normal upstream
workflow rerun alone does not establish this.

C6 establishes the local kernel cache/input mismatch. It does not establish
the exact remote 90-minute child derivation or elapsed-time cause. No UI/source
change or full rerun is justified by this evidence alone. Lead owns package
release and conditional final-CI acceptance; architect investigation ends here.

## K1: upstream trigger brief and exact published-kernel identity

2026-11-10 16:40–16:46 UTC, read-only. K1 design is recorded in design.md;
implementer3 owns the kernel workflow correction. User withdrew the C7 status
input split: preserve that original graph until a separately accepted correction.

Current OS `650170d699e3033c5279b911a2ef0a355439613c` already passed all seven
kernel jobs in [run 42803793083](https://github.com/vpsfreecz/vpsadminos/actions/runs/42803793083),
scheduled 10:59:59, completed 11:05:49 UTC. No active run appeared in the six-run
listing. Kernel 6.12.95 job `129787930479` published toplevel
`/nix/store/ninz99i83hj9na77pj3h7rf5hzhcsjiq-vpsadminos-system-vpsadminos-26.05.git.650170d`.
Read-only narinfo of that toplevel and its two kernel dev references established:

| Variant | Published out | Published dev |
| --- | --- | --- |
| Builtin ZFS (boot kernel) | `/nix/store/gm91ln07cdh6ainv8r27cl3vp66045m6-linux-6.12.95` | `/nix/store/sjnpva6b6x9yl72f1rfscwi7ss22c4wv-linux-6.12.95-dev` |
| Plain configuration kernel | `/nix/store/dpj159lw4p0bhpmdr07synryf1layjna-linux-6.12.95` | `/nix/store/sv79x5grw9hzmc2fa31rpd2yyz47005k-linux-6.12.95-dev` |

Both dev narinfos refer to their corresponding out, corroborating closure
coverage. Neither variant matches status's original p33nnz/5a3v7 or kwb292/fdm6
paths from C5. Current OS changes 6.12.95 features.livepatch, builtin-ZFS source
`6f5f54c3...` → `481845fc...`, and kernel config/builder code versus OS837baf.
Same displayed kernel version and nixpkgs revision are insufficient for identity.
Thus waiting for the already successful current workflow cannot establish that
the old status kernel requirements will appear. Exact old-output publication or
a separately approved dependency correction is still needed before test rerun.
No new run, source edit, build, VM or cache mutation was performed. Raw job log:
`/tmp/2026-11-10-status-theme-responsive-preview-k1-kernel-129787930479.log`.

## C9: active local runtime startup and first-example wait

2026-11-10 17:34:21–17:38 UTC, architect0 read-only diagnosis; identity/environment
and retained Astra/xhigh/workspace_write verified. Exact status source
`b589972c57a22fb806a643a1de9a683beca3a363`, owner exec 58463, PGID 2720984.
Watcher 381c85a0 remains sole terminal observer. Evidence below is from
`/tmp/os-test-2026-11-10-status-theme-responsive-preview-b589972/os-test-status-page-040d34e0/`
test-runner.log and services/node/status shell, console and lifecycle logs.
Guest log timestamps are UTC+0100; the following timeline uses UTC.

Before-suite completed, not stuck: services QEMU launched 17:26:19; API probes
from 17:26:47 initially failed to connect/returned 502, then the request at
17:28:58 completed successfully 17:29:10. Node launched 17:29:11 and shell was
available 17:32:31. Nodectld socket/ping became ready 17:32:45; one refresh failed
with connection refused, then succeeded 17:32:49. API node readiness and fresh
node/pool timestamps were true by 17:33:17. Status VM launched 17:33:26, PID
2924829. The first of seven examples began 17:34:19, after about 8m21 startup.

Current condition is the first example's operational JSON predicate, timeout
240 seconds (nominal deadline 17:38:19). The JSON timeline is significant:

- 17:34:19: API/WebUI/console down during initial status checks.
- 17:34:31: API operational, node API/pool flags true; console not ready yet.
- 17:34:32–35: API and console operational, all node values match expectations;
  WebUI down is the sole observed false predicate.
- From 17:34:36 through the inspected 17:36:29 sample: API also down, node API and
  pool flags false; console operational and node ping responding. WebUI remains down.

Pool state/scan “unknown” before API loss is explicitly expected by this suite;
it is not evidence of a storage defect. Failed API refresh intentionally clears
node API/pool flags, so those later flags do not independently prove nodectld
failure. Logs keep advancing via status JSON polls (status-shell.log updated
17:37:02); no terminal result had been observed at this checkpoint. The watchdog
owns any eventual example/whole-suite result, not this investigation.

No safe independent guest query channel was found: generated config gives every
VM exactly one worker shell, no named diagnostic shell; QEMU arguments have no
SSH port forward. The inspected CLI exposes script/test/debug, not independent
read-only attachment to a running test. Console and shell sockets belong to the
runner. No attachment, socket read, live disk mount, packet injection or signal
was attempted. Shared-dir contained no exported diagnostic files.

At 17:37:53, a read-only host process check found exactly three QEMU users of
multicast 230.0.0.1:22131: PIDs 2862542, 2881571 and 2924829, all own PGID 2720984.
No foreign-PGID QEMU on that endpoint was observed. This excludes that concrete
collision candidate at sampling time, not every possible network fault; no other
session records/files were accessed.

`http.go` and `api.go` are unchanged from feature base e560b43 through b589972.
WebUI uses HEAD and records HTTP/transport errors in the service journal; API
records its request/status error there. Neither the HTTP code/body nor those
journals are present in the current exported logs. Thus backend/container failure,
probe timeout and old-vpsAdmin/new-OS compatibility remain distinguishable
hypotheses; no new status UI defect or dependency fix is established.

Shortest next owned diagnostic contract, if failure persists: collect through the
runner's native machine objects before teardown, without relaxing assertions:
status `journalctl -u vpsf-status --no-pager -n 100` and bounded `curl -I` to
WebUI/API/console; services `systemctl --failed`, `journalctl -u vpsadmin-api
-u container@webui --no-pager -n 100`, and `nixos-container run webui --
systemctl --failed` plus its nginx/PHP journal. Preserve response status and a
bounded non-secret body only where necessary. Implementer0 may own a separately
released minimal failure-log fixture change; no retry, input refresh, service
restart or source correction follows from this diagnosis alone. C9 complete;
the existing watcher continues the original run.

## C10: services-only native diagnostic contract

Source-only check 2026-11-10 17:45–17:50 UTC. Existing `test-json-runner` loads
realized JSON directly and delegates to Executor, avoiding TestConfig Nix builds.
`debug` is interactive and still calls TestConfig.build, so it is not the shortest
path. Lead authorized preparing the session-only derivative, not executing it.

Prepared `c10-services-only.json` and readable `c10-services-only.rb` in this
tracking directory. The services machine definition is parsed-JSON identical to
reviewed b589 config `/nix/store/pdahm8qr3jh0x9p1nknnspv2v6pv2wpf-os-test-status-page.json`:
same image, kernel, system, networks, 8192 MiB RAM, 8192 MiB shm and eight vCPUs.
Other machine entries are omitted. One native script starts services, waits for
its shell, records bounded HTTP response codes/timings and unit/container journals,
waits at most 180s for API HTTP readiness, then repeats capture. Queries do not
change guest services. No full-suite hooks, node/status VM or 240s assertion runs.
Ruby syntax check passed; the diagnostic itself has not been executed.

Exact proposed argv, cwd this tracking directory, with a new state directory:

```sh
env TEST_PATH=status-page-services-diagnostic TEST_TIMEOUT=180 TEST_JOBS=1 \
  TEST_RECREATE_DISKS=1 TEST_DESTRUCTIVE=1 \
  /nix/store/lq19bmld805mhs566r4ymgb1hr244ayi-test-runner/bin/test-json-runner \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-11-10-status-theme-responsive-preview/c10-services-only.json \
  /tmp/status-c10-20261110-1758
```

The realized wrapper uses Ruby 3.4.11 and `/nix/store/dkxi673xxfxwqi1r9m5yrzcdlcpq7fi9-test-runner`
plus `/nix/store/8ilmr2s60xlbwzq42y43k4jhzswv7w85-osvm`. Production runner/OSVM
files match the inspected OS650 sources; only one unrelated spec differs.
No package resolution, evaluation or build is in this argv. The wrapper's
test-json runner currently omits resources when constructing Test: resource
admission can report zero even though the guest requires 8 GiB RAM/shm and eight
vCPUs. Lead must check that real capacity before launch; do not expand this task
into a runner fix. Ensure no concurrent same multicast 230.0.0.1:22131 test.

SHA256 receipts:

- Original immutable JSON: `e1574a0955e0eedb85c207489ccf3d1892bd6b0050cad35acc557c9b5a8c9db1`.
- Derived JSON: `88b9a16ad790e798c92bde4d2384e2352284aa480e6b3912128ab282ff4f78c4`.
- Readable script: `038d8cd21698c1713028cc446a398e7225d0d2af4e24c93b27a3053f57c2cd8e`.
- Native wrapper: `38a7d21d800116206698d376a9204ba793aab24284a363f9ee0f875f910691a8`.

Executor/TestEvaluator do_run owns normal shutdown and ensure-path termination,
new managed-disk destruction, descriptor finalization and socket cleanup. A fresh
watcher must join the source and reconcile its own QEMU/virtiofs children; no old
socket or disk is reused. This contract concerns diagnostic guest cleanup only,
not session lifecycle. Expected work is one services boot and bounded captures;
report a boot/cleanup failure instead of extending or relaunching. Capture uses
execute to retain failed HTTP/unit commands, so exit 0 means collection completed,
not healthy backend or passing integration. Services-only HTTP diagnosis cannot
establish node/data-path or full-fixture equivalence. U8 product capture stays
with implementer0; C10 adds no application code or testing subsystem.

### C10 launch failure: state path exceeded UNIX socket length

The original command used state root
`/tmp/os-test-2026-11-10-status-theme-responsive-preview-c10-services-1748`.
Lead's actual run (exec 59507) exited 1 after 21s at 17:55:53 UTC, before guest
boot. Read-only follow-up at 17:57:22 found the exact cause in
`services-console.log`: QEMU rejected its virtiofs socket path as too long,
“Path must be less than 108 bytes”. `services-fs-vmSharedDir.log` independently
reports “path must be shorter than SUN_LEN”. The socket path was 116 bytes;
the shell socket was 107 bytes. The later shell-wait IOError was secondary to
QEMU's immediate exit, not a test/API failure.

This was architect0's prototype state-path error. The argv above is corrected
to a fresh shorter root `/tmp/status-c10-20261110-1758`, which did not exist when
checked. With the same native suffixes its virtiofs socket is 72 bytes and shell
socket 63 bytes. The JSON/script/wrapper and their hashes stay unchanged. No rerun
was performed by architect; lead owns any subsequent authorized launch.

The actual copied JSON still hashes to 88b9a16a... and its services definition is
identical to the original b589 JSON. Its QEMU, kernel, initrd, system, disk-image
and virtiofsd paths all exist. QEMU/version/kernel/system match the original
successful boot receipt. There is no evidence of GC loss or a need to build,
copy cache objects, add roots, alter networking or change product code.
Parent owns survivor reconciliation. No HTTP or guest journal evidence was
captured by this failed pre-boot attempt.

### C11: bounded services-only request timing, prepared for lead-owned launch

C10's corrected short-state run completed collection (parent exec 70175, exit 0,
273.54s). API readiness expired, then API root GET returned 200 in 5.710s,
WebUI HEAD 200 in 4.384s and console HEAD 200 in 0.178s. No failed units were
reported; Puma started late and subsequently listened. These observations do not
prove a crash, sustained latency or a product timeout defect. The fixture's
unchanged two-second HTTP timeout remains unchanged.

Prepared session-only `c11-services-timing.rb` and `c11-services-timing.json`.
The only VM is the exact services definition from immutable b589 JSON above;
no image, kernel, network, CPU or memory settings change. Ruby syntax, JSON parse,
embedded script equality and equality of the services definition all pass.
Original JSON SHA256 remains `e1574a0955e0eedb85c207489ccf3d1892bd6b0050cad35acc557c9b5a8c9db1`.

The script boots services, waits up to 300s for the native API unit to become
active, records bounded journals, performs one API warmup and three timing rounds.
Each round probes API GET `/v7.0/nodes/public_status` and WebUI HEAD with two- and
ten-second caps, plus console HEAD with a two-second cap. Fresh curl processes
use HTTP/1.1, connection close and the default Go user agent; API requests accept
gzip. The public synthetic response is capped at 64 KiB; the reported envelope
contains status, a bounded message and node count. Headers/auth/query match the
unset defaults of pinned Go client v0.2.0 (`5f7c8a8e00a37dbcdddee222f059d32ec9fc91cc`).
HTTP 200 alone is not API success. Curl timings cover server latency, not exact
Go transport or cross-VM equivalence; no node health/full-suite pass is claimed.

Final SHA256 receipts:

- Ruby: `aea25da52ff8ffd5537a406ed96d1e17af8cf20d2a3c80ba58d1d64904a7f24b`.
- JSON (corrected native descriptor): `cacd5c1fb90eaa4e36e954a65dffd118e414bf7dee8caac5bfcd09c15ab457f2`.

Launch contract: cwd this tracking directory, using the lead-restored native
runner GC root with these exact arguments:

```sh
env TEST_PATH=status-page-services-timing TEST_TIMEOUT=180 TEST_JOBS=1 \
  TEST_RECREATE_DISKS=1 TEST_DESTRUCTIVE=1 \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-11-10-status-theme-responsive-preview/c11-test-runner-runtime/bin/test-json-runner \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-11-10-status-theme-responsive-preview/c11-services-timing.json \
  /tmp/status-c11-1810
```

The new short state did not exist at final preparation; the longest relevant
native socket suffix gives 63 bytes. Actual resources remain 8 GiB guest RAM,
8 GiB shm and eight vCPUs despite the direct runner's zero admission report.
Expect roughly five minutes for boot/readiness and 16 bounded HTTP requests;
request caps total 88s, with two five-second gaps. TEST_TIMEOUT is a native
command timeout, not a global deadline. Retain the native Executor teardown
contract above and have the fresh watcher join/reconcile its own guest children.

Resolved launch blocker: the previously recorded C10 wrapper
`/nix/store/lq19bmld805mhs566r4ymgb1hr244ayi-test-runner/bin/test-json-runner`
and recorded runner library directory were absent at final C11 preparation.
Do not execute that stale literal or silently substitute another runner.
Lead restored and rooted the current OS650 runner at
`/nix/store/6gr674mbb54m1ld3ibqr6iir0767xmgs-test-runner` through
`c11-test-runner-runtime`, and rooted the original config closure separately.

The parent's prelaunch gate also caught architect0's artifact schema error:
the final synchronization had replaced `testScripts.default` with a string.
JSON parsing and script equality did not validate the native descriptor contract.
Corrected it to the working C10 descriptor, retaining description, attempts,
expectFailure, tags and labels, and inserting the unchanged Ruby as `script`.
Actual native `Test.new`, `TestConfig.load` and `validate!(test.test_scripts.values)`
now pass using the restored wrapper's exact Ruby and declared GEM/RUBYLIB paths.
Descriptor preservation, immutable services equality and unchanged Ruby hash also
pass. No Executor, VM or build was invoked for this check. Runtime findings and
any product fix remain pending the authorized probe.

## C12: final CI queued before runner assignment, 2026-11-10 18:54–18:55 UTC

Bounded read-only diagnosis by architect0; session/thread identity and retained
Astra/xhigh/workspace_write verified. Lead reports the final faithful local suite
passed all seven examples with clean teardown. Existing GitHub watcher PGID
3466796 remains the terminal observer; it was neither duplicated nor changed.

At approximately 18:54 UTC, [Integration Tests run 42875825900](https://github.com/vpsfreecz/vpsf-status/actions/runs/42875825900),
attempt 1, exact head `9fb102e285a2847427ffc1d25919183298630f3b`, was **queued**.
Creation/update/run-start timestamps all remained `2026-11-10T18:30:10Z`.
Job `130038744764` was queued with `steps: []`, `runner_id: 0`, empty runner/group
names and labels `["self-hosted"]`. Its started timestamp therefore does not
establish execution. About 24 minutes had elapsed without assignment; no build,
VM startup or application test was running in this job.

Exact-head `.github/workflows/integration-tests.yml` requests only
`runs-on: self-hosted`, with no custom labels, explicit runner group or concurrency
gate. There is no narrow workflow label restriction to explain the wait.
Repository runners API returned HTTP 200 and `total_count: 0`; that does not prove
the absence of organization runners. Earlier C3 evidence assigned this repository
to organization group `vpsadminos runners` (ID 3), runner ID 10650.

The second bounded snapshot queried organization runners and runner groups.
Both returned HTTP 403: organization-admin or runners/runner-groups permission is
required; current credentials lack the necessary access. No credential refresh,
alternate credentials or previously denied SSH connection was attempted. The
previously documented remote runner is not this workspace's local service, so a
local service probe would not establish its current availability.

**Result: unassigned runner queue; busy/offline/group-access cause unknown.**
The shortest useful next step is an already-authorized organization operator's
read-only check of runner group 3: eligibility for `vpsfreecz/vpsf-status`, eligible
runner online/offline and busy flags, and whether an idle listener receives this
job. If all eligible runners are busy, wait for capacity without rerunning. If
offline, the runner operator should inspect its listener service status/journal
before proposing recovery; any service or registration change goes through lead
authorization. If online and idle, verify repository/group access and runner
dispatch diagnostics. No specific restart or label change is justified by the
accessible evidence. The local suite pass does not waive the requested final CI
gate. No source edit, runner mutation, cancellation, dispatch, build or test ran.
