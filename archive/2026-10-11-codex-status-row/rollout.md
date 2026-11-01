# Compact status row rollout

Activation and live browser acceptance passed. The accepted plan authorized
deployment; subsequent separately approved default-branch integration is recorded
in [integration.md](integration.md).

Sources and full branch inventory: [final-heads.json](final-heads.json),
[branch-inventory.md](branch-inventory.md). Runtime 17222c37, workspace 7c54c132
and configuration d1f0ce5a select one matching runtime. The provider and
extension remain unchanged; no API, on-disk schema, migration, native launch
policy or host option changes. The final deployment pin contract passed.

Verification completed before activation: actual Chromium/Firefox contracts, runtime and
composition package checks, candidate application, aitherdev host build, and
exact-head CI 38124238272. Fresh one-operation utilities owned the batches in
verification.sh. The first browser run's failures and subsequent test-only
corrections are recorded in state.md and verification-v1/v2.log. Superseded CI
38122847951, 38123289184 and 38123891506 completed successfully. The last was
observed separately because token permissions rejected cancellation with HTTP 403.

The prepared rollout.sh deployed the feature configuration with confctl
dry-activate-first, no reboot and automatic rollback, then switched the
application through its user profile from the workspace feature worktree.
The parent launched an owned transient user unit and recorded its invocation;
a fresh utility observed independently accessible logs, status and unit state.
It did not deploy. Acceptance required atomic status 0 and normal unit exit.

Baseline: [pre-deploy.json](pre-deploy.json). Installed application
/nix/store/m8vg5sfbasaza391j6bl2hcji5jf2kiq-dev-workspace-0.2.0; host
/nix/store/6fv1b4jfxkhrl4wzay088a7s2mpci93k-nixos-system-aitherdev-26.05.20261008.7c8764b.
Native Codex 0.160.0 PID 1204139 and tmux PID 435397 must remain running.
The switch's normal generation, journal, cluster and launch-identity checks
remain authoritative; do not bypass a refusal or stop another session.

Host recovery uses confctl's supported automatic rollback. Application profile
recovery is forward-only: repeat the same compatible switch or select a newer
reviewed compatible package, retaining pending reconciliation evidence.
Retain the built candidate root and source branches. Never select an older
application generation to bypass a transition refusal.

After activation, post-deploy.py checks health, exact final JS/CSS/template,
selected candidate, unchanged native executable, active units and native/tmux
PID continuity. A fresh one-operation utility runs read-only live-status.sh on
the existing evaluate-confctl session at 1280 and 420 pixels. It sends no prompts
or model-setting writes. The parent inspects cropped status images and records
actual peer/own states separately from deterministic fixture acceptance.

## Execution

Browser, runtime/composition, host build and exact-head CI passed before launch.
Candidate application is
/nix/store/v3ysv2w5zxc1rj36fbdrs4x59zh4vckm-dev-workspace-0.2.0; built host
generation is 2026-10-11--10-45-01. The runtime transition contract is identical
to the predecessor, including live switch policy 1 and cluster schema/policy
1/3. Candidate application does not expose bin/codex; a direct-path assertion
was invalid because native Codex is selected through its separate root. The
normal switch guard and post-deploy selected-native proof remain authoritative.

Refreshed pre-deploy.json immediately before launch; installed application,
host, native root and all four active units match the preparation baseline.
Parent launched portal-codex-status-rollout-20261011.service with invocation
9bb2fba75b3b4b609930fd1b05b62ad5 and initial PID 3541885. Exact startup metadata
is rollout-unit-start.json; independent logs/status/phase are rollout.*.
Fresh Luna/low utility monitor_compact_activation observes only this existing
operation. It cannot deploy or retry; parent owns acceptance and recovery.

Activation completed in 2m34s with atomic rollout.status 0, phase complete,
Result success, ExecMainCode 1 (CLD_EXITED), ExecMainStatus 0. Both confctl host
health checks passed. Parent captured exact invocation completion metadata in
rollout-unit-final.json and released only the exited helper unit; no session or
running service was stopped. Selected host:
/nix/store/mhf6xc33xh0hknhl992i29b52h612brb-nixos-system-aitherdev-26.05.20261008.7c8764b.

post-deploy.py passed: portal health, final template (JS v32/CSS v9, removed
codex-team-work paragraph), exact source asset bytes, candidate profile,
unchanged native Codex 0.160.0 root and native/tmux PIDs 1204139/435397. All four
user units are active and running. Evidence: post-deploy-result.json.
During verification the evaluate-confctl architect finished and the lead became
working; its other members were idle. The live browser utility verifies the
currently observed pair rather than assuming the preparation state persists.

## Live acceptance

Fresh Luna/low utility verify_compact_live ran only the prepared read-only
live-status.sh operation and exited 0. It used actual evaluate-confctl member
views at 1280 and 420 pixels without prompts or setting changes. Focused
reviewer0 and architect0 were idle while lead was working. Each displayed
"Other team members are working: lead." in the status row, with no separate
peer paragraph or attention marker. The lead retained "Codex is working".
Full label text was available through hover and accessibility attributes;
the timer remained readable and neither width caused horizontal page overflow.

The parent inspected the cropped reviewer desktop and narrow screenshots.
Narrow wording ends in an ellipsis while the timer stays visible. Evidence:
[live-status-result.json](live-status-result.json),
[desktop screenshot](status-reviewer0-1280.png),
[narrow screenshot](status-reviewer0-420.png).

Final source and consumer heads remain 17222c374bf48c65edc36895e07408c65f1e7b53,
7c54c132420ed367cfe0ed8445c8baf925b12d4d and
d1f0ce5a9a292039def259fef53c2f17bede4cac. Fresh remote proof in
[readiness-refs.json](readiness-refs.json) confirms clean one-commit branches and
unchanged master bases. The selected application and host match the candidate
and generation recorded above; native root and process continuity passed.
No deployment operation remains running. At rollout acceptance no default branch
had been integrated; subsequent approved integration retains these exact sources.
