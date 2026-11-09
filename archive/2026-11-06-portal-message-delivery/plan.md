# 2026-11-06-portal-message-delivery

## Goal

Keep explicit portal and team messages deliverable during long active turns,
independently of automatic-retry evidence compaction. Implement the solution
approved in this conversation after investigating the livepatch session lockout.
The user explicitly authorized implementation and then session tracking.

## Affected repositories

- dev-workspace: managed delivery, retry evidence storage and package compatibility,
  interruption settlement, diagnostics, tests and documentation.
- codex-web only if its existing typed delivery errors and submission ledger
  cannot express the required behavior; prefer the existing public interface.
- workspace and vpsfree-cz-configuration: matching runtime selection for the
  authorized aitherdev rollout, preserving extension/Codex/unrelated inputs.

## Approach

1. Record the design and acceptance checks after inspecting the current source.
2. Separate durable delivery receipts from automatic-retry eligibility. Preserve
   authorization, uncertain-submission reconciliation, immutable attempt IDs and
   cancellation ordering; retry verification must not gate ordinary input.
3. Replace the total 64-snapshot JSON budget with indexed SQLite evidence and
   shared immutable settings. Bound work per operation without limiting a turn's
   total accepted messages. Migrate supported records atomically.
4. Settle confirmed interruption immediately and classify known pre-send
   rejection correctly. Expose actionable compaction failure diagnostics.
5. Commit, run focused checks, independent final review, broader verification,
   and publish the feature branch.
6. Deploy to aitherdev through the matching configuration and workspace profile,
   verify service health and delivery, then integrate the deployed feature lineage.

## Decisions

- Initial investigation was read-only and untracked; tracking is authorized now.
- This initiative is threadless (`start --no-codex`), retaining this conversation
  as lead rather than creating a second executing lead. No retained team roster
  exists; ordinary lead execution, catalog-selected final reviewer and fresh
  verification utilities apply. Do not use the livepatch session's team.
- The original incident has confirmed capacity refusal and incorrect unknown
  delivery classification. Why its prefix compaction stopped remains unresolved.
- Subsequent user approval: "aitherdev can be deployed using
  vpsfree-cz-configuration. once deployed and verified, you can merge it".
  Scope: aitherdev deployment, then master integration of dev-workspace and its
  required workspace/configuration pins after successful live verification.

## Compatibility and deployment

Existing retry epochs, pending automatic identities, uncertain receipts and
settings proof remain authoritative. Migration must preserve them and be
restart-safe. Older packages must refuse incompatible persisted state before
activation; recovery is forward to a compatible package. No native Codex protocol,
model package is to change. Deployment updates only matching runtime selections;
ordinary package migration owns live evidence conversion. Do not manually edit
live-session records or send test messages to the original livepatch session.
Delivery API compatibility should use existing codex-web typed errors. SQLite
evidence retention and package-transition readers require explicit coverage.

## Documentation

Update dev-workspace's retry recovery and portal guides for operators and
maintainers. Keep investigation, verification and rollout status here.

## Testing plan

Focused storage/migration, managed-send and interruption tests; more than 64
messages with compaction deliberately unable to advance; restart and lost
acknowledgement reconciliation without duplicate delivery; interrupted and failed
automatic attempts; package compatibility refusal for old readers. Run broad
Go/Ruby/browser and applicable native integration checks after final review,
using disposable state and fresh verification watchers. Preserve the live portal.
