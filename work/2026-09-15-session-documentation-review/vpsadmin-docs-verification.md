# vpsAdmin documentation directory verification

## Scope and revision

User-requested rename of the top-level documentation directory to match the
other projects. vpsAdmin base: `c38839d5be62e9d40d055b23a84844e2037ba4db`.
Feature head: `f8fb5b3af225f20b40ad16df49d4f4ceca68fcf7`.
Branch: `2026-09-15-session-documentation-review`.

The change moves all 46 tracked files, including hidden metadata, release
scripts and assets. Git reports every move at 100% similarity. Independent
`git hash-object` comparisons against the old `doc/` tree confirm identical
blobs and executable bits. The old top-level directory is absent.

## References and build behavior

- README now links `docs/`; AGENTS uses `docs/` and `docs/i18n-cs.md`.
- `tests/ci-selection.yml` recognizes `docs/**` as documentation.
- Whole-tree searches found no other consumer of the top-level source path.
  API Rakefile and component .gitignore `doc/` entries refer to separate
  component-local generated documentation. The public `vpsadmin-doc` URL and
  publishing destination are unchanged.
- Recorded configuration and vpsAdminOS default refs, plus workspace rules,
  scripts, configuration and notes, had no matching live reference to the
  old vpsAdmin source directory. Historical commit-pinned links remain valid.
- `make -n -C docs IKIWIKI=ikiwiki` resolves the build source to the new directory
  and retains the existing flags and `html/` output. This validates command
  expansion only; no wiki render or publication was performed.

## Focused checks

Commands used the repository's pinned Nix tools:

- `ruby tests/ci-selection-test.rb`: 16 runs, 55 assertions; no failures,
  errors or skips.
- Selector checks against the actual staged changed paths: documentation-only
  paths skip runtime tests; adding a WebUI runtime path retains its auth/WebUI
  selection; including the changed rule file retains the full-suite policy.
- `git diff --check HEAD` passed before commit.
- Normal pre-commit hooks passed: Nixfmt, MigrationSpecs, API/WebUI i18n,
  and RuboCop. All commit-message hooks passed.
- Context owner applied the user-facing writing skill to the short new README
  pointer. Existing documentation prose is byte-identical.

## Investigated setup failures

The post-checkout hook refused a changed Overcommit signature after Git had
created the worktree. Inspected `.overcommit.yml` and all four local hook files,
then ran `nix develop --command overcommit --sign`. The subsequent session sync
succeeded. See `notes/cross-project/2026-06-03-worktree-hook-exit.md`.

The first commit attempt failed only in the API i18n hook because the separate
API bundle was missing ActiveRecord. Ran `nix develop .#api --command true`,
then retried the normal commit from the root Nix shell. All hooks passed.
See `notes/vpsadmin/2026-08-22-overcommit-api-bundle.md`. No hook was bypassed.

## Integration CI policy

Changing `tests/ci-selection.yml` matches its `full` rule. The push workflow
includes `tests/**`, so this otherwise mechanical rename selects the full
`tag=ci` runtime suite. That policy has not been weakened or bypassed. The last
successful default run (34889745709) took about four hours. Mandatory review
precedes starting this feature's long integration run.

## Mandatory review

General and architecture reviews completed at gpt-6-astra/xhigh with no
findings. Both inspected the exact committed head `f8fb5b3af`; no remediation
or rerun was necessary. The general reviewer independently repeated the
selector tests and verified the complete rename mapping.

## User-directed integration decision

After the committed rename passed hooks, focused checks and both reviews, the
user instructed "no waiting for CI". Integration therefore proceeds without
waiting for the full suite. Existing CI runs remain enabled; they have not been
reported as passed or cancelled. The change leaves normal CI rules intact.

## Integration and cleanup

`f8fb5b3af225f20b40ad16df49d4f4ceca68fcf7` was fast-forwarded to remote master
from a fresh temporary target worktree. Its 16 selector tests / 55 assertions
passed before push. Final fetched default/feature refs prove the exact local
and remote feature head merged into master. Both temporary and registered
feature worktrees were removed without force; branch refs and portal comparison
remain. No application deployment was necessary.

Feature CI: https://github.com/vpsfreecz/vpsadmin/actions/runs/34960028140
It was queued at the last inspection. The user explicitly waived waiting for CI;
no subsequent result is inferred and no run was cancelled.
