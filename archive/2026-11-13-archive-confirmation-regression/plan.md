# 2026-11-13-archive-confirmation-regression

## Current delivery

The authorized provider helper fix is deployed on aitherdev and merged into all three approved master branches after verification. Runtime9241a342, workspace5cde17b6 and configuration11197387 are the exact final heads. No Archive behavior changed. See state.md and rollout.md for final checks, paths and released ownership. Automatic post-merge CI43708559408 passed; delivery is complete and session stays open. Earlier investigation-only restrictions below describe historical phases; the explicit implementation and rollout authorization supersedes them.

## Goal

Clicking on the "Archive" button used to open up a confirmation prompt. I suppose that session 2026-11-11-session-archival-failures removed it, but that is not what I wanted. Investigate and suggest a solution.

Follow-up: the user accepted the existing Archive retry behavior ("aha, so that's ok") and requested investigation of a session-scoped provider-switch failure. UI failed at "Waiting for session access", 0 of 1 threads, elapsed 1s, with `native locking-sessions failed`. No Archive implementation is requested.

## Affected repositories

- `dev-workspace`: expected owner of the portal Archive action and lifecycle API.
- Follow-up: `dev-workspace` provider-switch orchestration/native CLI; `codex-web` only if its client contract is implicated.
- Workspace coordination records only; no application edits are authorized by this investigation request.

## Approach

Trace current Archive click/confirmation/request handling and directly relevant canonical repository history. Compare the browser flow with the documented one-confirmation contract. Distinguish a removed prompt from a prompt that is present but malfunctioning. Preserve exact source revisions and uncertainties in [design.md](design.md).

Architect owns bounded investigation and the proposed solution. Lead accepts evidence and reports the recommendation; implementation remains a possible follow-up.

Provider follow-up: architect traces preparation -> native locking-sessions invocation/exit contract and current installed source, then relevant history. Source first; no retry, target mutation or peer-owned file access. A safe disposable reproduction may be allocated separately after effects are known. Preserve confidence limits if the supplied generic error hides its original cause.

Root-cause continuation: user explicitly requires identifying the cause and clarifies the session is active with working threads. Active switching is supported intent; do not recommend idleness as the fix. Architect owns active-turn read/cancellation/order analysis (D). Implementer0 owns a disjoint isolated idle-versus-working-thread scoped-prepare reproduction (E), with exact underlying error capture in synthetic state and no full switch. Diagnostics-only findings are insufficient for this milestone. Keep real session/provider/routing untouched.

Root cause established: the raw provider client omits the workspace's vscode thread-source allowlist, so valid monitor utilities fail automated bootstrap identity proof. Correcting that option in the read-only diagnostic exposes a second omission: scoped helper launch lacks canonical Codex home. Supplying both existing workspace inputs makes the same utility's four validation gates pass. Minimal proposed product remedy is explicit ThreadSourceKinds in the intentionally raw no-resume/no-resolver client plus the existing workspace-specific capture_env! boundary for scoped subprocesses. Preserve all provenance/refusal checks and active switching; no data migration or idle-only policy. Functional fix is not assigned during root-cause investigation.

## Authorized implementation and rollout

User direction: "all right, implement fix, aitherdev can be deployed using vpsfree-cz-configuration, merge after verification". Implement the two helper boundaries with regression coverage; publish feature heads, independently review the committed full series after quick checks, then run required longer verification. Prepare matching workspace/runtime and configuration devWorkspace pins while preserving extension/sibling inputs. Build/copy before aitherdev ownership; deploy system configuration as needed and application via its user profile under the held machine claim. Verify deployment and active preparation in isolated fixtures; integrate the verified dev-workspace/master, workspace/master and vpsfree-cz-configuration/master changes with separate short repository claims. Record exact input/store/lineage evidence and promptly release aitherdev once verified and all deployed lineage is integrated. Leave session open; no lifecycle cleanup authorized.

G owner implementer0: functional source/tests/quick checks/commits/review fixes in clean dev-workspace worktree. H owner implementer1: workspace/config graph preparation now, pins/commits after G's published final head. Architect owns H dependency/deploy brief and material design clarification. Lead owns review invocation, checks orchestration, machine deployment, integration and records.

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
