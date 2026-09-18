# Documentation boundaries: review packet

## Request and acceptance

The user accepted a shared rule separating lasting project documentation from
repeatable operations, supported upgrade instructions and individual rollout
records. Implement across repositories, merge default branches and deploy the
updated skill package. Leave session 2026-09-09-ip-release-mechanism and all its
owned work untouched; deliver a separate handoff for its owner.

The rule must preserve lasting feature/compatibility/failure semantics and
needed upgrade/recovery instructions, distinguish transaction rollback from
software rollback, and handle one-time checklists without dates or hashes.
Avoid a fixed document bundle, new framework, arbitrary release versions,
private-only supported upgrade guidance or historical backfill.

## Repositories and reviewed commits

Workspace root: `/home/aither/workspace/ai/vpsfree.cz`.
All feature worktrees are beneath `worktrees/2026-09-17-documentation-boundaries/`.
All feature branches are `2026-09-17-documentation-boundaries`.

| Worktree | Base | Head |
| --- | --- | --- |
| dev-workspace | 0bd68efa9cadb0589148fac40de7645a06b03468 | 5bcb83120cf25974ecd2dad7b7e737473169b173 |
| vpsfree-dev-workspace | 90ce0cfe7c39c944aca0c7b27fe1e53a719075a3 | f2fdbcebc115b7fd07ab6e0c91ebea189a57f341 |
| workspace | 2c2ca547e9067ddcac9cae27f24c31d5f3536d5f | fd626e56f6440834c2ce50f32fd7f218a458f020 |

Runtime: one documentation/skill commit. Extension: one review/handoff guidance
commit plus a separate runtime pin. Workspace: one policy commit plus a
separate extension pin. Initial tracking is already in the workspace base.
There is no project-code change outside these ranges.

## Ownership and consumers

dev-workspace owns the generic authoring skill and human session guide.
vpsfree-dev-workspace consumes it through an exact flake pin and supplies
review/handoff skills. The workspace consumes that extension through an exact
pin and supplies site policy and configuration. Existing catalog packaging
installs these skill files; no discovery metadata, catalog schema or packaging
logic changed. No additional repository needs adoption work for the global
authoring rule to apply when loaded.

Updated paths:
- Runtime: skills/dev-session-documentation/SKILL.md and docs/dev-sessions.md.
- Extension: skills/mandatory-change-review/SKILL.md, its
  references/general-review.md, and skills/dev-session-handoff/SKILL.md.
- Workspace: AGENTS.md and the consumer pins in flake.nix/flake.lock.

Read [plan.md](plan.md), [state.md](state.md),
[verification.md](verification.md) and [ip-release-handoff.md](ip-release-handoff.md)
for context and the user-facing handoff artifact. The handoff is held here and
has not been delivered through another session's conversation or written into
its records. Do not inspect or mutate unrelated sessions to validate it; its
source map cites the previously inspected vpsAdmin revision.

## Risk, lanes and compatibility

Risk: Low. This is a bounded, reversible documentation-policy change with
mechanical pins to that same change. There is no runtime implementation,
authorization, persisted-state, schema, protocol, deployment mechanism or
compatibility-contract change. Plans/templates and lifecycle behavior are
unchanged. Profile rollback restores older skill text; committed workspace
policy and authored documentation remain unchanged by package rollback.

Lanes: general, plus architecture because the generic skill is a reusable
component with two downstream consumers. Scope/risk specialist triggers do not
apply to this narrow policy correction; assess that classification against the
actual diff. Both reviewers use gpt-6-astra/xhigh and work directly without
nested agents.

The local workspace operator is trusted to administer the development host.
Remote clients, guests and project tenants retain their existing boundaries;
the update changes none of them. Deployment uses the existing stable profile
switch with its current transition checks. It must not interrupt or reset
another session. No host configuration change is expected.

## Quick verification

- Three edited skills pass skill-creator quick_validate.py in pinned Nix
  Python/PyYAML; all frontmatter is unchanged.
- Changed Markdown relative-link checks (6) and git diff --check pass.
- Workspace deployment-contract tests: 3 runs / 14 assertions, no failures.
- Extension forward/reverse migration smoke: 1 run / 15 assertions, no failures.
  An initial environment-only failure and its correction are in verification.md.
- Manual scenario assessment covers feature fixes, application rollback,
  repeatable recovery, a supported upgrade, a site rollout and disposable branch
  database reset. It is not an automated behavioral guarantee.
- Nix evaluation results are recorded in state.md before review starts.
- No declared hook framework in these repositories; no hooks bypassed.
- Full package/Nix checks and live activation follow review. Provider feature
  CI starts automatically on branch pushes; results are still pending.

## Reviewer task

Read the installed mandatory-change-review skill and your lane reference, local
AGENTS files and the committed ranges. Perform the review directly. Do not
change implementation, stage files, commit, deploy, run long tests or launch
subagents. Report findings by severity with concrete file/commit references;
if none, state that and identify residual risks or verification gaps.
