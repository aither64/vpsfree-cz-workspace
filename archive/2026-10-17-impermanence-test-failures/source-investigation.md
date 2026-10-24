# Impermanence CI source investigation

Investigated read-only by architect0 at vpsadminos
`0081fc01f13236a098380094ddbd00539a9c8dae`, using the canonical bare repository.
All source line references below refer to that revision. No application changes,
worktrees, tests, builds or CI reruns were made.

## Finding and confidence

This incident is a shared fixture-build failure before VM startup, not evidence
that twelve persistence assertions failed. The native `test-runner.log` in
`ci-logs/os-test-dist-config__nixos-persistence-upgrade-8c45b496/` ends with:

- Lines 560–562: building `squashfs.img`, “Using 42 processors”, block size 1048576.
- Line 563: `NixCli#run!` raises `nix-build ... failed ()`.

`test-runner/lib/test-runner/nix_cli.rb:93–96` waits for the spawned nix-build
process and reports only `Process::Status#exitstatus`. Empty parentheses mean
nil exitstatus, consistent with signal termination; neither the signal number
nor its cause is retained. This does not prove that the compressor itself was
killed or that the kernel OOM killer acted.

`test-runner/lib/test-runner/test_evaluator.rb:50–56` builds the configuration
before constructing machine objects (:63–85) or running scripts (:96–106).
`test-runner/lib/test-runner/executor.rb:736–741` marks scripts without results
as failed. That accounts for all twelve names after one failed shared build.

## What the tests protect

Impermanence gives the container a disposable root while retaining explicitly
selected state. `osctld/lib/osctld/commands/container/start.rb:93–95,293–323`
creates a fresh ZFS run dataset, marks it for destruction on stop, and prepares
the empty root. The supplied NixOS configuration persists `/etc/nixos`,
`/var/log`, `/var/lib/nixos` and `/etc/machine-id` under `/persistent`
(`os/lib/nixos-container/stable/impermanence.nix:100–110`). The test explicitly
creates persistent `/nix`, mounts the original root at `/persistent`, and enables
impermanence (`tests/suite/dist-config/nixos-persistence-upgrade.nix:135–165`).

The regression being guarded against is account-ID drift: LXC mounts `/proc`
before NixOS init, so NixOS can skip early mounts and allocate users before
seeing saved `/var/lib/nixos/uid-map` and `gid-map`. Later mounts expose the old
maps and numeric file ownership while passwd/group already contain new IDs.
The owning explanation is `docs/containers/nixos.md:121–179`.

The compatibility adapter selects early mounts covering allocation state/logs,
includes their prerequisites, checks mount and directory-bind identity, and
aborts activation if required storage fails. It preserves existing metadata
and creates absent directories with root/0755 defaults. It makes legacy user
allocation depend on this mount step
(`os/lib/nixos-container/stable/vpsadminos-26.05.nix:24–83,85–178,225–252`).

The suite verifies these concrete guarantees:

| Guarantee | Source evidence |
| --- | --- |
| Live UID/GID agree with visible and backing allocation maps; bind sources match, without duplicate mounts | `tests/suite/dist-config/nixos-persistence-upgrade.nix:83–115` |
| Known payload checksum, numeric ownership, machine-id, existing source metadata and directory identity survive | Same file, :224–234 |
| Adding earlier-sorting `a-preservation-test` does not renumber `preservation-test`; new IDs remain distinct | Same file, :236–240; `tests/fixtures/nixos-persistence-guests.nix:69–78` |
| Healthy old configuration adopts candidate compatibility module, tolerates repeat activation and survives container restart | Suite :241–259 |
| Missing/conflicting storage and failed mounts/remounts abort before the real legacy allocator, leaving accounts/maps/payload unchanged | Suite :261–346 |
| Fresh sources get safe defaults, including below a setgid parent; ancestor and direct filesystem binds work | Suite :178–188,229–234; fixture :276–306 |

The twelve variants cover NixOS 25.11, 26.05 and unstable; root-backed,
guest-declared and dependent mounts; `/var` and `/var/lib` ancestors; direct
`fileSystems` binds; fresh initialization; and injected storage failures
(`tests/fixtures/nixos-persistence-guests.nix:295–327`). They retain
`system.stateVersion = "22.11"` and force the legacy allocator (:56–60).

“Upgrade” means replacing the vpsAdminOS guest compatibility module, with the
same guest nixpkgs and layout, not upgrading NixOS releases. The predecessor is
pinned to `1150e37b1cc997b1728f2fda806a3433ef55b798`
(`tests/fixtures/nixos-container-persistence.nix:18–23`; guest fixture :197–240).
Healthy guests can adopt independently; this does not repair already-drifted
IDs, and restarting an older generation can restore the ordering defect
(`docs/containers/nixos.md:167–179`).

## Build-cost contributors and remaining hypothesis

All twelve scripts share one host VM. The suite collects every variant's four
old/new, initial/challenge generations plus ten fault generations, puts them
and their closure registrations into that VM's `system.extraDependencies`, and
then generates the script names (suite :10–19,355–367; guest fixture
:235–249,295–327). This is 48 generation references plus 10 fault references
before Nix deduplication, not 58 independent systems or VMs. Multiple releases
add distinct runtime closures. Even selecting a single script retains the
shared machine definition and its complete fixture closure.

`os/modules/system/activation/top-level.nix:54,236–245,424–428` retains those
dependencies in the host closure and constructs its squashfs with `noStrip =
true`. The actual compression path is tar piped into **sqfstar**, despite the
shared “mksquashfs” progress wording
(`os/lib/make-squashfs.nix:41–46,56–79`). It uses 1 MiB blocks and default zstd
level 10 (:19–25,78), with no explicit processor or memory cap. The test CI
configuration does not override compression. Neither fixture closure size nor
compressor peak memory was measured in this investigation.

Resource estimates sum guest memory and CPUs (`tests/make-test.nix:321–339`);
they do not include a separate per-build memory estimate. There is a default
8 GiB global memory reserve (`test-runner/lib/test-runner/resource_pool.rb:6,
119–124,156–162`). Lead-observed admission was 10 tests and 80/86.5 GiB guest
memory reserved. Reservation is not a measurement of resident memory.

Concurrent guests, this large shared closure and 42 compression workers make
memory pressure a plausible explanation for signal termination. They do not
establish OOM. Runner/host kernel or cgroup evidence around
2026-10-17 02:01:27 UTC is needed to identify the signal, victim and cause.
Bounding compression or reserving fixture-build capacity are possible remedies
to evaluate after that evidence, not implemented or verified fixes.

## Revised resource recommendations: preserve automatic throughput

The user confirmed OOM termination and clarified that automatic concurrency and
build CPU throughput must be preserved. Victim details and peak memory remain
unknown. This section supersedes the earlier proposal for 4 test jobs, reduced
CPU overcommit, CPU reservations, 4/8 compressor threads and global Nix
max-jobs/cores limits. Those fixed caps are no longer recommended. No settings
were changed.

The comparison baseline is staging `0081fc01`, still current according to the
lead's remote check. Job logs :672–673 report 96 GiB assigned, 94.5 GiB available
at startup, 8 GiB reserve, 86.5 GiB guest-memory capacity and 63 guest vCPUs.

| Setting/behavior | Current baseline | Recommended direction |
| --- | --- | --- |
| Test scheduling | `--jobs auto` | Keep automatic; admit as many tests as memory budgets permit |
| Memory overcommit | 1.0 | Keep 1.0 |
| CPU overcommit | 1.5, giving 63 guest vCPUs | Keep; no new global CPU/kernel-build cap |
| Host memory reserve | 8 GiB | Keep as target; account for builds and VM overhead separately |
| Memory reservations | Configured guest memory only | Add per-VM host overhead and active build-phase peak budgets |
| sqfstar processors | All available; log reports 42 | Keep initially |
| sqfstar cache | Default 25% physical memory | Explicit calibrated cache budget; `-mem 4G` is a candidate to measure |
| Image compression | zstd level 10, 1 MiB blocks | Keep initially; test-only zstd level 3 is a benchmark candidate |
| Nix build concurrency | Separate from test scheduler | No proposed global max-jobs/cores reduction |

Current guest reservations leave unaccounted image construction and host-side
VM overhead. The target invariant is:

```text
reserved guest RAM + reserved VM overhead + active build peak budgets
    <= 86.5 GiB
```

This is the observed initial 94.5 GiB availability less the existing 8 GiB host
reserve, subject to detected limits. It is an admission budget, not a guaranteed
RSS bound. With no build active, capacity returns to guest work; while images
build, guest capacity decreases by their reserved peaks and VM overhead.
Concurrent image builds each need a charge. The actual budgets require cold
fixture/build measurements, not inference from the guest's configured RAM.

A feasible automatic scheduler would recognize build and VM phases. Reserve a
build's peak while preparing its exact image, then atomically exchange that
charge for the VM's configured RAM plus measured/estimated overhead before boot.
Charge both when phases overlap. Release a build charge only when the accounted
work has actually ended, including externally managed Nix work. Where phase
attribution is unavailable, conservatively retain the necessary combined charge.
Build CPU parallelism stays unrestricted by any new policy when memory fits.
Prebuilding exact test images before VM execution is an alternative phase split,
but should be compared with overlapping phases for total suite throughput. The
existing production-toplevel build (`ci.yml:124–130`) does not prebuild all test
images.

Add a separate pressure gate for new admissions using live host/cgroup headroom.
`CapacitySource` currently captures available memory once
(`resource_pool.rb:50`), while refresh rereads assigned/total memory
(:56–58,159–160). Shortening the refresh interval does not repair that gap.
Do not subtract all existing reservations from live free memory: resident guests
and builders are already reflected there. Account for the *remaining possible
growth* of active reservations plus new incremental demand and a race margin,
using attributable charged memory where reliable. Shared pages/cache and builds
outside the test process tree make raw summed RSS insufficient. This is a design
requirement to resolve before implementation, not a ready allocation formula.
The pressure gate delays new starts; it does not kill running tests or fix the
number of concurrent tests.

The lead verified squashfs-tools 4.7.5's upstream
`Documentation/manpages/sqfstar.1` and `squashfs-tools/memory_compat.h`:
`-processors` defaults to all available CPUs; cache defaults to 25% physical
memory obtained through sysconf/sysinfo rather than cgroup-aware accounting.
The failed process's actual selected cache size was not measured; do not claim
it was exactly 24 GiB from the runner's 96 GiB assignment.
`os/lib/make-squashfs.nix:68–85` supplies no processor/cache limit and does not use
`NIX_BUILD_CORES`. An explicit `-mem 4G` while keeping all processors is a useful
candidate, but this is a **cache budget, not total RSS**. Metadata, compressor
state/dictionaries and simultaneous builders add memory. Measure peak charged
memory and image-build/suite duration to calibrate the scheduler's peak charge.
A test-only zstd level 3 experiment may improve throughput, but requires checking
image size, I/O and VM loading costs; it is not established as better here.

Two other gaps remain relevant:

- `executor.rb:227–245` currently admits an oversized test alone even when memory
  limits fail. Reject impossible memory requests clearly; keep explicit CPU-only
  oversubscription for tests such as the special livepatch profiles.
- Each executor owns an in-process pool and mutex (:46–49,202–215). Independent
  executors/build clients can reserve the same physical capacity. If they share
  a runner/host, use shared reservations or an explicit aggregate partition.
  Labels and local settings alone do not establish a machine-wide budget.

For an optional temporary mitigation before build accounting exists, increasing
only the reserve to 24 GiB **while retaining auto scheduling and current CPUs**
would reduce the logged initial admission ceiling to 70.5 GiB. This trades guest
concurrency for unallocated headroom; the evidence does not establish that 24 GiB
is necessary or sufficient. No new arbitrary 16 GiB target is proposed. The goal
is measured build/overhead charges with the existing host reserve.

CLI source caveats remain: CI explicitly passes auto (`ci.yml:232`), although the
CLI default is 1 (`cli/app.rb:58–59`); auto creates one worker per test group
(`cli/command.rb:88–99`). Resource flags have `TEST_RUNNER_*` environment forms
with explicit CLI values taking precedence (`resource_pool.rb:119–195`).
The reserve is subtracted *after* the configured maximum
(:50–100,198–201): maximum 65536 MiB plus reserve 24576 MiB admits 40960 MiB,
not 65536 MiB. Neither jobs nor guest CPU budgeting limits compressor threads.
The separate `/dev/shm` budget is not additional compressor RAM.

These are recommendations only. Calibrate with cold-image peak memory, active
build counts, guest/VM host overhead, cgroup OOM events and total suite duration
on a future authorized run. Preserve signal diagnostics. No implementation,
builds/tests, CI dispatch, reviews or deployments were performed.
