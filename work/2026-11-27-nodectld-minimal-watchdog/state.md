---
lifecycle: active
---

# nodectld minimal mode and watchdog recovery

## Current phase

Implementation plan prepared; awaiting implementation direction. Production
recovery was performed by the user. The agent has made no application changes,
deployed nothing, and created no feature branches or worktrees.

- [x] Read-only central-log/source/monitoring investigation.
- [x] Confirm the user's restart restored transaction processing.
- [x] Create tracking after explicit authorization.
- [x] Prepare the implementation and verification brief.
- [ ] Implement the two fixes and focused regression coverage, if requested.
- [ ] Quick checks, committed deliverables and independent final review.
- [ ] Integration tests and CI.
- [ ] Separately authorized deployment/integration and delivery proof.

## Authorization and ownership

The user initially said "no tracking" and requested logs for vpsadmin1. No
tracking records were created until the later message: "okay i've killed it.
prepare an implementation plan to fix the issues: the requirement of osctld and
the missing watchdog, it's there for a purpose. you can start tracking this
session." This authorizes the plan and tracking, not implementation or deployment.

`dev-session current` initially found no current initiative, and neither identity
environment variable was set. Created the new tracking-only session with
`dev-session start 2026-11-27-nodectld-minimal-watchdog --as-is --no-codex
--no-attach --json`; creation returned this exact slug, a null threadId and the
portal URL below. A subsequent current check with both newly created identity
values set returned this slug. No other initiative was adopted.

There is no retained Codex roster: team listing reports no valid lead Codex
thread for this tracking-only session. No team was invented or reconfigured and
no subagents were assigned. The current conversation lead owns this plan.

## Incident evidence

Times below are 2026-11-27 CET, as recorded by the central logger.
Source: `log.int.prg.vpsfree.cz`,
`/var/log/remote/cz.vpsfree/vpsadmin/int.vpsadmin1/log`.

| Time | Observation |
| --- | --- |
| 03:19:39 | ExportMounts worker raises because `osctl -j ct ls --state "running"` cannot connect to `/run/osctl/osctld.sock`; the process exits with failure. Similar failures recur every six hours on prior days. |
| 03:19:45 | systemd starts PID 2401122. |
| 08:38:20 | Last completed chain before the gap: chain 13080125, transaction 75024103. |
| 08:44:30 | User identifies the first stuck transaction. Monitoring later shows oldest queued chains 13080126 and 13080127. |
| 09:19:46 | The same export-mount exception occurs, but PID 2401122 stays alive and continues status updates. |
| Before restart | Prometheus reports running=1, paused=0, initialized=1, zero used mail slots and zero mail reservations. No SMTP timeout or MySQL error appears in the relevant host-log window. |
| 12:46:05 | systemd logs that it is stopping nodectld; status updates continue. |
| 12:47:35 | Old process exits with signal 9/KILL. User confirms having killed it. Do not attribute the kill to automatic systemd escalation merely because 90 seconds elapsed. |
| 12:47:36 | New daemon PID 2440771 starts. |
| 12:47:38 | Oldest stuck chains 13080126 and 13080127 close. |
| 12:48 onward | Backlog chains continue closing; 62 chain closures were observed through 12:50:04. End-to-end delivery of every message was not independently verified. |

The daemon was running libnodectld 4.2.1 from store item
`f4sns0vs32b2kl7zrz9icdrpivzvmpw8-ruby3.4-libnodectld-4.2.1`.
The host is a NixOS mailer inside a vpsAdminOS container; the absence of osctld
inside it is expected. The recurring osctl error is a minimal-mode defect,
separate from the earlier transaction stall.

The symptoms strongly indicate a blocked main transaction loop with healthy
background/control threads. No pre-kill backtrace was captured, so the exact
blocking call and initial trigger remain unconfirmed. Do not present a mysql2
deadlock as established fact.

## Sources and checks

Fetched and inspected vpsadmin `origin/master`
`99207a8dcd92f5907c52dbc99af52b30aa7ecac1` and configuration `origin/master`
`2f264616638f4baa464692c02bea9ea76d7ffdde`.
The bare vpsadmin HEAD was older; final planning uses origin/master explicitly.

Relevant sources: AppConfig minimal-mode override, Daemon initialization,
ExportMounts/VpsOsRelease enable checks, CLI wrapper/watchdog exit paths, NixOS
and vpsAdminOS service modules, current watchdog/config/export specs, and the
existing services/mailer/Mailpit fixture. The current NixOS service combines
`--no-wrapper` with `Restart=on-failure`. The wrapper's watchdog stop path can
exit successfully, so enabling the wrapper also requires service restart-policy
coverage.

Read-only access to the central logger and documented Prometheus route worked.
Direct SSH to vpsadmin1 was denied for the available key. Investigation did not
change production state. No application tests were run for this planning task.
No independent review is required for routine planning/evidence alone.

Workspace has unrelated changes; preserve them and stage only this session's
three Markdown records plus its portal manifest. No hook framework or active
pre-commit/commit-msg hook was declared/found in the coordination repository.
Initial tracking commit must follow a fresh origin check and use the shared
tracking lock. Project hooks remain mandatory when implementation begins.

## Documentation and next action

- [Plan](plan.md): scope, packages, compatibility and delivery sequence.
- [Design and verification brief](design.md): concrete minimal-mode and systemd
  changes, acceptance criteria, focused checks, rollout and recovery.
- No product documentation was edited during investigation/planning. Its intended
  location and content are specified in the plan.

Next action: present the plan and wait for implementation direction. The two
reliability defects remain in production after the user's recovery restart.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-27-nodectld-minimal-watchdog/

## Retention

No owned temporary service, development cluster, feature worktree or raw artifact
needs cleanup. Keep the session active; no archival or deletion was requested.
Creation CLI note: `--as-is` and `--new` are mutually exclusive. The rejected
first invocation created nothing; retry with `--as-is` alone succeeded.
