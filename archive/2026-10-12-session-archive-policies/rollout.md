# Explicit session archival rollout

Executed and verified on aitherdev. The final application is selected in the
user profile. The requested session is archived with ten verified recovery
snapshots. Deployment left the configuration/project default branches unmerged. Their later
authorized integration is recorded in integration-result.json.

## Final deployment

Runtime 1a27453c0b67c8c24cbe1474d5a05607eb698a9a;
workspace d1e5888a9f96e32833d56f5ae18da477df44472b;
configuration 1697613eab00a4bb0642b79c355c0b673b758a41.
Both consumers select the same runtime and hash; extension, native Codex 0.160.0,
codex-web and sibling inputs are unchanged. Final builds and CI 38297311907 passed.

System: /nix/store/apsqp7fvi89kjc0fxp7gijq03sr4jm3n-nixos-system-aitherdev-26.05.20261010.6fcc160.
Application: /nix/store/yb4mamskfrlzaz71ncp3363bhl4jc6hg-dev-workspace-0.2.0.

Parent ran scoped confctl dry activation/configured SSH preview and switch from
the configuration feature worktree, then workspace-host switch --source from the
workspace feature. All four deployment/live statuses are 0; confctl systemd and
firewall health checks passed. All five user units are active. Native/tmux process
and native socket continuity passed against the explicit corrected baseline.
Own/network session GETs returned 200 with v36 assets. Installed artifact command
and documentation skill were verified. Task-specific application GC root removed
only after checking that the selected profile retains this exact application.

The direct ambient SSH preview used an untrusted hostname alias and failed
host-key verification. No checks were bypassed; configured confctl SSH completed
the preview normally. Corrected-deploy-* logs/statuses retain the full evidence.

## Requested archive acceptance

Parent ran the ordinary interactive dev-session archive command for
2026-10-11-diagnose-vpsadmin-api-exception and supplied its one yes/no confirmation
under the existing explicit user request. Exit 0; tracking transition committed
as 8df4f006. Quiescence, both cluster releases, cleanup, tracking archive/commit,
thread retirement and runtime retirement completed.

A fresh Luna/low observer retained actual archive status, then ran the read-only
recovery verifier after success. Exit 0: schema 3/neutral archived lifecycle,
ten checksum-verified complete checkout/admin snapshots, all worktree paths and
Git registrations absent, head recovery refs and branches retained, no journals.
Parent checked archived portal GET 200/read-only, absent tmux session and absent
runtime authority. [Curated archive proof](requested-archive-result.json).
No revival was performed and this implementation initiative remains open.

## Earlier deployed revision and correction

The first deployment actually selected runtime ebe612f8c890bfc5325c0e5f8e86490ffa2534e3,
workspace 7f932c7d44464c0de070e88ad17f9e903fe7ff78 and configuration
edeb94c1a810f17a148de3edc59209e0f580a967.
Application /nix/store/3lmslks7y6sigm6wsami3vzkmx9ww55h-dev-workspace-0.2.0;
system /nix/store/bicq7lfx2s6xay66zqqssp2swm7k41a4-nixos-system-aitherdev-26.05.20261010.6fcc160.
Builds and CI 38290319369 passed. Dry activation/switch/application/live checks
passed, including Chromium/Firefox read-only archive-dialog probes.

Its first actual archive attempt exited 1 before worktree removal or journal
capture: Ruby omitted the workspace/private-state arguments required by the Go
quiesce helper. The helper refused to lose private queued-prompt records. The
correction passes the selected context and adds caller/real CLI regressions.
Affected independent review found no issues; final builds/CI passed before the
corrected deployment. Existing formats and private recovery holds were preserved.

Native Codex restarted during the user pause at 20:37 and again at 21:18 before
the corrected deployment. Cause is not established; systemd showed normal
stop/start and NRestarts=0. Native remains 0.160.0. Initial, first deployment and
corrected deployment baselines/post-deployment evidence are retained separately:
live-before.json, live-before-deployment.json, live-after-first-deployment.json,
live-before-corrected-deployment.json and live-after.json. Continuity claims refer
only to each actual deployment's corresponding baseline.

## Recovery and integration limits

Explicit archival now writes schema-3 manifests/journals and schema-2 cleanup
sidecars; revival uses schema-4 journals. Use a capable executor and retain
private recovery receipts. Do not switch to an older parser after writing new
formats. Retry interrupted operations through their ordinary journal recovery
before another package transition. Workspace package recovery is forward-only.
Supported predecessor formats remain readable.

No database/node migration or coordinated running-node update was required.
No default-branch integration was authorized at rollout time. Later user
direction authorized all three master integrations, now verified. Final histories are
consolidated; exact earlier rollout revisions above preserve execution evidence.
Integration used the normal current-target rebase/final-history checks; all
three remote defaults contain the exact final feature heads. All source branches
are retained. No deployment repeat or CI wait was needed for integration.
