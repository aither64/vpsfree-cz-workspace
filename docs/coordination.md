# Coordinating merges and deployments

The workspace uses the selected user-profile runtime's
[coordinator](https://github.com/aither64/dev-workspace/blob/master/docs/coordination.md).
Its deterministic queue serializes small authorized mutations. Sessions prepare
their branches, reviews and builds independently. The catalog in
`config/coordination.nix` identifies canonical repositories and physical machines;
the extension supplies the immutable confctl adapter.

Read the runtime contract and its
[operations guide](https://github.com/aither64/dev-workspace/blob/master/docs/coordination-operations.md)
in full before submitting or recovering an operation. These procedures preserve
the existing merge, deployment, session-ownership and mandatory-review gates.

## Agent workflow

For a completed reviewed deliverable, prefer the installed runtime's
[integration driver](https://github.com/aither64/dev-workspace/blob/master/docs/integration.md).
Freeze the original review and check receipts, then provide the actual integration
and deployment directions in its request. The driver batches dependent merges,
refreshes proven mechanical changes and publishes compact completion records.
Conflicts and substantive changes return to the lead for applicable review.
The existing individual commands remain the recovery interface.

`config/integration.nix` selects the nested workspace runtime and configuration's
confctl channel. The extension supplies the immutable `workspace-pins` recipe.
The workspace pin remains a direct nested override; configuration still selects
the matching host module separately from the application profile.

1. Keep the initiative's own branches and worktrees. Complete implementation,
   history consolidation, quick checks and independent review. Run longer checks
   under the verification procedure. Rebase and rebuild outside coordination
   claims; preserve reviewed approval scope according to the Git procedure.
2. Prepare the exact operation with session-owned checksummed evidence. Record
   actual user approval for its repository/target or machine/actions. Deployment
   approval never becomes merge approval.
3. For the first deployment, request its machine reservation near completion of
   preparation. List every affected integration obligation. Aitherdev system
   activation and application profile selection share `vpsfree:aitherdev`.
4. Submit the returned snapshot, approval, reservation and explicit dependencies.
   Merge-only work needs no machine reservation. Read status and keep doing useful
   independent work while claims or reservations are busy.
5. Prefer `coordination integrate --background` for approved operation batches
   when this conversation matches the retained managed lead. Background admission
   verifies the recipient and checks every local/remote default branch before
   accepting a run. For an external conversation, supervise foreground integration
   under an attached observer, or deliberately select `--to-session-lead` to hand
   responsibility to the managed lead. A delivered notice alone does not prove
   pickup: acknowledge its event/generation from the matching conversation and
   renew the acknowledgement while handling it. Follow the installed integration
   guide for exact commands and preparation-only cancellation.
   Record its run ID. After verified background handoff, if only waiting remains, end the turn; the worker continues
   and the coordinator wakes the retained session when agent action or review is
   needed. Reread authoritative status on that message. Individual submitted jobs
   also run independently and retain their native notifications. Do not poll
   reservations, ask the user to restart the agent, or bypass a busy resource.
   A stale snapshot requires fresh preparation and applicable verification/review;
   an uncertain effect requires reconciliation.
6. Keep the machine reservation during UI review, feedback and redeployment,
   including periods when the session's agent is idle. Normal completion releases
   it after exact final integration proofs and explicit deployment/review completion.
   Successful archival also releases the session's reservations after cleanup;
   failed archives retain recovery holds. Keep the initiative active for follow-up
   unless the user requests archival or the enabled automatic policy applies.

Use `dev-session coordination status SLUG --as-is --json` for authoritative job,
reservation and delivery state. The workspace menu's Operations page gives a
bounded read-only view and links to blocking owners. Session-list badges identify
held machine reservations, including idle review and recovery. A notification supplies no approval.
It preserves the receiving thread's retained settings and policy.

## Git integration

After explicit integration direction, prepare and submit a `merge` job for each
named repository/target. Use dependencies for required cross-project order.
The runtime prepares a private target checkout, runs ordinary `git merge --ff-only`
and a normal non-force SSH push under the brief claim, with repository hook
dependencies already prepared in its Nix environment. Feature refs remain.

The shared workspace stays on master. Its feature merge uses the existing
`dev-session-tracking.lock`, preserves unrelated index/files and refuses overlap.
A new tracking commit invalidates a previously prepared baseline. A certified
refresh over tracking records preserves the original review when reconstruction
and complete input identities prove the applicable equivalence. Tracking-only
commits retain their existing approval exemption, but must use the same lock for
shared staging/commit operations. Never reset, clean, stash or switch the shared
checkout to force an integration.

If the installed command/catalog cannot coordinate the required operation, stop
that mutation and resolve the package/configuration mismatch. Do not fall back
to direct Git or confctl activation around another owner's reservation. Manual
operator commands and pre-contract store binaries are outside enforcement.

## Deployment and recovery

Manage configuration inputs with their confctl channels and preserve the
workspace's nested runtime override. The matching system module/runtime and
application profile come from the configuration and workspace feature branches.
Run `bin/check-dev-workspace-deployment` against the composed final locks.
The application remains in its user profile.

The configuration's
[aitherdev operations guide](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/master/docs/operations/workspace-coordination-aitherdev.md)
owns machine-specific rollout and recovery. The initial pre-contract installation
uses the reviewed candidate's bounded synchronous bootstrap. It creates no Codex
thread. Retained bootstrap-owner maintenance requires its explicit UUID and the
same active tracking incarnation; it cannot submit new unattended jobs.

The [dated integration procedure](maintenance/bootstrap-merge-2026-10-13.md)
covers the initiating threadless installation's authorized master merges. Its
reviewed source-only helper uses the selected runtime's existing workers and
receipts under a supervised exclusion of other bootstrap operations. It is
limited to that installation and keeps the machine reservation held for review.

Keep failed or interrupted attempts, deployed artifacts and GC roots. Archive,
delete, suspend and auto-archive do not free deployed ownership. A profile failure
after selection recovers forward under its original attempt. Ambiguous remote
activation remains a visible blocker. Informational Codex status messages retry
independently and do not hold machine ownership. There is no forced
release or blind replay. An exceptional ownership transfer/removal requires a
separate explicitly authorized reviewed recovery operation.
