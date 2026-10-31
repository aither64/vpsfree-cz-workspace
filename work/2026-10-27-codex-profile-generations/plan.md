# Codex generation retention implementation

## Goal and authorization

Implement the accepted plan to remove redundant per-application Codex roots, deploy and verify on aitherdev, and integrate the verified feature. User on 2026-10-31: “okay, so create a plan to implement it. aitherdev can be deployed using vpsfree-cz-configuration. when it's verified and done, you can merge it.” Subsequent “Implement the plan” accepts the proposed three-repository implementation/deployment/integration sequence. Targets: dev-workspace, workspace and vpsfree-cz-configuration → master, conditional on successful checks/review/deployment verification. No session lifecycle action authorized.

## Design and boundaries

The architect-owned [accepted implementation brief](design.md#accepted-implementation-and-verification-brief--2026-10-31) is authoritative. Historical investigation is retained there. Existing standard application profile retains bundled Codex; Nix runtime roots retain running store executables and closures. Keep codex/current for independent selection and existing pending/forward recovery; remove redundant numeric history through existing collector preview/apply. No replacement history, per-process pins, Codex upgrade, native-release pruning, forced GC or unrelated profile cleanup.

## Owners and dependencies

1. implementer0: dev-workspace writers/helpers, bounded collector action, focused tests, technical docs, hooks/quick checks, commit/publication and fixes.
2. implementer1: independent workspace/configuration preparation; exact final pins depend on published runtime head. Preserve nested runtime override, extension/siblings/follows; use confctl channel for configuration.
3. reviewer0: independent final committed-deliverable review after quick checks, including full histories/root-retirement provenance.
4. lead: acceptance, tracking, watcher verification, claims, system then user-profile activation, live validation, approved merges and release.

## Compatibility and migration

Collector uses existing exclusion and strict pending parser, preserves unknown layouts and current/profile roots, checks exact link/profile identity, and unlinks only recognized numeric direct-store symlinks. Valid pending skips only this cleanup; invalid pending fails closed. Existing forward recovery/schema/protocol stay unchanged. Root retirement is idempotent; Nix GC determines store liveness. No database migration.

## Checks and delivery

Quick focused Ruby checks/hooks, then independent review, then declared packaged checks and applicable transition/collection integration checks with fresh pinned Luna/low utilities. Final workspace/configuration lock identities must agree via bin/check-dev-workspace-deployment. Build final committed app/system before machine claim. Under vpsfree:aitherdev claim dry-activate/switch system without reboot then workspace-host user-profile switch. Verify exact identities, root retirement/current selection, services, naming and conversation/tmux continuity. Integrate runtime then consumers with short claims/FF/SSH/remote proof; release physical machine once verified and complete deployed lineage integrated. Session remains open.

## Documentation

Implementer0 updates owning package/collector docs; rollout/review evidence stays in this session. Shared plan/state follow normal tracking commit cadence. Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-codex-profile-generations/
