# Integration fixture diagnosis and repair

Failed revision: `49a8ff8086b7b325f9f1a8f4825619f8e03245ce`.
Local targeted run failed exit 1 after 749 seconds; automatic Integration Tests
39317498503 failed the same eighth example, while examples 1–7 passed in both
runs. RSpec 39317498639 succeeded. No rerun was launched by implementer0.

## Evidence and cause

Both eighth examples fail after about 30 seconds, at
`client.wait_for_names_include('summarybot')`. Local `irc-shell.log` shows
`systemctl start vpsfree-irc-bot-summary` exit 0, then shutdown after the timeout.
There is no bootstrap-file wait or new advisory creation command. Last IRC NAMES
contains only `vpsfbot observer`; no summary nickname joined. The test never
reaches advisory/digest behavior, so the failure does not demonstrate an
application summary defect.

The built fixture config selects nickname `summarybot` (ten characters).
Its exact built ngIRCd 27 config does not set MaxNickLength; its matching manpage
states a default of nine. A bounded direct socket reproduction using the exact
built server binary independently proves:

```text
432 * summarybot :Nickname too long, max. 9 characters
001 digbot :Welcome to the Internet Relay Network ...
005 digbot ... NICKLEN=9 ...
```

Full response: [nickname-reproduction.txt](nickname-reproduction.txt).
The owned reproduction server exited cleanly; no service or production action.
Its temporary config/log were under `/tmp/security-advisory-nick-repro`.
Existing failed VM evidence has no summary service journal, which is why the
fixture now captures that journal on failure rather than widening timeouts.

## Narrow change and verification

Only `tests/suite/vpsadmin-events.nix` changes from the failed head:
consistent nickname `digbot` in config, NAMES wait, sender and final-output regex;
explicit service readiness after start; last 120 summary-service journal lines
on StandardError, preserving the original error. OsVm::Machine#succeeds forwards
the pinned shell return `[status, output]`, so `_, output` is the actual output
shape. No fallback abstraction, application/server-limit/timing/public change.

Lead accepted the exact reproduction and directly inspected/accepted this
fixture-only boundary under the narrow-fix workflow, releasing amendment and
publication. Corrected exact-head VM/CI verification remains pending lead launch.

Quick batch exit 0 in bot's warm documented Nix environment:

```sh
nix develop -c bash -c 'nixfmt --check tests/suite/vpsadmin-events.nix && nix-instantiate --parse tests/suite/vpsadmin-events.nix >/dev/null && bundle exec rspec && bundle exec rubocop'
```

150 examples/0 failures; RuboCop 63 files/no offenses; Nix format/parse PASS.
Extracted Ruby testScript `ruby -c`: Syntax OK. `git diff --check`: PASS.

## Preserved failures

- [Local failed run archive](bot-local-failed-49a8ff8.tar.gz): entire
  `/tmp/os-test-runner/os-test-vpsadmin-events-8aba1688`, including dereferenced
  immutable config, all VM/test logs and result. Original directory retained.
- `ci-failed-39317498503/`: full downloaded GitHub log artifact
  `vpsfree-irc-bot-test-logs-39317498503`, artifact ID 12219184110, including
  failed vpsadmin-events and successful basic/webhook test evidence.
- Existing session `final-bot-integration.log/.exit`,
  `final-ci-integration.failed.log/.status` retained unchanged.
- [Committed old-to-new fixture diff](bot-integration-fixture.diff).

The completed failed workflows stay intact. Only superseded queued/running runs
for this exact branch may be cancelled after corrected publication.


## Corrected publication

Consolidated into original sole feature commit
`a5d1dfe565526c3532183d756c592a26e7270675` and SSH-published with an exact
force-with-lease protecting failed old head49a8ff8. Mandatory hooks passed.
Final worktree clean, default basee9c60b0 unchanged. No migrations/dependency
streams. All old-head workflows were completed, so none needed cancelling.
New automatic exact-head Integration Tests39321329088 queued and
RSpec39321328974 in_progress; handed to lead, no manual dispatch or local retry.
