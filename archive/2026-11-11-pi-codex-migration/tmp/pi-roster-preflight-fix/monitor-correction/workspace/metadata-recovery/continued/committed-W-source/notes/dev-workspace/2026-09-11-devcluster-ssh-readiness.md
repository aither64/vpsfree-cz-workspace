# Wait for bridge SSH after runner readiness

The packaged vpsAdmin runner can mark the node booted before its bridge address
and sshd are reachable. The first real start booted all VMs but automatic pool
refresh failed with SSH status 255 and No route to host. Manual refresh passed
once networking was ready.

The provider now probes SSH before services seed checks and each normal node
refresh. Only harmless probes retry transport failures. Mutating remote actions
run once and propagate failure. Probes use BatchMode and IdentitiesOnly, a five
second process timeout capped by the remaining two minute deadline, and a one
second forced-kill grace. Do not rely on ConnectTimeout to bound authentication
or remote command stalls. Tests exercise actual lock wrappers and verify a
stalled probe does not run actions and releases locks.

Related initiative: work/2026-09-11-devcluster-packaging-investigation.
