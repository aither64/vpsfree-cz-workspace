# Portal planning question controls

## Goal

Investigate why a planning question and the standard prompt/settings controls
remain visible together, despite the intended compact question layout. Trace the
current implementation, reproduce the cause, and prepare a focused fix if warranted.

## Affected repositories

- codex-web: shared conversation and question components.
- dev-workspace: host portal markup, styling, and integration of shared controls.
- Shared workspace: investigation tracking only.

## Approach

Inspect current upstream heads and prior question-layout decisions, identify who
owns prompt visibility, and exercise a pending planning question against the
current markup and assets. Preserve unrelated concurrent sessions and changes.
If a defect is established, fix it in isolated feature worktrees and add focused
regression coverage. Commit the implementation, run mandatory review, and report
the resulting scope and deployment status.

## Compatibility and deployment

This is expected to affect browser presentation only. Preserve persisted state,
database schemas, APIs, CLI and Terraform behavior, protocol formats, NixOS
options, session ownership, and approval/question semantics. Assess old/new cached
browser asset combinations if asset imports change. No coordinated node update or
state migration is expected; rollback should continue to read unchanged state.
Investigate the installed package to distinguish source bugs from stale assets.
No integration or deployment is requested at this stage.

## Testing plan

Use repository Nix shells for focused JavaScript/Go checks. Reproduce pending
question visibility and restoration after answering, including responsive layout
and any distinction between blocking and asynchronous questions. Apply mandatory
change review after committed changes and quick checks, before long integration
tests. Record exact results and remaining limits.
