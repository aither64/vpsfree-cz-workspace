# Documentation workflow review packet

Historical packet for the completed review. See [state.md](state.md) and
[verification.md](verification.md) for subsequent integration and deployment.

## Requested outcome and accepted scope

Implement the plan in plan.md. The user selected a GENERIC dev-workspace skill
and documentation improvements as projects are touched. Implement authoring,
package installation, session prompts, vpsFree review/handoff, and workspace
policy. Integrate the three repositories and deploy the application on aitherdev.
No historical backfill, portal search/UI work, new manifest schema, documentation
completion gate, or automatic deployment authorization is requested. Routine
writing remains owned by the agent with task context.

## Ownership and trust boundary

The generic runtime owns the skill, package catalog and session lifecycle.
The vpsFree extension owns local review and handoff integration. The consuming
workspace owns project/site destinations and pins the extension. Existing Nix
exports and catalog activation are the consumers of the new built-in skill.
The local operator is trusted to administer this development host. Preserve
ordinary concurrency, identity, data-integrity, retry and rollback checks;
remote clients remain untrusted. Do not extend that trust to managed projects
or guests. No host substrate or configuration repository change is expected.

## Risk and lanes

High classification because persisted session creation recovery, package
composition/rollback, and deployed cross-project behavior are touched. Run all
four adaptive lanes (general, architecture, scope, risk/compatibility), model
gpt-6-astra and xhigh effort, with fresh context and no nested reviewers.

## Repositories and commits

### dev-workspace

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-session-documentation-review/dev-workspace`
- Branch: `2026-09-15-session-documentation-review`
- Base: `227bcfc1b989407582d3b022f8b388ac29972c16`
- Head: `9a1b16464e45d722110b448a79315a0f3ce134aa`

```text
b485d5d skills: preserve development rationale in project documentation
9a1b164 session: prompt for decisions and documentation
```

### vpsfree-dev-workspace

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-session-documentation-review/vpsfree-dev-workspace`
- Branch: `2026-09-15-session-documentation-review`
- Base: `08d691cfd239260ce5bf7c269a44a49ce8de41e7`
- Head: `c6afe2905506fba0b8e372e0436b570f5597f8bd`

```text
dbf7a9b skills: include durable documentation in reviews and handoffs
c6afe29 flake: consume the generic documentation workflow
```

### workspace

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-session-documentation-review/workspace`
- Branch: `2026-09-15-session-documentation-review`
- Base: `d4382e7143b88e95bf093c8508c2867ff35160a1`
- Head: `7353127dc22275f24f1f92e5782fb34840dd0e49`

```text
9e7f55c workspace: maintain durable documentation during development
7353127 workspace: select the documentation workflow package
```

## Commit split

Runtime: generic skill, packaging, guide and link-reconciliation tests; then
session templates, predecessor recovery, fixtures and corresponding guide text.
Extension: review/handoff and entry-point guidance; then exact runtime pin.
Workspace: local authoring policy; then exact extension/consumer pin.

## Documentation to review

- Generic skills/dev-session-documentation/SKILL.md and agents/openai.yaml.
- Runtime docs/dev-sessions.md documentation section, README and AGENTS.md links.
- Extension review/handoff skills and general-review reference, README and rules.
- Workspace AGENTS.md documentation responsibilities and destinations.

The generic guide explains the rationale for model discretion and ordinary
Markdown, ownership, deployment/rollback of the skill, and current versus
historical instructions. Evaluate the guidance with a small local fix, a
consequential design choice, an ordered migration, and unknown historical intent.
The supporting verification.md records the author's editorial checks.

## Quick verification

- Runtime helper and test Ruby syntax passed; skill-creator validation passed.
- Focused session checks passed: 7 runs / 105 assertions; additional predecessor
  seeding and full startup-to-tmux-boundary recovery: 4 runs / 34 assertions.
- Focused catalog/skill reconciliation and transition checks: 5 runs / 29
  assertions. Workspace deployment-contract unit suite: 3 runs / 14 assertions.
- All three Nix flake evaluations passed without builds. Whitespace checks pass.
- No declared hook framework in the affected repositories. No hooks bypassed.
- See verification.md for investigated environment and test-fixture failures.
- Feature CI is running; local long package and integration checks await review.

## Compatibility and deployment assumptions

No schema, lifecycle state, external CLI, node/guest protocol, or database change.
The new built-in skill uses the existing catalog and reserves its name against
extension replacement; distinct extension skills remain available. Existing
activation reconciles managed links on rollback without deleting authored docs.

New templates preserve old required markers and lifecycle front matter. Existing
active/archived records are not converted. Goal seeding accepts exact predecessor
or current empty/already-seeded templates and rejects edits. Fork retry retains
its existing exact-template behavior; switches already reject unfinished forks.
Existing creation/transition ownership and journal checks remain in effect.

Deployment uses workspace-host switch --source from the consuming workspace
worktree and retains the preceding package. Tests will verify catalog packaging,
source boundaries, full package suites, and live discoverability/portal access.
The user authorized aitherdev deployment if host work becomes necessary, but
configuration integration remains separate. Preserve other sessions and branches.
