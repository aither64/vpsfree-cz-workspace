# Aitherdev rollout

Deployed and verified on aitherdev; source branches remain unmerged. Deployment is authorized by the accepted implementation
plan; integration into default branches is not authorized.

Sources: see branch-inventory.md. Workspace and configuration select runtime
e10a1887e4ba7051b5ebfcdd03412d130d76db4a; extension stays unchanged.
Predecessor user profile: /nix/store/s2zxa731kh87li7syxi3qzjzw3wcp9zd-dev-workspace-0.2.0.
Predecessor host: /nix/store/dmzm997gh7smblm2c1dlrcfsqwbr1mjq-nixos-system-aitherdev-26.05.20261008.7c8764b.
Predecessor native PID: 1204139; portal PID: 3094612.
Native Codex: /nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0.

After independent review and findings reconciliation:
1. Run package/provider/composed checks, browser integration and native protocol
   verification using fresh Luna/low monitoring operations. Build exact aitherdev
   configuration with confctl from its initiative feature worktree.
2. Build and retain the composed user package. Run confctl dry activation and
   switch only cz.vpsfree/machines/aitherdev, without reboot, with auto rollback.
3. Select the composed application using the stable workspace-host switch.
   Use an owned transient user systemd service for operations that outlive tools;
   retain atomic exit status and full logs, and let a fresh watcher observe them.
4. Verify every required user unit active, selected profile and native identity,
   session endpoint, served statistics/settings assets and read-only API behavior.

Native runtime policy is unchanged, allowing the existing compatible live switch
policy to preserve native work. Do not stop other sessions. A refused profile
switch leaves its predecessor selected. Following selection, recover by retrying
the exact target or selecting a compatible newer package. Profile rollback is
forward-only. Private counters and model choices do not alter roster/recovery
schemas; retain their records across recovery. No pending native settings are
modified in existing sessions during deployment verification.

Prepared operation: rollout-operation.sh. Executed after the successful verification batches, under the owned transient user unit portal-team-rollout-20261010. Its
atomic status and complete log are independently observable by a fresh watcher.
Configuration deployment performs dry activation first and enables auto rollback;
profile selection follows only on success. No reboot. The composed package is
built and retained beforehand in candidate-package.txt.

## Execution

All prerequisite checks and both CI runs passed. Candidate built from workspace
33bf097701012245366beee40146b4b7b6c2a76e:
/nix/store/5wr4k0dbh1n5miw5575lbi21z7svi257-dev-workspace-0.2.0. Owned GC root:
candidate-package. Configuration f86408a2 built generation 2026-10-10--17-51-00.

Authorized operation launched under portal-team-rollout-20261010.service,
invocation 6917d423efd349bda58a2c0fd4cf1af0. Full output: rollout-operation.log;
atomic result: rollout-operation.status; current phase: rollout-operation.phase.
Fresh monitor_rollout observes this operation. Operation finished status 0, phase complete; no running process remains.

## Verified result

Confctl activated the built host generation with dry activation first, no reboot
and automatic rollback enabled. Both host checks passed. Selected host:
/nix/store/g5gizpsrrjlx5nx784yz6xdffzapkpx5-nixos-system-aitherdev-26.05.20261008.7c8764b.
User profile equals the retained application candidate.

Backend health, own session page, Team API and exact source hashes of app.js,
style.css and conversation.js passed. This tracking-only initiative intentionally
has no Codex thread; unavailable statistics are expected. Retained-member UI is
covered by the completed browser fixtures. HTTPS verifies against the configured
public development CA and returns expected 401 authentication.

Native PID 1204139 and its exact 0.160.0 package remain unchanged. Portal PID
174457 and router PID 174429 serve the new profile; tmux PID 435397 remains.
All four workspace services are active; auto-archive and reconcile units were
restored and are active. Machine-readable proof: post-deploy-result.json.
No existing thread's model settings were changed during live verification.
No reboot, default-branch integration, session closure or branch deletion occurred.

## Compact Team follow-up: prepared deployment

Final provider/runtime/workspace/configuration heads are recorded in
final-heads.json. Host/profile sources agree on runtime 40abb17b. Verification
is running; no follow-up deployment has executed yet. Parent-owned
rollout-followup.sh will deploy the built configuration with dry-activate-first,
no reboot and automatic rollback, then select the built workspace user profile.

Predecessor proof is followup-pre-deploy.json. Native Codex remains 0.160.0;
Codex PID 1204139 and tmux PID 435397 must survive. The two example sessions are
read-only targets. Pre-deploy evidence shows each native thread active while the
old portal records unclassified time. After deployment, compare current turn IDs
and activity via read-example-statistics.py --after. Older unobserved timing
stays partial. Confirm health, exact served assets and all four user units with
post-deploy-followup-check.py, then inspect actual Team table/popup at 1280 using
the GET-only loopback proxy in live-team-preview.cjs. No settings writes or
inference turns are permitted by those live scripts.

The predecessor’s exact four source heads are retained under published tag
portal-team-statistics-deployed-20261010-v1. The candidate package will have a
session GC root. Profile recovery stays forward-only; on refusal, inspect the
reported condition and retry that candidate or a compatible newer package.
Do not silently roll back native Codex or mutate lifecycle/cluster state.

## Compact Team follow-up: executed and verified

Parent-owned unit portal-team-statistics-followup-20261010.service completed with
Result=success, ExecMainStatus=0 and rollout-followup.status=0. Watcher captured
invocation 7deeec078ee54b53b8387739e331fb41 and about2 minutes elapsed. It activated
built host generation 2026-10-10--19-48-46: both health checks passed, followed
by protocol compatibility checks. Profile switch selected
/nix/store/0s1hygvy92wf60bgwb22ydq398hmdw4d-dev-workspace-0.2.0.

The launching systemd-run client lost its D-Bus connection while waiting and
returned1. This is a client transport result: the independent unit/status/log
proof establishes deployment success. Parent confirmed Result=success and
ExecMainStatus=0 after completion; no deployment was retried.

Post-deploy health/page/Team API, exact served asset bytes, candidate selection
and all four user services passed. Native Codex 0.160.0/PID 1204139 and tmux PID
435397 remained unchanged. HTTPS with the configured development CA verified
TLS and returned expected401 authentication.

Read-only example checks now show network-ipv4-left-counter working with the
same active turn. evaluate-confctl-rewrite-language completed a later turn
during verification and now correctly reports idle, matching native idle.
Historical unobserved time remains partial; no inference or settings write was
used to produce this proof. See example-statistics-before.json and
example-statistics-after.json. Deployed browser inspection remains in progress.

Deployed browser acceptance completed successfully; geometry and loaded popup
pairs passed for both examples. Parent inspected screenshots and repeated native
activity comparison successfully. No operation remains running. The deployment
is ready for use; branches remain active pending explicit merge approval.


## Other-members-working rollout preparation

Prepared rollout-team-work.sh for configuration dry-activate-first/no-reboot/
auto-rollback followed by workspace user-profile switch from this initiative's
feature worktree. Native Codex provider/package are unchanged; preserve ongoing
turns and tmux. Old deployed source heads retained by v2 tags before consolidated
pin regeneration; previous application /nix/store/0s1hygvy92wf60bgwb22ydq398hmdw4d-dev-workspace-0.2.0
and host /nix/store/xw6l5ylfqcmi6jcgkwajc6ppfhwq812c-nixos-system-aitherdev-26.05.20261008.7c8764b
remain predecessor provenance. Host deployment uses confctl automatic rollback;
workspace user-profile switches are forward-only. Recover application failures
by repeating the same switch or selecting a newer corrected package, preserving
pending reconciliation evidence. Final review and verification passed before the
execution below.

## Other-members-working rollout: executed and verified

Parent launched portal-team-work-rollout-20261010.service with invocation
39a01b7d73aa4930a906d67c32db3607. It retains completion metadata through
RemainAfterExit=yes; no blocking systemd-run client wait was used. Fresh Luna/low
utility /root/monitor_team_work_rollout observes independent log/status/phase and
the exact unit. Sources are final-heads.json: runtime 27ff794, workspace bb21a0f0,
configuration 14cd296a, unchanged provider 7aff1632. Built host generation
2026-10-10--22-33-32 and application /nix/store/m8vg5sfbasaza391j6bl2hcji5jf2kiq-dev-workspace-0.2.0.
The continuity baseline was refreshed immediately before launch in
team-work-pre-deploy.json; all four services were active. Operation completed in
2m13s with Result=success, ExecMainStatus=0, phase complete and atomic status 0.
ExecMainCode 1 is the normal CLD_EXITED enum. Both host health checks and protocol
checks passed. The parent captured completed unit metadata in
rollout-team-work-unit.txt and released the completed helper unit; no process
remained and no deployment was retried.

Parent live checks confirmed health, actual session template, exact JS/CSS bytes,
selected candidate and four active user services. Native Codex 0.160.0/PID 1204139
and tmux PID 435397 were preserved. Selected host is
/nix/store/6fv1b4jfxkhrl4wzay088a7s2mpci93k-nixos-system-aitherdev-26.05.20261008.7c8764b.
Public TLS verified with the configured CA, returning expected anonymous 401.
Machine-readable proof: post-deploy-team-work-result.json.

Fresh utility /root/verify_team_work_live completed GET-only actual-page browser
acceptance in about 10s. Lead working view stays active; reviewer0 idle view shows
Other team members are working: lead, Idle label and no waiting-attention dot.
Both 1280/420 layouts fit. Parent inspected team-work-reviewer0-1280.png.
Result: live-team-work-result.json. No inference, settings write, reboot or
integration was used. All owned operations are complete; branches are ready,
awaiting explicit merge approval.
