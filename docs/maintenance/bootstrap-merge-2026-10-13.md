# Threadless installation integration, 2026-10-13

This dated, source-only route completes the coordination installation owned by
`2026-10-13-workspace-coordination`. It is not installed, exported through Nix,
exposed in the portal or used by automatic workers. Ordinary bootstrap selectors
still cannot prepare, approve or submit new work. Managed sessions use the normal
[coordinator](../coordination.md).

The initiating user authorized the four repositories' master integrations after
the session-creation fix was deployed. The helper binds that condition to frozen
successful deployment evidence. It uses the same retained threadless owner and
reservation. Each operation integrates one reviewed repository, head and target.
It creates no conversation, transfers no ownership and never deploys or releases
a machine. The selected runtime owns snapshots, receipts, claims, workers,
fast-forward Git integration, hooks and independent reconciliation.

## Prerequisites

Read the selected runtime's complete coordination and recovery guides with
`workspace-host coordination guide`. Read the Git, lifecycle and verification
procedures and complete ordinary final history/review/verification gates.
Capture comparisons before each integration; retain feature refs.

Finish the creation-fix deployment first. Its driver units and all owned jobs
must have settled successfully. Keep the same reservation in deployed_review.
Freeze a plan beneath the owned tracking directory containing schema 1, workspace,
workspaceName, slug, ownerId, reservationId, selectedPackage, profileToken,
catalogDigest, repositories (names mapped to exact head and full target), evidence,
deploymentEvidence and source. Source records the exact conditional user direction;
deploymentEvidence is a checksummed successful live-check result also included in
evidence. Include independent final review and exact verification evidence.
Workspace final head may descend from the deployed source when source-only code
leaves its application derivation identical; retain that equivalence evidence.

The helper accepts only this installation's owner, workspace, four repositories
and master targets. Run with the selected runtime's Ruby and declared Nix
environment. It loads the raw installed workspace-host from the selected profile,
not worktree runtime code. No state/profile/registry override or fixture mode.
Freeze and review the helper commit and application-derivation identity before
use. Exact plan and evidence hashes must remain unchanged for retries.

The lead holds a supervised maintenance window: start no other bootstrap deploy
or merge driver for this owner until serial integration finishes. A process lock
serializes this helper, and ordinary admission verifies there is no other pending
owner job. The process lock does not exclude the separate deployment bootstrap.
This route relies on the trusted lead's exclusion; it does not promise concurrent
bootstrap submission support. Other sessions keep their normal queue/resources.
If that exclusion cannot be guaranteed, stop and add a reviewed exact-job claim
interface to the owning runtime instead.

## Prepare, execute and retry

Use a fresh lowercase UUID P for a preparation request:

```json
{"schema":1,"requestId":"UUID-P","repository":"dev-workspace"}
```

Run the reviewed helper by its absolute path in the runtime repository's Nix
environment, retaining stdout and stderr separately. HELPER below is
`worktrees/2026-10-13-workspace-coordination/workspace/bin/bootstrap-merge-2026-10-13`
under the absolute workspace root:

```sh
ruby HELPER --plan PLAN --request PREPARATION --prepare
```

Preparation builds hooks and retains the target checkout outside admission locks.
Its result is the execution request with schema, a fixed UUID E and immutable
artifact ID. Save it exactly, then run:

```sh
ruby HELPER --plan PLAN --request EXECUTION
```

Use a parent-launched retained service for execution and a fresh verification
watcher to observe the wait. The driver reports the retained job ID before waiting.
Exit 0 with state succeeded identifies the completed merge and its remote proof.
Do this serially for runtime, extension, configuration and workspace. Register the
results in the initiating rollout/state. Each repository integrates separately.

Exact preparation retries return the retained bundle before rebuilding or making
another target checkout when no owned work is pending. Once its merge is pending,
retry the saved execution request E; preparation admission reports busy until
owned work settles. Execution retries reuse ordinary approval and submission
receipts, even after the target checkout has changed through successful integration.
An altered request with the same UUID refuses. Do not edit bundles or create new
IDs to avoid a pending claim. All new admission and claims recheck the selected
generation, active incarnation, lifecycle journals, reservation and supervised
owner exclusion. Hook preparation and worker/recovery waits hold no admission lock.

An interrupted driver does not stop accepted workers. Retry the exact execution
request: it consumes existing receipts and starts only the original independent
reconciliation service. Unknown effects retain the claim. A claim without durable
request.json retains the installed guide's operator-recovery requirement; this
helper never redispatches it. A package/generation change stops new admission;
ordinary retained-bootstrap reconciliation remains the recovery interface.

There is no refresh action. For an unclaimed needs_refresh result, preserve its
old evidence, cancel through the ordinary exact-owner command with current revision
and a fresh cancellation ID, then rebase/review/verify and prepare a new P.
Never cancel or replace an ambiguous claimed attempt to escape recovery.

## Compatibility and finish

This route uses the existing runtime schemas and worker envelope without
changing dependency pins. The
helper stores ordinary merge approvals/jobs, opaque bounded preparation receipts
and immutable artifacts through the selected engine. Existing readers can load
and reconcile them. Existing automatic workers still skip new bootstrap claims.
The application derivation must be identical before omitting another deployment.

Successful merges do not finish deployed review or release aitherdev. The original
reservation and deployment history remain held. Normal finish still requires exact
final/deployed integration proofs, settled operations and explicit user direction
that deployment/review is finished. Archive, delete, reboot and exceptional release
are outside this route.
