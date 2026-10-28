# Archive watcher fix rollout

## Current candidates and authorization

User authorized implementation, aitherdev deployment and original archive
recovery. User subsequently approved "merge and release aitherdev"; integration and release are complete. Both system and application deployments are complete and verified; the original
archive retry completed successfully. See execution results below. Original candidate/build history is
in rollout-before-refresh.md and must not be executed.

- Runtime 76c9ad4fbd877992464d2a7f2a1a2fe60db043b1, based on 2caa9419.
- Workspace 2c163abe58b0981b83f7ca9c23a55041f7723751, based on c4c6c95a7.
- Configuration 7c999104833e8cf2dd8ac779a9e8e51876fb7d85, based on e2a69b9c.
- Previous selected app: /nix/store/cfgd3aqs0s6ahgavyx17m1pc3rnnwww2-dev-workspace-0.2.0.
- Live and system profile: /nix/store/zyz7pvg8mzq1aiifhxpg6yhl7nknph4j-nixos-system-aitherdev-26.05.20261026.718f670.
- Native PID156049, portal PID3254866, both active; /healthz OK before refresh.

Original claim 0863838f-bef9-4fe0-8a5e-f6db26a4a1b5 was released unused after
the live application advanced. Do not reuse it. Fresh prepared request:
machine-claim-refreshed.json, UUID02a481db-1b51-436f-8c10-280afc633029.

## Sequence

Refreshed review accepted with no blockers; advisory stale rollout instructions
resolved by this rewrite. Complete the fresh composed/system builds and
CI40750004866 (including archive VM). Keep derivation/output receipts. Copy the
new exact confctl generation, then acquire fresh request and prove held status.
Recheck live package, source heads and default branches before activation.

Lead launches exact-generation confctl deploy with --yes --dry-activate-first
--no-reboot; preserve auto-rollback/health checks. Verify both live and system
profile paths, then guarded workspace-host switch --source at the absolute
workspace worktree, with both DEV_SESSION variables and DEV_WORKSPACE_CLAIM_ID.
Fresh utility observes independent service/log status; it never deploys.

Verify selected path, portal health, native PID/continuity and normal availability.
Perform a dedicated threadless disposable session archive/revive/rearchive test
using ordinary lifecycle commands and keep its retained archive. No source or
foreign sessions are fixtures. Then recover the original archive below.

## Original archive recovery

Target: 2026-10-28-observer-progress-guidance, failed attempt1, target still active.
Receipt8ef38791646bb344d6d0880a414e7c9b88f44d72a4f12831ef52ebb06cfc18c7;
journal eee092a6346cbc1e5e2def280080477fc0528fc837eec3a382b0489aa33fb004;
target d0b4d31d8b3e9638ceb9e2d5c5c64a56ca96edfc0a5cdf5da7fb80b27b3a2ae9;
root01a181a7-2ddc-7852-a8c7-56c27709c461. Re-read current identities.
POST /api/sessions/SLUG/operation/retry through the portal Unix socket with
current receiptId and journalId plus canonical Origin. Do not edit receipts
or replace the original operation. Observe its independent systemd worker;
verify complete receipt, archived tracking, removed owned worktrees, retained
branches and conversation. Check tracking-sync status independently.

## Recovery and retention

Keep previous outputs/roots and journal evidence. Package recovery is forward-only
through ordinary workspace-host; never bypass lifecycle/capability checks or
force a native restart. Keep the deployed machine held until effects are verified
and complete deployed lineage is integrated under separately approved master
integration. Do not archive this implementation initiative.

## Verified activation candidate

All refreshed builds and CI40750004866 passed. Application kdqm98kwk1mly4i1rfx58lnz6cscn6z6;
system l18arwf42sxzwf864yjwsvnjma5m5cav, generation2026-10-28--20-16-19.
Copy-only exit0. Remote baselines and live predecessor rechecked unchanged
immediately before acquiring the refreshed claim.

System activation completed with confctl exit0, both live/system profiles at
l18arwf42sxzwf864yjwsvnjma5m5cav, and both configured health checks passed.
Native PID156049 and portal PID3254866 remained active. The systemd-run waiting
client lost its D-Bus connection during activation; the independent unit and
atomic status prove success, so no deployment was repeated. Evidence:
verification/deploy-system.log and deploy-system.status; unit
archive-native-watchers-system-20261028.service Result=success, ExecMainStatus=0.
Claim02a481db-1b51-436f-8c10-280afc633029 remains held.

Lead launched guarded profile switch in independent unit
archive-native-watchers-profile-20261028.service using exact source and claim.
Fresh watcher launch was unavailable in this tool context; parent visibly uses
bounded independent unit/status monitoring under dev-session-monitor fallback.

Profile switch completed exit0; unit Result=success, ExecMainStatus=0. Selected
application is kdqm98kwk1mly4i1rfx58lnz6cscn6z6, portal PID1075392, native
PID156049 unchanged, /healthz OK. Dedicated threadless archive/revive smoke
fixture uses sensitive local tracking to avoid shared Git bookkeeping. Its first
archive refused because root Markdown-negation rules override info/exclude;
added only this owned fixture's exclusion to existing work/.gitignore and
archive/.gitignore, preserving previous entries. git check-ignore proves the
fixture directory and Markdown now excluded. Retry passed preflight and entered
ordinary archive. No private fixture content will be committed.

## Final execution result

Application kdqm98kwk1mly4i1rfx58lnz6cscn6z6 and system
l18arwf42sxzwf864yjwsvnjma5m5cav are selected; all activation commands exited0.
Health checks and /healthz pass. Native PID156049 preserved, portal PID1075392.
Disposable selected-package archive/revive/rearchive passed.

Original archive attempt2 completed2026-10-28T19:30:07Z, worker exit0.
Tracking-sync synced at19:30:20Z (commit5890b00b7). Original tracking and
worktree group removed, archive tracking present, original conversation ID and
all three finalized branch heads retained. Evidence:
verification/original-archive-final.json and original-tracking-sync.json.

No deployment/verification commands remain active. Deployment units were stopped
after their terminal success was verified. Claim02a481db-1b51-436f-8c10-280afc633029
remains held because deployed feature lineage is not yet integrated. Obtain
explicit dev-workspace/master, workspace/master and configuration/master approval
before integration; then satisfy retention proof and release.

## Integration and machine release

Approved master merges published: runtime76c9ad4f, configuration7c999104 and
workspace9d35428a. Workspace was rebased only over archive tracking; same
independent reviewer proved the deployed2c163abe and final9d35428a source/input
equivalence and identical package/contracts derivations. No redeployment needed.
Fresh remote ancestry and live health/path checks passed. Machine claim
02a481db-1b51-436f-8c10-280afc633029 released2026-10-28T19:40:04Z and verified
released. No reservation or deployment command remains owned. Automatic
master CI40756067530 is monitored independently after release.
