# Importing configuration branches older than Overcommit

When importing a historical branch into the canonical bare repository, existing
shared hooks also run for its new worktree. A branch predating `.overcommit.yml`
can fail in `post-checkout` with `Errno::ENOENT` after Git has created the branch
and worktree. The native `dev-session worktree add` may already have registered
the worktree and its true initial base before reporting the hook error. A direct
rebase from that checkout can fail in `pre-rebase` for the same missing file.

Inspect actual refs, worktree HEAD/status and session registration before retrying.
Preserve an exact original import ref. Prepare the fetched current configuration
and its Nix development shell, then replay the historical feature with the normal
declared hooks. A checkout hook can also report missing gems after changing HEAD;
the current repository's `nix develop` supplies its locked bundle. Do not disable
hooks or assume a reported checkout failure rolled back Git effects.

Recovery and verification: [mx2 import evidence](../../work/2026-11-01-mx2-nixos-migration/import-rebase.md).
