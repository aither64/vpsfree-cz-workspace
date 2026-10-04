# R1/R2 recovery remediation

Stable source barrier on runtime base
`edcfc18f2fdc3bdebfec7089e2bd79b2d9b918b1`. Application edits are uncommitted;
the index is empty. All 15 changed application paths below are frozen for the
coordinator's formatting, quick checks and prose pass. No member checks ran.

## Completed behavior

R1 retains renamed preparation records with a private confirmation obligation.
Confirmation reads the exact published record and syncs its required parent
directories before another transition or acknowledgment. Completed mapping
moves remain unconfirmed until both directories sync; receipt retirement waits.
The private attempt bookkeeping distinguishes pending, dispatched and stopped
work. Healthy replay launches a pending attempt once with its original receipt
and attempt. A stopped worker exposes existing paused/failed progress instead
of rerunning naming. Explicit retry preserves its published base/reservation.
Startup retains paused/explicit-retry semantics and generation validation.

The fixed request-bound 503 code is `preparation_persistence_unconfirmed`.
GET does not acknowledge an accepting intent whose attachment claim is still
incomplete. Once an incremented retry attempt is confirmed, GET exposes the
current matching receipt/attempt with a usable retry offer; that pending attempt
is dispatched without incrementing again. No new persisted or receipt schema.

Upload claim replay confirms existing catalog file/directory durability under
the catalog lock. Collection aborts on unconfirmed writes. A pending accepting
intent is confirmed and its attachments claimed before collection can expire
them, while dispatch remains pending. The coordinator's collector edge is
covered with a real nonempty completed upload and healthy collection after
eight days, proving preserved bytes, exclusive ownership and one later launch.

R2 offers Start a separate request after an attempted failure, beside recovery.
Its no-opener tab loads the current form without transferring text, settings,
files, scope or body and without submitting. Copy saved text uses the existing
copy handler. The original may still complete and remains immutable/recoverable.
The frozen helper resends after GET only for 404 or the exact saved-ID bound
persistence 503; ordinary/mismatched errors do not authorize another POST.

## Changed paths and proposed logical split

Backend durability: `portal/internal/uploads/{store.go,preparation_test.go}`;
`portal/internal/web/{preparation.go,preparation_store.go,preparation_test.go,server.go}`;
backend durability/retention paragraphs in `docs/session-preparations.md`.

Browser recovery: `portal/internal/web/preparation_browser_contract_test.cjs`;
`portal/internal/web/static/{app.js,preparation.js}`;
`portal/internal/web/templates/{index.html,creation.html,session.html}`;
`test/{creation_browser.cjs,README.md}`; browser paragraphs in the same owning doc.
The frontend group includes the bound-503 consumer and required asset versions.
The coordinator owns later consolidation into the corresponding unmerged units.

## Pending quick checks

Run from the runtime worktree in the prepared environment. These selectors
select six new web groups, the new upload group, and registered HTTP/Node cases:

```sh
nix develop /tmp/automatic-session-slugs-runtime-env -c env TMPDIR=/tmp GOWORK=off go -C portal test -mod=readonly ./internal/web ./internal/uploads -run '^Test(SessionPreparation(Published|StoppedWorker|MappingConfirmation|PendingConfirmation|AcceptingUpload)|PreparationUploadPublished|ShippedBrowserClientMatchesSessionAPI|SessionPreparationIndexMakesOnlyNewSessionNameOptional|SessionPreparationPageHasExplicitIdentityAndEscapedRawPrompt)' -count=1
nix develop /tmp/automatic-session-slugs-runtime-env -c node portal/internal/web/preparation_browser_contract_test.cjs
nix develop /tmp/automatic-session-slugs-runtime-env -c node --check portal/internal/web/static/app.js
nix develop /tmp/automatic-session-slugs-runtime-env -c node --check portal/internal/web/static/preparation.js
nix develop /tmp/automatic-session-slugs-runtime-env -c node --check test/creation_browser.cjs
```

The pure preparation suite now has 19 cases, with controls for stale 409+404,
lost response, bound-503 mismatch, identical-body repair, retained original
selection/envelope, current separate drafts and restored attempted drafts.
Go faults occur after actual file rename, including accepting/running admission,
retry, base/reservation/failed worker outcomes and mapping replacement/move.
Repeated faults, healthy confirmation, exact identity, one naming dispatch,
generation refusal and collection retention are asserted. Exhaustive filesystem
fault conformance is outside this bounded remediation.

The actual Playwright fixture adds stale and ambiguous-outcome separate-tab
cases: no opener, new ID/scope/current catalog, deliberate reattachment, saved
text copying, old selection retention and independent old recovery/completion.
It is written but unexecuted. Mandatory changed-head review still precedes
browser/binary/integration/race/package/VM release gates. No model isolation,
live completion, publication or deployment claim. No material design deviation.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/)

## R1-GET follow-up

The preceding barrier describes the original R1/R2 checkpoint. This bounded
follow-up starts from clean runtime head
`0ed3237557d1cac494b39234c1a0ae455fb6cee6` and changes only
`portal/internal/web/preparation.go` and
`portal/internal/web/preparation_test.go`. The edits are uncommitted, the index
is empty, and both source files are frozen for coordinator formatting/checks.

GET now captures the record, attempt-work bookkeeping and existence under the
same transition/upload/operation locks that confirm durability and classify
acceptance. Response projection consumes that captured value; it cannot adopt
a later accepting intent from a fresh preparation lookup. Published input/team
snapshots are immutable and replaced rather than mutated. Existing receipt and
session identity checks remain in the shared projection. Other status callers
retain their existing read behavior, and generation checks and lock order are
unchanged. The source comment records this invariant; no product/API/schema
or documentation contract change is needed.

Two new top-level test groups cover four leaf cases. The deterministic delayed
admission case captures an absent GET snapshot, then runs a POST that really
renames its accepting record before an injected directory-sync error. The old
snapshot remains absent; fresh API and HTML GETs return the bound 503 even after
sync succeeds, until the identical frozen POST finishes admission with the same
receipt/attempt and one naming call. Three snapshot controls retain confirmed
record/work projection for pending, dispatched and stopped work despite a later
worker-state update. No test callback or concurrency framework was added.

`git diff --check` passed. The prepared-environment formatting command failed
before execution with the existing native sandbox refusal:
`error: cannot connect to socket at '/nix/var/nix/daemon-socket/socket': Operation not permitted`.
No Go test or formatting result is claimed; no bypass was attempted. Coordinator
commands, from the runtime worktree:

```sh
nix develop /tmp/automatic-session-slugs-runtime-env -c gofmt -w portal/internal/web/preparation.go portal/internal/web/preparation_test.go
nix develop /tmp/automatic-session-slugs-runtime-env -c env TMPDIR=/tmp GOWORK=off go -C portal test -mod=readonly ./internal/web -run '^TestSessionPreparation(GETSnapshotDoesNotAcceptDelayedIntent|StatusSnapshotKeepsConfirmedRecordAndWork)$' -count=1
```

The selector names both new groups and selects four leaf cases. Existing
`^TestSessionPreparation` coverage remains the owning regression suite. Any race
check belongs to the coordinator's fresh watcher. No commits, dependency/pin
changes, browser/binary/integration/VM checks or lifecycle action were performed.
