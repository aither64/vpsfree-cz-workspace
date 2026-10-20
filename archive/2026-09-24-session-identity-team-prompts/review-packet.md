# Consolidated review packet: session identity and catalog role prompts

This packet records the pre-remediation review assignment. Final heads,
findings, fixes, checks, deployment and merge evidence are in `state.md`.

Review all committed changes in the three linked feature branches as one change.
The requested result is: portal-created threads can prove exact session identity
despite tool shells missing `DEV_SESSION_*`; persistent lead/member instructions
are configured in the team catalog, not hardcoded in the portal; custom role
names have stable purposes; prompts are carried with the first actual request,
without a prompt-only model turn. CLI and portal creation remain equivalent.
Retry/fork/revive must preserve frozen policy, while fork rebinds destination
identity. Team selection, reviewer routing and portal Add Member must work for
custom roles. User approved deployment to aitherdev and integration to master.

Initiative: `2026-09-24-session-identity-team-prompts`.
Plan/state: `work/2026-09-24-session-identity-team-prompts/{plan,state}.md`.
Feature worktrees under `worktrees/2026-09-24-session-identity-team-prompts/`:

- `dev-workspace`: base `1b836baf85e8486e0455ce2a70f9c4423328ac22`, head
  `9665c06766641a2781d998ed7f66c38950f94ed4` (one runtime commit).
- `vpsfree-dev-workspace`: base `ad13e7fc2a1874a54921bb91d743e4a4851d3c4a`,
  head `8cbb7ec84915414fb141113b3731eef638390bcc` (extension skills and a
  separate generic-runtime pin).
- `workspace`: base `7787ee79eadd14c2a7623eeb7a6b206b75ad9ee8`, head
  `8fb50c714919e4c4289b4c7dd5a9e1735e49e54f` (site rules, team config,
  site-package pin). This one commit bundles the site contract and pin because
  its schema-4 policy check and role fields cannot evaluate against old runtime.

The generic runtime owns the team catalog schema, direct creation snapshots,
rosters, thread developer instructions and portal session creation. Its public
consumers are the vpsFree extension (pinned by `flake.nix`/`flake.lock`) and the
site workspace (pins the extension). The extension owns mandatory-review and
handoff skill rules. The site workspace owns site role defaults and the operator
AGENTS/procedures. The new generic commit also updates the nested `codex-web`
lock pin transitively; no direct codex-web code change here.

Key implementation/documentation areas: generic `nix/agent-teams.nix`,
`portal/internal/agentteams`, `portal/internal/teamruntime`,
`portal/internal/workspacecodex`, `portal/internal/web`, Ruby `libexec/dev-session`;
extension `skills/{dev-session-handoff,mandatory-change-review}/SKILL.md`;
site `config/agent-teams.nix`, `docs/agent-teams.md`, `AGENTS.md`,
`docs/agent-instructions/{sessions,verification}.md`. The plan carries
deployment compatibility rationale; individual rollout evidence belongs in
state, not reusable docs.

Risk: **high**. This alters session ownership and a persisted roster/receipt
contract across runtime/extension/site packages, plus package transition and
rollback assumptions. Review lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. The installed catalog fallback is
`gpt-6-sol`/`xhigh`; current initiative has no retained roster/reviewer, so use
one fresh standalone reviewer. Reviewer's native role behavior config is the
installed delegated reviewer-xhigh TOML; model/effort are catalog settings.

Compatibility: catalog schema moves 3 to 4. Direct receipt envelope remains
schema 3 but accepts strict old or new snapshot shape. Old saved rosters use
exact legacy behavioral fallback. New snapshot may be unreadable by old package;
one-host aitherdev upgrade is intentionally forward-only after new sessions
are created. No database, vpsAdmin node, daemon protocol, API client, or cluster
schema changes. User specifically favored faster implementation over rollback
compatibility for this development-only host. The portal may prepend exact
technical identity; catalog supplies behavior. No user-editable role editor in
portal this phase; roles are configured in site Nix. No model request occurs at
idle thread start; developer instructions go into the first real turn.

Quick verification already passed: generic `go test -mod=mod` for
`./internal/agentteams ./internal/teamruntime ./internal/workspacecodex
./cmd/workspace-portal` and full `./internal/web` inside `nix develop`;
Ruby direct creation suite (9 runs/57 assertions) and revive test (1/27);
site agent-instruction tests (4 runs/48 assertions); extension skill quick
validators; site Nix catalog generator evaluated `valid = true`; site
`agent-team-policy` derivation evaluated. `git diff --check` clean in each
feature worktree. Long package checks and deployment deliberately await review.

Non-goals: changing production services or KB content, adding a portal role
editor, moving teams between sessions, preserving backward package rollback,
or inventing new shell-ownership heuristics from CWD. Do not demand speculative
support for arbitrary old receipt shapes: only the actual deployed shape is a
supported predecessor. The local operator is trusted for workspace
integration/namespace migration per extension AGENTS, but this does not relax
remote-client, KB publication, or session isolation requirements.
