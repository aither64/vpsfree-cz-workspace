# confctl integration preparation: lead execution only

Preparation is complete, unclaimed. No merge or default push has been performed.
User approval for all eight default integrations is recorded by the lead. The
lead alone launches the confctl claim and critical section below.

Prepared detached target:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/confctl-integration-target`.
It is clean at `cc40679d267165aecfa569128438bb55fe910268`. Feature source remains
clean at exact reviewed `822c0e35dbe2549111912f539116b4225dfd3035`.

Fresh canonical SSH observation/fetch at 19:35:32 UTC confirms default `master`
still `cc40679d`, feature `822c0e35`, and remote R evidence `5436d3d7`. No target
movement or rebase occurred. Complete two-commit series and full-index binary
diff match review `6bb7afca` and inventory `821181a5` exactly. Final comparison
was captured with the normal `dev-session worktree capture-comparison` command.
See [ready receipt](verification/confctl-integration-preparation/ready.json),
[source identity](verification/confctl-integration-preparation/source.json) and
[fresh refs](verification/confctl-integration-preparation/refs.json).

The target's declared shell/dependency inputs equal the feature's. A distinct
78 MiB copy of installed gems avoids a cold bootstrap. Target `nix develop`,
`bundle check`, ordinary Overcommit install/sign/list and executable-hook checks
passed. [Hook log](verification/confctl-integration-preparation/hooks.log) and
hashes in the ready receipt cover pre-commit, commit-msg, post-checkout,
post-merge and pre-push. Enabled commit hooks retain Nixfmt/RuboCop; configured
PostMerge and PrePush hooks are all disabled, while their framework entrypoints
remain installed and executable. No bypass or signature suppression was used.
No package, suite or live test was rerun.

Read in full: current Git/coordination/verification/commits procedures, repository
AGENTS, and the selected `workspace-host coordination guide`. That guide reports
package `/nix/store/l9sc1ksacdkm7iij99ggyg87bqsp9n15-dev-workspace-0.2.0` and
coordination catalog `sha256:7d6e4bf2dedfdadc36616646e079dfc598cd227c919302f1b54a1973ed465df8`.

## Exact bounded lead plan

Enter the prepared target's declared environment **before** requesting ownership:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/confctl-integration-target
nix develop --no-write-lock-file -c bash
```

Any shell/dependency intervention remains unclaimed preparation. The lead then
acquires **one confctl repository claim only**, using its fresh request ID and
the ordinary coordination interface. Confirm authoritative exact claim status
is held by this session before executing the following commands. No machine
claim or shared-workspace tracking lock is needed for this independent target.
Do not put shell bootstrap, tests, CI waits or review inside the claim.

In that already prepared shell, with the exact held claim:

```sh
set -euo pipefail
confctl_target=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/confctl-integration-target
confctl_feature=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-flake-update-downgrade-guard-replacement/confctl
confctl_logs=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/verification/confctl-integration-preparation
cd "$confctl_target"
[[ $(git rev-parse HEAD) == cc40679d267165aecfa569128438bb55fe910268 ]]
[[ -z $(git status --porcelain=v1) ]]
[[ $(git -C "$confctl_feature" rev-parse HEAD) == 822c0e35dbe2549111912f539116b4225dfd3035 ]]
[[ -z $(git -C "$confctl_feature" status --porcelain=v1) ]]
for confctl_hook in post-merge pre-push pre-commit commit-msg; do
  [[ -x $(git rev-parse --git-path "hooks/$confctl_hook") ]]
done
git ls-remote --symref git@github.com:vpsfreecz/confctl.git \
  HEAD refs/heads/master \
  refs/heads/2026-10-24-flake-update-downgrade-guard-replacement \
  refs/heads/2026-10-24-flake-update-downgrade-guard-replacement-provider-r-evidence \
  > "$confctl_logs/critical-before.stdout"
```

Inspect that fresh output before merging: default and HEAD must be `cc40679d`,
feature `822c0e35`, R evidence `5436d3d7`. Recheck feature/tree and full-series/diff
identity against the ready receipt if any preparation changed. Unexpected
movement stops the critical section; reconcile effects and release before
choosing repair. Never rebase or change the provider/pins under this claim.

```sh
git merge --ff-only 822c0e35dbe2549111912f539116b4225dfd3035 \
  > "$confctl_logs/critical-merge.log" 2>&1
[[ $(git rev-parse HEAD) == 822c0e35dbe2549111912f539116b4225dfd3035 ]]
[[ -z $(git status --porcelain=v1) ]]
```

**Inspect the actual complete merge/hook log before pushing.** A successful Git
status can coexist with a failed post-merge hook. Hook errors, trust changes,
or unexpected messages require effects inspection and unlocked repair, never
bypass or retry. No merge commit is allowed; detached target HEAD should simply
advance to the exact reviewed feature.

Once merge/hook results are accepted, freshly verify remote `master` still
`cc40679d` and then push normally:

```sh
git ls-remote git@github.com:vpsfreecz/confctl.git refs/heads/master \
  > "$confctl_logs/critical-before-push.stdout"
# Lead verifies that output is still exact cc40679d before the next command.
git push --porcelain git@github.com:vpsfreecz/confctl.git HEAD:refs/heads/master \
  > "$confctl_logs/critical-push.log" 2>&1
git ls-remote --symref git@github.com:vpsfreecz/confctl.git \
  HEAD refs/heads/master \
  refs/heads/2026-10-24-flake-update-downgrade-guard-replacement \
  refs/heads/2026-10-24-flake-update-downgrade-guard-replacement-provider-r-evidence \
  > "$confctl_logs/critical-after.stdout"
[[ $(git rev-parse HEAD) == 822c0e35dbe2549111912f539116b4225dfd3035 ]]
[[ -z $(git status --porcelain=v1) ]]
```

Fresh final proof must show default/HEAD and feature at exact `822c0e35`, evidence
at exact R `5436d3d7`, and clean detached target. A rejected/interrupted push or
failed proof requires inspecting actual remote refs and command effects before
any retry/release. Do not force-push a default or roll back/reset the target.

After known successful effects, inspect the authoritative exact owned claim,
release it through ordinary `coordination release`, and verify released state.
Do this **before** CI, records or any subsequent checkout work. Do not wait for
CI while holding ownership. If stopped with known-safe effects, release before
repairing preparation. Uncertain mutations require active reconciliation first.

Preserve feature and R-evidence refs, all existing roots and the prepared target.
No cleanup, lifecycle, deployment or other default integration is part of this
package. The lead records final merge/ref/claim receipts and owns further steps.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
