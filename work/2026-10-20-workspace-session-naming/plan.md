# Reliable workspace session naming

## Goal and authorization

Implement reliable automatic session naming with one 30-second total deadline,
bounded automatic recovery, and manual slug entry after ultimate failure. Never
silently allocate a generic or heuristic fallback identity. User authorized
implementation of the final plan and aitherdev deployment via
vpsfree-cz-configuration. No default-branch integration is authorized.

## Affected repositories

- codex-web: retry notifications and safe terminal retry eligibility.
- dev-workspace: naming orchestration, fallback removal, tests/docs and client pin.
- workspace: composed package selects the corrected exact runtime.
- vpsfree-cz-configuration: matching dev-workspace/devWorkspace channel pin and
  aitherdev host configuration deployment; application remains in its user profile.

## Backlog and ownership

| Owner | Expected result | Acceptance and checks | Dependencies |
| --- | --- | --- | --- |
| architect0 | Final design.md and contract | 30s policy, interfaces/ownership, boundaries, compatibility and checks | Read current baselines |
| implementer0 | codex-web execution package | Native willRetry progress; typed CanRetryEphemeralTurn; tests/docs, hooks, commits/publication | Saved final design |
| implementer1 | dev-workspace execution package | No generic fallback; <=2 calls, preserved inputs/manual recovery; tests/docs, hooks, commits/publication | Saved design; A accessor for integration |
| Assigned implementer | Dependency and deployment inputs | Exact corrected client/runtime pins; final lock consistency and package checks | A+B |
| reviewer0 | Independent final committed-deliverable review | Whole branch history, final diffs, migration and pin consolidation conclusions | All commits and quick checks |
| lead | Tracking, acceptance, review and rollout coordination | Evidence, correct claims, system then profile, real provider smoke check | Reviewed and verified deliverables |

## Accepted behavior

One absolute 30-second deadline starts before semaphore acquisition and includes
queue wait, native retry, at most one fresh utility retry, 200ms cancellable
backoff and cleanup. Hold the existing two-operation capacity slot throughout.
A fresh call needs proven transient failure, settled execution and cleanup, plus
at least one second inference and 250ms cleanup remaining after backoff.
Native willRetry notifications remain on the same owned turn. Never duplicate
an uncertain turn/start or retry based on provider message text.

Successful naming proceeds immediately. Ultimate failure leaves Base/Slug/Handoff
empty and reuses Retry naming/manual-name entry with accepted goal, uploads,
provider/settings and request identity preserved. Existing allocated slugs remain
immutable. Attachment-only automatic requests require manual entry.

## Compatibility, deployment and recovery

Preserve existing preparation, manifest, receipt, roster, journal and database
formats, current Codex version and public Go call signature/errors.Is categories.
Safe retry eligibility is an additive client accessor. No migrations, PHP changes,
fleet rollout or session renaming. Existing consumers remain compatible; old
writers retain their old policy until updated.

Publish exact client and runtime revisions. Preserve the workspace extension and
direct nested runtime selection; configuration selects that same runtime through
its dev-workspace/devWorkspace channel. Check composed locks, build exact final
commits, obtain the physical vpsfree:aitherdev claim, dry-activate/switch the host
without reboot, then select the workspace application profile. Verify actual
system/profile/package identities and conversation continuity. Follow the selected
runtime's retained ownership and forward-recovery contracts. Keep feature branches
unmerged absent explicit repository/target integration approval. Leave this session
open; no archive/delete/stop is authorized.

## Documentation and verification

Architect owns the technical brief. Implementers update owning project contracts
and naming recovery/timing documentation; lead applies any context-dependent
user-facing writing. Keep individual rollout revisions/logs in this session.

Quick focused tests and hooks precede committed final independent review. Inventory
complete base-to-head histories, superseded pin streams and no-migration provenance.
After review, fresh Luna/low watchers run long native protocol/ownership fixtures,
packaged creation/browser checks, applicable flake checks and builds. Exercise
retry-then-success, settled-failure-then-fresh-success, shared30s exhaustion,
cancellation, uncertainty, production adapter/manual recovery/replay, creation
during collection and preparation/package exclusion. Real selected-provider
naming and health/continuity smoke checks are required after deployment.
