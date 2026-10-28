# Files tab limit diagnosis and proposal

Implementation brief, finalized 2026-10-28 after the user said “Implement the
plan” and selected alphabetical pages. The investigation below is preserved as
evidence. This brief authorizes no integration or activation; those remain
separately gated. Readers: the lead, implementers and independent reviewer.

## Finding

The Files tab deliberately rejects the **entire recursive listing** when it
crosses 5,000 regular files or a 4 MiB path-metadata/output budget. The byte
budget is not a file-content-size limit. The scanner reads no file contents.
One large log cannot cause this listing error merely through its size.

The API returns HTTP 503 with no `files` array and the text:

> The file list is too large to display (limit: 5,000 files or 4 MiB).

The browser only populates the tree after a successful response. The first
failed load therefore shows the error and an empty tree. A failed refresh
preserves a previously loaded tree. This is documented and tested behavior,
not evidence that files were deleted or that registration is missing.

The initial investigation established the mechanism without inspecting other
sessions. A subsequent user-authorized metadata inventory found nine over-limit
tracking directories; see [file-inventory.md](file-inventory.md) for counts,
causes and scope limitations. No particular failed browser request was traced.

## Runtime identity and evidence

`dev-session current` and both environment values matched this session and
`/home/aither/workspace/ai/vpsfree.cz` before investigation. Read-only systemd
inspection identified `workspace-portal@vpsfree-cz.service`, PID 156059.
Its `/proc/156059/exe` and selected profile agree on:

- Package: `/nix/store/a3r70kgqaf46185cjmjgalza67vpg0hd-dev-workspace-0.2.0`.
- Profile: `/home/aither/.local/state/dev-workspaces/profile`.
- Deriver: `/nix/store/7xb8zyd1g0cv5xvlsnlw2lll07c4bn33-dev-workspace-0.2.0.drv`.
- Derivation `env.src`: `/nix/store/pzmrjkkvi3vh0qw649420xk8jw263ilx-source`.

References below are relative to that immutable source. This establishes the
running package's source without assuming that a checkout is deployed.
The scanner, repository adapter, limits and HTTP handler files are byte-identical
to locally available `origin/master` at
`4a002f52c3b55099540aa99708d5fcf29f7b2456`. The Files block of `app.js` also
matches; the complete JavaScript file differs elsewhere. No fetch was performed,
and no exact Git revision is asserted for the entire deployed source tree.
Local `master` is older (`52dcd471186ef874c5c93f4133744195d4815454`) and was
not used as evidence of current Files behavior.

| Location | Evidence |
| --- | --- |
| `portal/internal/session/tracking_files.go:75` | `ListTrackingFiles` recursively walks the current session root using nofollow directory descriptors and `ReadDir(128)`. It includes ignored/unregistered regular files, without Git or content reads. |
| Same file, lines 105–130 | Traversal budget adds each candidate relative path's byte length plus one, including directories and entries later excluded. A separate output estimate counts JSON paths and row overhead. Either exceeding 4 MiB, or accepting a 5,001st regular file, returns the same limit error. |
| Same file, lines 138–144 | Any error returns `nil`, discarding collected paths. Sorting occurs only after complete success. |
| `portal/internal/repository/review.go:24` | Shared review defaults: 5,000 entries, 4 MiB output, 512 KiB preview and 12,000 preview lines. |
| `portal/internal/repository/source.go:120` | `TrackingFiles` borrows review listing budgets and maps `ErrTrackingFilesLimit` to generic `ErrReviewLimit`. |
| `portal/internal/web/server.go:2033`; `source_files.go:277` | `GET /api/sessions/<slug>/files` calls that adapter; limits become HTTP 503 with the quoted error, never partial entries. |
| `portal/internal/web/static/app.js:3731` | `refreshFiles` renders only a successful `payload.files`; its catch displays the error and retains any prior tree. |
| `portal/internal/repository/source.go:74,274,295` | Direct file preview/download opens the selected path independently of listing. Text preview is capped at 512 KiB/12,000 lines; download is capped at 10 MiB and returns HTTP 413 when oversized. |
| `portal/internal/session/tracking_files_test.go:62`; `portal/internal/web/source_files_test.go:707` | Existing tests require nil results/503 for count and metadata overflow, including 5,001 empty files and fewer files with long paths. These tests were inspected, not run. |
| `docs/workspace-portal.md:220` | The documented contract explicitly refuses partial lists. |

## Accepted scope and implementation gates

Implement true lazy browsing of the session tracking directory. Initially show
only immediate root children; directories start collapsed and load direct
children on expansion. Do not recursively scan descendants, prefetch collapsed
subtrees or calculate descendant totals. Do not implement the earlier partial
recursive-listing mitigation; it is superseded by this design. Preserve the
inventory and do not clean, move or exclude the bulky files it identified.

The lead owns initial plan/state and must commit that tracking milestone before
any project-code commit or publication. Implementers own application changes;
this architect-owned brief fixes their shared contract. “Implement the plan”
does not approve merging feature branches or activating packages. The lead owns
rollout preparation, including the user-identified `vpsfree-cz-configuration`
route for aitherdev; preparation must distinguish host configuration from the
user-profile workspace application. No runtime mutation is part of this brief.

## Directory API and confinement

Add `GET /api/sessions/<slug>/directory?path=`. The required, explicitly empty
`path` selects the root; otherwise it is a canonical session-relative directory.
The only other parameter is an optional nonempty `cursor`. Reject missing or
repeated path, repeated/unknown parameters, malformed query encoding and malformed
or oversized cursors with HTTP 400. Validate nonempty paths as canonical UTF-8,
at most 4,096 bytes, with no absolute form, dot/traversal components, backslashes,
controls or `.git` components. The new directory input has no legacy own-root
prefix alias; existing file URL aliases remain unchanged.

Successful response:

```json
{
  "path": "reports",
  "entries": [
    {"path": "reports/browser", "kind": "directory"},
    {"path": "reports/result.md", "kind": "file"}
  ],
  "nextCursor": null
}
```

`entries` is always an array and contains only direct children; `nextCursor` is
null at the end or a continuation string. Paths are session-relative, not
absolute. Empty directories are visible and return an empty array when opened.
No content, file size or recursive count is needed. Set `Cache-Control: no-store`.

Resolve each request against the selected session's current `work` or `archive`
root. Reuse `trackingRoot`, safe-path validation and the existing `openConfined`
nofollow/beneath-directory mechanism; no client or cursor supplies an authorized
filesystem root. Exclude symlinks, `.git` and special files. Preserve ignored and
unregistered regular files and directories. Validate entry type without reading
file contents; selected content requests independently reopen the file through
existing confinement. Do not follow a replaced directory or symlink while paging.

## Alphabetical pages, resources and cursor

The user selected alphabetical pages. Use a fixed **200-entry** maximum page and
**256 KiB** maximum serialized response, including envelope, cursor and encoder
newline. No client-adjustable page limit. Order directories before files, then
compare basenames bytewise in UTF-8, case sensitively; do not use browser locale
sorting. `kind` and basename together are the keyset position.

Scan only the requested directory with `ReadDir(128)` batches. Among eligible
entries strictly after the cursor key, keep the smallest **201** in a bounded
max-heap, then sort that retained set. Never materialize the whole directory or
recurse. Emit at most 200 entries, shortening the sorted prefix if needed to fit
the exact encoded-response budget. Construct continuation after the **last
actually emitted** key whenever eligible entries remain. Account for the cursor
before committing a prefix; do not omit rows silently or return a nonadvancing
empty page. Valid path bounds leave ample space for at least one entry.

Every request rescans that one immediate directory. This deliberately trades
O(immediate children) work per page for useful stable ordering, bounded memory
and no shared snapshot subsystem. It does not scan any descendant directories.
Reuse `ReviewReader.Jobs`'s **four server slots** and the reader timeout convention
with a **four-second** default budget including slot acquisition. Check context
cancellation between batches/entries and before return. Close all directory/file
descriptors on completion, error or cancellation. No directory descriptor,
persistent cursor state or shared listing cache survives a request.

Use a compact, versioned base64url JSON cursor with exactly these fields:

```json
{"v":1,"binding":"<sha256 hex>","kind":"directory","name":"last-child"}
```

The binding is SHA-256 over an unambiguous canonical encoding of workspace,
slug, current `work`/`archive` root, canonical requested directory and generation
(dev/inode, mtime and ctime including nanoseconds). The cursor stores only this
digest and the last basename/type: **do not duplicate the potentially 4,096-byte
parent path** inside it. Limit the encoded cursor to **4 KiB**, decode with strict
shape/version/type validation, and reject unknown/duplicate JSON fields and
trailing input. The name must be one safe basename, not a relative path.

A cursor is an untrusted paging position, never an authorization token. A
signature, signing secret or server-side cursor registry is unnecessary: every
request independently revalidates the session root/path, and a forged position
can only select a position within that authorized directory. Wrong binding
uses the changed-directory behavior below; malformed structure uses HTTP 400.

## Live changes and error behavior

Stat the opened directory before and after scanning, using dev/inode/mtime/ctime
like the existing catalog stamps. Reopen the requested confined path and confirm
it still resolves to that same generation before return. A changed generation,
replacement, work/archive transition or cursor-binding mismatch returns
**HTTP 409**, `code: "directory_changed"`, and a short reload instruction. Do
not append pages from different generations. Content edits alone need not
invalidate directory pages. This is ordinary change detection, not an immutable
filesystem snapshot guarantee.

The UI retains successful rows and selected content on 409, disables the stale
continuation and offers **Reload directory**. It does not repeatedly restart on
its own. Missing/ineligible requested directory returns HTTP 404; timeout or
other scan failure returns HTTP 503 with a local retry notice. Cancellation does
not publish data. A failed scan never masquerades as a complete empty directory
or as a globally sorted partial result.

## Browser behavior

Keep the existing native `details`/`summary` tree and control styling. The root
is implicit and open; each child directory starts collapsed. First expansion
requests its first page, and **Load more** appends the next page locally. Each
loaded directory owns its rows, cursor, expanded/loading/error state and read
generation. Permit **two directory requests** in flight in the browser and at
most one for any directory. Reuse `createReadScope`'s abort and generation checks;
late success/error after cancellation must not alter current state.

Collapsing a directory removes queued requests and aborts in-flight reads for
that subtree, while retaining successfully loaded rows for reopening. It does
not affect the selected file. Hiding the page or leaving Files pauses all
directory reads; return retries only still-needed expanded nodes. No background
traversal. State lives only in the page and disappears on navigation; add no
browser persistence or server cache. Loading, retry and generation-change
messages belong beside the affected directory. Keep the tab label **Files**,
without claiming a total from the subset loaded.

**Refresh** invalidates existing continuation/read generations and refreshes
page one for the root and currently expanded, loaded directory nodes only, at
two requests maximum. Preserve old rows until their replacement succeeds; fresh
page one replaces older pages rather than mixing snapshots. Preserve expansion
for surviving directory nodes; no need to refetch pages solely to rediscover
old rows. Collapsed cached nodes become stale and reload when next expanded.
Do not refresh collapsed descendants or automatically load more pages.

List replacement, paging, collapse and 409 never clear `selectedPath` merely
because it is absent from a page. Refresh re-reads the selected file using the
existing file read/selection guards; actual disappearance shows unavailable and
clears stale actions, while transient errors may keep last successful content
with a notice. Preserve content, editor and selection through ordinary directory
updates. Existing standalone `/files/<slug>?artifact=...` and line links open
known paths directly without enumerating parents. Keep modifier/middle-click
behavior and the existing inline selection UI; add no new inline deep-link state.

## Implementation boundaries and compatibility

Use one coupled implementer if practical. If the lead splits execution, these
file boundaries are independent after accepting the API above:

- Backend package: `portal/internal/session/tracking_files.go` and tests for the
  directory scanner/cursor; `portal/internal/repository/source.go` adapter;
  `portal/internal/web/source_files.go`, `server.go` route and focused Go tests.
  It owns the exact response, ordering, generation and confinement contracts.
- Browser package: `portal/internal/web/static/app.js` client and Files block,
  `source_files_browser_test.cjs`, associated asset-version tests/templates, and
  the Files contract in `docs/workspace-portal.md`. It consumes the fixed API
  and owns expansion, queue/cancellation, refresh and selected-file behavior.

Serialize commits and other Git operations through the lead; route substantive
interface deviations back through the lead/design owner. Keep the standalone
source renderer unchanged unless required for the specified refresh behavior.
Bump the `app.js` asset URL consistently in `session.html`, `index.html` and
`automatic-archival.html`; reuse existing controls before adding CSS.

Keep legacy `GET /api/sessions/<slug>/files` behavior and tests unchanged for
already-open old browsers. The new UI must never call that recursive endpoint.
A separate new directory route prevents an old backend from ignoring a new
query and silently doing a recursive scan. A new browser against an old backend
reports unsupported/reload on 404 or invalid response shape, without fallback.
Bump browser assets with the paired backend deployment.

No persisted schema, database, manifest, journal, CLI, Codex protocol or generic
Nix option change is required. Preview/sanitization and download eligibility
remain unchanged, including 512 KiB/12,000-line text previews and 10 MiB downloads.
No coordinated node/fleet upgrade is needed. Any downstream pin or deployment
preparation is lead-owned and separate from this application package. Actual
integration and activation require their own approval and coordination. Runtime
switches are forward-only; recovery is a forward corrective package, with no
state migration or cleanup of session files.

## Acceptance and verification

- Root note plus a nested directory with more than 5,000 files loads only root
  children. An unreadable unopened subtree cannot fail root enumeration; no
  total-count or collapsed-descendant requests occur.
- An unchanged single directory with more than 5,000 immediate children pages
  completely, exactly once, in directories-first bytewise alphabetical order.
  Cover 0/200/201 entries, long parent paths, escaped/Unicode names, response-byte
  shortening and a compact cursor below 4 KiB without a repeated parent path.
- Add/remove/rename/replace during or between pages and work/archive transition
  produce 409, not mixed pages; direct content edits retain usability. Cover
  malformed/cross-scope cursors, invalid parameters, nofollow handling, `.git`,
  special files, ignored files and empty directories in both tracking roots.
- Resource checks exercise heap/page bounds, four-slot waiting cancellation,
  scan deadline, error exits and descriptor closure. No live workspace fixture.
- Browser contracts verify collapsed defaults, targeted expansion, two-request
  cap/one per node, Load more, collapse/hide cancellation and late responses,
  local errors/reload, refresh without recursive work, selection preservation,
  real missing content and old/new API handling. Direct links never need a tree.
- A large sparse file remains listable; existing preview/download and unsafe
  active-content regression checks continue to pass.

After implementation, use the repository Nix shell. From `portal/`, quick checks:

```sh
go test -mod=readonly ./internal/session -run 'TestTracking(Directory|Files)'
go test -mod=readonly ./internal/repository -run 'Test.*(Source|Tracking)'
go test -mod=readonly ./internal/web -run 'Test(TrackingDirectory|TrackingFiles|SourceFileBrowserContracts|SourceDownloads|BrowserAssetVersions)'
node --check internal/web/static/app.js
```

`TestSourceFileBrowserContracts` already runs `source_files_browser_test.cjs`;
use its existing harness rather than adding a new runner. Required hooks and
quick checks precede final independent review of committed deliverables. After
review, run broader `go test -mod=readonly ./...` and the package check
`nix build .#checks.x86_64-linux.package` from the repository root, plus applicable
repository checks. Delegate long/uncertain verification through the monitoring
skill. Use a disposable live-browser check for native expansion/cancellation
where the contract harness is insufficient. Host VM/lifecycle tests are not
required solely for this browsing change. No implementation checks have been
run as part of finalizing this design brief.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-files-tab-limit-diagnosis/>

## Archive preflight failure: root-cause and diagnostic brief

**Current implementation authority:** the final classifier correction below
supersedes the earlier hypothesis-specific measurement gate. The diagnostic
history remains evidence; no further diagnostic campaign is planned.

The user explicitly expanded scope to diagnose and fix the archive CI defect
before delivery. Deployment stopped before reservation/copy/activation;
integration remains denied. This section governs that necessary correction,
separately from the completed Files design. Architect0 owns cause/design;
implementer0 owns diagnostic instrumentation, application/tests and quick checks.
No live archive, lifecycle mutation, deployment, claims or peer-session access.

### Established evidence and unresolved cause

Exact failed candidate: `dd445cb0627f93375f1378af6b59d30ef8b34875`, based on
`76c9ad4fbd877992464d2a7f2a1a2fe60db043b1`. CI run 40757650687,
archive job 123060773953; log is retained at
`/tmp/files-tab-deploy-verification-dd445cb0-20261028/implementer0-ci-archive-job.log`
(693,149 bytes; strip ANSI for inspection). See implementer0-result.md for the
full chronology. At 19:56:54.769 UTC preparation failed in
`archive_preparation.go`'s raw latest-status default branch. At 19:57:01,
before releasing the held model, the restarted portal reported the SAME accepted
turn `01a18416-45d3-70a3-9b01-2d0ab31a6299` as `inProgress`. Its repair command
then completed with exit 0 at 19:57:02.868 and task_complete at 19:57:03.144.
Thus portal restart did not cause the original failure.

Source proves the generic failure is reached only after the latest turn ID
matches the accepted send receipt. The waiter permits only `completed` or
`inProgress`; every other raw status is declared unsuccessful. Exact unexpected
CI status was not logged. Do not claim it was `interrupted`, `failed`, empty,
or any other value until measured. The existing unit fixture always returns
`completed` and omits live thread status, so it does not cover this boundary.

`test/creation_model.py` creates `archive-repair-entered` before waiting for
`hold-turn` to disappear and before response headers/events are sent. The VM
checks only `operation.phase == lead_fixing_blockers`; a failed operation retains
that phase, so the assertion misses the premature failure and restarts anyway.
The timing proves the turn was intentionally waiting for a model response;
it does not alone distinguish a terminal-history projection from another native
race. Pinned codex-web 5830018 `ReadTurnState` models thread activity separately
from latest persisted-turn status and explicitly warns that observations can
lag. `ActiveTurnID` uses the same raw history endpoint and is not independent
live proof. No helper that resumes a thread may be used merely to observe it.

### Bounded diagnostic execution package

First prefer a small native disposable probe, using the exact selected Codex
0.164.0 package and the existing synthetic-provider/held-response pattern. Give
it isolated temporary home, socket, working directory and state; no registered
workspace or live threads. Record thread/start and accepted turn/start IDs,
then repeated read-only `thread/read` (excludeTurns) and
`thread/turns/list` (latest 1, itemsView notLoaded) snapshots while a response is
held, immediately after release and after completion. Retain timestamps, exact
status fields, accepted/latest IDs and errors only, not full prompts/transcripts.
Stop after the desired tuple is captured, or report inability to reproduce
without adding an arbitrary delay or silently rerunning the same experiment.
Native source/schema from its exact package input may explain the observation;
the source derivation is retained but its source output was absent locally.
Source retrieval is evidence gathering, not a Codex upgrade.

The first isolated probe stopped immediately after first-turn acceptance on
native `-32601`, `list_turns is not supported yet`; it captured no failing
status tuple. Pinned codex-web `Client.Request` has no legacy latest-turn
fallback. Its `initialHistoryPending` recognizes that exact error only during
initial-message persistence. The corrected probe therefore completes and proves
a seed turn before holding the second accepted turn, matching the CI ordering.
It records unsupported history as an observation error, never as a turn status,
and uses the same raw endpoint without a speculative compatibility fallback.
The old evidence remains in `/tmp/files-tab-native-status-probe-dd445cb0`;
the corrected run uses a new exclusive `-materialized1` root. A successful
stdio probe can establish a native mechanism, but absence of reproduction there
does not disprove the managed-daemon/VM failure.

The corrected run completed successfully at 20:17:31 UTC. Accepted repair-probe
turn `01a18429-2177-7dc3-be65-0a2128e2675d` first showed metadata `idle`, raw
latest `inProgress`, then metadata `active`; all held samples remained
`inProgress`/`active`, followed by native completion and raw `completed`/`idle`.
This proves an ordinary metadata-observation lag, not the CI terminal-status
failure. No contradictory terminal tuple was reproduced. Do not repeat the
isolated probe or select a behavior fix from this result; use the exact VM
decision-boundary instrumentation below.

If the small probe cannot exercise the archive race, implementer0 may add narrow
TEMPORARY observation in the existing archive waiter and disposable VM fixture:
log accepted/latest turn IDs, exact raw status, original identity-read status,
and a fresh passive thread metadata status at the decision boundary. Keep the
original result/classification unchanged. Log errors reading the extra snapshot
without replacing the original result. Do not print messages, tool arguments,
credentials or private live state. Assert the held-stage operation is running
as well as lead_fixing_blockers, so the first native mismatch is exposed before
restart. Capture native status on failure and the same accepted turn's eventual
result; do not rely only on the final assertion. This is diagnostic logging,
not a behavioral fix or new persisted receipt format.

Diagnostic ordering: the original metadata sample precedes reconciliation/send
and can predate acceptance. Do not add any read before the raw history decision.
After that raw sample, log a fresh passive metadata read with identity-match
booleans, history mode/status and error; on an unexpected terminal status, one
immediate repeated raw latest-ID/status read can expose a transient projection.
No sleep or result change is permitted. If the fixture detects an early failed
held operation, release only its owned synthetic hold, bound the existing idle
wait to 60 seconds, capture same-turn terminal evidence, then fail the preserved
running-state assertion without restarting the portal or continuing archival.
Added evidence contains IDs, statuses, event names and exit codes, not message
contents or tool arguments. The existing admission context bounds extra reads.

The single instrumented local KVM run completed with exit 0 (native VM script
1,054 seconds; full build about 31 minutes). Evidence:
`/tmp/files-tab-archive-status-vm-dd445cb0-20261028/{build.log,result.json}`;
diagnostic patch SHA-256
`9f4d2a8dc0fe22df68f8c6a68d01e9bfd371e3de82df5a0b99f8c6bda8cbf4b7`.
The repair subtest passed in 160.08 seconds. Accepted/latest turn
`01a1843b-0eca-7021-b505-0bcfdaf3f48a` was `inProgress` at 20:37:05.722 UTC,
with pre-send metadata `idle`, fresh metadata `active` and matching ID/CWD;
it remained `inProgress` through restart and became `completed`/`idle` at
20:37:29.868. No unexpected-status repeat marker occurred. This is
nonreproduction, not a resolved cause or validated fix.

### Next causal capture: one original-runner repair case

The lead accepted one targeted capture on the original CI runner, using the
frozen instrumentation, setup and first repair subtest only. No identical local
rerun, full suite, automatic retry or generalized harness. Implementer0 owns
preparation and execution; verify the original runner identity, supported job
entry and closure availability before triggering it. Do not assume that local
store paths exist on that runner.

Accepted runner limitation: failed job 123060773953 ran on ephemeral GitHub
runner `GitHub Actions 1000001732` (ID 1000001732), Azure eastus,
Ubuntu 24.04.5/image `20261025.353.1`. That machine cannot be selected again.
The lead therefore accepted one fresh GitHub-hosted **ubuntu-24.04** job as the
same OS class, with exact original machine/image equivalence explicitly unknown.
The existing Check workflow has no diagnostic dispatch input. Implementer0 may
add one minimal opt-in input and job gates on a separate diagnostic ref:
run only setup plus the first repair case through the built driver, retain the
600-second test bound, always retain logs, and skip unrelated default jobs.
No automatic retry or default full-suite dispatch. This is temporary diagnostic
delivery, not part of the final product by default; the actual-tuple fix gate
below is unchanged.

Diagnostic-worktree correction: the lead observed that the registered
`dev-workspace` checkout had been switched to the temporary diagnostic branch
while `portal.yml` still registered the feature branch. The resulting
“live worktree ... conflicts with its portal registration” warning is the
intended `MergeActiveRepositories` branch-identity guard, not an established
application bug. Existing `worktrees_test.go` and `details_test.go` cover the
conflict/warning path. Implementer0 alone preserves all three diagnostic diffs,
restores the feature branch at its registered path and prepares a separately
named diagnostic worktree through the existing `worktree add --name ...
--branch ...` helper. Verify both registrations and that the warning clears
before publication. Alternate diagnostic refs must get a separate named
worktree before checkout; do not rewrite the feature registration to silence
the warning. No guard weakening, new registration subsystem or new code test
is required by this operator error. This is separate from the unresolved
archive-status defect.

The built NixOS driver has a supported `--config`/`--output_directory` entry.
Locally verified driver:
`/nix/store/358qlamg9s8mcg60i8d5r7hzz7jvg78d-nixos-test-driver-dev-workspace-session-archive-lifecycle/bin/nixos-test-driver`.
Its config is `/nix/store/m2f5a95lbsi0nfiixfyhw1kb3rns247q-driverConfiguration.json`;
the rendered script is `/nix/store/6kqfljaxkn2x0n50hkl91wjg75bjmgkx-test-script`.
Prepare a disposable copy retaining setup, the first existing repair subtest and
its diagnostic exception handler; omit the six later subtests. Keep the same
packaged runtime/VM and set `global_timeout` to 600 seconds. Command shape:

```sh
<verified-built-driver>/bin/nixos-test-driver --config <private-capture>/driver.json --output_directory <private-capture>/out
```

This selects the existing fixture without rebuilding application code merely
to trim tests. Setup plus the target case took about 216 seconds locally;
expect 4–6 minutes with a hard 600-second test bound and the driver's ordinary
owned-VM shutdown. Use a fresh watcher. Stop after the first captured failure
or first-case completion; a green result leaves the original defect unresolved
and does not authorize another run automatically.

The required missing sample is the rejection's raw status with exact
accepted/latest identity, fresh passive thread identity/activity, immediate
same-ID reread and eventual same accepted turn's terminal event. A raw
`interrupted` followed by matching fresh `active` and/or immediate `inProgress`,
then same-ID completion, would establish an independently reproduced false
terminal observation. Only then design a narrow reconciliation/wait regression;
do not mask `failed`, genuine terminal `interrupted`, unknown status or changed
identity. Stable terminal outcomes must still fail without new send/retry
authority. The original CI raw value remains unobserved even if a matching
mechanism is independently proved. Supplying idle/false directly to native
normalization tests only demonstrates that function, not a reachable CI race.

Long or uncertain native/VM diagnostics must launch through a fresh Luna/low
watcher under the monitoring skill, or an explicitly reported supported fallback.
Implementer0 prepares the exact command, source/native identity, temporary paths,
expected evidence and stop condition; the lead/watcher runs it. Do not blindly
rerun the failed CI job or broad suites. Retain one compact evidence report with
actual tuple/ordering and classify source behavior versus test-fixture exposure.

### Fix boundary and verification contract

The final status decision is intentionally not selected before that diagnostic.
Once the tuple is established, amend this section with the native cause and
smallest local waiter correction. A candidate direction is to distinguish an
exact accepted turn still authoritatively active from an actual unsuccessful
terminal outcome, using fresh passive observations and the existing polling
loop. This is a hypothesis, not permission to poll every failed/unknown status.

Preserve exact accepted-turn identity, submission reconciliation/idempotency,
retained root/CWD/native/receipt admission, cancellation and operator-input
holds. Never start a second repair send or infer new retry/continuation authority
from a status mismatch. Genuine failed and interrupted outcomes, wrong/newer
turn identities, unknown status, missing/cold/unverifiable activity and transport
errors must retain explicit safe semantics. Successful terminal repair must
still be independently followed by archive-check; no early shutdown or lifecycle
journal handoff while the lead works. Restart continues the existing durable
preparation and same receipt, not a new intent.

Expected application boundary is archive_preparation.go plus its focused unit
fixture/regressions and the existing session-archive-lifecycle.nix/model test
only where needed to make the regression meaningful. No generic retry engine,
new persistent status store, arbitrary timing grace period or Codex/package
upgrade is planned. Any source/schema finding that requires a broader interface
change must return through the lead. Compatibility/recovery formats remain
unchanged unless evidence proves otherwise and the lead accepts the revision.

Regression acceptance must include the observed native sequence, completed
repair, genuine failure/interruption, changed accepted-turn identity, blocking
input, cancellation and portal restart with the same durable delivery. Quick
`TestArchivePreparation` checks in the repository Nix environment precede a
fix commit and mandatory final review. The exact repaired candidate then needs
targeted native/disposable archive verification through a fresh watcher; a green
rerun without a causal regression is insufficient. No actual deployment or
integration resumes from diagnostic success alone.

### Native source narrowing (diagnostic, not final causal proof)

The exact upstream `rust-v0.164.0` source is available read-only from GitHub;
its tree moved the processor to
`codex-rs/app-server/src/request_processors/thread_processor.rs` (the older
`codex_message_processor.rs` path is absent). No source checkout/build is needed.

- Lines 3251–3334: legacy `thread/turns/list` reads history, then separately
  samples loaded `agent_status == Running`, listener active-turn snapshot and
  thread-watch status before projecting a page.
- Lines 3396–3464: paginated history reads stored turns then samples live running
  and watch status, applying the same normalization.
- Lines 6246–6259: `normalize_thread_turns_status` changes every `InProgress`
  turn to `Interrupted` unless resolved thread status is `Active`.
- `codex-rs/app-server/src/thread_status.rs:290–303` promotes idle/notLoaded to
  Active when the separately observed running flag is true, documenting listener
  lag as the reason. These reads are not an atomic status/turn snapshot.

This is a concrete source path by which an apparent interrupted turn can be
synthetic rather than an explicit abort event. The original CI default-branch
status and the exact local ordering still require the native probe. Do not
claim source possibility alone proves that CI observed `interrupted`. The probe
must sample immediately after acceptance, not only after provider-entered, and
include historyMode to distinguish the two projection paths.

Source references:
<https://github.com/openai/codex/blob/rust-v0.164.0/codex-rs/app-server/src/request_processors/thread_processor.rs>
and <https://github.com/openai/codex/blob/rust-v0.164.0/codex-rs/app-server/src/thread_status.rs>.

## Final archive classifier correction (accepted by lead)

### Cause established independently of the missing CI field

The hosted diagnostic run 40769502261 at `9270118f` also passed: first repair
case 57.78 seconds, setup/test 94.58 seconds, runner image `20261026.354.1`.
Accepted/latest `01a1845f-daf8-75a2-8fd3-0ebf64d6bd5c` showed `inProgress`
with pre-send `idle` and fresh `active`, then `completed`/`idle`; no unexpected
repeat marker. Artifacts are under
`/tmp/files-tab-hosted-archive-diagnostic-9270118f-20261028/artifacts/`.
Original CI raw status remains unknown. Neither successful diagnostic is a
reproduction or a fix validation.

A local correctness defect is nevertheless established by the dependency
contract: archive preparation decides success/failure from latest-turn history
alone, although native history projection and live activity are separate,
non-atomic observations. Pinned codex-web `codex/turn_state.go` explicitly
represents terminal-history/active-thread disagreement, refuses terminal
continuation authority in that state, and limits `IsLoadedFailedTurn` to
same-ID `failed` with loaded `idle` or `systemError`. Native normalization can
project `InProgress` as `Interrupted`; an accepted turn's metadata can lag,
as all three successful probes demonstrate. The raw-only classifier lacks the
required activity corroboration. This is the proven local decision defect;
the original CI incident is likely the same class, with its exact status and
native ordering still unproved.

### Exact observation and decision matrix

Keep pre-send identity/CWD validation, admission/message locks, reconciliation,
receipt persistence and all holds unchanged. Replace the raw latest-turn
request in `archiveRepairClient`/the waiter with the existing passive
`ReadTurnState(context.Context, string) (codex.TurnState, error)` method.
It performs metadata then latest history without loading/resuming the thread.
No codex-web change or new observation service is needed.

1. Require a nonempty accepted receipt turn ID. After `ReadTurnState`, require
   exact thread ID and exact latest turn ID equal to that receipt **before**
   considering any activity. Missing/changed identity is unverifiable, never
   completion or a reason to send again.
2. Validate `state.Status`: only `idle`, `active`, `systemError` are loaded
   observations. `notLoaded`, empty or unknown status refuses as unverified,
   including when latest history says `inProgress`. Validate latest status as
   one of `inProgress`, `completed`, `failed`, `interrupted`; the helper already
   validates these, but a test double must not accidentally bypass the policy.
3. `inProgress` with any allowed loaded status keeps the existing poll/input
   checks. In particular, `idle` or residual `systemError` cannot override
   positively observed in-progress history. No extra post-history metadata read
   is needed on this path.
4. For each `completed`/`failed`/`interrupted` candidate, take one fresh passive
   `ReadThreadMetadata(..., true)` **after** the history sample. Require exact
   thread ID and CWD again. Validate its status against the same three loaded
   values; `notLoaded` or unknown refuses even if the earlier value was active.
   This brackets a terminal candidate because the helper's first metadata
   sample can predate the observed native activity change.

Once all identity/status validation has passed:

| Latest history | Helper activity | Fresh activity after history | Decision |
| --- | --- | --- | --- |
| `inProgress` | `idle`, `active` or `systemError` | Not requested | Pending; existing poll/input checks |
| Any known terminal status | Either observation `active` | Both observations loaded/valid | Pending; existing poll/input checks |
| `completed` | `idle` | `idle` | Repair complete; existing input check then archive-check |
| `completed` | Neither active, either `systemError` | Loaded/valid | Refuse inconsistent success; no shutdown or retry |
| `failed` or `interrupted` | `idle` or `systemError` | `idle` or `systemError` | Existing unsuccessful-repair failure |

`systemError` is a loaded error condition, not success and not a blanket reason
to poll. It can persist after a failed turn, as the pinned client documents.
Both stable `failed` and stable `interrupted` therefore still fail promptly;
an active observation postpones classification only until a later loaded
inactive observation. These samples are conservative corroboration, not a
claim of an atomic native snapshot. Unknown/cold/identity errors never become
pending work merely because another field says active.

All pending and completed paths still execute the existing blocking-prompt
check. Blocking input refuses preparation; cancellation exits without marking
it failed, as before. Propagate read/transport errors into the existing error
handling unchanged, including its established bounded delivery reconciliation;
add no retry counter, grace period, automatic continuation or new submission.
Retain the two-second polling interval and release admission locks between
iterations. Only successful repair followed by the ordinary archive-check can
handoff to lifecycle execution.

### Implementation and verification package

Implementer0 owns one coherent product commit after `dd445cb0` in the original
registered feature checkout. Keep diagnostic `9270118f` separate. Expected
files: `archive_preparation.go`, its focused tests, the held-state assertion in
`session-archive-lifecycle.nix`, and a short rationale in the existing archive
recovery guide. Do not carry the temporary workflow, per-poll sampling, duplicate
history query or diagnostic release/wait branch into the product.

Retain one compact useful diagnostic when a terminal candidate is refused:
accepted/latest ID, raw latest status, before/after activity (or explicit
unavailable), and the refusal category. Quote values; do not log messages,
tool arguments or native error payloads. Reuse the actual decision observations;
perform no extra requests solely to log. Preserve the existing user-facing
unsuccessful-repair message; distinguish unverifiable/inconsistent success
through the existing error conventions. No persistent format or browser API
change is required.

Deterministic unit regressions must exercise the waiter with scripted passive
observations, not claim an actual native scheduler reproduction:

- Same-ID `idle`/`interrupted`/fresh `active`, then `inProgress`, then
  `completed`/`idle`: exactly one send; no failed preparation or archive handoff
  while active; ordinary archive-check runs after confirmed completion.
- Helper `active` with terminal history and fresh `idle` remains pending for
  that iteration, then resolves on the next sample. Cover `completed`, `failed`
  and `interrupted`, especially active `failed` becoming inactive `failed`.
- Stable inactive `failed` and `interrupted` fail for idle/systemError
  combinations; `completed` requires both idle and refuses systemError.
- Changed/missing thread or accepted latest ID, fresh CWD/ID mismatch,
  notLoaded/unknown status and read errors refuse. Cover cold `inProgress` too.
- Existing cancellation, blocking input, lost-delivery reconciliation and
  restart preserve one delivery and the same durable receipt. No new native
  send is authorized by an activity/history disagreement.

Retain the VM check that the held operation is **running and
lead_fixing_blockers before restart**, using one captured operation snapshot.
Quick checks in the repository Nix shell use focused `TestArchivePreparation`
tests (and relevant compile/interface checks), Nix/Python syntax for the changed
fixture and `git diff --check`. After quick checks and the coherent fix commit,
the retained independent reviewer assesses this matrix and complete branch
scope. Then run the targeted native/disposable archive acceptance through a
fresh watcher. No more diagnostic campaign; a green acceptance validates the
corrected contract while retaining the historical uncertainty. No dependency
upgrade, receipt/journal migration, merge, deployment or pin change is included.
