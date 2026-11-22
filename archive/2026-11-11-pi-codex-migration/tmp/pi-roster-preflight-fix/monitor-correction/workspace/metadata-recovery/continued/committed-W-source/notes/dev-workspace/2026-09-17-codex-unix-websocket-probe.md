# Disable compression in the Python App Server probe

A read-only probe using Python websockets 16.0 against the installed Codex
0.154.0 Unix socket failed during the HTTP upgrade with `did not receive a
valid HTTP response`. Python offers WebSocket compression by default.

Connecting with `websockets.sync.client.unix_connect(socket_path,
uri="ws://localhost/", compression=None)` passed. This matches the existing
Go client's default of not negotiating compression. No App Server restart or
session change was needed. The precise server-side rejection was not traced.

Generate request schemas from the installed Codex package, initialize a fresh
connection, send `initialized`, then call `skills/list` with `cwds` and
`forceReload: true`. Check `data[].errors` and enabled skill paths. Do not create
a conversation or submit a model turn just to verify catalog discovery.

Verification passed in both a project directory and a fresh empty directory;
all three documentation/review/handoff skills were enabled with no errors.

Related initiative: `work/2026-09-17-documentation-boundaries/`.
