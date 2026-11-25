# Upstream NFS, SUNRPC and lockd audit

Owner: implementer3. Phase: authorized upstream investigation after the lead
accepted the custom-patch gate. Identity and saved same-session roster were
rechecked; no source/ref/production changes, builds or tests were performed.
Only this investigation artifact was written. The documentation and handoff
workflows read during the custom phase remain applicable. Lead owns portal
registration, state synthesis and tracking commits.

## Outcome

**No supported source chain from these inspected upstream changes to the
reported host-wide hang was found.** A concrete FREE_STATEID allocation-error
reference leak exists in the incident tree. Its proven effect is mount/server
resource retention, without a demonstrated host-wide wait dependency or an
incident trigger. TLS cancellation and client pinning were traced through
their completion/close actors; the proposed new deadlock is not supported.

| Examined mechanism | Source conclusion | Incident applicability |
| --- | --- | --- |
| NFSv4.1 FREE_STATEID allocation unwind | Source-proven leaked active-server and NFS-client references; mount resources can remain pinned | NFSv4.1 use and allocation failure unknown; no host-wide failure chain |
| TLS cancellation-loses-race wait | Completion ownership and close/destruction serialization account for the new wait; no stuck-wait cycle demonstrated | TLS mount use unknown |
| TLS upper client pin dropped before connect unlock | Transport's direct client-owned reference survives until separate free work; no inline self-destruction cycle | TLS use unknown; no attribution |
| Lock-list rwsem changes and pNFS callback relocation | Inspected paths release spinlocks before RPC/callback work; no newly proven lock cycle | NFSv4/pNFS mode and relevant stacks unknown |
| lockd traversal/file-open error changes | Next-node references protect unlock windows; error unwinds release the existing mutex | No lockd-server teardown signature or causal task stack |
| cache cleaner and rpc_pipefs lifetime/locking changes | Synchronous cleaner drain occurs after locks are dropped; pipefs creation drops parent inode lock before population | No demonstrated new cycle or incident evidence |
| Custom NFS sysfs cancellation interaction | Guard and cancellation path add no global wait; pointer-lifetime concern remains the pre-existing, unproven concern recorded separately | No shutdown-write/unmount activity established |

## Scope and source identity

Compared exact stable baselines:

- old `296aabce459470a4c1b68ffd0c0c0920e563aaad` (6.12.95);
- new `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` (6.12.113);
- validated relevant final behavior in incident tree
  `1dfea587406b7dd79973831d1677fb2418e5e9aa` (OS `2abbe3cc`).

Covered aggregate old/new source deltas and immediate callers in
`fs/lockd/{clntproc,svcsubs}.c`, NFS lock/delegation/client/server/FREE_STATEID
paths, `fs/nfs/{pnfs,pnfs_nfs,write,read,inode,internal}.c`/headers as relevant,
`net/sunrpc/{clnt,xprt,xprtsock,xprtmultipath,cache,rpc_pipe,svc,svcsock}.c`,
and handshake request/completion/cancellation in `net/handshake`.
`fs/locks.c`, `include/linux/filelock.h` and `net/sunrpc/sched.c` have no
aggregate delta in this stable range; existing behavior was consulted where
needed. All source line references below are to incident tree unless otherwise
stated.

This was a targeted locking/progress/lifetime audit, not complete verification
of every NFS, GSS, XDR, RDMA or layout-driver stable patch. RDMA-specific
request recycling, GSS token parsing and all layout implementations were not
exhaustively audited. Their use has no positive runtime discriminator in the
provided evidence. This limit does not exclude those modes or certify them.
Locally available later branch history supplied no later matching stable
fix/revert for the finding below; no assertion is made about unavailable
upstream history. No external search or ref fetch was performed.

## Proven FREE_STATEID allocation failure leak

`ed1161ab6239761958b38d5667225634fc2be894` (upstream
`cf616096a0f3a2b60f7d68b6b39674a6867ded9c`) pins the server during asynchronous
FREE_STATEID to fix an earlier use-after-free. Its incident-tree success path
balances pins in `nfs41_free_stateid_release` (nfs4proc.c:10585–10592).
The allocation-error path does not:

1. `nfs41_free_stateid` increments `clp->cl_count` with
   `refcount_inc_not_zero` (10630).
2. It calls `nfs_sb_active(server->super)` (10632). Failure here correctly
   drops the client ref and returns. Success acquires server activity.
3. `data = kmalloc(sizeof(*data), GFP_KERNEL)` can fail (10641).
   Lines 10642–10643 immediately return `-ENOMEM`, dropping neither pin.
4. No RPC task or calldata exists on this path, so no later `rpc_release`
   callback can drop these references.

`nfs_sb_active` (super.c:193–201) increments `server->active`, retaining one
aggregate `sb->s_active` reference while this activity count is nonzero.
`nfs_sb_deactive` (205–211) drops that superblock reference only when activity
reaches zero. The leaked activity keeps the count above zero, so the final
normal users cannot complete that balancing drop. Proven consequence:
server/superblock and associated resources remain pinned. The direct
`nfs_client` reference is leaked as well. There is no spinlock or mutex held
by this error return and no remote RPC to wait for on this path. This proof
does not establish a deadlock, synchronous unmount hang, all-node I/O loss or
host-wide CPU/scheduler failure.

The old pristine stable baseline already acquired the NFS-client ref before
allocation, so that part of the raw error-path leak predates the server-pin
change. **Do not equate pristine baseline behavior with the old effective
.95.6 runtime.** Inventory owner implementer0 supplied and this lane read the
retained effective alternatives:

- `fc37ccc43227ab8eef70b50660a081f2615d0ead` adds a livepatch-control adapter
  `vpsadminos_nfs_freeid`; its allocation failure goes to `out_deactive`, which
  drops both references (nfs4proc.c:10776 and 10864–10867). Dispatch uses it
  when the v6 control exists (10905–10908); the raw fallback remains distinct. The actual
  loaded control state at the old incident is not established.
- Historical NFS boot tree
  `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd` also drops both references on
  allocation failure in its FREE_STATEID implementation (10640–10644).
- The inventory owner locates the adapter/cleanup in historical OS `d9bd`'s
  `bp-6.12.95-cumulative.patch`. Publication/package/livepatch applicability
  remains the inventory/package lanes' authority.

Thus the .113 static leak is proven, and at least some supported old effective
paths had a correct unwind. Whether this was a runtime regression on the
actual old configuration remains qualified by livepatch/control identity.
The source comparison is local fix proof for this one allocation-error path,
not a later official upstream fix/revert or a reproduction.

This finding is specifically the **calldata** allocation failure. Failure of
the later RPC task allocation is different: `rpc_new_task` explicitly invokes
`rpc_release_calldata` if allocating the RPC task fails (sched.c:1147–1152),
which calls this operation's release handler and balances the pins. Do not
extend the leak claim to every `rpc_run_task` error return.

Required runtime trigger: NFSv4.1-capable FREE_STATEID path and failure of this
small allocation after both pins succeed. Neither NFSv4.1 mode nor this
allocation failure is established at the incident. If separately authorized,
a focused isolated test could inject failure at this allocation, observe
`server->active`/superblock lifetime, and compare incident code, old effective
adapter and a balanced-unwind correction. That would test the leak; it would
not establish host-hang causality without an additional progress chain.

## TLS cancellation and close actors

Inspected the final combined result of client TLS reference and wait fixes,
including `7a65b41b657b`, `8f39b1081c6a`, `e0f4691d42a5` and
`15431820f448`. These identifiers locate changes; conclusions below follow
final code, not the subjects.

Client operation and completion ownership:

- `xs_connect` takes an upper-client ref only for non-NONE TLS policy,
  serializes the worker with `xprt_lock_connect`, and queues the work
  (xprtsock.c:2816–2844). Plain TCP/UDP does not take this new pin.
- `xs_tcp_tls_setup_socket` obtains lower `XPRT_LOCKED` before handshake
  (2747). A killable lock-acquisition failure shuts down the lower client
  without pretending the bit was acquired (2747–2750).
- `xs_tls_handshake_sync` gives the callback a lower-xprt reference, initializes
  `handshake_done`, starts the request and waits with timeout (2614–2650).
  Submission failure drops the extra reference locally. Cancellation success
  owns that drop; cancellation failure waits for completion (2651–2677).
- `handshake_req_cancel` returns true only when it sets the completed flag;
  false means completed or missing (request.c:344–378). On successful
  submission the request stays tied to the socket. `handshake_complete`
  atomically claims completion and calls `hp_done` (313–328), which invokes
  the TLS consumer callback. `xs_tls_handshake_done` stores status and calls
  `complete` **before** `xprt_put` (xprtsock.c:2595–2610). That callback takes
  no lower `XPRT_LOCKED` or `recv_mutex` and does not wait for this worker.

The extra cancellation actor matters: `xs_reset_transport` also cancels
handshakes (1291). Its ordinary `xs_close` caller requires `XPRT_LOCKED`
(1324–1335), which the TLS worker holds on the lower transport until its
handshake/transfer/error handling completes. Full `xprt_destroy` acquires that
same bit (xprt.c:2149), and `xs_destroy` also drains connect work before close
(xprtsock.c:1363–1364). Therefore the proposed schedule in which close wins
cancellation on this live lower transport and leaves the worker waiting for
a callback that will never run is excluded by this inspected serialization.
The successful-submission, live-socket path supplies no demonstrated
request-missing branch without completion/cancellation ownership.

Another checked hypothesis was an upper-worker self-deadlock when its exit
drops the last upper-client ref before `xprt_unlock_connect`
(xprtsock.c:2784–2786). `rpc_free_client` destroys the switch iterator
(clnt.c:1005), but the client's direct `cl_xprt` reference survives until
separate `rpc_free_client_work` drops it (975–989). The switch's entry has
its own transport ref. Thus iterator release does not synchronously destroy
the worker's last transport reference; separate destruction may wait for
the bit while the worker can continue to unlock it. No self-cycle is proved.

Server-side TLS was also checked: `svc_tcp_handshake` pins the svc transport
before request submission; success callback signals `sk_handshake_done`
before its put; submission/cancel-success paths drop the pin directly
(svcsock.c:464–521). The `svc_sock_free` cancellation at 1674 cannot run at
last-reference destruction while that handshake pin remains outstanding.
Detach can close the socket but does not cancel the request at that site.
No new completion-owner cycle was identified in these actors.

Runtime gate: `xprtsec=tls` or `xprtsec=mtls` is needed for the client TLS path;
`sec=krb5*` alone does not imply it. Implementer1's bounded startup/pre-gap
log search found no literal TLS/RDMA/pNFS discriminator, but host forwarding
does not establish absence. Actual TLS/RDMA/pNFS use remains **unknown**.
No TLS defect or host-wide failure chain is supported here.

## Other concrete lock/progress checks

- **NFSv4 file locks:** `1cda95bf2e9c` adds write ownership of `nfsi->rwsem`
  while `nfs_delegation_claim_locks` traverses locks. It releases
  `flctx->flc_lock` before the synchronous recall RPC and drops the rwsem
  on both success and error. The paired change removes VFS-lock updates
  from `nfs4_lock_done`/`nfs4_locku_done`. `_nfs4_proc_setlk` performs its
  post-RPC VFS update under a read rwsem and clears `FL_SLEEP` first
  (nfs4proc.c:7620–7627). The hypothesized recall-waits-RPC / RPC-waits-same-
  rwsem cycle is not present in those callbacks. No source-proven new cycle
  to global host progress was found.
- **pNFS return:** `_pnfs_return_layout` retains `lo` and drops `ino->i_lock`
  before invoking the layout driver's `return_range` (pnfs.c:1465, 1488–1493).
  The early no-layout/no-return paths also unlock. The changed
  `clear_and_wake_up_bit` calls preserve exactly the prior clear-unlock,
  post-atomic barrier and wake sequence (wait_bit.h:330–335), so no missing
  wakeup follows merely from that replacement. Data-server cache operations
  now use the per-net lock consistently for lookup/add/final removal;
  destruction remains outside the spinlock. Actual layout use is unknown.
- **Lockd files:** `nlm_traverse_files` pins current and next `f_count` under
  `nlm_file_mutex` before dropping it for inspection (svcsubs.c:305–336).
  Its release checks respect outstanding refs; lookup's new fopen-error
  branches reach the existing mutex unlock. This repairs the prior
  unlock-window dangling-next-pointer schedule. The scan's global mutex and
  VFS close behavior were already present; no new reverse lock order was
  established by these changes. Client `h_rpcclnt` eager binding is unchanged.
- **Cache destruction:** `sunrpc_destroy_cache_detail` unlinks under
  `cache_list_lock` then `cd->hash_lock`, releases both, then synchronously
  drains the cleaner (cache.c:403–415). The cleaner uses the same lock order
  and releases locks before removing/putting an expired entry. A proposed
  spinlock-held wait cycle is excluded at the new drain call. No specific
  caller/cleaner callback reverse dependency to a host lock was demonstrated.
- **Pipefs/VFS:** `rpc_mkdir_populate` drops the parent inode lock before
  child population and does recursive error removal afterward
  (rpc_pipe.c:744–758). `rpc_populate` unlocks each directory operation on
  every shown failure branch (701–733). Client pipefs association checks
  pair creation/removal with the matching superblock. The inspected change
  does not retain a new parent/child inode lock across callback population.
- **Unstable writes/read errors:** accounting now charges and clears a
  request's `DIV_ROUND_UP(wb_bytes, PAGE_SIZE)` using matching expressions
  (internal.h and write.c); no new lock or remote wait is introduced by that
  arithmetic. Read-error updates hold/release the page-group lock locally.
  This inspection found no complete changed chain to host-wide failure.

## Custom sysfs interaction and incident evidence

The custom `shutdown_store` sets terminal shutdown state and cancels client
tasks; `rpc_cancel_tasks` holds `clnt->cl_lock` only while selecting/cancelling
activated tasks. It does not itself wait for remote replies or perform the
full client destruction loop. `shutdown_nfs_client` drops its RCU read lock
before marking/cancelling the shared client. The new upstream callbacks
inspected above do not add a demonstrated reverse dependency on that lock.
The earlier note's raw-pointer shutdown/unmount ordering concern remains
unproven and pre-existing, rather than a new upstream finding.

The log lane establishes 21 .113-period NFS timeouts, with the last at
18:58:18.238314+02 for container 19770/server 172.16.129.141, before the last
central record at 18:58:26+02 and reboot at 19:12:04+02. A startup warning
says new mount options conflict with an existing superblock but supplies no
options. None shows TLS handshaking, allocation failure, FREE_STATEID,
shutdown/unmount overlap, a specific blocked lock, or host-wide kernel
non-progress. Old .95.6 blocked NFS tasks are a separate pre-upgrade control.

Next useful evidence is a fault/blocked-task stack or dump, actual affected
NFS version/transport/mount options, and a source-specific trigger around the
gap. No runtime experiment, host change or generic kernel build is proposed
to turn the negative source result into apparent proof. A separately
authorized allocation-failure test can establish the bounded leak only.
