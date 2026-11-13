# CT1391 shutdown during osctld import: package C evidence

Status: bounded source investigation, 2026-11-13. Owner: implementer2. This is
investigation evidence and a proposal for architect0, not implementation or an
operational recovery instruction. Only this file was written by package C.

## Revisions, evidence boundary and checks

- Verified `dev-session current` and both `DEV_SESSION_SLUG` /
  `DEV_SESSION_WORKSPACE` against the trusted session binding before reading
  session files. Confirmed the retained same-session roster with
  `dev-session team list 2026-11-13-osctld-start-recovery-errors --as-is`.
- Source worktree: `worktrees/2026-11-13-osctld-start-recovery-errors/vpsadminos`.
  `git rev-parse HEAD origin/staging c0ad0ad` returned the same full revision
  for all three: `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`.
  Fresh `git ls-remote origin refs/heads/staging` independently returned that
  same revision. Origin is `git@github.com:vpsfreecz/vpsadminos.git`.
- The fleet deployment pointer, unchanged kernel 6.12.113, imported count,
  CT1391 timeline and successful manual recovery are user-supplied facts in
  [incident.md](incident.md). No production system/profile or logs were queried;
  the actual installed closure was not independently measured by this package.
- Read repository AGENTS/README and relevant osctld interface/development and
  container administration docs. Inspected source and existing specs below with
  `rg`, `cat` and `nl -ba`. No Ruby/VM test, build, code edit, hook/index mutation,
  commit, fetch, deployment or merge was performed. Static inspection establishes
  code paths; it does not reproduce the supplied production interleaving.

All source references below are relative to the vpsadminos worktree at the exact
revision above. The assignment is limited to current source; July comparison
belongs to implementer1. No older-session records, worktrees, teams or transcripts
were accessed by package C.

## What the incident establishes

The supplied timeline places guest teardown during new-daemon import: the old
daemon finished stopping at 23:04:18.616088 CET; guest systemd shutdown appears
at 23:04:46.967761; new osctld logs loading CT1391 at .996927. It receives
`veth_down` at 23:04:47.155460 and `ct_post_stop` at .284027; both LXC hook
scripts exit 1. Container preparation is still doing a dataset mountpoint query
at 23:04:48.429888. Both pools finish import at 23:06:59.

The subsequent 23:07:21 nodectld start request reaches veth-up with new
`vethjPIcYT(1180)` and is rejected against retained `vethxxOnPg(20)`. Recovery
reports the old recorded link absent, then retained host-link ownership. The
later generic start rejection and the user's successful privileged
`forget-host-link` followed by recovery cleanup fit the existing ownership and
taint gates.

This supports lost/failed normal teardown during import, retained host-link
metadata and a later failed start. It does **not** establish who initiated guest
shutdown, whether `LXC_TARGET` was halt or reboot, the exact hook JSON responses,
or the precise CT1391 DB publication time. The user-initiated-shutdown account is
plausible, not proven by the guest SIGTERM line. A failed hook status alone does
not distinguish lookup failure, ownership rejection, hook exception or another
handler error. Missing normal veth-down execution logging plus the import order
makes pre-publication lookup failure a strong source-backed explanation, not a
captured response.

## Source path and the publication window

| Source | Verified behavior / consequence |
| --- | --- |
| `osctld/lib/osctld/pool.rb:274` | Pool setup loads users before groups and containers; it becomes active only after container import and remaining setup. |
| `osctld/lib/osctld/commands/user/setup.rb:34` and `user_control/supervisor.rb:117` | User setup adds the user and starts its control socket before CT loading. Socket owner root, group user UGID, mode 0660; handler carries that user object. Callbacks can reach a valid user endpoint before their CT is published. |
| `osctld/lib/osctld/pool.rb:692` | Ordinary path constructs/loads CT, ensures limits, prepares LXC home/log/config, samples `fresh_state`, ensures runtime config if running, registers monitoring, reconnects tty0 if running, and only then calls `DB::Containers.add` at 743. |
| `osctld/lib/osctld/pool.rb:701` | Running NixOS-impermanent recovery already has a distinct authenticated publication path inside `ct.manipulate('pool import')`, before monitor/console attachment. Preserve its authentication and reclamation inhibition; it is not proof ordinary CT1391 used that path. |
| `osctld/lib/osctld/db/containers.rb:6` | Publication validates all container host-link claims under the global host-link registry lock. Failed/uncertain import inhibits temporary-dataset retirement; already-published objects remain managed (`pool.rb:744`). |
| `osctld/lib/osctld/user_control/commands/veth_down.rb:12` | First DB lookup, then `owns_ct?`, then normal log/netif lookup/down and user hook. An unpublished CT returns `container not found` before normal execution logging. |
| `osctld/lib/osctld/user_control/commands/ct_post_stop.rb:14` | Same lookup/owner sequence before AppArmor/BPF cleanup, reboot request, retirement, user hook or fallback scheduling. |
| `osctld/lib/osctld/user_control/commands/base.rb:24` | Ownership is `ct.user == user`; no run ID or callback generation is supplied by these hook commands. The generic namespaced endpoint permits only other mounting hooks, not these stop callbacks. |
| `osctld/hooks/veth-down:43`, `hooks/ct-post-stop:26` | One socket request with pool/CT and interface+veth or target. A false status prints the returned message and exits false; no retry/spool exists. |
| `osctld/lib/osctld/generic/client_handler.rb:175` | The debug received-command line occurs before execution. Error hashes become false-status replies; unexpected handler exceptions become `internal error`. Thus received-command logging does not prove accepted teardown. |

The ordinary window begins before CT construction finishes: the user socket
already exists while `Container.new` loads config, devices, netifs and saved run
state. It ends only at successful DB insertion. There is also a narrower window
between monitor registration and insertion: `Monitor::Process#update_state`
(`monitor/process.rb:128`) looks up in DB and drops events for an unpublished CT.
`Monitor::Master#update_state` (`monitor/master.rb:132`) samples state directly,
but does not perform post-stop retirement or reconstruct a stop target.

## Retained identity and cleanup are intentionally fail-closed

`container.rb:1042` loads internal on-disk config with `trusted_runtime: true`;
external replacement/import config does not gain that runtime authority. Saved
host links carry name, veth/IFB ifindices, boot ID and taint
(`net_interface/veth.rb:68`). A record with a different host boot ID is dropped
on load (`:749`); restarting osctld in the **same** kernel boot retains it.
Legacy records without a boot ID are adopted into the current boot and saved.

`Veth#setup` (`:202`) preserves an existing record even if its link is absent or
its index reused; it only discovers by name when there is no saved identity and
the CT is running. Routed setup may taint a missing live link while running
(`net_interface/routed.rb:72`); it does not erase ownership. Config loading
promotes netif taint to container recovery taint and persists setup changes
(`container.rb:101`, `:1139`).

`Veth#up` validates the live new veth, rejects an inconsistent prior identity or
cleanup taint, and persists a new accepted record before later host mutations
(`veth.rb:269`, `:356`). Failure taints a retained record. It cannot safely
replace `vethxxOnPg(20)` merely because the new hook proposes another name/index.

`Veth#down` validates callback name, positive saved indices and unshared claims,
deletes saved IFB first, persists partial completion, then deletes veth and
clears/persists the record (`:309`, `:388`). Kernel deletion requires the saved
index to still resolve to the expected name and kind, then deletes by reserved
name (`utils/ip.rb:77`). An absent/reused/wrong-kind record fails; it is not
normal success. Failures retain and taint ownership.

`Container::Recovery#cleanup_or_taint` (`container/recovery.rb:96`) attempts
cgroup cleanup, direct netif teardown and route-discovered cleanup, then verifies
all ownership released. Any failed stage retains container taint; complete
success may clear only that recovery taint. Direct teardown holds the registry
across all-record ownership preflight and delegated deletion (`:264`). Route
lookup is discovery, not deletion authority; discovered links must match the
exact configured netif's saved identity (`:176`, `:299`).

Explicit `forget_host_link` requires a fresh forced LXC stopped/no-init check,
the manipulation lock and unshared owner validation. It deletes no link:
`forget_absent_host_link!` requires both name and index absent for saved veth and
IFB on one netlink socket (`recovery.rb:139`, `veth.rb:438`). Only then does it
forget that netif's record. It does not by itself clear container recovery taint.
This explains the supplied two-stage recovery without making it universally
safe to recommend or automate for every start rejection.

`Container#can_start?` (`container.rb:413`) rejects staged/error state, container
or netif taint, and inactive pool. `Start#start_now` checks it before `--force`
(`commands/container/start.rb:83`), preserving force safety. Retained but clean
identity alone is not in this predicate: a stale record can therefore reject
later at veth-up, after which taint blocks subsequent starts. This is consistent
with the incident sequence.

## Shutdown, reboot and missing-callback variants

An accepted `ct_post_stop` handles `target == 'reboot'` by setting the current
run's in-memory reboot flag, captures `run_conf`, retires it via
`ct.stopped(run_conf)`, and runs the user hook. Its ensure block schedules the
shared stop handler only for a saved run without console ownership. Console
closure otherwise schedules that handler for the console's captured run.

`Container#stopped` (`container.rb:468`) keeps the retired run as `past_run_conf`,
clears current run and destroys its runtime file. `StopHandler#run`
(`container/stop_handler.rb:23`) waits up to 60 seconds for stopped state,
rejects a superseded explicit past run, and uses `claim_exit_handling` for
once-only cleanup. Proper stops fulfil the old run's exit promise after cleanup,
then reboot if requested; reboot waits for pool import before starting. Aborted
or improper stops use recovery cleanup/taint. An improper stop with no past run
has no trusted target from which to infer reboot.

`RunConfiguration#request_reboot` (`container/run_configuration.rb:345`) sets
`@do_reboot`; it is initialized false and is not in serialized `dump`.
Consequently:

- For a **halt** overlapping import, admission of the original callback can
  retire/clean its original run; if that callback has already failed, discovering
  stopped state can support conservative cleanup but cannot recover its target.
- For a **reboot** overlapping import, the callback's `LXC_TARGET=reboot` is the
  available intent. Dropping it and later reconciling only stopped state loses
  the restart request. Restarting every discovered stopped CT would wrongly turn
  halts into reboots.
- For a stop during the **daemon/socket blackout**, an import readiness gate
  alone cannot help: the existing hook does one connection and exits on failure.
  For a daemon crash **after callback acceptance**, an in-memory reboot flag
  alone is not durable either. Neither guarantee is provided by current source.

Monitoring only updates state and prunes mounts on STOPPED; it does not replace
post-stop semantics. `Recovery#recover_state` (`container/recovery.rb:23`) does
extra retirement/hooks only when original state differs from current stopped
state; if both are already stopped, it does not repair missed teardown. It also
has no reboot target. Thus a fresh-state sample or calling this helper alone is
not complete reconciliation.

## Smallest safe proposal for architect0

Keep this separate from the authorized diagnostics implementation. Recommend a
narrow **per-container stop-callback admission/readiness rendezvous during
import**, plus explicit stopped-run reconciliation at attachment completion.
Retain the current stop handler and host-link recovery mechanisms.

The rendezvous must exist before callbacks can arrive for CTs queued for import,
including before that CT's config load starts. It must wait without holding the
host-link registry, DB, container/config or manipulation locks. Only a fully
loaded/validated owner, netif manager and original run evidence can satisfy it;
failed/omitted import must resolve waiters with an error. A daemon stopping or a
bounded wait expiry must also resolve visibly. Do not acknowledge success before
the callback's effects complete. Unknown/nonimporting CTs and foreign owners must
continue to fail with no mutation.

Serialize callback retirement and import attachment for the **same original
run**: capture and recheck it; do not let post-stop retire a new run, let monitor
refresh create a replacement run, or let late console attachment claim a retired
one. Drain admitted stop effects / recheck authoritative state before exposing
normal start admission after import. Do not unconditionally stamp `:running`
after a callback. Preserve existing authenticated impermanent-root publication
and failed-import GC inhibition. A bare `DB.add` reorder or a manipulation lock
alone is insufficient: current user-control stop callbacks do not acquire that
lock, and partial object publication violates existing authority assumptions.

Reconciliation should distinguish an accepted target from an unknown target,
finish the exact old run's normal stop path once, and use existing identity-safe
cleanup/taint for missed effects. For this bounded fix, retain absent/reused-link
refusal and explicit privileged forgetting; do not silently weaken normal
`down` or clear taint based on STOPPED alone. If import reconciliation is to
release absent ownership automatically, that is a separate design decision:
require fresh stopped/no-init proof, both-selector absence, IFB and cross-record
checks, serialization against new starts and durable partial-failure handling.

Alternatives and boundaries:

1. Early authenticated publication followed by callback serialization could use
   existing objects with fewer rendezvous states, but must solve ordinary
   preparation re-entry and the monitor/console retirement race. The special
   impermanent path is an invariant to preserve, not a generic shortcut.
2. Hook-side bounded retry can cover socket blackout and importing lookup errors
   without a new disk schema, while keeping `LXC_TARGET` in the waiting process.
   It needs a precise retryable admission response, finite failure behavior and
   a guarantee the callback cannot replay onto a new run. Existing old hooks have
   no run token; never retry access-denied or identity failure as success.
3. Durable stop intent tied to an authenticated run can survive daemon crashes
   after acceptance and preserve reboot beyond the hook process. This needs an
   idempotent acknowledgement/consumption protocol, stale-run handling, rollback
   semantics and additional verification. A general lifecycle reducer is outside
   the incident's smallest fix and this package's scope.

The first proposal addresses callbacks delivered to the new daemon during import.
It does not claim guaranteed reboot recovery across the blackout or another
crash. If those are required, choose and document option 2/3 explicitly rather
than inferring intent from final LXC state.

## Deterministic regressions and compatibility

Use barriers/queues at import phases, not timing-only sleeps. Existing tests are
useful scaffolding, not evidence these interleavings pass:
`spec/osctld/pool_spec.rb:273` covers authenticated impermanent publication;
`:362` currently preserves ordinary late publication. `ct_post_stop_spec.rb`
covers direct versus console-owned cleanup and foreign-owner rejection;
`container/stop_handler_spec.rb` covers once-only/superseded runs, writeback and
reboot. Veth/recovery specs cover absence/reuse, cross-record claims, persistent
partial cleanup and explicit forgetting. `tests/suite/osctld/restart.nix` covers
management-client drain and active operations, not guest halt/reboot while its
CT is unpublished.

Required scenarios for a later implementation:

1. Halt with veth-down and post-stop delivered before CT construction, during
   preparation, between monitor registration/publication, and at console attach.
   Verify callback responses, one retirement/cleanup, stopped result, no stale
   run/host authority, no new start before admitted effects complete.
2. Repeat with target reboot: retain the old run's target, wait for pool readiness,
   start exactly once, and verify guest data survives. Halt must never autostart.
3. Drop each callback independently; simulate absent tty0, console close before
   post-stop, duplicate callbacks and already-stopped import. Confirm target
   remains explicitly unknown when lost; no manufactured reboot.
4. Fail config authentication/preparation/DB event/monitor/console attachment.
   Unblock waiters with failure; retain published authenticated run when required;
   preserve GC inhibition and reject foreign user/pool/CT requests.
5. Make saved veth/IFB live, absent, renamed, wrong kind, index/name reused or
   claimed by another netif/CT. Preserve safe refusal and taint; never delete a
   replacement. Inject IFB-success/veth-failure and persistence errors.
6. Interleave a fresh start or stale callback with old-run retirement. Old target,
   cleanup and exit fulfilment must not act on the next run. Test stopped state
   before final cleanup, and import failure/shutdown while callbacks wait.
7. Test old hook/new daemon and retained hook script/new symlink across userspace
   replacement; existing command fields and error envelopes must still work.
   If retries/durable intent are chosen, add daemon-unavailable, mid-acceptance
   crash, restart/replay and rollback tests with exact run identity.

A daemon-only in-memory rendezvous/state-recheck preserves current YAML and
hook schemas, can deploy node by node, and requires no coordinated all-node
update. It improves only the upgraded node and does not repair an already-lost
callback automatically. Rollback can load the unchanged persisted formats but
restores the original race; preserve any taint/ownership records. Running LXC
hooks can still be old scripts, so new hook fields cannot become unconditionally
mandatory for existing runs. Any durable intent addition must specify how older
daemons avoid losing or replaying it and how rollback retains pending reboot
intent; no such compatibility proof is supplied here. API/CLI diagnostic wording
and check selection belong to the other assigned packages.
