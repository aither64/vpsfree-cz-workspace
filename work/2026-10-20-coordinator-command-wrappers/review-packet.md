# Final branch review packet

Outcome: replace new merge/deployment orchestration with logged arbitrary command
wrappers. Sessions own hooks, signing, Nix environments, merges, deployments and
effect verification. Coordinator owns resource exclusion, explicit reservations,
command logs/results and notifications. Normal nonzero exit releases locks;
interruption retains them until owner resolution. No automatic effect inference,
command replay, source copying or multi-version trust adapter. Existing operations
and uncertain recovery must remain usable under their original contracts.

Initiative: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-coordinator-command-wrappers
Read plan.md, design.md, state.md and relevant repository AGENTS.md. Top-level
workspace AGENTS.md plus docs/agent-instructions/{projects,sessions,git,lifecycle,
documentation,verification,commits}.md apply. Reviewer must stay read-only and
perform all lanes directly without nested agents. User authorized implementation;
no default-branch integration, shared runtime selection, production actions,
cleanup of other sessions or initiating-session recovery is authorized.

Repositories and complete commit series:

- Generic /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-coordinator-command-wrappers/dev-workspace
  base ea3f9d36397e8c2c846bd456e51385d73a3a358a
  head d6690abc67be2f9c23da39950fb1f0b8742338ea
  one commit: coordination: run session commands under logged resource locks.
- Workspace /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-coordinator-command-wrappers/workspace
  base 650495d6bea856c75c5d717526c9a888f7f2fcf6
  head a11b2ce2261f87808e2867eca24e7d656636833c
  one commit: workspace: route new operations through logged command wrappers.

Inspect both complete git diffs/series. No superseded branch iterations, fixup
commits or repeated dependency/channel/flake updates. No database migrations.
Additive command metadata introduces its final schema directly. Neither commit
is merged, released, deployed or externally consumed. Runtime commit includes its
CLI, worker, coexistence/lifecycle/profile guards, package contract and status UI,
with the tests and owning documentation needed to describe that single feature.
Workspace instructions form a separate dependent commit in their own repository.

Risk: high. All lanes apply: general, architecture/repetition, scope/proportionality,
risk/compatibility. Use mandatory-change-review SKILL.md and every lane reference.
The local operator is trusted; evaluate ordinary concurrency, identity mistakes,
interruption and data integrity rather than attacks by an already compromised
operator. Remote clients stay untrusted and get no arbitrary-command mutation API.

Consumer discovery: generic runtime is consumed by the vpsFree extension through
its flake and by workspace's direct nested runtime override; system configuration
selects the matching host module separately. Installed coordination catalog owns
current canonical repository and physical machine identities. The extension's
workspace-confctl adapter remains for legacy retained operations. New commands
use the session's ordinary Git/Nix/confctl scripts. Existing format readers and
legacy adapter contracts are retained; no consumer pins change in this scope.
Read representative current config/coordination.nix and extension
repos/vpsfree-dev-workspace.git docs/workspace-confctl.md if needed. Profile switch
must recognize a live wrapper machine lock/reservation without requiring a new
legacy job; all existing package compatibility and forward recovery remain.

Documentation: generic README, coordination.md, coordination-operations.md,
integration.md, preserved coordination-legacy.md; package installs the missing
integration guide. Workspace AGENTS.md, coordination.md, Git/deployment/verification
procedures adopt wrappers while preserving approvals/review and retained recovery.

Quick checks passed: 20 command tests/77 assertions; 14 browser tests; selected
host tests 8/60; selected legacy coordination tests 19/142; affected Go policy
packages; Ruby syntax and whitespace checks. Known test gaps before final review:
committed real systemd and Overcommit 0.73.0 integration fixtures not yet run;
packaged broader suites follow review. Review is not asked to assume they pass.

Require explicit conclusions on whole-branch history, no migrations/new-state
lineage, repeated update streams, compatibility and scope. Report ordered concrete
findings with file/line/commit references and residual risks. Save or return report
to the main agent; do not edit application code, records, or shared state.
