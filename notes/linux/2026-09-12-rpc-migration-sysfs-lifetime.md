# RPC transport replacement removes client sysfs state

In Linux 6.12.95 and 6.12.109, rpc_switch_client_transport destroys
clnt->cl_sysfs before registering the replacement transport. The registration
helper does not recreate it: initial creation does that separately in
rpc_new_client. The same omission exists on the rollback registration path.

When retaining an NFS server kobject across migration, refreshing its mount
client link immediately after replacement therefore dereferences NULL unless
the RPC sysfs object is recreated first. The initiative reproduced the crash
on both kernels: sysfs_delete_link+0x23, address 0x30, called through
nfs_sysfs_link_rpc_client and nfs4_update_server. The added refresh introduced
this crash; the missing RPC sysfs recreation was already present.

The correction moves rpc_sysfs_client_setup into rpc_client_register, which
already owns the matching failure cleanup. All three callers pass their active
transport switch. NFS refreshes its link even on rollback and checks optional
sysfs allocation before dereferencing cl_sysfs. Check the actual
allocation/registration split instead of assuming registration rebuilds sysfs.
The correction is committed; runtime validation is pending.

Upstream source inspected on 2026-09-12:
https://github.com/torvalds/linux/blob/master/net/sunrpc/clnt.c

Related initiative: work/2026-09-12-nfs-cancellation.
