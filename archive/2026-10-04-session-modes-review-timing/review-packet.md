# Final review packet: session modes and reviewer timing

Review the completed, committed implementation yourself. Do not edit source or
launch reviewers/subagents. You are reviewer0 in this exact session, thread
`01a107a8-68eb-7ff3-b927-501bd21981c5`, saved GPT-6.1 Sol/xhigh, read-only.
No model/effort/access override applies. Report findings ordered by Blocking,
Important and Advisory, with lane/file/line/commit evidence, plus residual gaps.
Send the full report to the lead and include it in your final response. The
external coordinating conversation will preserve that report; do not attempt
to write tracking from your read-only sandbox.

Read `/home/aither/.codex/skills/mandatory-change-review/SKILL.md` and all four
references: general-review.md, architecture-review.md, scope-review.md,
risk-review.md. Also read canonical workspace AGENTS.md and applicable routed
procedures (projects, sessions, git, lifecycle, documentation, verification,
deployment, knowledge-base, commits), affected local AGENTS.md and relevant docs.
Verify your exact bound workspace/session before accessing its records.

## Outcome and boundaries

User accepted the plan and said "Implement the plan." Solo leads investigate,
design and implement without acquiring persistent specialists. Lead-designed
has the lead, implementer and reviewer, with the lead owning substantive design.
Full team remains default with architect-owned design and delegated edits.
Expected totals 1/3/4, specialist slots 0/2/3. Existing models, efforts, allowed
efforts, access and work/utility policies stay unchanged.

Automatic independent review follows completed substantive deliverables,
commits and quick checks, before long integration tests. Standalone substantive
documentation and configuration remain in scope. Routine planning,
investigation, findings and session tracking/evidence alone do not trigger it.
Earlier review requires explicit user request, is advisory and never substitutes
for final review. Temporary Solo final reviewers and watchers do not join rosters.
Retain adaptive lanes, saved reviewer settings, whole-history/migration gate,
mechanical-update exemptions and narrow-remediation policy.

Explicit user choice: new sessions only. Do not refresh existing saved prompts,
repair/mutate old rosters, change schemas, add runtime hard enforcement,
redesign manual team controls or introduce a policy refresh mechanism. Adding,
replacing or reconfiguring members needs explicit user direction. Generic legacy
fallback prompt constants are deliberately preserved: they are also used by
older sessions without saved prompts. The architect and lead agreed this
clarification; new behavior belongs in saved catalog prompts. Small bounded
edits can use a direct lead brief instead of a separate design document.

## Exact branches and complete histories

All feature branches: `2026-10-04-session-modes-review-timing`.
Worktrees beneath `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-04-session-modes-review-timing/`.

| Local project | Feature base | Final head |
| --- | --- | --- |
| dev-workspace | 45d4f13ab14a2dd7d19ea564dc1d364c5ac155c6 | 6a972b9ab01077611b2c60e0fc726c185e050315 |
| vpsfree-dev-workspace | 67c9a60b802537bbb7154959405b67f168f85397 | e1bb5cf3ad37c5ef31445a68ab85f53db2858777 |
| workspace | 232471a8e3e6fad07ac97ed0cf78b26cf411e406 | 9f016bf8685a5098fe24892cf9a539c031856eb9 |

Each `review-<project>-series.txt` contains the complete feature commit list and
messages; `review-<project>.diff` contains its final diff. Review those and the
actual Git branches. Runtime has one policy-documentation/regression commit.
Extension has one skill/docs/supporting-tests commit and a separate dependency
pin commit. Workspace has one coordinated mode-policy/docs/supporting-tests
commit and a separate dependency pin commit. Tests/docs accompany the behavior
they protect; dependency updates are independently reviewable. Precommit fixes
are folded into these final functional commits. No abandoned branch iteration,
new compatibility shim or follow-up tidy commit is intentionally retained.
**No migrations:** none created, merged, released, deployed or externally consumed.
Require explicit history and migration conclusions.

Workspace was rebased onto current shared master, `232471a8`; range-diff reports
the functional patch unchanged (`4dff7e71 = 4798f561`). At preparation time
remote master was `fc837e0b361c9f5c27081d7f38451537153c8fbb`. The full remote-base
series is `review-workspace-remote-series.txt`. The complete remote-base diff
was supplied as `review-workspace-complete.diff` during review and removed
afterward as an 18 MiB reproducible capture. Regenerate it in the retained
workspace worktree with `git diff fc837e0b 9f016bf8`. That series also inherits two already-shared
coordination commits: our initial tracking `75a13f0a` and another initiative's
archive `232471a8`. They contain coordination records, not this feature's
application behavior. Assess that provenance; do not expand this task into an
audit or rewrite of the other initiative's archived work. Shared checkout stays
on master with unrelated modifications preserved. No integration is authorized.

## Ownership and consumers

Generic runtime owns catalog validation/projection, saved team policy and
creation/fork persistence, portal team displays and user-profile package
transitions. Owning contract docs: dev-workspace `docs/dev-sessions.md` and
`docs/workspace-portal.md`. Runtime changes are docs/tests, not production source.
The organization extension consumes runtime through `inputs.dev-workspace` and
`lib.mkPackage`; it owns `skills/mandatory-change-review/SKILL.md`, metadata,
README guidance and policy tests. Its pin is exact runtime head above.
The site workspace consumes `inputs.vpsfree-dev-workspace` and supplies
`config/agent-teams.nix` through `teamConfig`. Its pin is exact extension head;
lock changes include only that input and its expected transitive runtime pin.
The site owns AGENTS.md, routed sessions/verification guidance,
docs/agent-teams.md and policy assertions in flake.nix/test.

vpsfree-cz-configuration is a discovered consumer of the generic hostModule and
Codex library; its confctl target cz.vpsfree/machines/aitherdev uses channel
dev-workspace role/input devWorkspace. No host interface changes are made;
host configuration needs no pin/build/deploy for this change. Application
deployment uses workspace-host's user profile, not system configuration.

Trust boundary: the local development-host operator is trusted to administer
that host. Preserve ordinary path/ownership, wrong-session, concurrency,
credential and state-integrity checks. Remote clients remain untrusted. No
new security boundary or filesystem defense is introduced.

## Compatibility, deployment and evidence

Risk: High conservatively because this cross-project rollout combines new
catalog defaults and globally installed instructions with retained session
snapshots, forward-only package transitions and mixed generations. Four lanes
apply: general; architecture (configuration/test logic and reusable owner);
scope (cross-project contract); risk (snapshot compatibility/deployment).
Classification does not override your saved effort.

No API, CLI, manifest, roster, lifecycle, runtime-authority or schema changes.
Existing snapshots retain lineup/prompts/settings on retry and fork; older
Lead-designed sessions can retain architects. Shared workspace instructions and
skills are global and can conflict with older frozen prompts, an explicitly
accepted residual behavior. Source AGENTS corrections live on the feature
branch pending integration; installed new-session developer prompts carry the
correct mode ownership. No canonical shared AGENTS is silently replaced.

Deployment is prepared, not executed: runtime -> extension -> workspace pins,
all checks/review, then workspace-host switch --source from the workspace
feature worktree. Recovery uses the same/corrected/newer forward package,
preserving transition locks, generation/schema checks and lifecycle journals.
Do not merge defaults, archive/delete sessions, or start deployment yourself.

Quick evidence:
- Core Go workspacecodex/agentteams/teamruntime and focused web count/saved
  prompt tests passed using pinned Go and GCC; see
  focused-go-with-compiler-result.json and associated logs.
- Runtime Ruby aggregate selection passed: 3 tests, 23 assertions, no skips.
- Extension policy suite: 5 tests, 72 assertions, all passed.
- Workspace instruction suite: 8 tests, 144 assertions, all passed.
- Catalog exact totals/owners/efforts/access and schema invariance evaluated;
  composed final-pinned package drvPath evaluated successfully.
- gofmt and git diff --check passed. No declared hook frameworks to install.

Initial quick-check failures were diagnosed and corrected before review: pinned
Go-only shell lacked GCC for cgo/SQLite; Markdown wrapping made policy
assertions whitespace-sensitive. These are recorded in state.md and a reusable
toolchain note. The implementer could not access the Nix daemon in its sandbox;
the parent and fresh utility ran the proper Nix checks. No failed check accepted.

Long packaged suites have not been manually started and will follow review.
No host-migration/development-cluster VM is required by these policy-only changes.
No existing sessions were mutated for smoke tests. This is instruction policy,
not a runtime guarantee of model compliance.

Plan/state/design and rollout evidence live in this initiative directory.
Documentation destinations above describe the supported behavior without
requiring this private session. The main lead applied the user-facing writing
skill after technical reconciliation and before commits. Portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-04-session-modes-review-timing/
