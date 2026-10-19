# GitHub notifications: accepted implementation design

Updated 2026-10-02 before application edits. The user has authorized
implementation of this contract. It supersedes the earlier sender-only
`ignored_senders` proposal: implement `ignored_users` with commit-author
filtering for nonempty pushes. Default-branch integration and production
deployment are not authorized. Architect owns this design; implementer owns
application edits; lead owns worktrees, tracking, review and coordination.
The bounded archive reliability amendment below was authorized during VM
verification and must precede its source fix. Notification policy and routes
remain unchanged.

## Scope and source evidence

Add exactly these six repository full names to the existing `#vpsadminos` list:

- `vpsfreecz/vpsadmin-webui`
- `vpsfreecz/vpsfree-kb-contracts`
- `vpsfreecz/ruby-lxc`
- `vpsfreecz/vpsf-status`
- `vpsfreecz/ssh-exporter`
- `vpsfreecz/syslog-exporter`

Keep existing entries and event coverage. Add no other repositories. The
captures project is now `vpsfree-kb-contracts`; the notification template route
already uses `vpsfree-notification-templates`. See the lead's
[repository inventory](repository-inventory.md) for the completed investigation.

Configure `ignored_users = [ "github-actions[bot]" ];` only on `#vpsfree`.
Retain its five repositories, allowed `push`/`issues`/`pull_request` types, and
`default_branch_only = true`. Leave `#vpsadminos` in the legacy array form.

Inspected source baselines:

| Component | Revision and relevant paths |
| --- | --- |
| Bot origin/master | `88906fd54b0fc8cf613fc2cec2fb930d8196d05a`; `lib/vpsfree-irc-bot/github_webhook/{event,announcer,server}.rb` |
| Configuration origin/master | `028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d`; `cluster/cz.vpsfree/containers/int.vpsfbot/config.nix` |
| Configured bot source pin | `565c4b4e99c7b6b6daf8b0a9768b9b3796611247`; `packages/vpsfree-irc-bot/default.nix` |
| Template route rename | `b928eea5f927c765e8c793fe232355638c5086b7`, 2026-09-01 |

Pinned and current bot GitHub source/specs are identical. Bot master has no
tracked `AGENTS.md`; its documentation starts at `README.md`,
`dist/config.yml.sample` and `tests/README.md`. Configuration has its own
`AGENTS.md` and `README.md`. Existing rules were read before selecting checks.

There is one configured IRC instance, Libera. Matterbridge relays both target
channels to Matrix. The change belongs in the Libera instance and preserves
those bridges. Configuration's daily-update workflow uses the bot's plain
noreply email; both plain and numeric-prefixed forms must be supported.
Actual webhook delivery bodies, hook subscriptions and private runtime overrides
remain unverified; the lead's hook metadata requests returned 403. Source
routing fixes do not establish successful production delivery.

## Configuration and identity contract

`ignored_users` is optional in each object-form channel configuration, defaults
to an empty list, and accepts string/symbol configuration keys through existing
normalization. Normalize list elements to strings consistently with existing
options. Legacy arrays mean no ignored users. No global ignored list or
compatibility alias for the unimplemented `ignored_senders` proposal is needed.

For every commit in a nonempty push, resolve the original author's account:

1. A present, nonempty string `author.username` is authoritative. Compare it
   exactly against `ignored_users`; do not override it using email.
2. When username is missing, null or empty, derive a username only from an
   entire author email of the form `LOGIN@users.noreply.github.com` or
   `DIGITS+LOGIN@users.noreply.github.com`. Strip only the numeric prefix and
   domain. Require a nonempty LOGIN, no additional `+`, whitespace or `@`, and
   the literal domain. Both forms support `github-actions[bot]`.
3. An unrecognized email or malformed username yields unknown identity and
   keeps the commit. Do not infer identity from display names. Do not consult
   committer, pusher, sender, issue/PR creator, commit message, path, or
   `head_commit` as a substitute for the individual original author.

Matching is exact and case-sensitive. Do not add substring/regex matching of
configured users, trimming, email alias normalization, or network lookups.
A malformed non-string username is unknown rather than an invitation to use
another identity field. Existing author name/email parsing remains usable for
rendering; add username/account resolution without changing displayed authors.

Webhook `sender.login` is the identity only for supported non-push events and
originally empty eligible pushes. It identifies the action sender, which can
differ from the issue/PR creator, pusher or commit author. A missing login does
not match an ignored user. Broader repair of malformed webhook payloads is out
of scope; the existing parser still expects the standard sender/author objects.

## Per-channel decision and rendering

Keep signature verification, parsing and `Event#announce?` in the server as they
are. Preserve channel repository/type/default-branch gates. Only after those
gates pass, compute a channel-specific announcement, returning either text or
no announcement. The result must be determined once per channel before sending
or logging. Do not mutate the queued Event, its commits, or nested author data.

| Channel policy / event | Result after existing gates pass |
| --- | --- |
| Absent or empty ignored list | Exact existing `event.to_s` behavior |
| Active list; originally nonempty push | Select commits whose resolved original author is not ignored |
| Active list; all original commits removed | No channel send or channel log |
| Active list; at least one commit retained | Render the retained commits, regardless of sender |
| Active list; originally empty eligible push | Filter sender; if retained use existing ref-update rendering |
| Active list; supported non-push event | Filter sender; if retained use existing event rendering |

A bot sender cannot hide a human or unknown-author commit. A human sender
cannot rescue a bot-authored commit. Preserve retained order. Determine the
push's force/fast-forward classification using original event facts, before
selection; filtering must not turn an ordinary push into a fast-forward.

For an active list and an originally nonempty push:

- Show at most ten retained commit lines, even when eleven remain. Filtering
  happens before truncation, so human commits after ten bot commits can appear.
- Use retained count N for summaries and overflow; ignored count M is original
  length minus N. When M is positive, an ordinary heading is
  `[repo] sender pushed 1 announced commit (4 ignored) to branch`, with normal
  singular/plural handling. When M is zero, retain ordinary `pushed N commits`
  wording (singular for one), while still applying the ten-line limit.
- Force-push and fast-forward events retain their existing update heading,
  including original branch and SHA range. Follow it with a count line,
  e.g. `[repo] 1 announced commit (4 ignored)`, then retained commit lines.
  With no exclusions, use `[repo] N commits` on that count line. This applies
  even when the active filter excludes nothing.
- Each retained commit line keeps the existing repository/branch, short SHA,
  original author display name and first subject line format. Do not relabel
  authors as the event sender or substitute the resolved account for the name.
- If N exceeds ten, use the existing `...and K more commits` style with
  K = N - 10. Ignored commits never contribute to K.
- Keep the original full comparison URL after the details; it still includes
  all changes, including ignored commits. Do not manufacture a filtered URL.
  Preserve existing ref-update URL fallbacks when a force/fast-forward payload
  lacks a usable comparison URL. Include that URL once.

The existing unfiltered formatter sometimes displays eleven commits and omits
commit details for force/fast-forward events. Preserve those exact legacy
behaviors whenever the ignored list is absent/empty. Use the new rendering
path only when the list is active and the original push has commits. Do not
reuse an emptied projection as an originally empty push: that would announce
an all-ignored push as a ref update.

## Interfaces, files and boundaries

Use a small pure rendering interface: existing channel predicates decide
routing, then a channel-aware announcement method produces text or nil. Its
push path selects a fresh array and passes retained commits and ignored count
to a renderer. Existing `to_s` remains the unfiltered interface. Exact helper
names may follow repository style; the observable contract above is fixed.

Application files:

- `lib/vpsfree-irc-bot/github_webhook/event.rb`: retain author username,
  implement account resolution and filtered push rendering. Derive metadata
  from the original event and avoid persistent mutation/caching by channel.
- `lib/vpsfree-irc-bot/github_webhook/announcer.rb`: normalize `ignored_users`,
  apply channel policy, and pass only the resulting text to
  `MultiLine`/`log_mutable_send`. A nil result skips both sending and logging.
- `spec/vpsfree/irc/bot/github_webhook/{event,announcer}_spec.rb`: verify identity,
  selection, formatting, routing, no-send/no-log and isolation invariants.
- `dist/config.yml.sample` and a concise README section/pointer: document this
  optional interface, original-author versus sender rules, retained counts and
  the full comparison URL. No deprecated sender-only example should remain.
- `tests/suite/irc-github-webhook.nix`, `tests/all-tests.nix`,
  `tests/README.md`: add/register/document the focused integration fixture below.
  The implementer owns these edits; the lead owns final public-prose polish
  before commit under the user-facing writing procedure.
- Configuration `cluster/cz.vpsfree/containers/int.vpsfbot/config.nix`: the six
  route additions and the `#vpsfree` ignored list only.
- Configuration `packages/vpsfree-irc-bot/default.nix`: exact tested bot source
  revision/hash, separate from functional configuration changes.

No change is required to `server.rb`, signatures, shared event eligibility,
IRC helpers, Matrix bridge, Nix service module, flake inputs/lock, dependencies,
workflows, database or migrations. The service module already accepts arbitrary
settings and serializes JSON. This bot source is a fixed fetchFromGitHub pin,
not a channel-owned flake input.

Rendering interaction: `Announcer` wraps the final text in `MultiLine`, so line
numbers must reflect retained output. `Helpers#log_send` sends ordinary IRC
PRIVMSG even when called with log type `:notice`, explicitly to support
Matterbridge. Preserve that behavior. HTML/YAML channel logs must contain the
same filtered text as IRC, not a second call to the original `event.to_s`.
Do not change log schema. No requirement to rewrite old logs or debug output.

## Event gates and invariants

The supported handlers remain `push`, `create`, `delete`, `fork`, `issues` and
`pull_request`. Existing event gates skip deleted pushes and empty creation
pushes; issues/PRs retain their existing opened/deleted/closed/reopened action
list. Unsupported event types remain unsupported. `#vpsfree` still excludes
create/delete/fork and non-default pushes. Where another channel enables these
non-push handlers with an ignored list, they use sender filtering.

Required invariants:

- Filtering one channel never changes another channel's output, even when
  channel order is reversed or the same Event is rendered repeatedly.
- Unknown original authors survive. Explicit username takes precedence over
  contradictory noreply email. Display names and committers have no authority.
- No send/log for an all-ignored originally nonempty push, for any sender,
  force flag or distinctness combination.
- Original branch, before/after SHA, comparison URL and event classification
  remain tied to the actual push. Only displayed commit selection/counts change.
- Legacy arrays and absent/empty lists preserve exact current output and gates.

## Compatibility, rollout and recovery

New bot with old configuration is behaviorally compatible. Old bot ignores the
unknown `ignored_users` field, so it runs but does not filter. Deploy the new
source pin and policy together when deployment is separately authorized.
Adding routes alone works with the old bot. No persisted-state/schema, API,
CLI, generated-client, Terraform or inter-service protocol change is involved.
Rollback can read the same bot state/logs. No fleet-wide node update is needed.

Target for later deployment: `cz.vpsfree/containers/int.vpsfbot`, service
`vpsfree-irc-bot-libera.service`. Review the entire pinned-to-selected bot
change because advancing from the old pin may include unrelated changes.
After reviewed verification, prepare the exact package/configuration together;
production activation and default-branch integration require later direction.
Do not run dry activation against production under the current authorization.

A later operator should check non-secret effective routes because
`/private/vpsfbot/libera.yml` is loaded after generated configuration and can
override settings. Verify actual hook subscriptions/deliveries, service health,
IRC joins and Matrix relay before declaring coverage restored. Do not print
private configuration or replay real events into public channels during tests.

Recovery: restore the previous package/configuration generation together, or
clear `ignored_users` to restore previous message volume with the new bot.
Keep state/log directories. The event queue is in-memory, so a restart can lose
queued events; this change adds no durable replay. No migration rollback or
data repair is required.

## Verification and acceptance

This revision records a verification plan; the architect has not run tests or
edited application files. Implementation checks use repository Nix environments
and hooks. Lead runs mandatory independent review after commits and quick
checks, before longer integration tests. Review must include complete branch
history, final diff, pin-to-target changes and an explicit no-migrations result.

Quick checks:

1. Author identity table: explicit ignored/human username; conflicting email;
   missing/null/empty username with both noreply forms; unknown address; forged
   display name; malformed prefix/domain/extra plus; committer/pusher/sender
   disagreements. Assert unknowns are kept and username takes precedence.
2. Mixed/all-human/all-ignored pushes with human and bot senders. Cover order,
   N/M counts, N = 1/10/11/12, filtered bot prefixes, and remaining overflow.
   Check full URL and original display attribution. Run exact legacy output
   regression cases with no option and with an empty list, including N = 11.
3. Force/fast-forward cases with all retained, mixed and all ignored commits;
   ordinary push whose only distinct commit is removed; originally empty
   eligible pushes with human/bot senders; deleted and empty-creation gates.
4. All five non-push types with ignored/human senders, including human action on
   a bot-created issue/PR. Preserve branch/event/repository gates and legacy
   arrays; verify object keys as strings/symbols and normalized configs.
5. One shared event sent through two channel policies in both orders; verify
   unchanged original data and unfiltered message. At the announcer boundary,
   assert no `log_mutable_send` for suppression and only filtered text for a
   mixed push, including correct MultiLine numbering.
6. In the bot shell, run focused specs then `bundle exec rspec` and
   `bundle exec rubocop`. Run configured Nix formatting checks. Inspect the
   instance diff/generated non-secret JSON: exactly six route additions,
   unchanged existing routes, ignored list only on `#vpsfree`, correct pin/hash,
   and no unrelated module/flake changes.

Minimal meaningful integration fixture (after review):

- Add `irc-github-webhook` using existing `tests/suite/common.nix`, one NixOS VM
  with ngIRCd and the bot, following the RSpec-style `irc-basic` setup. Keep
  vpsAdmin/API disabled. Existing test networking can be reused; no separate
  development cluster or network redesign is needed. A standalone fixture
  isolates the two-channel webhook configuration and contract from unrelated
  command tests, without changing shared helpers or adding another service VM.
- Configure both channels with one fabricated shared repository, filtering only
  `#vpsfree`; keep `#vpsadminos` unrestricted. Listen for webhook POSTs on VM
  loopback with a test-only secret. POST via the guest's curl; no webhook
  firewall opening or new host-forwarded port is needed.
- Generate JSON fixtures and matching existing SHA1 HMAC signature headers.
  Observe wire PRIVMSG using the existing `IrcBotClient` helpers. Check normal
  HTTP success, filtered/unfiltered channel output and channel HTML/YAML logs.
- Minimum scenarios: bot-sender mixed-author push (human survives); human-sender
  all-ignored push (filtered channel silent); human-sender force-push with
  mixed authors (heading and retained details); ignored issue event (filtered
  channel silent); invalid signature (neither channel receives output).
- Use unique markers. For negative assertions, post a later valid human event
  to both channels and wait for its final line, establishing that preceding
  queued events were processed before checking absence and logs. Inspect each
  channel's accumulated lines/log files after that barrier; do not rely only
  on a fixed sleep. Bound waits and report recent IRC lines/service logs on
  failure. Keep all messages and credentials inside the disposable test.

Run `./test-runner.sh test irc-github-webhook`; the existing vpsAdmin-events
suite adds no relevant coverage here. The fixture reuses startup/connectivity
checks, so a second irc-basic run is optional unless shared fixture code changes.
Build `confctl build cz.vpsfree/containers/int.vpsfbot` from the configuration
worktree. Long/uncertain tests and builds must use the mandatory Luna/low
watcher; stop unexpected local kernel builds under workspace policy. A scoped
build establishes package/configuration validity, not production delivery.

Read-only production delivery/bridge inspection may follow when access exists.
Actual deployment, dry activation, webhook changes and public message replay
remain outside current implementation authorization.

## Reliability amendment: concurrent HTML asset installation

Authorized by the lead on 2026-10-02 after the signed-webhook VM exposed a
second-channel archive failure. This amendment adds only shared asset-copy
synchronization and its regression/diagnostics. It does not revise authorship,
filtering, formatting or repository routing.

### Evidence and cause

At bot `cf21b243d1e207f5aeca0077112d8467af851b7f`, the VM passed wire
assertions but timed out waiting for the `#vpsadminos` archive barrier.
[Verification](verification.md) and [guest commands/logs](irc-shell.log) record
`ChannelLog#log` failing because `@loggers[channel]` is nil. The original JOIN
exception is outside the last-80-lines journal capture; the connection between
this VM failure and the following reproduced race remains an inference.

The implementer's pinned Ruby 3.3.10 reproduction loaded the actual failed VM
source at `/nix/store/18445p3snacwn7jpxz0d9hp1204ij09i-source`. Ten fresh
destinations, each with two concurrent channel constructors released by a Queue
barrier, produced nine `#vpsadminos` constructor failures: `Errno::EACCES` in
`FileUtils.cp_r` opening shared `assets/style.css`. Serial constructors passed.
The architect read `/tmp/vpsfbot-2026-10-02-logger-race-repro.rb`, inspected its
output tree and confirmed source CSS mode 0444; the stochastic test was not
rerun. Logger source is unchanged between base `88906fd...` and `cf21b243...`.

`HtmlLogger#copy_assets` creates shared `@dst/assets`, copies the read-only
source tree, then chmods copied assets to 0644. Another constructor can copy
over the temporary read-only destination before chmod completes. Both loggers
have the same HTML root but distinct channel log paths. `TemplateLogger`
already creates the channel HTML header before asset copying; `ChannelLog`
publishes its logger pair only after constructors return. This explains how a
directory/header can exist while its logger entry remains absent.

### Chosen change and boundaries

Add one eagerly initialized, process-wide mutex owned by `HtmlLogger` (a class
constant is sufficient). Inside `copy_assets`, hold it across destination
directory creation, the complete `FileUtils.cp_r`, and the complete existing
chmod loop. The source-directory existence check can stay outside. Preserve
operation order and current copy/update/permission semantics: run installation
on each construction, copy current source content, and finish with existing
destination asset mode 0644. Never modify the read-only source.

Use `Mutex#synchronize` so exceptions release the lock and propagate normally.
The existing per-instance log mutex cannot protect a directory shared between
logger instances. Keep rendering, log writes and all other constructor work
outside this new critical section. Add a short code comment explaining the
read-only copy-to-chmod interval; this is the durable rationale.

Implementer-owned files are exactly:

- `lib/vpsfree-irc-bot/html_logger.rb`: shared mutex and bounded critical section.
- `spec/vpsfree/irc/bot/html_logger_spec.rb`: focused constructor/asset regression.
- `tests/suite/irc-github-webhook.nix`: failure diagnostics may capture the full
  service journal from this disposable VM's boot, rather than only its tail.
  Preserve all current wire and both-channel HTML/YAML archive assertions.
- Configuration `packages/vpsfree-irc-bot/default.nix`: refresh tested source
  revision/hash after the bot correction, through normal lead coordination.

No `ChannelLog` nil guards, swallowed copy errors, formatter changes, schema,
dependency, module, input-lock, or general logging-concurrency redesign. If the
VM still fails after the reproducible race is fixed, preserve the diagnostics
and return the new evidence to the lead instead of relaxing the archive gate.

### Alternatives and residual assumption

A process-wide mutex also serializes installations into different roots, but
the small startup asset copy does not justify a per-path lock registry and its
path-identity/lifetime handling. Copy-once caching would prevent current assets
from refreshing during later logger construction. Locking only `cp_r` leaves
the chmod gap. A filesystem lock or staged atomic replacement would add a
cross-process/reader contract beyond this demonstrated in-process race.

The supported operational assumption remains one writing bot process per
archive root. This mutex does not coordinate independent processes or provide
atomic visibility to web readers; successful asset content/permissions and log
schema remain unchanged. A crash mid-copy can still leave a partial install,
as before. Do not claim new crash-recovery or cross-process guarantees.

### Deterministic regression and verification

Use real HtmlLogger construction for two different channel paths sharing one
fresh destination, with a temporary template tree whose asset files are 0444.
Keep template reads, file copying and chmod real. Test-only wrappers and Queue
barriers should pause the first installer after copying and before chmod, then
start the second at its asset-install entry. Record operation entry/completion:
the second copy must not enter until the first chmod phase finishes. Bound all
waits, propagate worker exceptions, and release barriers/join threads/close
handles in ensure cleanup. Do not use repeated lucky runs or fixed sleeps as
the regression oracle. Assert serialization directly as well as actual output
so privileged test execution cannot hide the bug by bypassing file permissions.

Both constructors must complete, both channel logs must accept a marker, and
shared asset bytes must match the source with destination mode 0644 while
source files stay 0444. Also verify that a subsequent constructor updates an
existing asset from changed source content, that missing source assets retain
the existing no-op behavior, and that an injected pre-write copy exception
propagates without preventing a later installer from acquiring the lock. The
controlled overlap case must fail against the pre-fix implementation; the
test should verify filesystem behavior rather than merely assert a mutex exists.

Run this focused spec, full bot RSpec and RuboCop in the pinned environment;
run fixture syntax/Nix formatting checks if diagnostics change. Lead arranges
the required review of the added application fix before another long run.
Then the Luna watcher reruns the existing isolated signed-webhook VM, requiring
both-channel HTML/YAML markers and unchanged filtering/wire assertions, and
the scoped configuration build for the refreshed pin/hash. Capture full
`journalctl -b -u vpsfree-irc-bot --no-pager` on VM failure to include the first
JOIN/constructor exception. No production replay, deployment or merge is added.

Compatibility and rollback: there are no format, persistent-state or interface
changes. Old/new software can read the same archive. Package/config rollback
needs no data conversion, but restoring the old bot restores the startup race.
Keep normal state/log directories and existing paired package/config rollback
procedures. No new runtime option or operator migration is required.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-vpsfbot-github-notifications/).
