# Drain autostarts before locking containers during osctld shutdown

## Symptom

During `work/2026-08-22-osctld-boot-failures`, the
`vps/autostart-monitoring` scenario passed its assertions but the test runner's
final `poweroff -f` hung until the 900-second command timeout. The same node had
powered off normally before the failed boot autostart was manually retried.

## Cause

`Commands::Self::Shutdown` disabled pools and acquired every configured
container's manipulation lock before stopping the pools' autostart plans.
Stopping a plan joins its continuous-executor workers. A retry worker could
already be waiting to start a container and therefore waiting for one of the
locks held by shutdown. Shutdown then waited for the worker while the worker
waited for shutdown's lock.

## Fix

After disabling pools, call `begin_stop` on every pool before acquiring any
container manipulation lock. This clears queued autostarts and joins active
workers while the locks they may need are still available. Acquire the
container locks only after all autostart executors have drained, then retain the
existing container stop and pool export sequence.

Keep a focused ordering spec in `heavy_system_spec.rb`, and keep the bounded
final poweroff inside `vps/autostart-monitoring`; otherwise runner teardown can
hide this regression behind its much longer default timeout.

## Verification

The focused shutdown spec passed two examples with zero failures, targeted
RuboCop passed, and the clean aggregate RSpec harness passed all 13 suites,
including 1,530 osctld examples. The final ordinary-shell exact-pin
`vps/autostart-monitoring` VM passed in 1,134.03 seconds. Its final
`poweroff -f` returned in 7.47 seconds after draining autostarts, stopping both
containers, and exporting the pool; reboot recovery then reported and cleared
the deliberately failed autostart as expected. Preserve a separate guest shell
only for diagnostics, never as the acceptance path for this regression.

The exact-pin VM then exposed a second daemon bug. A retrying autostart remains
in the plan's pending-intent table until its executor worker exits. Its first
lifecycle generation can meanwhile complete and be pruned when a manual start
creates a replacement. `AutoStart::Plan#pause` tried to cancel that missing
generation and `Container::Lifecycle#cancel_unlaunched` raised, aborting
shutdown before it acquired container locks.

Cancellation of an unlaunched generation must be idempotent when the exact run
has already completed, been superseded, or been pruned. Return false for the
missing run just as for an existing non-active run, then let executor drain
join the retry worker. Keep a lifecycle regression which prunes an old run and
cancels its stale ID.

Do not diagnose a post-reboot test hang as a stale default guest shell merely
because a separately named or traced shell succeeds. The test runner recreates
the command sockets on boot, and tracing changes timing. Capture guest syslog
before issuing diagnostic osctl commands. In this incident it showed the exact
`self_shutdown` exception immediately.

Also distinguish a valid daemon command rejection from socket EOF/reset in
`OsCtl::Client`. Only a real connection loss should enter `osctl shutdown`'s
marker fallback. Treating a `status:false` response as a disconnect hides the
real failure and can make shutdown wait for an hour.

The preserved evidence and exact commands are recorded in the initiative
state.
