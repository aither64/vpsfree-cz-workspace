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
- No default-branch integration is authorized by this task. Publish feature
  branches and retain them. User explicitly authorized deployment to aitherdev
  through vpsfree-cz-configuration; deploy without reboot and select the
  application from its workspace user profile.

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
