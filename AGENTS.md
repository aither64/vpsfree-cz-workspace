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
- `archive/`: committed plan, state, and curated durable artifacts for
  initiatives that are fully completed or explicitly abandoned.

The initiative slug must be descriptive and dated, for example
`2026-05-27-api-token-rotation`. For affected project repositories, use the
same slug for the tracking directory, feature branch, and worktree group unless
a repository-specific rule requires otherwise.

Use the NixOS-installed `dev-session start <name>` when starting a development
session in this workspace. It fixes the deployed host authority, tmux, Codex,
and portal endpoints, creates a dated slug from the short name, opens the
matching tmux session, and can add or remove worktrees under
`worktrees/<slug>/` using the canonical bare repositories in `repos/`. Use
`--as-is` when the full slug has already been chosen.

When running inside an existing development session, do not choose a new slug
until checking for the active one. Run `dev-session current` from the workspace
root. Treat the printed slug as belonging to the
current process only when the `VPSFREE_DEV_SESSION_SLUG` environment variable
is also set to that exact slug. If `current` prints a slug but the environment
variable is missing or different, assume it belongs to another concurrent
session and do not touch that session's `work/<slug>/`, `worktrees/<slug>/`,
branches, or notes. In that case, create a separate initiative unless the user
explicitly tells you to use that existing slug. Reuse `work/<slug>/` and
`worktrees/<slug>/` only for the verified current session, and record progress
in that session's `state.md`.

## Git And Worktrees

The top-level workspace repository has two distinct workflows:

- Keep the shared checkout on `master` at all times. Ordinary use of the
  workspace happens there: maintain initiative tracking under `work/`, archive
  terminal initiatives, add durable notes, and coordinate independent project
  worktrees. These coordination changes may be committed directly to `master`.
- Treat changes to the workspace itself as feature work. Changes to its rules,
  scripts, tests, documentation, skills, or other reusable behavior normally
  require a dated initiative branch and a dedicated worktree at
  `worktrees/<slug>/workspace`. Develop and rewrite those commits there before
  integrating them into `master`.
- Record the workspace feature branch and worktree in the initiative's
  `state.md`, which remains part of the shared coordination checkout. Fetch and
  rebase the workspace feature branch onto current `master` before final review.
- Integrate a reviewed workspace feature from the shared `master` checkout,
  after confirming that the feature branch is a descendant of current
  `master`. Preserve unrelated working-tree changes, stage nothing during the
  integration, and use `git merge --ff-only <feature-branch>`. Do not try to
  check out `master` in a second worktree because it is already checked out in
  the shared root. Keep the feature branch after integration unless the user
  explicitly asks for its deletion.
- Multiple sessions share the top-level `master` branch, index, and working
  tree. Before editing or committing coordination records, inspect the current
  status, preserve unrelated changes, and stage only the paths belonging to the
  current task. Never use a repository-wide reset, clean, or stash operation,
  and never switch branches out from under another session.
- Fetch `origin` before a top-level `master` commit and keep it linear. If local
  or remote `master` advanced, reconcile it without discarding shared
  working-tree changes. Do not rewrite published `master` history unless the
  user explicitly directs that exact operation.

The explicit top-level workflow above is complete for workspace changes. The
bare-repository, per-initiative worktree, and temporary target-worktree rules
below apply only to the independent project repositories.

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

For feature work in the independent project repositories:

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
- Remove worktrees after the work is merged or abandoned. Keep branches, then
  finalize the initiative as described under Planning And Tracking so its
  durable record is committed under `archive/`.
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

Treat `work/<slug>/` as active tracking and `archive/<slug>/` as terminal
tracking. New `state.md` files must begin with this exact YAML front matter:

```yaml
---
lifecycle: active
---
```

Change it to `complete` only when the requested outcome is finished, or to
`abandoned` when the initiative is explicitly closed without completion. The
anchored front matter is the only lifecycle authority; lifecycle-looking text
in the Markdown body has no effect.

Write a substantive plan and initial state, then commit both in the top-level
workspace repository before the first project-code commit or external mutation.
After that initial commit, keep plan and state current in the working tree
without committing every update. A short initiative should normally make no
further tracking-only commit until its final archive commit. If an initiative
remains unfinished at the end of an active working day, it may make at most one
consolidated tracking-only checkpoint for that day when material progress is
worth preserving. This is a ceiling, not a daily requirement. Material progress
includes changed implementation heads, durable decisions, completed phases,
new blockers, and results that change the next step.

An additional same-day tracking checkpoint is allowed only for a genuine
ownership handoff or an explicit user request. A pause until a future working
day can justify that day's consolidated checkpoint, but not a second one.
Individual plan edits, branch-head changes, review findings or remediations,
commands, test or CI results, deployment actions, and status polls do not by
themselves require commits; consolidate them into the next daily, handoff, or
final summary. Functional changes in the workspace repository and normal
commits in project repositories do not count as tracking-only checkpoints.

An initiative can leave `work/` only when its lifecycle is `complete` or
`abandoned` and it has no pending review, CI, merge, user approval, deployment
step, or cleanup owned by the session. Before archiving, remove credentials,
caches, reproducible bulk captures, and other transient outputs. Preserve
`plan.md`, `state.md`, and intentionally useful evidence. Stop shells, editors,
builds, and background processes that can still write into an initiative
worktree; the per-slug lock serializes helper commands, not external writers.
Every worktree must have an attached branch and ordinary clean `git status`.
The helper delegates removal to non-force `git worktree remove`; resolve and
retry any refusal before finalizing.
Run `dev-session finalize <slug> --as-is` to remove clean worktrees, retain
branches, and move the curated directory to `archive/<slug>/`. It keeps the
managed tmux session available so the exact
`work/<slug>/` to `archive/<slug>/` move can be inspected and committed once in
the top-level repository together with the final tracking content. Do not make
a separate tracking commit merely to set the terminal lifecycle before
finalizing; the helper requires an earlier committed active lifecycle and
accepts later tracking edits in the working tree. The helper never stages or
commits the archive move. After that commit, run
`dev-session stop <slug> --as-is` to close the managed session. The stop command
must refuse a finalized initiative whose archive move or terminal tracking
state is not committed.

Do not reuse an archived slug. Start a new dated initiative for follow-up work.
Do not delete tracking with `dev-session remove --all`; finalization and
archival are mandatory even for abandoned initiatives.

Keep these files current enough that a future agent can resume the work without
guessing. When plans change because code or tests reveal new facts, update the
tracking notes.

After material changes, review checkpoints, or user-requested status updates,
use `skills/dev-session-handoff/SKILL.md`. Keep the initiative portal manifest
current and include the stable link printed by
`dev-session url <slug> --as-is` in the handoff. If the portal has not been
deployed yet, identify it as the post-deployment URL.

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
`skills/mandatory-change-review/SKILL.md`; it owns reviewer model and effort,
adaptive lane selection, review packets, finding reconciliation, reruns, and
recording requirements. Follow it exactly, including its skip criteria.
Always use `xhigh` reasoning effort for review agents and review reruns,
regardless of a skill's default effort. Do not inherit a lower effort or select
`max` or `ultra` for review work.

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

Treat an unexpected local Linux kernel build in vpsAdminOS development or test
workflows as a bug unless the current work intentionally changes kernel sources
or configuration. vpsAdminOS kernels should normally be substituted from the
vpsAdminOS binary cache after GitHub Actions or its runners build them. When a
command starts building a kernel, stop it and investigate why the derivation
missed the cache. A local rebuild is acceptable only when the kernel or its
configuration is intentionally changed, or when the responsible runner has not
yet built and published the expected derivation; record the justification in
the initiative `state.md`.
If the work needs an additional kernel output, update the vpsAdminOS CI builder
to build and publish that output as part of the same initiative instead of
relying on recurring local builds.

When running `dev-clusters/vpsadmin/bin/devcluster`, use the bridge network by
default. Do not choose `--network local` unless the user explicitly asks for it
or the bridge network is genuinely unavailable; if local networking is used,
record the reason in the initiative state.

Use GitHub Actions as a feedback loop after pushing branches. If `gh` is not
available in the current shell, run it through Nix, for example
`nix shell nixpkgs#gh -c gh run list ...`. Inspect failed logs, monitor reruns,
and resolve failures instead of leaving CI for the user to chase.

After a force-push or a follow-up fix push, cancel superseded queued or
in-progress GitHub Actions workflow runs for the same branch. Only cancel runs
whose `headSha` no longer matches the current branch head; do not cancel
workflows for other branches or workflows already running on the current head.

When creating or editing GitHub workflows, verify the latest upstream version of
each imported action from its official repository before choosing the `uses:`
ref. Do not rely on remembered version numbers; use the newest compatible
version unless the workflow records a specific reason to pin an older one.

Rerunning a failed GitHub Actions job is not a substitute for investigation.
Before accepting a rerun as validation, download or open the failed attempt's
logs and artifacts, identify the root cause as far as the available evidence
allows, and record the finding in the initiative `state.md`. If the artifacts
are insufficient, improve the test or runner diagnostics rather than treating a
green rerun as proof that the failure did not matter. Prefer fixing the
underlying problem; when the failure is unrelated to the current change, record
the evidence for that conclusion.

When a repository is missing a tool in the ambient shell, enter the repository's
Nix shell or use an appropriate `nix shell` command. Do not work around missing
tooling by recording local environment limitations in commit messages.

When adding new integration tests that use the vpsAdminOS test-runner, write
test scripts in the current RSpec-style structure with examples and
expectations, such as `describe`, `it`, and `expect`. Do not refactor existing
tests solely to convert their style unless the user explicitly asks for that
refactor.

For `vpsfree-cz-configuration`, update flake inputs through `confctl`, not by
manually editing `flake.lock`. Use
`confctl inputs channel update --commit <channel> [role]` for normal channel
updates. Use `confctl inputs channel set --commit <channel> <role> <rev>` when
an exact unmerged feature revision has to be pinned. Keep changelogs enabled
when they are useful; skip them for noisy `nixpkgs` and `llm-agents` updates.
Keep automated `confctl ... --commit` commit messages exactly as generated;
do not amend or rewrap them to satisfy generic commit-message line length
rules. Edit them only when intentionally making a concise changelog edit.

DokuWiki user documentation is hosted at `kb.vpsfree.cz` and
`kb.vpsfree.org`. Their review instances are
`kb-cs.aitherdev.int.vpsfree.cz` and `kb-en.aitherdev.int.vpsfree.cz`. API
access to production uses one token per wiki:

When authoring or translating Czech KB pages, address the reader using
informal singular forms (`tykání`), for example `můžeš`, `potřebuješ`,
`nainstaluj`, and `použij`. Do not use formal `vy` or plural imperatives as a
polite form; use plural only when genuinely addressing multiple people.

The invisible DokuWiki `<page>` tag connects Czech and English translations.
Use the same tag value in every language variant, and always derive it from the
English KB page ID. The real DokuWiki page IDs remain language-specific.

For all user-facing prose, use the workspace skill in
`skills/vpsfree-user-facing-writing/SKILL.md`. This applies to KB pages,
vpsAdmin documentation and interface copy, user-visible errors and help, mail
templates, website copy, and member-facing release or operational messages.
The agent that owns the task context must apply the skill directly after the
technical content is settled and before committing. Do not delegate the main
rewrite to a context-poor subagent; a fresh agent may review the finished text.
Human-readable comments in bilingual scripts and configuration examples must
use the language of the surrounding page while commands and machine-significant
content remain equivalent.

Write KB pages as documentation of the current supported state. Do not
mention obsolete distributions, former defaults, superseded commands, or
historical workarounds unless readers of a still-supported installation need
that history to migrate or recover. Record removal rationale in commit
messages, DokuWiki revision summaries, or initiative notes instead of page
prose.

For vpsAdmin changes that can affect visible WebUI documentation, follow the
canonical workflow in `vpsfree-kb-contracts/docs/webui-change-workflow.md`.
Use `bin/kb-contract-fetch`, `bin/kb-contract-build`, and
`bin/kb-contract-manifest` for durable all-page candidate preparation; keep
capture generation and the documentation contract in the independent capture
repository.

Do not merge a `vpsfree-kb-contracts` feature branch merely to make managed-page
links work in staging. Managed release manifests pin the committed and pushed
feature revision, and staging resolves `<kb-managed>` links at that exact
commit. Before production promotion, integrate the contract changes into
`master`; the release tool verifies the recorded page and test files against
remote `master` before it writes production pages.

- `kb.vpsfree.cz`:
  `/home/aither/.codex/codex-kb-vpsfree-cz-aither-key`
- `kb.vpsfree.org`:
  `/home/aither/.codex/codex-kb-vpsfree-org-aither-key`

Never copy credentials into notes, commits, command output, URLs, or prompts.
Always prepare wiki changes as local candidate files first. Use `bin/kb-page`
for individual DokuWiki operations and `bin/kb-release` for a review bundle
instead of hand-crafting API calls.

The declarative `kb-staging` NixOS container on aitherdev is global and
on-demand. Its data and ownership survive `bin/kb-stage stop`; only
`bin/kb-stage reset --yes` discards staging content and mirrors the current
production pages and shared media. A development session must claim staging
with `bin/kb-stage start` before it can write. Staging ownership is serialized
by the active `VPSFREE_DEV_SESSION_SLUG`; do not manipulate another session's
staging data or ownership. `bin/kb-stage release --yes` stops the container and
releases ownership while retaining the data. It refuses a pending review
bundle unless `--discard-pending` is explicit.

Stage complete pages at their real page IDs so links and language mappings are
reviewed exactly as they will appear in production. For every new release,
prepare one bilingual `release-changes.yml` with an informative localized
summary for each page write or deletion, then generate checksummed schema-5
manifests with `bin/kb-contract-manifest --changes FILE`. Stage them with
`bin/kb-release stage --manifest FILE --yes` and verify them with
`bin/kb-release verify --manifest FILE`. The verification output must expose
each exact summary and its clickable staging revision-history URL so the user
can review revision metadata before publication. Do not use the production
`drafts:` namespace for routine review. The release tool verifies that
production still matches the recorded source revision and content before
staging or promotion.

Production writes always require direct user approval. After approval, promote
the exact staged manifest with `bin/kb-release promote --manifest FILE --yes`
and `--approved-production`. Individual production writes with `bin/kb-page`
also require `--approved-production`, including writes in `drafts:`. Read-only
production checks do not require approval. Before every write, verify
authentication and page permission against the exact target wiki.

Every production page edit must have an informative, single-line change
summary that describes the actual content change. Do not use generic summaries
such as "Publish reviewed KB release" for new edits. Write summaries for
`kb.vpsfree.cz` in Czech and summaries for `kb.vpsfree.org` in English.
Because each summary already belongs to one page, do not repeat that page's
title or subject. Describe only the resulting content changes.
Write Czech summaries as noun phrases that name the resulting changes, not as
infinitive instructions. For example, use `Doplnění síťové konfigurace a
vysvětlení správy obsahu v repozitáři`, not `Doplnit síťovou konfiguraci a
vysvětlit správu obsahu v repozitáři`. Do not rewrite existing DokuWiki
revision summaries merely to adopt this convention.

Page deletions belong in the same guarded schema-5 release manifest as page
writes. Stage and review their localized summaries and revision histories, then
promote the exact manifest after approval. Do not delete release pages with
separate `kb-page` calls. New `kb-cleanup` manifests must use schema 2 and give
every page deletion its own summary; media deletions do not have summaries.

Common KB tool examples:

```sh
bin/kb-page whoami --wiki cz
bin/kb-stage start
bin/kb-stage reset --yes
bin/kb-release stage --manifest work/example/kb-release.yml --yes
bin/kb-release verify --manifest work/example/kb-release.yml
bin/kb-page save --wiki cz information:published-page preview.txt \
  --summary "Aktualizace dokumentace" --update --approved-production
bin/kb-release promote --manifest work/example/kb-release.yml --yes \
  --approved-production
bin/kb-stage release --yes
```

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

- Wrap every commit message line at 80 characters or fewer. Generated
  `confctl ... --commit` messages in `vpsfree-cz-configuration` are the
  exception: keep them exactly as generated, even when they exceed this limit.
- Always write the commit message to a temporary file and commit with
  `git commit -F <tmpfile>`.
- Do not use `git commit -m` for final commits.
- Pre-commit hooks are mandatory, not advisory. Before the first commit in a
  repository or worktree, verify that the repository's hook framework is
  installed and active when the repository declares one, for example
  `.overcommit.yml`, `.pre-commit-config.yaml`, `lefthook.yml`, or Husky
  configuration. Install hooks with the repository-documented command, or infer
  the standard framework command when documentation is missing.
- Do not commit when expected hooks are absent, fail, or cannot be run. Fix the
  hook setup or the reported offenses first. Only continue without hooks when
  the user explicitly authorizes it for that commit, and record the reason and
  replacement checks in the initiative state.
- Running syntax checks or selected tests is not a substitute for hook-managed
  lint/format checks. If a hook framework cannot be installed but the
  equivalent command is known, run that command manually before committing and
  record that fallback in state.
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
- `security-advisories`: evidence-backed vpsFree.cz platform security
  assessments, including vpsAdmin Node evidence collection, advisory
  evaluation, and preparation of unpublished vpsAdmin drafts.
- `vpsfree-kb-contracts`: independent, reproducible Czech/English page,
  runtime-test, screenshot, and WebUI documentation contracts for an explicit
  subset of the vpsFree.cz knowledge bases. Its canonical
  `docs/webui-change-workflow.md` must be followed when a vpsAdmin feature can
  change visible labels, navigation, forms, layout, or screenshots.
- `ruby-lxc`: Ruby native extension wrapping liblxc. It is consumed by
  vpsAdminOS `osctld` and may need coordinated gem releases for Ruby or LXC
  upgrades.
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
