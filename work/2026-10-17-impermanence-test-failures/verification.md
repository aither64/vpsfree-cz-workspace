# Verification evidence

Source head: `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`. Tested tree: `98fab6887104cc1aa6f05941825047b031c7c662`. Base: `0081fc01f13236a098380094ddbd00539a9c8dae`. Source worktree is clean and feature branch is published. No deployment or default-branch merge.

## Quick checks and independent review

- Full runner specs: 373 examples, 0 failures, 88 seconds (`r1-runner.log/.status`).
- Full OSVM specs: 184 examples, 0 failures, 62 seconds (`r1-osvm.log/.status`).
- Pure SquashFS flags/module wiring: passed (`ready-cache.log/.status`).
- Declared Nixfmt/RuboCop hooks passed, including enabled scoped commit/amend hooks.
- Hosted GitHub RSpec 39068521789 and RuboCop 39068521800 passed on the exact head. Native CI 39068521841 is queued at last observation.
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
