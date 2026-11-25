# Exception root cause

## Goal and scope

Investigate the attached vpsAdmin API email reporting an ambiguous `detected_at`
ORDER BY column. Establish the failing request/query, root cause and relevance
on current upstream code; fix the defect if it persists. Keep the original email
outside version control and retain only sanitized technical findings.

## Affected repositories

vpsadmin is confirmed from the email and unchanged affected source on current
origin/master. Go, Rust and TypeScript clients require revision-specific no-change
assessment under the API contributor procedure. No integration or deployment is approved.

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

## Accepted brief and supporting assessment

[design.md](design.md) records the accepted root cause, scope, source lineage,
compatibility and verification brief. Implementer1 owns the required client
freshness comparisons using implementer0's final committed API export, under
each client repository's own guidance. Source edits remain restricted to the
incident-report resource and its existing request spec. Report unexpected
client drift before adding application scope.

## User-requested rule correction (supersedes client follow-up)

User rejected unrelated SDK refresh and requested improvement of the blanket
rule. D cancelled; no client commits/push, exact original sources restored.
Final6c16d045 changes only ordering/specs plus authoritative contract-first
synchronization procedure and routing label. Declaration-neutral tasks now
record exact-revision source assessment and stop before any export/client
worktree/generation/comparison/refresh; unrelated baseline drift separate.
Actual contract changes retain full synchronization safeguards. Both committed
deliverables independently reviewed with no findings.
