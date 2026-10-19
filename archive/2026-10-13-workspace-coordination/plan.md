# Workspace operation coordination

Implement the approved durable coordinator for concurrent development sessions.
Agents prepare independently; brief critical sections serialize repository
integration and deployment activation. Waiting sessions automatically continue
in their own Codex conversations without asking the user to resume them.

## Scope and decisions

- Generic scheduling, persistent job/reservation state, automatic notification,
  merge execution, profile activation, lifecycle integration and portal status:
  `dev-workspace`.
- Immutable confctl deployment adapter: `vpsfree-dev-workspace`.
- Agent procedure routing, canonical deployment target mapping, package
  composition and rollout records: this coordination workspace.
- Matching runtime selection and approved aitherdev deployment:
  `vpsfree-cz-configuration`.
- Reuse existing `codex-web` submission APIs unless precise design proves a
  missing required capability; do not change protocol versions incidentally.
- FIFO among ready mutations, with explicit dependencies and concurrent
  progress for unrelated resources. Preparation, conflict resolution, review,
  builds and long verification occur outside mutation locks.
- A deploy-first session retains its machine reservation throughout human UI
  review, feedback, idle turns, repeated fixes and redeployments. Only its final
  integration and finished deployment work normally release that reservation.
  Archive/cancel preserve unresolved deployed-state blockers.
- Merge-only sessions work independently. Manual deployments from the build
  machine are outside this work's scope.
- Keep existing merge/deployment approval rules. A runtime notification never
  supplies authorization. Material patch changes require renewed approval
  where current procedures require it.
- The user has authorized integration of this initiative's four repository
  branches into master after the provider-enabled creation fix is deployed and
  verified ("ok, after you'll deploy the fix, you can merge the changes").
  Retain feature refs. Deployment remains authorized through
  vpsfree-cz-configuration, without reboot; the application uses its user profile.
  Keep the reservation until explicit deployed-review completion.

## Design ownership and documentation

The user explicitly authorized GPT-6 Astra/xhigh for precise design and later
review. A fresh standalone designer owns `design.md`; the initiating lead
implements the accepted brief. A different fresh independent reviewer performs
the mandatory final committed-deliverable review. The tracking session is
threadless to avoid a second lead executing this task; it has no retained team.
Read and retain the full applicable workspace/repository procedures.

Readers are agent implementers, operators and maintainers. Keep generic feature
contracts and recovery documentation in dev-workspace, adapter semantics in the
extension, site procedures here/configuration, and individual rollout evidence
in this initiative. Register the design and other durable artifacts normally.

## Compatibility and recovery

Use a separately versioned private coordination journal; preserve session
manifest, lifecycle journal, Codex ledger and retained roster formats. Package
transitions must prove support for pending jobs and reservations and reject
stale generations. Preserve forward-only profile recovery. Deterministic
mutation workers must survive coordinator/portal restarts, and unknown mutation
outcomes must be reconciled before retry or resource release.

No application database, client API or vpsAdminOS node protocol changes are
intended. No coordinated update of running nodes is required. Browser/terminal
clients retain the selected validated Codex protocol. Establish bootstrap,
upgrade, generation checks, schema failure and recovery semantics in design.

## Verification and rollout

Verify concurrent merges with stale-baseline refresh; short critical sections
despite slow preparation; concurrent unrelated resources; repeated deploy-first
iteration and cumulative later deployments; merge-only jobs; automatic wakeup;
delivery/execution interruption; approval/ownership/cancellation/lifecycle and
package compatibility. Use repository Nix environments. Quick checks precede
the final independent review; long VM/App Server tests, CI and builds follow it
and use fresh Luna/low verification watchers. Preserve session continuity in the
approved no-reboot aitherdev rollout. Run the workspace/configuration deployment
contract check and retain exact sources, live identities and recovery evidence.


## Provider-enabled creation correction

The approved UI is deployed and live-verified. A user-reported creation error
exposed an inherited upstream provider helper bug. Correct the command runner
and unpack its stdout; preserve validated argv, initial-goal receipt, existing
thread and lifecycle authority. See creation-provider-runner-fix.md for the
bounded lead brief and isolated before/after acceptance. The correction has no
state or contract migration. Reuse unchanged UI/host/worker evidence, independently
review the committed correction and consolidated pins, then verify and deploy an
exact successor before the authorized merges. Preserve the failed session's state.

## First-installation integration gap

Astra/xhigh design concludes that a dated supervised source-only maintenance
helper is sufficient for the retained threadless owner. It reuses the exact
selected package's host admission, engine snapshots/receipts and ordinary merge
workers; no permanent CLI permission, new state format, automatic bootstrap
claiming or private Git implementation. The helper is substantive workspace
feature code and receives focused checks and independent final review. Prove the
application derivation unchanged; retain the creation rollout and integrate the
new descendant workspace head. The lead starts no other bootstrap operation
while serially integrating the four authorized repositories. All other owned
jobs must be settled. See bootstrap-merge-design.md and the lead acceptance.

## Concurrent configuration target advancement

Runtime and extension integrations succeeded through ordinary workers. During
serial preparation, configuration master advanced independently to 8bf9da9c
(upstream staging input update). No configuration job was admitted. Rebase
preserved the two feature patches exactly: fbbda8e9 becomes 9a481ba1 atop the
new base; ordered patch IDs and range diff match. Original deployed fbb source
ref is retained remotely, and input composition still selects runtime a10af6c4.
The Git procedure preserves the existing repository/target merge approval for
this clean patch-equivalent rebase.

The dated helper currently admits only deployed ancestors. Extend only that
source-only admission with independently reviewed exact patch-equivalent lineage
using the selected runtime comparator. Preserve already admitted plans, requests
and receipts. A new remaining-merges plan binds rebased configuration and final
workspace heads; normal finish later needs a canonical replacement review receipt
with the actual configuration merge approval ID. No release or new deployment
is implied. A focused follow-up helper commit preserves the already consumed
aadaa171 implementation used by the two live completed merges.

## Merge preparation correction requested during integration

The user asked to fix the observed excessive merge process. Capture hook
dependencies after the repository shell initialization, preserve runtime SSH,
and complete source and target checkout hooks before admission, including retry
after incomplete preparation. Keep network/fast-forward sections short. Exact
original configuration push recovery is complete. No broader automatic replay
or schema change is part of this correction. Deploy the reviewed runtime fix
under the existing authorization and reservation; verify representative actual
configuration hooks and composed package, without repeating unrelated browser
or source-identical VM suites. Shared-master foreign tracking publication remains
the only separate pending authorization.


## Final outcome, 2026-10-14

The permanent merge-preparation correction is deployed. All four exact final
feature heads are integrated into remote master and freshly proved by
`final-integration-acceptance.json`. No additional review or merge work remains.
Keep the initiative active and aitherdev reserved for human UI review; release
requires the explicit review-completion proof under the existing contract.


## Explicit release and handoff, 2026-10-14

The user clarified that no review remains and explicitly directed release.
Normal finish succeeded with the final integrated/deployed heads, historical
replacement lineage and unchanged live identities. Additional exact-mapping
review was explicitly waived; existing independent source reviews remain the
verification basis, with transparent user-acceptance receipts. Aitherdev is
available to other sessions. The initiative is complete; no archival or session
closure was performed. The requested running-session handoff is in
`running-sessions-handoff.md` and the portal Artifacts catalog.
