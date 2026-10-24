# Package B I3: current published result

I3 is implemented, committed, focused/race checked and SSH published at
`61de5e28d1cb1936aeb3ef2376cdaf17f6034e4b`. Independent affected authority review
is pending. Native fixtures remain **unrun**. No long verification, deployment,
merge, resource claim or session lifecycle action was performed.

Read-only follow-up of the completed prior CI runs found two consumer-fixture
defects still present at this head: missing modelProvider metadata in the
coordination notification test and missing retry.js in the browser contract's
copied module list. Both were outside the previous focused selectors. Complete
logs, exact run/attempt/job identities, source evidence and correction candidates
are in [the prior-CI diagnosis](implementer1-prior-ci-diagnosis.md). Source/refs
remain frozen at61de pending lead's release; no rerun or correction was performed.

## I3 exact range, series and provenance

The base and freshly fetched remote master remain
`bf6d4b0c49600c15e17fe71248807ef43424e932`, retaining installed
`483d4e7eafeda974dfe19de45687795562072d7d` ancestry. Own feature branch is
`2026-10-22-codex-thread-retries` in the registered dev-workspace worktree;
remote remains `git@github.com:aither64/dev-workspace.git`.

Complete final series, oldest first:

1. `7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99` — core, unchanged exact commit.
2. `b3c7187c6e26e269994433716a0ee719d0a7edf7` — capability, unchanged exact commit.
3. `5347f5ddacf321216b818a1e8a0373b7edbb3304` — owning runtime, I3 folded here.
4. `61de5e28d1cb1936aeb3ef2376cdaf17f6034e4b` — sole final A pin, unchanged patch.

The reviewed `cca49782ebd2d5135352cea4cb140548b36f7de9` range is preserved in
[its verified bundle](implementer1-reviewed-cca49782.bundle), requiring the
recorded base. [Complete old/new range-diff](implementer1-cca-to-i3.range-diff)
compares both four-commit ranges from that base. Only the runtime patch changed.
The pin stable patch ID remains `54bed62a7a4a2053fde96119c5b8d6f018a21082`.
Core/schema, capability, I1/I2 and all A API/source/input pins are unchanged.
No fixup or repeated dependency stream remains. The original `85f6f73` review
range and its separate remediation comparison remain preserved below.

The exact I3 delta is three files, 550 insertions and seven deletions:
`portal/internal/workspacecodex/turn_retry.go`, its new production-wrapper test
`turn_retry_settings_test.go`, and `docs/turn-retry-recovery.md`. The complete
base-to-head diff is 37 files, 5045 insertions and 17 deletions. Final tree
`401177e01abbba13009e4a197d694b15d0e58839` equals tested pre-consolidation
commit `1c25485`'s tree; `git diff --exit-code 1c25485 HEAD` is empty.
Final committed-head checks also pass. No hook framework is declared and no
hook was bypassed. SSH force-with-lease required the exact old `cca49782` ref;
the subsequent remote read proves `61de5e28` and unchanged master. Worktree and
index are clean.

Private final schema1/capability1 provenance is unchanged: no merged, released,
deployed or externally consumed predecessor; earlier shapes were disposable
fixtures only. There is no migration, compatibility shim, quota reset or public
contract change in I3. Existing native ledger schema3 is unchanged. There are
no database migrations. C pins belong to implementer0; B did not edit them.

## I3 behavior and focused evidence

The successful explicit settings owner may inherit only the existing verified
loaded witness when cold reads prove the same exact nonempty active/inProgress
turn before and after unequivocal settings success. Provider, socket, authorized
policy/MCP, common instructions and managed execution permission are rechecked.
Epoch advance, old-turn consumption and nil binding are saved before native
effects even with Pending=nil. Promotion changes only the binding's epoch/digest;
old snapshots, queued admissions and uncertain tuples remain unchanged. The
native sessionId is never a generation witness. Turnover, cold/idle state,
missing proof, failed/uncertain RPC or failed checks/persistence retain the hold.
No extra resume/rebind/native policy write or default-derived authority is added.

All commands ran in the repository Nix shell. Exact commands:

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly ./internal/workspacecodex -run '^TestRetryWarmSettings' -count=1 -v -timeout=30s
TMPDIR=/tmp go test -mod=readonly -race ./internal/turnretry ./internal/workspacecodex ./internal/web -run 'Test(Controller.*|Retry.*|TurnRetry.*)$' -count=1 -timeout=40s
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^$'
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -list '^TestNativeTurnRetryController$'
```

[Final validation log](implementer1-i3-final-validation.log): production selector
2.531s; races core4.565s/workspacecodex8.480s/web7.566s; native-tag compile-only
pass and exact native fixture listed (0.059s). [Final committed-head checks](implementer1-i3-final-head.log):
production2.680s; tagged compile/list pass (0.047s); pin contract and whitespace
checks pass. Earlier [full retry selector](implementer1-i3-final-quick.log) passed
3.154s. Gofmt reports no changes. No native case ran.

Four top-level new tests cover eight root/member positive model/effort/both-mode
paths, 22 conservative continuity refusals, pre-effect persistence refusal and
preservation of an uncertain old tuple. Prior MCP/instructions/access binding is
established through actual managed ActivateThread. Positives call actual
UpdateThreadSettings, native acknowledgement and active QueueWithPolicy, then
exact native-style rollout/context and client-ID/content history through the
real backend and Controller. Old queue failures are rejected; new-epoch failure
schedules and passes Check with the requested settings. FIFO and old snapshots
are unchanged. Proof/scheduling emits no resume/settings/policy/queue mutation.
Refusals include pre/post cold/idle, completion/automatic queue turnover,
provider/socket/policy/MCP/access/common changes, missing prior proof, authority
and postcheck errors, failed/unknown native settings and failed promotion save.

Two fixture corrections preceded the final green evidence: QueueEntry contains
an attachment slice, so equality assertions use DeepEqual; the uncertain tuple
fixture's Begin clock now reaches its capacity deadline rather than incorrectly
dispatching at observation time. These were test setup errors, not product
failures. Main lead's exact direct writing pass paragraph was applied before
commit; no diagnostics or status copy changed.

Post-push [Actions snapshot](implementer1-i3-publication-actions.json) shows the
new head queued, and completed failures for old `cca49782`/`85f6f73`. There was no
superseded queued/running run to cancel. No CI wait or rerun was started.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

# Historical B1/I1/I2 remediation receipt (published cca49782)

The accepted final-review corrections B1/I1/I2 are implemented, focused checked,
consolidated into the original owning commits and SSH published. Affected-lane
independent review remains outstanding. Native fixtures remain **unrun**.
No long verification, deployment, merge, claim or session action was performed.

## Current exact source and historical comparison

- Current head: `cca49782ebd2d5135352cea4cb140548b36f7de9`.
- Base: `bf6d4b0c49600c15e17fe71248807ef43424e932`; final SSH fetch still
  reports this origin/master. Installed `483d4e7eafeda974dfe19de45687795562072d7d`
  remains an ancestor.
- Branch/worktree/SSH remote are unchanged from the original packet below.
- SSH `git ls-remote` verifies the current exact head; working tree/index clean.
- Old fully reviewed head: `85f6f7327e6948a13ad110c4c058d8b96b6ab2b9`.
  [Verified original bundle](implementer1-reviewed-85f6f73.bundle) retains its
  feature ref and requires the recorded base. It contains the genuine reviewed
  old commits, not a reconstructed claim of equivalence.
- [Old/new complete range comparison](implementer1-reviewed-to-final.range-diff)
  compares both complete four-commit ranges from that base. Core/runtime patches
  deliberately change; they require affected-lane review, not equivalence reuse.

Current complete series, oldest first:

1. `7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99` — core/store/policy/tests.
2. `b3c7187c6e26e269994433716a0ee719d0a7edf7` — package capability.
3. `c493a41a75de6e1ff857c32b29620ee7862d362a` — runtime/admission/fixture/docs.
4. `cca49782ebd2d5135352cea4cb140548b36f7de9` — single final A dependency pin.

Corrections were folded into commits 1 and 3. No fixup commits remain.
Capability old/new stable patch ID is
`c98df1ec8b8d41855d9263096f4fddebc5d45c76`; dependency old/new stable patch ID is
`54bed62a7a4a2053fde96119c5b8d6f018a21082`. Those two patches are unchanged;
only ancestry changed. The codex-web stream still selects only FINAL A
`d2d74f931cc50e39345c6c15931748062ee51951`, with identical Go sums/Nix lock/vendor
hash. No A source/API change, extra pin stream or downstream C edit was made.

Old-to-new delta: 14 files, 1281 insertions, 110 deletions. Complete final
base-to-head diff: 36 files, 4502 insertions, 17 deletions. Added code is primarily
required regression fixtures. The consolidated tree
`8bbdd72dde0b8c7046d1b6fea7859318b9fd6b1f` exactly matches the tested pre-rebase
remediation tree; `git diff --exit-code fdd8288 HEAD` was empty. Full-range
whitespace check passes. No hooks are declared; no hooks were bypassed.
A post-force-push GitHub Actions list for this exact feature branch returned
`[]`; no superseded queued/running workflow existed to cancel and no CI wait
was started. Command: `nix shell --inputs-from . nixpkgs#gh --command gh run list --repo aither64/dev-workspace --branch 2026-10-22-codex-thread-retries --limit 20 --json databaseId,headSha,status,conclusion`.

## Corrected contracts and private format provenance

I1: a separate internal reconciliation-only admission takes transition/runtime/
roster/conversation/thread locks and exact retained identity. It only settles the
saved tuple with existing A Reconcile/DiscardPrepared APIs. It cannot dispatch,
resume, steer or write settings. The worker then reacquires the unchanged strict
ordinary resolver before any possible fresh dispatch. Foreign unknowns and cold,
stopped, generation, lifecycle and execution holds remain effective.

B1: settings intent proves the current native thread/turn identity, durably
advances a nonzero epoch and consumes the active/failed turn before the settings
effect, including Pending=nil. Every prior admission, including native queues,
loses automatic authority; the queue itself/FIFO remains untouched. Old tuples
are immutable for reconciliation; current binding establishment cannot retrobind
old empty admissions. New managed admission captures the new epoch. Preference,
enrollment and quota survive failed/unknown settings replies and restart.

I2: charges are UUID-keyed. Positive exact never-submitted proof is required to
renew that same UUID at the current clamped time before outbound. Unknown native
submissions never resend. Acceptance/reconciled acceptance anchors that ID's
charge once to conservative receipt observation time, covering network delay;
duplicate receipt observation neither adds a slot nor moves its anchor again.
Other equal-timestamp IDs remain distinct. Up to one retained old reservation
plus 30 other records fits the bounded store; dispatch still refuses 30 other
live charges. No elapsed-time quota rearm or replacement UUID is introduced.

Final prerelease private schema is **1**, capability `turnRetryStateSchema=1`,
as explicitly directed by lead and saved by architect. State/Binding/Snapshot
require nonzero epochs and digest inclusion; bindings match the current epoch,
while retained old snapshots may only reconcile. Charges require unique UUIDs,
positive timestamps and correspondence with charged Pending. Preliminary missing
epoch/anonymous charge shapes fail closed. There is no conversion/default/quota
reset or iteration-compatibility shim. This shape has no deployed/released/merged
or external predecessor; only disposable test records ever consumed the earlier
shape. Existing native ledger schema 3 and unrelated formats remain unchanged.
There are **no database migrations**.

## Remediation validation and native gate

All below are repository Nix development shell commands. Final logs:

- [Final focused races](implementer1-remediation-final-race.log): core 4.152s,
  workspacecodex 2.423s, web 7.185s; exit zero.
- [Final web/compile/list/pin checks](implementer1-remediation-final-quick.log):
  affected web 5.127s, tagged compile-only passed, expected native fixture listed
  0.050s, pin consistency and whitespace checks passed. A harmless ignored Nix
  evaluation-cache SQLite busy diagnostic occurred in the shell startup;
  command results were successful.
- Earlier complete new core package 1.107s and complete workspacecodex package
  7.185s passed. Final new core tests are included in the final race selector.

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly -race ./internal/turnretry ./internal/workspacecodex ./internal/web -run 'Test(Controller.*|Retry.*|TurnRetry.*)$' -count=1
TMPDIR=/tmp go test -mod=readonly ./internal/web -run 'Test(TurnRetry.*|CreationlessConversation.*|Recovery.*|.*Conversation.*|.*PlanImplementation.*)$' -count=1
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^$'
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -list '^TestNativeTurnRetryController$'
```

Real resolver regressions exercise creation-less root AND retained member with
actual workspacecodex observation and schema-3 A ledger: prepared, absent,
submitting after native acceptance/lost usable reply, cancelled, cold, stopped,
foreign same-thread/other-member unknowns, genuinely unknown history and package
generation replacement. Tests prove that strict mutation admission fails before
own exact reconciliation, owned receipts recover without another start, and
foreign unknowns keep the ordinary gate closed. Their native stub rejects every
resume/steer/settings/queue activation RPC. Provenance regressions cover active
and failed-but-unobserved Pending=nil executions, model/effort/both mode directions,
failed settings RPC, native autoqueue turnover after the identity read, old empty
binding rejection, post-barrier managed queue proof and durable restart shape.
Quota tests cover 299/301-second dispatch delay, 29/30 other live IDs, same-time
IDs, backward clock, conservative network-delay acceptance, unknown no-resend,
once-only delayed reconciliation reanchor, overflow and preliminary shape errors.

The native `TestNativeTurnRetryController` now uses an owned test-only WebSocket
receipt/history barrier: the real daemon accepts a turn, its usable reply is
removed and exact history is held, leaving A's ledger submitting. After client
restart the barrier opens and the **real portal scheduler/resolver** must recover
the same receipt without another provider request. The helper/fixture compile;
no native run or empirical inheritance/receipt claim has been made. Top-level
fixture name remains unchanged and it has no named subcases. Native execution
remains after affected-lane final review under the watcher brief.

One new settings fixture initially stalled because its fake returned a settings
error and stopped servicing subsequent RPCs on the still-open connection. The
owned test process was interrupted for diagnosis (not a native/live session);
the fake read loop was corrected and test contexts bounded. Final focused/race
checks pass. An initial resolver test assertion assumed Pending survived a
completed turn; it now checks the durable exact accepted snapshot, allowing
ordinary completed-state advancement. Production holds were not relaxed to
make either fixture pass.

Lead directly applied the required writing skills to the new guide paragraphs
and eight bounded diagnostics, and supplied the exact corrected settings
paragraph before these commits. Status mappings remain unchanged. The required
next action is affected general/architecture/risk review on this exact current
head and old/new range; longer verification and C repinning are lead/peer-owned.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

---

# Original reviewed package B packet (superseded source head)

The following preserves original evidence for reviewed85f6, not current readiness.

# Package B final source and verification evidence

Implementation, operating docs, focused checks and SSH feature publication are
complete. Independent final review and post-review native verification remain
outstanding. No native fixture execution, package build, deployment, merge,
resource claim or session lifecycle action was performed by this package.

## Exact source and history

Repository: `git@github.com:aither64/dev-workspace.git`.
Branch: `2026-10-22-codex-thread-retries`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace`.
Base: `bf6d4b0c49600c15e17fe71248807ef43424e932`.
Published final head: `85f6f7327e6948a13ad110c4c058d8b96b6ab2b9`.

Final SSH fetch kept origin/master at that base. Both the base and installed
`483d4e7eafeda974dfe19de45687795562072d7d` are ancestors of HEAD.
`git ls-remote origin refs/heads/2026-10-22-codex-thread-retries` returned
`85f6f7327e6948a13ad110c4c058d8b96b6ab2b9`. Index and working tree are clean.
Initial lead tracking gate: `4be0b2f3ae8257e8f0aaa9c1bd3a20bc376f4ea1`.

Complete series, oldest first:

1. `259fcd636ecb4afa0c7c4a2384c6f91d7ef8b353` — `turnretry: retain bounded retry policy and admission state`.
2. `1f76716cdec2348d65039220cfc33616702b1e80` — `runtime: require retry-capable package transitions`.
3. `0398d16bb166ccc2e16b683b9d45672172961d0c` — `portal: continue new managed failed turns through durable retry admission`.
4. `85f6f7327e6948a13ad110c4c058d8b96b6ab2b9` — `deps: pin codex-web failed-turn continuation support`.

Core policy/store and package capability are independently reviewable. Runtime
admission, settings proof, adapter, cancellation, native fixture and operating
docs jointly establish the execution boundary and form one integration commit.
Final diff: 33 files, 3331 insertions, 17 deletions. Full-range diff whitespace
check passes. This repository declares no hook framework.

Unpublished core fixups were folded before review: the previously reported
`aac0629` iteration is superseded by `259fcd6` and absent from the series.
No obsolete intermediate implementation remains. The sole dependency stream is
codex-web, consolidated in the final commit at FINAL A
`d2d74f931cc50e39345c6c15931748062ee51951`; no intermediate25f pin commit exists.
Nix source/lock, Go module/sums and vendor hash move together. Other locked
inputs remain unchanged.

- Go: `v0.0.0-20261022145556-d2d74f931cc5`.
- Source NAR: `sha256-O3GWvvYTSDKG3Ybsj0xbmEzGMLLSF09wv4iKc2DeIsU=`.
- Vendor NAR: `sha256-E0SeFk5IWAfvK4zbU9E/d5wODCS5i1NGqQj8btaw6ho=`.

Vendor hash command in the repository Nix shell:
`cd portal && go mod vendor -o /tmp/codex-thread-retries-vendor && nix hash path /tmp/codex-thread-retries-vendor`.
That owned disposable directory and temporary commit-message files remain as
generation evidence. No session cleanup was performed.

## Final quick checks

Commands below ran through `nix develop --command bash -c` from the worktree.
All final commands exited zero. Logs are siblings of this record.

```sh
cd portal
TMPDIR=/tmp go test -mod=readonly ./internal/turnretry ./internal/workspacecodex ./internal/web -run 'Test(Controller.*|Retry.*|TurnRetry.*|Recovery.*|.*Conversation.*|.*PlanImplementation.*)$' -count=1
TMPDIR=/tmp go test -mod=readonly -race ./internal/turnretry ./internal/workspacecodex ./internal/web -run 'Test(Controller.*|Retry.*|TurnRetry.*)$' -count=1
go test -mod=readonly ./cmd/workspace-portal -run 'Test(RootThreadSettings.*|ThreadEnsureInitial.*|Provider.*|ScopedProvider.*)$' -count=1
go test -mod=readonly ./internal/workspacecodex -run 'TestRetry.*' -count=1
TMPDIR=/tmp go test -mod=readonly ./internal/turnretry -count=1
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^$'
go test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -list '^TestNativeTurnRetryController$'
```

- [Normal focused log](implementer1-final-go.log): core0.146s, workspacecodex0.113s, web2.368s.
- [Race log](implementer1-final-race.log): core1.253s, workspacecodex1.272s, web1.626s.
- [Command regression log](implementer1-final-command.log):1.516s.
- [Final admission log](implementer1-admission-final.log):0.105s, after avoiding unnecessary pre-initial history reads.
- [Exact committed-head core/compile/list log](implementer1-final-head-compile.log): complete core0.333s; tagged compile0.045s; expected native fixture listed0.045s.
- [Contract/syntax log](implementer1-final-contract.log): Ruby1run/5assertions/0failures/0errors/0skips,0.053443s; Ruby syntax OK twice; node syntax, pin consistency and diff check exit zero.

Contract/syntax commands from the worktree root:

```sh
ruby -Itest test/workspace_host_test.rb -n /retry_records/
ruby -c libexec/dev-session
ruby -c libexec/workspace-host
node --check portal/internal/web/static/app.js
bash nix/check-codex-web-pin.sh portal/go.mod v0.0.0-20261022145556-d2d74f931cc5 "$(command -v jq)"
git diff --check
```

Earlier successful evidence includes the complete workspacecodex unit package
(6.542s), affected team Assign/Configure/Access/Remove selector(0.909s), complete
core race package(2.642s), actual cross-process lock exclusion, and complete core
normal tests(0.314s). No broad checks or CI waits were started before review.

Coverage includes enrollment/completion races and old-failure exclusion;
opt-out/re-enable; complete capped capacity schedule; durable30-send rolling
quota with uncertain sends, backward time and no exhaustion timer rearm;
restart/cancellation identity; corruption/version/scope rejection; cross-process
admission; provider/access/instructions/context mismatches; actual queue settings
versus enqueue defaults; steer context/settings and receipt restart; managed
model/effort/mode intent cancellation; HTTP origin/authority; native-child
exclusion; generation rejection; root roster-operation contention; and worker
reservations preventing concurrent duplicate jobs for one conversation.

## Failed checks and corrections

- Direct Ruby `test/workspace_host/profile_transition_test.rb -n /retry_records/`
  failed with `NameError: TransitionHost`: that file depends on its aggregate
  loader. The corrected exact aggregate command above passes five assertions.
- A web regression exposed a nil embedded optional fake client. Added nil-safe
  RetryAvailable/capability guards; the affected selector now passes.
- That run also failed Unix socket bind under Nix TMPDIR plus long fixture
  names (path exceeded Unix socket length). The same selector using
  TMPDIR=/tmp passes, earlier2.157s/final2.368s; no production path changed.
- The root roster contention test initially used a fake lacking the team
  interface; using the existing retained-conversation fake corrected it.
- The new settings-intent test initially referenced a nonexistent convenience
  constructor, then had incomplete fixture manifest provenance (plan/client
  version absent). Corrected fixtures exercise the real wrapper and prove
  pending work cancels even when the native settings mutation is rejected.
- Final inspection corrected steer receipt snapshot digest refresh, native
  sandbox rollout spelling (kebab-case, distinct from v2 request encoding),
  and repeated scheduler jobs for one thread. These fixes were folded before
  review. Exact history also binds contributing inputs to their executed turn
  and retires old proved inputs; unbound queue evidence remains retained/bounded.

## Native manifest and remaining gate

`TestNativeTurnRetryController`, in
`portal/cmd/workspace-portal/turn_retry_native_integration_test.go`, tag
`live_switch_integration`, is one top-level fixture with no named subcases.
Compilation/listing only are complete. It has never been executed.

The fixture selects the pinned executable through LIVE_SWITCH_CODEX, uses
private state/socket and an allowlisted child environment, and contacts only a
no-auth loopback synthetic Responses provider. It asserts managed creation and
initial failure, actual continuation preserving model/effort/mode, exclusion of
old failures, persisted scheduled UUID/deadline across client restart, actual
accepted receipt reconciliation after simulated application result-save loss
without another provider request, and opt-out before a later deadline.
No real provider key or policy-violating input is used.

After review, require go test -json top-level PASS and no skip under the fresh
watcher, per [native-verification.md](native-verification.md). The failure wire
and native inheritance contract remain source-confirmed, not empirical test
results. A owns the larger generic native campaign and native-direct CAS probe.

## Authority, docs and state provenance

Guarantees cover managed portal/CLI/retained-team operations sharing admission
and package generation. Exact historical native context plus the saved successful
managed provider/instructions/MCP/access binding is authority within that
boundary; display caches are never authority. Unmanaged direct native writers
can change loaded settings or race without CAS and are outside the guarantee.
Observed mismatches, unidentified input, changed socket epoch and recovery/queue/
provider holds fail closed. No managed admission path was deliberately excluded;
actual native compatibility remains the post-review gate.

Project explanations: README entry link, docs/workspace-portal.md controls and
schedule, docs/turn-retry-recovery.md persistence/locks/settings/uncertainty/
managed-authority/forward recovery. Lead directly applied the required writing
skills to all final prose, status reasons and defensive diagnostics before commit.

There are **no database migrations**. Existing native submission schema3,
recovery/roster/manifest/lifecycle formats retain their versions. New separate
private retry state is schema1, never merged/released/deployed/externally
consumed; only disposable fixture state exists. turnRetryStateSchema=1 gates
package selection whenever retry records exist, including cancelled records.
Forward recovery uses a matching compatible package; cancellation never deletes
uncertain identities or resets enrollment.

Final review must conclude on the complete four-commit history, consolidated
pin stream, state/migration provenance, interfaces and shared lock ordering.
Lead owns later verification/deployment/integration assignments.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
