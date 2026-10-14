# 2026-10-14-archive-complete-investigation

## Goal

Explain the failed explicit archive of
`2026-10-05-network-ipv4-left-counter`, which reports
`initiative lifecycle is complete; cannot archive it as archived`.
The requested scope is diagnosis. Runtime changes and archival are separate
actions; preserve the affected session's records, worktrees and lifecycle.

## Affected repositories

- `dev-workspace`: inspect the installed Ruby lifecycle executor, matching
  upstream implementation, recovery documentation and archive tests.
- Coordination workspace: investigation tracking and a reusable diagnostic note.

## Approach

Trace the reported error through explicit archive policy, tracking projection
and lifecycle conversion. Reproduce it through the installed pure conversion
helper, using the actual session state as read-only input. Establish the change
that introduced the mismatch and identify the missing regression coverage.

## Decisions

- Use a separate threadless investigation session because this conversation has
  no environment or trusted developer binding to an existing development session.
- Keep application code unchanged under the requested investigation scope.
- Do not work around the failure by changing the affected session's valid
  completed lifecycle or by selecting strict completion archival.

## Compatibility and deployment

Diagnosis changes no database, API, protocol, configuration, persisted runtime
format, package generation or deployment. A future fix must permit valid source
lifecycles to become `archived` for explicit archival, while preserving strict
completion/discard policy, anchored lifecycle validation and journal retry
identity. Add end-to-end explicit-archive and revival coverage for completed
and abandoned inputs before deploying that fix.

## Documentation

Readers are the local operator and lifecycle maintainers. Preserve the concrete
failure and implementation mismatch in a reusable `notes/dev-workspace/` note;
keep this investigation's evidence and completion status in its own state.
Existing runtime lifecycle documentation already describes the intended behavior.

## Testing plan

Load the selected immutable package's Ruby implementation without executing its
CLI. Allocate a runner without runtime initialization and invoke only the pure
tracking lifecycle conversion. Exercise active, complete, abandoned and archived
input and reproduce against the actual affected state file. No archive, build,
integration test or deployment is required for diagnosis.
