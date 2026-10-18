# Execution policy and verification brief

The lead owns this design and application implementation. Add a package-wide
execution override rather than changing role access or rewriting retained state.

## Interfaces and invariants

codex-web ThreadPolicy gains optional ApprovalPolicy (only empty or never), and
accepts danger-full-access alongside existing sandbox modes. Explicit policies
serialize both values on thread start/resume/fork. Default callers and immutable
retry records retain their existing meaning.

Catalog schema 6 requires execution_access: full_access. Schemas 4 and 5 omit it
and continue role sandbox behavior. Canonical catalog digests include the field;
team digests include it only for schema 6. Role access remains the historical
source responsibility setting, and roster/creation/ledger layouts do not change.

All CLI and browser member turn constructors must load the selected immutable
package catalog and apply the override. Cover initial creation, fork, direct
assignment, browser send, queue start and reconciliation. Never mutate an active
turn or silently change options of an uncertain submission. Runtime construction
must not accidentally leave CLI assignment on an unconfigured catalog.

Generated native role and utility TOMLs for full-access packages carry
sandbox_mode = danger-full-access and approval_policy = never. Model and effort
remain explicit caller settings. Legacy generation stays unchanged. Monitor
instructions require explicit CLI full-access options and no socket writable-root
workaround. UI projections show effective access without mutating retained data.

Existing CLI peer delivery supports a ready same-roster sender/recipient with
stable IDs; no new messaging service is needed. report_to_lead remains bound to
the native caller and lead. Preserve remote-client authentication, exact origin,
session ownership and coordination approval/reservation checks.

## Compatibility and operations

No database or persisted session migration. New catalogs require a compatible
package; existing catalog readers reject schema 6. Profile switches remain
forward-only. Match workspace's nested runtime selection and configuration's
dev-workspace/devWorkspace input. The Codex version remains unchanged. Build and
review before activation, preserve active turns under supported live switching,
and apply execution policy on subsequent turns. Recovery uses ordinary retained
operation receipts and the same reservation, never direct activation bypass.

## Acceptance and checks

Quick checks: focused Go policy/catalog/team/browser tests; protocol corpus
coverage; Ruby command/package contracts; syntax and Nix formatting checks.
Commit the intended deliverable, inventory full history and no migrations, then
independent general/architecture/scope/risk review. Long checks: packaged suites,
schema-4/5/6 generated catalog checks, isolated native lifecycle and member probes,
and exact aitherdev build. Fresh utility watchers own long checks.

Live acceptance must prove Nix daemon and declared-shell access, network and
owned temp writes outside the worktree in architect, implementer, reviewer and
watcher contexts. Test peer messages and replies, busy delivery, retry and resume
without duplicates. Repeat on the deployed package. Only after deployed success
merge all four approved master targets, verify exact deployed revisions integrated
and finish the machine reservation. Keep the session and feature refs.
