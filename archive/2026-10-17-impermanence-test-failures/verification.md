# Verification evidence

Source head: `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`. Tested tree: `98fab6887104cc1aa6f05941825047b031c7c662`. Base: `0081fc01f13236a098380094ddbd00539a9c8dae`. Source worktree is clean and feature branch is published. No deployment or default-branch merge.

## Quick checks and independent review

- Full runner specs: 373 examples, 0 failures, 88 seconds (`r1-runner.log/.status`).
- Full OSVM specs: 184 examples, 0 failures, 62 seconds (`r1-osvm.log/.status`).
- Pure SquashFS flags/module wiring: passed (`ready-cache.log/.status`).
- Declared Nixfmt/RuboCop hooks passed, including enabled scoped commit/amend hooks.
- Hosted GitHub RSpec 39068521789 and RuboCop 39068521800 passed on the exact head. Native CI39068521841 completed with a failure in upgrade/from-6.18-guests;
 126 other native test groups passed. Original logs/artifacts are preserved below;
 diagnosis is recorded in [native-ci-follow-up.md](native-ci-follow-up.md).
- [Independent review and R1 resolution](review.md): all four lanes, complete three-owner history, no migrations or pin streams. Important R1 fixed through canonical allocation-free parser/render validation and verified directly under narrow-fix policy.

## Selected image and VM run

Command in repository `.#test-runner` Nix environment:

```sh
bundle exec ./test-runner/bin/test-runner test --prebuild --jobs auto \
  --max-memory-mib 32768 \
  --state-dir /tmp/os-test-2026-10-17-impermanence-test-failures-32g \
  --fresh '{defaults,dist-config/nixos-persistence-upgrade#*}'
```

Selected two test configs and 13 scripts (defaults plus all 12 original persistence scripts). Preparation detected 96538 MiB assigned and 74699 MiB initially available, applied the configured maximum of 32768 MiB and reserve of 8192 MiB, obtaining 24576 MiB usable. With an 8192 MiB estimate and inherited local Nix max-jobs of 64, it chose 3 preparation jobs. CPU settings and Nix cores were unchanged.

Both selected SquashFS images were actually built. Live command samples confirm `sqfstar -b 1048576 -comp zstd -Xcompression-level 10 -mem 2048M`; tool logs report 64 processors each. See `compressor-sample.txt`. Process sample RSS/HWM is not an aggregate or final compressor peak.

`Preparation complete: 2 test configurations; starting runtime` precedes every executor/VM reservation at23:26:13CEST17Oct. Runtime retained the original 24 GiB RAM ceiling, 39.1 GiB shm ceiling and 96-vCPU capacity (64*1.5). Each group requested 8 GiB and 4 vCPUs; both were admitted together. No Nix preparation/compressor process remained during guest execution. Exact config JSON objects/paths are passed through executor/evaluator; unit tests also forbid runtime Nix and prove retry reuse.

All 12 unique persistence scripts and defaults passed. The command exited 0 after VM cleanup at 01:05:29 CEST on 18 October. Runtime was 5955.47 seconds (the persistence group took 5955.46 seconds); defaults passed in 479.4 seconds. The invocation GC root was present during the last scripts and absent after cleanup. Compact result files each say `expected_success`.

Evidence: `integration-retry-32g.log/.status`; raw build log `/tmp/os-test-2026-10-17-impermanence-test-failures-32g/prebuild-20261017-1571706-w76kq8/build.log`; test logs below that state directory.

## Monitoring interruption and environment

The first attempt was stopped after960seconds by an erroneous utility kernel detector matching a systemd unit named `unit-sys-kernel-debug.mount-disabled.drv`. Parent inspection confirmed ordinary unit builds, no kernel compilation. Exit1/TERM15 is monitor cancellation, not a test failure or OOM result. No VM started in that attempt. Logs `integration-32g.log/.status/-resources.txt` and original build log remain retained. Corrected retry reused those partial outputs; it is not a completely cold run. No shared store paths were deleted or kernel intentionally rebuilt.

Fresh utility invocation was unavailable in the continuation, so the corrected retry used the monitoring skill's visible parent-monitor fallback. Both owned command processes have exited; no verification process remains running. Both VMs took roughly7m10 to reach test-shell readiness, within900seconds. Architect read-only diagnosis confirmed eventual userspace/shell and successful virtiofs mount; no boot repair or timeout extension. Resource snapshot showed32GiB free shm, about55GiB host available, zero current job-cgroup OOM/limit events and zero current memory pressure. Slow-boot cause remains unproven.

## Warm check at the smaller ceiling

After the first command and VM cleanup finished, ran the same command with `--max-memory-mib 16384`, state directory `/tmp/os-test-2026-10-17-impermanence-test-failures-16g`, and exact selector `defaults`. It exited 0 at 01:10:41 CEST on 18 October; guest runtime was 261.7 seconds. No build overlapped the first run's guest.

| Input/result | First run | Warm representative run |
| --- | --- | --- |
| Configured memory ceiling | 32768 MiB | 16384 MiB |
| Existing reserve | 8192 MiB | 8192 MiB |
| Usable memory | 24576 MiB | 8192 MiB |
| Preparation jobs | 3 | 1 |
| Inherited Nix max-jobs | 64 | 64 |
| Runtime CPU ceiling | 96 vCPUs | 96 vCPUs |
| Guest RAM / CPUs per group | 8192 MiB / 4 | 8192 MiB / 4 |
| Selection | 12 persistence scripts + defaults | defaults |
| Result | 13 scripts passed, exit 0 | 1 script passed, exit 0 |

Both runs load the exact same defaults JSON `/nix/store/l7g7fssp5480p5vqbirysajpf60danvy-os-test-defaults.json`. Warm preparation built only the one-selection manifest, fetching a tiny stdenv output; it did not rebuild a test image. The warm GC root was also removed after VM cleanup. Logs: `integration-16g.log/.status`, `warm-preparation.log`, `warm-defaults-test-result.txt`.

Final job cgroup `memory.events` reports zero max/oom/oom_kill events (`final-job-memory-events.txt`). These counters cover the job scope, not an aggregate measurement of every shared daemon or unrelated process.

## Measurement limits

These are configured admission ceilings on one 96 GiB/64-CPU builder, not enforced memory cgroups or measurements from two physical builders. The large evaluator's observed client high-water mark was about 20 GiB; this is not total daemon/build memory. 8192 MiB/job and 2048 MiB cache are sizing policies, not RSS bounds or proof against arbitrary-build/unmanaged-neighbor OOM. No reliable aggregate daemon peak was measured. No fully cold original-fixture baseline or same-fixture warm repeat is claimed.

## Native CI follow-up, 19 October

Exact-head CI39068521841 completed. OS build passed; native job117523492265
completed with126 passing test groups and one failure, upgrade/from-6.18-guests.
Four livepatch jobs passed; six jobs had no steps and were cancelled after24h
without acquiring a runner. Full original job log is native-ci-final-job.log;
artifact12131444137 was downloaded to native-ci-final-artifacts. Architect0 completed
read-only diagnosis: a capability-denied network-setup.service in the predecessor
NixOS22.11 guest, before any upgrade. The branch does not change that fixture or
capability policy; the underlying syscall denial remains unproven. See
[native-ci-follow-up.md](native-ci-follow-up.md) for evidence and caveats. No rerun, source change, merge or deployment has been made.

The native suite ran on gh-runner3.int.vpsadminos.org, a different builder from
the local checks and original incident. Preparation logged assigned102400MiB,
initially available101437MiB, reserve8192MiB, usable93245MiB and inherited
Nix max-jobs48; it selected11 preparation jobs at8192MiB/job. All12 persistence
scripts succeeded; their shared group completed in3662.63seconds. This extends
the adaptation evidence to a second physical builder, but adds no aggregate
memory-peak or hard-containment claim.

## Full-native warm A/B timing, 20 October

Run [39305352549](https://github.com/vpsfreecz/vpsadminos/actions/runs/39305352549)
completed both independent CLI invocations at exact product
`a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`, using benchmark harness
`295b814ad3aadca80ee10c043327c4676d71913c` on gh-runner3. Both legs passed
335 scripts across 127 tests, all 127 group outcomes were expected_success,
and selection digests matched. Both recorded the same intentional driver retry.
No host image builds, OOM kills, runtime resource updates, guest kernel failures,
forced cleanup or remaining owned processes were recorded.

| Measured interval | Without prebuild | With prebuild |
| --- | ---: | ---: |
| Complete CLI wall time, including cleanup | 12297.60 s | 12515.11 s |
| Executor-reported interval | 12231.06 s | 10858.52 s |
| Separate global preparation receipt | None | 1571.26 s |

Observed total difference: +217.50 s, ratio 1.0176867, +1.77%. Executor spans
differ in meaning: the legacy span includes overlapping per-test evaluation and
preparation, while prebuild finishes the aggregate before entering Executor.
Phase receipts depend on buffered output. Warmup outside both measured legs
took 3369.92 s, including selection/preflight and package startup checks.

The harness correctly exited one with comparable_work=false because initial
memory ceilings differed: A 89.4 GiB, B 90.4 GiB. Assigned memory (102400 MiB),
shared-memory ceiling (367.1 GiB), CPU budget (72), Nix max-jobs (48) and cores
(0) were unchanged. Available memory before the legs was 99751 versus 100746
MiB. Both actual CLI commands exited zero. This is a qualified exploratory warm
comparison, not evidence of statistical equivalence or a repeatable regression;
randomized order and host/cache effects remain. No cold-build timing claim.

Original artifact:
[timings.json](benchmark-ci-39305352549/artifact/prebuild-benchmark-39305352549-1/timings.json).
Watcher receipt: [results.json](benchmark-ci-39305352549/results.json).
Interpretation: [benchmark-results-analysis.md](benchmark-results-analysis.md).
No further run, source change, merge, deployment or lifecycle action follows
automatically from this result.

## User-requested oversized-test fallback restoration

After accepting the measured performance tradeoff, the user rejected the added
memory refusal policy. Corrected product head
e32d5382910501b0c8fe80bc6b9e6044e56ead8e restores baseline run-alone admission
for oversized RAM, shared-memory or CPU requests. It retains prebuild, cache
settings, preparation sizing and normal concurrent resource accounting.

Focused checks in the declared runner environment pass: 155 examples, zero
failures, 1.48 seconds, covering scheduler/pool, prebuild/config/evaluator and
CLI app/command specs. New condition-variable cases wait while another test
runs, then reserve the complete oversized request alone and prevent concurrent
reservation. Enabled whole-owner scoped and final commit hooks pass. No real
OOM, VM or image build was induced. Historical measured a2 stays unchanged;
the benchmark is not relabeled as verification of the new source hash.
Independent final review passed with no findings; report is
admission-correction-review.md. Exact original-base range reviewed; no merge.
Published exacte32 hosted checks passed: RSpec39396698231 (3m56s) and
RuboCop39396698224. Native CI39396698293 remained active at the final sample and
was not awaited for this bounded baseline restoration. Report and retained raw
watch logs: admission-correction-ci-report.md and admission-correction-ci/.

## Premerge staging refresh

Clean rebase to staging f4bac6b493a507fb80b0935e703ac6568095b236 yields
49636f902704ce6019a7a8ae47ec0b3ca6902f68, with cache owner2028283db and
prebuild owner49636f902. Ordered range-diff and stable IDs match the reviewed
original two-owner series; no manual source resolutions or added feature pins.
155 focused examples pass in1.63s; scoped Nixfmt/RuboCop and diff-check pass.
A fresh utility evaluates current-flake nixpkgs
/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source: real Nix batch-selection
specs3examples0failures (7.85s) and pure cache/module fixture exit0. No image,
VM or kernel realization. Raw commands/statuses extracted from utility JSONL to
premerge-nix-checks.json; no repeat needed. Final context/lineage review pending.
