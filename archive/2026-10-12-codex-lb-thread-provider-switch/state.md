---
lifecycle: complete
---

# Codex thread provider transition

## Current status

Provider transition completed and verified. All 73 retained managed roots and
non-removed members persist codex-lb. All 15 resumed lead threads report the live
provider codex-lb and retain every other live resume setting. The shared Codex
0.160.0 service is active with PID 2615996, restarted at 21:18:18 CEST on
2026-10-12. The portal service and tmux were left running.
Disposable history probes confirm that thread/resume ignores an explicit
modelProvider change while the thread is loaded.
Cold thread/resume with an explicit provider persists the new provider across
another native process restart. A private isolated replay of a retained root
confirmed that explicitly carrying its live settings preserves every other resume
response field and retains the existing rollout bytes as an unchanged prefix.

Inventory covers 73 retained roots/members in 33 ready active manifests, excluding
removed members. All passed the native/portal idle, request, queue, submission,
goal and lifecycle-journal checks; read-only preflight left the 15 loaded IDs
unchanged. Private backups include all 73 rollouts (about 3.34 GiB), a consistent
SQLite snapshot, configuration/auth and 55 session/roster metadata files at
~/.codex/backups/20261012-managed-provider-switch/ (directory 0700, files 0600).

## Phase checklist

- [x] Identify the installed runtime, global provider, and loaded-thread behavior.
- [x] Create isolated operational tracking and record authorization and constraints.
- [x] Verify a supported provider transition on a disposable history.
- [x] Inventory exact targets, owner identities, saved settings, and activity.
- [x] Back up private state and execute the authorized bounded transition.
- [x] Verify effective providers and preserved settings, and prepare handoff.

## Next action and risks

No remaining provider-transition work or blocker. Use Codex normally. The final
native/portal activity checks passed and the complete Codex cgroup contained only
the native server before the controlled stop. A temporary native server applied
the provider overrides with the original lead settings and each member's saved
roster model, effort and access. The shared server was started in the recovery
path, then all original 15 lead IDs were resumed and compared field by field.
One root naturally unloaded during preflight, without any new subject appearing.

Verification checked all 73 saved providers, 40 retained member model/effort
bindings, unchanged original history prefixes for all 73 rollouts, and unchanged
hashes for all 55 manifests/rosters. Subscription auth and global configuration
bytes remained unchanged. No inference turn was started by the operation.
Keep the portal service running: its cgroup owns a tmux process. Never archive
initiatives, rewrite rollouts, reconfigure membership or kill cluster processes.
The earlier service restart killed development-cluster VM processes belonging to
its cgroup. Cluster recovery is outside this bounded provider transition.

## Documentation and repositories

This tracking-only initiative has no project worktrees or feature branches.
Documentation is operational evidence in this record and a reusable investigation
note. No project implementation or versioned configuration deliverable was made;
no automatic substantive-deliverable review or CI is due for operational evidence.
Preserve all unrelated workspace edits. Initial tracking commit: e76c0c14.

## Cleanup and recovery

Temporary protocol fixtures are isolated from managed conversations. Subscription
config and auth backup: ~/.codex/backups/20261012T180755Z-before-codex-lb/.
Private RESTORE.txt in the managed-provider backup explains the additional cold
provider override required to return retained threads to openai. Restoring the
global subscription config alone changes defaults for new conversations.
No private token, credentials, instructions, or full conversation data is committed.
Keep this initiative open for follow-up; no archive or delete action is authorized.
