# Aitherdev archive-readiness rollout

Status: deployed, verified and integrated; aitherdev claim released. Post-merge CI being observed.


## Authorized aitherdev rollout (2026-10-25)

User direction: "deploy aitherdev using vpsfree-cz-configuration". Deploy the
reviewed/published runtime b974f2f3f83792a494610d1ea03f3d69e97bc1a4 without
integrating any feature into master. Extend scope to initiative-owned configuration
and workspace-composition worktrees. Preserve shared master checkouts and all
unrelated files. Exact runtime selection uses configuration channel dev-workspace /
role devWorkspace and the workspace direct nested override; retain extension and
other inputs. Build final committed artifacts before ownership, then acquire
vpsfree:aitherdev and dry-activate/switch system before the ordinary workspace-host
profile switch with the held claim and exact session identity. Use the installed claims workflow and the current configuration site guide
docs/operations/codex-providers-aitherdev.md for ordinary confctl deployment.

Verify exact system/profile identities, contract, portal/router health,
conversation continuity and a disposable creation/archive acceptance. Use normal
forward profile recovery for interruptions, retain original journals, never
reboot or force release. Keep the machine claim while deployed feature lineage
remains unintegrated. No new database/state migrations are introduced by pinning.
Individual rollout evidence lives in rollout.md; source behavior remains in
runtime docs. Readers: operator continuing deployment/recovery and merge reviewer.

## Prepared source and baseline

- Runtime: b974f2f3f83792a494610d1ea03f3d69e97bc1a4, full CI 40223710351 passed.
- Configuration: 6428e280f06bffabef829a1335b36bac6cad5b9d over b167cd4388a5c94ff3f978df85b6800fafd1b8af.
- Workspace: ffadbf5b98adfc960ac61b558a051be005941e5e over a6ebab6b10a8d0806f4db9588e1433b568473990.
- Extension unchanged: 767dfd587e346168e1443e65ccdb67ce748f3fe3.
- Configuration input update generated through confctl; declared hooks passed.
  Checkout creation initially reported missing Gemfile dependencies from the
  shared hook. Nix development shell populated ignored checkout-local .gems;
  bundle install, overcommit install/sign completed before the first commit.
- Workspace direct nested lock generated through nix flake update. No declared
  workspace hook framework. Deployment contract and 4 tests / 19 assertions pass.
- Both downstream branches published through SSH; comparison snapshots retained.
- Predecessor system running/profile both:
  /nix/store/1bnl145ln79094l10j60cp4631a69vww-nixos-system-aitherdev-26.05.20261021.da6dc0e.
- Predecessor workspace profile generation 189:
  /nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0.
- Initial authoritative coordination status has no claims, reservations or jobs.
- Related final downstream rollout review resumed the same independent native
  reviewer 01a17467-084f-7932-b2f0-cf4352265c1e; actual launch confirmed
  gpt-6.1-sol/xhigh, approval never, danger-full-access. No source changes since
  its earlier review. No default-branch integration authorized.

## Final downstream review

Related independent reviewer reported no Blocking or Important findings.
Advisory corrected: use configuration docs/operations/codex-providers-aitherdev.md
at the exact prepared feature revision; the shared configuration checkout has
older site guidance. Current site guide agrees with ordinary claims/confctl and
system-first ordering. Source/extension/native versions unchanged apart from
reviewed runtime. Complete downstream history accepted: one focused pin per
repository, no obsolete updates, no repeated streams and no migrations.
Report: deployment-review.md. Exact native identity/settings retained above.

## Pre-activation checks

- Current site instructions read from prepared configuration worktree:
  docs/operations/codex-providers-aitherdev.md and AGENTS.md. Routine channel
  updates need no separate repository documentation or release receipt commit.
- Live SSH proof succeeds through configured target 172.16.106.40, with host-key
  checking retained. An initial diagnostic using the DNS alias refused because
  that alias is absent from known_hosts; no host key or SSH policy was changed.
- Router returned HTTP 200 before deployment.
- Pre-switch Codex service PID: 3387667; tmux service PID: 435397; both active.
  Live switch policy preserves these because the native invocation is unchanged;
  portal/router are expected to restart. Actual post-switch identity must prove it.
- Global status (not just session-filtered status) confirms no active claim,
  reservation or operation before build preparation. Recheck on acquisition.
- Fresh build watcher /root/deployment_build_watch uses installed Luna/low policy
  for the exact build-deployment.py batch. Parent owns activation and acceptance.
  Build outputs are rooted temporarily at /tmp/archive-unmanaged-files-deployment-build.

Build watcher native thread 01a1748f-1339-7191-9c3c-9ab25d029a21: actual
turn_context verifies gpt-6-luna/low, approval never, danger-full-access.
Both downstream worktrees remain clean at their reviewed heads.

System build succeeded in 112.9 seconds. Prepared generation:
2026-10-25--20-35-34, toplevel
/nix/store/g4kzll8pjprkwqrxk30crrksdxhimwwz-nixos-system-aitherdev-26.05.20261021.da6dc0e.
Retained auto-rollback helper:
/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb.
Metadata binds devWorkspace b974f2f3; nixpkgs da6dc0e7, llm-agents e85b9921
and home-manager c47b2cc6 remain unchanged. Parent copy-only deployment of this
exact generation returned success. No activation or claim acquired yet.

## Activation admitted

Both artifact builds passed (672.5 seconds total; workspace 559.7 seconds).
Composed package: /nix/store/bhi44p5ifayn90b8bnm1g5srdga46yn1-dev-workspace-0.2.0.
Deployment-contract output: /nix/store/x2ncq1fsb1n6yf1485xwzsqj27492gda-dev-workspace-deployment-contract-tests.
Installed workspace-host prepare completed protocol/semantic/native and retained
state/registration compatibility checks before ownership; its saved artifact
binds the exact candidate. Native Codex remains 0.163.0.

Acquired held machine claim c557c8ab-f8ff-454e-8f8c-683bec74ef37, owner
d9056db0-2d6a-463d-ba75-ef6622366976, resources machine:vpsfree:aitherdev.
Request is saved in deployment-claim-request.json. Parent-owned activation driver
rechecks exact clean heads, baseline system identities and held claim; confctl
uses the copied generation with dry-activate-first, no reboot and configured
auto-rollback. It proves both system identities before the ordinary claimed
workspace profile switch. Original results/logs retain any uncertain effects.

Activation driver is independently supervised by transient user unit
archive-readiness-rollout-20261025.service (invocation
4eb6e641c3a846218fe30b371b88f195). Initial unit submission refused because
/run/current-system/sw/bin/python3 is not installed; no command began. Resubmitted
once using the already running Python interpreter's real immutable executable,
/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin/python3.13.
Fresh watcher /root/deployment_activation_watch observes the existing unit and
result artifacts only; it cannot deploy/retry or change ownership.

## Activation and initial live acceptance

Activation completed successfully in 130.4 seconds. System dry activation/switch
and workspace profile switch both returned 0. Both live/system profile identities
select g4kzll8p; workspace profile selects bhi44p5i. Confctl's systemd and firewall
health checks both passed, with auto-rollback retained and no reboot.

Portal health, index, operations, initiative page and original HaveAPI archived
page all return HTTP 200 through the router. Codex PID 3387667 and tmux PID 435397
are unchanged and active. Portal/router/coordinator are active. Saved provider
selection remains openai; per-session provider selections were preserved.
The naming child uses the selected package's immutable catalog. A real isolated
Luna/low call returned {"name":"verify-archive-readiness"} in 2139ms, within its
10-second budget. No persistent conversation or model tools were created.

Created only disposable threadless session
2026-10-25-archive-deploy-smoke-2ec8f598 for final archive acceptance. Initial
selected-package archive-check passes all 6 checks with zero blockers. A fresh
verification watcher will run the confined marker/readiness/portal archive test;
no unrelated session is an acceptance target. Earlier start syntax combining
--as-is and --new refused before creating state; the exact unused full slug was
then started with --as-is, --no-codex, --no-attach.

## Final disposable archive acceptance

Passed in 100.0 seconds on the selected deployed package. The fixture's initial
readiness check passed all 6 checks. Its known executable marker outside any
checkout produced exactly one unmanaged_entry blocker. Readiness left its owned
terminal and tracking intact; Operations still returned HTTP 200. The test removed
only its exact known marker, then all 6 checks passed again. Portal Archive
returned HTTP 202 and completed on attempt 1. Terminal retirement occurred only
after archival, work/ tracking moved to archive/, and no fixture worktree group
remained. Receipt 74d27cec698d9a6505644b0cd241e76863ffb94d432f5d30cd4e9c335b54376b.
The terminal state was complete with asynchronous tracking sync initially pending.
The actual lead-assisted cleanup/restart path remains covered by final-head
packaged CI; this live fixture intentionally has no lead or repositories.

Evidence: deployment-archive-watcher.md, deployment-archive-smoke-result.json,
deployment-smoke-blocked.json, deployment-smoke-ready-after.json. Native standalone
watcher 01a174a2-1847-7951-ab2e-15cce3f395ac used the exact installed utility TOML;
actual model/effort/access/approval confirmed by parent. Activation watcher
01a1749c-1754-7fb0-86ef-3c3e8a20544d was independently confirmed the same way.
All watcher-owned commands finished; no verification guest was started.
Temporary /tmp build links removed after proving the selected profile. Retained
preparation roots and the selected package remain under normal runtime retention.

## Retention and next action

Deployment and live acceptance are complete. No master integration was performed
or authorized. Machine claim c557c8ab-f8ff-454e-8f8c-683bec74ef37 remains held by
this initiative because deployed runtime/configuration/workspace feature lineage
is unintegrated. Following explicit integration direction and normal verification,
prove the complete deployed lineage integrated, release this exact owned machine
claim and verify release. No additional deployment is needed for these unchanged
heads. Do not archive or stop this initiative as part of handoff.

Final fixture tracking-sync status: synced, empty error, verified through the
ordinary status command. No manual receipt/journal/state edits or forced sync.

User subsequently directed "merge and release". Integration/release is now
authorized for the three reviewed master targets, subject to fresh source,
claim, live-effect and deployed-lineage proofs. No lifecycle closure is requested.

## Integration and machine release completed

User direction: "merge and release". Three independent fast-forward integrations
were pushed and verified over SSH, each under a short single-repository claim:

- dev-workspace/master b974f2f3f83792a494610d1ea03f3d69e97bc1a4.
- vpsfree-cz-configuration/master 6428e280f06bffabef829a1335b36bac6cad5b9d.
- workspace/master 9c4c97cd1d49232cb930ff5037ae124295f04f0f.

Workspace rebase originally deployed ffadbf5b over only tracking/notes baseline
changes to fe4f9ff1, then reproduced the one reviewed pin as 9c4c97cd. Installed
Certification.prove returned reconstructed_patch with exact matching final tree;
range-diff matches, changed paths only flake.nix/flake.lock, no migrations.
Original review receipt and exact deployed ref retained. Quick contract tests
passed 4 tests/19 assertions again. Selected application remains the tested
original artifact, with no claim of identical new composition derivation.

Workspace shared-master integration also held dev-session-tracking.lock without
waiting. It preserved hashes of unrelated working diff, staged diff and untracked
names. All short repository claims released after exact remote proof, before
records/cleanup/CI. Temporary detached integration worktrees removed cleanly;
registered feature worktrees and branches retained.

Fresh remote ancestry proved runtime/configuration/final workspace and unchanged
extension 767dfd58 and codex-web 8b60554b integrated. System links, selected profile,
portal HTTP 200, active services, completed activation/acceptance and absence of
owned unsettled jobs were rechecked. Ordinary release confirmed aitherdev claim
c557c8ab-f8ff-454e-8f8c-683bec74ef37 released for owner d9056db0-2d6a-463d-ba75-ef6622366976.
Evidence is the normal release command status plus integrated-deployed-lineage.json;
no custom release protocol or state edits were used. No physical claim remains.

The master push triggered exact-head CI 40229910427. A fresh policy watcher is
observing that existing run with no retries, diagnosis, deployment or cancellation.

## Worktree-reader follow-up preparation

Source b75a6a10 passed independent review in all four lanes with no findings.
The source two-commit range is forward-only over merged b974f2f3. Current new
pins are config fc713f7c and workspace eb088284; one mechanical update per branch,
all unrelated selections preserved. Artifacts and CI batch use these exact clean
heads. Config hooks and cross-repository deployment contract passed.

Exact system generation 2026-10-25--22-04-50 is built/copied:
/nix/store/nvav7nvnrl9hjij2sab233rnlx8dlnn3-nixos-system-aitherdev-26.05.20261021.da6dc0e.
The initial copy selector current was resolved by confctl to this same immutable
name; saved preparation now uses the exact name and metadata. No activation yet.
Disposable baseline checkout removed after its failure evidence and review ended.

Corrected fresh utility uses absolute tracking artifacts; actual Luna/low,
full-access/approval-never launch verified. Reusable monitoring lesson saved in
notes/dev-workspace/2026-10-25-verification-artifact-paths.md.

Finish this bounded compatible remediation by integrating the same three already
approved master targets after successful final verification, then activate system
before profile under a new machine claim, verify and promptly release. An
integrate-first order avoids holding the physical machine for repository work.
No new integration scope, state format or host policy is introduced.

## Final compatible follow-up, prepared (not activated)

- dev-workspace: 960dd816b7e56cbdd4af0da15bf0b26257775151.
- vpsfree-cz-configuration: 270d348a29a832e552a798ba8bb467152a2d36d6.
- workspace: 3e72f394a73c33be71fcdc1313d05cc74abb802f.

Source review is clear in recovery-contention-review.md, all four lanes/high
risk; startup attachment-cancellation finding corrected and independently
assessed. New source adds reader registration, equivalent-status Retry, startup
signal cancellation, and temporary recovery classification. Native Codex,
extension, codex-web, sibling graph and follows identities unchanged. Contract
passes (startup-final-pin-proof.json). Consumer history assessment is pending.

Exact source CI40238397116 and parallel final system/application builds are
owned by fresh Luna/low watcher01a17518-bc1c-7183-a168-058247541a32, actual policy
verified full-access/approval-never. Earlier780 artifacts/failed creation CI are
intermediate evidence only. All registered final branch comparisons refreshed.
No resource request has been acquired for this follow-up.

After verification, integrate each master under one short repository claim,
preserve shared tracking/index, and release each immediately. Copy the immutable
system generation outside machine ownership. Acquire a fresh aitherdev claim
near activation, run configured rollback-protected system dry-activate/switch,
verify both system links, then ordinary claimed workspace-host selection. Verify
package identity, Codex/tmux continuity, portal/naming/model health and a fresh
owned threadless archive fixture. Prove complete deployed dependency lineage
integrated and release exact machine claim promptly; observe final master CI.
The actual initiative stays open and is never an archive acceptance fixture.

Final local builds passed: system147.3s, workspace558.2s. Exact generation
2026-10-25--23-06-03 / w1m7vv5c, packagefqajxhsm. Copy-only deployment returned0
(startup-final-system-copy.log); both live links and selected package remain
originalg4kz/bhi. CI40238397116 remains with its watcher. No claim acquired.

All final heads fast-forwarded/pushed to their approved masters; exact remote
proof and immediate claim release are in startup-final-merge-proof-*.json.
Shared working diff/index/untracked-name hashes remained identical across merge.
Fresh machine claim41f1b026-5b5f-400c-8148-99a6df008c20 acquired; parent launched
activation PID2902879, system-first dry-activate/switch with configured rollback
then claimed profile selection. Fresh observer owns status waiting only.
Result is pending; no claim of selected-package/live success yet. Master CI
run40239653867 is recorded for post-deployment observation.

## Verified final follow-up activation and release

System: `/nix/store/w1m7vv5ccfdx7h6jgzf0sxssldl1awps-nixos-system-aitherdev-26.05.20261021.da6dc0e`.

Workspace: `/nix/store/fqajxhsmaqg44pl8x2xshgn8q0bl7wr2-dev-workspace-0.2.0`.

Both system identities and the workspace profile match the exact built artifacts.
System dry-activation/switch and profile selection exited0, configured rollback
remained enabled, and no reboot occurred. Codex PID3387667 and tmux PID435397
are unchanged. Portal/router/coordinator are active; health/index/operations/
initiative/original HaveAPI pages and model catalog return200 (eight models).
Active provider remains openai; isolated naming canary succeeded.

Confined fixture2026-10-25-archive-deploy-smoke-7773a2ab passed archive readiness,
proved its terminal survived a loose-file blocker and unrelated operations stayed
available, then archived successfully after removing only its owned marker.
No actual initiative or other session was stopped. Live verification passed in
105.4s; its results are startup-final-live-health.json and adjacent artifacts.

Fresh remote ancestry proves current runtime, configuration, workspace,
extension767dfd58 and codex-web8b60554b integrated. Machine claim
41f1b026-5b5f-400c-8148-99a6df008c20 was then released and confirmed through the
normal selected-package API, without waiting for UI acceptance or master CI.
All three repository claims were already released. Detached merge targets and
obsolete owned interim build links are removed; initiative worktrees, branches,
final artifacts, deployment refs, profiles and recovery journals are preserved.
Master CI40239653867 is the final outstanding verification; no resource held.

Final exact feature archive VM log (run40238397116/job121304766832,1,266,648
bytes) contains zero portal stop-sigterm timeouts. The reproduction establishes
the startup cancellation defect and this final VM evidence shows clean stop
behavior; it does not reconstruct the original historical holder/order.
See startup-final-shutdown-ci-evidence.json for log digest and identity.

## Completed

Master CI40239653867 at960dd816 passed all four jobs, including host; exact
head feature CI40238397116 and both final builds also passed. Fresh completion
proof confirms clean integrated feature heads and all four final claims released.
No remaining process, verification, deployment or cleanup work. Actual initiative
worktrees and branches are retained; no archive/delete/stop action was requested.
