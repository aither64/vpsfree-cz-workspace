# osctld restart investigation on node23.prg and node24.prg

## Executive conclusion

The current shutdown does not provide the handoff that was expected. It waits
for ordinary management command threads, but it does not quiesce the internal
boot-time autostart executors before closing `UserControl` and `Eventd`.
Active starts then lose the callbacks needed to finish. At the same time,
`Container::Start` gives up waiting after 15 seconds, reports a normal start
failure to autostart, and autostart retries because its stop flag has not yet
been set. The retry can manipulate the same container while the first detached
LXC start is still alive.

This sequence explains both incidents:

- node23 exited cleanly from the daemon's perspective, but duplicate start and
  cleanup paths removed the host veths of three still-running containers;
- node24 appeared to hang because eight failed starts each waited about 20
  seconds for a nonexistent tty socket while holding one global console mutex,
  serializing approximately 160 seconds of work. The operator's `SIGKILL`
  interrupted that drain.

Autostart recovery is also incomplete. A container is written to
`started-cts.txt` in the pre-start callback, before LXC is running. If that run
then aborts, the replacement daemon considers the container already fulfilled
and does not resume it.

## Incident scope and deployed code

- Both nodes booted the `26.05.git.1895bbc` system with Linux `6.12.95`:
  - node24 booted at `2026-08-22 18:16:06.610 +02:00`;
  - node23 booted at `2026-08-22 18:17:23.635 +02:00`.
- Commit `1895bbc` is `livepatch: update 6.12.95 cumulative patch v5`.
- Relevant osctld shutdown, autostart, start, console, and recovery files have
  no changes between deployed commit `1895bbc` and the investigated
  `origin/staging` commit `97a8c8fc6`. Current source therefore reproduces the
  deployed behavior relevant to this incident.
- Earlier at approximately 18:03, each old daemon stopped cleanly and a new
  daemon started. The subsequent node resets ended those daemons abruptly.
  The failures discussed below happened during the post-reboot redeployment.

## What shutdown currently does

`OsCtld::Daemon#stop` performs these relevant phases:

1. sets the global daemon `stopping` flag;
2. runs pre-stop hooks;
3. stops the command server and drains the `:management` ThreadReaper group;
4. stops `UserControl`;
5. stops the general ThreadReaper and `Eventd`;
6. only then calls `Pool#stop`, whose `begin_stop` stops the autostart plan;
7. stops the monitor and exits.

The internal autostart workers belong to `ContinuousExecutor`, not to the
`:management` ThreadReaper group. `AutoStart::Plan#stop` does clear queued
work and join current executor workers, but it is reached too late: lifecycle
callbacks are already unavailable and active start waiters have already seen
the global stopping flag.

`Container::Start#wait_for_ct` allows at most 15 seconds after daemon shutdown
begins and then returns `[:error, 'osctld is shutting down']`. That stops only
the Ruby waiter. The detached pty wrapper and `lxc-start -F` process group are
not cancelled or proven stopped. Because the autostart plan's separate stop
flag is still false, `do_try_start_ct` interprets the result as an ordinary
failure, sleeps, and starts another attempt.

The deployed source locations are:

- `osctld/lib/osctld/daemon.rb`: daemon stop ordering;
- `osctld/lib/osctld/pool.rb`: late `begin_stop` and autostart stop;
- `osctld/lib/osctld/auto_start/plan.rb`: executor drain and failure retry;
- `osctld/lib/osctld/commands/container/start.rb`: detached wrapper and the
  15-second shutdown wait;
- `osctld/lib/osctld/user_control/commands/ct_pre_start.rb`: premature
  autostart fulfilment;
- `osctld/lib/osctld/console.rb` and `console/console.rb`: global mutex and
  socket retry;
- `osctld/lib/osctld/net_interface/routed.rb`: missing-veth recovery that
  explicitly logs `ignoring` and clears the recorded veth.

## node23.prg timeline

- `18:21:04`: post-reboot osctld PID 51382 starts.
- `18:23:37.109`: redeployment sends it `TERM` and shutdown starts.
- around `18:23:40`: active start waiters give up due to shutdown. Autostart is
  not stopped yet, so they log `Unable to start ... retrying in 5 seconds`.
- around `18:23:45-47`: retries encounter cgroup `EBUSY`, remove tty sockets,
  and attempt a second start while first LXC processes are still alive.
- around `18:24:03`: the late pool stop finally changes the messages to
  `giving up to stop`.
- `18:24:04.224`: osctld logs `Daemon stopped successfully` after console
  cleanup has removed veths from live containers.
- `18:24:05`: replacement osctld PID 323407 starts.

Twenty containers logged `Unable to start` during that shutdown:

| Pool | CTIDs |
| --- | --- |
| dozer | 28260, 28262, 28378, 28383, 28490, 28575, 28610, 28626, 28655, 28665 |
| tank | 14005, 20274, 24800, 26463, 26573, 26751, 26854, 26865, 26908, 27099 |

Their outcomes split into three groups:

- Five were resumed automatically: dozer `28626`, `28655`, `28665`; tank
  `26908`, `27099`.
- Four first LXC starts survived the daemon restart: tank `14005`, `20274`,
  `24800`, `26573`. Container `26573` retained a discoverable veth and tty;
  the other three did not.
- Eleven had reached pre-start fulfilment, later ended stopped, and were
  excluded from replacement autostart. They were started manually around
  19:32-19:44: dozer `28260`, `28262`, `28378`, `28383`, `28490`, `28575`,
  `28610`; tank `26463`, `26751`, `26854`, `26865`.

The broken live containers show the destructive overlap directly:

| CTID | Original host veth observed | Missing-veth recovery log |
| --- | --- | --- |
| 14005 | `vethPGITTB` at 18:23:07.918 | 18:24:19.960 |
| 20274 | `vethqT6aTz` at 18:23:07.024 | 18:24:19.967 |
| 24800 | `vethKVNT1f` at 18:23:03.989 | 18:24:19.973 |

The old daemon logged `Unable to properly handle container stop`, performed its
fallback network cleanup, and exited. The new daemon found each LXC container
running but logged that its veth no longer existed and ignored it. Its tty
socket recovery failed as well. The containers were stopped and started again
manually around 19:25-19:28, which created working veths.

## node24.prg timeline

- `18:18:04`: post-reboot osctld PID 15184 starts listening.
- `18:19:01.562`: redeployment begins shutdown.
- `18:19:01-04`: LXC pre-mount, pre-start, setup, and post-stop hooks begin
  failing because `UserControl` has already been stopped.
- `18:19:23.192` through `18:21:44.510`: eight start workers fail to connect
  tty0, one approximately every 20 seconds.
- around `18:21:44`: the old daemon is killed with `SIGKILL`.
- `18:22:06`: replacement osctld PID 75932 starts.

Sixteen affected CTIDs logged `Unable to start`:

`1341`, `1382`, `12629`, `13706`, `13863`, `13953`, `14076`, `14106`,
`14281`, `14325`, `14562`, `14875`, `14965`, `15240`, `15252`, `15541`.

The four called out in the incident report failed in LXC hooks immediately
after shutdown removed their callback endpoint:

- `1341`: mount-hook and spawn failure at 18:19:01.744-18:19:02.197;
- `13706`: pre-start and post-stop hook failure at 18:19:03.085-18:19:03.163;
- `1382`: pre-mount/setup/spawn/post-stop failures at
  18:19:03.349-18:19:03.532;
- `13863`: pre-mount/setup/spawn/post-stop failures at
  18:19:03.557-18:19:03.747.

All four later reached `RUNNING` under the replacement daemon: `13706` at
18:22:30, `13863` at 18:25:02, `1382` at 18:25:54, and `1341` at 18:27:44.
All sixteen affected starts ultimately recovered; no missing-veth case was
found on node24.

The slow stop was deterministic rather than an unexplained ThreadReaper
deadlock. Eight starts (`14076`, `14281`, `15541`, `13953`, `15252`, `14965`,
`15240`, `14875`) reached `Console.connect_tty0` after their wrappers had
failed to create a usable socket. Each connection retries 100 times at 0.2
seconds. `Console.connect_tty0` holds one module-wide mutex throughout those
retries, so the eight nominally parallel workers consume about 8 x 20 seconds
serially. Their log timestamps are 18:19:23, 18:19:43, 18:20:03, 18:20:23,
18:20:44, 18:21:04, 18:21:24, and 18:21:44.

## nodectld coordination was not effective

vpsAdmin commit `d0d5b6b91` installs an osctld daemon pre-stop hook that asks
nodectld to pause before osctld exits. It is a useful secondary guard, but it
did not protect either restart:

- on node24, nodectld had not completed pool initialization, so the hook was
  not yet installed when osctld stopped;
- on node23, activation stopped nodectld at 18:23:36.233 and stopped osctld at
  18:23:37.109. The hook ran at 18:23:37.179, but its nodectld connection was
  refused at 18:23:37.915.

The hook is installed only after nodectld sees all pools ready, and activation
currently tears down nodectld before osctld. Service ordering should keep
nodectld alive until osctld has entered and completed its drain, and the
coordination endpoint should be available earlier. Core correctness must not
depend on that external hook, however.

## Recommended shutdown and handoff design

Implement shutdown as explicit phases with one lifecycle admission gate:

1. **Enter draining atomically.** Reject new management lifecycle starts,
   immediately stop and clear every autostart queue, set each plan's stop flag,
   and make pre-start delays and cooldowns interruptible. Pause nodectld while
   it is still available.
2. **Drain active starts with dependencies alive.** Keep `UserControl`, LXC
   hooks, `Eventd`, monitor state, and console handling available until every
   active start reaches a definitive `RUNNING` or `STOPPED` state. A shutdown
   handoff is not an ordinary start failure and must never enter the retry and
   cleanup path in the old daemon.
3. **Retain ownership.** Give every start a run/generation identity and track
   its wrapper PID/process group until the lifecycle reaches a definitive
   result. All callbacks and cleanup must be fenced to that generation. A
   waiter returning to its client must not relinquish ownership of the LXC
   operation.
4. **Escalate only after a bounded deadline.** First send `TERM` to the exact
   tracked wrapper/start process group, then wait for `STOPPED` and post-stop
   cleanup while callbacks still work. Use `KILL` only for the exact residual
   generation and report it. Do not solve this by changing runit's
   `killMode = process` to indiscriminate cgroup killing, because container
   processes are intentionally preserved across daemon restart.
5. **Tear down daemon subsystems last.** Only after the lifecycle drain should
   osctld stop user control, events, thread reapers, pools, and monitors. Report
   successful shutdown only when no lifecycle worker or wrapper is unowned.
6. **Resume from definitive state.** Mark autostart fulfilled only after an
   exact run is observed `RUNNING`. Queued or failed/aborted starts remain
   eligible for the replacement daemon. This preserves the intended behavior
   for successful manual starts while fixing interrupted boot starts.
7. **Reconcile recovered containers.** For every LXC container discovered
   running, verify its required host veths, routes/shaper, tty/control socket,
   run configuration, cgroups, and generation ownership. A running container
   without a required veth should be quarantined and normally stopped/restarted
   under control; silently setting the veth to `nil` is unsafe.

Separately, shorten the critical section in `Console`: lock the registry only
while locating or creating a per-container console object, then connect under
per-container/per-tty synchronization. Socket waits should accept the shutdown
deadline/cancellation signal and log CTID, lifecycle stage, generation,
wrapper PID, and elapsed time.

An unmerged branch, `origin/2026-07-24-ct-start-hang-monolithic` at
`70b09f918`, already introduces durable lifecycle generation IDs, fenced
callbacks, ownership, and recovery. That design is directly relevant and
should be reused or split into the eventual fix. It is not sufficient by
itself: its current restart behavior aborts an active start to stopped and
expects a later manual start, whereas boot autostarts need the drain/resume and
fulfilment semantics described above.

## Activation safeguards

- Make service stop/start ordering dependency-aware: during shutdown or
  activation, osctld must drain before nodectld is stopped; during startup,
  osctld must become ready before nodectld begins normal work.
- Install the coordination hook/endpoint declaratively or early enough that it
  is available before all pools finish their initial autostart.
- Make nodectld tolerate osctld socket unavailability with bounded retry rather
  than repeatedly crashing during replacement startup.
- Review osctld restart triggers so kernel/livepatch-only deployments do not
  restart osctld accidentally. This is defense in depth, not a substitute for
  a safe restart when an osctld upgrade really is deployed.
- Add a drain/status command that reports queued and active CTIDs, lifecycle
  stages, elapsed time, generation, and wrapper PID. Activation can then wait
  on a meaningful condition and operators can distinguish progress from a
  deadlock before considering `SIGKILL`.

## Regression coverage

Add focused RSpec examples for:

- daemon stop order: autostart admission closes before callback services;
- no autostart retry once drain begins, including interruptible cooldown;
- fulfilment only on definitive `RUNNING` for the exact run;
- concurrent tty socket connects for different containers do not serialize;
- console retry observes cancellation and a shared shutdown deadline.

Extend the RSpec-style vpsAdminOS VM test to restart osctld during multiple
boot autostarts blocked at pre-mount, pre-start, veth-up, and on-start. Assert a
bounded restart, one LXC start per generation, eventual convergence of every
intended autostart, functional host veth/routes, and tty access. Also test:

- an aborted post-pre-start run is resumed by replacement osctld;
- `SIGKILL` mid-start is reconciled without leaving a live but unnetworked CT;
- nodectld coordination both before and after pools become ready.

The existing `tests/suite/osctld/restart.nix` test blocks one management
`osctl ct start` in pre-start. The management ThreadReaper drain keeps that
command alive until its hook is released, so the test passes. It does not cover
internal boot autostart executors, multiple simultaneous starts, callbacks
after `UserControl` teardown, console retry serialization, failed-start resume,
or missing-veth recovery.

## Follow-up state verification

At 20:36 CEST on 2026-08-22, the remote logs were checked again for all 36
affected containers. Every container's latest osctld monitor transition was
`RUNNING`, and there was no later transition for any of them in logs current
through `20:36:17` on both nodes.

- node23: all 20 affected containers had latest state `RUNNING`. The last one
  to reach it was tank `26854` at `19:44:32.170`.
- node24: all 16 affected containers had latest state `RUNNING`. The last one
  to reach it was tank `1341` at `18:27:44.523`.
- After their controlled stop/start at 19:25-19:28, there were no further
  missing-veth, missing-tty, improper-stop, or non-running state messages for
  node23 containers `14005`, `20274`, and `24800`.
- No matching missing-veth, missing-tty, improper-stop, or later non-running
  state message was found for the node24 set after recovery.

This is strong historical evidence, but it is not a live state query. Direct
`osctl` state, init PID, and host-veth checks on the nodes remain the definitive
verification.

## Compatibility and deployment

- Keep any status/API addition additive and avoid database/schema changes.
- Deploy node by node after VM coverage; mixed old/new nodes are acceptable if
  runtime lifecycle state remains backward compatible.
- If durable generation state is added, version it additively. An old daemon
  after rollback must ignore it safely or conservatively reconcile it rather
  than treating an incomplete new-generation start as successfully fulfilled.
- Test rollback against runtime state produced by the new daemon. A normal
  rollback should not require restarting healthy containers.
- A vpsAdmin change is appropriate for nodectld ordering/readiness, but the
  osctld safety fix must not require a coordinated update of every node.
