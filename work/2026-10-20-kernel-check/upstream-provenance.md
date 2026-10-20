# Upstream range provenance and old livepatch overlap

Owner: implementer0. Bounded provenance work after the lead accepted the custom
phase's negative result; semantic source audits remain with their assigned
owners. No source change, build, test, production mutation or new fetch.

## Exact range and totals

- Old stable base: `296aabce459470a4c1b68ffd0c0c0920e563aaad` (6.12.95).
- New stable base: `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` (6.12.113).
- Effective incident tree: `1dfea587406b7dd79973831d1677fb2418e5e9aa`.
- `git merge-base --is-ancestor OLD NEW` returns 0. `git rev-list --count
  OLD..NEW` returns **7,278**. The extracted commit/path inventory contains
  5,291 distinct changed paths and includes 18 release-version commits.

Counts below are commits touching at least one matching path; categories overlap
and must not be summed. They locate an audit scope, not suspected defects.
The complete metadata/path inventory was extracted locally with
`GIT_NO_LAZY_FETCH=1`, using `git log --no-renames --name-only OLD..NEW`.

| Scope | Path predicate | Commits |
| --- | --- | ---: |
| Memory | `mm/` | 123 |
| Memcg core | `mm/memcontrol.c`, `include/linux/memcontrol.h` | 7 |
| Selected reclaim/swap core | `mm/{vmscan,swapfile,swap_state,swap_slots,page-writeback,workingset,oom_kill}.c` | 7 |
| Cgroup | `kernel/cgroup/`, `include/linux/cgroup.h`, `include/linux/cgroup-defs.h` | 9 |
| NFS client | `fs/nfs/` | 27 |
| NFS server | `fs/nfsd/` | 70 |
| SUNRPC | `net/sunrpc/` | 58 |
| Lockd | `fs/lockd/` | 5 |
| Generic VFS / iomap / writeback | Direct `fs/*.[ch]`, `fs/iomap/`, `mm/page-writeback.c`, `include/linux/{writeback,fs,pagemap}.h` | 60 |
| Scheduler | `kernel/sched/`, `include/linux/sched*` | 23 |
| RCU | `kernel/rcu/`, `include/linux/rcu*` | 3 |
| Locking | `kernel/locking/`, `include/linux/lock*` | 6 |
| x86 | `arch/x86/` | 116 |
| Drivers | `drivers/` | 3,735 |
| Printk | `kernel/printk/`, `include/linux/printk*` | 7 |

Direct overlap with files carrying the custom Linux code:

| Path | Upstream range commits |
| --- | ---: |
| `kernel/syslog_namespace.c` | 0 (downstream-only file) |
| `kernel/vpsadminos.c` | 0 (downstream-only file) |
| `kernel/sched/syscalls.c` | 0 |
| `kernel/cgroup/rstat.c` | 0 |
| `fs/proc/meminfo.c` | 0 |
| `fs/nfs/sysfs.c` | 0 |
| `kernel/printk/printk.c` | 6 |
| `kernel/sched/core.c` | 4 |
| `kernel/cgroup/cpuset.c` | 7 |
| `mm/memcontrol.c` | 4 |
| `mm/swapfile.c` | 5 |
| `kernel/sys.c` | 1 |

These are whole-file overlap counts. They do not prove a change in the custom
hunks or exclude effects through callers, headers, locks or upstream helpers.
The complete downstream correspondence remains in [patch-inventory.md](patch-inventory.md).

## What the documented `.95.6` variants replace

At OS `c3f219a385e605ac00f2864c9c311902620271cd`,
`os/livepatches/available-patches.nix` explicitly selects version 6 and these
alternative cumulative/uname pairs. Original boot source is
`a2384967b90f24d2470c9eb15f0e66d938df7e08`; the documented NFS-cancellation boot
source is `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd`.

| Source patch under `os/livepatches/` | Bytes | Touched paths | SHA-256 |
| --- | ---: | ---: | --- |
| `bp-6.12.95-cumulative.patch` | 223,401 | 91 | `b8ba1b2fba3ba64ae890f0633aef26e053a942dff7f930179a357af9fae23171` |
| `bp-6.12.95-uname.patch` | 2,340 | 1 | `7ffc32367cbacfb1f7453f158985eacc7d512e1dd0eb01094eebbca01acc9a3c` |
| `bp-6.12.95-nfs-cancel-cumulative.patch` | 176,130 | 86 | `3da19eccaf56d2d73377902cc370c37d1444d4430a450951458d293e1fc97c1f` |
| `bp-6.12.95-nfs-cancel-uname.patch` | 2,563 | 1 | `fd770697c2ece0c6773d4700295825c514b7b92df0fff7701279fae6e8306f53` |

The plain cumulative patch is byte-identical at original v6 integration
`d9bd139cd3005657c5084dccda159b083ca9390d` and the variant-selection revision
above. Scanned all four patches, including their paths and added/removed text:

- Neither pair modifies `kernel/syslog_namespace.c` or
  `include/linux/syslog_namespace.h`; neither contains any `syslog` token.
  Thus the documented patch sources do not fix/replace `clone_syslog_ns`,
  `copy_syslog_ns`, `syslog_ns_setup_log_buf`, `syslog_ns_log_buf_free`,
  `free_syslog_ns` or `setup_syslog_namespace`.
- Neither pair modifies `kernel/vpsadminos.c`, `mm/swapfile.c`,
  `fs/proc/meminfo.c` or `kernel/sys.c`, or names
  `get_current_most_limited_memcg`, `fake_swap_show`, `swaps_open` or
  `swaps_release`. There is no source overlay of the audited custom memcg
  lifetime/swaps helper in these variants.
- Neither pair modifies `kernel/printk/printk.c`, ZFS `dnode_sync.c` or
  `dbuf.c`, or supplies the separately packaged ZFS free-accounting change.
  ZFS recipe selection is covered by the corrected ancestry paragraph in the
  custom inventory and [zfs-patch-audit.md](zfs-patch-audit.md).
- Original/NFS boot trees also have identical
  `kernel/syslog_namespace.c`, `kernel/vpsadminos.c`, `mm/swapfile.c` and
  `kernel/printk/printk.c` (direct endpoint comparison).

This excludes a direct fix in the documented v6 patch sources for those audited
functions. It does not certify all interactions or independently inventory a
loaded binary's replacement table. Generated header fanout, altered callers and
runtime transition state remain distinct questions. **The exact old loaded
module and its active transition state are unknown.** A `.95.6` release string
alone cannot prove that a historical source-described fix was active on node24.

## Targeted old-livepatch overlap for upstream owners

The documented source branch
`fc37ccc43227ab8eef70b50660a081f2615d0ead` is 104 commits above original boot
`a2384967...` and contains 74 upstream/prerequisite commits plus livepatch
adaptations. All 74 upstream/prerequisite commits map into the stable range by
explicit upstream IDs, except the stable-specific TLB ordering fix whose
complete commit message matches. This is lineage accounting, not 74 independent
payload-function or runtime-activation certifications.

Relevant overlap sent to the source owners:

| Fix | Old backport source | Stable-range counterpart |
| --- | --- | --- |
| mm/huge_memory: fix huge_zero_pfn race | `22fa8d08569ef23605a3c717fc828b861cf5eff9` | `6024f6d0d9b9ca5138bfc4ac6f6e4bdf616e42b3` |
| NFS: Pin the 'struct nfs_server' during a FREE_STATEID call | `6d5cc0d6681c54a1ddf186a4f9872ee1ae062612` | `ed1161ab6239761958b38d5667225634fc2be894` |
| mm/vmalloc: take vmap_purge_lock in shrinker | `3fed23dbf00ab8b562eeb0f971212bbc8b168e16` | `c15ff206ba78820bf2873d0c668a882e99f4b631` |
| posix-cpu-timers: Prevent UAF caused by non-leader exec() race | `d9f980d536c9eacd3d0febc9d8cbc22ed6ec1808` | `e74443f5db0037c556ef436fa64b88bf4ea08f83` |
| SUNRPC: pin upper rpc_clnt across the TLS connect_worker | `2b04179fb10b74a9285b2fb377bb340a0bd91af2` | `7a65b41b657b71d5a77861f47dd13eb4bc8e10d0` |
| nfs: use nfsi->rwsem to protect traversal of the file lock list | `90eeb06c03ae60c08128c3a4f5a80bb020eb73f0` | `1cda95bf2e9c0e6b63545b7565fe4a1e474322f4` |
| x86/mm: Fix check/use ordering in switch_mm_irqs_off() | `acd4273495dcc8dd41647de5c1e069b5836426d0` | `0650f1c8b6b02b3edd489848fb9daa325eccf42c` |
| perf/core: Detach event groups during remove_on_exec | `80d0b7fda7903a41e76dfd7c017f78078bbbc210` | `39358e856fb89e62e3c8d7389a2dc4ec33dbe90e` |
| x86/bugs: Enable IBPB flush on BPF JIT allocation | `209fc0382f260e24c450bd4e0591ad9d58b5897f` | `9354248fc1c33a844ca1872761f6668b393e8c37` |
| x86/bugs: Make Safe-RET robust against interrupt injection | `71fce134f76cce3a2d4cb0c728e6cf297a11ab5b` | `e262f28a69ae9e0791248f93b0173c1d1f3e1d5d` |

The vmalloc pairing uses upstream
`ec05f51f1e65bce95528543eb73fda56fd201d94`. The old plain cumulative patch
explicitly adds `guard(mutex)(&vmap_purge_lock)` to the shrinker. Therefore the
new mutex in `vmap_node_shrink_scan` is already represented by the old v6
source; range membership cannot establish that it is a new runtime behavior.
The old source also contains the `huge_zero_lock` race fix, NFS FREE_STATEID
transition glue, inode lock-list `nfsi->rwsem` operations and SUNRPC TLS client
lifetime protection. The NFS variant moves the corresponding NFS/SUNRPC fixes
into its boot source and omits their old livepatch replacements.

The old cumulative source also explicitly contains the synchronous
`on_each_cpu(vpsadminos_bpf_jit_ibpb_cpu, NULL, 1)` IBPB operation in
`arch/x86/kernel/cpu/bugs.c` and the Safe-RET handler/assembly stubs. The IBPB
pair uses upstream `a3af84b0fa00ead01fcd0e28b5d773ff25990a0d`; the Safe-RET
pair uses `7e7f81cf6f5ca3311e526308f55d7c54d3ba71f9`, with livepatch adaptation
owners `7ebdba98330ffa65ce536dd810c307ad198c0f69` and
`0b13466d3c6dcafec0454422598de8f43ba7326d`. These are source-described old
security changes, not automatically new runtime operations at the upgrade;
CPU/configuration gates and the loaded payload/transition state remain relevant.

NFS FREE_STATEID counterpart `ed1161ab...` is the exact ref reported by the NFS
owner for a bounded allocation-failure reference leak. Its old effective-source
comparison is more specific than the raw upstream pairing:

- At `fc37ccc43227ab8eef70b50660a081f2615d0ead`,
  `fs/nfs/nfs4proc.c:10776` defines `vpsadminos_nfs_freeid`. Its allocation
  failure takes `out_deactive`, dropping the superblock and client references
  at lines 10864–10867. `nfs41_free_stateid` at line 10884 routes through this
  adapter when the v6 control exists. The historical `d9bd139cd...` cumulative
  patch explicitly contains the adapter and cleanup. The inactive/raw fallback
  still lacks that cleanup, so configuration and control/transition state matter.
- At documented NFS boot source
  `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd`,
  `fs/nfs/nfs4proc.c:10610` also releases both references when allocation fails;
  its NFS livepatch variant omits this already-integrated replacement.

Thus the `.113` static-source leak must not be labelled an equally pre-existing
runtime leak from the `.95` base alone. The source-described active plain v6
adapter and NFS boot variant both clean it up. The actual old loaded module,
configuration and control/transition state remain unknown. The NFS owner
determines applicability and impact; this is not a host-hang cause claim.

## Locally available later-fix limit

The canonical Linux repository has no referenced later stable release after
6.12.113. An ancestry-limited scan of all local refs above exact `.113` base
found 67 commits, all downstream/custom or retained intermediate variants, and
no `Linux ...` release marker. Only two carry explicit `Fixes:` lines: the
original and consolidated memcg lifetime owners, both pointing to existing
custom owners rather than an upstream-range regression. Those owners were
already accounted for in the custom inventory. No later upstream fix/revert
explicitly repairing a regression introduced in this range was available in
that bounded referenced-history scan.

The 6.18.49 source pin `a770f5086fc500ca258852aea1cb3e209a342d2b` is not a local
commit (`GIT_NO_LAZY_FETCH=1 git cat-file -e ...^{commit}` refuses). It was not
fetched. No remote refs, unbounded external search, future stable history or
unreachable-object sweep was requested or performed. **This local limit is
not evidence that a relevant upstream fix does not exist.**

Checks: stable ancestry/count, commit/path inventory totals, exact v6 variant
selector and source hashes, targeted body/identity matches, local post-base
message scan, and Markdown whitespace check. No additional blob materialization
was needed for this package. Source-audit findings and incident attribution
remain with their named owners; this artifact claims no new incident cause.
