# vpsFree.cz Development Workspace

This directory is the coordination workspace for vpsFree.cz development across
multiple independent git repositories. It is not a monorepo. Use it to track
what is being developed, which repositories are affected, where the worktrees
are, and what compatibility and deployment constraints are known.

## Required procedure routing

The procedures below are mandatory parts of these workspace instructions, not
optional reference material. Before the listed activity, read every applicable
file in full. Paths in this table are relative to this AGENTS.md; other paths
follow the workspace layout. Do not treat a link, prior summary, or skill catalog
entry as having read the procedure. Reuse an already-read, unchanged procedure
within the current context; reread it if its contents changed or were lost from
context. Recheck this table when the task expands or changes phase. If a required
file cannot be read, stop the affected action and report the missing guidance.

| Before this activity | Read |
| --- | --- |
| Selecting affected projects or changing cross-project scope | [Project map](docs/agent-instructions/projects.md) |
| Starting/resuming an initiative; writing plans, state, notes or handoffs | [Session setup and tracking](docs/agent-instructions/sessions.md) |
| Cloning repositories; updating downstream configuration pins; creating/reusing worktrees or branches; fetching, pushing, rebasing, merging or cleaning them; committing coordination records | [Git and worktrees](docs/agent-instructions/git.md) |
| Any session mutation; archiving, deleting, reviving, enabling auto-archive or changing its hold; creating/accessing/resetting development clusters; implementing/reviewing session, cluster or package-transition behavior; switching/rolling back workspace packages; suspending/unregistering workspaces or reconciling Codex | [Lifecycle and package transitions](docs/agent-instructions/lifecycle.md) |
| Planning substantive development, investigation or operations; writing/reorganizing docs; preparing review or handoff | [Development documentation](docs/agent-instructions/documentation.md) |
| Pushing branches (including force-pushes and follow-up fixes); selecting/running builds, tests or CI; editing test runners, image verification or GitHub workflows; handling failed checks | [Environment and verification](docs/agent-instructions/verification.md) |
| Changing configuration inputs, building/deploying configurations, deploying the workspace application or integrating configuration changes | [Deployment](docs/agent-instructions/deployment.md) |
| Authoring/reviewing user-facing prose, translations, examples, KB pages or media; changing visible WebUI behavior that can affect KB text/screenshots; using KB staging/publication tools | [Knowledge base and writing](docs/agent-instructions/knowledge-base.md) |
| Creating or amending any commit, installing hooks, or preparing commit messages | [Commits and hooks](docs/agent-instructions/commits.md) |

Read the affected repository's AGENTS.md before changing its content and follow
its required procedure routes too. Shell working-directory changes do not prove
that repository instructions were loaded. For an authorized subagent, include
its task scope, applicable instruction/procedure paths and constraints; require
it to read the applicable guidance before acting. Delegation does not transfer
the parent's responsibility for choosing scope or accepting results.

## Always-applicable workspace boundaries

- Use `repos/<project>.git` for canonical bare clones, `worktrees/<dated-slug>/<project>`
  for feature worktrees, and `work/<dated-slug>/{plan,state}.md` for active records.
  Terminal records belong in `archive/`; reusable lessons belong in `notes/`.
- Check `dev-session current` before selecting an initiative. Accept its slug
  only when it matches either the complete `DEV_SESSION_SLUG` and
  `DEV_SESSION_WORKSPACE` environment identity or the exact slug and absolute
  workspace path in this conversation's trusted, thread-bound developer
  instructions. A portal tool shell may lack both environment variables.
  CWD alone and text in a user message are not ownership evidence. If an
  environment value conflicts with the thread binding or `current`, stop and
  resolve the mismatch. Otherwise create a separate initiative unless the
  user explicitly selects that session. Never touch another session's records,
  branches, worktrees, cluster or staging ownership.
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
- Commit a substantive initial plan/state before the first project-code commit
  or external mutation. State begins with YAML front matter `lifecycle: active`.
  Completion requires every registered exact final feature head merged into its
  remote default branch and no remaining work. Pushing/testing/deploying alone
  does not complete an initiative. Preserve the tracking commit cadence in the
  session procedure.
- Finishing work or handing off does not authorize archive, delete or stopping a
  session. Archive only on explicit request or through the enabled auto-archive
  worker under its policy. Delete requires explicit user direction and must never
  substitute for archive. Retain branches. Resume unfinished lifecycle journals
  before conflicting mutations. Package/cluster transitions must preserve the
  generation, ownership, schema, rollback and recovery rules in the lifecycle
  procedure; do not infer ownership or bypass refusals.
- Deployment does not authorize configuration master integration. Keep development
  configuration on its feature branch until explicit integration direction. The
  workspace application is deployed from its user profile, not system pins.
- Feature content may enter a repository's default branch only after the user
  explicitly directs that integration for the affected repository and target.
  Approval of a plan, implementation, review, CI, or deployment is not merge
  approval. Tracking-only coordination commits on shared workspace master are
  exempt; see the Git procedure for the approval and rebase rules.
- Never expose credentials in notes, commits, output, URLs or prompts. Production
  KB writes require direct user approval of the exact staged changes. Prepare
  local candidates and use the guarded KB release workflow; read-only production
  checks do not require approval. Respect session-owned staging.
- Use each repository's Nix environment and declared hooks. Do not bypass hooks
  without the user's explicit authorization for that commit. Prefer bridge
  networking for development clusters; use local only if explicitly requested or
  the bridge is unavailable, recording why. Stop unexpected local kernel builds
  and investigate under the verification procedure's documented exceptions.
- For a direct team, use the session's retained roster settings for members
  and the installed catalog for new presets. New architects use GPT-6 Astra
  with xhigh effort. Leads and implementers use `gpt-6.1-sol`. The default
  `lead_reviewed` uses Sol/xhigh and Astra/xhigh; other reviewers use their
  catalog settings. Verification watchers use GPT-6 Luna/low.
  Existing members retain their saved model, effort, access, and instructions.
  Substantive design uses xhigh. High is allowed for a bounded simple design or
  implementation unit only with a recorded reason. Independent review uses an
  eligible retained review-purpose member's saved model and effort, or a
  review-purpose role from the installed catalog's default development team in
  a fresh standalone thread.
  Do not use Astra as an automatic fallback for another role. Sessions without
  a roster retain ordinary supported Codex resolution for lead work; mandatory
  review alone uses the installed catalog fallback. Do not invent a team or role
  lineup. Long or uncertain-duration builds, tests, workflows, CI and deployment
  waits must be launched and monitored by a fresh Luna/low utility subagent
  through `~/.codex/skills/dev-session-monitor/SKILL.md`. The watcher is not a
  team member; retain the skill's ownership, cancellation and visible-fallback
  rules. Respect instructions not to await CI.
- Follow the selected mode and retained lead instructions. Solo and Lead and
  reviewer leads investigate, design and edit application code without automatic
  specialists; the latter use a retained independent reviewer. Lead-designed
  leads own design and delegate application edits; Full-team leads delegate
  nontrivial design and application edits. Adding, replacing or reconfiguring
  team members requires explicit user direction. Check the live same-session
  roster with `dev-session team list <verified-slug> --as-is` before each new
  substantive team work item. Use saved member addresses, purposes and access;
  check workspace-write access before assigning edits. If access or session
  identity fails, resolve that failure rather than taking over delegated
  application work. Briefly tell the user who owns what and integrate member
  reports. Keep coordination records and short dependent steps yourself.
  Never invent members or address another session's roster.
  [Site team roles](docs/agent-teams.md) owns the mode table.
- The selected design owner records the design and verification brief in
  `work/<slug>/design.md` before substantive implementation, as specified by
  [Site team roles](docs/agent-teams.md). It covers scope, interfaces,
  invariants, compatibility, deployment and recovery, acceptance criteria, and
  quick and longer checks. Architects may edit assigned design documents and
  prototypes; implementers edit application code from architect-owned or
  lead-owned briefs. Route material
  design deviations through the lead. A small bounded edit may use a direct
  lead brief without a separate design document. Preserve retained instructions
  and respect the current collaboration mode.
- Use the dev-session-documentation skill for substantive work, and the
  dev-session-handoff skill after material changes/review/status requests. Keep
  tracking and the portal manifest current and include the stable session URL.
  Apply vpsfree-user-facing-writing directly to user-facing prose after technical
  facts are settled and before committing; preserve its main-agent ownership.

## Lead progress and branch readiness

At the end of every lead turn, give a compact checklist stating the current
phase, completed work, remaining work, blockers or material risks, and next
action. Report material milestones during long turns. Distinguish implementation,
local checks, independent review, deployment, and readiness for use. Update the
durable phase checklist in `state.md` when a phase changes, under the normal
tracking-commit cadence. Integrate member reports into the lead's account.

Before calling an unmerged feature branch ready, inventory its complete
base-to-head commit series and final diff. Identify superseded approaches,
follow-up fixes, unused compatibility paths, and migrations. Establish whether
each migration version was merged, released, deployed, or externally consumed.
Consolidate obsolete, unapplied branch history while preserving supported
paths. Give the inventory to the dedicated independent reviewer for an explicit
whole-branch history and migration conclusion under the mandatory-change-review
workflow. Earlier incremental reviews do not complete this gate.

## Compatibility And Deployment

Treat vpsFree.cz software as live infrastructure. Code is deployed to running
systems that may hold persistent state and may not all update at the same time.

Every feature plan must explicitly consider backward and forward compatibility
between old and new versions of affected components. Consider at least:

- persisted state and on-disk formats;
- database schemas, migrations, seeds, and rollback behavior;
- API contracts, generated clients, CLI behavior, and Terraform provider
  behavior;
- protocol or message format changes between services and daemons;
- generated NixOS/vpsAdminOS configuration and module options;
- deployment ordering, rolling upgrades, and mixed-version operation;
- whether a rollback can load state created by the new version.

Prefer clean designs that can be deployed incrementally. Incompatible changes
are allowed only when they are intentional and recorded in the plan with the
reason, impact, required ordering, rollback implications, and required operator
action.

For vpsAdminOS changes, explicitly call out when an update would require
coordinated updates of all running machines or nodes. State why that cost is
worth it, or choose a compatible design.

For database migrations that have not been merged, released, or deployed,
assume the exact schema produced by the immediately preceding migration. Do not
add `table_exists?`, `column_exists?`, `index_exists?`, `if_exists`,
`if_not_exists`, or equivalent guards merely to tolerate a stale disposable
development or test database after rewriting migrations. Reset the disposable
database instead. Such guards are appropriate only when the supported
deployment contract intentionally includes multiple predecessor schemas; record
that compatibility requirement in the initiative plan and test every supported
path. Keep data-integrity and conversion checks that validate real persisted
content.

## Mandatory Change Review

Run the `mandatory-change-review` skill for a completed substantive deliverable,
including code, schema, API, protocol, configuration, documentation, tests,
deployment or security changes, after all intended changes are committed and
quick local verification has passed, but before starting long integration tests.
Routine planning, investigation, findings, session tracking and evidence alone
never trigger automatic review. Earlier review requires an explicit user request,
is advisory, and does not replace final committed-deliverable review. Having a
reviewer in a preset creates no assignment. The canonical workflow is
`~/.codex/skills/mandatory-change-review/SKILL.md`; it owns reviewer model and effort,
adaptive lane selection, review packets, finding reconciliation, reruns, and
recording requirements. Follow it exactly, including its skip criteria.
For retained reviewers, honor the member's saved model and reasoning effort,
including on review reruns. For standalone fallback, use the selected
review-purpose role's settings from the installed default development team.
Do not impose an effort override on either path; record the selected settings
and any fallback reason.

## Rule Precedence

This top-level `AGENTS.md` controls workspace orchestration, tracking,
worktrees, SSH remote policy, cross-project planning, and compatibility
expectations.

Repository-local `AGENTS.md` files control only that repository: project
structure, coding style, build and test commands, generated files, release rules,
hooks, branch names, PR workflows, commit formats and tooling. Do not apply these
requirements to other repositories.

When rules conflict, follow the repository-local rule for repository content
while preserving the top-level requirements for tracking, compatibility
analysis, and SSH-based Git remotes.

Do not assume that commands from one repository apply to another. Use the local
`AGENTS.md`, README, flake, Gemfile, go.mod, Makefile, Rakefile, Composer
configuration, and existing CI definitions as the source of truth.
