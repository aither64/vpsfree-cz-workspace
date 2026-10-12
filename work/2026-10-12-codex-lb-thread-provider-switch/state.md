---
lifecycle: active
---

# Codex thread provider transition

## Current status

Investigation in progress. The user authorized restarting retained managed threads
for the codex-lb switch. No managed thread configuration has been changed.
The workspace App Server runs Codex 0.160.0 and restarted on 2026-10-12 at
20:37:07 CEST. Its global disk configuration selects codex-lb, but 15 loaded
retained threads report live provider openai. A fresh disposable thread uses
codex-lb. Disposable history probes confirm that thread/resume ignores an
explicit modelProvider change while the thread is loaded.

## Phase checklist

- [x] Identify the installed runtime, global provider, and loaded-thread behavior.
- [x] Create isolated operational tracking and record authorization and constraints.
- [ ] Verify a supported provider transition on a disposable history.
- [ ] Inventory exact targets, owner identities, saved settings, and activity.
- [ ] Back up private state and execute the authorized bounded transition.
- [ ] Verify effective providers and preserved settings, and prepare handoff.

## Next action and risks

Inspect native reload/unload methods, including config/batchWrite runtime reload,
before choosing an operation. Do not archive initiatives, rewrite rollouts,
reconfigure team members, or restart the entire service as a workaround.
The earlier service restart killed development-cluster VM processes belonging to
its cgroup. Cluster recovery is outside this bounded provider transition.

## Documentation and repositories

This tracking-only initiative has no project worktrees or feature branches.
Documentation is operational evidence in this record; no reusable implementation
change has been chosen. No automatic substantive-deliverable review is due for
investigation, tracking, or evidence alone. Preserve all unrelated workspace edits.

## Cleanup and recovery

Temporary protocol fixtures are isolated from managed conversations. Subscription
config and auth backup: ~/.codex/backups/20261012T180755Z-before-codex-lb/.
No private token, credentials, instructions, or full conversation data is committed.
Keep this initiative open for follow-up; no archive or delete action is authorized.
