---
lifecycle: complete
---

# 2026-09-09-guix-test-fix

## Current handoff

The standalone Guix fix is merged and pushed to vpsfree-kb-contracts master at
81d6d7dfe530884aff3e1d2634e02e4b12fe28e8. Required reviews, quick checks,
the local five-example Guix run, feature CI and both merged-master CI runs
passed. All requested implementation, review, test and merge work is complete.
The final step is guarded archival of only this fork after the conversation
is idle, through the independent worker described below.

The parent 2026-08-18-vpsadmin-password-reset feature changes remain unmerged.
This fork did not modify its branches, worktrees, pins or independent running
cluster. No production or wiki deployment is required.

## Repository and change

- Repository: vpsfree-kb-contracts, the renamed KB captures repository.
- Canonical bare registration: repos/vpsfree-kb-contracts.git (an alias of
  repos/vpsadmin-kb-captures.git).
- SSH remote: git@github.com:vpsfreecz/vpsfree-kb-contracts.git.
- Feature branch: 2026-09-09-guix-test-fix.
- Feature worktree: worktrees/2026-09-09-guix-test-fix/vpsfree-kb-contracts.
- Base: e5ed479f9d4058556dcf225b4c16afd5b9f0051a.
- Reviewed, tested and merged head: 81d6d7dfe530884aff3e1d2634e02e4b12fe28e8.
- Commit: tests/kb: resolve the latest Guix image for each run.
- Only tests/suite/kb/guix.nix and its README description changed. The source
  fixture selects latest, reads and logs its concrete version, and reuses that
  exact version for the target. Assertions reject an empty/unresolved version
  and require both fixture versions to match. Existing retries and assertions
  remain in place. No dependency pins or parent feature changes are included.

## Root cause

Both fixture creation commands hardcoded image version 20260819. The public
image repository retains four numeric Guix builds, and that archive is absent.
The September 9 index contained 20260822, 20260823, 20260829 and 20260905;
latest and stable resolved to 20260905. The expired archive returned 404 while
latest and 20260905 were available. This is consistent with retention cleanup;
an individual deletion event was not inspected. Parent run 34276611772 and
master run 34020694050 failed during fixture creation before test assertions.

## Setup and review

- The user explicitly selected this fork and authorized implementation and
  merge. dev-session current reported no process-owned session and the slug
  environment variable was unset, so every helper call targeted this slug.
- Initial substantive plan, state and portal were committed to shared workspace
  master as f48080b before project commits or external mutations. Started the
  fork with installed dev-session start --as-is --no-attach --no-codex and added
  its registered worktree with dev-session worktree add from origin/master.
- Read repository AGENTS, README, flake and checks. No Git hook framework or
  package.json commit-hook integration is declared; the normal commit ran.
- Applied the English user-facing writing skill directly to the README.
- Mandatory low-risk general and architecture reviews both used fresh
  gpt-5.6-sol agents at xhigh on exact head 81d6d7d. Both found no Blocking,
  Important or Advisory issues. They verified the pinned provider's tag lookup,
  imported concrete version and shared Ruby local across suite hooks/examples.
  No remediation or rerun was needed. Review preceded all long tests.
- Review artifacts: review/packet.md, review/general.md, review/architecture.md.
  Their then-pending runtime validation gaps are covered by results below.

## Validation

- Full nix develop -c bin/check passed before commit, including all contract
  and unit checks and 120 PNG validations. Evaluated the final Guix test JSON,
  inspected generated Ruby and ran ruby -c in the pinned shell: Syntax OK.
  git diff --check passed.
- Feature Check 34344892246 passed.
- Feature Managed page runtime 34344892259 passed: all four suites / twelve
  scripts, 1581.96 seconds total; Guix passed in 1571.72 seconds. Downloaded
  the job log and inspected the successful summary. No CI rerun was needed.
- Focused local command:
  ./test-runner.sh test --state-dir /tmp/guix-vm.8StPJx --fresh --jobs 1
  kb/guix#reconfigure.
  All five examples passed, normal exit at 13:52:48 CEST on September 9,
  2013.83 seconds total. Both containers imported 20260905. Shipped integration,
  reconfiguration and generation activation, restart, networking/SSH, deployment,
  signing-key and post-deployment checks passed. Guix preparation took about
  21 minutes and succeeded without a retry. Cached Linux 6.12.95 kernel/initrd,
  QEMU and virtiofsd were used; no kernel source build occurred.
- Full nix develop -c bin/check passed again in the actual temporary target
  worktree before pushing master, including all 120 PNG checks.
- Merged-master Check 34347984918 passed.
- Merged-master Managed page runtime 34347984983 passed: all four suites /
  twelve scripts in 2336.94 seconds. All five Guix examples passed; the Guix
  suite completed in 1748.10 seconds. KVM was the last suite to finish, at
  2336.92 seconds. Downloaded master-ci.log and inspected the complete summary.
  Successful runs do not upload full machine-log artifacts, so no additional
  claim is made about internal Guix retries in CI. No workflow rerun was used.
- Final remote verification still showed both master and the retained feature
  at 81d6d7d, and the feature worktree remained clean and attached.

GitHub run URLs use
https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/<run-id>.
Temporary detailed logs are in /tmp/guix-test-fix-20260909.rC0rvr/:
check.log, guix-test.json, guix-test.rb, guix-vm.log, feature-ci.log,
integration-check.log, master-ci.log and CI watcher logs. Focused machine logs are under
/tmp/guix-vm.8StPJx/os-test-kb__guix-ca1988c9/. These are diagnostic files outside
the initiative, not portal artifacts or files to commit.

## Integration

Fetched master again after validation and confirmed it remained e5ed479 and was
an ancestor of the reviewed feature. Created a fresh temporary target worktree
at worktrees/2026-09-09-guix-test-fix/vpsfree-kb-contracts-merge on the unused
local master, advanced it to fetched origin/master, and merged the feature with
git merge --ff-only. After the target-worktree checks passed, pushed master over
SSH and verified remote master and feature refs both at 81d6d7d. No merge commit
or history rewrite was used. Removed the clean temporary worktree non-force.

## Cleanup and cutover workflow

The local test runner powered off its disposable VM and cleaned its disks.
Verified its QEMU and virtiofsd processes are gone and no VM disk images remain.
The feature worktree is clean and attached. Keep local and remote feature refs.
No managed vpsAdmin or vpsAdminOS cluster was started for this fork; both installed
cluster status helpers report stopped for this exact slug.

The deployed profile uses dev-session archive, which provides the guarded merged
branch proof, worktree removal, tracking archive/commit and session retirement.
The older checkout helper rejects the current tmux_identity authority field.
Do not alter authority metadata or bypass the owning-thread idle guard. The
installed archive command resets only resources for this fork's exact slug.
The parent password-reset cluster is outside that scope.

Reusable cutover lesson committed as workspace 3e8fe14:
notes/cross-project/2026-09-09-cutover-archive-helper.md.
The independent cleanup worker is prepared at
/tmp/guix-test-fix-20260909.rC0rvr/finish.py. Read-only preflight passed through a
systemd user service: SSH access, clean expected feature, prepared file hashes,
stopped fork clusters and the ordinary thread-idle check. The thread is active,
so archival must run after the final reply. With all CI now green, the finishing
service is queued as guix-fix-archive.service, outside the managed tmux session.
It verifies the final tracking fingerprints and worktree state while waiting
up to 30 minutes for the ordinary idle check, then invokes the pinned installed
dev-session archive command. Any changed input or unexpected state stops it.

Worker evidence is outside the archived tree:
/tmp/guix-test-fix-20260909.rC0rvr/finish.log and finish-result.json.
The latter is written only after archive completion and contains the final
archive commit. The installed helper changes lifecycle to complete, commits
only this initiative's archive transition, removes its clean worktree, retains
branch refs and retires this session. The lifecycle remains active until that
ordinary workflow runs; no idle or ownership check is bypassed.

Shared workspace stays on master. Preserve all unrelated tracked edits and
untracked files, including the parent's records. The installed archive command
stages and commits only work/2026-09-09-guix-test-fix and its archive destination;
no separate tracking checkpoint, manual archive commit or stop is needed.

## Portal

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-guix-test-fix/

No user decision is pending. Guarded archival is queued for after this reply.
If cleanup stops, inspect the worker log and installed helper journal before
retrying; do not change the parent initiative or bypass lifecycle checks.
