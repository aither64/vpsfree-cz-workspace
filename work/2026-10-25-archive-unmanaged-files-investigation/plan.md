# 2026-10-25-archive-unmanaged-files-investigation

## Goal

Investigate the portal archive failure for `2026-10-22-haveapi-release` and
recommend a durable solution. The requested deliverable is findings and a
proposal; do not repair, retry or archive the affected session or deploy code.

## Affected repositories

- `dev-workspace`: archive discovery, journaled cleanup and portal feedback.
- Coordination workspace: this investigation's tracking and evidence only.
- `vpsfree-cz-configuration`: starting location; no configuration changes needed.

## Approach

Inspect the selected package, systemd journal and blocking directory read-only.
Trace the cleanup invariant and archive ordering. Reproduce the failure with the
installed discovery class and a disposable Git repository. Compare a sibling
cache with the same files inside a verified checkout. Record a bounded proposal.

## Decisions

Keep the failed initiative untouched. Use a separate tracking-only session because
this conversation has no existing session binding. Do not infer the command that
created the cache from its name alone.

## Compatibility and deployment

Investigation makes no runtime, configuration, journal or manifest format change.
Any future support for auxiliary cleanup must preserve old journals and package
rollback rules, and retain strict automatic archive policy and repository checks.

## Documentation

Readers: the operator deciding on repair and developers implementing prevention.
Keep incident evidence and the unimplemented proposal in [findings.md](findings.md).
An implementation should update the owning runtime's archive and session guides.

## Testing plan

Run a short disposable Ruby/Git reproduction using the installed Ruby and archive
cleanup source. Verify sibling-file refusal, acceptance within a registered
checkout, and continued refusal of a loose sibling symlink. Remove the fixture
automatically. No live archive/revive, builds, CI or application changes.
