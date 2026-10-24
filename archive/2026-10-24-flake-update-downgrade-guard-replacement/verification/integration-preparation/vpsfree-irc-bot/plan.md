# vpsfree-irc-bot: prepared target and lead-only merge plan

Ready, unclaimed. Target `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsfree-irc-bot-integration-target` is detached, clean at `94ac4eb5a7caf0456fff7df86a44cae198463276`.
Feature `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsfree-irc-bot` is clean at exact reviewed `0a160463a4ee12ec5f6c45e38eaba11592787d9f`. Fresh SSH/fetch and
full-series/full-index binary diff/lock identity are in source.json and ready.json,
bound to review6bb7af and inventory821181. No source/head/pin change or test rerun.

Installed executable hooks: commit-msg, overcommit-hook, post-checkout, post-commit, post-merge, post-rewrite, pre-commit, pre-push, pre-rebase, prepare-commit-msg.
Declared environment and normal hook setup are recorded in environment.log.

The lead enters `nix develop --no-write-lock-file -c bash` in the target before
acquiring one `vpsfree-irc-bot` repository claim. Resolve any dependency/trust issue
unclaimed. Read authoritative exact claim status and proceed only when held.
No machine claim or shared workspace tracking lock is needed for this target.

Inside that already prepared shell and held claim:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsfree-irc-bot-integration-target
[[ $(git rev-parse HEAD) == 94ac4eb5a7caf0456fff7df86a44cae198463276 ]]
[[ -z $(git status --porcelain=v1) ]]
[[ $(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsfree-irc-bot rev-parse HEAD) == 0a160463a4ee12ec5f6c45e38eaba11592787d9f ]]
[[ -z $(git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsfree-irc-bot status --porcelain=v1) ]]
git ls-remote --symref git@github.com:vpsfreecz/vpsfree-irc-bot.git HEAD refs/heads/master refs/heads/2026-10-24-flake-update-downgrade-guard-replacement
```

Inspect the fresh target/feature equality before merging. Any movement stops
this attempt; reconcile effects and release before repair/rebase decisions.
Then ordinary fast-forward merge (retain full stdout/stderr):

```sh
git merge --ff-only 0a160463a4ee12ec5f6c45e38eaba11592787d9f
[[ $(git rev-parse HEAD) == 0a160463a4ee12ec5f6c45e38eaba11592787d9f ]]
[[ -z $(git status --porcelain=v1) ]]
```

Inspect actual complete merge/hook output even if Git exits0; post-merge hooks
can fail without failing Git. On hook failure, inspect effects, release once
known safe, repair unlocked. Never bypass hooks or silently retry.
Before push freshly prove remote target still exact `94ac4eb5a7caf0456fff7df86a44cae198463276`:

```sh
git ls-remote git@github.com:vpsfreecz/vpsfree-irc-bot.git refs/heads/master
# Lead verifies exact expected target before proceeding.
git push --porcelain git@github.com:vpsfreecz/vpsfree-irc-bot.git HEAD:refs/heads/master
git ls-remote --symref git@github.com:vpsfreecz/vpsfree-irc-bot.git HEAD refs/heads/master refs/heads/2026-10-24-flake-update-downgrade-guard-replacement
[[ $(git rev-parse HEAD) == 0a160463a4ee12ec5f6c45e38eaba11592787d9f ]]
[[ -z $(git status --porcelain=v1) ]]
```

Final target and feature must both equal exact `0a160463a4ee12ec5f6c45e38eaba11592787d9f`. No force push or
feature deletion. A rejected/interrupted push requires actual ref/effect
reconciliation before release/retry; do not reset the target or hide uncertainty.
Verify authoritative exact owned claim, release, and prove released state before
CI, records or any subsequent work. Do not hold ownership for CI waits/tests.
No cleanup, deployment or lifecycle action is authorized. Preserve target,
feature refs and existing roots. Lead records integration effects and receipts.
