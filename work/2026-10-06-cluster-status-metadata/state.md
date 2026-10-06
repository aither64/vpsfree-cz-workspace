---
lifecycle: active
---

# Cluster status metadata fix

Phase: application activation, awaiting archive recovery direction. The reviewed
runtime and both
matching pins are committed and published. Full runtime and composed Nix checks
and the aitherdev build passed. Initial CI failed in an unchanged archive test;
the installed baseline reproduces the same race. New exact-head CI passed.
aitherdev deployment passed, exit 0, including dry activation and both health
checks. Original authorized archive recovery completed successfully, and both
temporarily removed fix worktrees were restored at unchanged heads. Three new
unfinished archive operations prevent application activation; requested user
direction for their exact sessions. Profile switch/live verification and merges
remain outstanding.

## Phase checklist

- [x] Investigate helper, decoder, current runtime, and live portal.
- [x] Agree existing-card scope and deployment/integration authorization.
- [x] Implement, document, and complete focused checks.
- [x] Commit and independently review the complete branch.
- [x] Verify composed pins, package checks, and CI.
- [x] Deploy aitherdev and pass both health checks.
- [ ] Switch workspace user profile and verify the live card.
- [ ] Merge exact verified feature heads into remote master branches.

## Ownership and scope

`dev-session current` reported no session and both session environment variables
were absent. Created this separate initiative with the supported
`dev-session start ... --as-is --no-codex --no-attach --json` command; no roster
or second conversation was invented. Lead owns design and application edits;
catalog-policy standalone review and fresh utility watchers will be used.
The small decoder unit uses this lead-owned plan as its bounded design brief.
Preserve all unrelated shared-master/index changes and the storage session.

Owned worktrees use worktrees/2026-10-06-cluster-status-metadata/ for dev-workspace,
workspace, and vpsfree-cz-configuration. Their portal registrations record exact
bases. Configuration checkout hook initially failed because its ambient Bundler
could not load pinned gems; the worktree was created and remains owned. Hook
setup/registration was repaired inside its Nix environment: overcommit install,
trusted pre-commit signatures, and normal worktree-add retry all passed without
bypass. Existing worktree checkout-hook guidance explains the failure.

Review packet: [review-packet.md](review-packet.md). Runtime changes comprise
one coherent commit and three files, 195 additions/5 deletions; no migrations.
Standalone reviewer uses installed default reviewer gpt-6.1-sol/xhigh/read_only,
digest3343a06cbc8d3c181df52770086fb807894f9990132bb0792048e0ddabb764f8.
The missing root roster is expected for this no-Codex initiative, so no team
members or model overrides were invented. All four review lanes apply.
Final report: [review-result.md](review-result.md); no findings, no obsolete
branch history, explicitly no migrations. Long verification now authorized.

## Composition and verification progress

Runtime e3315a4 is published on the feature branch. Workspace a296f66f and
configuration 165e465a pin that exact runtime; both feature refs are published.
Their semantic diffs change only the respective runtime node, preserving the
extension revision, siblings and follows. Deployment-contract checker passed.
The same independent reviewer assessed both complete companion branch histories
and pins with no findings, no obsolete history, explicitly no migrations.
See [composition-inventory.md](composition-inventory.md).

Initial long-check launcher failed before running Nix because the parent joined
the clean-tree test and Nix command on one line. Corrected the missing newline
and checked script syntax; runtime source stayed unchanged. First log/exit are
retained. Runtime-checks2 completed successfully in about 10m20s; all Nix checks
passed, including host smoke tests. Ruby reported no failures/errors and twelve
skips. Its local log contains only the completion summary, not the full streamed
output. GitHub Check run 37510298035 failed in the archive-retry test; the
feature host job was skipped as configured. A separate fresh site-policy
Luna/low watcher completed composed checks/build, exit 0, in about eleven
minutes. Both complete Nix check operations passed. Candidate composed package:
/nix/store/b2q12p1725bqrb4nrd6yfjg28hgsggcf-dev-workspace-0.2.0.
Confctl built aitherdev generation 2026-10-06--20-46-15. Full composed output is
retained in composed-checks.log.

Failure investigation: [ci-investigation.md](ci-investigation.md). The exact
archive test failed 7/100 times on the feature and 20/100 times on the installed
baseline 4c3ea2e. Its code and all portal/internal/web files are identical across
those revisions. The full failed CI log is retained. The one-shot assertion
races the background display reconciler's compare-and-swap receipt update;
execution still revalidates journal identity after acquiring the mutation lock.
This is an existing failure outside the cluster-decoder patch. A rerun may
verify this patch, but does not resolve or certify the archive-test race.

The one authorized API rerun was refused: Resource not accessible by personal
access token. No second attempt was created. Published an owned verification
branch 2026-10-06-cluster-status-metadata-ci over SSH at the unchanged reviewed
runtime head to trigger normal push CI. Fresh Luna/low watcher observes exact
Check run 37514351752. Keep this auxiliary branch; no empty/source commit was
introduced.

That new exact-head run passed (fast job, about eleven minutes). Feature host
job was skipped as configured; the full local runtime flake check had already
passed its host smoke test. Final workspace head ef529ec8 is a clean rebase of
a296f66f onto shared master f8b7271d; range-diff reports the identical sole pin
patch. The inherited agent-instructions check passed and the composed package
output remained exactly b2q12p1725bqrb4nrd6yfjg28hgsggcf. Repeated deployment
contract validation passed. Original review/integration authorization still
applies. Runtime/configuration comparisons are captured before integration.

## Archive recovery and application activation

Read-only inventory found unfinished archive+cleanup journals for
2026-09-18-codex-web-portal-waiting (tracking_committed) and
2026-10-02-codex-package-portal-settings (clusters_released). The supported
workspace-host switch refuses all unfinished lifecycle operations. These
journals were not created or mutated by this fix initiative. Requested explicit
user direction to resume their existing archives or let their current owner
recover them. The user authorized "Resume the existing archive operations".
October 2 was already fully recovered by another operator before our retry.
The ordinary installed September 18 archive retry was confirmed and exited 1:
"archive worktree path or registration remains after removal". Read-only proof
shows the old checkout paths and registrations are absent. Git reused sealed
admin names dev-workspace4 and workspace2 for this fix's new clean worktrees,
with different inode identities and gitdir pointers to this initiative. After
the build finished, removed only those two clean owned worktrees with ordinary
non-force git worktree remove and retried the installed archive. It has reported
thread retired, runtime retired and archived, then exited 0 and cleared both
receipts. Restored the two fix worktrees through dev-session worktree add
--as-is --no-fetch at exact unchanged heads e3315a4 and a296f66f. The normal
installed executor and retained proofs remained in use. Reusable diagnosis is
in notes/dev-workspace/2026-10-06-archive-git-admin-name-reuse.md.
Do not alter journal/sidecar evidence or another initiative's live worktrees.

Host deployment ran in named user unit dev-cluster-status-host-deploy.service,
invocation 26c5dfb3f8d244eebd1095fa014f5ee8. Confctl dry activation and switch
completed in 109 seconds, exit 0; both health checks passed (system running and
firewall active). Selected system is now
/nix/store/4q2w8x1h0aavywk3qc031wnzr466zd9m-nixos-system-aitherdev-26.05.20261006.b253099.
Full output: host-deploy.log. The observer has finished; no deployment process
remains. Application profile remains the old h73nvgmd... package.

Three additional archive+cleanup journals now exist at clusters_released:
2026-10-02-portal-creation-performance, 2026-10-04-session-modes-review-timing,
and 2026-10-04-upload-display-limits. No corresponding archive CLI process is
running, and none of their removed administration names collides with an owned
fix worktree. Requested explicit user direction to resume these exact existing
archives or leave recovery with their owner. That answer is pending. They are
outside the earlier two-session approval. Application switch has not run;
ordinary preflight must remain intact. Live verification script is syntax checked
and will persist safe projections only. Integration target worktrees are prepared
under this initiative's integration-targets directory; defaults remain unmerged.

## Evidence

Installed runtime source: 4c3ea2eb3b82b572e86f23ec7f9e53a0f1dc6a0c.
Selected extension: 0ff827df13e82dfab4b536ff29979280f264e8f5.
Helper status exited zero: schema 2, running, ready true, storage topology,
bridge network, ten services, four commands. WebUI source is worktree revision
aa2f60b89df65d2f987be48784ed42bab7010833, clean. Maintenance version 2 is
released/pending false/copied true/active true. Only safe projections were
printed; credentials were never logged.
Read-only portal request reproduced unknown field webuiSource. Decoder also
lacks maintenance, so both metadata objects must be accepted together.

## Integration and deployment approval

User: "you can deploy aitherdev using vpsfree-cz-configuration and merge the fix
into the default branches when it is verified." Accepted plan identifies
dev-workspace/master, coordination workspace/master, and
vpsfree-cz-configuration/master. No separate approval remains for that scope.
Deployment only selects cz.vpsfree/machines/aitherdev and the workspace user
profile. No cluster reset or guest mutation is authorized or needed.
