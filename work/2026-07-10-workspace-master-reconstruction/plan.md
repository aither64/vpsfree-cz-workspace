# 2026-07-10-workspace-master-reconstruction

## Goal

Restore the top-level coordination repository to a complete linear `master`
history and make the shared-checkout policy explicit: the workspace repository
itself never uses per-initiative branches or worktrees.

## Affected repositories

- vpsFree.cz top-level workspace repository only

## Approach

- Start from the current `origin/master` at `17e1b24`.
- Reapply every final, non-duplicated workspace commit stranded on local or
  remote initiative branches, preserving their original order and messages.
- Exclude superseded commit `370edad` in favor of its amended successor
  `a16294d`.
- Exclude KB commits `69da5b9`, `c323793`, and `16c1b0b`: the first two are
  patch-equivalent to commits already on master, while master contains the more
  complete final version of the third change as `fbe7b78`.
- Include the reviewed dev-session shell fix from `b2b6fdc`.
- Add instructions that keep the shared checkout on `master` and restrict
  initiative branches/worktrees to the independent project repositories.
- Reconstruct in a disposable clone so the shared checkout's existing dirty
  and untracked files remain untouched, then move the shared checkout to the
  reconstructed master and push it.

## Compatibility and deployment

- History remains linear; the reconstructed commits receive new hashes because
  they are replayed on the complete master history.
- Existing branch refs are retained as recovery references unless cleanup is
  explicitly requested. No project repository branches or worktrees change.
- The top-level policy affects only workspace coordination. It does not alter
  schemas, APIs, protocols, persisted state, deployed services, rolling update
  behavior, or rollback compatibility.
- Existing unstaged modifications must remain present as the same local diffs
  on top of reconstructed master, and existing untracked file contents must
  remain untouched.

## Testing plan

- Compare the reconstructed tree with the source branch trees and the expected
  commit inventory, accounting for the intentionally richer KB master state.
- Run `git diff --check`, Ruby syntax checks, and the full dev-session suite.
- Run relevant Nix parse/evaluation checks documented by the recovered
  devcluster commits when practical.
- Perform the mandatory standalone change review before pushing master.
- Verify the final shared checkout is on `master`, tracks `origin/master`,
  retains pre-existing dirty/untracked files, and contains the shell fix.
