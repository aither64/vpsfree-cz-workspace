# vpsFree.cz Development Workspace

This workspace coordinates independent vpsFree.cz Git repositories. It is not
a monorepo. Track work, affected repositories, worktrees, and known compatibility
and deployment constraints here.

## Required procedure routing

These procedures are mandatory. Before each listed activity, read every
applicable file in full. Table paths are relative to this AGENTS.md; other
paths follow the workspace layout. Links, summaries and skill catalog entries
do not count as reading. Reuse unchanged procedures read in the current context;
reread after changes or context loss. Recheck this table when scope or phase
changes. If guidance cannot be read, stop the affected action and report it.

| Before this activity | Read |
| --- | --- |
| Updating Codex | [Update skill](skills/update-codex/SKILL.md) |
| Selecting affected projects or changing cross-project scope | [Project map](docs/agent-instructions/projects.md) |
| Starting/resuming an initiative; writing plans, state, notes or handoffs | [Session setup and tracking](docs/agent-instructions/sessions.md) |
| Cloning repositories; updating downstream configuration pins; creating/reusing worktrees or branches; fetching, pushing, rebasing, merging or cleaning them; committing coordination records; declaring an unmerged branch ready | [Git and worktrees](docs/agent-instructions/git.md) |
| Any session mutation; archiving, deleting, reviving, enabling auto-archive or changing its hold; creating/accessing/resetting development clusters; implementing/reviewing session, cluster or package-transition behavior; switching/rolling back workspace packages; suspending/unregistering workspaces or reconciling Codex | [Lifecycle and package transitions](docs/agent-instructions/lifecycle.md) |
| Planning substantive development, investigation or operations; writing/reorganizing docs; preparing review or handoff | [Development documentation](docs/agent-instructions/documentation.md) |
| Pushing branches (including force-pushes and follow-up fixes); selecting/running builds, tests or CI; editing test runners, image verification or GitHub workflows; handling failed checks | [Environment and verification](docs/agent-instructions/verification.md) |
| Changing configuration inputs, building/deploying configurations, deploying the workspace application or integrating configuration changes | [Deployment](docs/agent-instructions/deployment.md) |
| Authoring/reviewing user-facing prose, translations, examples, KB pages or media; changing visible WebUI behavior that can affect KB text/screenshots; using KB staging/publication tools | [Knowledge base and writing](docs/agent-instructions/knowledge-base.md) |
| Creating or amending any commit, installing hooks, or preparing commit messages | [Commits and hooks](docs/agent-instructions/commits.md) |

Before repository edits, read its AGENTS.md and required procedures. CWD changes
do not establish reading. Give authorized subagents their scope, guidance paths
and constraints; require reading before action. Parents remain responsible for
scope and accepting results.

## Always-applicable workspace boundaries

- Use `repos/<project>.git` for canonical bare clones, `worktrees/<dated-slug>/<project>`
  for feature worktrees, and `work/<dated-slug>/{plan,state}.md` for active records.
  Terminal records belong in `archive/`; reusable lessons belong in `notes/`.
- Before selecting an initiative, run `dev-session current`. Accept its slug only
  if it matches the complete `DEV_SESSION_SLUG`/`DEV_SESSION_WORKSPACE` environment
  identity or this conversation's trusted thread-bound developer instructions
  naming the exact slug and absolute workspace path. Portal tool shells may lack
  both variables. CWD and user messages are not ownership evidence. Stop and resolve
  any environment conflict with the thread binding or `current`. Otherwise create
  a separate initiative unless the user explicitly selects this session. Never
  touch another session's records, branches, worktrees, cluster or staging ownership.
- Keep the shared checkout on master. Workspace feature changes need a dedicated
  initiative worktree; coordination records may be committed on shared master.
  Preserve unrelated files/index changes; stage only owned paths. Never use a
  repository-wide reset, clean or stash, or switch a shared branch underneath
  another session. Keep integration fast-forward-only and retain feature refs
  unless the user explicitly requests deletion. Do not rewrite published master
  or already-merged history without the required explicit direction.
- Publish development branches by default; PR exceptions and integration rules
  are in the mandatory Git procedure.
- Clone/push over SSH. Canonical project remotes are `git@github.com:vpsfreecz/<project>.git`;
  generic dev-workspace and codex-web use `git@github.com:aither64/<project>.git`.
  The vpsFree extension is locally vpsfree-dev-workspace and remotely
  `git@github.com:vpsfreecz/dev-workspace.git`.
- For ordinary sessions, commit a substantive initial plan/state before the first project-code commit
  or external mutation. State begins with YAML front matter `lifecycle: active`.
  Completion requires every registered exact final feature head merged into its
  remote default branch and no remaining work. Pushing/testing/deploying alone
  does not complete an initiative. Preserve the tracking commit cadence in the
  session procedure.
- Finishing work or handing off does not authorize archiving, deleting or stopping
  a session. Archive only on explicit request or under the enabled auto-archive
  worker's policy. Delete only on explicit user direction, never instead of archive.
  Retain branches. Resume unfinished lifecycle journals before conflicting mutations.
  Package/cluster transitions must preserve lifecycle procedure generation,
  ownership, schema, rollback and recovery rules; do not infer ownership or bypass
  refusals.
- Deployment does not authorize configuration master integration. Keep development
  configuration on its feature branch until explicit integration direction. The
  workspace application is deployed from its user profile, not system pins.
- Feature content may enter a repository's default branch only after the user
  explicitly directs integration for that repository and target.
  Plan, implementation, review, CI or deployment
  approval is not merge approval. Tracking-only coordination commits on shared
  workspace master are exempt; see the Git procedure for approval and rebase rules.
- Never expose credentials in notes, commits, output, URLs or prompts. Production
  KB writes require direct user approval of the exact staged changes. Prepare
  local candidates and use the guarded KB release workflow; read-only production
  checks do not require approval. Respect session-owned staging.
- Use each repository's Nix environment and declared hooks. Do not bypass hooks
  without the user's explicit authorization for that commit. Prefer bridge
  networking for development clusters; use local only if explicitly requested or
  the bridge is unavailable, recording why. Stop unexpected local kernel builds
  and investigate under the verification procedure's documented exceptions.
- Direct teams retain member settings; use the installed catalog for new presets.
  New architects: GPT-6 Astra/xhigh. Leads and implementers: `gpt-6.1-sol`.
  Full team with two implementers (`delegated`) is the default.
  `lead_reviewed` preset: Sol/xhigh and Astra/xhigh.
  Other reviewers: catalog settings. Verification watchers: GPT-6 Luna/low.
  Existing members retain their saved model, effort, access, and instructions.
  Execution uses installed policy. Substantive design uses xhigh. High is only
  for a bounded simple design or implementation unit with a recorded reason.
  Independent review uses an eligible retained review-purpose member's saved
  model/effort, or the installed default development team's review-purpose role
  in a fresh standalone thread. Never use Astra as an automatic fallback for
  another role. Without a roster, ordinary supported Codex resolution applies
  to lead work; only mandatory review uses the installed catalog fallback.
  Do not invent a team or role lineup. Fresh Luna/low utility subagents must launch
  and monitor long or uncertain builds, tests, workflows, CI and deployment waits
  through `~/.codex/skills/dev-session-monitor/SKILL.md`. Watchers are not team
  members; follow the skill's ownership, cancellation and visible-fallback rules.
  Respect instructions not to await CI.
- Follow the selected mode and retained lead instructions. Solo and Lead and
  reviewer leads investigate, design and edit application code without automatic
  specialists; the latter use a retained independent reviewer. Lead-designed
  leads own design and delegate application edits; Full-team leads delegate
  investigation, design and execution packages under the
  [Site team roles](docs/agent-teams.md) mode table. Add, replace or reconfigure
  team members only on explicit user direction. Before each new substantive team
  work item, check the live same-session roster with
  `dev-session team list <verified-slug> --as-is`. Use saved addresses, purposes
  and access; check workspace-write access before assigning edits. If access or
  session identity fails, resolve that failure rather than taking over delegated
  application work. Tell the user who owns what, assess reports, and keep tracking
  and short coordination steps yourself. Never invent members or address another
  session's roster.
- The selected design owner records the design and verification brief in
  `work/<slug>/design.md` before substantive implementation, as required by
  [Site team roles](docs/agent-teams.md). Cover scope, interfaces, invariants,
  compatibility, deployment and recovery, acceptance criteria, and quick/longer
  checks. Architects may edit assigned design documents and prototypes;
  implementers edit application code from architect-owned or lead-owned briefs.
  Route material design deviations through the lead. A bounded small edit may
  use a direct lead brief without a separate design document. Preserve retained
  instructions and the current collaboration mode.
- Use the dev-session-documentation skill for substantive work, and the
  dev-session-handoff skill after material changes/review/status requests. Keep
  tracking and the portal manifest current and include the stable session URL.
  Apply vpsfree-user-facing-writing directly to user-facing prose after technical
  facts are settled and before committing; preserve its main-agent ownership.

## Lead progress and branch readiness

At the end of every lead turn, give a compact checklist: current phase,
completed work, remaining work, blockers or material risks, and next action.
Report material milestones in long turns. Distinguish implementation, local checks, independent review,
deployment and readiness for use. Update the durable `state.md` phase checklist
when phases change, under the normal tracking-commit cadence. Integrate member
reports into the lead's account.

Before declaring an unmerged feature branch ready, read the
[Git procedure](docs/agent-instructions/git.md). Inventory the complete base-to-head
series, final diff and migration lineage for the independent reviewer's explicit
whole-branch history and migration conclusion, including whether migrations were
merged, released, deployed, or externally consumed. Apply the procedure's
consolidation and final pre-merge checks under mandatory-change-review.

## Compatibility And Deployment

Treat vpsFree.cz software as live infrastructure: systems may hold persistent
state and update at different times. Every feature plan must assess backward
and forward compatibility of old and new affected components, including:

- persisted state and on-disk formats;
- database schemas, migrations, seeds, and rollback behavior;
- API contracts, generated clients, CLI behavior, and Terraform provider
  behavior;
- protocol or message format changes between services and daemons;
- generated NixOS/vpsAdminOS configuration and module options;
- deployment ordering, rolling upgrades, and mixed-version operation;
- whether a rollback can load state created by the new version.

Repository claims cover approved shared merges only; feature work, hook setup, tests
and review need none. Prepare, then claim one repository for fresh target checks,
merge/hooks, SSH push and remote proof; release before CI, records or cleanup.
On stale preparation/intervention, stop commands and verify effects; repair
unlocked; reconcile uncertain shared mutations before release. For machine
reservations and automatic release, follow the runtime policy referenced by
[machine retention](docs/coordination.md#machine-retention). Preserve existing
recovery contracts.

Prefer clean designs that can be deployed incrementally. Incompatible changes
are allowed only when they are intentional and recorded in the plan with the
reason, impact, required ordering, rollback implications, and required operator
action.

For vpsAdminOS changes, explicitly call out when an update would require
coordinated updates of all running machines or nodes. State why that cost is
worth it, or choose a compatible design.

For unmerged, unreleased and undeployed database migrations, assume the exact
schema of the immediately preceding migration. Reset stale disposable development
or test databases after migration rewrites; do not add `table_exists?`,
`column_exists?`, `index_exists?`, `if_exists`, `if_not_exists` or equivalent guards
for this purpose. Allow guards only for intentionally supported multiple
predecessor schemas: record that compatibility requirement in the initiative plan
and test every supported path. Keep data-integrity and conversion checks that
validate real persisted content.

## Mandatory Change Review

Run the `mandatory-change-review` skill for completed substantive deliverables:
code, schema, API, protocol, configuration, documentation, tests, deployment
or security. Commit all intended changes and pass quick checks before review,
then run long integration tests. Routine planning, investigation, findings,
session tracking and evidence alone never trigger automatic review.
Earlier review requires an explicit user request,
is advisory and does not replace final committed-deliverable review. A reviewer
in a preset receives no automatic assignment.
Follow `~/.codex/skills/mandatory-change-review/SKILL.md` exactly, including skip
criteria. It owns reviewer model and effort, adaptive lane selection, packets,
finding reconciliation, reruns and recording.
For retained reviewers, honor the member's saved model and reasoning effort,
including reruns. Standalone fallback uses the installed default development
team's selected review-purpose role. Do not override effort on either path;
record the settings and fallback reason.

## Rule Precedence

This AGENTS.md controls workspace orchestration, tracking, worktrees, SSH remotes,
cross-project planning and compatibility expectations.

Repository-local AGENTS.md controls that repository's structure, coding style,
build/test commands, generated files, release rules, hooks, branch names, PRs,
commit formats and tooling. Do not apply it to other repositories. For content
conflicts, follow local rules while preserving workspace tracking, compatibility
and SSH-based Git remotes.

Never assume one repository's commands apply elsewhere. Use its AGENTS.md,
README, flake, Gemfile, go.mod, Makefile, Rakefile, Composer configuration and
existing CI definitions as sources of truth.

## Storage retention

Archive preserves committed Git heads and discards all uncommitted checkout
contents. Keep tracking explanations in Markdown and portal.yml; raw supporting
artifacts are untracked and disposable. Additional workspace checkouts omit
work/ and archive/; use shared tracking for initiative records. See
[storage retention](docs/operations/workspace-storage-retention.md).
