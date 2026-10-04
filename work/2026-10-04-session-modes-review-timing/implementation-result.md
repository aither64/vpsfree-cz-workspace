# Implementation result

Implementer0 completed the bounded accepted-plan edits in the three assigned
feature worktrees. Changes remain uncommitted for the external lead's prose
pass, verification selection, dependency pins and commit sequencing.

## Behavior and documentation

- Distinct Solo, Lead-designed and Full-team lead prompts. Solo owns investigation,
  design and application editing with no automatic specialists; a bounded small
  edit needs no separate design document. Lead-designed owns design in the lead,
  delegates application edits, has no designer and has two specialist slots.
  Full team retains the designer and delegated implementation.
- Implementers accept architect-owned or lead-owned substantive briefs. All new
  lead and reviewer prompts require explicit direction for early review. Early
  review is advisory and does not replace final committed-deliverable review
  after quick checks and before long integration tests. Completed substantive
  documentation/configuration stays in scope; planning, investigation, findings,
  session tracking and evidence alone never trigger automatic review.
- Aligned workspace instructions, routed sessions/verification guidance, site team
  guide, generic runtime session/portal guides, extension README and owning review
  skill including frontmatter and agent metadata. Whole-branch/migration gates,
  mechanical-update exemptions and narrow-fix review policy remain intact.
- Preserved models, efforts, allowed efforts, role access, defaults, schema and
  separate watcher policy. No API, state-schema, snapshot, lifecycle, public CLI,
  CI or roster mutation code changes; no migrations.
- Meaningful coverage extends existing policy assertions, exact frozen lead prompt
  pass-through, lead-owned development validation/projection, Solo projection,
  visible 1/3/4 counts on new-session and plan dialogs, creation retry retention
  of an older four-member Lead-designed snapshot, and fork retry retention of
  that older lineup/settings/prompts after catalog replacement.

## Changed files

Paths are relative to the named worktree under
`worktrees/2026-10-04-session-modes-review-timing/`.

`workspace`:

- `AGENTS.md`
- `config/agent-teams.nix`
- `docs/agent-instructions/sessions.md`
- `docs/agent-instructions/verification.md`
- `docs/agent-teams.md`
- `flake.nix` (existing policy assertions only; no pins changed)
- `test/agent_instructions_test.rb`

`dev-workspace`:

- `docs/dev-sessions.md`
- `docs/workspace-portal.md`
- `portal/internal/agentteams/catalog_test.go`
- `portal/internal/teamruntime/runtime_test.go`
- `portal/internal/web/server_test.go`
- `portal/internal/workspacecodex/lead_policy_test.go`
- `test/dev_session/agent_team_creation_test.rb`

`vpsfree-dev-workspace`:

- `README.md`
- `skills/mandatory-change-review/SKILL.md`
- `skills/mandatory-change-review/agents/openai.yaml`
- `test/skill_policy_test.rb`

## Quick evidence

- `dev-session current` from the canonical session directory printed the exact
  bound slug. Both identity environment variables were absent. The earlier call
  from the canonical workspace root found no current session; the intended
  session-directory call established identity before any session-file access.
- `git diff --check` passed in all three worktrees.
- `nix eval --json --file config/agent-teams.nix` passed from the workspace
  worktree. Evaluation confirmed counts Solo/Lead-designed/Full team = 1/3/4,
  design owners lead/lead/designer, capacities 0/2/3, distinct prompts and
  unchanged lead model/effort/access settings.
- Pure Nix assertions comparing the previous `HEAD:config/agent-teams.nix` with
  the edited catalog passed for every retained role's settings excluding prompt
  text, work policy, utility policy, capacity, schema and both default-team keys.
- `nix-instantiate --parse flake.nix` passed in workspace and extension.
- `AGENTS.md` is 16,061 bytes, below its existing 16 KiB discovery-limit assertion.
- Diff inspection confirmed `leadDeveloperInstructions`, `legacyBehaviorInstructions`
  and runtime production Go/Ruby files are unchanged. Retained snapshot behavior
  is exercised by changed tests rather than new runtime paths.

Ruby/Go checks and gofmt are still pending. The pinned Nix environment could not
be realized in this member's sandbox: from the runtime worktree,
`nix build --offline --dry-run --inputs-from . nixpkgs#ruby nixpkgs#go nixpkgs#jq`
failed with `cannot connect to socket at /nix/var/nix/daemon-socket/socket:
Operation not permitted`. Approval policy is never; no escalation or ambient
interpreter fallback was used. The lead received this gap while work continued.
No long/uncertain check, packaged suite or integration test was launched.

## Exact remaining commands

Use each worktree's pinned tool environment. The following `nix shell` invocations
resolve tools from that repository's inputs. The lead selects/launches uncertain
Go compilation or environment realization through its utility watcher.

Workspace:

```sh
nix shell --inputs-from . nixpkgs#ruby -c ruby test/agent_instructions_test.rb
```

Extension:

```sh
nix shell --inputs-from . nixpkgs#ruby -c ruby test/skill_policy_test.rb
```

Runtime formatting (before commits):

```sh
nix shell --inputs-from . nixpkgs#go -c gofmt -w portal/internal/agentteams/catalog_test.go portal/internal/teamruntime/runtime_test.go portal/internal/web/server_test.go portal/internal/workspacecodex/lead_policy_test.go
```

Runtime focused Go checks (from the runtime root):

```sh
nix shell --inputs-from . nixpkgs#go -c go -C portal test -mod=readonly ./internal/workspacecodex -run 'TestLeadPolicy' -count=1
nix shell --inputs-from . nixpkgs#go -c go -C portal test -mod=readonly ./internal/agentteams -run 'TestDevelopmentTeamAcceptsPurposeBasedCustomRoles' -count=1
nix shell --inputs-from . nixpkgs#go -c go -C portal test -mod=readonly ./internal/teamruntime -run 'TestCatalogPresetUsesExplicitSiteSettingsAndArchitectAddress|TestCatalogPresetProjectsLeadOwnedDevelopmentWithoutDesigner|TestSoloCatalogPresetSerializesEmptyMembers|TestSoloPresetRetainsSelectionWithoutSpecialistThread|TestMemberPolicyBindsSessionAndRetainsInstructions|TestCatalogPresetRetryReusesPersistedThreadAndDoesNotAppend|TestForkKnownThreadRetryUsesFrozenSnapshot' -count=1
nix shell --inputs-from . nixpkgs#go -c go -C portal test -mod=readonly ./internal/web -run 'TestNewSessionShowsConcretePresetLeadSettings|TestDirectTeamPresetAcceptsFrozenCustomRoleInstructions' -count=1
```

Runtime focused Ruby checks (aggregate loader):

```sh
nix shell --inputs-from . nixpkgs#ruby -c ruby test/dev_session_test.rb --name '/test_prompt_bearing_direct_snapshot_and_thread_flags|test_cli_team_resolves_the_installed_direct_snapshot_without_hidden_lead_defaults|test_cli_team_retry_keeps_frozen_snapshot_after_catalog_changes/'
```

After the lead pins and commits all intended changes, final independent review
must cover all three full branches and explicitly conclude no migrations. Only
then run `nix flake check --print-build-logs` in each worktree against the final
pins, through the lead's separate watcher. Real-browser tests and host/cluster
VMs were not introduced or justified by these policy-only changes.

## Deviations and ownership

The lead explicitly clarified the original generic-policy item: preserve both
legacy fallback prompt constants exactly; new orchestration belongs in catalog
snapshots, with generic guidance and meaningful retention/projection coverage.
The later reviewer timing and Solo small-edit clarifications were incorporated.
No other design deviation. The Nix sandbox failure is the remaining verification
gap, not a change to the design.

No commits, pushes, rebases, dependency pin updates, deployments, hooks,
subagents, CI workflow edits, live roster mutations or lifecycle actions were
performed. Parent plan/state/portal records were left untouched; this is the
only implementation-owned canonical tracking artifact.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-04-session-modes-review-timing/
