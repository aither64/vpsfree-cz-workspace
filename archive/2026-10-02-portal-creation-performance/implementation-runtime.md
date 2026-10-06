# Runtime implementation result

Completed the two authorized focused local commits after the parent's corrected
checks and main-context writing pass. Runtime worktree is clean; no push occurred. Session identity was verified with
`dev-session current`: `2026-10-02-portal-creation-performance`; both identity
environment variables were absent and the trusted thread binding matched.
The complete accepted `design.md`, routed workspace procedures, runtime
instructions, README and documentation skill were read before application edits.

Runtime worktree: `worktrees/2026-10-02-portal-creation-performance/dev-workspace`.
The implementation is based on the parent's unchanged dependency commit
`dfda7b8fc501c4a6f761f6d5bc8451da3cc853b8`. The SDK result is in
[implementation-sdk.md](implementation-sdk.md); the parent published reviewed
SDK head `4c170393a96ed0a6ac2e43488d073f6fcab36132` and selected module
`v0.0.0-20261002145902-4c170393a96e`.

## Behavior and boundaries

- Start/approved-plan/fork freshness is local to the invocation and established
  under the existing creation and slug locks before create-only journal
  publication. Existing journals, tracking/worktrees, tmux, configured runtime
  authority and retained rosters prevent the fast path. An unconfigured optional
  authority follows the existing legacy Runner contract. Every retry loses the
  local proof and selects conservative recovery, including interruption before
  the first RPC. Source-turn checks remain mandatory for fresh forks.
- Recovery collects loaded metadata, tries a bounded DB-only index, and requires
  complete filesystem discovery before adoption or replacement. It validates
  identities, preserves vanished-loaded rechecks, handles stale/failed/empty
  index results, detects ambiguity and bounds pagination to 64 pages/4096 rows.
  Exact validated roster member IDs alone are excluded, with cwd/project checks.
  CLI discovery holds the roster operation lock and releases it before any new
  root. A retained roster forbids adopting a different root as well as starting
  a replacement. An undiscovered recorded ID requires an exact not-found read;
  wrong identity, contradictory existence or unknown read outcomes refuse.
- Root publication, sequential member initialization and durable initial-goal
  attempt ordering remain intact. Existing roots retain captured settings;
  replacement settings resolve only when a new root must be submitted.
- Opt-in framed stderr passes through concurrent Ruby nested capture and the
  creation-specific Go runner. The flag is consumed before runtime environment
  inheritance and explicitly supplied only to relevant thread/team children.
  Parsers bound candidate frames/rejected diagnostics, validate the private
  protocol, continue draining malformed output, preserve stdout/status and
  retain ordinary diagnostics. Member stages surround existing sequential loops.
- Progress callbacks merge only phase/update time under `operationMu`, checking
  workspace, slug, receipt ID, attempt and running state. Duplicate phases are
  coalesced and writes are capped at 256 per attempt. Final stdout/proof/upload
  checks still own readiness. No frame carries ready authority.

No persisted schema/migration, Codex version, root project, member concurrency,
archive/delete/revive algorithm or generic runtime contract source changed.
No parent-owned pin files were edited. Only the two explicitly authorized implementation commits were created.
No push, deployment, long check, benchmark execution or session lifecycle action
was performed by this member.

## Complete application snapshot

Paths are relative to the runtime worktree. `new` identifies files absent from
the dependency baseline. All 21 paths belong to this implementation. The
pre-commit snapshot had two intent-to-add progress files and four untracked test
files; both commits include the complete owned source. There are no remaining
untracked files or worktree changes.

| Path | Ownership in this diff |
| --- | --- |
| `libexec/dev-session` | Locked freshness, nested capture, flag consumption and Ruby stages |
| `portal/internal/workspacecodex/client.go` | Conservative recovery and nullable observer/options |
| `portal/internal/workspacecodex/client_test.go` | Existing ownership/history fixtures adapted to indexed discovery |
| `portal/internal/workspacecodex/recovery_candidates_test.go` (new) | Loaded/index/full coverage, exclusions, retained-root and recorded-ID refusals |
| `portal/cmd/workspace-portal/main.go` | Direct fork routing, validated locked roster snapshot, helper emitters |
| `portal/cmd/workspace-portal/main_creation_test.go` (new) | Fresh destination bypass and roster trust/lock boundaries |
| `portal/internal/creationprogress/progress.go` (new) | Shared ephemeral event, emitter and bounded decoder |
| `portal/internal/creationprogress/progress_test.go` (new) | Framing, malformed/bounded input and success-only durations |
| `portal/internal/teamruntime/runtime.go` | Sequential member stage callbacks |
| `portal/internal/teamruntime/runtime_test.go` | Failure/retry and member stage order |
| `portal/internal/web/server.go` | Creation-specific process runner |
| `portal/internal/web/creation.go` | Fixed phase labels and guarded phase persistence |
| `portal/internal/web/creation_progress_test.go` (new) | Live HTTP phase before child exit, stale/terminal guards, diagnostics/cancellation |
| `test/dev_session/session_initialization_test.rb` | Fresh start/approved-plan routing |
| `test/dev_session/session_recovery_test.rb` | First invocation versus retry with retained goal-attempt checks |
| `test/dev_session/fork_recovery_test.rb` | Fresh flag and interruption-before-RPC retry assertion |
| `test/dev_session/creation_progress_test.rb` (new) | Real Ruby nested capture, input/FD/status and bounded decoder |
| `test/dev_session_test.rb` | Includes the new progress file in Nix/CI's owning suite |
| `test/creation_browser.cjs` | Live member/completion phase and total elapsed polling assertion |
| `docs/dev-sessions.md` | Freshness, conservative recovery and exact exclusions |
| `docs/workspace-portal.md` | Private progress protocol, compatibility and readiness authority |

Parent applied `vpsfree-user-facing-writing` directly to the runtime draft.
Its exact final labels (`Checking open conversations`, `Checking saved
conversations`) and the requested creation-journal sentence were mechanically
applied with stage identifiers and facts preserved. Exact recorded-ID refusal
messages were added during final correctness inspection. The parent subsequently
approved the complete wording and source snapshot. No wholesale rewrite was made.

## Focused checks executed

All commands below ran from the runtime worktree unless `portal/` is specified.
Pinned Go/gofmt were supplied by the parent from the SDK Nix environment:

```sh
PCP_GO=/nix/store/hfb2fkwkkr6jdcg2ggibvf1zablw7i57-go-1.26.7/bin/go
PCP_GOFMT=/nix/store/hfb2fkwkkr6jdcg2ggibvf1zablw7i57-go-1.26.7/bin/gofmt
export GOWORK=off
export GOCACHE=/tmp/portal-runtime-quick.X3QtTR/cache
export GOFLAGS=-mod=readonly
export CGO_ENABLED=0
```

The initial unpublished-SDK checks used a private `/tmp` Go workspace; after
publication, the commands above use the normal module cache with no replacement.
CGO is disabled here because this member shell lacks a C compiler.

```sh
$PCP_GOFMT -w portal/internal/creationprogress/*.go \
  portal/internal/workspacecodex/client.go \
  portal/internal/workspacecodex/client_test.go \
  portal/internal/workspacecodex/recovery_candidates_test.go \
  portal/cmd/workspace-portal/main.go \
  portal/cmd/workspace-portal/main_creation_test.go \
  portal/internal/teamruntime/runtime.go \
  portal/internal/teamruntime/runtime_test.go \
  portal/internal/web/server.go portal/internal/web/creation.go \
  portal/internal/web/creation_progress_test.go
git diff --check
```

Formatting was applied as the files changed; final diff check passed. From
`portal/`, the combined final non-socket selection was:

```sh
$PCP_GO test ./internal/creationprogress ./internal/workspacecodex \
  ./internal/web ./internal/teamruntime ./cmd/workspace-portal \
  -run '^(TestDecoder|TestBegin|TestCreationProgress|TestCreationCommand|TestCreationRoster|TestCatalogPresetRetryReusesPersistedThreadAndDoesNotAppend|TestForkUsesDestinationMemberAddressInEachThreadEnvironment)' \
  -count=1 -timeout=45s
```

Passed: creationprogress 0.062s; web 0.206s; teamruntime 0.198s; CLI 0.053s.
workspacecodex compiled with no selected tests. After the recorded-root and
fork-fixture corrections, this command compiled both updated packages and
passed the CLI roster test (latest 0.051s):

```sh
$PCP_GO test ./internal/workspacecodex ./cmd/workspace-portal \
  -run '^TestCreationRoster' -count=1 -timeout=30s
```

The attempted member socket selection
`go test ./internal/workspacecodex -run '^TestRecover(Creating|Fork)' -count=1 -timeout=45s`
stopped at fixture socket setup (`setsockopt: operation not permitted`), so it
is compilation evidence only, not protocol assertion evidence.

Pinned Ruby/Node paths were verified from the exact runtime Nix env derivation
named in the parent's focused log:

```sh
PCP_RUBY=/nix/store/nin40kn7prvsn7pmbl7k576hhwcpp9x1-ruby-3.4.9/bin/ruby
PCP_NODE=/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node
$PCP_RUBY -c libexec/dev-session
$PCP_RUBY -c test/dev_session/creation_progress_test.rb
$PCP_NODE --check test/creation_browser.cjs
```

Passed. Direct owning-file execution initially exposed the existing shared
fixture dependency (`NullTmux`/`ManagedTmux` live in lifecycle_commands_test.rb).
Corrected focused execution loads the normal full entry point but runs only
the exact methods defined in each owning file. This exact command was executed
separately for each of `creation_progress`, `session_initialization`,
`session_recovery`, and `fork_recovery`:

```sh
PCP_FILE=test/dev_session/session_recovery_test.rb # select each owning file
timeout 45s "$PCP_RUBY" - "$PCP_FILE" <<'RUBY'
names = File.read(ARGV.shift).scan(/^\s*def (test_\w+)/).flatten
ARGV.replace(['--name', '/^(' + names.join('|') + ')$/'])
load './test/dev_session_test.rb'
RUBY
```

Final results: progress 4 runs/26 assertions (0.409s); initialization 12/217
(3.454s); recovery 10/148 (5.013s); fork recovery 17/113 (2.106s). All passed
with zero failures, errors or skips. Initial failures found and fixed the
optional-authority nil check and old first-invocation discovery expectations.

Parent's earlier focused log was inspected directly at the private verification
directory's `runtime-focused.log`. creationprogress, workspacecodex, web and
teamruntime passed, but the new fresh-fork fixture timed out at 120s. The
fixture had rejected the SDK's mandatory source `thread/turns/list` and kept
its connection open. It now answers the exact source request
(`limit:1`, `sortDirection:desc`, `itemsView:notLoaded`), then requires
`thread/fork`, returns the exact `forkedFromId`, and closes on every exit so a
mismatch fails promptly. No source validation was bypassed. The parent's corrected operation then passed exit 0 in 51s: all five selected Go
packages, 60 Ruby tests/624 assertions, syntax and diff checks. Its formatting
check returned no paths. Evidence is the private
`runtime-focused-corrected.log` and matching `.status`; this resolves the socket
verification gap above for the final approved source.

## Completed two-commit split

Keep the parent's completed dependency commit separate. Per the parent and
review lane, the implementation is split into exactly two commits:

- Routing/recovery: `bd18b321117ec144d66a06c5662a64004e413ae1`.
- Progress and final feature head: `7e4e62b9f7c785e9fc36b8fd3c75c0f864140c75`.

1. `sessions: bypass discovery only for locked fresh creation` — Ruby freshness,
   private fork flag and selected state-root argument; conservative recovery and
   validated locked roster composition; routing/recovery/roster tests; session
   guide. This commit has no progress dependency, observer or emission. It owns
   the ten routing paths: session guide, Ruby helper, CLI plus new creation test,
   workspacecodex client plus both recovery test files, and the three changed
   Ruby initialization/recovery/fork files.
2. `portal: stream initialization stages into creation receipts` — shared Go
   primitive and tests; optional recovery observer/stages; Ruby parser,
   concurrent capture/flag consumption/stage emitters; CLI observer wiring;
   sequential team stages; Go runner/receipt guard; progress/team/browser tests,
   owning Ruby suite include, and portal guide.

Mixed Ruby/CLI/recovery files are split through owned index blobs, with the
approved working-tree bytes preserved. Exported staged trees provide separate
compile checks without changing the worktree or pins. Progress can be reverted
independently: the first commit owns all routing/recovery behavior and needs no
progress package. No new functional edit was introduced to obtain the split.
Temporary message files were used with `git commit -F`; no hook framework is
declared in this runtime, and no hooks are bypassed.

## Staged-snapshot checks and source preservation

The approved final bytes of all 21 owned paths were saved and hashed privately.
Only owned index entries were updated to separate mixed files. The routing tree
was `abf848f3cd0c56ceee660ea1e394c3fbf57108cb`; the final progress tree is
`f45af09676204349c58efef6980dff50236f4daa`. Both were exported to private
`/tmp/portal-runtime-split-0w7f71kv/{routing,progress}` directories for checks.
Working-tree source was never rewritten to perform the split. Final committed
and working bytes match every approved hash; parent pin paths have an empty
`dfda7b8..HEAD` diff. Worktree and index are clean.

Using the pinned tool/cache environment above, from `routing/portal`:

```sh
$PCP_GO test ./internal/workspacecodex ./cmd/workspace-portal \
  ./internal/teamruntime ./internal/web -run '^TestCreationRoster' \
  -count=1 -timeout=30s
```

All four packages compiled without any progress dependency; CLI roster passed
0.051s (the other packages had no selected tests). From `routing/`, the exact
owning Ruby filter below passed 39 tests/478 assertions in 10.249s:

```sh
timeout 45s "$PCP_RUBY" - \
  test/dev_session/session_initialization_test.rb \
  test/dev_session/session_recovery_test.rb \
  test/dev_session/fork_recovery_test.rb <<'RUBY'
names = ARGV.flat_map { |file| File.read(file).scan(/^\s*def (test_\w+)/).flatten }
ARGV.replace(['--name', '/^(' + names.join('|') + ')$/'])
load './test/dev_session_test.rb'
RUBY
```

From `progress/portal`, the combined non-socket Go selection printed above
passed creationprogress 0.062s, web 0.193s, teamruntime 0.199s and CLI 0.060s;
workspacecodex compiled. From `progress/`, this owning entry-point check passed
4 tests/26 assertions in 0.485s:

```sh
timeout 45s "$PCP_RUBY" test/dev_session_test.rb \
  --name '/^test_creation_(capture|progress)/'
```

Both staged diffs and the complete committed diff passed `git diff --check`.
The first commit owns 10 files; the second owns 15, including four shared files
whose second-commit changes add only optional progress wiring/stages. Full
application coverage remains the parent's corrected focused operation above.

## Remaining parent gates and deferred commands

No unresolved design question or material deviation remains. The parent has
inspected the source, approved wording and commits, and passed corrected focused
checks. Parent owns whole-branch inventory (explicitly no migrations), mandatory
independent review, long verification, dependency/deployment coordination and
any publication. No integration or cleanup is authorized by these results.

Focused socket selection for review reruns, from `portal/` in the repository
Nix environment (the parent already passed the corrected source):

```sh
GOFLAGS=-mod=readonly go test ./internal/workspacecodex ./cmd/workspace-portal \
  -run '^(TestRecover(Creating|Fork)|TestCreationRecovery|TestFreshThreadCreateAndForkAvoidDiscovery)' \
  -count=1 -timeout=45s
```

After committed quick checks and review, send these longer commands to a fresh
policy watcher; they were not run by this member:

```sh
nix flake check --print-build-logs
nix develop -c bash -euc 'GOFLAGS=-mod=readonly go -C portal test ./...; ruby test/dev_session_test.rb; ruby test/auto_archive_test.rb; ruby test/workspace_host_test.rb'
```

The browser execution requires parent-selected pinned `PLAYWRIGHT_MODULE` and
`CHROMIUM_EXECUTABLE` values; syntax alone is not browser acceptance:

```sh
CODEX_WEB_SOURCE=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/codex-web \
  node test/creation_browser.cjs
```

Architect owns the complete, unexecuted real-App-Server harness and its required
inputs/limits in [verification-prototype.md](verification-prototype.md). Exact
watcher launch, once the parent supplies the reviewed consuming package and
private authentication source:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-portal-creation-performance/verify-creation.py \
  --candidate /nix/store/REPLACE-WITH-REVIEWED-WORKSPACE-PACKAGE \
  --auth-json /absolute/private/auth.json \
  --evidence-root /tmp/pcp-REPLACE-WITH-UNUSED-RUN-ID
```

Candidate interfaces remain the normal thread/team commands, JSON stdout and
the documented progress frames. No application fault-injection hook was added.
The adapter can drop a successful root JSON response at the Ruby/helper
boundary or interrupt the exact team helper after a member-finish frame.
The benchmark and partial-team/lost-response scenarios have not run; retain the
architect's stated scheduling and network-level coverage limits. Real performance,
full browser acceptance, packaged suites, independent review and deployment
remain pending. The parent's corrected focused checks are recorded above.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/>
