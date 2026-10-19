---
lifecycle: active
---

# 2026-10-17-impermanence-test-failures

## Status

Implementation is complete, independently reviewed and checked for correctness.
Performance acceptance remains open: user requested a matched execution-time
comparison with and without prebuild; the prior runs do not supply that comparison. The
feature branch is published at `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`.
All 12 original impermanence scripts plus defaults passed; cached defaults also
passed with a smaller configured memory ceiling. Native GitHub CI finished with
126 passing test groups and one failure in upgrade/from-6.18-guests. Diagnosis
found a capability-denied NixOS22.11 guest service on the pinned predecessor,
before any upgrade; no evidence warrants a resource implementation change.
No default-branch integration or deployment has been authorized or performed.
The session remains open.

## Phase checklist

- [x] Verify the exact session identity and saved same-session team.
- [x] Investigate the original shared fixture build failure and test purpose.
- [x] User confirms OOM; compare proposals with actual runner defaults.
- [x] Accept opt-in staged preparation and architect-owned design brief.
- [x] Implement, pass quick checks/hooks and commit logical owners.
- [x] Independent final review, history/migration inventory and R1 repair.
- [x] Build selected images and pass all 13 selected scripts.
- [x] Pass cached representative test at the smaller configured ceiling.
- [x] Publish exact final source head and capture native comparison.
- [x] Native GitHub CI completes; OS build passed, native suite has one failure.
- [x] Diagnose upgrade/from-6.18-guests failure and record its separate scope.
- [ ] Matched with/without-prebuild timing comparison (architect0 planning).
- [ ] Overall CI remains red; six livepatch profiles also lack executed coverage.
- [ ] Explicit integration direction, if requested later; no merge approval exists.

## Next action

Architect0 owns a matched benchmark brief (performance-plan.md). Measure total
wall time and preparation/runtime breakdown at identical source, selection,
builder, limits, CPU settings and fresh VM state; keep Nix cache conditions
explicit. Proceed with the stated full-native default after the optional scope question
received no answer. Local full-suite outputs are no longer present and only
about100GiB disk is free, so use one self-hosted CI job for both legs.
A separate same-session vpsadminos-benchmark worktree/ref holds only temporary
benchmark orchestration; both legs checkout producta2ccd72d0 exactly. Architect0
owns the brief, implementer0 the harness, reviewer0 the required final check,
and a fresh Luna/low watcher the eventual run. No benchmark has started yet.
Existing correctness evidence does not establish performance parity. No merge or
deployment has been authorized; leave the session/worktrees/refs open.

## Source and complete history

- Repository: `vpsadminos`, canonical remote `git@github.com:vpsfreecz/vpsadminos.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-17-impermanence-test-failures/vpsadminos`.
- Branch: `2026-10-17-impermanence-test-failures`, published to the same remote branch.
- Initial/review base and current origin/staging: `0081fc01f13236a098380094ddbd00539a9c8dae`.
- Final head: `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`.
- Exact tested final tree: `98fab6887104cc1aa6f05941825047b031c7c662`.
- Worktree/index clean; remote feature head matches. Final fetch confirmed staging
  remains at the reviewed base. Native comparison was captured after amendment.

Complete base-to-head series, oldest first:

1. `5acb08db650a0c72d3b00ab66cbdd9da6b50eb46` — test-image SquashFS cache option.
2. `09fb4131d65926e7490829d5a278b3d162fac44d` — strict RAM/shm admission.
3. `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1` — opt-in preparation and supporting
   exact-config/root/selection/CI/docs/tests, including the narrow R1 repair.

Three coherent owners; no obsolete approaches, fixup/repair residue, migrations,
transitional state formats, dependency/pin streams or generated update streams.
First two owners remained unchanged through R1. The amended final tree exactly
matches the frozen fully tested repair tree. No migration was merged, released,
deployed or externally consumed because there are no migrations.

## Delivered behavior and compatibility

`test --prebuild` is opt-in; `--no-prebuild` disables staging. Native CI enables it
and its manual boolean can explicitly disable it. All selected config/image
closures finish before any selected VM; runtime and retries consume exact rooted
configs without Nix. The pre-preparation ResourcePool is retained for runtime.

Preparation jobs scale with detected available/assigned memory, configured maximum
and the existing 8192 MiB reserve, divided by the overridable positive 8192 MiB/job
estimate and capped at inherited Nix max-jobs. Zero remains remote-only. Runtime
`--jobs auto`, CPU factor 1.5 and build cores/processor parallelism are unchanged.
Test-image compressor cache defaults to 2048 MiB; production defaults to null.
RAM/shm oversize requests fail finitely, while memory-fitting CPU-only exceptions
remain supported. Cache/admission policies are independent of the staging flag.

No guest-state/schema/protocol migration or coordinated node update. Existing
metadata, legacy/debug behavior and external tests/testsMeta-only exports remain
supported. Representative vpsAdmin HEAD `b4ef8535a629ee8c9cd753afecdb05e0895d0eea`
pins vpsadminos `8e44a5124439b1f3048ffc56b1717614a5360358`; it does not re-export
lib.testFramework. Consumer/pin code changes were unnecessary.

## Verification

See [verification.md](verification.md) for commands, timing, capacities, exact
store-path reuse, phase boundary, root lifetime, measurements and limitations.

- Full runner: 373 examples, 0 failures (88 seconds).
- Full OSVM: 184 examples, 0 failures (62 seconds).
- Pure SquashFS flags/module wiring and declared Nixfmt/RuboCop hooks pass.
- Enabled hooks ran for every commit/amendment; no bypass.
- 32 GiB configured ceiling: 3 prep jobs, unchanged 96-vCPU runtime budget;
  both new images compressed with 64 processors, zstd10 and explicit `-mem 2048M`.
  All 12 unique impermanence scripts plus defaults passed, exit 0. Runtime
  5955.47 seconds. No VM began before both configurations were prepared.
- 16 GiB configured ceiling: 1 prep job, same CPU settings, same cached defaults
  JSON/image, unchanged 8 GiB guest; passed, exit 0 (261.7 seconds).
- Owned preparation roots remained during runtime and disappeared after complete
  VM cleanup. Both owned command processes exited; no local verification remains.
- Final job cgroup max/oom/oom_kill event counts are zero.
- GitHub exact-head RSpec39068521789 and RuboCop39068521800 succeeded.
- Native CI39068521841 failed: OS build passed; native suite126 test groups passed/1 failed
  (upgrade/from-6.18-guests); four livepatch jobs passed and six jobs that never
  started were cancelled after24h. Original logs/artifacts downloaded; architect0 traced the failure to
  network-setup.service exit218/CAPABILITIES on NixOS22.11 before the upgrade.
  Its fixture and capability policy are unchanged by this branch:
  https://github.com/vpsfreecz/vpsadminos/actions/runs/39068521841

The local ceilings were admission settings on one 96 GiB/64-CPU builder, not
enforced cgroups. Native CI adds a second physical builder:100GiB/48CPUs,
11 adaptive prep jobs and unchanged72-vCPU runtime capacity; all12 persistence
scripts passed there too. Evaluator client high-water mark was about
20 GiB; no aggregate daemon peak was measured. The per-job estimate and cache size
are policies, not RSS caps or an arbitrary-build OOM guarantee. Dependency caches
were partially primed; both selected images were actually compressed. No fully
cold closure or same-full-fixture warm repeat is claimed. The smaller warm check
used defaults to avoid repeating the large fixture's evaluation and long scripts.

## Independent review

[review.md](review.md) records reviewer0's all-four-lane review and lead decisions;
[review-packet.md](review-packet.md) contains the complete history/consumer packet.
Retained reviewer0 used saved gpt-6.1-sol/xhigh/read_only, no override/fallback.
Risk high because of host resource/public framework behavior.

One Important R1: partial TestConfig validation could admit malformed later
machines and allow earlier fresh disk reset. Fixed by sharing canonical OSVM
parser/network rendering with MAC/port allocation disabled. Regressions prove
valid-first/invalid-later rejection before Executor, VM/disk/global allocation,
including expectFailure. Full suites and scoped hooks passed on the exact repair;
lead directly verified this narrow requested fix under review steps 9–10. No new
contract or scope expansion requiring unaffected-lane reruns. Repair was folded
into the preparation owner; first reviewed head `fac4fe226` and original diff
receipts remain recorded in the review artifacts.

## Original incident and setup evidence

User confirmed the original build was OOM killed. One shared fixture image failed
before any VM/assertions; 12 reported script failures followed that single build
failure. The tests protect UID/GID maps, account IDs, payload integrity/ownership,
machine-id and bind metadata through compatibility-module adoption, activation
and restart. They retain each scenario's NixOS release/stateVersion22.11; the old
pin `1150e37b1cc997b1728f2fda806a3433ef55b798` is compatibility source, not a release
upgrade. [source-investigation.md](source-investigation.md) preserves source lines
and original evidence. Runner SSH keys were refused and physical host key was
untrusted; no trust bypass or exact victim/aggregate peak claim.

A utility accidentally stopped the first long attempt on a systemd unit named
sys-kernel-debug after960seconds; parent confirmed no kernel compile. That TERM
attempt is invalid verification, not a product failure/OOM. Corrected retry used
visible parent monitoring because fresh utility invocation was unavailable.
Slow guest boot (~7m10) eventually reached userspace/shell within900seconds; no
boot fix/timeout change was made. No kernel was intentionally rebuilt.

Fresh worktree hooks needed install/sign; native Ruby specs needed the existing
CI libosctl extension recipe and -Itest-runner/spec. Incorrect initial harness
commands ran zero examples. Nix fixture context-parsing errors were test-only
and fixed while retaining production references. Hook signature during ambient
push required signing/pushing in the declared Nix environment, without bypass.
Known lessons already live in notes/vpsadminos/2026-07-04-test-runner-rspec-local.md
and 2026-06-03-overcommit-nix-env.md. Official action versions were verified;
compatible existing @v7 refs retained (checkout7.0.1/upload-artifact7.0.2).

## Artifacts and ownership

- [plan.md](plan.md), architect-owned [design.md](design.md), [verification.md](verification.md).
- [native-ci-follow-up.md](native-ci-follow-up.md): exact CI failure and scope.
- Original job.log/native-logs.zip/ci-logs; review diffs and frozen quick receipts.
- r1-runner/r1-osvm/ready-cache logs/status; integration-retry-32g and integration-16g
  logs/status; image-preparation.log, warm-preparation.log, compressor-sample.txt,
  compact expected_success results and final-job-memory-events.txt.
- Transient whitelisted runner-nix-env.sh/hooks-nix-env.sh are local environment
  receipts only; do not publish/commit them. No credentials were captured.
- Native test-state directories: /tmp/os-test-2026-10-17-impermanence-test-failures-32g
  and -16g. Managed VM disks were removed by normal runner cleanup. Logs retained;
  no manual session/worktree/branch deletion, archival or stop requested/performed.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-17-impermanence-test-failures/

## Performance comparison ownership

- Benchmark-only worktree: worktrees/2026-10-17-impermanence-test-failures/vpsadminos-benchmark.
- Benchmark-only ref: 2026-10-17-impermanence-test-failures-benchmark, initiallya2ccd72d0.
- This ref is not part of the product integration request. Product branch stays unchanged.
- Hooks installed/signed in declared Nix environment; retry registered the worktree
  after the known inherited post-checkout signature refusal. No hook bypass.
- Architect brief is written/accepted and registered. Implementer0 committed the temporary workflow/harness and focused specs as
  4a3e43347ffe9913b330a97fd297d7e64db51d50 (treeb153c396a52f1bd7e9e72317de7dc67e8eeda2fa).
  11 focused examples, YAML/bash syntax and hooks passed; source/index clean.
  Lead final prose pass and actual admission-ceiling comparison are included.
  Retained reviewer0 completed all-four-lane final review; benchmark-review.md
  records two Important measurement findings (guest builds misclassified as host
  builds; transient runtime capacity changes ignored). Both accepted and assigned
  to implementer0 for narrow fixes/regressions/amendment. Lead directly verified both narrow fixes and meaningful regressions under
  review steps9–10. Final amended benchmark06915925a7a63a2fac7135a752101228b5b699e0,
  tree771895324cfc498413a8eb801ac0b0b9bac5fb4b;13 examples0failures, hooks pass,
  clean worktree. Review gate satisfied; publication/dispatch next.

## Active matched timing run

Benchmark-only head06915925a7a63a2fac7135a752101228b5b699e0 was published over
SSH after independent review and direct R1/R2 verification. No rebase onto a
new product revision: exact producta2 is the deliberate benchmark boundary.
Native comparison captured full inherited range from0081fc01 to06915925a.

Dispatched manual CI39276852536 at2026-10-19T15:18:40Z:
https://github.com/vpsfreecz/vpsadminos/actions/runs/39276852536
Initially queued; one job, exact producta2 for both CLI legs, full native335
scripts/127 groups, warm roots retained, A(no-prebuild) thenB(prebuild), auto jobs
and production CPU/memory settings. No timing result yet.

Fresh utility /root/prebuild_benchmark_ci_watch owns monitoring this exact run
and head, resolved from retained verification_watcher gpt-6-luna/low and utility
identitydw_024841fba072af1d79bd78026612eaeca055acfa31ecc89f; current installed
execution_access=full_access. No retained-member reconfiguration. Follow monitor
skill; original product branch unchanged. Root will interpret artifacts and
report totals/deltas after completion, not infer performance from correctness.
