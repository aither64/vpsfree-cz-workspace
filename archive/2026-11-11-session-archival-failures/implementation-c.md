# Package C: archive preparation retries and actionable status

Owner: implementer0. Scope: accepted design C, plus the architect/lead-approved
restoration of the semantic preparation phase after portal restart. No deployment,
merge, push, live archive recovery, service stop or monitor resolution was performed.

## Result

Typed runtime-lock contention leaves the original preparation active and durable.
Each attempt releases admission locks before waiting 100 ms, doubling to a
two-second cap. Waiting has no total deadline, consumes no model repair or
no-progress rounds, and preserves the receipt, attempt, message, options and
accepted delivery. Every admission retains generation/provider/target/identity
checks; the wait also checks cancellation and the current receipt. Only
`EAGAIN`/`EWOULDBLOCK` returned by `LockRuntimeShared` is retryable. An action's
own errno, permanent refusal or failed durable save remains an error.

The existing preparation `Error` records the waiting reason. Session status and
the response-only operation view expose it; successful admission clears it.
Restart-paused preparations restore `checking`, `rechecking` or
`lead_fixing_blockers` through the guarded existing update, after verifying the
same running request. This keeps the waiting reason and Cancel presentation
available after restart without restoring canceled/replaced preparations.

The browser shows the first exact blocker, directs the user to resolve it and
retry, and says registered-service cleanup has not started. It points to
Resources → Services without claiming that unknown services are stopped.
The three-round no-progress limit and readiness-before-cleanup ordering remain.

## Owned files and documentation

- `portal/internal/web/archive_preparation.go`: bounded admission wait and
  guarded restart phase restoration; existing persisted schema/states retained.
- `portal/internal/web/archive_preparation_contention_test.go`: real disposable
  runtime/transition locks, durable wait reason, accepted repair/restart identity,
  cancellation/generation/target refusal, action-error and persistence boundaries.
- `portal/internal/web/{operation_state.go,server.go}`: current waiting reason in
  existing status/view projections, including when a cached snapshot is older.
- `portal/internal/web/{static/app.js,browser_contract_test.cjs}`: actionable
  blocker and pending service cleanup presentation.
- `docs/session-archive-recovery.md`: maintained runtime recovery documentation
  for operators; covers wait/restart behavior, blocker action and cleanup ordering.
  The README already links this guide. The lead applied the required direct
  writing pass before commit; UI/wait strings were retained, doc wording refined.

No schema, migration, API request contract, system/configuration pin or session
authority helper changed. Older preparation readers use the same fields/states;
older monitor records and their recovery policy are owned by package D.

## Verification

All language tools came from the repository's `nix develop`. Fixtures used
temporary workspace/state/profile/authority paths, never live session data.

Focused Go selector:

```sh
go -C portal test -mod=readonly ./internal/web \
  -run 'TestArchivePreparation|TestLifecycleOperationErrorsAreBoundedAndHideCommandInvocation|TestLifecycleSnapshotGETDoesNotWaitForGenerationOrReceiptMutex' \
  -count=1
```

- Initial run failed on a new fixture's absent transition-lock file. The fixture
  now creates that mode-0600 file; this was test setup, not a runtime defect.
- The corrected run passed in 18.235 s (`/tmp/session-archival-c2.log`).
- After the approved restart phase correction, the same known-quick selector
  passed inline again in 18.343 s (tool session `86316`, exit 0). This input is
  the final committed C code/test; the browser inputs were unchanged since their
  successful unit check.

The Node presentation contract passed with the existing unit mode, actual pinned
shared module, and its expected package working directory:

```sh
nix develop --command bash -c 'cd portal/internal/web
node browser_contract_test.cjs --unit http://127.0.0.1 /home/aither/go/pkg/mod/github.com/aither64/codex-web@v0.0.0-20261108185431-dd90fb4308ba/conversation/assets/conversation.js'
```

Earlier Node invocations omitted the required URL/unit selector, shared module or
package CWD and failed in harness setup before completion. Those setup failures
did not warrant production changes or another Go rerun. Full first/second batch
logs: `/tmp/session-archival-c1.log`, `/tmp/session-archival-c2.log`.

Fresh native watchers used the installed catalog's Luna/low utility selection for
those two batches; they were not registered runtime monitor operations. The
second watcher could not independently inspect its launch-policy correspondence;
do not treat this as a registered watcher receipt/proof. All their tool sessions
finished. Final known-quick checks ran inline under the parent.

`gofmt`, `node --check portal/internal/web/static/app.js`, and `git diff --check`
passed. The declared hook-framework search found none; canonical hooks contained
only samples, with no `core.hooksPath` override. No hook was bypassed.

## Commit and review handoff

Initial repository base: `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
Package D predecessor: `3a0af7ad6b97ae4a3a7e38921beac8a2cdf9ff54`.
Initial unpushed C commit `4db1c975f8b707956267a7aa0cb9b20d126e4016` was amended
under the lead's exclusive C window to include the bounded restart fix.
C head accepted before C3: `359636df4e38b3f8c4049eb7e894c3c5eeca2625`; seven files changed,
388 insertions and six deletions, including 269 lines of focused concurrency
tests. The project worktree and index are clean. The commit window was explicitly
released to the lead after commit/status proof. No feature push was performed.

The intended whole branch contains two independent logical commits: D's new
terminal-report acceptance boundary, then C's preparation retry/status change.
No database or file-format migrations exist; no obsolete pin stream or
transitional migration requires retention. At this original C handoff, no C
history had been pushed, deployed, released, merged or externally consumed. The
superseded local C head was consolidated by amendment before final review.

The lead owns packet acceptance and independent final review. Longer packaged
archive-lifecycle/VM checks follow that review; no such test or deployment has
been performed by C. Component tests do not prove the installed lifecycle path.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/).

## Packaged VM follow-up (C3)

The lead-owned exact-head local batch at `359636df` exited 1. Failure derivation:
`/nix/store/iaaixc0lpin9lvxhwzp9lvw5minsy63r-vm-test-run-dev-workspace-session-archive-lifecycle.drv`.
Logs: `/tmp/session-archival-local-359636df.14txHw/{build.log,archive-vm.log}`.
This package inspected those retained logs and source only; it did not rerun,
signal or interrupt the original operation.

The first browser fixture failed at `archive_lifecycle_browser.cjs:87` with
`page.waitForResponse: Timeout 30000ms exceeded`. No archive request had been sent:
diagnostics recorded phase `open page`, no operation GET/POST, no lifecycle reads
and no browser page errors. The real page, app.js and conversation.js returned
200, while eight asynchronous conversation dependencies were still pending.
The waiter was armed at 6,490 ms, navigation began at 6,515 ms and settled at
34,091 ms, and hydration timed out at 36,543 ms. Cold navigation consumed 27.6 s
of the shared 30 s readiness wait, leaving about 2.4 s for asynchronous imports.
This failure preceded C's archive preparation logic; it does not establish a
runtime archive failure or a permanent loading deadlock.

Architect0 approved the smallest scoped correction: retain the prearmed real
response waiter and set only its initial timeout to 60,000 ms, covering the
existing 30 s navigation allowance plus 30 s module hydration/first response.
Two nearby comment lines explain the allowance. Navigation, control and POST
deadlines, exact GET predicate, `hydrated.ok()`, accepted-202, page-error and
all native/archive assertions remain unchanged. No production, Nix, schema,
recovery or documentation behavior changed; no new helper/framework was added.

Quick checks: repository `nix develop --command node --check
test/archive_lifecycle_browser.cjs` and `git diff --check` passed. The one-file
diff has three insertions and one deletion. Node syntax is not behavioral VM
proof; the existing packaged archive VM remains the required verification after
review and lead rerun direction. If the 60 s gate still expires, preserve its
diagnostics and stop rather than repeatedly raising its deadline.

The lead accepted this bounded fixture correction and granted an exact-file
amend window. Final C3/C head: `79700e46361543dbc399647a218671d7ad4b55e1`, with
unchanged D parent `3a0af7ad6b97ae4a3a7e38921beac8a2cdf9ff54`. The exact delta
from previously reviewed/published head `359636df` changes only the three
insertions and one deletion above; all prior C and D content is retained.
The project worktree/index are clean and the commit window was released. This
implementer performed no push. Per the lead, the branch remains unmerged and
undeployed; the lead owns the affected independent review, publication and
existing packaged archive VM rerun. No new migration or compatibility boundary
was introduced by the amendment.


## P2: direct CI observer and accepted archive integration (2026-11-13)

Current implementation base is `eabb56a278bd8eb1759041467eaebfa6392ddcb2`.
P1 component checkpoint `269e2e92849f7920b59cb1817beee4fdd9fe0a17` is
unpublished and depends on P2's exported web target/receipt adapter. Root requires
one coherent final commit, preserving that checkpoint and incorporating P1's
source-only canonical lifecycle-ID and startup-marker corrections. No final
index/commit window has been used by P2.

P2 owns the existing worker's direct GitHub adapter, positive owned process-group
join proof, browser preparation/readiness integration, admitted CLI parent FD
handoff, read-only archive-check projection, related tests, archive VM fixture and
three lead-reviewed docs/skill passages. The existing runner entry points retain
their behavior; the new detailed entry point retains raw wait/cancel/pipe/group
proof. Only a fixed run-attempt GET is allowed. Poll intents bind operation,
source, owner epoch and original live handle; lost ownership remains unknown.
Joined local reads do not imply terminal remote CI. Accepted archive detachment
spends no model repair/no-progress rounds and preserves ordinary readiness,
resource/native/target checks before cleanup. Pending CLI joins release both
creation and exclusive session locks, then fully revalidate the same request.

Development checks (all repository Nix environment, disposable state only):

- Tool70970: `go -C portal test -mod=readonly ./internal/processgroup
  ./internal/web -run 'TestRunDetailed|TestMonitorCI' -count=1` passed
  (helper2.068s, web0.129s), before later integration tests were added.
- Tool98833: initial integrated `./internal/web -run
  'TestMonitorCI|TestArchivePreparation' -count=1` failed18.595s in exactly
  `TestArchivePreparationDetachesQueuedCIWithoutRepairAccounting` and
  `TestMonitorCIWorkerQueuedArchiveAndLostOwner`, both with
  `observer archive authority requires exact accepted identities`. Real archive
  IDs are64 lowercase hex; P1's archive validator wrongly used monitor-ID rules.
  Root authorized the narrow validator/allocator fix; no fixture assertion was
  weakened. Ruby syntax passed before this batch stopped on Go failure.
- Tool35491: after P1's source-stable canonical64 fix, reran only those two exact
  cases with an anchored selector; passed0.434s, exit0. Own native terminal
  receipt at2026-11-13T12:50:15.142Z confirms completion; no repeat for lost output.
- Tool83224: a split-file Ruby invocation failed in harness setup (missing shared
  `NullTmux` and archive-cleanup helpers). No production conclusion or source
  repair followed from this invocation error.
- Tool53940: corrected entrypoint `ruby -Itest -r ./test/dev_session_test.rb
  -e '' -- --name '/test_(monitor_|cli_preserves_exact_operation|
  cli_refuses_changed_action|native_binding_refuses|solo_monitor_preflight|
  collects_loose_files_without_quiescing|archive_reader_|fresh_archive_reader|
  readonly_checkout_cache|ready_check_does_not_pin)/'` passed14 tests,
  200 assertions in3.913s. New parent tests are required by the normal aggregate
  entrypoint as well. The actual selector has no whitespace/newlines.

Host web tests explicitly set `DEV_WORKSPACES_CODEX_PROVIDERS` to the verified
absent `/tmp/session-archival-p2-no-providers`, preserving package catalog
isolation; Go uses `-mod=readonly`. Nix's dirty-source and renamed-system warnings
are environment notes, not failures. Every listed command is terminal/joined.

The packaged fixture extends the existing real archive/repair/restart scenario
with a synthetic exact queued GitHub run. It keeps the registered portal's actual
argv/environment and injects only its existing `--gh` executable option, verifies
runtime ownership without a native launch record, requires durable joined and
detached proof before genuine model repair, then checks unchanged queued snapshot,
no events, no surviving local request and no poll after archive/revival across an
ordinary poll interval. Packaged VM execution remains deferred until committed
independent review. A16 retained daemon-start MCP cutover acceptance is P1's
existing host/live-switch fixture, by direct ownership coordination.

No live monitor/session/CI mutation, deployment, merge, claim, helper cutover or
package selection was performed by P2. Final quick-input identity, final manifest,
compatibility/history inventory and commit receipt follow below when complete.


### P2 documentation, compatibility and final input boundary

| Topic / reader | Authoritative home | Preservation / evidence |
| --- | --- | --- |
| Monitor selection and acknowledged ownership / agents | `skills/dev-session-monitor/SKILL.md` | Runtime-owned existing GitHub reads route before native utility selection; retained native operation IDs, native-only utility policy/reporting, missing-proof refusal and member fallback preserved. |
| Managed observation and status / developers | `docs/dev-sessions.md` monitor section | Direct/native distinction, exact source and acknowledgement, local attestation digests, pending local shutdown and explicit archive authority. |
| Local readiness and archive recovery / operators | `docs/session-archive-recovery.md` | Read-only typed state; durable detach does not assert terminal CI or cancel it; complete current resource admission, unchanged journal/native/file-removal ordering, lost handles remain unknown. |
| Runtime contracts, capability gate and policy-2 ordinary helper cutover / operators | P1's `docs/workspace-portal.md`, `docs/workspace-updates.md` | P1 owns schema/policy and retained-helper acceptance; P2 binds those exact source inputs rather than altering host policy. |

Root completed the prose pass on all three P2 docs/skill paths and accepted the
additional exact-incarnation error string `Monitor observation owner changed.`
unchanged. Entry-point links already exist; no new specialist documentation tree
or individual rollout record was added to project docs.

The native schema1 record and original receipt/report bodies retain their old
contract. New observer records use their separate schema1 directory with the two
explicit observer capabilities; P1's source/activation guards refuse a target
that could ignore that directory. There is no database migration, native receipt
rewrite, destructive down-conversion or supported automatic rollback to an
observer-unaware package after first use. Forward upgrade with absent observer
state creates no observer obligations. Existing preparation schema/states and
ordinary target, generation, resource, native and recovery invariants remain.

P2 final18-file map: `/tmp/session-archival-p2-final-files.json`,
SHA256 `5bea46e6d338544d1aa3117965a509b997f34630b767db1b0632f735592e9e0a`.
P1 final30-file map: `/tmp/session-archival-p1-a16-files.json`,
SHA256 `dd1118ba77cd22f0f48cc893f031a105c41e1e4ff72c02f2fca48bdf73b0c4c7`.
The maps are disjoint; together they exactly enumerate the complete base-to-final
source delta, including untracked new sources. Needed final runtime-contract
bytes SHA256 `1f8b91d7e2a587912c7e8b8cb094e754ff2f156837d8bc6ccfbafe2daf26ea5f`
select live package-switch policy2 and reporting policy3. P1's full manifest and
own targeted evidence cover its core/caller/capability changes; P2's related final
batch compiles the joint CLI and directly exercises its archive integration.

Current series is one component checkpoint269 on base eabb, plus intended
unstaged final sources. No A14 commit was published, merged, installed, deployed
or externally consumed. Root's final joint window must retain exact269 as a
checkpoint and amend it with the complete final map, leaving one coherent
buildable commit on eabb. No obsolete pin stream, transitional migration or
intermediate source boundary needs retention in that final series. Earlier
merged/deployed eabb ancestry is preserved.


### Final P2 quick batch and ready-for-joint-commit packet

Tool59972 joined exit0. Exact command: `nix develop --command python3
/tmp/session-archival-p2-final-checks.py`, complete output
`/tmp/session-archival-p2-final.log`. The batch itself took55.384s, known-quick
inline; no long check or VM was launched. Results:

- `go -C portal test -mod=readonly ./internal/processgroup ./internal/web
  -run 'TestRunDetailed|TestMonitorCI|TestMonitorPortal|TestArchivePreparation'
  -count=1`: helper2.055s, web19.593s, passed. This includes original worker
  scheduling/shutdown, same-source separate handles, queued/running/terminal/API
  failure truth, pre-start quiescence, lost-owner restart refusal, exact archive
  admission/refusal and repair accounting, plus existing contention/cancellation.
- `go -C portal test -mod=readonly ./cmd/workspace-portal
  -run TestMonitorArchive -count=1`: passed0.185s against final P2 web adapter and
  P1 canonical64/policy2 inputs; full core was not redundantly rerun.
- Repository Ruby aggregate entrypoint, same focused selector as above plus
  `explicit_archive_shutdown|explicit_threadless_archive|
  committed_archive_discards|automatic_archive_projects`: passed19 tests,
  308 assertions in16.429s. This adds normal explicit/threadless/committed and
  automatic archive paths to the new inherited-FD/pending/projection coverage.
- Ruby syntax for both changed executables, new parent fixture and aggregate
  entrypoint; Node syntax for existing shipped browser/VM driver; Nix parse and
  generated VM Python/GH/capture/exec launcher syntax; owned Go formatting;
  diff check: all passed.

The batch verified the18-file P2 map unchanged before/after and preserved exact
compiling P1/core/CLI/native-contract inputs in
`/tmp/session-archival-p2-final-dependencies.json`. After joining, all48 final
source files still match the disjoint P1+P2 maps; complete base-to-working-tree
`git diff --check eabb... -- <48 paths>` passes and the index is empty.
Combined map `/tmp/session-archival-a14-combined-files.json` SHA256
`c6701ebd6a0d20590c64792cc0beadfdbf11dacecb7a9dc4da7b1d094f6296fa`.
Runtime repository declares no hook framework; no active non-sample canonical
hook or `core.hooksPath` override was found, and no hook was bypassed.

P2 is ready for the root-authorized final joint amendment window. All P2-owned
commands and reporting cells have joined; there is no owned verification still
running. Remaining work: preserve component269, amend one coherent complete
48-file A14 commit on eabb under root's explicit window, then root-owned committed
independent review and post-review packaged/native checks. No publication,
activation, live archive/monitor action or integration is included in this packet.
P2 retains ownership of review fixes; capacity is available after acceptance.


### Final coherent A14 amendment receipt (implementer0, 2026-11-13)

Root accepted both complete manifests and released the exclusive final runtime
index/commit window. Component `269e2e92849f7920b59cb1817beee4fdd9fe0a17`
was preserved by atomic create-if-absent at
`refs/checkpoints/2026-11-11-session-archival-failures/a14-p1-269e2e92849f`.
A collision would have required that exact same object; no foreign ref was
replaced. All original merged eabb ancestry and older reviewed/built refs remain.

Only the approved combined48 paths were staged. Ordinary repository Nix Git
`commit --amend -F <temporary-message>` produced:

- Final head: `b9b408710e5c20ffa470afde10e4f7afc33919d2`.
- Final tree: `2c6e10d1104a9fc942088a5872694b2a35d6b788`.
- Sole parent/base: `eabb56a278bd8eb1759041467eaebfa6392ddcb2`.
- Complete base-to-head count:1; final scope48 files,4546 additions/131 removals.
- Combined approved manifest SHA256:
  `c6701ebd6a0d20590c64792cc0beadfdbf11dacecb7a9dc4da7b1d094f6296fa`.

Every committed blob and working file matches the approved map. The exact
base-to-head changed-path set equals those48 paths; whole diff check passes.
Existing modes are unchanged;14 new source/test files are100644. Final index and
working tree are clean, including untracked-file inventory. Repository hook
framework search, default `core.hooksPath` and non-sample-hook inventory remain
empty; no hook was bypassed. The first missing-checkpoint probe used `show-ref`
without `--quiet` and exited128 before any mutation; the corrected documented
quiet probe returned absent, then atomic create succeeded. This was command
setup only, with no source/index/commit uncertainty. The amendment command and
all verification cells joined exit0.

The final series contains the complete P1/P2 implementation and narrow source
fixes in one buildable logical commit, rather than retaining the incomplete
component or follow-up fix streams. New persisted state is separate observer
schema1 under explicit observer-state/lifecycle capabilities1+1; native schema1
receipts and historical reports remain unchanged. No database migration, eager
conversion, destructive downgrade or intermediate externally consumed A14 format
exists. Final live-switch policy2 requires ordinary helper cutover for the new
MCP surface; reporting policy3 and native/package interfaces are preserved.

Previously passing quick evidence applies to identical final source bytes.
No test/build rerun, publication, deployment, merge or live lifecycle/monitor
mutation was performed in this commit window. Exact machine-readable receipt:
`/tmp/session-archival-a14-commit-receipt.json`. Source/index/commit window
released to root immediately after joined clean proof. Independent final review
and post-review packaged/native verification remain root-owned; implementer0
retains P2 review fixes and has available capacity after acceptance.


### R9 bounded P2 remediation (2026-11-13)

Reviewed head `b9b408710e5c20ffa470afde10e4f7afc33919d2` and original maps,
R9 report and component269 checkpoint remain preserved. Root released source-only
changes to exactly `portal/internal/web/monitor_ci.go`, `monitor_ci_test.go` and
`test/dev_session/deletion_lifecycle_test.rb`. Root separately returned the skill
with its numeric direct-source wording; no other P2 doc/source was changed.

The adapter now calls P1's single `ValidateDirectCISource` grammar. It first
verifies the exact operation/source/poll/owner-epoch binding, derives its existing
deterministic call handle and registers only that original call. After the
current-admission recheck, an argument or admission refusal before Start returns
joined/finished proof with no exit status. The existing worker metadata commit
persists it without process/API execution, remote snapshot or event. Missing or
mismatched binding, duplicate calls and genuine lost-owner state retain their
unknown fence. No blanket error-to-joined conversion, registry adoption, new
receipt schema or processgroup behavior was introduced.

The worker/store regression includes a faithful historical direct record whose
named workflow passed the old generic grammar; unchanged exact replay succeeds,
then the original worker positively refuses Start and durably saves unsent proof.
A second case changes admission after Claim but before Start. Separate source,
epoch and duplicate negatives do not acquire proof. Existing lost-owner/restart,
separate-handle, context/pipe/group and fixed-GET tests remain in the selector.

Ruby production deletion is unchanged. Two tests run the ordinary disposable
`Runner.delete`: readiness precedes any delete journal, then its existing revoke
and archive calls retire monitoring under ordinary deletion authority; completed
removal retains its normal private recovery record. Live/unknown refusal precedes
journal publication, native shutdown and cleanup. These Ruby adapter tests verify
call ordering; P1's real-store core tests own terminal/joined and delivery safety.
No poll-quiescence/archive authority was added to deletion.

Focused proof, all from repository Nix:

- Tool72605: exact two new `test_delete_...` regressions via the aggregate
  `test/dev_session_test.rb` entrypoint passed2 tests/17 assertions in0.203s;
  Ruby syntax passed. No Ruby production input changed afterward.
- Tool81190: helper+adapter selector initially exposed a moved local `err`
  declaration at response decoding; helper passed2.057s, web compile failed.
  First output preserved at `/tmp/session-archival-p2-r9-first.log`; first map
  preserved separately. The one declaration was fixed. This is implementation
  compile evidence, not a runtime failure or a reason to repeat passing suites.
- Tool27580: only blocked web selector reran:
  `go -C portal test -mod=readonly ./internal/web -run TestMonitorCI -count=1`.
  Passed0.302s; exact19-file P2 map and dependent monitoroperation Go inputs
  unchanged before/after, gofmt/diff checks passed, index stayed empty.
  Complete log `/tmp/session-archival-p2-r9.log`; executable quick-check source
  `/tmp/session-archival-p2-r9-checks.py`; dependency map
  `/tmp/session-archival-p2-r9-dependencies.json`. Nix's ignored SQLite busy,
  dirty-tree and renamed-system warnings did not change the successful result.

Final P2 scope19 paths is prior18 plus the existing deletion test file. New
frozen map `/tmp/session-archival-p2-r9-files.json` SHA256
`d3c32f0bdbcbb497b5b8dfbfc60b50409ba3037a0971149eda723fcb7f7dfa57`.
Only the three released paths and root-owned skill wording differ from the
original P2 map. P1 independently owns shared direct-source validation, naturally
completed direct retirement/Revoke and their proof. No data format, schema,
migration, eager conversion, operator action or framework was added by this
remediation. All owned tools have joined; no VM, live lifecycle/monitor action,
index/commit or publication occurred. Ready for root's final joint amendment
window after P1's complete proof/map; retain b9/R9 as the reviewed predecessor.


R9 final assembly prerequisite is now satisfied: P1 source9600 core passed6.298s;
only its blocked CLI selector reran and passed0.322s in source10634, then diff
check passed. P1's final30-file map
`/tmp/session-archival-p1-r9-files.json` SHA256
`5d90b0192d79faff8e761f58cedacc519ad6f5caa82f446ff5ce2897f0e958e4`
was independently verified against actual files and combined with P2's19 paths.
The maps are disjoint and exactly equal the complete49-path eabb-to-working-tree
delta, with no extra/untracked source. Full diff check passes; HEAD remains b9,
index empty. Combined map `/tmp/session-archival-a14-r9-combined-files.json`
SHA256 `362800c3927db2448cb1c5062b8e714889ed941265f53d8f8abfbb735bb4d4d0`.
Root's exclusive amendment window is the only remaining mutation prerequisite.
No tests were repeated to assemble this packet.


### R9 final joint amendment and narrow-fix lineage

Root inspected the exact12-path remediation and all new tests, accepted the
errors/docs and resolved R9 findings1/2 under mandatory-review step9. The
original report remains unchanged: reviewed runtime range
`eabb56a278bd8eb1759041467eaebfa6392ddcb2..b9b408710e5c20ffa470afde10e4f7afc33919d2`.
The amended runtime is:

- Final head `4f99d2eb84e35750108fdc6fbc1449b185d48f9a`.
- Final tree `2a08df578c861fb99dc2e9ece1993377a366f146`.
- Sole parent/base `eabb56a278bd8eb1759041467eaebfa6392ddcb2`; exactly1 commit.
- Final scope49 paths,5031 additions/132 removals; exact combined map
  `362800c3927db2448cb1c5062b8e714889ed941265f53d8f8abfbb735bb4d4d0`.
- Reviewed predecessor b9 is retained atomically at
  `refs/checkpoints/2026-11-11-session-archival-failures/a14-r9-reviewed-b9b408710e5c`.
  The original269 checkpoint, original maps/check receipts and R9 report remain.

The explicit narrow comparison is
`b9b408710e5c20ffa470afde10e4f7afc33919d2..4f99d2eb84e35750108fdc6fbc1449b185d48f9a`:
12 paths,505 additions/21 removals. It contains P1's six core/test files, P2's
adapter/test/delete-order coverage and the three root-reviewed docs/skill
passages. It introduces no design, authority, schema, data-format, migration,
eager conversion, framework or operator-action expansion. The A14 separate
observer schema1/capability gate and unchanged native schema1 remain as reviewed.
Neither predecessor nor final A14 format has been installed, released or
externally consumed by these implementation packages. Root's separate activation
hold is unchanged by the two fixes.

Source proof retained without repeating passing suites: P1 fullcore6.298s,
blocked CLI-only0.322s; P2 helper2.057s, corrected blocked web-only0.302s,
exact delete Ruby2tests17asserts0.203s plus syntax/gofmt/diff. All proof applies
to unchanged final source bytes, verified against the two disjoint maps and all49
committed blobs/working files. Original first compile failure remains recorded.

Root's final exclusive window staged only the approved49 paths and used ordinary
repository Nix `git commit --amend -F <temporary-message>`, preserving the eabb
ancestry. The reviewed-b9 ref used create-if-absent, with any collision required
to match that exact object. An initial commit-message length guard stopped after
staging but before commit; the message was wrapped and resumption revalidated
all staged paths/blobs and no unrelated source. No source changed during that
setup correction. Final command91316 joined exit0; no uncertain commit effect
remains. Hooks used the unchanged default path; no framework or active hook was
present and none was bypassed.

Final whole diff check passes,49 committed+working hashes match, existing modes
are unchanged and14 new files are100644. Index, tracked tree and untracked
inventory are clean. Exact receipt:
`/tmp/session-archival-a14-r9-commit-receipt.json`.
The source/index/commit window was released immediately after verified completion.
No extra test/build/VM, push, merge, claim, activation or live session/monitor
mutation occurred. Root owns publication and subsequent exact-head verification;
implementer0 retains P2 follow-up fixes and available capacity after acceptance.

Original unchanged R9 report SHA256: `feac82b0d175b2818cd6ff6ca9067b3cbc48cc1406fc643cabcb257bfc0c89ed`.


### C4: exact4f99 archive-CI fixture admission correction

Root assigned diagnosis of completed Check archive job131928637767, exact workflow
run43438190694/attempt1/head `4f99d2eb84e35750108fdc6fbc1449b185d48f9a`.
No run watcher/poller or job rerun was started. Finite completed-job GET used
`gh api --allow-escape-sequences --hostname github.com --method GET
repos/aither64/dev-workspace/actions/jobs/131928637767/logs`. The first GET77510
exited1 because gh refused terminal escape bytes; the same read with its explicit
output flag42382 joined0. Private full log720805 bytes:
`/tmp/session-archival-ci-43438190694/archive-failure.log`, SHA256
`7d843fb410d78b9d514a5c9aca42e92fc3e373cc27f64d497dfcbaee29181073`.

First refusal14:05:25.916Z at direct monitor start, before archive preparation or
GH polling. Exact caller/root were both `01a1d53a-1f04-7242-8815-f7804fa1b1a1`,
slug `2026-10-25-lead-archive-repair`; source fixture/project/workflow73/run42/
attempt1/40a. Initial turn `01a1d53a-2518-7631-8b92-bdf4bc9a4f9b` completed at
14:05:20.491Z (log4555); require-idle succeeded14:05:22.965Z (4481), then fixture
invoked start14:05:24.348Z (4490), receiving `CI observer lead changed` (4493).
Source authority.go122 obtains `ActiveTurnID`; pinned codex-web client.go5962
returns an empty value when the lead is idle. StartCIObservation requires a
nonempty originating turn. That fixture ordering is sufficient to explain the
refusal without any root/slug change. Epoch/incarnation values are not logged;
no measured epoch/owner mismatch is claimed.

Root accepted the direct bounded two-file brief. Actual fixture path is
`nix/tests/session-archive-lifecycle.nix`. It now arms the existing provider
`hold-turn` before initial creation, waits for its existing `turn-entered` marker,
registers the observer during that genuine initial active turn, releases the
hold, then retains the original require-idle and retry-policy gates. Subsequent
repair/restart, same-receipt completion, detachment and no-late-poll assertions
are unchanged. No substituted runtime IDs, relaxed admission, assertion/deadline
weakening, new model/provider framework or production runtime change exists.

Only other source path is `portal/internal/web/monitor_ci_test.go`: the new
`TestMonitorCIRegistrationRequiresActiveOriginatingTurn` uses actual
Service.StartManaged with otherwise identical owner/source fixtures. Empty
origin refuses without an observer; nonempty origin is retained in acknowledgement
and persisted registration, with no invented poll/snapshot/event/native state.

Known quick check18018 joined0 from repository Nix:
`go -C portal test -mod=readonly ./internal/web
-run '^TestMonitorCIRegistrationRequiresActiveOriginatingTurn$' -count=1`
passed0.092s using the verified absent test provider catalog. Nix parse and
complete generated Python/GH/captured-exec/launcher syntax passed. Executing the
actual generated first-scenario setup with external effects recorded proves
`hold,start,entered,register,release,idle,retry-policy,worktree` ordering; this is
fixture-order proof, not a packaged native execution claim. Source/check script
`/tmp/session-archival-ci-43438190694/c4-focused-checks.py`, full quick log
`/tmp/session-archival-ci-43438190694/c4-focused.log`.

Both owned file hashes are frozen in
`/tmp/session-archival-ci-43438190694/c4-files.json`; before/after checks pass,
gofmt/diff pass and index is empty. No broader suite, VM, build, publication,
pin regeneration, claim, live lifecycle/monitor write or peer native read occurred.
Prepared F3 config29075/workspace689 checkpoints remain unchanged on exact4f99.
Old passing results retain their original input scope. Root inspects this small
source delta before releasing the commit window; no state/schema/DB migration,
conversion or new operator action is introduced.


### C4 committed correction and window release

Root inspected/accepted the exact two-file C4 diff and focused evidence, then
released the short amendment window. Exact published/reviewed predecessor
`4f99d2eb84e35750108fdc6fbc1449b185d48f9a` was preserved by atomic
create-if-absent ref
`refs/checkpoints/2026-11-11-session-archival-failures/a14-c4-reviewed-4f99d2eb84e3`;
a collision could only reuse that exact object. Existing269/b9 checkpoint refs,
original review reports, maps, CI/job logs and F3 pins/receipts remain unchanged.

Only the accepted two frozen paths were staged from an empty index. Ordinary
Nix Git `commit --amend -F <temporary-message>` retained the complete feature
message and produced final runtime:

- Head `1e5f566e4dc77a7d45d545b06bf345bdf5d82edc`.
- Tree `9417a48d198e29ee76aa4a17063f896260267617`.
- Sole parent/base `eabb56a278bd8eb1759041467eaebfa6392ddcb2`; count1.
- Original narrow range `4f99d2eb84e35750108fdc6fbc1449b185d48f9a..1e5f566e4dc77a7d45d545b06bf345bdf5d82edc`:
  exactly `nix/tests/session-archive-lifecycle.nix` and
  `portal/internal/web/monitor_ci_test.go`,39 additions/2 removals, no mode change.

All49 complete source blobs/worktree files match the prior approved map with
only the two accepted C4 hashes replaced. The complete frozen map
`/tmp/session-archival-ci-43438190694/c4-complete-files.json` SHA256 is
`b5c9389d7ce7c2ace22cdf17c856ddf3828ea496cf5ca005594b468ffc6cfdf8`;
C4's two-file map stays
`b7675c923ff2b787207089daddddd573de516cd369b6625afa80a0ab1685e0fc`.
The focused0.092s originating-turn regression and generated-syntax/order proof
bind these exact final C4 inputs; no successful check was repeated for amendment.
Earlier fast/creation/package receipts keep their exact old-head/input scope.

Final complete diff check, one-commit history, index/tracked/untracked/unmerged
cleanliness and modes pass. Runtime still declares no hook framework, uses the
default hook path and has no active non-sample hook; no hook was bypassed.
Command46139 and all cells joined exit0. Exact machine-readable receipt:
`/tmp/session-archival-ci-43438190694/c4-commit-receipt.json`.

The fixture correction is consolidated into the one complete A14 feature commit;
no obsolete unapplied fixture-fix stream remains. No production admission,
assertion/deadline waiver, new schema/persisted-format/database migration/eager
conversion/operator action or runtime recovery change was introduced. Merged
eabb ancestry and the original reviewed A14 observer capability/format contract
remain. Neither correction nor publication authorizes activation or live lifecycle
work. Source/index/amend window released immediately on joined proof. No push,
CI/job rerun, VM/build, pin refresh, claim or live action occurred. Root owns the
affected committed review/publication; F3 config29075/workspace689 checkpoints
still select4f99 until root settles the new final runtime head. Implementer0
retains C4/P2 follow-up fixes and available capacity after acceptance.


### C6: managed native acceptance invocation identity

Original owned execution34808 joined1 after successful exact1e5 managed package
build. Tagged TestNativeMonitorOperation's11 cases all stopped at the fixture's
immediate post-Start identity assertion before socket readiness. Full suite and
package build were not repeated. Original managed package/source/input/derivation
and failed log receipts remain in `/tmp/session-archival-managed-1e5f566e/` and
retain exact old-head scope, without a candidate acceptance claim.

Immutable file proof identifies the root invocation error. `run.sh` supplied
`readlink -e candidate/libexec/codex/bin/codex` as LIVE_SWITCH_CODEX. For retained
candidate `/nix/store/qnyfj061z49nmpjwfnrcn35h8y27r71r-dev-workspace-0.2.0`, that
resolves to `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/bin/codex`.
This is a415-byte Bash launcher with SHA256
`8da58a478557a971106be8f69fc484fc5777650d1d6aabbdb7feb229f3b3861f`, whose
shebang exactly matches observed
`/nix/store/axl12yr00f105bjqvj628f5f0s6r0cnp-bash-5.3p9/bin/bash`.
It execs the same package's `libexec/codex/bin/codex` ELF. Waiting alone would
not repair comparison against the script path after that exec.

The canonical inner ELF is
`/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`,
SHA256 `647b0157e6472a793e0a0bd45bc44ef8ade673b6d8f3db4118260acda4976652`.
Existing provider_native_binary at workspace-codex-providers.rb367 resolves this
launcher-to-inner-ELF layout; nix/workspace-portal.nix528 checks the same
`candidate/libexec/codex/libexec/codex/bin/codex` path. The native test's existing
contract requires the exact pinned executable. Root accepted the invocation
correction; no production/fixture source correction or relaxed equality is needed.

Root released exactly one startup-only disposable probe. Tool60127 joined0 in
the repository Nix environment using
`/tmp/session-archival-managed-1e5f566e/c6-startup-probe.py`. Exact argument vector:
canonical inner ELF, `app-server`, `--strict-config`, `--listen`,
`unix:///tmp/session-archival-managed-1e5f566e/c6-startup-yw9ykrm6/native.sock`.
CWD/private HOME is
`/tmp/session-archival-managed-1e5f566e/c6-startup-yw9ykrm6`, private CODEX_HOME
its `codex-home` subdirectory. The fresh config has only a synthetic loopback
provider, no MCP child and no model prompt; no live home/socket/daemon was used.

The original captured childPID2885433 reached a real Unix socket in0.286095s,
within the finite10s startup bound. Only after legitimate socket readiness, its
`/proc/2885433/exe` path and actual executable SHA256 matched the exact selected
inner ELF above, with the child still running. Normal cleanup sent SIGTERM only
to that captured child; Wait joined exit0. Total native probe0.874357s. No fallback
SIGKILL or alternate path was used. Receipt:
`/tmp/session-archival-managed-1e5f566e/c6-startup-yw9ykrm6/receipt.json`; private
native log/config and original script remain beside the receipt/task directory.

C6 wrote only disposable evidence and this existing P2 record, with no application
source/index/commit, full tagged case/package/VM/CI rerun, pin, review, claim,
activation or lifecycle/monitor-state action. P1's C5 code ownership and root's
README clarification are untouched. All probe/tool processes and code cells
launched by C6 are joined; the only daemon launched was the original captured
private child above. Root owns the future corrected complete source batch and
all candidate acceptance decisions. Capacity is available after C6 acceptance.

C6 receipt SHA256: `1f0ac4b7b1a5e5caf961d714ef44aef3621a00d99abb4a33116466e9c0f73421`.
