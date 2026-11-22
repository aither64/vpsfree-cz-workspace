# Pinned Codex MCP test harness

When an opt-in codex-web Go test starts pinned Codex App Server 0.155.1 with a
required stdio MCP probe, keep the test server's identity in its command
arguments. App Server did not forward an inherited probe environment variable
to the MCP child, causing an initialization handshake to close. The test
binary now uses `-test.outputdir=<private-root>` and a private sentinel;
ordinary package tests return without opening a server.

Pass a non-nil environment map to `StartThreadWithSettings` and
`ResumeThreadWithSettings`. A nil map serialized as an invalid
`shell_environment_policy.set` value before any model turn. The team runtime
already constructs a non-nil member environment.

After `SendWithOptions` returns, an immediate `ActiveTurnID == ""` and empty
`ReadThread` can precede the turn appearing in history. Wait for the returned
turn ID and its completed status before declaring a missing MCP call. The
two-turn reconnect contract passed at codex-web `ef4cd581b1c0`, logged in
`work/2026-09-21-agent-teams-workflow/logs/pinned-mcp-contract-ef4cd58.log`.

This host has no `/usr/bin/time`; a Luna watcher that wrapped its command
with that path failed before running the test. Use tool wall time or shell
built-ins when timing verification, and keep the command's exit status.
