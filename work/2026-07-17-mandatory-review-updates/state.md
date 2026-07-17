# 2026-07-17-mandatory-review-updates

## Repositories

- Workspace repository
  - Branch: `master` (shared top-level checkout)
  - Path: `/home/aither/workspace/ai/vpsfree.cz`
  - Starting HEAD: `dd26273`
  - Upstream at start: `origin/master` at `143d7c6`

## Status

Implementation complete and quick verification passed. The active development
session is verified by matching `bin/dev-session current` and
`VPSFREE_DEV_SESSION_SLUG` values. The change is ready to commit and review.

## Commands run

- `bin/dev-session current`
- Inspected the skill-creator guidance and the existing mandatory review skill.
- Inspected vpsAdmin API resource declarations and ActiveRecord migration
  patterns from `repos/vpsadmin.git`.
- Attempted to execute the skill validator directly.
- Attempted to invoke the validator with ambient Python and with PyYAML added as
  a separate `nix shell` package.
- Ran the validator with a Nix-built Python environment containing PyYAML.
- Ran `git diff --check` and inspected all four new review checks and their
  exception cases.
- Checked the workspace root for declared hook frameworks and active Git hooks.
- Fetched `origin` and checked the shared `master` ancestry.

## Results

- The current skill already checks feature-branch history and deployed-version
  compatibility, but does not distinguish abandoned branch-only formats.
- vpsAdmin convention uses HaveAPI `resource` declarations for live
  associations, separate files for top-level resources, and parent files for
  nested resources.
- Direct validator execution failed with `Permission denied` because
  `quick_validate.py` is not executable.
- Ambient Python lacks PyYAML, and adding the Python package separately with
  `nix shell` does not add it to the interpreter's module path.
- A Python environment built with `python3.withPackages` validated the skill
  successfully.
- The skill explicitly covers superseded never-merged branch formats, HaveAPI
  associations with historical/deleted-resource exceptions, top-level and
  nested resource file placement, and `change`/`reversible` migrations with
  justified `up`/`down` exceptions.
- `git diff --check` passed.
- The workspace repository declares no hook framework and has only Git's sample
  hook files, so no hook installation is required for this commit.
- After fetching, local `master` is three commits ahead of `origin/master` and
  is not behind, so no reconciliation is required before committing.
- The shared checkout contains unrelated modified and untracked files. They
  must remain untouched and unstaged.

## Open questions

None.

## Cleanup

- No independent repository worktrees were created.
- Keep the initiative tracking files after completion.
