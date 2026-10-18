# Linux 6.12.113 source reconstruction

Current phase: consolidated review fixes folded into ordinary-view v3, quick
checks passed, final feature head published with exact lease after retaining the
reviewed backup. The lead owns direct finding reconciliation, the final OS pin
and `staging` integration. No build or runtime validation has been performed.
Implementer0 owns this artifact; [design.md](design.md) records the accepted
scope and ordinary-view corrections.

## Exact source and publication

| Identity | Exact value |
| --- | --- |
| Upstream Linux v6.12.113 | `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` |
| Inherited task base | `108d4158fae3c0d0affb58491ee67b9f573b550e` |
| Original product tip | `11058eb4fe1cba30653e8e643546c13bc8bcd792` |
| Final feature head | `1dfea587406b7dd79973831d1677fb2418e5e9aa` |
| Feature remote ref | `refs/heads/2026-10-16-proactive-swap-patch-removal` |
| Original source ref retained | `refs/heads/codex/kernel-6.12-upgrade-20261017` = `11058eb4fe1cba30653e8e643546c13bc8bcd792` |
| Dated local backup | `refs/heads/backup/2026-10-18-proactive-swap-patch-removal-6.12.113-original` = `11058eb4fe1cba30653e8e643546c13bc8bcd792` |
| Retained reviewed remote backup | `refs/heads/backup/2026-10-18-proactive-swap-patch-removal-reviewed-86d54e7` = `86d54e7adff82e632299b41a2d1397ccbec1cb9e` |
| Worktree | `worktrees/2026-10-16-proactive-swap-patch-removal/linux` |

Native session comparison was captured successfully with explicit task base
`108d4158fae3c0d0affb58491ee67b9f573b550e` and final head
`1dfea587406b7dd79973831d1677fb2418e5e9aa`. The command returned those exact
identities with `baseLabel: Captured comparison`; source and refs were unchanged.

Publication used `git@github.com:vpsfreecz/linux.git`. The initial new feature
head was `86d54e7adff82e632299b41a2d1397ccbec1cb9e`. After the consolidated review, that exact head was published
and SSH-verified under the dated reviewed backup above. Only then did an exact
`--force-with-lease=refs/heads/2026-10-16-proactive-swap-patch-removal:86d54e7adff82e632299b41a2d1397ccbec1cb9e`
replace this session-owned unmerged feature ref with `1dfea587406b7dd79973831d1677fb2418e5e9aa`. The lead explicitly
authorized that update. SSH `ls-remote` then verified the new feature head, old
reviewed backup and unchanged original product source ref.

The retained local `origin/vpsadminos-6.12` remains
`9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd`. No pre-existing release/default/product
source ref was rewritten, merged or promoted. The published feature and reviewed
backup refs must remain for exact OS pin/review provenance. No pull request was
created. Branch-scoped GitHub Actions inspection after replacement returned `[]`;
there were no superseded runs to cancel and no CI wait occurred.

## Baseline, ownership and history boundary

The full original range has 61 downstream commits; the final range has 55.
The first 50 commits through `108d4158fae3c0d0affb58491ee67b9f573b550e` are commit-identical in both ranges.
They were already published and selected by the OS's 6.12.113 source at
vpsAdminOS `60f9ed1c153a734880e002b63d6ab7ed5fe87d0e` (this establishes source
consumption, not deployment). The user states that the experiment was never
deployed.

Lead and architect explicitly bounded this task to the affected suffix. The
inherited prefix still contains earlier loadavg v18/v18.1, CPU-visibility
v16/v17/v18 and terse Common-functions stages. This work does not claim to have
normalized those existing stages/messages. Final review receives the complete
upstream range and this inherited-history boundary.

The task-owned range is `108d4158fae3c0d0affb58491ee67b9f573b550e..1dfea587406b7dd79973831d1677fb2418e5e9aa`: five logical owners, no merges,
reverts, fixup/WIP stages or separate early-CSS repair. The six experiment
owners are absent from final ancestry. Their custom behavior is omitted;
ordinary unlimited-swap intent is separately extracted from the mixed accounting
owner under the lead-approved design adjustment.

### Final task-owned sequence

| Order | Final owner | Subject |
| --- | --- | --- |
| 1 | `83a59ebf6d041c57d445fefd69e9ec6cd019314f` | mm: memcg: fix NULL deref in __invalidate_reclaim_iterators |
| 2 | `def4b8a2613fd958daf882cfd4a9ff7a7e7ac1f0` | [vpsAdminOS] Preserve memcg CSS lifetime in memory views v2 |
| 3 | `b7609ccb76dabcb146356ea4c318715d1e9332bf` | [vpsAdminOS] sched: intersect fake affinity masks |
| 4 | `7ab40a1fe08da2c7cc2f6b369d10938c6579de81` | [vpsAdminOS] NFS: tolerate a cold NLM client during sysfs shutdown |
| 5 | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | [vpsAdminOS] Report ordinary cgroup swap consistently v3 |

The iterator patch keeps its independent generic identity and full original
Pavel Snajdr authorship, explanation, report and sign-off. CSS lifetime and early
guards are one v2 product owner, preserving Pavel's authorship, original Fixes
provenance and substantive chronological history. Its helper source matches the
original product exactly; the swap-view reference fix is adapted to ordinary
views. Affinity preserves Jakub Skokan's source/body/authorship/sign-off; its
subject receives the product marker only, so no semantic version is invented.
The NFS patch preserves Pavel's full message, sign-off and 6.12.109 provenance.

The final ordinary-view owner is independent of those safety patches and is
placed after them; none depends on its reporting arithmetic. It credits Pavel
and exact mixed-owner provenance. Its v1/v2/v3 history describes the original
mixed intent, the sysinfo extraction, and the four requested ordinary-view review
corrections. No custom proactive state or shared reporting framework is retained.

### Complete original-owner disposition and final upstream inventory

Rows 1–50 below retain their exact original ID, content, message and order.
Append the five-owner sequence above to those rows for the complete final
upstream-to-head series. The remaining original rows account for every omission,
fold or transplant.

| Original order | Original owner | Final disposition | Original subject |
| --- | --- | --- | --- |
| 1 | `f66047656f599a04407422afb34953f6b6e83839` | Same exact commit; inherited baseline | mem_cgroup_css_rstat_flush: fix NPE |
| 2 | `f6a3be8d94ecfc3f183d14bc457e7f9dbeff338c` | Same exact commit; inherited baseline | sched.h: include nommu.h |
| 3 | `aab33f20897f153a0c2cbb2330c4f88c40b17881` | Same exact commit; inherited baseline | [vpsAdminOS] Pushing GPL too much inhibits innovation |
| 4 | `cc468c700f3665455c3ff7ac69217b4aa652c34e` | Same exact commit; inherited baseline | [vpsAdminOS] Common functions |
| 5 | `1e8a19a71c2077c64a2614962228b01093b77d44` | Same exact commit; inherited baseline | [vpsAdminOS] Allow mknod in user namespace v2 |
| 6 | `c45dcd9c2c615ebc1c19352ecced8d232aa096e9` | Same exact commit; inherited baseline | [vpsAdminOS] Enable mounting Ceph in user namespace |
| 7 | `7df015b352f9f653544751d2d4d021df7593fffe` | Same exact commit; inherited baseline | [vpsAdminOS] Enable NFS in user namespace |
| 8 | `400b70495941b9b5ab7627198c1d569477389533` | Same exact commit; inherited baseline | [vpsAdminOS] nfsd: skip unknown words instead of ignoring them |
| 9 | `65115e17527fcdf71771e7d79ea0abdc25df6b50` | Same exact commit; inherited baseline | [vpsAdminOS] NFS client: force soft in CT |
| 10 | `2c221b260b9c7f38c6a9c0db054392d99578b360` | Same exact commit; inherited baseline | [vpsAdminOS] smb/client: force soft in CT |
| 11 | `9db02ef496e84104c99a06961276bc90572954f2` | Same exact commit; inherited baseline | [vpsAdminOS] Enable trusted xattrs for 1st-lvl userns |
| 12 | `284fe6df59835042b3f17a63592d59a623d55da4` | Same exact commit; inherited baseline | [vpsAdminOS] Ignore sync() calls from non-init user ns |
| 13 | `caf1ca7bd058f54834111ec9cdb86e6d0a9fa290` | Same exact commit; inherited baseline | [vpsAdminOS] fork: allow ct root fork over prlimit |
| 14 | `3efdbea2302bd986c1de985e6000a4d334b3c169` | Same exact commit; inherited baseline | [vpsAdminOS] proc/oom_score_adj: allow changing oom_score_adj_min from first-level userns |
| 15 | `3555692676ccde4f513b270fc013d15f06238861` | Same exact commit; inherited baseline | [vpsAdminOS] oom_kill exceptions for CT init & lxc |
| 16 | `f1ffad28d3dcf7a55f26ab5b7eb23d3ed5b05e6f` | Same exact commit; inherited baseline | [vpsAdminOS] /proc/stat: virtualize oom_kill v2 |
| 17 | `55a0cd80a61099752a6863a335de07022f3d2a95` | Same exact commit; inherited baseline | [vpsAdminOS] out_of_memory in memcg: last resort v3 |
| 18 | `6e4b1e9a2690d4562250f3f1219efcbdd5a36e19` | Same exact commit; inherited baseline | [vpsAdminOS] netfilter: make all sysctl values per net |
| 19 | `9166afd319cb73c0e0182f27c2afd9297beb2450` | Same exact commit; inherited baseline | [vpsAdminOS] Enable taskstats netlink in userns |
| 20 | `c061ef0c856509ad32703439a1f9974664b90d5b` | Same exact commit; inherited baseline | [vpsAdminOS] dump_stack: print memcg path |
| 21 | `ab6555cd05d3c0b9de3df20e2ad06659c34df7c5` | Same exact commit; inherited baseline | [vpsAdminOS] silence print_modules |
| 22 | `a136c3aac6db4d4e1dfba7bb3961def7bf6bb5fb` | Same exact commit; inherited baseline | [vpsAdminOS] Virtualize module parameters |
| 23 | `c107a8dd8ccf5b4e60b0a86b9014445b4c8c1448` | Same exact commit; inherited baseline | [vpsAdminOS] ipvs: enable configuration in userns |
| 24 | `b501613dd1bd56e1e6ba029babc304ef9381569d` | Same exact commit; inherited baseline | [vpsAdminOS] Allow container admin to renice tasks v2 |
| 25 | `067d69b968bb750e29961bc7cfa8a37f60a992c1` | Same exact commit; inherited baseline | [vpsAdminOS] procfs: fake uid_map for Docker v2 |
| 26 | `d7b2eb86175e8a032840b2f8f210ce803825d7d5` | Same exact commit; inherited baseline | [vpsAdminOS] sysctl: virtualize vm.swappiness |
| 27 | `cd1a8c094f2f3703b5fc732a18c5ec216c9c35a9` | Same exact commit; inherited baseline | [vpsAdminOS] Enable NFS server in containers |
| 28 | `ffe1b46509456bb1c7ce7f5e5db39c8647155631` | Same exact commit; inherited baseline | [vpsAdminOS] translate max gid to containers for ping_group_range netns sysctl v6 |
| 29 | `f52151fb6591710d602e6d06a2ca013b4062771d` | Same exact commit; inherited baseline | [vpsAdminOS] tmpfs: use 1/2 of memcg limit if present v3 |
| 30 | `1f0b72aeb1a5eeafd1b88caf5503b8c30e134642` | Same exact commit; inherited baseline | [vpsAdminOS] tmpfs: show uid/gid from current user_ns PoV |
| 31 | `b64b21f929ed7e906f12f661bc157274f04acc1d` | Same exact commit; inherited baseline | [vpsAdminOS] memcg: skip shrink_slab when cgroup_memory_nokmem |
| 32 | `7d57b65e2d50c448e74e2e0406bf12c331a9d813` | Same exact commit; inherited baseline | [vpsAdminOS] /proc/cpuinfo cache |
| 33 | `557227f8d5ea0eb066e95ce34553ac0670f59f39` | Same exact commit; inherited baseline | [vpsAdminOS] allow proc_pid_stack in 1st level userns |
| 34 | `2fd8fffd7001b2cc9872dfa0d3be154ba2a53e52` | Same exact commit; inherited baseline | [vpsAdminOS] dump_stack: print memcg path v2 |
| 35 | `5ca4cab11dfc4cdd3c53b7d66ead5fa5978fe598` | Same exact commit; inherited baseline | [vpsAdminOS] respect CAP_LINUX_IMMUTABLE in 1st level userns |
| 36 | `ca88e27931186c722b6762f760c0535c08d3ad46` | Same exact commit; inherited baseline | [vpsAdminOS] syslog_ns: v21 |
| 37 | `b933b0ada59df128258507fcceebdab174166461` | Same exact commit; inherited baseline | [vpsAdminOS] limit visible cpus for containers v16 |
| 38 | `944bcab9438bf7ef9c43ba84aec6b5cfd1856e85` | Same exact commit; inherited baseline | [vpsAdminOS] /sys/fs/vpsadminos |
| 39 | `ab8099a28ab2e3bddf35edcf1b46b15d73517e6b` | Same exact commit; inherited baseline | [vpsAdminOS] get_slabinfo: do nothing outside init userns |
| 40 | `48191791f11bc460cccd29e04005e2ea4b65b80c` | Same exact commit; inherited baseline | [vpsAdminOS] Hide diskstats in non-init userns |
| 41 | `af1fc8835a3acd83938bf85bbda819c859248101` | Same exact commit; inherited baseline | [vpsAdminOS] kvmalloc: kvmalloc_noreclaim |
| 42 | `65feb0c6fad58966754f0039dae1575c362415f5` | Same exact commit; inherited baseline | [vpsAdminOS] unprivileged BPF: round down time |
| 43 | `34221b5e9c8e5e8b420b6e54df010b0e3b2be828` | Same exact commit; inherited baseline | [vpsAdminOS] enable ipsec sysctls in 1stlvl userns |
| 44 | `34eca213f739506c140858d3046c5ee35f9f05c5` | Same exact commit; inherited baseline | [vpsAdminOS] Virtualize meminfo and swaps v4 |
| 45 | `9b4e42807767565e8ce201caddb56415c64d73a7` | Same exact commit; inherited baseline | [vpsAdminOS] syslog_ns: makedumpfile compat v2 |
| 46 | `6148a729711ca4db2f8c8163975dcd3c9bbed005` | Same exact commit; inherited baseline | [vpsAdminOS] Virtualize loadavg v18 |
| 47 | `212835625c605b754d6ff434d57a0e080dd0e452` | Same exact commit; inherited baseline | [vpsAdminOS] limit visible cpus for containers v17 |
| 48 | `c472cb613a5e9f36c10d58828dd87d78a2c11daa` | Same exact commit; inherited baseline | [vpsAdminOS] limit visible cpus for containers v18 |
| 49 | `8b123110b064574516fabea81ff2906f682aa67f` | Same exact commit; inherited baseline | [vpsAdminOS] set prb correctly |
| 50 | `108d4158fae3c0d0affb58491ee67b9f573b550e` | Same exact commit; inherited baseline | [vpsAdminOS] Virtualize loadavg v18.1 |
| 51 | `a9dd8baca1c921a11942fdc63862be4fcab2dce3` | Omitted experiment owner | mm: add proactive DAMON reclaim controls |
| 52 | `b1fe371e52aa7e7bee1ee5490c408ffed9a28c5d` | Experiment omitted; ordinary no-capacity row guard retained in `1dfea587406b7dd79973831d1677fb2418e5e9aa` | mm: expose proactive swap via virtual swap views |
| 53 | `a2425d1734ae90527da3f8494c76d839c2a60712` | Experiment omitted; ordinary intent extracted/adapted as `1dfea587406b7dd79973831d1677fb2418e5e9aa` | mm: account proactive swap on top of virtual swap |
| 54 | `7b11a3286173b93209b2c4c1f27614aed946cf5a` | Omitted experiment owner | mm/damon: add per-node reclaim scope support |
| 55 | `c89d7963a742b99287fd41c007f3358967ba15a2` | Omitted experiment owner | mm/damon: fix damon_reclaim scope updates from sysfs |
| 56 | `5bbdd2635be1a3ca6a34201626e93cee78256e70` | Omitted experiment owner | docs/mm/damon: document reclaim scope |
| 57 | `0ffa2e5c545f333fc43f116ad4ce17e1e35e86be` | Patch-equivalent transplant → `83a59ebf6d041c57d445fefd69e9ec6cd019314f` | mm: memcg: fix NULL deref in __invalidate_reclaim_iterators |
| 58 | `b2c3db758ae499f7b6cdb116e41fba26e219ba08` | Combined/adapted CSS v2 → `def4b8a2613fd958daf882cfd4a9ff7a7e7ac1f0` | vpsadminos: fix memcg CSS ref ownership in memory views |
| 59 | `8d97a7a9c6aa096d58ff87269168b28c54a9b548` | Patch-equivalent, marker corrected → `b7609ccb76dabcb146356ea4c318715d1e9332bf` | sched: intersect vpsadminos fake affinity masks |
| 60 | `35b639015c452a5834371ee67b31554031780f31` | Combined/adapted CSS v2 → `def4b8a2613fd958daf882cfd4a9ff7a7e7ac1f0` | vpsadminos: tolerate missing early memcg CSS |
| 61 | `11058eb4fe1cba30653e8e643546c13bc8bcd792` | Patch-equivalent transplant → `7ab40a1fe08da2c7cc2f6b369d10938c6579de81` | [vpsAdminOS] NFS: tolerate a cold NLM client during sysfs shutdown |

## Final original-product-to-new-product diff

Exact two-tree comparison:

```bash
git --git-dir=repos/linux.git diff --no-ext-diff --binary 11058eb4fe1cba30653e8e643546c13bc8bcd792 1dfea587406b7dd79973831d1677fb2418e5e9aa
```

This complete source diff is anchored by retained immutable commits. Its summary
is `28 files changed, 160 insertions(+), 821 deletions(-)`. Every changed path belongs to the union of
the six omitted owners' original file sets; no unrelated path changed against
the original product.

| Path | Added | Removed | Final behavior / reason |
| --- | --- | --- | --- |
| `Documentation/ABI/testing/sysfs-kernel-mm-damon` | 1 | 3 | Exact inherited-prefix documentation restored; experiment ABI description removed |
| `Documentation/admin-guide/cgroup-v2.rst` | 2 | 11 | Exact inherited-prefix documentation restored; experiment ABI description removed |
| `Documentation/admin-guide/mm/damon/reclaim.rst` | 1 | 49 | Exact upstream .113 DAMON source/documentation restored |
| `Documentation/admin-guide/mm/damon/usage.rst` | 1 | 3 | Exact upstream .113 DAMON source/documentation restored |
| `fs/proc/meminfo.c` | 11 | 24 | Ordinary-view v3 cgroup-v1 capacity/usage correction and finite-v2 free-space bounds |
| `include/linux/damon.h` | 0 | 12 | Exact upstream .113 DAMON source/documentation restored |
| `include/linux/memcontrol.h` | 1 | 24 | Exact inherited-prefix native interface/implementation restored |
| `include/linux/swap.h` | 10 | 19 | Exact inherited-prefix native interface/implementation restored |
| `include/linux/swap_cgroup.h` | 3 | 11 | Exact inherited-prefix native interface/implementation restored |
| `kernel/sys.c` | 14 | 26 | Ordinary-view v3 unlimited capacity and finite-v2 free-space bounds |
| `mm/damon/core.c` | 4 | 163 | Exact upstream .113 DAMON source/documentation restored |
| `mm/damon/dbgfs.c` | 1 | 3 | Exact upstream .113 DAMON source/documentation restored |
| `mm/damon/lru_sort.c` | 0 | 1 | Exact upstream .113 DAMON source/documentation restored |
| `mm/damon/paddr.c` | 1 | 2 | Exact upstream .113 DAMON source/documentation restored |
| `mm/damon/reclaim.c` | 41 | 275 | Exact upstream .113 DAMON source/documentation restored |
| `mm/damon/sysfs-schemes.c` | 0 | 3 | Exact upstream .113 DAMON source/documentation restored |
| `mm/internal.h` | 1 | 2 | Exact inherited-prefix native interface/implementation restored |
| `mm/madvise.c` | 8 | 8 | Exact inherited-prefix native interface/implementation restored |
| `mm/memcontrol.c` | 15 | 60 | Ordinary prefix charging plus patch-equivalent generic iterator safety |
| `mm/memory.c` | 1 | 1 | Exact inherited-prefix native interface/implementation restored |
| `mm/shmem.c` | 1 | 1 | Exact inherited-prefix native interface/implementation restored |
| `mm/swap.h` | 2 | 2 | Exact inherited-prefix native interface/implementation restored |
| `mm/swap_cgroup.c` | 0 | 34 | Exact inherited-prefix native interface/implementation restored |
| `mm/swap_slots.c` | 2 | 2 | Exact inherited-prefix native interface/implementation restored |
| `mm/swap_state.c` | 2 | 2 | Exact inherited-prefix native interface/implementation restored |
| `mm/swapfile.c` | 25 | 47 | Ordinary prefix view, CSS lifetime owner and v3 no-capacity row guard |
| `mm/vmscan.c` | 11 | 32 | Exact inherited-prefix native interface/implementation restored |
| `mm/workingset.c` | 1 | 1 | Exact inherited-prefix native interface/implementation restored |

### Dependency and safety reasoning

- Every experiment-touched file except `mm/memcontrol.c`, `mm/swapfile.c`,
  `kernel/sys.c` and `fs/proc/meminfo.c` is exactly its inherited-prefix blob.
  Thus callers, prototypes, swap bitmap machinery, charging/bypass plumbing
  and custom DAMON controls are restored together.
- `mm/memcontrol.c` adds only the original generic iterator RCU/null protection
  to the prefix. Its stable patch ID equals the retained source owner.
- `kernel/vpsadminos.c`, `kernel/sched/syscalls.c` and `fs/nfs/sysfs.c` are
  byte-identical to the original product. The CSS reference acquisition and
  early/disabled guards, affinity behavior and cold-NLM check remain intact.
- `mm/swapfile.c` retains the original ownership fix: `show()` does not put the
  memcg, failed `single_open()` puts it, and release drops the reference once
  before `single_release()`. Ordinary capacity/usage calculations retain the
  prefix semantics; the v3 guard returns after the header when selected
  capacity is zero. No `virtual-system` row remains.
- The ordinary-view owner retains host capacity for unlimited sysinfo in both
  cgroup versions and for cgroup-v1 meminfo. Changed v1 paths use ordinary
  `max(0, memsw_usage - memusage)`; finite meminfo selects container capacity
  before free-space calculation. Finite-v2 free space is bounded at zero in
  both meminfo and sysinfo after a legal limit reduction below current usage.
  Native and compat sysinfo share `do_sysinfo()`. No-capacity /proc/swaps is
  header-only for either cgroup version.
- Native `MEMCG_RECLAIM_PROACTIVE`, `memory_reclaim()` and
  `proactive_swappiness` remain. `mm/damon`, `include/linux/damon.h` and the
  DAMON admin-guide directory compare exactly with upstream v6.12.113.
- The custom flags/counters/bitmap/event/view/quota/scope implementations are
  absent. Other retained kernel entries are outside this source package; the OS
  owner changes only the selected .113 source pin.

The four original CSS/scheduler/NFS safety commits become three coherent product
owners because the two CSS commits are folded. The generic iterator remains
independent. The revised ordinary-view owner adds one meaningful
reporting boundary; it does not retain the mixed experimental owner.

## Quick verification performed

| Check | Result |
| --- | --- |
| `git diff --check` old product → final and task base → final | Passed |
| Native `scripts/checkpatch.pl --no-tree --no-signoff` on task source diff | 0 errors, 0 warnings, 227 lines checked |
| Combined CSS and ordinary-view v3 source checks | 0 errors, 0 warnings (97 / 70 lines) |
| Reviewed v2 → final v3 diff | Exactly requested three files, 15 insertions / 7 deletions; diff --check passed |
| Exact upstream comparison: DAMON code/header/admin docs | No differences |
| Exact prefix comparison of all non-adapted experiment paths | No differences |
| Custom-interface search in original affected source/docs areas | No remaining experimental symbols/interfaces |
| Native reclaim symbol/source inspection | Native proactive reclaim and swappiness paths present |
| Original-to-final changed-file union | All 28 paths belong to omitted owner file sets |
| Original iterator / new iterator stable patch ID | `423a142ce07f6f11145efe2b73b6e05168dbfc2b`, equal |
| Original affinity / new affinity stable patch ID | `5fc35c9e255e8e80127f11fcbf2177ecdc79bd6d`, equal |
| Original NFS / new NFS stable patch ID | `a4647d7634f67a8253d5b303fef012a6c979e940`, equal |
| Original product CSS helper / affinity / NFS whole files | Exact final blob equality |
| Prefix / old range / final range / task suffix commit counts | 50 / 61 / 55 / 5 |
| Full final range merge count | Zero |
| Working tree after final commits | Clean |
| New feature publication and exact remote head | Verified over SSH |

The exact Linux tree contains no AGENTS.md, declared Overcommit/pre-commit/
Lefthook framework, Nix development shell or active custom hook path. Native
patch checks were used; no hook was bypassed. Existing author/sign-off and
upstream/subsystem identity were preserved as described above.

Useful reviewer commands from the workspace root:

```bash
git --git-dir=repos/linux.git log --reverse --format=fuller 7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e..1dfea587406b7dd79973831d1677fb2418e5e9aa
git --git-dir=repos/linux.git log --reverse --format=fuller 108d4158fae3c0d0affb58491ee67b9f573b550e..1dfea587406b7dd79973831d1677fb2418e5e9aa
git --git-dir=repos/linux.git range-diff 108d4158fae3c0d0affb58491ee67b9f573b550e..11058eb4fe1cba30653e8e643546c13bc8bcd792 108d4158fae3c0d0affb58491ee67b9f573b550e..1dfea587406b7dd79973831d1677fb2418e5e9aa
git --git-dir=repos/linux.git diff 108d4158fae3c0d0affb58491ee67b9f573b550e 1dfea587406b7dd79973831d1677fb2418e5e9aa -- fs/proc/meminfo.c kernel/sys.c mm/swapfile.c kernel/vpsadminos.c
git --git-dir=repos/linux.git diff 86d54e7adff82e632299b41a2d1397ccbec1cb9e 1dfea587406b7dd79973831d1677fb2418e5e9aa -- fs/proc/meminfo.c kernel/sys.c mm/swapfile.c
git --git-dir=repos/linux.git diff 11058eb4fe1cba30653e8e643546c13bc8bcd792 1dfea587406b7dd79973831d1677fb2418e5e9aa
```

## Consolidated review and narrow remediation

The original [review packet](review-packet.md) and its exact Linux
`86d54e7adff82e632299b41a2d1397ccbec1cb9e` / OS `bf9bcb5e83f21d17561aad9416eeef2853d90956` anchors remain the
original review checkpoint. The dated remote source backup retains that exact
Linux object and archive provenance. The lead reported final independent review
complete with Important I1–I4, no Blocking or other source-removal findings.
Whole-prefix/history, logical ownership, migrations and original source-pin
conclusions were otherwise accepted. The lead directly inspected the prepared
three-file 15-add/7-remove remediation and authorized its coherent v3 fold and
exact-lease publication. These were the reviewer's direct requested fixes;
the lead owns final direct reconciliation under the narrow-remediation workflow.

| Finding | Final ordinary-view v3 correction |
| --- | --- |
| I1: cgroup-v1 meminfo unlimited path unreachable / combined usage | Keep `PAGE_COUNTER_MAX` outside the zero branch; preserve host total and derive swap-only usage from memsw minus resident memory. |
| I2: finite-v1 free swap uses earlier host capacity | Set `memsw - totalram` capacity before computing bounded free space. |
| I3: finite-v2 free space wraps after lowering limit below current usage | Clamp free to zero in both meminfo and sysinfo; configured capacity and actual charging remain unchanged. |
| I4: host capacity zero still yields an empty virtual swap row | Return after the existing header when computed capacity is zero in either cgroup version. |

Only the final ordinary owner changes between reviewed and final heads; its
parent remains `7ab40a1fe08da2c7cc2f6b369d10938c6579de81`. The first four suffix
owners and all 50 inherited commits are exact same objects. The v2 owner is
retained through the review backup, while the shipping task suffix contains v3
only, with truthful chronological history and both mixed-source credits.

Advisory: the inherited ordinary `/proc/swaps` virtual row still prints byte
values where the interface normally uses KiB. The lead explicitly excluded this
pre-existing mismatch from the current fix. It is a known staging-validation
limitation; no runtime test result is claimed for it and no unit conversion was
added in this work.

## Documentation, migrations and validation gaps

The kernel's experiment-only DAMON ABI/usage/reclaim documentation is removed
with its owners and restored to the native source. The relevant project policy
is vpsAdminOS `docs/os/patch-series-policy.md`; current intent and the accepted
ordinary-view adjustment live in [design.md](design.md). The 6.18-specific
platform documentation and ordinary test files were not edited by this package.

**No migrations.** This package introduces no database/schema, persisted
container/on-disk format, API/client/Terraform or daemon protocol migration.
There is no merged, released, deployed or externally consumed migration version
to consolidate. Original source refs and the dated backup protect reconstruction
evidence; they do not create a deployed rollback contract. No compatibility
bridge is needed under the user's never-deployed premise.

No kernel/module build, boot, runtime test, full suite or CI wait was performed.
No tests were authored. Compilation and runtime correctness remain unverified;
the user owns subsequent staging validation after the lead's independent review
and OS `staging` integration. The OS pin/archive-byte hash and bounded Nix
checks are implementer1-owned. This source report does not claim OS integration,
deployment, final independent acceptance or readiness for production use.

## Acquisition note

Session command, both environment identities and retained implementation role
were verified. The canonical non-shallow `blob:none` clone lacked .113 objects.
An explicit bounded SSH fetch acquired the exact named product branch, whose
head was verified against `11058eb4fe1cba30653e8e643546c13bc8bcd792`; .109 source was not substituted. A dated
backup preceded source reconstruction.

The clone had approximately 39,533 packfiles and a 36-day-old multi-pack-index.
Refreshing that index made new object lookups fast. The first fetch's old index
state was interrupted and the same bounded fetch then succeeded. Missing-object
probes and normal fetch connectivity walks were expensive in this promisor
clone; a single object enumeration identified 3,270 missing blobs for the exact
upstream/prefix/suffix snapshots. Explicit blob hydration used transient
`fetch.hideRefs=refs/` and `fetch.negotiationAlgorithm=noop` settings to keep
connectivity work bounded. Inspection thereafter retained `GIT_NO_LAZY_FETCH=1`.
All packs, old refs and other sessions' worktrees were preserved; no cleanup
or lifecycle operation was performed. The registered task worktree started at
the exact inherited prefix, whose unchanged history was verified before source
changes and remains the common ancestor of old and new product tips.
