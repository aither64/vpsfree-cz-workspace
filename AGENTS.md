# vpsFree.cz Development Workspace

This directory is the coordination workspace for vpsFree.cz development across
multiple independent git repositories. It is not a monorepo. Use it to track
what is being developed, which repositories are affected, where the worktrees
are, and what compatibility and deployment constraints are known.

## Workspace Layout

Use these paths consistently:

- `repos/<project>`: canonical local checkout of an upstream repository.
- `worktrees/<yyyy-mm-dd-slug>/<project>`: per-initiative feature worktree.
- `work/<yyyy-mm-dd-slug>/plan.md`: durable plan, affected repositories,
  compatibility notes, and decisions.
- `work/<yyyy-mm-dd-slug>/state.md`: current status, branch names, commands
  run, test results, open questions, and cleanup notes.
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

For feature work:

- Keep `repos/<project>` as the canonical checkout for fetching, inspecting,
  and creating worktrees.
- Create feature branches named `<yyyy>-<mm>-<dd>-<slug>`, for example
  `2026-05-27-api-token-rotation`, unless a repository-local rule requires a
  different name.
- Create worktrees under `worktrees/<yyyy-mm-dd-slug>/<project>` so all changes
  for one initiative are easy to inspect together.
- Record every affected repository, branch, and worktree path in
  `work/<yyyy-mm-dd-slug>/state.md`.
- Remove worktrees after the work is merged or abandoned. Preserve the plan and
  state notes, moving them to `archive/` if useful.

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

Do not assume that commands from one repository apply to another. Use the local
`AGENTS.md`, README, flake, Gemfile, go.mod, Makefile, Rakefile, Composer
configuration, and existing CI definitions as the source of truth.

## Commits

Write informative commits. A commit message must explain what is changing and
why it is needed. The subject should summarize the change; the body should
explain the problem, rationale, deployment or compatibility notes, and test
evidence when that context matters.

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
