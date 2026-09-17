# Risk and compatibility review, focused migration repair

Reviewed the focused committed revision ranges from
`implementation-review-packet-v3.md`, including the review-driven ownership
amendment that supersedes the packet's initial kernel heads:

- default Linux 6.12.109
  `c099b00eafe7ced993eb6a7166876bb12bef8c72..7c66ab3c284a5fb5b615f874a99cb16501d6de23`
- retained Linux 6.12.95
  `e232e2bdcc9a552b60b49ab8994bd49b115e1e58..a2bdcc5b5067dcb7b8f36ef955cd6ee29c9c215a`
- `vpsadminos`
  `2bb3c251b8be913363b11809a2c0793213820ba2..c9260bbbe68c4368e2acab1ba32ae7612a763b43`

I inspected both equivalent kernel deltas, the full SUNRPC registration and
transport replacement paths, all in-tree callers of the changed helpers, the
sysfs namespace and removal implementation, NFS server/client replacement and
rollback context, the migration regression, and the earlier review
reconciliation and crash evidence.

## Findings

No Blocking, Important or Advisory findings.

The amended lifecycle is balanced on every registration path. The static
`rpc_client_register()` helper now owns optional RPC sysfs setup and its
existing error cleanup (`net/sunrpc/clnt.c:329-374`). Its three callers pass
the transport switch which is current for the client: the initial iterator's
switch at line 471, the newly installed switch at line 814, and the restored
old switch after rollback at line 830. The iterator holds or receives the
corresponding switch reference in each case. A registration error destroys any
successfully allocated sysfs client before rollback, and a second allocation
failure during rollback remains non-fatal to registration.

NFS refreshes the mount-client link before it tests the transport-switch return
value, so both success and restored-old-transport outcomes are covered
(`fs/nfs/nfs4client.c:1360-1364`). The link helper rejects an unpublished NFS
server directory and an absent optional RPC sysfs allocation before
dereferencing either kobject, then uses `sysfs_delete_link()` with the live
target to select the tagged link namespace (`fs/nfs/sysfs.c:389-409`). The only
in-tree `rpc_switch_client_transport()` caller is this NFS migration path, whose
existing `net == clp->cl_net` check preserves the published server's original
network-namespace identity. Exporting the existing deletion helper GPL-only is
sufficient for modular NFS and does not introduce a new userspace ABI.

The committed NFSv4.2 migration regression exercises a real successful
replacement, verifies a known payload checksum before and after replacement,
writes through the destination transport, requires both RPC links to resolve,
and distinguishes state-client replacement by requiring its target to change
(`tests/suite/osctl/nfs-cancellation/migration.rb:1-82`). The initial server
readiness check now requires both a populated export table and active NFSD
threads. The target's active-thread check occurs after its runit service has
run `exportfs -ra`, and the link checks use BusyBox-compatible `test -e` plus
`readlink -f`.

## Residual risks and required validation

- The OS commit still pins the superseded provider revisions and archive
  hashes. It must be mechanically amended to the two reviewed heads above, and
  the exact archives must be hash-verified, before the provider/consumer pair
  is deployable or its integration results can be accepted. GitHub HTTP 429 is
  the recorded temporary blocker for that download validation.
- Full corrected kernel and module builds have not completed at these amended
  heads. Final linking/modpost must verify the new GPL export for modular NFS,
  and normal plus diagnostic migration VMs must prove both link replacements
  and the absence of the prior NULL dereference at runtime.
- The regression covers successful NFSv4.2 replacement. Runtime tests do not
  force `rpc_client_register()` failure to execute rollback, force optional RPC
  sysfs allocation failure, or exercise NFSv4.0's distinct quiescing path.
  Those paths are consistent on source inspection but remain failure and
  mixed-path coverage gaps.
- Concurrent migration with sysfs shutdown/cancellation remains a pending
  diagnostic stress case. KASAN, lockdep and delayed kobject release are still
  needed to validate the source-level lifetime reasoning under contention.
