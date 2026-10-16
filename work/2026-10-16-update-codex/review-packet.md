# Final independent change review

Review the completed, committed deliverable for initiative
2026-10-16-update-codex. No long integration tests or deployment have started.
The selected native package was fetched as a prerequisite for schema checks;
dependency-only vendor preparation has also completed.

## Instructions and independence

Read /home/aither/.codex/skills/mandatory-change-review/SKILL.md in full and all
four lane references: general-review, architecture-review, scope-review and
risk-review. Perform these lanes yourself without nested agents. Remain read-only.
Read the workspace AGENTS.md and applicable required procedure routes, plus each
affected worktree's AGENTS.md before reviewing it. The common root is
/home/aither/workspace/ai/vpsfree.cz. Check project instructions against their own
repository, not another project's style or commands.

Overall risk is high: experimental protocol, native daemon/persisted state,
utility isolation, package/runtime compatibility and ordered deployment. There is
no eligible retained reviewer because dev-session team list reports roster null.
The installed catalog's default lead_reviewed team selects review-purpose role
reviewer, model gpt-6-astra, effort xhigh; exact policy is in reviewer-policy.json.
This is the mandatory standalone fallback, not a team addition.

The development host operator is trusted. Apply the generic runtime's documented
trust boundary: preserve remote-client authorization, ordinary concurrency,
wrong-session refusal, state integrity and recovery; do not require protection
against a fully compromised local administrator.

## Requested outcome and boundaries

The user requested latest Codex in dev-workspace/codex-web and aitherdev, a
repeatable skill, then selected repository-owned layered skills plus a workspace
entry point. They authorized aitherdev deployment through configuration and
implementation of the plan, but have not authorized default-branch integration.

Freeze stable Codex 0.163.0 and llm-agents
e85b99217baf13a38fc887b31338b1833f1159c0. Preserve model choices, utility tool
restrictions, application state contracts, saved conversations, package roots and
forward-only application recovery. No new public Go/browser API, fleet rollout,
Rust patch, module-option redesign or package-assembly removal is intended.

The source of truth for each process is its repository's skill. The sequence is
workspace -> configuration -> runtime -> protocol library. Runtime installs its
own and selected lower-level skills through the core catalog. Workspace adds its
entry point using the existing extension override, preserving organization skills.
Configuration's skill remains repository-owned and is routed by its instructions.

## Exact whole-branch inventory

Read review-heads.json for each exact base/head, absolute worktree and complete
ordered commit list. Matching *-series.txt and *-final.diff files retain the full
series and final diffs. Independently inspect actual history and final trees.

There are two codex-web commits (procedure/helper, then bound catalog update),
two runtime commits (upgrade, then skills/catalog installation), three configuration
commits (procedure/docs, generated llm-agents pin, generated runtime pin), and two
workspace commits (procedure/package installation, nested runtime pin).

No application migrations were introduced, merged, released, deployed or
externally consumed. Native upstream migrations belong to the selected Codex
release; old/new reader verification remains an explicit predeployment gate.
Require an explicit independent whole-branch history and migration conclusion.

There are no repeated updates to the same dependency/channel stream in the final
series. Each runtime llm-agents and codex-web selection occurs once in the upgrade
commit; each configuration channel occurs once; workspace's nested runtime occurs
once. Source catalog/hash refresh is one commit. Temporary workspace instruction
length correction was folded into its owning skill commit before this review.
No superseded approach is intentionally retained. Verify these claims.

The runtime upgrade deliberately bundles its Codex input, codex-web Nix/Go pin,
immutable catalog assertions and exact-version naming gates: changing these
separately would produce an unsupported or unavailable naming profile. The skills
and their installation are a separate commit. Generated confctl messages remain
unchanged. Published lower-level feature refs are consumed by the companion
branches, but no feature has been deployed or merged.

## Relevant documentation and consumers

Session plan.md and design.md contain the approved intent, interfaces,
compatibility, verification and recovery brief; state.md has current evidence.
Owning project docs changed: codex-web README/reference and catalog provenance;
runtime codex-package/session-preparations guides; configuration's Codex operations
guide. Each repository's AGENTS.md links its skill. Exact rollout records remain
session-owned. The main operating agent applied the plain technical writing rules.

Consumers discovered from pins/imports: runtime portal imports codex-web and
installs its Luna catalog; runtime mkCodexPackage serves both workspace packages
and aitherdev's system Codex/codex-ds. Configuration selects its host module via
devWorkspace; the workspace selects that same runtime through a direct nested
override while preserving its extension. Root package composition was evaluated.
Inspect these actual consumers and companion feature pins, including Nix package
and extension catalogs, not an assumed consumer list.

## Quick verification already performed

- Exact candidate-generated experimental App Server request/event corpus passes.
- All 55 utility restriction keys/types and literal MCP enabled pass against
  the exact 0.163.0 source config schema.
- codex-web full Go suite passes (TMPDIR=/tmp avoids an unchanged 108-byte socket
  fixture path); 64 browser contracts pass; focused ephemeral tests pass.
- Catalog generation is idempotent and existing semantic Luna derivation tests
  validate the intended three-field transformation and immutable metadata rules.
- Four skill validators pass using Nix Python with PyYAML.
- Runtime local semantic protocol corpus, naming unit tests and codex-web pin
  contracts pass. Local naming tests require a nonexistent isolated provider
  catalog path to avoid the real host catalog; package sandbox tests do not.
- Vendor dependency output passes with its existing hash.
- Configuration input commits pass declared Overcommit hooks. Nix changes are
  formatted and owned source diffs pass whitespace checks.
- Workspace instruction tests pass (8 tests, 144 assertions), root package
  composition evaluates and the cross-project deployment contract passes.
- Semantic lock inspection confirms unchanged extension identity and matching
  runtime/llm-agents identities across workspace and configuration.

Long release gates remain: packaged checks/builds, actual-binary utility isolation
for both profiles, managed naming lifecycle/canary, persisted-state probes, exact
system/application builds, and coordinated deployment acceptance. Do not claim
these passed. Current live versions are system 0.162.1 and workspace 0.160.0.

## Report

Write your report to work/2026-10-16-update-codex/review-report.md (the sole allowed
output mutation). Return findings ordered by Blocking/Important/Advisory, evidence
and precise paths/commits. Assess all four lanes and explicitly conclude on whole
history, repeated update consolidation and migration lineage, including no
migrations when applicable. Identify residual test gaps without treating pending
post-review release checks as completed evidence. State the reviewer identity and
actual model/effort if available; do not invent unavailable identity metadata.
