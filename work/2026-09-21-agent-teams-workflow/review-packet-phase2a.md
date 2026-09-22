# Phase 2A mandatory change-review packet

## Requested outcome and acceptance criteria

Implement the dormant compatibility foundation for managed, session-long agent
teams without yet creating agents, selecting teams at runtime, retaining Nix
packages, or changing a live Codex thread.

Acceptance for this slice requires:

- a bounded `codex-web` turn-options API for explicit model, reasoning effort
  and application context on both start and steer delivery;
- option-aware prepare, send, reconcile and discard operations whose retry
  identity includes the options digest;
- compatible wrappers for existing callers and byte-compatible schema-3 ledger
  records when options are absent;
- idle-only managed starts, deterministic context bounds and recovery rules that
  reuse prepublished initial-message state rather than accepting replacement
  options;
- a strict generic reader for the installed immutable agent-team catalog;
- schema-1 dormant state with pinned catalog/package identity, selected team,
  pending transitions, outbound dispatch, retained members and bounded history;
- strict JSON shape, closed enum, catalog-reference, revision, lifecycle,
  timestamp and identity validation;
- compare-and-set state storage with bounded files, owned permissions,
  symlink refusal, cancellable locking and crash-temporary handling;
- a package-retention interface and deterministic absolute root derivation, but
  no root creation, release or other retention action;
- no runtime manager, portal route/UI, native child creation, state emission,
  source publication, default-branch integration or deployment in this slice.

## Initiative and durable design

- Slug: `2026-09-21-agent-teams-workflow`
- Plan: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-21-agent-teams-workflow/plan.md`
- State: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-21-agent-teams-workflow/state.md`
- Runtime design:
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-21-agent-teams-workflow/design-phase2-runtime-teams.md`
- Exact schema checkpoint:
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-21-agent-teams-workflow/phase2a-state-schema.md`
- Accepted source proposal:
  `/home/aither/workspace/ai/vpsfree.cz/tmp/codex-workspace-token-efficient-workflow-v3.md`

## Repositories and reviewed ranges

1. `codex-web`
   - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-21-agent-teams-workflow/codex-web`
   - Base: `0a75d720171c52719679c7dd2e356d50f4b81f16`
   - Head: `52b8ca6e9ddf2175d1a9163996fa9073f9c1882d`
   - Commits:
     - `16894b42952b320385acbfa24a85bec6f8006252 codex: add option-aware turns`
     - `52b8ca6e9ddf2175d1a9163996fa9073f9c1882d codex: complete option-aware retries`
2. Generic `dev-workspace`
   - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-21-agent-teams-workflow/dev-workspace`
   - Base: `39bfa664298443334d12b08dd42a475eef1c38e4`
   - Head: `729e5e08a9d57e537250da157d74720af50003eb`
   - Commit:
     `729e5e08a9d57e537250da157d74720af50003eb teams: add pinned state primitives`

Both worktrees were clean at the exact-head verification checkpoints.

## Commit split

`codex-web` owns the public App Server client abstraction and its durable send
ledger. Its first commit introduces explicit turn options; its second completes
the option-aware retry family and compatibility rules. Generic `dev-workspace`
owns the installed catalog reader and future portal state boundary in one
coherent commit that introduces the final dormant schema, validation, storage,
pinning and canonicalization contract. This split follows ownership and keeps
the lower-level client usable without importing workspace policy.

## Important design decisions and non-goals

- The portal cannot invoke in-process collaboration tools. Later phases will
  persist desired/observed state while the session root reconciles native child
  operations.
- Designer, implementer and reviewer are session-retained roles. The Luna/low
  verification watcher is operation-only and is never serialized as a member.
- Runtime/request identifiers are bounded opaque UTF-8 strings. Request IDs are
  unique within their operation domain; pending transitions and retained history
  share one transition domain. Equal byte values in different namespaces are
  valid.
- Native config and task names may repeat across replacements. Canonical agent
  paths and non-null native thread IDs are unique among retained members.
- Transition deduplication is guaranteed only while an entry remains in the
  bounded retained history. Phase 2C must add tombstones before claiming
  session-lifetime idempotency after eviction.
- Catalog hashing must reproduce Nix `builtins.toJSON` bytes, including literal
  `<`, `>`, `&`, non-ASCII text and U+2028/U+2029 behavior. A literal
  Nix-generated fixture anchors this contract.
- Persisted pins require the package metadata schema and a canonical
  `/nix/store/<32-base32-hash>-<name>` package root. Staged package inspection
  cannot establish a persisted pin.
- State and retention roots use separate private namespaces. This slice derives
  retention paths but does not create roots or call Nix retention commands.
- Phase 2B owns registration/creation, Phase 2C owns transitions and dispatch,
  and Phase 2D owns member observation and lifecycle. Those behaviors are not
  preimplemented here.

## Public interfaces and consumers

- `codex-web` adds `TurnOptions` and option-aware variants of send,
  initial-message, prepare, reconcile and discard operations. Existing methods
  remain wrappers with zero options.
- The durable send identity adds an options digest. A zero digest remains omitted
  from schema-3 bytes so pre-feature readers can continue reading ordinary
  activity. A later package transition must refuse rollback once nonzero option
  identity has been persisted unless the target reader advertises support.
- Generic `agentteams` exposes strict catalog loading, state encode/decode and
  validation, a revision-CAS store, retention path derivation and the
  `PackageRetainer` boundary. No production caller emits managed state yet.
- Later portal/session runtime code is the intended generic consumer. Existing
  unmanaged sessions and callers remain on their prior paths.

## Documentation changed

- `codex-web/docs/reference.md` documents turn options, bounds and recovery.
- `dev-workspace/docs/workspace-portal.md` documents the dormant reader,
  pin/state limits and deliberately inert retention boundary.
- Initiative design/schema files record rollout and compatibility constraints.

## Quick verification

- `codex-web` exact head `52b8ca6e`:
  `nix develop path:<codex-web> -c env TMPDIR=/tmp/cw-go-test go -C <codex-web>
  test -mod=mod ./codex` passed in 0.975 seconds under a fresh Luna/low watcher.
  Log: `logs/phase2a-codex-tests-exact.log`.
- Generic pre-review exact head `19e56a6c`:
  `nix develop path:. -c go -C portal test -mod=mod
  ./internal/agentteams` passed in 33 seconds under a fresh Luna/low watcher with
  clean pre/post status. Log:
  `logs/phase2a-generic-agentteams-tests-final-exact.log`.
- Review remediation passed the same focused command in 35 seconds before the
  coherent-commit rewrite. The final rewritten exact-head result is recorded in
  `logs/phase2a-review-fix-tests-final-exact.log`; it passed in 33 seconds with
  a clean worktree and exactly one commit in the reviewed generic range.
- Gofmt and diff checks were clean before the final generic commit.
- Earlier generic watcher logs include one real unused-import failure that was
  fixed and one watcher command-transcription failure. Neither is acceptance
  evidence; the clean exact-head run above is definitive.

Long package, integration and deployment checks have not started. They remain
behind this review gate and must each use a fresh Luna/low operation watcher.

## Risk and required review lanes

Overall risk is **high**. This slice introduces durable protocol/state identity,
filesystem persistence, retry semantics and a public lower-level client API that
later runtime work will depend on. Review effort is xhigh.

One independent Sol/xhigh reviewer must cover all four mandatory lanes in one
coherent retained context:

1. General correctness and maintainability.
2. Architecture, ownership and unnecessary repetition.
3. Scope and proportionality against the accepted Phase 2A boundary.
4. Risk, security and compatibility, including malformed/untrusted JSON,
   symlink/permission/locking behavior, crash recovery, retry ambiguity,
   old/new ledger readers, mixed package generations and rollback.

The reviewer must report findings with severity, exact file/line evidence,
impact and a concrete remedy; explicitly report a clean lane where applicable.
No Blocking or Important finding may remain unresolved before long verification.

## Compatibility and deployment analysis

- Existing `codex-web` callers use unchanged wrappers. Zero-option schema-3
  records retain their prior serialized representation and ordinary legacy
  readers remain compatible.
- Nonzero options create a new identity dependency. Before later activation,
  package-transition preflight must prove the target ledger reader supports it;
  silent downgrade is forbidden.
- Generic state schema 1 is new but dormant. Because no runtime code writes it,
  schema corrections can still be made without migrating live state.
- Catalog pins bind immutable package/catalog/generator/adapter/capacity identity.
  A session using managed state must retain that exact package until lifecycle
  cleanup explicitly releases it.
- No database, public vpsAdmin API, daemon protocol, vpsAdminOS state, generated
  node configuration or production deployment changes occur in Phase 2A.
- No coordinated node update is required. Development deployment remains for a
  later integrated phase after runtime behavior, package transitions and
  rollback have been implemented and reviewed.

## Reviewer constraints

- Review only the exact ranges above plus the linked design artifacts needed to
  evaluate intent.
- Do not edit, commit, push, test, deploy or broaden scope.
- Treat generated artifacts and tests as evidence, not as substitutes for
  reviewing the implementation paths.
- Respect the user's no-Astra decision: reviewer model is Sol with xhigh effort.
- Retain reviewer context for remediation and later relevant phases.
