# Final follow-up review

User reports observers never run in confctl rewrite/UI sessions and questions
new readme/TypeScript sessions. All four ready observers are cold according to
private recovery permission; early recoveryHeld(observer) gate silently skips
them. Cold scheduled sends already use durable queue-before-activation.
Remove the early gate without weakening automatic active-development admission.
User also requests controls in Settings, per-session cadence, and Check now.

Acceptance/design: design.md follow-up section; state.md current status.
Automatic checks remain idle/human-input excluded; explicit Check now may run
while idle/paused but never wakes an idle lead. One pending request, stable
identity, three-minute deadline and existing manual-work protection remain.
Interval 1..1440 whole minutes, absent/zero=15, worker visits once per minute.
Cross-origin/missing-observer/session-operation mutations must refuse.

All intended changes are committed. Quick checks passed: nix develop;
Go TestProgress* in progressobserver/web/workspacecodex and real-wire cold
assignment/progress receipt test; Node controller assertions and syntax;
matching consumer-pin checker. Configuration ordinary hooks pass. No long
local integration suite has started. Existing final master CI40306866062 passed
all four jobs; that is earlier baseline evidence, not follow-up verification.

High risk: recovery permission and optional persisted cadence plus explicit
native turn submission. Review all four lanes. Read skill and every lane file.
Same independent reviewer /root/final_review, retained Sol/xhigh settings; no
managed roster/valid lead thread exists, catalog fallback remains appropriate.
Installed catalog digest1da70b758790d079c1c74aa8666e9d3a72665fdb7d95ab703951abeb38a60a6d.
Do not spawn nested agents, run long tests, edit sources, deploy or merge.
Write findings to followup-final-review.md; report severity/commit/file/lines.

Runtime fix and session-controls commits are separate logical changes. Tests
and explanations accompany their owning behavior. Workspace docs and generated
runtime pin are separate. Configuration generated channel pin is mechanical.
No repeated update streams in these unmerged ranges; previous pins are already
merged/deployed master history and cannot be rewritten. No obsolete approaches
or migrations. No schema/roster/native version transition. Optional cadence is
ignored by the old scheduler, which may drop it on a later state rewrite;
rollback restores15-minute scheduling. Existing root activation, lifecycle and
package-transition contracts remain. Do not require extra model pilot or host
VM tests for unchanged host code.

Owner and consumers: dev-workspace owns scheduler/state/API/browser and send
boundary; workspace composes nested runtime with site catalog; configuration
selects the matching host runtime. Both lock changes affect exactly their runtime
node and preserve extension/sibling inputs. Application stays in user profile.
No new Codex or system behavior. Guides changed: runtime dev-sessions.md and
workspace-portal.md, workspace docs/agent-teams.md. Individual rollout stays in
session rollout.md. No KB writes. New feature merges not yet authorized.

### dev-workspace
Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-progress-oversight/dev-workspace
Base: 9baeea528f2e270332afa13786ec85a49a68e4c3
Head: 5fea2be1cba9d1574c178951170cb68b639d58f1
Complete series:
54e968ae progress: schedule checks for cold observers
5fea2be1 progress: configure session checks from settings

Diff: followup-dev-workspace.diff
### workspace
Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-progress-oversight/workspace
Base: dacd3d7afb20f42c6f7bf95b767fb73fbbd61ea4
Head: a878419176920e5521743fbbd633a8b293032c77
Complete series:
e3aff9c9d docs: locate progress controls in session settings
a87841917 runtime: select observer activation and session settings

Diff: followup-workspace.diff
### vpsfree-cz-configuration
Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-progress-oversight/vpsfree-cz-configuration
Base: 7eaaafd718809e16867c9b4614f9b2e2d54fa62a
Head: 7dd40ff46d78a475d9730888771d20122d51c919
Complete series:
7dd40ff4 inputs: set devWorkspace to 5fea2be1

Diff: followup-vpsfree-cz-configuration.diff
