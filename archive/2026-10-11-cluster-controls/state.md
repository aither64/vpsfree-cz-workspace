---
lifecycle: complete
---

# 2026-10-11-cluster-controls

## Status

Complete: all four exact final feature heads are merged into remote master,
and both post-merge CI workflows passed.
Inset Reveal is deployed and verified on aitherdev.
The toolbar, retained Start/Stop/Release and credential icons are available; secret
fields contain Reveal and plain fields/commands have no external placeholder.
Independent whole-branch review, quick/browser/package/composition checks, CI, host
build/activation and authenticated asset verification passed.
The user's "Implement the plan" authorizes implementation and deployment.
User authorized integration into all four master branches with "better, merge it".

- [x] Plan and user preferences: normal Start, visible toolbar controls.
- [x] Create separate owned initiative (no native Codex lead/roster).
- [x] Implementation and documentation.
- [x] Quick verification and commits.
- [x] Independent final review and branch-history inventory.
- [x] Longer verification and CI.
- [x] aitherdev deployment and authenticated live assets.
- [x] Disposable-cluster known-file creation and portal Stop validation.
- [x] Portal Start disk-retention and Release validation.
- [x] Inset Reveal implementation and focused checks.
- [x] Updated branch history/pins and independent review.
- [x] Browser verification, CI and aitherdev update.
- [x] Merge approval received.
- [x] Four fast-forward integrations and remote proof.
- [x] Post-merge CI and final integration handoff.

## Next actions

No remaining work or operator action. Session stays open for follow-up;
registered feature worktrees and primary/rollout references are retained.
Rebased workspace head 0ea24610 is patch-equivalent to the reviewed/deployed
86d96b26; its deployed exact source remains published on rollout-2. The other
three final heads are unchanged. Updated inventory: [merge-record.md](merge-record.md).
Reviewed history/pin streams remain clean, with no migrations.

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

Initiative complete; session remains open and all branches are retained.
Temporary integration worktrees were removed non-force. No archive/delete or
session stop is authorized.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-11-cluster-controls/

## Inset Reveal follow-up

Committed and published runtime 60c679c52c263a0fc7a4b08c5f83a291cfd89191.
Secret inputs now contain the eye; plain fields and commands have no placeholder.
Copy uses one aligned outer column. Existing labels/event handlers remain intact.
Quick JavaScript syntax and two focused Go rendering/browser-contract tests passed
(0.088s); diff whitespace passed. Portal guide updated and parent applied the
user-facing writing skill before committing.

Final configuration e65ef2c4cd179dac2d96cfdfe6d6c6967f08d566 selects 60c679c
through its confctl channel (hooks passed). Workspace 86d96b2656c89f37cd4d521fb150ebb123efa89c
is based on current shared master 64a39659 and selects extension 7157c80 plus
60c679c. Only intended lock nodes changed, and the final deployment contract
passed. Both primary branches force-pushed with exact leases after upstream fetch.
Superseded exact deployed consumer sources 4d0ff7c and 7c226d3 are retained and
published as 2026-10-11-cluster-controls-rollout-1, while final primary pin streams
contain one update each. No migrations.

Fresh standalone /root/inset_review, GPT-6 Astra/xhigh, all four lanes. Previous
standalone reviewer absent from live tree, identity/settings unverified, so replaced
under skill policy; no retained roster exists. Installed policy catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd, published
catalog file hash abc80df4cd14ba74a26f9de1f807b6f2a49f2b9651aea7acbbb70d9a2e5fe7bc.
Native role/model/access selector limitations match the original review. Complete
packet: inset-review-packet.md. Generic exact-head CI 38216790841 passed at 60c679c;
no superseded live runs exist. Workspace/configuration have no Actions runs.

New browser/package/build batch is prepared but waits for independent review.
The initial full checks and live disk-retention/Release evidence remain valid for
unchanged backend/provider code; this follow-up verifies new presentation and exact
composed package. No new live cluster is required.

Independent inset review passed at all four final heads with no findings. All four
lane conclusions, complete history/pin consolidation and no-migration conclusion
are in inset-review.md. Fresh /root/inset_checks, GPT-6 Luna/low utility under the
same installed catalog policy, now owns the prepared related batch. No new
integration test/build was launched before review completion.

Inset verification progress: both browser engines passed; generic packaged suite
and host-package contract completed. Workspace deployment-contract tests passed
(4 runs, 19 assertions). Site-composed package Go tests passed; its Ruby suite
is still running. Watcher retains sole operation/log ownership; no timeout or
retry introduced and no unexpected local kernel build reported.

Inset batch passed: status 0, about 25m40s. Real Chromium/Firefox fixture passed
in 17.14s. Generic package/host-package contract and composed workspace flake
checks passed. Packaged Ruby suites in each composition: 405 runs/5463 assertions
(0 failures/errors, 12 existing skips), auto-archive 12/50 (no skips), host 127/994
(0 failures/errors, 3 existing skips). Host configuration built generation
2026-10-12--10-08-43 for exact cz.vpsfree/machines/aitherdev. No unexpected local
kernel build or cancellation. Parent checked actual status and bounded log evidence
after watcher completed. Full local evidence: inset-checks.log/status.

Parent launched guarded deployment once, unit
cluster-controls-inset-deploy-20261012.service, invocation
3379efe48b994cd7b6fc3ddb132d6a88, under workspace-portal-owner. Fresh
/root/inset_deployment_watch (same Luna/low policy) observes independent
inset-deploy.log/phase/status and unit state. Parent owns deployment, watcher
only observes; no retries/cancellation/diagnosis delegated. Candidate profile
evaluates to /nix/store/0yf4aajlf1jp68ab4d0llar89lf91i5x-dev-workspace-0.2.0.

Inset deployment passed: status 0, phase complete, about 3m49s. Host generation
2026-10-12--10-08-43 activated, system
/nix/store/bz16nqb4iq55kg52nc16621hgx08rkzw-nixos-system-aitherdev-26.05.20261010.6fcc160;
application /nix/store/0yf4aajlf1jp68ab4d0llar89lf91i5x-dev-workspace-0.2.0.
Two health checks passed, zero failed. Authenticated HTTP 200/TLS 0; live app.js
and style.css match reviewed source and both user services are active. Watcher
completed successfully; parent checked actual status/phase/log and both selected
generations independently after ownership returned. No operation remains running.
All four published final heads independently match local clean worktrees.

This is the completed implementation/deployment handoff to the user for the
integration decision, not another intermediate status checkpoint. Keep lifecycle
active and retain primary/rollout refs. No default integration, archive, delete or
session stop occurred. The shared-master handoff tracking commit may advance its
local tip beyond the reviewed workspace feature base; before integration, perform
the required fetch/rebase/patch-equivalence checks and comparison capture. Final
reviewed/deployed workspace source remains 86d96b26.

## Integration authorization and pre-merge phase

User instruction on 2026-10-12: "better, merge it", following the explicit
four-branch handoff. Approved set: dev-workspace, vpsfree-dev-workspace,
vpsfree-cz-configuration and workspace, each into its master branch. This covers
the reviewed cluster controls and inset Reveal deliverable, not unrelated feature
branches, archive/delete or another deployment. Clean patch-equivalent rebases
retain this approval under the Git procedure. Shared master coordination ancestry
is preserved; no unrelated working-tree or index change will be staged.

The integration phase refreshed upstreams, compared the final complete series/diff
to inset-review.md, rebased workspace onto current shared master with
patch-equivalence proof, repeated affected quick checks, captured comparisons and
fast-forwarded/pushed all four targets. Feature and rollout refs are retained.

Workspace rebase completed cleanly onto ea7d06da. range-diff confirms exact patch
equivalence, and flake.nix/lock have no differences between 86d96b26 and 0ea24610.
New workspace feature published with exact force lease; no Actions workflows on
that branch, so no superseded runs to cancel. Quick rebase checks passed: deployment
contract fixture 4 runs/19 assertions; agent instructions 8 runs/144 assertions;
real composed configuration/workspace deployment contract at runtime 60c679c.
All four final comparisons captured before integration. Fresh owned detached
integration-targets created for the three independent repositories; no shared
default checkout switched. Configuration checkout/merge uses its Nix environment
so Overcommit runs normally.

Integration target checks passed: Go web cases (0.096s) and JS syntax; provider status
2 runs/37 assertions and retained-start 2/40, no failures/errors/skips; actual
configuration-target deployment contract passed. Default pushes succeeded for
generic, extension and workspace. Configuration's first push used ambient Git;
its Overcommit pre-push loader refused absent gems, before pushing. Corrected
command uses configuration nix develop with hooks enabled. No bypass, no source
or history fix and no CI retry. This matches the earlier environment lesson.

Post-merge master Check runs: generic 38225092025 at 60c679c and extension
38225093076 at 7157c80. Fresh Luna/low /root/merge_ci_watch observed exact runs
under the installed policy; parent retained source/integration decisions. No new local long
tests: exact unchanged source heads already passed the complete suites.

All four default pushes succeeded. Fresh fetch and SSH ls-remote prove exact
feature heads on their remote master: generic 60c679c, extension 7157c80,
configuration e65ef2c4, workspace 0ea24610. No default branch was force-pushed.
Unrelated root tracked changes/index were hash-verified preserved during ff-only
merge. Temporary integration targets were removed with ordinary non-force
worktree remove; registered feature worktrees and branch refs remain retained.

All temporary integration worktrees removed non-force after successful pushes;
parent directory removed only when empty. Registered feature worktrees remain
clean. Explicit final-head checks prove all four exact final feature heads are
ancestors of fetched remote master.

Both exact post-merge Check workflows completed successfully:
[runtime 38225092025](https://github.com/aither64/dev-workspace/actions/runs/38225092025)
at 60c679c52c263a0fc7a4b08c5f83a291cfd89191 (12m00s) and
[extension 38225093076](https://github.com/vpsfreecz/dev-workspace/actions/runs/38225093076)
at 7157c8098dcf60127aa4df823fab82b4185ad22a (15m16s). Watcher completed;
parent checked its exact-head results. No retry, cancellation, failure or running
job remains. Configuration/workspace have no Actions workflows; their exact
composed checks and deployment passed before integration. No additional deployment
is needed for the workspace's patch-equivalent coordination rebase.

Final integration handoff records the approved scope, exact heads, comparison and
remote ancestry proofs, cleanup and CI. No technical blocker or required work
remains. Feature documentation already matches the deployed behavior; integration
adds no behavior requiring another project documentation change.
