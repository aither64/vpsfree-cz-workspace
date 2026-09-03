# Codex App Server thread naming method

Related initiative: `work/2026-09-03-dev-session-portal`

## Symptom

Codex CLI 0.152.1 rejected the generated-schema method `thread/setName` while a
portal integration spike named a newly created thread.

## Cause

The running App Server advertised `thread/name/set` as the supported method.
The generated v2 schema installed with the same CLI still used the older
`thread/setName` spelling.

## Workaround

Use `thread/name/set` with the same `threadId` and `name` parameters. Treat the
runtime initialize/error response as authoritative and keep protocol failures
isolated from read-only portal status.

## Verification

The portal client integration test creates and names a disposable thread
through the App Server Unix socket.
