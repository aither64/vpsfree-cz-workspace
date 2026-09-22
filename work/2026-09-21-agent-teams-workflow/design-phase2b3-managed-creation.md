# Phase 2B.3 managed creation and UI design

## Scope and fixed inputs

This slice activates agent-team policy only for fresh `new` and
`plan-to-new-session` creation. It is based on generic `dev-workspace`
`285e998f4aae703f1d6b639a7bf23f7e111a660c` and the Phase 2B.1/B.2 contracts
already present there.

The deployment is forward-only on aitherdev. This slice does not add rollback
or mixed-generation support. It also does not implement ordinary managed sends,
team transitions, member reconciliation, migration execution, managed forks, or
managed archive/revive/delete/auto-archive. The latter operations fail closed
until their owning later slice. Ordinary finish, handoff and restart without a
new team selection remain available.

Schema-1 creation receipts/journals and the unmanaged path remain the supported
legacy-session behavior. The rollout deliberately does not migrate or adopt
idle sessions: a session is managed only when a new schema-2 creation accepts a
team binding. Existing legacy sessions may be resumed and completed, but a
fresh destination must be managed. Future managed features preserve the old
path rather than forcing conversion; legacy retirement is outside this
initiative.

The recorded Phase 2B statement that `codex-web` needs no change is superseded.
The current generic package pins `0a75d720171c52719679c7dd2e356d50f4b81f16`,
which lacks the required option-aware first-turn API. B3 requires the reviewed
local codex-web head `52b8ca6e9ddf2175d1a9163996fa9073f9c1882d`
or an approved successor containing `TurnOptions` and
`EnsureInitialMessageWithOptions`.

## Ownership and files

Generic `dev-workspace` owns the behavior:

- `portal/internal/agentteams/` keeps creation resolution, immutable binding,
  retained state publication, registration-plan comparison and strict runtime
  launch-evidence validation;
- `portal/cmd/workspace-portal/main.go` owns bounded direct-CLI resolution,
  publication, unmanaged guards and managed initial-turn reconstruction;
- `portal/internal/web/{server,creation,creation_store}.go`, templates, CSS and
  `static/app.js` own the browser selector, receipt and proof path;
- `libexec/dev-session` owns opaque lifecycle transport, journals, publication
  ordering and recovery;
- `libexec/workspace-host` supplies package/runtime authorities and blocks
  transitions while a managed creation receipt is open;
- `portal/internal/session/runtime-contract.json`, its generated/projection
  checks, Nix wiring and focused tests describe the new flags and records.

The organization and site repositories receive only later exact dependency-pin
updates. They are not part of B3.

## Installed catalog and launch authority

`workspace-host run-portal` passes three new exact authorities to `serve`:

```text
--package-root REAL_CURRENT_PACKAGE
--workspace-name REGISTRY_NAME
--registration-marker PRIVATE_RUNTIME/registration.json
```

They become `PackageRoot`, `WorkspaceName` and `RegistrationMarker` in
`web.Config` and are added to the runtime contract's `portalServeFlags`.
Portal startup loads the installed package through
`agentteams.LoadInstalled(PackageRoot)`. Managed page data is a presentation
projection only: exact catalog digest, default team and sorted rows containing
team name, neutral description, compact role summary and lead override policy.
No site team or model name is embedded in generic HTML or JavaScript.

Before accepting a managed creation, the portal:

1. obtains the live App Server model inventory;
2. resolves the submitted selection with `ResolveCreation`;
3. lists and strictly validates current retained state;
4. computes `BuildRegistrationPlan` for the current package and states;
5. strictly reads the private, owned and bounded B2.2 launch marker; and
6. requires a live Unix Codex socket and an equal registration policy and
   semantic digest.

The semantic digest and live socket are the launch authority. The portal must
not require the marker's package path to equal the current package path: B2.2
deliberately permits an inventory-only refresh when two packages have identical
registration semantics.

Missing or stale launch evidence returns 503 without accepting a receipt.
An explicit stale displayed catalog digest returns 409 with reload guidance.
Empty, unknown or otherwise invalid selection returns 400. Resolver or launch
validation failure precedes every thread, worktree and retained-state effect.

## Creation interfaces

### Browser resolution

Managed new-session and plan-to-new-session forms submit an explicit team and
the exact displayed catalog digest. Lead model and reasoning effort are optional
advanced overrides; empty values mean absence. The server remains the authority
for team existence, allowed effort and live model/effort availability.

Plan-to-new-session creation uses the selected team's lead. It does not copy the
source conversation's model or effort into the new policy. Source thread, plan
turn and plan digest still prove that the displayed plan is current.

Existing unmanaged sessions retain their model/effort conversation and
lifecycle behavior. An unmanaged-source fork remains a continuation of that
legacy workflow; managed-source forks are rejected until their managed-
destination design is implemented.

### Direct CLI resolution

The public interface adds:

```text
dev-session start NAME --team TEAM
```

Omitted `--team` selects the installed default for a fresh managed session. The
private portal interface uses `--team-binding TOKEN`; it is mutually exclusive
with `--team`. Either option is rejected for fork, `--no-codex`, or an existing,
preserved or revived destination.

Ruby never reads catalog policy. A bounded Go command, recommended as
`workspace-portal agent-teams resolve-current-creation`, takes explicit current
package and Codex-socket authorities plus strict selection JSON, obtains the
live model inventory, and returns the same opaque binding, digest and effective
lead as browser resolution. This keeps the public CLI independent of a
user-displayed catalog digest.

The opaque token remains `v1.<base64url>.<sha256>` and at most 32 KiB. Ruby may
validate only syntax, size, digest equality and exact transport equality. It
must not decode the payload.

## Strict schema-2 records

All readers branch by schema before validating an exact key set. Schema 1 stays
exactly unmanaged for legacy sessions; schema 2 is the team-bound path. Unknown
keys, duplicate keys, `null` impersonating omission, unsafe files and
unsupported schemas fail closed.

The managed portal receipt retains every current receipt field and adds:

```text
schema: 2
agentTeamBinding: required opaque token
agentTeamBindingDigest: required lowercase SHA-256
model: required effective lead model
effort: required effective lead effort
```

Its nested request permits only `new` or `plan`, retains the applicable current
goal/source/plan fields, and adds required `team` and `catalogDigest`. Optional
`model` and `effort` are submitted lead overrides; empty form values are
normalized to absence before persistence.

The receipt-bound `.request` record and workspace `.creation.json` journal use
schema 2 and add required `agent_team_binding` and
`agent_team_binding_digest` to their current exact fields. Their recorded model
and effort must equal the separately returned effective lead. A `creating`
journal requires its 64-hex tmux identity; a `ready` journal forbids it, as in
schema 1. Token, digest and effective settings are immutable across retries.

Completion evidence uses schema 2 and retains the current workspace, slug,
receipt, thread, source, goal, model/effort and tracking identity fields. It also
records:

```text
agentTeamBindingDigest
catalogDigest
creationIdentity
removalEpoch
```

It does not duplicate the opaque token. Proof checks the receipt, goal, thread,
tracking identity, ready manifest, exact managed state identity and pinned
catalog. It checks initial selection provenance, not equality to the state's
eventual current selection, so Phase 2C can later transition it.

## Receipt-before-journal transition blocker

The existing browser path atomically saves a receipt while holding the shared
workspace transition lock, then starts its asynchronous worker. There is a real
durability window before that worker writes `.creation.json`. Scanning only
workspace journals lets a portal crash or scheduling gap strand an accepted
binding across a package switch.

Therefore `workspace-host#require_no_unfinished_lifecycle_operations!` also
strictly scans the private portal creation directory derived from the existing
user-state namespace:

```text
$STATE/portal/<basename(workspace)>-<first-16-hex-of-sha256(workspace)>/creations
```

The scanner parses each receipt once with duplicate-key rejection. An
unambiguous integer schema-1 receipt belongs to the legacy workflow and is
ignored. A schema-2 receipt file must be owned, mode 0600, regular and bounded.
Managed schema-2 receipts in `running`, `paused` or `failed` state block package
transition and Codex reconciliation. `ready`, `conflict` and a pre-effect plan
`cancelled` receipt are terminal and do not block. A malformed, duplicate-key or
unsupported-schema record fails closed. Final-file checks catch ordinary
configuration mistakes; the trusted development host boundary does not treat an
operator-managed ancestor symlink as hostile.

This blocker becomes durable in the same transition-locked acceptance step.
Direct CLI creation already holds the host's shared transition lock for the
command. Consequently every managed state published by B3 is bound to the
catalog already present in the running registration plan; state publication
cannot introduce an unregistered role and does not need to restart its own App
Server.

## Publication and initial turn

After the exact root thread exists, tmux creation identity is known and
`sync_slug` has succeeded, but before `initial_goal_attempted` becomes true,
Ruby calls the existing `agent-teams publish-creation` helper with:

- the opaque binding and expected digest;
- the separately recorded effective lead;
- workspace, slug and private state root authorities;
- completed-removal digest as removal epoch;
- exact tmux creation identity; and
- actual root thread ID.

The helper revalidates the binding against its immutable pinned catalog,
retains the package first, and publishes revision-one state with
`Store.CreateRetained`. A lost response is success only when the complete
existing state is exactly equal; any differing state is a hard conflict.

Only after publication succeeds does Ruby durably set
`initial_goal_attempted=true`, release the slug lock and invoke `thread
ensure-initial` with an all-or-none managed authority set:

```text
--agent-team-state-root
--agent-team-workspace
--agent-team-slug
--agent-team-removal-epoch
--agent-team-creation-identity
```

The existing thread ID is the root-thread authority. Go loads state and pinned
catalog, validates the full identity, calls `ManagedTurnOptions`, converts the
neutral projection to codex-web `TurnOptions`, and calls
`EnsureInitialMessageWithOptions`. Ruby supplies no managed model, effort or
application context. The context source remains exactly
`dev-workspace.agent-team`.

After the exact initial goal materializes, Ruby reacquires the slug lock,
revalidates session, manifest and authority identities, reconciles the native
client, marks manifest/journal/authority ready, writes schema-2 evidence and
allows the portal receipt to become ready.

## Recovery invariants

- Before retention, retry follows the exact schema-2 journal and token.
- A retained root without state is repaired by the same publication request.
- An exactly published state reconciles a lost response; differing state is
  fatal.
- Published state with `initial_goal_attempted=false` permits one initial send.
- Once the attempt bit is durable, an unmaterialized thread is an explicit
  no-resend recovery blocker because the native initial-turn API has no durable
  request identity.
- An exact materialized goal completes recovery without a second turn.
- A different materialized goal is a hard conflict.
- An open portal receipt or creation journal continues to block a package
  transition until recovery reaches a terminal receipt.

## Temporary managed-operation guards

A strict Go helper, recommended as `agent-teams require-unmanaged`, loads state
for explicit state-root/workspace/slug authorities. Missing state succeeds;
valid managed state and malformed state both refuse the caller.

`dev-session` calls it before a source fork and before archive, revive or
delete. Auto-archive reports the managed session as ineligible rather than
mutating it. Portal routes enforce the same restriction before spawning the
CLI and render the lifecycle controls unavailable, but the CLI helper remains
the authority. These guards are removed only when the later lifecycle slice
implements retained-pin release/adoption.

## Browser behavior

Managed new and plan-to-new forms show:

- a Starting team selector with installed default preselected;
- neutral description and compact role summary;
- hidden exact catalog digest; and
- a collapsed Advanced lead override section whose controls are empty until
  intentionally changed.

Copy states that specialists start on demand and that staffing choice does not
grant edit authority. Team, digest and advanced values remain in the existing
session-storage draft after validation or stale-catalog errors. Unmanaged pages
retain their current controls. Fork has no selector.

User-visible copy must pass the `vpsfree-user-facing-writing` skill before the
implementation commit. This slice does not stage or publish knowledge-base
content.

## Verification

Focused checks before mandatory review cover:

- `portal/internal/agentteams`: default/non-default/current selection, lead
  overrides, strict marker evidence and retained publication identity;
- `portal/cmd/workspace-portal`: direct resolver, managed ensure-initial exact
  start fields/context, identity failures and unmanaged zero-option regression;
- `portal/internal/web`: managed new and plan creation, no source-setting
  inheritance, 400/409/503 boundaries, immutable retry binding, strict proof,
  unmanaged/fork regression and lifecycle refusal;
- `test/dev_session_test.rb`: CLI flags and exclusions, opaque token checks,
  schema-2 records, publication-before-attempt ordering, crash edges, unknown
  initial outcome and managed operation blockers;
- `test/workspace_host_test.rb`: new serve authorities and the pre-journal open
  receipt blocker, including unsafe path, permission, duplicate-key and
  malformed cases;
- browser/Node contracts: selector, digest, drafts, empty advanced defaults,
  managed plan behavior, unmanaged and fork absence;
- runtime-contract projection, Nix smoke and packaged suite, without paid
  inference.

Every long or uncertain test/build wait is delegated to a fresh Luna/low
watcher. Mandatory Sol/xhigh review follows the coherent committed B3 slice and
precedes packaged integration verification.

## Codex-web publication and commit boundary

Implementation may proceed locally before publication. Go checks can use a
temporary, uncommitted `go.work` containing the portal and sibling codex-web
worktrees; Ruby and Node checks are independent. Never commit an absolute Go
`replace`, a path flake input, or a fabricated remote version.

The active generic B3 commit must atomically contain its source changes plus
`portal/go.mod`, `portal/go.sum`, `flake.nix` and `flake.lock` pinned to the
published reviewed codex-web head. Normal Go module resolution, reproducible Nix
builds and the packaged suite cannot complete while `52b8ca6` exists only in a
local worktree.

Pushing that codex-web head to `aither64/codex-web` requires explicit push
authorization. Until it is granted, B3 may be implemented and locally tested
through the temporary workspace boundary, but it must not be represented as a
reproducible final generic commit. Downstream organization and site pins remain
outside this slice.
