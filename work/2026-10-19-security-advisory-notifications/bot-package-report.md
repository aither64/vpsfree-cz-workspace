# Bot execution package

Implemented, independently reviewed, and locally verified at final published
head `94ac4eb5a7caf0456fff7df86a44cae198463276`. Worktree is clean. The final
isolated targeted VM run passed all eight examples, including hourly digest
behavior. Exact-head RSpec CI passed; Integration Tests CI remains queued under
the lead's watcher. Lead owns the remaining integration gate and Git coordination.
No source change, rerun, CI observation, Git or cleanup performed for this update.

## Final local acceptance evidence

- Exact source: `94ac4eb5a7caf0456fff7df86a44cae198463276`, unchanged from the
  final reviewed/narrow-fixed feature head.
- Single-execution `run-short-verification.sh` invoked
  `./test-runner.sh test --state-dir /tmp/sa-94ac4eb-r1 vpsadmin-events`.
- [short-runtime.log](short-runtime.log) records all eight examples passed and
  `vpsadmin-events` successful after **513.15 seconds**.
- The gradual-arrival summary example passed in **71.68 seconds**; existing public
  status, news, outage, individual advisory and update examples also passed.
- [short-runtime.exit](short-runtime.exit) contains `0`.
- Exact-head [RSpec 39325998769](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/39325998769)
  passed, as reported by the lead.
- Exact-head [Integration Tests 39325998761](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/39325998761)
  remains queued; the fresh watcher owns observation. No duplicate monitoring.

The short task-owned state root avoids the proven UNIX socket pathname limit.
Prior failed and contaminated runs remain preserved with their diagnoses below;
this final pass does not replace their failure evidence. The remaining report
retains implementation, review and historical verification provenance.

## Revisions and history

- Repository/worktree: `worktrees/2026-10-19-security-advisory-notifications/vpsfree-irc-bot`
- Feature: `2026-10-19-security-advisory-notifications`
- Fetched base/default: `e9c60b0b95d3cc0dad6f012d8127c2bc078cfa7d`
- Final published head: `94ac4eb5a7caf0456fff7df86a44cae198463276`
- Complete series: one commit, `security_advisories: add interval summaries and silent mode`.
- No migrations, schema changes, intermediate pins, dependency changes,
  obsolete approaches or follow-up history. No migration was merged, released,
  deployed or externally consumed. Existing advisory YAML value format unchanged.
- Origin is `git@github.com:vpsfreecz/vpsfree-irc-bot.git`; fetched default did
  not advance, so no rebase was necessary. Feature pushed with hooks under Nix.

Final diff: five files, 785 insertions and 27 deletions:

| Path | Purpose |
| --- | --- |
| `lib/vpsfree-irc-bot/security_advisories.rb` | Modes/default/validation, summary sets, monotonic deadlines, independent flush timer, serialized bootstrap/poll/flush, complete summary/off batch staging, list URL |
| `spec/vpsfree/irc/bot/security_advisories_spec.rb` | 38 focused examples, controlled clocks and API responses, concurrent poll/flush exercise |
| `tests/suite/vpsadmin-events.nix` | Verified digest bot case with 60-second summary and 2-second poll; original individual coverage retained |
| `README.md` | Supported modes, count rules, delays, restart/off/mute/failure semantics and package compatibility |
| `dist/config.yml.sample` | Summary mode and positive interval example |

## Behavior and documentation

Default remains individual, missing advisory configuration keeps plugin absent,
unknown modes/invalid intervals reject during plugin initialization. Summary uses
memory-only distinct ID sets; new wins across an entire window. Separate timer
flushes due pending data even without new API arrivals. Empty windows advance the
deadline silently, arrivals never reset it, delayed handling schedules a full
interval after completion, and no count/size threshold causes output. Poll and
flush share one mutex. Summary/off snapshot/count application follows both
successful queries and snapshot reads. Individual notices retain their original
query/report flow and update detail. Off advances snapshots/watermark silently.
All output retains configured-channel routing and existing mutable-send policy.
No durable queue/API/client/schema change or deployment coordination needed.

Main-agent writing inspection accepted README/sample, validation messages and
summary wording before commit, applying vpsfree-user-facing-writing and pinned
humanizer-en. No prose changes requested. No consequential design deviations.

## Quick verification

All commands used the documented, warm bot `nix develop` environment (Ruby 3.3):

- `nix develop -c bundle exec rspec spec/vpsfree/irc/bot/security_advisories_spec.rb`:
  first focused run 33 examples passed; final focused remediation run 38 examples passed.
- `nix develop -c bash -c 'bundle exec rspec && bundle exec rubocop && nixfmt --check tests/suite/vpsadmin-events.nix'`:
  PASS exit 0; 150 examples/0 failures, RuboCop 63 files/no offenses, Nix formatting clean.
- `nix-instantiate --parse tests/suite/vpsadmin-events.nix`: PASS in Nix shell.
- Extracted final testScript, replacing Nix constants, then `ruby -c`:
  `Syntax OK`. This verifies syntax only, not VM/runtime behavior.
- `git diff --check`: PASS.
- Commit: Overcommit RuboCop PASS; commit-msg hooks PASS, with nonblocking
  warnings for two body lines longer than 72 characters (all lines <=80).

Coverage includes defaults/validation/all modes, silent bootstrap, restart,
off watermark/store/no queue, zero/one/many events, 250 IDs with no `limit`,
repeated update IDs, cross-poll new/update overlap, retracted/update-only,
channel routing/subpath list URL, no first/early/reset/size flush, due flush
after empty/failed poll, empty boundaries, delayed/slow handling, wall-clock
jumps, failed/muted output discard, complete-batch retry and mutex serialization.

## Setup evidence

Reviewed `.overcommit.yml` (only RuboCop enabled, CapitalizedSubject disabled);
no repository AGENTS.md or custom hooks present. Lead's setup watcher ran
`nix develop -c bash -c 'bundle exec overcommit --sign && bundle exec overcommit --install'`
with exit 0; 70 gems installed. Logs: `bot-setup.log` / `bot-setup.exit`.
Then `dev-session worktree add 2026-10-19-security-advisory-notifications vpsfree-irc-bot --as-is --no-fetch`
registered the exact existing branch/worktree successfully. No gem/lock edits.
Ambient `git push` later refused an Overcommit config-signature mismatch;
`nix develop -c git push -u origin 2026-10-19-security-advisory-notifications`
succeeded without resigning or bypassing hooks. Use Nix for Git hooks too.

## Automatic CI and post-review checks

Push automatically started these exact-head workflows; no manual CI dispatch or
local long check was started. Initial observed state:

- [Integration Tests 39321329088](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/39321329088): queued.
- [RSpec 39321328974](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/39321328974): in_progress.

Both bind head `a5d1dfe565526c3532183d756c592a26e7270675`. Hand these IDs
to the lead's fresh policy watcher; no waiting performed by implementer0.

After the mandatory final-review gate, the exact targeted local command is:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-security-advisory-notifications/vpsfree-irc-bot
./test-runner.sh test vpsadmin-events
```

The wrapper runs the pinned flake test-runner. Test boots its existing vpsAdmin
services and IRC NixOS VMs; the added digest bot is started only in the final
example. Tests use the repository's existing user/socket network arrangement.
A fresh verification watcher must own execution/logs, with unexpected local
kernel build escalation from workspace policy. No extra build is assigned to
this package; affected-container build belongs to config/lead verification.
Do not infer runtime success from unit/static checks.

## Handoff

Whole-branch review of prior head `2756ee653fb844a611a9f2083ca8890a1f70f72d`
completed with one Important finding (bootstrap recovery) and one Advisory
(YAML off quoting). Both were fixed within the accepted narrow boundary and
consolidated into final head. Lead and reviewer accepted step-9 direct fix
verification without a full review rerun. Final targeted VM check now passes;
remaining exact-head Integration Tests CI is queued under the lead's watcher. Implementer0 remains available for owned review
fixes. Config owner may pin the published bot head above. Deployment, service
restarts, default-branch integration and session lifecycle actions excluded.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-security-advisory-notifications/)

## Final review remediations

See [bot-bootstrap-recovery.md](bot-bootstrap-recovery.md) for failure diagnosis
and focused/full evidence, and [bot-review-remediation.diff](bot-review-remediation.diff)
for the exact old-to-final committed patch. Bootstrap retries preserve the same
store/startup watermark, run silently on a normal poll tick, and begin a full
summary interval after complete success. No shared Api or public contract change.

The README now explains YAML `mode: 'off'`; sample quotes `mode: 'summary'`.
Selected Ruby/Psych validation confirms unquoted off parses false, quoted mode
values remain strings, and the uncommented sample parses summary/3600. Strict
validation remains unchanged. Main-agent approved exact wording before commit.

Final amended commit hooks passed; branch force-with-lease updated from the exact
old head. The superseded old-head RSpec run 39315420448 completed success. The
superseded queued old-head Integration Tests run 39315420422 was selected for
cancellation after corrected publication; final cancellation evidence follows.
No current-head run was cancelled, no manual workflow dispatched.

Cancellation confirmed by `gh run view`: old-head Integration Tests 39315420422
is completed/cancelled; cancellation request command exited 0. Current-head
RSpec 39317498639 was observed in_progress, Integration Tests 39317498503 queued.
Lead owns monitoring these exact final-head runs.

## Integration fixture correction

The initial corrected head `49a8ff8086b7b325f9f1a8f4825619f8e03245ce` passed
RSpec but failed both lead-owned local targeted integration and CI integration
39317498503 at the new fixture's NAMES wait, before bootstrap/advisory creation.
Cause: ten-character nickname `summarybot` rejected by ngIRCd's default nine.
Exact binary socket reproduction returned 432 for that name and 001 for `digbot`.
Only the integration fixture changed: shorter nickname consistently, service
readiness, bounded failure journal diagnostics. Application code unchanged.
Lead directly inspected/accepted this narrow fix. Full quick150/0, RuboCop63,
Nix format/parse and extracted Ruby syntax passed before consolidation.

[Diagnosis and failure provenance](bot-integration-diagnosis.md),
[committed fixture-only diff](bot-integration-fixture.diff),
[exact binary reproduction](nickname-reproduction.txt),
[local failure archive](bot-local-failed-49a8ff8.tar.gz).
CI artifact preserved in `ci-failed-39317498503/`. Failed completed workflow
and prior successful RSpec left intact. All old-head runs completed, so no
additional cancellation was necessary after publication. New exact-head runs:
Integration Tests39321329088 queued, RSpec39321328974 in_progress. No manual
workflow starts; local retry is assigned through lead's watcher, not started by
implementer0. Final bot SHA `a5d1dfe565526c3532183d756c592a26e7270675`.

## Final digest assertion repair

Lead's targeted retry on a5d1dfe passed registration, bootstrap, the expected
combined digest and >=60-second minimum; it then failed expected1/got5 because
the fixture counted four UrlMarker replies as summaries. No application bug was
indicated. The fixture now selects digest category lines for count/payload while
still rejecting individual advisory headings across all bot output. Explicit
RSpec assertion-error diagnostics retain recent IRC lines and service journal.
Lead directly accepted this narrow test-only repair after a real-handler short
probe reproduced old5/new1 counts. Full150 examples, RuboCop63, Nix parse/format,
Ruby syntax and mandatory amendment hooks passed; no application/prose changes.

Final head263ddbc0b541b5df2d025a73f1759d33db3f30b2 published with exact lease.
[Latest diagnosis](bot-digest-assertion-diagnosis.md),
[committed test-only diff](bot-digest-assertion.diff),
[separately preserved failed retry](bot-local-failed-a5d1dfe.tar.gz).
Latest runtime verification remains pending lead's fresh watcher.

## Existing Cluster readiness correction

The lead-owned exact263ddbc run passed all seven other examples, including the
corrected complete hourly digest scenario, then failed overall because unchanged
firstexample sent !status while independent Cluster API setup was still pending.
Its explicit not-ready response and separate OutageReports readiness prove the
fixture race; initial network exception detail is unknown. Only firstexample now
reissues normal !status after explicit not-ready, bounded120s/15s response, and
still requires original concrete nodes-online result. Silence/unmatched errors
fail; no app or generic retry change. Lead directly inspected/accepted this narrow
fixture repair. Quick150 examples, lint63, Nix parse/format/Ruby syntax and hooks
passed before final amendment/publication.

Final head94ac4eb5a7caf0456fff7df86a44cae198463276 published with exact lease.
[Cause/evidence](bot-status-readiness-diagnosis.md),
[committed first-example-only diff](bot-status-readiness.diff),
[separately preserved exact263ddbc failed run](bot-local-failed-263ddbc.tar.gz).
Final exact-head local runtime verification passed as recorded at the top;
remaining Integration Tests CI is queued under the lead's watcher.
