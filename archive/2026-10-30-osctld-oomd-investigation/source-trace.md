# osctl-oomd source trace and local proof

Read-only investigation by implementer0, 2026-10-30. Session identity and both
`DEV_SESSION_*` values verified against
`2026-10-30-osctld-oomd-investigation` and
`/home/aither/workspace/ai/vpsfree.cz`. No application changes, commits, fetches,
worktrees, production commands, builds or integration tests were performed.

## Conclusion and evidence boundary

The source permits a queued miss to recreate a pruned container record with
zero counters and no `last_hit`. The next prune evaluates `nil < Time` and
raises the exact reported exception. The daemon enables
`Thread.abort_on_exception`, making this worker failure process-fatal.
Both the state transition and process exit were reproduced locally using the
actual source loaded into memory from the canonical bare repository.

Local source revision:
`49636f902704ce6019a7a8ae47ec0b3ca6902f68` in `repos/vpsadminos.git`.
`killer.rb` blob: `e29af7eb8480a1d17dac1434f0d24f71829a3fe9`, unchanged since
`9a366e5d7c51acccba086a69170167bc92b75e9e` (2026-04-06).

Architect0 reports matching central-log failures at
2026-10-29 15:33:50.376 and 2026-10-30 13:26:51.279 CET, with replacement
daemons within one second. The logged package is
`/nix/store/fmzf8z0lf0bzg5pv3s5a5q2dpz3kpxil-ruby3.4-osctl-oomd-26.05.0/lib/ruby/gems/3.4.0/gems/osctl-oomd-26.05.0/`.
Its traceback locations match local source, but deployed source bytes and Git
revision were not independently verified. Gem version `26.05.0` alone does not
establish an exact revision. No host-key check was bypassed.

## Source chain at the local revision

All paths below are relative to vpsadminos at the revision above.

| File and lines | Evidence |
| --- | --- |
| `osctl-oomd/bin/osctl-oomd:2-4` | Requires the CLI and calls `Cli.run`. |
| `osctl-oomd/lib/osctl/oomd/cli.rb:11-28` | Enables `Thread.abort_on_exception = true` at line 12 and runs the watcher. |
| `osctl-oomd/lib/osctl/oomd/watcher.rb:25-33` | Starts killer, exporter and ct-top workers. |
| `osctl-oomd/lib/osctl/oomd/watcher.rb:55-62` | Separately tests `watched?` and queues a miss for a currently watched container. |
| `osctl-oomd/lib/osctl/oomd/killer.rb:7-39` | Nested `Container`: construction sets counters to zero but no timestamps (10-15); only `hit` sets `last_hit` (17-21); `miss` clamps counters at zero (24-29). |
| `osctl-oomd/lib/osctl/oomd/killer.rb:53-55` | Starts event and prune threads without an exception rescue. |
| `osctl-oomd/lib/osctl/oomd/killer.rb:58-69` | Hit/miss operations enqueue events; `watched?` checks positive counters under a mutex. |
| `osctl-oomd/lib/osctl/oomd/killer.rb:85-106` | A single event consumer creates a missing record for every event (93), including a miss (99). |
| `osctl-oomd/lib/osctl/oomd/killer.rb:117-155` | Event worker synchronously waits for `osctl ct` (124), then event broadcast (139-143), outside the container mutex. Queueing and pruning can continue during this wait. |
| `osctl-oomd/lib/osctl/oomd/killer.rb:158-169` | Every 60 seconds, deletes zero-counter records whose last hit is older than 300 seconds. Line 166 compares `last_hit` without a nil check. |
| `libosctl/lib/libosctl/queue.rb:10-18,37-61` | FIFO queue; events are not coalesced or canceled when a tracked record disappears. |
| `os/modules/osctl/osctl-oomd.nix:43-56` | Runit service waits for osctld and execs osctl-oomd. |
| `os/modules/system/boot/runit/default.nix:316-335` | Default service finish sends SIGTERM to the remaining service cgroup, consistent with child termination after the crash. |

## Reachable sequence

1. A tracked container has positive counters; its last hit eventually becomes
   older than five minutes. The serial event worker can be delayed in an
   external restart/stop command while the watcher continues queueing misses.
2. The watcher sees positive counters twice and enqueues two misses. Each
   `watched?` result is valid at observation time; it does not reserve a record
   for later event consumption.
3. Processing a miss drains the remaining counters to zero. Further queued
   misses can still exist.
4. The prune worker removes that zero-counter record because its last hit is
   older than five minutes.
5. A later queued miss finds no record. `process_events` constructs a new
   `Container`, then calls `miss`: counters remain zero and `last_hit` is nil.
6. Unless a new hit arrives first, the next prune raises at `killer.rb:166`.

This is a possible ordering under the existing locks and queues. No malformed
ct-top input is necessary. Architect0's logs support this mechanism: a
`tank:27837` restart occupied the worker from 13:15:21.950 to 13:24:41.272 CET,
followed by bursts of misses including repeated 0/0 entries. The exact production
prune/removal/interleaving is inferred: pruning itself does not log removals.

## Local reproduction and result

Executed successfully with Ruby 3.4.9. The harness evaluated unmodified
`killer.rb` and the real `OsCtl::Lib::Queue` directly from `git show`; only
logging was stubbed. Two Fibers supplied deterministic event/timer boundaries,
and the timestamp was aged in memory to represent elapsed time. No service,
external osctl command, real timer wait or source edit was involved.

Compact reproducer, run from the workspace root:

```ruby
rev = '49636f902704ce6019a7a8ae47ec0b3ca6902f68'
module OsCtl
  module Oomd; end
  module Lib
    module Utils
      module Log
        def log(*); end
      end
    end
  end
end
$LOADED_FEATURES << 'libosctl.rb'
%w[libosctl/lib/libosctl/queue.rb osctl-oomd/lib/osctl/oomd/killer.rb].each do |path|
  src = IO.popen(['git', '--git-dir=repos/vpsadminos.git', 'show', "#{rev}:#{path}"], &:read)
  raise 'git show failed' unless $?.success?
  eval(src, TOPLEVEL_BINDING, path)
end
k = OsCtl::Oomd::Killer.new(restart_hits: 8, stop_hits: 40, dry_run: true)
ct = OsCtl::Oomd::Killer::Container.new('tank', 'ct1')
ct.hit
ct.instance_variable_set(:@last_hit, Time.now - 601)
k.instance_variable_get(:@containers)['tank:ct1'] = ct
2.times do
  raise 'not watched' unless k.watched?('tank', 'ct1')
  k.add_miss('tank', 'ct1')
end
k.instance_variable_get(:@event_queue).define_singleton_method(:pop) do
  Fiber.yield
  super()
end
k.instance_variable_get(:@prune_queue).define_singleton_method(:pop) do |**|
  Fiber.yield
  nil
end
events = Fiber.new { k.send(:process_events) }
pruner = Fiber.new { k.send(:prune) }
events.resume
pruner.resume
events.resume                    # First miss: zero counters, valid timestamp
pruner.resume                    # Removes idle record
raise 'not pruned' unless k.export.empty?
events.resume                    # Stale miss recreates record
raise 'not nil' unless k.export.first.last_hit.nil?
pruner.resume                    # NoMethodError at killer.rb:166
```

Observed output from the equivalent instrumented harness:

```text
after first queued miss: counters=[[0, 0]] last_hit_present=true
after scheduled prune: tracked=0
after stale queued miss: counters=[[0, 0]] last_hit=nil
next scheduled prune: NoMethodError: undefined method '<' for nil;
  osctl-oomd/lib/osctl/oomd/killer.rb:166
abort_on_exception child: exit=1 main_survived=false
  exact_prune_failure=true traceback_renderings=2
```

The independent child-process check loaded the same source, enabled
`Thread.abort_on_exception = true`, inserted a fresh miss-only record, primed
the prune queue and called the actual `Killer#start`. Its prune failure ended
the child with status 1 before the main thread reached its survival marker;
two traceback renderings contained the same `NoMethodError`. Duplicate traces
therefore do not establish two distinct failures. Runtime restart observation
comes from architect0's logs, not a locally started runit service.

## Recommended correction and acceptance

Within the existing event-processing mutex, create records only for `:hit`.
A `:miss` for an absent record should be a no-op. This preserves the invariant
that every tracked record has received a hit and has a valid `last_hit`.
A nil guard in pruning alone would leave an invalid miss-only record behind.
This is a recommendation; no fix was implemented or tested.

Focused regression acceptance for a future fix:

- Unknown miss creates no tracked record and triggers no action.
- The deterministic miss/prune/stale-miss sequence leaves the record absent;
  repeated pruning remains safe.
- A real hit creates timestamps and counters; a miss decreases counters without
  making them negative.
- Zero-counter records older than 300 seconds are pruned, recent zero-counter
  records are retained, and positive-counter records remain tracked.
- Existing restart/stop thresholds and successful/failed-action counter reset
  semantics remain intact.

State is in memory; this correction needs no persisted-state migration or
cross-node protocol change. Exact production triggering order and deployed
source identity remain the stated limits. Lead owns final state/portal updates.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-osctld-oomd-investigation/>
