# Creation acceptance after mandatory review

Prepared on 2026-09-12 and subsequently executed after mandatory review.
Results and limitations are recorded in [creation-integration-results.md](creation-integration-results.md).
The private fixture has been removed. The commands below describe the planned
acceptance; another live run needs fresh authorization. Budget: one package build, up to 15 minutes
for acceptance, at most four new portal fixture conversations plus the transient
protocol probe, no destructive lifecycle actions against registered workspaces.
Keep the initiative open.

The executable controller and current command line are now saved in
[creation-acceptance-run.md](creation-acceptance-run.md), with
[creation-acceptance.py](creation-acceptance.py) and the real-CLI
[delay wrapper](creation-session-gate.rb). They passed syntax checks and ran against the selected real App Server. The fourth fixture now covers the
reviewed mixed-generation conflict path described below.

## Reuse and limits

- `dev-workspace/portal/internal/web/creation_test.go`: deterministic acceptance
  latency, message-lock serialization, duplicate requests, restart/retry guards,
  source replacement, package-generation changes, exact plan replay, failed final
  persistence, and completion proof before fork-journal removal. These use fake
  Codex/CLI boundaries; they do not establish packaged-runtime compatibility.
- `dev-workspace/test/dev_session_test.rb`: real Ruby initializer logic with
  controlled tmux/App Server doubles. Reuse the `portal_(fork|creation|start)` and
  `exclusive_browser_start` cases for proof-write failure and journal crash points.
- `codex-web/codex/client_test.go:TestConfiguredCodexFreshThreadContract`: starts
  the specified real Codex binary in an isolated home; no existing conversation
  is needed. It submits one fixed initial request and verifies materialization
  and replay; it does not require a successful model answer. Enable with
  `CODEX_WEB_TEST_BINARY` and cap at two minutes.
- Packaged `workspace-host check-codex --codex PATH`: generates schemas from that
  binary, checks the client contract, starts a short App Server probe, and checks
  the model catalog. It does not send a user turn.
- `portal/internal/web/browser_contract_test.cjs` and `TestShippedBrowserClientMatchesSessionAPI`
  exercise transport/browser helpers, not real browser navigation. The earlier
  `work/2026-09-11-portal-trusted-host/browser-check.py` demonstrates the installed
  Firefox/Selenium setup; copy its setup pattern, not its old fixture URL or fake
  Codex server. Use BiDi `set_viewport`, and assert actual `innerWidth`.

## Package and selected Codex

Run from the dev-workspace initiative worktree in its Nix environment. Root owns
building/pinning the final package; reuse that output rather than rebuilding it
for every check. Set these variables to the reviewed output and retained prior
output, then retain their resolved store paths with the results:

```bash
export ACCEPT_PACKAGE=/nix/store/REVIEWED-DEV-WORKSPACE-PACKAGE
export ACCEPT_PREVIOUS=/nix/store/RETAINED-PREVIOUS-DEV-WORKSPACE-PACKAGE
export ACCEPT_CODEX="$ACCEPT_PACKAGE/libexec/codex/bin/codex"
"$ACCEPT_CODEX" --version
"$ACCEPT_PACKAGE/bin/workspace-portal" thread defaults
timeout 60 "$ACCEPT_PACKAGE/bin/workspace-host" check-codex --codex "$ACCEPT_CODEX"
```

`ACCEPT_PACKAGE` must include this initiative's committed codex-web module and
CLI changes. The currently recorded selected Codex is 0.154.0; verify the built
output still selects that version rather than trusting the recorded number.
Do not replace global `HOME`, `CODEX_HOME`, or the installed workspace profile.

For the direct real-binary contract, from the codex-web worktree:

```bash
CODEX_WEB_TEST_BINARY="$ACCEPT_CODEX" \
  go test ./codex -run '^TestConfiguredCodexFreshThreadContract$' -count=1 -timeout=2m
```

## Isolated packaged portal

Create a short private directory such as `/tmp/creation-accept.XXXXXX` using
`mktemp -d`; use a task variable `ACCEPT_ROOT`. Its workspace must be a new git
repository on `master`, with `work/`, `worktrees/`, and `repos/`. Configure git
identity locally for the fixture. All fixture tracking, authority, locks, helper
arguments, logs, TLS files, and portal private state stay there with private
permissions. Record the directory in the results; it is not an initiative or a
registered workspace. Do not point this fixture at the shared coordination tree.

The currently recorded authenticated App Server socket is
`/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock`. Re-read the current initiative manifest before using it. It can be reused with
this separate workspace and the unchanged selected Codex binary: only create
fixture threads rooted below `$ACCEPT_ROOT/workspace/work/`. Do not restart that
shared App Server, change its credentials, or address another thread. Alternatively,
root may supply an already authenticated isolated App Server using the same
selected binary. Do not copy credentials into the fixture or evidence.
Use a transparent fixture-local Unix relay to that authenticated socket, and pass
the relay socket to the portal and CLI. The client's adjacent submission ledger
then stays private too. The relay must not record or alter protocol payloads.

Launch the actual `$ACCEPT_PACKAGE/bin/workspace-portal serve` with these flags:

```text
--workspace             $ACCEPT_ROOT/workspace
--base-url              https://127.0.0.1:<private-test-port>
--unix-socket           $ACCEPT_ROOT/portal.sock
--dev-session           $ACCEPT_ROOT/session-gate
--authority-dir         $ACCEPT_ROOT/authority
--user-state-root       $ACCEPT_ROOT/state
--host-profile          $ACCEPT_ROOT/profile
--transition-lock       $ACCEPT_ROOT/transition.lock
--codex-socket          <selected authenticated socket>
--codex-version         <exact selected binary version>
--tmux                  <Nix tmux executable>
```

Create `profile` as a symlink to `ACCEPT_PACKAGE`, a private empty transition lock,
and private authority/state/gates directories before launch. The `session-gate`
fixture is a small wrapper with this exact behavior:

1. Accept only the portal's `start` or `fork` command; obtain the destination from
   argument 2 for start or argument 3 for fork (one-based including the command).
2. Increment a private invocation counter for that destination and create an
   `entered` marker. While `gates/<destination>.hold` exists, wait in 100 ms steps,
   failing after four minutes. This accommodates the newer-plan response before
   the deliberate restart. An optional `<destination>.fail-once` file is consumed
   and returns exit 1 before invoking the CLI, for the explicit retry scenario.
3. Execute `$ACCEPT_PACKAGE/libexec/workspace-portal/dev-session`, preserving the
   incoming arguments and inherited `DEV_WORKSPACE_TRANSITION_LOCK_FD` descriptor.
   Prefix the raw CLI arguments with the fixture's `--workspace`, `--tmux-socket`,
   `--authority-dir`, `--codex-socket`, `--codex-version`, `--codex-command`,
   `--portal-command`, `--portal-base-url`, `--transition-lock`, and
   `--require-runtime`. The portal command is the packaged workspace-portal;
   Codex is `ACCEPT_CODEX`. Pass no altered model, effort, source, receipt, or goal.
4. Include `--host-profile`, `--expected-host-generation`, and
   `--expected-host-profile-token`. Compute the token with the packaged
   `libexec/workspace-profile-identity.rb` (`DevWorkspaceProfileIdentity.token`),
   using the fixture profile. Keep the expected generation/token fixed for that
   wrapper launch. Ruby `exec(..., close_others: false)` preserves inherited fd 3.

This wrapper only delays initialization; it must not fake manifests, authorities,
Codex replies, CLI results, receipt files, or completion evidence. Preserve the
wrapper with the test results so its exact boundary is reviewable.

For HTTP assertions, `curl --unix-socket "$ACCEPT_ROOT/portal.sock"` reaches the
packaged handler directly. For real-browser assertions, put a loopback-only HTTPS
proxy in front of that socket with a fixture-local certificate, and use the exact
same base URL. Enable `acceptInsecureCerts` only in this fixture browser profile.
Use the existing browser tools at
`/nix/store/aklba75zn5fpld8y81ifqxx7j8vmj376-portal-browser-tools/bin` if still present;
otherwise reuse the root's newly built Firefox/GeckoDriver/Selenium environment.

Define a direct HTTP helper after setting `ACCEPT_BASE` to that HTTPS base URL:

```bash
accept_http() {
  curl --silent --show-error --max-time 5 \
    --unix-socket "$ACCEPT_ROOT/portal.sock" \
    -H "Origin: $ACCEPT_BASE" "$@"
}
```

## Acceptance sequence

Use an ISO date and unique names under 48 characters, for example `Accept_New`,
`accept-fork`, `accept-plan`, and `accept-interrupted`, with an optional short run
suffix. Keep fixture messages harmless and specific: “Reply exactly READY. Do not
use tools or change files. Keep this session open.” Default model/effort come
from the selected package's `thread defaults` output.

### New session: final URL before initialization

Place the destination's hold file, then submit the normal new-session form in
Firefox. Capture navigation timestamps and a screenshot after navigation. The
same request can be inspected directly without following its redirect:

```bash
accept_http --dump-header "$ACCEPT_ROOT/new.headers" \
  --output "$ACCEPT_ROOT/new.body" --write-out '%{http_code} %{time_total}\n' \
  --data-urlencode "creation_date=$ACCEPT_DATE" \
  --data-urlencode 'name=Accept_New' \
  --data-urlencode 'goal=Reply exactly READY. Do not use tools or change files. Keep this session open.' \
  http://localhost/sessions
```

Require 303 to `/<date>-Accept_New/`, and response plus creation-shell GET each
under 750 ms while the real helper remains held for at least five seconds.
The shell must show an advancing elapsed counter, no composer controls, and
roughly one creation-status request per second. Check 1440×1000 and 390×600.
Direct mutations against the initializing destination must be rejected: the
conversation handler masks its resolver refusal as 404, and the fork endpoint
returns 409. This includes the interval where a ready manifest exists before the
portal receipt has been saved. Save errors/status, not submitted goal text in HTTP logs.

Repeat the identical form while held: same final URL, receipt ID and attempt,
one worker/helper invocation. Change only the goal with the same name: 409.
Remove the hold file, then poll the creation endpoint with a one-second interval,
maximum 120 seconds. Require `ready`, normal session navigation, one materialized
thread, and one initial user message. Compare the ready manifest's goal digest
with the exact fixture message. Record elapsed time separately from initial turn
completion; runtime readiness does not mean the model finished replying.

### Fork: 202 before live source verification/CLI completion

Wait for the new source to become idle. Hold `<date>-accept-fork`, then use the
actual Fork dialog. Require immediate navigation and a 202 JSON response with
`slug`, `url`, `receiptId`, `attempt`, and `state`; it must arrive before the gate
opens. The HTTP equivalent is:

```bash
accept_http --dump-header "$ACCEPT_ROOT/fork.headers" \
  --output "$ACCEPT_ROOT/fork.json" -H 'Content-Type: application/json' \
  --data-binary "{\"name\":\"accept-fork\",\"creationDate\":\"$ACCEPT_DATE\"}" \
  "http://localhost/api/sessions/$ACCEPT_SOURCE/fork"
```

Repeat it while held: same receipt and attempt, one worker. Release the gate and
require the new thread ID differs from the source, `forked_from` matches the
source slug, repositories/artifacts are empty, and completion evidence names
that exact source thread. The `.fork.json` journal must be gone before `ready`.
The destination may display inherited history, but must not send a new initial
user message merely because it was forked.

### Plan-new: exact accepted snapshot survives a newer plan and retry

Use the new source's UI to enter Plan mode and request a tiny two-step proposed
plan with no tools or file edits. Wait for a completed plan and the plan action
panel. Open “New session…” and capture the displayed plan text, turn ID, SHA-256,
model and effort. Hold `<date>-accept-plan`, then submit the dialog. Require 202
and the destination progress shell before the helper gate opens.

When the receipt reports validation complete and the gate's `entered` marker is
present, request a different plan in the source conversation. Stop only the
fixture portal process gracefully while its worker is held, wait for its child
wrapper to exit, then restart the same packaged portal with the same private
state. Require `paused` and an explicit retry action; no invocation may start
merely from loading the page or polling it. A retry with a wrong receipt ID or
old attempt returns 409. Retry the exact receipt/attempt using:

```bash
accept_http -H 'Content-Type: application/json' \
  --data-binary "{\"receiptId\":\"$ACCEPT_RECEIPT\",\"attempt\":$ACCEPT_ATTEMPT}" \
  "http://localhost/api/sessions/$ACCEPT_DESTINATION/creation/retry"
```

After releasing the hold, require exactly this destination's first user message:
`Implement the following approved plan from session <source>.\n\n<captured plan>`.
Compare bytes/digest, turn ID and captured settings against the first snapshot,
not the newer source transcript. A failed creation from a valid uppercase or
underscore source slug must provide a working “Return to the source session”
link. Keep actual request bodies and receipts private; retain digest assertions
and thread/receipt IDs in the concise results.

The before-snapshot stale-plan/source-replacement cases remain deterministic
focused tests. Re-run those once against the final source; do not introduce
nondeterministic SIGSTOP races inside the real CLI to recreate covered crash
points.

## Additive-state rollback and upgrade

Use only the isolated fixture. Complete the new/fork/plan cases, then hold the
fourth request before its CLI starts and stop the fixture portal gracefully.
Record receipt IDs, attempts, thread IDs, the ready creation-journal key set, and
SHA-256 of each ready manifest and private receipt. Keep the real Codex process
and fixture tmux sessions unchanged during this check.

1. Point only the fixture profile at `ACCEPT_PREVIOUS`, update the fixture wrapper's
   expected generation/token, and launch the prior packaged portal with the same
   workspace/private state and selected Codex. Require startup, index reads and
   existing conversation reads to work. The prior portal may return 404 for the
   new creation-status endpoint and the uninitialized slug; it must not start an
   operation or rewrite/discard new receipt files.
2. Run `"$ACCEPT_PREVIOUS/bin/workspace-portal" validate --workspace
   "$ACCEPT_ROOT/workspace"`. Replay the ready new session once through the prior
   raw `dev-session start <slug> --as-is --exclusive --no-attach --goal-file <the
   original fixture goal> --json --model <captured> --effort <captured>`, with the
   same raw runtime/generation flags described above and **without** new receipt
   flags. Require the same thread ID and no additional initial user message.
   This exercises the unchanged strict creation journal, not only manifest parsing.
   Then use the previous package's raw CLI to create the held fourth slug with a
   different initial request, without the head receipt flags or delay wrapper.
   Require the earlier receipt files to remain unchanged and no binding or
   completion evidence to appear for that head request.
3. Stop the prior fixture portal, restore the reviewed package/profile/wrapper,
   and restart. Require ready receipts retain their IDs and heads; the held
   receipt becomes `conflict`, exposing the independently created canonical
   session and its normal controls while refusing retry. It must retain its
   original request identity without claiming receipt completion. Recheck
   manifest validation and status. Do not mutate or rewrite receipt schemas to
   make rollback pass. Post-binding/pre-journal conflicts remain focused
   regressions so this packaged sequence stays within four fixture threads.

This establishes additive state compatibility for the old/new packages and the
unchanged Codex binary. Host-wide `workspace-host switch`/`rollback`, systemd
reconciliation and package generation activation remain root's separate delivery
checks; do not switch the shared host profile from this fixture.

## Evidence and cleanup boundary

Write `creation-integration-results.md` with exact package/Codex revisions,
command exit codes, POST/GET timings, status/attempt transitions, helper invocation
counts, thread IDs, digest comparisons, browser screenshots and rollback outcomes.
Keep raw receipts, goal/plan payloads, helper logs and TLS materials private in the
fixture directory; promote only useful redacted assertions into initiative tracking.

Stop the fixture HTTP proxy/portal processes when their checks finish. Record the
remaining fixture directory, dedicated tmux socket and four test thread IDs for
root-owned cleanup. Do not stop/delete/archive any registered development session,
do not use the shared tmux socket, and do not remove the initiative worktrees.
