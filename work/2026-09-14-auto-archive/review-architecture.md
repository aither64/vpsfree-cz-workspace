# Architecture and repetition review

Reviewed `dev-workspace` `df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933..ef1fa85451ee98f9d0a1d167d586ea2765b67cf7`, `vpsfree-dev-workspace` `89a03581b13056fa83114e592f2e2993e6a87887..bba4b8d8208bdfbe9a08e2a90ce04c1910c6cfce`, and workspace `758834a..89f8efe2f7171b2a0b388e0349c24121da0ceef6`. The consumer pins resolve in the intended order: the extension pins generic runtime `ef1fa85451ee98f9d0a1d167d586ea2765b67cf7`, and the workspace pins extension `bba4b8d8208bdfbe9a08e2a90ce04c1910c6cfce` with the same generic runtime in its lock graph.

## Findings

### Blocking: an unavailable observation source still lets the grace period elapse

- **Commit:** `6524018e1ed958aca848dd30eec453957e2d27fc`
- **File:** `libexec/workspace-auto-archive.rb:241-250`, with the state transition at `libexec/workspace-auto-archive.rb:92-113`

`auto_archive_scan_session` handles an exception raised before `auto_archive_snapshot` can return by overwriting `blockers` and `checked_at`, while retaining the last successful `fingerprint` and `idle_since`. When the source becomes available again and its current snapshot equals the last successful snapshot, `Policy.observe` sees no change and computes eligibility from the old `idle_since`. The time for which activity was unknown therefore counts as verified inactivity. A reproduced activity-reader outage followed by recovery returned `eligible: true` immediately after the stored timestamp crossed 24 hours.

This violates the accepted rule that an unknown or failed activity check must not age a candidate and can automatically archive immediately after a monitoring gap. Route failed observations through the retention state owner, or persist a reset/paused-period marker that makes the next complete observation start a fresh verified interval. Add a scanner-level test covering failure for longer than each relevant grace period followed by an otherwise unchanged snapshot.

### Important: session sidecars are scoped to a reusable slug rather than the conversation identity

- **Commit:** `6524018e1ed958aca848dd30eec453957e2d27fc`
- **File:** `libexec/workspace-auto-archive.rb:71-79`, `libexec/workspace-auto-archive.rb:92-113`, and `libexec/workspace-auto-archive.rb:133-147`

The sidecar filename and validation bind a record to workspace plus slug. An identity change resets `idle_since`, but `Policy.observe` copies the old record and preserves `hold`, `result`, and other session-specific fields. `delete` does not clear or rebind this record. A deleted session can be recreated under the same dated slug with a different Codex thread, and the new session inherits the old session's persistent Keep open hold; this was reproduced through a complete delete/recreate cycle with a changed thread ID. The new work can then remain exempt from automatic archival indefinitely without anyone applying a hold to it.

Bind the complete per-session record to the conversation identity, reinitialize identity-owned fields when that identity changes, or clear the sidecar as part of completed deletion. Cover delete/recreate with a different thread ID and both held and unheld predecessor states.

### Important: the JSON scan path has two output owners and emits invalid JSON during a successful archive

- **Commit:** `6524018e1ed958aca848dd30eec453957e2d27fc`
- **File:** `libexec/workspace-auto-archive.rb:170-203` and `libexec/dev-session:223-266`

`auto_archive_scan` redirects `DevSession::Runner`'s `@out` to stderr so lifecycle announcements do not precede the structured result. `CommandRunner`, however, captured the original stdout when the runner was constructed and its `run` method continues writing subprocess output there. A successful archive runs `git commit`; in a reproduced scan its commit summary was emitted on stdout before the result. Consequently `dev-session auto-archive scan --json` is not a valid single JSON document whenever an archive command writes output.

Give the scan one explicit output owner and route all lifecycle command output through it, or capture operational output separately from the structured response. Add a full non-dry CLI test that archives a disposable session and parses stdout as exactly one JSON value.

## Residual risks and test gaps

The focused tests cover the provider policy and representative extension/portal consumer, but they do not exercise the three cross-boundary scenarios above. Long packaged timer, switch, and rollback validation remains pending as recorded in the review packet. I found no additional consumer-pin mismatch or repeated policy implementation that requires a separate finding.
