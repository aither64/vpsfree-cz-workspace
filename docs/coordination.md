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

Develop independently in session-owned worktrees. Edits, commits, rebases,
dependency updates, feature pushes, hook preparation, tests and review take no
repository claim. Prepare the clean target checkout and its dependencies first;
obtain merge approval before requesting ownership. Repository tools own hook
trust and ordinary Git locking. Keep hooks and signatures enabled.

Use `coordination acquire SESSION --as-is --request FILE` with a schema-1 request
containing a UUID `requestId`, `label`, and `repositories`/`machines` arrays.
Supply at least one registered repository or configured machine. The request
atomically returns `held` or `waiting`. A waiter owns no resources; the coordinator
notifies its retained conversation when the complete request is granted. End the
turn when only waiting remains. Read `claim-status` before acting on any notice.
A notice neither authorizes work nor proves command completion.

Run the shared merge or deployment only while its claim is held. Independent
feature commands remain available during a merge wait. Keep machine ownership
until deployment and integration are verified as described below. Aitherdev system
activation and workspace profile selection share the physical resource
`vpsfree:aitherdev`.
Use `release SESSION --as-is --id UUID` after the applicable release requirements
are met, or `cancel-claim` for an unneeded waiting request. Retrying the exact
acquire request returns the same claim even after release; a new attempt needs
a new UUID. Request all resources
together or keep separate claims disjoint to avoid waiting on your own ownership.

Claims do not expire when an agent becomes idle or disconnected. After an
interruption, inspect effects and stop remaining local/remote mutations before
considering release. Repository locks follow the short merge procedure below;
deployed machines follow the retention rule below. Held claims block lifecycle
cleanup until explicitly released. Session completion still requires exact final
heads integrated and all work finished. Existing legacy reservations keep their
original completion requirements. Never release another session's resources or
edit records.

The Operations page shows owners and waiters; machine claims also appear in the
session Reservations tab. This is cooperative locking. Ordinary project tools do
not intercept arbitrary commands. Participating sessions must acquire the required
resources before mutation and keep ownership until the work is safe to release.

## Machine retention

Promptly release each deployed physical machine once both conditions are met:

1. Deployment and its effects have been successfully verified.
2. Its complete deployed feature lineage is integrated into the approved remote
   default branches, including deployed dependencies.

The agent runs the normal release command without another user confirmation.
No separate UI acceptance or release direction is required. Missing integration
or failed/uncertain deployment keeps ownership. Idle time, feedback, review,
redeployment, disconnects and turn completion do not replace either proof.
Default-branch integration still needs its own explicit approval; deployment
approval grants no merge approval.

Retain the rollout and review receipts: physical machine and aliases, resolved
system and user-profile store paths, complete source/input graph, canonical
repository/target mapping, exact deployed and intended final feature heads, and
fresh remote ancestry proofs. For refreshed history, retain reviewed old/new
base/head ranges, range-diff or patch-equivalence evidence and migration lineage.
Do not call a nonancestor deployed commit literally merged. An independently
proven equivalent successor can establish integrated feature lineage; a
substantive successor requires its own verified deployment. Ordinary session
completion still requires every registered exact final feature head.

Before release, inspect authoritative status for the exact claim owned by this
session, reconcile known command effects and verify both conditions.
Promptly release that claim and verify its resulting state. The owner-only,
idempotent release API does not enforce this workflow. Do not edit claim
records or add release receipts to substitute for the evidence.
Release does not archive, delete, stop or clean a session. A later deployment
requires a fresh machine claim.

## Git and deployment

Acquire one repository only for the final target/feature/cleanliness checks,
ordinary fast-forward merge and hooks, non-force SSH push and remote verification.
Release immediately before CI, records, artifact registration or checkout cleanup.
Do not hold multiple repositories while integrating them sequentially. Stale
baselines or hook intervention return to unlocked preparation once commands stop
and effects are known. Reconcile uncertain shared mutations before release.

The shared workspace stays on master. Preserve unrelated files/index changes and
use its short `dev-session-tracking.lock` for shared tracking writes; independent
bookkeeping does not need a durable repository claim. Shared-checkout integration
acquires the repository claim first and then tries that tracking lock without
waiting; if busy, release the claim and retry after the writer finishes. Hold both
through the fresh target check, merge/hooks, push and remote proof. Preserve
unrelated dirty paths and index entries; disposable target checkouts must be clean.
A resource claim is metadata, not an acquired OS file lock. Keep machine reservations separate from merge claims;
build and copy artifacts before reserving a machine when supported.

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

Legacy lifecycle completion can automatically release reservations as part of
its existing implementation. That behavior grants no permission to archive,
delete or release a deployed machine before the retention conditions above.
No lifecycle action is implied by finishing work or preparing a handoff.
