# 2026-11-19-ct-top-full-team-validation-retry-2

## Goal

User request: Launch a new session with the Pi backend and codex-lb provider, with a Full team, to independently validate or improve the proposed solution to unstable osctl ct top content. Scope now is investigation, reproductions and a validated/improved fix proposal; do not infer approval to merge, deploy, or implement a production fix.

Issue: in one continuous osctl ct top run during osctld restart, and also during normal operation, the container list disappears and returns. Some refreshes show rows but no CPU usage, only -/socket. The user explicitly confirms the affected implementation is already in the default branches and deployed in production. Verify fresh upstream/default sources; the prior investigator incorrectly treated stale local bare HEAD 49636f902 as upstream default and later corrected this. Do not repeat that claim.

Evidence: four screenshots, inputs outside version control (read these exact paths):
1. /home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/uploads/files/90e75fd4-d7e7-4ae2-a33a-99e9b4c7f203/file.png : 11:31:03, total 67, only placeholder host, CPU/memory/ARC calculating, 0 running.
2. /home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/uploads/files/450f7afc-aae3-4465-adb3-56924cbe652d/file.png : 11:31:27, total 189, running 154, memory/load values present but CPU/network/ZFS rates are dashes; CPU cells -/0 or -/1.
3. /home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/uploads/files/9965395b-eeec-408a-9e85-868e56c6b84f/file.png : 11:31:40, total 225, running 186, full normal metrics.
4. /home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/uploads/files/ccc699d5-025f-4f9d-a9b6-d8024d3744eb/file.png : 11:31:57, total 249, only placeholder host, CPU/memory/ARC calculating, 0 running.
Keep screenshot files out of version control. Source conversation reference only: work/2026-11-17-ct-top-display-bug; it has no application edits from this investigator. Do not adopt or mutate its state/team/resources. No standing cross-session communication permission is implied by this initial handoff.

Hypothesis to validate, not settled design: the coherent snapshots implementation (located locally at ea46474c5, osctl: add optional Top collectors and coherent snapshots, on ref 2026-11-12-node-loadavg-investigation-watchdog-top) applies strict whole-sample invalidation to interactive display and global baseline resets, producing both symptoms.
Relevant osctl/lib/osctl/cli/top/model.rb paths at that revision:
- measure captures global generation and rejects publication if changed during acquisition. monitor.rb calls changed! for state/PID/CPU-scheduling/netif events.
- checks two running inventories, process run identities, all required cgroup values, and requires a valid loadavg entry for every running container.
- rescue StandardError resets host and every container's measurements, clears baseline, and publishes invalid_snapshot: CPU/memory/load/ZFS nil and containers=[placeholder host].
- reason = measured_host.core_delta_error || running.filter_map(&:core_delta_error).first. Any new/restarted container needing initial_baseline causes rates suppressed for ALL rows, and all histories reset to one retained measurement.
- result_for retains gauges but nils rate/counter fields for a reason; TUI renders nil CPU as '-' then appends /socket. UI running count = published rows minus host, misleadingly zero on invalid frames.

Prior focused reproduction executed actual model.rb sampling/projection code with simulated inventory, host/container measurements, load reader and one changed! event. Output: stable valid rows/CPU -> one event during collection: inventory_changed and only host -> next successful refresh: initial_baseline and all rows with nil CPU -> following refresh: normal values. Adding one new container suppressed CPU for all rows. Removing one container load entry yielded missing_container_load and only host. This was a focused simulation, NOT a production/interactive integration reproduction. Exact reason per screenshot was not captured.

Proposed direction to challenge/improve: isolate validity and baseline history per container run/collector, preserve unaffected rows and host gauges/rates, avoid allowing scheduling/netif metadata changes to globally invalidate unrelated core metrics. Count lifecycle states from inventory, label unavailable/warmup/stale samples with reasons. Preserve strict coherent complete/valid semantics for watchdog/JSON/oomd automated decisions; partial display data must never become actionable inadvertently. If retaining an old frame, keep original timestamps and explicit stale status. Assess JSON compatibility and automated consumer contracts before choosing an interface or implementation. Also evaluate counter reset/window checks and event churn amplification as possible triggers. No need to implement a new subsystem if a small separation suffices.

Earlier findings against stale older code (transient measurement sets ct.state=:error; event stream lacks reconnect; raw cursor query uses swapped coordinates) are not established as the cause of these screenshots. Treat independently and do not let them distract or expand scope.

Deliver: independently established root cause, reproduction evidence, smallest safe fix design and regression/compatibility plan. Use Full-team ownership: architect substantive diagnosis/design, bounded independent implementer reproduction/consumer-contract investigations where useful, lead synthesis. This user explicitly requests validation; an advisory reviewer critique of the proposed design is authorized, but final change review rules still apply if later implementation is requested. Do not start production mutations. Suggested acceptance: existing rows/rates survive another container's add/restart, mid-sweep metadata event, one missing loadavg/cgroup metric, with safe run-identity boundaries and strict consumers rejecting incomplete data.

## Implementation plan (authorized)

This is the consolidated proposal published as `59d8ad12-a8cf-4342-bd3d-7dbba97fbb0f`, including the `~` amendment. The user authorized implementation, not integration, deployment, or enabling oomd actions. The original investigation brief above is retained as provenance. The architect owns the detailed implementation and verification brief in `design.md`.

## Affected repositories

- `vpsadminos` (`staging`): `osctl` interactive and opt-in JSON Top, and `osctl-oomd`.
- `vpsadmin` (`master`): `libnodectld` and compatibility checks against the existing supervisor consumer.

## Approach and decisions

1. **Top:** Use one sampling sweep per invocation and shared existing readers; select policy before the setup seed. Keep the default `osctl -j ct top` schema-1 route, including incomplete/warmup frames, nulls, baseline recovery, units, timing/window metadata, collector switches and interval/USR1 behavior. The TUI and explicit `osctl -j ct top --partial` use best-effort acquisition. Pin representative versioned wire fixtures before releasing consumers. Expose original time/sequence, inventory coverage, current run identity, load and resource availability, and a distinction between unknown and known-unlimited limits. Do not bridge gaps, reset neighbors, replace live monitor metadata with stale copies, hold the publication lock across I/O, or turn an unknown inventory into an empty one.
2. **TUI:** Keep independently valid gauges and rows. Take lifecycle counts from inventory. Prefix comparable measured partial totals with `~` per affected metric and explain it in the legend: missing contributors are excluded, not estimated. Leave complete and independently measured node totals unmarked. Show a dash if there is no usable number, and zero only for actual zero or a known-empty contributor set. Do not sum incompatible windows or attribute missing observations to the synthetic `[host]` residual. No stale row cache, unsafe PID target or reconnect redesign.
3. **nodectld:** Keep the full Top observation and join by pool/ID and current PID/start ticks. Use independent authoritative lifecycle, rescue and autostart evidence; missing telemetry does not mean stopped. Preserve cadence/USR1, reject wrong-run/stale/ambiguous stats, and opt in only with a compatible CLI. Publish healthy VPSes normally. For a running VPS without the required stats bundle, keep the existing `status:false, running:true` envelope. No new nil arithmetic, fake zeros, stale carry-forward, AMQP/public API/DB change, or sparse downstream status redesign.
4. **oomd:** A disabled-by-default partial-restart option uses the guarded controller, not the legacy unguarded action path. Keep existing ordinary and watchdog behavior when disabled. Require a verified running inventory and all ranking loads including host, but allow a fresh same-run candidate with sufficient CPU/memory/limit evidence when a different row is missing resource metrics. Unknown is not a hit or miss. Preserve ranking and thresholds, use established complete-sample host-load history, require distinct qualifying post-entry sweeps in watchdog mode, and recheck evidence, gate and expected run at dispatch. Partials do not advance or authorize stops and cannot substitute a restart for a pending stop. A blocked sweep supplies no new evidence.

## Compatibility and deployment

Default strict JSON remains usable by old consumers. New nodectld can report through the existing supervisor protocol, retaining supported legacy CLI behavior. Upgrade the CLI before opting in to partial data and verify the daemon guard before partial oomd use. Evaluate oomd in observe-only mode before seeking separate approval to enable actions. Roll back by disabling partial actions and draining guarded work, and by restoring legacy reporting before rolling back the CLI. No DB migration, fleet lockstep, or production fault injection.

## Documentation

Update Top’s man page for the machine opt-in mode and `~` display, `docs/os/oomd.md` for policy and operational limits, and the owning nodectld integration documentation for version pairing and unavailable status. Keep temporary receipts and reproduction inputs out of project commits.

## Testing plan

- Replay B’s missing memory with A healthy: A retains rates/cumulative origin, only affected totals get `~`, nodectld publishes A normally and B as running but unavailable, and qualified A can earn a guarded mock restart.
- Cover start/stop/restart including PID reuse, scheduling/netif events, missing load/cgroup, invalid time intervals and resets, stale/duplicate/unknown inventory and blocked sampling, complete recovery, compatible totals and no `~0` for entirely unavailable inputs. Verify default JSON golden output, USR1 and collector-off behavior.
- Exercise old/new CLI/consumer combinations and the existing vpsAdmin supervisor. Test both oomd gates, no partial stops, no actions with stale/unproved evidence, and no score from ticks without a sample.
- After committed quick checks and independent final review, run disposable daemon restart, overload/RTNL, and vpsAdmin reporting integration. Record exact source and test results. No approval to merge or deploy is inferred.
