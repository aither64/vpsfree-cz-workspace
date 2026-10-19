# 2026-10-17-impermanence-test-failures

## Goal

investigate nixos impermanence test failures seen in https://github.com/vpsfreecz/vpsadminos/actions/runs/38967764636/job/117240569669

find the root cause. what are these tests for anyways?

Follow-up authorized: implement the agreed opt-in prebuild plan. Prevent selected
test image preparation from overlapping selected test VMs, preserving automatic
VM concurrency and build CPU parallelism across differently sized runners.

## Affected repositories

- vpsadminos, investigation and implementation based on failed staging revision
  `0081fc01f13236a098380094ddbd00539a9c8dae` (staging).

## Approach

- Lead inspects original job logs and uploaded native test artifacts.
- Retained architect0 traces test purpose, implementation and failure boundaries.
- Separate observed failures from inferred causes. Seek runner evidence for any
  process termination before proposing changes. Do not rerun CI as a substitute.
- Investigation follow-up: user confirmed OOM and requested resource-allocation suggestions. Actual CLI/scheduler/compressor defaults were compared before implementation was authorized.
- User clarified throughput goal: retain automatic test admission and maximize
  concurrent fitting work; preserve CPU parallelism, especially kernel builds.
  Compare every recommendation with current values. Withdraw fixed test-count
  and global CPU/Nix parallelism reductions; focus memory-accounting and bounded
  compression allocations.

## Decisions

- User authorized implementation after accepting the final staged plan.
- `test --prebuild` / `--no-prebuild` defaults off. CI opts in and provides a
  manual boolean override. No broker, new daemon, profiles or VM-overhead schema.
- Build exact selected JSON/image closures in one rooted aggregate; then load
  those immutable configs without Nix calls during runtime. Preserve filters,
  template/single-test arguments, configuration overrides and source snapshot.
- Capture the nominal ResourcePool before preparation and inject the same pool
  after preparation; do not mistake preparation file cache for unavailable RAM.
- Preparation jobs = min(inherited local Nix max-jobs, usable memory / 8192 MiB),
  with positive `--prebuild-memory-per-job-mib` override; cores unchanged,
  no memory overcommit, explicit insufficient-capacity errors and remote-only
  max-jobs=0 handling.
- `system.squashfsMemoryMiB` defaults null in production, 2048 in test config;
  both SquashFS branches pass the cache setting, retaining all CPUs and configured compression (zstd10 by default).
- Reject oversized memory requests; preserve CPU-only run-alone exceptions when
  memory fits. Cache policy and memory-limit fix are separate from staging flag.
- No merge or deployment authorization. Publish and verify the feature branch.

## Compatibility and deployment

No guest persisted-state, schema or protocol change. Existing CLI interleaving
remains available with prebuild disabled; existing metadata and external flake
contracts remain supported. Test cache sizes may change derivation identities;
production defaults remain unchanged. No coordinated host update or new daemon
configuration is required. Initial 8 GiB/build and 2 GiB/cache values are sizing
policies, not guaranteed RSS bounds. One heavy Actions job per runner and local
builds are the supported sizing domain; independent clients/remote builders are
outside the local estimate. Revert the feature or disable prebuild to recover
orchestration; cache/strict-memory changes are independently described.

## Documentation

Readers: requester, runner operators and future investigators. Keep incident
evidence in this session. Owning product explanation belongs in docs/os/testing.md,
test-runner CLI/man help, and Nix option descriptions. Architect owns design.md.
Lead applies the user-facing writing skill after technical facts settle.

## Testing plan

Meaningful Ruby specs and small Nix evaluations cover batch selection, GC roots,
prepared config loading, no VM-before-build, failure/cancel/retries, CPU settings,
memory sizing and oversized memory. Run hooks and commit intended deliverable;
independent final review precedes long tests. Use fresh Luna verification watcher
for long checks. Then validate cold/warm impermanence and representative tests
at two memory sizes where practical, preserving CPUs and stopping unexpected
kernel builds. Record actual coverage and limitations; do not infer a cold build
from a warm pass or promise arbitrary-build OOM prevention.

## Verification refinements during implementation

Independent review found incomplete preparation-side machine validation. The accepted narrow repair uses canonical OSVM parsing and existing network renderers with MAC/port allocation disabled; no duplicate schema or runtime default change. See design.md R1 refinement and review.md disposition.

Actual original fixture evaluation is expensive (~20GiB client high-water mark on this96GiB builder) and scripts are sequential. The long32GiB configured-ceiling run builds both original fixture and defaults images, then executes all13selected scripts. The planned smaller16GiB warm check selects exact cached defaults, avoiding another full giant fixture evaluation. Both are admission ceilings on one builder, not hard cgroup limits or evidence from two physical hosts. The first interrupted attempt was a monitoring false-positive on a systemd unit name; preserve it as invalid verification, not a product failure/cold success.

## Performance acceptance correction,19October

The user explicitly requires execution-time comparison with and without prebuild.
Earlier correctness and capacity runs are insufficient for that acceptance.
Measure the same full native selection at producta2ccd72d0 on one physical
builder in one job, using identical defaults/cores/guest state and warm retained
closures for both legs. Record end-to-end wall time (including evaluation and
cleanup), preparation/runtime breakdown, results and resource state. Treat one
A/B pair as exploratory and warm-cache-only; a regression cannot be excluded
from correctness evidence, failed/incomplete legs, or different-host timing.
See performance-plan.md once the architect brief is written. Benchmark-only
workflow/harness stays on a separate ref; no product behavior or integration
authority changes. No shared-store deletion or intentional kernel rebuild.
