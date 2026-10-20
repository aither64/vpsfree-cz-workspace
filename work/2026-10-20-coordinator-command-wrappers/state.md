---
lifecycle: active
---

# Logged coordination commands

Phase: authorized aitherdev rollout preparation; runtime implementation is
published and locally verified. Default-branch integration is not authorized.
User authorized aitherdev deployment and verification through
vpsfree-cz-configuration, including matching runtime/profile selection.

- [x] Investigate merge preparation and agree the simpler design.
- [x] Implement logged commands, explicit reservations and legacy coexistence.
- [x] Complete quick checks and independent review; reconcile findings.
- [x] Pass signed Overcommit, actual systemd and profile recovery fixtures.
- [x] Publish both feature branches and save exact comparisons.
- [x] Complete final package build.
- [ ] Complete GitHub CI.
- [x] Receive explicit aitherdev deployment direction.
- [ ] Prepare/review matching pins, owned admission and exact build artifacts.
- [ ] Deploy system and application profile; verify operation.
- [ ] Await explicit default-branch integration direction.

## Identity and branches

External threadless initiative created with dev-session start --no-attach --no-codex:
2026-10-20-coordinator-command-wrappers in /home/aither/workspace/ai/vpsfree.cz.
Both DEV_SESSION identity variables and dev-session current were verified.
No retained team/native lead exists; the lead owns application edits and uses
installed standalone review/utility policy. No team has been invented or changed.
Initial tracking plan/state were committed as 7330469e before project-code commits.

Both branches: 2026-10-20-coordinator-command-wrappers, published over SSH.

| Repository | Base | Final head |
| --- | --- | --- |
| dev-workspace | 74ff349efc9238922a63a47af815504c305c9838 | f7ebc3e151cd52d1e45c22adb8da7b9fc1940e18 |
| workspace | 9439f4c5569997f465e51be2fb9459e4afd3e304 | 5e6c5aa411af16e2d81a5e3440c09c35b1884b10 |

Dedicated worktrees: worktrees/2026-10-20-coordinator-command-wrappers/dev-workspace
and worktrees/2026-10-20-coordinator-command-wrappers/workspace. Preserve unrelated
shared checkout/index changes. Each branch has one coherent feature commit;
there are no migrations, intermediate state schemas or dependency-update streams.
The new command schema 1 is additive; original ledgers and recovery formats remain.
Nothing from this initiative is merged, deployed, selected or externally consumed.
Deployment preparation adds workspace pin commit 28a524a4 and configuration
worktree worktrees/2026-10-20-coordinator-command-wrappers/vpsfree-cz-configuration:
base b748fb08c3f5aac12b302414cc45936f663d1cbd, head 029cf654 (exact full
heads will be retained in the rollout inventory). Both select runtime f7ebc3e.
Configuration's channel update used confctl and passed its ordinary hooks.
The composed deployment contract checker passed; extension/sibling pins are intact.
The selected stable command was rechecked after publication and resolves to
/nix/store/mdqyfwclfbjp43akmagd1r5qidfdpiny-dev-workspace-0.2.0/bin/dev-session;
other work changed selection concurrently. This initiative has not selected its
newly built candidate.

## Result and documentation

New work uses logged session-supplied commands and optional explicit machine
reservations. Sessions own commands, hooks/signing, environments, merges,
deployments and effect verification. The coordinator owns exclusion, process
results, bounded logs and notifications. Normal nonzero exits release locks;
interruption retains exclusion until inspection and explicit owner resolution.
New commands create no feature/target copies or hook dependency payloads.
Retained snapshots, jobs, integration journals and uncertain recovery retain their
original contracts. No initiating-session recovery or other-session cleanup ran.

Owning runtime guides: docs/coordination.md, coordination-operations.md,
coordination-legacy.md and integration.md. The legacy guide preserves the original
text, and packaging now installs the integration guide previously missing from the
observed package. Workspace AGENTS.md and Git/deployment/verification procedures
adopt wrappers while retaining approval and review gates. See plan.md/design.md.

## Review and verification

See [independent review](review-result.md), [verification evidence](verification.md)
and the two final-inventory.txt files. Review packet retains original exact ranges.
Standalone /root/final_command_review used gpt-6-astra/xhigh from installed default
lead_reviewed/reviewer, catalog digest
ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376.
All four lanes covered this high-risk persisted-state/package/lifecycle change.
Reviewer concluded coherent complete history, no repeated updates and no migrations.

Important retained-job approval recovery and advisory foreign-reservation visibility
findings were fixed and directly verified. Narrow remediations introduced no new
contract and do not require a reviewer rerun. Later changes improve fixture setup
and coverage only. Both upstream rebases were clean and range-diff equivalent;
current inventories record deltas from the reviewed commits. No obsolete fixups
remain in either published series.

Quick command suite: 22 tests / 89 assertions; browser coordination: 14 tests;
selected original host/coordination: 8/60 and 19/142; affected Go policy packages
passed. Added profile forward recovery: 1/14; retained profile recovery: 1/12;
background CLI admission: 1/13. Actual systemd survival, interruption and latency:
3/22. Signed Overcommit 0.73.0: 1/33, including ordinary checkout/merge/push hooks,
a failing pre-push hook and explicit successful retry. Git post-merge can return
zero on hook failure; the wrapper reports process status and leaves verification
to the session. No source payloads appeared in the new path.

The full packaged Ruby aggregate passed with complete unique shard coverage:
851 cases / 9,630 assertions, no failures/errors, 16 declared environment-dependent
skips. Final package build (including Go/browser checks), host contracts/module and
source-filter checks passed in 432.3 seconds. Candidate:
/nix/store/ay9ac0azmkhn4jgjzharafk8nvxcf6n6-dev-workspace-0.2.0, built only.
CI remains in progress. Runtime GitHub Check run 39452948198 at the exact final head:
https://github.com/aither64/dev-workspace/actions/runs/39452948198
Workspace-instruction repository has no CI runs configured for its branch.

Five no-op systemd commands had median 0.490 seconds (range 0.467 to 0.554), with
14,079 bytes of regular records/logs and no source payload directory. This measures
wrapper overhead, not production merge time or project hook/dependency costs.

## Evidence, monitoring and cleanup

Initial long checks used fresh installed-policy Luna/low/full-access utilities.
Fresh utility launch subsequently became unavailable in the current tool interface;
the lead visibly used the monitoring skill's bounded parent fallback. Final local
handle 82633 exited zero; parent retains handle 50247 for the exact-head CI watch.

Earlier failed attempts were diagnosed before reruns: systemd fixture basename
started the real CLI too early; plugin signatures needed explicit generated-content
signing; isolated gem setup needed Nix's Minitest path; two legacy test doubles
needed their environment/package identity. These were fixture setup failures.
Complete prior evidence is retained under attempt1 through attempt4, plus quick logs.
Reusable lesson: notes/dev-workspace/2026-10-20-loaded-host-fixture-entrypoint.md.

All integration repositories/state, generated signatures, transient units and gem
homes are disposable and initiative-owned. Fixtures tear down their own repositories
and units; the integration runner removes its temporary GEM_HOME on completion.
Do not touch existing sessions' trust, worktrees, operations or payloads. Read-only
planning accounting found about 69 GiB coordinator sources and 5.1 GiB integration
scratch; no reclaimability was established and none was cleaned.

The selected predecessor requires a managed conversation for ordinary deployment
admission; initial bootstrap refuses this nonempty historical ledger. Use the
ordinary retained-tracking conversation creation route for this own initiative,
without a team selection or added members. Preserve its branches/tracking. An
empty owned terminal may be restarted as required by that supported conversion;
the external lead continues implementation and supervises deployment.

Next: complete composition review and CI, build/copy exact artifacts and activate
through the selected coordinator's owned machine reservation and jobs. Verify
system/profile identities, service health and new command behavior. Master merges
remain subject to separate explicit approval.
Keep this initiative active and retain branches; do not archive or delete it.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-coordinator-command-wrappers/
