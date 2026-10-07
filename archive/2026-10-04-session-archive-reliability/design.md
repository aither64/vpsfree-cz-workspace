# Session archive reliability: implementation and verification design

Status: follow-up brief READY, reconciled 2026-10-05 with the user-approved
[follow-up plan](followup-plan.md). Owner: architect0; application implementation:
retained implementer0. Main owns checks, review, rollout and authorized real repair
and the two remaining ordinary archive retries. The current follow-up below
supersedes earlier rollout holds, implementation schedules and broad acceptance
matrices in this document. Do not repeat the stopped native-fixture investigation.
Unchanged identity, cleanliness, merge, activity, receipt and recovery invariants
remain binding. The installed migrator remains removed; repair stays source-only.
Architect0 performs no deployment, repair, archive or integration action.

Historical decisions remain in [legacy root observation](design-legacy-observation-result.md),
[migration admission](design-migration-gate-result.md),
[legacy revival](design-legacy-revival-result.md) and
[idle legacy roots](design-legacy-activity-result.md). Their migration-specific
owners/interfaces are superseded here; exact identity, idle proof, no adoption,
prose preservation and honest unknown-base requirements remain. The recommendation
records the source assessment at runtime `6c110be5` / workspace `1026bd46`.

## Approved follow-up: responsiveness and real backlog repair

### Scope, evidence and implementation order

The inspected runtime baseline is `e05915986227af41ececea55e498dc07ea1bc219`
in this initiative's dev-workspace worktree. Main records subsequent exact heads
and live profile selection in state/rollout evidence. No Codex, client, schema,
roster or migration-framework change is required.

The freeze has a concrete lock chain: `lifecycleOperationForSlug` and reconciliation
in `portal/internal/web/operation_state.go` hold `operationMu` while waiting up to
15 seconds for generation SH; `executeLifecycleOperation` in `server.go` holds EX
through the entire archive subprocess. `computeIndexStatus` repeats reconciliation
per row, and `indexStatus` reconciles again. That mutex also serves unrelated
portal admission paths. Main's short idle sample measured 5.5% of one core; this
does not establish a constant idle CPU defect. Measure activity/request-dependent
cost during the follow-up. CPU samples supplement, rather than delay fixing,
the demonstrated wait chain.

One retained implementer should complete these bounded units, in order:

1. **Runtime concurrency:** cached status, bounded asynchronous reconciliation,
   SH lifecycle guards, retained session locks and serialized tracking commits.
   Own `operation_state.go`, `server.go`, affected `auto_archive.go` guards,
   Ruby `dev-session` and focused host/portal/Ruby regression tests. Preserve the
   existing inherited-EX host contract; change host code only if its regression
   exposes an actual violation.
2. **Ordinary negative discovery:** after the concurrency unit, implement the
   native indexed plus saved-header proof below in `workspacecodex`, shared by
   ordinary observation/auto-archive and the dated helper. No migration API.
3. **Browser refresh/navigation:** separate fast progress from full refresh, move
   Automatic archival to `/automatic-archival`, and offer fresh inline confirmation
   for stale pre-journal retries. Own existing templates, `static/app.js`, routes,
   browser tests and `docs/workspace-portal.md` / `docs/session-archive-recovery.md`.
4. **Dated tool preparation:** add the bounded historical-scope mapping below,
   reconcile exact runtime/helper selection, preserve corrected socket behavior,
   and prepare the existing context and reviewed batches. Main executes the
   approved real window after deployment. Do not rebuild acceptance fixtures.

### Status is a snapshot; mutations still prove authority

Keep existing lifecycle receipt/journal formats. Split display lookup from fresh
mutation validation explicitly: GET `/api/sessions/SLUG/operation` copies the last
published operation/progress/target snapshot and returns immediately. It performs
no generation-lock wait, native request, receipt reconciliation or directory scan.
Use a small separately protected immutable snapshot/cache so persisting a receipt
does not hold the display read lock. Startup seeds it from validated stored
receipts; newly accepted attempts and executor results publish their known state.
Cold or stale progress remains unknown/last-known, never inferred completed.

Use one coalesced reconciliation task per server, tied to server cancellation;
no goroutine per row/request and no unbounded queue. It copies operation IDs,
attempts and records briefly under `operationMu`, then acquires generation SH
outside that mutex, validates the current profile and reads progress/targets.
For this display task, try the generation lock once nonblocking: busy leaves the
snapshot stale and defers another attempt, rather than producing `failed/unsafe`.
Use a bounded pass context (six seconds), one pass at a time, and at most one
pending refresh request. Inspect running known operations at most once per second;
after generation contention/error back off to the ordinary 15-second refresh.
Discover journals with one `PendingLifecycles` scan in that full refresh, not in
each fast poll. Existing validated progress/completion owners remain authoritative.

Before saving any proposed reconciliation, reacquire `operationMu` and compare
the captured full record, operation ID and attempt against the current record.
Discard obsolete work after retry, dismissal, replacement or executor completion;
never resurrect a dismissed record or overwrite a newer attempt. Store writes
remain serialized through the existing owner. No generation acquisition,
`PendingLifecycleProgress`, session lookup or subprocess/native wait occurs while
holding `operationMu`, including admission and executor-completion paths. Move
those existing reads outside it and retain compare-before-save validation.

Retry/dismiss/start must not begin using cached display results as admission.
Under their generation/session guards, reread the owning receipt/journal, exact
target and profile and perform existing expected-journal/no-adoption checks.
Malformed evidence still refuses mutation. A display may expose response-only
`statusCheckedAt`, `statusStale` and `statusWarning`; these never alter the persisted
operation outcome or certify eligibility. No asynchronous task executes or retries
a lifecycle mutation.

### Fast progress and expensive refresh have separate budgets

Retain `/api/index-status`; add the narrow query `progress=1` for cache-only reads
of the same response shape. Both variants return the cached index and published
operation snapshots without waiting for a full computation. The ordinary variant
requests a background full refresh when due; a cold cache reports loading rather
than an authoritative empty/clean inventory. Reuse existing single-flight/cache
ownership, with a minimum 15-second full-refresh interval, a six-second pass
context, and 30-second error backoff measured from the last attempt. Fast requests
must never launch full computation. Warm index rendering likewise uses these
snapshots rather than synchronous lifecycle reconciliation.

Each full pass lists sessions/pending lifecycle progress once and joins one copied
operation map; remove per-row reconciliation and the second post-computation pass.
Keep repository/activity/cluster work in that full pass. Existing narrow activity
and message paths remain independent. A one-second poll while operations run uses
`progress=1`; the 15-second timer requests full refresh separately. Use one in-flight
request per timer, pause hidden pages and back off failures. An older `generatedAt`
must not trigger a one-second full-refresh loop. An accepted mutation may request
one coalesced full refresh, never one per rendered row.

Move the workspace Automatic archival overview off the index to the ordinary
GET page `/automatic-archival`, with a navigation link and a dedicated initializer.
Reuse `/api/auto-archive`, its counts, typed reasons and hold/eligibility semantics;
refresh the visible overview on its existing 30-second cadence. Keep per-session
controls. Show unavailable/stale status as such, not zero blockers or readiness.
No new batch action or policy is introduced.

For `target_changed` on a failed **pre-journal** browser attempt, refresh the target
inline and require a new explicit confirmation before the normal superseding
request. The already allocated journal ID alone does not mean a journal was
accepted: use the existing `JournalExpected` coordinate and owning progress proof.
An expected journal that is missing stays failed; never adopt a replacement root,
supersede a started receipt, or turn a GET into a retry. Same-target ordinary retry
continues unchanged. Old loaded JavaScript still may require reload; the new
bundle's inline stale-target recovery must work without reload. Publish the fresh
target already obtained by the rejecting mutation into its response/snapshot so
the confirmation does not loop on an old cached target or wait for a full scan.

### Lock ownership and inherited FD

Ordinary archive/delete/revive/automatic execution and hold changes take generation
**SH**, followed by their existing session mutation locks. Change the Go execution
guard and Ruby `with_lifecycle_transition` accordingly; retain post-acquisition
generation/profile/token checks and refuse stale queued callers. Include lock
waiting in the operation timeout/cancellation context. Existing Ruby creation/slug
EX locks and Go message/team runtime SH/operation locks remain: conflicting work
on the same session cannot proceed; a different session remains usable.

Package selection/switch/rollback and the existing narrow host recovery caller
retain generation **EX** and all pending-lifecycle checks. They cannot switch the
selected executor while any ordinary SH mutation is running. The source repair
tool's maintenance EX is also unchanged. Do not add a lock bypass to achieve
concurrency.

No new transition-FD protocol is needed. The Go parent can retain SH while passing
its existing fd 3. `workspace-host#inherited_exclusive_transition_lock?` already
rejects that FD as an EX shortcut when a separate SH probe succeeds; ordinary
dispatch then supplies `--transition-lock` and Ruby acquires its own SH. The Go
guard remains held until subprocess exit. A genuinely inherited EX from the
existing recovery owner still follows its validated host path. Never upgrade or
downgrade an inherited open-file-description lock, and never infer authority from
the environment's FD number without the existing ownership/inode/probe checks.

Add one cooperating tracking-Git commit lock in the shared coordination Git common
directory, `dev-session-tracking.lock`, using the existing safe owned-file lock
helper. Its order is generation -> creation/slug -> tracking commit; no reverse
acquisition. Both `commit_tracking_transition!` and `commit_removed_tracking!`
hold it only for current branch/HEAD/index validation, owned-path staging/commit
with normal hooks, owned-path failure reset and post-commit proof. Preserve unrelated
index/worktree bytes. Each waiter reads current HEAD after acquisition.

**Source-backed correction:** `require_linear_workspace_master_for_tracking!`
currently performs `git fetch origin master`. Keep that required refresh outside
the commit critical section; inside, freshly verify shared `master`, cached origin
ancestry, HEAD and staged-path constraints. Do not drop ancestry/fetch checks or
hold this cross-session lock across network, native retirement, worktree cleanup
or cluster work. Normal hooks are necessarily inside the commit boundary. The
dated tool may reuse this Ruby lock owner for its short row commit if needed;
its maintenance EX and external-writer exclusion already prevent normal lifecycle
commits from racing it. Do not add a second tool lock/format or a general Git daemon.

### Real repair: exact preparation and bounded execution

The existing [inventory](real-repair-inventory.json) contains 147 dated rows lacking
manifests, 146 also lacking headers. Main's
[scope inventory](real-repair-scope-inventory.json) divides them into 112 ordinary
Git-evidence rows, 22 needing historical/coordination disposition, three artifact
count failures, one dirty checkout, one duplicate repository name and eight
ambiguous defaults. These are metadata findings, not native absence or apply
results. The source-only corrections below address artificial metadata blockers;
do not discard dirty content or classify historical work as coordination-only.
The existing tool validates at most 128 rows and
validates the whole chosen batch before writing; one blocked row blocks that batch.
Prepare up to two successive batches (128 then the remainder), excluding blocked
rows with recorded reasons and rerunning preview for the reduced selection.
Prepare the second projection after the first batch's commits. Never edit a sealed
projection to remove a blocker. Exclude this active initiative, non-session folders
and all actual writers; no root guessed from prose or current directory names.

Keep separate the tool's exported source-owner revision (`RUNTIME = 0bce6075...`)
and its dynamically selected installed executor. Main confirms that source remains
available and ordinary selection correctly resolves installed `e059...` / `vnx...`;
their different revisions alone are not a preparation failure. However, Main's
later byte-level check supersedes the earlier helper-reuse report: the scratch
main hash `77a5ce...` lacks the selected-socket alias correction present in committed
workspace main `0f5ac987...`, and the old binary refused that alias before a native
request. It is **not reusable**, regardless of its executable hash `063f549d...`.
Build the existing helper from the reviewed current workspace sources against the
final committed R's exported module; update the tool's explicit R pin/guide and
record actual full source/module/executable hashes. Use the existing build commands,
not a new package. Prepare fresh context/projections with actual installed
generation/token selection. Preserve the logical socket/public ledger path and
selected Codex 0.160.0. Never change coordinates under unfinished recovery.

**Dirty checkouts are not metadata blockers.** The existing archive owner already
offers `ArchiveCleanup#discover(clean: false)`. Use that read-only mode in the
source utility's initial evidence and every inventory recheck. Keep real `dirty`
booleans in the projection; use a narrow source-local shape check accepting either
boolean, because the installed cleanup-sidecar `discovery_shape?` deliberately
requires false. Do not weaken that installed validator or coerce dirty evidence
to false. Registration/common-dir/admin/checkout identity, HEAD, branch and retained
ref checks stay exact. Do not call cleanup/prove/remove, stash/reset/checkout,
stage or commit project files. The held writer window and read-only before/after
Git status/diff evidence establish that the dirty checkout was preserved; the
ordinary later archive still refuses it until its owner resolves the dirt.

**Artifact bulk is preserved, not rewritten.** `Evidence#snapshot` currently
embeds every file's Base64 bytes, caps files at 512 and rejects artifacts above
8 MiB; `expected_blobs`/`commit_row` also treat the entire tracking tree as commit
payload. Main's [bulk inventory](real-repair-bulk-inventory.json) records 10,550
files / 325 MB for nixos26.05, 2,467 / 473 MB for conntrack and 1,329 / 5.3 MB for KB.
These rows must remain repairable without deleting or embedding their artifacts.
For the dated tool only, retain bytes for `plan.md`, `state.md` and existing
`portal.yml`; store all other unchanged regular artifacts as path, identity, mode,
size and streamed SHA256 evidence, with no embedded payload. Keep directory/path
ownership and no-symlink checks. Remove the 512-entry and per-artifact 8 MiB caps;
the existing bounded 32 MiB evidence envelope, metadata-file limits and <=128-row
batch limit remain. Split a large batch if its metadata exceeds the envelope;
do not require removing artifacts. Hash before/after an open-file stat check so
an actively changing file does not supply a stable snapshot.

Only `state.md` and `portal.yml` may be written, staged or committed by repair.
Change the source tool's commit pathspecs and committed-target check to those two
files, and preserve the exact tracked/staged/untracked state of all other paths.
The artifact listing, identities and streamed hashes must still agree at the
existing filesystem barriers; unknown/missing/replaced/changed artifacts refuse.
Keep full tracking backups independent of the compact projection. An artifact
never needs restoration from the recovery file because this utility never writes
it. Refresh old unapplied projections; no real apply has consumed the old source
snapshot format, and disposable source-test state creates no runtime compatibility
owner. Keep ordinary archive journal/sidecar formats untouched.

**Defaults and names use the existing mapping.** For each `(project, branch)`,
`default_branch` selects one actually discovered structured/symbolic-ref candidate,
not whichever makes merge proof easiest. Resolve the eight ambiguities explicitly;
do not rewrite repository HEAD/origin refs. For duplicate display/registration
names, give each existing distinct branch obligation a unique valid `name`, retaining
both `(project, branch)` identities. If an actual current checkout supplies its
registration name, preserve that binding and rename the other historical obligation.
Reject an unmapped conflict rather than dropping a row. These two cases need no
new schema or runtime owner; the tool already supports the mapping fields.

**Historical scope gap, minimal source-only correction.** `Evidence#repositories`
currently groups only manifest/ref/worktree discoveries; `mapping.repositories`
cannot introduce a missing registration. Extend that existing array with optional
`historical_commits: [FULL_SHA, ...]` evidence for a reviewed additional registration.
No new mapping file, runtime field or inference from prose is needed. Main's row
`rationale` identifies the old note and why the exact project/branch/commits belong
to it; that note's original bytes are already sealed in the tracking snapshot.
The tool verifies each full commit exists in the canonical project's Git object
store and is reachable from the chosen real retained ref. Normally that is the
named existing local/cached-origin branch. For an explicitly reviewed deleted
historical branch, retain its exact missing branch name as an obligation and use
its real commits' reachability from an existing default/other retained ref only
as retention evidence; it does not recreate or discharge the missing obligation.
Seal present ref/head and explicit missing ref values, canonical origin/common-dir
identity and commit evidence in the existing projection proof.
Recheck at preview/apply/recovery boundaries. Reject unused mappings, contradictory
project/origin/branch evidence and unreachable/non-commit SHAs. Do not fetch or
create refs, and do not use object existence alone as proof of session ownership.

Union these reviewed additions with all automatically discovered obligations;
they cannot replace a missing known feature obligation with another branch.
An actual direct-master change, such as Main's reported bot `6db629e...` example,
can explicitly register its genuine existing `master` with that commit evidence
after resolving the full SHA and reviewing scope. The ordinary schema-1 branch
validator and archive proof already support this branch; a detached historical
checkout is not recreated. Omit unknown `initial_base_sha`; active repair still
has no `final_head_sha` or completion claim. Its later ordinary archive must prove
the exact then-current registered branch published/merged and unchanged under the
existing gates. The historical commit remains maintenance evidence, never an
invented initial base or exemption. If a known feature ref vanished, keep its
obligation and later archive blocker; that absence alone need not prevent writing
honest metadata. Do not silently substitute current master. Main's
[historical excerpts](real-repair-historical-scope-excerpts.json) illustrate the
distinction: actions-checkout records a direct-master commit; github-event-verbosity
records real feature work and explicitly deleted branches; vpsadminos-ci-logs
records a removed detached investigation and explicitly no source changes.
These are review leads, not automatically verified Git or completion proofs.

Genuine notes-only/read-only investigations may use the existing reviewed
`coordination_only` decision when there is no produced/retained repository
obligation. Its rationale must say that, rather than claiming no repository was
ever inspected. Actual source edits, uncommitted work or deleted historical
features require repository mapping; absence of refs is not coordination-only.
For direct edits to the coordination workspace, record project `workspace` and
the real master/commit evidence. Its `refs/heads/master` necessarily advances
through repair's own normal-hook tracking commits: permit only the exact chain of
recorded repair commits from the sealed head, validating parent, message and the
two intended metadata paths with the existing recovery commit proof. All other
ref drift still refuses. This same bounded own-commit chain permits final/retry
checks of earlier rows after later rows have committed; do not require every
earlier row's commit to remain HEAD, and do not accept arbitrary ancestor commits.

### Ordinary negative discovery: bounded native index and saved headers

Main accepted this ownership split; performance acceptance remains measured.

This supersedes the proposed source-only batch scan/longer-timeout workaround.
The [fresh helper result](followup-native-proof-result.json) reports an 11-second
build from current helper sources against `0bce6075`, followed by a real negative
proof failure after 62 seconds. Its binary is
`/tmp/archive-followup-native-proof-2026-10-05/threadless-proof`, SHA256
`ce7911738e5390cb23e003763ebad7598dbd5635fbf85c73443e7ba20795bdbe`.
Do not repeat that full scan for 147 rows. The same owner serves ordinary
threadless observation/automatic archival, so repair-only bypasses would leave
the worker broken.

Main's [saved-header inventory](real-repair-saved-rollout-inventory.json) found
3,833 saved JSONLs, 3,832 indexed, one unindexed, zero read/parse failures and zero
selected exact-CWD matches. The unindexed ID `019cadcc-f98c-7332-b7b8-c34f8e8ccbab`
has positively different CWD `/home/aither/workspace/confctl`. This disproves generic
index completeness, but does not require adopting/indexing that unrelated record.
Runtime proof must freshly establish scope; it cannot trust this saved inventory.

Keep the existing exported `RequireThreadlessConversations(ctx, client, cwd)` as
the common owner and its public directory submission checks before/after discovery.
Replace its slow saved-list portion through one concrete client method,
`RequireSavedConversationAbsence(ctx, cwd) error`, added to the local
`ThreadlessObservationClient` contract. That method owns the following two
complementary sources. `LoadedThreadIDs`/`ReadThreadMetadata` and their existing
exact-CWD/identity validation remain the third source; a loaded-only same-CWD
thread still blocks. No caller supplies a "complete" flag or prior inventory.

1. **Fail-closed public native index.** Do not use a bare empty
   `useStateDbOnly:true` response as absence. Selected 0.160
   `rollout/src/recorder.rs:list_threads_with_db_fallback` turns unavailable DB
   into empty through `unwrap_or_default()`. Instead use the existing public
   project partition: completely paginate `project/list`, then query `thread/list`
   for unassigned `projectId:null` and every returned project ID, with exact CWD,
   active then archived, explicit `ArchiveDiscoverySourceKinds()`,
   `modelProviders:[]` (all providers), ascending order and limit 1. These explicit
   project selectors enter `thread-store/src/local/list_threads.rs`'s direct
   `list_threads_db(...).ok_or_else(...)` path, which propagates unavailable/error
   rather than returning false empty. `local/projects.rs:list_projects` likewise
   requires state and propagates errors. Use public `Request` and local typed
   responses; no codex-web change or private SQLite read is needed.
2. **Saved files missed by the index.** Walk only the selected actual Codex home's
   `sessions/` and `archived_sessions/` trees and inspect the first `session_meta`
   record of each saved rollout, never its turn history/body. Reuse/extract the
   existing `archive_proof.go:readArchiveHeader` strict duplicate-key, newline and
   1 MiB header boundary and existing filename/ID/path validation. Require a real
   canonical CWD; a matching header blocks, a verified different CWD is harmless.
   This catches unindexed imports regardless of source/provider and preserves the
   known unrelated unindexed record. Unknown/malformed/unreadable scope is unknown,
   not an omitted record or successful native proof.

For each native response require present non-null `data`, valid unique project
IDs, bounded nonrepeating cursors, and complete project pagination. Any thread hit
or cursor on a limit-1 scope query blocks absence. Re-list project IDs at the end
and refuse observed membership drift; no retry loop inside the proof. Cap work
with the existing observation context and a finite page bound; bounds/timeouts
produce unknown. This costs two indexed queries per project plus the unassigned
partition, rather than scanning all saved event bodies per session. Do not add a
new background project registry/cache. The selected local server's ordinary
project-assignment invariants provide these exhaustive partitions; unsupported
stores/API responses remain unknown.

Bound actual work explicitly: project pages of 100, at most 64 pages per enumeration,
and at most four in-flight indexed scope queries, all within the caller's existing
deadline/cancellation. Do not spawn one unbounded goroutine per project or retry
a failed partition. The two project enumerations and actual loaded reads also use
that deadline. Exceeding a bound is unknown, not a truncated complete list.
Selected project count P and loaded count L are **not known in architect evidence**;
3,833 saved files is not either count. A proof entails `2*(P+1)` partition queries,
both paginated project enumerations, loaded enumeration/metadata reads (roughly
L metadata calls), public submission reads, and the bounded header walk. Compressed
fallback reads are additional. Repetition at the tool's row/file barriers multiplies
this cost; no claim that it is fast enough follows from choosing indexed queries.

The header walk validates real owned directories/files and rejects symlink or
replacement tricks; missing saved roots may be empty only when positively absent.
Record directory entry sets and file identities for the pass and recheck them
before accepting, so new imports, archive moves or replacement cause unknown.
Normal append-only turn bodies must not invalidate an unchanged metadata prefix;
do not use ctime as thread identity/activity. No persisted header index or cache
is introduced. A process may reuse parsed headers during that same proof after
identity/prefix checks; each new observation/retry rediscovers the directory set.

Selected 0.160 also supports `.jsonl.zst`. If a plain sibling exists, use the native
owner's plain-first convention. For a compressed-only saved file, obtain exact
ID/CWD/path through public `ReadThreadMetadata` and verify it refers to that same
saved file (allow only its native plain/compressed sibling spelling), rather than
adding a decompressor/private parser. Native read errors, unknown scope or an
unsupported file representation refuse absence. Do not silently skip compressed
imports. A malformed or missing-CWD plain header may use the existing exact native
metadata owner only if identity/path can still be established; never infer CWD
from its filename, enclosing date directory or a previously cached inventory.

The final absence claim is the conjunction of native indexed scope, saved-file
scope, actual public loaded scope and resolved directory-operation proof. Reuse
the existing final rechecks and typed `activity_unknown`/submission failure handling;
the subsequent successful observation starts fresh grace as before. It is still
sampled proof, not exclusion of every possible external writer. Ordinary session
and generation locks, and the real repair's continuously held writer window,
retain their existing roles.

**Import/restore compatibility:** raw/copied old JSONL need not be indexed to be
noticed. A same-CWD import blocks threadless readiness until its ordinary owner
resolves it; an unrelated readable header does not block the workspace. Restoring
a whole Codex home/DB or replacing files must happen through the existing stopped
writer/selected-home procedure, then obtain fresh proof; inventory from before
restore is unusable. This reader never imports, resumes, repairs, archives or
adopts a thread. Unavailable native DB/unknown compressed or malformed input remains
an actionable blocker, never an excuse to delete it. No installed migration state,
completion marker or upgrade dependency is added.

Implementation belongs after the concurrency unit: `discovery.go`, a small local
saved-header reader reusing `archive_proof.go`, the concrete client method and
focused tests/ordinary docs. Update existing source helper to compile against
that final R and keep calling this same public owner. Preserve per-row native
rechecks at the accepted boundaries below and all existing recovery phases; the
obsolete batching/deferred-complete proposal above has no implementation
requirement. Do not introduce another CLI.

Focused cases: unrelated unindexed header passes; same-CWD unindexed/plain or
compressed file blocks; malformed header/file-set drift is unknown; empty/unavailable
native DB cannot pass; assigned and unassigned project hits block; project cursor/
membership errors, loaded-only hits and submission residue block. A large saved
file with a small valid first line must read only that bounded prefix. Assert no
scan-and-repair `thread/list` calls and no whole-body reads. Main repeats the fresh
installed negative pilot and ordinary worker observation after review, records
actual timings, and proceeds with the prepared batches only after successful proof.
No full acceptance matrix or 147 repeated timeout experiment.

Main's successful final source-native pilot was reported at **about3.5seconds
per complete absence proof** (exact wall timing was not captured), with stored/native ChatGPT checks passing before and after.
That measurement plus the tool's deterministic call sites (eight full
row proofs plus its all-row preflight) is sufficient to select the following **accepted,
source-only** reduction. Running the obsolete slower tool on a real row is not a
prerequisite. Main measures a representative row using the final coalesced tool,
recording full-proof counts and elapsed time; retain available P, L and query/read
counts from the ordinary pilot/worker evidence. No final row timing is claimed yet.

Keep the existing all-row full-native preflight. Extract/reuse the local portion
of `Proof.sample` at ordinary `barrier` calls, and retain a fresh full sample at
`apply_row` entry before any mutation and after commit/grace before recording
`complete`. The entry proof applies to every unfinished retry, including one
already at `files_written`, `tracking_committed` or `grace_started`. These are two
full proofs per mutating row in addition to its unchanged all-row preflight;
preview remains unchanged. Every intervening barrier still checks current
context/generation, continuously held masked/external-writer window, exact
tracking/artifact identities, refs, authority/roster and owning receipt evidence.
Do not represent a previous native sample as newly observed evidence.

Window loss stops writes and requires fresh proof on retry. No proof permission
is shared across rows, processes or retries, persisted in projection/recovery, or
used to change ordinary runtime cadence. Keep existing phases and once-only
grace. A failed final proof leaves the row unfinished and retryable; only a
successful final proof permits `complete`. A genuinely completed reapply keeps
its existing no-op behavior, never certifying an unfinished row retroactively.

Focused existing tool tests must count one full all-row preflight plus two full
row proofs for each successfully applied initially incomplete row, independent
of its file-barrier count. Assert local checks still run at every barrier; injected
context/window, artifact/ref, authority/roster or receipt drift must stop the next
write or completion. Entry-proof failure writes nothing for that row; final-proof
failure cannot mark it complete; each unfinished retry repeats both row proofs
without restarting grace. Include two rows and retries from existing phases to
prove no cross-row/retry reuse. Main releases source work after the current batch
freeze, selects focused checks and any warranted same-reviewer General/Risk
follow-up, then measures the final representative row. No new schema, recovery
phase, installed behavior or verification framework is required.

### Prepared mapping disposition

Architect reviewed the shape and explicit choices in Main's
[147-row draft](real-repair-mapping-draft.json): unique selected slugs, 15 reviewed
template/read-only `coordination_only` scopes, seven historical repository scopes,
eight default choices, and three distinct merge-branch names for replace-backups.
These choices fit the preceding mapping contract; Main's canonical commit/ref and
remote-HEAD verification supplies their reported Git evidence, not a new check
performed by architect. Preserve all ordinary discovered obligations in the union.

For github-event-verbosity, the mapping records actual configuration commit
`53192f7871db7b035b8eb70fbb3bc51670f3e6a8`, corroborated by Main against the independent
short SHA, subject and origin/master ancestry. Keep the incorrect expanded SHA in
the original prose unchanged, with the correction explicit in mapping rationale;
do not silently rewrite history or invent a base. Both deleted feature refs remain
registered missing obligations despite retained commit evidence. The unusual
origin-HEAD defaults are explicit existing remote choices, not changes to refs.

The 147-row draft is a master review document, **not a valid direct --mapping input
for a <=128-row batch**: the current parser also requires every mapping row to belong
to that exact selected batch. Main produces immutable batch-specific mapping files
by selecting the corresponding draft rows, preserving schema/workspace and each
decision/rationale unchanged. Preview each exact subset afresh. Do not hand-edit
the sealed projection, feed all 147 mapping rows to a partial batch, or treat the
draft's null roots as completed native absence proof.

Main prepares one mode-0600 `REPAIR_LEGACY_CONTEXT` and private evidence/recovery
directory outside selected tracking, on the same filesystem. Use the exact schema
and build commands in `docs/maintenance/repair-legacy-sessions-2026-10-04.md`.
Obtain its `runtime` group from the actual selected registry/profile owner, not a
fixture or remembered path. This is the existing source-only preparation call
(run by Main after source selection is reconciled, with its real operator environment):

```sh
ruby - "$TOOL" "$WORKSPACE" "$R_SOURCE" > "$EVIDENCE/selected-runtime.json" <<'RUBY'
load ARGV.fetch(0)
runtime = LegacySessionRepair20261004::Runtime.new(ARGV.fetch(1), ARGV.fetch(2), ENV.to_h)
begin
  puts JSON.pretty_generate(runtime.selected_coordinates(ENV.to_h))
ensure
  runtime.close
end
RUBY
```

Here `TOOL` is the reviewed absolute workspace `bin/repair-legacy-sessions-2026-10-04`
path, `WORKSPACE=/home/aither/workspace/ai/vpsfree.cz`, and `R_SOURCE` is this
initiative's canonical runtime worktree. Set `umask 077` first. Populate the existing
context `helper` hashes and `maintenance_window` fields; preserve the real HOME,
UID, Codex home, socket, state/authority, profile generation/token and transition
lock returned above. Applicable `DEV_*` values must agree. This call exports
committed owners to disposable scratch and reads selection; it does not register
a workspace or alter its profile. Context and logs contain coordinates, no copied
credentials or private thread contents.

Before apply, Main owns a maintenance window from an operator process **outside**
the portal unit being stopped. Resolve the exact registered workspace name from
ordinary registry evidence and record prior unit states. Stop that instance's
`workspace-auto-archive@NAME.timer`, then its `.service`, then
`workspace-portal@NAME.service`; Main's prepared exact-instance runtime masks can
hold these exclusions against restarts. Retain the selected native Codex service for public
read-only proof. Do not stop other workspaces, tmux or this session as cleanup.
Disable/exclude operator-managed external CLI/team/Git writers through their
actual owning processes and retain that exclusion after interruption. No assertion
in a JSON file proves their absence.

For each exact unit, record a fresh, error-checking verifier in the context's
existing `verify` argv, equivalent to the following; use the actual absolute
`systemctl` and shell paths and each recorded unit name:

```sh
state=$("$SYSTEMCTL" --user show --property=ActiveState --value "$UNIT") || exit 1
test "$state" = inactive
```

Verify both timer and worker, plus portal, at every existing tool boundary. Keep
the timer stopped and prohibit manual restarts throughout the window. Where Main
uses a runtime mask, also freshly require that exact unit's `LoadState=masked`.
After successful recovery/postchecks, remove only masks created for this window
and restore recorded prior unit states; never enable an originally stopped timer.
Also record
fresh concrete external-writer checks and the operator/crash-hold method; empty
checks or an unavailable user bus are not exclusions. If a writer cannot be
identified/excluded, keep its row blocked. Native positive root/team or negative
threadless/submission proof still runs through existing owners under maintenance
EX. It is not a substitute for excluding other processes that can start new work.

Back up exact selected tracking bytes, shared HEAD/index/worktree evidence, holds,
ref/obligation evidence and context/mapping/projection before mutation. Use one
recovery file per batch. Commands stay the existing interface:

```sh
args=()
while IFS= read -r slug; do args+=(--session "$slug"); done < "$BATCH_SLUGS"
"$TOOL" preview --workspace "$WORKSPACE" --runtime-source "$R_SOURCE" \
  "${args[@]}" --mapping "$MAPPING" --json > "$PROJECTION"
"$TOOL" apply --projection "$PROJECTION" --recovery "$RECOVERY"
```

Omit `--mapping` only when existing evidence is unambiguous. Explicit reviewed
threadless/root/repository decisions use the current mapping format. Inspect every
row's blockers even when preview exits zero. Main supplies the tool's ordinary
confirmation only after the window checks pass. After interruption, preserve or
re-establish the same exclusions and use the same apply/context/projection/recovery;
do not delete receipts, reset tracking or make a new projection over partial apply.
Complete all post-commit/proof checks before restoring prior portal/worker/timer
states. A restored portal then uses ordinary refreshed snapshots; Main performs a
fresh ordinary worker scan and reports repaired, archived and still-blocked counts.

The two failed browser requests, `2026-10-03-infra-monitoring` and
`2026-10-03-newadmin-exception`, have no accepted archive journals and remain with
ordinary retry/fresh confirmation. Their unresolved receipts exclude them from
repair overwrite. `2026-10-03-newadmin-http-check` and
`2026-10-03-api-specs-optimization` are already archived; do not repeat them.
All other repaired rows retain holds, exact refs/obligations, prose, honest unknown
bases and once-only fresh grace; ordinary 1/7/14-day policy decides any later
archive. Nothing here authorizes bulk abandonment or fabricated completion.

Retained archived/revivable records and incomplete tool recovery still appear in
the existing removal inventory. Fixing these active rows does not prove that
inventory empty. Keep the source-only tool/procedure until its explicit supported
restore/import/revival and unfinished-recovery removal criteria are satisfied;
no date-based extension and no installed migration reader.

### Focused verification, review and rollout

Use the existing Go/Ruby/browser harnesses, deterministic blocking channels and
owned temporary locks/Git repositories. The quick regression is deliberately small:

- Stall archive after it acquires its generation/session guard; cached operation
  status and warmed index responses finish within one second. A second session's
  ordinary message/admission remains usable; the same session stays serialized.
- Reconciliation under EX generation contention returns cached stale data, does
  not mark the receipt failed, and does not hold `operationMu`. Retry/dismiss/new
  attempt during a delayed read cannot be overwritten by its old reconciliation.
- Fast polls perform zero full scans; one full refresh coalesces concurrent demand
  and reads pending progress once. Failure/backoff and old `generatedAt` cause no
  tight loop. The dedicated overview and fresh pre-journal confirmation work;
  expected missing journals and replacement targets still refuse adoption.
- Ordinary CLI plus portal lifecycle acquire SH through real host/Ruby dispatch;
  two different-session operations can overlap. Package EX waits for both, stale
  generation/token callers refuse, and validated inherited EX recovery remains
  EX. Preserve existing same-session message/team/creation conflict checks.
- Two short tracking commits serialize and each uses fresh HEAD, normal hooks
  and owned paths. A hook failure preserves unrelated staged/worktree content.
  A stalled fetch occurs outside the tracking commit lock. No force/ref deletion.
- Run affected existing source-tool/helper tests after the bounded tool changes: context/source
  mismatch, logical socket/ledger selection, selected receipt blockers, once-only
  recovery/grace and unchanged refs/prose/unknown bases. Add focused historical
  mapping cases: real direct-master commit adds scope; nonexistent/unreachable
  commit, unused mapping or replacement of a discovered obligation refuses;
  known missing historical branch remains registered and later archive-blocked.
  Verify dirty checkout bytes/index unchanged, hash-only bulk beyond 512 files
  and 8 MiB, and commits touching only state/portal. Check two-row interrupted
  repair with own master commits and fresh ordinary native proof on retry.
  The ordinary negative-discovery cases are specified in its addendum above.
  No new native-fixture matrix or mandatory helper rebuild for unchanged inputs.

Commit all substantive source/docs/tests and pass affected quick checks before
retained independent final review; include this concurrency contract and complete
final branch history. Keep only exact reviewed coordinates/generated locks in the
mechanical tail. Main then runs the relevant package build and deploys the matching
user-profile application and host code under the accepted deployment procedure,
preserving current extension/sibling selections. No system application pin or
Codex upgrade. Do not await CI. Use a policy watcher only for required long work.

Main checks real status/index latency and short CPU samples during the two ordinary
retries, observes other-session responsiveness, runs the approved repair window
and fresh worker, and records outcomes. These focused checks replace the historical
acceptance matrix as this follow-up's gate. Unexecuted no-model fixture coverage
remains an honest limitation, not a deployment blocker. Existing pending-journal,
generation and package preflights still apply; deployment approval does not waive
them. Persisted schemas are unchanged; restart drops display caches only, preserves
receipts/journals and permits their ordinary recovery. Rollback uses the supported
host/profile transition, with no live mid-operation downgrade or private-state edit.
Main owns exact final-head integration under the user's existing approval.

## Scope and evidence

Implement the accepted [plan](plan.md). A clean, merged session must use the
ordinary CLI or browser archive action even with nested integration checkouts,
detached auxiliary checkouts, a retained team, or interrupted retirement. Preserve
the 1/7/14-day policy and Keep open. Add useful workspace diagnostics. Repair
historic inputs with a separately reviewed, source-only maintenance utility;
ordinary runtime behavior must not depend on that tool or its recovery file.

Initial source inspection confirmed these causes (historical pre-implementation
evidence; the follow-up above starts from the implemented runtime):

- `libexec/dev-session` discovers immediate children containing `.git`, requires
  attached HEAD, and rejects other children before proving repository heads.
- Archive schema 2 has an exact key set and seals the projected tracking tree,
  retained root, and registered heads. It has no auxiliary cleanup inventory.
- Archive calls root retirement before team archival. The normal team archive
  path can recreate fresh members; `ArchiveRetainedAll` already avoids that.
- `workspace-host` discards the environment returned by `dev_session_invocation`
  on exec paths. Narrow recovery hard-codes 0.155.0 and requires an already
  archived root, excluding the recorded 0.160.0 incident with an active root.
- Browser lifecycle target identity includes tracking-directory ctime.
- `ObserveThread` uses `thread.updatedAt`; automatic proof errors set `reset_at`,
  and the fingerprint includes error messages and runtime authority identity.
- Schema-1 manifests already permit absent initial bases while active, but both
  finalization validators require a base as well as a final head.

The [incident note](../../notes/dev-workspace/2026-10-04-team-archive-root-retirement-order.md)
provides the team/dispatch evidence. The coordinator's read-only investigation
reports 146 front-matter-blocked records without manifests, 124 with exact-slug
retained branches, clean auxiliary heads reachable from cached origin/master,
and settings events newer than actual turns. These counts are input evidence,
not an authorization list or a permanent migration rule.

## Boundaries and files

| Owner/repository | Intended surface |
| --- | --- |
| dev-workspace lifecycle | `libexec/dev-session`; a focused `libexec/workspace-archive-cleanup.rb` for inventory, proof and sidecar validation; corresponding Ruby tests |
| dev-workspace host | `libexec/workspace-host`, `test/workspace_host/{commands_and_locks,archive_recovery}_test.rb` |
| dev-workspace Codex adapter | `portal/internal/workspacecodex`, `portal/internal/teamruntime`, `portal/cmd/workspace-portal/main.go` |
| dev-workspace browser/status | `portal/internal/web/{server,operation_state,auto_archive}.go`, templates, `static/app.js`, existing browser test harness |
| dev-workspace retention | `libexec/workspace-auto-archive.rb`; keep semantic retention and status, remove installed migration dependencies |
| dev-workspace normal record readers/readiness | Ruby and Go manifest/finalization validation; ordinary creation-less retained readiness across observation/start/revive/interaction; repository comparison fallback for unknown bases; raw producer refusal |
| dev-workspace docs/package | `docs/dev-sessions.md`, `docs/workspace-portal.md`, a linked `docs/session-archive-recovery.md`, `nix/workspace-portal.nix` and focused protocol fixtures |
| workspace feature worktree | Source-only `bin/repair-legacy-sessions-2026-10-04`, focused tool fixtures, dated maintenance instructions; `docs/agent-instructions/{lifecycle,sessions,git}.md` and affected instruction tests; lead-owned package selection |
| vpsfree-dev-workspace | Preserve the already consumed extension; no owned source/pin change under the accepted nested-runtime composition |

No codex-web modification is needed. The current merged baseline pins
`v0.0.0-20261004200036-3d07cf60cfde`; its Go client is unchanged from the initial
`32775fa7fdd9` selection and exposes `Request`,
`ReadThreadMetadata`, `ListThreads`, prompt/queue readers and
`RequireSubmissionAttemptsResolved`. Use those in the local adapter. Keep Codex
0.160.0 and the dependency direction workspace -> extension -> runtime -> client.
Do not expand delete's force semantics or rewrite its existing removal journal.
Shared inventory primitives may be extracted, but archive's new allowances must
not implicitly change delete, worktree-add or worktree-remove behavior.

The 2026-10-05 selected-baseline reconciliation is
[design-current-baseline-result.md](design-current-baseline-result.md). Before
final source review, preserve merged runtime `3edc605d` and workspace `88a75655`
and later merged advances through the lead's clean final rebases. They include
deployed 50-file upload/preparation support and the already landed nested-runtime
declaration. Retain
client `3d07cf60` and the sibling input graph. That report's extension `cd81e83f`
was the then-selected baseline; the lead's subsequent shared-default observation
includes already-merged extension `77dd0d04`. The lead's consumer refresh preserves
that newer selection; do not restore the historical extension pin. Initial
`6a972b9`/`e5ba1912` and package `s7y4bgq…` remain historical checkpoints, not
current selection or rollback targets. The `profile-85-link` / `jq982nq…` selection
is historical; `3fzif056…` was Main's later checkpoint, not a current selection
assertion. At that checkpoint Main had completed the
workspace rebase to `a8fee24807f85cadd9245a25a89df625714e4519` over `4df3b7c`, composing
extension `77dd0d04` / runtime `6c110be5` with all 23 input nodes/edges preserved.
These are reported checkpoints, not a new action or pin change by this design.
No new protocol/schema or archive behavior was needed for that baseline change.
Current action scope and verification are set by the approved follow-up above;
Main's state/rollout evidence owns current selection and final heads.

The trusted local operator is the runtime's existing boundary. Handle ordinary
wrong paths, identities, concurrent edits and interrupted operations; do not
design a new defense against a malicious host administrator. Remote portal
clients remain untrusted.

## Archive invariants

1. Every registered feature obligation survives removal of its worktree. Complete
   mode proves the exact local and, where required, remote feature head merged
   into its configured origin default branch. Squash equivalence is insufficient.
2. No checkout is removed without a clean-state check, verified Git registration,
   stable directory and worktree administration identity, and retained reachability
   of its exact sealed HEAD. No archive path uses force, deletes refs, prunes Git
   administration, creates rescue refs, or recursively deletes arbitrary files.
3. Abandoned mode skips merge/publication proof only. It still preserves detached
   commits through existing retained refs and enforces identity, cleanliness,
   idle/submission, tracking, and generation checks.
4. Once cleanup is sealed, additions, replacements, branch/HEAD changes and
   unexpected files refuse retry. An absent checkout is accepted only after
   proving both its directory and its Git registration absent.
5. The root and all retained member identities come from verified manifest,
   authority and roster state. Unknown same-directory threads are never adopted,
   archived or treated as team members by an archive operation.
6. New inactivity uses semantic activity, not administrative metadata. A safety
   blocker never supplies evidence of completion or inactivity.
7. A browser retry is bound to the accepted journal or the same confirmed session
   target; it cannot silently move to a replacement bearing the same slug.
8. Ordinary manifests register exact retained identity and repository obligations.
   Repair establishes that metadata without declaring work complete or inventing
   creation/goals, original bases or active history. Runtime readiness depends on
   ordinary identity/activity proof, never a durable migration receipt.

## Git inventory and proof

### Discovery

Enumerate canonical `repos/*.git` common directories and the shared workspace's
common directory, deduplicating permitted canonical aliases. Read each using
`git worktree list --porcelain -z`. Select registrations whose normalized absolute
path is strictly below `worktrees/<exact-slug>/`, with a component boundary. This
finds `integration-targets/<project>` and detached checkouts. It must not match a
slug prefix, another group, the bare repository, or the shared root checkout.

For each candidate, validate canonical common-dir ownership, non-symlink path
components within the group, repository toplevel equal to the candidate, and
agreement among `.git`, resolved `--git-dir`, `--git-common-dir` and the porcelain
registration. Record relative path, project, canonical common dir, worktree
admin dir and their dev/inode identities, checkout dev/inode, HEAD, attached
branch or explicit detached state. Do not use ctime as identity. Reject locked,
prunable, missing-but-still-registered, duplicate, foreign or overlapping
registrations. A checkout nested *inside another checkout* is an overlap, not
an ordinary integration-target container, and remains unsupported.

Walk only the group/container levels outside accepted worktree roots. Every
nonempty subtree must lead to a discovered checkout. Refuse symlinks, plain
files, foreign/unregistered repositories and unknown directories; do not infer
ownership from a directory name. Allow empty plain container directories and
seal their identities. After removal, remove verified empty containers deepest
first using `rmdir`; an added file causes refusal. Never traverse or clean a
worktree's contents as part of container cleanup.

Use one inventory value for archive preflight, automatic eligibility, cleanup
and diagnostics. Keep portal repository cards as feature registrations; nested
paths are not new card names and must not be squeezed into `SAFE_PART` names.

### Obligations and retained refs

Build the union of manifest registrations and independently discovered attached
feature branches. Matching is by canonical project/branch and expected path,
not by a basename that may repeat in nested containers.

| Checkout/obligation | Complete | Abandoned |
| --- | --- | --- |
| Registered feature, with or without checkout | Existing exact local/remote feature and default ancestry proof; retain recorded initial-base exception only when its evidence is present | Keep branch and exact recorded final head; no merge proof |
| Unregistered attached non-default branch | Additional exact branch obligation: require matching origin feature and default ancestry; no invented initial-base exception | Existing shared local branch retains HEAD |
| Attached default/integration target | Exact checkout HEAD must remain the attached branch tip and be ancestor of freshly fetched configured origin default; it may lag that default | Existing shared local branch retains HEAD |
| Detached auxiliary | Exact HEAD must be ancestor of freshly fetched configured origin default; record that ref/tip as retained reachability | Exact HEAD must be reachable from an existing shared `refs/heads/*`, `refs/tags/*`, or retained `refs/remotes/origin/*` commit ref |

An attached checkout for a manifest registration cannot switch to detached mode
to escape its feature obligation. Unregistered branches remain cleanup-sidecar
obligations, not fabricated manifest comparisons. Determine the default from
consistent registered project metadata or the canonical origin HEAD; require an
explicit registration/mapping if conflicting or unavailable. Never guess a
default using prose. Preserve the runtime's existing canonical repository and
origin identity checks, including the workspace special case.

Reachability uses commit ancestry from a named shared ref. Exclude worktree
HEADs, reflogs, `refs/worktree/*`, replacement refs, pseudo refs and arbitrary
unreferenced objects. No new ref is created to make an orphan removable. Report
an orphan with the checkout path and exact HEAD so an operator can deliberately
retain it outside this operation. Abandoned mode can use locally retained remote
tracking refs without fetching; it asserts local retention, not publication.

Seal the chosen proof ref and tip. On retry, an auxiliary retention ref may
advance if it still reaches the sealed HEAD; deletion, rewind losing reachability
or changing the origin/default identity refuses. A registered or additional
feature branch must still equal its sealed exact head locally and remotely as
required by the complete proof. Refresh default/feature refs before complete
proofs using the existing narrow refspec fetches. Network failure blocks cleanup.
Never substitute a later feature head just because it too is merged.

### Cleanup sidecar and schema-2 journal

Keep archive journal schema 2, its exact keys, phase ordering and
`target_tracking_sha256` unchanged. Add private
`worktrees/.locks/<slug>.archive-cleanup.json`, schema 1, maximum 1 MiB,
strict-key/duplicate-key validation, owner-only mode and atomic fsync+rename.
Bound the inventory before starting an operation; no truncation.

The sidecar contains:

- workspace, slug, operation ID, mode, finalized timestamp, projected tracking
  digest and retained root, identical to the journal's immutable fields;
- `sealed: true`, a canonical SHA-256 of the immutable inventory/proof payload,
  checkout records with the identities above, container records, and additional
  feature/auxiliary proof records;
- per-checkout `removed` and per-container `removed` progress, outside that
  immutable digest, and a terminal `completed` flag initially false. No error
  strings or scan times enter the seal. Include the exact projected final-head
  map for registered repositories in either mode, so partial removal in abandoned
  mode cannot lose the data needed to reproduce the projected manifest.

Create the fully checked sidecar first, then the matching ordinary journal,
before quiescing or any irreversible action. An interruption between those
writes leaves a **prepared intent**, not permission to clean: the next matching
archive revalidates the exact tracking projection, inventory, refs, idle state,
mode and generation before publishing the same journal. The normal command asks
for confirmation again if no retained browser/automatic authorization receipt
exists. Never attach an orphan sidecar to a different journal ID. All new helper
mutation/package preflights recognize such an unfinished intent and direct the
operator to the same archive command; read-only status remains available.

Before each removal, revalidate the sealed inventory, exact checkout/admin/common
directory identities, branch/HEAD, retained proof and cleanliness. Use ordinary
non-force `git worktree remove`. Persist progress after each success. If removal
succeeded before the progress write, retry proves absence from both the path and
the owning canonical repository's worktree list, then marks it removed. If an
already removed path reappears, refuse even when its branch and HEAD match.
Refuse stale Git registrations; do not run `worktree prune` to hide them.

On every remaining destructive phase, validate sidecar/journal agreement and
reprove the sidecar's retained heads alongside the existing registered proofs.
This continues after the directory is gone and after tracking is committed.
Project archived manifest hashes only from manifest registrations; auxiliary
records do not change the schema-2 journal's `proven_heads` namespace. Complete
archive with no manifest is supported only after offline repair of its registrations;
do not let an unregistered legacy branch vanish from retry proof.

After recording the ordinary journal's final `archived` phase, durably mark its
sidecar completed before removing the journal, then remove the sidecar. A crash
after journal removal leaves a completed sidecar receipt. Clear it only after
proving the exact committed archive and retained thread/team/runtime retirement;
its durable completed flag supplies the operation result even for CLI operations
with no browser receipt. A sidecar without that flag and without its journal is
a prepared intent only when tracking is still at its exact source projection;
otherwise refuse. It must not start another archive. Any inability to prove
completion remains visible and blocks conflicting mutations.

For an existing schema-2 journal without a sidecar, retain the historical recovery
path and its exact projected tree/head/root checks. Do not adopt new auxiliary
checkouts into that old operation. Pre-move recovery accepts only the old
immediate, attached layout and known manifest obligations; later recovery proves
the recorded archive. Unknown/nested/detached additions refuse. This adapter is
temporary compatibility support, with removal criteria below. New operations
always create the sidecar, including an empty inventory.

External writers must still be stopped before archive. Locks serialize supported
helpers, not arbitrary `git`, editors or native clients. Rechecks and non-force
removal bound the existing concurrency risk; no claim of filesystem-wide atomic
cleanup is made.

## Retained team and host recovery

Before any new archive side effects, prove the root and each nonremoved retained
member belongs to this workspace/CWD and recorded project, is materialized where
required, and has no active turn, prompt, runnable queued input or unresolved
submission. Active/fresh threads keep the full ordinary queue-emptiness proof.
Check active same-CWD discovery against the exact retained set, including when
the root itself is already archived. Unknown threads refuse before cleanup.
Unfinished member creation, replacement or removal remains a blocker.

The shared discovery owner must combine persisted lists with complete public
`LoadedThreadIDs` enumeration and exact `ReadThreadMetadata(ctx, id, false)`
reads. Selected 0.160.0 `thread/list` enriches only its persisted result slice;
it can omit a newly loaded thread before its first turn/persistence. A loaded
same-CWD identity outside the proved retained set blocks even without a rollout
or turn. Verify every loaded ID/CWD before excluding a positively unrelated
directory; unreadable or malformed loaded identity makes discovery unknown.
Union matching identities across saved and loaded results without double-counting
or requiring a valid fresh retained subject to have a saved row. Contradictory
identity blocks; all retained source/project/materialization and idle checks
remain independent. Threadless proof requires both persisted active/archived
absence and loaded absence at that exact CWD. Keep this rule in the existing
shared owner for observation and retirement, with existing final rechecks and
native sampling limits. See [loaded discovery clarification](design-observation-loaded-result.md).

At `tracking_committed`, after exact tracking/heads are revalidated:

1. Run the existing retained-only member archive path. It may reconcile a member
   already archived by App Server before its roster write. It must not recycle,
   create, replace, interrupt or force a member.
2. Prove every nonremoved retained member archived and all submission attempts
   resolved using exact metadata/archived-rollout identity checks.
3. Run ordinary root retirement. Keep its unknown same-CWD refusal and exact
   archived-root recovery; no general relaxation of `RetireThread` discovery.
4. Advance the existing `thread_retired` phase only after both proofs succeed.

An interrupted member list simply resumes the same sequence. A root archive
acknowledgement lost before the journal write is reconciled by exact root proof.
Removed members stay removed. Archived roster state alone is insufficient proof.
Revalidate identities and idle/submission state at the point of retirement as
well as the initial preflight. Preserve the outer 210-second retirement timeout
around the client's 180-second deadline.

For an already archived root/member, use the accepted bounded proof in
[design-archived-idle-result.md](design-archived-idle-result.md). Require exact
retained `vscode` identity and archived rollout, metadata status `notLoaded`,
absence from complete public `LoadedThreadIDs` enumerations, public
`RequireThreadTurnsIdle`, no known prompts and resolved public submissions;
recheck identity, file and unloaded state across the sample. Reuse those existing
client helpers; no second unit-2 turn parser or codex-web edit is needed. Refuse
archived loaded threads even when idle. Native loaded-list omits internal
sessions: this inference must never be extended beyond the verified `vscode`
source. Archive metadata alone does not imply unloaded or immutable history.

Do not call queue/list on the archived-unloaded path: selected 0.160.0 rejects
that read. Archive preserves durable queue rows, which cannot dispatch while the
thread is unloaded but may become runnable on a later resume. This is a proof
of no currently runnable input, not an empty durable queue. Preserve those rows;
unresolved public submissions still block. Do not unarchive, match error text,
parse private queue storage or force retirement to obtain proof. Failure retains
the operation for a fresh exact retry. Rechecks are bounded observations under
existing locks, not an atomic lease against external native clients.

`workspace-host dispatch` must exec the exact environment returned by
`dev_session_invocation` on every branch, as the inherited-lock path already
does. Host-selected workspace/Codex home overrides caller values; keep the
profile generation and inherited-lock checks. No public flag permits arbitrary
runtime roots.

Keep `workspace-host recover-archive --source PATH --workspace NAME --session
SLUG` narrow: exact candidate source, exact selected predecessor, schema-2
`tracking_committed`, matching committed tree/root/heads and unchanged locks,
profile token, runtime contract and selected Codex executable. Replace both
0.155.0 literals with the selected executable's verified version. Run the
candidate's generated protocol checker against that *selected* executable;
accept only a proven compatible generated contract, including selected 0.160.0.
Do not select or upgrade Codex or the profile.

Recovery must accept a proved active idle root as well as an already archived
root. Add a bounded read-only archive-state helper in the local adapter rather
than requiring `thread require-archived` before member retirement. Verify the
same retained set and unknown-thread refusal, archive retained members, prove
them, then invoke the selected ordinary executor with only its portal helper
replaced. Its schema-2 journal is never rewritten by hand. Refuse incompatible
contracts, other phases/operations, and a new cleanup sidecar that the selected
executor cannot honor. Existing no-sidecar incidents are the supported recovery
input. Tests must cover active root, archived root and partially archived team.

Preserve the selected predecessor's actual recovery eligibility, including its
ready-creation gate. Ordinary creation-less readiness below does not relax that
separate executor contract. The removed positive installed predecessor fixture
has no genuine ready-creation evidence and remains unsupported. Fake-server and
owner tests cover recovery logic; do not claim that fixture proves native success.

## Browser target and operation state

Use a versioned target hash over canonical workspace, slug, tracking location
(`work` or `archive`), tracking directory dev/inode and retained root thread ID
(explicit absence for threadless tracking). Exclude ctime, mtime, manifest bytes,
repository lists, settings and artifact membership. This mirrors the existing
repository comparison identity's reason for excluding ctime. A directory/thread
replacement or lifecycle location change creates a different target; adding an
artifact or atomically rewriting `portal.yml` does not.

New operation receipts record `targetIdentityVersion: 2`. Keep the existing
receipt schema readable with an optional additive field. GET operation/session
state includes the current target and version. Browser target state must be
mutable: refresh it with operation reconciliation and settings refresh, without
reloading the document. Update confirmations from that snapshot before sending.
Revalidate on the server under the existing transition gate and again immediately
before launching the helper.

Adoption rules are explicit:

- Same version-2 target, no journal and no missing expected journal: refresh
  status and retry the same eligible pre-journal receipt. A started receipt
  cannot become pre-journal merely because its expected journal is absent.
- A matching accepted journal: its operation ID and immutable journal evidence
  own retry. Directory moves or old target hash changes do not retarget it.
- Different current target without an accepted journal: return structured
  `target_changed`, show the current session summary, and require a new explicit
  confirmation. Do not automatically replay the prior action.
- Old receipt with no identity version and no journal: recompute the old hash
  only to establish a positive exact match. If it still matches, persist the
  version-2 target bound to that same directory/thread before retry. If it does
  not match, it is **unverifiable**, not presumed to be ctime noise: use the fresh
  confirmation path, even if the slug/thread text looks familiar.

A fresh confirmation can supersede a failed pre-journal receipt through its
exact `receiptId`; under lock, refuse if a journal appeared or the receipt
changed. This avoids a reload/dismiss/manual-command repair. It cannot supersede
an accepted or missing-expected journal. Success reconciliation must verify the
receipt's target/operation evidence as well as terminal lifecycle, so a later
archive of a replacement cannot complete the old receipt accidentally. Apply
the common identity rules to archive, revive, delete and Keep open, preserving
delete's stronger force confirmation.

Ordinary archive/revive journals are unlinked on success. New manifestless revival
is refused before mutation under the producer rules below. For a supported older
accepted manifestless revival that creates a fresh root, completion of the owning CLI
invocation completes its browser receipt, bound to that invocation and operation.
If the portal restarts after journal unlink but before durably saving that
result, there is no same-root target proof for the newly created conversation.
Keep the started receipt failed with `missing-expected-journal`; do not adopt
the new root, supersede the started receipt, replay it as a fresh action or infer
success merely from active tracking. This is a supported fail-closed recovery
limit, consistent with the no-adoption table, not a new completion format.

Retained creation/manifest/history evidence may establish the new active session
but does not certify this lost browser-operation result. Offline repair,
its reviewed mapping, active baseline and maintenance recovery file cannot retrospectively
complete or rebind the old revive receipt. Keep its ordinary pending-operation
preflights; repair gets no waiver for this window. A still-present matching
revive journal or durably saved owning CLI result remains valid existing evidence;
once both are absent, the accepted contract supplies no fresh-root completion
proof. New archive cleanup-sidecar receipts are specific to their own operation
and do not supply a general legacy-revive completion certificate.

Unit 3 acceptance covers owning CLI success, restart while the matching journal
still exists, and restart in this unlink-before-result window. The last case
must remain failed across refresh and later repair, without changing its
target or enabling supersession. Ordinary same-root reconciliation and the new
bundle's in-page refresh objective remain unchanged.

These in-page refresh and legacy-receipt rules are implemented by the new browser
bundle. A page already running the predecessor's static JavaScript is not hot
upgraded; it may need a normal reload after a safe stale-target refusal. Preserve
the no-reload objective for a page loaded with the new bundle, including after
artifact additions and atomic manifest edits. Old receipts read by new code and
an already loaded old bundle are separate compatibility cases.

## Actual activity and retention

### Observation interface

Implement `workspace-portal session observe` with host-selected `--workspace`,
`--session-slug`, `--socket`, `--user-state-root`, `--authority-dir` and
`--codex-home`. The command coordinator resolves the exact root and retained
roster, aggregates local workspacecodex observation primitives and supports the
negative threadless proof below. Extend `thread observe` with the same semantic
primitive for existing single-thread callers. Ruby receives one versioned JSON
result for the session, not raw transcript content. Required result fields are:

`schema: 1`, `workspace`, `slug`, `identity`, `activityKnown`, `activityToken`,
`lastActivityAt` (nullable), `idle`, `subjects` (root/member identity and stable
token), and bounded diagnostics with machine code/category/message. Retain the
old `updatedAt` field only as explicitly administrative data for existing callers;
automatic inactivity must never read it.

For each exact thread, verify metadata identity/CWD/source/project, then request
`thread/turns/list` with `limit: 1`, `sortDirection: desc`, `itemsView: notLoaded`
through the existing public `Request`. Validate the selected 0.160.0 generated
shape. Stable activity comprises the latest actual turn ID, status, valid start
and completion boundaries (including terminal failures/interruption), plus the
publicly observed queue/request/client-message identities needed for busy-state
transitions, plus the public submission-resolution proof state. Private unresolved
attempt IDs are not exposed by the pinned client and must not be invented.
Do not hash durations that are recomputed, request poll timestamps, settings,
model selection, names, settings-applied events, or `thread.updatedAt`.

A valid empty turn array is a stable no-turn token, subject to ordinary identity,
materialization/fresh-thread and submission checks. Missing/null data, malformed
IDs/status/times, future times, unavailable history and unverifiable persistence
are unknown, not zero activity. Missing historical timestamps can use a verified
turn ID/status token and observation-based grace; report `lastActivityAt: null`
rather than inventing a date. An active turn, pending request, queued input or
unresolved submission blocks archive. Recheck the latest turn after the idle
checks so a concurrent start cannot be missed. Final exclusive revalidation
remains necessary for native clients outside the portal.

Use existing prompt/queue/submission APIs; never parse the client's private
submission ledger format or clear it while observing. An accepted send becomes a
turn; an in-flight/uncertain send remains blocked by the ledger. Observed queue
or request activity restarts grace on return to idle even if no new turn resulted.
Changes made and reverted entirely between scans remain the documented sampling
limit. This design needs no transcript backfill or full history scan per poll.

Submission proof uses existing `RequireSubmissionAttemptsResolved`. Its success
is a stable resolved condition; every error becomes local typed
`activity_unknown/submission_unverified`, loses continuity and blocks eligibility.
Do not classify error text or claim inaccessible attempt IDs/counts/times were
read. The next successful proof starts fresh grace even if all observable tokens
are unchanged, including after restart. Accepted-send acknowledgement or options
compaction alone is bookkeeping, not activity. The public helper may inspect
history to resolve an outstanding queue attempt; that existing proof is separate
from the bounded latest-turn observation. See
[submission observation clarification](design-observation-submission-result.md)
for the supported state transitions and sampling limits.

Archived retained `vscode` members use the same positive archived-unloaded proof
above, without queue/list. Dormant durable queue storage is uninspected, not an
observed empty queue. The semantic observer still owns latest-turn timestamps,
tokens and drift checks separately from the reused unit-2 idle helper. Do not
treat archival as no activity. Loss of positive unloaded/identity/submission
proof blocks and follows the existing unknown-continuity rule.

Aggregate the root and all nonremoved retained members in sorted identity order.
Observe or prove archived members exactly; a ready roster entry with an already
archived thread can be reconciled through existing identity proof. Unfinished
creation/replacement and unknown member history make the aggregate unknown.
Model/effort/access policy refreshes do not count; changing the retained identity
set does. Fail closed on unknown same-directory threads.

### Fingerprint and grace

Separate `activityKnown`, the stable content/activity fingerprint, and proof
diagnostics. Fingerprint schema/version must be explicit. Include semantic
conversation tokens; lifecycle; normalized repository obligations/actual feature
heads; sealed-style checkout identity, HEAD and clean/dirty state; plan/state and
declared artifact content digests; and meaningful artifact registrations.
Exclude diagnostic strings, checked times, tmux/runtime regeneration, Codex
client version, routine manifest rewrites and fetched default advancement that
does not change the feature obligation.

On upgrade from the old unversioned fingerprint, take one new trustworthy baseline
and start fresh grace. Thereafter preserve the baseline across worker/portal/host
restarts and across unchanged proof failures. Continue to apply these tiers:

| Lifecycle/obligations | Delay | Result |
| --- | --- | --- |
| Explicit complete | 1 day | Complete, subject to normal proofs |
| Active with one or more registered/additional feature obligations | 7 days | Complete, subject to normal proofs |
| Active with no repository obligations and no owned worktrees | 14 days | Abandoned |
| Explicit abandoned | None | Manual archive only |

Auxiliary-only checkouts do not qualify a session for the empty tier; report no
eligible rule until the normal cleanup/registration situation is resolved.

- Content, feature/checkout identity or actual activity changes reset the grace.
  Observed dirty -> clean and busy -> idle transitions reset it.
- Unchanged dirty state, unmerged ancestry, a dirty/missing shared-master commit
  precondition, unknown files or network failure of a merge proof remain blockers
  without resetting an otherwise trustworthy inactivity baseline.
- If a missing ref or inventory failure prevents a fresh *proof* observation,
  retain the last trustworthy fingerprint and mark that dimension unknown; never
  assert eligible from it. When it becomes readable, compare it and reset if
  changed. Do not classify it as conversation activity merely because an exception
  was thrown.
- Unknown conversation/submission activity clears eligibility and records that
  continuity is lost. The next trustworthy observation starts fresh grace. This
  also covers unexplained identity changes and malformed activity output.
- Enabling/re-enabling policy, releasing a hold, revival and offline repair establish
  fresh grace. Preserve holds while translating old root-ID identities to the new
  bound identity when positive same-session evidence exists.

Proof categories must survive Ruby exception handling; remove the current blanket
`reset_at` on all scan/merge errors. Use typed results or exceptions with stable
codes, not matching human error text to decide policy. Every eligible execution
still takes exclusive session mutation locks under the shared generation guard
specified above, and repeats identity, activity, inventory and exact
merge proofs before beginning an ordinary archive journal. Once an automatic
journal exists, only its own operation ID can resume it; disabling does not erase
or replace an accepted operation.

### Verified tracking-only sessions

A missing manifest/thread is not by itself evidence of no conversation. An
ordinary threadless session has a valid schema-1 manifest with explicit
repository/artifact lists and no fabricated Codex or creation identity. Bind
activity to workspace/slug and tracking directory dev/inode. Verify no live tmux
or authority, retained team, pending creation/submission/lifecycle receipt, or
active/archived exact-CWD Codex conversation contradicts that absence. Use the
selected authority's filtered discovery with the complete explicit source-kind
set generated by selected 0.160.0 and shared with unit 2, plus the same owner's
complete loaded-ID enumeration and exact metadata reads described above. Saved
active/archived lists alone cannot establish absence. Omitting `sourceKinds` or
passing an empty array selects only interactive sources and cannot prove absence.
An unavailable or incomplete absence proof means unknown activity.
Cache diagnostic observations only, not permanent permission to skip this proof.
Recheck it before archive.

The executing archive may pass the paired internal arguments
`--expected-operation-id ID --expected-archive-mode complete|abandoned` on the
single observation adapter call so its own accepted receipt/journal/cleanup
intent does not contradict this negative proof. Require both arguments together,
a valid operation ID and the exact existing mode enum; reject orphan arguments
and mismatches with the receipt/journal owner. The mode comes from the validated
archive caller or its loaded/reconstructed journal, not from inference by the
observer. Ordinary scans and fresh manual pre-journal proof pass neither;
ordinary scans observe active tracking only. This is an exact
ownership comparison, not permission to ignore pending state: require canonical
workspace, slug, archive kind/mode, operation ID and the positively accepted
target under the existing generation, transition and session gates. The portal's
`portal_operation_id` binds its validated pre-journal receipt; a retry uses the
fully validated archive journal. An intent supplies an ID only through the
archive owner's existing `cleanup.prepared_journal(sidecar)` reconstruction and
revalidation, before that journal is republished. A raw sidecar ID is insufficient.
A fresh manual archive has no operation ID before preparation and needs no
exception. Never manufacture journal evidence during that pre-journal interval.
Keep read-only receipt/target inspection in the existing Go web owner within
this adapter call; do not add a separate receipt-query subprocess. Strict cleanup
reconstruction, projection and ref proof remain in Ruby. There is no migration
receipt gate or parser in the current design. During offline repair, the
maintenance window excludes all ordinary writers and workers; it supplies no
special receipt exemption to the observer.

After the accepted move to `archive/`, only that owning validated archive retry
may observe the preserved tracking directory and its actual dev/inode identity.
Still prove conversation and submission absence at the original exact
`work/<slug>` CWD. Keep normal journal/target/tree proof before observation; do
not compare a moved target as a fresh browser request or broaden ordinary scans
to archived sessions. The exception covers only matching records of this one
operation. Malformed/unavailable state, another operation/kind/target, a missing
expected journal or contradictory conversation/runtime residue still blocks.
It cannot adopt a root, certify completion or rewrite another receipt. See
[executing archive observation](design-observation-operation-result.md) for the
preparation, retry and conflict cases and the existing owners of each proof.

For directory-bound submission residue, use public
`ThreadOperationAttempt(exactCwd)` on the existing correctly configured selected
authority client. A nonempty binding contradicts threadless status; an error is
unknown submission proof. Never adopt or clear the returned identity. Successful
empty proves only absence of that operation binding and must be combined with
complete active/archived discovery and all other absence checks. It does not
enumerate every private per-thread attempt. Missing/unavailable historical
identity evidence remains unknown; do not certify a lost thread from current
absence alone or require a new global ledger reader. A fully verified ordinary
tracking-only record remains supported without a private ledger-file requirement.

Threadless sessions with registrations can use complete/merged tiers. Only a
verified absence of obligations and worktrees qualifies for the 14-day tier.
Normal archival skips actual thread retirement after the same negative proof;
it must not discover and adopt a conversation at that late phase. Revival clears
grace and preserves verified threadless tracking. It does not create a conversation
as a revive side effect. A later explicit start uses genuine creation evidence
and changes the identity and activity baseline explicitly.

## Workspace diagnostics

Keep `dev-session auto-archive status SLUG --as-is --json`. Add
`dev-session auto-archive status --json` without a slug for a workspace snapshot.
The workspace response is an envelope with `schema: 1`, workspace identity,
policy enabled/epoch, last scan time/result, status counts and sorted `sessions`.
Include active tracking, persisted pending automatic operations even after the
tracking move, and malformed legacy entries that normal session listing omits.
One malformed record yields a row, not failure of the whole response.

Rows preserve existing fields and add stable diagnostics: slug, lifecycle or
unknown, identity kind, tier or none, hold, activity-known and last actual
activity, observation time, idle-since, earliest eligible-at, eligible flag,
blocker codes/categories, last attempt/result/time, journal operation/phase and
whether offline repair is needed. Categories are `activity_unknown`, `busy`,
`worktree`, `merge_proof`, `tracking`, `legacy_format`, `hold`, `policy`,
`lifecycle_pending`, `generation`, and `observation_stale`. Bound error text and
expose no prompts, credential paths or entire transcripts.

Remove the unit-5 `legacy_migration` reservation/status view and admission
subprocess. Ordinary structural errors and pending lifecycle diagnoses remain;
status does not run historical scope reconstruction or read a maintenance file.
An apparently valid but historically incomplete shell is handled by the explicit
pre-rollout inventory, not certified by an empty ordinary status result.

Status is read-only and does not refresh remote refs, advance observations or
initialize a grace clock. Render absent/stale observations honestly; it may show
cached proof results with their times. The existing `scan --dry-run --json` is
the explicit fresh diagnostic operation and may fetch refs under its documented
contract, without persisting or archiving.

Add `GET /api/auto-archive` to expose the same envelope through the existing
generation/authorization checks. Add an Automatic archival overview on the
workspace page with policy state, counts, last scan and per-session rule,
earliest eligibility, hold and actionable diagnosis. Link to existing session
operations for recovery; the overview does not supply mass archive/migration
buttons. Refresh while visible using the existing polling patterns, without
performing an expensive live scan on every visit. Session status continues to
show current journal phase separately from the last worker failure.

## Ordinary retained readiness and closed legacy producers

This is the replacement for installed unit 5. A valid ordinary manifest is the
lasting registration; public native evidence proves current identity/activity.
Do not add a migration marker, require a private completed repair receipt, parse
history on every ordinary call, or manufacture ready creation/goals. The exact
same root remains usable after repair, archive/revival and later legitimate
content/roster changes without retaining the maintenance utility at runtime.

### Creation absence is different from incomplete creation

Keep schema 1 and distinguish an actually absent YAML `creation` key from a
present empty/null/malformed block. Decoding both to a zero-valued Go structure
must not turn the latter into the former. Existing schema-2 creation/fork and
receipt contracts remain unchanged.

| Ordinary state | Readiness and permitted behavior |
| --- | --- |
| Present creation evidence | Keep existing strict validation and genuine ready/completion requirements. Pending, failed, malformed or contradictory evidence blocks ordinary use and directs to its existing owner. No fallback to the absent case. |
| Absent creation, exact retained root | Require valid schema-1 tracking with explicit repository/artifact lists, complete exact root/socket/client tuple, and no contradictory creation/start/fork/lifecycle/browser evidence. Prove selected socket, exact CWD/source/project/materialization, retained roster and authority when present. Keep the existing operation's native activity/submission requirements and complete unknown same-CWD discovery; archive requires idle. Missing or unavailable proof blocks. |
| Absent creation, no root | Require the existing strict threadless shape: explicit lists, no Codex/creation/fork placeholders, no roster/runtime/authority/operation residue, and complete saved-plus-loaded exact-CWD absence plus public submission-binding proof. Missing manifest is never enough. |

For absent creation, inspect actual receipt absence through the existing creation
and operation owners. A present private creation receipt (including a completed
or rotated one inconsistent with the manifest), pending start/fork or another
lifecycle operation cannot be ignored. Preserve the exact executing-archive
exception already specified; it does not waive other receipts. Reuse/refactor
these nonmigration checks from `web/observation_receipts.go` instead of deleting
them with the migration wrapper. Keep all ordinary transition/generation,
creation/session/team locks. No new ledger, provenance flag, stdin observation
protocol or per-mutation migration subprocess is needed.

Apply the distinction consistently at these owners:

- **Observation/archive:** `cmd/workspace-portal/session_observation.go` uses the
  ordinary manifest and existing retained observer, with the checks above. Remove
  `--legacy-observation-stdin`, `session/legacy_observation.go` and completed
  provenance lookup. All semantic token, grace, socket and activity gates remain.
  Ruby's archive owner performs its normal final proofs; repaired records have
  no special archive exemption. Directory/root replacement loses continuity and
  starts fresh grace; browser operation target binding remains independently strict.
- **Start/attach/resume:** update `prepare_creation_journal`, start's ready-write
  path and `require_reconcilable_portal_thread!` to accept the verified absent
  case without inserting a creation block, dispatching a goal or creating a new
  root. Preserve the exact retained root and ordinary authority/tmux/client
  admission. An explicit start from genuine threadless tracking creates a real
  conversation with genuine creation evidence under existing creation recovery.
- **Revive:** `revived_portal_manifest` and
  `apply_revived_portal_transition!` preserve explicit repository scope, unknown
  bases and the absence of creation. Use the accepted revive journal's exact
  root/operation context when resuming that root; do not require or synthesize
  `creation.tracking_origin` to recognize it. A repaired threadless archive
  revives as threadless. Ordinary revive grace reset and journal recovery stay.
- **Interaction:** `normalizeInteractivity` and its actual mutation admission
  accept ordinary retained readiness for the absent case. Presentation alone
  never authorizes sending. Existing authority, generation, exact root and
  native request/submission gates still control interaction. Busy may permit
  only what existing interaction semantics allow; it never becomes archive-idle.
- **Manifest producers:** distinguish tracking/worktree-only factory call sites
  from real creation and fork placeholders. New genuine threadless records omit
  empty Codex/creation blocks. Do not globally change `new_portal_manifest` and
  accidentally alter a fork's accepted projection/retry. Never erase present
  evidence from an existing record to make it fit the absent case.

### Creation-less start/revive retries: match their existing owners

Use the existing `workspace-portal session observe` and
`web.RequireObservationReceipts`, with two narrow internal optional coordinates:
`--expected-start-tmux-identity TOKEN` and `--expected-revive-operation-id ID`.
Both values, when supplied, are exactly 64 lowercase hex characters. They are
mutually exclusive with the existing paired archive ID/mode arguments. Either
may appear alone; both are required when the accepted revive start also has its
own child start journal. Ordinary scans/fresh start/attach pass neither. These
coordinates are accepted only for a nonempty creation-less retained root in
active tracking, never as root selectors or threadless/archive exceptions. No
browser request field, journal schema, stdin bridge or general receipt API is added.

The actual committed journal shapes determine the split:

- Start schema 1 has exactly `schema`, `slug`, `state: creating` and
  `tmux_identity`. It has **no** workspace, root, operation ID, phase or tracking
  digest. Ruby `load_start_journal` validates it; `start` also matches any live
  tmux identity and normal manifest/socket/authority. The expected token comes
  only from that loaded journal, never from an invented start operation ID.
- Revive schema 3 records workspace/slug, `operation_id`, phase, lifecycle,
  `legacy_without_portal`, `abandoned_confirmed`, `retained_thread_id` and the
  existing plan/state/portal/target-tree hashes. Ruby `load_revive_journal` and
  `prepare_revive_runtime_start!` own full shape, committed projection and root
  proof. This context is only for same-root recovery with a nonempty retained
  root and `legacy_without_portal: false`, after the latter function has reached
  `runtime_starting`. Use the loaded journal's ID even when the outer CLI option
  was omitted. It cannot adopt the fresh root of an older manifestless revive.

Ruby passes these coordinates explicitly through its creation-less readiness
call from `start`/`reconcile_native_client!`/`require_reconcilable_portal_thread!`;
ordinary callers retain no-context defaults. Validate/load the journals before
that call, under the existing generation/transition, creation and slug locks.
Bind the exact manifest root/socket, tracking dev/inode and applicable authority/
tmux to the invocation. Use the existing Ruby `auto_archive_tracking_identity`
formula shared with Go `session.ObservationIdentity`, and require the returned
workspace/slug/identity and lead subject ID to match that snapshot. Re-read the
same journals, root, directory and authority before the next runtime effect;
repeat the owning phase/projection proof where required. A start token does not
prove a root: this Ruby binding and Go's ordinary native proof supply it. Keep
the manifest's registered root consistent with existing authority/tmux evidence
on retry and refuse contradictory identity. Do not claim the start journal itself
contains historical root/directory proof across a process restart or add invented
fields to obtain it; revive's retained-root field supplies its stronger binding.

Go extends the **existing** receipt owner, not Ruby browser parsing. For the
start token, `requireOrdinaryCreationReceipts` may exclude only the exact canonical
`worktrees/.locks/<slug>.start.json`, positively read with the existing safe,
bounded file-reading conventions and the exact four-field/schema/state/slug/token
match. Missing, unsafe or malformed expected files refuse. No other initialization
file is excluded. For revive, `PendingLifecycleProgress` must positively match
kind `revive`, expected ID, phase `runtime_starting` and recorded root equal to the
ordinary manifest root. Its progress/evidence remains a read-only match; it does
not replace Ruby's full journal/projection validation. A lifecycle journal without
that matching context, or a start journal without its matching token, still blocks.

A browser receipt, if pending, must be that exact revive kind/ID, match its saved
immutable journal evidence when present, and positively bind its accepted target
using the existing version-2/journal-target identity at the recorded original
location. This supports the preserved directory after archive-to-work rename.
Reuse the existing receipt/target owners without adoption or conversion. A start
token alone cannot excuse any browser receipt. Missing expected journal, another
kind/ID/target, stale unversioned target, fork, cleanup intent, creation journal,
or current/rotated creation receipt still blocks. A CLI-only accepted operation
needs no fabricated browser receipt. Re-run these read-only checks and ordinary
root/directory/socket/authority validation after native sampling. If a journal
has legitimately been unlinked by its owner, later calls must use the newly
validated current context; never reinterpret an expected missing file as success.

**Native requirements remain operation-specific.** Committed start/attach uses
exact provenance, `require_portal_thread_materialized` and existing tmux/native
resume checks; it does not require an archive-idle team. When using this observer
for positive creation-less readiness, require valid `activityKnown` and exact
subject identity, but do **not** require `idle: true`: a known active turn,
request or queued input does not by itself forbid attaching to the same active
root. Unknown identity/activity/submission evidence still blocks; no uncertainty
is classified from error strings. Archived subjects retain the existing positive
archived-unloaded proof before same-root revival. Archive alone requires the full
idle/empty-runnable-queue/resolved-submission proof. Interaction retains its
existing authority/request admission and cannot use these internal coordinates
to bypass a pending lifecycle operation or to interrupt/replace a root.

Focused cases: valid start-only, revive-only and revive-plus-child-start recovery;
known busy active root attach succeeds while archive refuses; root/socket/tmux or
directory drift, missing/mismatched tokens, wrong revive phase/root, mixed archive
arguments and malformed journals refuse. Own revive browser target survives the
tracking move; a conflicting receipt and missing-expected-journal still refuse.
Current/rotated creation evidence is never waived. Ordinary scans with no context
remain blocked by these journals. No creation/goals block or root replacement is
introduced, and actual native/submission failures remain unknown.

### Refuse unresolved inputs before producing an ordinary record

New manifestless retained start/adoption and manifestless archive revival refuse
before publishing a new journal, moving tracking, starting runtime/root creation
or writing an empty/partial manifest. The remedy is the dated repair procedure.
Apply the same structural refusal before worktree-add/sync can create a partial
manifest or mutate refs/checkouts for unresolved retained tracking. Creating
genuinely new tracking with explicit scope remains supported; it is distinct
from adopting pre-existing raw tracking and its possible retained branches.
Do not reconstruct historical scope inside every start/revive call. Existing
accepted start/revive/creation journals finish through their compatible owning
executor before these entry rules take effect; do not reinterpret their saved
projection or use the new refusal to strand an accepted operation.

Inventory already-created revived/adopted shells as well as visibly malformed
records before releasing the simplified runtime's workers. A current empty list,
`tracking_origin: revived`, a missing former hint, or one re-added checkout does
not establish complete historic scope. The maintenance utility uses structured
history to repair those shells. Afterward ordinary runtime calls rely on the
committed explicit scope, not repeated history scans or durable tool provenance.
If any unresolved valid-looking shells remain, keep the affected operational
scope held; absence of an installed reservation service is intentional.

Restore/import procedures must repair raw backup records before exposing them
to runtime writers/workers. Future supported producers either create complete
ordinary records or refuse raw input before mutation. There is no supported
online arbitrary legacy import path.

### Retained branches and unknown bases are ordinary behavior

Keep every current/historical structured registration, including missing refs
and missing checkouts. Exact-slug refs across several canonical repositories are
several obligations. Re-add an existing registered branch at that exact ref;
missing retained ref refuses, never creates a replacement at today's default.
For an existing unregistered branch in otherwise valid ordinary tracking, register
that exact branch with base unknown unless independent authoritative historical
metadata establishes it; apply the same rule to `sync_portal_repositories`.
Raw unresolved tracking first needs repair. Do not retain the migration
`require_resolved_legacy_scope!`/history/provenance dependency under another name.

Omit unknown `initial_base_sha`. `--base` selects a genuinely new branch's start;
it cannot establish the historic base of a retained unknown-base branch merely
by naming an ancestor. Reject that use. The dated repair projection may preserve
an independently recorded historical base. Both Ruby and Go finalization still
require immutable final heads. A saved exact comparison may remain usable;
otherwise the portal shows historical comparison unavailable, never today's
default as the start. Unknown base never earns the unpushed-at-initial-head
exception. These are permanent ordinary semantics, not temporary migration code.

## Dated source-only repair and ordinary archive

Implement `bin/repair-legacy-sessions-2026-10-04` in the owned **workspace** feature
worktree, with its focused fixtures and dated instructions. This is a new source
utility, not an installed command today. Do not export it from a Nix package,
`dev-session`, portal, auto-archive worker or host service. Workspace maintainers
own the utility; the lead owns this installation's concrete inventory, approval
and supervised maintenance window. Runtime maintainers own ordinary readiness.

The new source-tool interface is:

```text
bin/repair-legacy-sessions-2026-10-04 preview --workspace PATH --runtime-source PATH --session SLUG [--session SLUG ...] [--mapping FILE] --json
bin/repair-legacy-sessions-2026-10-04 apply --projection FILE --recovery FILE
```

Preview emits the read-only projection to stdout. Exact selected slugs may resolve
in `work/` or `archive/`; conflicting duplicate locations block. Apply requires
confirmation of the reviewed selected rows and a standalone recovery-file path
outside selected tracking directories; retry is the same invocation. The
projection names the exact compatible runtime source/executor and selected
workspace authority/profile; refuse a different one on retry. These are proposed
source-tool commands, not available installed parser aliases. Do not add a generic
batch daemon, global reservation store, automatic inventory adoption or permanent
migration status API.

### One source-tool preparation input

Accept the operator-authored JSON file named by `REPAIR_LEGACY_CONTEXT`; keep the
preview/apply CLI above unchanged. This is one preparation record for the approved
workspace/batch, not one per session. It is read only by the dated utility, never
by an installed helper, registry or worker. Require an absolute non-symlink regular
file owned by the executing UID with mode 0600, schema 1, a 64-KiB bound, strict
known fields/duplicate rejection and no secrets. Its required groups are:

| Group | Exact purpose |
| --- | --- |
| `workspace`, `runtime_source`, `runtime_commit` | Canonical workspace and runtime source identity plus the exact reviewed source commit; the current replacement checkpoint is `c9bea61e48b5e6f2e5552b549409cccf172c9901` |
| `runtime` | Explicit absolute portal/dev-session executables, selected profile path and its resolved identity, existing host generation/token and transition-lock coordinates, and complete existing host-selected socket, Codex home, private state, authority and tmux coordinates needed by ordinary invocations; retain actual HOME/UID and selected Codex 0.160.0 |
| `helper` | Absolute prebuilt helper executable, executable SHA-256 and path/digest map for **both** workspace-owned source files below; bind its runtime R/module inputs to the same recorded source |
| `maintenance_window` | Exact excluded portal mutation entry points, automatic workers and external writers, each with the concrete quiescence/verification method, plus the operator/evidence reference for the supervised window and how it stays closed after interruption |

Read/bind this once for preview and seal its canonical parsed content and digest
into the projection, then into the standalone recovery evidence. Apply/retry
requires the same record; do not accept a changed coordinate or rebuilt helper
under the old projection. Resolve executables/source/profile positively through
the existing canonical and host identity owners, check helper bytes, and compare
every applicable supplied `DEV_*` coordinate with the record. Do not silently
overwrite conflicts, infer a default private state/home/socket, or let a context
file impersonate selected package authority. Existing profile/generation/transition
preflights still apply under their normal locks; record contents do not waive them.

The window section may describe the reviewed method before the window is active:
read-only preview does not require stopping writers merely to prepare a projection.
It supplies no mutation permission. At apply/retry, the existing explicit operator
confirmation must also attest that these exclusions are currently established;
check their observable conditions and fresh native/Git/identity evidence before
writes and retain that execution evidence in the recovery file. Unknown writers,
failed exclusions or lost window continuity block. The operator must re-establish
the same window after interruption. Do not treat a saved timestamp or an old
`held` claim as present proof, add a background lease service, or make the utility
stop services itself. Missing preparation is an actionable error, not fallback
to ambient defaults. Main owns the approved real preparation/window execution
under the current follow-up; this design owner does not execute it.

### Source-only native proof caller before a manifest exists

At committed runtime `6c110be5`, the positive root/team proof already has an
ordinary CLI. Use the exact approved absolute portal executable, under the
utility's existing locks/window and selected host environment:

```text
PORTAL team require-archive-ready --workspace W --session-slug S --root-thread-id ROOT --cwd W/work/S --socket SOCKET --codex-home CODEX_HOME --user-state-root STATE --authority-dir AUTHORITY
```

`teamCommand` calls `Service.RequireArchiveReadyAll`, which locks/loads the real
retained roster and proves the exact root/members and complete active discovery;
it needs no manifest and creates no members. The utility still owns reviewed
root selection, tracking/authority/receipt checks and before/after evidence binding.
Even for an archived tracking row, the native CWD is the original `W/work/S`.

There is no equivalent ordinary threadless CLI at that commit: `session observe`
requires the manifest, and its legacy stdin path is removed in `c9bea61e`. Add
`bin/repair-legacy-sessions-2026-10-04-threadless/main.go` to the **workspace**
source. Its default `--mode threadless` accepts `--workspace`, `--session-slug`,
`--socket` and `--codex-home`, derives the exact original CWD, and calls exported
`workspacecodex.RequireThreadlessConversations(ctx, client, cwd)`. Apply the existing
slug validator and canonical absolute workspace/socket/home checks; resolve the
workspace identity positively, not from the helper's build CWD. The owner in
`portal/internal/workspacecodex/discovery.go` checks public
`ThreadOperationAttempt` before/after complete saved/loaded discovery. Exit zero
only on success; every error/timeout is blocking unknown or residue, with bounded
stderr. No stdin projection, manifest creation, root flag, ledger parser, native
resume/subscription, turn or persistence write is added by this wrapper.

The Go `internal` boundary determines the build layout. Verify the supplied
runtime source against the canonical runtime common-dir/origin and the exact
reviewed commit R recorded with the executor/selection. Export **committed** R's
`portal/` tree to a fresh private build directory using `git archive`; do not use
an implementer's working files or modify any runtime checkout. Copy the
workspace-owned main into that disposable module at
`portal/cmd/dated-legacy-threadless/main.go` and the receipt bridge below into its
stated same-build package path, then, in the declared runtime Nix
environment with absolute BUILD, build with `GOWORK=off go -C BUILD/portal build -mod=readonly -trimpath
-o BUILD/threadless-proof ./cmd/dated-legacy-threadless`. It is thus genuinely a
command inside module `github.com/aither64/dev-workspace/portal` for this build,
with legitimate access to its exported internal owner. Keep R's `go.mod`/`go.sum`
unchanged, including pinned codex-web `3d07cf60` at the inspected baseline; no
separate module, `replace`, vendored proof copy or dependency upgrade. Record R,
both helper source digests and executable provenance in maintenance evidence. Missing
dependencies/build failure blocks preparation. Build once during approved
preparation, never silently compile a different revision on repair retry. Nothing
is installed into the runtime package or its public command parser.

Construct the helper client with `workspacecodex.NewWithOptions(socket, workspace,
codex.ClientOptions{...})`, using the ordinary client's `ClientInfo` identity and
explicit `SubmissionLedgerPath: socket + ".submission-attempts-v3.json"` from
`main.go:newCodexClient`. The workspace wrapper supplies `CodexHome` from
`DEV_WORKSPACE_CODEX_HOME`; require it to equal the explicit canonical selected
`--codex-home`, exactly as the ordinary preflight does. Preserve the host-selected
HOME/Codex/private-state environment, numeric UID and exact socket/executor;
the private **build** directory must never become a replacement runtime home,
ledger or empty private state. Reject coordinate/profile drift and do not fall
back to the default socket or a PATH-selected executable. Public client methods
own ledger interpretation; an inaccessible ledger is not empty. Use the existing
one-minute observation deadline and close the client. No model request is needed.

The threadless mode proves only conversation/submission absence. The separate
receipt mode below supplies its narrow local receipt result. Existing owners still
prove no roster, runtime/authority and creation/lifecycle residue, plus the tool's
exact tracking/refs and maintenance window, before and after the proof calls.
It supplies no durable provenance or waiver. Focused wrapper checks cover exact
arguments/environment/ledger wiring and propagation of owner failures; reuse
the existing discovery fixtures for protocol behavior. Real native execution
remains behind the accepted review/isolation gates. No build or probe was run
for this caller clarification.

### Per-slug browser receipt proof in the same source-only build

Whole-file presence of `lifecycle-operations.json` is **not** a repair blocker.
At R `c9bea61e`, `newLifecycleOperationStore` is read-only and `loadReadOnly`
already owns strict schema/workspace/duplicate/record/permission validation;
`save` can leave a valid empty store. `RequireObservationReceipts` deliberately
requires different evidence for an archived summary and cannot be called with
a fabricated manifest or `Archived: false` to obtain this narrower answer.

Add one workspace-owned source file alongside the main, at
`bin/repair-legacy-sessions-2026-10-04-threadless/web/receipt_bridge.go`.
During the same disposable R-module build, copy it to
`portal/internal/web/dated_legacy_repair_bridge.go` with `package web`. Its sole
bridge function, `DatedLegacyRepairRequireNoPendingBrowserOperation(workspace,
slug, stateRoot string) error`, validates canonical supplied coordinates/slug,
calls `newLifecycleOperationStore(workspace, stateRoot)` then `loadReadOnly`, and
tests only the returned entry for that selected slug. It is exported **only in
this disposable build** so the existing dated helper main can call it legally.
No runtime source/export, installed package/command or ordinary readiness API
changes. Do not copy or reimplement the store decoder or its validators.

The same executable gains only `--mode receipts --workspace W --session-slug S
--user-state-root STATE`. This mode performs local file reads and exits zero on
the narrow proof; it does not construct a Codex client or call App Server. No
generic RPC, stdin view, manifest summary, mutation or completion reconciliation
is introduced. Missing/unavailable proof yields nonzero with bounded diagnosis.

| Validated store result | Repair receipt decision |
| --- | --- |
| Store absent, valid empty store or no entry for selected slug | No browser reservation for this row; other proofs still required |
| Selected entry has validated `state: complete` | No pending browser reservation; retain it untouched, regardless of an old target/version; this does not certify that target or the current lifecycle |
| Selected entry is running, paused or failed, including pre-journal or missing-expected-journal | Block this row and direct to its existing operation owner; never mark it complete, supersede, delete or adopt its target |
| Valid unrelated entries, including unrelated pending entries | Do not reserve this selected slug; keep them untouched and retain other ordinary global preflights |
| Malformed/duplicate/unsupported schema or state, wrong workspace, unsafe ownership/mode, unreadable store or invalid record anywhere | Owner cannot establish a trustworthy view: block with unknown evidence, even if the bad record appears unrelated |

The loader's in-memory running-to-paused conversion is still nonterminal and is
never saved by this bridge. Completed lifecycle receipts differ from conflicting
private creation evidence: preserve the accepted exact creation/start/fork/
lifecycle-journal/cleanup checks at their current owners; even a completed browser
row cannot excuse a still-present owning journal. For raw creation-less
rows, if access to portal-private current/rotated creation receipt paths is needed,
the same bridge may perform the existing exact slug filename/prefix **presence**
check under its owner-resolved `store.directory/creations`; any matching entry or
unreadable directory blocks. Do not parse creation receipts in Ruby, fabricate a
ready creation summary or treat a completed creation receipt as absent. This
limited refusal does not apply to the validated completed lifecycle row above.

Run the receipt mode at preview, before apply row writes/commit and after native
sampling under the established maintenance window/locks. It proves current
per-slug reservation absence, not an enduring lease or cleanup authorization.
The utility never deletes a store to pass. Both source files and the mode dispatch
belong in the tool's substantive review; focused fixtures cover absent/empty,
selected complete, each selected nonterminal state, unrelated valid entries,
foreign/malformed/duplicate/unsafe stores, creation residue and no file writes.
Reuse the existing store tests for decoder semantics rather than another parser
matrix. This bounded preparation/receipt clarification is READY/FROZEN for lead
relay; no build, test, native call or real preparation was performed here.

### Projection and approval boundary

Inventory active **and archived** selected tracking, including valid-looking
legacy revived/adopted shells, using exact Git paths/blobs and current identities.
The earlier 146/124 incident counts are not a complete or current inventory.
Use the existing canonical repository and archive inventory owners. Union current
and historical structured registrations, exact local/cached-origin slug refs,
and owned attached feature branches even when all checkouts are gone. Record
canonical common-dir/origin identity, branches/defaults/tips, worktree/admin
identities, source file identities/bytes, exact historical blob evidence, retained
root/team and the proposed ordinary manifest/state. Do not fetch or create refs,
change branches, start/resume/archive threads, create roster members or manufacture
an operation receipt during preview/apply.

Produce a bounded, deterministic JSON projection with selected source/target
paths and hashes, evidence, decisions, blockers and proposed later archive mode
(or retain). Report/projection and one optional mapping are sufficient: no full
normalizer plan registry. Infer unambiguous rows in bulk. Require reviewed mapping
only for genuine conflicts in canonical identity, defaults, historical metadata,
root selection, unsupported front matter or empty scope. Multiple exact-slug
repositories are not ambiguity. No-evidence scope is not automatically empty.
Mappings cannot waive foreign ownership, missing registrations, dirt, actual
writers or unknown native proof. Reconstruct the target from sealed evidence
on apply; editing the JSON or its digest is not authority.

Before a manifest exists, the **tool's** reviewed row binds the exact retained
root/socket/roster for the existing lower public retained-readiness proof. Reuse
the same helpers used by the archive/team owner, with complete saved/loaded
same-CWD discovery; do not call the normal manifest observer through a fabricated
ready manifest or retain the migration stdin bridge. Threadless decisions need
the existing complete negative proofs independently of repository scope. A
positively identified idle unarchived root/team is allowed; archived retained
subjects use the supported archived-unloaded proof. Busy, queued, pending,
unresolved, unreadable or unknown identity/activity blocks. Recheck during apply;
preview observations are never permission to mutate later.

Preserve plan/state body bytes, artifacts, titles and valid explicit lifecycle.
For an active-path record lacking anchored lifecycle, prepend honest `active`
front matter, then commit that baseline now; prose is not completion or historical
active evidence. Unsupported/conflicting headers require a reviewed decision,
not a second silent header. Retained archives keep genuine terminal state and
history; unknown terminal provenance is blocked for an explicit disposition,
not assigned a fictional completion or active past. An archived final head also
needs positive recorded evidence; today's feature tip is not its historic final
head. Preserve all exact refs and roots. Omit unknown bases and invented
creation/goals. Identify predecessor
post-revival inferred bases and omit them unless independently supported. An
approved projection authorizes metadata repair only, not real archival.

### Maintenance window, bounded apply and recovery

The maintenance window replaces the removed online reservation machinery. Before
writes, the lead records exact workspace/source/profile identity, excluded portal
mutation entry points and automatic workers, known external native/Git/editor
writers and the method keeping them quiescent through a crash/restart. Acquire
the existing generation/transition and creation/session locks in normal order;
reuse the existing retained-team proof locks. Locks exclude cooperating helpers,
not arbitrary native or Git writers. Keep App Server available for read-only
proof. Fresh exact identity/activity/ref/content checks must pass before each
row's writes and commit. No background writer may enter because a prior sample
was idle. Missing window evidence or unknown writers refuses apply. This design
does not authorize stopping this initiative or any actual service.

Inventory old lifecycle/start/revive/creation/browser journals and cleanup
sidecars before repair. Resolve them through their existing owner or exclude the
row without touching protected files. Repair cannot certify a lost browser
result, adopt its target or replace its journal. Unexpected installed migration
receipts are a separate upgrade blocker as described below.

Use one tool-owned, bounded recovery file (with source/target bytes, exact
identities, approved row actions and commit/progress evidence), atomically
persisted and fsynced **before** writes. Process selected rows sequentially, with
an exact-path tracking commit per repaired row; partial completion is explicit,
not an all-or-nothing batch transaction. Preserve unrelated index/worktree bytes,
shared-master linearity and normal hooks. Do not project or commit application
code. Verify committed target trees before marking a row committed. Reuse an
already made exact commit only after proving it belongs to this recorded repair.

Retry accepts only recorded source or target bytes/identities, repeats native,
ref and writer checks and stops on drift. It may finish an uncommitted exact
projection or recognize its exact committed result. It never rolls back committed
tracking, shrinks the approved selection silently or invents a new baseline to
cover unrelated edits. Fsync a fixed per-row grace epoch before resetting the
existing automatic-observation store after commit; retain positively same-identity
holds. Retry uses that epoch exactly once, and completed apply does not reset
again or overwrite later legitimate activity. Archived rows gain normal fresh
grace only when revived; do not invent active automatic observations for them.
Reuse existing store/locking helpers from the pinned source, without a new
installed reset API. Do not move the 1,217-line online framework into this file:
no cross-row reservation/admission service, completed runtime provenance reader,
private status protocol or generalized transaction framework.

After interruption, keep the window closed until the recovery file and all
selected rows are reconciled. Advisory locks disappearing on process exit do
not preserve that window. Do not re-enable workers over incomplete valid-looking
shells. If unattended online repair across crash/reboot becomes required, return
that changed requirement to the lead; this tool does not promise it. Retain the
source/projection/recovery evidence for audit and supported restore paths, but
ordinary use after repair must work without reading or even having that file.

### Archive is still the normal operation

After separately approved repair, run ordinary `dev-session archive SLUG --as-is`
for the exact approved archive selection. Preserve real PTY/confirmation behavior;
supervised automation may answer only the exact expected prompts for that approved
selection. Do not invent `archive --yes`, forge portal authorization or substitute
file moves. Complete mode repeats cleanliness, exact local/remote merged heads,
retained refs, current root/team/submission and ownership/generation proof. Dirty,
unmerged, busy or unknown rows remain open with concrete reasons. Abandoned mode
requires explicit discard approval and retains all other protections; it is not
a fallback for migration failures. Root/member/branch ownership never changes.

Once an ordinary archive journal/sidecar exists, that owner controls retry. The
maintenance file may record the result; it must not project over, clean up or
supersede the operation. Stale projections from before archive cannot repair the
moved tracking. No actual inventory, apply or archive is authorized by this brief.

### Installed removal boundary

Delete `libexec/workspace-legacy-migration.rb`, its requires/mixin, installed CLI
help/parser/dispatch, reservation exceptions/calls, historical scope and completed
provenance lookups in `dev-session`, `workspace-auto-archive.rb` and `workspace-host`.
Delete `web/legacy_migration.go`, `session/legacy_observation.go`, migration stdin
handling and mutation call sites in `web/{server,preparation,operation_state,auto_archive}.go`.
Remove the migration-only status field/counts, package helper install/symlink
entries in `nix/workspace-portal.nix`, and migration-specific test registration.
Preserve ordinary transition admission while removing migration wrappers.

Keep generic canonical helpers such as `legacy_project_name`, real receipt and
package/lifecycle guards, archive sidecars, browser conversion, threadless proofs,
unknown-base tests and semantic retention. Move only useful historical-evidence
fixtures to focused source-tool tests. Adapt acceptance support to ordinary repaired
records or the dated tool, not an installed migration command. Replace the
installed normalization guide/references with ordinary runtime contracts and a
link to the separately owned maintenance procedure where site-specific. No new
configuration, extension behavior, Codex dependency or public protocol is needed.

## Compatibility, package selection and recovery

- Keep existing portal manifest schema numbers, archive schema 2, creation and
  submission ledger formats, tmux/runtime identities, cluster state and transition
  policy. New private sidecars/observations are independently versioned and
  strictly validated. Do not add fields to schema-2 archive JSON. Schema-1 manifests
  may genuinely lack creation metadata; schema-2 in-flight creation remains strict.
  The dated utility's projection/recovery file is operational evidence, never an
  installed runtime format or a condition of later retained readiness.
- Older finalized-manifest readers may refuse an absent initial base. This is an
  intentional forward-only compatibility boundary: refusal is preferable to
  invented comparison history. Older start/revive/observation readers may also
  reject creation-less roots. Select a coherent capable runtime/portal/helper
  package; do not mix old writers with repaired records. Preserve the documented
  forward-only profile switch and do not claim downgrade support.
- Old executors do not understand the new cleanup sidecar. Finish pending
  operations using the same/newer capable package before switching; never remove
  receipts to bypass a gate. The narrow selected-executor recovery above applies
  only to compatible predecessor journals without a new sidecar and retains its
  genuine creation evidence requirements.
- Main reports no migration of real sessions or installed/native acceptance
  fixtures. Source unit/fault tests in committed `test/dev_session/legacy_migration_test.rb`
  did exercise `legacy_migrate_apply` in disposable `with_legacy_fixture`/
  `with_workspace` state; those tests passed. That disposable test consumption
  creates no supported persisted upgrade dependency. The read-only 09:53 UTC
  inventory found both the private `legacy-session-migrations` parent and
  workspace directory absent; see
  [read-only-migration-state-inventory.json](read-only-migration-state-inventory.json).
  Removal has no established local persisted migration upgrade dependency.
  Recheck this at package selection alongside active/archived input inventory
  and external-consumption provenance. If an
  unexpected pending batch or completed dependent receipt exists, hold transition
  and reconcile it offline through its exact capable owner; do not silently
  ignore/delete it or add a permanent reader to the simplified runtime. Preserve
  ordinary journals/sidecars/browser/creation owners independently. Finish the
  maintenance inventory/window before allowing workers over historic partial
  shells, and route supported raw backup restoration through the same procedure.
- New helpers continue to recover old valid schema-2 journals. A package switch
  must preserve its existing pending-operation refusal and candidate activation
  checks. Waiting commands still reject a changed profile generation/token after
  lock acquisition, including compensated switches.
- No database, API daemon protocol, generated client, Terraform behavior or NixOS
  fleet state changes. No coordinated node update is required. HTTP additions are
  additive; the new browser bundle supports old receipts and fresh in-page
  confirmation for unverifiable targets, never a guessed target. Already loaded
  old static JavaScript is not hot upgraded and may require a normal reload after
  a safe stale-target refusal. Pages loaded with the new bundle retain the
  no-reload refresh objective.
- Preserve the currently merged selected extension and its sibling graph. The
  initial preservation decision kept `cd81e83f`; the lead now reports already
  merged `77dd0d04` in workspace default `4df3b7c`, which its consumer refresh
  must retain. This reconciliation does not update any pins.
  The workspace owns a direct nested `vpsfree-dev-workspace.inputs.dev-workspace`
  URL override selecting exact reviewed runtime, while still using extension
  `lib.mkPackage` and existing team/site configuration. That declaration shape
  is already in workspace default `88a75655`, selecting merged runtime `3edc605d`.
  Retain it as the current baseline; do not replay the owned old `6a972b9` pin or
  recreate the declaration as new work. Preserve useful unmerged selection docs.
  Review the composed result and any remaining substantive consumer/cache fixes;
  generate exact final coordinates with Nix afterward under the accepted
  mechanical-pin rule. The owned extension checkout remains unchanged
  at its already merged `e1bb5cf` head. See
  [composition preservation](design-composition-preservation-result.md), which
  supersedes the former extension-pin sequence. Preserve the entire sibling
  input/follows graph. Configuration aligns its host-module runtime identity
  through confctl as required by the unchanged deployment checker; application
  selection remains in the user profile.
- Preserve the current 50-file preparation reader and its documented compatibility
  limits. The initial 10-file reader rejects unfinished 11–50-file snapshots even
  though the schema number is unchanged. Existing normal terminal compaction,
  creation proof and upload binding own recovery; never remove records or drafts
  to permit an older reader. Selected `jq982nq…` replaced `s7y4bgq…` at the recorded
  checkpoint; neither is a promise that an older executor reads new cleanup state.
  The positive predecessor-recovery fixture has been removed as unsupported. Record
  fresh generation, lifecycle and preparation inventory before any future switch.
- Publish feature revisions as needed for reproducible package selection, with
  the lead's normal Git/verification procedure. No default-branch integration is
  implied. Before a requested deployment, record selected package/Codex identity,
  pending receipt inventory, source heads and exact candidate closure. Switch only
  through the user profile. Recovery rolls forward to a capable reviewed package.

## Temporary compatibility inventory and removal contract

Generic lifecycle maintainers own runtime adapters. Workspace maintainers own the
dated source utility; the coordinating lead owns this installation's inventories,
window and rollout evidence. Label each temporary path and its input format in
its owning documentation/tests. A date or successful deployment never permits
removal; archive location does not mean a record can no longer be revived.

| Temporary support | Accepted input | Inventory-based removal condition |
| --- | --- | --- |
| Dated source-only historic repair | Active or archived plan/state lacking anchored lifecycle/manifest; retained exact refs and structured historical evidence; incomplete legacy revived/adopted shells; predecessor inferred-base records | All supported active **and archived** records repaired or explicitly excluded from runtime use; no unfinished maintenance recovery, start/revive/creation/browser operation needs it; every supported backup restore/import/predecessor upgrade either already produces ordinary complete records or retains access to this source tool/procedure |
| Legacy archive recovery without cleanup sidecar | Exact schema-2 archive journals written before sidecar support | No unfinished dependent journals/intents and no supported predecessor operation or upgrade recovery can create another |
| Old browser target receipts | Current receipt schema with ctime-derived target and no target identity version | No unfinished receipts of that shape, including pre-journal and missing-expected-journal states, and no supported old portal/upgrade/restore can reintroduce them |
| Old automatic observation conversion | Schema-1 observations without a semantic fingerprint version, root-ID-only identity | All supported observations/holds upgraded or reset with positive binding; no supported old worker/restore path can write them again |

The installed unit-5 normalizer, reservation reader and completed-provenance reader
are removed as superseded feature paths with no reported real-session or installed
acceptance application, subject to the provenance check above. Disposable source
unit/fault-test application does not require retaining compatibility for that test
state. They are not new compatibility obligations merely because a feature
commit/package was published or tested. Record any contrary actual consumption
before removal/selection; an unfinished receipt is never garbage-collected to
make the inventory empty. Resolve its exact supported recovery before proceeding.

The common gate inventories active/archived tracking, unfinished lifecycle,
creation/revive/browser operations, cleanup sidecars, private observations/holds,
any historical migration or tool recovery files, retained supported package
versions and all supported upgrade/revival/restore paths. Record counts, schemas,
oldest supported source and replacement path. Require zero dependent inputs and
zero supported ways to reintroduce them before removing a compatibility owner.
Keep tool recovery evidence until its operation is reconciled. Afterwards retain
it as operational/audit evidence, never a live readiness dependency. Schema-2
archive support, creation-less ordinary readiness and unknown-base manifests are
lasting contracts and have no date-based removal gate.

## Documentation placement

The runtime session guide owns normal cleanup/idle proofs, unknown bases, strict
creation absence versus present evidence, raw producer refusal and status commands.
The portal guide owns stable targets, interactivity/readiness and operation recovery.
The archive recovery guide owns partial team/no-sidecar recovery, selected executor
constraints, input formats and runtime adapter removal inventory. Remove the
installed normalization guide and its command/provenance/admission instructions;
generic docs must explain ordinary behavior without this private workspace.

Workspace `bin/` and its linked dated procedure own this installation's repair
selection, projection/apply/window/recovery and ordinary archive sequence. Keep
that procedure available for supported backup restore/import. Update workspace
lifecycle/session/Git instructions from installed migration dependence to this
boundary; do not spread historical inference across runtime commands. Exact pins,
reviewed projections, approvals, actual results and inventories belong in lead-owned
tracking/rollout records. Preserve historical design reports with the supersession
notice at this document's start. The coordinating main agent reconciles final
user-facing text with vpsfree-user-facing-writing before commits.

## Historical implementation sequence: migration simplification

This sequence records the preceding completed scope. Use the approved follow-up
above for current assignments and verification; do not restart these units.

Units 1–4 remain the ordinary reliability contract already implemented/reviewed;
this reconciliation does not authorize unrelated rework or repeated verification.
One retained implementer handles the replacement units below under the lead's
assignments. No additional role, repository, service or framework is introduced.

1. **Archive inventory and sidecar:** retain discovery/proof/sealing/retry, unknown
   bases and the old schema-2 compatibility owner.
2. **Retirement and dispatch:** retain team-first flow, complete saved/loaded
   discovery, public archived-unloaded proof, environment fix and narrow recovery.
3. **Browser identity:** retain stable targets, safe old-receipt conversion,
   new-bundle refresh and no-adoption/missing-expected-journal behavior.
4. **Semantic retention/status:** retain actual-turn observations, typed blockers,
   threadless proof, grace/holds, unchanged tiers and useful workspace diagnoses.
5. **Unit 5a, replace installed migration (next actionable unit):** implement ordinary
   creation absence/readiness at the named Ruby/Go owners and close raw
   start/adopt/revive producers before mutation. Preserve exact roots, unknown
   bases, fork and accepted-journal recovery. Remove installed migration code,
   CLI/stdin/status/package/admission/provenance integration and migration-only
   tests/docs in the same coherent unit; retain general receipt/generation checks.
   Report focused readiness/producer/lock regression results to the lead. Do not
   attempt live repair or bypass existing recovery refusals to demonstrate it.
6. **Unit 5b, dated maintenance utility:** implement the source-only preview/projection,
   bounded sequential apply/recovery and window checks, using existing strict
   owners; add focused evidence/crash/drift fixtures and site instructions. Adapt
   owned acceptance support to ordinary repaired metadata or this utility. A
   concrete real inventory and later repair/archive execution require separate
   approval; they are not implementation work or a test prerequisite.
7. **Composition and final reconciliation:** preserve the latest merged consumer
   baseline/extension graph, reconcile prose and acceptance support, complete
   intended substantive commits and quick checks, then obtain revised independent
   whole-branch review. Exact post-review coordinates/locks remain the mechanical
   tail under the accepted packaging sequence. Long checks follow that gate.

The prior unit-5 final review does not approve this replacement. The lead owns
history consolidation and confirms which discarded versions were actually
consumed. Do not rewrite published default history or erase supported inputs.

## Acceptance and verification plan

All mutation fixtures use disposable repositories, tracking roots and private state.
Unit tests may use fake App Servers and simulated clocks; native acceptance uses
the selected real authority with its actual clock and no model turn. Do not use
the cited incident or the 146 records as destructive acceptance fixtures. Read-only inventories may
inform preview examples, but actual apply/archive needs separate approval.

### Focused checks before final review

Use the repository Nix environment. Run focused Minitest cases in
`test/dev_session/{archive,lifecycle_archive,automatic_archive,worktrees}_test.rb`,
`test/auto_archive_test.rb` and affected host files as relevant to changed owners.
Replace migration-only suites with focused ordinary readiness/producer tests and
dated source-tool fixtures; reuse existing repository test conventions.
Run affected Go package tests for workspacecodex/teamruntime/session/web, including
the Node-backed lifecycle harness, and `node --check` on edited JS. Include the
repository's declared lint/hooks and workspace instruction/deployment-contract
tests when changed. Commands expected to exceed a minute or with unknown duration
go to the policy watcher; a focused label alone does not make a check quick.

| Area | Required concrete cases and result |
| --- | --- |
| Discovery | Direct feature + `integration-targets/project` + detached auxiliary from same/different canonical repos; exact slug only; all verified clean eligible paths removed, all refs retained |
| Ownership | Foreign common dir, symlink component, unregistered `.git`, duplicate/overlapping worktrees, lock/prunable record, missing checkout registration, unknown file/container: refuse before removal |
| Heads | Registered missing checkout remains obligation; unregistered attached feature unmerged/missing origin refuses complete; default checkout behind origin allowed; detached merged allowed; orphan detached refuses even abandoned |
| Complete/abandoned | Dirty/untracked state refuses both; abandoned bypasses merge only; unpushed exact recorded initial base keeps current supported behavior; no base never earns exception |
| Recovery | Crash before/after sidecar and journal publication, each checkout removal/progress write, container removal, tracking rename/commit and journal deletion; retry proves absence and completes once |
| Concurrent change | Add checkout/file, replace directory/admin dir with same HEAD, change branch/HEAD/ref, move default losing ancestry, mutate tracking or root identity at every destructive boundary: refusal with retained evidence |
| Old journal | Valid no-sidecar schema-2 at prepared/clusters_released/tracking_committed recovers under old layout; new auxiliary additions and changed heads/tree refuse |
| Team | All idle, partially archived, App Server archive before roster write, archived root with active unknown, unknown same-CWD alongside root, busy/queued/unresolved member, unmaterialized/replacing member: only exact retained idle set can retire; archived `vscode` requires positive notLoaded/complete loaded-list absence and terminal turns/submissions, no queue/list; archived loaded or unknown source refuses, dormant rows preserved |
| Host | Ordinary and inherited-lock dispatch preserve canonical home without exports; caller override cannot win; selected 0.160.0 active/archived root recovery; incompatible generated contract and generation races refuse without changing selected profile |
| Browser | Artifact creation and atomic manifest write do not change target; restart/failed archive retry updates in-page; directory/thread replacement refuses; old pre-journal exact-positive match converts; unmatched old receipt requires confirmation; accepted journal never retargets |
| Activity | Settings-applied/updatedAt/name/poll changes do not move idle-since; new root/member turn, failed/interrupted turn, observed queue/submission, dirty->clean and real content/head changes do; restart preserves grace |
| Unknown/blockers | Repeated identical unmerged/network/cleanup failure leaves elapsed grace; fixed proof can succeed next scan; unknown/null/malformed/future activity blocks and next trustworthy observation restarts grace; team identity mismatch blocks |
| Policy | Exact 1/7/14 boundaries with fake clock, hold/release and enable epochs, backwards clock, no implicit abandonment, automatic receipt resumes only its journal, disabled worker does not start new operations |
| Tracking-only | Genuine ordinary no-thread with merged branches or explicit empty scope eligible by proper tier; loaded-but-not-saved exact-CWD thread blocks; positively verified unrelated loaded CWD does not block; missing manifest alone, live/archived unknown thread, authority/creation/team/submission residue or unavailable loaded/list/metadata proof blocks |
| Ordinary retained readiness | Creation key absent with valid exact root/socket/explicit scope succeeds through normal observation, archive, start/attach, revive and eligible interaction; root is preserved and creation/goals remain absent. Remove the maintenance evidence file after completed fixture repair and repeat ordinary use: no dependency on it. Empty/null/malformed, pending/failed creation, missing tuple, contradictory completed creation receipt, foreign socket/authority/roster, busy/unresolved/unknown native proof still block at the appropriate owner |
| Producer refusal | New raw manifestless retained start/adopt and revival refuse before journal/move/root/manifest mutation; worktree-add/sync cannot create a partial shell or mutate branches first. Existing accepted journals retain exact owning recovery. Tracking-only factory output omits fabricated placeholders; real fresh creation/fork and their retry evidence stay unchanged |
| Repair projection | Active and archived inputs, previously revived/adopted partial shells, missing worktrees with retained refs, aliases/multiple projects, remote-only and missing registered refs all retain obligations; prose completion ignored; no base invented; genuine ambiguity requires one mapping; unavailable terminal provenance blocks archived repair |
| Repair apply/recovery | Prose preserved, exact-path current baseline committed, unrelated index/worktree untouched, hooks enforced, same-identity holds and fresh grace once; missing window/writer proof, changed files/refs/root/checkouts refuse; crash before/after each file/commit/grace checkpoint resumes exact source/target once, never rolls back committed tracking or resets completed rows again |
| Repair to archive | Idle unarchived root/team can be repaired without retirement; selected archived-unloaded semantics retained. Ordinary CLI confirmation/proofs follow separate archive approval; dirty, unmerged, busy/unknown and unexpected prompt refuse, no fallback abandonment. Archive interruption returns to journal/sidecar owner; maintenance retry cannot overwrite it |
| Revival/re-add | Repair an archived record with checkout-less retained refs, revive preserving exact root or true threadlessness and all obligations, then ordinary archive; no false empty/14-day tier. Unknown bases survive re-add/sync/finalization/revival; missing registered ref refuses; --base cannot certify retained history; predecessor inferred bases never earn an initial-head exemption |
| Removed integration | No installed migration command/module, stdin observation bridge, status reservation view, package preflight parser or Go mutation subprocess remains; normal generation/transition locks, pending creation/lifecycle/browser gates and package refusals still work |
| Format/limits | Strict sidecar/ordinary receipt validation remains; tool projection/recovery is bounded, rejects duplicate/unknown fields and path escapes/drift; shared Ruby/Go fixtures distinguish absent/present creation and agree on unknown-base/threadless manifests |
| Status | Valid, malformed legacy, pending moved archive, stale observation, disabled policy and hold rows all appear; one bad row does not hide others; read-only status changes neither grace nor refs; browser overview uses same diagnostics |
| Current baseline composition | Preserve 50-file preparation/upload bounds, provider summaries and archive UI/cache behavior; retain client 3d07cf60, latest merged extension 77dd0d04 and sibling graph in lead-owned consumer refresh; no historical runtime/extension pin replay |

Add protocol contract coverage for the local `thread/turns/list` request/result
fields against schemas generated by selected 0.160.0. The existing codex-web
coverage check scans client sources, so merely reusing `Request` does not prove
the new local payload: a focused local contract fixture must cover it.

### Historical replacement review and longer verification

The following records the migration-simplification review/acceptance plan. Current
follow-up verification is the focused set above; the old native fixture matrix
and its former live-action holds are superseded.

All intended substantive runtime/tool/docs/acceptance changes must be committed
and affected quick checks must pass before revised independent final review.
Use the accepted [source-review and mechanical-pin sequence](design-packaging-result.md),
[composition preservation](design-composition-preservation-result.md) and
[current baseline reconciliation](design-current-baseline-result.md), retaining
later already-merged baseline advances identified by the lead. Only exact reviewed
coordinates/generated locks remain in the exempt tail. No hand-edited locks,
fake published revisions or CI suppression. The tool, ordinary readiness/producer
changes and removal of unit-5 owners are substantive; they cannot go in that tail.

Inventory complete base-to-head history and final diffs for each changed repo.
Identify removed implementations and migration/projection/receipt versions;
record separately whether each was merged, released, deployed or externally
consumed. Distinguish the successful disposable source-unit/fault-test applications
from no reported real-session or installed/native acceptance application and the
absent live private migration store. Do not retain disposable test-state readers.
Consolidate
obsolete unapplied history through the normal procedure without rewriting
published default history or deleting real recovery evidence. Reviewer0 receives
that inventory and this matrix and must explicitly conclude on final history,
migration removal, ordinary creation-less safety and the maintenance-window
boundary. Earlier unit-5 approval is historical, not approval of this replacement.
Routine design reconciliation itself does not trigger automatic final review.

After review, a fresh policy watcher runs the necessary changed package composition
and the changed isolated installed path. Reuse unchanged exact-input evidence for
Codex generated contracts/startup, archive fault cases, tiers and host/cluster VMs;
do not duplicate the current watcher or repeat unchanged suites/CI matrices merely
because migration code was removed. Run declared package checks when required by
the final composition; Main selects commands and records which existing evidence
is retained and why. Changed owners and generated/package wiring still need real
coverage. No local kernel build or Codex upgrade is intended.

The isolated installed path exercises ordinary creation-less retained readiness
where a supported public fixture can establish it without inference, or honest
threadless repair; normal archive/revive, held exact refs, unknown base and once-only
grace; selected settings; and removal of installed migration dependencies. Reuse
existing package/browser harnesses and the prepared acceptance/network procedure.
Every fixture has separate registry, HOME/Codex/private state, sockets, Git refs
and genuine named unit cgroups. Prove native/App Server/browser egress isolation
before executing them. The ordinary host Nix daemon lies outside a client's netns;
do not claim that namespace contains daemon-delegated builds. Real native checks
have no model turn or fabricated persisted creation/team/operation receipts.

Retain ordinary CLI/browser team archive, nested/detached cleanup, stable new-bundle
page target, semantic settings-versus-turn and restart coverage from the existing
acceptance brief. Use existing package/fake-server tests for retirement faults
and genuine ready-creation recovery contracts; real selected-executable startup
smoke proves only its exercised public protocol/startup behavior. The removed
positive installed predecessor-recovery fixture remains removed: creation-less
tracking journal production does not satisfy that predecessor's ready-creation
eligibility. If a required retained-root/team native fixture cannot be produced
through supported public methods without inference, record that positive-native
coverage gap explicitly instead of constructing private state or claiming a
threadless/fake-server substitute passed it.

Do not run a second upload/VM matrix for unchanged behavior. No production repair,
archive, auto-archive enablement or default integration is a test prerequisite.
Those live actions were held at this historical checkpoint. The subsequently
approved follow-up above governs Main's real repair selection, two ordinary retries,
rollout and integration; earlier fixture gaps do not reinstate those holds.
