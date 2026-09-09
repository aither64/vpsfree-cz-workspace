---
lifecycle: active
---

# 2026-09-09-guix-test-fix

## Repositories

- vpsfree-kb-contracts: planned branch 2026-09-09-guix-test-fix, worktree
  worktrees/2026-09-09-guix-test-fix/vpsfree-kb-contracts; upstream SSH remote
  git@github.com:vpsfreecz/vpsfree-kb-contracts.git. Master currently resolves
  to e5ed479f9d4058556dcf225b4c16afd5b9f0051a; fetch before creating worktree.

## Status

- The user approved the implementation and merge plan. This fork already has
  a portal manifest, blank initial tracking and an empty worktree group.
- dev-session current reports no session and VPSFREE_DEV_SESSION_SLUG is unset.
  The user's explicit fork identity authorizes this existing slug; target it
  explicitly rather than inferring another concurrent session.
- Shared workspace remains on master. Preserve unrelated tracked edits,
  including retained password-reset state, and all unrelated untracked files.
- Read the KB repository AGENTS, README, flake and checks, required general and
  architecture review guidance, handoff skill and English writing skills.

## Commands run

- Read-only session, branch/worktree, hook-manifest and SSH remote inspection.
- Read prior failed Guix evidence and live image index during the parent
  investigation. Both latest and stable resolve to 20260905; 20260819 is absent.

## Results

- The two test creation commands pin 20260819; the image repository retains
  only four dated Guix builds. Current master has the same stale pin.
- No feature branch or repository worktree has been created for this fork yet.

## Open questions

None. Initial tracking commit, isolated implementation, verification, review,
integration tests, CI, merge and archival remain.

## Cleanup

Remove only this fork's test VM state and clean feature/temporary worktrees
after merge. Retain branches. Never touch the independent password-reset cluster.
The installed helper lacks finalize; the version-controlled libexec/dev-session
implements the guarded finalization workflow if the installed version still
lags at completion.
