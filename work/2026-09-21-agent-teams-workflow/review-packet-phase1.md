# Phase 1 mandatory change-review packet

## Requested outcome and acceptance criteria

Implement the first package/policy slice of the accepted session-long agent
team design. The generic package must accept an optional neutral team catalog,
validate it strictly, produce an immutable canonical catalog and behavior-only
native role files, and expose native model defaults without inventing model
fallbacks. The organization layer must forward the optional policy and define
an independent retained review procedure. The site workspace must be the sole
owner of the actual role, model, effort, team and watcher choices.

Acceptance for this slice requires:

- no automatic Astra selection or fallback;
- `delegated`, `lead_designed` and `solo` site teams with explicit compatible
  role/model/effort combinations;
- session-lifetime designer, implementer and reviewer definitions;
- a fresh independent Sol/xhigh reviewer that is subsequently reusable;
- designer and implementer defaulting to xhigh, with high permitted only for a
  bounded simple task whose reason is recorded;
- Luna/low represented only as a fresh operation-scoped utility watcher for
  long or uncertain builds, tests, workflows, CI waits and deployment waits;
- four native child slots, excluding the root, so three retained specialists
  and one transient watcher can coexist;
- generated role TOMLs that contain behavior only, leaving model and effort to
  explicit native spawn settings and sandbox/approval to live inheritance;
- `teamConfig = null` retaining unmanaged native behavior rather than creating
  a vpsFree.cz lineup; and
- no source publication, default-branch integration or deployment in this
  slice.

## Initiative and records

- Slug: `2026-09-21-agent-teams-workflow`
- Plan: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-21-agent-teams-workflow/plan.md`
- State: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-21-agent-teams-workflow/state.md`
- Portal manifest: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-21-agent-teams-workflow/portal.yml`
- Accepted source proposal:
  `/home/aither/workspace/ai/vpsfree.cz/tmp/codex-workspace-token-efficient-workflow-v3.md`

## Repositories and reviewed ranges

1. Generic `dev-workspace`
   - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-21-agent-teams-workflow/dev-workspace`
   - Base: `b52a2363be8bb9985e4b9f254fb43e8cade4551d`
   - Head: `39bfa664298443334d12b08dd42a475eef1c38e4`
   - Commit: `teams: add immutable agent catalog contract`
2. Organization `vpsfree-dev-workspace`
   - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-21-agent-teams-workflow/vpsfree-dev-workspace`
   - Base: `298a8a42282f193c82a24e87a95300548a4d5903`
   - Head: `583647dd998e5b4cb0e9fa6833e29bb5aec757b8`
   - Commit: `teams: forward policy and retain independent review context`
3. Site workspace (`vpsfree-cz-workspace`)
   - Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-21-agent-teams-workflow/workspace`
   - Base: `e55bb318c2db3a1bf698511f9040da57f76b013c`
   - Head: `0ccd1101f56499b69312c72de82f4171dde08762`
   - Commit: `teams: define retained development roles`

All three worktrees were clean when this packet was prepared.

## Commit split

There is one logical commit per owning repository. The generic commit owns the
schema, validation, generated artifacts, package metadata, neutral native
model-default behavior, tests and generic documentation. The organization
commit owns only policy pass-through and the vpsFree.cz review procedure. The
site commit owns the concrete catalog and site-specific instructions/assertions.
Tests and documentation remain with the behavior they validate and explain;
separating them would make each cross-project contract commit harder to review
and revert coherently.

## Non-goals, rejected alternatives and user decisions

- No orchestration service, scheduler, message bus, pricing engine, metrics
  dashboard or generalized DAG implementation.
- No `codex-web` change: capability inspection found that the current pin
  already supports thread settings and child activity observation.
- No host-configuration change yet: the native child-capacity setting will be
  supplied by the package/runtime integration unless later deployment proof
  shows a host-level requirement.
- Role TOMLs intentionally do not encode model, effort, sandbox or approval.
  Model/effort are explicit spawn settings; sandbox/approval inherit the live
  root permission profile.
- The reviewer is fresh only at initial review creation. The same reviewer is
  retained for coherent finding remediation and later relevant revisions.
- Luna is not a team member and is never retained. Every long or uncertain
  operation gets a fresh Luna/low watcher.
- Source pushes, publication, default-branch integration, configuration-master
  integration, archive and deletion are outside the current authorization.

## Dependencies and configuration

- Generic adds `teamConfig ? null` and packages a validated catalog only when
  configured.
- Organization adds the same optional argument and forwards it only when
  non-null, preserving evaluation against the currently pinned generic package.
- Site imports `config/agent-teams.nix` and supplies it to the organization
  package. It currently pins the pre-feature organization revision and is
  therefore evaluated for this branch with local generic and organization
  overrides. Remote pin updates belong to the later authorized publication and
  dependency-integration phase.
- The site catalog requires native
  `agents.max_concurrent_threads_per_session = 4`; Codex documents this limit as
  excluding the root thread.

## Documentation changed or checked

- Generic: `README.md`, `docs/workspace-portal.md`
- Organization: `skills/mandatory-change-review/SKILL.md`
- Site: `AGENTS.md`, `docs/agent-instructions/verification.md`
- Durable cross-project rationale and rollout boundaries remain in the
  initiative `plan.md`; this packet is review evidence, not product guidance.

## Quick verification

- Generic Nix parse/diff checks passed.
- `nix eval .#checks.x86_64-linux.agent-team-catalog.drvPath` passed.
- `nix eval .#packages.x86_64-linux.dev-workspace.drvPath` passed.
- `ruby -c libexec/workspace-host` passed.
- `nix develop -c go test -mod=mod ./internal/workspacecodex ./internal/web ./cmd/workspace-portal`
  passed.
- The unflagged Go command encountered the repository's pre-existing stale
  local vendor tree; it made no changes. Module mode follows `go.mod` and passed.
- `gofmt` diff was empty.
- Organization Nix parse/diff checks and its current pinned package evaluation
  passed.
- Organization evaluation with local generic override and non-null site policy
  passed.
- The changed review skill passed its canonical `quick_validate.py` under a
  Python environment containing PyYAML. A fresh Luna/low operation watcher ran
  the validation; the first system-Python invocation lacked PyYAML and the same
  watcher reran the corrected exact command successfully.
- Site Nix parse/diff checks passed.
- Site policy validated against the generic schema using local overrides.
- `ruby test/agent_instructions_test.rb` passed: 2 runs, 32 assertions.

Long package builds and integration tests have intentionally not started. A
fresh Luna/low watcher will own them only after the review gate is accepted.

## Review remediation verification

The generic commit was amended in place after the first review. It now makes
the monitor procedure catalog-neutral, preserves omitted unmanaged App Server
settings through `thread/start`, removes obsolete generic Astra UI/docs/default
probing, includes team name and generated behavior/generator/adapter identity in
digests/native names, and applies forbidden-setting checks to the utility TOML.
Creation retry validation accepts only a fully omitted captured unmanaged
model/effort pair; explicit, effort-only and fork paths remain strict.

- Nix parse and package/catalog drvPath evaluations passed.
- `ruby -c libexec/workspace-host` passed.
- Gofmt and diff checks passed.
- A fresh Luna/low watcher ran
  `nix develop <generic> -c go -C <generic>/portal test -mod=mod
  ./internal/workspacecodex ./internal/web ./cmd/workspace-portal` on exact head
  `b5eafc66498997e947054cae3145d09dde61a98c`; all packages passed. The final
  test-only amendment at `39bfa664298443334d12b08dd42a475eef1c38e4`
  independently recomputes native names from the emitted identity and canonical
  inputs; Nix parsing and drvPath evaluation pass.
- The same operation-scoped watcher ran canonical `quick_validate.py` for the
  changed `dev-session-monitor` skill in a PyYAML Nix environment; it passed
  with `Skill is valid!`.
- Earlier watcher invocations are not code evidence: two used the wrong Go
  module directory. The first correct module run exposed and preserved a real
  test log, leading to fixes for stale slow-validation fixtures and unmanaged
  retry validation before the successful exact-head run.

## Risk and selected review lanes

Overall risk is **high** because this is a new versioned cross-project package
and runtime-policy contract that affects deployment, mixed package generations,
rollback and the semantics of future agent execution. Review effort is xhigh.
General, architecture/repetition, scope/proportionality and
risk/compatibility all apply. Per the user-approved team design, one fresh
independent Sol/xhigh reviewer covers all four lanes in one coherent context
and is retained after this first review. This intentionally replaces the
installed skill's older Astra/per-lane topology while retaining all lane
criteria, packet requirements, severities and remediation gates.

## Compatibility and deployment assumptions

- The new package contract is additive. `teamConfig = null` preserves unmanaged
  behavior.
- Existing sessions remain unmanaged or legacy-bound until explicit adoption.
- Managed sessions will pin immutable catalog content and native role files;
  later runtime work must fail closed if a rollback generation cannot interpret
  that session's catalog/state.
- Generic, organization and site package generations are integrated in that
  dependency order. Mixed source revisions are supported during development by
  null forwarding and local flake overrides.
- No database, public vpsAdmin API, node protocol, daemon message or vpsAdminOS
  persisted-state format changes occur in this slice.
- No deployment occurs before downstream pins, combined package checks and
  explicit aitherdev smoke/rollback evidence in the later phase.

## Ownership, interface and consumers

- Owner: generic `dev-workspace` owns the `teamConfig` schema/validator,
  canonical digest, generated role artifacts and package metadata.
- Public package interface: optional Nix argument `teamConfig`; resulting
  catalog/metadata consumed by later portal/session runtime code.
- Organization consumer: `vpsfree-dev-workspace` forwards a non-null catalog
  without imposing concrete policy.
- Site consumer/owner of choices: `vpsfree-cz-workspace` supplies
  `config/agent-teams.nix`, verifies delivered artifacts, and defines local
  development/review/watcher procedure.
- The current `codex-web` pin is an observed runtime client, not a changed
  consumer in this slice.
- Later session/portal/runtime phases are the intended consumers of catalog
  metadata. They are deliberately not preimplemented here.
