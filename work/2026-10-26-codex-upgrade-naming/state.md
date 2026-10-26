---
lifecycle: active
---

# 2026-10-26-codex-upgrade-naming

## Status

- Phase: scope and fresh-worktree preparation. Session identity verified against
  thread binding and both environment markers. Same-session roster is null.
- [x] Read source final state/rollout and relevant historical naming/upgrade design.
- [x] Fetch current defaults; identify already merged UI and latest observer work.
- [ ] Finish bounded design and port remaining changes.
- [ ] Quick checks, committed independent review, feature publication.
- [ ] Required changed-input package/integration checks and final consumer builds.
- [ ] Explicit approval for default integration and physical activation.
- No claims, active deployment, lifecycle action or old-session ownership adopted.

## Next actions

Finish own worktree setup, preserve exact client025 evidence, port only selected
runtime units, then regenerate downstream pins on current defaults.

## Documentation

## Repositories

Feature branch: 2026-10-26-codex-upgrade-naming in each affected repository.
Worktrees: worktrees/2026-10-26-codex-upgrade-naming/{codex-web,dev-workspace,
vpsfree-cz-configuration,workspace}. Client base8b60554, runtime7e6d7c9c,
configuration45334601, workspace116671cb3. All old refs remain untouched.

## Commands run

Identity/current and roster; read routed procedures and update skills; fetch each
origin over SSH. Client/runtime worktree registration succeeded. Configuration
worktree creation reached HEAD45334601 but inherited post-checkout hook failed
because ambient Bundler lacks its declared gems; reconcile in its Nix shell and
retry ordinary registration, without reset/removal. Workspace worktree pending.

## Results

Saved client-native-verification-preparation/parent-025-state06-assessment.json in
source session records exact025 native upgrade/restart/fork/receipt/queue/message
and offline old-reader cold-read PASS (43s batch, 7s stage). It does not prove safe
downgrade, old-version writes or mixed-version operation; preserve that limit.

## Open questions

## Cleanup

No cleanup or lifecycle actions authorized for either session. Keep both open.
