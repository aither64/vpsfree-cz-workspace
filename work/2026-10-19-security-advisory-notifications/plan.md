# Hourly security advisory digests

## Goal and authorization

Implement the finalized plan as requested by the user: “Implement the plan.”
Update both the bot and its package/settings in site configuration. Deployment,
service restarts, and default-branch integration are out of scope. Keep this
session open.

## Design and affected repositories

The accepted technical brief is [design.md](design.md), with the finalized chat
plan authoritative where it narrows scope. Its proposal-only and rollout wording
is historical; implementation is now authorized, deployment is excluded.

- `vpsfree-irc-bot`: individual/summary/off modes and positive integer
  `summary_interval` seconds, default 3600. Omitted mode stays individual.
- `vpsfree-cz-configuration`: select summary/3600 for the Libera instance,
  preserve channels, update `packages/vpsfree-irc-bot/default.nix` to the final
  published bot revision and matching source hash. No unrelated input updates.
- Existing vpsAdmin/HaveAPI contracts are read-only dependencies; no changes.

## Behavior and compatibility

Poll each minute. Accumulate distinct new/updated advisory IDs across polls.
New takes precedence for an ID throughout the interval. Emit at most one line
per channel per interval, skip empty windows, and link the existing WebUI list.
First output waits a full interval after bootstrap; arrivals never postpone
its deadline or trigger early output. Use monotonic scheduling and no catch-up
bursts; schedule a full interval after delayed processing.

Off keeps consuming events silently without accumulating a digest. Preserve
individual notices, eligibility, existing storage and silent bootstrap. Pending
digest counts remain in memory and are discarded on restart. No durable delivery,
API/schema migration or fleet coordination. Old versions can read state, but
ignore new mode settings and restore individual output; package and settings
must select compatible versions together. No production actions in this task.

## Owners and dependencies

- implementer0 owns bot diagnosis, code, tests, documentation, quick checks,
  commits, publication and review fixes.
- implementer1 owns site settings, final package pin/hash, configuration checks,
  commits, publication and review fixes. Final pin depends on bot publication.
- reviewer0 provides independent committed-deliverable review after quick checks.
- Lead coordinates scope, tracking, user-facing writing, acceptance and watchers.

## Documentation and verification

Readers: bot maintainers and site operators. Update bot README/sample config for
supported modes, interval and restart/off semantics. Session records own temporary
branch/review evidence. Lead applies vpsFree writing guidance before prose commits.

Cover gradual arrivals, cross-poll distinct counts, overlap, update/retraction-only
and empty windows, fixed deadlines, first delay, delayed processing, all modes,
validation, routing, URL, restart and complete API enumeration. Run quick tests
and hooks first. After final commits, inventory full histories, diffs, pin streams
and migration provenance, then independent review. Only then run targeted
vpsadmin-events integration with shortened intervals and evaluate/build the
single affected bot container without activation. Fresh policy watchers own long
or uncertain checks. Publish feature branches; no PR unless local rules require.
