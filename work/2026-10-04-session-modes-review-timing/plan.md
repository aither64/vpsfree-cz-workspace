# Restore session modes and review timing

Implement the plan accepted in this conversation. New Solo sessions let the
lead investigate, design and implement without acquiring specialists.
Lead-designed sessions contain the lead, implementer and reviewer, with the
lead owning design. Full-team sessions retain architect-led design.

## Components and implementation

- `aither64/dev-workspace`: generic lead orchestration instructions and session
  documentation; preserve retained snapshots and manual member management.
- `vpsfreecz/dev-workspace` (local `vpsfree-dev-workspace`): mandatory review
  skill excludes routine planning, investigation, and coordination records;
  completed substantive deliverables still require independent branch review.
- `aither64/vpsfree-cz-workspace` (local `workspace`): distinct preset prompts,
  lead-owned design for `lead_designed`, two specialist slots, Solo source
  ownership, aligned workspace rules and policy tests, dependency pins.

Adding specialists or changing a team requires explicit user direction.
Earlier review is allowed only when explicitly requested and never substitutes
for final review. Keep the independent temporary reviewer for Solo and the
separate watcher for long checks. Keep existing models, efforts and the
Full-team default. The user explicitly selected new-session defaults only;
do not refresh retained prompts or mutate existing rosters.

## Compatibility, rollout and recovery

No API, database, manifest, roster or runtime-authority schema changes.
Creation retries and forks retain saved policy; mixed versions continue using
existing snapshots. Shared workspace instructions and installed skills change
globally and can conflict with saved older prompts. No existing-session repair
mechanism is included. No vpsAdminOS or machine coordination is needed.

Update pins in dependency order: runtime, organization extension, workspace.
Verify and independently review all committed changes before long packaged
checks. Deploy the workspace application with `workspace-host switch --source`
from the workspace feature worktree. Changes to aitherdev host configuration,
if genuinely required, belong in `vpsfree-cz-configuration` and deploy through
confctl target `cz.vpsfree/machines/aitherdev`; none are currently expected.
Deployment does not authorize any repository master integration. Recovery uses
a corrected forward package switch, preserving schema and lifecycle checks.

## Verification and documentation

Verify preset member counts 1/3/4; design ownership, access, effort support and
portal role counts; no specialist creation or automatic planning review;
explicit early review and normal final review remain supported. Run affected
instruction, skill-policy, Go lead/preset and Ruby creation/snapshot checks,
then packaged checks after mandatory review. Review complete feature histories
and explicitly record no migrations. Document supported behavior in project
session guides, the owning review skill and workspace team guidance; retain
exact rollout revisions and evidence here.

The accepted plan settles the behavior. A bounded design reconciliation and
verification brief is sufficient; do not add another planning review.
