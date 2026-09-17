# NFS migration test exports and source ports

An NFSv4 migration fixture with two NFSD namespaces and shared backing storage
reached nfs4_update_server but failed with EPERM from nfs_probe_server. The
6.12 rpc_switch_client_transport path creates its replacement transport without
copying resvport from the old transport. The destination export's default
secure option rejects its unprivileged source port.

Using insecure for these isolated test exports made replacement return zero,
preserved the payload checksum and allowed a destination write. This avoids
confusing the existing port-policy behavior with sysfs lifetime or cancellation
failures. The initiative does not change transport port policy.

Evidence: `work/2026-09-12-nfs-cancellation/migration-validation.md` and
`scratch/migration95-insecure.rb` in that initiative. Verified on repaired
6.12.95 at e232e2bdcc9a552b60b49ab8994bd49b115e1e58.
