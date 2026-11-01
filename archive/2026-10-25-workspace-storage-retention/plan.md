# Workspace storage retention

Implement the user-approved plan from this conversation. Repositories:
`dev-workspace`, `workspace`, `vpsfree-cz-configuration`; feature branch and
worktree group `2026-10-25-workspace-storage-retention`.

## Accepted decisions

- Explicit archive keeps committed Git heads/branches and removes all checkout
  contents, including staged, unstaged, untracked and ignored files. Revival
  recreates committed heads only. Automatic archive eligibility stays intact.
- Tracking archives retain Markdown and portal.yml only; discard raw artifacts.
  Existing records can be cleaned with a simple script, without rewriting Git
  history or adding external artifact storage.
- Exclude work/archive tracking from workspace feature/source/scratch checkouts
  and Nix package sources. Preserve the shared workspace checkout.
- New unused coordinator preparations/orphans expire after 24 hours. Add explicit
  legacy expiration, independent collection past busy integrations, optional
  size reporting and preservation reasons. Keep all live/recovery dependencies.
- Compact completed old recovery payloads only after saving committed-head
  metadata; never alter unfinished operations or active session worktrees.

## Compatibility and rollout

New committed-only inventory schema 3/archiveRecoveryPolicy 3; retain readers
and exact policy for predecessor archive/revive journals. No database migration
or history rewrite. Do not delete Nix store paths manually. Runtime and matching
host input deploy from feature branches; no default-branch integration authorized.
User explicitly authorizes aitherdev deployment using vpsfree-cz-configuration.

## Verification and documentation

Quick checks before independent final review; packaged/native checks and host
build/dry activation afterward. Use disposable runtime state, current repository
Nix tools, fresh catalog watcher for long work, and preserve existing host service.
Exercise dirty/conflicted/ignored/detached/nested archives, retry/legacy/mixed
versions, summary filtering, 24h expiry, explicit expiration, live dependencies,
busy integrations and sparse/Nix source identity. Measure allocated space before
and after. Owning runtime docs describe behavior/recovery; workspace procedures
and host operations docs describe site rollout. Session state owns exact heads,
review/test evidence and deployment receipts.
