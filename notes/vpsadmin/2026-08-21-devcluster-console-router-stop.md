# Console router can consume the full stop timeout

Initiative: `work/2026-08-18-vpsadmin-password-reset`

## Symptom

`devcluster update <slug> services` reached activation, but
`vpsadmin-console-router.service` remained in `deactivating (stop-sigterm)`
after Puma logged that it was gracefully stopping. The process had no active
requests, yet it did not exit before the unit's five-minute stop timeout.

## Behavior and workaround

Leave the update attached. The unit has `SendSIGKILL=yes` and a five-minute
`TimeoutStopSec`, so systemd terminates the old stateless router and continues
activation without resetting the cluster or its database. Use
`systemctl list-jobs` and `systemctl status vpsadmin-console-router.service` in
the services VM to distinguish this case from a stalled Nix build.

## Root cause

The deployed Puma 8.0.2 has the shutdown-pipe race tracked as upstream issue
`puma/puma#3677` and fixed by pull request `puma/puma#3940`, merge commit
`515987476202e0bd6faf5f14ba9838fdf088b5d5`. During graceful stop,
`notify_safely` can race its buffered `@notify << message` write against the
server thread closing the same pipe. The closer can remain blocked, while
`Server#stop(true)` waits forever for that thread.

The incident followed that exact control flow. systemd delivered SIGTERM,
Puma entered graceful stop, and systemd killed it exactly five minutes later.
The old process received no dynamic console requests: its only console traffic
was static `HEAD /console.js` checks, so the router's Bunny connection and
upkeep thread were never created. systemd recovered correctly and did not
cause the hang.

Puma's merged fix replaces the buffered pipe operations with `syswrite` and
`sysread` and adds safe rescue handling. Puma 8.0.2 predates the fix, and no
newer Puma 8 release exists as of this investigation.

## Operational decision

Do not carry a local Puma patch. Tolerate the intermittent stop timeout and
systemd's forced termination until an upstream Puma release contains merge
commit `515987476202e0bd6faf5f14ba9838fdf088b5d5`, then update Puma normally.
After that update, run Puma's trap-context and concurrent-stop regression tests
and a NixOS smoke check that stops the console router, requires it to become
inactive within about ten seconds, restarts it, and waits for readiness.

Changing only the stop timeout or forcing non-graceful shutdown limits the
delay but leaves the race. Production API and console-router packages also use
Puma 8.0.2; the issue is intermittent and can delay restarts or force-kill
in-flight requests, but it does not change persistent state or protocols. If
the operational frequency or impact increases before an upstream release, the
exact upstream backport remains the fallback.

## Verification

After the timeout, activation started the API, password-recovery worker,
console router, WebUI, and mailer from vpsAdmin revision `00674913`. The bridge
cluster returned to ready state with no failed units, and the public recovery
form returned HTTP 200.
