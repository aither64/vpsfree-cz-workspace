# vpsf-status: prepared target and lead-only merge plan

Ready, unclaimed. Target `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsf-status-integration-target` is detached, clean at `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb`.
Feature `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsf-status` is clean at exact reviewed `018b700f06cf216a125a70ac9bfedddaabf07b92`. Fresh SSH/fetch and
full-series/full-index binary diff/lock identity are in source.json and ready.json,
bound to review6bb7af and inventory821181. No source/head/pin change or test rerun.

Installed executable hooks: pre-commit, prepare-commit-msg.
Declared environment and normal hook setup are recorded in environment.log.

The lead enters `nix develop --no-write-lock-file -c bash` in the target before
acquiring one `vpsf-status` repository claim. Resolve any dependency/trust issue
unclaimed. Read authoritative exact claim status and proceed only when held.
No machine claim or shared workspace tracking lock is needed for this target.

Inside that already prepared shell and held claim:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsf-status-integration-target
[[ $(git rev-parse HEAD) == 587cd65bb02e6dddea7f6b6409e42a15f36ab4fb ]]
[[ -z $(git status --porcelain=v1) ]]
[[ $(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsf-status rev-parse HEAD) == 018b700f06cf216a125a70ac9bfedddaabf07b92 ]]
[[ -z $(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsf-status status --porcelain=v1) ]]
git ls-remote --symref git@github.com:vpsfreecz/vpsf-status.git HEAD refs/heads/master refs/heads/2026-10-24-flake-update-downgrade-guard-replacement
```

Inspect the fresh target/feature equality before merging. Any movement stops
this attempt; reconcile effects and release before repair/rebase decisions.
Then ordinary fast-forward merge (retain full stdout/stderr):

```sh
git merge --ff-only 018b700f06cf216a125a70ac9bfedddaabf07b92
[[ $(git rev-parse HEAD) == 018b700f06cf216a125a70ac9bfedddaabf07b92 ]]
[[ -z $(git status --porcelain=v1) ]]
```

Inspect actual complete merge/hook output even if Git exits0; post-merge hooks
can fail without failing Git. On hook failure, inspect effects, release once
known safe, repair unlocked. Never bypass hooks or silently retry.
Before push freshly prove remote target still exact `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb`:

```sh
git ls-remote git@github.com:vpsfreecz/vpsf-status.git refs/heads/master
# Lead verifies exact expected target before proceeding.
git push --porcelain git@github.com:vpsfreecz/vpsf-status.git HEAD:refs/heads/master
git ls-remote --symref git@github.com:vpsfreecz/vpsf-status.git HEAD refs/heads/master refs/heads/2026-10-24-flake-update-downgrade-guard-replacement
[[ $(git rev-parse HEAD) == 018b700f06cf216a125a70ac9bfedddaabf07b92 ]]
[[ -z $(git status --porcelain=v1) ]]
```

Final target and feature must both equal exact `018b700f06cf216a125a70ac9bfedddaabf07b92`. No force push or
feature deletion. A rejected/interrupted push requires actual ref/effect
reconciliation before release/retry; do not reset the target or hide uncertainty.
Verify authoritative exact owned claim, release, and prove released state before
CI, records or any subsequent work. Do not hold ownership for CI waits/tests.
No cleanup, deployment or lifecycle action is authorized. Preserve target,
feature refs and existing roots. Lead records integration effects and receipts.
