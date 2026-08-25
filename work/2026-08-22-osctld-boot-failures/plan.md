# 2026-08-22-osctld-boot-failures

## Goal

Make osctld restart and runtime vpsAdminOS upgrades preserve or safely recover
all container lifecycle operations. A restart must stop new starts, drain or
fence work already in flight while lifecycle callbacks remain available,
restart the daemon, adopt healthy running containers without disturbing them,
and resume unfinished desired work exactly once.

The implementation must be deployable onto already-running nodes. It must not
require a reboot, a coordinated fleet update, or a generic change to runit's
service semantics. This initiative changes feature branches and permitted
configuration pins only; it does not deploy any node.

## Affected repositories

- `vpsadminos`
  - adopt the reviewed container lifecycle-generation work from
    `2026-07-24-ct-start-hang`;
  - add daemon drain/readiness control and durable start intent;
  - reconcile existing runtime containers and incomplete generations before
    admitting new lifecycle work;
  - special-case osctld ordering in `switch-to-configuration` without changing
    generic runit behavior;
  - add focused unit and VM coverage.
- `vpsadmin`
  - install and refresh nodectld's osctld pre-stop hook as soon as remote
    control is available, rather than waiting for pool readiness;
  - consume the exact vpsAdminOS feature revision on the feature branch.
- `vpsfree-cz-configuration`
  - after both feature branches are committed and pushed, pin only the
    `staging`/`os-staging` feature inputs needed for review and CI;
  - do not deploy or activate the resulting configuration.

Historical scripts in `vpsfree-maintenance-tasks` are explicitly outside this
initiative and remain unchanged.

## Design

### Independent configuration and runtime state

Remove the ambiguous public container `state` and replace it with orthogonal
`config_state` and `runtime_state` values. `config_state` is one of `staged`,
`ready`, or `error`; `runtime_state` is `unknown` or an observed LXC runtime
state. Configuration and runtime observation errors have separate structured
diagnostics. A container may therefore be `config_state=error` while its exact
owned generation remains `runtime_state=running`.

New osctld and osctl interfaces emit only the split contract. Updated osctl,
osctl-exporter, and nodectld normalize legacy `state` responses during the
first runtime upgrade. Prometheus exports separate configuration and runtime
state sets; central rules accept both old and new metric generations while
nodes are upgraded incrementally. vpsAdmin continues to report the VPS as
running when its runtime is running, and reports configuration failure through
separate node health monitoring.

Persist `config_state: staged` for new staged containers and accept the legacy
`state: staged` key when loading. Runtime state is never persisted as current
truth: every daemon startup inventories LXC and exact lifecycle evidence before
admission. Runtime rollback remains unsupported after the new format is
written.

### Durable lifecycle ownership

Use the reviewed July lifecycle-generation series as the foundation. Every
start/stop run has a durable generation with its wrapper, LXC process, hooks,
effects, and terminal result attributed to that generation. A stale callback
cannot mutate a newer run. Startup first inventories live LXC processes,
cgroups, and durable generations, then correlates them with configured
containers before admission or autostart is enabled.

Healthy configured containers are rediscovered through LXC and adopted in
place with the same init PID, cgroup, network, console, and data. A configured
runtime whose ownership cannot be proven blocks readiness until it is
deliberately reconciled.
Only recorded generation processes may be terminated when drain escalation is
necessary. Escalation sends TERM before KILL and never kills the long-lived
wrapper or `lxc-start` manager of an already-running container merely because
a hook child is blocked. Live processes found in a configured container cgroup
without exact lifecycle ownership remain restart blockers through both
escalation phases; osctld reports them but does not signal them.

### Drain and direct service restart

Keep the existing osctld CLI supervisor. It captures daemon output/backtraces,
cleans management and user-control sockets after crashes, and forwards
`INT`/`TERM`/`HUP` to the daemon child. Both `osctl daemon prepare-stop` and the
daemon's `INT`/`TERM` handler enter the same idempotent drain coordinator;
prepare-stop drains without exiting, while a direct signal drains and exits.

Drain closes lifecycle admission and pauses every internal autostart plan
before callbacks or event services are stopped. Queued starts already have a
durable desired intent, so clearing an executor queue cannot lose work. Retry,
pre-start, post-start, and console waits are cancellation-aware. UserControl,
Eventd, lifecycle monitors, console handling, and generation finalizers remain
available until active operations finish or their exact generations are
fenced. The default natural drain is 300 seconds, followed by up to 60 seconds
for cleanup of an attributable generation. Unattributable live work blocks a
graceful restart instead of being killed heuristically.

Daemon pre-stop hooks are a checked restart barrier. A nonzero hook result
aborts preparation before osctld is stopped, runs the post-resume path while
admission remains closed, and reopens admission only after that path succeeds.
This makes nodectld pause failure visible to both direct service restarts and
configuration switches instead of continuing with an unsafe partial pause.
When drain escalation deliberately interrupts an exact lifecycle effect, its
failure is distinguished from an ordinary hook or command failure. The old
daemon keeps effect-ID validation, exact process discovery, interruption
marking, and signal delivery inside one lifecycle reducer fence, retains the
effect worker as a blocker until its real exit, and preserves the existing
durable desired state. It may then hand the resulting quiescent start, stop, or
cleanup state to startup reconciliation; the replacement daemon retries the
unfinished desired work instead of converting it into an opposite intent. A
managed launch whose start effect was released by the pre-start callback is
fenced by its exact starting phase and receives the same interrupted-start
marker. A stale blocker may neither mark nor signal a replacement effect or
generation phase. A successful
stop retains its completed cleanup effect and exact worker identity as a drain
barrier through compatibility artifact removal and replacement-start handoff.
If abrupt loss leaves a stopped compatibility run file after lifecycle
completion, startup recognizes its exact clean generation, removes the stale
file, and preserves any pending desired-running intent. An uncertain runtime
observation leaves that state untouched and blocks readiness instead of
guessing that the container stopped. Reload also clears only provably dead
terminal cleanup ownership before evaluating an incarnation change.
The complete startup import, live-cgroup inventory, legacy-handoff persistence,
and runtime network reconciliation sequence is itself a registered lifecycle
task. A direct restart during startup therefore waits for that exact startup
generation instead of racing teardown against partially imported state.

`sv restart osctld` remains an ordinary runit operation. The supervisor forwards
TERM and the daemon performs the same drain. The `sv` client may time out after
its normal short wait and print an error, but runsv does not then SIGKILL the
service: it waits for exit and starts it again. Operators can use
`sv -w 420 restart osctld` when they want the client to wait for the full drain.
Abrupt supervisor/daemon SIGKILL remains recoverable through durable startup
reconciliation.

### Configuration switch

Do not change generic `Service#start`, `#stop`, `#restart`, exit-status
handling, runit timeout policy, or configuration rollback. Only osctld is
removed from the ordinary restart loop when it is in the restart set.

For a new-daemon to new-daemon switch:

1. call `osctl daemon prepare-stop` while nodectld and lifecycle callbacks are
   still available;
2. if preparation fails before any service or activation change, call
   `osctl daemon resume` and abort the switch;
3. stop osctld and wait at most 60 seconds for its existing supervisor to exit;
4. abort before activation or other service changes if it does not stop;
5. perform the existing generic stop and activation phases unchanged;
6. start target osctld before the ordinary start/restart loop and wait at most
   300 seconds for `osctl daemon wait-ready`; target osctld runs its checked
   post-resume hook as the final fallible readiness step and thereby resumes an
   unchanged nodectld;
7. changed nodectld and all ordinary services continue through the existing
   start loop.

Failure after activation returns nonzero and leaves the resulting system state,
matching existing switch behavior. There is no automatic configuration
rollback.

For the first legacy-to-new runtime upgrade, feature-detect prepare-stop. When
it is absent, verify that the legacy daemon is initialized. When nodectld is
configured, atomically journal its exact PID, `/proc` start time, boot ID, and
`acquiring-supervision` phase before changing runit. Then create an owned runit
`down` file, request one-run mode, and advance the journal to
`supervision-held`. Both phases are recoverable. The owned `down` file,
boot-bound pause marker, and exact process identity survive a dead runsv
supervisor or configuration coordinator without allowing a replacement legacy
nodectld to open admission.
When nodectld is configured, pause it logically, then poll its status until
every queue worker and tracked subprocess has drained. When it is not
configured and no durable barrier exists, skip the nodectld-specific barrier
and idle wait.

Snapshot and cancel pending boot autostarts into the boot-ID-bound
`/run/osctl/upgrade-handoff.yml`. Persist the priority of queued and active
starts so a failed preflight or interrupted coordinator can requeue every
intent exactly once. The handoff also records the latest stable set of
RUNNING/FROZEN containers; this is narrow provenance for claiming exact legacy
network shapers during in-place adoption. Wait up to 300 seconds for legacy
nonterminal operations and wrappers to settle, including a 60-second stable
window. A preflight failure restores all proven queue and active-start state,
resumes nodectld, and aborts before activation. Unresolved inherited intent is
retained rather than silently discarded.

Classify legacy nonterminal work by direction: only `starting` and its
`aborting` cleanup enter the handoff's desired-start section. A concurrent
`stopping` operation is allowed to settle but never receives desired-running
intent, even when the container remains configured for autostart. While the
legacy daemon still reports that container as running, the handoff may list it
temporarily in the separate live-runtime provenance section; this cannot start
the container and is removed from the latest snapshot once the stop settles.

Treat same-boot handoff files as a strict interface: validate the complete root
and entry schemas, exact legacy-upgrade provenance, integer priorities, and
duplicate consistency in both the configuration coordinator and target daemon.
Malformed current-boot state blocks the upgrade and readiness; other-boot state
is ignored.

After activation, stop the exact recorded legacy nodectld even if its runsv
supervisor died. Open a pidfd first, then revalidate the persisted start time
and runit service-cgroup membership before signalling through that descriptor;
PID reuse can therefore neither redirect nor race the signal. A terminal or
zombie wrapper is not sufficient proof of service exit: the runit service
cgroup must also report `populated=0` (or have no tasks on cgroup v1), covering
the wrapper's daemon child and other live threads. Only then release the owned
`down` file and start the target nodectld. Its status must prove both logical
pause and marker awareness before target osctld is allowed to start. The
target osctld's post-resume hook defers legacy markers to the configuration
coordinator, so nodectld remains paused until `osctl daemon wait-ready`
succeeds. The coordinator then resumes nodectld, removes the marker, verifies
the currently supervised process is unpaused, and suppresses a redundant
ordinary nodectld restart. An interrupted switch can resume this state without
opening a transaction-admission window. All marker mutations share a file lock
and are conditional on the recorded same-boot reason, so an ordinary hook
cannot overwrite or clear coordinator, unknown, or malformed ownership.

### Runtime reconciliation and health

Startup readiness requires a two-pass inventory/reconcile sequence. For each
running container:

- preserve a healthy runtime unchanged;
- repair existing host-veth link, bridge, route, and shaper drift in place;
  remove only routes and filters carrying osctld's explicit ownership markers;
  claim an exact matching unmarked legacy route by replacing it with the
  marker; claim legacy CAKE/IFB state only for a handoff-attested live
  container and only when bandwidth, topology, and redirect filters match
  exactly; preserve and report all foreign or conflicting state without
  replacing it;
- if an enabled required host veth is absent, perform one controlled
  stop/cleanup/restart when desired state is RUNNING;
- treat a missing tty socket as degraded console state, not as a reason to
  restart the container;
- fence the configured container and keep the daemon not ready when ownership
  or repair cannot be proven.

Console registry locking covers only lookup/creation. Connection/retry
serialization is per container/TTY and cancellation-aware so one unavailable
socket cannot stall recovery of unrelated containers.

### Control and observability

Add:

- `osctl daemon status --json`;
- `osctl daemon prepare-stop`;
- `osctl daemon resume`;
- `osctl daemon wait-ready`.

Status includes daemon phase/readiness/admission, active container generations
and effects, pending desired intents, deadlines, failures, and orphans. Restart
defaults are natural drain 300 seconds, exact-generation cleanup 60 seconds,
and startup recovery 300 seconds.

## Compatibility and deployment

- The durable lifecycle records are additive to existing osctld state. The new
  daemon imports configured containers and live legacy runtime before enabling
  admission. No coordinated update of other nodes is required.
- The first legacy-to-new runtime transition is an explicit supported path and
  receives VM coverage. Mixed node versions are allowed because all APIs and
  records are node-local.
- The target activation coordinator uses Linux pidfds to signal a recorded
  orphan safely. Supported vpsAdminOS kernels provide `pidfd_open` and
  `pidfd_send_signal`; lack of either facility fails the switch closed before
  the replacement service is started.
- Runtime rollback is deliberately not supported after the new daemon has
  written lifecycle-generation state. The operator must finish the upgrade or
  repair the new version; this is accepted to keep the recovery contract
  unambiguous.
- New routes use protocol 230 (`osctld`) and shaping filters use reserved
  handles as ownership markers. A locally configured foreign route or filter
  which deliberately reuses those markers can collide with reconciliation;
  this residual risk is documented and the markers must remain reserved for
  osctld on managed nodes.
- When nodectld is configured, it must tolerate a bounded osctld outage. Its
  hook installation timing changes compatibly and does not alter the inter-node
  protocol. A target configuration that contains nodectld must contain the
  marker-aware version together with, or before, the new legacy-upgrade
  coordinator. The first switch enforces this ordering at runtime with an owned
  runit `down` file and an explicit target status capability check before
  osctld starts. A legacy marker is not resumed by the target daemon hook; only
  the coordinator which observed osctld readiness may clear it.
- Configuration consumers are updated only after exact feature commits exist.
  Feature pins may be pushed for CI/review, but no production deployment or
  activation is part of this initiative.
- `killMode` is not relied on for container survival: container payloads are in
  separate cgroups. Safety comes from lifecycle ownership and reconciliation.

## Testing plan

Quick unit/spec coverage will exercise drain state transitions, signal/API
convergence, admission rejection, cancellation-aware queues and sleeps, durable
autostart intent, exact-generation escalation, legacy handoff, veth repair,
console lock granularity, readiness/status output, and supervisor behavior.
It will also exercise split-state persistence and legacy normalization,
configuration failures alongside live runtime, event compatibility, osctl and
nodectld runtime decisions, exporter output, and mixed-generation Prometheus
rules.

RSpec-style vpsAdminOS VM scenarios will cover:

- legacy-to-new runtime upgrade preserving init PID, cgroup, veth, routes,
  console, and data;
- legacy upgrade with a blocked start and configuration coordinator SIGKILL at
  the durable handoff boundary, followed by a successful retry;
- direct `sv restart osctld`;
- configuration switches with nodectld changed and unchanged;
- missing veth, repairable route/bridge/shaper drift, failed ownership
  reconciliation, and parallel missing tty sockets;
- nodectld refusing the checked pause barrier, followed by a successful retry
  which proves osctld and all running containers were left untouched;
- nodectld stopping before legacy preflight and restarting after a successful
  pause, including a SIGKILLed runsv supervisor and orphaned exact legacy
  process, proving the boot-bound marker keeps transaction admission closed;
- coordinator loss after the runit hold but before the journal advances,
  followed by supervisor replacement and recovery using only the previously
  recorded exact process identity;
- a legacy autostart-configured container blocked in `stopping`, proving the
  handoff excludes it and the target daemon leaves it stopped;
- direct osctld restart while startup reconciliation is still active;
- exactly-once resumption of boot autostarts after interrupted starts;
- direct osctld restart while a local state copy is stopping its source,
  proving that restart escalation preserves and resumes the desired stop before
  the copy is retried and its data is verified.
- split local copy and remote send/receive across daemon restarts, including
  explicit `config_state=staged` and `runtime_state=unknown` assertions and a
  no-consistency clone whose source must be preflighted before mutation.

After intended changes are committed and quick checks pass, run the mandatory
fresh-agent change review and address significant findings before long VM
tests. The long vpsAdminOS gate includes `osctld/restart`,
`osctld/resilience`, `osctld/lifecycle`, `system/switch-to-configuration`,
`declarative-containers`, `osctl/ct-local-transfer`, and
`osctl/ct-send-recv`; the vpsAdmin gate includes `vps/migrate` and
`vps/autostart-monitoring`. Push feature branches and use GitHub Actions as a
feedback loop. Do not deploy nodes.

## Explicit exclusions

- no generic runit service or `switch-to-configuration` rollback redesign;
- no removal of the osctld CLI supervisor;
- no production or development-node deployment;
- no reliance on production-system access;
- no runtime downgrade from the new lifecycle format.
