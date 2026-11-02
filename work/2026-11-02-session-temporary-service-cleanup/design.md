# Session temporary service cleanup

**IMPLEMENTATION AUTHORIZED / NOT YET VERIFIED — 2026-11-02.** The user directed
implementation and allowed aitherdev deployment through vpsfree-cz-configuration.
Default-branch integration and session lifecycle actions remain unauthorized.
The execution contract below supersedes provisional API/storage choices in the
earlier proposal. Architect work remains design-only; implementers own code.
Scope amended by the user: "let's not handle existing unregisteredservices."

## Frozen execution contract (implementation kickoff)

Reconciled against feature base `c2182254d29c4175c3e9fe4267e5a92dd1da6b79` in
`worktrees/2026-11-02-session-temporary-service-cleanup/dev-workspace`. The relevant
archive/delete order and reader boundaries match the inspected installed source:
fresh archive still prunes at `libexec/dev-session:2134` before journal creation;
delete already publishes its removal journal before worktree removal. No scope
expansion is needed. Use `nix/workspace-portal.nix` for packaging (there is no
`nix/package.nix`). This section freezes A/B interfaces; implementation-private
details may vary without changing the persisted/public contracts or invariants.

### State and ownership (A owns the writer and shared Ruby validator)

Implement `libexec/workspace-session-services.rb`, module `WorkspaceSessionServices`.
Use the existing workspace ID formula: basename + `-` + first 16 SHA256 hex digits
of the canonical workspace root. All JSON below is strict, atomically replaced,
fsynced, private mode 0600, with owner-only directories and ordinary symlink/path
validation. UUIDs are lowercase canonical UUID strings; lifecycle IDs remain the
existing 64 lowercase hex characters. Bound registry/projection to 1 MiB and 256
resource records; refuse new launches before those bounds, never truncate ownership.

| File | Frozen schema-1 fields |
| --- | --- |
| `worktrees/.locks/<slug>.services-registration.json` | `schema`, `workspace`, `slug`, `registry_id` (UUID), `retained_thread_id` (nullable), `tracking_identity` (`dev`, `ino`), `state` (`initializing` or `ready`), `created_at`. First-registration marker only; no coverage/audit semantics. |
| `<state-root>/session-services/<workspace-id>/<slug>.json` | `schema`, same ownership fields, `revision` (monotonic integer), `activity_token` (UUID), `resources` (array). Each resource: `id`, `label`, `unit`, `description`, `argv`, `cwd`, `request_sha256`, `phase`, `created_at`, `updated_at`, `boot_id`, `manager_uid`, `invocation_id` (nullable until observed), `control_group` (nullable until observed), `stopped_at` (nullable), `retired_at` (nullable), `error` (nullable `{code,message}`). No persisted arbitrary environment dump. |
| `worktrees/.locks/<slug>.services-cleanup.json` | `schema`, `workspace`, `slug`, `registry_id`, `retained_thread_id`, `tracking_identity`, `operation` (`archive` or `delete`), `operation_id`, `mode` (archive policy, otherwise null), `force` (delete boolean, otherwise null), `automatic` (boolean), `resource_ids` (sorted frozen UUIDs), `phase` (`services_pending` or `services_stopped`), `created_at`, `updated_at`. Maximum 64 KiB. This is a subordinate lifecycle prelude, not a new public lifecycle command. |

Resource phases: `starting`, `running`, `stopping`, `retired`. Observation failure
or failed application exit does not retire a record; record a safe error/live state
in the projection. `retired` requires verified empty cgroup, settled jobs and
removed transient unit. Resource IDs and generated unit names are never reused.
This makes a separate revival epoch unnecessary: retain the registry identity and
old retired records, and allocate new UUIDs for new launches after ordinary revival.
The existing root plus tracking-directory identity binds the session; archive/revive
rename preserves that directory. A different root/incarnation must not inherit
live or uncertain entries. Successful delete transfers marker/registry to its
existing private removal recovery before clearing active ownership; retry uses the
same journal. Do not introduce a new history collector or quota eviction policy.

First launch writes an `initializing` marker, then registry/launch intent, then
durably changes the marker to `ready`, then contacts systemd. Both files absent
means an untouched session. Either present establishes expected registration;
a missing counterpart, identity mismatch or corrupt state refuses destructive
cleanup. A failed first initialization may complete the same marker's empty
registry only while it still says `initializing`, which forbids a systemd attempt.
A `ready` marker never resets or repairs a lost registry as empty. Reuse any
existing valid initialized registry instead of replacing it. No unit scan/adoption repairs loss.
All service-only scratch files remain inside ordinary session-owned file boundaries.

Generate `workspace-session-<resource UUID>.service` and a nonsecret Description
binding `registry_id` + resource ID. Enforce Type=exec, Restart=no,
RemainAfterExit=yes, KillMode=control-group, SendSIGKILL=yes, TimeoutStopSec=15s.
Do not auto-collect before cleanup. Existing stop design remains: bounded native
TERM→KILL, job/unit identity and descendant-cgroup proof, then exact unit retirement.
A missing unit with unobserved cgroup after an uncertain launch is not enough proof;
positively reconcile native ownership/absence or leave registered state blocked.
Bound systemd calls/observation to at most 20 seconds per resource and report partial
progress. No process/port matching, custom stop hooks, external routing or discovery.

### CLI, locks and the Ruby seam

Freeze public verbs `service run`, `service list`, `service stop`, with the proposal's
session arguments. `run` also accepts optional `--id UUID` for exact-request replay;
without it allocate an ID before intent. Reusing an ID with a different label/cwd/
argv digest refuses; an existing attempted launch is reconciled/reported, never
blindly relaunched. `list --json` is the portal interface. `run`/`stop --json` may
return that same projection after the action. No inventory/adoption/restart API.

Use transition SH with post-acquisition generation validation, then existing
creation and session EX locks for run/stop/lifecycle writes. A's Runner integration
owns lock acquisition; the service Store does not nest those locks. `list` uses
existing session observation SH nonblocking admission and a bounded read. Exit 75
means busy (no JSON); malformed ownership/state returns nonzero; transport/native
status failure with intact registry returns known membership and unknown live state.
Archive/delete may call the Store while already owning their lifecycle locks.
Reads never initialize records or write reconciliation/progress/activity metadata.

Shared Ruby seams (A implements; B calls the pure validator from workspace-host):

- `WorkspaceSessionServices.paths(workspace:, state_root:, slug:)` returns marker,
  registry and prelude paths; path computation never creates them.
- `WorkspaceSessionServices.requirements(workspace:, state_root:)` returns
  `{required: Boolean, pending: Array}` after strict file/identity validation.
  `required` means nonretired/uncertain registration or a cleanup prelude; unknown
  state raises. `pending` contains validated prelude slug/operation/ID summaries.
  Marker/registry presence must be checked in both directions, not one glob only.
- `WorkspaceSessionServices::Store.new(workspace:, state_root:, slug:, runner:)`
  uses the existing command-runner interface. Public collaborators:
  `run!(id:, label:, cwd:, argv:)`, `stop!(id:)`, `public_status`,
  `prepare_cleanup!(operation:, operation_id:, mode:, force:, automatic:)`,
  `cleanup!`, `verify_clean!`, `handoff_cleanup!(journal:)`.
  Runner supplies verified session identity; Store never invents it from slug/CWD.
  Internal method decomposition is A's choice; keep paths/requirements/public JSON stable.

### Public JSON (A emits; B consumes without reading private registry)

`list --json` returns exactly this schema-1 envelope (optional values use null):

```json
{"schema":1,"workspace":"/canonical/root","slug":"SLUG","registryId":null,
 "registered":false,"count":0,"countKnown":true,"observedAt":"RFC3339 UTC",
 "services":[],"history":[],"cleanup":null,"notice":null}
```

Each `services`/`history` row has `id`, `label`, `phase`, `state`, `observedAt`,
`retiredAt`, `error`. `state` is `starting|running|exited|failed|stopping|stopped|unknown`;
it is an observation, not readiness or permission to prune. `error`/`notice` are
null or `{code,message}` with bounded, explicitly safe messages (not raw stderr).
`cleanup` is null or `{operation,operationId,phase}` from the verified prelude or
matching active lifecycle. `services` contains nonretired entries; `history`
contains retired entries and does not contribute to `count`. An intact registry
means `countKnown:true` even if unit observations fail. No marker/registry gives
the empty envelope without probing systemd. Known-state corruption is an error,
not empty JSON. Busy/read failure makes B preserve a visibly stale snapshot or
show unknown, never synthesize zero. Do not expose argv/cwd/unit/cgroup/environment.
B wraps the call in existing exact-session/profile/incarnation checks before and
after reading, like coordination; uses the same accepted snapshot for page/count.
Archived sessions return retained history without probing retired units.

### Lifecycle handoff and package compatibility (A/B joint contract)

For fresh archive, after normal authorization/preflight and the final automatic
eligibility check, allocate/reuse the accepted operation ID, publish/fence the
prelude, stop/verify all entries, and mark `services_stopped` **before pruning**.
Then create the unchanged ordinary archive journal/sidecar with that exact ID.
Delete uses its already published removal journal ID and guards first file removal.
After validating matching ordinary journal identity, remove the prelude; that
journal retains admission ownership. A crash between journal publication and
prelude removal permits both only when operation/ID/mode agree and deletion's
force setting follows its existing authorized false→true retry rule. A prelude
alone resumes via the original archive/delete command, retaining saved policy.
No service state means the old path without a prelude. Validate known registrations
and require verified retired state before every remaining destructive phase on retry.
Old journals keep their exact schemas, phases and sealed file/Git proofs; add no
fields to them and do not rerun an older tracking prune. They receive only the
registered-resource guard before any remaining deletion. No unregistered-resource gate.

A wires prelude ownership into Runner conflicts/admission, archive-check and
automatic-worker own-operation recovery. B wires it into Go PendingLifecycle/
Progress/receipt identity and host unfinished-operation scanning. Do not append a
second mapping for archive/delete to `lifecycleJournals` (the current contract
requires unique command mappings). Treat this suffix explicitly, like the existing
archive-cleanup sidecar; pending+ordinary same-ID is one operation. Prelude progress
evidence excludes `phase`/`updated_at` and deletion's authorized `force` upgrade;
other immutable identity must remain stable.
Creation, revival, cluster/provider admission and package paths must honor its
pending fence; ordinary status reads may show it, never finish it. Publish the
existing coordination lifecycle fence atomically with prelude intent using the
existing bind callback; preserve worker ownership before stopping on automatic runs.

B adds runtime keys `sessionServicesStateSchema: 1` and
`sessionServicesLifecyclePolicy: 1`. Host selection **and candidate activation**
call A's strict requirements validator: pending preludes block package transition;
live/uncertain state requires both matching keys; unknown/missing known state
refuses. Fully retired records without pending recovery impose no new capability
gate, but remain retained and must not resurrect on rollback/revival. No records
means no gate. Preserve post-lock stale-generation refusal and selected recovery
paths; do not select an incapable package or delete evidence to escape uncertainty.
A's auto-archive semantic token includes `activity_token`, changed on admitted new
launch only, not status observations, stop progress or polling. Old absent state
adds a stable empty dimension and no audit/coverage marker.

### Execution ownership and checks

A: new Ruby owner; `libexec/dev-session`, `workspace-archive-check.rb`,
`workspace-auto-archive.rb`; focused Ruby tests/aggregator; `docs/dev-sessions.md`
and `docs/session-archive-recovery.md`. B: portal/service projection and nested
Resources/counts; `libexec/workspace-host`, Go lifecycle/status readers,
`portal/internal/session/runtime-contract.json`, `nix/workspace-portal.nix`, host
tests, `docs/workspace-portal.md`/host docs and VM fixture. B does not edit A's
Ruby owner or lifecycle Runner; A does not edit B's host/Go/Nix files. B may begin
service-reader work from this contract now; surface a contract mismatch to lead
and architect before making incompatible shared changes.

Quick commands, from the feature root and using its Nix shell (run only relevant
focused files; these are a verification plan, not checks performed by architect):

```sh
nix develop --command ruby -Itest test/dev_session/session_services_test.rb
nix develop --command ruby -Itest test/dev_session/archive_check_test.rb
nix develop --command ruby -Itest test/dev_session/archive_cleanup_test.rb
nix develop --command ruby -Itest test/dev_session/deletion_lifecycle_test.rb
nix develop --command ruby -Itest test/workspace_host/profile_transition_test.rb
nix develop --command node --check portal/internal/web/static/app.js
nix develop --command node --check portal/internal/web/static/coordination.js
nix develop --command go -C portal test -mod=readonly ./internal/session ./internal/cluster
```

Use focused `go ... ./internal/web -run PATTERN` for affected existing/new browser
fixtures; its unbounded suite and unknown-duration batches use the required watcher.
Register new Ruby tests in the existing test aggregator so exported shards cover
them. After committed quick checks and mandatory review, watcher-run
`nix build --no-link --print-build-logs .#checks.x86_64-linux.ruby-verification`,
`.#checks.x86_64-linux.host-package-contract`,
`.#checks.x86_64-linux.session-archive-lifecycle`, and applicable package checks.
The existing VM must prove real user-unit descendants, start/stop interruption,
pre-prune ordering and old-format recovery. Do not replace its native proof with
fake-command unit tests or point it at live workspace services.

## Recommendation and supported boundary

Add one local temporary-service owner to reusable `dev-workspace`: a public
launcher that durably registers each service before starting its systemd user
unit, and an archive/delete cleanup gate that stops and verifies every registered
unit before deleting any supporting files. Future previews and candidates use
the same launcher, including new launches in existing sessions. A service can
remain available after feature integration and through idle conversations until
its session is explicitly archived or the enabled automatic worker archives it
under its existing policy.

This covers registered local transient systemd **user services and their native
cgroup descendants**. Existing unregistered services are excluded: no inspection,
discovery, adoption, cleanup or new archival gate for them. Commands that
deliberately escape into another unit/cgroup, remote servers, containers with an independent
lifecycle, persistent system services and production services are outside this
launch contract and do not acquire a new reconciliation gate. Existing development
cluster ownership remains separate. Do not kill by port, PID, pathname or a
matching name. The trusted local operator boundary remains unchanged; this is not
containment against a hostile operator.

## Evidence

Identity was verified with `dev-session current` and both environment markers:
`2026-11-02-session-temporary-service-cleanup`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. The same-session roster retains
architect0 as Astra/xhigh, workspace-write. Its exact
`worktrees/.locks/2026-11-02-session-temporary-service-cleanup.creation.json`
records `state: ready`, `schema: 3`, `provider: codex-lb`; settings were unchanged.

`workspace-host status` and `workspace-host coordination guide` select:

- Package: `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
- Derivation: `/nix/store/2jvhgyq2ilxa4cprlswc7fwh93b3snpx-dev-workspace-0.2.0.drv`.
- Exact derivation `src`: `/nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source`.

Paths below are relative to that immutable source. Its `libexec/dev-session`
matches installed `libexec/workspace-portal/.dev-session-wrapped` except for the
packaged Ruby shebang. This identifies the inspected implementation without
assuming that the canonical repository's current HEAD is the deployed revision.

| Evidence | Consequence |
| --- | --- |
| `libexec/dev-session:2041`, `archive_with_access` | Explicit, strict and automatic archive converge here. Fresh archival calls `WorkspaceTrackingSummaries.prune(..., apply: true)` at line 2134, **before** `prepare_archive_journal!`. Cleanup added only to a later journal phase is too late. |
| `libexec/dev-session:9341`, `quiesce_explicit_archive!`; `:9392`, `quiesce_and_require_idle!`; `:7000`, `retire_session_runtime!` | Current shutdown concerns Codex clients, native/team conversations and trusted tmux identity. It does not inventory independent user services. |
| `libexec/workspace-tracking-summaries.rb`; `libexec/workspace-archive-cleanup.rb` | Tracking pruning removes non-Markdown/non-portal files; cleanup inventories and removes owned checkouts. Neither is a temporary-service owner. |
| `libexec/dev-session:2463`, `delete_with_access` | Delete has its own journal and removes worktrees before runtime retirement; it needs the same service gate. |
| `portal/internal/web/archive_worker.go:77` | The portal already launches an independently supervised transient user service using `systemd-run`, `Type=exec`, `RemainAfterExit=yes`, and `KillMode=control-group`. Reuse this native mechanism, not the archive worker's authorization or unit. |
| `docs/session-archive-recovery.md`; `docs/dev-sessions.md` | Existing archive/revival policy, saved operation identities, package exclusion, automatic eligibility and deferred tracking synchronization must remain authoritative. |
| `libexec/workspace-host:3082` and `portal/internal/session/runtime-contract.json` | Package selection already checks capabilities against retained archive state; extend that boundary for service ownership and pending cleanup. |

The HaveAPI incident is supplied evidence, not a live finding from this session.
It includes `haveapi-doc-language-preview-20261101.service` and all three
candidate units (`candidate`, `nov2-candidate`, `cachefix-candidate`). Their
reported independent user-service lifetime and lack of `PartOf`/`BindsTo` explain
why terminal/agent retirement does not stop them. Their launch scripts, preview
source and ignored gem dependencies are vulnerable to the existing prune/removal
order. No originating-session files, units or transcript were inspected. Under the
user's amended scope these existing unregistered examples remain outside the
cleanup guarantee and untouched; they do not block this feature's archive path.

## Proposed API and ownership record

Exact spelling and timeout defaults below are proposed, not tested interfaces:

```text
dev-session service run SLUG --as-is --name LABEL --cwd PATH -- COMMAND ARG...
dev-session service list SLUG --as-is --json
dev-session service stop SLUG --as-is --id RESOURCE_UUID
```

`run` is the normal launch path, including experimental candidates. The CLI
returns an opaque resource ID and exact generated unit name. Labels are display
metadata, not identities; repeated launches create separate resources. `list`
reports saved ownership and fresh status without mutating it. `stop` uses the
same stop verifier as archive. There is no generic unregister-live-service or
arbitrary shell cleanup-hook API. There is no inventory/adoption command.

Use one bounded, private, atomic JSON registry per session under the existing
user-state root, for example `session-services/<workspace-id>/<slug>.json`,
outside pruned tracking and worktrees. Proposed schema 1 contains:

- Exact workspace root, slug, retained root/creation identity where available,
  a fresh resource epoch and binding to the verified current session incarnation.
  Use existing lifecycle/creation identity checks; slug or CWD alone is insufficient.
- Per resource: UUID, label, generated exact unit, local user-manager identity,
  ownership nonce, launch intent, boot ID, observed InvocationID and ControlGroup,
  bounded stop policy, phase and last bounded diagnostic. Keep commands/environment
  private; do not copy secrets into tracking or public status.
- When cleaning: lifecycle kind, exact operation ID and saved archive mode,
  frozen resource IDs, phase and per-resource stop/removal results. This is a
  service cleanup prelude to the existing lifecycle, not a second archive engine.

On the first managed launch, publish a small durable registry-ID reference in
retained session metadata, then create the matching registry and launch intent
**before** contacting systemd. This reference records only that managed
registration exists; it says nothing about other services. A crash between these
writes leaves a recoverable incomplete registration, never permission to launch.
Choose the exact metadata location during implementation and retain it through
archive/revival; do not infer a missing reference from a session's age.

Serialize launch, stop and lifecycle admission using the existing transition →
creation → session lock order and post-lock generation checks. Pending cleanup rejects new
launches, even after an interrupted archiver releases its OS locks. A timed-out
start is uncertain: reconcile the exact nonce/unit/job under the original resource
ID; never launch a replacement merely because its reply was lost.

Prefer `Type=exec`, `Restart=no`, `KillMode=control-group`, `SendSIGKILL=yes`,
`RemainAfterExit=yes` and a bounded `TimeoutStopSec` (proposed 15 seconds).
Retaining the transient unit until explicit cleanup makes short-lived/failed
launches observable. Do not enable it at login, add activation units, or let a
caller override ownership, restart or cgroup properties. Allocate unique unit
names and attach the ownership nonce when launching; verify live properties
against the durable record. No dependency on terminal or portal lifetime is
needed. Ordinary forks, daemonization and grandchildren remain in that cgroup;
escaping into another manager resource is outside the contract.

## Archive/delete sequence and failure contract

1. Run current authorization, ownership, claims, journal and archive-readiness
   checks. Add registered-resource validation to read-only `archive-check`, without
   stopping anything. No registry and no registration evidence means no managed
   resources and no new blocker. Automatic scans retain existing eligibility/holds.
2. Under lifecycle admission, freeze launch admission and durably bind the service
   cleanup prelude to the exact accepted archive/delete operation and resource set.
   Publish it **before any service stop or tracking prune**. Preserve existing
   explicit agent quiescence and automatic idle requirements. All conflicting
   lifecycle, creation, revival and package paths must recognize this prelude as
   pending even if the ordinary archive journal has not yet been written. Sessions
   with no managed resources continue the ordinary path without a service prelude.
3. For every registered resource, including failed/starting candidates, reconcile
   its exact identity and outstanding start/stop jobs. Request native service stop;
   systemd sends the graceful signal to the cgroup and escalates to SIGKILL after
   its timeout. Bound the observation wait as well (proposed another 5 seconds).
   Do not substitute process-group killing or a PID-file check.
4. Prove no pending activation/start job, a terminal unit state, and an empty or
   removed recorded cgroup including descendants. A successful `systemctl` exit,
   absent MainPID, closed port or `ActiveState=failed` alone is insufficient.
   Changed InvocationID, manager identity, unknown job state, permission failure,
   lingering descendants or a timeout blocks file deletion. A still-busy kernel
   task remains a blocker even after SIGKILL. Record which owned services stopped;
   leave other sessions and registered-service-dependent files untouched.
5. Release only the exact owned transient unit state (including failed-state reset
   when needed) and verify it unloads without activation sources. No unlinking
   systemd's private unit files or global `reset-failed`/journal vacuum. Preserve
   compact private stop evidence; system journal retention follows host policy.
   Recheck the complete frozen set immediately before the first file deletion.
6. Mark service cleanup verified, then prune tracking, prepare/seal the existing
   archive inventory and continue normal cluster, worktree, tracking and runtime
   phases. Delete calls the same gate before its first worktree/file removal.
   Existing ownership, exact-head and recovery checks remain in effect; `--force`
   cannot bypass unproved service shutdown.

New service-created scratch files should live inside the owning session's existing
tracking/worktree boundaries and use their ordinary removal policy. The API does
not grant arbitrary external file deletion. Ordinary tracking/worktree pruning
remains unchanged, including files used by unregistered services. Markdown/portal
retention and committed-only worktree restoration remain unchanged. No attempt
to preserve a temporary server's in-memory fixture state.

Every step is retryable under the original operation ID. A crash after stop but
before its progress write requires fresh manager/job/cgroup proof, not a second
launch. A unit name reused for another invocation refuses. A lost manager/reboot
must be positively reconciled with the recorded boot, unit and cgroup evidence;
connection failure is not absence. Partial cleanup keeps the operation pending
and recovery files intact. Retry never restarts services to compensate for failure.

## Existing sessions, revival and rollback

Initialize registration lazily at the first managed launch in any session. A new
or old session that never used the launcher needs no service record, migration,
audit or confirmation. Archive/delete proceeds under its ordinary rules. Only
future launches through the API become managed; other services remain untouched
and outside the guarantee. Forks do not inherit another session's registrations.

Distinguish absence from loss: a registry-ID reference or pending lifecycle/launch
evidence proves that registration is expected. A missing, corrupt or mismatched
registry in that case blocks file deletion until the original registered state is
recovered. So does uncertainty about a registered launch or stop. An untouched
old session has no such evidence and gains no blocker. Do not discover units to
fill missing records, and do not turn the registration reference into a claim
about all services belonging to a session.

Preserve all predecessor archive/removal/revival journal formats, saved policies,
sealed tracking checksums, recovery snapshots and committed-head proofs. Add the
registered-resource guard before any *remaining* file deletion without rewriting
old evidence; no registered state means no added recovery obligation. Files already
removed by an old executor cannot be retroactively protected. Completed archives
are not reopened or backfilled. Revival never restarts temporary services; retain
completed registration/stop evidence and use a fresh resource epoch for subsequent
managed launches. Sessions without registrations retain their original revival
and file-restore behavior without an audit gate.

Advertise service state/cleanup support in the runtime contract and check it in
both package selection and candidate activation, following existing capability
checks. New launch/prelude state must survive a compatible package switch; service
registration neither stops nor restarts previews during ordinary activation.
Pending cleanup already excludes package mutation. Refuse rollback to a package
that would ignore live/uncertain registered state or required pending recovery.
Absent registrations require no new package capability. Fully verified retired
resources alone need not forbid rollback if the target preserves their terminal
records and normal revival semantics; never discard evidence to pass the check.
Recover forward for incompatible live or pending state. First-upgrade and rollback
tests must include stale pre-upgrade commands waiting on locks. No database/API/client/protocol migration,
fleet coordination or system configuration change is indicated; the persistent
change is local runtime state and its package compatibility contract.

Explicit archive approval covers this necessary temporary-service cleanup for
that session. Automatic cleanup occurs only inside its already enabled worker's
authorized archive operation; preserve the 1/7/14-day policy and Keep open hold.
Managed service launches should reset inactivity through the existing
semantic observation mechanism; status polling and service uptime should not.
Ordinary completion, merge, review, handoff or release of a machine never triggers
service cleanup or session closure. Delete retains its separate exact user approval.

## Proposed portal resources and Team count

Per the user's amendment, replace the separate Clusters/Reservations entries and
proposed Services entry with one **Resources** sidebar entry (label for lead
acceptance). Its page has **Clusters / Reservations / Services** subtabs, using
existing tab, card, badge and notice styles. Preserve current cluster/reservation
controls. Services remains visibility-only; no new resource manager or dashboard.

Show three compact, distinguishable icon/count indicators inside the sidebar
entry, with per-kind accessible names/tooltips and existing icon styling. Hide
each confirmed zero; when all three are confirmed zero show no indicators, but
keep Resources available. Unknown/busy/unavailable is not zero: show a per-kind
unknown marker or visibly stale last-known count with its age/tooltip, including
when the last known value was zero. Do not sum unlike resource kinds.

| Indicator | Authoritative count and page relationship |
| --- | --- |
| Clusters | Existing provider-owned clusters confirmed by `found`, including stopped clusters with retained state; not configured provider definitions, VMs, endpoints or only running clusters. Match the current cluster cards, excluding retired history. `InspectContext` synthesizes unavailable cards on errors, so raw `len(.Clusters)` is not proof: preserve presence/count certainty separately and do not count a diagnostic placeholder as a confirmed cluster. |
| Services | Current, not-yet-retired resource IDs in the registered-service reader: include starting, running, exited/failed and stopping/uncertain cleanup entries until verified retirement. Match the current Services list; put retired records in historical evidence outside the count. Registry membership supplies the count without a live unit scan; a unit-status failure need not invalidate known membership. Lost/corrupt expected registry makes membership unknown. No registry/registration evidence means zero. |
| Reservations | Distinct canonical machines currently held by this exact session incarnation, matching the existing Reserved machines section and complete `reservationHolders` summary. Include held claims and legacy review/recovery holds, deduplicating aliases/records. Requested/waiting claims own nothing and do not increment this count; they remain visible separately. Released/canceled history and repository-only claims do not count. Tooltip identifies the count as held machines, not requests or claim records. |

Team becomes **Team (N)**, including the lead: its current Members table renders
a lead row plus every retained roster member whose state is not `removed`.
Use that same roster projection, including idle, creating, failed or archived
retained members; do not use `readyMembers` or running-agent counts. Exclude removed
history and utility watchers/temporary reviewers outside the roster. A known solo
session shows Team (1); retain the current absence of Team navigation for a
threadless session. The parenthetical is never suppressed as a resource-zero
rule. A failed roster read shows unknown or a marked stale count, not inferred 1.

Retain `#clusters`, `#reservations` and proposed `#services` as child deep links:
hash handling selects Resources and the indicated subtab. `#resources` opens
Clusters by default. Reuse the Settings nested-tab/history pattern, preserving
reload, back/forward, query parameters, keyboard focus and panel ARIA relationships.
Update coordination's visibility check/event handling for the nested Reservations
panel; do not break existing controls or links from Workspace operations.

Source anchors under `portal/internal/web/` in the inspected immutable package:
`templates/session.html:25`–`:28`, `:69`, `:236`, `:338`–`:360`; `templates/clusters.html`;
`static/app.js:3042`–`:3113` (nested Settings/hash navigation) and `:4028` (details
refresh); `static/coordination.js:42`–`:64` and `:229` (held-machine count/refresh).
`portal/internal/cluster/status.go:189` distinguishes found/error results;
`libexec/workspace-coordination.rb:1550`–`:1604` builds incarnation-bound held-machine
summaries before limiting history. `portal/internal/web/coordination.go:15`
documents read-only GET.

Add current counts plus known/stale metadata to initial/session-details projections
for clusters, services and Team; reuse coordination's existing session-scoped GET
and complete holder summary for reservations, not truncated claims/history arrays.
Keep the existing bounded, visibility-aware refresh/cancellation loops; no new poller.
Apply each count with its corresponding accepted page snapshot, including deferred
Team updates during editing. Resource counts should refresh while another session
subpage is visible. Check exact workspace/session/incarnation and registered ownership;
bounded shared/nonblocking reads respect lifecycle fences and never initialize
records, wake/revive services, retry cleanup, write activity or reset inactivity.

Services shows label, lifecycle phase, observed unit state/time and bounded safe
diagnostics; running is not HTTP readiness. Unknown observations stay explicit.
Archived stop/removal evidence is historical, outside current counts, with no live
probing of retired unit names. Allowlist the public projection: no commands,
environment, credentials, raw helper output or logs. Cleanup failures identify the
registered service and pending operation, pointing to existing explicit lifecycle
recovery; reading never retries it. Existing unregistered services remain invisible
and uninspected. Defer preview links: no browser URL contract exists, and workspace
localhost is not automatically browser-reachable. No discovery, proxying, routing
or network exposure. Service Start/Restart/Stop/log streaming remain separate
choices. Lead owns final wording; no KB or site runtime change is indicated.

## Alternatives and implementation packages

A session target/slice with `PartOf` can group units, but it does not durably record
registered ownership, uncertain launches or verified shutdown before file removal.
It is unnecessary for the initial implementation. Name/path/port scans cannot
safely distinguish another session or a durable service. Manual cleanup reminders
leave the reported failure intact. A general resource-plugin framework or remote
server orchestration is outside this change.

Everything functional belongs to `dev-workspace`. No HaveAPI, codex-web,
vpsFree extension runtime or production configuration change is indicated.
Update generic session/launch instructions so agents use the supported launcher
for every preview/candidate. A short workspace procedure pointer may be useful;
do not duplicate the implementation in site code.

Proposed implementation boundaries, after user authorization:

| Package | Files and dependencies | Acceptance |
| --- | --- | --- |
| A: service owner and lifecycle integration, one implementer | New `libexec/workspace-session-services.rb`; `libexec/dev-session`; `libexec/workspace-archive-check.rb`; focused `test/dev_session/*` and service tests. Own CLI, registry, locking, stop proof, pre-prune integration and bounded public status projection. | No admitted launch can escape the durable inventory; all file deletion waits for verified complete cleanup; uncertainty remains recoverable; status reads have no lifecycle side effects. |
| B: compatibility, portal resources/counts, documentation and packaged fixtures, second implementer | `libexec/workspace-host`, `portal/internal/session/runtime-contract.json`, necessary Go lifecycle/status readers; `portal/internal/web/server.go`, `templates/session.html`, new service template, `static/app.js`, `static/coordination.js` and minimal existing stylesheet changes; cluster reader's presence-summary metadata in `portal/internal/cluster/status.go`; owning Nix package expression if needed, `nix/tests/session-archive-lifecycle.nix`, focused portal/host tests; `docs/dev-sessions.md`, `docs/session-archive-recovery.md`, `docs/workspace-portal.md`. Depends on A's frozen state/prelude and public reader contracts. | Selection/activation/refusal and old-format recovery agree; CLI/browser/worker expose the same blocker and resume the same operation. Resource/Team counts match their authoritative page snapshots; nested navigation preserves existing controls/links. Services rendering remains read-only, authenticated, session-bound and distinguishes historical from observed state. |

Lead serializes overlapping reader/test edits and Git operations. Package B's
fixture design and docs can proceed once the record and recovery interfaces are
settled; do not force parallel edits to the lifecycle owner. Exact file additions
are implementation decisions, not authorization to broaden scope.

## Verification brief

No runtime checks were run for this proposal. Later, use the repository's Nix
environment and disposable state; never point lifecycle tests at this workspace
or the supplied HaveAPI units.

Quick component checks should cover:

- Multiple previews/candidates, a fast-exiting launcher, ordinary grandchildren,
  another session's unit and a durable unrelated service; only owned resources stop.
- Lost launch replies, archive versus launch races, late jobs, reused names or
  InvocationIDs, missing/corrupt known registry and manager-unavailable failures.
- Graceful stop and ignored SIGTERM, bounded forced stop, residual cgroup members;
  assert tracking scripts/assets and worktree dependencies still exist on failure.
- Interruption before/after intent, launch, stop, unit unload, prune and main-journal
  handoff; exact retry, no duplicate launch, unchanged old journal policy.
- Old/new sessions without a registry continue ordinary archival; no service
  discovery/adoption occurs and unregistered fixtures remain untouched. Future
  registered launches in an old session receive the full cleanup guarantee.
- First-registration interruption, known registry loss, all registered candidates,
  revival without service restart, and unchanged automatic holds/eligibility.
- Compatible upgrade and refused rollback, candidate activation, waiting stale
  commands and pending old archive/delete/revival formats.
- Focused portal reader/template/browser fixtures: no-registry empty state,
  multiple registered candidates, stale/busy/unknown status, cleanup failure and
  archived evidence; safe text rendering, secret exclusion and session isolation.
  Verify mixed/zero/unknown resource indicators; stopped versus absent clusters and
  unavailable placeholders; active versus retired service records; distinct held
  machines versus waiting/released/repository-only claims and truncated history.
  Verify Team includes lead/nonremoved members in every retained state, excludes
  utilities/removed history, handles absent versus unreadable roster, and updates
  with its table. Check old child links, nested keyboard navigation, reload/back/
  forward, compact sidebar/accessibility, existing controls and hidden-page pause.
  Repeated count/status reads must not mutate state/inactivity or inspect
  unregistered/retired units; stale responses must not cross session incarnations.

After committed implementation, quick checks and mandatory independent review,
extend and run the existing `session-archive-lifecycle` NixOS VM check with real
systemd user units and cgroup descendants. Exercise CLI, browser worker, automatic
archive, delete and interrupted retry; prove all owned units/cgroups disappear
before the first artifact/worktree removal while unrelated fixtures stay running.
Run applicable host package-contract checks for compatibility. Use the required
verification watcher for long checks; stop on identity uncertainty, file deletion
before verified stop, unrelated-unit effects or timeout overruns. Deployment, if
later authorized, additionally requires a fresh disposable installed-package
archive/revive check. None of these proposed checks authorizes live cleanup now.
