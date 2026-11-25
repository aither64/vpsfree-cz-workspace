# Kernel hang investigation brief

## Current CI duration investigation brief

The user reports that run `39767770407` has remained active for about nine hours
and asks whether workflow duration has regressed. Establish its critical path
and compare like-for-like execution before calling this a regression or hang.
The current source is `846bb469505789ba0b2a405fa5905ba6d8253006`. This assignment
is historical metadata/log reading and local source analysis only: no new test,
workflow, retry, cancellation, build, VM, evaluation, source/Git change, host
write or additional current-run observer. Previously accepted CI failures and
their root-cause investigation belong to the separate session and are not
reopened here. The already completed merge remains recorded separately.

| Owner | Independent package and output |
| --- | --- |
| implementer0 | Own historical timing metadata and any required historical downloads: initial 10–15 recent completed comparable workflow runs, prioritizing staging and recent feature runs. Record exact run/attempt/head/date, workflow and matrix job names, runner/platform where available, job/step timestamps and outcome. Separate comparable successful execution, failed runtime, cancelled/incomplete samples and pre-execution infrastructure failures. Own `ci-duration-history.md` and its evidence. |
| implementer1 | Own exact-source budget/dependency analysis: workflow DAG, runner allocation, build/cache prerequisites, job/step timeouts, runner/test deadlines/retries, scale/aged preparation and stress loops, cleanup/artifact stages. Trace the still-active job identified by implementer2, then relevant comparator source/config differences. Own `ci-duration-source.md`; no duplicate historical API discovery or current polls. |
| implementer2 | Remains sole current `39767770407` observer. Supply one fresh receipt from the existing watcher: observation time, active/queued jobs, start/finish/step timestamps, latest progress evidence and runner context available. Keep uncertainty where live logs/queue reasons are unavailable; no new observer or retry. |
| architect0 | Reconcile elapsed-time accounting, source budgets and comparable history into this design and synthesis. Identify the likely bottleneck only at the strength supported by timestamps and progress evidence; propose the smallest follow-up if necessary. Lead assigns packages and owns user communication. |

Distinguish workflow wall age from job runtime and from the active test's
runtime. Use one timestamp zone and record snapshot time. Trace prerequisite
completion before describing later starts as runner queue delays: a gap may be
dependency waiting, runner allocation, concurrency scheduling or unavailable
evidence. Do not sum overlapping jobs as workflow duration. For an unfinished
job, report observed elapsed time as a lower bound, not a completed duration.
Separate preparation/build/substitution, guest boot, intentional aging/workload,
activation/checks, teardown and artifact upload where the logs permit.

The comparison must match exact matrix identity, platform, scale parameters,
source/test configuration and attempt, or disclose the mismatch. Record
historical sample counts and exclusions; a cancelled nine-hour run is censored,
not a nine-hour pass. Give per-comparable-lane range/median and current elapsed
against configured bounds where evidence supports them. A high workflow age or
quiet step alone does not establish active runtime regression or a hang; a
large designed timeout alone does not explain the observed time consumed.

Acceptance is a compact timeline/critical-path explanation, actual historical
sample and links, remaining progress/deadline limits, and a supported verdict:
designed workload, waiting/preparation overhead, demonstrated regression or
still unresolved. Reconcile matrix totals and source references locally; no
new execution is selected. There is no compatibility/deployment behavior change
in this investigation. Any subsequent fix, cancellation or test requires a
separate lead decision; retain current CI ownership and leave sessions open.

### CI duration finding

<a id="current-timing-evidence-and-provisional-interpretation"></a>

**The observed nine-hour age is explained chiefly by sequential AMD allocation
and deliberately four-hour aging workloads. This bounded comparison does not
demonstrate a new execution-duration regression or hang.** That conclusion is
about the fixed snapshot, not a claim that current guest progress is proven or
that the long feedback cycle is desirable.

The accepted [current receipt](ci-duration-current.md),
[historical sample](ci-duration-history.md) and
[exact-source budget](ci-duration-source.md) separate the time spent:

| Segment on 2026-10-22 (UTC) | Observed time |
| --- | --- |
| Workflow creation 11:03:56 to build start 11:04:51 | 55s initial waiting |
| OS/cache 11:04:51–11:18:07 | 13m 16s |
| AMD aged-v6 11:18:09–15:42:18 | 4h 24m 09s; failed assertion |
| AMD low-memory-v5 15:42:20–15:48:38 | 6m 18s; passed |
| AMD low-memory-v6 15:48:40–15:54:57 | 6m 17s; passed |
| AMD aged-v5 15:54:58 to snapshot 20:32:57 | 4h 37m 59s active; test step began 15:55:02 |
| AMD fresh and ordinary AMD | Still queued since 11:18:07, no assigned runner or steps |

The four executing AMD rows used runner ID 11199,
`gh-runner4.int.vpsadminos.org`, without overlap. Aged-v5's 4h 36m 51s
creation-to-start wait is accounted for almost entirely by preceding same-run
AMD work. Precisely: 55s + 796s build + 16,611s allocation wait + 16,679s active
v5 = 34,141s, or 9h 29m 01s workflow age. Queued jobs' placeholder start times
are not execution. API overall `queued` is compatible with an active job.
This proves the observed serial allocation, not a complete inventory of runner
capacity or every external scheduling cause. The raw
[run](generic-sysctl-ci-39767770407-duration-run.json) and
[job](generic-sysctl-ci-39767770407-duration-jobs.json) receipts were captured by
implementer2's sole observer at 20:32:55–57Z; no new current query was made here.

The workflow has a build/cache prerequisite, then parallel native and nine
livepatch matrix lanes: six request `amd-livepatch`, three `intel-kvm`. They
need only build completion; no native-test dependency, `max-parallel` or
workflow concurrency group imposes the observed AMD sequence. `fail-fast: false`
keeps remaining jobs eligible after failures. At the snapshot, six jobs had
passed, two failed and three remained unfinished. Aged-v5 finishing would still
leave two queued AMD lanes.

The aged profiles intentionally use 128 guest vCPUs, 16 GiB, 100,000 tasks and
14,400 seconds of aging *before* hotplug/activation. Aging checks progress,
network/TUN/NFS and kernel health each iteration; it is not a blind four-hour
sleep. Setup readiness, activation and disable each have separate 1800-second
bounds; activation retries share one deadline. The 900-second default is per
guest command, not the entire test. No whole-test retry is selected. The fresh
lane itself contains 22 sequential cases. Details and exact source lines are
in the source note; per-phase limits must not be added into a promised runtime.
The aggregate main-step/job cutoffs are 350/360 minutes. For the active v5
attempt they project to 21:45:02Z / 21:54:58Z, not a nine-hour workflow deadline.
At the fixed snapshot, 1h 12m 05s remained in the step budget. These are configured
bounds, not finish estimates or proof of forward progress.

Historical coverage is **15 completed push runs**, all attempt 1, Oct18–22,
with three focused dispatch discoveries excluded. The 72 AMD records comprise
20 successful test steps, three runtime failures, three runtime cancellations
and 46 cancelled jobs with no runner/steps. Only successfully completed,
source-matched executions enter the following baseline:

| Aged matrix | Successful sample | Job min / median / max | Test-step range |
| --- | --- | --- | --- |
| v5 | 2 runs / 2 heads | 4h 44m 25s / 4h 44m 48.5s / 4h 45m 12s | 4h 44m 12s–4h 44m 59s |
| v6 | 2 runs / 2 heads | 4h 42m 14s / 4h 45m 36s / 4h 48m 58s | 4h 42m–4h 48m 44s |

At `b81c43ff` and `49636f90`, the workflow, qualification shape/script/common/
helper, fixture and boot-base recipes, test-runner and osvm match `846bb`.
Root Nixpkgs and OS inputs differ, so this establishes workload/machinery
comparability rather than identical environments. The added `system/sysctl`
case belongs to the native suite, not these aged selectors. Older comparators
have the same aging workload but changed preparation machinery and are excluded
from these strong statistics. Full heads, branches, UTC timestamps, job links,
exclusions and comparison objects are retained in the lane notes.

The current v5 step's 4h 37m 55s elapsed was below both matched prior successful
v5 durations. Bootarg-only `b81c` run `39600028637` already took 12h 41m 30s
through its last job completion, with all nine livepatch jobs passing. Its six
AMD jobs executed sequentially for 11h 56m 21s. (The API run-update timestamp was
one second later; it is not the completion definition used for comparison.)
Same-head staging short failures and unassigned 24-hour cancellations do not
represent faster successful qualifications. The sample is too small to estimate
tail latency, and an unfinished current run is not a measured faster pass.

Latest inner-test progress is unavailable. An actual stall conclusion would
require a nonadvancing phase/state, breached progress/readiness/transition bound
or a timeout result; step metadata supplies none. A large timeout alone likewise
does not prove useful work. The existing observer owns subsequent receipts;
this investigation selects no extra polling, reproduction, retry, cancellation
or source change. The evidence supports a longstanding feedback-latency issue
from workload and allocation; any capacity or coverage-scheduling change needs
its own scoped decision rather than silently shortening qualification coverage.
The completed merge and separate failure investigation remain unchanged.

## Module-autoload compatibility investigation brief

New bounded question: does the merged generic sysctl service preserve
`boot.kernel.moduleAutoload`, and does verification establish that behavior?
Inspect exact merged `846bb469505789ba0b2a405fa5905ba6d8253006` and its actual
pinned Nixpkgs renderer/activation inputs. No source edit, build, VM, evaluation,
host write, Git mutation or additional CI observer is selected. Current
implementer2 retains CI/Git; the separate CI-failure session is untouched.

Initial source facts: `os/modules/config/kernel.nix:160–179` defines autoload
`enable = false`, `log = true`. Lines 12–34 select a logging wrapper which
denies or loads; without logging, disabled mode uses an empty modprobe path.
Lines 435–446 set `boot.kernel.sysctl."kernel.modprobe"` and replace the
modprobe activation script whenever denial or logging is requested. The generic
service applies normal `sysctl -w --system`; it does not itself select kmod.
These facts are a source starting point, not a runtime compatibility verdict.

| Owner | Disjoint package and acceptance |
| --- | --- |
| implementer0 | Existing test coverage and adequacy only: inspect `tests/suite/system/sysctl.nix`, module-autoload/boot tests and retained successful receipts. Identify exact assertions for autoload enable/log combinations, boot and changed/unchanged live switch, restart, overrides/null/removal and generated versus extra sysctl inputs. Separate executed tests from source-inferred coverage; propose the smallest missing meaningful cases. No new checks or runtime tests. |
| implementer1 | Exact source/render/ordering lane: trace kernel module policy, pinned upstream kernel/modprobe activation and sysctl/ETC renderers, stage-2 → activation → runit stage1 → service ordering, switch/test and restart ordering, input precedence and key-removal behavior. Produce a four-mode value/activation table and explicit conflicting-override/null/extra-file limits. No evaluations, product changes or host operations. |
| architect0 | Synthesize lane evidence, distinguish intended default preservation from explicit overrides and unsupported guarantees, and record the smallest correction/test proposal only if a concrete regression exists. Own this document and synthesis; lead assigns packages and decides any fix. |

Required conclusion: whether late boot/service replay can replace the disabled
autoload value with plain modprobe; whether live transitions/removal preserve
the intended policy; and exactly what existing tests demonstrate. Account for
normal procps file precedence and asynchronous new-service startup, without
assuming switch success proves application. Keep initrd behavior, explicit
module loads and kernel autoload distinct. Any proposed fix must preserve
enable/log semantics, explicit override policy, mixed-version switching and
rollback, and must be a new supported change after the merged head rather than
rewriting merged history. No deployment or lifecycle action is authorized.

### Module-autoload compatibility finding

**Source-supported result: the merged generic service preserves ordinary
`boot.kernel.moduleAutoload` settings. No default-policy regression or runtime
fix is established.** Existing tests exercise real autoload behavior, but do
not explicitly prove its composition with a completed service restart or a
policy-changing switch. These are separate strengths of evidence.

All OS references below are at `846bb469505789ba0b2a405fa5905ba6d8253006`.
Implementer1 verified the root Nixpkgs input `da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36`
against the cached `/nix/store/640irzgl08asrnjly4dspdbx8lz3cvqr-source` NAR hash
without evaluation/build. That pin supplies the sysctl, modprobe, ETC and
activation modules imported by `os/modules/nixos-modules.nix`.

| enable | log | Activation writes | Generated `kernel.modprobe` and replay |
| --- | --- | --- | --- |
| false | true (default) | Logging wrapper which exits 1 without loading | Same denying wrapper |
| false | false | Empty helper path | Empty string; procps writes the empty value |
| true | true | Logging wrapper which executes kmod | Same loading wrapper |
| true | false | Upstream plain kmod path | No OS declaration for this key; replay alone makes no write absent other inputs |

`os/modules/config/kernel.nix:12–34,159–177,435–446` defines the table. The last
row assumes upstream `boot.modprobeConfig.enable` remains at its default true;
disabling that separate option also removes its activation writer. Pinned
`nixos/modules/config/sysctl.nix:94–98` emits non-null values in `60-nixos.conf`.
An empty string is not null. Retained procps 4.0.6 `sysctl.c:623,684–707,718–738`
accepts and writes an empty value, so silent denial is not converted to kmod.
No `logModuleLoading` option/coupling was found in exact OS/pinned upstream
modules; kernel-request logging here is distinct from explicit configured-module
loading in `os/modules/config/kernel-modules.nix`. Explicit host loads remain
permitted when automatic kernel requests are denied.

Boot ordering is activation (`stage-2-init.sh:65`) → explicit configured module
loads and synchronous `sysctl --system` (`config/runit.nix:19–26`) → supervised
service replay in default/rescue. The earlier initrd helper setting
(`stage-1-init.sh:73`) is pre-existing and outside this stage-2 policy guarantee.
All default-policy writers agree, including the second boot application.

On every real switch/test, activation writes the target policy even for an
otherwise identical configuration. Changed existing services restart afterwards
assuming their stop succeeded (`switch-to-configuration.rb:75–120,198–203,295–302`).
A newly introduced service starts asynchronously as its `/etc` symlinks become
visible; there is no dependency ordering it after the modprobe activation
fragment. Its replay and activation can therefore race for *conflicting* values,
but ordinary settings agree in either order. Switching to enabled/unlogged mode
restores plain kmod through upstream activation, not by resetting an omitted
sysctl. Direct activation alone does not replay sysctl files.

Limits which matter for overrides and tests:

- The policy's sysctl declaration has ordinary priority; a stronger explicit
  value can replace it. Equal-priority conflicting values fail Nix merging.
  Activation remains an independent forced policy writer. A null declaration
  omits replay but does not cancel activation or restore a previous value.
- Later files or `/etc/sysctl.conf` can override `60-nixos.conf`; an earlier
  conflicting file can also create a transient value before the policy is
  reapplied. Procps applies writes in order, not atomically. Managed inputs
  trigger service changes; unmanaged inputs can affect a replay without
  triggering it. These are deliberate-input/ordering limits, not observed
  default-policy failures.
- An unchanged switch still activates and can overwrite manual drift or an
  explicit sysctl value while an unchanged service skips replay. Restarting the
  service can then reapply the explicit value. Do not copy the printk test's
  unchanged-input retention expectation to this independently activated key.
- Removed/null keys do not reset live values. Protected/stopped services,
  unsupported runlevels and failed writes limit application. Switch exit,
  supervisor down and the completion stamp alone are not current-value proof.

The accepted [coverage matrix](module-autoload-test-coverage.md) records saved
exact-head CI `39767770407`: **16/16 module-autoload examples passed** (182.24
seconds), covering enable false/true with logging, five real trigger families,
module-state assertions, wrapper/logging, direct activation, explicit host loads
and manual sysctl toggles. **All eight generic sysctl examples passed** (82.02
seconds), using printk/vfs settings. Neither suite explicitly waits for a fresh
service application and then probes autoload after a restart or policy-changing
switch. Silent modes and explicit key override/null/removal are also absent.
No new test, evaluation, build or runtime operation was performed in this review.

Smallest proposed improvement: extend the existing autoload fixture with one
existing dummy-link probe after fresh boot/restart service completion, then a
compact four-mode switch/test roundtrip including permissive → disabled. Check
helper/empty value, actual module outcome and logging; observe completion before
trusting down/check. Reuse existing probe guards instead of multiplying all five
trigger families. Focused module/render cases can cover explicit override/null,
and a later-file case should assert the documented precedence and a subsequent
unchanged activation's independent rewrite. A narrow documentation clarification
should scope unchanged-input manual-value retention to the service, since other
activation writers can change keys. These are proposals only: no source fix,
new tests, merged-history rewrite, deployment or lifecycle change is selected.

## Current integration and investigation status

Integration is complete: vpsAdminOS `staging` advanced fast-forward from
`55c5046514d06fe9398a022c1622bdaae5228841` to
`846bb469505789ba0b2a405fa5905ba6d8253006`. The lead directly inspected successful
hooks/push receipts and remote feature/staging ref proof at
`2026-10-22T17:19:40Z`. Repository claim
`8c19bca8-754b-4b6c-9400-78ab645943f0` was authoritatively released at
`17:19:57Z`. The user accepted the observed red-CI exceptions; this records a
completed merge, not green CI or a deployment.

Failure investigation is handed off to the newly created
[2026-10-22-ci-failure-analysis session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/),
whose lead verified the delegated_4 roster: four ready implementers, architect
and reviewer. Its goal covers causes, recurrence, solutions and test purpose /
usefulness, including keep/revise/remove recommendations. The evidence and
suggested lane boundaries below remain its handoff inputs. Current-run
600-second CI observation remains implementer2-owned through terminal status.
This session stays open; no deployment, pin change or lifecycle action occurred.

## Separate failure-investigation handoff

The user has explicitly said the observed CI failures are not blockers for this
merge and requested a new workspace session with four implementers to investigate
their causes, suggest solutions and assess the failing tests' purpose/usefulness.
The lead has created that session and completed integration as recorded above.
Earlier merge-blocked/unmerged statements below describe the previous gate.
CI remains red; accepting these failures does not make it green. Current
implementer2 retains CI/Git ownership; the current session remains open.

The expanded historical comparison has **not started**: no new historical API
queries/downloads or implementation assignments were launched here. Transfer
the existing evidence and any future comparison into the new session rather
than running parallel investigations. Proposed independent packages:

| Lane | Investigation and proposed outcome |
| --- | --- |
| 1: retained impermanent datasets | Explain the five post-switch clone-to-base `boot_dataset` mismatches using saved pre/post identity and runtime/mount evidence where available. Distinguish API reporting from actual mount/data behavior. Assess what the upgrade assertions protect and propose a supported fix or narrower diagnostic step. |
| 2: nested Podman readiness | Trace the predecessor DHCP/seccomp denial and missing IPv4/default route before target activation. Assess whether the readiness assertion protects a supported upgrade prerequisite and whether its diagnostics/timeout need revision. Do not attribute this path to the incoming service, which never executed. |
| 3: AMD hotplug warning | Investigate the scheduler teardown invariant violation during the first CPU127 offline, before incoming v7 execution. Identify the excess runnable/pinned task if evidence permits; assess hotplug coverage and the final no-fault assertion without assuming successful commands make the warning benign. |
| 4: comparative history and test value | Own shared historical metadata/sample selection and coordinate lane-specific artifacts to avoid duplicate downloads. Compare exact signatures across an initial 10–15 relevant completed runs per lane, with staging/feature provenance. Independently assess all three families' intended guarantees, validity, diagnostic quality, maintenance/flakiness and evidence for keep/revise/remove recommendations. |

Each causal lane should also assess its own tests; lane 4 reconciles those
assessments. Future reports must distinguish test pass, exact-signature failure,
other failure, unexecuted/skipped, cancelled and unavailable evidence. Include
run/attempt, exact head, date, job/test, URL/local evidence and sample denominator.
Overall red jobs, timeouts alone and unrelated warnings are not signature
matches. Recurrence does not prove harmlessness or exclude current contribution.
The new lead selects any expansion, reproduction or implementation separately;
this handoff selects none.

Current source is `846bb469505789ba0b2a405fa5905ba6d8253006`; CI run
[39767770407](https://github.com/vpsfreecz/vpsadminos/actions/runs/39767770407).
Product job `119793311317` has 124 passes and six failures; the separate
focused service VM passed all 8 examples, and CI `system/sysctl` passed.
Use [current failure synthesis](generic-sysctl-ci-failure.md),
[nested evidence](generic-sysctl-ci-nested-podman.md),
[dataset causal boundary](#current-product-ci-causal-boundary), and
[AMD source boundary](#amd-livepatch-hotplug-warning-boundary).
Product saved artifacts are under
`generic-sysctl-ci-39767770407-600s-failure-119793311317/artifacts/os-test-logs-39767770407-1-native/`;
AMD artifacts under
`generic-sysctl-ci-39767770407-600s-failure-119793311395/artifacts/`.

Historical seed: [bootarg-only b81c analysis](os-hardlockup-ci-failure-analysis.md)
and `os-hardlockup-ci-new-result.json` / `os-hardlockup-ci-new-jobs.log` record
[39600028637](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637)
at `b81c43ff6865a033268072f55cd94ad763d0630b`: 124 product passes, the same
five dataset failures, and all nine livepatch jobs successful. Its local native
archive/extracts are retained. Prior `852826` run `39745935323` failed before
VM execution on HTTP429; `88486` run `39759039117` and `895870` run
`39764186292` were cancelled. These are exclusions/coverage limits, not negative
evidence for the signatures. No broader recurrence frequency is established.

## Pre-merge evidence and historical checkpoints

Second current-head CI failure: `kernel/livepatch-qualification@amd-scale-aged-v6`
failed its final no-fault dmesg assertion on a scheduler warning during CPU127
offlining. The [bounded source interpretation](#amd-livepatch-hotplug-warning-boundary)
below separates this from product failures and does not select a repair.

Current accepted source: generic v3
**`846bb469505789ba0b2a405fa5905ba6d8253006`**, tree
`df9bd828d843225df749b7a05ed9529bf17425c9`, on unchanged base `55c50465` and
panic parent `85282623`. Same-path normalization proof, ten ordinary variants
and the corrected EINVAL fixture's quick checks pass. [Final review](generic-sysctl-final-review.md)
accepted the complete range across all four HIGH-risk lanes with no findings,
including full history, no migrations and no repeated update streams.

Normal declared-environment SSH publication and remote-ref proof for `846bb469`
are complete; staging remains `55c50465`. The focused `846bb469` VM command
**passed with durable exit 0: all eight examples and the single test succeeded**.
It ran from `2026-10-22T11:08:31Z` to `11:14:33Z` (362 seconds wrapper elapsed;
353.17 seconds runner elapsed). The lead inspected the selected current log,
exit receipt and clean source. The accepted
[final VM binding receipt](generic-sysctl-focused-vm-846bb4695-receipt.json)
confirms all six changed files in the actual frozen runner equal exact
`846bb469` blobs and the worktree; its native configuration includes the
corrected boot wait, EINVAL probe and single-attempt assertion. Current native
`expected_success` at `11:14:33Z` agrees with durable exit 0 and all eight
passing examples. Older `89587060` diagnostic timestamps remain historical.
Exact-head CI `39767770407` is not green: product job `119793311317` failed at
`2026-10-22T14:42:27Z` after 3h 6m 41s; other jobs remain active. The conditional
merge gate is blocked. Bounded local diagnosis identifies five recurring
dataset-reporting failures and a separate nested-container timeout; see
[the causal finding](#current-product-ci-causal-boundary). No claim, merge, rerun,
source change or broad repair is selected. The focused eight-example pass
remains separate evidence. Existing CI observation stays with the current
watcher; architect0 does not duplicate it. The session remains open, unmerged
and undeployed.

The user explicitly approved periodic CI checks (approximately every ten
minutes) and merging when done. The lead records this as authorization to merge
**vpsadminos into its registered `staging` branch after successful exact-head
CI**, subject to the final freshness gate before the short repository claim.
Implementer2 owns the existing watcher cadence and unlocked target/hook
preparation. No new observer is needed. This authorization excludes deployment,
pin changes, configuration-repository integration and session lifecycle actions.
Earlier no-integration statements below describe superseded authorization.

## Current product CI causal boundary

CI `39767770407` on `846bb469` completed its product suite with 124 passing
tests and six failures. Architect0 compared the five current dataset first
errors, switch commands and container/boot identities with the preserved
[b81c failure provenance](os-hardlockup-ci-failure-analysis.md). Implementer2
owns current sysctl execution evidence and the consolidated failure note;
implementer0 independently owns the nested-container timeout. No new runtime
loader audit, evaluation, VM, remote collection or repair is selected.

The five cases again report `tank/ct/niximpermanent` after previously reporting
`tank/ct/niximpermanent.impermanence-<suffix>`. All execute the `846bb46`
`switch-to-configuration test` with status 0 and retain kernel release, boot ID,
booted-system path and the impermanent container's running state/init PID.
Within the current artifact root
`generic-sysctl-ci-39767770407-600s-failure-119793311317/artifacts/os-test-logs-39767770407-1-native`,
the following `machine-shell.log` lines record before/switch/after respectively;
each `test-runner.log:4-5` records the expected/actual dataset:

| Case directory suffix after `os-test-upgrade__from-` | Clone suffix | Init PID | Shell lines |
| --- | --- | --- | --- |
| `6.12-guests-96d1dd0d` | `4febac` | 6191 | 1927 / 2854 / 3255 |
| `6.12-guests-v1-d2a0633c` | `bd3a1e` | 6280 | 1993 / 2832 / 3223 |
| `6.12-inherited-guests-ca257393` | `931fb2` | 6158 | 1946 / 3436 / 4007 |
| `6.18-guests-7613a053` | `798605` | 7370 | 2772 / 3703 / 4107 |
| `6.18-guests-v1-148de9c7` | `7b3ada` | 6802 | 2700 / 3543 / 3947 |

These same five signatures occurred at `b81c43ff` before the generic service
existed. The upgrade fixture, container export/run-configuration files, runit
stage-1 file and Ruby switcher have no diff between that head and `846bb469`.
This establishes prior occurrence and unchanged inspected source boundaries,
not a controlled current-baseline result or proof of identical root cause.
The preserved export/loader fallback explains the shape of the report without
establishing whether runtime metadata or the actual mounted root changed.

The earlier exclusion of the new boot argument does **not** exclude today's
generic service: this service can execute after a userspace switch without a
reboot. Implementer2 found `runsv sysctl` and its logger in all five postfailure
process snapshots, with the service down for 43/37/68/99/101 seconds. This proves
presence, not successful application. The saved artifacts omit post-switch
service log contents, applied/done stamps, custom-check results and value
readbacks. Missing explicit `sv sysctl` in the switch log is not exclusion:
runsv starts new services asynchronously. Exact application timing, outcomes
and a causal link to the dataset mismatch remain unresolved. Neither prior
signature nor the focused/current-CI sysctl test passing proves compatibility
with this inherited-container path.

No generic-service or impermanence fix follows from the present evidence.
Useful discriminating data, if a later diagnostic is authorized, are pre/post
impermanent run-configuration bytes and actual mount source, together with
timestamped sysctl service logs, completion identity/check and relevant value
readbacks around activation. These distinguish reporting fallback from a mount
change and service execution from mere presence. First consume retained evidence;
do not launch a blind rerun or broaden the repair under this finding.

The [independent nested-container finding](generic-sysctl-ci-nested-podman.md)
has a different execution boundary: on pinned predecessor `3cb830e5` with
kernel `6.18.49`, dhcpcd reported `ps_managersandbox: seccomp: Permission denied`
before target activation. Interface setup failed, leaving no IPv4/default
route, followed by 126 failed readiness probes. The exact fixture calls this
readiness wait before activation; the preserved commands and service listing
corroborate that the incoming generic sysctl service never executed in this
failing path. That excludes the incoming service as this timeout's executed
cause, without identifying the effective filter/syscall denial mechanism or
which component introduced it. Do not transfer this exclusion to the five
post-switch dataset cases. The suite and conditional merge gate remain failed.

The prior second `89587060` VM run booted and
passed six normal examples; two negative assertions exposed invalid failure
injection. Native `unexpected_failure` is explicit and the outer exit remains
unavailable. That run does not validate the corrected v3 source or fixture.

Current implementation: **declarations only** for both hard- and soft-lockup
panic sysctls, accepted at `85282623` with quick checks passed. Its earlier
CI preparation failure is separate from the generic-service checkpoint below.
The user rejected the additional activation hook. The
[declaration-only correction](#declaration-only-hard-and-soft-panic-policy)
governs this revision. Earlier activation design/review is superseded and kept
as history. Conditional vpsadminos-to-staging integration is authorized as
recorded above; runtime deployment, pin updates and lifecycle actions are not.

The user has now authorized implementation of the
[generic runit sysctl service](#approved-generic-sysctl-service).
This approved contract supersedes both earlier generic proposals. The paired
panic declarations remain unchanged; the generic service is a separate logical
commit, **`88486d43f7d47917b6ab796163abf8cd1f0be94a`**, on that panic-policy
parent and base `55c5046514d06fe9398a022c1622bdaae5228841`. The worktree is clean
and all intended quick checks passed. Final reviewer0 review accepted the
complete range with no findings, and normal SSH publication is verified;
staging remained `55c50465`. This is the earlier `88486d43` checkpoint: CI
`39759039117` had started and the focused VM was awaiting cache prerequisites.
The later `89587060` VM has since launched, as recorded above; implementer2
retains verification ownership.

## Approved generic sysctl service

Implementation authorized, 2026-10-22. The user chose a normal runit service,
one application attempt per start/configuration change, and the existing
switcher's exit-status behavior. No direct switcher step, crashdump-specific
activation hook, generic wrapper change or control-script framework is in scope.
This section is the current implementation brief; prior proposals below are
historical. Source basis: [existing contracts](generic-sysctl-contract.md).

Current checkpoint: [verification packet](generic-sysctl-verification.md)
records commit `88486d43`, ten real module-graph variants, isolated native
runsv checks, fixture rendering/generated Ruby syntax, Nix/MkDocs checks and
normal hooks, all passed. [Final review](generic-sysctl-final-review.md)
accepted all four lanes at high risk with no findings, including the complete
`55c50465` to `88486d43` history, no migrations and no repeated update streams.
Source acceptance and verified publication do not establish CI success, focused
VM behavior or actual host application. At this earlier checkpoint CI
`39759039117` was pending and the focused VM had not run. The prior panic-head
[HTTP429 preparation failure](os-hardlockup-v3-ci-failure.md) is separate
evidence and does not assess this generic service.

### File ownership and interface

| Owner | Files and responsibility |
| --- | --- |
| implementer2 | New `os/modules/config/sysctl.nix`, registration in `os/modules/os-modules.nix`, generated-module/script quick checks, and all serialized Git/commit/publication operations. |
| implementer0 | New focused `tests/suite/system/sysctl.nix`, registration in `tests/all-tests.nix`, and a sysctl section in existing `docs/os/configuration.md`. Supply test/docs changes to implementer2 without concurrent Git mutation. |
| architect0 | This brief and `synthesis.md`; consequential deviations go through the lead. |
| lead | Acceptance, final reviewer assignment, verification coordination, state and portal. |

The service is named `sysctl`; its custom completion check is exposed through
the existing `/service/sysctl/check`. Use `/run/service/sysctl/applied` as the
service-local success stamp, with a single current-input identity. The test
and documentation must use these same interfaces. No new product option or
general status API is needed. Implementer2 sends the rendered run/check paths
and identity construction to implementer0 for focused tests.

### Service, input and completion contract

Declare `runit.services.sysctl` with `oneShot = true`, `onChange = "restart"`,
runlevels `[ "default" "rescue" ]`, and standard logging including stderr.
Leave `os/modules/config/runit.nix` stage-1 application and ordering unchanged.
The later service application on boot is intentional; single/custom runlevels
do not gain the service automatically. No dependency on crashdump enablement.

Select enabled entries from the final merged `environment.etc`, using their
**effective target**, not merely their attribute key: `sysctl.conf` and direct
`sysctl.d/*.conf` files, including generated `sysctl.d/60-nixos.conf`. Build a
deterministic ordered identity from effective target names and final source
paths. Use the same managed-input set for `restartTriggers` and the identity
embedded in run/check scripts. Include additions, removals and target renames;
ignore disabled and unrelated entries. Do not introduce a second renderer.

### Literal-source content tracking correction

Lead accepted, 2026-10-22: `toString file.source` preserves an ordinary literal
path outside the store, so editing that file at the same pathname can change
installed `/etc` content without changing the service identity, triggers or
run/check paths. Reproduced on `895870606179f0c1170ad92a5fdc49eb2d6d1bbf`.
The final source option remains type `path`; it is not already normalized.
Root Nixpkgs `da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36` explicitly uses
`"${etcEntry.source}"` in `nixos/modules/system/etc/etc.nix:60-61` to copy local
paths into the store; its source option at lines 157-160 has no such conversion.

In `managedInputs`, replace `source = toString file.source;` with
`source = "${file.source}";`, plus a short comment explaining agreement with
the etc renderer. This is the complete product-source correction: no new
abstraction, string-path policy, framework or test harness.

The retained direct-import reproducer is
`/tmp/kernel-check-literal-sysctl-lcphi09o/eval.nix`, with
`literal-module.nix` selecting `source = ./some-sysctl.conf` for effective target
`sysctl.d/80-literal.conf`. Changing only the file from
`kernel.printk_ratelimit=7` to `=9` changed the renderer's store snapshot while
the old identity, triggers and run/check paths stayed identical. Acceptance
after correction requires that same-path edit to change the canonical source,
identity, triggers and generated run/check paths, matching the renderer's
snapshot; ordinary text/store inputs retain their existing results.
Implementer2's corrected-source proof now meets this acceptance: canonical
source, identity, triggers and run/check paths change for the same-path content
edit, and all ten ordinary variants remain stable.

Implementer2 completed the minimal fix and quick regression evidence in generic
logical owner v3 `846bb469`; fresh final review accepted all four affected lanes,
as linked above. Publication is verified and the corrected focused VM passed
all eight examples with exit 0; CI remains pending. The earlier
frozen-source run remains separate evidence for its old snapshot. Its reported
second-run boot and six passing normal examples do not certify the literal-path
fix or corrected negative probe. Implementer2 retains diagnosis and the existing
watcher for `89587060` CI; no additional observer.

Use the existing service environment field `SYSCTL_INPUT_IDENTITY` to carry
the computed identity. Keep run/check text independent of its value and refer
to the exported variable; the existing wrapper embeds the value. Implementer2
found that interpolating the identity directly into check text recurses through
`environment.etc`, because runit tests whether check text is empty while
constructing etc keys. This service-local plumbing avoids that recursion without
changing the wrapper, triggers or external completion interface.

The application command is the explicit `${pkgs.procps}/bin/sysctl -w --system`.
It retains normal procps file precedence and the full system input set. The
managed trigger set is narrower: unmanaged/local edits and other runtime or
vendor inputs do not themselves schedule an application. A manual retry reads
their current contents. A successful stamp records an application, not continuous
equality between configured and live values.

The first service-local operation is checked, **non-waiting** explicit runit
`sv once`, before marker invalidation or sysctl. After successful control,
invalidate prior `applied` and legacy `done` markers, then apply settings.
Ordinary setup/application failures must exit explicitly before the success
footer, without automatic retries. If sending supervisor control fails,
best-effort invalidate the old markers, report the failure and exit without
invoking sysctl. In that exceptional case, once mode and absence of supervisor
retries cannot be certified. If marker invalidation fails, report that any
remaining stamp is not evidence of fresh success and do not apply settings.
Do not use a waiting `sv once` from inside the service or add a retry loop.

Invoke sysctl without `exec`. On failure, emit a diagnostic and explicitly exit
nonzero before the existing oneShot footer. Only after successful application,
write the expected identity to a temporary file in the same directory and
atomically rename it to `applied`; handle marker-write failure explicitly too.
Then fall through to the unchanged wrapper success/footer behavior. The custom
check requires the current identity in `applied`, never just existence of
`done`. An older configuration's stamp must fail immediately, before the new
run starts. An interrupted or failed attempt cannot publish success.

No `control.u` hook: runit's `once` also uses that hook, including the wrapper
footer's own command, so clearing success there would undermine completion.
No collection of signal/control overrides is authorized to create synchronous
switch success. If actual supervisor behavior contradicts the one-attempt
contract during verification, report the evidence before expanding the design.

### Runtime limits, retry and compatibility

Keep switch/test ordering and exit-status handling unchanged. New `/etc` is
installed before normal changed-service start, but a successful switch exit is
not proof of sysctl success. Supervisor `sv status` or `sv check` alone is also
insufficient; a completed oneShot is normally down, and `sv check` can skip its
custom check in that state. Application errors remain visible in service logs
and the custom completion check. Partial writes are not rolled back.

Clearing markers inside run leaves a same-configuration check-before-start
race. Do not claim latest-attempt completion from a start command's return.
Document the explicit retry sequence: stop and confirm the old attempt ended;
invalidate `applied` and `done`; issue `sv once`; observe that attempt completing;
then invoke `/service/sysctl/check` and inspect logs. Do not confuse the initial
down state before an asynchronous start with completed execution. After an
attempt has finished, a failed retry must leave no valid success stamp.

Old and new OS versions can coexist; no coordinated fleet update or persistent
format, schema, API or protocol migration is needed. The stamp is ephemeral
under `/run`. Switching to a generation containing this service can apply
configured sysctls without reboot, including overwriting manual overrides.
Removing/nulling a key or removing the service does not restore its prior live
value. Rollback to an older OS without this service does not automatically apply
old values; any future operator rollback needs explicit readback/application or
an appropriate reboot. Conditional staging integration follows the current
authorization above. No pin update, deployment, production sysctl write,
induced lockup/crash or session lifecycle action is authorized.

### Acceptance and verification order

Quick checks: real module evaluation and rendered scripts; enabled/effective
target selection, disabled exclusions, deterministic ordering, changed/add/remove
input triggers and unchanged-input stability; default/rescue membership; unchanged
stage 1 and panic declarations. Check old-identity rejection even with stale
`done`, non-waiting once before apply, explicit failure exit and atomic success
publication. Isolated mocks may verify ordering and failure paths without host
sysctl writes. Run normal format/parse/whitespace and repository hooks.

Implementer0's focused VM test uses benign sysctls and current RSpec-style test
examples. Cover boot's intentional second apply, changed configuration through
switch/test, effective-target aliases and other managed files, stale-generation
rejection, a failed application after prior success with no automatic retries,
and successful/failed explicit same-config retries. Confirm values, logs and
custom completion independently of switch exit. Bound waits and distinguish an
attempt's completion from supervisor down before start. No forced faults or
kernel changes are needed.

Negative-probe correction from the second VM run: pinned procps 4.0.6
`sysctl --system` ignores missing-key `ENOENT`, so a nonexistent key does not
establish application failure. That injection invalidated two negative
assertions, rather than proving a service failure. Implementer0 replaced it
with an invalid integer for a known key, yielding `EINVAL`; graph/render,
generated Ruby syntax and format quick checks passed. The focused VM must
eventually demonstrate a real nonzero sysctl result before asserting failure
status and absence of retries. The previous run's native `unexpected_failure`
is known, but its outer process exit is unavailable; do not call it a passing
full run. The later corrected `846bb469` fixture passed all eight examples in
the focused VM, as recorded in the current checkpoint above.

Complete and commit module, tests and docs as a separate coherent generic
feature after the existing panic-policy commit. Quick checks precede final
independent review of the complete deliverable and history. Only after accepted
review run the focused long VM test through a fresh policy-selected watcher;
long/uncertain commands use the monitor skill, and unexpected local kernel
builds stop for diagnosis. Preserve existing CI ownership and prior CI history;
do not start another observer for the earlier panic revision.

## AMD livepatch hotplug warning boundary

Current `846bb469` CI job `119793311395` failed the final no-fault dmesg
assertion at 17:41:35 CEST. Implementer2 owns its preserved local log analysis;
architect0 inspected only the narrow local pinned kernel path. Logs are under
`generic-sysctl-ci-39767770407-600s-failure-119793311395/artifacts/`
`os-test-logs-39767770407-1-livepatch-amd-scale-aged-v6/`
`os-test-kernel__livepatch-qualification__amd-scale-aged-v6-0921d60d/`.

At uptime 14636.489, CPU127's `migration/127` task reported
`Dying CPU not properly vacated!` from `sched_cpu_dying`, `kernel/sched/core.c:8333`.
The adjacent `test-runner.log:158-160` dump reports **two enqueued tasks**, but
lists only PID789 `migration/127`. It does not identify the other task or the
pinning state. A preceding task-affinity message is context, not proof of the
offending task. The first offline/online commands returned 0; subsequent work
continued. This does not make the warning benign or establish scheduler safety.

Exact boot source is local Linux `a2384967b90f24d2470c9eb15f0e66d938df7e08`,
from the frozen boot recipe rooted at OS `c065fa2f8485399737e20e8ef9e44299d0766654`.
At `core.c:8332-8335`, the warning checks `rq->nr_running != 1` or
`rq_has_pinned_tasks(rq)`; the latter is `rq->nr_pinned` (`:2386-2388`).
`balance_hotplug_wait` expects one running task and no pinned tasks (`:8004-8010`)
before final teardown. The nearby wait-empty comment (`:8270-8278`) describes
parked/unbound per-CPU threads and warns against later bound wakeups; it does
not identify which callback, task or accounting error produced this event.
The observed count of two supports failure of the running-task invariant.
`migration/127` is expected CPU-stopper context, not an identified culprit.

The warning path dumps tasks, continues scheduler cleanup and returns 0
(`:8336-8343`); `kernel/cpu.c:2160-2164` registers it as the scheduler teardown
callback. Thus successful sysfs hotplug commands are compatible with this WARN.
This is a real CPU-hotplug invariant warning, not a hard/soft-lockup detector
report or proof of panic. Local comparisons show this core/cpu path unchanged
in the documented v6 `fc37ccc4` and NFS boot `563bbb35` sources; that proves
source continuity only, not prior runtime occurrence or absence of interactions.

The first hotplug occurred 17:24:42-17:24:51 CEST, before incoming v7 module
insertion at 17:26:09. Its later single activation completed in 757.998 seconds
within the 1800-second bound, with expected trace/callback events, followed by
another hotplug. This timing excludes execution of incoming v7 as the cause
of the earlier warning; successful activation does not erase the failed
no-fault assertion. The OS already booted current `846bb469` with the frozen
6.12.95 kernel/v6 livepatch. Its sysctl supervisor/logger and down status are
present, but no service output, stamp/check or managed-value readbacks were
uploaded. The qualification workload also writes selected sysctls after boot.
Therefore generic-service boot-state contribution remains unresolved; the
pre-activation exclusion from the nested-container case cannot be reused here.

No kernel/generic-service fix, rerun or broader audit is selected. A causal
resolution would require evidence identifying the excess runnable/pinned task
and its hotplug timing, plus actual boot/service/stress value history if a
sysctl contribution is proposed. Do not infer a callback owner, harmlessness,
data corruption or a production-hang mechanism from this warning alone.
Merge remains blocked. Implementer2 retains logs, CI/Git and the existing
600-second watcher; no evaluation, fetch, build, VM or new observer was used
for this source interpretation.

## Question and scope

Determine whether changes in vpsAdminOS's custom Linux patches between
6.12.95 and the 6.12.113 kernel used on node24.prg can explain the reported
hang: the console remained at a login prompt with a blinking cursor, while
the machine was otherwise unresponsive.

This is an investigation, not an implementation or rollout. Read canonical
bare repositories and production logs without changing them. Only this
session's investigation records are writable. The lead serializes any necessary
fetch/ref changes. Do not build kernels, change host settings, reproduce on
production, reboot, deploy, merge, or alter the session lifecycle.

Audit custom patch changes first. The user subsequently authorized an upstream
patch investigation if the custom audit yields no supported cause. That second
phase must be explicitly identified and targeted by incident evidence; do not
mix broad upstream change counts into the downstream conclusions.

## Evidence and confidence

Keep three separate propositions for every finding:

1. A code defect exists in a precisely identified version.
2. Its required configuration and triggering conditions are possible on the
   affected node.
3. The incident actually exercised that defect.

Source proof can establish the first proposition and sometimes the second; it
does not automatically establish the third. Report a cause only when a complete,
reachable failure chain is obvious from source and consistent with incident
evidence, or when focused verification reproduces it on the relevant code.
An unproven concern, commit subject, plausible subsystem match, absent log
message, or blinking console cursor does not establish causality.

Use these outcome labels:

- **Confirmed incident cause:** exact deployed code and trigger tied to a
  matching stack, trace, dump, or controlled reproduction with a discriminating
  old/new or fix/revert comparison.
- **Source-proven defect, incident attribution unresolved:** exact code proves
  the failure, but deployed identity or triggering evidence is missing.
- **Not supported:** no demonstrable failure chain or runtime corroboration.
- **Excluded within stated scope:** a specific hypothesis is contradicted by
  exact code, configuration, lineage, or runtime evidence. This does not
  certify the whole kernel.

For concurrency claims identify every lock, context, acquisition order,
reference owner, and progress dependency needed for the proposed cycle or
lifetime violation. Check error paths and compare old and new behavior.
Separate a newly introduced regression from a pre-existing defect.

## Version provenance

The version string alone is insufficient. Record the vpsAdminOS package
revision, Linux commit, matching upstream baseline, applied package patches,
configuration and boot/livepatch identity where evidence is available.
Distinguish the initial 6.12.113 pin from any later repin.

Package values read from the canonical vpsadminos repository's
`os/packages/linux/available-kernels.nix`, corroborated at incident OS revision
`2abbe3cc`:

| Package label | Linux revision | Qualification |
| --- | --- | --- |
| 6.12.95 | `a2384967b90f24d2470c9eb15f0e66d938df7e08` | Current retained pin; has `features.livepatch = true` |
| Initial 6.12.113 | `11058eb4fe1cba30653e8e643546c13bc8bcd792` | Historical first pin; includes proactive swapping |
| Incident/current 6.12.113 | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | Pin at incident OS revision `2abbe3cc`; proactive swapping removed |

The log owner found `vpsadminos=2abbe3cc`, OS `26.05.git.2abbe3c`, generation
144, and a Linux 6.12.113 build timestamp of 2026-10-18 17:47:47 UTC. This build
booted on 2026-10-19 and again after the incident. The previous kernel was
reported as 6.12.95.6; its livepatch identity must be accounted for separately
from the .95 boot source. The inventory owner records immutable package-history
refs and upstream/custom boundaries in
[patch-inventory.md](patch-inventory.md). Runtime identity and timestamps belong
in [log-evidence.md](log-evidence.md).

## Independent work boundaries

The lead owns plan/state, assignments, fetches, portal registration and external
communication. Architect0 owns this brief, causal standards, cross-lane
synthesis and follow-up verification design. Retained roster settings apply.
No repository source files are assigned for edits.

| Owner | Package and writable artifact | Acceptance and dependencies |
| --- | --- | --- |
| implementer0 | Custom patch inventory and exact old/new provenance; `patch-inventory.md` | Account for added, removed, changed and equivalent downstream patches against each version's own upstream baseline. Include initial/current .113 and runtime-identity uncertainty. Send changed symbols early. |
| implementer1 | Central log analysis; `log-evidence.md` | Establish incident interval, timezone, last/first messages, boot/build identity and specific diagnostic evidence. State collection limits and distinguish logging failure from host failure. |
| implementer1, follow-up | Packaged ZFS free-accounting patch; `zfs-patch-audit.md` | Audit `os/packages/zfs/zfs235-free-account.patch` at incident OS `2abbe3cc` against ZFS `481845fca6ae3f61ca2262c1a5693a58ae364650`, including dnode/dbuf locks, reference ownership and transaction accounting. This custom patch ships with .113 but not .95; finish before the conditional upstream phase. |
| architect0 | Fake affinity/scheduler source check and causal synthesis; `scheduler-analysis.md`, `synthesis.md` | Compare the identified affinity owner and immediate helpers; distinguish code changes from message-only identity changes; integrate all lanes without overstating causality. |
| implementer2 | Memory cgroup lifetime, proactive DAMON removal and swap; `memory-audit.md` | Consume inventory; trace changed lifetime, locking and progress behavior. Prove or reject concrete claims against incident pin. |
| implementer3 | Syslog namespace and NFS cold NLM guard; `syslog-nfs-audit.md` | Inspect changed ownership, formatting/iteration and lock paths; report exact source refs and exclusions. |
| implementer4 | Kernel packaging and runtime reachability; `packaging-audit.md` | Identify Nix-applied custom patches/config/livepatch/boot selection outside linux.git; test whether source findings can execute on the deployed package. Coordinate deployed identity with log owner; avoid repeating inventory. |

The lead assigned these refined boundaries after the early inventory. The
architect reports any necessary split or expansion through the lead. Source
reads may overlap to establish interfaces; each artifact has one writer.

The packaging lane identified a relevant kernel-resident change outside
`linux.git`: OS commit `9bca43d3` added
`os/packages/zfs/zfs235-free-account.patch`, selected for .113 at `2abbe3cc`.
Both compared versions select the same ZFS source commit, but .95 lacks this
package patch. Its changes to `dnode_sync.c` move free accounting across
dbuf-mutex/rwlock boundaries. Include this in the custom phase and its coverage
accounting; a Linux-tree-only audit is incomplete.

## Interfaces and invariants

- A direct old-to-new Linux diff includes upstream work. Compare downstream
  ranges against their own upstream bases before assigning semantic ownership.
- Commit subjects and patch versions help locate lineage; equivalent patch
  identity and exact source determine whether behavior changed.
- Package-applied patches and configuration may change effective behavior even
  when the referenced Linux tree is unchanged.
- Historical boot, current running kernel, and on-disk generation can differ.
  A current node read does not prove incident identity without continuity.
- Retain exact hashes and file/function/line references for reproducibility.
  Summarize logs and redact credentials or unrelated tenant content.
- Absence of an error in central logs cannot exclude a lockup that prevented
  local logging or log forwarding.

## Compatibility, deployment and recovery

No persisted state, API, protocol, ABI, schema, Nix option, or production
configuration changes are planned. No coordinated node update is required for
this investigation. A future remedy must receive its own implementation brief:
kernel/module compatibility, livepatch versus reboot choice, mixed fleet
operation, deployment ordering, rollback to a compatible boot generation and
ability to read existing persistent state must be explicit.

No recovery operation is authorized here. Recommendations to collect dumps or
enable diagnostics remain proposals unless separately authorized.

## Checks and stopping conditions

Quick checks: resolve immutable refs; verify upstream ancestry and patch
boundaries; compare corresponding source and caller paths; cross-check
timestamps/timezones and boot identity; verify artifact references and clearly
mark unavailable evidence.

Longer checks are conditional on an actual source candidate: define the
smallest isolated reproducer that distinguishes the proposed mechanism,
specify old/new and fix/revert controls, observable failure signature and
timeouts. Route the experiment through the lead; use the required fresh
verification watcher for long or uncertain execution. Do not start a kernel
build merely to seek a generic passing test.

The downstream phase is complete when the custom delta inventory is accounted
for, source lanes have explicit evidence-based outcomes, and log/package
identity is established or its limits are documented. If no supported custom
cause remains, report that bounded result and propose the authorized targeted
upstream phase. A negative source audit is not proof that the kernel is safe.

The final synthesis must say what is proven, what remains unknown, and the
specific additional evidence or experiment needed to settle remaining claims.
Investigation and evidence alone do not require a mandatory change review.

## Authorized targeted upstream phase

The lead accepted the custom-negative gate after complete Linux inventory,
memory/syslog/scheduler conclusions, package coverage and the bounded ZFS source
audit. The targeted upstream phase is now complete. This was an authorized
investigation expansion, not a claim that upstream Linux caused the incident.

Use these exact stable boundaries, supplied by the inventory owner and resolved
in the canonical Linux repository:

- Old baseline: `296aabce459470a4c1b68ffd0c0c0920e563aaad` (6.12.95).
- New baseline: `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` (6.12.113).
- Effective incident tree: `1dfea587406b7dd79973831d1677fb2418e5e9aa`.

An upstream-range commit is a locator, not a finding. Inspect its final
incident-tree source and downstream interactions. The old effective runtime
also included livepatch v6, so an upstream change already backported there
cannot automatically be called new at the upgrade.

Assigned independent packages, now completed:

| Owner | Source boundary and artifact | Evidence/acceptance boundary |
| --- | --- | --- |
| implementer0 | Stable-range provenance, custom-overlap map and old livepatch applicability; `upstream-provenance.md` | Own missing-object materialization. Confirm exact stable ancestry and whether a candidate was already active on .95.6. Supply facts to other lanes, not a second full semantic audit. |
| implementer0, follow-up | Seven upstream printk changes and custom namespace intersection; `upstream-printk-audit.md` | Check final panic predicates, namespace/global locking, console handover and pre-kexec ordering. Equivalent custom bodies alone do not exclude changed upstream context. |
| implementer2 | Upstream reclaim/memcg, cgroup lifetime and memory-accounting changes; `upstream-memory-audit.md` | Focus on changed paths called by downstream helpers and paths compatible with cgroup-v1 `cgroup.memory=nokmem`. Distinguish tenant-local OOM from global allocator or reclaim failure. Identify a concrete new invariant violation or known-fix match. |
| implementer3 | Upstream NFS client, SUNRPC, lockd and directly implicated VFS/writeback paths; `upstream-nfs-audit.md` | Investigate the actual timeout-adjacent evidence, but require an escalation mechanism from one container's NFS failure to host-wide loss. Check transport/error/unmount/close lock dependencies. Earlier .95.6 NFS blockage is a separate control. |
| architect0 | Upstream scheduler, RCU and locking changes that intersect the custom CPU/cgroup paths; `upstream-scheduler-audit.md` | Check changed lock/progress dependencies under observed `preempt=full`, online CPU topology and cgroup namespaces. Avoid attributing cause from cursor blinking or lack of watchdog output. |
| implementer4 | Runtime/config applicability and platform/diagnostic gates; `packaging-audit.md`, `upstream-platform-audit.md` | Match candidates to available boot/config/hardware evidence; verify watchdog/panic and dump expectations from actual configuration. Expand to a driver delta only with a matching incident clue or source-proven defect. No trust bypass or host mutation. |
| implementer1 | Incident follow-up on source-directed discriminators; extend `log-evidence.md` | Search bounded intervals for exact candidate signatures, determine which live checks actually failed from user evidence, and retain logging/console limitations. Do not rescan unrelated history without a new discriminator. |

Use `GIT_NO_LAZY_FETCH=1` for other owners' reads. Implementer0 is the single
lead-authorized owner of object-only retrieval; missing blobs are dependencies
to report, not permission to fetch refs. Keep external upstream references
limited to primary patch/code discussions and exact fixes whose mechanisms
can be checked in the incident source.

End each upstream package with either a supported defect/fix chain or a bounded
negative result and the diagnostic evidence needed next. A host hang with no
stack, dump or reproducible trigger may remain unattributed after a correct
source audit; do not substitute a ranked list of guesses.

## Final evidence constraints and disposition

The user reported that the normal crash-kernel/upload recovery did not happen,
and confirmed that configured sysctls had no runtime changes. The traced
configuration therefore supplies incident policy: hardlockup panic is 0,
softlockup panic is 1, watchdog/NMI watchdog are enabled, and the threshold is
10 seconds. A detected hard lockup need not panic under this policy.
Positive `Kdump: loaded` markers at 18:31:57/59 prove a crash image was present
about 26.5 minutes before the last log. No upload does not identify whether
panic occurred, crash transfer completed, or capture/upload failed.

The VGA text cursor can blink in hardware without scheduler progress. Neither
that observation nor missing forwarded diagnostics supplies a failure stack.
The full custom inventory/package coverage and the targeted upstream lanes
found no supported incident cause. Three definite source defects are recorded
separately from attribution in [synthesis.md](synthesis.md). No source change,
generic test, policy change or further broad audit is proposed as verification
of an unidentified mechanism. A future incident's CPU/task trace or a concrete
source-specific trigger is the next discriminating evidence. This completes
the assigned source investigation; the session remains open.

## Separate follow-up: cluster hard-lockup history and recovery

Status: collection, independent episode classification and synthesis complete.
Broad searching stopped on the first matching file, followed only by the
two remaining small legacy files in the already approved budget. This follows the user's
question about machines surviving hard-lockup detections. The completed
node24 patch audit and its unattributed
incident conclusion remain unchanged. This follow-up asks whether central logs
contain actual hard-lockup reports and what those records can prove about
subsequent host operation and affected-CPU recovery. It supplies evidence for
the user's decision about `hardlockup_panic`; it does not authorize changing it.

Session identity, both environment markers and the retained same-session
roster were rechecked before this work. Existing member settings are retained.
Only session evidence/design artifacts may change. No configuration changes,
forced lockups/crashes, tests, deployments, trust changes or lifecycle actions
are part of this package.

### Ownership and independent boundaries

| Owner | Writable artifact and scope | Acceptance/dependency |
| --- | --- | --- |
| implementer1 | `cluster-hardlockup-history.md` and compact raw excerpts; sole central-log discovery/search owner | Record exact searched nodes/files/ranges, signatures, completion and limits. Extract real hard-lockup reports and bounded surrounding records for episode classification. Keep production reads serial and bounded. |
| implementer4 | `hardlockup-recovery-semantics.md`; exact detector reporting, suppression, rearm and panic paths | Establish what an accepted report means, when it returns, how the warning state resets, alternative reset paths and whether recovery itself emits a log. Qualify historical versions against their actual source; do not infer fleet occurrences from source alone. |
| architect0 | This design and synthesis of accepted findings | Distinguish observed report, host continuity and affected-CPU progress; reconcile source semantics with log identity and chronology before making a survival claim. |
| implementer2, assigned after the first hit | `hardlockup-episode-analysis.md`; independent local episode classification from the log owner's extracted evidence | No additional remote scanner or overlapping log collection. Check duplicates, old kernel/build, positive boot continuity, target CPUs, meaningful host service continuation, CPU-specific progress and confidence. Source-owner checks are dependencies for historical detector-state inferences. |

The lead owns assignments, query-budget expansion, state/portal and the
policy-facing conclusion. No additional production scan is justified merely
to keep members busy.

### Search and resource boundary

Discovery found approximately 1.08 TiB in 3,477 files, without a ready index
or compressed subset. The lead accepted an initial single sequential pass
over 13 current logs, approximately 3.8 GB. This is a discovery sample, not
cluster-history coverage. A blind scan of the full retained corpus is excluded.
Before historical expansion, the log owner reports throughput, completed
coverage and hit counts; the lead chooses an explicit historical byte/file
budget and selection rule. Short or interrupted reads remain partial coverage.

The lead subsequently selected a bounded historical pass: 78 files,
approximately 28 GiB, within a 30 GiB budget. Seven full days would have been
43.4 GB and were not selected. The chosen rotation suffixes are October 16–20
for 13 active nodes, plus the newest retained rotation for each of 13 inactive
nodes; those inactive-node samples have latest dates ranging from December
2022 to October 2025. All 26 host directories are represented, but this is
sparse historical coverage, not 26 continuously observed hosts over one
common interval. Current-file boundary samples span approximately October 20
00:00–20:52, but the actual search finished before the last-line sampling;
later append events are not certified as searched. Exact observed spans and
completed byte counts remain the log owner's evidence.

The historical pass is serial with a 20-second timeout per file. A timeout
leaves that file incomplete and must be reported even if no hit was emitted.
All 78 files completed: 30,118,840,414 bytes in 119 seconds, approximately
253 MB/s, with no matching detection, error or timeout. The lead then allowed
three legacy files totaling 861,203,528 bytes within the same 30 GiB budget.
The first, `stg/node1/log.3` (689,725,792 bytes), completed in three seconds
and matched two actual hard-lockup messages. The scanner stopped there for
classification. The lead then explicitly resumed only the other two legacy
files (171,477,736 bytes); both completed with no match or error.

Completed historical files therefore total 30,980,043,942 bytes across 81
files. This excludes the separate growing-current-file pass. A proposed
calendar-stratified older tranche of at most 60 GiB was not run: the hit
redirected work to bounded context and episode classification. No further
broad scan is needed to answer whether a retained report exists.

The local search record identifies:

- `stg/node1/log.3:2590055`, `2022-10-28T13:28:16.420512+02:00`,
  kernel uptime `129.298213`, hard lockup on CPU 25.
- `stg/node1/log.3:2590091`, `2022-10-28T13:28:16.420575+02:00`,
  kernel uptime `129.298239`, hard lockup on CPU 33.

These are two detector reports in one multi-CPU episode, not two proven
recoveries. The context identifies livepatched runtime 5.10.147.8, preceding
page-fault/RCU diagnostics and a following new 5.10.149 boot. The next original
record after the final diagnostic is that new boot; no intervening host or
affected-CPU recovery is established. Collector timestamps compress buffered
kernel events, so kernel uptime supplies their relative timing. Do not
transfer the 2026 incident's configured panic policy to the 2022 boot without
historical evidence. There is no fresh same-CPU report supporting a rearm
claim, so old-version reset semantics are not needed for this bounded
classification. No false-positive, irreversible-stall or reset-cause
claim follows from the record. See [search output](cluster-hardlockup-legacy-search-output.txt),
[remaining-file results](cluster-hardlockup-legacy-remaining-search-output.txt)
and [history evidence](cluster-hardlockup-history.md).
The independent [episode analysis](hardlockup-episode-analysis.md) confirms
that neither same-boot operational continuation nor affected-CPU recovery is
established; recovery before reset remains unknown.

For each completed pass record the server/root, exact file manifest, snapshot
time or append cutoff, actual observed timestamp span, node coverage, search
patterns, scanned bytes/lines where available, output caps and exit status.
Rotation suffixes are not event dates. Preserve source file/line references
and timestamp offsets. An output cap must not silently turn an incomplete
search into a zero-result claim. Separate files discovered from files read.

Search broad enough to find the version-specific hard-lockup emission
strings supplied by the source owner, then validate each candidate against its
kernel source/context. Count hard-lockup detector reports separately from
soft lockups, RCU stalls, hung tasks, watchdog startup/configuration lines,
userspace quoted messages and unrelated watchdog device diagnostics.
Retain adjacent stacks and CPU headings only where needed to establish the
report and target CPU. Deduplicate replayed/forwarded copies before counting
distinct reports.

### Episode identity and evidence tiers

An episode record contains node, observed kernel/build, strongest available
boot identity, detector type, affected CPU, original record references,
first/last timestamps, duplicate disposition and the follow-up interval
actually inspected. Group records by node, boot and target CPU; keep a
concurrent multi-CPU incident relationship separately. A convenient time
bucket must not be treated as proof of a new episode or recovered interval.
The affected CPU can differ from the CPU printing another diagnostic.

| Claim | Minimum useful evidence | Limit |
| --- | --- | --- |
| Hard-lockup report observed | Valid detector emission and target CPU, with exact retained record | A detector threshold violation does not prove an irreversible hardware/kernel failure or a false positive. |
| Host operated after the report | Subsequent meaningful service/control traffic with identified chronology | Other CPUs can supply that traffic while the reported CPU remains stuck. Buffered forwarding must be distinguished from fresh activity. |
| Same-boot host continuation | Positive boot-ID or credible uninterrupted uptime/boot chronology spanning report and later activity | Same kernel version, same generation, or absence of a reboot line alone does not establish the same boot. State weaker evidence as such. |
| Affected CPU made progress | Fresh normal-context activity explicitly bound to that CPU, an explicit suitable recovery event, or a detector-rearm proof with reset alternatives excluded | A migratable task's later log, another CPU's output, or the original NMI stack does not prove resumed ordinary execution. Progress at one point does not establish complete workload recovery. |
| Sustained recovery | Affected-CPU progress plus same-boot continued relevant service activity over a stated observed interval | A finite interval cannot certify future stability. Recovery from a transient stall does not automatically mean the detection was false. |

The [source owner](hardlockup-recovery-semantics.md) establishes that in the
inspected .95/.113 detector the completed nonpanic warning path sets a
per-CPU warning flag, repeated stalled checks are suppressed, and observed
heartbeat advance clears that flag without a recovery log. The message
precedes diagnostic operations that can themselves wait; its presence does
not prove the reporting path finished or set the flag. Historical versions
need their own source check. Consequently, silence after
one report proves neither recovery nor continued stall. A later fresh warning
for the same CPU can support an intervening healthy check only after matching
the applicable source and excluding duplicated/replayed reports, a reboot,
CPU hotplug and watchdog reinitialization/other flag resets. If those
alternatives cannot be excluded, label it possible rearm, not proven recovery.
Keep the exact source proof in the semantics artifact.

### Acceptance and policy confidence

The final result must answer separately:

1. Does the inspected detector source allow an accepted hard-lockup report to
   return without forcing panic, and can later heartbeat progress clear it?
2. Were hard-lockup reports actually observed within the stated cluster-log
   coverage?
3. Which observed reports have host continuation, same-boot continuation or
   affected-CPU recovery evidence, and how strong is each classification?
4. What evidence remains missing before estimating the operational effect of
   enabling panic on these detections?

Source semantics indicate `hardlockup_panic=1` requests panic on the first
accepted report if the intervening diagnostic path completes, rather than
waiting for multiple reports to establish permanence. Therefore it can turn
a recoverable threshold-crossing stall into a forced crash; the setting is
not a guarantee that panic/crash transfer completes. Changing it after an
already warned episode does not retroactively panic suppressed repeats.
This is a mechanism-level tradeoff; source alone does not establish how
often that happens on this fleet. No hits in the bounded sample do not prove
that enabling panic is safe. Warning suppression, missing forwarding, uneven
retention and unknown monitored node-hours preclude deriving a fleet event
rate from raw log counts alone.

The conservative disposition pending actual recovery/frequency evidence is
to retain the current policy. This does not prove that `hardlockup_panic=0`
is optimal or identify node24's failure. Reconsideration needs a concrete
incident/capture benefit weighed against recoverable detections, or a
separately justified and authorized limited pilot with explicit success,
abort and rollback criteria. No automatic rollout, forced lockup or crash
test follows from this investigation.

The follow-up should finish with a bounded answer
even if CPU recovery cannot be proven from existing logs. Additional historical
coverage requires a useful, explicit budget; a lack of conclusive evidence is
not permission to scan the full corpus or induce a fault.

Quick checks consist of source-path consistency, completed-query coverage,
deduplication, boot/CPU attribution, timestamp/replay checks and artifact links.
No dynamic test or mandatory final review is triggered by this evidence-only
work. Persist findings under this follow-up scope and keep the session open.

Final disposition: the inspected detector permits nonfatal/recoverable reports
in principle. The completed approximately 35 GB log sample contains one
historical serious episode and no verified nonfatal recovery example.
It cannot estimate the recoverable fraction or certify either panic policy.
Retain the current policy pending a separately justified change; no further
collection, test, configuration action or review is required for this bounded
answer. See [the final synthesis](synthesis.md#earlier-cluster-follow-up-can-machines-survive-hard-lockup-detections).

## New follow-up: all retained node24 hard-lockup history

Status: complete, including final directory reconciliation and independent
local coverage verification. Explicitly requested by the user after the bounded
cluster sample: inventory and search **all retained node24 logs** for hard-lockup
reports and diagnostic mentions, then determine what each episode establishes
about survival. The previous 30 GiB cluster budget and stop-on-first-hit rule
do not limit this request. This is confined to node24; it does not reopen the
full cluster corpus or the original source audit.

The current session, both environment markers and the retained roster were
verified. Workspace session/documentation/verification guidance and the
existing source confidence boundaries remain applicable. The possible
node24-only panic pilot is a policy discussion, **not authorization to change
configuration**. No deployment, forced fault/crash, test, trust change or
lifecycle action is in scope.

| Owner | Artifact boundary | Acceptance |
| --- | --- | --- |
| implementer1 | `node24-hardlockup-history.md`, `node24-hardlockup-manifest.tsv`, `node24-hardlockup-search-output.txt` and compact raw excerpts; sole central collector | Account for every retained node24 file through the declared cutoff, including legacy/compressed sources if present. Preserve exact source references and completion/error status. Continue after hits until coverage is complete. |
| implementer2 | Separate local node24 episode-classification artifact | Use extracted records only; establish report identity, boot chronology, operational continuation, affected-CPU progress and reboot separately. No second remote scanner. |
| architect0 | This brief and follow-up synthesis | Accept coverage before any whole-corpus negative; reconcile episode evidence with applicable source semantics and distinguish findings from pilot authorization. |
| lead | Artifact naming/registration, resource coordination and policy conclusion | Resolve collection problems, accept results and keep state current. A source-owner follow-up is needed only if an actual historical candidate requires version-specific interpretation. |

### Full-retention coverage contract

Accepted inventory snapshot: epoch `1792523256`, 2026-10-20 21:07:36 CEST,
under `/var/log/remote/cz.vpsfree/nodes/prg/node24`. The manifest contains
**181 regular uncompressed files**, comprising 180 daily rotations and one
current log, totaling **89,603,613,857 bytes (83.450 GiB)**. Actual content
bounds are **2026-04-23 00:00:01.261611 CEST** through the current-file prefix
ending **2026-10-20 21:07:36.802428 CEST**. That prefix is **359,236,720 bytes**,
device 74/inode 204420, and ends with a complete newline. The largest file is
2,669,968,761 bytes. Every snapshot entry has now been searched in full through
its recorded cutoff.

Named-host/IP discovery under `/var/log/remote/` to depth six identified no
additional node24 alias path; the node24 directory has no nested, legacy,
compressed or nonregular entries, and the parent hierarchy has no symlink
alias. This bounds the discovered corpus without asserting that an undocumented
unrelated name cannot exist. See [the collector's inventory and limits](node24-hardlockup-history.md)
and [the exact snapshot manifest](node24-hardlockup-manifest.tsv).

The low-priority sequential pass completed in **402 seconds**, collecting
hard-lockup mentions and boot/version labels from the same bytes. Final results:
**181 unique completed files, 89,603,613,857 bytes, zero hard-lockup mentions
or detections**. All 19 matched records were boot/version labels. Five files
returned match status 0 and 176 returned no-match status 1; none had an error,
timeout, partial read, identity mismatch or changed rotation metadata.
Implementer2 independently reconciled all manifest/completion pairs and matches.

Post-inventory at 21:15:43 CEST retained the same 181 paths with no new/missing
entry and unchanged metadata for all 180 rotations. The current file retained
its device/inode and grew from 359,236,720 to 361,554,913 bytes. Its 2,318,193
post-cutoff append bytes are outside this search. The
[final receipt](node24-hardlockup-coverage-receipt.json) binds these results to
manifest SHA256 `caba1fe8496cf65f6230c07203ee1f8d146fe76b3f8c43ebcd017c993a138346`.
No episode-classification file is needed because no candidate episode exists.

The inventory must identify the node24 roots/aliases actually retained,
snapshot time, all file paths, format/compression, sizes and available date
bounds. Keep duplicate copies distinguishable from distinct source records.
Report actual retained intervals and gaps; rotation suffixes alone are not
event dates. No need to read unrelated hosts' contents to satisfy this scope.

Run one sequential, low-priority, interruptible scan. For growing files, record
a stable byte/record cutoff rather than chasing new appends indefinitely.
Track file identity/size sufficiently to detect rotation, replacement or
truncation during the pass; reconcile those changes against the snapshot
manifest. A partial final record or decompression failure is an explicit
coverage limit, not a clean negative. Preserve per-file result, completed
extent, exit status and any resumable position. Timeouts, read errors or
resource problems pause collection for resolution; they do not silently remove
files from the denominator. The final result may say “complete” only when all
manifest entries are accounted for through their cutoffs.

Use broad hard-lockup diagnostic matching, including historical prefixes and
spelling variants, and retain the exact expressions used. Capture **all**
matching reports/mentions with original file/line or stable record references;
do not truncate output and then claim a complete match list. Separate actual
kernel detector reports from boot capability, configuration, quoted text,
backtrace headings and other diagnostic mentions. Soft-lockup, RCU and
hung-task messages may supply episode context but are not hard-lockup events.
Compressed-file completion includes successful decompression, not just the
downstream match command's return status.

### Episode acceptance and conclusion

Apply the prior evidence tiers to each node24 episode: an observed detector
report, subsequent meaningful host operation, positive same-boot continuity,
progress of the named CPU, and sustained recovery are different claims.
Group duplicate/replayed lines and simultaneous CPU reports appropriately.
Use embedded kernel time where collector timestamps are batched. A following
boot is not survival of the old boot; lack of another warning is not recovery.

Do not project the modern .95/.113 state machine or current policy onto an
older kernel. Existing recovery-semantics work suffices unless a particular
candidate needs historical source checks, such as inferring rearm from a fresh
same-CPU report. Do not start a new source audit simply because old logs exist.

If the complete retained corpus has no validated reports, the conclusion is
**no forwarded hard-lockup detection found in the retained node24 logs through
the documented cutoff**. It is not proof that node24 never stalled, that
forwarding was complete, or that first-report panic would never sacrifice a
recoverable event. If reports exist, summarize recovery confidence for every
episode and distinguish the node24 result from the older staging-node example.

Full node24 retention improves the historical evidence for that host; it still
does not itself authorize or establish the safety/benefit of a panic pilot.
The earlier recommendation against blanket cluster enablement is not an
automatic rejection of a node24-only trial. If the complete search and local
coverage reconciliation find no detections, there is no recorded recoverable
node24 detection in this retained interval to serve as a historical
counterexample. A limited trial can then be more defensible than fleet-wide
enablement, with an explicit tradeoff: a first-report panic may improve
capture/recovery of a future persistent lockup, but can crash a future transient
one. Capture benefit still requires a detector report, completion of the
pre-panic diagnostics and a successful crash/capture path; the setting guarantees
none of those stages. The absence of historical reports cannot quantify the
remaining risk, and older workloads/kernel versions need not predict future
behavior. The final recommendation must use completed evidence, not interim
no-hit progress, and any actual setting change requires explicit user direction.

Conclude the search and classify available evidence without requiring induced
faults or a generic test. Session-artifact link/coverage/source-consistency
checks suffice for this evidence-only package; no automatic review is required.

Final disposition: no forwarded hard-lockup detection was found in this
retained node24 corpus, so it supplies no observed survived/recovered node24
event. A node24-only panic trial is a reasonable option to consider for future
capture, without implying zero risk, guaranteed capture or fleet-wide advice.
The original node24 cause remains unestablished. No change is authorized by
this search request. See [the completed node24 synthesis](synthesis.md#node24-complete-retained-log-result-and-policy).

## New follow-up: complete cluster history for three calendar months

Status: complete, including independent data reconciliation and final directory
metadata checks. Explicitly requested by the user: search all identified cluster
node directories for hard-lockup reports in the window beginning
**2026-07-20T00:00:00+02:00**, through the fixed collector upper boundary
**2026-10-20T23:08:52+02:00**. Every growing-file byte cutoff is preserved in
the manifest. The approximate request time of 23:05 CEST is not the cutoff.
Include both exact boundary instants. This is a
calendar-month interval, not an inferred rolling 90-day interval.

This supersedes the earlier cluster sample's 30 GiB budget and first-hit stop
for this requested window. All eligible records must be accounted for even
when detections are found. It does not authorize scanning unrelated older
contents beyond necessary boundary files, changing panic policy, sending
SysRq/NMI, connecting to consoles, altering hosts, or inducing faults. Earlier
completed findings retain their original scope and cutoffs.

Current session/environment and retained roster were verified before the
design update. Existing workspace documentation, session and verification
guidance remains applicable. Only this session's investigation artifacts may
be written; the lead owns state, portal registration and user communication.

| Owner | Work boundary | Acceptance |
| --- | --- | --- |
| implementer1 | Sole central inventory and low-priority sequential collection; window-specific manifest, matches, completion/error records and history summary | Inventory all identified node directories, including inactive nodes and known aliases; account for every eligible retained file/prefix, compressed or legacy if present. Continue after hits. Publish selected bytes and estimated duration before the pass. |
| implementer2 | Independent local coverage reconciliation and episode classification from collected artifacts | Match manifest entries to completed reads/reuse receipts, bytes, cutoffs and identity; classify in-window reports separately from mentions and duplicates; assess same-boot operation and affected-CPU progress without another remote scanner. |
| architect0 | This brief and final synthesis | Accept completeness and date filtering before a whole-window conclusion; preserve per-node retention gaps and evidence tiers; assess any proposed reuse. |
| lead | Assignments, resource coordination, progress updates and final acceptance | Maintain interruptible operation and approximately minute-spaced user updates; resolve errors or collector impact without silently shrinking the requested scope. |

### Inventory, window selection and resource limits

Accepted initial inventory contains 3,477 plain retained files across 26
identified node directories. The selected manifest contains **1,221 files,
557,248,915,782 bytes (approximately 519 GiB)**, from 13 active sources.
The other 13 directories' retained content ends before July 20 and supplies
no data in this window. Metadata endpoint timestamps parse and all selected
prefixes end at complete newlines; no compressed, symlink or unexpected entry
was found in the recorded discovery. Architecture's local metadata check
reproduced the selected count/bytes and endpoint-overlap set. Independent
local completeness checking remains implementer2's responsibility.

The [collector method](cluster-hardlockup-three-months.md),
[inventory](cluster-three-month-inventory.tsv) and
[selected manifest](cluster-three-month-manifest.tsv) retain per-file endpoint
and byte-identity metadata. Selection uses endpoint overlap plus a conservative
recent-modification-time fallback. All endpoints parse, with no observed
inversions/anomalies; this does not prove interior timestamp monotonicity.
Arbitrary future-dated interior records in excluded old rotations cannot be
ruled out without scanning all retention; preserve that explicit limit rather
than expanding this window search or claiming strict ordering. Any known
ambiguous or out-of-order boundary needs reconciliation, not silent exclusion. Some
current-file prefixes contain records fractionally later than the exact upper
instant (for example node24 ends at 23:08:52.564105). Reading them is allowed,
but classification must exclude matches later than **23:08:52.000000** and
retain their out-of-window disposition. A last record earlier than the upper
instant may simply reflect inactivity, not a missing read.

The collector chose fresh reads for every selected file, including node24;
no prior receipt was reused. The low-priority serial pass completed all
**1,221 files / 557,248,915,782 bytes** in **2,344 seconds (39m 04s)**.
One 30-second timeout on `brq/node5/log-20260820` was followed by a successful
full-file retry. All manifest extents have completed receipts; no read remains
partial or failed. The optimized prefilter uses case-insensitive literal
`lockup` plus three fixed boot/version labels, then applies the narrower hard
lockup expression, exact time window and report classification locally.
The literal includes concatenated and separated hard-lockup wording, plus
soft-lockup/configuration candidates; all such output remains uncapped with
source references. All **253 unique matches are in-window**: **96
`softlockup_panic` boot command-line records and 157 boot/version labels**.
There are **zero hard-lockup mentions or detector reports**. The broader
literal matches are configuration records, not observed soft-lockup events.
The collector additionally checked the full directory hierarchy for symlinks
and confirmed rsyslog's `%HOSTNAME%` routing template; no known relocated alias
was found. This supports source discovery without excluding undocumented names.

Independent local reconciliation accepted all file/byte/status/identity and
match accounting. The final inventory contains the same **3,477 paths**;
**3,464 fixed files** have unchanged metadata and all **13 current files**
retain identity. Their **263,131,061 post-snapshot append bytes** remain outside
the read extents. See [coverage receipt](cluster-three-month-coverage-receipt.json)
and [final metadata receipt](cluster-three-month-final-metadata-receipt.json).

Record the discovered roots/aliases and discovery limits, the fixed upper
timestamp with timezone, and all node directories regardless of whether any
in-window logs remain. For each node, report actual retained content bounds,
eligible file count/bytes, empty coverage and known gaps. An inactive node
whose retained logs end before July 20 contributes a retention gap, not a
negative detection result for the requested interval.

Select files by actual content timestamps. Rotation suffixes alone do not
establish overlap. Include boundary files and any file whose overlap cannot
be safely decided from metadata/boundary records; do not assume every file is
strictly timestamp-ordered when that assumption is unverified. Compression,
legacy naming, duplicates and known symlink/alias targets must be accounted
for. Keep discovery findings separate from searched content. An undocumented
unrelated alias cannot be excluded by a named-node search; state that limit.

The collector reports selected on-disk bytes, compression implications and a
duration estimate based on measured read throughput. Use one low-priority
sequential scanner, with interruptible per-file work and progress in completed
files/bytes. This is investigative log reading, not a build/test requiring a
verification watcher. Slow throughput or production impact calls for an
explicit pause/resume or adjusted pacing, not a parallel scanner or a partial
negative conclusion. Preserve exact completed and outstanding entries so a
pause does not require restarting the whole corpus.

Each source is bounded by its snapshot extent. Reconcile rotation, replacement,
truncation, rename and new paths against the manifest; later appends remain
outside the fixed cutoff. A new path containing pre-cutoff records needs
reconciliation rather than automatic exclusion. Read/decompression errors,
timeouts, partial records or lost snapshot data remain unresolved coverage
until repaired or explicitly reported as incomplete. Success of a downstream
grep cannot mask a failed source read/decompression stage.

### Reuse of the earlier node24 pass

Default to a fresh scan of eligible node24 files within the same new pass for
uniform provenance. The earlier complete receipt is useful corroboration but
does not automatically cover the new current-file tail or a later snapshot.
Reusing a previous immutable-file result is acceptable only with an explicit
per-file mapping to its successful exact-byte receipt, unchanged byte identity
with documented provenance, and an old search predicate covering the new one.
Record the old cutoff, identity evidence and zero-match/full-match result.
Filename, date, tree equality or equal file size alone is insufficient; a
manifest hash authenticates the manifest, not the file contents. If proving
byte equality requires rereading the file, scanning it afresh is simpler and
avoids the same I/O plus reuse bookkeeping. Do not re-query unrelated hosts
to support reuse. The lead accepts any concrete exception before it is counted
as completed coverage.

### Matches, episode grouping and completeness

Search broadly for historical hard-lockup wording and diagnostic mentions.
Retain all matching records with source positions, then classify genuine
kernel reports versus configuration/capability text, quoted messages and
other mentions. Keep exact predicates and untruncated match output. Boot
identity records may be collected in the same pass for chronology. Soft
lockups, RCU stalls and hung tasks can be context but are not hard-lockup
episodes by themselves.

Normalize each match's outer timestamp/offset to the defined window; retain
counts and source references for out-of-window boundary matches rather than
silently mixing them into the result. Unparseable or ambiguous timestamps
need explicit resolution and cannot be silently discarded. The window is
defined by retained record timestamps; buffered forwarding can differ from
actual execution time. Use embedded kernel uptime to order episode events
where available, without inventing their wall-clock time.

Apply the established tiers separately: report observed; meaningful host
operation; positive same-boot continuation; named-CPU normal progress;
sustained recovery. Deduplicate forwarded/replayed records, group concurrent
CPU reports into episodes with justified boot identity, and do not count an
NMI backtrace heading as another detector warning. A following boot does not
prove the old CPU recovered or could never recover. Do not apply modern
warning/reset semantics or current panic policy to historical kernels without
version-specific evidence. Source work is conditional on a real candidate
needing that interpretation, not a new general audit or fetch authorization.

Completion requires every eligible manifest extent to have a successful read
or accepted exact reuse receipt, no unexplained identity/path discrepancy,
and every match to have a window disposition and classification. Local
independent reconciliation must agree with file/byte totals and pending/error
lists. Report observed retention gaps separately from scan failures.

If no genuine reports are found, say **no forwarded hard-lockup detection was
found in the available retained cluster logs for the stated window and
coverage**. Do not say no machine stalled, every machine had three months of
logs, or panic would be safe. If reports exist, enumerate episodes and recovery
confidence without turning report counts into fleet frequency without a valid
observation denominator. No interim no-hit progress is a final negative.
The search itself authorizes no configuration or operational policy change.

Final acceptance: no forwarded hard-lockup detection was found in the available
retained cluster logs for the exact window and stated coverage. Thirteen
inactive-source retention gaps, endpoint-selection limits, forwarding losses
and undocumented-alias limits remain explicit. No recovered episode can be
classified because no candidate exists in-window. This does not establish
that a panic policy is risk-free or that node24's original hang was a hard
lockup. No further collection, source work or test is required for the requested
answer; no policy, host or lifecycle action was performed. See
[the final three-month synthesis](synthesis.md#cluster-complete-three-month-result).

## All-node hardlockup panic configuration

Superseded by the [move-policy brief](#move-panic-policy-to-vpsadminos).
The status and receipts in this section describe the earlier implementation.

Status: the one-line change is committed as
`8515b68288be7f6c78ed010f93d1424c377973fd` and published on the feature branch.
Effective all-node evaluation, quick checks, commit hooks and final independent
review passed. The required all-node system build was attempted and blocked by
the missing local initrd SSH key; no compilation or deployment occurred,
2026-10-21.
This is a new, explicit user policy decision following the completed
investigation; the negative log searches do not prove that enabling panic is
risk-free or identify node24's hang.

### Scope and implementation boundary

Affected repository: `vpsfree-cz-configuration`. The initial inspected base was
`86e19685313270d88e4db30038c056ce4b807abd`; it remains the historical design
reference. Upstream advanced during environment setup, and implementer0 rebased
onto **`d5c95e9315fb62cf38a172b303527c6553d752ba` before checks**. This is the
current implementation/evaluation base, not a claim that final verification has
completed. Implementer0 owns the source change, quick checks, commit and any
required corrections in its session worktree.
Add exactly one ordinary integer assignment to the existing
`boot.kernel.sysctl` attribute set in
`cluster/cz.vpsfree/nodes/common/all.nix`:

```nix
"kernel.hardlockup_panic" = 1;
```

Use the existing indentation and surrounding ordering, without `mkForce`,
per-host copies, input changes, kernel command-line changes or watchdog changes.
No separate repository documentation is needed for this single standard sysctl;
this brief records the policy rationale and rollout limits.

All 12 compute nodes import this module through their regional `common.nix`:
`brq/node5`, `brq/node6`, `pgnd/node1`, `prg/node19` through `prg/node25`,
`stg/node1`, and `stg/node2`. The thirteenth node, `prg/backuper2`, explicitly
shares the same policy through `common/storage.nix` → `common/all.nix`.
**Backuper2 is included.** It is a registered vpsAdminOS storage node, not an
unrelated machine. Implementer2 independently traced all 60 configuration roots:
exactly these 13 reach `common/all.nix`, matching the registered node set; no
non-node root reaches it. The lead accepted this scope. No existing assignment
to `hardlockup_panic` was found in the configuration source at the inspected
base. Implementer2 repeated the complete import/inventory check at `d5c95e93`:
the same 60 roots and exactly 13 node consumers remain, with no non-node
consumer and only the intended ordinary assignment in the proposed change.

The full ordinary confctl metadata inventory has 67 entries: these 60
`cz.vpsfree` local configuration roots plus seven `org.vpsadminos` entries.
Implementer2 checked that all seven are unmanaged NixOS metadata entries with
`managed = false`, no local configuration root and no import of this shared
node policy. They are not seven omitted node configurations.

The rebase incorporates upstream input updates: production vpsAdminOS remains
`2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`, staging moves from `f4bac6b4` to
`252b80dfdb4bced0713e8423ef7ba3d5600d05dd`, and both node Nixpkgs channels now
select `cd4ea8d57de16f4810bc5f14207bac45fbf19f67`. These are baseline changes,
not changes made by this sysctl package. All final check receipts must identify
the rebased inputs; the one-setting/no-input-change acceptance is relative to
`d5c95e93`, rather than the superseded initial base.

Effective-value evidence now binds that base to commit `8515b682` in
[hardlockup-verification.json](hardlockup-verification.json). The successful
[full-module receipt](hardlockup-effective.json) reports integer `1` and the
generated sysctl assignment for all 13 exact registered nodes, and absence of
the assignment in two evaluated non-node controls. The helper uses the pinned
confctl `evalConfigFor`; receipt inputs match the current lock. Implementer2
independently reconciled the raw output, JSON, inventory, import scope and
source assignment. Evaluation was performed before commit against the same
source blob recorded in that commit. This establishes effective configuration,
not a build result or a changed runtime value. The initial helper invocation
error was corrected before the successful receipt; no source workaround or
input change was required. Commit hooks passed, with a non-blocking message
width warning recorded in [the hook log](hardlockup-commit.log).

[Final independent review](hardlockup-final-review.md) accepted this exact
base/head range across all four assigned lanes with no findings. The reviewer
confirmed the complete one-commit history, empty migration lineage, effective
13-node scope and absence of repeated dependency/update streams. Publication,
quick checks and provenance are recorded in
[hardlockup-verification.md](hardlockup-verification.md).

The post-review watcher attempted a dry-run of the 13 nodes' real confctl
`toplevel` and `autoRollback` outputs. Top-level evaluation failed because
`/secrets/nodes/initrd/ssh_host_ed25519_key` is absent in this environment;
it did not reach substitution planning or compilation. See the
[watcher result](hardlockup-dry-run-watcher-report.txt) and
[command receipt](hardlockup-build-dry-run-result.json).

The required actual build was then attempted through a fresh watcher using
`nix develop -c confctl build --yes 'cz.vpsfree/nodes/*'` at unchanged commit
`8515b682`. It selected all 13 nodes and 26 outputs, then exited `1` after
58.12 seconds while evaluating node5.brq because the same initrd Ed25519 key
was absent. It did not reach substitution planning or compilation; no operation
remains active. The [actual build log](hardlockup-build.log) and
[exit/elapsed receipt](hardlockup-build-watch-result.json) record this attempt.
Consequently successful system builds and cache availability remain
**unverified**, despite successful effective-option evaluation and accepted
review. There is no pending build invocation or further workaround in this
handoff. No secret provisioning, placeholder key, source workaround or
production access is authorized to bypass this environment limitation.
No further source edit or review is needed absent a new substantive change.
Neither publication nor review authorizes integration or deployment, and
runtime settings remain unchanged by this work.

Architect0 owns this brief; implementer2 owns independent local corroboration
of the import/override boundary and implementation receipts. The lead owns
repository/worktree coordination, tracking, publication and final-review
assignment. Do not add another source writer or remote investigation package.

### Behavior, compatibility, activation and recovery

The intended effective value is integer `1` for all 13 nodes. An accepted
hard-lockup detection can then invoke Linux panic; it need not wait for repeated
reports. This changes failure policy, not detection coverage or the underlying
hang. Panic, successful crash-kernel entry, capture and upload are distinct;
none is guaranteed by this assignment. The existing detector enablement,
threshold, soft-lockup policy and crashdump configuration remain unchanged.

There is no persisted-state, database, API, protocol or format migration and
no dependency/input change. Old and new node configurations can coexist; no
coordinated update of all running nodes is required. The sysctl is an existing
Linux interface used by the investigated kernels. Future application to an
unexpected kernel lacking the interface must be reported, not hidden with
additional compatibility code.

Source changes, evaluation, builds and publication do not change a running
node. The pinned production OS `2abbe3cc` explicitly applies sysctl files with
`sysctl -w --system` during runit stage 1
(`os/modules/config/runit.nix:20–26`). The current staging pin `252b80df` has
no delta from the initially inspected `f4bac6b4` in that file,
`os/modules/system/activation/switch-to-configuration.rb`, or the NixOS module
import list. The startup/activation conclusion therefore retains that source
basis after rebase; final effective-value evaluation still uses the new pinned
module graph. Thus booting an appropriately prepared configuration
applies the setting during startup, not before that startup step. Do not promise
that merely updating a PXE image or running an ordinary live switch updates the
current kernel value: the inspected switch code does not explicitly rerun
stage 1. A later authorized rollout must verify the actual runtime value and
its application method. No deploy, dry-activate, live sysctl write, reboot,
SysRq, NMI, forced lockup or crash test is authorized here.

Source rollback is a revert of this one assignment. Removing a sysctl from
configuration does not itself reset an already-applied live value. A future
authorized runtime rollback must explicitly restore `0` by its approved
application method, or boot the prior configuration whose applicable kernel
default is `0`, and verify the resulting value. No data rollback is involved.

### Acceptance and verification

1. Preserve the exact source base/head and show a one-file, one-setting diff;
   inputs, generated files and unrelated machines must remain unchanged.
2. Run syntax/format and whitespace checks in the repository's declared Nix
   environment. Evaluate the actual pinned module graph for every registered
   node and record all 13 names with effective
   `boot.kernel.sysctl."kernel.hardlockup_panic" == 1`; inspect generated sysctl
   text where available. Use a session-owned evaluation helper if confctl does
   not export the effective option directly. A grep or a reduced fragment-only
   evaluation is useful corroboration, not complete effective-value proof.
   Record the pinned inputs and any evaluation limitation instead of silently
   substituting inputs or changing the configuration to make a check pass.
3. Corroborate the import boundary against the complete registered inventory
   and scan for overrides; implementer2 independently checks these receipts.
   No non-node consumer should acquire the setting through this edit.
4. Commit the intended change after quick checks. The substantive configuration
   deliverable now requires final independent review under the mandatory review
   skill, including the complete base-to-head history and no-migration finding.
   Earlier investigation-only review exemptions do not apply to this change.
5. The lead corrected the initial evaluation-only verification scope: repository
   `AGENTS.md` requires `confctl build` for touched nodes. After final review,
   run the required all-node builds through a fresh Luna/low verification
   watcher under the monitor skill. No deployment or dry activation. Stop an
   unexpected local kernel build and investigate the missing substitution under
   the verification procedure; this sysctl edit intentionally changes neither
   kernel sources nor kernel build configuration. Report build/input failures
   precisely; do not claim completed checks from evaluation alone.

No dedicated behavioral test or induced failure is justified for this setting.
Implementation, quick evaluation, independent review and required builds are
separate acceptance stages; live activation remains unperformed and requires
separate authorization. Publication does not authorize default-branch integration.

## Move panic policy to vpsAdminOS

Current status, 2026-10-22: OS commit
`b81c43ff6865a033268072f55cd94ad763d0630b` on base `252b80df` implements the
one-file parameter/description change. Actual enabled/disabled/override module
evaluation, formatting, parsing and hooks passed. The latest
[implementation packet](os-hardlockup-verification.md) records verified SSH
publication; staging remains unchanged. [Final review](os-hardlockup-final-review.md)
accepted source and configuration withdrawal. Its one Important finding was
resolved by adding validation prose to the commit message: predecessor
`f3e91f62` and final `b81c43ff` have identical tree
`3585d2ce3669cddcc689522072f22802cb2fa8c3`, module blob and parent. The lead
verified the direct fix and passing hooks under review step 9; no source
re-review is required. Automatic CI for final head, run `39600028637`, is
terminal **completed/failure**, updated `2026-10-22T01:11:10Z`. All 11 jobs
finished: ten succeeded (OS build/cache and all nine livepatch jobs, including
the final AMD fresh run), and the product-test job failed with 124 tests
passed and five failed. The [final metadata](os-hardlockup-ci-new-result.json)
binds these results to exact head `b81c43ff`. The watcher ended; no CI observer
remains active. The accepted
[failure analysis](os-hardlockup-ci-failure-analysis.md) ties all five first
errors to retained-impermanent `boot_dataset` mismatches after a live userspace
switch. Kernel, boot ID, booted system and container init identity remained
unchanged, so these paths did not execute the new boot argument. This supports
no panic-policy edit or blind rerun. Exact runtime-YAML/mount root cause remains
unresolved; no baseline reproduction, harmlessness or data-loss claim is made.
Source acceptance stands, while CI is failed and cannot be called green.
No extra source audit, test, observer or local long check is selected.

Configuration withdrawal is complete and published: feature base equals head
`37a338b25192d9271ee211110800c2dc6a094a57`, with zero feature commits/diff;
master was unchanged and the branch retained. The obsolete `8515b682` is no
longer the proposed configuration result. See
[withdrawal evidence](hardlockup-configuration-withdrawal.md). No downstream
pin, runtime setting, deployment or integration changed.

The following accepted brief records package boundaries and acceptance.
The user's instruction to handle hard lockups like soft lockups explicitly
broadens scope from the 13 site nodes to
**every vpsAdminOS configuration with `boot.crashDump.enable = true`**.

- **Implementer2, vpsadminos:** use registered staging base
  `252b80dfdb4bced0713e8423ef7ba3d5600d05dd`. Edit only
  `os/modules/misc/crashdump.nix`: add `"nmi_watchdog=panic"` beside
  `"softlockup_panic=1"` in the existing `boot.kernelParams` list inside
  `config = mkIf cfg.enable`. Update the nearby `boot.crashDump.enable`
  description to say that it enables panic on soft and hard lockups, replacing
  the inaccurate claim that it activates the NMI watchdog. No new option,
  global sysctl, detector enable/disable bit, threshold or unrelated change.
- **Implementer0, configuration withdrawal:** the published feature commit
  `8515b68288be7f6c78ed010f93d1424c377973fd` is unmerged and superseded.
  Preflight established a clean owned worktree, only owned containing refs,
  no default-branch assignment, and no known deployed/supported consumer.
  Withdraw it by the planned empty-range rebase onto current master
  `37a338b25192d9271ee211110800c2dc6a094a57`, dropping `8515b682` from the
  feature series, then publish with an exact lease against the old remote
  feature head. Preserve the branch and original receipts; verify zero final
  feature diff/commits and remote head. Do not retain an add/remove commit pair,
  reset/clean/stash, delete refs, rewrite master, change pins or rerun builds
  of the now-withdrawn configuration change. Stop if preflight facts change.

The two packages have independent repository/file boundaries. Architect0 owns
this brief; the lead owns acceptance, review and tracking.
Use plain session Markdown for concise check results, not a new evidence system.

Linux's valid hard-panic boot parameter is `nmi_watchdog=panic`, not
`hardlockup_panic=1`. At incident Linux `1dfea587`,
`kernel/watchdog.c:80–104` parses `panic` by setting `hardlockup_panic = 1`;
separate `0`/`1` tokens control detector enablement. The chosen token leaves
detector enablement unchanged. The OS gate and list-merge behavior match soft
panic exactly. With crashdump disabled this module adds neither panic token.

Override semantics remain native: a later `nmi_watchdog=nopanic` token can
clear the hard-panic flag; Nix list ordering (`mkAfter`) determines that order,
and `mkForce` can replace the entire parameter list. A configured or manual
runtime `kernel.hardlockup_panic=0` can override the boot value until next boot.
No override or runtime write is added by this task. The existing crash-kernel
parameter construction forwards normal parameters except `crashkernel=` and
appends `boot.crashDump.kernelParams`; leave that behavior unchanged, as for
soft panic.

Acceptance: evaluate the real OS module graph with crashdump enabled and
disabled; enabled must include each panic token once and disabled must gain
neither from this module. Check ordinary `mkAfter [ "nmi_watchdog=nopanic" ]`
ordering, unchanged detector tokens and absence of a new sysctl assignment.
Run format, parse, whitespace and declared hooks in `nix develop`; record exact
base/head, commit one coherent change, publish and obtain final independent
review of the OS change plus configuration withdrawal/history. The old review
of the site sysctl does not certify this replacement. No new VM/fault test,
induced lockup, crash test or local kernel build is needed for this bounded
module change. No further long check is selected absent a concrete evaluation
failure or review finding; any subsequently required long check uses the
verification watcher policy.

There are no data, schema, API, protocol or migration changes. Mixed old/new
systems remain compatible and need no coordinated fleet update. No downstream
pin bump is needed: current configurations retain their existing OS revisions
until a normal separately authorized update. The changed policy applies when a
system containing it boots; a live configuration switch does not replay boot
arguments. It can panic on a recoverable detection and cannot guarantee crash
capture. Reverting the OS addition and booting the prior applicable policy
restores the prior boot behavior; any immediate runtime override is a separate
authorized operation. No merge, deployment, host mutation or lifecycle action
is part of these packages.

## Runtime hard-lockup policy supplement

Superseded by the user's [declaration-only correction](#declaration-only-hard-and-soft-panic-policy).
The hook design, implementation and review below are historical, not remaining
requirements.

Historical v2 checkpoint, 2026-10-22: implementation was committed and published as
`14cdf1caec606bb6bc88fcb32ac48f707f5dabb0` on base
`55c5046514d06fe9398a022c1622bdaae5228841`, consolidated into one v2 policy
commit. The pre-publication rebase from `10f31e04` preserved the exact policy
patch and module blob; checks were repeated against the refreshed upstream
inputs. The single module file has 19 insertions
and one deletion. Real enabled/disabled/zero/null/false evaluations, generated
activation ordering and dry-script checks, isolated mock success/failure checks
of exact sysctl arguments, format/parse and hooks all passed. No real host
activation or sysctl invocation was executed. [The verification packet](os-hardlockup-verification.md)
links those results. [Final runtime review](os-hardlockup-runtime-final-review.md)
accepted all four lanes with no remaining findings, including verification of
the corrected lifecycle-note pin label. The feature is clean and published;
staging was unchanged by publication. CI run `39744127896` and RSpec run
`39744127815` were pending at that historical checkpoint; this is not a current
watcher-status claim. Earlier
`b81c43ff` review/CI remains historical and does not certify this revision.
No downstream pin, merge, deployment or host runtime change occurred.

The accepted brief follows; it supersedes the boot-only completion claim for
`b81c43ff`. Changes stay within `os/modules/misc/crashdump.nix`: retain both boot
arguments, add the nearby
comment `# Panic on hard lockups detected by the NMI watchdog.` immediately
above `"nmi_watchdog=panic"`, and declare
`boot.kernel.sysctl."kernel.hardlockup_panic" = 1` inside the existing
`config = mkIf cfg.enable` boundary. Keep detector flags and thresholds unchanged.
Use an ordinary sysctl assignment with normal Nix override semantics.

The requested new runtime behavior is hard-lockup panic. Do not add a soft
runtime assignment solely for stylistic symmetry: existing soft boot policy
stays unchanged unless the lead confirms that the user's plural wording covers
both. No global sysctl policy, site assignment, input update or new option.

The completed [runtime sysctl lifecycle trace](hardlockup-sysctl-lifecycle.md)
records exact standalone/site pins, boot versus switch behavior, inert systemd
declarations, runit one-shot limits and the activation-status caveat. It
corroborates this design; it does not certify later implementation edits.

**Selected live-switch contract:** add a narrowly named
`system.activationScripts.crashdumpHardlockupPanic` entry within the same
crashdump-enable gate in `crashdump.nix`, dependent on `specialfs`, with
`supportsDryActivation = false`. Implementer0's source trace confirms that
stage-1 `sysctl --system` runs only at boot; the imported systemd sysctl unit
does not run under runit, and `switch`/`test` invokes the existing activation
script. The existing kernel-modprobe activation fragment demonstrates the
`specialfs` dependency. No service, general sysctl replay or framework is needed.

The snippet invokes the explicit `${pkgs.procps}/bin/sysctl` path for only
`kernel.hardlockup_panic`, using its **final merged configuration value**.
Honor an explicit override to `0`; if the merged value is null, omit the write.
Encode values as the existing sysctl module does (`false` becomes `0`, otherwise
`toString`) and shell-escape the complete assignment. Do not hardcode `1` in
the application command. A missing interface or write failure must emit a clear
diagnostic to stderr and leave a nonzero snippet status; do not swallow it or
silently skip a missing proc path. Use the existing activation error handling,
without exiting the activation script early or modifying the generic switcher.
The current Ruby switcher does not enforce the return value from `OUT/activate`;
therefore a switch exit code alone must not be claimed as proof of application.
Future authorized rollout must verify the sysctl value directly.

Activation runs before changed runit services are restarted, so this write can
precede crash-image loading/reloading. It does not prove that a usable crash
image exists. The lead accepted this narrow boundary. Implementer2 owns this
additional snippet and option-description update; implementer0 corroborates
exact generator/dependency/error references. No further source investigation is
required before implementation.

Checks: evaluate real enabled/disabled module configurations, requiring hard
sysctl integer `1` and generated text only when crashdump is enabled, unchanged
boot arguments except the documented comment, and explicit site override to `0`
using the normal override mechanism. Once the live-switch contract is selected,
check its generated command, dependencies, `switch`/`test` invocation and dry
activation behavior without writing host sysctls. A missing kernel interface or
failed write must be reported according to that mechanism, not silently treated
as successful application. Disabled crashdump must not gain an activation write.
Format/parse/whitespace/hooks and final reviewer0 acceptance apply to the new
committed revision; old accepted source/CI do not certify changed runtime code.

Consolidate this refinement into the existing unmerged OS policy owner after
fresh upstream/provenance checks; preserve historical heads and receipts, and
publish the final feature head with the appropriate lease. Configuration
withdrawal remains complete. No new persistent state, API, protocol, migration
or coordinated fleet update is needed. Current downstream pins stay unchanged.
If later deployed, a successful live application should take effect without a
reboot; it still does not enable an inactive detector or guarantee a dump.
Removing the assignment or disabling crashdump does not by itself restore an
already-applied `1`: future authorized rollback must set/verify `0` or boot the
prior applicable policy. No live write, deploy, merge, induced failure or
impermanence repair is authorized; existing CI dataset-failure analysis remains
separate. The lead owns the pending activation decision and any longer check.

## Declaration-only hard and soft panic policy

Accepted user correction, 2026-10-22: “just set kernel.sysctl, do it also for
softlockup.” This explicitly replaces the automatic live-application requirement
and rejects the additional activation mechanism in this policy package.

Current status: final v3 **`8528262315b0794a8f50917cf33c53a07fd14030`** on base
`55c5046514d06fe9398a022c1622bdaae5228841` is clean and SSH-published as one
coherent commit. [Final v3 review](os-hardlockup-v3-final-review.md) accepted
all four lanes with no findings. Enabled/disabled, paired zero/null override,
generated sysctl and no-hook checks passed, along with formatting, parsing and
normal hooks; see [verification evidence](os-hardlockup-verification.md).
Exact-head CI is pending under implementer2's existing watcher. This revision
supersedes the targeted-hook head `14cdf1ca`; its review and CI are historical.
The separately [approved generic service](#approved-generic-sysctl-service)
is now authorized for implementation and leaves these declarations unchanged.
No merge, pin update, deployment or host write occurred.

Within `os/modules/misc/crashdump.nix`, retain the existing crashdump-enable
gate, both boot arguments and the comment explaining `nmi_watchdog=panic`.
Declare both `boot.kernel.sysctl."kernel.hardlockup_panic" = 1` and
`boot.kernel.sysctl."kernel.softlockup_panic" = 1` under that same gate. Remove
the targeted activation snippet, its value helper and description claims of
automatic application during activation. Use ordinary assignments with normal
overrides; add no service, framework, global sysctl replay or other mechanism.

The chosen boundary is generated configuration plus the retained boot policy.
NixOS normally reapplies changed sysctl configuration through
`systemd-sysctl` restart triggers. vpsAdminOS uses runit; the existing sysctl
application is boot-stage-only, and the imported systemd declaration does not
automatically apply these values on a live switch. **This remaining distinction
is the user's explicit choice, not an unresolved implementation requirement.**
Do not claim automatic live application or silently reintroduce it.

Quick checks cover real enabled/disabled module output, both generated sysctl
assignments, explicit zero overrides and null omission, unchanged boot arguments
and NMI comment, and absence of the removed hook from normal/dry activation
scripts. Format/parse/whitespace and normal commit hooks apply. Consolidate the
change into the single unmerged policy owner with truthful version/validation
history; prior hook review and CI are historical. Reviewer0 completed the
required review of the final v3 range, as linked above. No new behavioral test
or observer is selected by this brief.

All crashdump-enabled vpsAdminOS consumers are in scope; disabled configurations
gain neither declaration from this module. No site input/pin, data/API/protocol
or migration changes are required, and mixed versions need no coordinated
fleet update. Removing/nulling a declaration does not reset an already applied
live value; an explicit later runtime rollback is separate authorization.
No source edits by architect, no impermanence repair, host write, merge,
deployment or lifecycle action. Earlier incident findings remain unchanged.

## Proposal: generic sysctl application on switch

**Superseded historical proposal.** The user's subsequently approved
[normal runit service](#approved-generic-sysctl-service) is authoritative.
The direct switch step and synchronous failure propagation below will not be
implemented. Both this proposal and its earlier service alternative are kept
only as decision history.

Earlier recommendation: a direct checked switch step, not a new service.
The user's requested contract is applying sysctl changes on configuration
switch, so the following smaller design supersedes the preliminary service
recommendation retained below. Proposal only; implementation awaits acceptance.

1. Generate a small `${pkgs.procps}/bin/sysctl -w --system` helper in the new
   system closure, exposed as `$out/bin/apply-sysctl` by
   `os/modules/system/activation/top-level.nix`. Use the new closure's explicit
   procps path and installed `/etc`; no dependency on the old system's PATH.
2. In `switch-to-configuration.rb`, invoke it on **every real `test` or `switch`**
   immediately after successful activation installs new `/etc`, before changed
   services restart. Check activation success and the helper result explicitly.
   Skip the command for `dry-activate` and `boot` alone. Leave the existing
   stage-1 sysctl application and its early-boot ordering unchanged. No service,
   markers, retry loop, runlevel change or trigger registry is required.
3. Apply the existing complete `--system` input set and precedence, including
   generated `60-nixos.conf`, other sysctl.d files and local `sysctl.conf`.
   Reapply unchanged declared settings as part of each real switch; this also
   overwrites manual runtime overrides when configuration specifies a value.
   Choosing every switch avoids unreliable partial change detection. Removed
   keys remain untouched; absent kernel keys or invalid values retain procps'
   diagnostics/failure semantics without a blanket error-suppression flag.
4. Report application failures and return a nonzero overall switch result;
   partial writes are not rolled back automatically. Changed services have
   already been stopped by this point: on a sysctl failure, retain the error,
   complete the existing service restart steps, then return failure rather than
   stranding those services with an immediate exception. A failed activation
   must prevent sysctl application against an uncertain `/etc`. Do not globally
   rewrite unrelated service error handling. A future rollback applies the old
   generation's configured values but cannot infer resets for removed keys.

Implementation boundaries, if accepted: helper generation in `top-level.nix`,
the existing Ruby switch/test path, focused Ruby switch specs and a small
disposable switch integration case. Keep this generic behavior as its own
logical commit, independent of the panic declarations. Quick checks must prove
call ordering, explicit new helper path, actual/dry/boot distinctions, successful
activation gating, failure propagation after service recovery, and no trigger
state. Later integration uses benign sysctls to verify live apply and rollback;
no host writes, induced lockups or new tests are authorized by this proposal.

Source basis is the same `55c50465`/`14cdf1ca` lifecycle inspected below and the
[independent source-contract note](generic-sysctl-contract.md). Existing
`Configuration#test` already has the required post-activation/pre-restart point;
`#switch` delegates to it, and the system builder already installs commands in
`$out/bin`. This is a targeted contract addition, not a framework. The service
alternative below is relevant only if a separate changed-input/status contract
is explicitly requested later; its markers/retries and duplicate boot apply
are not needed for this recommendation.

### Superseded service alternative

The final [generic source-contract note](generic-sysctl-contract.md) corroborates
the service, marker, retry and switch-status constraints below. This proposal
chooses changed-input application with separately observable service status.
If the desired contract is instead synchronous application on **every**
`switch`/`test`, a checked generic step immediately after successful activation
in the existing switcher is the smaller state model: no service marker, trigger
or extra boot-time application. It would require checking activation success
and propagating the sysctl command's failure, and would replay unchanged policy
on every switch. Present that as a concrete alternative, not an automatic
extension of the recommended service. Default/rescue service membership also
does not silently cover arbitrary custom runlevels.

Earlier proposal, 2026-10-22; no generic implementation is authorized.
Considered a generic **runit one-shot `sysctl` service**, independent of crashdump,
that applies configuration through the existing procps `sysctl --system`
semantics and restarts when managed sysctl input files change. This mirrors
NixOS's service/trigger model without introducing a daemon, polling loop or
crashdump-specific hook.

### Smallest useful implementation boundary, if accepted

- Add `os/modules/config/sysctl.nix` and register it in the OS module list.
  Reuse the existing generated `environment.etc."sysctl.d/60-nixos.conf".source`;
  do not create another renderer or modify Nixpkgs. Set `oneShot = true`,
  `onChange = "restart"`, and `restartTriggers` to the managed sysctl inputs.
  Include the canonical 60 file and other declared `environment.etc` sysctl.d
  files or `sysctl.conf` using a deterministic name/source list. Source paths
  make generated content changes affect triggers without building files during
  evaluation. Include both default and rescue runlevels, matching kernel modules.
- Read the newly installed `/etc` through explicit `${pkgs.procps}/bin/sysctl
  --system`, preserving current boot-time file precedence and diagnostics.
  Apply after `/etc` activation through the existing changed-service restart
  path. Kernel-module reloads precede changed-service starts, which also helps
  when a setting belongs to a newly loaded module. The command may partially
  apply values before reporting failure; it is not a transaction.
- Use a small service-local success record tied to the current managed-input
  identity and a custom `check` that validates that identity. Clear the old
  record before each attempt, publish it only after successful application,
  and explicitly exit nonzero on failure before the generic one-shot wrapper
  can append `done`. Do not rely on the default unversioned `done` file.
  The custom check must reject an older configuration before the new run body
  even starts; clearing a plain `done` only inside `run` has a race. Explicit
  restarts of the same configuration must invalidate their previous success
  before readiness is checked. Do not `exec sysctl`: that would bypass the
  one-shot footer. Recommend **one attempt per start/configuration change**,
  leaving permanent-key failures failed until explicit retry or another change;
  arrange the existing `sv once` behavior before the application so early exit
  does not trigger runsv's default indefinite one-second retries. Verify this
  bounded stop/retry behavior and readiness race before acceptance. Failure
  remains visible in logs/check status; no polling/retry framework is introduced.
  This is one service status marker, not a state system.
- Keep `os/modules/config/runit.nix` stage-1 application in its current place
  after boot module loading. Moving it to normal runit services would delay
  early-boot policy relative to networking and other setup. The new service
  may apply the same managed policy again when normal/rescue services start;
  document that deliberate repetition and verify it, rather than adding
  boot-only marker plumbing in this first change.

Trigger scope is managed configuration, not arbitrary edits to a running host.
Files outside the declared input set keep `sysctl --system` precedence when
the service runs, but editing such an unmanaged file alone is not detected.
There is no filesystem watcher. Package/vendor sysctl changes need to enter
the managed source list if they are expected to trigger application; do not
promise coverage from only the 60-file trigger. Deleting/nulling a key omits
it from later writes and **does not reset its live value**.

### Existing switch contract and choice

`switch` and `test` stop changed services, install the new `/etc` via activation,
then start changed services. The plain `boot` action only prepares bootloader
state; `dry-activate` must print the intended service action without running it.
First introduction of a new service is started asynchronously by runit, unlike
the explicit restart of an existing changed service. The current switcher
ignores activation and service subprocess return values. Therefore this minimal
proposal means **automatic application with independently observable service
success/failure**, not that successful switch exit proves every sysctl applied.

Recommended initial acceptance preserves that existing contract and requires
service check plus selected sysctl readback for a later authorized rollout.
If the user instead requires `confctl`/switch failure whenever sysctl application
fails, explicitly add a bounded synchronous check for this service, including
first introduction, and propagate that check's failure. That is an additional
switcher contract change requiring its own review/tests; do not silently change
error handling for every service. A generic activation fragment would be fewer
lines but would replay on every activation, run before current module reloads,
and still suffer ignored child status; the service better fits change-triggered
application and operator-visible status.

### Source basis, ownership and verification

Source basis: OS staging base `55c5046514d06fe9398a022c1622bdaae5228841` with
root Nixpkgs `da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36`; source contract was
read at runtime-policy head `14cdf1ca` before declaration-only cleanup. The
root/site predecessor uses `cd4ea8d5`; nested impermanence `e4bae1bd` is not the
OS root input. Existing site pins remain unchanged. The
[lifecycle trace](hardlockup-sysctl-lifecycle.md) gives earlier exact references;
the current read confirms `switch-to-configuration.rb:75–121,185–318` and runit
`default.nix:283–313` retain these activation, trigger and marker semantics.
Implementer0 independently corroborated this contract without executing it.

If accepted, this generic behavior is a **separate logical commit/package**
from the panic-policy declarations. Proposed owned files: the new sysctl module,
module-list registration, focused existing switch/service tests and a short
module/operations explanation of application and rollback. No required edit to
crashdump or kernel sources; no pin update, fleet coordination or data/API/schema
migration. A rollback re-applies values present in the old configuration; it
does not undo removed keys or partial earlier writes automatically.

Quick acceptance: evaluate actual input lists/triggers, changed versus unchanged
selection, normal/rescue participation and dry behavior. Use an isolated mock
for exact command/path, success, missing/invalid key failure, stale-marker
rejection, changed configuration and rollback identity. After committed review,
run one focused disposable switch integration covering new-service first
introduction, existing-service restart, unchanged no-reapply, new `/etc` values,
failure reporting and rollback using benign writable sysctls. Never induce a
lockup or write host sysctls. Long verification would use the normal watcher
policy only after implementation is authorized; no test or observer is launched
for this proposal. No merge, deployment or lifecycle action is authorized.
