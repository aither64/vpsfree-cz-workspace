# Team lead delegation instructions

## Goal and scope

Make delegated team leads coordinate, assess evidence and report status while
members own substantive investigation, design, implementation, checks and fixes.
The user also authorized a read-only sample of active sessions to understand lead
and member working time. Evidence must distinguish duplicated work from required
coordination and real dependencies, and respect sensitive-source restrictions.

Affected repository: this workspace (AGENTS.md, docs/agent-teams.md and selected
routed guidance; config/agent-teams.nix catalog prompts). No runtime features,
new telemetry or team reconfiguration. Later user additions authorize workspace/master
integration after checks/review and workspace application activation; full system
deployment remains outside scope.
Readers: future workspace leads and members. Authoritative rules stay in existing
instruction homes; session-specific evidence stays here.

## Approach and ownership

Architect0 owns bounded investigation/design and design.md. Implementer2 owns a
sample of at most three active Full-team sessions (~10 minutes). Release settled
instruction-document and catalog-prompt packages to separate implementers when
safe. Lead owns this plan/state, allocations, acceptance, independent review and
user communication; does not repeat member investigation or application edits.

## Compatibility and delivery

Preserve Solo and Lead-and-reviewer behavior, retained model/effort/access/prompts,
review independence, approvals and lifecycle/resource safety. Shared instructions
apply when read; catalog prompt changes require separate package deployment and
do not rewrite retained sessions. No persistent schema/API change or migrations.
Develop in worktrees/2026-11-25-team-lead-delegation/workspace on its dated branch.
Publish feature branch; workspace/master integration and application activation
now explicitly approved in this conversation after checks/review.
Recovery is reverting the instructions/catalog patch before a future deployment.

## Verification

Members run proportional syntax/catalog checks and instruction consistency/link
checks, commit complete deliverables and assemble exact base/head/history evidence.
Lead checks packet completeness and assigns retained reviewer0 mandatory final
review after intended commits and quick checks, before any long checks. No broad
runtime tests unless the final change requires them. Track actual results in state.
