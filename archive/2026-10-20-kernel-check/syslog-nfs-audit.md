# Syslog namespace and NFS source audit

Owner: implementer3. Read-only investigation; no source/ref edits, builds,
tests, production writes or reproductions. Session/environment identity matched
`2026-10-20-kernel-check` and `/home/aither/workspace/ai/vpsfree.cz`.
This artifact follows the architect's `design.md` and the lead's narrower lane
assignment. Repository README and relevant source/callers were inspected; no
root Linux `AGENTS.md` exists in the selected tree.

## Result and confidence

No supported new downstream syslog/NFS failure chain explains the incident.
One allocation-error crash is source-proven but pre-existing. It is not proof
of a whole-host hang. A separate pre-existing NFS shutdown/unmount lifetime
concern remains unproven and must not be presented as an incident cause.

| Candidate | Code result | Required trigger / incident evidence | Classification |
| --- | --- | --- | --- |
| Syslog v20→v21 namespace lock/lifetime regression | Normalized printk patch added/removed lines identical; namespace storage/ownership sources identical | No newly changed namespace lock or owner found | Excluded within this downstream-delta scope |
| Syslog namespace allocation cleanup | Definite NULL dereference after ring-buffer allocation failure; identical in all three trees | Explicit new syslog namespace followed by allocation failure; neither established near incident | Source-proven defect, incident attribution unresolved; pre-existing |
| NFS cold NLM guard introduces hang | New code only returns for NULL; non-NULL path unchanged | Sysfs `shutdown=1`, absent RPC client; ordinary successful mount eagerly binds NLM in all three trees | Not supported; ordinary cold-mounted-client premise contradicted by source |
| NFS shutdown races unmount | Teardown releases RPC/NLM resources before deleting shutdown sysfs node; callback takes raw pointers | Concurrent privileged shutdown write and teardown, plus final-ref/lifetime conditions; no incident evidence | Unresolved pre-existing lifetime concern, not a demonstrated incident mechanism |
| NFS timeout immediately before logging stops | Timeout can establish remote RPC non-progress, not execution of shutdown callback | Need callback/unmount/stack evidence; supplied log lane has none | Not supported as attribution to this guard |

## Versions and equivalence checks

References: old `a2384967b90f24d2470c9eb15f0e66d938df7e08`, initial .113
`11058eb4fe1cba30653e8e643546c13bc8bcd792`, current .113
`1dfea587406b7dd79973831d1677fb2418e5e9aa`. Source line numbers below are
at current .113 unless stated otherwise. Exact deployed package provenance is
owned by the inventory/package lanes; the lead reports vpsAdminOS `2abbe3cc`.

Exact `git ls-tree` blob equality across **all three** refs:

| Path | Blob |
| --- | --- |
| `kernel/syslog_namespace.c` | `e55346ef9a374d12966d4c10ae3d81fb0d9949c1` |
| `include/linux/syslog_namespace.h` | `4d6c605cf3f58880005ce1255a35512ecdfa7f29` |
| `fs/proc/kmsg.c` | `0f4990848f025ea051f368d3c6e0c8d2029c4c16` |
| `fs/kernfs/dir.c` | `ec55b8dac57d860322885b239f70a21d2a6ceaa3` |
| `fs/lockd/clntlock.c` | `a7e0519ec024a9f73ca05d0d4a0ca29f22d0eb23` |

`fs/nfs/sysfs.c` is old blob `53d4cdf28ee008fd8ab1df25533754a78205dbb0`
versus both new refs' `d72e4c29444a40c53a6440192319ae20dd045dea`.
Its entire old/new delta is the three-line NULL guard in `shutdown_client`.
There are no initial→current .113 changes in this lane's printk/NFS/lockd paths.
Direct old/new diff also found no changes in `kernel/nsproxy.c` or
`kernel/user_namespace.c`.

Compared `14e1e939b8ce` (v20) and `ca88e2793118` (v21) parent-to-commit
`kernel/printk/printk.c` patches after removing hunk offsets, index and file
headers: all additions and removals match. The only remaining difference is
context immediately before `vprintk_emit`, now containing upstream's
`debug_non_panic_cpus` module parameter. Old/new effective printk differences
are upstream panic helpers/non-panic CPU logging and console-flush refactoring,
not a newly different namespace adaptation. Those contexts were inspected to
validate that namespace-aware entrypoints and initial-ring-buffer selection
survive the port; this is not a general upstream printk audit.

The separately reapplied `set prb correctly` patch sets global `prb` alongside
`ns->prb` in early `setup_log_buf` (current printk.c:1230–1233). This is an
initialization-time assignment under local IRQ exclusion, not a runtime
namespace-switching lock or a new delayed progress dependency.

Inventory owner implementer0 independently reports exact path/addition/removal
equivalence for the retained NFS patches: user namespace support
`21afe14423c8`→`7df015b352f9`, nfsd word parsing
`bb7abf8a43bb`→`400b70495941`, force-soft container mounts
`3dcfa2a13c69`→`65115e17527f`, and container NFS server support
`ea9578903c18`→`cd1a8c094f2f`. The newly added guard has identical body in
initial/current .113. The stable bases are old
`296aabce459470a4c1b68ffd0c0c0920e563aaad` and new
`7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e`. The effective old/new
`fs/nfs/client.c` changes concern upstream NFSv4 callback-IDR removal and
per-net data-server caching, not `nfs_start_lockd` or server destruction ordering.

## Source-proven pre-existing syslog allocation failure

Concrete path in `kernel/syslog_namespace.c`:

1. `clone_syslog_ns` allocates the namespace with `kzalloc` at line 128,
   proving `ns->prb == NULL`. Lines 145–148 initialize its mutex, wait queue,
   spinlock and list; none is acquired here.
2. Line 151 calls `syslog_ns_setup_log_buf`. Its four allocations are the
   ring-buffer object (44), text (48), descriptors (56), and info (61).
   The namespace's `prb` is assigned **only after all succeed**, at line 70.
3. Failure at any allocation returns `-ENOMEM` through lines 77–85, after
   freeing any locally acquired components. In every such path `ns->prb`
   remains NULL. Failure before the initial namespace allocation or in
   `ns_alloc_inum` instead takes other cleanup paths and does not hit this bug.
4. Caller lines 152–160 select `fail_free_log_buf`, drop parent/user refs,
   then call `syslog_ns_log_buf_free(ns)`.
5. That routine immediately evaluates `ns->prb->desc_ring.descs` at line 90.
   This dereferences NULL before an error can return to the clone caller.

On descriptor/info allocation failure, `ns->log_buf` also still names text
already freed by setup's local unwind. Line 93 would free it again **if execution
ever reached that line**. The unconditional first failure is the line-90 NULL
dereference; do not describe a double-free as the actual first executed fault.

Trigger requires `CONFIG_SYSLOG_NS`, an explicit request for a new logging
namespace and failure of one of these allocations after namespace creation
has progressed this far. `do_syslog(SYSLOG_ACTION_NEW_NS)` sets the child flag
and name (printk.c:1840–1865); `copy_namespaces` checks capability and routes
the flag into `create_new_namespaces` (nsproxy.c:168–197). That routine calls
`copy_syslog_ns` at 126–127 after the preceding `copy_*` routines have returned.
`copy_syslog_ns` calls clone only when its `new` flag is true (170–181).

Ownership/locking: the new nsproxy and namespace are private and not yet
installed into the child; `copy_namespaces` installs only after success
(nsproxy.c:204). The selected path holds references to old/parent/user
namespaces, not their locks. No syslog mutex/spinlock, console semaphore,
mount namespace lock or `userns_state_mutex` is visibly held across this
allocator/cleanup call in the inspected immediate path. `copy_process` calls
`copy_namespaces` at fork.c:2424 after earlier copy routines return. Therefore
this source proof establishes an oops/crash in creation context, not an orphaned
global-lock cycle or a whole-host progress failure. Panic-on-oops configuration
or a separate lock held by an unexamined caller could change consequences;
neither is established here.

Blob equality proves the defect predates .113 and the v21 port. Central logs
may fail to preserve an oops, but absence of a record supplies no evidence of
the necessary allocation failure or namespace creation. A focused future test
would fault-inject each of the four allocation stages during explicit namespace
creation on an isolated matching kernel, compare old/new, then compare a
minimal cleanup correction. No such test or fix is authorized/executed here.

## NFS guard, cancellation, ownership and removal

`7ab40a1fe08da2c7cc2f6b369d10938c6579de81` adds only:

```c
if (!clnt)
    return;
```

before the existing `clnt->cl_shutdown = 1` and `rpc_cancel_tasks(..., -EIO, ...)`
in sysfs.c:228–235. It does not add locks, waits, ref drops, retries, or an
early return from the **server** shutdown operation. The caller still sets
`NFS_MOUNT_SHUTDOWN`, shuts down available server/ACL/NLM clients, and invokes
`shutdown_nfs_client` (280–294). The latter checks `cl_superblocks` under an RCU
read section, releases RCU, then marks/cancels the shared client when every
remaining listed server has shutdown set (243–252). There is no RCU-held wait
introduced by this guard.

Crucially, clntlock.c:61–62 already calls `nlm_bind_host` if `h_rpcclnt` is NULL
and fails initialization if binding fails. `nfs_start_lockd` assigns
`server->nlm_host` only after successful `nlmclnt_init` (client.c:619–625).
`nlm_bind_host` creates/assigns the RPC client under `host->h_mutex`
(host.c:435–487). Consequently a normally completed NFSv2/v3 mount does not
retain a client-side `nlm_host` waiting for its first remote lock to allocate
`h_rpcclnt`. The guard's commit message describes a defensive scenario that
is contradicted by this successful-mount path in all three selected trees.
The server-host shutdown path clearing `h_rpcclnt` at host.c:623–630 walks
`nlm_server_hosts`; it is not evidence that a live client mount's NLM pointer
becomes cold.

Cancellation and unmount are different: this callback calls `rpc_cancel_tasks`,
which tests the task list then walks it under `clnt->cl_lock`, invoking
`rpc_task_try_cancel` for activated tasks and releasing the lock
(clnt.c:919–934). The new guard runs before that lock. Full destruction
`rpc_shutdown_client` instead loops killing outstanding tasks,
waits on `destroy_wait`, and drops the client reference (clnt.c:956–968).
Remote NFS timeouts alone do not imply sysfs shutdown was requested, let alone
NULL NLM state or a deadlock. They can explain blocked I/O only with a matching
mount/task/progress chain; a host-wide hang needs additional evidence.

There is a separate pre-existing lifetime concern worth preserving without
promoting it to a confirmed defect: `nfs_free_server` calls server destroy
(including `nlmclnt_done`) and shuts down RPC clients, then puts the shared
NFS client (client.c:1103–1111), **before** `nfs_sysfs_remove_server` performs
`kobject_del` (1113–1115; sysfs.c removal helper). The shutdown callback reads
those same raw pointers without taking a new RPC/client reference. Full RPC
release can ultimately queue/free the object (clnt.c:975–1059). A possible
schedule is a sysfs writer paused with the node active, teardown releasing the
last client ref, then writer resuming before node deletion drains callbacks.
Proving reachability requires checking all teardown entrypoint exclusion,
actual final-reference ownership, sysfs active protection and RPC work ordering;
this audit does not assert that complete proof. The NULL guard neither creates
nor fixes stale non-NULL pointers. No incident shutdown/unmount overlap or
matching stack has been supplied.

## Incident attribution and remaining evidence

Per lead/log lane: old .95.6 blocked NFS tasks predate the October 19 upgrade.
On October 20 the last NFS timeout for container 19770 was 18:58:18.238314+02,
last central record 18:58:26+02, reboot records begin 19:12:04+02. There were
21 timeouts during the .113 period, without logged blocked-task/lockup/RCU/host
OOM evidence. These are chronology constraints, not proof of the sysfs callback
or the syslog allocation path.

To discriminate the remaining candidates, obtain exact fault/blocked stacks
or a dump, namespace-creation/allocation-failure evidence, and sysfs shutdown
writes/unmount activity tied to the incident window. An isolated concurrency
experiment must first establish the NFS lifetime exclusions above and use
old/new/fix controls. No broad upstream audit, reproduction, deployment or
operational diagnostic change was performed in this lane.

Verification was source/ancestry/diff inspection only. Git partial-clone object
retrieval was initially implicit; subsequent reads used no-lazy-fetch and the
lead designated implementer0 as missing-blob materialization owner. Lead owns
artifact registration, state synthesis and coordination commits.
