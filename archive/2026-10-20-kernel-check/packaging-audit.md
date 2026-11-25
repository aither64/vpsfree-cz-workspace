# Kernel packaging and runtime reachability

Owner: implementer4. Read-only source/store investigation on 2026-10-20;
no builds, tests, fetch/ref changes or production mutations. This complements
[patch-inventory.md](patch-inventory.md) and [log-evidence.md](log-evidence.md).
It does not reproduce the Linux custom-series inventory.

## Outcome and completeness boundary

The reported node24 package revision selects the **post-retirement Linux
6.12.113 tree `1dfea587`**, not the initial `.113` tree `11058eb4`.
All kernel/ZFS package patch selectors in that exact vpsAdminOS revision were
accounted for below. The additional substantive package delta is the ZFS
free-accounting patch, assigned separately to implementer1 in
[zfs-patch-audit.md](zfs-patch-audit.md). Neither a conventional cumulative
livepatch nor a default eBPF program is selected for `.113`.

These are source/package-selection conclusions. The running kernel's complete
config, kernel/module bytes, livepatch sysfs and BPF links were not retrieved.
There is **no confirmed incident cause** from this packaging investigation.
The custom phase needs the separate Linux and ZFS semantic conclusions before
closing; unavailable runtime state remains an explicit limitation.

## Exact provenance

All vpsAdminOS paths/line numbers below refer to immutable commit
`2abbe3cc1c102a4b39022d3f73ef4a432ad4d616` unless stated otherwise.

| Item | Evidence |
| --- | --- |
| Incident OS | Central October 19 boot logs explicitly report input `vpsadminos=2abbe3cc`, OS `26.05.git.2abbe3c`, Linux `6.12.113`; generation 144 and the same init path recur in the October 20 recovery boot. See log owner's exact excerpts. |
| Incident init | `/nix/store/39yak5qzbm4fya40zg8nw4za6x8k3xir-vpsadminos-system-node24.prg.vpsfree.cz-26.05.git.2abbe3c/init` |
| Selected Linux | `os/packages/linux/available-kernels.nix:47-54`: `1dfea587406b7dd79973831d1677fb2418e5e9aa`; archive hash `sha256-IvyBosmZkpWxAK4Bz0sQ+RBwUQZwN+GtBxwjBY1lAdQ=`. |
| Initial `.113` | vpsAdminOS `eb5c39c0789401117c48cd124e47b7a401fb91b6` selected `11058eb4fe1cba30653e8e643546c13bc8bcd792`. Ancestor `ca3ff61a3931f0eb524543151d5d78a70f87bfc7` repinned to `1dfea587` while retiring the proactive-swap experiment. |
| Build-time cross-check | Boot banner `Sun Oct 18 17:47:47 UTC 2026` equals Linux `1dfea587` commit epoch `1792345667`. `manual-config.nix:258` sets `KBUILD_BUILD_TIMESTAMP` from `SOURCE_DATE_EPOCH`. This corroborates the source input; it is not binary attestation. |
| Retained `.95` | `available-kernels.nix:80-87`: Linux `a2384967b90f24d2470c9eb15f0e66d938df7e08`, archive hash `sha256-QlwV4uFeX7ZbWHMuU14rFXswmpqpb1hdVmYUAGOWRh8=`. Earlier node24 blocked-task reports identify `6.12.95.6`, so bare `.95` source alone does not identify all earlier runtime replacements. |
| Nixpkgs | Log owner retrieved `log-20261020:215495`: `input nixpkgs=26f4107e`. Historical configuration commit `177a9305f00d1755c66d170b4fa500d3ad18b6c2` locks production Nixpkgs to `26f4107e47e3ad0ffd0db220469ba83b6f6d96e8`, NAR hash `sha256-OaQwAtPMTjQiY2sT/2/62UbSPhzP/0aDnWzMm/NCiUw=`, and production vpsAdminOS to the exact `2abbe3cc` commit. |

The Nixpkgs NAR hash resolves, without evaluation/download/build, to existing
local store source `/nix/store/c7w4dnzdyg31wrnx56y17wihi5zaibsl-source`.
Its kernel patch registry and bridge patch were read directly. The exact
incident configuration-repository commit is not logged in the inspected
adjacent boot messages; the historical lock proves a matching retained input
pair, not that node24 was built from that configuration commit.

The locally retained realized `.113` output
`/nix/store/0lgvd22dlh9l0pn8vafx15wklbmvkcrc-linux-6.12.113` and config
`/nix/store/c1jiyfrhmjyzkpidmlmyzm5ai5k3lfcg-linux-config-6.12.113` belong to
the **initial** `11058eb4` source, as shown by their retained derivations
`zbmalg803ljsk6p98lpfynlybz5jzpwv-linux-6.12.113.drv` and
`9yq71142xkjs0bwg109y9722qbxxz9f1-linux-config-6.12.113.drv`.
Their configuration must not be presented as the incident config.
The incident system closure is absent from this local store.

## Patches and source transformations outside linux.git

| Selector | Effective selection at `.113` | Comparison/limit |
| --- | --- | --- |
| `linux/default.nix:38-44` | Nixpkgs `bridge_stp_helper` | Also selected for retained `.95`. Exact pinned Nixpkgs patch changes only `BR_STP_PROG`, from `/sbin/bridge-stp` to `/run/current-system/sw/bin/bridge-stp`. It adds no lock or wait; the existing `br_stp_call_user()` already calls `call_usermodehelper(..., UMH_WAIT_PROC)`. Patch SHA256 `53d467696157b4ca71535a3021d8b9d8db3fa765ea2f8db01fbf2e607e6032e5`. |
| `linux/default.nix:41` | NFS sysfs NULL-rpc-client repair **not selected** | Selected only for exact version `6.12.109`. This excludes that packaging selector, not equivalent code already in another tree. |
| `linux/manual-config.nix:167-177` | `randstruct-provide-seed-5.19.patch` | Applies to both `.95` and `.113`; other version-gated build patches do not match either. It changes seed input generation, not runtime locking. Patch SHA256 `cc19d1c516342cd8728b98538819067a6cd0e5d20460a75b85f1e1727812cb03`. |
| `available-kernels.nix:64`; `config/kernel.nix:128-132` | No `postConfigPatches` for `.113` | `native-nmi-sched.patch` is selected only for `.110`. Do not infer native `.113` semantics from this package patch's presence on disk. |
| `available-kernels.nix:50-54`; `linux/packages.nix:66-77` | ZFS `481845fca6ae3f61ca2262c1a5693a58ae364650` plus `zfs235-free-account.patch` | Retained `.95` selects the same ZFS revision without this patch. Builtin package prep copies the patched ZFS source into Linux (`manual-config.nix:179-187`). External ZFS forwards the same patch list (`config/kernel.nix:39-50`). |

ZFS patch blob: `9cfc5041877462bcad0be25f89f06e66d904af74`; SHA256
`6337b8683fe4b24467ff74e7d17eac7ae5424586d9c413a9570e20a3fc0b6e93`.
It was introduced by `9bca43d32a84d0f76e2e497f68840143fa9bbbab` and splits
free accounting from hole publication in `module/zfs/dnode_sync.c`. The semantic
audit must check block-pointer lifetime/ownership and the lock/progress paths;
the explanatory patch comment alone proves neither a defect nor incident use.
`os/packages/zfs/default.nix:85` applies exactly `extraPatches`. ZFS userspace
selection does not forward this kernel-only patch (`linux/packages.nix:79-86`).

**Both-mode ancestry correction:**
`358cd303ca236957054e6cc110c52a050a4ce448`, which forwards external ZFS
patches, is the **direct parent** of incident OS `2abbe3cc`; its parent is
`ca3ff61a`. Both `358cd303c` and `2abbe3cc` have commit timestamp
`2026-10-18T20:16:06+02:00`. Timestamp order must not replace ancestry.
`git merge-base --is-ancestor 358cd303c 2abbe3cc` exits 0; reverse exits 1.
Thus both packaging modes select the patch at the incident revision. The actual
loaded mode/bytes remain unknown. `boot.zfsBuiltin` defaults true, but that flag
alone does not prove static linking of ZFS into the boot image.

Remaining kernel packaging transformations strip FHS paths from build/install
scripts, fix tool/shebang paths, set deterministic seed/build metadata and,
for `.113`, suppress the GNU build ID. `.95` requests preserved build IDs via
`features.livepatch = true`; `.113` does not (`default.nix:49`,
`manual-config.nix:188-205`). These are accounted for as build/identity changes;
no runtime progress defect is established by them.

## Config, boot selection and runtime replacements

The `.113` entry supplies no `structuredExtraConfig` override. The common recipe
requests `MEMCG`, `MEMCG_V1`, `CPUSETS_V1`, `SYSLOG_NS`, CFS bandwidth, cgroup
perf, DAMON/DAMON_RECLAIM and `LIVEPATCH`; requests `PSI = no` and
`PROVE_LOCKING = no`; and defaults to non-RT preemption. Relevant references:
`linux/common-config.nix:49-82,103-120,499-511,527-559,862`.
These are source requests, not a recovered final node24 `.config`.

The boot banner reports `PREEMPT_DYNAMIC`, and the command line contains
`preempt=full`. This is evidence for dynamic full preemption, **not** PREEMPT_RT.
Boot arguments also include `cgroup.memory=nokmem`, `nosmt`,
`amd_pstate=guided`, `intel_idle.max_cstate=1`, `softlockup_panic=1` and
`crashkernel=4096M`; refer to the log evidence for their observed scope.

Configuration source at `177a9305` selects hybrid cgroups for node24
(`boot.enableUnifiedCgroupHierarchy = false`) and empty `swapDevices`.
Relevant node24, common `all.nix`/AMD/tunables and `configs/node` files have no
diff between that historical commit and inspected configuration HEAD
`b748fb08c3f5aac12b302414cc45936f663d1cbd`.
No kernel-package/patch, ZFS-mode or eBPF-program override was found in that
configuration's configs/profiles/modules/cluster/environments. This supports
source applicability, but does not prove runtime mounts, swaps or manual changes.

`configs/node/base.nix:35` obtains a runtime-selected kernel; `kernels.nix` allows
an ignored/generated `kernels.json` override. PXE-only builds instead select
the boot kernel (`configs/node/pxe-only.nix:22`). Consequently current
configuration defaults alone do not establish the boot kernel. The matching
generation/init/banner/input log evidence is stronger here.

Conventional livepatch selection is empty for `.113`:
`os/livepatches/available-patches.nix` registers exact `.95` and the bounded
`.48`–`.89` range; the filter's summed version is 0 for `.113`.
`services/livepatches/default.nix:22,409-434` therefore supplies an empty
`livepatch-store-path`, no compiled payload/monitor and a sleeping service.
The source `LIVEPATCH=y` capability does not imply an active livepatch.
At this source revision `.95` selects v7, whereas historical node logs show
`.95.6`; the former is not evidence that v7 ran on node24.

The common node configuration enables the separate eBPF livepatch service.
However `os/livepatches/ebpf/available.nix:15-79,178-193` selects no default
program for either `.95` or `.113`: the enabled ptrace guard ends before
`.89`, the enabled CIFS guard ends before `.92`, and uname/LSM examples are
disabled. The loader's table is generated only from selected names
(`os/packages/ebpf-livepatch/default.nix:30,173-176`). Thus an enabled service
does not establish an attached BPF mitigation. Pinned generations would be under
`/sys/fs/bpf/vpsadminos/ebpf-livepatch/generations`; these were not inspected.

DAMON reclaim's system-managed enable defaults false
(`config/damon-reclaim.nix:14-23`), and no node configuration override was found.
The service writes upstream parameters and enforces its enabled value
(`:254-319`). This is distinct from compiling DAMON capability and from the
removed experimental proactive-swap code; manual runtime activation is unknown.

## Trusted runtime-access limit and further evidence

The log owner could not inspect node24 because host-key validation failed.
Bounded local diagnosis found that `node24.prg.vpsfree.cz` resolves to configured
management address `172.16.0.34`; `node24.prg` and
`node24.int.prg.vpsfree.cz` do not resolve. Effective SSH configuration supplies
no special alias/proxy for the FQDN, short name, int name or address. Targeted
`ssh-keygen -F` checks found no matching existing trusted entry in the effective
user/global known-host files. Configuration refers to protected production host
key material, not a usable checked public trust mapping. No trust changes,
host-key bypass, unverified key acceptance or new node connection followed.

If trusted access is separately available, useful read-only evidence is the
booted security-evidence JSON/config reference, kernel/module symlinks,
`/proc/cmdline`, `/sys/kernel/livepatch/*/{enabled,transition}` and eBPF monitor
metadata plus pinned/live link identity. A post-recovery snapshot still needs
continuity evidence before representing pre-hang state. No recovery or diagnostic
configuration operation is proposed as already executed.

## Upstream-phase applicability handoff

The initial-to-incident Linux comparison has no changes in `**/Kconfig*`,
`**/*defconfig`, `scripts/kconfig` or the top-level `Makefile`. The corresponding
vpsAdminOS comparison `eb5c39c..2abbe3cc` has no changes in `common-config.nix`,
`generic.nix`, `generate-config.pl`, `manual-config.nix` or Linux `default.nix`.
The generator retains boolean defaults unless explicitly overridden; its
automatic-module preference applies to tristates, not arbitrary booleans
(`generate-config.pl:1-10,82-89`). Together with Kconfig definitions, the
initial realized config supports the following **recipe-inferred** values for
the ordinary post-retirement build. It still does not attest node24's final
config or rule out an unrecorded build override.

| Gate | Source-derived expected value | Runtime limit |
| --- | --- | --- |
| `SCHED_CORE` | n; boolean defaults off (`kernel/Kconfig.preempt:118`) | No final config; `nosmt` is separately observed. |
| `SCHED_CLASS_EXT` | n; boolean defaults off (`kernel/Kconfig.preempt:136`) | No evidence of an SCX scheduler being loaded. |
| `PREEMPT_RT` | n; package RT feature absent and preemption choice requests `PREEMPT_NONE`; dynamic mode is separate | Banner says `PREEMPT_DYNAMIC`; cmdline `preempt=full` does not enable RT. |
| `PSI` | n, explicit common recipe request | No final config snapshot. |
| `PROVE_LOCKING` / `LOCK_STAT` | n, explicit common recipe requests | `LOCKDEP` itself conservatively unknown without checking every selector; initial config exposes `LOCKDEP_SUPPORT=y` but no active `LOCKDEP`. |
| `LRU_GEN` | n; boolean defaults off (`mm/Kconfig:1283`) | Dependent `LRU_GEN_ENABLED`, `LRU_GEN_STATS`, `LRU_GEN_WALKS_MMU` consequently off in ordinary recipe. |
| `MEM_ALLOC_PROFILING` | n (`lib/Kconfig.debug:993-1015`) | Dependent profiling-default/debug options consequently off. |
| `SLUB_DEBUG` | y; Kconfig default (`mm/Kconfig.debug:48-57`) | Capability does not mean runtime checking of all caches. |
| `SLUB_DEBUG_ON` | n; Kconfig default (`mm/Kconfig.debug:59-71`) | Per-cache/manual activation and complete runtime flags not inspected. |
| cpuset hierarchy | `CPUSETS_V1=y` requested, node24 source requests hybrid/v1 | Runtime cpuset mounts/controllers not retrieved. |
| DAMON | Capability requested; system-managed reclaim enable defaults false with no node override | Actual `enabled`, manual sysfs use and custom schemes unknown. |
| NFS TLS / RDMA / pNFS | Unknown | Bounded log search does not establish mount/transport selection. See log evidence. |

The booted memory-controller `nokmem` setting does not disable global shrinkers
or establish the values of these independent memory/debugging features.

The user's subsequent confirmation that repository-configured sysctls had no
runtime changes resolves the sysctl-policy uncertainty. The exact configured
hard/soft watchdog, panic and crashdump gates, positive pre-incident
`Kdump: loaded` evidence, and their limits are recorded in
[upstream-platform-audit.md](upstream-platform-audit.md). In particular,
hardlockup panic is 0 and softlockup panic is 1; the earlier lack of direct
runtime inspection must not be used to leave those configured values unknown.
