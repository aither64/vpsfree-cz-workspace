# Packaged creation acceptance harness

Executed against the reviewed packages; see [creation-integration-results.md](creation-integration-results.md) for results and limitations. The isolated four-thread fixture has been removed. The commands below document the harness and require fresh authorization for another live run.
The controller is [creation-acceptance.py](creation-acceptance.py); its real CLI
delay wrapper is [creation-session-gate.rb](creation-session-gate.rb). Both are
initiative artifacts, not installed project code.

The controller creates a new private `/tmp/creation-accept.*` workspace, local
Git identity, profile symlink, authority and state directories, transition lock,
dedicated tmux socket, and HTTPS certificate. A loopback HTTPS proxy forwards to
the actual packaged portal's Unix socket, including its event streams. A
transparent fixture-local Unix relay reaches the supplied authenticated Codex
socket; this keeps the client's adjacent submission ledger under the fixture
directory. It forwards bytes without logging protocol payloads. The
wrapper delays only `start` and `fork` for the four fixture slugs, then executes
the package's real raw CLI with fixed runtime provenance and inherited lock fd.
It does not create or alter manifests, journals, receipts, or completion evidence.

Supply the final package and the authenticated socket selected by the initiative
manifest. `ACCEPT_CODEX_VERSION` makes a mismatch with that socket's recorded
client version fail before any fixture thread is created. No credential is read,
copied, or printed by the harness. It does not register a workspace, switch an
installed profile, or send requests to any existing registered conversation.

```bash
export ACCEPT_PACKAGE=/nix/store/REVIEWED-DEV-WORKSPACE-PACKAGE
export ACCEPT_PREVIOUS=/nix/store/aamx7bqmg406w3zrfnvpd60knhrgps4s-dev-workspace-0.2.0
export ACCEPT_CODEX="$ACCEPT_PACKAGE/libexec/codex/bin/codex"
export ACCEPT_CODEX_SOCKET=/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock
export ACCEPT_CODEX_VERSION=0.154.0

# Reuse the root's Nix browser environment. Required: Python with selenium,
# Firefox, GeckoDriver, Ruby, tmux, Git, OpenSSL, and coreutils timeout.
# ACCEPT_FIREFOX / ACCEPT_GECKODRIVER / ACCEPT_RUBY / ACCEPT_TMUX /
# ACCEPT_OPENSSL can name exact executables if they are not on PATH.
timeout --signal=TERM --kill-after=30s 900s \
  python3 work/2026-09-12-portal-review-experience/creation-acceptance.py --run
```

For an environment prepared directly from the initiative's Nix inputs, run from
its dev-workspace worktree after setting the variables above:

```bash
nix shell --impure --expr '
  let
    flake = builtins.getFlake (toString ./.);
    pkgs = import flake.inputs.nixpkgs { system = builtins.currentSystem; };
  in pkgs.buildEnv {
    name = "creation-acceptance-tools";
    paths = with pkgs; [
      (python3.withPackages (p: [ p.selenium ]))
      firefox geckodriver ruby tmux git openssl coreutils
    ];
  }' \
  -c timeout --signal=TERM --kill-after=30s 900s \
  python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-09-12-portal-review-experience/creation-acceptance.py --run
```

The `withPackages` environment supplies Selenium to that exact Python binary.
No build or live command is required merely to inspect the harness. Syntax-only
checks are:

```bash
python3 -c 'import ast, pathlib; ast.parse(pathlib.Path("work/2026-09-12-portal-review-experience/creation-acceptance.py").read_text())'
ruby -c work/2026-09-12-portal-review-experience/creation-session-gate.rb
```

The run checks these behaviors:

- Real new-session form returns 303; fork and plan dialogs receive 202 and
  navigate to the destination before the held CLI initializes it. Acceptance
  and shell GET each must take less than 750 ms; browser navigation has a
  separate two-second bound. The new shell is captured at 1440×1000 and 390×600,
  with an advancing elapsed counter and roughly one status poll per second.
- Matching submissions reuse the same receipt/attempt and one helper invocation.
  Different requests cannot reuse a reserved name; the pending destination
  rejects message and fork mutations. New starts submit one exact initial
  request, and forks inherit history without submitting another initial turn.
- The source produces a real completed Plan-mode plan. After its exact snapshot
  is accepted, it produces a different plan. A graceful fixture portal restart
  leaves the destination paused; browser retry preserves the earlier plan,
  turn ID, digest, model and effort. Wrong receipt and stale attempt retries
  fail. The failed/paused source link covers an uppercase/underscore source slug.
- After the plan destination finishes, the source receives one fixed request to
  call `request_user_input` with one blocking two-choice question. The browser
  stays on the destination while `/pending` confirms the interactive request and
  two source activity snapshots, three seconds apart, show increasing waiting
  time with paused work. The browser then opens the source, selects an option,
  and submits through the real question UI. The request must disappear, the same
  turn must finish, and the elapsed wait must remain in closed waiting time.
  The final idle state may already have a new open trailing wait.
- The fourth head request stops before CLI binding. The previous package reads
  all three canonical sessions, validates their manifests, and replays the first
  session's unchanged strict creation journal without another user turn. Its
  actual CLI independently creates the fourth slug with a different request.
  After rollforward, the old receipt becomes `conflict`, the canonical page and
  composer remain visible, and retry cannot claim or replace that thread.
  Existing manifest/receipt digests and conversation IDs are checked across
  rollback. No receipt or journal fixture is fabricated for this sequence.

Allow up to 15 minutes on an otherwise responsive host. Most elapsed time is
model initialization and two small Plan-mode responses, each capped at three
minutes. The blocking question, browser answer, and final model response share
one additional three-minute deadline. The pre-CLI gate has a four-minute watchdog
so a slow newer plan can complete before the deliberate restart. Creation completion has a 150-second
cap. A model that declines to return a completed plan causes a clear failure;
the harness does not create replacement threads or retry with broader prompts.
The question check also fails if the selected model does not produce the
specified blocking request; it does not install or enable additional tools.
There are exactly four intended fixture threads and no protocol probe in this
controller. Root's selected-Codex probe may use the separately budgeted fifth
transient thread.

The controller prints check names and its private results path. `results.json`
contains package paths, status transitions, timings, receipt/thread IDs and
digests; `http-metadata.json` contains method/path/status/timing only. Screenshots,
receipts, plans, helper configuration, process logs and TLS material remain in
the private fixture directory. Promote only the concise results needed for
review into `creation-integration-results.md` after inspecting them.

The browser, fixture portal, HTTPS proxy and local Codex relay stop on completion
or failure.
The dedicated fixture tmux socket and recorded fixture threads remain for root
cleanup. Do not run `dev-session delete`, stop the shared App Server, or remove
registered session state as harness cleanup. The post-binding/pre-journal
rollback variation and journal-crash recovery are covered by the focused Go/Ruby
regressions; this live run stays within the four-thread budget.

## Completed checkpoint verification

The same fixture resumed on the reviewed package
`/nix/store/prpvck3v35xbvyz60gfwprz9p3lsagal-dev-workspace-0.2.0`.
`--resume-plan` proved that the repaired package reconciled the exact deployed
receipt without changing its frozen goal, plan snapshot, CLI binding, completion
proof, attempt, thread or invocation count. Completed allocation phases were
not repeated.

The source used one authorized question retry after ordinary default-to-plan
settings restored live mode. Its passive timing assertions passed. A Selenium
stale-form exception occurred after selecting an option, before submission;
closing the fixture connection lost that interactive request delivery. The real
answer and closed-wait checks remain unverified. The exact stranded question was
interrupted through the normal portal API, then `--resume-rollback` completed the
fourth-thread old/new checks. No third question was sent.

The checkpoint options remain as diagnostic artifacts. Their old private root,
App Server, tmux sessions and metadata have been removed; none can be resumed.
The controller propagates `DEV_WORKSPACES_STATE` and the private `CODEX_HOME` to
CLI and tmux children. Any future run needs its own approved fixture and must
preserve exact receipt/thread identities across a failure before retrying.
