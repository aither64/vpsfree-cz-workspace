# Enter the export server's PID namespace when flushing NFS exports

In an osctl-exportfs test server, `nsenter -m -n -u --root` followed by
`exportfs -i ...` and `exportfs -f` returned success and updated etab, but the
kernel export cache retained the old options. `/proc/net/rpc` was absent because
the calling process was outside the PID namespace associated with mounted procfs.

Use `nsenter -t SERVER_PID -m -n -u -p --root --wdns=/` for these operations.
Adding `-p` made the referral update take effect and an NFSv4 migration kprobe
hit `nfs4_update_server`. Verify actual kernel behavior; an updated etab and a
zero exit status alone do not prove that an export update reached NFSD.

Related initiative: `work/2026-09-12-nfs-cancellation/migration-validation.md`.
