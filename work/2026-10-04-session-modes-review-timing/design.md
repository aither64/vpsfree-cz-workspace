# Session modes and review timing: implementation brief

Status: bounded reconciliation of the accepted [plan](plan.md), 2026-10-04.
Design owner for this brief: architect0. The external lead coordinates this
initiative and assigns application edits. This is not an additional review or
a proposal to change the accepted architecture.

## Scope and ownership

All feature paths below are relative to the named worktree under
`worktrees/2026-10-04-session-modes-review-timing/`. Architect0 owns only this
file and [design-result.md](design-result.md). The lead retains state, portal
registration, assignments, commit/pin sequencing, final review and deployment.
Implementers edit the three application worktrees; this assignment creates no
members, assigns no reviewer, and performs no commit, push or deployment.

| New preset | Persistent lineup | Design / application owner | Specialist capacity |
| --- | --- | --- | --- |
| `solo` | lead (1 total) | lead / lead | `max_open_agents = 0` |
| `lead_designed` | lead, implementer, reviewer (3 total) | lead / implementer | `max_open_agents = 2` |
| `delegated` (Full team, unchanged default) | lead, architect, implementer, reviewer (4 total) | architect / implementer | `max_open_agents = 3` |

Solo permits investigation, design and application editing without acquiring
specialists. Its independent final reviewer remains a temporary standalone
reviewer selected by the mandatory-review skill; its long-check watcher remains
a separate utility. Neither joins the roster. Lead-designed has
`design_owner = "team_lead"` and no designer role. Full team keeps
`design_owner = "designer"`. User-directed creation of a selected preset is
distinct from later team changes: do not add, replace or reconfigure members
without explicit user direction. Existing manual team controls remain available.

Preserve every model default, role access and work-effort rule: Sol leads,
implementers and reviewers; Astra architect; Luna/low watcher; Solo and Full-team
lead default high with high/xhigh allowed; Lead-designed lead default xhigh;
substantive design/implementation xhigh, bounded simple high with a recorded
reason. Preserve reviewer independence, read-only access and saved effort.
Keep catalog schema 4, global native capacity 4 and utility policy unchanged.

## Small edits and authoritative documentation

| Worktree / files | Implementation responsibility |
| --- | --- |
| `workspace/config/agent-teams.nix` | Give Solo, Lead-designed and Full team distinct lead prompts. Share only common progress, verification and final-review requirements. Restore Solo source ownership; remove `designer` from Lead-designed, set its design owner and capacity, and retain the Full-team lineup. Let the implementer follow either the designated architect's brief or the lead's brief according to the selected mode. Require explicit user direction for later roster changes and explicit requests for early review. |
| `workspace/AGENTS.md`, `docs/agent-instructions/sessions.md`, `docs/agent-instructions/verification.md`, `docs/agent-teams.md` | Route design and source ownership by selected mode/retained instructions. Remove the universal architect and read-only Solo requirements. Keep identity/access failures actionable for work that is delegated; they do not justify silently taking over an implementer's assignment. Apply review timing consistently. The site team guide owns the concrete mode table and model defaults. |
| `workspace/test/agent_instructions_test.rb`, `flake.nix` | Replace obsolete Solo and four-member Lead-designed expectations. Assert all three role sets/counts, design owner, capacities, write access, distinct lead prompts, retained model/effort rules and final-review policy. Extend the existing policy checks rather than adding another policy framework. |
| `dev-workspace/docs/dev-sessions.md`, `docs/workspace-portal.md` | Describe catalog-owned mode selection, Solo source ownership, lead-owned design without an architect, manual team changes, review timing and preserved snapshots. Keep generic docs independent of site model choices and hostnames. Qualify the current unconditional design-delegation paragraph and distinguish current catalog defaults from saved policy. |
| `dev-workspace/portal/internal/workspacecodex/lead_policy_test.go`, `portal/internal/teamruntime/runtime_test.go`, `portal/internal/web/server_test.go`, existing creation/snapshot tests | Verify exact saved prompt pass-through, roster projection and visible 1/3/4 preset counts, including a lead-owned design preset. Reuse existing retry/fork coverage. Add focused cases only for changed contracts or missing coverage. |
| `vpsfree-dev-workspace/skills/mandatory-change-review/SKILL.md`, `test/skill_policy_test.rb` | Make the invocation boundary explicit in metadata, purpose and workflow step 1. Keep existing reviewer selection, lanes, findings handling, targeted remediation and whole-branch readiness gates. The skill remains authoritative for review routing. |
| `vpsfree-dev-workspace/flake.nix`, `flake.lock`; then `workspace/flake.nix`, `flake.lock` | Pin exact completed upstream feature revisions in dependency order; generate lock updates and inspect the full transitive diff. |

The runtime already accepts a development team whose design owner is the lead
(`nix/agent-teams.nix`), projects installed roles into presets, and saves exact
instructions. No new dispatcher, role, endpoint, schema or refresh mechanism is
needed. Preserve `LeadThreadPolicy`'s saved-instruction precedence and technical
binding. Its `leadDeveloperInstructions` constant is also the legacy fallback:
do not replace that original fallback in order to update catalog-created
sessions. Likewise preserve `legacyBehaviorInstructions`. The accepted new
orchestration belongs in the distinct catalog prompts and generic guidance.
Route any necessary deviation from this preservation boundary through the lead.

## Review trigger and implementation boundaries

Do not automatically assign a reviewer for routine planning, investigation,
findings, design reconciliation, session plans/state or evidence records.
Explicitly requested early review remains possible and must be described as
early review, without claiming final readiness. Merely having a reviewer in a
preset creates no assignment.

After the intended substantive deliverable is complete, committed and has
passed quick checks, run independent final review before long integration or
packaged checks. Substantive documentation, instructions, configuration, tests
and deployment changes are deliverables too; documentation-only work is not a
blanket exemption. Session tracking/evidence stays context for review and does
not itself trigger an assignment. Preserve existing exemptions for genuinely
mechanical dependency/generated updates and existing rules for narrow fixes
after a completed review.

Final review covers all three complete base-to-head histories, final diffs,
dependency pins and changed documentation. Inventory obsolete approaches and
follow-up fixes; the migration conclusion for this change is **no migrations**.
The external lead selects the reviewer under the installed skill, with retained
settings or its standalone fallback. No planning-review checkpoint is added.

## Compatibility, deployment and recovery

Existing sessions keep their exact roster, saved prompts, models, efforts and
access. A retry uses its recorded selection despite an updated catalog. A fork
copies the source snapshot, including the old four-member `lead_designed`
lineup if present; the destination gets only its normal fresh session identity
binding. Do not reinterpret saved preset IDs against the current catalog or
materialize missing members on resume. User-requested additions continue using
the existing installed-catalog path.

There is no API/CLI contract, database, manifest, roster, receipt, runtime
authority, protocol or on-disk format change. Existing schema-3 creation receipts
and schema-4 catalogs retain their current compatibility rules; no migration or
new compatibility shim is warranted. Old/new components can continue consuming
the same saved snapshots. New defaults require the composed new package.

Shared workspace rules and installed skills change globally when made available;
they are not frozen per session. Older saved prompts can therefore conflict
with newer shared guidance. This accepted limitation is documented rather than
repaired: do not refresh prompts, rewrite rosters, restart sessions to adopt
policy, or add a policy-refresh feature. Shared workspace master is not edited
as a shortcut to activating the feature-branch instructions.

The lead's rollout order is:

1. Complete and quick-check runtime changes; publish its exact feature revision.
2. Pin that revision in the extension, complete its skill/tests and publish its
   exact feature revision.
3. Pin the extension in the workspace feature branch. Verify expected runtime
   transitive pinning and unchanged unrelated inputs. These two consumers have
   ordinary flake inputs, not confctl-managed channels.
4. Commit all intended changes, run the complete independent final branch review
   and resolve/accept findings under the review skill. Then run longer packaged
   checks on those exact revisions, with the separate watcher.
5. Deploy from the workspace feature worktree with
   `workspace-host switch --source "$PWD"`, using the stable installed command.
   Record package revisions, results and preserved-state observations in the
   lead's rollout evidence. The application belongs in the user profile.

No aitherdev host configuration change is expected. If a real host dependency
appears, refer the scope change to the lead; its owner is
`vpsfree-cz-configuration`, deployed with confctl to
`cz.vpsfree/machines/aitherdev` after that repository's required procedures.
Do not pin the workspace application into host configuration. No vpsAdminOS
changes, coordinated machine update or cluster reset is needed.

Package recovery is a corrected forward `workspace-host switch`, or resuming
the same supported switch after resolving its refusal. The runtime deliberately
refuses selecting an older profile with `workspace-host rollback`; unchanged
formats do not override that policy. Preserve transition journals, generation
checks, retained ownership and schema checks. Do not use lifecycle actions or
state resets to work around a switch failure. Deployment does not authorize
default-branch integration; retain feature refs and keep the initiative active.

## Acceptance scenarios

1. New Solo has exactly one persistent lead, write access and instructions to
   design and implement. A normal implementation task does not add specialists.
   Required final review and long verification can use their separate utilities.
2. New Lead-designed has exactly lead/implementer/reviewer, lead-owned design,
   two specialist slots and a lead brief accepted by the implementer. New Full
   team remains the four-member default with architect-owned design.
3. New-session and plan-to-new-session views show matching 1/3/4 totals and
   role summaries. Model/effort defaults, supported efforts and role access
   remain intact; legacy/custom model fixtures must not be rewritten to site
   defaults merely because the defaults differ.
4. Routine planning/investigation and tracking-only edits cause no automatic
   reviewer assignment. An explicit early-review request remains supported.
   Completed application, documentation-only and configuration-only substantive
   deliverables require final independent review. Early review cannot satisfy it.
5. Catalog replacement leaves retained prompts, roster/settings and retry/fork
   snapshots untouched, including old Lead-designed sessions. Manual additions
   still work when explicitly directed; selecting a preset sends no work task.
6. Final composed package contains the changed catalog and review skill; its
   checks accept legacy and new snapshot shapes without schema changes.
   Deployment preserves existing sessions and requires no host reconfiguration.

## Verification brief

These are planned checks, not results from this design assignment. Use tools
from each repository's pinned Nix inputs/package environment. No flake declares
a default dev shell; use the package development environment or an appropriate
`nix shell --inputs-from .` tool shell. Do not silently use an unrelated ambient
toolchain. Execute known quick selectors inline; uncertain-duration checks and
builds go through the fresh Luna/low watcher under `dev-session-monitor`.

Quick checks before final review:

- Each changed worktree: `git diff --check`; inspect changed Nix/policy text
  against the mode table and excluded scope. Evaluate `config/agent-teams.nix`
  without a package build for role counts, ownership and unchanged effort policy.
- Workspace: `ruby test/agent_instructions_test.rb`.
- Extension: `ruby test/skill_policy_test.rb`; cover both the no-review examples
  and positive documentation/configuration final-review examples.
- Runtime Go, from the runtime root: focused `go -C portal test -mod=readonly`
  selectors in `./internal/workspacecodex` for `TestLeadPolicy`, in
  `./internal/agentteams` for lead-owned development and snapshot validation,
  and in `./internal/teamruntime` for catalog preset projection, role summaries,
  Solo without specialists, retained instructions, catalog-change retry and
  frozen-source forks. Include the corresponding added tests. Use
  `./internal/web -run 'TestNewSessionShowsConcretePresetLeadSettings|TestDirectTeamPresetAcceptsFrozenCustomRoleInstructions'`
  for rendered counts and saved prompts; keep these fixtures free of live Codex.
- Runtime Ruby: use the aggregate loader, for example
  `ruby test/dev_session_test.rb --name '/test_prompt_bearing_direct_snapshot_and_thread_flags|test_cli_team_resolves_the_installed_direct_snapshot_without_hidden_lead_defaults|test_cli_team_retry_keeps_frozen_snapshot_after_catalog_changes/'`.
  Do not invoke individual `test/dev_session/` files directly; they depend on
  shared helpers loaded by the aggregate entry point.
- Review source changes for accidental edits to schema versions, legacy prompt
  constants, snapshot/retry/fork mutation paths, public APIs, host modules,
  model defaults or work-effort rules. Check documentation links and remove
  contradictory current-mode prose, while retaining historical session records.

After independent review, the watcher runs
`nix flake check --print-build-logs` in runtime, extension and workspace against
the final pins. This includes runtime Go/Ruby/package and catalog contracts,
extension skill/packaging checks, and workspace `agent-instructions`,
`agent-team-policy`, deployment and provider-composition checks. Keep command
logs, exact heads and exit status in lead-owned evidence. Escalate unexpected
local kernel builds under workspace verification policy.

The existing real-browser team suite is a longer opt-in check, not a quick Node
test; run it after review only if rendering behavior changes or focused count
coverage leaves a concrete gap. Host-migration VMs and development-cluster VMs
are not required by this policy-only change. Inspect installed catalog/skill
content and retained-state preservation after the user-profile switch without
creating or changing live teams merely for a smoke test.
