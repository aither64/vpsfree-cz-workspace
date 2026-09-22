# Phase 2 design: pinned runtime teams

## Boundary and capability decision

Phase 2 implements plan phases 3 and 4: creation-time team selection,
session-pinned catalogs, safe runtime team transitions, next-turn lead settings
and persistent member bookkeeping. It does not implement snapshot/check/CI or
Git integration commands.

The App Server accepts model, effort and application `additionalContext` on a
real `turn/start`. The current `codex-web` pin does not expose those fields on
its send/initial-message API, so a small compatible `codex-web` extension is
required. Existing zero-option methods remain wrappers. An active `turn/steer`
must not receive new model/effort values.

The portal can observe native collaboration identities but cannot spawn,
follow up or close child agents through App Server RPC. Session state therefore
records desired and observed membership; the root lead performs native
reconciliation lazily on real assignments. This is bookkeeping around native
agents, not a scheduler.

Luna is never represented in session member state or registered as a selectable
agent. Each long or uncertain operation gets a fresh explicit utility watcher
under the monitor procedure.

## Ownership and bounded implementation slices

### 2A: turn options and state primitives

- `codex-web/codex/client.go`: add `TurnOptions` with model, effort and bounded
  application context; add option-aware send, prepare, retry reconciliation,
  prepared-attempt discard and initial-message methods while preserving current
  zero-option callers. Bind the option digest to every durable-send operation
  and omit model/effort from active-turn steering. A managed start prepares an
  idle-only attempt so a concurrent active turn is rejected instead of silently
  receiving new-policy context without its requested model and effort.
- Generic `portal/internal/agentteams/`: add strict installed/pinned catalog
  loading, schema-1 state value validation, private atomic compare-and-set
  storage and a `PackageRetainer` interface/derived-root contract. This slice
  does not run `nix-store`, emit managed state, register agents, or introduce a
  transition/member manager; those production effects belong to 2B–2D.
- Tests cover exact start versus steer requests, retry mismatch/unknown outcome,
  option-aware prepare/reconcile/discard, the idle-only guard, zero-option
  ledger behavior, strict state/catalog validation, symlink/size
  boundaries and atomic recovery.

No managed session state, runtime-contract change, App Server registration or
UI is emitted by this slice.

The retained design review tightened the dormant contract before any state can
be emitted. Catalog hashing must reproduce `builtins.toJSON` byte-for-byte and
is proven by a literal Nix-generated fixture rather than a self-referential Go
fixture. Persisted package pins include the metadata schema and a canonical Nix
store output. The removal epoch is the existing completed-removal-history
SHA-256 identity, not a fabricated counter.

Runtime and request identities are bounded opaque strings, separate from the
catalog identifier grammar. Dispatch records cover prepared, submitting,
accepted and unknown delivery, bind the caller request/message identity and
exact selection/lead, and permit an unknown result before a turn ID is known.
Member records distinguish immutable spawn provenance from current requested
and observed settings and retain the real native task/agent/thread identity.
Nullable observation, assignment and ownership fields represent unspawned,
idle and read-only states without placeholder values. All enums and catalog
references are closed and validated, including pending/history endpoints and
revision ordering; live idleness and writer-liveness evidence remains a later
manager responsibility.

CAS mutation uses cancellable lock acquisition. Crash-orphaned atomic-write
temporary files cannot hide valid state. Indirect GC-root paths are absolute
and derived below a separate private workspace-scoped roots namespace, never
the state directory or caller working directory.

### 2B: startup registration and creation

- `workspace-host` asks the packaged helper for exact App Server `-c` arguments
  covering the current catalog and every retained session-pinned catalog.
- Portal creation gains a server-populated Starting team selector and binds the
  submitted team to the displayed catalog digest.
- `dev-session start --team` and schema-2 creation receipts/journals carry an
  opaque resolved binding; Ruby does not interpret catalog policy.
- The first real root turn uses the selected lead model/effort and application
  context. Selecting a team starts no specialist.
- Tests cover stale catalogs, a non-default/solo Plan creation, exact first-turn
  fields, crash/retry edges, zero child creation and unmanaged regression.

### 2C: transitions and managed dispatch

- Add the accepted `workflow team list|show|set|cancel|adopt` and `workflow
  policy` interfaces plus equivalent portal controls.
- One pending transition is allowed. Requests are idempotent by caller request
  ID and compare-and-set revision. A stale browser or CLI cannot overwrite a
  newer selection.
- A committed selection changes policy for the next real idle turn; it never
  changes an inference already running or sends a blank turn.
- Managed model/settings and queue paths that cannot bind the selected revision
  fail visibly rather than bypass policy.
- Tests cover all site-team directions on the same root, active-turn pending,
  cancellation, restart, lost responses, override preservation and no model on
  steer.

### 2D: member reconciliation and forward lifecycle migration

- Reconcile native identities from observed events and compact turn context.
  Reuse only compatible idle members; retain inactive members without relabeling
  provenance; never retask an active writer.
- A reviewer starts fresh and remains reusable within its independent review
  context. Authorship or incompatible redesign requires replacement.
- Add the one-time idle-session forward migrator plus archive/revive/delete root
  handling. Package changes quiesce open lifecycle work and validate the current
  registration inventory; no old-target rollback negotiation is required.
- Tests cover retained designer/reviewer follow-up, dormant capacity, unknown
  spawn outcomes, fork isolation, GC-root lifecycle and migration restart.

Each slice receives focused quick checks, a coherent commit and mandatory
review before any long integration test. A fresh Luna/low watcher owns every
long or uncertain build/test wait.

## Private state

Store bounded state below the workspace user-state root in an `agent-teams`
namespace. Directories are mode 0700, regular files mode 0600, symlinks are
rejected, state is capped at 256 KiB, and updates use fsynced temp-file rename
plus parent-directory fsync. Address sessions by a digest of the slug and bind
the document to workspace identity, slug, completed-removal epoch,
creation/tmux identity and root thread ID so slug reuse cannot adopt old state.

Schema 1 uses exact flat root keys `schema`, `state_revision`, `workspace`,
`slug`, `removal_epoch`, `creation_identity`, `root_thread_id`, `catalog`,
`selection`, `pending_transition`, `dispatch`, `members` and `history`. It
records:

- state and selection revisions;
- exact pinned package store path, catalog path/digest/schema,
  generator/canonicalization/adapter identities and capacity;
- active team/digest, tri-state lead overrides, effective lead and provenance;
- at most one pending transition with base revisions, exact before/after
  policy, actor/reason, blocker and trusted continuation provenance;
- at most one unresolved real-turn dispatch with message/options/context
  digests and accepted/unknown outcome;
- at most 32 retained member records with immutable creation provenance,
  logical role, requested/observed settings, native identities, assignment,
  independence/write ownership and desired/observed state; and
- at most 32 compact completed transition outcomes.

Transition base revisions preserve the caller's original CAS base. Publishing
a pending record therefore leaves its base below the current state revision.
Resolution records the post-CAS revision as completion, which must be greater
than the original base but may have a gap after pending publication or unrelated
member/dispatch updates. Retained outcomes remain selection-chained, have
strictly increasing completion revisions, and each later base is at least the
preceding completion revision.

Root the whole pinned package output through an owned indirect Nix GC root
before publishing state. Archive retains it. Explicit canonical deletion removes
it only after deletion/recovery completion. Ordinary finish or handoff does not.

## App Server registration

Before App Server exec, load and validate the current catalog plus all retained
managed-session catalogs, including archived/revivable sessions and pending
transition endpoints. Deduplicate native role names, reject name/target
collisions, bound count and argv size, and register immutable role TOMLs through
explicit `-c agents.<name>...` arguments. Register role variants only; never
register the operation watcher as persistent/selectable. Set native child
capacity to the maximum required by the validated catalogs. Do not mutate
global user configuration. The same generated name at different immutable
package paths is equivalent only when native identity and exact TOML bytes match;
choose one deterministic path. Reject equal names with different identity or
bytes rather than rejecting harmless path inequality.

## Creation and transitions

Creation request schema 2 adds explicit team and catalog digest plus separately
marked lead overrides. Omitted team input resolves the installed default
once; explicit empty, stale, unknown or unavailable choices fail without silent
substitution. Managed receipt/evidence freezes the package/catalog/team/effective
lead. Schema-1 records remain unmanaged and readable.

Phase 2B activates only new and plan-to-new-session creation. Managed-source
forks and explicit team selection on forks fail closed until Phase 2D can provide
isolation and lifecycle reconciliation. Managed archive/revive/delete likewise
remain blocked until root release/adoption is recoverable. These temporary
blockers are not deployed independently of the later lifecycle slice.

After native root creation and before the initial message, publish the pinned
state and GC root. The initial message is then the first real turn with exact
options. Because the generic initial-message API has no durable App Server
attempt identity, that prepublished state is authoritative: every recovery must
reuse its exact catalog, team, effective options and thread binding. Recovery
never accepts caller-supplied replacement options and never sends the goal
twice. Forks inherit the source catalog/team but receive fresh history and no
child ownership.

A transition validates the pinned target and installed runtime, checks the
root/children/writers/checks/prompts/lifecycle boundary, and either commits at an
idle boundary or records one `pending_boundary` request. It never polls, kills,
interrupts, cancels or silently arms a fully blocked request. Commit increments
the selection revision and records desired member reuse/inactivation only.
The next real turn binds that revision and exact effective lead; unknown delivery
blocks another dispatch or transition until reconciled.

## Root-initiated transition limitation

A root cannot alter its own currently running inference. `workflow team set`
therefore returns `pending_boundary` promptly and the new lead applies on the
next real turn. No blank turn or fabricated user message is allowed. Automatic
continuation after a root-initiated change remains unsupported unless a
non-fabricated native continuation interface is proven later; application
context alone is not user approval.

## Forward-only deployment and migration

Aitherdev is the sole deployment. Package changes do not negotiate rollback or
mixed-generation readers. They quiesce creation/lifecycle work, validate current
state and GC roots with the candidate helper, switch forward, and restart App
Server consumers whenever either the binary or semantic registration plan
changes. Future schema changes use explicit offline forward migrators.

Before the first managed deployment, stop portal/App Server clients and migrate
every idle materialized session through an atomic mode-0600 journal. Each keeps
its worktree, slug and root conversation ID, receives the installed default team
without inferred overrides, retains the current package and publishes
revision-1 state. Tracking-only sessions remain without fabricated state until
their first conversation. Migration is exact-idempotent; partial failure remains
offline and rolls forward. Start App Server once after all migrated states are
included in the registration plan, then verify thread readability without
inference.

The existing zero-option codex-web schema-3 byte behavior remains harmless, but
the rollout does not depend on an older package being able to read new ledgers.
