# Compact file tree and scrolling commit details

Approved implementation 2026-09-12, reusing the active initiative and all retained
feature branches. Baseline deployed profile 31: runtime 41c6d75, provider de83e9c,
organization 6c98b36, site cd648e2; coordination handoff f106e8c.

## Behavior

Remove tree file counts, repeated aggregate counts and copy buttons. Keep colored
status letters, one-line basenames, ellipsis/full-path tooltips, selected-file
styling and header path copying. Add decorative native SVG open/closed folders
beside native directory disclosures. Retain expansion/keyboard/history behavior.

Keep a compact toolbar with identity, Back to repositories, copy-link and layout
controls. Full commit message, author/date/hash-copy, parents and aggregate stats
belong to the right pane before the diffs and scroll away. Remove message height
cap and separate scrolling. Apply the same structure to branch details. Keep the
left tree independently scrollable and mobile stacked layout. Opening without
file/line starts at details; explicit file/line navigation reveals that target.

## Components, compatibility and delivery

Runtime owns repository UI; codex-web copy/editor interfaces remain unchanged.
Organization and site only pin the resulting package. No new dependencies, API,
URL keys, database/schema/protocol/canonical/private state changes. Old and new
packages accept the same URLs and state, including rollback. No migration,
system configuration or coordinated node update. Deploy runtime -> organization
-> site through normal workspace-host switch, preserving the open initiative.
The user subsequently authorized default-branch integration on 2026-09-12. After
live acceptance, fast-forward all four reviewed branches into their remote master
branches, verify CI, and retain the feature branches/session. No archive, delete
or session-stop authorization was given.

Two independently reviewable runtime commits: compact tree and scrolling details,
with their associated browser checks/docs; separate downstream pin commits. Apply
user-facing writing guidance directly before committing. Run Nix JS and focused
checks, actual component browser acceptance, mandatory fresh xhigh adaptive review,
then exact package/CI and live browser acceptance. Cover long messages, initial vs
explicit targets, scrolling/toolbar geometry, folders, copying/counts, parent/history,
full-file return, desktop/mobile, strict CSP and existing lazy/editor limits. Retain
useful screenshots/results, record review findings and provide stable portal URL.

CI exposed an existing 500 ms wall-clock acceptance-test flake. Add a separate
test-only runtime commit proving response order while validation stays blocked,
then amend only this follow-up's downstream pins. No creation behavior change.
See compact-ci-investigation.md for failure evidence and focused verification.

Final delivery: profile 32 passed 27 live checks, then all four exact heads were
fast-forwarded into remote master. The user requested cleanup and no waiting for
CI. Clean feature/integration worktrees and temporary files were removed; local
and remote branches and the open session were retained. Provider/runtime master
CI passed; organization master CI is recorded at its last observed running state.
