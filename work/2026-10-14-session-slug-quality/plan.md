# 2026-10-14-session-slug-quality

## Goal

Generate concise session names from the task, accepting two-word names such as
`workspace-notifications`. Stop automatic creation on naming failure and let the
user retry naming or supply a custom name without losing the accepted request.

## Affected repositories

- dev-workspace: naming policy, preparation recovery API and browser, tests/docs.
- workspace: composed runtime selection in an isolated feature worktree.
- vpsfree-cz-configuration: matching dev-workspace/devWorkspace channel pin.

## Approach

Use the existing isolated ephemeral naming helper and existing preparation
format. Accept 2-6 words, prefer 2-3, and instruct the model to summarize the
subject and intended work. Preserve the 48-byte limit, concurrency and deadline.
Replace prompt-prefix fallback with a failed/stopped preparation before slug
reservation. Add a derived canSetName status and identity-bound POST /name to
resume the same request with a custom name. Keep submission snapshots/digests
immutable and save selection in Base/NamingOutcome. Permit another manual
selection after a pre-reservation custom-name collision. Log sanitized helper
error categories; do not log remote diagnostics, input or output.

## Decisions

User selected pausing creation on naming failure and explicitly accepted
two-word names. User authorized aitherdev deployment and said "you can merge
this feature when deployed & verified". Integration scope is master in
dev-workspace, workspace and vpsfree-cz-configuration after verified deployment.
This conversation had no bound session; created this separate tracking-only
initiative without another Codex lead or team. Parent owns design and edits;
final reviewer and verification watchers follow installed policy.

## Compatibility and deployment

Keep schemas, existing slugs, frozen reservations, attachment ownership,
receipt IDs, original prompt/settings and CLI/fork/plan naming unchanged.
Attachment-only requests retain session as their base. Earlier readers retain
their previous retry behavior; use the new runtime and refreshed browser assets
for new naming recovery. There are no database or on-disk migrations.
Publish exact feature heads, pin both composed workspace and configuration to
the runtime, check the deployment contract, build outside claims, and activate
system then application user profile through the coordinator under the shared
vpsfree:aitherdev reservation. Recover forward under the original jobs. Merge
only after deployed acceptance, preserve feature refs and leave the session open.

## Documentation

Update dev-workspace docs/session-preparations.md and docs/workspace-portal.md
for users/API clients/operators. Keep rollout evidence in this initiative.

## Testing plan

Quick checks: focused Go/browser naming/preparation tests, JS syntax and diffs.
Independent committed-deliverable review precedes long tests. Then run package
checks and actual pinned native naming-runtime tests with fresh utility watchers.
Verify failure preservation, custom continuation/collision, stale/concurrent
actions, lost responses, restart recovery and earlier-reader compatibility.
Exercise the real helper with the supplied notifications prompt and diverse
requests; require descriptive names without conversational prefixes. Verify
deployed system/profile revisions and portal/Codex continuity before merging.
