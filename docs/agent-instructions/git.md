# Git and worktrees

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

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
- After the workspace feature's final rebase and review, run
  `dev-session worktree capture-comparison <slug> workspace --as-is` before
  integration. Repeat the capture after any head change.
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

The reusable workspace components are narrow exceptions to the organization
rule above. Use these exact SSH remotes:

```text
git@github.com:aither64/dev-workspace.git
git@github.com:aither64/codex-web.git
```

The organization extension repository has the same basename as the generic
runtime. Refer to it as `vpsfree-dev-workspace` in local project names,
worktrees, and session registration, while keeping its canonical remote as
`git@github.com:vpsfreecz/dev-workspace.git`.

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
- After the final rebase and commit, and before integrating each feature
  branch, save its comparison with
  `dev-session worktree capture-comparison <slug> <name> --as-is`. Repeat after
  any head change. This keeps the Repositories tab useful after integration
  even if nobody opened it before merging. For a historical recovery, supply
  both `--base <SHA>` and `--head <SHA>` from recorded integration revisions;
  never guess the pre-merge base from the current default branch.
- When merging a feature back, create a fresh temporary worktree from the target
  branch, usually the upstream default branch. Fetch the target branch first,
  rebase the feature branch onto the current target branch if needed, and merge
  only when it can fast-forward, using `git merge --ff-only <feature-branch>` or
  an equivalent fast-forward-only command. Do not create merge commits in normal
  feature integration history. Test and push from the temporary worktree, then
  remove it after the merge is complete.
- Record every affected repository, branch, and worktree path in
  `work/<yyyy-mm-dd-slug>/state.md`.
- Archive the initiative after the work is merged or abandoned, as described
  under Planning And Tracking, so its clean worktrees are removed and its
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
