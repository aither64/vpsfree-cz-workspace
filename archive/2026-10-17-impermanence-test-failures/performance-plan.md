# Matched full-native prebuild benchmark

Accepted execution brief, 19 October 2026. Product revision is exactly
`a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`. The existing correctness runs are
not a performance comparison. The lead has selected the previously stated
default of the full native suite after allowing time for the optional scope
answer. This benchmark changes no product code or production settings.

## Ownership and workflow

Implementer0 owns one isolated benchmark commit in the registered worktree
`worktrees/2026-10-17-impermanence-test-failures/vpsadminos-benchmark` and its
benchmark ref. Replace its existing `.github/workflows/ci.yml` with a manual-only
workflow containing one self-hosted job. Keep the product feature branch/head
unchanged. The benchmark ref and workflow SHA must be reported separately from
the exact tested product SHA. Do not merge the temporary workflow into product.

The job first checks out the benchmark ref/harness, then checks out the exact
product revision in a separate directory. Execute all product commands from
that product directory. Warmup and both measured legs stay in this one job,
which preserves runner assignment without SSH or runner-label mutation. Use
the existing prepare-test-state action and separate child state directories.
Use current repository action versions subject to the required upstream check.
The existing workflow path supports dispatch with the benchmark ref; no new
default-branch workflow registration is required.

Run meaningful pure harness/command-construction checks and hooks, commit the
complete benchmark package, and obtain independent review before dispatch.
The lead then assigns a fresh pinned Luna/low verification utility under the
monitor skill. The architect performs no builds, runs, commits, or dispatches.

## Preflight and warm-root lifetime

Record hostname, runner identity, physical-host identity when available, CPU
model/count/affinity, Nix version and effective max-jobs/cores, source HEAD/tree
and cleanliness, selected tests/scripts, memory/cgroup limits and headroom,
shared-memory capacity, disk free space, and pressure/OOM/throttling counters.
Repeat resource observations before and after each leg. Same runner assignment
does not prove absence of other host consumers.

Local inspection found approximately 100 GiB free on the shared store/tmp
filesystem, 47 GiB free shm, 96 GiB physical RAM and 70 GiB available. Earlier
local defaults/impermanence JSON symlinks now point to missing store outputs.
Therefore neither local full-suite capacity nor a warm local cache is proven;
do not launch the full comparison locally on that evidence.

On the selected CI runner, record actual filesystem free bytes, dry-run
substitution bytes and missing derivations, and managed-disk metadata before
warming. Retain the existing native prepare-state operational checks. These
observations inform capacity assessment; they are not a formal proof of peak
temporary-space usage. Concrete disk insufficiency, active
resource pressure, required uncached kernel compilation, or an unsupported
hardware-specific selection is an escalation to the lead, not permission to
delete shared store paths, change selection, reduce CPU settings, or raise limits.
Stop unexpected kernel compilation under the verification procedure. Recognize
actual kernel derivations, not any unit whose name contains “kernel”.

Preflight clarification accepted by the lead: do not add generic
`build_temp_gib` or `disk_headroom_gib` inputs or a new capacity framework.
Nix does not expose the ordinary builds' peak temporary-space requirements,
and sparse managed disks need not occupy their full logical size. Record these
unknown peaks as limitations; their uncertainty alone must not block the
benchmark. The sum of all selected logical disk sizes is not required resident
space, since the native allocator admits a subset concurrently and normal
cleanup releases completed tests' disks. The same runner class already runs
full native CI. Escalate concrete capacity/pressure evidence or an uncached
kernel requirement, preserve uncertainty about neighboring consumers, and
continue under the accepted one-job benchmark scope otherwise. This clarification
adds no design gate and changes no implementation ownership.

Use the product `.#test-runner` environment for a benchmark-only orchestration
helper. The helper opens `RepositorySource.open`, selects the full native suite
using `TestScriptList` and the existing `Cli::TagFilters` for `ci`, then opens
`Prebuild` with the ordinary `ResourcePool` and configuration. Hold BOTH existing
`RepositorySource.open` and `Prebuild.open` blocks across both external CLI
children. This retains all selected warm JSON/image closures and their source
without a new root protocol. Do not instantiate Executor in the warmup helper.
Do not pass its prepared objects to the measured children. Retain roots until
both children and their native VM cleanup finish, including failure handling.

Warmup includes environment/package preparation and realizing the selected
aggregate. Record its wall time and any downloads/builds separately. Verify all
selected JSON/image paths exist before leg A, retain the manifest/selection in
artifacts, and verify that neither measured leg builds missing image closures.
Warmup may build ordinary missing images outside measurement; it may not
intentionally rebuild a kernel. Package preparation may run the standard
test-runner package build outside measurement so its normal CLI package check
is warm for both legs.

## Exact measured comparison

Use stable native CI configuration: `VPSADMINOS_CONFIG` empty,
`tests/test-configs/ci.nix`, `x86_64-linux`, tag `ci`, no pattern, no optional
proxy/full-ZTS overrides. Record any relevant inherited environment explicitly.
The previous native selection was 127 tests/335 scripts; verify equality of the
actual selection in warmup and both legs instead of relying only on that count.

From the exact product checkout, run these external commands sequentially:

```sh
# A: current preparation lifecycle disabled
./test-runner.sh test --no-prebuild --jobs auto \
  --test-config tests/test-configs/ci.nix --system x86_64-linux \
  --fresh --state-dir "$BENCH_ROOT/A-state" -t ci

# B: preparation lifecycle enabled
./test-runner.sh test --prebuild --jobs auto \
  --test-config tests/test-configs/ci.nix --system x86_64-linux \
  --fresh --state-dir "$BENCH_ROOT/B-state" -t ci
```

`BENCH_ROOT` is the job's isolated state root. Both state directories start new.
Keep production defaults: 8 GiB host/shm reserves, memory factor 1, CPU factor
1.5, automatic runtime jobs, inherited Nix cores/max-jobs, and the existing
adaptive prebuild estimate. No local 32 GiB clamp, fixed job cap, CPU limit,
timeout increase, or weakened assertion. Set the same effective environment for
both legs; only the prebuild flag and isolated output/state names differ.

Measure each entire `test-runner.sh` process from spawn through exit using a
monotonic clock, capturing its true exit status. This includes package check,
source snapshot resolution, selection/evaluation, preparation, runtime and
cleanup. Capture complete stdout/stderr plus passive receipt timestamps for
phase markers. Environment setup and warmup remain outside both leg timers.
Do not monkey-patch product methods, scheduling, random order, or resource
detectors. Small harness implementation choices belong to the implementer.

Report total wall time; CLI prefix until Executor's “Running ... scripts” line;
the executor's reported elapsed runtime; and cleanup/tail interval where
observable. For B additionally report the “Preparing ...” to “Preparation
complete ...” interval. This B interval includes aggregate evaluation/build
checks, not a pure compressor duration. For A, per-test evaluation/preparation
overlaps the executor span: do not call it VM-only runtime or pretend there is
an equivalent isolated global preparation phase. Optional per-test
admission-to-first-script timing is only a provisioning proxy. Label
log/receipt-derived timings and their precision; they need not sum exactly to
the monotonic total because output can buffer. Exact subprocess tracing is not
required and should not expand this benchmark.

## Failures, cleanup, order, and acceptance

Do not use stop-on-failure: complete each selected suite and retain every result.
Capture a failed A exit without skipping B, but start B only after A's owned
runner, QEMUs and build clients have ended and native cleanup has completed.
If owned processes remain, cleanup is uncertain, resources are exhausted, or
the job is cancelled, escalate and mark the pair incomplete. Never kill another
job's processes or treat forced cleanup as a normal completed measurement.
Keep always-run artifact upload and bounded owned cleanup handling; no VM or
active build may overlap the next leg. Release warm roots only after owned
children are accounted for. Preserve logs, status, timings and resource samples.

Start with one A/B pair. The executor and scripts shuffle without a fixed public
seed, and filesystem caches, thermal state, network fetches inside guests, and
neighbors vary. Therefore the pair is exploratory. If it suggests a regression,
the lead may authorize a balanced B/A repeat where runtime/resources permit;
do not automatically launch ABBA. Set the reviewed job deadline with room for
warmup, both full legs, cleanup and upload within platform/token limits. A
deadline is an incomplete measurement, not a passing comparison.

Publish A and B wall seconds, delta `B - A`, ratio `B / A`, and percent change
`100 * (B / A - 1)`, with phase timings, per-test results and capacity snapshots.
The known predecessor `upgrade/from-6.18-guests` capability failure and possible
900-second cleanup timeout can materially distort elapsed time. Unequal
failures/executed work or capacity drift prevent a clean suite-time conclusion;
report these effects and compare common completed work only as secondary data.
No numerical regression threshold was agreed: report the measured size and
uncertainty instead of inventing a pass threshold or declaring equivalence
from one pair.

This same-head flag-only comparison isolates orchestration with warm Nix
closures. Both sides retain the new deterministic test-image cache policy and
strict memory admission. It does not compare the old cache default, predict
cold image-build/VM overlap performance, or establish arbitrary-build memory
safety. Historical timings on another builder are context only. Product branch,
accepted design, guest requirements, and application code remain unchanged.
