# Portal changed-character highlighting investigation

## Goal

Explain the fragmented changed-character backgrounds in the supplied portal
screenshot and the immutable review of `configs/vpsadmin/api/abuse_notice_parser/master_dc.rb`.
The request is an investigation; collect a reproducible diagnosis and a concrete
repair recommendation before any implementation or deployment.

## Affected repositories

- `aither64/dev-workspace`: portal review model, editor decorations, locked
  CodeMirror diff dependency, and regression coverage.
- `vpsfreecz/vpsfree-cz-configuration`: immutable before/after Git objects used
  only as evidence. Do not modify the source session or its worktree.

## Approach

1. Compare the supplied screenshot with the exact review payload.
2. Trace Git line classification, character comparison, syntax coloring, and
   editor decoration rendering independently.
3. Reproduce the marked ranges using the locked dependency and exact sources;
   test whether the behavior is deterministic and how it handles unrelated code.
4. Record the root cause, impact, coverage gap, and bounded repair options.

## Decisions

- Reuse verified current session `2026-09-15-portal-diff-highlighting`.
- Keep the user attachment and reproducible source snapshots outside Git.
- No project feature branch is required for this read-only investigation.

## Compatibility and deployment

No application, database, API, protocol, Nix configuration, persistent format,
or deployment changes are planned. A potential rendering repair should preserve
Git line classification, immutable review identities, source contents and line
links in both layouts. Browser-only changes can be rolled back without migration.

## Documentation

Readers are the user and future portal maintainers. Read the runtime README,
portal guide and repository instructions. Keep diagnosis and evidence in this
initiative; promote a concise reusable lesson to `notes/dev-workspace/` if useful.
No supported behavior change requires project documentation in this phase.

## Testing plan

Inspect deployed assets and API payloads, run the existing projection with the
locked CodeMirror version against the reported immutable sources, inspect
representative ranges and compare repeated runs. Use focused existing tests if
helpful to establish why this case escaped coverage. Do not deploy or run long
integration suites for this investigation.
