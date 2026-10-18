# 2026-10-18-portal-untracked-files

## Goal

Open local links to tracked and non-ignored untracked files in verified session
worktrees, the shared workspace, and existing session tracking folders without
staging or artifact registration. The reported Rust design link must open.

## Affected repositories

- dev-workspace: file authorization, source viewer labels/errors, tests and docs.
- workspace: matching direct nested runtime selection and composed lock.
- vpsfree-cz-configuration: matching dev-workspace channel for aitherdev.

## Approach and decisions

Preserve routes, query parameters, source enums and preview fields. Extend the
current regular-file reader using exact literal Git index/untracked membership.
For tracking paths, preserve published artifact authorization and add independent
eligibility for ordinary tracked/non-ignored files. Publication still governs
the artifact list, preview and download endpoints. Session lookup determines the
active/archive root. Archived project source remains the recorded final commit.

The user selected non-ignored files; do not broaden access to ignored untracked
files except existing explicitly authorized artifacts. Keep the Rust initiative's
records untouched. Its design is tracked, but its catalog incorrectly prefixes
the session-relative path with work/<slug>/. Direct reads remove that dependency.

## Compatibility and deployment

No persisted schema, DB, protocol, CLI, generated client, host module option or
journal changes. Old/new browser routes and response shapes remain compatible.
Older packages can read all existing state but lack the wider file eligibility.
Preserve metadata restrictions, registration verification, confinement, symlink
rejection, preview limits and authentication. Do not capture/archive untracked
project contents as part of this feature. Recover packages through supported
forward recovery, never by bypassing profile transition/coordination guards.

Publish feature branches and set matching exact runtime pins in the workspace
and configuration using the documented nested override/confctl channel. Check
composition before preparing system activation then user-profile activation.
User deployment authorization: "aitherdev can be deployed using
vpsfree-cz-configuration", followed by "Implement the plan." Default-branch
integration has not been authorized. Respect vpsfree:aitherdev ownership.

## Documentation

Update dev-workspace's portal file-link contract and source-viewer UI text for
developers/operators. Keep rollout revisions/results here, not in feature docs.
Apply the user-facing writing skill directly before committing prose.

## Verification

Focused file-reader/HTTP/browser checks first, followed by completed-commit
independent review covering all applicable lanes and whole-branch history.
Then packaged Go/browser/Nix/composed-workspace checks and CI, with a fresh
Luna/low watcher for each long batch. Cover ignore rules and local exclusions,
tracked ignored files, published ignored artifacts, literal/encoded paths,
missing and wrong registrations, symlinks/directories/FIFOs, preview bounds,
line anchors, archive reads, and the workspace-prefixed catalog regression.
Live acceptance requires the original Rust design link to return the file in
the deployed viewer and a disposable non-ignored untracked link to open while
its ignored sibling remains unavailable.
