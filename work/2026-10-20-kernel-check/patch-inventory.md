# Custom kernel patch inventory: 6.12.95 → incident 6.12.113

Owner: implementer0. Read-only source investigation; no build, test, deployment,
source edit or production mutation. Runtime identity is supplied by the log lane
and corroborated here against immutable package recipes. See [design.md](design.md),
[log-evidence.md](log-evidence.md) and the source audits for causal conclusions.

## Result

The incident Linux stack has 55 downstream commits: 52 carry exactly the same
file paths and added/removed lines as their 6.12.95 counterparts; two existing
memcg lifetime fixes were consolidated into one; six proactive swap/DAMON
experiment commits were removed; and two commits add logic (the NFS cold-client
NULL guard and ordinary swap reporting corrections). The initial 6.12.113 stack
had all 60 old custom patch bodies unchanged plus the NFS guard.

This accounts for every Linux downstream commit. The additional packaged ZFS
free-accounting patch is a real custom change outside linux.git and is included
below; its causal audit belongs to implementer1. Patch equivalence does not prove
that an unchanged patch interacts correctly with every upstream change. No
incident cause is established by this inventory.

## Exact boundaries

All Linux references below belong to `repos/linux.git` (`vpsfreecz/linux`); OS
references belong to `repos/vpsadminos.git` (`vpsfreecz/vpsadminos`). The upstream
base is the `Linux 6.12.x` commit immediately preceding each linear custom stack.

| Variant | vpsAdminOS recipe/provenance | Linux head | Upstream base | Custom commits |
| --- | --- | --- | --- | --- |
| Original 6.12.95 boot source | Retained entry at incident OS; frozen boot producer `c065fa2f8485399737e20e8ef9e44299d0766654` | `a2384967b90f24d2470c9eb15f0e66d938df7e08` | `296aabce459470a4c1b68ffd0c0c0920e563aaad` | 60 |
| Initial 6.12.113 | Upgrade `eb5c39c0789401117c48cd124e47b7a401fb91b6` | `11058eb4fe1cba30653e8e643546c13bc8bcd792` | `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` | 61 |
| Incident 6.12.113 | Repin `ca3ff61a3931f0eb524543151d5d78a70f87bfc7`; selected at incident OS `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` | 55 |

The log owner identifies incident OS `26.05.git.2abbe3c`, generation 144, kernel
build 2026-10-18 17:47:47 UTC. `2abbe3cc:os/packages/linux/available-kernels.nix`
selects `1dfea587...`, so the proactive experiment in the initial `.113` pin is
not the incident variant. That recipe's source archive SHA-256 is
`sha256-IvyBosmZkpWxAK4Bz0sQ+RBwUQZwN+GtBxwjBY1lAdQ=`; old `.95` uses
`sha256-QlwV4uFeX7ZbWHMuU14rFXswmpqpb1hdVmYUAGOWRh8=`. The initial `.113`
archive hash was `sha256-YuxV0X1N5f42y6Jlx1bbiXWU0U3ETg233f1OYL0a0vA=`.

## Selection and application

- `os/packages/linux/available-kernels.nix` selects the stable version and immutable
  Linux source revision. `packages.nix` constructs the GitHub archive URL;
  `default.nix` fetches that archive. The custom commits in the tables are already
  in the downloaded Linux tree, rather than individually applied by Nix.
- `default.nix` adds `pkgs.kernelPatches.bridge_stp_helper` for both versions.
  `manual-config.nix` also applies `randstruct-provide-seed-5.19.patch` for both.
  That local patch is unchanged between frozen producer `c065fa2f...` and incident
  OS. Both recipes pin the same nixpkgs input
  `e4bae1bd10c9c57b2cf517953ab70060a828ee6f`, so the bridge-helper patch input is
  the same. The randstruct patch is build determinism support.
- The separate package patch `nfs-sysfs-null-rpc-client-6.12.109.patch` is gated on
  exactly `kernelVersion == "6.12.109"`; it is not applied to `.95` or `.113`.
  `.113` contains the guard directly in linux.git. The NMI/scheduler patch
  `native-nmi-sched.patch` belongs to the `.110` entry and is not selected by the
  `.113` entry. Neither compared entry supplies `postConfigPatches`.
- `manual-config.nix` copies an optional built-in ZFS source into the Linux tree
  in `prePatch`. Both incident-recipe version entries use ZFS
  `481845fca6ae3f61ca2262c1a5693a58ae364650`, but `.113` additionally selects
  `../zfs/zfs235-free-account.patch`; `.95` does not. OS commit
  `9bca43d32a84d0f76e2e497f68840143fa9bbbab` introduced that package patch.
  `358cd303ca236957054e6cc110c52a050a4ce448` extends selection to both packaging
  modes and is an ancestor of incident OS
  `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`: `git merge-base --is-ancestor`
  returns 0 in that direction and 1 in reverse. Both commits have the same
  committer timestamp, so timestamps do not establish their ancestry order.
  At the exact incident revision, `os/modules/config/kernel.nix:39-50`
  passes `extraPatches` to external ZFS at line 49, and
  `os/packages/linux/packages.nix:66-77` passes it to built-in ZFS at line 76.
  Thus both packaging modes select the patch in the incident source recipe.
  This proves recipe selection; it does not independently prove the bytes
  loaded by the affected node. This is distinct from the Linux stack accounting.
- `.95` retains livepatch features/frozen boot outputs, while `.113` has no
  matching livepatch entry. The exact old running `.95.6` identity needs the
  additional qualification below. Configuration/reachability analysis belongs
  to [packaging-audit.md](packaging-audit.md).

## Semantic changes and consolidation

| Owner | Exact source references | Semantic delta from old custom stack |
| --- | --- | --- |
| NFS cold-client shutdown guard | New `7ab40a1fe08da2c7cc2f6b369d10938c6579de81` (initial equivalent `11058eb4fe1cba30653e8e643546c13bc8bcd792`), `fs/nfs/sysfs.c:shutdown_client` | Adds `if (!clnt) return` before setting `cl_shutdown` and cancelling tasks. Three added lines including comment; introduces no wait or new lock. |
| Ordinary swap views | New `1dfea587406b7dd79973831d1677fb2418e5e9aa`, `fs/proc/meminfo.c:meminfo_proc_show`, `kernel/sys.c:do_sysinfo`, `mm/swapfile.c:fake_swap_show` | After removing proactive accounting, retain ordinary cgroup swap visibility; distinguish unlimited `PAGE_COUNTER_MAX`, saturate subtraction in affected branches and suppress a zero-total virtual swap row. Reporting changes, not a new reclaim mechanism. |
| Existing memcg lifetime fixes | Old `f69b960f6ed027c407b38bd38a25caaf995428b4` + `a2384967b90f24d2470c9eb15f0e66d938df7e08`; consolidated `def4b8a2613fd958daf882cfd4a9ff7a7e7ac1f0`; `kernel/vpsadminos.c`, `mm/swapfile.c` | Same final `get_current_most_limited_memcg` source: whole `kernel/vpsadminos.c` blob is identical in old and incident trees (`062ad3f5617ddea097566d69b46006ce452aa003`). `/proc/swaps` still holds the memcg reference until release; the removed proactive-use line changes surrounding context, not that reference owner. |
| Proactive swap/DAMON controls | Removed old owners `d85ac37a...`, `60bf9987...`, `313512f1...`, `ebc2300c...`, `273fde50...`, `ecc2a8fb...`; full refs/paths below | Remove system-proactive swap charging bypass and separate proactive usage accounting/views, free-memory quota goals, per-NUMA-node reclaim scope and its sysfs update fix/documentation. No proactive swap implementation remains in the incident stack. |

The six removed owners in detail:

| Old owner | Removed behavior |
| --- | --- |
| `d85ac37a38c074930f5fb256803e04f50660f13a` | `system_proactive_swap` flow through reclaim/swap allocation and charging; `quota_free_mem_rate` / `quota_free_mem_bytes`; proactive memory event and DAMON quota metrics. |
| `60bf998759588694c64ab1fb3601ae9f2d8a0b67` | Per-memcg proactive swap charge/uncharge/usage and per-swap-entry marker; exposure through meminfo/sysinfo/swaps. |
| `313512f1adf252edf51429af9490c4152eaf8e95` | Combine proactive usage with virtual swap totals/usage in those views. |
| `ebc2300c324a3e52376f1b5a1b7079ff52810ed3` | `damon_set_regions_system_ram`, per-node quota/watermark metrics and `damon_reclaim` scope selection/context replacement. |
| `273fde50609185956830b485cf3662d23019a5bf` | Update/commit handling when changing the experimental reclaim scope through sysfs. |
| `ecc2a8fb021b16bd126d39ef359f0268705c7e45` | Documentation for that scope. |

The initial-to-incident `.113` tree comparison uses the same upstream base and
therefore isolates this custom removal/reporting adjustment: 28 files, 160
inserted / 821 deleted lines. It does not change the NFS guard, scheduler,
`kernel/vpsadminos.c`, or printk/syslog files.

The syslog namespace patch was renamed v20 → v21, but its path + added/removed
lines are identical. Its raw signed-line SHA-256 (excluding paths/context) is
`7028761f6f217bf3a22072a98436845c4e614dd8c558bed118b6d3549a5e5934` in both
versions. New panic-logging declarations/functions visible in its context are
upstream changes, not newly added downstream lines. Fake affinity and the
memcg iterator NULL check likewise have identical downstream bodies. The
respective source audits inspect interactions rather than infer changes from
commit titles.

## Complete Linux custom correspondence

Every row names one old custom commit in application order. All 60 have identical
path + signed-line bodies at the initial `.113` reference. In the incident
column, `=` means the same exact commit as the initial column; `removed` means
absent; a full hash names the corresponding rebased/consolidated owner.
`C` = body unchanged; `R` = removed; `M` = consolidated existing memcg fix.
File paths are relative to linux.git and list all touched paths (renames are
expanded as delete/add paths). Full hashes avoid ambiguous abbreviations.

| # / status | Old subject | 6.12.95 commit | Initial 6.12.113 commit | Incident 6.12.113 commit | Paths |
| --- | --- | --- | --- | --- | --- |
| 1 / C | mem_cgroup_css_rstat_flush: fix NPE | `ff7af1357a6323e7cd4f9234469ea0d76cdcf1aa` | `f66047656f599a04407422afb34953f6b6e83839` | = | `mm/memcontrol.c` |
| 2 / C | sched.h: include nommu.h | `327f02abeb3d9a58120a217370863195d2c65612` | `f6a3be8d94ecfc3f183d14bc457e7f9dbeff338c` | = | `kernel/sched/sched.h` |
| 3 / C | Pushing GPL too much inhibits innovation | `d620ddaa1c3deab10b3fe172ef85359841dfb22f` | `aab33f20897f153a0c2cbb2330c4f88c40b17881` | = | `include/linux/license.h`, `kernel/user.c` |
| 4 / C | Common functions | `63d919a6055a83cb33279e133437f353e1c34fad` | `cc468c700f3665455c3ff7ac69217b4aa652c34e` | = | `include/linux/vpsadminos.h`, `kernel/Makefile`, `kernel/vpsadminos.c` |
| 5 / C | Allow mknod in user namespace v2 | `94e9f39fb7e9518c7dc2916e78e95804da554e87` | `1e8a19a71c2077c64a2614962228b01093b77d44` | = | `fs/namei.c`, `fs/super.c` |
| 6 / C | Enable mounting Ceph in user namespace | `53b371850421ed891da5f3ada2ceb766cb63fc7e` | `c45dcd9c2c615ebc1c19352ecced8d232aa096e9` | = | `fs/ceph/super.c` |
| 7 / C | Enable NFS in user namespace | `21afe14423c8f7b7b8d9bada2a8041d1ba2546c4` | `7df015b352f9f653544751d2d4d021df7593fffe` | = | `fs/nfs/fs_context.c` |
| 8 / C | nfsd: skip unknown words instead of ignoring them | `bb7abf8a43bbdaebb3d7924e350c8c387d8f83b0` | `400b70495941b9b5ab7627198c1d569477389533` | = | `fs/nfsd/export.c` |
| 9 / C | NFS client: force soft in CT | `3dcfa2a13c69c391e7021a90eba30ee667e7583a` | `65115e17527fcdf71771e7d79ea0abdc25df6b50` | = | `fs/nfs/fs_context.c` |
| 10 / C | smb/client: force soft in CT | `8ebc44871e2ff890488d1c8bdf48d3d5f43ed132` | `2c221b260b9c7f38c6a9c0db054392d99578b360` | = | `fs/smb/client/fs_context.c` |
| 11 / C | Enable trusted xattrs for 1st-lvl userns | `237cc2874dadad413d3bec61a7e3f127b2859bbf` | `9db02ef496e84104c99a06961276bc90572954f2` | = | `fs/overlayfs/inode.c`, `fs/overlayfs/xattrs.c`, `fs/xattr.c` |
| 12 / C | Ignore sync() calls from non-init user ns | `fb6a2debd9c9e871203482580f2b8d60085bd510` | `284fe6df59835042b3f17a63592d59a623d55da4` | = | `fs/sync.c` |
| 13 / C | fork: allow ct root fork over prlimit | `f7af894e3191f8f74c8b7b0e6b52d2e01f26f55f` | `caf1ca7bd058f54834111ec9cdb86e6d0a9fa290` | = | `kernel/fork.c` |
| 14 / C | proc/oom_score_adj: allow changing oom_score_adj_min from first-level userns | `d4df05e8e8a6c8e873887b3e43135bc862c8ed87` | `3efdbea2302bd986c1de985e6000a4d334b3c169` | = | `fs/proc/base.c` |
| 15 / C | oom_kill exceptions for CT init & lxc | `2bf0211bc6f8110928bc9a724780273f3865cc39` | `3555692676ccde4f513b270fc013d15f06238861` | = | `mm/oom_kill.c` |
| 16 / C | /proc/stat: virtualize oom_kill v2 | `9bf13e3e6c2b6d7d9bdea0994191e2ced068c9ec` | `f1ffad28d3dcf7a55f26ab5b7eb23d3ed5b05e6f` | = | `mm/vmstat.c` |
| 17 / C | out_of_memory in memcg: last resort v3 | `fe5d2e13a833ae00459821cbc37a6176a560350a` | `55a0cd80a61099752a6863a335de07022f3d2a95` | = | `mm/oom_kill.c` |
| 18 / C | netfilter: make all sysctl values per net | `a1bf7de996a08e6483c2cbe13bd07e9404276b44` | `6e4b1e9a2690d4562250f3f1219efcbdd5a36e19` | = | `net/netfilter/nf_conntrack_standalone.c` |
| 19 / C | Enable taskstats netlink in userns | `e8a7139643182c8564167155f6f33a6c05bb9ff0` | `9166afd319cb73c0e0182f27c2afd9297beb2450` | = | `kernel/taskstats.c` |
| 20 / C | dump_stack: print memcg path | `59000a8e7688ac14aa4df56c266618d5e6fedac1` | `c061ef0c856509ad32703439a1f9974664b90d5b` | = | `include/linux/memcontrol.h`, `lib/dump_stack.c`, `mm/memcontrol.c` |
| 21 / C | silence print_modules | `cf12930b2f6b88df8294ea206379510557de59f0` | `ab6555cd05d3c0b9de3df20e2ad06659c34df7c5` | = | `kernel/module/main.c` |
| 22 / C | Virtualize module parameters | `e487c551d27ab25769ccad7b738f96a422f8ecd0` | `a136c3aac6db4d4e1dfba7bb3961def7bf6bb5fb` | = | `fs/sysfs/file.c`, `include/linux/user_namespace.h`, `include/linux/vpsadminos.h`, `kernel/user_namespace.c`, `kernel/vpsadminos.c` |
| 23 / C | ipvs: enable configuration in userns | `46e083b8e072be829ce264a5d677d2f67ca1eb26` | `c107a8dd8ccf5b4e60b0a86b9014445b4c8c1448` | = | `net/netfilter/ipvs/ip_vs_ctl.c`, `net/netfilter/ipvs/ip_vs_lblc.c`, `net/netfilter/ipvs/ip_vs_lblcr.c` |
| 24 / C | Allow container admin to renice tasks v2 | `a289c8c389cec1ce9bc27d522bf174d75ab041a5` | `b501613dd1bd56e1e6ba029babc304ef9381569d` | = | `include/linux/sched.h`, `kernel/sched/syscalls.c` |
| 25 / C | procfs: fake uid_map for Docker v2 | `79d127a59258a1aefa06611aee944d5aa3d63b13` | `067d69b968bb750e29961bc7cfa8a37f60a992c1` | = | `kernel/user_namespace.c` |
| 26 / C | sysctl: virtualize vm.swappiness | `6d59147bcd660b99d80ec95a59b6dc7f9e3274be` | `d7b2eb86175e8a032840b2f8f210ce803825d7d5` | = | `kernel/sysctl.c` |
| 27 / C | Enable NFS server in containers | `ea9578903c185a7a59f61b84f497ed9f43be4572` | `cd1a8c094f2f3703b5fc732a18c5ec216c9c35a9` | = | `fs/nfsd/nfsctl.c`, `net/sunrpc/rpc_pipe.c` |
| 28 / C | translate max gid to containers for ping_group_range netns sysctl v6 | `dc8cb5483d22bae750039d6e21591f41ebc51b41` | `ffe1b46509456bb1c7ce7f5e5db39c8647155631` | = | `kernel/user_namespace.c`, `net/ipv4/sysctl_net_ipv4.c` |
| 29 / C | tmpfs: use 1/2 of memcg limit if present v3 | `e43666ebd0dc9e0cd161416271ff45ec7b5fb4cd` | `f52151fb6591710d602e6d06a2ca013b4062771d` | = | `mm/shmem.c` |
| 30 / C | tmpfs: show uid/gid from current user_ns PoV | `938d4894e695bf1e0789c43a24db8751cb0af559` | `1f0b72aeb1a5eeafd1b88caf5503b8c30e134642` | = | `mm/shmem.c` |
| 31 / C | memcg: skip shrink_slab when cgroup_memory_nokmem | `19ab64019a3bf3efbe042406db2149166d321f01` | `b64b21f929ed7e906f12f661bc157274f04acc1d` | = | `include/linux/memcontrol.h`, `mm/memcontrol.c`, `mm/vmscan.c` |
| 32 / C | /proc/cpuinfo cache | `5399bedc36a0d33f851364896fff2ebfa0f24b44` | `7d57b65e2d50c448e74e2e0406bf12c331a9d813` | = | `arch/x86/kernel/cpu/proc.c`, `fs/proc/cpuinfo.c` |
| 33 / C | allow proc_pid_stack in 1st level userns | `7fc6f44456e2a616e62214771dc27f7c7bf02b61` | `557227f8d5ea0eb066e95ce34553ac0670f59f39` | = | `fs/proc/base.c` |
| 34 / C | dump_stack: print memcg path v2 | `d1d3b6bc2059bec70f5332720c03da0f6fd5e6a7` | `2fd8fffd7001b2cc9872dfa0d3be154ba2a53e52` | = | `kernel/workqueue.c`, `lib/dump_stack.c` |
| 35 / C | respect CAP_LINUX_IMMUTABLE in 1st level userns | `bdd070750d1fdfe113e64ae5b37a833d684761ed` | `5ca4cab11dfc4cdd3c53b7d66ead5fa5978fe598` | = | `fs/ioctl.c` |
| 36 / C | syslog_ns: v20 | `14e1e939b8ce7a1389c3f20e27714630b05abaae` | `ca88e27931186c722b6762f760c0535c08d3ad46` | = | `fs/kernfs/dir.c`, `fs/proc/kmsg.c`, `fs/proc/namespaces.c`, `include/linux/nsproxy.h`, `include/linux/printk.h`, `include/linux/printk_ringbuffer.h`, `include/linux/proc_ns.h`, `include/linux/sched.h`, `include/linux/syslog.h`, `include/linux/syslog_namespace.h`, `include/linux/user_namespace.h`, `include/net/net_namespace.h`, `include/net/netfilter/nf_log.h`, `init/Kconfig`, `init/init_task.c`, `kernel/Makefile`, `kernel/fork.c`, `kernel/nsproxy.c`, `kernel/printk/internal.h`, `kernel/printk/nbcon.c`, `kernel/printk/printk.c`, `kernel/printk/printk_ringbuffer.c`, `kernel/printk/printk_ringbuffer.h`, `kernel/printk/printk_safe.c`, `kernel/sysctl.c`, `kernel/syslog_namespace.c`, `kernel/ucount.c`, `kernel/user.c`, `kernel/user_namespace.c`, `lib/bust_spinlocks.c`, `lib/dynamic_debug.c`, `net/bridge/br_private.h`, `net/core/net_namespace.c`, `net/netfilter/nf_log.c`, `net/netfilter/nf_log_syslog.c` |
| 37 / C | limit visible cpus for containers v16 | `0ade7066c0a4bb18fb42df28429a1b1bf9034ad1` | `b933b0ada59df128258507fcceebdab174166461` | = | `arch/x86/kernel/cpu/proc.c`, `drivers/base/cpu.c`, `fs/kernfs/dir.c`, `fs/proc/stat.c`, `include/linux/cgroup-defs.h`, `include/linux/sched.h`, `include/linux/vpsadminos.h`, `init/init_task.c`, `kernel/cgroup/cpuset.c`, `kernel/cgroup/rstat.c`, `kernel/fork.c`, `kernel/sched/core.c`, `kernel/sched/cpuacct.c`, `kernel/sched/sched.h`, `kernel/sched/syscalls.c`, `kernel/vpsadminos.c` |
| 38 / C | /sys/fs/vpsadminos | `3923273449dff3e07730142f90db4f84d6156bb2` | `944bcab9438bf7ef9c43ba84aec6b5cfd1856e85` | = | `kernel/vpsadminos.c` |
| 39 / C | get_slabinfo: do nothing outside init userns | `280d42d24b63e2ad73cf93a55243b0d9ccb7bd9f` | `ab8099a28ab2e3bddf35edcf1b46b15d73517e6b` | = | `mm/slub.c` |
| 40 / C | Hide diskstats in non-init userns | `e7876b7ecac042f06c7b5450f1a6d299f03ed38f` | `48191791f11bc460cccd29e04005e2ea4b65b80c` | = | `block/genhd.c` |
| 41 / C | kvmalloc: kvmalloc_noreclaim | `cfb647337938c2a288041f4b0cea7c53e6bd7f16` | `af1fc8835a3acd83938bf85bbda819c859248101` | = | `include/linux/slab.h`, `kernel/sysctl.c`, `mm/util.c` |
| 42 / C | unprivileged BPF: round down time | `20ce14cf6fd4aff5c6ae33d7da6952e392beecb4` | `65feb0c6fad58966754f0039dae1575c362415f5` | = | `include/linux/bpf.h`, `kernel/bpf/helpers.c`, `kernel/bpf/syscall.c` |
| 43 / C | enable ipsec sysctls in 1stlvl userns | `e89219e9206268ee652be42c9dc42e61c94df2e2` | `34221b5e9c8e5e8b420b6e54df010b0e3b2be828` | = | `net/xfrm/xfrm_sysctl.c` |
| 44 / C | Virtualize meminfo and swaps v4 | `7d14c6022c3b5ac494d90671174ae06ba75b82c8` | `34eca213f739506c140858d3046c5ee35f9f05c5` | = | `fs/proc/meminfo.c`, `include/linux/memcontrol.h`, `kernel/sys.c`, `mm/memcontrol.c`, `mm/swapfile.c` |
| 45 / C | syslog_ns: makedumpfile compat v2 | `820a58d5713b589a9eb5ea5dc65596bcbe820574` | `9b4e42807767565e8ce201caddb56415c64d73a7` | = | `include/linux/syslog_namespace.h`, `kernel/printk/printk.c`, `kernel/syslog_namespace.c` |
| 46 / C | Virtualize loadavg v18 | `92241147c92e781f5c87b071d5700c8895a5468d` | `6148a729711ca4db2f8c8163975dcd3c9bbed005` | = | `fs/proc/loadavg.c`, `fs/proc/uptime.c`, `include/linux/cgroup.h`, `include/linux/sched.h`, `include/linux/vpsadminos.h`, `kernel/cgroup/cgroup.c`, `kernel/cgroup/namespace.c`, `kernel/exit.c`, `kernel/fork.c`, `kernel/sched/core.c`, `kernel/sched/sched.h`, `kernel/vpsadminos.c` |
| 47 / C | limit visible cpus for containers v17 | `a8be141773a05782769dc82a1c7da1880694659d` | `212835625c605b754d6ff434d57a0e080dd0e452` | = | `kernel/vpsadminos.c` |
| 48 / C | limit visible cpus for containers v18 | `1d8b13ff8a32dfe904d70c1c3d6e3439bfc6803c` | `c472cb613a5e9f36c10d58828dd87d78a2c11daa` | = | `kernel/vpsadminos.c` |
| 49 / C | set prb correctly | `d849066001994641263617830ba43c8018fce362` | `8b123110b064574516fabea81ff2906f682aa67f` | = | `kernel/printk/printk.c` |
| 50 / C | Virtualize loadavg v18.1 | `20fd3906bced8b0fd2b789adebad76c28d473598` | `108d4158fae3c0d0affb58491ee67b9f573b550e` | = | `kernel/sched/core.c` |
| 51 / R | mm: add proactive DAMON reclaim controls | `d85ac37a38c074930f5fb256803e04f50660f13a` | `a9dd8baca1c921a11942fdc63862be4fcab2dce3` | removed | `Documentation/ABI/testing/sysfs-kernel-mm-damon`, `Documentation/admin-guide/cgroup-v2.rst`, `Documentation/admin-guide/mm/damon/reclaim.rst`, `Documentation/admin-guide/mm/damon/usage.rst`, `include/linux/damon.h`, `include/linux/memcontrol.h`, `include/linux/swap.h`, `mm/damon/core.c`, `mm/damon/paddr.c`, `mm/damon/reclaim.c`, `mm/damon/sysfs-schemes.c`, `mm/internal.h`, `mm/madvise.c`, `mm/memcontrol.c`, `mm/memory.c`, `mm/shmem.c`, `mm/swap.h`, `mm/swap_slots.c`, `mm/swap_state.c`, `mm/swapfile.c`, `mm/vmscan.c`, `mm/workingset.c` |
| 52 / R | mm: expose proactive swap via virtual swap views | `60bf998759588694c64ab1fb3601ae9f2d8a0b67` | `b1fe371e52aa7e7bee1ee5490c408ffed9a28c5d` | removed | `fs/proc/meminfo.c`, `include/linux/memcontrol.h`, `include/linux/swap_cgroup.h`, `kernel/sys.c`, `mm/memcontrol.c`, `mm/swap_cgroup.c`, `mm/swapfile.c` |
| 53 / R | mm: account proactive swap on top of virtual swap | `313512f1adf252edf51429af9490c4152eaf8e95` | `a2425d1734ae90527da3f8494c76d839c2a60712` | removed | `fs/proc/meminfo.c`, `kernel/sys.c`, `mm/swapfile.c` |
| 54 / R | mm/damon: add per-node reclaim scope support | `ebc2300c324a3e52376f1b5a1b7079ff52810ed3` | `7b11a3286173b93209b2c4c1f27614aed946cf5a` | removed | `include/linux/damon.h`, `mm/damon/core.c`, `mm/damon/dbgfs.c`, `mm/damon/lru_sort.c`, `mm/damon/reclaim.c`, `mm/damon/sysfs-schemes.c` |
| 55 / R | mm/damon: fix damon_reclaim scope updates from sysfs | `273fde50609185956830b485cf3662d23019a5bf` | `c89d7963a742b99287fd41c007f3358967ba15a2` | removed | `mm/damon/reclaim.c` |
| 56 / R | docs/mm/damon: document reclaim scope | `ecc2a8fb021b16bd126d39ef359f0268705c7e45` | `5bbdd2635be1a3ca6a34201626e93cee78256e70` | removed | `Documentation/admin-guide/mm/damon/reclaim.rst` |
| 57 / C | mm: memcg: fix NULL deref in __invalidate_reclaim_iterators | `cd535286625cd6930130ccfc06053e2bf3723779` | `0ffa2e5c545f333fc43f116ad4ce17e1e35e86be` | `83a59ebf6d041c57d445fefd69e9ec6cd019314f` | `mm/memcontrol.c` |
| 58 / M | vpsadminos: fix memcg CSS ref ownership in memory views | `f69b960f6ed027c407b38bd38a25caaf995428b4` | `b2c3db758ae499f7b6cdb116e41fba26e219ba08` | `def4b8a2613fd958daf882cfd4a9ff7a7e7ac1f0` | `kernel/vpsadminos.c`, `mm/swapfile.c` |
| 59 / C | sched: intersect vpsadminos fake affinity masks | `b9c9c0ed09699ad89751b21459c8abf99550a84e` | `8d97a7a9c6aa096d58ff87269168b28c54a9b548` | `b7609ccb76dabcb146356ea4c318715d1e9332bf` | `kernel/sched/syscalls.c` |
| 60 / M | vpsadminos: tolerate missing early memcg CSS | `a2384967b90f24d2470c9eb15f0e66d938df7e08` | `35b639015c452a5834371ee67b31554031780f31` | `def4b8a2613fd958daf882cfd4a9ff7a7e7ac1f0` | `kernel/vpsadminos.c` |

Additional Linux owners (not new rows for the already-accounted consolidated
memcg owner):

| Subject | Initial 6.12.113 | Incident 6.12.113 | Paths |
| --- | --- | --- | --- |
| Cold NLM client NULL guard | `11058eb4fe1cba30653e8e643546c13bc8bcd792` | `7ab40a1fe08da2c7cc2f6b369d10938c6579de81` | `fs/nfs/sysfs.c` |
| Ordinary cgroup swap reporting v3 | absent | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | `fs/proc/meminfo.c`, `kernel/sys.c`, `mm/swapfile.c` |

## Old `.95.6` runtime qualifier

`6.12.95.6` is a livepatch-reported release, not a different base source revision.
Historical OS integration `d9bd139cd3005657c5084dccda159b083ca9390d` pins Linux
`a2384967...` and selects cumulative livepatch version 6. Its
`os/livepatches/bp-6.12.95-uname.patch` updates `init_uts_ns.name.release` using
`LIVEPATCH_ORIG_KERNEL_VERSION` and `LIVEPATCH_NAME`. The cumulative backport
branch documented in `docs/os/livepatches/6.12.95.md` ends at Linux
`fc37ccc43227ab8eef70b50660a081f2615d0ead`; the documented reviewed upstream
range is `.95..104`. This runtime overlays upstream security backports and
custom livepatch glue on the old boot image, so it must be checked before
calling a later upstream fix new to the node.

That page also describes another boot source
`563bbb35e8753e1bb34dad19ebeec8962ee3c1cd` with module
`livepatch_6_nfs_cancel`; original `a2384967...` uses `livepatch_6`. Both can
report `.95.6`. The version string alone does not identify the variant or exact
module bytes. Moreover, incident OS `2abbe3cc` now advertises production v7;
that current recipe cannot prove which v6 payload ran before the reboot. The
`.95` source table is exact for the retained/original boot input, with this
explicit runtime qualification. No unsupported inference from current on-disk
configuration to the historical running module is made.

Frozen original `.95` boot output provenance is documented at
`2abbe3cc:os/packages/linux/boot-6.12.95/README.md`: producing OS
`c065fa2f8485399737e20e8ef9e44299d0766654`, GNU build ID
`7801779436291880089e3407e50e5813f80d76f1`, restored `bzImage` SHA-256
`3265b29d00581f09f9f171342c24cc8c6872ac679aca01f5e3fdb33d7850c541`.
This is source/recipe provenance, not an assertion that a collected incident
binary was independently hashed here.

## Evidence method and gaps

Read the verified session's workspace procedures, vpsAdminOS `AGENTS.md`, README
and kernel development documentation. Inspected canonical bare repositories
only; no other session's worktree was used. Enumerated first-parent custom
commits between each precise `Linux 6.12.x` base and selected head, then compared
individual diffs with full blob indices and rename detection disabled.
Canonical bodies retain each `diff --git` path pair plus all `+` / `-` content
lines, excluding file headers, context, hunk coordinates and metadata. Every
match is unique with paths included. Thus the count does not confuse unrelated
one-line patches with identical text.

Quick checks completed:

- Old / initial / incident series account for 60 / 61 / 55 commits.
- Initial 60/60 old body matches, plus one guard; incident 52 unique old body
  matches + one consolidated owner + two added owners = 55.
- Exact final `kernel/vpsadminos.c` blob equality; direct initial/incident tree
  diff isolates only the removal/reporting paths described above.
- Recipe pins, package-patch predicates, unchanged randstruct source and same
  pinned nixpkgs input checked at frozen producer and incident OS.
- Bare Linux is a partial/promisor repository. Early source reads triggered an
  implicit object fetch; those commands were stopped and disclosed to the lead.
  After explicit lead authorization, one exact object-only fetch materialized
  the 67 missing blob IDs among 449 distinct blobs touched by these three custom
  series, using `--no-tags --no-write-fetch-head --filter=blob:none --stdin`.
  It completed in a few seconds without a ref refresh. Subsequent reads use
  `GIT_NO_LAZY_FETCH=1`; extraction then completed locally.

No dynamic reproduction or kernel build was needed for inventory accounting.
Host incident attribution, .95.6 exact module identity, upstream interaction
correctness and the separate ZFS patch's locking semantics remain the owning
lanes' work. This investigation evidence does not change supported deployment,
persistent state, APIs, protocols or rollback behavior.
