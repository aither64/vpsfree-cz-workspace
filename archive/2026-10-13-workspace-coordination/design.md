# Workspace operation coordination: implementation and verification brief

Status: proposed implementation contract, grounded in the checked-out sources on
2026-10-13. Design owner: the explicitly requested GPT-6 Astra/xhigh designer.
The initiating lead owns implementation and acceptance. A different independent
reviewer reviews the final committed deliverable. This document authorizes no
merge, deployment, session mutation, or change of team.

## Outcome and scope

A deterministic coordinator in the selected user-profile runtime schedules small,
explicitly authorized mutations across every registered workspace. Agents retain
responsibility for design, edits, rebases, review, tests, builds, approval and
resolving conflicts. They prepare independently and submit immutable results.
The coordinator chooses ready work, verifies its baseline immediately before the
mutation, records the result, and notifies its existing owning conversation.
There is no additional LLM supervisor and no persistent coordination team.

The first implementation has exactly three mutation kinds: `merge`,
`machine_activate`, and `profile_activate`. Jobs can depend on earlier jobs.
There is no general shell-task executor, CI engine, dependency rebasing engine,
or distributed coordinator. Manual deployments from the operator's build machine
remain outside the coordinator. The guarantees cover cooperating commands in one
user-profile runtime; they cannot serialize arbitrary Git, SSH, confctl or old
store-binary invocations by the trusted operator.

A machine reservation belongs to an initiative, not to a turn, process, build,
job or timeout. Deploy-first work keeps it throughout human UI review, idle
periods, feedback, repeated fixes and redeployment. Its normal release requires
both final integration and an explicit declaration that deployment/review work is
finished. An active reservation does not block another session's preparation or
repository integration. It blocks all other coordinated deployment operations on
that physical machine, including a workspace user-profile switch there.

No repository/default-branch integration is authorized for this initiative.
The user authorized a no-reboot aitherdev deployment through the configuration
feature branch, followed by selection of the workspace application profile.
Therefore this initiative's deployed reservation remains held after that rollout
until a later authorized integration and deployment completion, or an explicitly
authorized recovery disposition.

## Evidence and ownership of implementation

| Existing source | Consequence for implementation |
| --- | --- |
| `dev-workspace/libexec/workspace-host`, `switch` and command dispatch | `nix build`, Codex probes, profile replacement and activation currently run inside the exclusive transition lock. Extract preparation before that lock; retain `_activate`, generation checks and forward-only recovery. |
| `libexec/workspace-profile-identity.rb` | Reuse the complete profile token, not just the resolved package path, to detect changes including compensated/repeated selection. |
| `libexec/dev-session`, lifecycle/session lock helpers | Keep transition → creation → session → tracking-commit lock order. Add coordination admission without acquiring these locks while holding the ledger mutex. |
| `docs/session-archive-recovery.md` | Explicit archive keeps captured worktrees and conversation identities. Coordination obligations must survive moving tracking to `archive/`; they cannot live only in `portal.yml`. |
| `portal/cmd/workspace-portal/main.go:newCodexClient` | Notifications must use the same selected workspace socket, recovery wrapper and private submission ledger as portal/team sends. Do not create a second submission ledger. |
| `portal/internal/workspacecodex/recovery.go`, `teamruntime.Service.Assign` | Existing-thread start/steer and cold recovery are available. Reuse their identity and settings rules, without creating/replacing a root or assigning a team member. |
| selected codex-web `codex/client.go:SendWithOptions`, `ReconcileSendWithOptions` | Stable IDs, action context, options and native receipts already exist. An ambiguous submitting attempt reconciles history and refuses blind replay. |
| `nix/workspace-portal.nix`, `ExtensionCatalog` | The existing schema-1 extension catalog has exact keys. Preserve it; use a separate coordination catalog rather than silently changing its format. |
| confctl `Cli::Cluster#deploy` | Deployment without `--generation` calls `do_build`. Do not use that path for queued activation. |
| confctl `Generation::Build`, `Nix#copy/#activate/#activate_with_rollback/#set_profile` | A named build generation records exact store paths and inputs; copy, activation and profile publication are distinct operations. Live activation can succeed before profile publication fails. |

Implement the ledger, scheduler, reservation rules, generic Git integration,
profile preparation/activation, lifecycle gates and user services in
`dev-workspace`. Prefer a new Ruby library `libexec/workspace-coordination.rb`
and a small packaged command/runner, shared by `workspace-host` and
`dev-session`. Ruby owns every write to the coordination ledger. Keep the Go
addition small: a private existing-thread notification helper and authenticated
read-only portal views that call the packaged coordination reader. Do not add
SQLite, a message broker, a separate web server or a new Go dependency for this
feature.

`vpsfree-dev-workspace` supplies the immutable confctl adapter and its tests.
The consuming workspace supplies concrete target aliases, repository/flake-input
mappings, procedures and package composition. Configuration selects the matching
host-module/runtime revision and owns its repeatable rollout procedure. There is
no planned codex-web source change; see the delivery limitation below before
claiming a stronger transport guarantee.

## Immutable catalogs and canonical resources

Add optional `coordinationConfig` to generic `lib.mkPackage`, defaulting to an
empty schema-1 catalog. Package it as
`share/dev-workspace/coordination.json`. It contains `schema`, `adapters`,
`machines`, `repositories`, and `profileMachine`. Adapter commands are immutable
Nix store references validated with the same Nix-context rules as extensions.
Workspace JSON may select a configured target ID but cannot supply commands,
resource strings, profile paths, SSH endpoints or arbitrary executables.

An illustrative consuming configuration is:

```json
{
  "schema": 1,
  "adapters": {
    "confctl": {"protocol": 1, "command": "/nix/store/…/bin/workspace-confctl-adapter"}
  },
  "machines": {
    "aitherdev": {
      "id": "vpsfree:aitherdev",
      "aliases": ["aitherdev.int.vpsfree.cz", "cz.vpsfree/machines/aitherdev"],
      "adapter": "confctl",
      "configurationRepository": "vpsfree-cz-configuration",
      "selector": "cz.vpsfree/machines/aitherdev"
    }
  },
  "repositories": {
    "dev-workspace": {"remote": "git@github.com:aither64/dev-workspace.git"},
    "vpsfree-dev-workspace": {"remote": "git@github.com:vpsfreecz/dev-workspace.git"},
    "vpsfree-cz-configuration": {"remote": "git@github.com:vpsfreecz/vpsfree-cz-configuration.git"}
  },
  "profileMachine": "vpsfree:aitherdev"
}
```

Include the workspace repository's observed canonical SSH remote in the real
catalog; derive it from the checked-out repository rather than guessing it.
Configuration/module input mappings and the workspace's nested runtime mapping
are package-time data in this same catalog or the adapter's packaged site data.
The extension validates and passes generic coordination config through; concrete
host names stay out of its tracked sources. The catalog digest is SHA-256 of the
installed bytes, saved with each prepared snapshot.

Canonical identities are:

- repository target: normalized canonical SSH repository identity plus exact
  full target ref (`repo:github.com/aither64/dev-workspace:refs/heads/master`);
- machine: the configured stable ID (`machine:vpsfree:aitherdev`);
- profile: canonical selected profile path within this runtime
  (`profile:<sha256(canonical-profile-path)>`), always paired with its machine;
- local shared Git mutation: canonical Git common-directory identity, also using
  the existing `dev-session-tracking.lock` for the shared workspace checkout.

Resource keys are computed by trusted runtime code. Accept scp-style SSH and
`ssh://git@github.com/...` as the same Git identity, remove only the optional
`.git`, and normalize the host case. Reject HTTPS for normal writes under these
workspace rules. For GitHub normalize repository owner/name case; do not apply
that rule to arbitrary servers. Resolve remotes and registration ownership at
admission and again before mutation. Local fixture remotes are test-only.

Do not canonicalize machines by DNS lookup. An alias is accepted only if it maps
uniquely in the installed catalog. Registration/package preparation rejects
conflicting aliases, duplicate machine IDs with incompatible endpoint mappings,
and configured profile deployment without a machine association. A user-profile
switch on aitherdev always competes for aitherdev, regardless of which registered
workspace supplied its package.

## Persistence and admission

Store private state under the existing selected user state root:

```text
coordination/
  ledger.lock
  ledger.json
  scheduler.lock
  attempts/<attempt-id>/{request.json,phase.json,result.json,worker.lock,log}
  sources/<snapshot-id>/…
  roots/<snapshot-id>-<artifact-name>
```

Directories use mode 0700 and ordinary private JSON/lock files 0600. Use the
existing safe-file conventions: refuse symlinks, unexpected ownership and
malformed JSON; reject duplicate/unknown fields, trailing data and unsupported
schemas. This protects mistakes and concurrent/recovery integrity, not a hostile
local administrator. Store no credentials or environment dumps. Bound request
JSON to 256 KiB, ledger to 16 MiB, and outstanding jobs to 4096. Refuse new
admission before exhaustion while reserving space for result/recovery updates.
Reserve at least 2 MiB of that bound exclusively for recovery/result updates;
new admission uses the remaining space and conservatively accounts for each
job's maximum terminal result. No first-release automatic history pruning; a full
ledger is a visible admission
failure, not permission to delete unresolved receipts. Logs are separately
bounded/rotated and never carry authority.

Use one atomically replaced ledger, with a monotonically increasing `revision`
and `nextSequence`, containing maps of owners, approvals, reservations, jobs and
notification outbox entries. Under `ledger.lock`, read/validate, apply one
transaction, write a same-directory temporary file, fsync it, rename, and fsync
the directory. Never run Git, Nix, SSH, Codex, systemctl, hooks, or wait for another
lock while holding this mutex. Orphan temporary files are ignored, not recovery
facts. A malformed committed ledger blocks mutations and package transitions;
show its error in status without silently initializing an empty replacement.

Owner identity is the registered workspace's canonical root and registry name,
exact slug, the retained root thread ID when present, and the current session
creation/deletion identity (reuse existing removal history/creation receipts).
Save a generated `ownerId` and its initial identity once. Same slug after deletion
is a different owner. Archives retain that owner. Revival can reconnect only to
the same retained identity; it never transfers another session's reservation.
Session/registry names and CWD alone are not ownership proof.

Normal autonomous jobs require the exact existing root conversation in the
validated session manifest/authority. No `start`, fork, guessed thread lookup or
implicit adoption is allowed during job admission or notification. Retained team
lead settings remain untouched. A threadless tracking session has no automatic
notification destination; its special bootstrap path is discussed below.

## Public CLI and JSON contracts

Add these commands to the stable dispatcher. All session forms accept the normal
`--workspace NAME` and exact-slug `--as-is` handling. Default output is concise;
`--json` returns the envelopes below. JSON input comes from stdin or a file,
never interpolated into a shell command.

```text
dev-session coordination status SLUG --as-is --json
dev-session coordination approve SLUG --as-is --request FILE --json
dev-session coordination reserve SLUG --as-is --request FILE --json
dev-session coordination submit SLUG --as-is --request FILE --json
dev-session coordination refresh SLUG JOB --as-is --request FILE --json
dev-session coordination cancel SLUG JOB --as-is --reason TEXT --json
dev-session coordination finish SLUG RESERVATION --as-is --request FILE --json
dev-session coordination reconcile SLUG JOB --as-is --json
workspace-host coordination status --json
workspace-host prepare --source PATH --json
workspace-host switch --source PATH [--from-candidate]
```

`approve` records the trusted operator/lead's attestation to an actual user
instruction; it is not a new permission source. Admission checks recorded scope
and evidence. The software cannot infer semantic human approval from prose.
Portal status is read-only in this release; do not add a generic Approve/Run
button that accidentally changes approval policy. `reconcile` inspects/resumes a
known operation under its original authority, never authorizes a new mutation.

For `submit`, `approvalId` may be null to retain concrete work in
`waiting_approval`; such a job is never eligible to claim. Every executing job
must resolve an applicable recorded approval.

All mutations require a caller-generated lowercase UUID `requestId`; exact
repeat returns the existing result, while reuse with different canonical payload
fails. Every update also supplies `expectedRevision` of the modified job or
reservation. Requests use schema 1; reply shape is:

```json
{
  "schema": 1,
  "requestId": "UUID",
  "id": "UUID",
  "revision": 3,
  "state": "waiting_resource",
  "reason": {"code": "machine_owned", "ownerId": "UUID", "resource": "machine:vpsfree:aitherdev"},
  "portalUrl": "https://…/SESSION/"
}
```

`reason` is null when absent. Stable codes, not message-text matching, drive
clients. Exit 0 means accepted/status returned, not successful mutation; exit 2
means invalid input, 3 stale revision/baseline, 4 missing authorization/ownership,
5 recovery required, 75 temporarily unavailable. Keep existing commands' exit
contracts unchanged outside the new subcommands.

A merge approval request is:

```json
{
  "schema": 1,
  "requestId": "UUID",
  "kind": "merge",
  "scope": [{"repository": "dev-workspace", "target": "refs/heads/master"}],
  "source": {"kind": "user_instruction", "reference": "conversation message or exact state artifact reference", "quote": "exact relevant approval"},
  "reviewedSnapshot": "sha256:…"
}
```

Machine/profile approvals instead use `kind: "deploy"`, canonical machine IDs,
allowed actions (`switch`, `profile_activate`), and `reboot: false`. Record an
optional explicitly approved iteration scope. Omitted iteration scope binds the
prepared change; never manufacture standing approval. Reuse existing approval
semantics: repository/target approval survives a proven patch-equivalent rebase,
but material patch, repository, target or deployment-scope changes invalidate its
applicability. An approval is never created from a notification, job success,
build, review, deployment or session-completion criterion.

A reservation request is:

```json
{
  "schema": 1,
  "requestId": "UUID",
  "target": "aitherdev",
  "mode": "deploy_first",
  "approvalId": "UUID",
  "integrationObligations": [
    {"repository": "dev-workspace", "target": "refs/heads/master"},
    {"repository": "workspace", "target": "refs/heads/master"},
    {"repository": "vpsfree-cz-configuration", "target": "refs/heads/master"}
  ]
}
```

The real request lists every affected registered branch, including the extension.
`mode` is `deploy_first` or `integrated`; the latter still keeps ownership until
explicit deployment completion. Registration changes that add affected branches
expand the final proof requirement, never silently discard an obligation.

A job submission has this shared envelope:

```json
{
  "schema": 1,
  "requestId": "UUID",
  "kind": "merge",
  "dependsOn": ["earlier-job-UUID"],
  "approvalId": "UUID",
  "reservationId": null,
  "snapshot": {
    "id": "sha256:…",
    "catalogDigest": "sha256:…",
    "preparedGeneration": {"package": "/nix/store/…", "profileToken": "HEX"},
    "evidence": [{"kind": "review", "path": "work/SESSION/review.md", "sha256": "HEX"}],
    "operation": {}
  }
}
```

`operation` is a strict tagged structure:

| Kind | Required operation fields |
| --- | --- |
| `merge` | registered `repository`, full `target`, registered `featureBranch`, exact `featureHead`, exact `expectedRemoteHead`, `expectedLocalTargetHead` (nullable only when no local target exists), `comparisonBase`, `patchDigest`, retained local `sourceRef`; shared-workspace flag derived by runtime |
| `machine_activate` | `target` ID, adapter-produced `preparedArtifact` ID, `expectedLive` identity, `coverage` list of repository/revision pairs, `configurationHead`; action fixed to `switch`, `reboot` fixed false |
| `profile_activate` | runtime-produced `preparedArtifact` ID, exact `candidatePackage`, `expectedProfileToken`, machine ID derived from catalog, source/input `coverage` |

The caller cannot choose worker executable, locks, output paths or runtime socket.
The runtime canonicalizes the snapshot and hashes it, verifies evidence digests
and retained sources, and stores its own accepted bytes. A metadata file pointing
at a mutable checkout is not an immutable snapshot. For jobs, require clean,
committed project sources and retain exact Git objects and detached preparation
checkouts outside the initiative worktrees. Preserve shared workspace tracking
changes by building the exact committed source revision separately. Profile
`--source` compatibility for ordinary local builds is described below.

Dependencies must name existing jobs in the same owner's graph, so insertion
order makes cycles impossible. Cross-session ordering comes from resources and
reservations, not references to another session's jobs. Duplicate dependencies
are rejected. Job success means verified operation result, not just process exit.
A failed/canceled dependency blocks downstream jobs visibly; it is never skipped.

`refresh` replaces only an unclaimed job's snapshot, with a new request ID and
expected revision. It records previous snapshot/result evidence, rechecks
approval and dependency requirements, and receives a new ready sequence. A
claimed/uncertain attempt cannot be refreshed. Material changes need renewed
approval; a patch-equivalent rebase records range-diff/patch-ID proof and fresh
verification without expanding the existing authorization.

## Scheduler and job states

Use one `workspace-coordinator.service` per user-profile runtime, not per
workspace. It runs a deterministic Ruby event loop from the selected profile,
uses a singleton `scheduler.lock`, reconciles existing attempts first, and wakes
on a state-change signal plus a bounded five-second fallback tick. Restart it
on failure; it takes no action when its package/profile token is superseded.
The loop does no long work itself. Spawn a bounded number of attempt services
(default four); notification delivery has a separate small bound (two).

Jobs use these states:

| State | Meaning and next transitions |
| --- | --- |
| `waiting_approval` | Concrete snapshot is stored; approval is missing/stale. No claim. Approval/refresh can make it eligible. |
| `waiting_dependency` | An earlier required operation has not succeeded. No claim. |
| `waiting_resource` | All other readiness checks pass, but a claim/reservation blocks this mutation. |
| `ready` | Complete snapshot, applicable approval, dependencies and ownership pass. Receives monotonic `readySequence`. |
| `claimed` | Ledger atomically assigns all execution resources and an attempt ID before launching anything. |
| `running` | Exact worker identity has acknowledged the immutable attempt request. |
| `needs_refresh` | Fresh baseline, source, catalog, generation, verification or approval snapshot differs. No mutation occurred; release execution claims and notify the owner. |
| `reconciling` | An attempt may have mutated state. Keep claims and reservation; inspect exact effects, never blind replay. |
| `succeeded` | Postconditions are proved and result persisted. Release execution claims; retain machine reservation. |
| `failed` | Definite failure with a proved no-effect or known settled effect; retain explicit outcome evidence. A deployment failure can still keep a blocker. |
| `canceled` | No future attempt may start. This does not undo a completed/possible mutation or release deployed ownership. |

Represent failure reasons and `retryAt` separately from state rather than adding
one state per external service. Automatic transient retries are restricted to
read-only reconciliation, pre-mutation availability checks, and proved never
started dispatch. Never use a process timeout as proof that activation did not
happen. `reconcile` can return to `claimed` only if the operation-specific proof
establishes that its original mutation did not start and no worker can still run.

FIFO is among jobs that are currently ready to claim a given resource, ordered
by `readySequence`, then job ID for deterministic ties. Waiting on approval,
missing dependencies, refresh or a foreign durable reservation does not block an
unrelated ready job. A job becomes ready only once every resource can be
considered; atomically claim its entire resource set, never hold one while
waiting for another. For competing ready sets, scan sequence order and grant
nonconflicting jobs in one ledger transaction. Keep earlier ready priority on
transient dispatch contention; refresh/new substantive preparation gets a new
sequence. The machine owner may run repeated jobs while a later reservation
waits: that is the expressly requested review ownership, not a FIFO violation.

Reservations are requested near first prepared deployment, not at initiative
creation. Requests for a free machine are FIFO by their own sequence. Grant only
when the owner has a ready first deployment snapshot and valid approval; a
partially prepared session cannot capture a free machine for days. Grant and
claim the first deployment atomically. A granted reservation then has no TTL.
An operator can see an old reservation but age is never release authority.

## Attempt workers, locks and self-deployment

Launch each mutation in an independent user-systemd transient **service**, named
from its UUID, with immutable store `ExecStart`, private request path, `UMask=0077`
and a separate cgroup. It must not be `PartOf`, `BindsTo`, or a child process in
the coordinator, portal, Codex or tmux service cgroup. Use `Restart=no`; a dead
attempt must be reconciled before a replacement starts. Retain its executable,
adapter and artifact closures through coordinator GC roots before dispatch.
A restart of the coordinator/router/portal does not stop an admitted worker.
A host reboot makes unresolved attempts reconcile; PID absence alone does not
prove that a remote mutation did not occur.

The claimed ledger record is the dispatch intent. A worker holds
`attempts/ID/worker.lock` for its lifetime and proves job ID, attempt ID, request
digest and its systemd unit identity. It writes only its own schema-1 phase/result
files atomically with fsync. The selected scheduler owns ledger transitions;
an old worker may finish its already admitted immutable attempt after a compatible
profile switch without becoming a general old-generation ledger writer.
Candidate compatibility must explicitly support that worker-result schema and
all still-running adapter protocols. A ledger claim missing a service is not
immediately recycled: inspect its unit, worker lock and attempt phase first.

Lock ordering for code that must hold physical locks is:

1. package `transition.lock` (shared admission, exclusive profile selection);
2. existing creation/session locks, when a session mutation needs them;
3. existing shared-workspace `dev-session-tracking.lock`, if needed;
4. coordination `ledger.lock`, held only for an in-memory state transaction.

Never acquire any earlier lock from inside `ledger.lock`. The scheduler selects
tentative candidates from a snapshot, releases the ledger, acquires necessary
outer locks nonblockingly, and revalidates the ledger revision/readiness before
committing a claim. Notification uses the same discipline with native submission
locks acquired only after the ledger lock is released. Worker locks are acquired
by the worker before publication and are never waited on while holding an outer
lock; readers only try-lock them to establish liveness.

Resource claims are durable logical exclusion, not OS mutexes held during builds.
Ordinary merge and machine activation take shared transition access only for
final generation/admission and the start-intent handshake. Their immutable
worker may then run without blocking unrelated package-independent resources.
A profile transition checks active attempts before selection and either supports
their exact continuation contract or defers. Same-machine profile/machine jobs
cannot overlap because they claim the same machine. Lifecycle commands honor
claims without waiting under locks. This avoids serializing all repositories
behind a machine's SSH command.

Profile activation still requires the exclusive transition lock for the actual
selection, link/service update and durable forward-recovery handoff. Do not
pretend this can be a millisecond transaction: service activation has real work.
Move builds, transfers, protocol probes, speculative health checks and long
post-activation tests outside. If a safe contract check must repeat under the
lock, bound it and measure it; if it becomes long, defer rather than run a new
build there. Keep the profile execution claim until postconditions finish.

## Merge execution and refresh

Preparation outside all mutation claims fetches the remote, rebases the owner's
feature branch, resolves conflicts, consolidates branch history, captures the
comparison, runs required review/checks/CI and retains the final head. The
coordinator does not run a rebase, edit code or decide whether a conflict is
semantically equivalent. It wakes the owner when those steps must repeat.

Immediately before mutation, prove the registration/common directory and remote,
feature head and source ref, applicable approval, evidence hashes, and exact
current local and remote targets. Fetch into operation-private refs outside the short local
tracking lock; under the claim, perform a fresh bounded `ls-remote` observation
and ancestry check. If the target advanced, return `needs_refresh` before any
local/default-branch change. A prior successful job or old cached origin ref is
not a fresh baseline.

For independent project repositories, prepare a private target worktree from the
recorded target and use ordinary `git merge --ff-only` with the retained exact
head. For the workspace repository, merge from the shared master checkout under
`dev-session-tracking.lock`; compare the local target with the prepared exact
local head after taking that lock, prove branch and index/worktree state, preserve
unrelated tracking changes, and fail on overlapping changes. Never reset, stash,
clean, stage unrelated paths or switch the shared checkout. Hooks retain their
normal behavior. A new tracking-only commit on local master invalidates the prepared local
baseline even if the remote has not moved; return `needs_refresh`, preserving that
commit and all unrelated edits. Do not run tests or builds inside the integration
claim.

Publish with a normal non-force SSH push of the exact head to the exact target.
Git's fast-forward check prevents losing a concurrent remote writer's work.
A remote writer outside this coordinator can still race the final observation;
rejection returns refresh/reconciliation, never a force push. Record local merge
intent, local resulting target, push intent and fresh remote proof separately.
After lost push output, a fresh remote head containing the exact feature head
proves integration; current unrelated/nonancestor state requires reconciliation.
A local fast-forward followed by failed push is retained, never automatically
reset. Reconcile it before granting that same target again. Feature refs stay.

Merge-only jobs have no machine reservation and run while another session holds
that machine. Multi-repository integration is an ordered job graph, not an
atomic transaction or a combined unmerged branch. Partial successful integration
is recorded honestly; no automatic history rollback is attempted.

## Machine reservation and deployment coverage

Reservation states are `requested`, `held`, `deployed_review`, `closing`,
`released`, and `blocked_recovery`. `held` becomes `deployed_review` on the first
proved deployment, including a deployment whose subsequent health check failed.
Repeated fixes transition jobs, not reservation ownership. `deployed_review`
continues through idle turns, user questions and browser closure. Unknown effects
use `blocked_recovery`. The UI may show a descriptive current phase such as
“Waiting for UI review”; that label does not drive ownership.

The reservation stores an append-only deployment history with exact source
coverage, toplevel/package identities, expected and observed baselines, attempts,
and integration obligations. Once deployment happened or might have happened,
`cancel`, archive, deletion, branch removal, agent stop, suspend or inactivity
cannot make the machine free. A successful subsequent activation does not erase
an earlier unknown operation until reconciliation establishes its disposition.

Normal `finish` request contains:

```json
{
  "schema": 1,
  "requestId": "UUID",
  "expectedRevision": 7,
  "deploymentWorkFinished": true,
  "evidence": "work/SESSION/state.md#deployment-acceptance",
  "finalHeads": [
    {"repository": "dev-workspace", "target": "refs/heads/master", "head": "40-hex"}
  ]
}
```

Before releasing, require all current registered feature obligations and every
recorded deployed source obligation to be covered by exact final heads; prove
those heads are included in freshly fetched configured remote targets; prove
there are no queued/running/uncertain jobs or delivery/recovery obligations that
could initiate more deployment; and reobserve the machine's last settled live
identity. The operator/lead declaration records that UI feedback and deployment
work are done; the runtime cannot infer human satisfaction from agent idleness.
A renewed fix before successful release clears closing intent. A later fix after
release must request a new reservation.

Early release before any deployment is allowed when all associated jobs are
proved unstarted and canceled. Releasing a deployed/unknown reservation without
integration is a separate explicit operator recovery action, requiring recorded
user direction and evidence that the deployed change was removed/superseded or
ownership deliberately transferred. Do not ship an unguarded `--force-release`.
The minimal release command may refuse this exceptional case and point to a
reviewed recovery procedure; it must not delete the blocker. An archived owner
can be revived for normal recovery, retaining the same reservation.

To prevent a later deployment from undoing earlier work, preparation records:

- exact configuration source commit and its freshly observed target baseline;
- effective package/input source revisions, resolved through installed mappings;
- machine's currently selected/live system and profile identities;
- machine's cumulative integration frontier from released reservations.

The adapter derives coverage from actual effective flake inputs/build metadata,
not a caller's unverified list. A prepared configuration must include its current
remote target baseline and every relevant released frontier head. For a package
input, prove the selected revision contains the required head in the canonical
repository; different commit hashes with equivalent patches do not prove lineage.
When rebasing an unmerged deployed feature, retain old artifact/source history
but record an explicit reviewed replacement mapping for that same owner's change;
a later session must contain the final integrated revision, not the abandoned
pre-rebase hash. Do not demand ancestry of rewritten, never-integrated feature
commits forever.

When A releases after integration, B's previously built snapshot is stale if it
lacks A's final coverage. B receives `needs_refresh`, updates its own branch/input
pins onto the integrated baseline, rebuilds and requeues. B may have merged its
own feature while A reviewed the UI. Neither A nor B deploys an invented branch
that combines multiple unmerged sessions. Baseline changes that do not alter the
resolved closure may reuse the already-built store artifact only after refreshed
source/coverage proof; do not assume the closure is unchanged.

## Confctl adapter protocol

Package `workspace-confctl-adapter` as an immutable extension command and refer
to it from the separate coordination catalog. It implements a strict schema-1
JSON request on stdin, one JSON result on stdout, and diagnostics on stderr.
No arbitrary command strings, patterns matching multiple machines, or optional
reboot flags are accepted. The concrete first target is a standalone NixOS
configuration with action `switch`. Carried-machine and coordinated node upgrades
are not supported by this first adapter; reject them explicitly.

```json
{
  "schema": 1,
  "operation": "prepare",
  "requestId": "UUID",
  "target": "aitherdev",
  "source": {"path": "/retained/private/source", "revision": "40-hex"},
  "attemptId": null,
  "preparedArtifact": null
}
```

Operations are `prepare`, `inspect`, `activate`, `reconcile` and
`transition-check`. `prepare` evaluates the exact configured selector in the
configuration's pinned Nix environment, builds its generation, resolves/retains
its JSON metadata and closure, and copies the exact closure to the target. It
may perform `dry-activate` under the owner's authorization; this does not select
the live system. Store copy roots independently from the source checkout. No
reservation is needed for evaluation/build; a dry activation on an owned target
must respect its reservation because it executes target-side code. For simplicity
perform dry activation after ownership is granted as a distinct preflight of the
same attempt, and keep its logs separate from final activation proof.

Preparation returns:

```json
{
  "schema": 1,
  "requestId": "UUID",
  "status": "prepared",
  "artifact": {
    "id": "sha256:…",
    "adapterProtocol": 1,
    "configurationRevision": "40-hex",
    "generationName": "2026-10-13--12-34-56",
    "generationDigest": "sha256:…",
    "toplevel": "/nix/store/…-nixos-system-…",
    "autoRollback": null,
    "coverage": [{"repository": "dev-workspace", "revision": "40-hex"}]
  },
  "observed": {"runningSystem": "/nix/store/…", "systemProfile": "/nix/store/…", "machineIdentity": "sha256:…"}
}
```

Generation metadata is parsed from confctl's supported JSON, not terminal output.
Use the pinned confctl library in that prepared environment to identify exactly
one generation and to perform its copy/activation/profile operations. Retain the
resolved environment executable/derivation with the snapshot. Do not repeatedly
enter an evolving `nix develop` or rebuild at activation. The extension wrapper
may launch a retained development-environment command assembled at preparation;
its executable is produced by the immutable adapter, never supplied by a job.
Confctl's current CLI provides `--generation` and `--copy-only`, but activation
must not perform a fresh build/copy implicitly. If implementing through the CLI,
prove by test that the selected path only activates the sealed named generation;
otherwise use the existing Ruby operations directly.

`inspect` reads both `/run/current-system` and the configured system profile via
the evaluated `MachineControl` endpoint and verifies the expected machine. It
returns exact identities with `observedAt`; SSH credentials never enter JSON.
Endpoint/protocol data comes from the evaluated configuration and installed target
mapping. Require agreement before mutation. NixOS activation can update the live
system before `set_profile` succeeds; comparing only one link is insufficient.

`activate` runs in the attempt worker, durably records start intent, repeats
`inspect`, and requires exact expected baseline. It uses the prepared toplevel
and preserves configured confctl auto-rollback behavior. Persist phase boundaries
before activation, after activation, before profile publication and after live
verification. Do not disable auto-rollback silently. A complete result is:

```json
{
  "schema": 1,
  "attemptId": "UUID",
  "requestDigest": "sha256:…",
  "outcome": "applied",
  "phase": "verified",
  "observed": {"runningSystem": "/nix/store/TARGET", "systemProfile": "/nix/store/TARGET", "machineIdentity": "sha256:…"},
  "error": null
}
```

Other outcomes are `not_applied`, `baseline_changed`, and `unknown`. A failed
command is not itself `not_applied`. Reconciliation distinguishes both links at
target, both at baseline, partially changed links and a foreign later target.
When live activation and profile publication differ, retain recovery ownership;
complete only the exact originally approved forward publication when the saved
phase and live state prove it is safe. A baseline-looking system after lost SSH
may reflect auto-rollback or a still-running activation. Prove the original
attempt is finished, including any rollback timer/process, before deciding
not-applied or retrying. Without that proof return `unknown`, retain ownership,
and expose operator recovery. First release may conservatively refuse ambiguous
remote outcomes; no remote daemon or distributed lease is required.

`transition-check` verifies that a candidate adapter understands all retained
artifact, attempt and reservation payloads without modifying the machine. A
protocol mismatch blocks package selection. Long health checks happen after the
activation result, outside global/repository locks, while the durable machine
reservation remains held.

## Profile preparation and activation

`workspace-host prepare --source PATH --json` resolves the real source, captures
its source identity/dirty digest and current profile token, builds exactly one
package, retains its GC root, validates metadata and performs expensive Codex
protocol/registration probes outside the transition lock. It returns a sealed
artifact containing source identity, candidate path, observed profile token,
registry/catalog digests, registration-plan digest, candidate native invocation
identity and probe evidence. The normal coordinated session path requires clean
committed source and verified coverage; the existing direct `--source` interface
can still prepare a local source snapshot, but records its exact Nix source
identity and must revalidate it rather than claiming Git ancestry it lacks.

`workspace-host switch --source PATH` remains valid and synchronous for callers.
Internally it prepares, then submits the fixed `profile_activate` operation and
waits for its durable result outside locks. If a foreign reservation blocks it,
it reports the owner/job and does not activate. An agent-facing coordinated
submission can return immediately; its existing conversation is notified when
refresh/action is needed or execution finishes. Do not put a sleeping shell at
the front of an execution queue while it rebuilds.

At activation, acquire the machine/profile execution claim and exclusive
transition lock, revalidate the complete profile token, registry, source and
catalog baseline, all existing lifecycle/cluster/runtime/provider gates, and
candidate coordination compatibility. Recheck native launch markers against the
prepared plans. If the exact native invocation is unchanged, preserve existing
live switch behavior: keep Codex/tmux and active conversations running. If an
idle cutover is required, mark waiting and notify; do not interrupt active turns
or hold the transition lock waiting for them.

Reuse the existing selection, pending-Codex-update, root retention, link install
and `_activate` implementation. Candidate `_activate` repeats coordination
compatibility and machine claim checks, so a pre-contract initiating helper
cannot skip them. The private activation request binds the exact attempt and
candidate; an environment boolean alone does not bypass reservation admission.
After selected profile replacement, failure always retains that forward target.
Retry/reconcile the same target or a compatible newer target; never restore an
older user-profile generation. Same-target recovery may bypass its now-obsolete
preselection token only through the exact admitted attempt and saved selected
identity, not a general ignore-generation flag.

Move final socket waits and long behavioral checks outside the exclusive lock
only after durable selected-generation/pending state is published and candidate
services own the stable commands. While that pending record exists, affected
commands honor its existing recovery restrictions. Preserve terminal restoration
and its explicit `dev-session sync` notice. The independent attempt service
survives restarting the coordinator itself; the new coordinator consumes its
compatible result. Do not make activation wait for that new coordinator to
process its own running job while it still holds the transition lock.

`--from-candidate` remains an explicit recovery entry. Its source build moves
outside the lock too; under the lock prove executing candidate equals the sealed
source output and that the observed selected profile has not changed. It runs
all existing and new gates. It is not a reservation or schema bypass.

## Automatic conversation delivery

Persist an outbox event in the same ledger transaction as a meaningful job or
reservation transition: ready-after-wait, refresh required, successful mutation,
definite failure, recovery blocker, reservation granted/released. Polling and
unchanged blockers do not create new events. Each event stores an immutable text,
exact owner thread, action context, native client message UUID, turn options and
payload digest. Coalesce only unsent events by a recorded rule; never change a
submitted event's text under the same UUID. Keep delivery state independent of
job outcome so a notification failure cannot cause mutation replay.

Add a private Go helper using `newCodexClient`/`workspacecodex.Client` and the
same selected registry/socket/submission ledger. Resolve the owner's current
retained model/effort and lead policy once for each event. Preserve existing
instructions; do not install a new role or choose a different model. Use
`ReconcileSendWithOptions` before retry and `SendWithOptions` for the exact
attempt. Busy recipients receive native steer; idle recipients get a new turn
on the existing thread. Existing recovery support may activate that exact cold
thread after durable admission; it never creates/replaces a conversation.

The message states the event, job ID, current result and stable portal URL, and
instructs the agent to reread coordination status, continue its own authorized
preparation and honor current approval scope. It explicitly states that the
event supplies no merge/deployment approval. It asks no human to resume and
does not pollute the user's composer or masquerade as a fresh user instruction.
Use action context `coordination:<owner-id>:<event-id>` and the saved UUID for
all native attempts. Store `SendReceipt` fields unchanged.

Transport failure uses persisted exponential backoff (1, 2, 5, 15, then 60
seconds). Reconcile automatically until the exact receipt is observable. Do not
change ID, message, settings or turn-kind assumptions to get around an ambiguous
attempt. A provider transition, pending lifecycle operation, archived/deleted
thread or different owner identity holds delivery; it does not authorize implicit
revival or wake a replacement session. Portal exposes held/unknown delivery.
After revival, only events still applicable to the same owner can resume.

**Known boundary:** selected codex-web marks a send `submitting` before the RPC.
If the process dies before the RPC reaches native Codex, history absence cannot
prove whether native admission occurred. `ReconcileSendWithOptions` returns
`UnknownSendOutcomeError`, and `SendWithOptions` intentionally refuses replay.
This supports retry-safe observable completion, but not an unconditional eventual
wake guarantee after every possible crash. Preserve automatic reconciliation and
visible unresolved status. Do not claim exactly-once eventual delivery from a
client UUID alone. If the user requires that stronger guarantee, first prove the
selected native start/steer API's durable idempotency contract with a native test;
only a demonstrated capability gap justifies a narrowly scoped codex-web change.
No local ledger or new message UUID can safely solve that ambiguity. This is a
material review/acceptance limitation, not permission to ask users to resume
ordinary waiting jobs.

## Lifecycle, package contracts and recovery

Add a separately versioned installed coordination contract, mirrored by additive
runtime metadata:

```json
{
  "schema": 1,
  "ledgerSchema": 1,
  "snapshotSchema": 1,
  "attemptSchema": 1,
  "adapterProtocols": [1],
  "notificationSchema": 1,
  "transitionPolicy": 1
}
```

Do not change session manifests, creation/lifecycle journals, Codex submission
ledger or roster formats merely to add coordination. They continue to own their
existing identity/recovery contracts. Candidate package preflight and candidate
activation both read the full coordination inventory. A target lacking support
refuses whenever retained coordination state/obligations exist. No downgrade to
an old binary that ignores the state is supported. Compatibility is a declared
schema/policy plus validation of actual pending records and immutable adapter
availability, not just a larger version number.

Every stable command captures its originating profile token and validates it
after acquiring its admission lock. Never accept a stale waiter because the
candidate resolves to the same package path. A claimed attempt is a distinct,
explicitly admitted continuation with its own ABI and immutable sources; it may
finish only that attempt. New-generation scheduler adoption validates that ABI
and cannot reinterpret it as a fresh operation. No lossy automatic journal
migration is needed in release one. Unknown schema blocks writers, dispatch,
release and transition, while a bounded read-only error remains visible.

Before an explicit archive/delete writes its lifecycle journal, atomically fence
new coordination admissions for that owner under existing session locks. Cancel
only jobs proved unclaimed/unstarted. If a running or uncertain mutation exists,
refuse/defer lifecycle mutation with its concrete job ID until it settles; do not
kill deployment workers as if they were agent children. After definite settling,
archive/delete can proceed under their existing policies, leaving any deployed
reservation as `blocked_recovery` and holding unsent notifications. Independent
source refs, preparation snapshots and GC roots survive worktree removal. Tie
the fence to the exact lifecycle operation identity; retries resume it, and
revival clears it only after ordinary lifecycle completion. An interruption
between coordination fence and lifecycle journal must be recognized as a prepared
lifecycle intent, resumable by that same command, not an orphan automatically
released on timeout.

Automatic archival treats pending jobs, unresolved notifications, any held or
blocked machine reservation, and incomplete coordination lifecycle fences as
concrete blockers. It must not archive a session merely because all branches
merged while its UI review remains open. Poll/status/notification retries do not
advance inactivity; an actually delivered Codex turn contributes normal native
activity under existing observation rules.

Workspace unregister refuses outstanding jobs, reservations or unresolved owner
recovery for that workspace. Suspension fences scheduling and delivery, preserves
the ledger and blockers, and refuses to tear down services needed by active
attempts. It never grants a waiting session another owner's machine. Codex
reconciliation/provider switches defer notification submission through existing
admission, preserve exact outbox identities, and cannot erase queued delivery.
Package switches may coexist with held reservations only for their owning
initiative on the mapped local machine; compatible workers on unrelated machines
can continue under the explicit attempt contract.

Retain source objects, generation metadata, prepared environments, candidate,
worker and adapter closures until the job and any reservation/recovery that
references them are settled. Terminal job cleanup alone cannot remove a deployed
reservation's recovery source. Explicit archive/delete retains those roots.
Pruning needs a separate checked reachability walk and is deferred from release
one; Nix GC must not invalidate a pending job between preparation and activation.

## Portal and agent procedure changes

Expose authenticated read-only `GET /api/coordination` for the registered
workspace and `GET /api/sessions/<slug>/coordination` for its owner. Return bounded
JSON with job state, sequence, kind, exact source/result identities, dependencies,
blocking owner/portal URL, machine reservation/review phase and delivery state.
Include a summary of foreign blockers, not their private paths or evidence.
No GET performs reconciliation or mutation. Existing origin/authentication rules
remain in effect for any future write route.

Show a small Operations panel in the session and workspace views: queued,
preparation needed, running, UI review ownership, completed, recovery required.
Provide the blocking session link and concrete next action. A machine must never
look available because its owner's agent is idle. Do not show “ready for use”
solely from mutation success; show deployment health/review evidence separately.

Update workspace Git/deployment/lifecycle/verification procedures and relevant
skill guidance to prepare independently, submit only under existing approval,
use exact registered resources, respond to coordinator events by rereading state,
and finish reservations only after final integration plus deployment acceptance.
Use the required writing skill for visible copy after technical facts settle.
Keep generic contracts and recovery in a linked `dev-workspace` coordination
guide; adapter operations in the extension; concrete aitherdev instructions in
configuration/workspace docs; this rollout's exact revisions and evidence in
initiative records. Do not freeze live coordination status into AGENTS.md.

## Bootstrap and aitherdev rollout

Before deployment, review and test the final committed implementation, publish
feature branches, select exact runtime/extension revisions in the workspace and
matching `devWorkspace` revision via configuration's confctl channel. Preserve
the nested runtime override and unrelated locks. Run
`bin/check-dev-workspace-deployment` against those final source locks. Do not add
the application package to the system configuration.

Bootstrap has a genuine trust boundary: the currently installed runtime does not
know about coordination, and this initiative was deliberately created threadless.
Neither fact can be solved by inventing a Codex owner. Use an explicitly recorded
one-time bootstrap operation from the reviewed candidate:

1. Complete preparation/builds outside the old transition lock. Verify registered
   workspace identities, live systems/profile, pending lifecycle/provider state
   and active session safety. Check with the lead for existing deployment work;
   do not import other sessions as owners from guessed activity.
2. Under the normal transition lock, enter the candidate's explicit bootstrap
   mode and install schema-1 state with this exact initiative as a **threadless
   bootstrap owner**, its recorded deployment approval and a held aitherdev
   reservation. Refuse preexisting unexplained coordination state. This owner has
   no notification destination and cannot enqueue unattended waiting work.
   Its caller observes the synchronous result; the exception is visible in status.
3. The candidate's independent worker runs the prepared no-reboot configuration
   activation through the adapter, then the prepared profile activation as an
   explicit dependent operation. Preserve forward-only profile recovery and
   current live-switch checks. While pre-contract commands still exist, the lead
   uses only this bootstrap path and records that old unmanaged writers remain
   outside the coordinator; no claim of retroactive enforcement is made.
4. After selection, start the profile-wide coordinator, verify it reads/adopts the
   original reservation and bootstrap results, and verify router/portal/Codex/tmux
   continuity and selected runtime/host-module agreement. Keep the aitherdev
   reservation throughout human UI review. Do not mark the initiative complete
   or release its machine without the later integration approval/proof.

The bootstrap command is private, candidate-only, requires explicit `--source`,
expected installed profile token, exact selected workspace/slug, and the approved
prepared deployment request. It cannot create a persistent lead, infer another
thread or import unrelated deployments. A repeated identical bootstrap recovers
its original operation; a different request colliding with existing state fails.
Do not implement a public general-purpose `--no-notify` escape for autonomous jobs.
If deploying host configuration before bootstrapping state is operationally
required, record that one pre-contract activation explicitly and import its exact
observed receipt under the same one-time maintenance window before profile
selection; never describe the earlier action as coordinated.

This bootstrap exception is bounded to first installation. Ordinary managed
sessions thereafter must have existing proven thread identities for automatic
continuation. The present initiating conversation has no retained root binding
in this threadless session; adding one would require a separately supported,
explicit ownership-binding operation and is not part of this design.

No service/node protocol, application database or cluster-state conversion is
planned. No coordinated update of running vpsAdminOS nodes is required. All
changes are runtime-local except the approved aitherdev configuration activation.
Recover package failures forward to the same/newer compatible reviewed package.
System configuration recovery follows the approved configuration procedure and
keeps the reservation until both actual system/profile identities are settled.
No reboot or default-branch integration is part of this rollout.

## Meaningful verification and implementation order

Implement in these reviewable units, keeping the public schema stable across
units: (1) catalog/ledger/identity/state machine, (2) worker execution and Git
integration, (3) reservation/coverage and confctl adapter, (4) profile split and
lifecycle/package gates, (5) notification/portal/procedures, (6) composition and
rollout. No temporary unsafe executor or no-op lifecycle gate should be deployed.
Use source-level fixtures until all gates are implemented; preparation design
alone does not justify activation.

Quick deterministic tests before mandatory review:

- Two subprocesses race admission/refresh/cancel; one atomic winner, monotonic
  sequences, exact idempotent retry, corrupt/unsupported/oversized state fails
  closed, disk-write failure leaves the previous committed ledger usable.
- Ready FIFO per resource; unavailable approval/dependency and a foreign machine
  do not block unrelated repository/machine work; all-resource claims prevent
  deadlock; stale refresh cannot replace a running/unknown attempt.
- Local bare Git fixtures prove two simultaneous ready merges: first integrates,
  second detects advanced target and wakes its owner; patch-equivalent refreshed
  second head integrates. Include non-FF external advancement, lost push reply,
  local-merge/push failure and shared workspace dirty tracking preservation.
- A deploy-first A retains aitherdev through success, UI review, idle, agent stop,
  feedback and several redeployments. B builds and merges independently; B's
  machine and profile activations remain blocked. Final-head proof without
  deployment completion, and completion without integration, both refuse release.
- After A releases, B's older input/closure coverage fails refresh; cumulative
  refreshed B can deploy. Rebased pre-merge feature lineage uses recorded final
  integration coverage without requiring obsolete hashes as ancestors forever.
- Adapter fixtures assert build/copy only occur in preparation, exact named
  generation/store identity in activation, selector resolves one permitted
  machine, no reboot/carrier path, auto-rollback preserved, both live/profile
  links inspected, partial/unknown SSH outcomes keep reservation and claims.
- Slow profile-build/probe fixture proves ordinary session admissions and
  unrelated ready jobs continue; generation changes during preparation or lock
  wait reject activation. Test same-target forward recovery after `nix-env`
  changes the profile and reports failure. Candidate activation repeats gates.
- Kill coordinator and portal during attempts; independent worker continues.
  Kill worker at each write-before-effect/effect-before-receipt boundary and
  prove exact reconciliation or a persistent blocker, never duplicate mutation.
- Lifecycle fencing races with admission; explicit archive/delete cannot remove
  a running attempt's source or release deployed ownership; revival retains its
  blocker; automatic archive refuses review reservations; unregister/suspend and
  candidate schema/adapters reject incompatible pending state.
- Notification fake server covers idle start, busy steer, exact owner isolation,
  retained settings, stable ID across retry, lost response with observed native
  receipt, provider/lifecycle holds, no replacement thread and no implied approval.
  Explicitly test the submitting-before-RPC ambiguity remains unresolved safely.
- Catalog/path tests prove alias equivalence and collision rejection, same
  machine/profile exclusion across two registered workspace roots, and no
  executable/resource/SSH injection through session JSON. Test ordinary remote
  client authorization; do not invent hostile-local-admin filesystem tests.
- Portal fixtures show foreign blocker link, held UI review during idle, delivery
  failure separately from mutation success, stable bounded read-only responses.

Run the repository Nix environments and declared focused Ruby/Go/JavaScript/Nix
checks. Do not add tests that merely duplicate schema implementation; exercise
observable concurrency, recovery, attribution and non-mutation behavior. Record
which fast checks ran and the exact final heads. Complete whole-branch history,
pin-stream consolidation and migration-lineage inventory for independent review.
There are new versioned private files, but no migration of existing session or
Codex formats; review must verify that statement against the final diff.

Only after final committed-deliverable review and reconciliation, launch longer
checks through the required fresh Luna/low watcher:

1. Full package checks and NixOS/user-systemd integration, including real transient
   service survival through self-profile switch and restart/reboot reconciliation.
2. Native selected-Codex start/steer receipt test with a held/lost transport reply;
   assert one observed notification and no new conversation. Report unresolved
   pre-RPC ambiguity honestly; do not weaken the test to prove only mock behavior.
3. End-to-end two-workspace scenario with actual local Git remotes, blocked
   deploy-first reservation, simulated human review, B merge, A repeat deployment,
   final integration/completion, automatic B refresh wake, and cumulative B deploy.
4. Configuration build and dry activation, no unexpected local kernel build,
   deployment-contract check, approved no-reboot aitherdev activation and user
   profile switch, then live status/continuity/ownership checks. Keep long build
   logs with their sources and artifact identities.

Acceptance requires independently evidenced implementation, local checks,
independent review, integration checks, deployment and human UI review phases.
Successful rollout alone does not make feature branches integrated or release
this initiative's machine reservation. User-facing handoff links the stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-13-workspace-coordination/.

## Decisions requiring explicit lead attention

- Accept the safe delivery boundary above, or separately establish native durable
  start/steer deduplication before promising wakeup through every crash window.
  Existing codex-web APIs do not by themselves provide that stronger guarantee.
- The threadless initiative needs the bounded, visible synchronous bootstrap
  owner; it must not be given a fabricated existing conversation identity.
- Short locks mean no preparation under them. Actual SSH activation, service
  selection, hooks and Git push still take time. Unknown outcomes retain durable
  claims rather than sacrificing recovery to a lock-duration target.
- Confctl auto-rollback and split live/profile publication require conservative
  reconciliation. If the existing library cannot prove a remote attempt ended,
  retain the blocker; do not introduce a new distributed execution service just
  to make the first implementation claim automatic recovery in every case.

These are concrete compatibility/trust boundaries. Any implementation deviation
that weakens ownership, approval, generation fencing, source retention or
unknown-outcome handling returns to the lead/design review before deployment.

## Implementation refinement: ownership, admission and completion

This addendum resolves the lead's bounded follow-up questions after inspecting
`workspace-coordination-host.rb`, `workspace-coordination.rb`,
`workspace-coordination-execution.rb`, and the extension's confctl adapter.
It refines the preceding contract where more precision is needed. This is design
completion, not final independent review or evidence that implementation passes.
Only the design document was edited by the designer.

### 1. Existing threadless bootstrap owners can finish and recover

Separate **loading an existing owner** from **creating/admitting a new owner**.
The current `Engine#owner` combines them and normally requires a thread; calling
it with `bootstrap: true` from ordinary commands would also permit owner creation.
Do not use that as the public recovery entry.

Add `--bootstrap-owner UUID` to the existing session `status`, `reconcile`,
`cancel`, and `finish` forms only. For example:

```text
dev-session --workspace vpsfree-cz coordination reconcile SESSION JOB \
  --as-is --bootstrap-owner OWNER_UUID --json
dev-session --workspace vpsfree-cz coordination finish SESSION RESERVATION \
  --as-is --bootstrap-owner OWNER_UUID --request finish.json --json
```

The selector is an explicit request to manage an already recorded bootstrap
owner; it is not authority to create a threadless owner, waive approval or enqueue
unattended work. The implementation uses a read-only `existing_owner` lookup and
requires all of the following under normal current-generation/session admission:

- The owner exists, has `bootstrap: true` and `thread: null`, and its exact
  workspace root, registry identity and slug match the selected invocation.
- The ready active tracking and retained creation/deletion incarnation match the
  saved owner. A same-name replacement directory is not that owner. Preserve
  existing threadless absence checks; a new manifest thread, conflicting runtime
  authority/team or a lifecycle fence refuses this path.
- The job/reservation named by the command belongs to this owner. Normal revision,
  idempotency, worker-liveness, unknown-outcome and finish proofs remain unchanged.

Do not silently choose the sole bootstrap owner when the normal threaded lookup
fails. Do not add a general `--bootstrap` or `--no-notify` flag to `submit` or
`approve`. The selector cannot convert another owner into bootstrap mode and
never creates an outbox event with an invented thread ID.

`reconcile` may finish the exact previously admitted forward profile operation
or settle an existing machine attempt under its original authority. It cannot
select a different artifact. `cancel` retains its current limitation to proved
unclaimed jobs. `finish` does not merge anything: it verifies already integrated
heads and declared deployment completion. Therefore a bootstrap owner can release
normally after the user later authorizes integration and those integrations
actually occur, without ever acquiring a Codex thread.

Keep ordinary finish/recovery restricted to active tracking. An archived owner
must be explicitly revived through its existing lifecycle before using this
path. A deleted owner retains a visible blocker for the separately authorized
operator recovery procedure; a newly created same-slug session cannot claim it.
Changing this exception to create new deployment jobs after bootstrap would be a
separate design change. Normal threaded sessions retain repeated deployment
support; recovery of the original bootstrap pair is already in scope.

### 2. Synchronous switch submits a retained approved snapshot internally

Keep `workspace-host switch --source PATH`. A caller need not pre-submit the job,
but must already have the exact deployment approval and reservation. Invocation
of `switch` is not an approval record. A reservation's machine approval alone is
also insufficient if it covers only system `switch` and not `profile_activate`.

Persist the exact canonical value produced by `prepare_snapshot` in a private
content-addressed `snapshot.json` before returning it. Reuse the existing source
artifact store and digest rules; this is a small retained descriptor, not a new
workflow service. `approve` resolves `reviewedSnapshot` to this saved descriptor,
validates its owner, immutable artifact and evidence, and retains that binding.
A syntactically valid SHA without a saved prepared snapshot is insufficient.
The recorded snapshot does not lose its original bytes when its baseline later
becomes stale; it simply becomes ineligible to execute.

The synchronous wrapper follows these steps:

1. Resolve the normal proven owner and canonical `profileMachine`. Prepare the
   source/build/probes outside locks as now. Find the owner's nonreleased
   reservation for **that exact machine**, including `requested` when this is
   its first approved deployment. A reservation for another machine cannot match.
2. First reuse an exact matching previously submitted job, preserving its saved
   approval, dependency graph, snapshot and attempt. In particular, a running or
   uncertain operation is reconciled, not duplicated under a new request ID.
3. Otherwise resolve an existing approval to its retained profile snapshot and
   artifact. Compare the newly prepared result with that artifact on the complete
   semantic identity: source repository and exact source revision/content digest,
   effective coverage, candidate package and native executable, expected profile
   token, catalog, registry and registration-plan digests, and mapped profile
   resource. An equivalent source checkout path may differ; a source revision,
   coverage, baseline or evidence difference may not. Use the original sealed
   artifact and snapshot for execution after the comparison, so approval remains
   attached to the bytes it approved.
4. Validate current evidence and generation, then apply the same `approved?`
   predicate used by ordinary jobs. Do not derive fresh review evidence, copy an
   `iterationScope` string onto an unrelated new snapshot or create an approval.
   For iteration approval the particular prepared snapshot must already carry
   the approved change scope and current review evidence. The wrapper cannot
   classify an arbitrary new source as belonging to that scope.
5. Under ordinary session admission, atomically find-or-submit the exact job via
   the existing submit path. Derive its stable request UUID from a versioned tuple
   `(ownerId, reservationId, snapshotId, approvalId, profile_activate)`; recompute
   and recheck the tuple in the transaction. Concurrent identical switch calls
   return one job. The persisted request bytes and receipt use normal exact-retry
   validation. No private bypass of mutation approval or resource scheduling.
6. Wait for that job outside transition/session/ledger locks. Display its ID,
   blocking owner and portal URL. A stale or refused snapshot returns the normal
   actionable status. A lost caller connection does not cancel the admitted job.

Minimal dependency rule: when reusing a job, keep its dependencies exactly. When
creating a new synchronous job, use an empty dependency list only if no other
nonterminal deployment job for this owner/reservation exists. If such a job exists,
require the existing explicit submit workflow to state the intended dependency;
do not guess deployment order or silently skip a pending configuration operation.
The bootstrap command continues to create its explicit machine → profile graph.

For unambiguous selection, optional `--approval ID` and `--reservation ID` may
narrow the candidates without changing `--source` compatibility. With no flags,
require a single matching snapshot/reservation; multiple approvals of the exact
same snapshot and identical effective scope can choose a deterministic retained
ID. Conflicting applicable snapshots/scopes are an error, never “latest wins”.
No matching approval returns the prepared snapshot ID and explains that approval
must be recorded through the normal command; it never activates on failure.

A previous `succeeded` job is an idempotent success only when its full observed
profile token and package still match live state and the requested source matches
its artifact. Package-path equality alone cannot certify a new switch. A changed
baseline requires fresh preparation/approval applicability. `--from-candidate`
keeps its exact candidate-source and original admitted-attempt checks; it cannot
turn this convenience wrapper into a new owner or approval source.

### 3. Integrated inputs do not become fictitious feature registrations

The current finish implementation sends every coverage entry through
`registration(owner, repository)`. That confuses a deployed upstream input with
an initiative-owned feature branch. Keep these proof categories distinct while
retaining both in the release decision:

| Category | Required proof |
| --- | --- |
| Owned feature obligation | Exact final feature head from the current registration, plus every frozen reservation/admission obligation, is contained in its configured remote target. |
| Unowned integrated coverage | Each actual deployed input revision is already contained in that repository's explicitly configured default target; no feature registration or invented branch head is required. |

Add an optional full-ref `defaultTarget` to catalog repository entries, such as
`refs/heads/master`; it becomes mandatory whenever that repository participates
as unregistered coverage. Verify real default-branch selections while authoring
the site catalog. Never guess `master`, trust a stale `origin/HEAD`, or accept a
caller-provided target to resolve missing configuration. Registered obligations
continue to use their own recorded `default_branch`; a configured catalog default
must not overwrite an explicitly registered release-branch target.

Use the catalog's canonical SSH remote and canonical workspace bare clone
(`repos/<catalog-repository-id>.git`, with the special shared workspace root).
Validate Git common-directory/remote identity. Do not borrow another initiative's
worktree or branch. A missing clone or missing exact object is a proof failure
with a concrete remediation, not permission to omit that coverage. Remote reads
and fetches occur outside the ledger mutex, retaining ordinary generation/session
admission and a final ledger revision comparison.

Fetch the exact full target into an operation-private proof ref and record its
fetched commit. Prove `is-ancestor(deployedRevision, fetchedTargetHead)` for each
unowned coverage revision. This demonstrates integration of the deployed input;
it does **not** require the deployment to use the current latest upstream commit.
If a covered revision is unmerged, it must be an actual owned feature obligation
or release refuses. Missing registration cannot hide a deployed feature belonging
to another session.

Freeze the applicable repository identity, target and whether it is an owned
feature obligation when admitting deployment. Union those facts with current
registrations at finish. Removing a registration later never downgrades a frozen
owned obligation to unowned input coverage. Unregistered coverage uses its sealed
catalog default target; a later catalog retarget requires explicit refreshed
proof, not silent reinterpretation of history.

`finalHeads` continues to contain the exact **owned** feature heads supplied by
the caller. The runtime derives unowned coverage proofs; users do not fabricate
`finalHeads` for unchanged inputs. Save both categories, including observed
remote target heads, in completion evidence. Duplicate `(repository, target)`
proofs with conflicting values refuse rather than picking the first array entry.

Update the machine frontier by deployment kind using the owned final head after
valid lineage resolution, and the actual unowned deployed input revision after
its ancestry proof. Do not put the fetched latest default tip into the frontier
for an older unchanged input: that would claim undeployed changes and require
later sessions to pick up unrelated new upstream work. Preserve all required
coverage entries when the same repository has multiple effective input revisions;
never use `find` to silently discard the others. A later deployment must cover
all applicable frontier heads or demonstrate that one descendant covers them.

### 4. Replacement lineage is an exact reviewed relation

Retain the existing inline `finish.replacements` interface, but strengthen its
meaning. A generic nonempty review artifact plus arbitrary `from`/`to` hashes is
not enough to classify a rebase. Use a small explicit tuple:

```json
{
  "repository": "dev-workspace",
  "target": "refs/heads/master",
  "from": "DEPLOYED_HEAD",
  "fromBase": "OLD_REVIEWED_BASE",
  "to": "EXACT_FINAL_HEAD",
  "toBase": "NEW_REVIEWED_BASE",
  "relation": "patch_equivalent",
  "approvalId": "EXISTING_APPLICABLE_MERGE_APPROVAL",
  "evidence": {"kind": "review", "path": "work/SESSION/rebase-review.json", "sha256": "HEX"}
}
```

The referenced bounded JSON review receipt contains schema 1, owner/reservation
identity, the exact same tuple (excluding the evidence pointer), `decision:
"accepted"`, the independent reviewer's recorded identity, and references/digests
for the actual range-diff, verification and migration-lineage assessment. It may
reference a normal Markdown review rather than duplicating its prose. Validate
its exact tuple and digests; do not infer reviewer authority merely from a name.
The trusted lead attests that this is the independently reviewed result under
the existing review procedure. A transport/cryptographic identity system for
reviewers is not being added.

For every mapping require that `from` was actually recorded in this reservation's
owned deployed-source history, both bases/heads are retained exact commits in
the same canonical repository, bases are ancestors of their respective heads,
`to` equals the current exact final feature head, and `to` is included in the
freshly fetched same configured remote target. The mapping can discharge only
that owner/reservation/repository/target relation. It cannot discharge unowned
input coverage, another session's source, an unknown attempt, or another target.

Support these two relations only:

- `patch_equivalent`: a clean rebase/consolidation preserves the reviewed patch
  and migration behavior. Recompute retained range comparison/patch evidence,
  require the independent review receipt and appropriate fresh checks. The
  existing repository/target approval may remain applicable under the Git
  procedure. Byte equality of raw diffs is not required across different bases;
  neither branch-name equality nor same commit subjects are proof. For the
  mechanically provable case compare ordered stable patch IDs of ordinary
  nonmerge commits and retain range-diff; unsupported/ambiguous histories cannot
  silently receive this classification.
- `reviewed_change`: conflict resolution or other substantive changes produce a
  reviewed replacement. Require a newly recorded user integration approval that
  binds the new reviewed snapshot, plus the explicit replacement assessment of
  persisted/deployed compatibility. If the resulting change materially differs
  from the last accepted deployment, require a later successful deployment
  covering the replacement, under its applicable deployment approval, before
  declaring deployment work finished. Do not use lineage metadata to waive UI
  acceptance, deployment work or renewed approval.

Prefer a direct mapping from every nonancestor deployed revision to the final
head. Several earlier deployments can share one review receipt containing
several exact mappings. Do not add a generalized transitive equivalence graph.
Reject cycles, duplicate conflicting mappings, unused mappings and mappings to
intermediate rather than final heads. An ordinary ancestor relationship needs
no mapping. Freeze accepted mappings with the completion receipt, while retaining
all original deployed heads/artifacts/GC roots needed by supported recovery.

A reviewed equivalent rebase does not require deploying solely to change commit
IDs if closure behavior and supported migration/recovery behavior are unchanged;
that conclusion belongs in the review evidence. Rewriting a source commit never
erases the fact that its migration or artifact was deployed or externally
consumed. Preserve that supported boundary and any necessary exact source ref.

### 5. Bound diagnostic output without discarding recovery authority

The current generic and adapter `capture` helpers use `Open3.capture3`, which can
buffer arbitrary build/activation output. Replace that usage on potentially long
commands with one small shared streaming runner in each owning component; do not
add a logging service or retain every output byte in ledger JSON.

Use two explicit modes:

- **Protocol capture:** bounded stdout with strict complete parsing. Default
  256 KiB, or a separately named existing larger contract where required (for
  example the prepared Nix environment). Git ref/path outputs can use a smaller
  bound. On overflow report a protocol error; never parse a truncated JSON object
  or use a truncated diff as evidence. Hash large Git comparison streams
  incrementally where their complete digest is needed.
- **Diagnostic streaming:** drain stdout and stderr concurrently in fixed-size
  chunks, retaining at most 4 MiB per preparation/attempt: 1 MiB of the beginning
  and 3 MiB of the tail, with stream labels and a truncation marker. Keep byte
  counts and a full-stream digest if useful. After the cap, continue draining;
  reaching a log limit must not kill an activation or create a pipe deadlock.

Request/phase/result/approval/snapshot files remain complete, bounded and fsynced;
logs are never outcome authority. Error messages copied into the ledger or portal
are sanitized valid UTF-8 and bounded to 4096 bytes. Private log files use mode
0600; stdout for adapter protocol remains reserved for its one JSON result, with
diagnostics routed separately. Do not emit environment dumps, SSH credentials or
secrets. Do not emit full child output again through the worker's systemd journal;
log only short attempt/state summaries there. Loss of logging after mutation
starts must not erase the claim: finish/write the bounded result when possible,
or leave the exact attempt for reconciliation.

For release one, retain admitted request/phase/result records, idempotency
receipts, completion/lineage evidence, referenced source objects and Nix roots.
There is no age-based deletion of ownership, approvals, uncertain attempts or
source/artifact roots. This deliberately bounds each log and ledger admission,
not the total lifetime size of source closures. State that distinction honestly.
Use a 1 GiB free-space floor before new preparation/admission, keep the ledger's
2 MiB recovery reserve, and refuse new work visibly when either is exhausted.
Do not discard an old unresolved reservation to reclaim space. Completed
non-authoritative logs can be removed only through a later explicit checked
cleanup; automatic general source/GC-root pruning remains out of scope.

### Focused acceptance checks for these refinements

Add meaningful tests to the existing focused suites:

- A retained bootstrap owner can reconcile and finish under the explicit selector;
  missing/foreign/recreated owners and attempts to use that selector for new
  unattended jobs refuse. No thread or notification is invented.
- An approved retained profile snapshot plus the exact machine reservation lets
  two synchronous callers create exactly one job; a missing approval, changed
  coverage/evidence/token, wrong machine and ambiguous snapshot refuse. An existing
  dependency graph is retained. `--source` performs real submission, not just a
  lookup for an already queued job.
- A deployment containing a registered configuration feature and an unchanged,
  unregistered integrated runtime input can finish. An unmerged unregistered
  input, removed owned registration, wrong remote/default target or missing object
  prevents release. The frontier records the actual unchanged input, not a newer
  remote tip that was never deployed.
- Clean rebased deployed sources discharge only exact reviewed mappings. Random
  review text, swapped range endpoints, foreign ownership, wrong target, stale
  evidence and a material change without fresh approval/deployment fail. The
  pre-rebase artifacts remain available.
- A child writing more than the log bound to both pipes finishes without deadlock
  or unbounded memory. Complete protocol output is validated separately; overflow
  cannot produce a success receipt from truncated bytes. Low-space admission
  refuses new work while existing recovery records remain writable.

## Final-review remediation amendment

This amendment resolves the design choices raised by findings 1–10 and the two
recovery advisories in [the final review](final-review.md). It is a design brief,
not verification or acceptance of the lead's fixes. The runtime, adapter and
installed-policy paths were inspected while those fixes were in progress. The
lead owns application edits, regression checks and the independent re-review.
The three mutation kinds, user approval boundary, no-reboot rollout and absence
of default-branch integration approval remain as previously specified.

### 1. Registration reconciles the selected package

Keep ordinary `register` and `register --replace` as host configuration commands.
They do not create a fictitious deployment job. Under the originating generation's
exclusive transition lock, preflight the intended registration and coordination
admission before writing the registry. Refuse if the selected package has pending
activation recovery, a claimed profile operation or a held reservation on its
mapped machine. Validate the existing lifecycle/cluster/provider contracts before
an otherwise predictable activation refusal can leave a changed registry.

Give the private activation entry an explicit registration-reconciliation mode
carrying the full selected profile token. That mode must prove that its executable
is the already selected, settled package and repeat coordination admission. It
may configure that package's services; it cannot select a profile, waive a profile
attempt, or accept an unselected candidate. The ordinary candidate path retains
its exact claimed `profile_activate` check. A private environment marker is a
dispatch mode under the trusted-local-operator model, not an authorization secret.
Unexpected service failure must retain a clear retryable registration outcome;
the new admission path must not imply that registry writes and systemd are atomic.

### 2. Suspension has explicit forward recovery

Add `workspace-host resume`, using the same originating-generation check and
exclusive transition lock as suspension. It resumes the selected package without
waiting for the scheduler to grant a profile operation. Suspension must refuse
admitted/uncertain attempts before tearing down their services, preserve queued
jobs, claims, reservations and exact outbox records, and durably pause scheduling
before service teardown. Ordinary service activation must not silently unpause it.

Resume validates retained coordination and lifecycle state, restores selected
services and their native registration, and clears `suspended` only after those
steps succeed. Partial resume leaves the pause visible and the same command
retryable. Suspension failure compensates every service change already attempted,
including automatic-archive and reconciliation services stopped before the ledger
flag was written. Restore the prior suspension value only when compensation is
complete; otherwise preserve a visible pause and direct recovery to `resume`.
An exact retry must neither drop pending jobs nor release a held machine.

### 3. Completion belongs to an exact selected generation

Expensive socket/native observation can remain outside the transition lock.
Before deleting pending recovery or restoring terminals, reacquire the lock and
check the full postselection profile token, selected package, and saved pending
operation evidence. A coordinated completion additionally belongs to its exact
attempt. Same native registration semantics or package-path equality alone are
insufficient. A superseded completion returns a retryable error and leaves the
new generation's recovery and clients untouched.

The default empty-catalog path requires the same protection. If an operation
cannot be distinguished safely, keep its completion serialized. A missing pending
file is acceptable only when the exact generation is already reconciled; it is
not proof that an arbitrary later transition finished. Preserve the existing
pending-record format rather than adding fields casually to a published contract.

### 4. Lifecycle completion is journaled through coordination finalization

Use the ordinary archive/delete/revive journal's exact `operation_id` as the
coordination binding. A small `lifecycles` collection in the new coordination
ledger records workspace, slug, command, frozen `{ownerId, identity}` bindings and
completion. This keeps existing lifecycle journal formats unchanged. Bind only
owners proved from that tracking incarnation; never enumerate all historical
owners of a slug as the affected set. An empty binding is a valid recorded fact.

Refine the earlier fence-before-journal ordering: under transition → creation →
session locks, first prove there is no admitted attempt, prepare the ordinary
durable journal, then atomically bind its exact owner fence before proceeding
with lifecycle removal/movement. The held locks and existing unfinished-journal
admission check protect the interval before binding. A retry reconstructs the
binding from that journal, never from a newly invented operation ID. The fence
and its operation binding should be one ledger transaction.

After ordinary terminal lifecycle work is durable, finalize that exact binding
idempotently **before** unlinking/fsyncing the journal or discarding its cleanup
sidecar. A ledger-write failure leaves the journal for the normal retry command.
A crash after coordination finalization but before unlink simply repeats the
same completion. A completed receipt prevents an old retry from changing a
later fence. Deletion retains the binding after tracking moves to recovery.

Revival clears only the completed archive fence associated with the retained
owner incarnation and saves its own completion receipt before removing its
journal. Cover explicit archives and complete/abandoned archives: older revival
schemas do not carry `archive_operation_id`. For those, resolve the unique exact
owner's completed archive binding under lifecycle locks; record that selection
in coordination state. Absence of the optional journal field must not leave a
valid owner fenced forever or clear another incarnation's fence. Revival restores
held notifications only for those bound owners and retains deployed blockers.

### 5–6. Fair delivery and independent reconciliation

Filter due outbox entries by eligible workspace/owner before applying each
delivery bound. A failed owner lookup must not reserve the first global outbox
positions indefinitely. Preserve its events and retry state while healthy owners
continue. Native requests retain their existing bounded transport timeout and
exact message/options identity; transport failure never creates approval or a
replacement conversation.

Keep the sole scheduler limited to bounded local observation, ledger transitions
and worker dispatch. Move remote Git/SSH reconciliation and forward profile
completion into an independent `workspace-reconcile-ATTEMPT.service`. It consumes
the original immutable request and retained package/adapter contract, acquires
the same nonblocking per-attempt worker lock, and refuses overlap with a running
mutation worker. The deterministic unit identity prevents concurrent reconcilers;
exited retries use bounded backoff. These units survive coordinator restarts and
do not become children canceled with the owner conversation.

Reconciliation writes the original attempt's bounded result for ordinary receipt
import. It may prove an effect or complete the already selected approved profile;
it must not repeat an uncertain machine activation or push as a new operation.
Read-only probes may use explicit deadlines and SSH connection/liveness limits.
A timeout preserves unknown outcome and the original claim. Do not put a generic
short kill deadline around forward activation and call its timeout no effect.
Admission, notification delivery and unrelated resources must progress while a
reconciler is stalled. Count resource conflicts separately from live-worker
capacity so retained unknown outcomes do not permanently consume every unrelated
execution slot.

### 7. Use the pinned stateless confctl constructor

The inspected confctl revision `7bee58a52372b95c2198ce3f2a719807a3c2c66b`
provides public `ConfCtl::Nix.stateless`, supplying `max_jobs: 'auto'` and avoiding
`Settings.instance.max_jobs`. Use it for prepared activation/profile publication.
Ordinary `ConfCtl::Nix.new` remains appropriate during preparation, where settings
evaluation and builds are allowed. Preserve dry activation, rollback behavior,
profile publication and exact live checks. Loading the retained generation must
not rediscover configuration through `MachineList` or evaluate/build/copy again.
Verify the real pinned constructor path with `Settings`/evaluation made fatal;
a fixture that only mirrors the intended API is additional, weaker evidence.

### 8. Recovery capacity is an admission obligation

Separate new-work admission from bounded completion/cancellation. New work must
reserve the bytes and receipt slots needed to settle its jobs, reservations,
notifications and lifecycle bindings. The 14 MiB admission ceiling and admission
receipt limit must not reject those already reserved completion writes. The hard
16 MiB structural bound remains; account conservatively for actual bounded
payloads, duplicated history/completion data and native options, rather than
assuming a worker-result bound also bounds every other record.

Each job/reservation gets at most its bounded terminal transition and exact
idempotent receipt. Repeating an accepted request returns that receipt. A new
request ID must not finish an already released reservation repeatedly, grow
completion history, or create unlimited release notifications from the reserve.
Retain all evidence; neither a full ledger nor low free space permits pruning
ownership or unknown results. Capacity tests must show successful settlement at
both admission ceilings, not merely that new submissions are refused.

### 9. Recheck the configuration target before machine mutation

The admitted machine snapshot freezes the canonical configuration repository,
configured full target ref and source head, along with its preparation baseline.
Immediately before machine intent, fetch/observe that exact target and prove its
current head is an ancestor of the prepared configuration source. Use the sealed
coverage/remote contract, not a newly selected default branch. An incompatible
advance returns `needs_refresh` before the adapter mutates the machine; the owner
then prepares and verifies again. An already included advance is safe. Keep both
this source check and the released-deployment frontier/live baseline checks:
merge-only work can advance a target without changing the live machine.

The observation is the deployment admission boundary for the configuration
baseline. It does not imply a distributed transaction with arbitrary remote
writers. Do not hold a repository lock throughout a remote deployment merely
to prevent later, independently approved integration.

### 10. Deliver the authoritative guide with the selected package

Install both generic coordination contract and operations guide beneath
`share/dev-workspace/`, and expose them through the stable read-only command
`workspace-host coordination guide`. Its output must give the workflow and
approval/reservation rules directly, or identify usable absolute installed paths
to the companion document. Printing an unresolved relative Markdown link alone
does not make the companion available to a shell reader. Show the selected
package/catalog identity and where its configured resource mappings can be read.

Add a short technical cue to the freshly composed managed-session identity
binding: before merging or deploying, read that command and use coordination for
catalog-covered operations. Keep saved role instructions byte-for-byte intact;
do not alter retained model, effort, access, roster or instructions to achieve
discovery. Apply the cue to roots and applicable team-member bindings, preserving
their existing role authority. Notification options already saved for an event
remain immutable for native reconciliation; new delivery policy composes the cue
normally. No workspace-master merge is needed to make deploy-first guidance
available, and the generic guide contains no concrete site deployment identity.

### Recovery advisories

**Never-started dispatch:** serialize dispatch-request publication/start and
recovery inspection with the same attempt lock. If there is no durable request,
no phase/result and no matching running/queued unit, while dispatch is excluded,
the write-before-start invariant proves that the attempt never ran. Commit a
bounded `not_applied`/failed recovery result and release only its execution claim.
Keep its reservation until explicit completion. Revalidate the exact ledger
attempt before that commit; a delayed dispatcher must then refuse to launch it.
Missing or unreadable systemd evidence is uncertainty, not this negative proof.
An existing request without a phase is a different window and must not be
classified solely by missing acknowledgement.

**Release before deployment:** add an explicit bounded `finish` disposition for
`no_deployment`, carrying the current reservation revision and reason/evidence.
It can release a requested/held reservation only when every associated deployment
job is canceled or conclusively no-effect, there is no dispatched unresolved
attempt, and all current and historical attempts prove no machine/profile effect.
Empty deployed history alone is insufficient. Settle or cancel `needs_refresh`
jobs first. Do not require feature integration for this branch, do not advance
the machine frontier, and retain the original feature obligations/history for
normal initiative tracking. Any applied/unknown effect requires normal integrated
completion or separately authorized exceptional recovery. Cancellation alone
does not silently release ownership.

### Verification and compatibility acceptance

Quick regression coverage belongs in the existing Host, coordinator, lifecycle,
adapter and native-policy suites. In addition to each invariant above, exercise:

| Review item | Required regression |
| --- | --- |
| 1 | Real Host registration/replacement with a nonempty catalog succeeds without a profile job; conflicting reservation refuses before registry write; an unselected candidate cannot use registration mode. |
| 2 | Suspend/resume retains exact queued work and held ownership; inject failures before/after pausing and during service recovery; reject a stale generation waiter. |
| 3 | Interleave ordinary switches with identical native semantics but different package generations; the old completion cannot clear new recovery or restore old terminals. |
| 4 | Interrupt archive, delete and revive before/after coordination completion; resume exact journals; test complete/abandoned revival and a recreated same-name session. |
| 5–6 | A missing owner with the earliest events and a stalled Git/SSH reconciler cannot block a healthy second workspace's job or notification; duplicate reconcilers cannot overlap. |
| 7 | The pinned confctl constructor performs no Settings/evaluation/build/copy during prepared activation, including a fresh process. |
| 8 | Fill both admission ceilings, then cancel and finish accepted work; exact retries do not grow state and fresh-ID terminal repeats refuse. |
| 9 | Prepare at R, integrate R+A without deployment, then attempt activation: return `needs_refresh` with zero adapter mutation. |
| 10 | Discover the installed guide from an unchanged shared checkout after package selection; frozen role instructions/settings remain identical. |
| Advisories | Crash after claim but before request publication and race the delayed dispatcher; prove safe no-effect release and refusal after any applied/unknown attempt. |

After fixes are committed and quick checks pass, obtain independent re-review
before long checks. Then verify real systemd worker survival, two-workspace
progress, native delivery and no-reboot coordinated self-deployment as already
planned. The new coordination protocol remains unmerged, undeployed and
unconsumed at this amendment; its initial schema can incorporate these fields
without migration. Existing lifecycle, pending-Codex and roster formats retain
their supported recovery contracts. No deployment or integration was performed
by this design task.

### Lead reconciliation of optional recovery paths

The two advisory recovery paths above remain deferred for this rollout. Missing
request publication retains the original claim for explicit operator recovery.
Cancellation before deployment retains full integration requirements for release.
This accepts conservative blocking behavior instead of adding new no-effect
proof/disposition contracts during remediation. The runtime operations guide
describes both limits. Independent re-review includes this disposition.

Owner identity excludes the three mutable creation tracking-proof fields
(`tracking_origin`, `tracking_plan_sha256`, `tracking_state_sha256`). Revival
changes these fields while retaining the directory, conversation and original
creation state; changing them must not manufacture another coordination owner.
The full directory identity, workspace, slug, retained thread and remaining
creation identity still bind the owner.

## Recovery-capacity accounting refinement

This design addresses finding 2 in [the remediation review](remediation-review.md).
The lead separately owns the completed-creation admission fix. Replace the
six-result-units heuristic with the prospective size and bounded future growth
below. Reuse the existing content-addressed artifact store; no storage service,
garbage collector or native transport change is needed. This is an implementation
brief, not a claim that the capacity regression or independent re-review passed.

### Immutable options and finite notification identities

Save native options as an ordinary checksummed artifact with
`kind: notification_options` and the complete original `options` object. Store
only its digest in the outbox. Write/fsync the artifact before atomically binding
its digest to an event; a failed ledger write may leave an unreferenced artifact.
Never replace an event's saved options. Load, verify digest/kind, and expand the
same object for each native send/reconciliation attempt. The event payload digest
binds the artifact digest, which transitively binds the full immutable options.
Retain the artifact after delivery. Model, effort and frozen instructions remain
unchanged, and the existing native message ID/receipt contract remains in force.

Derive an event UUID from a versioned tuple of owner ID, item ID, snapshot ID
(null for a reservation), and semantic state. Re-entering that state keeps the
first event's text, options, message ID, delivery state and receipt. Job snapshots
can create at most five events: `ready`, `needs_refresh`, `reconciling`, `succeeded`
and `failed`. A reservation can create at most `held` and `released`. A refreshed
snapshot has its own bounded set; old events remain retained. Reason changes or
resource churn update current job status without growing the outbox indefinitely.

Use encoded UTF-8 JSON byte lengths throughout. Raw character/string lengths do
not bound JSON escaping. Keep these explicit supported bounds:

| Payload | Bound and enforcement |
| --- | --- |
| Complete job result | `R = 16 KiB`, at worker writing, reconciliation writing and result import. |
| Complete job reason | At most `R`; diagnostic strings use a smaller 4 KiB encoded bound. |
| Cancel/finish request and request-receipt result | Each at most `R`; receipt wrapper/key bytes are additional. |
| Complete outbox event | At most `R`, including options digest, final native receipt and retry diagnostic. |
| Native receipt | At most 4 KiB, preserving the complete four-field `SendReceipt`; never truncate its identities. |
| Event routing/text base | At most 4 KiB; reserve 4 KiB for a diagnostic and remaining space for receipt, artifact/digest fields and bounded counters. |
| Options artifact and assembled native request | Each within the existing 256 KiB protocol bound, including its wrapper. |

Validate the actual assembled native request before adopting prepared options;
an artifact-size check alone does not account for its send envelope. Keep the
supported options/envelope limits consistent with owner admission so an accepted
event is not permanently undeliverable solely because its retained policy fits
the artifact but not the transport. Large policies such as the review's
200,000-byte case remain supported without occupying ledger space. A valid
native receipt must fit the event's reserved envelope after a send; do not rely
only on discovering an oversized record at the subsequent ledger commit.

### Prospective admission formula

Let `b(x)` be the serialized JSON byte size. Compute `B` from the prospective
ledger **after** the mutation callback, insertion of its actual idempotency
receipt, and the next ledger revision. Include the on-disk trailing newline.
Any admission error aborts that transaction; the callback must not perform
external effects. A refresh's copied old snapshot/result is already included in
`B`, so do not estimate it from the incoming request's length.

New work requires:

```text
B + J + E + C <= MAX_LEDGER - RECOVERY_RESERVE
MAX_LEDGER = 16 MiB; RECOVERY_RESERVE = 2 MiB
```

All terms are computed from the prospective ledger. `J`, `E` and `C` account for
the following still-possible additions; the separate 2 MiB reserve is not a
substitute for them. Conservative overlap is acceptable. Do not reserve a whole
256 KiB snapshot when only its coverage fields can be copied during settlement.

**Job settlement (`J`).** For each nonterminal job reserve:

```text
max(0, R - b(job.result))
+ max(0, R - b(job.reason))
+ Q
+ 1 KiB
+ H(job)
```

`Q` is one cancellation receipt map entry with an `R`-byte result: derive the
fixed wrapper/key overhead from the existing receipt shape, including its
71-character digest and UUID key. `R + 256` is a safe simple bound. The 1 KiB
covers later fixed-size attempt/state fields and bounded revision/sequence
growth, not arbitrary new payloads. No effect/history term is needed for a merge.

For a deployment job, build its possible reservation-history skeleton using the
actual serialized `coverage`, `coverageContracts`, artifact digest, kind and a
36-character attempt ID, plus null `observed`, `outcome: unknown`, and an empty
`dispositions` array. Define its maximum as `b(skeleton) + 2R + 256`: one current
observation and at most one prior observation/disposition. `H(job)` is that maximum
minus the existing same-attempt history record, floored at zero. Without that
record, reserve the whole maximum. Enforce the only supported history update as
one `unknown` → `applied` disposition; repeated reconciliation cannot append an
unbounded disposition log. The complete job result and the observation copied
into reservation history are separate retained allocations.

**Notifications (`E`).** Independently of job state, reserve the unused part of
the `R` event envelope for every existing undelivered outbox entry. In addition,
enumerate the deterministic event IDs still possible for each nonterminal job's
current snapshot and each unreleased reservation. Remove IDs already in the
outbox, deduplicate, and reserve `R + 64` per missing entry, including its map key.
Only owners with a retained native thread need these slots. A terminal job
ceases needing job-settlement growth, but its undelivered events remain charged
until delivery. Delivered records and their retained options references remain
in `B`; they do not disappear from the accounting.

**Reservation completion (`C`).** For every unreleased reservation construct a
potential deployment history containing its actual history plus one record for
each associated nonterminal deployment job whose attempt is not already present.
Use each job's current coverage/contracts. An unknown attempt already recorded
does not add another coverage record merely because it may later be proved
applied. Include existing history regardless of its jobs' terminal states.

Using that potential history, mirror the current unowned-proof loop: for every
distinct unowned coverage contract and every matching deployed/potential coverage
revision, construct the exact future proof shape with repository, target,
`owned: false`, head, and a 40-character placeholder remote head. Let `U` be the
encoded size of that array. Preserve multiplicities used by the implementation;
assuming deduplication which `finish` does not perform would undercount.

Set `P = 2R + U`. The `2R` bounds owned integration proofs: their final-head
entries already fit inside the `R`-byte finish request, and adding the fixed
remote-head/owned fields adds fewer bytes than each original validated entry.
This also accommodates final owned registrations added after reservation without
guessing their names. Larger finish requests remain outside the supported bound.

Reserve for each live reservation:

```text
R + 3P + Q + 1 KiB
```

This covers the saved finish request, one integration-proof array, at most two
frontier projections of those proofs (machine/profile), the finish receipt, and
JSON framing/fixed fields. Each frontier projection drops remote-head/owned data
and adds only the shorter fixed operation kind, so it cannot exceed its proof
array. Existing frontier content is already in `B`. This derivation depends on
the current two deployment kinds; adding another must update the multiplier.
The reservation's future `released` event is covered by `E`.

### Enforce promises across every writer

The request-receipt ceiling applies to prospective new admission, including its
new receipt. Cancel and finish bypass that admission ceiling while consuming
their already reserved single receipts; the hard ledger bound still applies.
Exact retries return the existing receipt, and fresh-ID terminal repeats refuse.

New owner and lifecycle-intent records created outside `Store#request` must use
the same capacity predicate, or have their exact bounded growth reserved before
they become required recovery work. In particular, preflight a new lifecycle
intent's capacity before making a journaled operation depend on that new record.
Its subsequent completion updates only the admitted binding. Read-only polling,
delivery retries and already admitted result import are settlement, not reasons
to apply the new-work ceiling again. They must not add unbounded new records.
Use bounded numeric representations/saturating delivery retry counts; fixed
framing allowances cannot prove safety for arbitrary-length integers or strings.

The hard writer/read limit must agree about the trailing newline. Apply result
and event bounds to every producer and importer, not only ordinary workers;
oversized authoritative output preserves uncertainty rather than being truncated
into a successful result. Diagnostics can be safely shortened to their encoded
bound. No capacity failure permits deleting an artifact, receipt or reservation.
Disk availability remains an operational constraint separate from this ledger
proof; source and option artifacts retain the documented no-pruning policy.

### Meaningful capacity regressions

Exercise actual materialization after admission: many small jobs with distinct
200,000-byte valid options, bounded events, maximum result/reason/receipt payloads,
and retained deployment coverage. Deliver events after their jobs become
terminal, then finish reservations with real integration-proof/frontier records.
New admission must refuse before the projection crosses 14 MiB, while the
accepted work settles below 16 MiB. Include unknown → applied history, multiple
snapshots and unowned revisions, pending events from old snapshots, and repeated
ready/reconciling churn with no new event IDs. A post-callback rejection must
persist neither its job/history mutation nor its request receipt. Test encoded
diagnostics with escaping, artifact/envelope limits, and complete receipt bounds.
Filling the ledger with one inert filler entry and finishing one tiny operation
does not establish this invariant.

The lead owns these tests and source edits. This design task performed no test,
commit, deployment or default-branch integration; independent verification and
review of the final implementation remain required.

### Lead implementation refinement

Native notification receipts also use the existing immutable artifact store with
`kind: notification_receipt`; the outbox keeps the digest. This preserves complete
identities without allocating arbitrary native reply strings inside its bounded
envelope. Options are expanded into the actual send envelope and size-checked
before their digest is adopted. Encoded diagnostics remain at most 4 KiB, and
delivery retry counters saturate at one billion. This changes only the initial,
unmerged and undeployed private representation, with no migration or old-shape
reader. Public native send/reconciliation semantics are unchanged.

## Lifecycle publication capacity correction (lead brief)

Independent review identified a gap between the read-only lifecycle capacity
preflight and ordinary journal publication. Another owner can admit new work in
that gap, so binding after publication can refuse at the new-work ceiling and
leave the ordinary journal blocked. The early check is only an optimization.

Use the existing Store lifecycle binding transaction as the publication guard.
Prepare inventories, recovery snapshots, hashes and journal bytes first. Within
the short ledger write mutex, construct the exact binding/fences, check its
prospective capacity, publish the bounded ordinary journal (or archive cleanup
sidecar), then persist the ledger. Existing bindings remain exact/idempotent.
No new provisional state, schema collection or exceptional release is needed.
Physical write errors retain ordinary recovery behavior and exact identity.

Archive recovery capture remains outside the mutex. Its first sidecar publication
must bind under the guard too because a sidecar is enough to reserve the ordinary
retry path. Archive/revive journal create and deletion journal publication use
the same guard. Subsequent phase writes do not allocate new coordination records.
Capacity refusal before publication leaves no new lifecycle authority. Test the
actual writer boundary after deliberately consuming capacity following preflight,
and use a concurrent contender to prove publication excludes a ledger writer.
This is a bounded correction to the reviewed admission contract, not a new
lifecycle recovery mechanism. Implement only after the current review snapshot
has finished; verify narrowly and fold into the owning core commit.

## Worker request capacity correction

Late duplicate review independently found that valid repeated refreshes make
ledger audit history too large for the immutable 256 KiB worker envelope.
Keep full history and results in the ledger; worker copies retain existing
job fields with empty history and null previous result. Worker execution and
reconciliation use the current snapshot, attempt and coverage contracts only.
A shared pure envelope builder computes the exact digest and file size.
Before changing reservation ownership or creating an attempt, admission checks
the prospective claimed envelope including its newline. Oversize work becomes
needs_refresh with no resource claim, so owners can reduce their snapshot.
Dispatch uses that same builder. Private request schema and recovery stay the
same; no feature format has been deployed. Test repeated actual valid refreshes,
real dispatch and Worker read/execution, plus a near-limit actual snapshot that
fits independently but cannot fit its worker wrapper. This directly implements
the review's requested bounded correction under mandatory-review step 9.

## Operations navigation and machine reservation badges

User-approved bounded presentation follow-up: move the coordination panels to
read-only /operations, linked beside Automatic archival in the shared menu.
Keep active/completed jobs with active jobs first. Replace Handoff's full panel
with a link. Session-list cards show only durable machine ownership, including
idle review and recovery; requested/released reservations and brief claims do
not receive badges. No scheduler, admission, ledger schema or release behavior
changes. Existing deployed state and exact source roots remain supported.

Portal status adds reservationHolders before its 128-record history truncation.
Rows contain ownerId, slug, portalUrl and sorted machine/state entries. Reuse
Store.lifecycle_owners to match exact active/archive incarnations rather than
infer ownership from a reused slug. Foreign workspace owners stay separate.
The browser uses one five-second visible-only coordination reader for each page,
reapplies its cached badge projection after card refresh, and retains prior
content with an explicit warning on read errors. Only a successful status read
can remove a badge within the same incarnation; a changed observation identity
immediately hides the previous incarnation's badge. Abort hidden/navigation reads and reject late responses.

Verify held states, idle/archived recovery, slug reuse, workspace isolation,
multi-machine badges, history truncation, refreshed cards, failed reads and
visibility/navigation cancellation. Run quick Ruby/Go/browser checks, independent
affected-lane review and then composed package verification. Consolidate the final
runtime pin streams, preserve previous deployment evidence, and redeploy system
then application through synchronous bootstrap under the same reservation.
No reboot, default-branch integration, ownership release or closure is authorized.

## Operations review remediation

Carry the established session-observation-v1 directory/root identity from the
incarnation-verified Ruby projection to initial/index-refreshed cards using the
existing Go session.ObservationIdentity contract. Cache/late responses may badge
only an equal nonempty identity. Failed-read retention and successful-release
removal apply within that incarnation. A changed identity immediately hides the
old badge. No persisted schema, ownership or scheduling changes. Verify same
incarnation refresh, same-slug replacement during failure, and delayed old reply.

## Approved Operations clarity revision

Implement the user-approved structured dashboard, Operations above Automatic
archival, a single-machine short-name badge or distinct-machine count, and a
tooltip listing every held machine/status. Add Reservations between Clusters
and Artifacts, deep-linked through #reservations. The lead implements from this
brief; /root/operations_rework_design (Astra/xhigh) provided the timing design.
The session is threadless with no retained roster. Default-branch integration
remains paused; deployment authorization and the existing review reservation
persist. Preserve prior artifacts and exact deployed source roots.

The read-only Operations dashboard separates held machine cards, running/waiting
jobs and completed results. Human labels, targets, ownership, reasons and dates
are primary; diagnostics, IDs and store paths are expandable. Keep clear empty
states, bounded-view warnings, suspension/delivery notices and stable details
expansion/focus across refresh. The per-session pane uses its existing status
endpoint and shows only incarnation-proven records, pending requests separately,
and related jobs. Refresh only while the document and pane are visible; abort
obsolete reads and retain successful content with a warning on failure.

Derive shortName from the installed catalog key for a canonical machine ID,
using a qualified-ID fallback for unknown catalog entries. Add optional timing
metadata and owner observationIdentity to portal projections. Extend the
nontruncated holder summary with reservation details so truncation cannot hide
held machines. Carry the same observation identity in the session body. Existing
status fields, authority, permissions, scheduling and completion stay unchanged.

Store optional UTC event dates in private bounded coordination/timing.json,
separate from ledger schema 1, job history, worker envelopes/results and the
package compatibility contract. Store.transaction compares before/after entity
revision/state, publishes the authoritative ledger first, then timing while
holding the same mutex. Capture one clock value per committed transaction.
createdAt exists only for actual new records; stateChangedAt only for actual
state changes; finishedAt marks terminal jobs/released reservations; heldAt
marks the first held reservation. Preserve earlier fields only from timing
matching the predecessor UUID/revision/state. Expose metadata only when it
matches the current record. Idempotent retries and reads never stamp dates.
Missing/malformed/stale/oversized metadata or write failure affects dates only;
keep committed work successful and wake the scheduler. No backfill from mtimes,
phase receipts or observation times. Display Time unavailable for missing dates.
This handles predecessor/candidate overlap without new rollback machinery.

Acceptance: one held review machine, zero active jobs and four completed steps
are immediately understandable. Machine/app deployment steps have distinct
labels. Named/plural badges and their tooltip remain correct across failed
reads, confirmed release, truncation and session recreation. Quick Ruby/Go/Node
checks cover timing transactions, predecessor validation, worker envelopes,
navigation and async ownership. Final independent review covers the complete
consolidated branch histories and no-migration lineage; then run composed
package/system checks and desktop/narrow-screen browser acceptance. Update only
the owned runtime pin streams, retaining the extension revision, and redeploy
under the existing reservation without reboot or integration.

## Direct Reservations link correction

Live Chromium acceptance found that an initial `#reservations` URL can activate
the panel after coordination.js first observes it as hidden. The main app awaits
its conversation module, then emits the existing `session-section-change` event.
The polling helper now observes that event in addition to clicks and hash changes.
The handler retains the same visibility, abort and incarnation rules, and all
three page templates advance the script cache version. No API, ledger, timing,
worker, host-module or ownership contract changes.

This is a bounded correction within the independently reviewed behavior. Direct
inspection, ten browser harness tests and a read-only real-browser preview with
the exact new script verify it under mandatory-review step 9. The preview uses
the deployed backend and original app script, testing the real asynchronous
activation ordering, desktop/narrow layout and inactive-tab polling. Final
packaged checks, exact-head CI and unmodified live-browser acceptance remain
required for the successor. Earlier Ruby/backend and VM evidence remains valid
for unchanged sources; no provider-recovery or activation implementation changed.

## Accepted installation-only integration extension

The first rollout's retained owner is threadless. Its normal CLI selectors cannot
admit merges, and no conversation should be created merely to complete integration.
The separately designed [dated supervised route](bootstrap-merge-design.md) is
accepted by the lead for this installation. It composes exact selected Host/Engine
interfaces in workspace source-only code, with ordinary merge workers and receipts.
It does not install new permissions, modify runtime schemas or claim other pending
owner work. The lead holds a quiescent owner window, and all deployment jobs/drivers
must have settled. Focused private-Git fixtures cover exact retries, interruption,
wrong authority/evidence, claim scope and preservation of shared staged/unstaged
files. Independent final review and unchanged application derivation proof precede
use. Review completion and machine release remain separate.

## Reviewed patch-equivalent integration after target advancement

Accept integration-rebase-design.md from Astra/xhigh. The lead implements an
optional dated-plan lineageEvidence list, bounded pre-approval review receipts
using existing Engine lineage readers/comparator, applied-owned deployment
coverage, exact bases/ranges and immutable operation-base validation. Old plans
retain ancestry-only behavior. New configuration/workspace plan and preparation
UUIDs preserve already accepted runtime/extension requests/results. Canonical
future finish proof must use the actual job approval record ID, not bundle
request UUID; creation of evidence never authorizes finish/release.

Append a focused helper commit after live-consumed aadaa171. Verify new policy
with private Git/actual selected worker tests, all four affected review lanes,
configuration build-only/input comparison, workspace checks and identical app
derivation. Dispatcher/reconciler unchanged; existing real systemd interruption
evidence remains applicable unless those paths change. No permanent runtime API,
new pins, ledger format, owner transfer, new conversation or activation required.
