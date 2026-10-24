# vpsadminos: prepared target and lead-only merge plan

Ready, unclaimed. Target `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsadminos-integration-target` is detached, clean at `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854`.
Feature `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsadminos` is clean at exact reviewed `889f14e5f964c85eac0dbffdff96909a46ab35c6`. Fresh SSH/fetch and
full-series/full-index binary diff/lock identity are in source.json and ready.json,
bound to review6bb7af and inventory821181. No source/head/pin change or test rerun.

Installed executable hooks: commit-msg, overcommit-hook, post-checkout, post-commit, post-merge, post-rewrite, pre-commit, pre-push, pre-rebase, prepare-commit-msg.
Declared environment and normal hook setup are recorded in environment.log.

The lead enters `nix develop --no-write-lock-file -c bash` in the target before
acquiring one `vpsadminos` repository claim. Resolve any dependency/trust issue
unclaimed. Read authoritative exact claim status and proceed only when held.
No machine claim or shared workspace tracking lock is needed for this target.

Inside that already prepared shell and held claim:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsadminos-integration-target
[[ $(git rev-parse HEAD) == e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854 ]]
[[ -z $(git status --porcelain=v1) ]]
[[ $(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsadminos rev-parse HEAD) == 889f14e5f964c85eac0dbffdff96909a46ab35c6 ]]
[[ -z $(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsadminos status --porcelain=v1) ]]
git ls-remote --symref git@github.com:vpsfreecz/vpsadminos.git HEAD refs/heads/staging refs/heads/2026-10-24-flake-update-downgrade-guard-replacement
```

Inspect the fresh target/feature equality before merging. Any movement stops
this attempt; reconcile effects and release before repair/rebase decisions.
Then ordinary fast-forward merge (retain full stdout/stderr):

```sh
git merge --ff-only 889f14e5f964c85eac0dbffdff96909a46ab35c6
[[ $(git rev-parse HEAD) == 889f14e5f964c85eac0dbffdff96909a46ab35c6 ]]
[[ -z $(git status --porcelain=v1) ]]
```

Inspect actual complete merge/hook output even if Git exits0; post-merge hooks
can fail without failing Git. On hook failure, inspect effects, release once
known safe, repair unlocked. Never bypass hooks or silently retry.
Before push freshly prove remote target still exact `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854`:

```sh
git ls-remote git@github.com:vpsfreecz/vpsadminos.git refs/heads/staging
# Lead verifies exact expected target before proceeding.
git push --porcelain git@github.com:vpsfreecz/vpsadminos.git HEAD:refs/heads/staging
git ls-remote --symref git@github.com:vpsfreecz/vpsadminos.git HEAD refs/heads/staging refs/heads/2026-10-24-flake-update-downgrade-guard-replacement
[[ $(git rev-parse HEAD) == 889f14e5f964c85eac0dbffdff96909a46ab35c6 ]]
[[ -z $(git status --porcelain=v1) ]]
```

Final target and feature must both equal exact `889f14e5f964c85eac0dbffdff96909a46ab35c6`. No force push or
feature deletion. A rejected/interrupted push requires actual ref/effect
reconciliation before release/retry; do not reset the target or hide uncertainty.
Verify authoritative exact owned claim, release, and prove released state before
CI, records or any subsequent work. Do not hold ownership for CI waits/tests.
No cleanup, deployment or lifecycle action is authorized. Preserve target,
feature refs and existing roots. Lead records integration effects and receipts.
