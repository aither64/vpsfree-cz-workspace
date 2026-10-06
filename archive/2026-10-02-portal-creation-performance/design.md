# Portal creation performance design

Status: implementation brief for the accepted plan, 2026-10-02. Architect owns
this document; the lead owns tracking, dependency publication and deployment.
Application edits belong to the retained implementer. No implementation,
verification run or deployment is claimed by this document.

Verification refinement, 2026-10-02 21:24 UTC: the parent’s method-specific
SDK 4c observer found the old lost-response root absent from loaded membership;
read, turns-list and idle checks all returned exact-target `thread not loaded`.
That prevents any old-receipt retry or replacement. Preserve the stranded
journal and original five measurements. The accepted next prototype is two
new ordinary fault creations in the retained isolated runtime: exact slugs
`2026-10-02-creation-root-loss-corrected` and
`2026-10-02-creation-member-loss`. A pinned corrected Go `thread create`
provider at the existing adapter boundary must recover the new root’s exact
ID and every ready member ID on immediate normal retry. Keep the old Ruby,
profile, processes and all other helpers; use separate fault/result files and
an exclusive preservation claim. No schema, lifecycle or recovery-policy
expansion is involved. Parent owns provider freeze, host preflight, affected
independent review, execution and eventual full-package canary. See
[recovery-design.md](recovery-design.md) and the
[fresh fault preparation](verification-corrected-fault-preparation.md).

## Scope and evidence

Remove history discovery from proven fresh new-session, approved-plan and fork
creation. Preserve journal-owned retry behavior and show live stages while the
creation command runs. Keep team initialization sequential.

The preceding [analysis](../2026-10-02-portal-creation-latency/analysis.md)
measured a 103.546-second acceptance-to-ready interval. A separate read-only
probe measured filesystem-backed filtered listing at 98.212 seconds, DB-only
listing at 4–7 milliseconds, and all 38 ordinary metadata reads at 0.239 seconds.
These are separate traces. `excludeTurns` is not an optimization for these
ordinary reads; `thread/read` already defaults `includeTurns` to false.

The local source of the selected Codex 0.160.0 confirms that
`ThreadListParams.use_state_db_only` omits its false default and bypasses rollout
repair when true. It also confirms that DB failure can become an empty result.
Do not change Codex, add a root project, redesign roster recovery, or introduce
new receipt, journal, manifest, authority or database schemas.

Readers are runtime/SDK maintainers and operators. Lasting contracts go in
`codex-web/docs/reference.md`, `dev-workspace/docs/dev-sessions.md` and
`dev-workspace/docs/workspace-portal.md`. This design and the session rollout
record retain cross-repository decisions and deployment evidence.

## Files and interfaces

All project paths below are relative to their worktrees under
`worktrees/2026-10-02-portal-creation-performance/`.

| Repository and files | Responsibility |
| --- | --- |
| `codex-web/codex/client.go` | Add `UseStateDBOnly bool` to `ThreadListOptions`; add the JSON `useStateDbOnly` parameter only when true. All other fields and result checks stay intact. |
| `codex-web/codex/client_test.go`, `test/codex_protocol_contract.py`, `docs/reference.md` | Test true serialization and false omission, validate both request forms against selected Codex schemas, document incomplete-index semantics. |
| `dev-workspace/libexec/dev-session` | Decide freshness before journal publication; select direct start/fork only on that proof; preserve all journal and prompt markers; emit Ruby stages and stream nested helper frames through `CommandRunner.capture`. |
| `dev-workspace/portal/internal/workspacecodex/client.go` and `client_test.go` | Implement loaded/index/full-scan discovery and its identity checks; accept only application-validated exact member exclusions and an optional per-call progress observer. Keep retirement/revive discovery unchanged. |
| `dev-workspace/portal/cmd/workspace-portal/main.go` and command tests | Route direct fork versus recovery; load and validate retained roster exclusions in this layer; bind progress to thread/team commands. |
| `dev-workspace/portal/internal/teamruntime/runtime.go` and `runtime_test.go` | Report each member's initialization around the existing sequential preset/fork loops. Preserve project/start/bootstrap reservations and exactly the existing recovery policy. |
| `dev-workspace/portal/internal/creationprogress/progress.go` and `progress_test.go` (new) | Small internal wire event, bounded decoder and optional emitter shared by Go helpers and the portal. No persistence or Codex policy here. |
| `dev-workspace/portal/internal/web/server.go`, `creation.go`, `creation_test.go` | A creation-specific streamed-command path and active-attempt phase updates; existing buffered path remains for unrelated commands. |
| `dev-workspace/test/dev_session/{session_initialization,session_recovery,fork_recovery,fork_receipts,agent_team_creation,codex_runtime}_test.rb`, `test/support/dev_session_test_case.rb` | Fresh versus resumed routing, fault injection, initial-goal markers and Ruby capture forwarding. Put reusable fixture support in the existing support file. |
| `dev-workspace/test/creation_browser.cjs` | Verify live stage text and elapsed display through the existing polling UI. `portal/internal/web/static/creation.js` needs no transport redesign: it already polls and renders `phase` with `textContent`. |
| `dev-workspace/docs/{dev-sessions,workspace-portal}.md` | Own freshness/recovery behavior and the private progress transport contract respectively. Add concise comments at decisions a later refactor could undo. |
| `dev-workspace/{flake.nix,flake.lock,portal/go.mod,portal/go.sum,nix/workspace-portal.nix}` | Lead-coordinated SDK pin, matching Go pseudo-version and any required vendor hash. No Codex/llm-agents update. |
| `vpsfree-dev-workspace/{flake.nix,flake.lock}`, `workspace/{flake.nix,flake.lock}` | Exact downstream feature revisions only. Preserve provider and team catalogs. |
| `vpsfree-cz-configuration/flake.lock` | Generated exact `dev-workspace` channel / `devWorkspace` role pin via confctl. No host-module behavior or application system pin is needed. |

Keep recovery options internal to dev-workspace. An options-bearing helper may
carry exact excluded IDs plus an observer; retain existing convenience methods
as empty-options wrappers where useful. Do not put roster policy into the SDK.
`teamruntime` already imports `workspacecodex`, so load rosters in the CLI
composition layer, not by importing `teamruntime` into `workspacecodex`.

## Freshness proof and lock boundaries

The host transition lock and generation validation stay outermost. Retain the
existing destination creation lock, then slug lock. Compute the fresh decision
inside both locks, before any creation journal, tracking, manifest, tmux or
authority mutation. In particular, the existing `fresh_destination` used for
team selection outside the slug lock is not sufficient proof for this decision.

A destination is fresh only when all of these hold:

1. This is a normal start with an initial request, or a new fork destination;
   it is not preserved tracking, revival, an existing-session open, or the
   legacy allow-empty recovery path.
2. No destination creation, fork or runtime-start journal already exists.
   Conflicting lifecycle journals and archived destinations retain their
   existing refusals.
3. There is no existing active/archive tracking, destination worktree directory,
   portal manifest, selected tmux session, runtime authority or retained team
   roster. Use the existing bounded/path validators and `lstat`-style presence
   checks; uncertainty disables the fast path or refuses through its owner.
4. The receipt/request and any source selection pass the existing validation.
   A private accepted portal receipt is allowed: it precedes CLI effects and is
   not evidence that a root-thread request has already been submitted.
5. The current invocation successfully publishes the existing durable creation
   or fork journal with create-only semantics before contacting App Server.

Use a local boolean, never a persistent `fresh` flag. Freshness means this
locked invocation is the first possible submitter in the supported workspace
creation workflow. Local operators are trusted; do not add defenses against
an operator fabricating an unrelated thread at an unused destination outside
that workflow. Concurrency, accidental stale state and interrupted commands
remain in scope.

For start/plan, preserve `prepare_creation_journal` and its exact request
matching. A freshly written `state: creating` journal must not itself select
recovery. Invoke `create_portal_thread` without `recover_creating` only when the
local fresh decision is true and no recorded ID exists. Its existing
`OpenThreadWithSettings` empty-ID path starts directly. A plan still validates
the source plan, source identity and captured settings before creating its
destination; it does not inherit the source conversation.

For fork, decide within the locked `unless fork_journal` branch after the
existing empty-destination checks, before `prepare_fork_journal!`. Add an
explicit private helper option such as `thread fork --fresh`; default helper
behavior remains recovery for existing callers. Only this proven first
invocation passes it. Direct mode calls `ForkThread`, then preserves the
existing upload-reference and result handling. All fresh-source validation,
source settings resolution and frozen fork journal fields remain unchanged.
Do not move source and destination lock acquisition into a new nested order.

Any process interruption destroys the local boolean. A retry sees the original
journal and enters recovery even if the prior process died before the first
RPC. Do not reconstruct freshness from an empty manifest, an empty DB page,
receipt attempt number or journal `creating` state. Retained tracking and
`allow_empty_thread` keep their conservative behavior.

## Recovery, ambiguity and exact member exclusions

Recovery continues to belong to the original journal. Preserve its goal digest,
source/fork identity, frozen model/effort, direct-team snapshot and tmux nonce.
Ready roots always open their recorded ID; they are never replaced.

For creating-root recovery, inspect loaded threads and indexed threads, then
use complete discovery before an identity decision that needs absence or
uniqueness. Fork recovery also needs the loaded-thread pass, since a fork
response can be lost while the destination exists only in memory.

### Exact roster filtering

Member threads intentionally share the root cwd. Do not classify a candidate as
a member by project presence, name, address prefix, source kind, or apparent
role. Those are not root ownership proofs.

The CLI loads the destination's `teamruntime.Store` using the selected private
state root, workspace, slug and recorded root ID. Hold `Store.LockOperation`
while loading its validated snapshot and reconciling root candidates; release
it before invoking preset/member bootstrap. Keep the lock order
transition → creation → slug → team operation, matching the existing team path.
No new thread should be created while that roster operation lock is held.
If a replacement would be needed with a retained roster, refuse: the roster
binds the old root and must not be silently retargeted.

Use `Store.Load`/`Roster.Validate`, including duplicate/member-is-root checks.
Only exact nonempty member `Thread` IDs from that valid roster can be removed
from the root candidate set. When metadata for one is encountered, verify its
cwd and retained project identity where present before excluding it. Preserve
legacy roster entries without a project field; do not require a migration or
invent a project for them. A missing roster means no exclusions. A malformed,
wrong-workspace, wrong-slug or wrong-root roster is a refusal. A roster without
an independently recorded root is inconsistent; do not use its own root ID to
bootstrap trust or hide candidates. A `creating` member without a recorded
thread does not authorize excluding a thread found by project alone.

### Discovery decision procedure

1. Collect all loaded IDs, read metadata without turns, verify returned IDs, and
   preserve the existing vanished-loaded-thread recheck. If an ID disappears
   from a second loaded list it may be skipped; a still-loaded unreadable ID
   prevents a safe decision. A recorded root with wrong cwd/source is a refusal.
   Unrelated cwd/source threads are not candidates.
2. List the exact destination cwd, `sourceKinds: [vscode]`, active history,
   ascending order, with `UseStateDBOnly: true`. Enumerate enough pages to prove
   the result after exact member exclusions. The old raw `limit: 2`/nonempty
   cursor ambiguity rule is invalid when a page contains only known members.
   Deduplicate by ID; repeated cursors or contradictory rows are inconsistent.
   Bound the indexed pass to 64 pages / 4096 rows in addition to the existing
   context deadline. Reaching a bound is inconclusive and selects full scan,
   never success or absence. Complete discovery may stop once two validated
   nonmember candidates prove ambiguity; otherwise it must finish pagination
   or refuse when its deadline/bounds prevent proof.
3. Validate candidate metadata, including nonempty ID, exact cwd and source.
   Re-read index-only candidates before relying on them; do not let stale
   cached fields hide wrong source, fork ancestry, or a disappeared thread.
   Never stop at the first matching loaded candidate before checking indexed
   candidates. Two confirmed nonmember candidates refuse immediately.
4. Empty, failed, malformed or inconsistent indexed discovery cannot authorize
   a replacement. Perform the existing filesystem-backed list with the same
   filters and `UseStateDBOnly` omitted. Merge its validated candidates with
   the loaded set and preserve disagreement/refusal evidence. The scan must
   finish successfully; a timeout, unreadable metadata or unresolved pagination
   cannot be converted to an empty candidate set.
5. Conservative completeness rule: an otherwise positive indexed result also
   cannot prove that an unindexed second root does not exist. This design keeps
   complete filesystem discovery before adopting or resuming a recovery root,
   as well as before replacement. The fast index can expose a refusal early;
   it is not a uniqueness certificate. This preserves the previous ambiguity
   contract literally. Rare recovery remains slow, with a visible scan phase.
6. After complete discovery, more than one nonmember candidate refuses. One
   candidate must pass the existing history rules. For start, a materialized
   candidate different from the recorded root refuses. A sole proven fresh,
   unmaterialized candidate is adopted with its original start-time policy and
   environment, without `thread/resume`; materialized retained roots keep the
   existing resume/policy behavior. Prompt-attempt behavior remains unchanged.
   This proposed correction follows the real lost-helper-response failure;
   see [recovery-design.md](recovery-design.md) for evidence and review boundaries.
   A normal start must not adopt a fork as its replacement. For fork, require
   exact `ForkedFromID == journal.source_thread_id`, exact cwd/source, and idle
   turns before resume. Never replace the source or use a different fork.
7. Only a complete, consistent zero-candidate result may start/fork a
   replacement, subject to existing retained-history/refusal checks and no
   roster binding to the missing root. Resolve new settings only when a new
   root actually must be created. Existing roots retain captured settings.

Step 5 is a justified refinement of the accepted plan, explicitly accepted by
the coordinating parent through the session lead on 2026-10-02. Even a nonempty
DB page lacks a completeness proof. Omitting the full scan for a positively
validated recorded root would weaken the refusal guarantee for unindexed
duplicate roots. Fresh start/plan/fork bypass remains the latency solution;
the optional SDK flag supports bounded indexed discovery and protocol tests.

Retirement, archive/delete/revive and member project reconciliation keep their
current algorithms and timeouts. No new global history scan is introduced on
the normal start/plan/fork path or on fresh member initialization.

## Initial goal and interruption invariants

Publish the recorded root ID before member creation. Team initialization must
finish before the lead receives the initial request. Keep the current roster
project ID, create-attempt and bootstrap-attempt reservations; do not parallelize
members or start model turns to initialize them.

Preserve the meaning and ordering of `initial_goal_attempted` exactly:

- A genuinely new root gets `false`; write `true` durably before the one allowed
  initial submission and pass `--start-unmaterialized` for that first attempt.
- Recovery of the same root never resets `true` to `false`. Legacy omission
  remains conservative. An uncertain initial turn is reconciled against its
  exact history, not resubmitted because the DB is empty or metadata has no turns.
- Reset to `false` only after an authorized replacement has returned a different
  root ID and that ID is durably recorded. Never replace a materialized/ready
  root or one still bound by a retained roster.
- Keep the creation lock across the initial request. Release the slug lock as
  today so that the initial turn can use session helpers; reacquire and recheck
  root/manifest/tmux identity before recording sent/ready state.

Failures after journal publication, lost start/fork replies, interrupted
manifest writes, partially initialized teams, unknown prompt outcomes and lost
completion replies all retry through the same journal and receipt. Do not
truncate/delete those files or discard the original settings to obtain speed.

## Progress transport and receipt updates

Use an opt-in environment variable `DEV_WORKSPACE_CREATION_PROGRESS=1` for the
portal's creation subprocess only. This permits a new portal to run an older
helper that emits no frames without an unknown-option failure. Ruby consumes
the flag and enables it explicitly on the relevant nested `workspace-portal`
thread/team subprocesses. Do not persist it in tmux or Codex runtime environment,
manifests, journals or saved team policy. Default CLI output remains unchanged.

The private protocol is a record-separator byte, an exact ASCII prefix, one
UTF-8 JSON object and LF:

```text
\x1eDEV_WORKSPACE_CREATION_PROGRESS/1 {"stage":"team_member","event":"finish","elapsedMs":1042,"member":"architect0"}\n
```

The displayed escapes above denote bytes, not literal backslashes. Contract:

- Maximum complete frame: 4096 bytes. Fields are `stage`, `event`, `elapsedMs`
  and optional `member`; no prompt, tool output, instructions or absolute path.
- `stage` is one of `prepare`, `conversation`, `recovery_loaded`,
  `recovery_index`, `recovery_scan`, `team_member`, `prompt`, `terminal`,
  `evidence`. `event` is `begin` or `finish`. `elapsedMs` is an integer from zero
  through 86400000: zero at begin and monotonic stage duration at finish.
  The optional member is the validated roster address, bounded to 128 bytes.
- Timers are local to the emitting stage; nested durations overlap and must not
  be added. Acceptance-to-ready remains the receipt interval. No process's
  monotonic timestamp is interpreted as another process's clock.
- A stage begins before its blocking operation and finishes only after success.
  Ordinary errors remain diagnostics and follow the existing command result.
  There is no `ready` event and no field that can change receipt authority.

Emit Ruby stages for preparation, direct conversation invocation, terminal
preparation/reconciliation, initial-request persistence and final evidence.
The Go thread helper emits recovery loaded/index/scan stages immediately before
the relevant calls. `teamruntime.Service` gets a nil-by-default progress callback
and reports each member around the existing sequential loops, including forked
member bootstrap. Preserve stdout: thread JSON, roster JSON and final
`dev-session --json` must each remain independently parseable as before.

`CommandRunner.capture` currently uses `Open3.capture3`, which hides child
stderr until exit. Add an opt-in streaming branch using `Open3.popen3` with
concurrent draining of stdout and stderr (and safe concurrent stdin delivery
where input is used). Forward complete valid progress frames immediately to
the outer stderr and flush them; keep ordinary diagnostic bytes in the returned
stderr/`CommandError`. Avoid replaying already-forwarded frames on failure.
Preserve argument arrays, timeout wrapping, `pass_fds`, transition/slug lock
descriptors, input bytes, exit status and exception cleanup. Keep the default
capture path for unrelated commands. Never read all stdout before stderr, which
can deadlock a child with full pipes.

In Go, use a creation-specific runner alongside
`runDevSessionWithTransition`; preserve `ExtraFiles`, environment and
`processgroup.Run` cancellation. Assign an incremental stderr writer/parser
that forwards valid events to a callback while retaining diagnostics. Drain
through EOF and join callbacks before applying the final result. Preserve
ordinary stdout and command failure handling. The callback must not recursively
take an operation lock already held by the runner.

Both parsers handle split prefixes/JSON/newlines, multiple frames per write,
diagnostics between frames and trailing non-frame bytes. Invalid JSON, unknown
versions/stages/fields and oversized/truncated frames never update phase.
Use a bounded buffer and discard oversized candidate records through their
delimiter while continuing to drain subsequent output; do not use an uncaught
`bufio.Scanner` token-limit error that stops reading the child. Keep surrounding
diagnostics, with a bounded truncation notice for oversized records. A malformed
progress frame alone must not fail an otherwise successful creation or hide
the actual child exit status. Avoid repeated warnings or unbounded diagnostic
retention from rejected frames.

For every callback, under `operationMu`, look up the current receipt and require
the same workspace/slug, receipt ID and attempt, with state still `running`.
Merge only `Phase` and `UpdatedAt` into that current receipt, then persist it.
Do not write the callback's stale whole-receipt copy over validation/settings,
terminal states or a newer attempt. A cancelled/paused/failed/ready/conflict
attempt ignores later frames. The subprocess callback closure supplies identity;
frames cannot select a receipt. Progress persistence failure may be reported
without killing the child; final outcome persistence and evidence remain the
existing authority. Bound/coalesce duplicate updates so output cannot cause
unbounded receipt writes.

Map stage codes to fixed phase text, with validated member address and completed
duration where useful. Retain the existing browser's total elapsed clock and
one-second polling; no new browser API or receipt fields are needed. Apply the
user-facing-writing skill to final labels in the implementation before commit.
Progress never sets `State`, `Validated`, initial-goal flags or ready evidence.
Only normal final stdout validation, `proveCreation` and upload binding may
let `runCreation` publish ready. Existing recovery after a lost success reply
still requires `proveCreation` to succeed.

## Compatibility and operational recovery

`UseStateDBOnly` is an optional SDK addition; zero-value callers emit exactly
their old request. The selected Codex supports true; no version negotiation or
Codex upgrade is needed. Validate this against schemas generated by that exact
package, not only the SDK coverage-only corpus. A server rejecting the optional
parameter enters conservative discovery on a recovery call rather than being
treated as an empty result. No change to generated clients, Terraform, service
messages, host module options or vpsAdminOS fleet coordination is involved.

Existing creation/fork journals, schema-1/3 receipts, expanded/legacy roster
snapshots and schema-1/2 manifests retain their bytes and validation contracts.
Existing schema-2 virtual-team refusals remain. There is no migration, seed or
new supported predecessor schema. The progress protocol is ephemeral and
versioned independently; old callers omit opt-in, old helpers simply provide
the existing broad phase, and newer helpers keep stdout compatible.

The new private fresh-fork option is used only within the matching package.
Profile generation checks still reject a command waiting across a package
transition. Do not support bypassing that gate to mix arbitrary helper binaries.

Deployment, owned by the lead, is ordered as follows:

1. Finish focused checks and committed whole-branch inventory, including an
   explicit no-migrations conclusion. Run independent mandatory review before
   long integration tests. Reconcile material changes through the lead.
2. Publish feature revisions over SSH; align codex-web → dev-workspace
   (flake and Go pins) → vpsfree-dev-workspace → workspace. Preserve Codex and
   unrelated inputs; account for expected transitive locks/vendor hash.
3. In the configuration feature worktree, use
   `confctl inputs channel set --commit dev-workspace devWorkspace <runtime-rev>`.
   Keep generated history/messages and inspect its lock diff.
4. Run the workspace's `bin/check-dev-workspace-deployment` with the exact
   workspace/configuration worktrees. The nested workspace runtime revision
   must equal the configuration's `devWorkspace` revision.
5. Build `cz.vpsfree/machines/aitherdev`, dry-activate, then activate its host
   configuration. Switch the workspace application from the user profile using
   the supported `workspace-host switch --source <workspace-worktree>` command.
   Do not install the workspace application through system pins.
6. Verify selected revisions, service health, retained conversation/root/team
   identities, creation progress and the retained real-history canary. Keep
   deployment outputs/revisions in the session rollout record.

Recover by repeating an interrupted supported switch or building a new forward
generation that reverts the faulty code while retaining current state support.
Never select an older profile generation. Existing interrupted-creation
journals may block a switch: resume their exact accepted requests and preserve
refusals; do not delete state to clear the transition gate. Slow complete recovery
is an acceptable outcome. Do not reset production Codex history or its DB for
performance testing. No deployment or handoff authorizes integration or session
cleanup; retain branches and canary sessions.

## Acceptance and verification brief

Correctness gates:

- Fresh new, approved-plan and fork creation perform no `thread/list` or
  loaded-thread discovery for the destination root. Fixture handlers must fail
  if these requests occur, rather than merely asserting lower elapsed time.
- Competing attempts serialize. A waiter that observes another attempt's
  journal never uses the fresh path. Test interruption before/after journal
  publication, before/after root RPC, before/after manifest publication, each
  member, prompt-attempt publication, prompt acceptance and final evidence.
- Recovery preserves stable root/member IDs and exactly-once initial requests.
  Test loaded-only roots, disappeared loaded candidates, lost responses,
  App Server restart, DB error/empty/stale/missing rows, one hidden filesystem
  candidate, two hidden/visible candidates and unreadable full-scan failure.
- Wrong cwd/source/returned ID, wrong fork source, a different materialized
  root, active fork turns, changed settings/source/goal and contradictory
  history refuse. Unknown indexed outcomes never create replacements.
- Exact roster exclusions handle several pages of known members, a root after
  member-only pages, missing/invalid/wrong-root rosters, an unknown same-cwd
  project thread, unrecorded member IDs and duplicate root/member IDs. Prove a
  hidden unindexed duplicate still refuses under the conservative scan rule.
- A retry with the same root and `initial_goal_attempted: true` cannot send
  another unmaterialized initial turn. Only a proven different replacement can
  reset the marker; a retained roster prevents silent root replacement.
- Observe a nested Go stage at the HTTP creation endpoint while the fake child
  remains blocked before exit. Cover real Ruby forwarding, split/multiple
  frames, diagnostics, invalid JSON, duplicate/unknown fields, oversized records,
  final partial records, later valid frames, stale attempts, terminal-state
  guards, timeout/cancellation, failure status and old helper silence.
- Neither forged-looking stage fields nor a successful final progress event
  can mark ready without matching final evidence. Test phase persistence racing
  final receipt updates and currentCreation's ready reconciliation.

Known quick checks, using each project's Nix environment:

- SDK focused `go test ./codex -run 'Test.*(ListThreads|Project)'` and the
  request-corpus coverage check; add an accurately named list-options test.
- From `dev-workspace/portal`, focused tests in `./internal/workspacecodex`,
  `./internal/creationprogress`, `./internal/web`, `./internal/teamruntime` and
  `./cmd/workspace-portal`, selected by the changed recovery/progress tests.
- Ruby syntax and the individual owning files in `test/dev_session/` above;
  use `test/support` fixtures instead of real sessions for fault injection.
- `node --check portal/internal/web/static/creation.js` if changed and the
  creation browser contract. Run declared hooks; syntax checks do not replace
  them. `git diff --check` includes documentation and generated pin diffs.

The lead selects exact focused test regexes after implementation. A check that
is not known to finish within one minute, and any integration/build command,
belongs to a fresh catalog Luna/low watcher before launch. No such command was
launched during design.

After quick checks and independent review, run packaged flake checks and full
Go/Ruby suites, the exact installed Codex protocol/schema check, and integration
against an isolated App Server/tmux/state root. Include one real lost-response
recovery sequence and a multi-member partial-creation retry. Do not substitute
a fast fake-only suite for real App Server behavior. Existing package checks
cover host/profile contracts; additional VM checks follow the actual affected
contracts and the lead's verification decision, without unrelated cluster VMs.

Performance gate: five sequential warm Full-team creations with representative
history in isolated state. Record acceptance, CLI start, root invocation, each
member, prompt persistence, final proof and ready timestamps. Median
acceptance-to-ready must be below 10 seconds and maximum below 15 seconds.
Keep warm-up separate, report all five values, history size, exact package
revisions and clock source. Do not exclude slow samples or remove history to
pass. Root/model response latency is recorded separately and is not part of
readiness. A slower recovery scan is outside the fresh-path latency gate.

After deployment, retain one actual-history portal canary with a harmless
initial request. Verify live progress before ready, final root/roster evidence
and acceptance-to-ready independently of the first assistant response. Avoid
inventing an unapproved destructive cleanup step for the canary.

## Implementation sequence for the lead

1. Implement the SDK field/corpus tests and the locked fresh-path selection.
2. Add conservative recovery discovery, exact roster filtering and targeted
   lost-response/initial-goal tests before considering any fast recovery return.
3. Add the shared progress event/decoder, nested Ruby forwarding, per-stage
   emissions and guarded portal phase persistence; keep member order unchanged.
4. Reconcile project docs and focused checks, then commit implementation and
   give the reviewer the whole-branch history plus no-migrations inventory.
5. The lead coordinates long verification, exact dependency pins, deployment
   and measured canary acceptance. Architect reviews consequential deviations.

No blocking design question remains. Material changes requiring referral are:
skipping the complete scan during recovery, deriving member exclusions without
the recorded root/validated roster, altering initial-goal attempt semantics,
changing persisted schemas, parallel member bootstrap, adding a root project,
changing Codex, or moving application deployment into the system configuration.
The coordinating parent owns final acceptance and implementation assignment.

## Assigned verification prototype

The architect's follow-up assignment permits a standalone harness and brief in
this tracking directory only. It will invoke the explicit candidate package and
its selected Codex 0.160.0, create synthetic representative history with real
start/inject RPCs, and use isolated registry/state/profile-link/tmux/socket paths.
It will not activate a package or change production state. Candidate public
launch commands and the existing dev-session helper boundary are the fixture
interfaces; no application changes or new persisted application schema belong
to this prototype. Execution is deferred to the lead's fresh watcher after
committed checks and review. Runtime evidence and any supplied authentication
copy stay in a private directory outside Git.

The prototype measures durable portal acceptance-to-ready separately from model
response for one warm-up and five sequential measured creations. Its fault
cases drop a completed root helper response and interrupt a team helper after
a completed member stage. These exercise real Codex operations, but the first
is not a network-level RPC response drop and the second is subject to scheduling
between the progress event and interruption. The brief must expose these limits
and treat a missed partial-state boundary as inconclusive. No automatic session
archival, deletion, process retirement or artifact cleanup is included.

The lead's bounded continuation assignment permits reusing only the failed
pre-registration fixture `/tmp/pcp-oct02-a` and its unchanged candidate package.
The prototype must add the schema-2 `sshHost: ""` key, with no loader relaxation.
An explicit `--resume-seeded` path validates the original registration failure,
empty creation results, private ownership, retained auth metadata, exited seed
process, unchanged preset/version and all 3,379 persisted 16 KiB seed payloads.
It refuses registration, runtime, creation or prior-continuation evidence. The
observed empty `state/transition.lock` is allowed only when it can be locked
without waiting; it is retained. An exclusive, never-removed continuation
directory preserves the original failure result, stderr and invalid fixture
before any replacement. Repeated or interrupted continuations refuse. The
existing registration/launch, warm-up, five timings, model/progress and fault
checks then run unchanged. This is a fixture correction, not application or
session recovery; the architect prepares it and the parent's watcher executes.

The subsequent pre-portal failure exposed a prototype identity error: the
selected public Codex command is the assembled package's shell launcher, while
the process executes the native entrypoint declared in its layout-1 manifest.
One prototype helper resolves that declared native identity. A separate thin
`verify-started-creation.py` driver may continue only the demonstrated registered
fixture, after exact process start/executable/cwd, marker, profile and retained
record checks. It preserves the live App Server and the first continuation
claim. Its own exclusive claim preserves the current failure/process/config/
marker evidence. The environment block and existing tmux/portal/full acceptance
tail are extracted unchanged for reuse; no new main flags, runtime restart,
generic adoption, schema or acceptance changes belong to this follow-on.

The selected Codex transport advertises its protected Unix socket through a
symlink. The parent's corrected metadata proves the exact alias and unchanged
physical target; the earlier proxy interpretation was incorrect. The follow-on
driver must pin the sibling alias proof, validate both recorded identities and
the original App Server's exact listener FD/kernel inode before claiming the
continuation. Only that proved alias is allowed by the fixture link/writability
guard. Preserve both proofs with the failure evidence. Focused checks model the
real alias/target separately and reject replacement, foreign ownership and
listener changes. Application behavior, deployment, recovery limits and the
full acceptance sequence are unchanged; the parent owns review and execution.

The completed warm-up exposed another prototype contract error: selected Codex
0.160 persists canonical user `ResponseItem` content with harness classifications,
without requiring a `user_message` event echo. The counter must count exact GOAL
parts classified `user.text`, distinguish only the known AGENTS/environment
context classifications, validate any event echo without counting it, and keep
the exact-one, no-tool, assistant, completion and timeout gates. A separate
one-use after-warm-up driver may validate the current failure and parent-pinned
process/socket/receipt/roster evidence, recompute the completed warm-up proof
read-only, preserve all prior claims and make a new exclusive preservation
claim. It must not resubmit the goal or restart services. The five samples and
both faults have one shared extracted owner; progress validation is shared with
fresh creation so retained warm-up evidence passes the same checks. No sample
is omitted or replaced by warm-up. Focused checks use mocked runtime boundaries;
actual host preflight, independent review and one watcher run remain parent-owned.

## Real lost-root-response correction proposed to the lead

All five measured creations passed at runtime `8ae46f9`; the subsequent fault
retry failed after complete discovery. The failed manifest has no recorded root
ID and still has `initial_goal_attempted: false`. The selected Codex source
requires persisted storage inside `thread/resume`, including for a loaded
thread. Its exact `-32600: no rollout found for thread id <ID>` means missing
persistent rollout, not proof that the live thread is absent. The current
nonzero-policy recovery branch therefore attempts an unsupported resume of the
valid, unmaterialized root. Widening SDK `IsThreadNotFound` would not fix this
branch and would affect unrelated retirement proofs.

The bounded implementation belongs in runtime
`portal/internal/workspacecodex/client.go`: retain every discovery, identity,
roster, fork and history check, then adopt a proven unmaterialized candidate
without resume regardless of whether its frozen policy is nonempty. The
successful original `thread/start` already installed that policy, lifecycle
instructions, MCP configuration and environment. This retains those settings;
it does not claim to reapply new instructions through a read or initial turn.
The existing materialized-root resume path and conservative uncertain-goal
refusal remain. No SDK predicate, persisted format, Codex version, fresh path,
progress or team ordering changes are proposed.

[recovery-design.md](recovery-design.md) specifies consumers, source evidence,
focused negative cases and the two unfinished fault checks. It also records a
parent-owned operational prerequisite: the normal package switch refuses the
retained unfinished creation. A continuation must establish a supported way to
run the reviewed correction while retaining the live root; it cannot clear
journals, forge package identity or restart away the failure. The five original
timings remain evidence for their original revision, with corrected fault
evidence recorded separately. Parent acceptance, implementation, review and
actual continuation remain outstanding.

## Bounded corrected-provider fault verification

The parent accepted the narrow recovery correction and assigned its application
edit to the implementer. The existing prototype's configured Go-helper adapter
provides a concrete compatibility-test boundary: old Ruby retains its selected
profile/generation and forwards the original complete runtime/frozen-policy
arguments to `thread create`. That Go entry has no profile/package switch.
A finite `rootRecoveryProvider` adapter field may select one explicitly pinned
new compiled provider only for `thread create` on the two fixed fault slugs.
Every other command, argument, environment and inherited lock FD remains on the
existing path. Provider default Codex and runtime contract must match the old
package. This is an old-consumer/new-provider fault check, not activation or a
substitute for the full-package canary.

Prepare `verify-fault-creation.py` to validate the exact attempt-2 failure, five
retained samples and current parent process/socket proofs, then make one new
exclusive durable preservation claim. Only afterward may execution add the
adapter field and write a new result. Retry the same root receipt from 2 to 3,
require the original root, and run the original member fault once. Extract the
existing post-ready acceptance tail into one shared owner; preserve all goal,
model, no-tool, roster, stage and timing checks. No warm-up, reseed, five-sample
rerun, profile/registration change, service restart or generic resume API.
The architect prepares source and focused mocked/static checks only; parent
freezes the built provider path/hash, reviews and owns read-only host preflight
and watcher execution. Detailed command and evidence go in
`verification-fault-preparation.md`.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/>
