# CI duration: exact source budgets and observed critical path

Implementer1, 2026-10-22. Source is exact merged vpsAdminOS
`846bb469505789ba0b2a405fa5905ba6d8253006`. Session identity/environment and
retained roster were verified; workspace procedures and repository AGENTS were
read. This package uses local source/history and implementer2's saved current
receipt only. No current API query, extra observer, test, evaluation, build,
retry, cancellation, source/ref change, host configuration write or lifecycle
action was performed. Implementer0 owns historical timing collection;
implementer2 retains the existing 600-second current observer.

**The observed nine-hour workflow age is chiefly the serialized AMD job
schedule, with two deliberately four-hour aging workloads, rather than one
test running for nine hours.** At the fixed receipt time below, the active
job had run 4h37m59s and had not exceeded the matched historical successful
duration or its configured timeout. Its inner phase/progress was unavailable,
so no current inner-loop hang or runtime regression is established.

## Fixed current receipt and elapsed accounting (UTC)

Sole-observer capture: **2026-10-22T20:32:55–20:32:57Z**. Saved
[run metadata](generic-sysctl-ci-39767770407-duration-run.json) and
[all 11 job records](generic-sysctl-ci-39767770407-duration-jobs.json) bind run
`39767770407`, attempt 1, push event and exact head above. Overall API status
was `queued`, conclusion null, despite an actually running job. Do not derive
active runtime from that overall field or the queued jobs' placeholder starts.

| Critical-path segment | UTC interval | Duration |
| --- | --- | ---: |
| Initial build allocation wait | 11:03:56–11:04:51 | 55s |
| Build/cache job, runner1 | 11:04:51–11:18:07 | 13m16s |
| AMD aged-v6, runner4 | 11:18:09–15:42:18 | 4h24m09s, failed |
| AMD low-memory-v5, runner4 | 15:42:20–15:48:38 | 6m18s, passed |
| AMD low-memory-v6, runner4 | 15:48:40–15:54:57 | 6m17s, passed |
| AMD aged-v5, runner4 | 15:54:58–20:32:57 snapshot | at least 4h37m59s, active |

The gaps between the AMD rows and after build total 7 seconds. All four AMD
rows used runner ID 11199, `gh-runner4.int.vpsadminos.org`. This is positive
evidence of serialized allocation in this run; it does not prove the runner
group has only one eligible machine. The active v5 job was created at build
completion, 11:18:07Z, then waited **4h36m51s** before actual start. Thus:

```text
55s initial wait + 796s build + 16,611s v5 pre-start wait
  + 16,679s active v5 job = 34,141s = 9h29m01s workflow wall age.
```

The active `Run livepatch lifecycle tests` step started 15:55:02Z and had run
**4h37m55s / 16,675s**, four seconds less than its job. There is no current
inner-log progress receipt, so the step could include fixture builds, image
preparation, guest setup, aging, transitions, checks or guest teardown.

`amd-fresh` job `119793311399` and `amd` job `119793311543` were explicitly
**queued**, runner ID 0/name empty, with no steps. Their queue age since
11:18:07Z was **9h14m50s**. Their `started_at == created_at` is not evidence
of execution. Native tests and all Intel jobs were finished and have no DAG
edge blocking those AMD jobs. Future queued work means v5 completion alone
would not finish the workflow.

## Workflow DAG, runner assignment and actual outer limits

Exact `.github/workflows/ci.yml`:

- `:97–100`: one build/cache job, self-hosted, **480 minutes**. Its checks,
  toplevel build, artifact/cache upload and generation publication are within
  that job. The normal toplevel cache does not prove all test fixtures/images
  are already available.
- `:169–178`: native test job needs only `build`; full ordinary CI has a
  **360-minute job / 350-minute Run tests step** (`:192–196`). Focused defaults
  are 240; full unstable 420; ZFS 1380. The latter are not this push's selector.
- `:347–398`: nine livepatch matrix jobs also need only `build`, not native
  tests or each other. Six AMD lanes require `amd-livepatch`; three Intel
  lanes require `intel-kvm`, in `vpsAdminOS runners`. `fail-fast: false` allows
  other lanes to continue after a failure. No workflow concurrency group or
  matrix `max-parallel` is declared. Physical runner availability and other
  allocations remain external scheduling inputs.
- `:355,412–416`: each livepatch job has **360 minutes**, its main step
  **350 minutes**, nominally leaving ten minutes for logs/cleanup if setup
  consumes none. This is not a separately reserved ten-minute guarantee.
  Checkout/setup also consume the job budget.

For active v5, those configured cutoffs project to **21:45:02Z for the step**
and **21:54:58Z for the job**, assuming this attempt and normal Actions timeout
enforcement. At the fixed snapshot, **1h12m05s** remained in the main-step
budget. These are configured cutoffs, not forecasts or proof of progress.
The YAML has no aggregate workflow/queue timeout: adding overlapping job
durations or treating the six-hour job timeout as a workflow-age deadline is
incorrect. A useful accounting identity is build completion plus the maximum
of each downstream job's allocation wait and active duration.

## Preparation and selection inside the 350-minute step

`ci.yml:428–443` first evaluates/checks and builds corrected v7, released-v5
and shipped-v6 fixtures. `test-runner.sh:13–19` builds/selects the runner itself.
These operations are in the main step, before the guest test. They have no
separate shorter timeout in this YAML.

`ci.yml:445–471` selects `--fresh --jobs 1 --tag <matrix.tag>`. `--fresh` resets
managed disks before an attempt, not a rerun count. Scale lanes add
`--max-cpus 128 --cpu-overcommit ceil(128/host-visible-cpus)`, preserving the
128 **guest** vCPU envelope and memory admission; this does not promise 128
physical CPUs or a particular speed. No CPU-only oversubscription factor
explains how many physical runners exist.

Pushes use prebuild (`ci.yml:4–5,465–469`).
`test-runner/lib/test-runner/cli/command.rb:59–72` prepares all selected images
before starting the executor. `prebuild.rb:27–52,66–90` batches preparation,
uses an 8192 MiB per-build-job estimate and available memory/Nix max-jobs to
cap concurrency. `nix_cli.rb:110–119` waits for the build without its own wall
timeout. Cache substitution, builds and resource admission are possible
preparation costs, not measured current costs without logs. Runtime admission
also uses a resource pool (`executor.rb:215–254`).

The aged-v5 tag selects one qualification instance.
`tests/all-tests.nix:45–89` generates v5/v6 scale/low-memory/retention and
twenty AMD fresh instances. `livepatch-qualification.nix:74–85` gives the
`amd-fresh` lane all **20 fresh + 2 AMD retention** cases. With `--jobs 1` those
22 tests are sequential. Even age-zero profiles execute one sleep-60/check
iteration before testing the break condition; they are not zero-cost VMs.
The separate `amd` tag includes ordinary main/perf/other selected tests and
does not have the aged-v5 shape. Do not compare their aggregate time as if
all six AMD lanes were identical cases.

## Aged workload and phase budgets

References `Q = tests/suite/kernel/livepatch-6.12.95/qualification.rb`,
`C = tests/suite/kernel/livepatch-6.12.95-common.nix` at exact head.

| Phase / check | Intended bound or minimum | Source |
| --- | --- | --- |
| Scale-aged shape | 128 guest vCPUs, 16 GiB, 100,000 tasks, age 14,400s | `livepatch-qualification.nix:20–25` |
| Population readiness | 1800s monotonic deadline, checked after guest probe | `Q:51–67` |
| Aging | At least 14,400s elapsed after ready; sleep 60 then progress/health checks, repeat until age met | `Q:458–489` |
| Workload helper lifetime | 21,600s (6h) from helper startup; not a suite/activation deadline | `Q:453–456`, `task_population.c:331–343,365–397` |
| Post-hotplug/relocation progress | Required counters advance; bounded wait 60s | `Q:79–96,231–240,518–521` |
| Each cgroup population move | 180s command bound | `Q:99–126,513–521` |
| v7 activation | 1800s common deadline for attempt(s) and convergence; expected EBUSY may retry within it, not another 1800s per retry | `Q:266–307`, shape `:86–95` |
| v7 disable | Separate 1800s budget for command plus remaining convergence wait | `Q:220–229,524` |
| Final three workload exit markers | 180s wait; all required success/stopped checks follow | `Q:528–546` |
| Most guest commands without an override | 900s each, not 900s for an entire test/example | `cli/app.rb:112–113`, `test_evaluator.rb:62–78` |
| Transition failure reporter | Up to 300s host command / 290s guest timeout in addition to failed transition | `C:784–817`, `Q:277–281` |
| Failed-example diagnostic/cleanup | Three diagnostic commands with 30s outer/25s guest bounds, then one cleanup batch with 30s bound | `Q:310–374` |
| Guest shutdown | Default 900s command and up to another 900s reaper wait, followed by ensured kill/destroy cleanup | `test_evaluator.rb:764–780`, `osvm/machine.rb:337–357,367–397` |

The successful aged example therefore cannot finish before its four-hour
aging interval plus setup/post-aging work. Both activation and disable can
consume significant additional time. Summing all per-operation maxima does
not yield a valid independent guaranteed completion time: guest command waits,
diagnostics after failures, and many probes have their own bounds; the
350/360-minute Actions limits cap the aggregate job/step instead. Monotonic
deadlines checked between commands are not preemptive guards over every
intervening diagnostic command. Aging can overshoot 14,400s while its checks
run; 14,460s is not a declared hard maximum.

Aging is active qualification, not a four-hour blind sleep: every iteration
requires task/wakeup/fork/per-CPU counters to advance, network stress to
advance, TUN activity, retained SCTP/NFS lock/data, and a healthy kernel. It
prints `qualification predecessor=... tasks=... cpus=... age=...` after those
checks (`Q:468–489`). `C:962–984` health checks include a six-second observation
sleep. Preparation, hotplug, activation, migration and teardown have different
markers; the job step title does not identify which is current.

There is no selected whole-test retry for this qualification: its source
does not override `attempts`, whose renderer default is 1
(`tests/make-test.nix:350–353`, `test_script.rb:27–35`). Executor retries only
unexpected scripts with remaining attempts, stops retrying kernel failures,
and sleeps five seconds between eligible attempts (`executor.rb:485–513`).
Activation's local EBUSY retry is a separate, bounded mechanism. No workflow
retry action is declared.

Executor status messages default to 300 seconds (`executor.rb:12–14,359–365,
430–440`); per-test last-output heartbeats require verbose mode
(`:662–679`), which this command does not request. Status/heartbeat text says
the process is alive; it is not guest forward-progress proof. Inner logs are
redirected to the per-test `test-runner.log` (`:622–627`).

## Historical source comparability

Local Git object reads with `GIT_NO_LAZY_FETCH=1` compared only the four heads
selected by implementer0. [Object receipt](ci-duration-source-comparison.json)
records full commits, exact blobs/trees and stable Nixpkgs pins; no fetch or
history mutation occurred.

| Comparator | Workload / machinery comparison to 846bb |
| --- | --- |
| `b81c43ff6865a033268072f55cd94ad763d0630b` | Identical workflow, qualification shape/Ruby/common/helper, fixture recipe, boot-base module, test-runner and osvm trees. `all-tests.nix` only adds native `system/sysctl`; qualification selection unchanged. Root stable Nixpkgs `cd4ea8d5` becomes `da6dc0e7`; OS sysctl service and panic sysctls differ. Strong workload/machinery comparison, not identical guest/environment. |
| `49636f902704ce6019a7a8ae47ec0b3ca6902f68` | Same listed workload/workflow/runner identity; only native `system/sysctl` selection added. Stable pin `f3a73bcf` becomes `da6dc0e7`; other OS/pin differences remain. |
| `3ae196d60b2811e52cbb75a204108df629dca42d`, `e074a470291570d355a0c27a6d8706561e28d8dd` | Same qualification shape/Ruby/common/helper/fixture/boot-base recipe. New workflow has 24 added lines including prebuild/default selection and two build checks; runner/prebuild/resource/source/VM machinery and native test selection changed. Same intended qualification workload, weaker preparation/overall timing comparators. |

None of these comparisons introduces a longer four-hour age, bigger task/CPU
shape or changed local qualification transition budget at 846bb. Immutable
recipe identity does not guarantee equal build outputs when inputs/pins differ,
and changed OS services remain part of the guest. This lane does not diagnose
the separate CI failures or attribute an execution-time change to a component.

See [historical timing sample](ci-duration-history.md) for implementer0's
complete denominators, exclusions and job/step statistics. Its recent strong
comparators have successful v5 job runtimes 17,065/17,112s and corresponding
main-step runtimes 17,052/17,099s. Current v5 job 16,679s / step 16,675s is
below those completed durations at the fixed snapshot; it is an unfinished,
censored observation, not a measured faster pass. Prior serial AMD totals
also demonstrate that a full workflow may exceed nine hours without any
individual job exceeding its six-hour limit.

## Supported limits and next discriminator

The fixed metadata supports an allocation/scheduling plus designed-workload
explanation of current wall age. It does not prove the guest is presently
healthy or determine time spent inside the current step. A real stall claim
needs an observed expired local readiness/progress/transition bound, a failed
timeout result, or an identified nonadvancing phase/state; quiet step metadata
alone supplies none. A declared large timeout is likewise not evidence that
time was spent productively. If more evidence is needed, the existing sole
observer can preserve the next available phase/progress/terminal receipt;
this package starts no new collection or reproduction.

Upload/evaluation/summary/cleanup remain inside the job budget
(`ci.yml:473–512`). Livepatch logs are uploaded even on success, excluding
binary VM state. Cleanup retains unpublished failure evidence unless successful
or uploaded (`.github/actions/cleanup-test-state/cleanup-test-state.bash:30–47`).
No additional wall timeout/retry is declared in the inspected local composite
actions; external action internals were not audited. Job cancellation/timeout
may still limit artifact availability; this
source inspection does not authorize lifecycle or CI actions.
