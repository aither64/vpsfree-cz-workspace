# Architecture and repetition review, migration repair

Reviewed the focused committed delta at:

- default Linux 6.12.109
  `c099b00eafe7ced993eb6a7166876bb12bef8c72..4459e6f4f8958910fdfe5cd966450b5cab099449`
- retained Linux 6.12.95
  `e232e2bdcc9a552b60b49ab8994bd49b115e1e58..ec548c1a4ee1a41645fcfe84a9180ccce7a30796`
- vpsAdminOS
  `2bb3c251b8be913363b11809a2c0793213820ba2..c9260bbbe68c4368e2acab1ba32ae7612a763b43`

The provider/consumer placement is otherwise sound. SUNRPC owns allocation and
destruction of `rpc_clnt::cl_sysfs`; NFS owns its per-superblock links; sysfs
core provides the namespace-aware deletion primitive. Source search found
`nfs_sysfs_link_rpc_client()` as the only new `sysfs_delete_link()` consumer,
and its `state_in_sysfs`/`cl_sysfs` guards satisfy the source and target
preconditions before the core helper reads either kernfs node. The NFS
same-network check keeps the target namespace tag equal to the retained server
directory's tag. The two release branches carry byte-identical focused diffs,
which is necessary duplication between independent kernel release histories.
The migration scenario is shared through one Ruby source file across the
derived normal and diagnostic test instances.

## Blocking

None.

## Important

### 1. SUNRPC registration still splits one lifecycle invariant across three repeated call sites

Commit `4459e6f4f8958910fdfe5cd966450b5cab099449` (identically
`ec548c1a4ee1a41645fcfe84a9180ccce7a30796`) adds
`rpc_sysfs_client_setup()` immediately before `rpc_client_register()` in both
the replacement and revert arms (`net/sunrpc/clnt.c:813-815` and
`net/sunrpc/clnt.c:826-831`). The original-client path already repeats the same
pair at `net/sunrpc/clnt.c:469-472`. In contrast, `rpc_client_register()` owns
the matching sysfs destruction on every registration error
(`net/sunrpc/clnt.c:329-372`). Setup and failure cleanup therefore have
different owners, and the required setup-before-register rule remains an
implicit convention at every caller.

This is the exact class of omission that produced the migration crash: the
transport-switch path destroyed `cl_sysfs`, re-registered the client without
recreating it, and returned to an NFS consumer with a missing object. The new
NFS guard prevents another NULL dereference, but a future registration or
rollback edit that misses the same convention will now silently leave the NFS
RPC link absent or dangling. Because sysfs allocation is intentionally
optional and setup returns no status, that omission is indistinguishable from
an accepted allocation failure and will not fail the transport operation.

Make one SUNRPC helper own the setup/register pair, accepting the active
`rpc_xprt_switch` and the existing authentication arguments, and use it for
initial registration, replacement, and rollback. Keep allocation failure
non-fatal. This localizes the invariant without moving NFS link ownership into
SUNRPC. If the explicit pairing is deliberately retained, record that decision
and add provider-focused coverage for both replacement arms so a missing setup
cannot again compile and pass ordinary RPC tests.

## Advisory

None.

## Residual validation gaps

- The committed migration regression proves only the successful
  `nfs4_update_server()` path (`migration.rb:48-81` requires kprobe result zero).
  The newly changed `rpc_client_register()` failure/revert branch and its
  restored sysfs target are not exercised. This matters independently of the
  successful consumer scenario because the revert setup is one of the two new
  provider calls.
- The exact corrected provider heads are not yet pinned by the reviewed OS
  commit. Its `cb16974b`/`6090ca00` revisions, archive hashes, and documentation
  SHA still await the packet's mechanical amendment after GitHub download rate
  limiting clears. No corrected-head VM result can be inferred from the
  candidate run.
- `scratch/compile-migration-objects.log` shows warning-free compilation of
  NFS sysfs, NFSv4 client, and SUNRPC client objects for both configured kernel
  versions. Full kernel/module linking (including the new GPL export), corrected
  normal and diagnostic boots, migration runtime, optional sysfs-allocation
  failure, and matching corrected-base livepatch identity remain pending.
