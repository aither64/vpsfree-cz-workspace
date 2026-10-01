# Current-staging provider review packet

Purpose: mandatory HIGH-risk, four-lane independent whole-branch review before
publishing the rebased provider and building the fresh disposable cluster.
User requested current-default rebases and the new React component, explicitly
authorized resetting this cluster, and authorized stopping the cluster occupying
the shared addresses. No default-branch integration or shared-host rollout.

Session: `2026-09-23-storage-redesign`; see [design.md](design.md),
[state.md](state.md) and [rebase-devcluster-20261001.md](rebase-devcluster-20261001.md).
Reviewer0 is retained review-purpose, read-only, GPT-6.1 Sol/xhigh; no override.
Read the canonical skill and general, architecture, scope and risk references.

Repository: canonical registered vpsAdminOS worktree under this session.
Base: `26f28c69149b5312305aceb7f5614bd1d3fe3bbc` (fresh origin/staging).
Head: `8d05dc3ae1fb71c1385609990acdf093af49ceec`.
Complete series: one commit, `osctld: report bounded pool storage activity`.
No migrations. No superseded provider implementation remains in the new series;
dcad and the earlier staging port 107cef remain only retained provenance refs.

The rebase's range-diff is equivalent. All fourteen non-registration final
provider blobs match dcad; tests/all-tests.nix is current staging plus exactly
one osctld/storage-activity registration. Fifteen paths, 883 additions and
23 deletions. Full diff and complete series are available directly in Git.
Tracked tree is clean; preexisting untracked libosctl/tmp is outside the patch
and its metadata was preserved by the implementer.

Owning contract is the generic root-socket pool_storage_activity read command
and bounded gc_trash_v1 observations, documented in docs/osctld/interfaces.md.
The vpsAdmin 5291 Node consumer and private ActivityReport use it. vpsAdmin
remains advisory: child coverage unknown, node_quiet/repair_ready/executable
false, no APPLY and production strict off. Old providers yield unknown;
no fleet-wide coordinated upgrade is required for this inert read primitive.

The new staging lineage supplies modern OSVM per-disk/root-disk preservation
required by the current installed cluster provider. Its test framework and
dependencies must be evaluated at the actual pinned candidate; old-lineage VM
results are prior evidence, not results on this new combination.

Quick evidence: scoped diff --check clean, Overcommit installed/sign active,
fourteen blob parity and additive registration comparison. Fresh Luna/low
utilities ran the five focused osctld specs (36 examples, zero failures) and
normal Nix hooks (Nixfmt/RuboCop, exit 0 after normal signature refresh). Logs
are private under /tmp/storage-redesign-redeploy-20261001/os-specs.log and
os-hooks-signed.log. No local kernel build occurred.
After clearance the exact provider is published and selected by one generated
vpsAdmin pin. Fresh cluster acceptance includes Node/osctld protocol/health and
real React/BFF login alongside legacy PHP, after schema/OAuth seed checks.

Please conclude explicitly on complete history and no-migration lineage,
source/context compatibility, distinct review lanes and residual verification.
No source edits, tests, deployment or nested reviewers in this assignment.
