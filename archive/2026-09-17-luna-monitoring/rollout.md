# Rollout record

## Prepared
- Generic skill revision: 8c6f7025fc3c86b02b602dbd1f478c3a6de460f3.
- Extension revision: 4ffe714 (full revision in review-packet.md).
- Workspace revision: 0820a61bf202eb5ec41a4e406fe4f77cd9de177b.
- Configuration revision: 37dc56ee72600cbe21fd9e9a42442741cf117c09.
- Existing profile: /nix/store/mk716d08x840l2wdlc1mbaqpnhabn30f-dev-workspace-0.2.0.
- Application activation: workspace-host switch --source the workspace worktree.
- Host activation: reviewed feature configuration for cz.vpsfree/machines/aitherdev,
  after build and dry-activate. Configuration branch remains unmerged.
- Generic host-module and host-path sources are unchanged by this initiative.
  No Codex version or protocol change, migration or node update is introduced.

## Recovery
Use workspace-host rollback for the preceding user profile and restore the
matching workspace policy/pin if reverting the feature. Retained generations
manage skill links. Host input alignment uses the recorded previous configuration
revision; host module behavior is unchanged. Preserve concurrent sessions and
obey normal activation guards; never interrupt unrelated work to activate.

## Execution
Package and host builds delegated to separate fresh Luna/low watchers after all
four mandatory Astra/xhigh lanes passed. Activation and live discovery completed.

Host build passed at generation 2026-09-17--11-09-33 (131 seconds, 78/78
steps). confctl deploy --yes --generation 2026-09-17--11-09-33
cz.vpsfree/machines/aitherdev dry-activate passed. Explicit switch of that same
generation passed; see host-dry-activate.log and host-deploy.log.
All 47 portal manifests validated before deployment.

Host switch succeeded with both systemd and firewall health checks passing.
Application build passed in 216 seconds; same packaged 77 runs / 475 assertions
with 0 failures, 0 errors, 3 skips. Output/activated profile:
/nix/store/nh6p0ccmhgx853nxdzbqsrjqgw59hh04-dev-workspace-0.2.0.
workspace-host switch succeeded; Codex 0.154.0 protocol check passed.
Skill link resolves to the reviewed source in the Nix store. App Server
skills/list forceReload discovers exactly one enabled dev-session-monitor and
reports no skill errors. No deferred activation was reported.

Workspace policy/pin is integrated at 0820a61 on remote master. Generic,
extension and configuration feature branches remain published and unmerged.
All feature comparisons have been captured for portal review.

Live ordinary-request delegation, parent continuation, synthetic failure,
delegation-disabled fallback and caller-directed escalation passed; details in
[verification.md](verification.md). The parent retained Astra/xhigh and the
watcher actually ran Luna/low with fresh context. Router and vpsfree-cz portal
services were active after activation. User-profile generation is 50. No CI
wait, configuration default-branch merge or session closure was performed.

## Integration after deployment

The user subsequently authorized all default-branch merges. Generic, extension
and workspace commits are integrated unchanged. Configuration patch `37dc56ee`
was rebased without patch changes to `52175f81` on current upstream and integrated.
The deployed generation above is unchanged; newer unrelated configuration
dependencies were not deployed by this integration. See integration.json.
