# Mandatory change review rerun: SSH readiness risk and compatibility

Lane: risk and compatibility
Reviewed repository: `vpsfree-dev-workspace`
Previously reviewed head: `3d83a8392cd77fb7e92587ed4ea1a5cc665bd3fb`
Final amended head: `9e8783d68fdf40de04683e419d4f373bc27e3730`

This rerun reviewed the narrow remediation for the prior Important finding that
an SSH authentication or session stall could outlive the declared readiness
deadline while holding the cluster lifecycle lock.

## Blocking

None.

## Important

None.

## Advisory

None.

## Assessment

- `wait_for_machine_ssh` now invokes the harmless `true` probe with
  `BatchMode=yes` and `IdentitiesOnly=yes`, preventing password, keyboard-
  interactive, askpass, and unrelated-agent identity behavior from making the
  readiness path interactive (`dev-clusters/vpsadmin/bin/devcluster:717-745`).
- Each probe runs under coreutils `timeout`. Its normal limit is five seconds
  and is reduced to the remaining portion of the 120-second deadline. A stuck
  SSH process receives `TERM` at that limit and `KILL` after a one-second grace,
  so authentication and remote-session stalls can no longer retain the lock
  indefinitely.
- Only SSH status 255 enters the retry loop. Timeout statuses and other local or
  probe failures return immediately before the services seed check or any node
  preparation. The seed check and each node preparation action remain outside
  the loop and execute once only after a successful probe.
- The hanging-stub regression exercises the real `timeout` program, observes
  status 124 within the per-probe limit, confirms that no remote action ran,
  and confirms lifecycle-lock release. The existing transient-255 regression
  still proves recovery followed by one execution of each real action.
- Coreutils was already present in the packaged cluster runtime path and the
  Nix test environment. The remediation adds no dependency, configuration,
  privilege, secret, state, schema, socket, disk, guest-protocol, or dispatcher
  contract.
- Package rollback remains compatible with retained state and VM disks. No data
  conversion, deployment ordering constraint, or coordinated node update is
  introduced.

## Residual risks and test gaps

- A process that ignores `TERM` can use the documented one-second forced-kill
  grace after the calculated deadline. This is a small, explicit cleanup bound
  rather than an unbounded stall; ordinary OpenSSH termination returns at the
  main timeout.
- The focused suite does not wait through the complete 120-second terminal
  deadline or exercise a process that requires the forced `KILL`. It also does
  not cover a transient services-VM failure or the original bridge-network
  `No route to host` path.
- The final amended head has not received live start acceptance. Repeated bridge
  startup remains the material integration check for the observed failure.
- The previously accepted non-transactional forced-certificate replacement
  behavior is unchanged and is outside this readiness remediation. Live
  acceptance must continue to avoid forced certificate replacement.
