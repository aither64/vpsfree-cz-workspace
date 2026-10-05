# Repeated VPS deletion investigation

## Goal and scope

Investigate three user-supplied API exception emails and suggest a solution for
repeated VPS deletion requests. This request authorizes investigation and a
proposal, not implementation or production changes. Keep raw email files in
portal upload storage, outside version control; record only sanitized evidence.

## Affected repositories

- vpsadmin: API lifetime transitions, transaction locking, and PHP WebUI deletion.
- HaveAPI/client behavior may be inspected as supporting read-only context.

Read canonical bare repositories; no feature branches or worktrees are needed.
The initial vpsadmin baseline is 9fc0648accd414246d6422e67106ae7217486020.
Compare deployed revisions identified in the emails before attributing behavior
to current source.

## Approach and ownership

The Full-team architect (architect0, retained Astra/xhigh, workspace_write)
owns the diagnosis and proposal in design.md. The lead compares sanitized email
facts, checks the proposed contract, and maintains tracking. No application edit
or automatic final review assignment is intended for investigation alone.

## Compatibility and deployment

Evaluate API response/state tracking, retries, account authorization, soft versus
hard deletion, concurrent requests, rollback and existing transaction locks.
Prefer no schema, persistent-format or node protocol changes. Any proposal must
allow old clients and mixed API/WebUI revisions; preserve intentional admin
soft-to-hard deletion. No deployment is authorized or performed in this phase.

## Documentation

Readers are the requesting maintainer and future implementer. Keep diagnosis,
uncertainties and verification brief in session design.md and evidence in state.md.
Application documentation will be considered if implementation is requested.

## Verification plan

Trace each supplied stack through the deployed source and current baseline.
Separate code-proven behavior from inference about prior requests and production
chain outcomes. Specify acceptance tests for repeats, concurrency, authorization,
expiration preservation, admin escalation and transaction failures. Runtime
reproduction and integration tests are deferred to an implementation phase.
