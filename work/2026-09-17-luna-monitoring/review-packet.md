# Review packet: automatic Luna monitoring

## Request and boundary
User explicitly accepted native Luna/low monitoring subagents for long tests,
CI checks and builds, preserving Astra/xhigh for planning, implementation,
diagnosis and mandatory review. User corrected ownership to generic dev-workspace.
Deployment to aitherdev is authorized; do not wait for GitHub Actions. No
configuration master integration is authorized. No runtime scheduler, durable
supervisor, global model downgrade, broad AGENTS cleanup or usage dashboard.

## Scope and commits
- dev-workspace: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-17-luna-monitoring/dev-workspace
  Base 5bcb83120cf25974ecd2dad7b7e737473169b173; head 8c6f7025fc3c86b02b602dbd1f478c3a6de460f3.
- vpsfree-dev-workspace: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-17-luna-monitoring/vpsfree-dev-workspace
  Base f2fdbcebc115b7fd07ab6e0c91ebea189a57f341; head 4ffe714dc46d94907e8dfc45019e52de8743cdb3.
- workspace: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-17-luna-monitoring/workspace
  Base 7df00d65cefb827028bce2e18db8e081a30264f3; head 0820a61bf202eb5ec41a4e406fe4f77cd9de177b.
- vpsfree-cz-configuration: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-17-luna-monitoring/vpsfree-cz-configuration
  Base 3caab98ddc3e45c97a49c0c0f6a02e6cc612b662; head 37dc56ee72600cbe21fd9e9a42442741cf117c09.

Generic commit bundles its skill, catalog installation/collision checks and
feature documentation because they implement one capability. Extension commit
only updates its runtime pin. Workspace keeps policy and generated pins in
separate commits. Configuration pin is produced by confctl; preserve its generated
message despite long changelog lines. Configuration base's previous runtime is
an ancestor of the new runtime, with no host-module or host-path changes.

## Public interface, ownership and consumers
Generic skill dev-session-monitor uses existing schema-1 skill catalog.
Extension calls generic lib.mkPackage and receives built-in skills. Workspace
consumes the extension and requires automatic use. Configuration consumes only
generic nixosModules.host and must match the workspace generic revision under
bin/check-dev-workspace-deployment. Codex-web needs no change. Existing runtime
installs/removes managed skill links on activation/rollback.

## Documentation
Generic skills/dev-session-monitor/SKILL.md and agents/openai.yaml;
docs/dev-sessions.md#monitor-long-verification, linked in README. Workspace
AGENTS.md contains model/use policy and passes project escalation rules.
Current intent: work/2026-09-17-luna-monitoring/plan.md.
Evidence/rollout: state.md in the same tracking directory.

## Quick verification
Skill creator quick_validate.py passes with Python/PyYAML from Nix.
nixfmt --check passes both changed Nix files; git diff --check passes.
Generic extension-catalog derivation evaluates with collision assertions.
Consumer package-metadata derivation evaluates; workspace/site deployment
contract passes at the exact new generic revision. Configuration commit ran
all Overcommit hooks successfully; only the generated changelog width warning.
Long package checks and live delegation tests deliberately follow review.

## Compatibility and risk
Overall high risk under the review workflow because deployment/rollback is in
scope; implementation itself is an additive workflow and skill packaging change. Review at
xhigh in general, architecture, scope and risk lanes. No API, schema, protocol,
state migration or parent-model mutation. Automation is instruction-driven,
not deterministic scheduling; docs say so. Fallback is visible parent monitoring.
Model defaults are unchanged. Local operator is trusted to administer the
workspace host; preserve remote-client boundaries and ordinary operational
checks, without inventing defenses against a compromised local administrator.

Perform your assigned lane directly, with no nested agents. Review committed
changes. Report concrete findings and residual gaps, keeping the response concise.
