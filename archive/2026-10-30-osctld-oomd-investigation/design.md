# osctl-oomd stale-miss fix and incident evidence

Owner: architect0. The initial read-only incident diagnosis for node23.prg on
2026-10-30 is complete. The user subsequently said "ok, implement the fix",
as relayed in the lead's implementation assignment. Scope now includes the
narrow event-processing correction and regression coverage defined below.
The service is named `osctl-oomd` in the logs and source.

Lead owns plan/state/portal and delivery coordination; architect0 owns this
design; implementer0 owns the source change, regression tests and quick checks.
Integration and deployment remain unauthorized. The incident evidence below
describes the original failure and is preserved independently of implementation
progress, which belongs in the lead's state record.

## Finding

The pruning thread dereferences a missing `last_hit` timestamp. The recorded
expression is `ct.stop_hits == 0 && ct.restart_hits == 0 && ct.last_hit < Time.now - 300`;
the first two conditions pass and `nil < Time` raises `NoMethodError`.
This is a tracking-record invariant bug, with a reachable stale-miss/prune
interleaving identified in source. Long container restart handling and bursts of
queued misses immediately precede the production failure and support that
trigger; the logs do not record the actual deletion/recreation interleaving.

## Evidence and attribution

Read as `root@log.int.prg.vpsfree.cz`, whose `hostname -f` agrees. Primary file:
`/var/log/remote/localhost/log`. Every cited line embeds
`node23.prg.vpsfree.cz osctl-oomd`, distinct from other nodes interleaved there.
The running rsyslog process uses
`/nix/store/ygyjf4i3m7gl6l41n7dwnkv8r5privir-syslog.conf`, whose remote file template
is `/var/log/remote/%HOSTNAME%/log`. The received record is parsed with outer
hostname `localhost` while the original svlogd timestamp/hostname/service remain
in its body. Thus the directory name is not evidence that the error arose on the
log server. A separate node directory also exists at
`/var/log/remote/cz.vpsfree/nodes/prg/node23`.

Exact ordered excerpt, with unrelated lines omitted; outer timestamps use CET
(`+01:00`), while the embedded svlogd timestamp uses UTC:

```text
2026-10-30T13:26:19.482898+01:00 localhost 2026-10-30_12 26:19.48286 node23.prg.vpsfree.cz osctl-oomd I, [2026-10-30T13:26:19.482391 #2545797]  INFO -- : [killer] restart dozer:28376
2026-10-30T13:26:44.753738+01:00 localhost 2026-10-30_12 26:44.75368 node23.prg.vpsfree.cz osctl-oomd D, [2026-10-30T13:26:44.753621 #2545797] DEBUG -- : [watcher] OOMd inactive
2026-10-30T13:26:51.279297+01:00 localhost 2026-10-30_12 26:51.27920 node23.prg.vpsfree.cz osctl-oomd #<Thread:0x00007a0dc6508338 /nix/store/fmzf8z0lf0bzg5pv3s5a5q2dpz3kpxil-ruby3.4-osctl-oomd-26.05.0/lib/ruby/gems/3.4.0/gems/osctl-oomd-26.05.0/lib/osctl/oomd/killer.rb:55 run> terminated with exception (report_on_exception is true):
2026-10-30T13:26:51.326928+01:00 localhost 2026-10-30_12 26:51.32683 node23.prg.vpsfree.cz osctl-oomd /nix/store/fmzf8z0lf0bzg5pv3s5a5q2dpz3kpxil-ruby3.4-osctl-oomd-26.05.0/lib/ruby/gems/3.4.0/gems/osctl-oomd-26.05.0/lib/osctl/oomd/killer.rb:166:in 'block (3 levels) in OsCtl::Oomd::Killer#prune': undefined method '<' for nil (NoMethodError)
2026-10-30T13:26:51.334989+01:00 localhost 2026-10-30_12 26:51.33492 node23.prg.vpsfree.cz osctl-oomd /nix/store/fmzf8z0lf0bzg5pv3s5a5q2dpz3kpxil-ruby3.4-osctl-oomd-26.05.0/lib/ruby/gems/3.4.0/gems/osctl-oomd-26.05.0/lib/osctl/oomd/killer.rb:166:in 'block (3 levels) in OsCtl::Oomd::Killer#prune': undefined method '<' for nil (NoMethodError)
2026-10-30T13:26:51.365900+01:00 localhost 2026-10-30_12 26:51.36577 node23.prg.vpsfree.cz osctl-oomd error: SIGTERM
2026-10-30T13:26:51.775110+01:00 localhost 2026-10-30_12 26:51.77502 node23.prg.vpsfree.cz osctl-oomd I, [2026-10-30T13:26:51.774826 #640135]  INFO -- : [ct-top] Started with pid 640300
2026-10-30T13:27:08.788376+01:00 localhost 2026-10-30_12 27:08.78836 node23.prg.vpsfree.cz osctl-oomd D, [2026-10-30T13:27:08.788242 #640135] DEBUG -- : [watcher] OOMd inactive
```

Backtrace continuation: `Killer#prune` line 165 (`Hash#delete_if`), line 162
(`Thread::Mutex#synchronize`), line 159 (`Kernel#loop`), then `Killer#start`
line 55. Both renderings describe the same failing thread and expression.

The exact logged package is
`/nix/store/fmzf8z0lf0bzg5pv3s5a5q2dpz3kpxil-ruby3.4-osctl-oomd-26.05.0`.
Implementer0 reports the same failing expression/line at canonical bare HEAD
`49636f902704ce6019a7a8ae47ec0b3ca6902f68`. This is a source match at the implicated
code, not proof that the entire deployed system equals this Git revision.
Direct node SSH failed host-key verification; no bypass, trust change or further
SSH investigation was performed. Deployed system path and Git revision remain
unverified.

## Recurrence and preceding operations

The bounded scan covered the complete daily files `log-20261028` (Oct 27,
160,589,537 bytes), `log-20261029` (Oct 28, 151,138,659 bytes),
`log-20261030` (Oct 29, 172,590,590 bytes), plus today's current file through the
collection around 13:35 CET (about 100 MB). Every read was capped at 180 MB or
less, and output filtered to this hostname/service. No full-history scan.

| Local date/time (CET) | Signature | Observed daemon transition |
| --- | --- | --- |
| Oct 29 15:33:50.376 | `killer.rb:166`, nil `<`, pruning thread | 3438 → 2545797; new `ct-top` starts at 15:33:50.887 |
| Oct 30 13:26:51.279 | Same exception and package path | 2545797 → 640135; new `ct-top` starts at 13:26:51.774 |

There are two crash events, each with two traceback renderings. No matching
exception was found on Oct 27 or Oct 28 within these files. Separate warnings
`osctl ct restart tank:27837 failed` appear Oct 27 08:36:38.661 and Oct 29
15:31:11.923. Their underlying container restart failure is not diagnosed here
and must not be presented as the same root cause.

Today's relevant operation sequence:

- 13:15:21.950: `tank:27837` reaches 8/8 restart hits, 8/40 stop hits;
  `[killer] restart tank:27837`.
- 13:24:41.272: its stop/start/console output arrives more than nine minutes
  later. At 13:24:41.936 the event worker resumes with `dozer:28376` hits and
  `tank:27837` misses; another restart begins.
- 13:25:08.102: a microsecond-scale burst drains `tank:27837` to zero counters,
  interleaved with `dozer:28376` hits. Further miss/hit bursts and dozer restarts
  occur at 13:25:44.616 and 13:26:19.482. The tank record repeatedly logs 0/0
  misses; dozer reaches 32/40 stop hits at its last restart before the crash.
- 13:26:51.279: pruning thread fails; about half a second later a new daemon
  initializes its `ct-top` child. Normal watcher messages resume and remain
  visible through 13:32:19.778 in the collected tail.

## Causal interpretation and impact

The source trace identifies `Container#initialize` with zero counters and no
`last_hit`; only `hit` initializes that timestamp. `process_events` creates a
new record for a miss as well as a hit. A miss for a record already removed by
pruning therefore constructs a zero-counter record with a nil timestamp.
The next prune evaluates the unsafe comparison. Source allows this through
separate watcher lookup/enqueue operations and through queued events retained
while the single event worker performs container actions.

The delayed restart and subsequent event bursts support that reachable path on
node23. The exact doomed record and instruction interleaving are inferred,
because creation/deletion and timestamps are not logged. `tank:27837` is the
leading candidate from the repeated zero-counter misses; do not claim it is
proven to be the nil record.

`Cli.run` sets `Thread.abort_on_exception = true` (line 12 in the traced source),
making the pruning exception fatal to the daemon. The runit service executes
that daemon, and the observed new PID plus immediate `ct-top` initialization
supports supervisor restart. The traced runit finish script calls control-group
SIGTERM (`os/modules/system/boot/runit/default.nix:316-332`), explaining cleanup
of remaining child processes after the daemon exits. The SIGTERM messages follow
the exception; their emitting process is not identified by these lines. This is
not merely a dead background thread or evidence that an independent SIGTERM
initiated the incident.

The OOM policy daemon temporarily loses service and resets its in-memory
hit/miss history when restarted. Its watcher resumes, so the observed outage
is transient. The recorded container restarts were policy actions already in
progress before the exception; no additional container loss or lasting service
outage is established by this investigation.

## Completed diagnosis checks

The completed independent diagnosis package assigned to implementer0 covered
`osctl-oomd/lib/osctl/oomd/{killer,watcher,cli}.rb` (the tracked `Container` class
is nested in `killer.rb`) and the runit module,
with a deterministic in-memory reproduction of miss delivery after pruning.
Acceptance: establish reachability, exception propagation, smallest correction
and a regression scenario without running container commands or modifying source.
Completed by implementer0; detailed evidence is in [source-trace.md](source-trace.md).

The deterministic reproduction loaded actual `killer.rb` and `libosctl` Queue
source read-only from bare Git revision
`49636f902704ce6019a7a8ae47ec0b3ca6902f68`, with Ruby 3.4.9. With a timestamp aged
601 seconds and two queued misses, explicit Fiber boundaries produced:

1. First miss: counters become 0/0 and timestamp remains present.
2. Prune: removes the old zero-counter record.
3. Second miss: recreates a 0/0 record with nil `last_hit`.
4. Next prune: raises the exact `NoMethodError` at `killer.rb:166`.

No real delay or container command was used. A separate local subprocess loaded
the same source, enabled `Thread.abort_on_exception`, and invoked the actual
`Killer#start` with a primed prune queue. It exited with status 1; the main thread
did not survive, and Ruby rendered the exception twice, matching the production
traceback duplication. These checks prove a reachable mechanism and fatal
propagation, while leaving the production interleaving explicitly inferred.

## Accepted implementation and verification brief

Required invariant: only a hit may create a tracked record; a miss for a
missing record is a no-op. Apply the existence check and creation decision in
the same synchronized event-processing section. A nil guard in pruning alone
would conceal invalid miss-only records and leave their lifecycle unresolved.

One implementation package, owned by implementer0:

- Change `osctl-oomd/lib/osctl/oomd/killer.rb` in `process_events` so only a hit
  creates a missing nested `Container`; ignore a miss whose record is absent.
  Keep record lookup, creation and counter mutation under the existing mutex.
- Extend `osctl-oomd/spec/osctl/oomd/killer_spec.rb` using its existing harness.
  Exercise the actual event-processing and pruning paths with deterministic
  queue/timer boundaries, without real container commands or elapsed-time waits.
- Preserve event interfaces, FIFO processing, counter decay/clamping, hit
  timestamps, pruning age, action thresholds and action-result reset behavior.
  Watcher, queue, CLI and runit contracts need no change. There is no dependency
  on another implementation package or on further incident investigation.

Acceptance criteria:

1. An initial unknown miss creates no record and triggers no container action.
2. After a valid hit and queued misses, processing one miss can drain counters;
   pruning can delete the old record; a later queued miss leaves it absent.
   Subsequent pruning completes without an exception. This regression must fail
   against the original event-processing behavior and pass with the correction.
3. Real hits still create valid timestamps and counters. Misses on existing
   records decrement counters without making them negative.
4. Old zero-counter records are pruned, recent zero-counter records remain,
   and records with positive counters remain tracked.
5. Existing restart/stop thresholds and successful/failed-action counter reset
   tests continue to pass.

Quick verification uses the repository's Nix Ruby environment: run the focused
`killer_spec.rb`, then the `osctl-oomd` RSpec suite and applicable declared hooks.
Keep checks bounded to this component and report exact commands/results through
the lead. Once intended changes are committed and quick checks pass, the lead
coordinates mandatory independent final change review. No long VM integration
test is needed for this in-memory bookkeeping change; reconsider only if the
implementation changes real restart, supervision or packaging behavior. A
material design deviation goes through the lead before expanding scope.

No API, protocol, database, persisted-state or Nix option change is needed for
the accepted correction. Nodes can update independently; coordinated fleet
updates are unnecessary. Existing persisted state remains compatible in both
directions. The corrected daemon still uses in-memory tracking; a later
deployment that restarts it resets this transient history as before.
Deployment/restart and rollback are not authorized or performed; rolling back
the local code fix would reintroduce the defect. No production recovery action
is needed for the investigation or feature-branch implementation.
