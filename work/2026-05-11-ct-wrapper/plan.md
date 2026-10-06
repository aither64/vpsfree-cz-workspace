# 2026-05-11 ct wrapper

## Goal

Prepare the `vpsadminos` branch `2026-05-11-ct-wrapper` in this workspace,
rebase it onto current upstream `staging`, and determine whether the osctl gem
package update commit has to be regenerated after the rebase.

## Affected repositories

- `vpsadminos`

## Worktrees and branches

- Repository: `repos/vpsadminos.git`
- Feature branch: `2026-05-11-ct-wrapper`
- Worktree: `worktrees/2026-05-11-ct-wrapper/vpsadminos`
- Base branch: `staging`

## Approach

1. Fetch upstream `staging` and `2026-05-11-ct-wrapper` into
   `repos/vpsadminos.git`.
2. Create a dedicated feature worktree from the fetched branch.
3. Rebase the feature branch on top of current upstream `staging`.
4. Inspect the rebased history for generated osctl gem packaging commits.
5. If `staging` already contains a newer gem update commit, replace the
   feature branch's generated gem update commit instead of stacking stale
   generated package metadata.

## Compatibility and deployment notes

The feature rewrites the pty wrapper from Ruby to Rust. The rebase itself should
not change the intended runtime behavior, but the final branch still needs the
normal compatibility review for vpsAdminOS deployment:

- Rust and Ruby wrapper packaging must preserve the same CLI/API contract for
  callers in osctl/osctld.
- Generated gem package metadata must match the rebased source tree so Nix
  builds and integration tests use the new code.
- Mixed-version deployment risk is expected to be limited to hosts running the
  old or new wrapper package; no database schema or persisted format change is
  expected from the rebase alone.
- Rollback should continue to work if the wrapper interface is unchanged and no
  persisted state is written in a new format.

## Testing plan

- Inspect rebase result and generated package commits.
- Run focused packaging/build checks if gem metadata is regenerated.
- Run relevant osctl/osctld or wrapper tests if available and practical in the
  repository's Nix development environment.

## Decisions

- Use the upstream-pushed feature branch as source because the older checkout's
  local and `origin/2026-05-11-ct-wrapper` refs match.
- Drop the old feature gem update commit during rebase and regenerate package
  metadata on top of current `staging`, because `staging` already contains
  `os: update gems to 25.11.0.build20260531170948`.
- Merge into `staging` by fast-forward only from a temporary staging worktree.
- Push `staging` only. Keep branch refs, but do not force-push or delete the
  remote feature branch.
