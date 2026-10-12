# Portal review experience: remediation review

Read this packet, plan.md and the original review-packet.md for the requested
behavior, accepted boundaries, component ownership and consumers. This packet
supersedes the original heads and implementation details below. Review the final
committed series and concentrate on the design changes since the first review,
including their interactions with existing code. Do not merely confirm the listed
fixes. Perform the assigned lane directly without nested agents or edits.

All four lanes apply, each fresh gpt-5.6-sol/xhigh. Risk remains HIGH for private
persistence, asynchronous recovery, public protocol consumption and package
rollback. The local operator is trusted; remote clients are untrusted. No new
dependency, schema migration, system configuration change or Codex version change
was added during remediation. Earlier unmerged recorder iterations were never
deployed and require no migration.

## Changes requiring renewed review

The authority-wide JSON activity ledger was replaced by a private directory with
per-thread asynchronous writers, bounded current checkpoints and compact per-turn
summaries. Closed requests are discarded. Snapshots include only durable coverage;
a stalled or failed writer leaves its pending interval unclassified. Thread caches
retire when no longer watched/read, while historical summaries remain available.
History caches and cancellable pagination are per-thread, and interrupted backfills
retain completed pages. Snapshot aggregation is outside event locks. Ordinary
ReadThread once again requests only the latest 20 full turns. Complete turn
metadata is internal to ReadActivity; unused public arrays were removed.

Creation receipts now form a bounded completed retry cache. Lifecycle-aware cleanup
retains pending journals and attempts, removes old request/evidence companions,
and allows fully deleted destinations to reuse names. A canonical session created
independently by the old package can no longer be shadowed by a stale receipt:
the receipt becomes conflict and the canonical page remains usable. A binding
written before any destination journal does not alone establish ownership. Goal/
settings contradictions are reconciled; a fork with binding but neither completion
evidence nor fork journal cannot be recovered by the CLI and is also a conflict.
Pending journals continue to control recovery. Established exact fork journals
recover after their source is archived/deleted, with source validation remaining
required for a fresh fork. Existing manifest and strict journal schemas remain.

The narrower directly checked fixes use complete Git rename detection with the
existing process deadline, simplify typed renderer selection from normalized
activity, and call the required shared browser export directly. No new viewer
behavior was introduced. CodeMirror and all transitive versions remain unchanged.

## Verification

Provider full Go and race suites, browser contract and selected Codex0.154.0
experimental schema pass. Stress covers25,000 request cycles across250 turns,
compact storage and exact restart totals, stalled writer/RPC isolation, cancellable
history progress and bounded recent transcript reads. Exact provider CI passes
at4dde3c6: https://github.com/aither64/codex-web/actions/runs/34693913115.

Runtime all Go packages and browser unit contract pass against actual pinned
provider4dde3c6. Creation full web race and focused subsequent rollback race
regressions pass; Ruby26 runs/255 assertions pass. A1001-modified-renames fixture
passes with all rename metadata preserved. Vendor hash was regenerated from a
fake hash to force a fresh fixed-output build.

Long packaged VM, actual App Server/browser creation, live profile upgrade and
rollback tests remain pending until this review is reconciled. Prepared harnesses
are initiative artifacts, not installed code. Do not treat them as completed
verification. No default branches were merged, no deployment performed.

## Commit series and dependency chain

Provider keeps typed rendering and timing in two owning commits. Runtime keeps its
original seven behavior/dependency commits, with remediations folded into their
owners. Organization and workspace contain delivery pins only. The Go module,
Nix provider source and shared browser assets select the same provider commit.
Final exact bases, heads and old-reviewed-to-final comparison ranges follow.

- codex-web: `269962eb65007581ba69c205634f9e6c14cc39d3..4dde3c6aaa1d038c518563762fa7ac480b650cd2`
  Original reviewed to final tree: `bba2ae1d9796dc7267c0bfc5ee9f072f43d6e92e..4dde3c6aaa1d038c518563762fa7ac480b650cd2`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`.
- dev-workspace: `bcbaf825d71285cbbd05b56e78bc386f2df480bd..40837d245e867aa0edd35f59f72b63bba80034d1`
  Original reviewed to final tree: `774c2083333b9b71d4abb04d4aa7c79ea0aa897d..40837d245e867aa0edd35f59f72b63bba80034d1`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`.
- vpsfree-dev-workspace: `c4df3838de8b42083bd43e86bfdff7d45a7e952f..4e03a3f0a3fd439ae2c645ab41fa736051c5b8c9`
  Original reviewed to final tree: `d0ebe39e4cc2e41cb791ad048c60eb1e940c023e..4e03a3f0a3fd439ae2c645ab41fa736051c5b8c9`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`.
- workspace: `e0d3dee52ac637a96a7d73299aecd753759b484b..ea6cc34a303dc2c8d9027f109a2212d1ebea02c5`
  Original reviewed to final tree: `bfc80f25864528b5b954daf84c6e8a7d4a8348c7..ea6cc34a303dc2c8d9027f109a2212d1ebea02c5`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`.

Vendor hash: `sha256-TXo4Wd1OI7+voHwR8InNxlu/P9fCwvn1LyYbyl8MHO4=`.
Creation final narrow fork boundary race regression passed8.730s.
All four code/pin worktrees are committed and clean. Runtime autosquash
resolved only README context and preserved exactly the tested final tree.
