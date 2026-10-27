# 2026-10-26-document-title-notifications

## Goal

seems to me that document title icons in the dev-workspace portal aren't working as they should. I have a session that is waiting for my input (asking if it should implement the plan) and yet it's document title has no marker. the codex tab has a badge as it should, but document title doesn't signal anything. please investigate.

## Affected repositories

- `dev-workspace`: portal document title and session notification aggregation.
- `codex-web`: Codex tab badge and conversation attention semantics (reference
  investigation until evidence establishes a change is needed).
- workspace: nested runtime selection and composed application package.
- `vpsfree-cz-configuration`: matching devWorkspace channel and aitherdev host.

## Approach

Implement the accepted background attention correction described in `design.md`.
Architect `architect0` owns the design; `implementer0` owns the controller, tests,
documentation and follow-up fixes. `implementer1` owns matching workspace and
configuration pins after the fixed runtime is published. The lead coordinates
acceptance, independent review, verification, deployment, integration and release.

Restore bounded five-second attention reads and title reconciliation while hidden;
preserve focused-only acknowledgement/presence and pause heavier hidden reads.
Retain identity, generation, pagehide and stale-result fences. Update existing
synthetic/Firefox expectations and asset version, without adding infrastructure.

## Decisions

- User approved the plan with "Implement the plan." The preceding instruction
  directs aitherdev deployment via `vpsfree-cz-configuration`, then merging and
  release after verification. Approved repository/target set: `dev-workspace`,
  workspace and `vpsfree-cz-configuration`, each `refs/heads/master`.
- Release means the exact aitherdev machine claim; no session lifecycle action.
- No codex-web, native Codex, server protocol/store, schema or migration changes.

## Compatibility and deployment

The browser fix preserves persisted state, schema and public interfaces. Old open
pages retain their existing behavior until reloaded; mixed pages use the same
attention endpoint/read IDs. Keep unrelated input graphs unchanged. Select the
same exact runtime in workspace and configuration, run the deployment contract,
prepare system/profile closures, then claim `vpsfree:aitherdev` for host activation
followed by application user-profile switch. Verify effects and lineage before
release; use compatible forward recovery on uncertainty.

## Documentation

Readers: portal users, future maintainers and rollout operators. Keep supported
behavior in runtime notification/portal documentation, design in `design.md`,
current progress in `state.md` and this rollout's exact paths/heads/input evidence
in `rollout.md`. Lead owns required user-facing copy.

## Testing plan

Run focused Node attention/syntax checks and Nix evaluation first. Commit all
intended changes, consolidate branch history/pins, then obtain retained reviewer0
final review of complete series/diffs and no-migration provenance. Afterwards run
required packaged and creation/archive VM checks plus existing native Firefox
visibility acceptance. Fresh monitor utilities own long checks/builds. Build
configuration/profile and verify matching input contracts before reserving the
machine. After deployment verify exact live system/profile/assets, portal health,
conversation continuity, background markers and focused clearing. Merge approved
targets with short per-repository claims, prove remote lineage, release aitherdev.
