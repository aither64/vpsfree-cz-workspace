# Security advisory notifications — accepted implementation brief

Accepted implementation brief, reconciled by architect0 on 2026-10-19 with
the user's finalized plan and “Implement the plan.” authorization. Scope includes
the bot changes and its package/settings update in `vpsfree-cz-configuration`.
Deployment and service restart are excluded. The user subsequently authorized
both master integrations after passing review and verification; see state.md.
The hourly design supersedes the initial per-poll proposal because gradually
added advisories would still produce spam. Current execution status and evidence
belong in [state.md](state.md); this reconciliation changes only this record.

## Accepted behavior

Add `security_advisories.mode` with `individual`, `summary` and `off`. Keep
`individual` as the default when omitted; select `summary` in the site's bot
configuration. Reject an unknown mode during configuration instead of silently
falling back. Preserve the existing behavior when the entire advisory
configuration is absent: the plugin is not loaded.

Add `security_advisories.summary_interval`, a positive integer number of seconds,
defaulting to `3600`. Reject a supplied zero, negative or non-integer value during
configuration. Only summary mode uses the interval; individual mode retains its
existing reporting behavior. The accepted site settings are:

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
unseen advisory whose current state is `published`, matching the existing
notification condition; updates
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

Use a fixed interval schedule based on monotonic time. When processing a due
tick, schedule the next deadline a full interval after that processing time,
including when the tick was delayed. Do not catch up to missed deadlines or
send less than one interval apart. At the accepted site value this permits at
most one summary line per channel per hour, including
when advisories arrive gradually. Clear the pending sets after the due output
attempt, retaining the existing best-effort delivery policy. No durable queue,
severity policy or delivery guarantee is included.

## Checkpoints, disabled mode and compatibility

- `off` suppresses output but keeps the existing polling, advisory-store updates
  and in-memory watermark advancement. It does not accumulate a deferred digest.
  Pending summary sets must be empty in off mode; no flush is allowed. This
  treats disabling as discarding announcements during that period.
- Keep the existing silent startup bootstrap: set the watermark to startup time
  and load advisories published or updated within the preceding 30 days into
  the store without sending messages. Configuration takes effect on a subsequent
  service restart, which is excluded from this task; re-enabling does not replay
  the disabled interval.
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
- An old bot ignores the new mode and keeps individual reporting. The site
  settings and updated package pin must select compatible versions together.
  A software rollback can therefore restore the former notification volume.

## Source evidence and API conclusion

These references record the original investigation's local canonical
bare-repository snapshots. That investigation did not refresh upstream or
inspect live production state; implementation revisions belong in session state.

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

## Assigned implementation packages

| Owner | Independent file boundary | Acceptance and dependencies |
| --- | --- | --- |
| implementer0 | Bot `lib/vpsfree-irc-bot/security_advisories.rb`, focused new advisory spec, `dist/config.yml.sample`, `README.md`, and `tests/suite/vpsadmin-events.nix` if needed for the targeted integration check. Touch `lib/vpsfree-irc-bot.rb` only if required for configuration validation. | Implement mode/interval validation and defaults, periodic combined summary with memory-only sets, distinct-ID counting across polls, off-mode consumption, unchanged individual behavior and state format. Document delayed delivery and restart/off semantics. No vpsAdmin or HaveAPI edits. Lead owns final message wording. |
| implementer1 | Configuration `cluster/cz.vpsfree/containers/int.vpsfbot/config.nix` and `packages/vpsfree-irc-bot/default.nix`. | Set mode to `"summary"` and `summary_interval = 3600`, retain channel routing, then pin the published final bot revision and source hash. Generic Nix module needs no new option. Policy edit can proceed independently; final pin and package verification depend on implementer0's final published head. |

Lead owns worktree creation/registration, tracking, assignments, shared Git
coordination, review and acceptance. Both implementers are assigned. Their
packages include quick checks, commits, feature-branch publication and review
fixes. No deployment or service restart is assigned. The lead coordinates the
subsequently authorized master integrations after passing verification.

## Verification brief

Quick checks after implementation, in the bot's documented Nix environment:
focused RSpec and RuboCop, then the repository's normal quick suite. Cover omitted
and invalid mode/interval, each mode, zero/one/many advisory batches, repeated
updates to one ID across polls, new/updated overlap across the whole window,
update-only/retraction windows, channel routing and correct base/list URL.
Use a controlled monotonic clock and a short interval in unit tests: no immediate
first message, gradual arrivals accumulate, arrivals do not move the deadline,
large batches do not flush early, an empty poll can precede a due flush, empty
windows stay silent, and a delayed tick sets its next deadline a full interval
later without catch-up bursts or shortening the interval between sends.
Verify off advances state without accumulating,
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
only the affected bot container via the repository's confctl workflow without
activation. Follow applicable verification/coordination guidance; current check
results belong in session state.

## Operational compatibility and recovery — reference only

Deployment and service restart are excluded from this task. The following describes compatibility and recovery implications;
it is not an execution plan or authorization.

The affected deployment would be `cz.vpsfree/containers/int.vpsfbot` and
`vpsfree-irc-bot-libera.service`. The updated package and summary/3600 settings
must take effect together. Additional private configuration is loaded afterward
and can override site settings. A newly started bot waits a full interval before
any summary, discarding pending in-memory counts from the previous process.

If separately authorized later, recovery options are `mode = "off"` with the
new package or restoration of the prior package/configuration generation. The
latter restores individual output. Both retain the existing bot state format;
neither requires an API rollout, schema rollback or state conversion.
