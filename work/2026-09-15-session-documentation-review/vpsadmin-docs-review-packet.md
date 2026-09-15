# vpsAdmin documentation directory review

## Scope and acceptance

User: "let's unify it so what vpsadmin also uses docs/". Rename only the
top-level `doc/` tree to `docs/`, preserve all 46 document/asset contents and
modes, update live pointers and CI path consumers, and keep the existing build
and publication behavior. Earlier runtime/extension/workspace work in this
initiative is already integrated and outside this follow-up review.

Initiative: `2026-09-15-session-documentation-review`. Plan/state are alongside
this packet. Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-session-documentation-review/vpsadmin`.
Branch: `2026-09-15-session-documentation-review`.
Base: `c38839d5be62e9d40d055b23a84844e2037ba4db`.
Head: `f8fb5b3af225f20b40ad16df49d4f4ceca68fcf7`.

## Commit and ownership

One logical rename commit includes the exact file moves, two AGENTS pointers,
a README entry point and the CI skip path. These support the directory move;
there is no separate behavior change. vpsAdmin owns the documents and selector.
No runtime sources, dependencies, workflow actions, state schemas, project APIs
or other repository implementations change. Component-local generated `doc/`
paths such as the API Rakefile are separate and remain valid in their own scope.
No repository-wide documentation rewrite or directory fallback is introduced.

## Risk and lanes

Low: reversible source-directory rename with bounded reference and CI metadata
updates. No persisted/runtime/public API or deployment behavior changes. General
and architecture lanes apply because hand-maintained CI configuration changes.
Use standalone gpt-6-astra/xhigh reviewers; no nested reviewers. No new abstraction
or expanded cross-project contract triggers additional lanes.

## Documentation and compatibility

README links to `docs/`; AGENTS names `docs/` and `docs/i18n-cs.md`. Existing
README/Makefile inside the documentation tree remain byte-identical. The
Makefile derives source from its working directory and keeps the existing
published URL/deployment destination. A dry run resolves the new source path.
Unpinned browser or local references to the old repository source directory must
use `docs/`; commit-pinned historical links still work. No redirect/symlink tree
is introduced. Workspace rules/config/notes and recorded configuration/OS
default refs had no live consumer of the old vpsAdmin source path.

## Verification before review

- All 46 moved files have identical Git blob IDs and executable mode bits.
- Whole-repository reference search found only the updated AGENTS/CI pointers
  and unrelated generated doc paths, public publication URL or code identifiers.
- CI selector suite: 16 runs, 55 assertions, no failures/errors/skips.
- Ad hoc actual-path checks: moved documentation skips runtime CI; mixing it
  with a WebUI runtime change retains WebUI/auth tags; changing the rule file
  still selects the full CI suite. No bypass of that policy is introduced.
- `make -n -C docs IKIWIKI=ikiwiki` resolves the source to `docs/` and retains
  build flags/output. This was a command dry run, not a rendered wiki build.
- `git diff --check HEAD` passed before commit.
- Normal pre-commit and commit-message hooks passed in the Nix shell. Initial
  setup failures were investigated: sign inspected Overcommit config and prepare
  API's separate bundle for the API i18n hook. No hook was bypassed.
- Context owner applied the writing skill to the short README entry point;
  no existing page prose changed.

Full runtime CI is triggered by the repository's rule-file policy, even for this
rename. The previous successful default run took roughly four hours. No long
integration run for this feature has started before review.
