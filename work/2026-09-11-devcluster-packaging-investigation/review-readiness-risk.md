# Mandatory change review: SSH readiness risk and compatibility

Lane: risk and compatibility
Reviewed repository: `vpsfree-dev-workspace`
Reviewed range: `d2380cbe77f711627ba461ef9359724b6255a5db..3d83a8392cd77fb7e92587ed4ea1a5cc665bd3fb`

## Blocking

None.

## Important

1. **The SSH readiness wait is not actually bounded or reliably noninteractive.**
   Commit `3d83a83` checks its 120-second deadline only after the synchronous
   `ssh_cmd` invocation returns
   (`dev-clusters/vpsadmin/bin/devcluster:717-735`). `ConnectTimeout=3` limits
   TCP connection setup plus the initial SSH handshake and key exchange; it does
   not bound authentication or completion of the remote `true`. The probe adds
   `-n`, but that only prevents SSH from reading its standard input. The packaged
   OpenSSH defaults still have `BatchMode no`, password and keyboard-interactive
   authentication enabled, three password prompts, and no server-alive timeout.
   If the configured key is rejected, SSH can prompt through the controlling
   terminal or an askpass helper. If a reachable SSH endpoint finishes key
   exchange but stalls during authentication or session execution, the call can
   remain blocked indefinitely. In both cases the shell never reaches the
   `SECONDS` check, so a direct or automated `start`/`refresh` can exceed the
   documented two-minute wait while retaining the cluster lifecycle lock.

   Make the probe explicitly noninteractive, restrict it to the generated
   identity, and enforce a hard per-attempt timeout capped by the remaining
   overall deadline. Treat expiration as a readiness failure while preserving
   the single execution of the real seed and node actions. Add focused coverage
   for a probe that does not return and for an authentication failure; the tests
   should prove both the overall bound and that no remote action ran.

## Advisory

None beyond the residual coverage gaps below.

## Compatibility and residual risks

- The change does not alter persistent cluster state, VM disks, configuration
  schemas, socket identities, credentials, guest protocols, or the generic
  dispatcher. An older package can still read and stop the retained cluster, so
  package rollback needs no data conversion or coordinated node update.
- The harmless `true` probes do not mutate guests, and the committed call sites
  keep the services seed check and each node preparation action single-shot.
  A transient failure between a successful probe and the following action still
  causes that action to fail without retry, as intended.
- The regression covers one transient exit 255 from `node1` in local-network
  mode and confirms that the three real remote actions run once. It does not
  cover a transient services probe, bridge routing, terminal timeout, a hanging
  SSH process, authentication prompting, or immediate propagation of a non-255
  probe result.
- The new head has not received live start acceptance. Repeated bridge startup
  remains necessary after the Important finding is fixed or explicitly accepted
  because the observed production-like failure was `No route to host` on the
  bridge path.
