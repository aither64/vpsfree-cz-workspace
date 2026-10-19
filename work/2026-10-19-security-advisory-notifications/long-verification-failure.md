# Final verification failures

Exact bot head 49a8ff8086b7b325f9f1a8f4825619f8e03245ce and configuration
e30cd3399c5f57fd792afa4147d293307227d9b4. Reviewed fixes and quick checks pass;
long verification has not passed, so neither conditional merge is executed.

- Final scoped configuration evaluation passed. Parsed settings/source identity
  retained in final-config-eval-result.json.
- Local ./test-runner.sh test vpsadmin-events exit1, elapsed749.18s. Examples1-7
  pass, new digest example8 times out waiting for IRC line nil. Full batch log
  final-bot-integration.log; exact status final-bot-integration.exit. Test runner
  log/artifacts: /tmp/os-test-runner/os-test-vpsadmin-events-8aba1688/.
- Exact-head GitHub RSpec39317498639 success; Integration39317498503 failure,
  same example8. final-ci-integration.failed.log and status files retained.
  CI runner path recorded in failure logs. No manual dispatch or retry.
- Watcher incorrectly continued to the container-build step despite stop-on-first
  failure instructions. It exited1 at confctl Continue?[y/N] EOF before do_build;
  only settings/machine-list metadata ran. Evidence final-config-build.log/exit
  and configuration .confctl/logs/2026-10-19--22-35-02-confctl-build.log.
  implementer1 inspected complete logs and pinned docs/source: command-local
  --yes is documented. Correct future command:
  nix develop -c confctl build --yes 'cz.vpsfree/containers/int.vpsfbot'
  Singleton selector confirmed; no deployment/activation involved.

No verification process remains. implementer0 owns diagnosis/source/test correction
before retry; implementer1 owns dependent pin and build-command correction. Any
new behavior beyond narrow review boundary receives affected-lane independent
review. Fresh watchers for later long checks, explicitly gated by parent.

## Confirmed root cause and bounded correction

Owner inspected local VM shell logs and CI failure artifact. Both fail in the
NAMES join wait before bootstrap-file check or any new advisory creation. Test
nick summarybot has ten characters; exact built ngIRCd27 default limit is nine.
Exact-binary local socket reproduction (0.05s) returns numeric432 “Nickname too
long, max. 9 characters” for summarybot; digbot receives001 welcome and005
NICKLEN=9. Evidence nickname-reproduction.txt. Owned short reproduction server
stopped. Local failed test tree retained in bot-local-failed-49a8ff8.tar.gz,
CI artifacts in ci-failed-39317498503/.

Lead directly inspected bot-integration-fixture.diff: tests/suite/vpsadmin-events.nix
only, consistent shorter nick, service readiness wait and bounded service journal
diagnostics on exception. No server limit, timing, app behavior, API or public
contract change. Full150/0 specs, RuboCop63 clean, Nix parse/format, extracted
Ruby syntax and whitespace pass. Direct narrow acceptance within already-reviewed
fixture behavior; consolidate into feature commit, repin single package stream,
then fresh watcher runtime retry at corrected exact revisions. No blind rerun.

## Second targeted runtime attempt

Exact bot a5d1dfe local retry failed exit1 after566.22s. Examples1-7 pass;
new digest example8 fails after70.86s. New fixture gets past original short-nick
registration issue; actual current assertion/journal evidence delegated to bot
owner for diagnosis before retry. Raw bot-runtime-retry.log/exit and standalone
runtime-watcher-report.md retained. No CI wait/build or merge performed by retry
utility, no owned runner left. App code unchanged in this retry. Separate
supported coordinator hook dependency setup utility may run while owner diagnoses;
no source/lock edits or queue bypass permitted.

## Second failure diagnosis

Owner read the actual assertion: expected one message, received five. The exact
combined digest wait and elapsed>=60-second checks had already passed; this is
not a digest timeout. UrlMarker is always enabled and responds to standalone
advisory/update links emitted by the original individual bot. Those four replies
plus the actual digest were all counted by the fixture's broad digbot PRIVMSG
filter. Correct owned assertion scope is digest category only, while separately
rejecting individual advisory headings across all digbot output. No product
change or disabling unrelated plugin. Explicit RSpec expectation failures need
bounded diagnostics because they do not inherit StandardError. Owner preparing
minimal fixture correction/static checks; lead direct inspection before publication.
Local failure tree retained as bot-local-failed-a5d1dfe.tar.gz. RSpec39321328974
success; same-head Integration39321329088 was still queued at owner observation.

## Latest runtime: feature passes, unchanged first example times out

Exact263ddbc local run exits1 after622.04s. Unchanged first public-node-status
example times out30.02s; all other seven examples succeed, including final
hourly digest scenario (its payload/delay/count and individual-output checks).
Owner assigned bounded diagnosis/readiness evidence and supported per-example
rerun discovery before any edits/retry. Preserve this distinct failure tree.
No runtime process remains; no CI monitoring by the utility after failure.
The seven exact-head successes and produced test derivation/input identities
can support focused verification reuse once firstexample cause is established;
this is not a full-green or integration acceptance claim. Container build already
passed exact config9c8e7351; both coordinator snapshots prepared, no merge jobs.

## Latest first-example diagnosis and correction boundary

Owner inspected IRC response: !status returned “Status unknown, unable to reach
vpsAdmin API”; Cluster#cmd_status emits it when its own api_setup? is false.
Existing fixture waits only OutageReports ready, but each Api consumer owns its
own setup/retry connection. Fixed4s sleep cannot establish Cluster readiness.
Original network exception not retained for this unchanged example, so no
precise network failure claim. Latest seven other examples all passed at exact
263ddbc; no evidence of product regression. No supported per-example runner
selector (--filter selects testScript metadata only).

Lead chose minimal fixture readiness correction rather than blind stochastic
retry: explicitly establish Cluster readiness using existing IRC mechanisms,
leave application/API behavior and all success assertions intact. Exact proposed
diff/quick evidence required before publication. Original failure retained as
bot-local-failed-263ddbc.tar.gz. Current CI RSpec39323728164 success, Integration
39323728183 queued. No merges or retry yet.
