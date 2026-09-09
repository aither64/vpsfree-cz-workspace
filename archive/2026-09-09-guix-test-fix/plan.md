# 2026-09-09-guix-test-fix

## Goal

Fix the managed Guix runtime suite's expired image pin and merge the standalone
fix into vpsfree-kb-contracts master. The user forked this initiative from
2026-08-18-vpsadmin-password-reset and explicitly authorized the fix and merge.
Leave all password-reset feature branches, worktrees, pins and its independent
running development cluster untouched.

## Affected repositories

- vpsfree-kb-contracts (the renamed KB captures repository), with a new feature
  branch and worktree named 2026-09-09-guix-test-fix, based on current master.
- Workspace coordination records only; no workspace behavior change.

## Approach

- Create the first Guix test container using the published latest tag. Read
  and log its concrete image version and use that version for the deployment
  target, then assert both containers use the same build.
- Preserve visible image lookup failures and existing classified Guix retries.
  Do not fall back to an older image or update the image publication pipeline.
- Update the README to describe latest selection once per run. Keep the test
  and its directly supporting prose in one focused functional commit.
- Verify and review before long tests, push and monitor CI, then fetch master
  again and integrate only this fix using a temporary target worktree and a
  fast-forward-only merge. Retain branch refs after cleanup and archive this
  completed initiative using the installed guarded archive workflow.

## Compatibility and deployment

This changes only disposable test fixture selection and its README description.
There are no API/client interfaces, persisted production formats, schemas,
migrations, protocols, generated configuration or dependency pin changes.
Both test containers use one resolved build even if latest moves during a run.
No production deployment, wiki publication, rolling upgrade or coordinated
node update is required. Reverting the change restores the expired test pin
without affecting production state. The password-reset initiative stays active
and unmerged, and its cluster must not be modified or stopped.

## Testing plan

- Run the pinned-shell bin/check, inspect and syntax-check the generated Ruby
  test script, and verify any declared Git hook framework before committing.
- Required review is low risk: general and architecture lanes, each with a
  fresh gpt-5.6-sol reviewer at xhigh. Resolve findings before long validation.
- Run test-runner.sh test --fresh kb/guix#reconfigure in its own test state.
  Require image identity, shipped configuration, reconfiguration, restart,
  networking, SSH, deployment, signing-key and post-deployment checks to pass.
- Require static and full managed-page runtime CI on the feature and merged
  master. Investigate logs and artifacts before any rerun. Stop and investigate
  an unexpected local kernel build; use cached kernels for this test-only fix.

## Cleanup decision after the runtime cutover

The deployed profile exposes `dev-session archive`, which verifies merged
remote branches, removes clean worktrees, retains branches, archives and commits
only this initiative's tracking, and retires its session. Its live authority
includes `tmux_identity`, which the older checkout finalizer does not understand.
Use the installed archive command, without changing authority metadata or
bypassing its checks. It resets only cluster resources belonging to this exact
fork slug; both fork cluster helpers report stopped and no such cluster was
started for this task.

The archive command requires the owning conversation to be idle. After all
merged-master CI passes, prepare final tracking and queue an independent user
service to wait for that ordinary guard, recheck the prepared input hashes and
clean worktree, and invoke archive after the final reply. Stop on unexpected
state or changed inputs. Keep its logs outside the worktree and tracking tree.
This preserves the parent password-reset session and its running cluster.
