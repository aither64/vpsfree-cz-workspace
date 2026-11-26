# 2026-11-26-compressed-zfs-send

## Goal

I'd like to enable compressed zfs send in vpsadminos and vpsadmin by default. there were some zfs bugs in the past that made us avoid it, but now we're transferring needlessly large data and lose time decompressing/compressing. so essentially enable the `-c` switch on `zfs send`. handle all occurrences in vpsadminos/vpsadmin, so ct sends, backups, etc.

I wonder if it would be possible to make it easier to toggle this and possible other settings in the future using configuration rather than modifying code.

Investigate and suggest a solution.

## Affected repositories

- vpsadminos: container send/copy/migration, image/storage utilities and other send users.
- vpsadmin: node dataset transfer, backup and restore paths and configuration modules.
- Local OpenZFS references may be read to resolve stream compatibility; no ZFS changes.

## Approach

Investigation and recommendation only, as requested. Inventory all send construction
and execution paths at recorded canonical default heads, inspect existing
configuration seams, then propose default-on compressed sends with an operator
override. No application edits, new worktrees, tests or deployments in this phase.

| Package | Owner | Acceptance | Status |
| --- | --- | --- | --- |
| vpsAdminOS send/config inventory | implementer0 | Complete operation/flag map, source references, config choices and gaps | Executing |
| vpsAdmin send/config inventory | implementer1 | Complete operation/flag map, source references, config choices and gaps | Executing |
| Cross-project design and check plan | architect0 | Minimal proposal, compatibility/recovery, residual gates and execution boundaries | Executing |

Other retained members remain unassigned; no independent review is required for
investigation/findings alone. Lead owns scope, acceptance and tracking.

## Decisions

- Preserve the session's saved delegated_5 roster/settings; use only two independent
  repository surveys plus the retained design owner for this investigation.
- Prefer repository-native configuration; determine semantics from source before
  choosing specific option names or allowing arbitrary flags.
- Historical bug resolution must be established from evidence, not assumed.

## Compatibility and deployment

Assess compressed stream receiver/pool features, all send modes including estimates
and resume, persisted send state and mixed-version operation. Distinguish disabling
future compression from restoring streams already produced with compressed blocks.
No integration/deployment is authorized or planned for this investigation.

## Documentation

Readers: maintainers choosing implementation and operators needing an escape hatch.
Current findings and proposal belong in this session's findings files and design.md.
An implementation should document enduring option semantics in each owning project;
concrete rollout receipts remain session records.

## Testing plan

Read-only source and bounded history inspection now. Proposal must identify focused
flag/config tests and realistic full/incremental/resume receive checks, including
backup/restore, before any later default change is considered verified.
