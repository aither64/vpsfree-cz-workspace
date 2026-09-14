# Scope and proportionality review

Reviewed the committed ranges in the packet:

- `dev-workspace` `df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933..ef1fa85451ee98f9d0a1d167d586ea2765b67cf7`
- `vpsfree-dev-workspace` `89a03581b13056fa83114e592f2e2993e6a87887..bba4b8d8208bdfbe9a08e2a90ce04c1910c6cfce`
- `workspace` `758834a..89f8efe2f7171b2a0b388e0349c24121da0ceef6`

## Important

### Revival can finish irreversibly and then fail on optional sidecar state

Owning commit: `dev-workspace` `6524018` (`sessions: archive inactive sessions through the lifecycle runner`).

Location: `libexec/dev-session:1539-1545` at the reviewed head, together with `libexec/workspace-auto-archive.rb:158-167`.

`revive` calls `finish_revive_journal!`, prints `revived session`, and only then calls `auto_archive_reset`. The reset reads and rewrites the per-slug automatic-archive sidecar. If that sidecar is malformed or cannot be written, the command exits with an error after tracking has moved back to `work/`, the revive commit and runtime start have completed, and the recovery journal has been removed.

Reproduction: create an automatic-archive sidecar for an archived slug, replace `session-SLUG.json` with invalid JSON, then run `dev-session revive SLUG --as-is`. The tracking transition completes before `WorkspaceAutoArchive::Error` is raised. A retry cannot resume the original operation because the archive source and revive journal are gone.

Impact: the new optional policy state weakens the existing journaled, retryable revive contract and can tell an operator that revival failed when it actually completed. It also leaves no durable phase from which the sidecar reset can be retried.

Smallest correction: perform the reset before removing the final revive journal, under the existing final creation/slug lock, so a reset failure retains the `runtime_started` journal and a repaired retry can finish idempotently. This keeps the fresh-period requirement inside the existing lifecycle boundary without adding another recovery mechanism.

## Assessment

No other scope or proportionality findings. The worker, per-workspace policy and per-session observations, CLI and portal controls, timer lifecycle handling, dependency pins, and standing authorization map directly to the accepted 1/7/14-day policy. Reusing the established archive runner and journals avoids an independent cleanup framework. The two generic-runtime commits and downstream mechanical pin commits are coherent and do not introduce unrelated product behavior.

The original head's focused tests covered all retention boundaries but did not positively execute a successful registered-and-merged seven-day archive end to end; that is a narrow residual test gap rather than a reason to expand the implementation.
