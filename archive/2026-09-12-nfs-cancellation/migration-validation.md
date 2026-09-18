# NFSv4 migration validation

The scratch probe proves an actual nfs4_update_server call. Cached 6.12.48
reproduces the kobject reinitialization warning in nfs_sysfs_add_server.
Repaired 6.12.95 at e232e2bd reaches and successfully returns from replacement,
preserves the payload SHA256 and verifies a destination write. It eliminates
the reinitialization warning but exposes the anticipated stale RPC sysfs link.
The first link-refresh follow-up crashed on both kernels because RPC transport
replacement left cl_sysfs NULL. Corrected commits4459e6f4/ec548c1a recreate that
object on replacement and rollback and guard optional allocation. Runtime
acceptance remains pending; see runtime-validation.md.

The initial probe on both kernels failed with EPERM from nfs_probe_server.
The existing rpc_switch_client_transport creates a transport without preserving
resvport, while the test export defaults to secure. Allowing unprivileged ports
with insecure makes replacement and data checks pass. This fixture requirement
is separate from cancellation; no transport port-policy change is included.

Both NFSD servers bind the same backing directory and explicit fsid. The target
uses a different UTS hostname; after NFSD is ready, writing its thread count
updates its server identity. The source export is switched to refer= only after
the client is mounted, then its export cache is flushed. Exportfs must enter
mount, network, UTS **and PID** namespaces with --root --wdns=/: otherwise
/proc/net/rpc is absent in the mounted procfs and the export cache remains stale,
even though exportfs returns success and changes etab.

Use short server names (server2) because exportfs derives veth names from them.
The server PID file appears before RPC services are ready; wait for positive
/proc/fs/nfsd/threads before changing its identity.

Primary sources inspected: Linux fs/nfs/nfs4state.c nfs4_try_migration,
fs/nfs/nfs4client.c nfs4_update_server, fs/nfsd/nfssvc.c nfsd_svc, and
[nfs-utils exports manual](https://github.com/linux-nfs/nfs-utils/blob/master/utils/exportfs/exports.man).

Evidence: scratch/migration-probe-vm-v3.log and the shell log under
/tmp/nfs-migration-probe-v3.eiMeuS. The successful trace hit followed the
scratch/migration-pidns-retry.rb commands. This is trigger validation on an old
kernel, not repaired-kernel runtime acceptance.

Repaired-kernel evidence: scratch/migration95-vm.log and
/tmp/nfs95-migration.iijoWZ/machine-shell.log. The successful sequence is
scratch/migration95-insecure.rb, with kretprobes returning zero from
nfs4_set_client, nfs_probe_server, and nfs4_update_server. The payload and
post-migration write checks passed at 14:52 UTC. Product regression also requires
both sysfs links to resolve after replacement and the state-client target to
change. The mount-client id itself is retained, although its sysfs object is
recreated.

At 17:48 UTC, the rescheduled normal 6.12.109 suite completed all 44 protocol
examples successfully (NFS3/4.0/4.1/4.2, including osctld restart, both dirty-init
namespace modes, processless namespaces, locks and tenant isolation). Its one
migration example failed before triggering migration because BusyBox readlink
has no -e option; the pending test change uses test -e plus readlink -f.
The overall suite is correctly reported FAILED, not a full pass.

Focused probes reproduced a real NULL dereference on BOTH final candidate
kernels: cb16974b 6.12.109 clean migration and 6090ca00 6.12.95 race setup.
The crash is sysfs_delete_link+0x23, called by nfs_sysfs_link_rpc_client from
nfs4_update_server. clnt->cl_sysfs is NULL. The newly added link refresh exposed
that rpc_switch_client_transport destroys the RPC sysfs client and does not
recreate it before returning success. This is a regression in our follow-up,
not a passing migration result. Both first-oops traces are retained in
scratch/migration{109,95}-null-sysfs.txt. Correct the transport replacement
sysfs lifecycle and handle optional sysfs allocation failure before rebuilding.
The two crashed disposable probe guests were closed after capturing evidence;
the development session and feature worktrees remain open.
