# Coordinating shared resources

The selected user-profile runtime provides
[resource claims and notifications](https://github.com/aither64/dev-workspace/blob/master/docs/coordination.md).
Sessions acquire repository or machine ownership, run their own commands,
verify effects and explicitly release. Read `workspace-host coordination guide`
before using it. A predecessor without claims retains its installed job workflow.

## Session workflow

Complete implementation, history consolidation, checks and independent review.
Obtain the user's explicit direction for the affected repository/target or
machine/actions. Deployment approval never grants merge approval.

Prepare commands and dependencies in the session's own worktrees. Build and copy
large deployment artifacts before taking machine ownership when the tool supports
that separation. Acquire repository ownership before shared Git mutations,
including checkout hooks or reviewed signing that change common trust state.
The session runs ordinary hooks and resolves trust through the repository's tools.

Use `coordination acquire SESSION --as-is --request FILE` with a schema-1 request
containing a UUID `requestId`, `label`, and `repositories`/`machines` arrays.
Supply at least one registered repository or configured machine. The request
atomically returns `held` or `waiting`. A waiter owns no resources; the coordinator
notifies its retained conversation when the complete request is granted. End the
turn when only waiting remains. Read `claim-status` before acting on any notice.
A notice neither authorizes work nor proves command completion.

Run ordinary commands only while the claim is held. Keep machine ownership
through UI review, feedback and repeated deployment. Aitherdev system activation
and workspace profile selection share the physical resource `vpsfree:aitherdev`.
Use `release SESSION --as-is --id UUID` when finished or `cancel-claim` for an
unneeded waiting request. Retrying the exact acquire request returns the same
claim even after release; a new attempt needs a new UUID. Request all resources
together or keep separate claims disjoint to avoid waiting on your own ownership.

Claims do not expire when an agent becomes idle or disconnected. After an
interruption, inspect effects and stop remaining local/remote work before release.
Held claims block lifecycle cleanup until explicitly released. A machine release
needs no integration proof; session completion still requires exact final heads
integrated and all work finished. Existing legacy reservations keep their original
completion requirements. Never release another session's resources or edit records.

The Operations page shows owners and waiters; machine claims also appear in the
session Reservations tab. This is cooperative locking. Ordinary project tools do
not intercept arbitrary commands. Participating sessions must acquire the required
resources before mutation and keep ownership until the work is safe to release.

## Git and deployment

After explicit merge approval, use normal fast-forward integration and non-force
SSH pushes under repository ownership. Create only the target worktree the session
needs; retain feature refs and remove disposable worktrees when safe. Verify hooks
and resulting refs: Git can exit zero after a failing post-merge hook.

The shared workspace stays on master. Preserve unrelated files/index changes and
use its ordinary `dev-session-tracking.lock` for tracking commits in addition to
repository ownership. A resource claim is metadata, not an acquired OS file lock.

Use confctl channels for inputs. Preserve the direct nested runtime override,
extension selection and matching configuration runtime. Run
`bin/check-dev-workspace-deployment` against final locks. The application stays
in its user profile. For ordinary `workspace-host switch --source PATH`, hold the
configured machine claim and pass `DEV_WORKSPACE_CLAIM_ID` plus the exact session
environment identity. Workspace-host owns compatibility, activation journals and
forward recovery. The configuration repository's operations guide owns concrete
machine deployment steps. Runtime selection and default-branch integration retain
their applicable explicit authorization gates.

## Retained operations

Existing snapshot-based jobs, integrations, deployment history, reservations and
uncertain attempts keep their original recovery procedures. New claims cannot
release their reservations or replace evidence. A retained job's preparation
supplies its exact `legacyJobId`; integrations resume by their original ID.
Never submit a replacement job to hide an uncertain effect. Legacy bootstrap
operations retain their dated recovery procedures. The generic package installs
the retained integration guide alongside current coordination/recovery guides.
