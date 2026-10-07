# Archive content integrity and useful failures

Implement the user-approved investigation plan: recover the completed
2026-10-04-session-archive-reliability archive, remove permission bits from new
record integrity checks, preserve useful errors, and deploy to aitherdev.

Affected repositories: dev-workspace (implementation and reusable docs),
workspace (matching nested runtime selection), vpsfree-cz-configuration
(matching devWorkspace host selection). No extension or Codex update.

The archived state.md is 0600, while its existing journal projects 0644. A
read-only hash calculation with that single mode correction exactly matches
the recorded target. All registered retained heads match and are ancestors of
cached origin/master. No contents or operation evidence need replacement.

New tree hashes preserve paths, entry kinds, bytes and symlink targets but omit
permission bits. Readers accept new hashes or the previous exact mode-sensitive
hash, preserving existing journal and cleanup-sidecar formats. Old executors
cannot run newly created operations; existing transition rules already require
pending operations to finish before changing package generations. No database,
protocol, manifest or Codex migration is needed. Unrelated ownership, worktree,
merge, content and activity checks remain in force.

The worker keeps its real bounded exception in last_attempt_error; Settings
shows one concrete failure summary and the existing Retry action, with policy,
activity and diagnostic detail collapsed. Main-agent writing review applies.

Recover the old archive before any package switch, stopping its automatic
worker while correcting only state.md mode and using the same native retry.
Build and deploy the matching host through vpsfree-cz-configuration and confctl;
activate the application from the workspace composition user profile. Deploy
feature branches. The user has not authorized default-branch integration.

Verification covers 0600 records and umask 077, already-complete lifecycle,
interruption/retry, chmod-only changes, real content/path/link changes, legacy
archive/revive journals, retained worker exceptions and browser presentation.
Quick checks precede committed whole-branch independent review. Longer checks,
builds and deployment observation use fresh catalog-policy utility watchers.

Documentation readers: runtime maintainers and operators. Lasting behavior and
compatibility belong in dev-workspace's existing session/recovery guides;
this specific recovery and deployment belong in this initiative's rollout.
