# General change review, focused migration repair

Reviewed the focused committed revision ranges from
`implementation-review-packet-v3.md`:

- default Linux 6.12.109
  `c099b00eafe7ced993eb6a7166876bb12bef8c72..4459e6f4f8958910fdfe5cd966450b5cab099449`
- retained Linux 6.12.95
  `e232e2bdcc9a552b60b49ab8994bd49b115e1e58..ec548c1a4ee1a41645fcfe84a9180ccce7a30796`
- `vpsadminos`
  `2bb3c251b8be913363b11809a2c0793213820ba2..c9260bbbe68c4368e2acab1ba32ae7612a763b43`

I inspected the exact one-commit series, repository guidance, relevant NFS,
SUNRPC and sysfs context, all callers of `rpc_switch_client_transport`,
`rpc_sysfs_client_setup`, `nfs_sysfs_link_rpc_client` and
`sysfs_delete_link`, the migration regression, prior review reconciliation and
the two captured NULL-dereference traces. The equivalent kernel deltas are
focused and have a convincing indivisibility rationale: NFS cannot safely
refresh its link until SUNRPC recreates the target object, and modular NFS needs
the GPL export of the namespace-aware deletion helper. The OS commit keeps the
test, corresponding source pins and livepatch documentation together. Commit
messages describe the final behavior and rationale and satisfy the applicable
format rules.

## Findings

No Blocking, Important or Advisory findings.

The corrected ordering is consistent on both success and rollback. The old RPC
sysfs object is destroyed at `net/sunrpc/clnt.c:797`; setup recreates the object
for the selected transport before each registration at lines 813 and 830, and
the registration error path already destroys a successfully allocated
replacement before rollback. `nfs4_update_server` refreshes the mount-client
link after both successful replacement and rollback
(`fs/nfs/nfs4client.c:1360-1364`). The shared link helper first verifies that
the server directory was published and optional RPC allocation succeeded, then
uses the target's namespace to remove the old link before recreating it
(`fs/nfs/sysfs.c:395-406`). The only in-tree transport-switch caller is this NFS
migration path, whose existing namespace identity check prevents selecting a
target from another network namespace.

The migration test establishes a known payload and checksum, proves a zero
return from the real replacement function, rechecks the payload, writes through
the migrated mount, and requires both RPC links to resolve. Requiring the state
client target to change also distinguishes actual state-client replacement
from a merely surviving link. The new initial NFSD wait covers both the export
table and active server threads, and the replacement fixture's active-thread
wait occurs after its run script has completed `exportfs -ra`.

## Residual validation gaps

- The committed OS pin and livepatch documentation still name the superseded
  provider heads `cb16974b` and `6090ca00`, as the packet explicitly records.
  They must be amended to the exact reviewed heads and verified flat archive
  hashes before this series is deployable or any exact-pair integration result
  can be accepted. GitHub HTTP 429 currently blocks that mechanical validation.
- The focused object check compiled `fs/nfs/sysfs.o`,
  `fs/nfs/nfs4client.o` and `net/sunrpc/clnt.o` from both corrected trees
  without warnings or errors. Full corrected kernel/module builds and the
  normal and diagnostic migration VMs have not run, so symbol resolution,
  runtime link replacement and the absence of the prior NULL dereference remain
  unproved at these exact heads.
- The committed regression exercises successful NFSv4.2 replacement. It does
  not fault `rpc_client_register` to execute transport rollback, or force
  optional RPC sysfs allocation to fail. Those source paths are consistent on
  inspection but remain runtime test gaps, as do NFSv4.0's distinct quiescing
  path and concurrent migration/shutdown stress.
