# Historic session metadata repair, 2026-10-04

This dated workspace source utility repairs this installation's historic
tracking during a supervised maintenance window. Workspace maintainers own it;
the coordinating lead owns the selected inventory, preparation, approval and
execution. It is never exported by Nix, a profile, dev-session, the portal or an
automatic worker. Writing this procedure does not authorize a real repair.

The tool reads the committed runtime owners at
`43fc46e89c6ccafec16002e960c8fb11ff9f58ba`. The supplied runtime checkout must use
the selected workspace's canonical `repos/dev-workspace.git` common directory
and `git@github.com:aither64/dev-workspace.git` origin. Working files are not
runtime proof inputs. Prepare a new projection if source, helper or selected
executor/profile/generation coordinates change.

## Supported inputs and scope

Select exact slugs in either `work/` or `archive/`. Preview unions current and
committed structured manifests, exact local/cached-origin slug refs and owned
attached features, including obligations whose checkout or ref is missing.
It does not fetch. Several projects with one slug are several obligations.
Ambiguous defaults, branches or roots need one reviewed mapping that selects
existing evidence. A no-evidence record needs explicit coordination-only scope
and an explicit threadless decision. Prose does not prove scope or completion.

Preserve original plan/state body bytes, CRLF, artifacts, exact roots/teams and
refs. Dirty checkouts are read-only metadata evidence, with their real dirty
flags and status/diff hashes retained. Repair does not clean or commit project
files; ordinary archive still refuses dirty worktrees. Active-path records without an anchored lifecycle receive an active header
above all original bytes. Unsupported headers need an explicit reviewed
`prepend_active` decision. Archives need genuine committed terminal lifecycle,
recorded finalization and exact recorded final heads. Unknown archive provenance
blocks; the tool cannot invent an active past or a completion. Historical bases
come only from structured evidence, never today's default, ancestry or a tip.
Predecessor post-revival inferred bases are omitted unless independent recorded
history supports them. Missing retained refs remain obligations.

Creation-less retained roots require fresh exact public root/team/authority/
discovery/submission proof. Present malformed, pending or contradictory creation
blocks. Genuine ready CLI creation metadata and a matching ordinary creation
journal can be preserved through the pinned Ruby creation owner, including
`initial_goal_sent: false` without a goal digest; the tool creates no ready or
goal evidence. Portal-created rows with any selected current or rotated private
creation receipt are **excluded**, including genuine ready rows. Their ordinary
creation owner remains authoritative. This utility never parses or corroborates
those private receipts, deletes one, or supplies a ready summary. An unresolved
row that also has such a receipt needs a separate lead disposition.

Pending start/fork/lifecycle/cleanup journals and nonterminal browser receipts
also block and stay with their ordinary owners. A valid completed browser row
is retained untouched; it certifies no target or lifecycle here. Unrelated valid
browser rows do not reserve this slug. A malformed store is unknown, not empty.
No repair can certify lost expected revive journal/success evidence or adopt a
new root. Ordinary runtime reads never depend on the tool's recovery evidence.

## Preparation and native proof callers

This dated operation supports only selected Codex 0.160.0 ordinary stored ChatGPT
authentication. Main must exclude account/login/config writers for the entire
window and interruption recovery, freshly read `getAuthStatus` with
`includeToken: false, refreshToken: false`, require `authMethod` exactly `chatgpt`,
and verify the actual selected `auth.json` has `auth_mode: chatgpt`.
`account/read.type` alone is insufficient. External tokens, other or unknown
authentication block this operation. The ordinary client does not subscribe or
resume threads; this auth precondition excludes its global external-token refresh
callback. Main owns the private native preflight, window checks and execution.

For a positive root, the tool calls the selected absolute `workspace-portal team
require-archive-ready` with the reviewed root, original `WORKSPACE/work/SLUG`
CWD and actual selected socket, Codex home, private state and authority. The
existing owner proves the exact retained set and idle public state. Archived
subjects use its positive vscode/notLoaded/unloaded/terminal-turn/resolved-
submission proof. Dormant archived queue rows are preserved; queue/list is not
called on that branch. Native calls do not create, resume or archive threads.

Prepare the source-only negative/receipt caller once in private scratch. In the
declared runtime Nix environment, with absolute `R_SOURCE`, `BUILD` and `W_SOURCE`
and the exact reviewed `R`:

```sh
umask 077
mkdir -m 700 "$BUILD"
git -C "$R_SOURCE" archive "$R" portal | tar -x -C "$BUILD"
mkdir -p "$BUILD/portal/cmd/dated-legacy-threadless"
cp "$W_SOURCE/bin/repair-legacy-sessions-2026-10-04-threadless/main.go" \
  "$BUILD/portal/cmd/dated-legacy-threadless/main.go"
cp "$W_SOURCE/bin/repair-legacy-sessions-2026-10-04-threadless/web/receipt_bridge.go" \
  "$BUILD/portal/internal/web/dated_legacy_repair_bridge.go"
GOWORK=off go -C "$BUILD/portal" build -mod=readonly -buildvcs=false -trimpath \
  -o "$BUILD/threadless-proof" ./cmd/dated-legacy-threadless
```

The exported source has no Git worktree; disable Go VCS stamping and retain the
explicit runtime revision and executable hash below. Keep committed `go.mod`/`go.sum`
unchanged. The default threadless mode calls
exported `workspacecodex.RequireThreadlessConversations`, including the reviewed
fail-closed project index partitions, bounded saved headers, exhaustive loaded
scope and public submission bracketing. Prepare against the final committed
runtime containing that owner, then roll this tool's exact source revision and
context together before a fresh preview; never compile working owner edits.
Receipt mode uses
the existing web store's strict read-only loader. This export exists only in
scratch. There is no installed bridge, protocol copy or private ledger parser.
Actual selected HOME/UID/Codex/private state/socket and the public ledger path
`SOCKET.submission-attempts-v3.json` must survive invocation. Scratch is a build
directory, never a replacement home or empty ledger. Missing build/native proof
blocks preparation. Do not silently rebuild on retry.

Set `REPAIR_LEGACY_CONTEXT` to one absolute owned regular mode-0600 JSON file
outside selected tracking. It is bounded to 64 KiB, rejects duplicate/unknown
fields, contains no secrets and has these exact schema-1 groups:

| Group | Required fields |
| --- | --- |
| Top level | `schema`, `workspace`, `runtime_source`, `runtime_commit`, `runtime`, `helper`, `maintenance_window` |
| `runtime` | `portal`, `dev_session`, `profile`, `generation`, `profile_token`, `transition_lock`, `socket`, `codex_home`, `state_root`, `authority_dir`, `tmux_socket`, `codex_command`, `codex_version`, `home`, `uid` |
| `helper` | `executable`, `sha256`, `sources`, `runtime_commit`, `go_mod_sha256`, `go_sum_sha256` |
| `maintenance_window` | `operator`, `evidence_reference`, `crash_hold`, `exclusions` |
| Each exclusion | `kind` (`portal`, `automatic` or `external`), `name`, `method`, `verify` (absolute executable followed by bounded arguments) |

The helper `sources` object maps both canonical workspace helper source paths
to their SHA256 values. Record executable and committed module hashes. Runtime
coordinates must equal actual host registry/profile selection and ordinary
profile-token/generation checks; a context file is not package authority.
Supplied applicable `DEV_*` values must agree. Preserve actual public ledger
configuration and selected Codex 0.160.0.

The window records exactly which portal mutation entry points, automatic workers
and operator-managed external writers are excluded, the observable checks and
how exclusion remains in effect after a crash. Preview may describe the planned
method without stopping writers. Apply/retry confirmation attests that the
window is now established; each boundary freshly verifies checks and native/Git
evidence. A saved timestamp is not a held window. The utility stops no services
and creates no background lease. Failed or unknown exclusions block.

## Preview, approval and apply

```sh
bin/repair-legacy-sessions-2026-10-04 preview \
  --workspace "$WORKSPACE" --runtime-source "$R_SOURCE" \
  --session "$SLUG" --mapping "$MAPPING" --json > "$PROJECTION"
bin/repair-legacy-sessions-2026-10-04 apply \
  --projection "$PROJECTION" --recovery "$RECOVERY"
```

Repeat `--session` for the reviewed selection; omit `--mapping` when evidence is
unambiguous. Preview changes no tracking, refs or repair state; ordinary advisory
locks are acquired. Review every blocker, retained obligation/root, exact source
bytes/identities and proposed target before approval. Editing a projection/digest
cannot supply new evidence. The optional mapping is schema 1 with exact workspace
and unique selected `sessions`; each row requires `slug` and `rationale` and may
select `root_thread_id` (including null), `scope: coordination_only`,
`state_decision: prepend_active`, `finalized_at` and exact `repositories` choices.
Repository choices use `project`, `branch` and optional `name`, `default_branch`,
`initial_base_sha`, `final_head_sha` and optional `historical_commits`, an array
of unique full commit SHAs. Historical additions need the row's reviewed rationale
and canonical project/origin proof. Each commit must exist and be reachable from
the named retained local/cached-origin branch. If that branch was explicitly
reviewed as deleted, an existing retained default/other ref can prove retention;
the missing branch remains an obligation with its missing refs recorded. An
additional registration is unioned with discovered obligations. Unused mappings,
unreachable objects and contradictory scope refuse. No historical commit becomes
an invented base or final head.

Preview embeds bytes only for `plan.md`, `state.md` and existing `portal.yml`.
Other regular artifacts retain exact path, identity, mode, size and streamed
SHA256 evidence, with before/after hashing checks. File-count and per-artifact
size limits do not require removing useful artifacts. The 32 MiB projection/
recovery bound, metadata-file limit and 128-row maximum still apply: prepare
smaller successive batches when needed, and preview the next batch after the
prior batch's commits. Refresh old unapplied projections; no previous real repair
has consumed their artifact payload format.

Apply takes the normal exclusive generation/transition gate, then creation/slug
locks; the retained proof owner holds its team locks. It validates **all** selected
rows before any tracking write. Keep independent backups of source tracking,
Git HEAD/index/worktree, holds and the reviewed preparation/projection before
opening the window. No build, window or real apply has been verified merely by
preparing this procedure.

Use one recovery file in an owned mode-0700 same-filesystem directory outside
selected tracking; its mode is 0600. It seals projection, immutable evidence,
exact source/target inodes and bytes, window attempts and sequential row phases:
`prepared`, `files_written`, `tracking_committed`, `grace_started`, `complete`.
Payloads and recovery are fsynced before replacement. Each normal-hook commit
writes, stages and commits only that row's `state.md` and `portal.yml`. Original
plan/artifact bytes and their tracked/staged/untracked state remain unchanged,
including dirty artifacts under selected tracking. Keep full backups separately;
unchanged artifact payloads are not recovery-file restoration inputs. No fetch/ref synthesis/branch deletion occurs. A failed hook does
not permit bypassing it.

Preview and all-row preflight keep full native proof. Each unfinished row repeats
full proof before mutation and after commit/grace before completion, including on
retry. Intervening barriers still verify the window, context, tracking/artifacts,
refs, worktrees, authority/roster and receipts. No native permission is cached or
shared between rows or attempts. A failed final proof leaves the row unfinished;
retry repeats both proofs without restarting grace. Completed reapply remains a
no-op.

After interruption, retain the window or re-establish its exact exclusions, then
retry the **same invocation** with the same preparation/projection/recovery.
Only exact recorded source or target is accepted; changed roots, artifacts,
refs, checkouts, identities, receipts or commit evidence refuse. A commit that
won before checkpoint is reused only when its recorded parent/message/paths/tree
prove it. A workspace/master obligation can advance only through this recovery's
recorded sequential repair commits, with exact parents, messages and those two
metadata paths. Earlier rows need not remain HEAD after later rows commit;
arbitrary ancestor or outside commits are refused. Never automatically roll back
a committed tree. Restore backups only
under explicit operator direction after inspecting actual commit/recovery state;
restoring raw backups requires repair before ordinary writers are exposed.

Active rows receive one fixed fresh grace checkpoint through the ordinary store,
preserving positively same-identity holds. Completed reapply is a recorded no-op,
even after legitimate ordinary edits. Archived rows get grace through later
ordinary revival. Keep the entire window closed until all selected rows and
post-write/commit/native evidence are complete; no installed reservation guards
an interrupted source-tool run.

Archive is separately approved for an exact selection after repair completes.
Use actual stable `dev-session archive SLUG --as-is` with a real PTY and its one
expected confirmation. Busy, dirty, unmerged, unknown or unexpected prompts
leave the row and reason intact. Abandonment/discard requires explicit approval.
Once an ordinary archive journal/sidecar exists, that owner controls retry;
never write a maintenance projection over it.

## Checks and removal

Focused disposable fixtures live in `test/repair_legacy_sessions_test.rb`; they
use real Git with simulated proof/window commands, not native acceptance.
Copy the two helper test files alongside their corresponding scratch sources
and run `GOWORK=off go -C "$BUILD/portal" test -mod=readonly -count=1
./cmd/dated-legacy-threadless ./internal/web -run
'TestSelectedCoordinatesAndLedger|TestDatedRepair'` in the runtime Nix shell.
Ruby uses `REPAIR_TEST_RUNTIME_SOURCE="$R_SOURCE" ruby
"$W_SOURCE/test/repair_legacy_sessions_test.rb"`. Main owns execution and reports
actual results separately. Installed acceptance support's `verify-repaired`
consumes this ordinary projection; PTY/native/browser execution remains isolated
and separately authorized. Final snapshots alone do not prove native retirement
order, and the unsupported positive predecessor factory remains absent.

Remove this dated tool and its scratch callers only after workspace maintainers
inventory active **and archived/revivable** records, interrupted recovery files,
supported package generations and backup/import/upgrade/revival producers, prove
zero dependent inputs, and close every supported path that could reintroduce raw
records. A date or successful deployment is not the removal gate. Keep ordinary
unknown-base manifests, archive journals, cleanup sidecars and their runtime
recovery owners independent of this tool's lifetime.
