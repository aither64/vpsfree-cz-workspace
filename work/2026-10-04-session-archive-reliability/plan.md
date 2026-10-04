# 2026-10-04-session-archive-reliability

## Goal

Implement the accepted archival reliability plan: completed clean sessions must
archive through the normal command or browser confirmation without worktree
repairs, team-retirement commands, environment exports or page reloads. Include a
supported legacy migration and workspace-wide automatic archive diagnostics.

## Affected repositories

- dev-workspace: archive inventory and recovery, team ordering, host dispatch,
  browser identity, automatic activity/retention, diagnostics and legacy migration.
- workspace: lifecycle guidance and application package selection.
- vpsfree-dev-workspace: downstream runtime pin if needed for the deployable bundle.
- codex-web only if the architect proves a public client addition is necessary;
  retain the current Codex 0.160.0 protocol and dependency direction.

## Approach

- Inventory verified Git worktrees beneath the exact session root, including
  nested auxiliary checkouts. Preserve heads through retained refs, remove only
  clean worktrees, and retain every registered branch obligation.
- Seal auxiliary cleanup identities in a private operation sidecar while retaining
  existing archive journal support. Recover interrupted removal idempotently.
- Retire the verified retained team before the root; preserve unknown-thread,
  idle/submission, committed-tree, exact-head and generation checks.
- Pass host-selected environment through dispatch and support recovery against the
  selected generated protocol contract.
- Remove directory ctime from browser identity, refresh operation state without
  reload, and require fresh confirmation only for genuine session replacement.
- Use actual turn/submission activity, including retained members, for automatic
  inactivity. Administrative settings, polling and restarts must not restart it.
- Preserve elapsed grace for unchanged merge/cleanup failures; unknown activity
  continues to defer and require a fresh trustworthy observation.
- Add workspace-wide CLI/portal archive status and a preview/apply batch legacy
  migrator. Recover branch registrations even when worktrees have been removed.

## Decisions

- User chose fixing false blockers while retaining merged-and-clean requirements,
  and including older sessions, on 2026-10-04.
- Keep existing 1/7/14-day automatic tiers and Keep open holds.
- No implicit abandonment, invented completion, fake historical bases or empty
  registration lists; ambiguous legacy mappings need one batch review.
- Isolate and label temporary legacy support. Record input formats, owner and
  removal criteria: no supported dependent records, unfinished receipts or
  upgrade/revival paths that can reintroduce those inputs. Removal requires an
  inventory, not an elapsed date. The user explicitly requested this criterion.
- The external initiating conversation coordinates this freshly created session;
  its new root received only a readiness request and must not duplicate lead work.
- Default retained delegated roster: architect0 designs, implementer0 edits,
  reviewer0 independently reviews final committed work. Do not alter that roster.

## Compatibility and deployment

Preserve persisted manifests, schema-2 archive journals, runtime ownership and
retained branch semantics. Any additive sidecar has versioned validation and
recovery tests, including legacy receipts and package-generation transitions.
Old helpers may refuse new auxiliary layouts but must not destroy state. The
workspace uses forward-only user-profile package switches; prepare supported
recovery without deleting journals. No database/API daemon/NixOS fleet change or
coordinated node update is expected. Update the deployable extension/workspace
pins only after verified runtime commits. Implementation is authorized; default
branch integration, legacy batch application and archiving other sessions are
not authorized by that instruction.

## Documentation

Runtime behavior and removal contracts belong in dev-workspace project docs;
repeatable migration/recovery instructions belong in its operations guidance.
Workspace lifecycle rules must match the final contract. Record exact rollout
revisions and verification here. Apply the user-facing writing skill directly
before final documentation/interface commits.

## Testing plan

Focused Ruby/Go/browser checks cover nested/detached cleanup, retained and orphan
heads, dirty/foreign state, interrupted removal, partial team retirement,
tracking_committed retry, helper environment, stable browser identity versus
replaced sessions, semantic activity versus settings changes, worker restarts,
legacy records with missing worktrees, ambiguous mappings, tracking-only sessions,
and repeatable migration. Inventory final branch history and migration provenance
and run mandatory independent review after commits/quick checks, before long
packaged/live tests. Delegate long or uncertain verification to fresh Luna/low
watchers from the retained catalog. Keep unrelated state and all branch refs.
