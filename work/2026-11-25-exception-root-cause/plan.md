# Exception root cause

## Goal and scope

Investigate the attached vpsAdmin API email reporting an ambiguous `detected_at`
ORDER BY column. Establish the failing request/query, root cause and relevance
on current upstream code; fix the defect if it persists. Keep the original email
outside version control and retain only sanitized technical findings.

## Affected repositories

vpsadmin is the initial candidate; architect0 confirms scope from the stack and
current source before application changes. No integration or deployment is approved.

## Approach and ownership

Architect0 owns bounded investigation and the design/verification brief in
`design.md`. Implementer0 will own the resulting narrow fix, regression checks,
hooks, commits, publication and evidence after the brief is accepted. Lead owns
tracking, acceptance and independent-review invocation. Extra implementers remain
unassigned because there is one exception to resolve.

## Compatibility and deployment

Preserve API contracts, authorization, ordering semantics and persisted state.
Assess whether schema or client synchronization is affected before implementation.
Prefer a local query correction with no migration. Any rollout remains separate.

## Documentation and testing

Readers are maintainers diagnosing the exception. Session records hold findings,
verification and branch status; source comments or project docs only when useful
for a lasting invariant. First establish a faithful regression check, then run
applicable quick checks/hooks, commit all changes, obtain mandatory independent
review and run required longer verification. Publish the feature branch only.
