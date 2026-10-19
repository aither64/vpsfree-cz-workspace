# Handoff for sessions already running

The merge/deploy coordinator is installed and active. The installation's
aitherdev reservation has been released. Keep your current initiative, worktrees,
branches, Codex conversation and retained team settings. Use the stable installed
commands; no session restart is required to read the guide or submit operations.

## Read current guidance and verify your own identity

Read `/home/aither/workspace/ai/vpsfree.cz/AGENTS.md` and its applicable routed
procedures, then `/home/aither/workspace/ai/vpsfree.cz/docs/coordination.md`.
Read both installed runtime guides with:

```sh
workspace-host coordination guide
dev-session current
```

Verify that `current` matches your own complete DEV_SESSION_SLUG and
DEV_SESSION_WORKSPACE identity or trusted thread binding. Use YOUR verified
slug below. Do not copy the installation session's slug, owner or reservation.
Use the session's existing registered repositories and exact configured targets.

## Prepare independently; coordinate only the final mutations

Continue implementation, input updates, rebasing, reviews, builds and tests in
your own worktrees. Do these before taking merge claims or reserving a machine.
Use the usual verification watcher for long preparation/build operations.
Publish feature branches normally. Capture the final branch comparison.

Default-branch integration and deployment still need their existing explicit
user authorization. Preserve an authorization already given in your session;
record its actual quote, scope and source rather than asking for it again.
A notification or deployment approval supplies no new merge authorization.

Read your authoritative state:

```sh
dev-session coordination status YOUR-SESSION --as-is --json
```

Keep checksummed review/verification evidence and saved JSON request/result files
under your own `work/YOUR-SESSION/`. Every new request uses `schema: 1` and a fresh
lowercase UUID `requestId`. Exact retries reuse the saved request unchanged.
Use the response's actual `id` for approval/job/reservation references; the
request UUID is not the resulting record ID.

## Merge

1. `prepare`: request `kind: "merge"`, the registered `repository`, and nonempty
   checksummed `evidence`. Save the complete returned snapshot.
2. `approve`: request `kind: "merge"`, exact repository/full-target-ref scope,
   `reviewedSnapshot` equal to the snapshot's `id`, and the actual user instruction.
3. `submit`: use `kind: "merge"`, the full saved snapshot, returned `approvalId`,
   `dependsOn` for earlier same-owner jobs when order matters, and
   `reservationId: null`. A merge job never acquires a machine reservation.
4. Wait for the job's actual `succeeded` state and remote proof; command exit zero
   can mean only admission. The worker performs the fast-forward and normal SSH
   push, with hooks prepared before its brief claim. Do not integrate or push
   default-branch feature content around the coordinator.

Command sequence, with your saved request files:

```sh
dev-session coordination prepare YOUR-SESSION --as-is --request PREPARE.json --json
dev-session coordination approve YOUR-SESSION --as-is --request APPROVE.json --json
dev-session coordination submit YOUR-SESSION --as-is --request SUBMIT.json --json
```

## Deploy and reserve the machine through review

Prepare `machine_activate` with the catalog target and evidence from your
registered configuration branch. Prepare `profile_activate` separately when
updating the workspace application from your registered workspace branch.
The system configuration and user-profile application are separate operations.

For aitherdev, the catalog target is `aitherdev`, physical identity is
`vpsfree:aitherdev`, and confctl selector is
`cz.vpsfree/machines/aitherdev`. System and application deployment share that
same reservation. These identifiers are aliases/contracts, not interchangeable
request field names.

After preparation and actual deployment approval, request `reserve` near the
first deployment, with `target`, `mode: "deploy_first"` (or `"integrated"` when
appropriate), returned deployment `approvalId`, and all repository/full-target
`integrationObligations`. Record the returned reservation ID. A reservation
request is granted with its eligible first operation; requesting one is not
proof that you hold the machine yet.

Submit each deployment with its exact snapshot, appropriate approval, same
reservation ID and explicit dependencies. If system then application ordering is
required, the profile job depends on the system job. Approvals bind prepared
snapshots; retain the correct approval for each operation. The installed guide
owns the exact request formats.

```sh
dev-session coordination reserve YOUR-SESSION --as-is --request RESERVE.json --json
```

Keep the reservation while the user reviews the deployed UI, gives feedback or
you iterate and redeploy. Another session may build or merge while its deployment
waits. Idle time, successful deployment and successful integration do not release
ownership. Iterations still need applicable authorization and fresh exact evidence.

When deployment/review work is finished and every exact final/deployed revision
is integrated, call:

```sh
dev-session coordination finish YOUR-SESSION RESERVATION-ID --as-is --request FINISH.json --json
```

The request declares `deploymentWorkFinished: true`, includes current
`expectedRevision`, nonempty completion `evidence`, and every exact registered
`finalHeads` repository/full-target/head tuple. Rebased nonancestor deployed
sources require the installed guide's canonical replacement-lineage evidence.
Preserve original refs/artifacts. Explicit user acceptance or a direction that
no UI review is required counts toward finishing the review work; do not keep a
machine reserved after the user has directed normal release and proofs pass.
Finish verifies remote integration and live identities and publishes the machine's
integrated frontier. A subsequent deployment must include those integrated changes.

## Waiting, stale work and recovery

Keep the turn open while waiting on another owner. Continue independent work;
when only waiting remains, use an interruptible tool wait of at most 60 seconds,
then reread status after a coordinator notification. Do not ask the user to
restart your turn merely because a resource is occupied. Notifications steer
busy threads or start a turn on idle retained threads using their saved policy.

For `needs_refresh`, rebase/update inputs, resolve conflicts, repeat appropriate
verification, preserve authorization only when the reviewed scope still matches,
and prepare a fresh snapshot outside claims. Refresh the unclaimed job with a
new request UUID and its current revision. Capture comparisons again after head
changes. Do not rebuild or resolve conflicts while holding the execution claim.

For interrupted/uncertain execution, identify the exact original job/attempt and
use ordinary reconciliation. Workers survive portal/coordinator restarts. Never
create a replacement job or replay activation to escape an uncertain effect.

```sh
dev-session coordination reconcile YOUR-SESSION JOB-ID --as-is --json
```

Use stable commands from the installed profile. Do not use old store binaries,
direct confctl activation/SSH, private ledger edits or the dated threadless
installation bootstrap helpers to bypass ownership. If your identity, catalog
or selected generation is stale, resolve it rather than impersonating another
owner. A missing operation capability requires resolving the installed contract.

## Inspect coordination in the UI

[Operations](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/operations)
is in the workspace menu above Automatic archival. It shows reservations, active
work and recent completed results. Session cards show machine/count badges with
tooltips; each session's Reservations tab shows its ownership and related work.

This handoff describes the installed workflow and supplies no new authorization
for another session's merges, deployments, release or lifecycle changes.
