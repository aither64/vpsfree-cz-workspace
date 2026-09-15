# Prepared delivery and recovery

No deployment, production lookup, mailbox processing, or ticket replay has been
performed in this initiative.

The configuration's `cluster/cz.vpsfree/vpsadmin/common/api.nix` supplies
`configs/vpsadmin/api` to the API and console. The parser consumes the existing
vpsAdmin incident-array interface. There are no dependency pin changes,
migrations, client updates or coordinated node changes.

On a later authorized rollout, build/deploy the intended API configuration
using the reviewed feature revision and normal confctl workflow. Inspect
UCEPROTECT diagnostics for created/duplicate/sentinel/rejected counts and RT
references. This is configuration deployment, not authorization to merge the
configuration default branch.

For ticket 95047, inspect the existing incident for the first IP and the
original RT report before replay. Process only the missing second report.
The mailbox task deletes fetched mail independently of parser success; use RT
for rejected-entry recovery. There is no automatic retry or cross-message
deduplication. Check database and notification state before recovering from
persistence or delivery failures. Rollback cannot retract already sent mail.

Offline upload verification used controlled assignments, not production owners.

## Integration and cleanup completed

The user authorized default-branch integration and cleanup. Fetched origin/master
was still 713fb3ba48ae31c87519e75892d1413a48a22fb0, so no rebase was needed.
A fresh integration worktree fast-forwarded to reviewed commit
b6e650ad902482b4c4e66b5a89a4275bed92419e. Its full suite passed (118 examples,
seed 62935). An atomic SSH push updated master and created remote feature branch
2026-09-15-abuse-uceprotect. Both refs were verified directly with ls-remote;
the local master was also fast-forwarded to the same commit.

The two owned worktrees and transient test files were removed; feature branches
and the portal comparison remain. No push-triggered GitHub Actions workflow
exists, and no run was created for this head. Deployment and ticket replay were
not performed. Session records are retained rather than archived.
