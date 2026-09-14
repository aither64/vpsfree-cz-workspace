# General review

## Findings

### Important — a reused slug inherits the previous session's hold and result

- File: `dev-workspace/libexec/workspace-auto-archive.rb:71-78,92-112,151-155`
- Commit: `6524018e1ed958aca848dd30eec453957e2d27fc`

The sidecar is selected only by `session-<slug>.json`. `Policy.observe` detects
that `identity` changed and restarts `idle_since`, but it begins with
`previous.dup` and never clears the old `hold`, `result`, `archived_at`, or
`archive_mode`. `auto_archive_status` also returns that record without comparing
it with the current portal-manifest conversation identity.

This is observable when a held session is manually deleted and a new session is
later created with the same slug: the first observation changes the stored
identity to the new thread but retains `hold: true` and reports `Keep open is
enabled.` The new session therefore remains outside every automatic tier until
the operator discovers and releases a hold that belonged to a different
session. Before the first scan, the portal can also display the previous
session's terminal result. This conflicts with the review packet's requirement
that per-session sidecars be bound to the session conversation identity.

Reset session-specific fields when an already-recorded identity differs from the
current identity, while preserving the hold across archive/revive when the
conversation identity is unchanged. Add regression coverage for delete followed
by creation at the same slug; coverage should also prove that same-identity
revival retains the intended persistent hold and receives a fresh inactivity
period.

## Commit series and residual test gaps

No Blocking findings were found. The two generic-runtime commits have distinct,
reviewable purposes, the downstream policy and dependency-pin commits are split
cleanly, and their messages follow the applicable repository rules.

The focused tests cover all retention boundaries and end-to-end completed and
empty archival, but there is no positive end-to-end test in which a registered,
merged branch is automatically archived through the seven-day tier. Merge proof
behavior and the tier delay are covered separately, so this remains a targeted
integration gap rather than a separate finding. The timer test exercises link,
enable, stop, and removal commands through a host double; actual user-manager
timer execution and package rollback remain appropriately gated packaged/live
validation.

Reviewed ranges:

- `dev-workspace`: `df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933..ef1fa85451ee98f9d0a1d167d586ea2765b67cf7`
- `vpsfree-dev-workspace`: `89a03581b13056fa83114e592f2e2993e6a87887..bba4b8d8208bdfbe9a08e2a90ce04c1910c6cfce`
- `workspace`: `758834a..89f8efe2f7171b2a0b388e0349c24121da0ceef6`
