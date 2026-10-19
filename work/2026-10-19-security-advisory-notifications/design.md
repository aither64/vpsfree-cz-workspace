# Security advisory notifications — PROPOSED

Revised recommendation, prepared by architect0 on 2026-10-19 following the
user's correction that gradual arrivals would still make per-poll summaries
spam. This supersedes the initial per-poll proposal; it is not user-approved
implementation. Implementation awaits the user's choice through the lead.
No source changes, fetches, worktrees, commits, tests, review or deployment were
performed for this investigation or revision.

## Recommended behavior

Add `security_advisories.mode` with `individual`, `summary` and `off`. Keep
`individual` as the default when omitted; select `summary` in the site's bot
configuration. Reject an unknown mode during configuration instead of silently
falling back. Preserve the existing behavior when the entire advisory
configuration is absent: the plugin is not loaded.

Add `security_advisories.summary_interval`, a positive integer number of seconds,
defaulting to `3600`. Reject a supplied zero, negative or non-integer value during
configuration. Only summary mode uses the interval; individual mode retains its
existing reporting behavior. The proposed site settings are:

```nix
security_advisories.mode = "summary";
security_advisories.summary_interval = 3600;
```

Keep API polling every 60 seconds. Summary mode accumulates distinct new and
updated advisory IDs in memory across polls, then sends one combined line per
configured channel at an interval boundary, for example:

> 12 new security advisories, 3 updated in vpsAdmin: <advisory list URL>

Omit empty categories and use singular/plural forms. Count distinct advisory
IDs, not CVEs or update records. Multiple updates to one advisory count as one
updated advisory. Across the entire summary window, an advisory classified as
new counts only as new, even if it also has updates in later polls. New means an
unseen advisory whose current
state is `published`, matching the existing notification condition; updates
include those for visible published/retracted advisories. Do not announce an
empty window. Keep the individual reporting methods available.

Use the API's existing `webui/base_url` setting with `?page=security_advisory`.
The WebUI already routes this URL to its advisory list; no WebUI change or
separate configurable URL is needed. The lead owns final user-facing wording.

Use a periodic flush independent of arrivals and API results, serialized with
poll processing. Start its schedule after silent startup initialization, with
the first deadline one full interval later. Do not send the first event
immediately, reset a deadline when events arrive, or flush early because a batch
is large. Empty boundaries send nothing; they still advance the schedule.
Pending entries can flush when due even if the latest poll has no new events.

Use elapsed monotonic time for scheduling. Delayed handling must not create
catch-up bursts or sends less than one interval apart. At the proposed site
value this permits at most one summary line per channel per hour, including
when advisories arrive gradually. Clear the pending sets after the due output
attempt, retaining the existing best-effort delivery policy. No durable queue,
severity policy or delivery guarantee is proposed.

## Checkpoints, disabled mode and compatibility

- `off` suppresses output but keeps the existing polling, advisory-store updates
  and in-memory watermark advancement. It does not accumulate a deferred digest.
  Pending summary sets must be empty in off mode; no flush is allowed. This
  treats disabling as discarding announcements during that period.
- Keep the existing silent startup bootstrap: set the watermark to startup time
  and load advisories published or updated within the preceding 30 days into
  the store without sending messages. Configuration changes use a normal service
  restart; re-enabling does not replay the disabled interval.
- Pending summary sets and the flush deadline are memory-only. Restart discards
  unsent summaries and starts a fresh full interval after initialization. It does
  not immediately flush or replay the preceding window. This loss is intentional
  within the existing best-effort policy; no new durable format is introduced.
- The YAML store retains advisory snapshots by ID; `@since` is not persisted.
  FileStorage writes asynchronously every 15 seconds. Existing behavior is best
  effort: downtime events are not replayed, muted output is discarded, and
  crashes/failures can lose or repeat announcements. The existing end-of-poll
  timestamp also does not provide an atomic API snapshot. Do not describe the
  summary as a durable notification feed or broaden this change into checkpoint
  repair.
- Preserve store path and value format, API requests and credentials model.
  There are no database migrations, client-generation changes, daemon/protocol
  changes or fleet-wide coordination requirements. No new persisted state is
  needed, and the old bot can read the retained state after rollback.
- An old bot ignores the proposed mode and keeps individual reporting. Deploy
  the site mode together with a package that supports it. A software rollback
  can therefore restore the former notification volume.

## Source evidence and API conclusion

All references below are local canonical bare-repository snapshots; no upstream
refresh or live production-state inspection was performed.

| Repository / revision | Relevant paths and findings |
| --- | --- |
| `vpsfree-irc-bot` `e9c60b0b95d3cc0dad6f012d8127c2bc078cfa7d` | `lib/vpsfree-irc-bot/security_advisories.rb`: 60-second timer (environment override for tests), 30-day bootstrap, ID store, separate advisory/update queries and multiline output. `lib/vpsfree-irc-bot.rb`: optional plugin and settings forwarding. `lib/vpsfree-irc-bot/api.rb`: unauthenticated HaveAPI setup. `lib/vpsfree-irc-bot/file_storage.rb`, `persistence.rb`, `helpers.rb`: state path, 15-second writes and mute behavior. |
| `vpsfree-cz-configuration` `91639dec2c78721b3d8765de10dc65e0c66d59db` | `cluster/cz.vpsfree/containers/int.vpsfbot/config.nix`: Libera instance sends advisories to `#vpsfree`. `modules/services/vpsfree-irc-bot.nix`: arbitrary `settings` serialized to JSON; additional private configuration is loaded afterward. `packages/vpsfree-irc-bot/default.nix`: `fetchFromGitHub` rev/hash currently selects the exact bot revision above. This package pin is not a flake input. |
| `vpsadmin` `fb2f51222503a45f2e5a42af505f719e44279ed0` | `api/lib/vpsadmin/api/resources/security_advisory.rb`: `recent_since` filters published/retracted rows by publication or update timestamp. `api/lib/vpsadmin/api/resources/security_advisory_update.rb`: `since` filters update creation time and supports the included advisory. `api/models/security_advisory.rb`: public visibility and update semantics. `webui/pages/page_security_advisory.php`, `webui/forms/security_advisory.forms.php`: existing list route. |
| `haveapi` client v0.26.5, `aa3f2afa7b26dbbaa76c5171a4f1ea8db0d5cc18` | Bot `Gemfile.lock` selects this client version. `clients/ruby/lib/haveapi/client/resource.rb` and `resource_instance_list.rb` return a single array response, without automatic pagination. |
| `haveapi` server v0.29.9, `784e113c216b16586c482e710ee4a0e0a04e6f8e` | vpsAdmin `api/Gemfile` requests `~> 0.29.9`. `servers/ruby/lib/haveapi/actions/paginable.rb` and `model_adapters/active_record.rb` impose a limit only when provided; there is no default limit. |

**The existing API is sufficient unchanged.** Both advisory list actions have
optional `limit`/`from_id` inputs without a default limit. Current bot calls omit
them and receive the complete matching result. Count the locally selected
distinct IDs, not an API total (which would include already-seen advisories or
multiple update rows). Keep the unlimited request shape for this bounded change;
adding a limit would require explicit full traversal before summarizing or
advancing the watermark. Bootstrap and CVE lookups also currently omit limits.

No actual backlog size was measured. The user reports gradual arrivals, which
requires aggregation across polls. API recovery can also place many events in
one poll; these join the current window without triggering an early summary.

## Implementation packages, if selected

| Owner | Independent file boundary | Acceptance and dependencies |
| --- | --- | --- |
| implementer0 | Bot `lib/vpsfree-irc-bot/security_advisories.rb`, focused new advisory spec, `dist/config.yml.sample`, `README.md`, and `tests/suite/vpsadmin-events.nix` if needed for the targeted integration check. Touch `lib/vpsfree-irc-bot.rb` only if required for configuration validation. | Implement mode/interval validation and defaults, periodic combined summary with memory-only sets, distinct-ID counting across polls, off-mode consumption, unchanged individual behavior and state format. Document delayed delivery and restart/off semantics. No vpsAdmin or HaveAPI edits. Depends on lead accepting this revised brief and final message wording. |
| implementer1 | Configuration `cluster/cz.vpsfree/containers/int.vpsfbot/config.nix` and `packages/vpsfree-irc-bot/default.nix`. | Set mode to `"summary"` and `summary_interval = 3600`, retain channel routing, then pin the published final bot revision and source hash. Generic Nix module needs no new option. Policy edit can proceed independently; final pin and package verification depend on implementer0's final published head. |

Lead owns worktree creation/registration, tracking, assignments, shared Git
coordination, review and authorized rollout. Implementers remain idle during
this recommendation stage.

## Verification and rollout brief

Quick checks after implementation, in the bot's documented Nix environment:
focused RSpec and RuboCop, then the repository's normal quick suite. Cover omitted
and invalid mode/interval, each mode, zero/one/many advisory batches, repeated
updates to one ID across polls, new/updated overlap across the whole window,
update-only/retraction windows, channel routing and correct base/list URL.
Use a controlled monotonic clock and a short interval in unit tests: no immediate
first message, gradual arrivals accumulate, arrivals do not move the deadline,
large batches do not flush early, an empty poll can precede a due flush, empty
windows stay silent, and delayed ticks cannot cause catch-up bursts or violate
the interval between sends. Verify off advances state without accumulating,
startup is silent, restart discards pending sets and waits a fresh interval, and
failed polling does not produce a partial successful batch. Exercise a batch
larger than a customary API page size and assert no request introduces `limit`;
do not assume client auto-paging.

After committed changes and quick checks, use mandatory independent final
review. Longer verification should target the bot's documented
`./test-runner.sh test vpsadmin-events` flow with summary behavior and retained
individual coverage. Use its existing
`VPSFREE_IRC_BOT_SECURITY_ADVISORY_CHECK_INTERVAL` timing override for short polls
and set `summary_interval` to a short positive number of seconds, spanning
multiple polls, in test settings; tests need not wait an hour. A fresh verification
watcher owns uncertain-duration checks. Configuration verification evaluates the
selected instance's mode, interval, package and generated settings, then builds
only the affected bot container via
the repository's confctl workflow. Read deployment/coordination instructions
before executing; none of these checks or operations has been run here.

Rollout affects `cz.vpsfree/containers/int.vpsfbot` and
`vpsfree-irc-bot-libera.service`. Publish/select the compatible bot, then deploy
the exact package pin, site mode and interval together through the lead's
authorized workflow. Verify the effective private config does not override them
without exposing its contents. Observe service health and subsequent natural
advisory activity, allowing a full summary interval; do not manufacture
production advisories for testing.

Recovery is either `mode = "off"` on the new package or restoring the prior
package/configuration generation. The latter restores individual output.
Retain bot state in both cases. No API rollout, schema rollback or state
conversion is required. Deployment and default-branch integration remain
separate authorizations.
