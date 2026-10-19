# Committed confctl library bootstrap correction

Review the changed confctl adapter and composed pin independently before further
long verification/deployment. Parent implements; you remain read-only and do not
spawn agents. Report findings in your final answer (parent will retain the report).
Read mandatory-change-review SKILL.md and all four lane references. This is an
affected-scope follow-up, not a request to re-review unchanged runtime internals.

Initiative: 2026-10-13-workspace-coordination, workspace
/home/aither/workspace/ai/vpsfree.cz. Applicable workspace AGENTS.md and required
routes: projects, git, sessions, documentation, lifecycle, verification, deployment,
commits; read local extension/workspace AGENTS before inspecting their content.
Prior final/capacity reports and reconciliation are in this tracking directory.

Risk remains high for this deliverable (deployment tooling), though the change is
bounded initialization. Lanes: general, architecture, scope, risk; concentrate on
library integration and diagnostics/protocol behavior affected by this correction.

Outcome: call actual pinned confctl preparation/activation APIs in a standalone
process while preserving bounded private diagnostics and exactly one JSON stdout
response. No new adapter protocol, ledger format, authority, mutation action,
reservation release behavior or exception fallback. No default-branch integration,
archive or reboot authorized. Operator is trusted to administer this host.

Real preparation failed BEFORE activation with undefined method << for nil in
ConfCtl::Logger#write. Its CLI opens Logger; direct library callers must do so.
Actual pinned SystemCommand true reproduces the failure, then succeeds after
Logger.open(..., output: STDERR). Folded that initialization into extension core.
Strict fixture checks logger initialization before machine inspection and stderr
routing. Focused test: 4 tests / 19 assertions, zero failures. Composition check
passes. Inspect pinned confctl at
/nix/store/8mjng71gica53p9jr4085f22xq1zslzg-source/lib/confctl,
including Logger, SystemCommand and CLI initialization; do not activate anything.
The configuration shell only has hooks/gems, not an ambient require-able confctl.
Pinned helper explicitly supplies its own Ruby/GEM_HOME/RUBYLIB. Actual logger
primitive smoke used those same immutable paths, no operator credentials.

Inventory: review-inventory.json contains exact final bases/heads and complete
cleaned two-commit histories for all four repos, plus final patches. Narrow change:
confctl-library-fix.patch. Only extension and workspace changed. Runtime a0be8843
and config e8bcc4b6 remain unchanged. Workspace flake updates only extension locked
identity; direct runtime override and all unrelated nodes remain unchanged.
One runtime selection stream in extension, one runtime/extension selection stream
in workspace, one generated confctl runtime selection in config. All remain
consolidated; no fixup commits. Confirm whole changed-branch history/disposition
and explicitly conclude no migrations (none merged/released/deployed/consumed).
No feature was activated or integrated; the only retained pre-activation state is
one threadless owner, zero jobs/reservations, and immutable profile preparation.
Original candidate remains rooted and unused. Prior reports retain earlier heads.

Owning component: extension WorkspaceConfctlAdapter. Consumer: generic runtime
Engine adapter_call; extension.mkPackage exports helper in coordination catalog;
workspace composes it; config selects matching host/runtime module. Owning docs
are extension docs/workspace-confctl.md, runtime docs/coordination*.md, workspace
docs/coordination.md and config docs/operations/workspace-coordination-aitherdev.md.
Individual rollout is rollout.md. Logger setup adds no new user-visible contract,
so adjacent comment plus rollout diagnosis is the needed documentation.

Catalog fallback selected because no retained roster and previous standalone
review identities cannot be validated in current native list. Installed catalog
digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd,
default lead_reviewed/reviewer: gpt-6-astra, xhigh, read-only.
Do not inspect credentials or change live services. Return an independent report
with concrete findings, test gaps and explicit history/migration conclusion.
