# Automatic session archival on aitherdev

An hourly systemd user timer runs the existing session archive workflow.
The vpsfree-cz workspace policy was enabled at 2026-09-14 14:23:27 UTC.
Other workspaces remain disabled by default.

| Session state | Inactive period | Archive mode |
| --- | --- | --- |
| Explicit lifecycle complete | 24 hours | Complete |
| Active, all registered branches merged | 7 days | Complete |
| Active, no registered repositories or owned worktrees | 14 days | Abandoned |

Keep open in the portal prevents automatic archival. CLI controls:

```sh
dev-session --workspace vpsfree-cz auto-archive hold SLUG --as-is
dev-session --workspace vpsfree-cz auto-archive release SLUG --as-is
dev-session --workspace vpsfree-cz auto-archive status SLUG --as-is --json
dev-session --workspace vpsfree-cz auto-archive scan --dry-run --json
dev-session --workspace vpsfree-cz auto-archive disable
systemctl --user status workspace-auto-archive@vpsfree-cz.timer
```

Disabling the policy prevents new archives; a previously prepared automatic
archive retains normal journal recovery. Re-enabling the policy and releasing
a hold start fresh grace periods. Manual archival remains available.

The initial scan inspected 174 directories, recorded activity for 18 sessions,
and archived none. Fourteen had repository registrations and four had none.
Every recorded eligibility date retained its full interval from first
observation; the earliest was 2026-09-21 14:23:29 UTC, conditional on the normal
merge and cleanup checks. The scanner skips unverifiable legacy records:
146 directories lack the required lifecycle front matter, eight have no shared
conversation identity, and two lack a portal manifest. These counts describe
the initial scan and may change as sessions are updated.

The deployed revisions are now merged into master in all three repositories.
The 2026-09-14-auto-archive branches are retained, and their clean worktrees
have been removed. No system configuration change or redeployment was needed.
The pre-feature user-profile package is retained in generation 39. Review
reconciliation, first-scan results and a read-only live portal screenshot are
included in this initiative's artifacts. CLI/API hold changes and actual
archives were tested with disposable fixtures; no other live session's hold
was changed for testing.

Final validation passed: mandatory reviews, packaged runtime and site checks,
both final feature-branch GitHub CI runs, live service execution and browser
inspection. Default-branch runtime CI also passed. Per the user request,
handoff did not wait for the organization default-branch CI to finish.
All 18 unchanged observations retained their original periods across the final
profile switch; no archive or pending operation was created.
