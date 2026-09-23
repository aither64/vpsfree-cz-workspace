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
- Check `dev-session current` before selecting an initiative. It belongs to this
  process only if DEV_SESSION_SLUG matches. Otherwise create a separate initiative
  unless the user explicitly selects that session. Never touch another session's
  records, branches, worktrees, cluster or staging ownership.
- Keep the shared checkout on master. Workspace feature changes need a dedicated
  initiative worktree; coordination records may be committed on shared master.
  Preserve unrelated files/index changes; stage only owned paths. Never use a
  repository-wide reset, clean or stash, or switch a shared branch underneath
  another session. Keep integration fast-forward-only and retain feature refs
  unless the user explicitly requests deletion. Do not rewrite published master
  or already-merged history without the required explicit direction.
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
  and the installed catalog for new presets. The vpsFree.cz policy selects
  GPT-6 Sol for retained roles and GPT-6 Luna/low for verification watchers.
  Substantive design uses xhigh. High is allowed for a bounded simple design or
  implementation unit only with a recorded reason. Independent review uses an
  eligible retained reviewer member's saved model and effort, or the installed
  catalog's default development reviewer in a fresh standalone thread.
  Never select or fall back to Astra automatically. Sessions without a roster
  retain ordinary supported Codex resolution for lead work; mandatory review
  alone uses the installed catalog fallback. Do not invent a team or role
  lineup. Long or uncertain-duration builds, tests, workflows, CI and deployment
  waits must be launched and monitored by a fresh Luna/low utility subagent
  through `~/.codex/skills/dev-session-monitor/SKILL.md`. The watcher is not a
  team member; retain the skill's ownership, cancellation and visible-fallback
  rules. Respect instructions not to await CI.
- Use the dev-session-documentation skill for substantive work, and the
  dev-session-handoff skill after material changes/review/status requests. Keep
  tracking and the portal manifest current and include the stable session URL.
  Apply vpsfree-user-facing-writing directly to user-facing prose after technical
  facts are settled and before committing; preserve its main-agent ownership.

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

For feature, bugfix, refactor, or cross-project work with relevant code,
schema, API, protocol, configuration, documentation, deployment, or security
impact, run the `mandatory-change-review` skill after all intended changes are
committed and quick local verification has passed, but before starting long
integration tests. The canonical workflow is
`~/.codex/skills/mandatory-change-review/SKILL.md`; it owns reviewer model and effort,
adaptive lane selection, review packets, finding reconciliation, reruns, and
recording requirements. Follow it exactly, including its skip criteria.
For retained reviewers, honor the member's saved model and reasoning effort,
including on review reruns. For standalone fallback, use the installed catalog's
default development reviewer settings. Do not impose an effort override on
either path; record the selected settings and any fallback reason.

## Rule Precedence

This top-level `AGENTS.md` controls workspace orchestration, tracking,
worktrees, SSH remote policy, cross-project planning, and compatibility
expectations.

Repository-local `AGENTS.md` files control changes inside that repository:
project structure, coding style, build and test commands, generated files,
release rules, hooks, and repository-specific commit formats.

When rules conflict, follow the repository-local rule for repository content
while preserving the top-level requirements for tracking, compatibility
analysis, and SSH-based Git remotes.

Do not assume that commands from one repository apply to another. Use the local
`AGENTS.md`, README, flake, Gemfile, go.mod, Makefile, Rakefile, Composer
configuration, and existing CI definitions as the source of truth.
