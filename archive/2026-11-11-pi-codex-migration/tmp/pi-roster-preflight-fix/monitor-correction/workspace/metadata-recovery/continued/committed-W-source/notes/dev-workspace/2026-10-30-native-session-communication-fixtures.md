# Native communication fixture startup

During `2026-10-29-cross-session-communication-authorization`, the new tagged
native communication test compiled and its command-path test passed, but the
first native execution failed before delivery. Two fixture contracts mattered.

Native MCP children filter the daemon's environment. Fixture guard and path
variables supplied only through `daemon.Env` did not reach the MCP helper,
which closed during initialize. Passing the disposable fixture variables through
the MCP server's explicit `env` configuration changed a short startup check from
failure (0.661s) to success (0.680s). Keep that environment explicit and scoped;
do not depend on ambient host state.

A fresh `thread/start` has no rollout for managed resume/receipt preparation.
Using `SendWithOptions` as its first seed failed with “no rollout found”. The
fixture now submits a real `turn/start` with its model and effort, then waits for
native idle before managed sends, following the existing native reporting test.
The combined short startup/seed check changed from failure (0.691s) to success
(1.036s). A managed initial-message helper correctly rejected the raw client's
`source=vscode`; its production freshness refusal was preserved. No rollout,
source identity or successful receipt was fabricated.

These focused checks establish fixture startup, not cross-session acceptance.
The full idle/steer round trip and packaged suite remain separate requirements.

Attaching a test-owned recorder exposed the missing active observation but would
have hidden the production composition defect. The portal owns a separate
observer; its operational client has no recorder. Communication now delegates
fresh, gated activity reads to that observer while retaining the operational
client for delivery and reconciliation. The final native fixture uses the real
portal constructor and worker. An idle direct-client pass alone did not establish
working-recipient delivery. The design addendum and `implementation-c.md` record
the production proof and focused red/green results.

Source: `portal/cmd/workspace-portal/session_communication_native_integration_test.go`
in dev-workspace. Detailed revisions, commands, initial failures and final
acceptance evidence belong to the session's `implementation-b.md`,
`review-followup.md` and `verification/` records.
