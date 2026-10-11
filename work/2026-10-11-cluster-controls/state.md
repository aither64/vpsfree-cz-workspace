---
lifecycle: active
---

# 2026-10-11-cluster-controls

## Status

Ready, awaiting merge approval. Implementation, independent review, local checks,
CI, aitherdev deployment and live VM validation are complete.
The user's "Implement the plan" authorizes implementation and deployment.
Feature integration into master is not authorized.

- [x] Plan and user preferences: normal Start, visible toolbar controls.
- [x] Create separate owned initiative (no native Codex lead/roster).
- [x] Implementation and documentation.
- [x] Quick verification and commits.
- [x] Independent final review and branch-history inventory.
- [x] Longer verification and CI.
- [x] aitherdev deployment and authenticated live assets.
- [x] Disposable-cluster known-file creation and portal Stop validation.
- [x] Portal Start disk-retention and Release validation.
- [x] Ready, awaiting merge approval.

## Next actions

No remaining implementation or verification work. Integrate the four published
feature branches only after explicit repository/target direction. Final series:
[final-heads.md](final-heads.md). Review: [review.md](review.md);
inventory: [review-packet.md](review-packet.md).
Integration remains gated on explicit repository/target direction. Before an
approved integration, fetch current upstreams and rebase as needed, prove patch
equivalence and repeat affected checks/comparison capture. Shared workspace
master advanced with unrelated tracking after final review; the exact reviewed
and deployed workspace feature head remains 7c226d3.

## Documentation

Design: [design.md](design.md). Provider contract and UI explanation:
dev-workspace/docs/workspace-portal.md. Retained-start and opt-in controls:
vpsfree-dev-workspace/dev-clusters/{vpsadmin,vpsadminos}/README.md.
Reusable setup lessons: notes/cross-project/2026-10-11-cluster-control-test-environment.md.
Live readiness: notes/vpsfree-dev-workspace/2026-10-12-live-devcluster-readiness.md.

## Repositories

Registered: dev-workspace, vpsfree-dev-workspace, workspace,
vpsfree-cz-configuration. All worktrees beneath
worktrees/2026-10-11-cluster-controls/<project>; feature branch:
2026-10-11-cluster-controls. Initial bases are recorded in portal.yml.

## Commands run

- dev-session current: no current session and no environment/thread binding.
- dev-session start cluster-controls --no-codex --no-attach --json: created slug.
- With both explicit environment values, dev-session current returned the
  created slug and this workspace. team list refuses because this shell session
  has no native lead; no retained member roster is available or changed.

## Results

- Initial plan/state committed on shared master as 1deacf09. Dedicated
  worktrees registered; design recorded before application edits.
- First focused batch (fresh Luna/low quick_checks watcher): Go cluster and
  selected web tests passed. Ruby status tests refused missing default fixture
  environment. Corrected shared shell setup to match extension testEnvironment.
- Corrected-environment run: status cases passed (2 runs, 37 assertions).
  Retained-start test reached the build but its assertion expected selection
  in argv, while helpers pass it in environment. Fixed assertion to observe
  the actual build environment. Complete focused batch passed; see
  quick-checks-3.log and quick-checks-3.status (0). Start: 2 runs/40 assertions.
- Configuration checkout initially refused its Overcommit post-checkout hook
  because ambient Ruby lacked gems. Checkout was created; registration retry
  succeeded. Nix shell now installed/signed the hooks and bundle check passed.
- Final composed deployment contract passed with runtime bc6b841 and extension
  7157c80, preserving sibling inputs. All four branches are published over SSH;
  final exact heads are in final-heads.md.
- Chromium and Firefox real portal fixture passed (14.86s): keyboard reveal,
  hidden-password copy, clipboard errors, icon preservation, alignment at
  1280/375 widths, pending/error controls, tab preservation, legacy Release-only,
  cancel/confirm Release and refresh without page reload.
- Full long batch passed (status 0, about 1h 7m): real browser fixture, generic
  and extension flake checks, composed provider smoke and final workspace flake
  check. No unexpected kernel build or cancellation. Full local evidence:
  long-checks.log and long-checks.status. Verification summary: verification.md.
  The host-module and session-recovery VM tests passed; the reboot fixture's
  portal stop timeout was recovered and did not fail the test.
- Initial host build stopped at confctl's confirmation prompt (EOF/status 1).
  Build --help confirms --yes; corrected the prepared noninteractive command.
  Original evidence: host-build-confirmation.log/status. No system deployment
  occurred. The first build watcher admitted reading guidance after launching;
  the replacement is instructed to complete all reads before execution.
- Corrected host build, dry activation, host switch and application-profile
  switch passed, guarded by exact source heads and prior generations. Two host
  health checks passed and none failed. Current profile is hw9v17h...; system
  ccgznwp2... (full paths in rollout.md).
- The deployment unit's asset check lacked the newly configured owner group
  inherited by its existing user manager. Inline current-shell verification
  passed: authenticated HTTPS, exact reviewed assets, portal/router active.
  No password or file permissions changed. The reusable group note describes
  the corrected launcher for subsequent verification.
- All four feature worktrees are clean, and an independent SSH ls-remote check
  confirms their published feature heads match final-heads.md exactly.
  The first live VM startup reached readiness, but the verification script
  omitted the documented -- separator before its remote SSH command. SSH
  interpreted that command as a hostname and refused it. The unit's exit then
  stopped its child runner; retained state is stopped with Start/Release
  available. Evidence is preserved as live-cluster-ssh-failure.*. The corrected
  script uses -- and normal retained Start; no source changes or disk reset.
- The corrected SSH invocation then ran before guest networking/SSH services
  were ready. Console and shell logs show OSVM's control shell was available
  while host keys/services were starting, followed immediately by the script's
  failed connection and systemd terminating QEMU. Existing runner readiness
  waits for that control shell, not SSH/tank. Evidence is preserved as
  live-cluster-network-wait.*. Verification now probes guest SSH/tank readiness
  before writing/comparing the file, without retrying portal Start operations.
- Final live validation passed (status 0, phase complete, about 10 minutes):
  guest readiness, initial known-file write/read, portal Stop, normal portal
  Start and exact file comparison, and portal Release. Saved single/bridge
  selection remained unchanged. Stop advertised Start/Release; Start reported
  running/ready with Stop/Release. Release removed the owned state directory.
  Primary verified the final log and absence of that directory. No unexpected
  kernel build or cancellation. Retained disks were reused until the intended
  Release; application sources did not change during validation.

## Open questions

No technical blockers. Primary-agent design/edits used ordinary supported
resolution for this unmanaged caller; review used the installed catalog
fallback. Destructive Release, long Start handling and mixed-version provider
compatibility were covered by review and verification. Initial cluster setup
remains a CLI operation; portal Start requires retained configuration.

## Independent review

High risk: secrets, destructive Release, host operations and cross-project
contracts. All four lanes applied. Fresh /root/final_review launched with
fork_turns none, GPT-6 Astra/xhigh from installed lead_reviewed reviewer policy;
no retained roster is available. Catalog digest:
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.
Role identity and tool/API attestation limitations are recorded in review.md.

Whole branches reviewed at heads 74b2dc1, 7157c80, 04039ba9 and 72a2876.
No obsolete history; one final update per pin stream; no migrations. One
Important General finding: existing rendering test still expected the removed
Release footer. Replaced it with toolbar/Release assertions and folded into the
owning commit; runtime now bc6b841be0bf83ad84f47daa2e0c064f477bdf23.
Affected rendering/control/browser-contract tests passed (web 1.344s).
No other Blocking/Important findings. Narrow correction and pin refresh do not
change reviewed design; direct verification suffices under skill step 9.

Initial automatic runtime CI 38170806132 failed on that same obsolete assertion;
downloaded failure logs in ci-runtime-initial.log establish the cause. No blind
rerun. New head CI 38171425609 passed on exact runtime head bc6b841;
no superseded live runs remain to cancel.
Extension CI 38170807346 passed on exact head
7157c8098dcf60127aa4df823fab82b4185ad22a (normal flake and packaged
devcluster-check workflow).

## Cleanup

Keep initiative active and retain all branches. No archive/delete is authorized.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-11-cluster-controls/
