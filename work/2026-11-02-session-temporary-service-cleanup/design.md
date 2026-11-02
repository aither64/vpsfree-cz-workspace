# Session temporary service cleanup

**PROPOSED / NOT IMPLEMENTED — 2026-11-02.** Read-only investigation and design
only. No service inspection, launch, stop or removal; no lifecycle experiment,
project edit, commit or deployment. The user decides whether to implement this.

## Recommendation and supported boundary

Add one local temporary-service owner to reusable `dev-workspace`: a public
launcher that durably registers each service before starting its systemd user
unit, and an archive/delete cleanup gate that stops and verifies every registered
unit before deleting any supporting files. Main previews and every candidate use
the same launcher. A service can remain available after feature integration and
through idle conversations until its session is explicitly archived or the
enabled automatic worker archives it under its existing policy.

This covers local transient systemd **user services and their native cgroup
descendants**. It is not universal process discovery. Commands that deliberately
escape into another unit/cgroup, remote servers, containers with an independent
lifecycle, persistent system services and production services are outside this
launch contract. Existing development-cluster ownership remains separate. A
known unsupported session resource blocks cleanup until its owner reconciles it;
do not kill by port, PID, pathname or a matching name. The trusted local operator
boundary remains unchanged; this is not containment against a hostile operator.

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
order. No originating-session files, units or transcript were inspected.

## Proposed API and ownership record

Exact spelling and timeout defaults below are proposed, not tested interfaces:

```text
dev-session service run SLUG --as-is --name LABEL --cwd PATH -- COMMAND ARG...
dev-session service list SLUG --as-is --json
dev-session service stop SLUG --as-is --id RESOURCE_UUID
dev-session service inventory SLUG --as-is --file INVENTORY_JSON
```

`run` is the normal launch path, including experimental candidates. The CLI
returns an opaque resource ID and exact generated unit name. Labels are display
metadata, not identities; repeated launches create separate resources. `list`
reports saved ownership and fresh status without mutating it. `stop` uses the
same stop verifier as archive. There is no generic unregister-live-service or
arbitrary shell cleanup-hook API. `inventory` is the explicit legacy adoption or
audited-empty procedure described below, not an automatic name scanner.

Use one bounded, private, atomic JSON registry per session under the existing
user-state root, for example `session-services/<workspace-id>/<slug>.json`,
outside pruned tracking and worktrees. Proposed schema 1 contains:

- Exact workspace root, slug, retained root/creation identity where available,
  a fresh resource epoch and binding to the verified current session incarnation.
  Use existing lifecycle/creation identity checks; slug or CWD alone is insufficient.
- Coverage: `managed-from-creation`, `audited`, or `unknown`, with the audit's
  ownership source when applicable. Absent/corrupt state never means audited-empty.
- Per resource: UUID, label, generated exact unit, local user-manager identity,
  ownership nonce, launch intent, boot ID, observed InvocationID and ControlGroup,
  bounded stop policy, phase and last bounded diagnostic. Keep commands/environment
  private; do not copy secrets into tracking or public status.
- When cleaning: lifecycle kind, exact operation ID and saved archive mode,
  frozen resource IDs, phase and per-resource stop/removal results. This is a
  service cleanup prelude to the existing lifecycle, not a second archive engine.

Write and sync launch intent **before** contacting systemd. Serialize launch,
inventory and lifecycle admission using the existing transition → creation →
session lock order and post-lock generation checks. Pending cleanup rejects new
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
   checks. Add coverage/registry validation to read-only `archive-check`, without
   stopping anything. Automatic scans retain their existing eligibility/hold rules.
2. Under lifecycle admission, freeze launch admission and durably bind the service
   cleanup prelude to the exact accepted archive/delete operation and resource set.
   Publish it **before any service stop or tracking prune**. Preserve existing
   explicit agent quiescence and automatic idle requirements. All conflicting
   lifecycle, creation, revival and package paths must recognize this prelude as
   pending even if the ordinary archive journal has not yet been written.
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
   leave other sessions and all service-dependent files untouched.
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
not grant arbitrary external file deletion. Adopted external artifacts need
explicit ownership/recovery treatment; unknown ones block a claimed complete
cleanup. Markdown/portal retention and committed-only worktree restoration remain
unchanged. No attempt to preserve a temporary server's in-memory fixture state.

Every step is retryable under the original operation ID. A crash after stop but
before its progress write requires fresh manager/job/cgroup proof, not a second
launch. A unit name reused for another invocation refuses. A lost manager/reboot
must be positively reconciled with the recorded boot, unit and cgroup evidence;
connection failure is not absence. Partial cleanup keeps the operation pending
and recovery files intact. Retry never restarts services to compensate for failure.

## Legacy coverage, revival and rollback

**Recommended default: fail closed for unknown coverage.** New session creation
publishes a managed-empty registry before exposing a ready session. Forks create
their own empty ownership; they do not inherit live services. Existing sessions
without this feature's coverage record start `unknown`, including ones first
using the new launcher after upgrade. Their new launches can be registered, but
that does not certify the absence of older services. Automatic archival skips
them with an actionable blocker; manual archive/delete refuses before removing
files. This one-time migration cost is preferable to claiming cleanup succeeded
while known previews survive.

The supported owner/operator audit supplies a **complete** inventory of temporary
resources, including all candidates, or an explicit audited-empty declaration.
For each adopted transient user unit, bind the owner's explicit assertion and
evidence to the freshly checked user-manager identity, boot, InvocationID,
ControlGroup and absence of activation sources. Matching names, scripts or ports
are discovery hints only. Refuse incompatible/persistent units and ownership that
cannot be established. Reconcile those separately with explicit authority, then
record the completed inventory. An adopted unit must satisfy the same bounded
stop/removal contract; do not silently weaken it for migration. No global scan or
automatic adoption, and no fresh recurring confirmation after coverage is established.

For the supplied HaveAPI example this means the originating owner must account
for the preview **and all three candidates**. This proposal grants no authority
to audit or change them. Missing evidence leaves coverage unknown and blocks
destructive cleanup; an empty list generated from the new registry is not an audit.

Preserve all predecessor archive/removal/revival journal formats, saved policies,
sealed tracking checksums, recovery snapshots and committed-head proofs. Add the
new guard before any *remaining* file deletion without rewriting old evidence.
An exact-operation inventory recovery path must permit an authorized audit while
that journal is pending; it cannot accept a different lifecycle action. Files
already removed by an old executor cannot be retroactively protected. Resolve
uncertain legacy resources before completing that recovery, and retain its
original recovery semantics. Completed archives are not automatically reopened
or backfilled. Revival never restarts temporary services; it creates a fresh
service epoch only from proved completed cleanup. Legacy revival starts with
unknown coverage until audited; it retains its existing file-restore policy.

Advertise service state/cleanup support in the runtime contract and check it in
both package selection and candidate activation, following existing capability
checks. New launch/prelude state must survive a compatible package switch; service
registration neither stops nor restarts previews during ordinary activation.
Pending cleanup already excludes package mutation. Refuse rollback to a package
that would ignore live, uncertain or coverage-bearing state. Keep the guard while
such records or supported restoration paths depend on it; recover forward rather
than deleting evidence. First-upgrade and rollback tests must include stale
pre-upgrade commands waiting on locks. No database/API/client/protocol migration,
fleet coordination or system configuration change is indicated; the persistent
change is local runtime state and its package compatibility contract.

Explicit archive approval covers this necessary temporary-service cleanup for
that session. Automatic cleanup occurs only inside its already enabled worker's
authorized archive operation; preserve the 1/7/14-day policy and Keep open hold.
Service launch/inventory changes should reset inactivity through the existing
semantic observation mechanism; status polling and service uptime should not.
Ordinary completion, merge, review, handoff or release of a machine never triggers
service cleanup or session closure. Delete retains its separate exact user approval.

## Alternatives and implementation packages

A session target/slice with `PartOf` can group units, but it does not establish
ownership of existing units, record uncertain launches or prove safe file removal.
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
| A: service owner and lifecycle integration, one implementer | New `libexec/workspace-session-services.rb`; `libexec/dev-session`; `libexec/workspace-archive-check.rb`; focused `test/dev_session/*` and service tests. Own CLI, registry, locking, stop proof and pre-prune integration. | No admitted launch can escape the durable inventory; all file deletion waits for verified complete cleanup; uncertainty remains recoverable. |
| B: compatibility, documentation and packaged fixtures, second implementer | `libexec/workspace-host`, `portal/internal/session/runtime-contract.json`, necessary Go lifecycle/status readers, `nix/package.nix` packaging if needed, `nix/tests/session-archive-lifecycle.nix`, relevant host tests; `docs/dev-sessions.md`, `docs/session-archive-recovery.md`. Depends on A's frozen state/prelude contract. | Selection/activation/refusal and old-format recovery agree; CLI/browser/worker expose the same blocker and resume the same operation. |

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
  InvocationIDs, missing/corrupt registry and manager-unavailable failures.
- Graceful stop and ignored SIGTERM, bounded forced stop, residual cgroup members;
  assert tracking scripts/assets and worktree dependencies still exist on failure.
- Interruption before/after intent, launch, stop, unit unload, prune and main-journal
  handoff; exact retry, no duplicate launch, unchanged old journal policy.
- Managed-empty creation versus legacy unknown, explicit adoption/audited-empty,
  missed candidates, unsupported resources, revival without service restart,
  unchanged automatic holds/eligibility and inactivity semantics.
- Compatible upgrade and refused rollback, candidate activation, waiting stale
  commands and pending old archive/delete/revival formats.

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
