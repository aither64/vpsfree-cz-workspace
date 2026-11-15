# 2026-11-13-archive-confirmation-regression

## Goal

Clicking on the "Archive" button used to open up a confirmation prompt. I suppose that session 2026-11-11-session-archival-failures removed it, but that is not what I wanted. Investigate and suggest a solution.

## Affected repositories

- `dev-workspace`: expected owner of the portal Archive action and lifecycle API.
- Workspace coordination records only; no application edits are authorized by this investigation request.

## Approach

Trace current Archive click/confirmation/request handling and directly relevant canonical repository history. Compare the browser flow with the documented one-confirmation contract. Distinguish a removed prompt from a prompt that is present but malfunctioning. Preserve exact source revisions and uncertainties in [design.md](design.md).

Architect owns bounded investigation and the proposed solution. Lead accepts evidence and reports the recommendation; implementation remains a possible follow-up.

## Decisions

- Investigate and suggest only; do not implement or execute archival to reproduce it.
- Inspect ordinary repository history, without accessing the suspected peer session's files, worktrees, team or transcript.
- No session lifecycle changes, package switches, deployment, integration or cross-session messages.

## Compatibility and deployment

The proposal must preserve one explicit user confirmation, cancellation without mutation, and existing archive recovery/async operation behavior. Assess browser/server compatibility; no schema or migration change is expected. Deployment is outside this request.

## Documentation

Readers are the user and a future implementer. Findings, evidence and proposed acceptance checks belong in this session's design.md; current phase and ownership belong in state.md. No reusable project documentation change is planned during investigation.

## Testing plan

Read-only inspection of handlers, relevant tests and history. No live Archive clicks or destructive reproduction. Proposed implementation checks must cover opening the prompt before any request, cancellation, and a single confirmed request.
