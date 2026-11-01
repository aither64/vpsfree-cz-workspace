# Portal conversation status and submission repair

Investigate and fix unavailable Codex timing/status for
`2026-10-22-limit-autostart-alerts-to-boot` and the failed original message
`yes go ahead` for `2026-10-17-confctl-rust-rewrite-plan`. The user authorizes
retrying that message after repair and deploying aitherdev through
vpsfree-cz-configuration if needed. Default-branch integration is not authorized.

Scope initially includes dev-workspace, codex-web if its transport is responsible,
and configuration/workspace composition only if deployment requires changes.
Inspect the live service, native writer ownership, activity and submission errors
before selecting the smallest corrective change. Preserve both target sessions'
records, conversations and active work; use supported controls for recovery.

Compatibility: preserve thread identities, durable submission deduplication,
timing history, session manifests and lifecycle journals. Avoid restarting active
unrelated conversations. Assess mixed native versions and client ownership before
any operational change. Persisted-format changes are not expected.

Verification: capture the failing path, add focused regression coverage for any
code change, pass quick checks, commit and independently review before long tests.
Deploy only reviewed required changes, then verify live timing, status and message
acceptance without duplicate delivery. Record actual evidence and deployment/recovery
steps here; lasting behavior belongs in the owning project's existing guides.

This initiative was created by this conversation with `dev-session start
portal-status-timing --no-attach --no-codex --json`. It has no retained team;
lead owns diagnosis and bounded repair, with mandatory independent final review
for substantive deliverables and utility watchers for long verification.

## Accepted implementation

The user selected private portal state, Codex 0.165.0 and independent portal
settings/login, then authorized implementation. Stock CLI retains ~/.codex;
portal uses ~/.local/state/dev-workspaces/codex-homes/vpsfree-cz. Existing portal
tmux clients remain supported. All native launch/helper paths must agree on this
home, SQLite and log paths; inherited stock configuration must not override them.

This is the only installation. Migration is a one-time operational job, not a
permanent project command or compatibility framework. Preserve source and recovery
instructions with the rollout. Partition exact registered roots, retained team
threads and native dependencies; leave unknown/unowned history in stock. Preserve
thread IDs, complete native history, relationships, queues/goals, attachments,
submission receipts, timing and lifecycle state. Do not copy locks/sockets/PIDs or
stock remote-control enrollment into the new portal home.

Prepare independent portal authentication before downtime. Use a detached systemd
user job with durable phase/status/recovery, wait for both backends' active turns,
exclude new writers, checkpoint databases, validate staged homes and publish with
same-filesystem renames. Keep the original home as a backup. Reserve at least
20 GiB free after a conservative 40 GiB migration allowance; remeasure after builds.
No backup deletion, active-turn interruption or default-branch integration is
approved. Before publication restore original availability on failure; after
publication recover forward without overwriting new writes with stale state.

Affected repositories: codex-web (0.165 protocol/naming), dev-workspace (private
state and packaged runtime), workspace (composed application), and
vpsfree-cz-configuration (host contract/system package). Preserve the selected
extension revision. Deploy through configuration then the user application profile
under the ordinary aitherdev claim and transition contracts.

Quick checks and committed deliverables precede independent final review and
long native/package/migration checks. Verify every inventoried thread is readable,
portal/stock isolation, tmux, providers, naming, team and recovery behavior, both
reported sessions, then reconcile and retry the original message with its original
client ID exactly once. Publish feature branches; integration needs separate user
direction. Lasting behavior belongs in existing component guides; this individual
rollout and one-time migration belong in initiative operations records.
