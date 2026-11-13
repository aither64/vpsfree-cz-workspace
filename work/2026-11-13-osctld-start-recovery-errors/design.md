# Start admission diagnostics and shutdown/import recovery

Design owner: architect0. Source baseline: vpsadminos
`c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`. Scope comes from [plan](plan.md)
and the lead's explicit addition of foreground error propagation. The supplied
[incident](incident.md) is not an independently reproduced execution trace.

## Release boundary A: accepted by lead, implementation released

The lead accepted this boundary and released implementer0 at 22:41 UTC on
2026-11-13. Subsequent proposal work below does not change A.

Implementer0 owns the entire diagnostic implementation, tests, technical docs,
quick checks, hooks/index/commits and later review fixes. No other member edits
these files. Lead owns the prose pass before commit. Architect0 owns this design.
The broader race proposal below is independent and does not block A: A changes
explanation of existing decisions, never admission, cleanup or lifecycle policy.

### Files and interfaces

- `osctld/lib/osctld/container.rb`: retain `can_start?` as the public Boolean
  predicate. Add a small read-only reason helper (recommended name
  `start_block_reason`, returning nil or String) that represents the same five
  gates, in their existing order. Derive the predicate from that decision or
  share one private decision helper; avoid competing truth tables. Keep expensive
  explanation out of successful starts and autostart predicate checks.
- `osctld/lib/osctld/commands/container/start.rb`: replace the generic rejection
  at the existing first line of `start_now` with the reason. Keep this check
  ahead of the starting/running no-op, `force` handling and every Start side
  effect. No gate moves in Restart or Boot.
- If needed, `osctld/lib/osctld/net_interface/manager.rb`: a small read-only
  snapshot/helper for affected interface names and existing host-link tuples.
  Do not change Veth identity/cleanup behavior. Use existing synchronized readers;
  do not acquire the global host-link registry inside a held container lock.
- `osctl/lib/osctl/cli/container.rb`: foreground start/restart/boot capture a
  failed response, close the console client as today, allow `open_console` to
  finish waiting and restore the terminal, then raise `OsCtl::Client::Error`
  with the original message. Do not raise from the callback while the terminal
  is raw. Share a small helper if useful; retain the existing success path.
- Focused existing specs under `osctld/spec/osctld/commands/container/`,
  `osctld/spec/osctld/container/`, `osctl/spec/osctl/cli/container_spec.rb` and
  `osctld/spec/osctld/commands/container/lifecycle_spec.rb`; add a focused
  admission spec if needed.
  `osctl/man/man8/osctl.8.md` holds operator explanations; a short existing
  `docs/osctld/interfaces.md` clarification is optional if useful. No new subsystem.

Detailed source/consumer/check inventory: [contracts-checks](contracts-checks.md).

### Required reasons and safe advice

| First failing gate | Explanation and next step |
| --- | --- |
| `state == :staged` | Container is staged and preparation/import has not completed. Inspect the originating operation; complete it before retrying. Do not suggest forced start or state-file editing. |
| `state == :error` | Container has a configuration/runtime error. Inspect `osctl --pool POOL ct show ID`, assets where relevant, and daemon logs. Recovery taint cleanup cannot repair unrelated configuration/runtime errors. |
| Container recovery taint | Previous cleanup could not establish a safe released state. Identify the container and any currently tainted interfaces/recorded identities; inspect daemon logs for the original failure. |
| Network-interface recovery taint | Identify affected configured interfaces and available recorded host-link name/ifindex/IFB metadata. Explain that retained ownership blocks start until guarded recovery succeeds. |
| Pool not active | Name the pool and its current state; inspect pool status and osctld import/export logs before retrying. There is no pool-enable CLI; disabled state can result from export or failed import. |

The first reason follows the old short-circuit order. Tests exercise all five
gates independently and a multiple-blocker case. Combined taint explanation may
include both container and interface facts without hiding the first gate.

There is **no persisted recovery issue list** in this baseline. Do not invent one,
turn asset validation errors into historical cleanup causes, or add a new schema.
Available facts are the container flag, affected netif names/types/taint and
recorded host-link tuple. Explain missing detail honestly and point to existing
logs. Diagnostic formatting must not issue netlink/ZFS/LXC queries or mutate state.

For taint, suggest inspection first. `ct recover state` is an active reconciliation
command, not a read-only inspection command. Only after verifying the container
is stopped and understanding leftover resources should the operator attempt
ordinary `ct recover cleanup` without force. If a stale ownership record remains
and **both recorded name and ifindex are absent**, including IFB where recorded,
`ct recover forget-host-link ID INTERFACE` is the existing explicit privileged
acknowledgment; then run cleanup. The command independently rechecks stopped
state, ownership and absence and may refuse. Never imply a missing name alone
proves absence, advise forgetting a live/reused link, or recommend `--force`,
manual YAML edits, network deletion, reboot or draining other containers as a
routine escape. The incident's successful two commands are conditional evidence,
not a universal remedy. Keep concise error text and detailed conditions in the
existing recovery man-page section.

### Invariants, compatibility and non-goals

- Every preexisting `can_start?` true/false result stays unchanged. `--force`
  cannot bypass any gate. Running/starting no-op still follows admission.
- Normal restart and custom boot use the common Start message through
  `call_cmd!`. Boot already prepares an image/stops the CT before reaching Start;
  this package does not claim to remove those earlier effects. Guest
  `restart --reboot` uses another path and is unchanged.
- The wire error remains `{status: false, message: String}` and the client
  exception remains the existing class. Change only the human-readable message;
  no error code, JSON field, API/generator, hook protocol or state-schema change.
- Queue/autostart filtering and asynchronous acknowledgment remain unchanged.
  `--queue --no-wait` success acknowledges enqueueing; it cannot promise an
  immediate later start rejection. The existing JSON/raw-console path does not
  invoke the operation block; this package does not redesign raw console behavior.
- Do not change host-link ownership (name, ifindex, kind, host boot identity,
  owner claims), recovery checks, taint persistence, import, stop handlers,
  callback routing, start generations, run IDs, or shutdown/reboot intent.
- Old/new clients accept the same envelope; mixed daemon versions differ only
  in message detail. No database/API/CLI option/Nix module change or migration.
  Rolling userspace update is sufficient; all nodes need not update together.
  Rollback loads the same state and returns older messages. No deployment is
  authorized by this brief.

### Acceptance and verification

Quick checks, in repository Nix environments, must establish:

1. All five gate reasons, nil/success, and first-gate order using real predicate
   behavior; aggregate taint with and without available interface metadata.
2. Both force values fail before Start mounts/cgroups/run initialization/spawn;
   starting/running no-op is still subordinate to the gate.
3. Existing normal restart/boot forwarding retains the daemon message; foreground
   start/restart/boot surfaces the exact response after console cleanup/terminal
   restoration, while successful foreground behavior remains successful.
4. Error remains the same string-valued wire/client contract; no diagnosis path
   invokes cleanup, forget, external queries or persistence.
5. Existing recovery/host-link protection specs pass, including absent/reused
   identities and stopped-state requirements. Update the exact old generic-string
   expectation in `lifecycle_spec.rb` without weakening its safety assertion.
6. Required Overcommit checks and documentation factual/prose pass, then commits.

Implementer0 selects the focused spec commands from [contracts-checks](contracts-checks.md),
reports exact command/revision/result and gaps, and refreshes packaged metadata
under repository rules (record an empty result if unchanged). Longer tests run
only after the completed committed change's mandatory independent review. Use the
fresh watcher for uncertain/long commands. The lead selects the proportional
existing lifecycle/recovery VM and Ruby check batch from that inventory; no
production reproduction is required to validate message-only admission changes.
Stop unexpected local kernel builds under the workspace procedure. Final review
must explicitly conclude whole-branch history and no migrations. Publication,
integration approval and any later deployment remain lead-owned separate phases.

## Race diagnosis and proposal: complete, implementation not released

Accepted evidence inputs are [race-evidence](race-evidence.md),
[July comparison](july-comparison.md), and [contracts-checks](contracts-checks.md).
Their exact revisions, function/test locations and limits are authoritative
evidence inventories; the design does not repeat the full histories.

### Diagnosis and July comparison

At the baseline, user-control sockets exist before ordinary CT loading.
`Pool#load_container` publishes ordinary CTs only after configuration preparation,
state sampling, monitor registration and console attachment. `VethDown` and
`CtPostStop` first look up the published CT and its owner. A callback in that
window can therefore fail before performing teardown. The supplied timing and
missing normal execution log fit that explanation. The exact reply, publication
time and shutdown initiator remain unproved; no production query or reproduction
was performed. The later changed-link, retained-ownership and taint errors match
the deployed fail-closed checks.

July OS head `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44` and admin head
`807e9d7f1277217d3cf2d49b7c4b2525dc441c10` were compared read-only. Neither exact
head is an ancestor of its observed remote default. July adds durable accepted
intent, exact generations, leased callbacks and cleanup-before-replacement, but
still rejects callbacks before CT lookup succeeds. Its stopped-run reconstruction
uses saved reboot state: it cannot infer an unseen `LXC_TARGET=reboot`.
Its older name-based networking lacks the baseline's persisted ifindex/kind/boot
ownership and recovery-taint protection. Do not import that lifecycle branch or
treat its successful starts as proof of safe handling of this incident.

### Recommended scope and alternatives

Recommend a **per-run terminal outcome record plus import reconciliation**, with
a small readiness rendezvous for callbacks delivered during import. Keep the
current cleanup and host identity mechanisms. This addresses two separate gaps:
admission during import and retaining a target while no daemon can accept it.
An outcome means an observed hook target, not proof that LXC teardown or cleanup
has completed. A reboot either produces one safely admitted successor or remains
explicitly pending/blocked; it must not silently become a halt.

| Alternative | Benefit | Missing guarantee / decision |
| --- | --- | --- |
| Earlier `DB.add` alone | Small diff | Exposes incomplete authority or races monitor/console attachment against retirement; does not cover callbacks before publication or daemon downtime. Reject as a complete fix. |
| Readiness plus final state recheck only | No durable schema change; repairs callbacks still waiting during import | Lost reboot target remains unknown when socket/hook is gone. Acceptable only as a separately scoped partial improvement with that limit. |
| Bounded hook retry | Keeps target in a live hook process during a short outage | Finite expiry, process death and crash after acceptance still lose intent; safe replay still needs exact launch binding. Not the full solution. |
| Narrow durable terminal record, readiness and reconciliation | Retains exact target across daemon restart and fences replacement behind cleanup | Requires new-run hook identity, crash-safe state and rollout/rollback proof described below. Recommended future package. |
| July's complete reducer | Covers more admitted lifecycle concurrency | Much broader scope and incompatible assumptions about newer host-link/impermanence contracts; still lacks prepublication target capture. Reject for this task. |

### Required terminal-record contract

1. Before each supported launch, register an immutable, root-owned identity:
   pool, CT, owning user, exact run ID, host boot identity and a unique launch
   token. Preserve the old run's resource/cleanup references separately from
   `config.yml`, which `RunConfiguration#destroy` currently unlinks on retirement.
   Bind the hooks to this launch when LXC starts; never discover identity later
   from whichever run configuration happens to be current.
2. The post-stop hook writes its validated `stop` or `reboot` target to that
   launch's outcome slot **before** contacting the daemon. Unknown/malformed
   targets stay unknown/error; a missing record never implies halt or reboot.
   Identical duplicate writes are harmless; conflicting targets fail visibly.
   A daemon-independent writer is necessary for the blackout case.
3. Use a root-authoritative registration and a separate narrowly writable
   per-run target slot, with no authority derived from hook-supplied paths,
   owner IDs or resource tuples. A hook writer gets no more authority than the
   existing owning-user socket. The reader must bound and validate input and
   reject symlink/replacement/cross-owner records. Hook bytes are only intent;
   authenticated CT/run lookup and fresh state authorize later effects.
   Exact filesystem mode/atomic-write mechanics require a focused prototype
   before future implementation release; an arbitrary user-writable JSON spool
   with trusted self-declared owner/run fields is not this design.
4. Store outcome/consumption/cleanup/successor state independently of the
   current-run pointer. Atomic replacement and appropriate file/directory sync
   must establish the crash boundaries. Recommended lifetime is the existing
   host-boot runstate under `/run/osctl/pools/<pool>/`: it survives daemon
   replacement, not host reboot. Bind/check boot identity and never replay a
   previous host boot's guest reboot after host restart. This is explicitly a
   same-host-boot guarantee, not persistent desired-running state across power loss.
5. The daemon first authenticates the original owner, registered launch and
   retained run/resource evidence, then commits terminal acceptance before
   retirement. Distinguish recorded, accepted, cleanup pending/blocked, successor
   reserved and completed. A consumed marker must not discard unfinished cleanup
   or mean success. Do not acknowledge callback effects before their actual
   completion; durable recording while unavailable is a separate result from
   successful daemon handling.
6. On reboot, cleanup completion and pool readiness precede a durable reservation
   of one successor run. Normal Start joins/observes that reservation; duplicate
   callbacks/restarts do not create another successor. A newer explicit Stop
   durably cancels a pending reboot for that exact predecessor. A crash around
   spawn must reconcile the reserved successor with real launch/process evidence;
   an uncertain spawn does not authorize a fresh second launch.
7. Keep external user-hook execution distinct from idempotent internal cleanup.
   A crash during a non-idempotent user hook can leave its outcome unknown;
   record and expose that state instead of promising exactly-once arbitrary
   external effects or replaying blindly. Retain cleanup obligations and block
   unsafe replacement until the supported recovery path resolves uncertainty.

Current run IDs identify runs but are not caller credentials. New exact launch
binding must cover both managed Start and supported direct `lxc-start`:
`ct_pre_start` currently creates the direct run after LXC has read its config.
Do not silently attribute an unbound direct-start callback to a newly current
run. Proving a supported direct-launch binding is a future release dependency;
otherwise direct starts need an explicit legacy coverage boundary, not a false
full-guarantee claim. The root-owned registration/slot and hook delivery prototype
are open implementation choices, not authorization for a new privileged service.

### Import admission and cleanup invariants

- Establish readiness for the known pool/CT import set before callbacks can
  fall through missing-DB lookup. Waiters hold no DB, registry, container,
  configuration or manipulation lock. Import failure, daemon shutdown and
  bounded wait expiry resolve visibly. Unknown CTs and foreign owners still fail.
- Only publish/use a fully authenticated owner, installed netif manager and
  exact retained run. Serialize original-run retirement with monitor/console
  attachment; recheck authoritative state and queued outcome after attachment.
  Do not re-create a run or stamp it running after a concurrent accepted stop.
  Preserve the special authenticated impermanent-root import path and its
  garbage-collector inhibition on uncertain import.
- Stop callbacks carry the immutable launch identity. Late/duplicate callbacks
  for a retired run cannot mutate a successor's AppArmor/BPF, network interfaces,
  run pointer, hooks or exit promise. Veth-down also validates configured netif
  ownership and the existing kernel tuple. Readiness is not an authentication
  bypass; record-only intake before publication cannot grant effect authority.
- Reconcile an imported stopped run even when the original cached state was
  already stopped. `recover_state` currently skips that path when states agree;
  simply calling it is insufficient. With missing target, cleanup may be safe
  but automatic reboot is not justified. Keep the unresolved target explicit.
- Reuse the current host-link checks: saved name, ifindex, kind, boot, owner
  registry, cross-record claims and IFB identity. Kernel/query/persistence errors
  preserve ownership and taint. A terminal target alone cannot authorize deletion
  or forgetting. Deletion/partial completion must remain durably attributable
  to the old run before another run receives ownership.
- In particular, keep same-boot absent/reused links fail-closed. The proposal
  does **not** turn `forget-host-link` into automatic reconciliation. If LXC
  removed a link while the daemon was unavailable, retained ownership can still
  require existing stopped/no-init, both-name-and-index, IFB and owner checks plus
  explicit privileged acknowledgement and full cleanup. Preserve the pending
  reboot through this blocked state. A future automatic absence-release policy
  is a separate consequential design change, not needed for honest diagnostics
  or retained intent, and is not released here.

### Proposed file boundary and future release gate

One future implementation package should own the coupled hook/run/import/cleanup
contract; do not split interface ownership prematurely. Candidate paths are
`osctld/hooks/{ct-post-stop,veth-down}`, `templates/ct/config.erb` and netif hook
templates, `container/{lxc_config,run_configuration,stop_handler,recovery}.rb`,
`pool.rb`, user-control stop/pre-start admission, and the narrow Start/Stop checks
needed for terminal fences/successor cancellation. A focused terminal-record
helper is preferable to a replacement general lifecycle subsystem. Include
matching unit specs, `tests/suite/osctld/{restart,resilience,direct-start}.nix`,
maintained recovery/compatibility documentation and any required registration.

This future package has **no assigned execution owner and is blocked on new
scope authorization and lead allocation**. Architect0 owns this proposal only.
Before release, settle root registration/write authority and crash persistence,
actual immutable LXC hook binding for direct/managed launches, legacy admission,
explicit-stop precedence, and a rollback fence. These are relevant contracts,
so they cannot be deferred to keep an implementer busy. Current A is unaffected.

### Regression and verification plan for the proposal

Use deterministic barriers in unit tests; use a VM for actual LXC hook behavior
and process/socket blackout. No tests below have been run by package D.

| Case | Required observation |
| --- | --- |
| Halt and reboot at pre-construction, preparation, monitor registration, publication and console attachment | Exact original target/run retained; halt stays stopped; reboot waits for cleanup/import and produces one successor or a visible durable blocker. |
| Socket unavailable; crash before/after outcome write, acceptance, retirement, each cleanup stage and successor reservation/spawn | No lost accepted target, no false completed cleanup, no duplicate/guessed successor; incomplete writes fail closed. |
| Callback delivered twice, wrong owner/boot/run, conflicting target, stale callback after successor | Rejection/no foreign or successor effects; same exact duplicate is idempotent. |
| Fresh Stop or Start races guest reboot | New Stop cancels the pending reboot; Start shares or follows the exact reserved successor after predecessor cleanup. |
| Link/IFB matching live, absent, renamed, reused by name/index, wrong kind or shared claim; failed kernel query/save | Existing guards and explicit acknowledgement survive; no replacement-link deletion or false taint clearing. |
| Import/config authentication, publication event, monitor or console failure | Waiters resolve, ownership remains knowable, authenticated impermanent run/GC protections preserved. |
| Post-stop before full teardown, each callback independently lost, console absent/early close, already-stopped import | No premature cleanup/replacement; unknown target never inferred from final stopped state. |
| User post-stop hook crash | Indeterminate external effect is visible; no unsupported exactly-once claim or blind replay. |
| Old/new hook and daemon combinations, direct start, ordinary and impermanent/custom boot, rollback attempt | Explicit supported/degraded behavior; old daemon cannot bypass unresolved terminal obligations. |

Quick checks: terminal record/parser/permissions and crash-boundary specs; pool
import and stop-handler specs with barriers; existing identity/recovery specs;
template/hook argument tests and required Overcommit. Then all intended changes
committed and independently reviewed before a watcher runs VM halt/reboot during
real daemon downtime/import, direct-start binding, and resilience cases. Verify
a known guest payload survives reboot/custom-root cases. A full lifecycle rewrite
or broad benchmark campaign is not a prerequisite. Stop at a reproducible failure,
fix its owning contract, and rerun only affected checks before the next VM batch.

### Compatibility, deployment cost and recovery

Unlike A, this proposal adds a versioned runtime sidecar and exact-run hook
contract. Management/API envelopes, database schemas, Terraform/generated clients
and kernel configuration need not change. Old unbound hooks must remain explicitly
legacy; a new daemon must not pretend they supply exact-run evidence. Old daemon
ignoring a new sidecar is **not safe rollback** even if old YAML still parses.

Deploy node by node with new daemon/readers before enabling new launch bindings.
Already-running legacy LXC processes cannot be assumed to acquire immutable
per-run identity merely because the shared hook symlink changed. Full protection
requires newly bound runs or a separately proven live handover. There is no
reason to update all fleet nodes simultaneously; broad immediate coverage would
cost planned per-CT restarts. Prefer incremental adoption because evidence does
not justify that fleet disruption for this incident.

Rollback must refuse while new-format runs, pending targets, uncertain cleanup
or successor reservations remain unless an independently verified compatibility
reader/fence exists. The conservative path is finish/reconcile affected runs
under the new daemon, preserve all ownership/taint, verify terminal obligations
complete, then downgrade with legacy hooks for future launches. Never discard
pending records to make downgrade pass. Host reboot uses its separate boot/auto-
start policy and must not replay a prior boot's terminal record. This is a future
operational contract, not an instruction to deploy, drain, reboot or downgrade now.

## Package D evidence and completion

Architect0 verified the bound session/environment, live same-session roster and
baseline worktree head; read required workspace/repository procedures, source and
the accepted B/C/E evidence. Commands were bounded `rg`, `cat`, `sed`, `git
rev-parse`, `git status`, roster and same-session clarification/report calls.
Only this design file was edited. No application code, hook/index, old-session
record/ref, production machine or lifecycle state was changed. Tests and runtime
race reproduction remain unperformed; source reasoning is not runtime proof.

The diagnostic brief is accepted and executing; the race recommendation is ready
for lead acceptance with its explicit future release dependencies. Findings are
sufficient for this requested proposal; no production logs are needed to choose
these boundaries. Lead owns implementation acceptance, final review/checks,
tracking commits, publication and any future scope decision.
