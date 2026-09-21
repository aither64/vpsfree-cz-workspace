# Session-long agent teams and deterministic workflows

## Goal

Implement the accepted configurable-team design from
`tmp/codex-workspace-token-efficient-workflow-v3.md`, as refined in the root
conversation. A user keeps one root conversation while selecting `solo`,
`delegated`, or `lead_designed`; compatible designer, implementer and reviewer
contexts are reused for the session. Long or uncertain verification is handed
to a fresh minimal Luna/low utility watcher and is not represented as team
membership.

Quality is the primary constraint. Substantive design defaults to Sol/xhigh,
implementation to Terra/xhigh, and independent review to Sol/xhigh. Sol/high
design and Terra/high implementation are allowed only for bounded simple work
with a recorded reason. No automatic path may select or fall back to Astra.

## Affected repositories

- `dev-workspace`: generic schema/resolver, immutable catalogs, native agent
  generation, portal/session selection, persistent member bookkeeping, workflow
  evidence commands, packaging and generic documentation/tests.
- `vpsfree-dev-workspace`: package pass-through and vpsFree.cz review,
  verification and role-procedure integration.
- workspace repository (`vpsfree-cz-workspace`): authoritative
  `config/agent-teams.nix`, site instruction routing, downstream pins and site
  assertions.
- `codex-web`: only if capability proof finds that the installed client cannot
  submit or observe the required per-turn settings/member events.
- `vpsfree-cz-configuration`: only if aitherdev needs a host-level native child
  capacity or runtime setting. The workspace application remains a user-profile
  deployment and is never system-pinned here.

## Phased approach

1. Establish initiative/worktrees and prove installed native capabilities:
   explicit model/effort selection, fresh-context review, idle follow-up,
   next-turn settings, identity observation, recovery and capacity for three
   retained specialists plus one transient watcher.
2. Add generic `teamConfig ? null`, schema validation, canonical digests,
   generated effort variants, catalog retention and the site configuration.
3. Add portal/CLI starting-team selection, first-turn resolution and pinned
   catalog/session state.
4. Add safe runtime team transitions and the persistent member registry while
   keeping watcher operations separate.
5. Add bounded snapshot/check/CI evidence commands and the minimal Luna watcher
   path; update design/review/verification procedures.
6. Add safe integration prepare/status/apply and real-Git race/interruption
   tests.
7. Integrate pins in dependency order, build the combined package, deploy the
   user profile to aitherdev, and exercise creation, switching, persistence,
   watcher and rollback scenarios.

Each phase is committed and given quick verification before the mandatory
independent Sol/xhigh review. Long or uncertain builds/tests after that review
are launched and monitored by a fresh Luna/low subagent. Dependency order is
generic, organization extension, site workspace, then configuration if needed.

## Decisions and invariants

- `config/agent-teams.nix` is the single site source of models, efforts, named
  teams, defaults and utility policy. The generic and organization layers do
  not duplicate those subjective choices.
- Persistent team roles are lead, designer, implementer and reviewer. Luna is
  an operation-scoped utility, not a role, member, selectable team or reusable
  specialist.
- The site variants are `solo`, `delegated` and `lead_designed`;
  `delegated` is both the starting and substantive-development default.
- A catalog is immutable and session-pinned with its generated native files and
  Nix store path. Active selection and bounded transition history are mutable
  session state. Package upgrades do not silently alter old sessions.
- The Go portal/session layer owns selection, transition and native-member
  reconciliation. Ruby CLI commands are thin clients and own deterministic
  repository/check/CI/integration mechanics where appropriate.
- Team changes occur at safe boundaries and affect the next real root turn;
  they preserve the root thread, collaboration mode, accepted plan, approvals,
  worktrees and evidence. No active inference or writer is retasked.
- The first reviewer is independent and starts without implementation/design
  conversation history. The same reviewer is normally reused for findings and
  later relevant revisions.
- Long/uncertain or polling verification is delegated before launch. The Luna
  utility receives exact argv/cwd/terminal conditions, owns the process, writes
  full logs and returns a bounded result. It does not edit, diagnose, retry,
  approve, deploy independently or adopt an already-running process.
- Do not add an orchestration service, scheduler, message bus, pricing engine,
  metrics dashboard or generalized DAG system.

## Compatibility and deployment

All new state is private, additive and versioned. Existing sessions stay
unmanaged or legacy-bound until explicit adoption. `teamConfig = null` retains
ordinary supported Codex resolution without inventing a lineup or Astra
fallback. Old package generations may ignore new private records but must not
corrupt them. Session catalog GC roots keep rollback/loadability intact.

No vpsAdmin API, database, node protocol or vpsAdminOS format changes are
planned. Mixed package generations remain supported because each session uses
its pinned catalog/runtime identity. Transition and integration records use
compare-and-set revisions and explicit unknown/blocked states for interrupted
operations.

The user authorizes user-profile deployment to aitherdev and necessary
development configuration build/dry-activation/deployment from the
configuration feature branch. This does not authorize source publication,
pushes, default-branch integration, configuration-master integration, archival,
branch deletion or lifecycle completion.

## Public interfaces

- `dev-session start ... --team TEAM`
- `dev-session workflow team list|show|set|cancel|adopt`
- `dev-session workflow policy`
- `dev-session workflow snapshot`
- `dev-session workflow check run|status|logs`
- `dev-session workflow ci inspect|wait|cancel-superseded`
- `dev-session workflow integrate prepare|status|apply`
- Portal Starting Team and existing-session Change Team controls.

## Documentation

Keep generic schema/workflow and recovery behavior with `dev-workspace`,
organization review/verification extensions with `vpsfree-dev-workspace`, and
the concrete team choices plus site deployment notes with this workspace.
Update command help and existing documentation indexes rather than relying on
the private initiative record.

## Testing plan

- Schema/generator tests for neutral fixtures, invalid definitions, canonical
  digests, effort variants, utilities versus members and no Astra site path.
- Portal/server tests for non-default creation, stale catalogs, first Plan turn,
  tri-state lead overrides and existing-session transitions.
- Transition/recovery tests for compare-and-set races, interruption, next-turn
  settings, member reuse/replacement, fresh reviewer independence and legacy
  adoption.
- Catalog retention tests across two package generations and garbage
  collection.
- Snapshot/check/CI tests for bounded valid output, streaming logs, revision
  applicability, interruption, pagination, superseded runs and no model polling.
- Real-Git integration tests for main/master discovery, fast-forward-only
  operation, shared-root preservation, stale evidence, two-writer races,
  uncertain pushes and multi-repository partial success.
- Repository quick checks, packaged tests and flake checks. Luna owns every
  long or uncertain build/test/CI/deployment wait.
- Aitherdev smoke test for solo creation, first-turn settings, same-root
  switching, retained designer/reviewer follow-ups, watcher cleanup, catalog
  retention and profile/configuration rollback.
