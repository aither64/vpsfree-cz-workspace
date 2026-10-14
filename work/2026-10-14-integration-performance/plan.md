# 2026-10-14-integration-performance

## Goal

Implement accepted integration optimizations 1–5: a resumable driver, bounded
shared admission, mechanical refreshes, certified evidence reuse, and cached,
parallel verification. Model/team settings are out of scope. Standard aitherdev
targets: administration <=5 minutes; full verification/rollout <=30 minutes with
dependency caches populated, excluding external queue waits.

## Affected repositories

- dev-workspace: coordination, integration driver/certificates, Nix checks, docs.
- vpsfree-dev-workspace: immutable confctl recipe and review/monitor guidance.
- workspace: recipe selection, runtime pins, procedure adoption.
- vpsfree-cz-configuration: matching runtime pin and aitherdev operations guide.

## Approach

Implement admission/notification isolation first, split verification next, then
certification, driver/recipes and adoption. Reuse the existing coordinator's jobs,
dependencies, approvals, reservations, physical claims and recovery.

## Decisions

- User requested automatic mechanical refreshes and certified review/check reuse.
- Stop on conflicts, new behavior requiring review, or uncertain effects.
- Batch submission is atomic admission, not a cross-repository Git transaction.
- Preserve original revisions and independent substantive review.
- This conversation owns design and implementation; retained roster is null.
  Native session root is notification-only, not an implementation delegate.
- "Implement the plan" authorizes the described aitherdev rollout. It does not
  authorize integration of these feature branches into master.

## Compatibility and deployment

Preserve ledger/snapshot/attempt schema 1 and existing jobs. New driver journals
and certificates are separate versioned files; pending runs require an advertised
integration capability at package selection. No DB/API/CLI-client/protocol or
vpsAdminOS changes. Lifecycle writers remain exclusive; notifications retain a
shared lifecycle/generation guard during RPC. Profiles recover forward.
Old package checks remain supported. Exact tree equality does not establish Nix
derivation or machine artifact equality; confctl self.rev remains exact.
Deploy matching module/runtime from configuration, then application profile under
the same reservation. Retain feature refs and session; no archive/delete/stop.

## Documentation

Generic contracts/recovery: runtime coordination guides. Site recipes and policy:
extension/workspace guides. Concrete rollout: configuration operations guide.
Session decisions and evidence: design.md, state.md and curated result bundles.

## Testing plan

Quick focused checks before committed-deliverable independent review. Long checks
after review using a fresh Luna/low utility watcher. Exercise contention, lifecycle
exclusion, slow delivery, resumable/idempotent runs, concurrent baselines, positive
and negative certification, derivation invalidation, complete shards, and existing
schema-1 compatibility. Record three comparable benchmark runs by phase, cache
condition and queue time. Canaries use disposable repositories and owned state.
