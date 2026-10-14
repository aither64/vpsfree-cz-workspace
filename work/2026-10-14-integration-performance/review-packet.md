# Final committed integration-performance review

Scope: accepted optimizations 1–5. Plan/design/state are in this directory.
Four feature worktrees under worktrees/2026-10-14-integration-performance.
Exact complete series and bases/heads: review-inventory.json. Inspect full Git
diff/history directly; the packet is not a substitute. No migrations, no releases
or feature deployment yet. Original source refs remain available. Master history
was not rewritten. The source tree after history consolidation is unchanged.

Risk: high (persistent orchestration journals, lifecycle concurrency, deployment
ordering, automatic approval composition/equivalence and package selection).
All lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Reviewer: standalone installed default lead_reviewed reviewer fallback because
roster:null; gpt-6-astra/xhigh/read-only. Catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.

Changed provider APIs: optional integrationConfig; CLI integrate/status/resume and
submit-batch; certified_equivalent lineage; package integration capability; cached
Ruby checks/passthru and dev shell. Existing ledger/snapshot/attempt contracts stay
schema 1. Actual consumers: organization extension calls mkPackage, workspace
selects extension plus nested runtime, configuration selects runtime host module.
The extension implements pin recipes and the workspace selects site mappings.
Nix/CI uses exported checks. Existing standalone commands remain recovery paths.

Scope decisions: auto mechanical refresh and certified reuse authorized by user.
No model/team changes. Keep full substantive initial independent review and exact
Nix derivation check reuse; tree equality alone is insufficient for builds/artifacts.
Local operator is trusted per repository AGENTS; no hostile-operator filesystem
tests. Remote portal clients remain untrusted; driver is CLI-only.

Commit split: source admission/notification, cached test infrastructure and driver
contracts. Shared host/execution/package integration touches multiple behaviors;
please assess series order/dependency coherence, not only final tree. Extension
recipe+new upstream pin are together because the new mkPackage argument requires
that provider API; workspace adoption+pins similarly require the new extension.
Configuration operations docs and generated input pin remain separate. One final
update per input stream, no superseded intermediate pin commits. No released,
merged, deployed or external migration boundary requires an intermediate commit.

Quick verification: admission 4 tests/13 assertions; integration disposable worker,
atomic batch rollback, lost submission reply, status immutability, notification
dispatch and capability 8 tests/29 assertions; certificates 4 tests/8 assertions;
extension recipe 3 tests/8 assertions. Ruby syntax and diff whitespace checks pass.
Pure Nix source-filter assertions prove portal-only edits reuse Ruby derivations
and Ruby command edits invalidate. Nix package/dev-shell/recipe evaluation passes.
Generated locks inspected: intended provider/extension nodes only. Configuration
Overcommit and generated pin hooks pass; no bypass. Full suites not started.

Docs: runtime docs/integration.md with README/coordination links; extension README
and mandatory review skill; workspace coordination/Git/verification procedures;
configuration docs/operations/workspace-coordination-aitherdev.md. Session-only
rollout/evidence stays here. User-facing prose reviewed by lead using writing skill.

Review exact concurrency, owner/incarnation binding, interruption/resume, partial
publication, notification ambiguity, generation transition and certificate
boundaries. Verify complete shard coverage/cache dependencies and stated docs.
Return Blocking/Important/Advisory findings with references, and explicit whole-
branch consolidation/history and migration conclusions. No source edits or nested
agents. Do not run long tests; focused reproduction is allowed with Nix tooling.
