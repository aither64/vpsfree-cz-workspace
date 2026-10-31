# Final runtime branch review

Review all four lanes: general, architecture/repetition, scope/proportionality,
and risk/compatibility. Risk is high because this is a cross-project helper
protocol reader with credentials and mixed-version deployment consequences.

## Scope and revisions

Initiative: 2026-10-06-cluster-status-metadata in
/home/aither/workspace/ai/vpsfree.cz. Read its plan.md and state.md.
Runtime worktree: worktrees/2026-10-06-cluster-status-metadata/dev-workspace.
Base: 4c3ea2eb3b82b572e86f23ec7f9e53a0f1dc6a0c.
Final head: e3315a483f3d3536d492ecbe40f2655449cf630f.
Complete series is one owning behavior commit, with regression tests and its
contract documentation. No superseded approaches, follow-up fixes, compatibility
shims, or migrations are present; no schema/persisted-state changes. Inspect the
full branch and explicitly conclude obsolete history and migration lineage.
The complete full-index diff is runtime-final.diff in this initiative.

Representative producer: installed extension source
/nix/store/0cs72gdqxa8sdl06b6rffd5mv396q7dm-source at selected revision
0ff827df13e82dfab4b536ff29979280f264e8f5; inspect dev-clusters/vpsadmin/bin/devcluster,
dev-clusters/vpsadmin/lib/maintenance.rb, and test/devcluster_status_test.rb.
The coordination workspace consumes it through the extension's nested runtime
override. Its current runtime and the configuration devWorkspace input are
4c3ea2e. The two subsequent revision-pin-only commits will select this exact
reviewed runtime; no extension source update is intended.

## Outcome and bounds

The real helper succeeds with schema 2/running/ready and ten services. Its source
and released-maintenance metadata currently cause portal unknown-field errors.
Restore the existing card by accepting typed optional metadata only at the wire
boundary, validating and discarding it. Public Status/browser UI remain unchanged.
Retain strict field/trailing-output checks, old helper support, and credential
protection. Pending maintenance must replace ready cached service credentials.
No guest work, cluster resets, maintenance receipt manipulation, new metadata UI,
generic metadata framework, or transition-policy changes.

The local operator is trusted for host administration; assess ordinary mistakes,
concurrency, integrity, rollback/refusals and remote-client boundaries. Do not
invent local hostile-operator filesystem defenses. The storage session is only
a read-only reproducer and must not be mutated. No secrets are in this packet.

Quick evidence: Nix shell go test -mod=readonly ./internal/cluster passed (0.993s);
focused ./internal/web -run Cluster -count=1 passed (0.140s); git diff --check passed.
All intended substantive code/tests/docs are committed; runtime has no declared
hook framework or active pre-commit/commit-msg hooks. The doc update was checked
against producer fields and main-agent writing guidance. Long checks have not
started. User authorized aitherdev and user-profile deployment, then verified
fast-forward integration into the three named master branches. Persisted state
is unchanged; recovery uses the same/newer compatible policy-3 package.

## Reviewer selection

No eligible retained reviewer exists: this newly created no-Codex initiative has
no root roster. Per mandatory-change-review, use the installed default development
team's reviewer role: gpt-6.1-sol/xhigh/read_only, catalog digest
3343a06cbc8d3c181df52770086fb807894f9990132bb0792048e0ddabb764f8.
Remain read-only; return findings and evidence to the lead without nested agents.
