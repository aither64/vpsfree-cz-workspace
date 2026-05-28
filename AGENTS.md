# vpsFree.cz Development Workspace

This directory is the coordination workspace for vpsFree.cz development across
multiple independent git repositories. It is not a monorepo. Use it to track
what is being developed, which repositories are affected, where the worktrees
are, and what compatibility and deployment constraints are known.

## Workspace Layout

Use these paths consistently:

- `repos/<project>.git`: canonical bare clone of an upstream repository.
- `worktrees/<yyyy-mm-dd-slug>/<project>`: per-initiative feature worktree.
- `work/<yyyy-mm-dd-slug>/plan.md`: durable plan, affected repositories,
  compatibility notes, and decisions.
- `work/<yyyy-mm-dd-slug>/state.md`: current status, branch names, commands
  run, test results, open questions, and cleanup notes.
- `notes/`: durable development notes, troubleshooting tips, and reusable
  lessons that should survive beyond one initiative. Store each lesson in its
  own file to reduce conflicts between concurrent Codex instances.
- `archive/`: optional location for completed initiative notes after worktrees
  have been removed.

The initiative slug must be descriptive and dated, for example
`2026-05-27-api-token-rotation`. Use the same slug for the tracking directory,
feature branch, and worktree group unless a repository-specific rule requires
otherwise.

## Git And Worktrees

Clone and push repositories over SSH. Use remotes in this form:

```text
git@github.com:vpsfreecz/<project>.git
```

Do not use HTTPS remotes for normal development pushes. If an existing checkout
uses HTTPS, switch `origin` to the SSH URL before pushing. GitHub tokens may be
used for API access, metadata, pull requests, and CI checks, but must not be
embedded in remotes, committed to files, or recorded in work notes.

Multiple Codex instances may work in this workspace at the same time. Keep
`repos/<project>.git` bare, and do not reuse another initiative's branch or
worktree. Use feature branches and separate worktrees so concurrent work does
not conflict over checked-out branches, index state, or uncommitted changes.

For feature work:

- Keep `repos/<project>.git` as the canonical bare clone for fetching,
  inspecting refs, and creating worktrees.
- Before pushing or updating downstream configuration pins, fetch upstream
  and rebase feature branches when appropriate. Several repositories use
  scheduled GitHub workflows to update dependencies, inputs, or generated
  metadata, so default branches may advance while feature work is in progress.
- Create feature branches named `<yyyy>-<mm>-<dd>-<slug>`, for example
  `2026-05-27-api-token-rotation`, unless a repository-local rule requires a
  different name.
- Create worktrees under `worktrees/<yyyy-mm-dd-slug>/<project>` so all changes
  for one initiative are easy to inspect together.
- When merging a feature back, create a fresh temporary worktree from the target
  branch, usually the upstream default branch. Fetch the target branch first,
  rebase the feature branch onto the current target branch if needed, and merge
  only when it can fast-forward, using `git merge --ff-only <feature-branch>` or
  an equivalent fast-forward-only command. Do not create merge commits in normal
  feature integration history. Test and push from the temporary worktree, then
  remove it after the merge is complete.
- Record every affected repository, branch, and worktree path in
  `work/<yyyy-mm-dd-slug>/state.md`.
- Remove worktrees after the work is merged or abandoned. Preserve the plan and
  state notes, moving them to `archive/` if useful.
- Keep feature branches after merge, both locally and remotely, unless the user
  explicitly asks for branch deletion. Cleanup means removing worktrees and
  transient build/cache files, not deleting branch refs.

Feature branch history may be rewritten while the branch is under development
and has not been merged into the main branch. Use this to keep functional
commits, generated updates, and follow-up fixes reviewable. Do not rewrite
history that has already been merged.

Before changing code in a repository, read its local `AGENTS.md` if present.
When a repository has no `AGENTS.md`, infer commands and style from its
existing files, history, and manifests.

## Planning And Tracking

Start each requested feature or fix by identifying the affected projects. Some
features span multiple repositories; plan the cross-repository shape before
editing any one component.

For each initiative, maintain:

- `plan.md`: the goal, affected components, approach, compatibility analysis,
  deployment ordering, testing plan, and explicit decisions.
- `state.md`: branch/worktree locations, current progress, commands run,
  results, blockers, and cleanup status.

Keep these files current enough that a future agent can resume the work without
guessing. When plans change because code or tests reveal new facts, update the
tracking notes.

Promote reusable lessons to `notes/`. In particular, write a note when a
command, shell, test, build, deploy, hook, or worktree operation fails in a
non-obvious way; when a workaround saves future time; when a repository has
undocumented setup or ordering requirements; or when an investigation finds a
dead end worth avoiding later.

Keep `state.md` detailed for the current initiative and keep durable notes
concise for future reuse. Store each lesson in a separate file, using
`notes/cross-project/<yyyy-mm-dd-short-topic>.md` for cross-project notes and
`notes/<project>/<yyyy-mm-dd-short-topic>.md` for repository-specific notes.
Record the command or workflow, symptom, cause if known, fix or workaround,
verification result, and related initiative path. Summarize long logs instead
of pasting them. Redact secrets and avoid recording temporary local paths unless
the path itself matters.

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

## Development Environment

Development is generally Nix-based. Prefer each repository's `nix develop`,
`nix-shell`, flake outputs, or documented development shell before running
language-specific tools. Deployment is usually to NixOS or vpsAdminOS systems,
often through `confctl` and the configuration repositories.

Use GitHub Actions as a feedback loop after pushing branches. If `gh` is not
available in the current shell, run it through Nix, for example
`nix shell nixpkgs#gh -c gh run list ...`. Inspect failed logs, monitor reruns,
and resolve failures instead of leaving CI for the user to chase.

When a repository is missing a tool in the ambient shell, enter the repository's
Nix shell or use an appropriate `nix shell` command. Do not work around missing
tooling by recording local environment limitations in commit messages.

For `vpsfree-cz-configuration`, update flake inputs through `confctl`, not by
manually editing `flake.lock`. Use
`confctl inputs channel update --commit <channel> [role]` for normal channel
updates. Use `confctl inputs channel set --commit <channel> <role> <rev>` when
an exact unmerged feature revision has to be pinned. Keep changelogs enabled
when they are useful; skip them for noisy `nixpkgs` and `llm-agents` updates.

When changing Ruby code that is packaged for Nix as gems, rebuild the packaged
gems so integration tests and future deployments use the new code. This applies
to tools such as vpsAdminOS `osctl` components and vpsAdmin `nodectl`
programs. In vpsAdminOS, see `make gems` and `make commit-gems`. In vpsAdmin,
use `rake vpsadmin:gems`.

Commit gem rebuilds separately from functional changes. Gem rebuild commits use
only a subject line, following the repository's generated-gem commit style. One
gem rebuild commit per feature branch is enough; amend or recreate it as needed
while the feature branch is still unmerged.

Do not assume that commands from one repository apply to another. Use the local
`AGENTS.md`, README, flake, Gemfile, go.mod, Makefile, Rakefile, Composer
configuration, and existing CI definitions as the source of truth.

## Commits

Write informative commits. A commit message must explain what is changing and
why it is needed. The subject should summarize the change; the body should
explain the problem, rationale, and deployment or compatibility notes when that
context matters. Do not add command transcripts, "Checks:", "Tests:",
"Syntax checks:", "Validated with:", or local tool availability notes to commit
messages; record validation in `state.md` or PR notes instead.

Rules:

- Wrap every commit message line at 80 characters or fewer.
- Always write the commit message to a temporary file and commit with
  `git commit -F <tmpfile>`.
- Do not use `git commit -m` for final commits.
- Do not bypass git hooks unless the user explicitly authorizes it and the
  reason is recorded in the initiative state.
- Keep commits focused. Split generated updates, dependency bumps, release
  metadata, and functional changes when repository rules or review clarity call
  for it.
- Respect each repository's local commit subject style and special release or
  generated-file rules.

## Project Map

These repositories are in scope for this workspace:

- `vpsadminos`: NixOS, ZFS, and LXC-based host OS for containers. It is the
  core runtime for vpsFree.cz nodes and many integration tests.
- `vpsadmin`: Ruby/PHP control panel and API for managing VPSes on top of
  vpsAdminOS.
- `haveapi`: framework for self-describing APIs. It underpins vpsAdmin's API
  shape and client generation.
- `vpsf-status`: Go status page and monitoring-facing status service for
  vpsFree.cz.
- `vpsadmin-go-client`: generated Go client library for the vpsAdmin API.
- `confctl`: Ruby/Nix deployment management tool used with NixOS and
  vpsAdminOS fleets.
- `vpsfree-cz-configuration`: production vpsFree.cz cluster configuration in
  Nix.
- `vpsadminos-org-configuration`: vpsadminos.org cluster configuration in Nix.
- `vpsfree-irc-bot`: IRC bot for vpsFree.cz channels and infrastructure
  integration.
- `vpsfree-mail-templates`: localized mail templates consumed by vpsAdmin.
- `terraform-provider-vpsadmin`: Go Terraform/OpenTofu provider for vpsAdmin.
- `web`: PHP and server-side-include website for vpsFree.cz and its
  translations.
- `ssh-exporter`: Prometheus exporter that checks systems over SSH and exports
  metrics.
- `syslog-exporter`: Prometheus exporter that parses syslog streams into
  metrics.
- `vpsfree-client`: Ruby CLI and client library for the vpsFree.cz API, built
  on vpsAdmin and HaveAPI clients.
- `vpsfree-maintenance-tasks`: dated operational scripts for maintenance work.
- `linux`: Linux kernel tree used by vpsAdminOS. Treat it as reference material
  unless the task explicitly targets kernel work.
- `zfs`: OpenZFS tree used by vpsAdminOS. Treat it as reference material unless
  the task explicitly targets ZFS work.

Common dependency flow: HaveAPI defines the API framework and client-generation
model. vpsAdmin consumes HaveAPI and manages infrastructure running on
vpsAdminOS. The Go client, Ruby client, and Terraform provider consume the
vpsAdmin API. The configuration repositories deploy NixOS and vpsAdminOS
systems, usually with confctl. Status, exporters, web, IRC bot, mail templates,
and maintenance tasks support operations around the core platform.
