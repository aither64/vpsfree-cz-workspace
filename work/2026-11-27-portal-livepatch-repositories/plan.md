# Investigate livepatch repository browsing

## Goal and scope

Investigate the repository tab for `2026-11-18-livepatch-backport-process`
and suggest a solution. Inspect the deployed generic dev-workspace portal,
its read APIs, registered Linux/vpsAdminOS worktrees and bounded Git reads.
No application implementation, deployment or changes to the target session.

## Approach

Compare API failures with direct no-fetch Git reads and trace the installed
source. Separate comparison metadata failures, timeouts and browser behavior.
Use the target session as read-only reference; its private sensitivity marker
is absent. This investigation owns a separate CLI-created tracking session.
No valid lead thread/roster exists for this CLI-only record, so no team is
invented or borrowed; investigation continues in the originating conversation.

## Compatibility, verification and documentation

Keep persisted manifests, comparisons and Git refs unchanged. Any proposed fix
must preserve exact base/head semantics, local-only reads and bounded commands.
Use short API/Git probes; no builds or integration tests are needed for diagnosis.
Record evidence and proposed changes in state.md for the operator and a future
implementer. Product documentation will only need changes with implementation.
