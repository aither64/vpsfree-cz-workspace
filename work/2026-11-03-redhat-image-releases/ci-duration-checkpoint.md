# CI duration checkpoint

2026-11-03 21:44 UTC; read-only architect0 checkpoint. Current generic CI
41695511680, head `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`.

**Conclusion:** about one hour in `Run tests` does not establish a stall.
Recent full-suite jobs took 2h18m–4h10m, and the exact baseline spent over two
hours preparing tests before any VM test began. This supports allowing the
existing run to continue within its configured bounds; it does not prove
current test progress or predict a successful result.

## Configured work and stopping conditions

The push selects the whole `ci` suite/tag, `--prebuild`, `--jobs auto`, fresh
disks, and `tests/test-configs/ci.nix`. Stop-on-failure defaults to false, so
an individual failure need not end the batch. The CLI's 900-second default
is a machine-command timeout, not a suite deadline. Test-script attempts are
bounded by their declared attempts (default one). Resource admission controls
the actual concurrency; `auto` does not promise a fixed completion time.

The [workflow](https://github.com/vpsfreecz/vpsadminos/blob/1a637e9eac4311adba2b08d60dfa7a17d07bcb52/.github/workflows/ci.yml#L169-L292)
sets **350 minutes for Run tests**, **360 minutes for the job**, and explains
that full CI includes cold livepatch builds and NFS guests. Current job
126191147285 started at 20:42:40 UTC; its test step started at 20:42:44.
Nominal deadlines are therefore **2026-11-04 02:32:44 UTC** for the test step
and **02:42:40 UTC** for the job. Timeout is a failed check requiring evidence
review, not an acceptable substitute for completion. Queued jobs have no
completion ETA established by these running-job limits.

## Small historical sample

These are push-triggered `CI (ci)` runs. Durations below are the `Run tests`
step, excluding queue time and the preceding OS build.

| Run / suite job | Source | Runner | Test-step duration | Result |
| --- | --- | --- | --- | --- |
| [41666620193 / 126034272635](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193/job/126034272635) | exact baseline `dd188397`, Nov 3 | gh-runner3 | 4h10m06s | failure |
| [40296454457 / 121489063136](https://github.com/vpsfreecz/vpsadminos/actions/runs/40296454457/job/121489063136) | staging `d9be8c4b`, Oct 26 | gh-runner3 | 2h18m26s | failure |
| [40174698311 / 121115448755](https://github.com/vpsfreecz/vpsadminos/actions/runs/40174698311/job/121115448755) | staging `cb4dcaaa`, Oct 25 | gh-runner1 | 2h30m12s | failure |

Older revisions are contextual samples, not equivalent verification. All three
failed; these durations must not be described as successful-check benchmarks.
The exact-baseline log confirms whole suite/tag `ci`, preparation of 109 tests
at 16:03:28, first test start at 18:40:18, and final result at 20:11:24.
It completed 317 scripts across 109 tests in 5465.88 seconds of execution:
108 tests passed and one failed. Thus its long duration included observable
completion of work, rather than only waiting until a timeout. Current runtime
cannot be inferred to follow the same preparation/execution split.

## Current visibility and next milestone

A single job API snapshot confirms checkout and state preparation passed and
`Run tests` remains active on gh-runner3. Its log endpoint returned HTTP 404
(`BlobNotFound`) at 21:43:13 UTC. The artifact list has production/livepatch
matrix artifacts but no native-suite artifact. Native log upload occurs after
the test step and is conditional; the workflow does not publish a live native
artifact. There is therefore **no current case-level progress evidence** from
the inspected public endpoints. The runner normally emits five-minute status
messages, but they were not available through this active-job log endpoint.

Shortest valid next milestone: let the existing sole watcher report the test
step's completion, then inspect its result and newly available job log/artifact;
also observe the separately queued image and Intel jobs starting. No duplicate
watch, rerun or infrastructure change is justified by duration alone. If still
active at 4h10m elapsed (00:52:50 UTC), reassess against the baseline and any
new visibility. The configured 350/360-minute limits remain the hard bounds
for this running test/job. All required checks still need their ordinary
disposition before merge.

Evidence: job/step timestamps from GitHub API; baseline log retained at
`ci-root-cause/ci-baseline-suite-job-126034272635.log` (lines 244–348 selectors,
711–718 preparation/start, 5404–5408 final result); active log response at
`ci-current-suite-log-response.txt`. No application changes, CI mutations,
new watcher, runner access or repository claim were made.
