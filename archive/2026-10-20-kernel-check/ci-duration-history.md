# CI duration history: bounded AMD comparison

Timestamps are UTC. Primary sample: the latest **15 completed push runs** of
`ci.yml` returned on 2026-10-22; all attempt 1, 2026-10-18 through 2026-10-22.
The initial unfiltered latest-15 discovery also contained three focused
`workflow_dispatch` benchmark runs (39305352549, 39296042103, 39276852536),
which have no AMD matrix jobs and are excluded. No remote request targeted
current run 39767770407; its state below comes exclusively from implementer2's
[same-watcher local capture](ci-duration-current.md).
The completed [source budget and comparison report](ci-duration-source.md)
records exact workflow/fixture references and the full
[source identity comparison](ci-duration-source-comparison.json).

**No execution-duration regression is demonstrated by this sample.** The best
historical comparators already spend about 4h42–4h49 in each successful aged
AMD job. Serial allocation to the same AMD runner plus these long executions
explains a multi-hour workflow age. This does not prove current inner progress
or exclude a new failure; the active step is unfinished.
At the fixed 20:32:57Z snapshot, source-derived main-step/job cutoffs were
21:45:02Z / 21:54:58Z. These are configured limits, not completion forecasts.

## Sample and exclusions

Each run link resolves its exact head/attempt. “End” is latest job completion,
not `updated_at`; workflow wall age includes build/dependency/allocation waits.
Full job/step timestamps, runner ID/group/labels and outcomes are retained in
`ci-duration-history-jobs-RUN-1.json` and [normalized evidence](ci-duration-history-normalized.json).

| Run / attempt | Branch | Full head | Created UTC → latest job end UTC | Wall | Result / AMD rows |
| --- | --- | --- | --- | --- | --- |
| [39764186292](https://github.com/vpsfreecz/vpsadminos/actions/runs/39764186292/attempts/1) / 1 | 2026-10-20-kernel-check | `895870606179f0c1170ad92a5fdc49eb2d6d1bbf` | 2026-10-22T10:35:03Z → 2026-10-22T11:04:55Z | 0:29:52 | cancelled / 6 |
| [39759039117](https://github.com/vpsfreecz/vpsadminos/actions/runs/39759039117/attempts/1) / 1 | 2026-10-20-kernel-check | `88486d43f7d47917b6ab796163abf8cd1f0be94a` | 2026-10-22T09:54:34Z → 2026-10-22T10:37:57Z | 0:43:23 | cancelled / 6 |
| [39745935323](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323/attempts/1) / 1 | 2026-10-20-kernel-check | `8528262315b0794a8f50917cf33c53a07fd14030` | 2026-10-22T08:11:43Z → 2026-10-22T09:57:45Z | 1:46:02 | cancelled / 6 |
| [39744127896](https://github.com/vpsfreecz/vpsadminos/actions/runs/39744127896/attempts/1) / 1 | 2026-10-20-kernel-check | `14cdf1caec606bb6bc88fcb32ac48f707f5dabb0` | 2026-10-22T07:57:01Z → 2026-10-22T08:15:23Z | 0:18:22 | cancelled / 0 |
| [39600028637](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637/attempts/1) / 1 | 2026-10-20-kernel-check | `b81c43ff6865a033268072f55cd94ad763d0630b` | 2026-10-21T12:29:39Z → 2026-10-22T01:11:09Z | 12:41:30 | failure / 6 |
| [39598560664](https://github.com/vpsfreecz/vpsadminos/actions/runs/39598560664/attempts/1) / 1 | 2026-10-20-kernel-check | `f3e91f6213934bf5d1a2ca52a7fdc6e63941a647` | 2026-10-21T12:18:32Z → 2026-10-21T12:30:53Z | 0:12:21 | cancelled / 0 |
| [39414347376](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376/attempts/1) / 1 | staging | `49636f902704ce6019a7a8ae47ec0b3ca6902f68` | 2026-10-20T11:21:17Z → 2026-10-20T21:24:03Z | 10:02:46 | failure / 6 |
| [39413777406](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406/attempts/1) / 1 | 2026-10-17-impermanence-test-failures | `49636f902704ce6019a7a8ae47ec0b3ca6902f68` | 2026-10-20T11:16:29Z → 2026-10-21T13:14:38Z | 25:58:09 | failure / 6 |
| [39396698293](https://github.com/vpsfreecz/vpsadminos/actions/runs/39396698293/attempts/1) / 1 | 2026-10-17-impermanence-test-failures | `e32d5382910501b0c8fe80bc6b9e6044e56ead8e` | 2026-10-20T08:53:41Z → 2026-10-20T11:17:41Z | 2:24:00 | cancelled / 6 |
| [39381114351](https://github.com/vpsfreecz/vpsadminos/actions/runs/39381114351/attempts/1) / 1 | fix/kernel-stability-20261018 | `e074a470291570d355a0c27a6d8706561e28d8dd` | 2026-10-20T06:33:59Z → 2026-10-21T08:29:24Z | 25:55:25 | cancelled / 6 |
| [39358414083](https://github.com/vpsfreecz/vpsadminos/actions/runs/39358414083/attempts/1) / 1 | fix/kernel-stability-20261018 | `8019b9ffb7bc3350b64eccb86274b825e47a015b` | 2026-10-20T02:20:53Z → 2026-10-21T02:33:20Z | 24:12:27 | failure / 6 |
| [39309610523](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523/attempts/1) / 1 | fix/kernel-stability-20261018 | `3ae196d60b2811e52cbb75a204108df629dca42d` | 2026-10-19T19:16:38Z → 2026-10-20T18:50:02Z | 23:33:24 | failure / 6 |
| [39154883451](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154883451/attempts/1) / 1 | fix/kernel-stability-20261018 | `7c1af032a281c13efeb205f0d7f3e3b0ac19853d` | 2026-10-18T18:35:54Z → 2026-10-20T03:12:41Z | 32:36:47 | failure / 6 |
| [39154204132](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154204132/attempts/1) / 1 | staging | `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616` | 2026-10-18T18:27:04Z → 2026-10-20T03:00:16Z | 32:33:12 | failure / 6 |
| [39153773022](https://github.com/vpsfreecz/vpsadminos/actions/runs/39153773022/attempts/1) / 1 | 2026-10-17-review-deployment-readiness | `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616` | 2026-10-18T18:21:18Z → 2026-10-18T23:17:13Z | 4:55:55 | failure / 0 |

There are 72 AMD matrix job records: 20 successful test steps,
3 failed runtime test steps, 3 cancelled/incomplete test steps, and
46 cancelled jobs with runner ID 0, empty runner name and no steps.
Only assigned, successfully completed comparable executions enter the success
statistics below. The unassigned jobs have misleading `started_at` values equal
to creation; their recorded span is waiting/censored metadata, not execution.
Three sampled push runs never created AMD jobs because the prerequisite build
was cancelled or failed. No independent green-workflow population is claimed.

## Strongest workload comparators

Implementer1 compared local exact sources: b81c43ff and 49636f90 have identical
`ci.yml`, qualification Nix/Ruby, common/task-population/fixture/boot-base files
and test-runner/osvm code to 846bb. The only all-tests addition is system/sysctl,
outside these qualification tag selectors. All assigned historical AMD jobs use
`gh-runner4.int.vpsadminos.org`, runner ID 11199, label `amd-livepatch`, group
`vpsadminos runners`, matching the current runner. This is workload/matrix
comparability, **not exact environment equivalence**: root Nixpkgs is cd4ea8d5
at b81c and f3a73bcf at 49636, versus da6dc0e7 now; OS policy/service inputs differ.
Two runs share 49636 but have independent feature/staging executions.

Older 3ae196d6/e074a470 retain the same qualification workload and budgets but
differ in workflow prebuild and runner preparation/resource/source machinery.
They are listed below as weaker corroboration and excluded from these summary
statistics. Other heads were not source-matched for runtime statistics.

| AMD matrix label | Successful n (unique heads) | Job min / median / max | Test-step min / median / max |
| --- | --- | --- | --- |
| amd | 2 (2) | 0:38:17 / 0:39:01.5 / 0:39:46 | 0:38:03 / 0:38:48.5 / 0:39:34 |
| amd-fresh | 3 (2) | 1:32:17 / 1:32:30 / 1:32:30 | 1:32:04 / 1:32:17 / 1:32:17 |
| amd-scale-aged-v5 | 2 (2) | 4:44:25 / 4:44:48.5 / 4:45:12 | 4:44:12 / 4:44:35.5 / 4:44:59 |
| amd-scale-aged-v6 | 2 (2) | 4:42:14 / 4:45:36 / 4:48:58 | 4:42:00 / 4:45:22 / 4:48:44 |
| amd-low-memory-v5 | 2 (2) | 0:06:14 / 0:06:16.5 / 0:06:19 | 0:06:02 / 0:06:04.5 / 0:06:07 |
| amd-low-memory-v6 | 3 (2) | 0:06:10 / 0:06:13 / 0:06:13 | 0:05:56 / 0:06:00 / 0:06:01 |

Success denominator is small: two aged-v5 and two aged-v6 executions from two
heads. Staging 49636 aged jobs failed after short runtime, not a short complete
qualification: historical job logs [v5](ci-duration-history-job-118604848615.log)
and [v6](ci-duration-history-job-118604848680.log) show tests actually started
and failed after 400.44 / 388.81 seconds; they were not prebuild-only failures.
Their failure causes are outside this duration package.

One successful b81c [v5 job log](ci-duration-history-job-119228579023.log), lines 208–277,
distinguishes phases: job starts 18:54:25; test step 18:54:28; discovery finishes
18:55:50; selected prebuild finishes and runtime starts 18:56:29; example passes
23:38:21 (16843.97s); native test completes 23:38:40 (16930.66s); job ends
23:38:50, all on 2026-10-21 UTC. Thus about two minutes preceded native runtime
and almost all remaining duration was one qualification test. Five-minute
“1 running” messages are harness liveness, not proof of an inner workload phase.

## Current snapshot and serialization

At implementer2's 20:32:57Z capture, current workflow age is 9:29:01. Exact
current head is 846bb469505789ba0b2a405fa5905ba6d8253006, attempt 1.

| Current critical-path interval UTC (2026-10-22) | Evidence / duration |
| --- | --- |
| 11:03:56 → 11:04:51 | Workflow creation to OS/cache start, 0:00:55 |
| 11:04:51 → 11:18:07 | OS/cache job, 0:13:16 |
| 11:18:09 → 15:42:18 | AMD aged-v6, failed after 4:24:09 |
| 15:42:20 → 15:48:38 | AMD low-memory-v5, passed after 0:06:18 |
| 15:48:40 → 15:54:57 | AMD low-memory-v6, passed after 0:06:17 |
| 15:54:58 → snapshot 20:32:57 | AMD aged-v5 still running, elapsed 4:37:59; test step 15:55:02, elapsed 4:37:55 |
| Created 11:18:07 → snapshot 20:32:57 | AMD fresh and ordinary AMD queued 9:14:50, runner ID 0/no steps |

The four assigned AMD intervals above are on the same named runner and do not
overlap. Aged-v5 waited 4:36:51 after its build dependency completed; that span
is accounted almost entirely by earlier same-run AMD jobs, rather than its own
execution. Queued fresh/ordinary AMD did not execute for nine hours. The active
v5 step's elapsed time is below the strongest historical success range
4:44:12–4:44:59; no current completion/ETA is inferred. Current failed-v6 duration
is shorter than the strong successful range; weaker historical 3ae196d6 also
had an executed-v6 failure after 4:26:54. Similar timing does not imply same cause.

Historical serialization is directly visible too: b81c six assigned AMD jobs
ran on gh-runner4 between 2026-10-21T13:14:39Z and 2026-10-22T01:11:09Z,
with only second-scale gaps. Their summed job time is 11:56:21, inside workflow
wall time 12:41:30, with build and initial allocation wait outside the serial
chain. Other historical runs have up to 24-hour unassigned cancellations after
a successful build. The evidence establishes allocation waiting and repeated
one-runner execution; it does not certify all runner capacity or every scheduling
reason. Workflow age alone is therefore a poor execution-regression metric.

## Complete sampled AMD job inventory

Timestamps below use `MM-DD HH:MM:SS` UTC, year 2026. All rows are attempt 1.
Assigned rows show actual job span; `unassigned` rows retain API creation-to-end
span explicitly as waiting. Test-step timestamps are in the linked raw JSON;
its duration/outcome is shown separately. Full matrix name is
`Livepatch lifecycle (LABEL)`. Job links carry exact IDs.

| Run | Label / job | Created UTC | Runner-start → end UTC (or unassigned metadata span) | Job or wait | Test step / outcome |
| --- | --- | --- | --- | --- | --- |
| 39764186292 | [amd-scale-aged-v6 / 119782206375](https://github.com/vpsfreecz/vpsadminos/actions/runs/39764186292/job/119782206375) | 10-22 10:51:24 | 10-22 10:51:26 → 10-22 11:04:55 | 0:13:29 cancelled | 0:13:12 / cancelled |
| 39764186292 | [amd-scale-aged-v5 / 119782206388](https://github.com/vpsfreecz/vpsadminos/actions/runs/39764186292/job/119782206388) | 10-22 10:51:24 | unassigned 10-22 10:51:24 → 10-22 11:04:28 | 0:13:04 cancelled | — / not executed |
| 39764186292 | [amd-fresh / 119782206403](https://github.com/vpsfreecz/vpsadminos/actions/runs/39764186292/job/119782206403) | 10-22 10:51:24 | unassigned 10-22 10:51:24 → 10-22 11:04:28 | 0:13:04 cancelled | — / not executed |
| 39764186292 | [amd / 119782206409](https://github.com/vpsfreecz/vpsadminos/actions/runs/39764186292/job/119782206409) | 10-22 10:51:24 | unassigned 10-22 10:51:24 → 10-22 11:04:28 | 0:13:04 cancelled | — / not executed |
| 39764186292 | [amd-low-memory-v5 / 119782206547](https://github.com/vpsfreecz/vpsadminos/actions/runs/39764186292/job/119782206547) | 10-22 10:51:24 | unassigned 10-22 10:51:24 → 10-22 11:04:28 | 0:13:04 cancelled | — / not executed |
| 39764186292 | [amd-low-memory-v6 / 119782206696](https://github.com/vpsfreecz/vpsadminos/actions/runs/39764186292/job/119782206696) | 10-22 10:51:24 | unassigned 10-22 10:51:24 → 10-22 11:04:28 | 0:13:04 cancelled | — / not executed |
| 39759039117 | [amd-fresh / 119763880080](https://github.com/vpsfreecz/vpsadminos/actions/runs/39759039117/job/119763880080) | 10-22 10:07:29 | 10-22 10:07:30 → 10-22 10:37:56 | 0:30:26 cancelled | 0:30:13 / cancelled |
| 39759039117 | [amd / 119763880093](https://github.com/vpsfreecz/vpsadminos/actions/runs/39759039117/job/119763880093) | 10-22 10:07:29 | unassigned 10-22 10:07:29 → 10-22 10:36:39 | 0:29:10 cancelled | — / not executed |
| 39759039117 | [amd-low-memory-v5 / 119763880151](https://github.com/vpsfreecz/vpsadminos/actions/runs/39759039117/job/119763880151) | 10-22 10:07:29 | unassigned 10-22 10:07:29 → 10-22 10:36:39 | 0:29:10 cancelled | — / not executed |
| 39759039117 | [amd-scale-aged-v6 / 119763880155](https://github.com/vpsfreecz/vpsadminos/actions/runs/39759039117/job/119763880155) | 10-22 10:07:29 | unassigned 10-22 10:07:29 → 10-22 10:36:39 | 0:29:10 cancelled | — / not executed |
| 39759039117 | [amd-low-memory-v6 / 119763880174](https://github.com/vpsfreecz/vpsadminos/actions/runs/39759039117/job/119763880174) | 10-22 10:07:29 | unassigned 10-22 10:07:29 → 10-22 10:36:39 | 0:29:10 cancelled | — / not executed |
| 39759039117 | [amd-scale-aged-v5 / 119763880329](https://github.com/vpsfreecz/vpsadminos/actions/runs/39759039117/job/119763880329) | 10-22 10:07:29 | unassigned 10-22 10:07:29 → 10-22 10:36:39 | 0:29:10 cancelled | — / not executed |
| 39745935323 | [amd-scale-aged-v6 / 119720146437](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323/job/119720146437) | 10-22 08:26:01 | 10-22 08:26:02 → 10-22 09:57:45 | 1:31:43 cancelled | 1:31:24 / cancelled |
| 39745935323 | [amd-fresh / 119720146525](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323/job/119720146525) | 10-22 08:26:01 | unassigned 10-22 08:26:01 → 10-22 09:56:23 | 1:30:22 cancelled | — / not executed |
| 39745935323 | [amd-scale-aged-v5 / 119720146545](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323/job/119720146545) | 10-22 08:26:01 | unassigned 10-22 08:26:01 → 10-22 09:56:23 | 1:30:22 cancelled | — / not executed |
| 39745935323 | [amd / 119720146556](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323/job/119720146556) | 10-22 08:26:01 | unassigned 10-22 08:26:01 → 10-22 09:56:23 | 1:30:22 cancelled | — / not executed |
| 39745935323 | [amd-low-memory-v6 / 119720146563](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323/job/119720146563) | 10-22 08:26:01 | unassigned 10-22 08:26:01 → 10-22 09:56:23 | 1:30:22 cancelled | — / not executed |
| 39745935323 | [amd-low-memory-v5 / 119720146643](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323/job/119720146643) | 10-22 08:26:01 | unassigned 10-22 08:26:01 → 10-22 09:56:23 | 1:30:22 cancelled | — / not executed |
| 39600028637 | [amd / 119228578843](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637/job/119228578843) | 10-21 12:44:21 | 10-21 13:14:39 → 10-21 13:52:56 | 0:38:17 success | 0:38:03 / success |
| 39600028637 | [amd-low-memory-v6 / 119228578848](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637/job/119228578848) | 10-21 12:44:21 | 10-21 18:41:57 → 10-21 18:48:07 | 0:06:10 success | 0:05:56 / success |
| 39600028637 | [amd-scale-aged-v6 / 119228578904](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637/job/119228578904) | 10-21 12:44:21 | 10-21 13:52:57 → 10-21 18:41:55 | 4:48:58 success | 4:48:44 / success |
| 39600028637 | [amd-low-memory-v5 / 119228578910](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637/job/119228578910) | 10-21 12:44:21 | 10-21 18:48:08 → 10-21 18:54:22 | 0:06:14 success | 0:06:02 / success |
| 39600028637 | [amd-fresh / 119228579002](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637/job/119228579002) | 10-21 12:44:21 | 10-21 23:38:52 → 10-22 01:11:09 | 1:32:17 success | 1:32:04 / success |
| 39600028637 | [amd-scale-aged-v5 / 119228579023](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637/job/119228579023) | 10-21 12:44:21 | 10-21 18:54:25 → 10-21 23:38:50 | 4:44:25 success | 4:44:12 / success |
| 39414347376 | [amd-scale-aged-v5 / 118604848615](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376/job/118604848615) | 10-20 11:34:42 | 10-20 16:51:45 → 10-20 17:01:57 | 0:10:12 failure | 0:09:19 / failure |
| 39414347376 | [amd-scale-aged-v6 / 118604848680](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376/job/118604848680) | 10-20 11:34:42 | 10-20 19:29:52 → 10-20 19:38:55 | 0:09:03 failure | 0:08:49 / failure |
| 39414347376 | [amd / 118604848710](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376/job/118604848710) | 10-20 11:34:42 | 10-20 18:50:04 → 10-20 19:29:50 | 0:39:46 success | 0:39:34 / success |
| 39414347376 | [amd-low-memory-v5 / 118604848789](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376/job/118604848789) | 10-20 11:34:42 | 10-20 21:11:29 → 10-20 21:17:48 | 0:06:19 success | 0:06:07 / success |
| 39414347376 | [amd-fresh / 118604848796](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376/job/118604848796) | 10-20 11:34:42 | 10-20 19:38:57 → 10-20 21:11:27 | 1:32:30 success | 1:32:17 / success |
| 39414347376 | [amd-low-memory-v6 / 118604848806](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376/job/118604848806) | 10-20 11:34:42 | 10-20 21:17:50 → 10-20 21:24:03 | 0:06:13 success | 0:06:01 / success |
| 39413777406 | [amd-fresh / 118603543951](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406/job/118603543951) | 10-20 11:31:23 | 10-20 21:24:05 → 10-20 22:56:35 | 1:32:30 success | 1:32:17 / success |
| 39413777406 | [amd-scale-aged-v5 / 118603543952](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406/job/118603543952) | 10-20 11:31:23 | 10-21 08:29:26 → 10-21 13:14:38 | 4:45:12 success | 4:44:59 / success |
| 39413777406 | [amd-scale-aged-v6 / 118603543983](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406/job/118603543983) | 10-20 11:31:23 | 10-20 22:56:36 → 10-21 03:38:50 | 4:42:14 success | 4:42:00 / success |
| 39413777406 | [amd / 118603544068](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406/job/118603544068) | 10-20 11:31:23 | unassigned 10-20 11:31:23 → 10-21 11:31:23 | 24:00:00 cancelled | — / not executed |
| 39413777406 | [amd-low-memory-v5 / 118603544104](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406/job/118603544104) | 10-20 11:31:23 | unassigned 10-20 11:31:23 → 10-21 11:31:24 | 24:00:01 cancelled | — / not executed |
| 39413777406 | [amd-low-memory-v6 / 118603544260](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406/job/118603544260) | 10-20 11:31:23 | 10-21 03:38:51 → 10-21 03:45:04 | 0:06:13 success | 0:06:00 / success |
| 39396698293 | [amd / 118546351291](https://github.com/vpsfreecz/vpsadminos/actions/runs/39396698293/job/118546351291) | 10-20 09:06:44 | unassigned 10-20 09:06:44 → 10-20 11:16:38 | 2:09:54 cancelled | — / not executed |
| 39396698293 | [amd-fresh / 118546351340](https://github.com/vpsfreecz/vpsadminos/actions/runs/39396698293/job/118546351340) | 10-20 09:06:44 | unassigned 10-20 09:06:44 → 10-20 11:16:38 | 2:09:54 cancelled | — / not executed |
| 39396698293 | [amd-scale-aged-v5 / 118546351378](https://github.com/vpsfreecz/vpsadminos/actions/runs/39396698293/job/118546351378) | 10-20 09:06:44 | unassigned 10-20 09:06:44 → 10-20 11:16:38 | 2:09:54 cancelled | — / not executed |
| 39396698293 | [amd-low-memory-v6 / 118546351403](https://github.com/vpsfreecz/vpsadminos/actions/runs/39396698293/job/118546351403) | 10-20 09:06:44 | unassigned 10-20 09:06:44 → 10-20 11:16:38 | 2:09:54 cancelled | — / not executed |
| 39396698293 | [amd-scale-aged-v6 / 118546351495](https://github.com/vpsfreecz/vpsadminos/actions/runs/39396698293/job/118546351495) | 10-20 09:06:44 | unassigned 10-20 09:06:44 → 10-20 11:16:38 | 2:09:54 cancelled | — / not executed |
| 39396698293 | [amd-low-memory-v5 / 118546351525](https://github.com/vpsfreecz/vpsadminos/actions/runs/39396698293/job/118546351525) | 10-20 09:06:44 | unassigned 10-20 09:06:44 → 10-20 11:16:38 | 2:09:54 cancelled | — / not executed |
| 39381114351 | [amd-fresh / 118493907862](https://github.com/vpsfreecz/vpsadminos/actions/runs/39381114351/job/118493907862) | 10-20 06:45:56 | unassigned 10-20 06:45:56 → 10-21 06:45:56 | 24:00:00 cancelled | — / not executed |
| 39381114351 | [amd-scale-aged-v6 / 118493907887](https://github.com/vpsfreecz/vpsadminos/actions/runs/39381114351/job/118493907887) | 10-20 06:45:56 | 10-21 03:45:06 → 10-21 08:29:24 | 4:44:18 success | 4:44:04 / success |
| 39381114351 | [amd-scale-aged-v5 / 118493907941](https://github.com/vpsfreecz/vpsadminos/actions/runs/39381114351/job/118493907941) | 10-20 06:45:56 | unassigned 10-20 06:45:56 → 10-21 06:45:56 | 24:00:00 cancelled | — / not executed |
| 39381114351 | [amd-low-memory-v5 / 118493907991](https://github.com/vpsfreecz/vpsadminos/actions/runs/39381114351/job/118493907991) | 10-20 06:45:56 | unassigned 10-20 06:45:56 → 10-21 06:45:56 | 24:00:00 cancelled | — / not executed |
| 39381114351 | [amd-low-memory-v6 / 118493908017](https://github.com/vpsfreecz/vpsadminos/actions/runs/39381114351/job/118493908017) | 10-20 06:45:56 | unassigned 10-20 06:45:56 → 10-21 06:45:56 | 24:00:00 cancelled | — / not executed |
| 39381114351 | [amd / 118493908023](https://github.com/vpsfreecz/vpsadminos/actions/runs/39381114351/job/118493908023) | 10-20 06:45:56 | unassigned 10-20 06:45:56 → 10-21 06:45:56 | 24:00:00 cancelled | — / not executed |
| 39358414083 | [amd / 118422229477](https://github.com/vpsfreecz/vpsadminos/actions/runs/39358414083/job/118422229477) | 10-20 02:33:19 | unassigned 10-20 02:33:19 → 10-21 02:33:19 | 24:00:00 cancelled | — / not executed |
| 39358414083 | [amd-low-memory-v6 / 118422229516](https://github.com/vpsfreecz/vpsadminos/actions/runs/39358414083/job/118422229516) | 10-20 02:33:19 | unassigned 10-20 02:33:19 → 10-21 02:33:19 | 24:00:00 cancelled | — / not executed |
| 39358414083 | [amd-low-memory-v5 / 118422229530](https://github.com/vpsfreecz/vpsadminos/actions/runs/39358414083/job/118422229530) | 10-20 02:33:19 | unassigned 10-20 02:33:19 → 10-21 02:33:20 | 24:00:01 cancelled | — / not executed |
| 39358414083 | [amd-scale-aged-v5 / 118422229544](https://github.com/vpsfreecz/vpsadminos/actions/runs/39358414083/job/118422229544) | 10-20 02:33:19 | unassigned 10-20 02:33:19 → 10-21 02:33:20 | 24:00:01 cancelled | — / not executed |
| 39358414083 | [amd-scale-aged-v6 / 118422229562](https://github.com/vpsfreecz/vpsadminos/actions/runs/39358414083/job/118422229562) | 10-20 02:33:19 | unassigned 10-20 02:33:19 → 10-21 02:33:20 | 24:00:01 cancelled | — / not executed |
| 39358414083 | [amd-fresh / 118422229589](https://github.com/vpsfreecz/vpsadminos/actions/runs/39358414083/job/118422229589) | 10-20 02:33:19 | unassigned 10-20 02:33:19 → 10-21 02:33:20 | 24:00:01 cancelled | — / not executed |
| 39309610523 | [amd-scale-aged-v6 / 118261936621](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523/job/118261936621) | 10-19 19:30:02 | 10-20 06:52:25 → 10-20 11:19:19 | 4:26:54 failure | 4:26:40 / failure |
| 39309610523 | [amd / 118261936676](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523/job/118261936676) | 10-19 19:30:02 | 10-20 16:06:28 → 10-20 16:45:32 | 0:39:04 success | 0:38:51 / success |
| 39309610523 | [amd-low-memory-v5 / 118261936718](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523/job/118261936718) | 10-19 19:30:02 | 10-20 16:45:33 → 10-20 16:51:43 | 0:06:10 success | 0:05:57 / success |
| 39309610523 | [amd-scale-aged-v5 / 118261936728](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523/job/118261936728) | 10-19 19:30:02 | 10-20 11:19:20 → 10-20 16:06:26 | 4:47:06 success | 4:46:53 / success |
| 39309610523 | [amd-fresh / 118261936744](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523/job/118261936744) | 10-19 19:30:02 | 10-20 17:02:14 → 10-20 18:43:41 | 1:41:27 success | 1:40:29 / success |
| 39309610523 | [amd-low-memory-v6 / 118261936750](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523/job/118261936750) | 10-19 19:30:02 | 10-20 18:43:43 → 10-20 18:50:02 | 0:06:19 success | 0:06:07 / success |
| 39154883451 | [amd-fresh / 117871456781](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154883451/job/117871456781) | 10-19 03:12:41 | unassigned 10-19 03:12:41 → 10-20 03:12:41 | 24:00:00 cancelled | — / not executed |
| 39154883451 | [amd / 117871456784](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154883451/job/117871456784) | 10-19 03:12:41 | unassigned 10-19 03:12:41 → 10-20 03:12:41 | 24:00:00 cancelled | — / not executed |
| 39154883451 | [amd-scale-aged-v6 / 117871456809](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154883451/job/117871456809) | 10-19 03:12:41 | unassigned 10-19 03:12:41 → 10-20 03:12:41 | 24:00:00 cancelled | — / not executed |
| 39154883451 | [amd-low-memory-v5 / 117871456812](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154883451/job/117871456812) | 10-19 03:12:41 | unassigned 10-19 03:12:41 → 10-20 03:12:41 | 24:00:00 cancelled | — / not executed |
| 39154883451 | [amd-scale-aged-v5 / 117871456823](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154883451/job/117871456823) | 10-19 03:12:41 | unassigned 10-19 03:12:41 → 10-20 03:12:41 | 24:00:00 cancelled | — / not executed |
| 39154883451 | [amd-low-memory-v6 / 117871456867](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154883451/job/117871456867) | 10-19 03:12:41 | unassigned 10-19 03:12:41 → 10-20 03:12:41 | 24:00:00 cancelled | — / not executed |
| 39154204132 | [amd-scale-aged-v5 / 117868416193](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154204132/job/117868416193) | 10-19 03:00:15 | unassigned 10-19 03:00:15 → 10-20 03:00:16 | 24:00:01 cancelled | — / not executed |
| 39154204132 | [amd / 117868416194](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154204132/job/117868416194) | 10-19 03:00:15 | unassigned 10-19 03:00:15 → 10-20 03:00:16 | 24:00:01 cancelled | — / not executed |
| 39154204132 | [amd-fresh / 117868416213](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154204132/job/117868416213) | 10-19 03:00:15 | unassigned 10-19 03:00:15 → 10-20 03:00:16 | 24:00:01 cancelled | — / not executed |
| 39154204132 | [amd-low-memory-v5 / 117868416234](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154204132/job/117868416234) | 10-19 03:00:15 | unassigned 10-19 03:00:15 → 10-20 03:00:16 | 24:00:01 cancelled | — / not executed |
| 39154204132 | [amd-scale-aged-v6 / 117868416249](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154204132/job/117868416249) | 10-19 03:00:15 | unassigned 10-19 03:00:15 → 10-20 03:00:16 | 24:00:01 cancelled | — / not executed |
| 39154204132 | [amd-low-memory-v6 / 117868416312](https://github.com/vpsfreecz/vpsadminos/actions/runs/39154204132/job/117868416312) | 10-19 03:00:15 | unassigned 10-19 03:00:15 → 10-20 03:00:16 | 24:00:01 cancelled | — / not executed |

Reproducibility: API discovery used completed-only `ci.yml` runs, then completed
push-only runs (per_page 15). Each sampled historical run was read once through
`actions/runs/RUN/attempts/1/jobs?per_page=100`; no job list needed pagination.
Three small historical job logs (about 128KB total) were fetched to distinguish
actual runtime from early failure/preparation. No historical native archive was
downloaded. Initial gh refused terminal escapes for one log; the read was
repeated with its documented `--allow-escape-sequences` flag and retained locally.
No workflow/test/build/evaluation/retry/cancellation/source/ref/host mutation was
performed by this lane. Current observation remains exclusively implementer2-owned.
Failure causes/test usefulness remain with the separate investigation session.
