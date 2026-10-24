# Prepare selected test images before starting VMs

The separate [matched performance benchmark brief](performance-plan.md) defines
the accepted same-head, warm-cache full-native A/B comparison. Its temporary
workflow lives only on the session's benchmark ref and changes no product code.

Status: implementation brief approved through the lead on 2026-10-17. The user
authorized implementation. This document records the agreed scope; it does not
authorize merge, deployment, or session closure.

Accepted correction, 2026-10-20: the user rejects strict refusal of oversized
runtime requests and wants the runner to attempt them. Restore the baseline
run-alone fallback for memory, shared memory, and CPU. The previous strict
memory-refusal decision is superseded throughout this brief. Under this policy,
failure or OOM is a signal to investigate and fix the fixture, rather than a
reason for a new admission toggle, retry policy, or OOM-handling framework.

Benchmark run `39305352549` measured product
`a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`, which still included strict refusal.
Its [results and qualifications](benchmark-results-analysis.md) remain receipts
for that exact revision; restoring the fallback produces a later product head
and does not relabel the completed measurement.

Design owner: architect0. The lead assigns application implementation and owns
tracking, review coordination, and acceptance. This assignment changes only this
document. The session is `2026-10-17-impermanence-test-failures` in
`/home/aither/workspace/ai/vpsfree.cz`.

## Problem and intended result

At staging `0081fc01f13236a098380094ddbd00539a9c8dae`, the impermanence fixture
failed while building its squashfs image, before starting a VM. The user confirmed
an OOM kill; the killed process and peak memory are not established. Twelve script
failures were consequences of that shared preparation failure, not failed
impermanence assertions. See [source investigation](source-investigation.md)
for incident evidence and the earlier, superseded proposals.

The current executor reserves guest RAM while each evaluator builds its test
configuration. Several image builds can therefore compete with running VMs.
The squashfs builder also leaves its cache size at the tool default, which the
pinned squashfs-tools 4.7.5 derives from physical RAM rather than cgroup capacity.

Add an optional preparation phase that builds every selected test configuration
and its image dependencies before starting any selected test. Nix reuses cached
paths and shared dependencies; the runner does not predict the dependency graph.
Keep automatic VM scheduling, CPU overcommit 1.5, and existing kernel/build CPU
parallelism. Bound the known squashfs cache contribution and choose preparation
concurrency from the builder's available memory.

This deliberately gives up preparation/VM overlap. It is a bounded remedy for
the observed competition, not a proof that arbitrary Nix derivations cannot OOM.
There is no daemon change, broker, resource controller, calibration database,
per-test memory profile, live pressure sampler, or new VM-overhead schema.

## Interfaces and defaults

| Interface | Agreed behavior |
| --- | --- |
| `test --prebuild` / `--no-prebuild` | Preparation phase enabled/disabled; default disabled. Applies to `test`, not `debug`. |
| `--prebuild-memory-per-job-mib` | Positive integer, default 8192; estimate used to select preparation concurrency. |
| Existing `--jobs auto` | Unchanged automatic runtime scheduling; preparation jobs are a separate value. |
| Existing memory maximum/reserve | Honored by preparation sizing; reserve is subtracted after applying the maximum. Default reserve remains 8192 MiB. |
| Existing CPU options and Nix `cores` | Unchanged, including livepatch exceptions. No new CPU or global Nix limits. |
| `system.squashfsMemoryMiB` | New optional positive integer; default `null` retains the production tool default. |
| Test vpsAdminOS base module | Sets `system.squashfsMemoryMiB = lib.mkDefault 2048`; explicit module override, including `null`, remains possible. |
| CI dispatch input | Boolean enabling preparation, default true; explicit false disables preparation. Push/PR CI enables it. |

`--no-prebuild` restores per-test preparation. It does not undo the independent
test-image cache default. Both modes retain the baseline oversized-test
run-alone fallback. State these boundaries in help, the man page, and testing
documentation.

## Preparation and runtime boundary

1. Enter the existing repository snapshot lifetime. Resolve effective source,
   system, test configuration, and selection once. Preserve patterns, tags,
   labels, metadata expressions, script selectors, single-test arguments, and
   template instance arguments. Normalize configuration paths through the
   existing snapshot resolver; avoid rereading a moving repository at runtime.
2. Deduplicate selected scripts into test identities containing the effective
   test path and arguments. Selecting several scripts of one test prepares its
   configuration once. An empty selection performs no preparation build.
3. Capture the nominal `ResourcePool` before preparation, with zero reservations.
   Calculate the separate preparation concurrency from current available memory.
   Do not construct an executor or start an evaluator/VM during preparation.
4. Invoke one `nix-build` for an aggregate derivation whose output is a manifest
   mapping selected test identities to their exact test JSON store paths. Keep
   Nix string references intact so realizing and rooting this manifest also
   realizes and roots every selected JSON and its referenced image closure.
5. Validate the manifest and load the selected JSON configurations. Missing,
   duplicate, or unexpected identities and invalid configurations are preparation
   failures. Check selected scripts against the prepared configuration before
   machine construction or destructive disk reset.
6. Only after complete success, construct `Executor` with the captured pool and
   the prepared configuration mapping. Refresh assigned capacity limits once
   before admitting VMs, using the existing monotonic memory-capacity behavior.
7. Pass each exact prepared configuration through evaluator construction and
   retries. In this mode, evaluator loading must not invoke Nix, re-evaluate a
   test, or silently fall back to building a missing output. Keep the aggregate
   root through all attempts, VM termination, cleanup, and result publication.

The runtime promise covers preparation performed by the test runner. A test
script or extension that explicitly launches a separate host build is outside
that promise and must be identified if encountered. Existing workflow fixture
builds that run before the test-runner invocation remain before all VMs.

### Resolver compatibility

The batch resolver must share the single-test resolver's effective context, not
invent a second selection language. Registered native tests, templates, and
direct single-test fallback must preserve arguments and effective
`VPSADMINOS_CONFIG`/`--test-config` behavior. Do not blindly select native
`flake.tests` when that export would discard the active configuration.

External consumers may export only `flake.tests` and `flake.testsMeta`, without
`flake.lib.testFramework` or a repository-local `test-runner/nix/lib.nix`.
Use their registered exports in that case. Retain the existing requirement for
framework exports when `--test-config` is used. A real source-layout check must
guard native direct-import fallback; a matching `tests/suite` path alone does
not prove that a consumer has the native helper. No downstream repository or
external framework API migration is required.

### Capacity snapshot

Keep the existing startup-headroom contract: available memory is sampled before
preparation, and subsequent refreshes follow assigned limits. Inject the same
pool object instead of constructing a new pool from post-build availability.
Image builds can leave reclaimable file cache charged to the cgroup; sampling
`limit - current` immediately afterwards can otherwise strand capacity.

Do not add inactive-file credit arithmetic or subtract current RSS from the
remaining nominal reservation budget. The initial snapshot is not a claim about
post-preparation free RAM. The existing 8 GiB reserve remains the allowance for
host/QEMU overhead; its adequacy for every possible suite is not established.
Unrelated post-start memory growth and unmanaged competing Nix clients remain
outside this scheduler's accounting. The supported CI assumption is one worker
job per runner container and no competing test invocation/build workload.

## Preparation memory algorithm

Read effective inherited Nix local `max-jobs`, including normal configuration
and environment precedence. Resolve `auto` according to Nix semantics. Preserve
an explicit numeric setting; do not additionally clamp it to `nproc`.

For local builds, let `A` be the minimum available host/cgroup headroom detected
before the build, bounded by detected assigned capacity and an explicitly
configured runner memory maximum. Apply existing maximum/reserve ordering:

```text
usable = max(0, A - memory_reserve_mib)
estimate = prebuild_memory_per_job_mib       # default 8192
memory_jobs = floor(usable / estimate)
J = min(effective_inherited_local_max_jobs, memory_jobs)
```

Do not apply the runtime memory-overcommit factor to this calculation. Unknown
headroom without a usable explicit capacity must give an actionable error,
rather than silently choosing unbounded concurrency. When local builds are
enabled and `usable < estimate`, stop with a clear sizing error; do not coerce
zero into one. Log all inputs, their origins, and the resulting `J`.

Pass `--max-jobs J` only to the aggregate preparation build. Do not change global
Nix configuration, `--cores`, `NIX_BUILD_CORES`, processor flags, or kernel make
parallelism. Honor inherited `max-jobs=0` as remote-only/substitution behavior:
preserve zero, do not apply a local minimum-one rule, and explain that local
headroom does not size remote builders. Remote execution follows existing Nix
configuration; it supplies no local or remote memory guarantee.

8192 MiB is a common, overridable admission estimate, not a derivation RSS cap.
One derivation may exceed it or run multiple memory-intensive subprocesses.
Do not promise a guaranteed 6 GiB margin beyond a 2 GiB compressor cache.
Substitution, evaluation, and daemon overhead are not exact per-job reservations.

## Squashfs cache and oversized runtime requests

Add optional `memoryMiB` to `os/lib/make-squashfs.nix` and propagate the module
option through both system-root and installer-image call sites. Emit an explicit
`-mem` value only when configured, with the tool's MiB-equivalent units. Apply it
to both the `sqfstar` and `mksquashfs` branches. Keep all available processors,
zstd level 10, the existing block size, and filesystem ownership/metadata behavior.

The 2048 MiB test default is deterministic across hosts, avoiding host-dependent
derivation variants. It bounds the compressor cache, not total RSS: metadata,
compression contexts, dictionaries, and other processes consume additional RAM.
Production module configuration defaults to `null`; this is not a production
compression-policy change. Old pinned OS sources and unrelated Nixpkgs builders
do not automatically acquire this new option or cache default.

Preserve the baseline executor fallback in both preparation modes: normal
admission uses the configured memory, shared-memory, and CPU budgets; if no
pending test fits and no test is running, admit the first pending test alone
despite its oversized request. An oversized request must not cause a new
resource refusal or wait forever solely because it cannot fit those budgets.
This includes intentional large-vCPU livepatch cases and memory/shared-memory
requests. While tests are running, retain the normal admission checks.

Keep the actual requested resources reserved and reported. Do not clamp guest
RAM, shared-memory requirements, or CPU counts, enlarge nominal limits, or alter
disk state to make the request appear to fit. This fallback can exceed the
runner's nominal budget and can OOM; that consequence is part of the user's
requested attempt-and-diagnose policy. Preparation sizing and its insufficient
local-build-memory error remain unchanged, as do canonical configuration
validation, root lifetime, cancellation, and existing runtime failure reporting.

## Failure, cancellation, roots, and logs

Preparation failure is an infrastructure/build failure and starts zero selected
VMs. It must not produce fabricated assertion failures for every selected
script, nor become successful through `expectFailure`. Record the preparation
phase, complete build log location, selected identities, and ordinary exit code
or terminating signal. Correct the current nil-exitstatus diagnostic.

Handle interruption while waiting for the aggregate build: forward cancellation
to the owned client/process group as appropriate, reap it, and do not enter
runtime. Nix daemon work may be shared with another client; do not kill the
global daemon or unrelated builds. Preserve useful logs on failure.

Use unique invocation-owned root locations and the existing source/root and test
state locking conventions. Never replace another invocation's root. Normal
release occurs only after owned build clients and runtime cleanup finish.
Crash leftovers use the existing ownership-aware stale-root convention; no
hostwide ledger, cleanup daemon, or PID-only deletion scheme is introduced.
Retrying the command can reuse valid store outputs. Disk lifecycle and `--fresh`
semantics begin in the runtime phase exactly as before.

## Implementation packages and source boundaries

The lead serializes overlapping edits and Git operations and assigns only
retained implementation members. These are boundaries, not new assignments.

| Package | Files and responsibility | Dependency |
| --- | --- | --- |
| Runner orchestration and resolver | `test-runner/lib/test-runner/cli/{app,command}.rb`, `nix_cli.rb`, `test_config.rb`, `test_evaluator.rb`, `executor.rb`, `resource_pool.rb`, `repository_source.rb` as needed; `test-runner/nix/evaluate-tests.nix`; focused adjacent specs | Main implementation; preserve source/config resolution and root ownership |
| Cache option | `os/lib/make-squashfs.nix`, `os/modules/system/activation/top-level.nix`, `os/modules/installer/cd-dvd/iso-image.nix`, `tests/configs/vpsadminos/base.nix` | Independent of runner source, but combined acceptance checks |
| CI and explanation | `.github/workflows/ci.yml`, `docs/os/testing.md`, `test-runner/man/man1/test-runner.1.md`, CLI help | Use finalized option names and behavior |

A small preparation helper/class may be added inside `test-runner` if it keeps
root ownership and the phase transition clear. Avoid general scheduler
abstractions or exposing an unnecessary persistent manifest protocol.

Reference points at the failed staging SHA: `cli/command.rb:23` begins current
test orchestration; `executor.rb:49` constructs the resource pool;
`resource_pool.rb:50` captures initial available memory;
`executor.rb:227` contains scheduling and the oversized bypass;
`test_evaluator.rb:50` begins configuration preparation;
`test-runner/nix/evaluate-tests.nix:38` begins native direct resolution;
`tests/make-test.nix:324` exports resource metadata and `:365` writes the JSON
derivation. The lead verifies the actual implementation base before edits; do
not use a foreign worktree or silently assume staging has not advanced.

## Compatibility, rollout, and recovery

Existing callers default to the current preparation lifecycle. Existing test
JSON/resource metadata remain readable, and external exports need no new
fields. Prepared manifests are invocation-local implementation data; there is
no database, guest-state, API, or persistent on-disk format migration.

CI enables preparation in native test invocations, including the existing
livepatch lifecycle invocations, while retaining their selectors, timeouts,
serial job choices, and 128-vCPU exception. A dispatch boolean defaults to true
and explicitly disables it when false. Avoid Boolean/string fallback expressions
that turn an explicit false back into true. Do not add or update action versions
incidentally; follow the upstream-version procedure for any required change.

Changes do not require coordinated updates of running vpsAdminOS machines.
New runner behavior is selected by the source/package used for that invocation;
the new module option is used only with sources that define it. Do not inject it
into historical pinned OS modules that cannot recognize it. Reverting the runner
or using `--no-prebuild` restores the previous orchestration, and reverting or
overriding the test base option restores its previous compression policy. No
guest data conversion is required. The restored oversized-test fallback retains
the baseline runtime compatibility contract for suites that exceed nominal
memory, shared-memory, or CPU budgets. It adds no CLI switch, metadata field, or
new recovery mechanism.

## Acceptance and verification brief

The implementation must demonstrate these behavioral contracts with meaningful
specs and focused evaluation, before long integration verification:

- CLI default/off/on behavior, positive estimate validation, dispatch false
  preservation, and unchanged CPU/cores arguments.
- Batch selection for ordinary tests, multiple scripts of one test, explicit
  arguments, templates, native configuration overrides, and an external flake
  with tests/testsMeta but no native helper/framework export. Compare effective
  selected configurations against the existing supported single-test behavior.
- Aggregate reference closure/root lifetime; no evaluator or VM start before
  complete batch success; exact prepared-config reuse on retries; no runtime
  Nix invocation; invalid/missing manifest entries fail before disk mutation.
- Build error and signal/cancellation paths start zero VMs, preserve diagnostics,
  release only owned roots after cleanup, and do not fabricate script results.
- Memory sizing across at least two detector capacities, maxima and reserves,
  inherited numeric/auto/zero max-jobs, unavailable detection, and insufficient
  memory. Verify the same pre-preparation pool is used at runtime and assigned
  limit decreases remain honored.
- Baseline run-alone fallback for oversized memory, shared memory, CPU, and
  combined requests when the pool is idle and no pending test fits; retain
  normal budget checks while tests are running. Verify unchanged behavior in
  both preparation modes and preservation of raw requested resources and
  nominal limits. Use focused scheduler specs; deliberately causing host OOM is
  not needed to verify this policy correction.
- Both squashfs branches receive the configured cache argument; production null
  omits it, test defaults are overridable, and processor/compression settings
  remain unchanged. Use a small Nix evaluation for selection/option wiring rather
  than building OS images as a quick check.

Implementers run the relevant runner specs and repository formatting/hooks in
the declared Nix environment. Complete and commit the intended deliverable with
hooks enabled. The lead then obtains mandatory independent final review of the
complete branch, including history and the explicit absence of migrations,
before starting long integration runs. This document itself is planning, not a
request for an early review assignment.

After review, a fresh Luna/low verification utility runs and monitors authorized
long checks under the monitoring skill. Exercise the original impermanence
fixture and a representative selected suite, cold and warm where practical,
across at least two accessible memory sizes with CPU resources unchanged.
Retain phase timings, chosen preparation jobs, capacity inputs, compressor cache
settings, build failure/signal diagnostics, available memory observations, and
OOM evidence where accessible. Label sampled maxima as sampled; client RSS is
not daemon build RSS. Record VM start ordering and exact prepared-path reuse.

Cold means necessary test images are absent from cache where safely practical;
it does not authorize deleting shared store paths or intentionally rebuilding a
kernel. Stop unexpected local kernel builds and investigate substitutions under
the verification procedure. If a second resource size or reliable peak data is
unavailable, report the gap instead of claiming measured safety. Revisit the
8192 MiB estimate or 2048 MiB cache only from evidence and through the lead.

Readiness requires passing applicable quick checks, completed final review,
reported integration results and limitations, and accurate user documentation.
Successful tests do not authorize merge or deployment. The session remains open.

## R1 refinement: canonical validation before runtime

Final review of implementation head `fac4fe226` found that the preparation
validator copied only part of `OsVm::MachineConfig`'s contract. For example,
`testShells = 0` or a bridge network with empty `opts` could pass preparation.
The evaluator constructs machines in order and performs `--fresh` disk reset
inside that loop, so a valid earlier machine could lose its disks before a
later invalid machine was rejected. This repair completes the existing
pre-runtime validation boundary; it does not introduce another subsystem.

Add a narrow `OsVm::MachineConfig.validate_config!(raw)` entry point. It uses
the existing `from_config` spin dispatch and the same machine, disk, CPU, and
network constructors, with an internal `allocate_resources: false` mode.
Propagate that keyword through the existing constructors/factory methods;
ordinary `from_config`/`load_file` retain allocation by default and unchanged
runtime behavior. Do not copy field lists, constraints, or per-spin schemas into
another validator.

The validation mode suppresses only actual global allocation operations:
`MacAddressGenerator.next_mac`, `MacAddressGenerator.register_mac`, and
`PortReservation.get_port`. It still resolves and normalizes supplied MAC
values, selects network subclasses, checks socket port value types, and executes
the existing constructor checks for shells, roots, disks, and bridge options.
Keep unallocated network values local to the disposable validation object.
No random MAC generation, registry mutation, port reservation, lock-file work,
or VM construction is allowed during this pass. Do not achieve this with global
mocking, temporary monkey-patching, allocate-and-undo, or a new worker process.

After construction, the canonical validation entry point must invoke each
network's existing `qemu_options` renderer and discard its result. At this head,
`UserNetwork#qemu_options` performs the required option fetches, so running only
the constructors is insufficient. These renderers build strings and do not
execute QEMU or allocate resources when their validation-only inputs have already
been parsed. Do not add a second list of user-network option names. This scope
does not attempt to validate arbitrary extra QEMU arguments or resource
availability on the host.

`TestConfig.validate!` retains test-envelope/selected-script checks and its
distinct admission sanity checks for positive guest memory/CPU counts. Replace
its duplicated machine-specific validation list with the canonical entry point.
Do not extend the normal MachineConfig contract with unrelated new restrictions
to preserve a duplicated preparation-only field list. Validate every machine
of every prepared configuration before `Prebuild.load_manifest` yields to the
executor. The evaluator may repeat the same pure validation defensively, but
must never be the first place a selected configuration is validated.

Do not save validation-only MachineConfig instances as runtime machine configs.
Keep the original prepared JSON; runtime construction follows the normal parser
and performs real allocation once. Availability and global MAC/port conflicts
remain runtime resource checks. This refinement guarantees earlier rejection of
malformed configurations under the existing parser/rendering rules, not future
availability of external resources.

The bounded implementation touches `osvm/lib/osvm/machine_config.rb`,
`test-runner/lib/test-runner/test_config.rb`, and their relevant specs, plus a
preparation/CLI regression demonstrating the barrier. No public option, JSON
format, guest state, scheduler algorithm, or daemon change is needed.

Required regressions: a valid first machine followed by an invalid second
machine (empty bridge options, zero/invalid shell count or conflicting named
shells, and simultaneous NixOS rootDisk/diskImage), with `--fresh` and an
expected-failure script, must fail preparation before Executor construction.
Assert no machine construction, disk reset, or global MAC/port calls. Also
exercise incomplete user-network options through the renderer, invalid socket
port types, and successful user/socket/bridge validation without allocation.
Existing normal-parsing tests must continue proving runtime MAC registration,
generation, and port allocation. Tests may spy on or forbid allocator calls;
production validation must not replace those global methods. Run affected
OSVM/test-runner specs and hooks, commit the repair, and return it through the
lead for the required review follow-up. Long integration verification remains
held until the finding is resolved.
