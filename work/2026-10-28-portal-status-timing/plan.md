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
