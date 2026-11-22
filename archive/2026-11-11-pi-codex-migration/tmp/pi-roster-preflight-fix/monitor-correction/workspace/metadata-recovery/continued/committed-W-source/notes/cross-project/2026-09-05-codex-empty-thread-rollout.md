# Codex threads need a first turn before resume

## Symptom

Starting a shared session without an initial request called App Server
`thread/start` but did not start a turn. The portal later failed to list the
thread history with:

```text
invalid paginated history lineage: missing source rollout
```

The terminal client also failed to resume the same thread because its rollout
file did not exist.

## Cause

Codex App Server keeps a newly started thread in memory, but it does not create
the rollout file until the first turn. The terminal UI has the same
materialization boundary: it creates its new thread only after the first user
message. Waiting for a detached terminal UI and trying to discover its thread
therefore cannot bind a session before that message.

The first-turn acknowledgement and rollout-file creation also precede stable
paginated history. During that short transition, `thread/turns/list` can return
`list_turns is not supported yet` or a turn whose user item is not visible yet.
The caller must keep waiting for the exact first user message; the presence of
the rollout file alone is not the ready-state boundary.

Launching the terminal UI in `work/<slug>` can also show Codex's project trust
prompt. Trust is persistent user configuration for the exact project path, not
a documented per-process switch suitable for session bootstrap.

## Supported workflow

Every new shared session starts with an initial request. Interactive
`dev-session start <name>` reads one request before creation. Scripts use
`--goal-file`. The portal already supplies a goal file through the same public
command. Both paths create the App Server thread, start its first turn, persist
the thread ID, and attach the terminal client with `codex --remote ... resume`.
Creation becomes ready only after bounded polling sees both a regular rollout
and the exact submitted first user message.

`thread/read` can still report a proven fresh missing-rollout thread as an empty
transcript. This keeps the portal diagnostic view useful after an interrupted
creation, but such a thread is not treated as resumable session state.

## Verification

A source-built portal returned an empty `entries` array for a fresh thread with
the exact missing-rollout response. The session test suite covers the
interactive prompt, noninteractive refusal without `--goal-file`, fail-closed
behavior before tracking files are written, and terminal attachment to the
thread created by the initial-request path. The package contract exercises the
transient paginated-history response against the configured Codex executable.

Related initiative: `work/2026-09-03-dev-session-portal/`.
