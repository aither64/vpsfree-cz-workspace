# Implementation evidence and decisions

Historical implementation checkpoints; current status is in [state.md](state.md).
Final interfaces and proof requirements are in [design.md](design.md). These are
execution records, not deployment or integration approval. Superseded heads and
partial checks retain their original scope.


- Empty question drain selected work only after exclusive admission and then
  invalidated fresh observations. No-op reconciliation and failed/inflight display
  demand amplified repeats. A adds read preflight, real exclusive reread, conditional
  invalidation, coalescing and 1s→30s failure backoff.
- Final scheduling seam: acquirePiForeground(ctx, SessionRef) (func(), error).
  Atomic grant/registration allows eight foreground turns before one eligible due
  round-robin background pass. Context/all-exit cleanup; no authority bypass or
  preemption of admitted effects. Backed-off demand cannot reserve. Reserved work
  may cost the ordinary six-second budget plus an admitted effect; measure limits.
- Queue uses isolated portal SQLite v1 and explicit shared optional deliveries
  endpoint/status. Ordinary message success remains native Accepted. Local admission
  has no Pi/Host.Inspect calls or runtime-lock wait; it validates current local
  identity/access/selection, pins uploads and compares the tuple before commit.
- Saved original ID, full target/settings/policy/mode and native ref remain immutable.
  Durable dispatch claim precedes native call. Recovery after claim only looks up
  original receipts; missing legacy retry:true receipt stays Unknown. No replay.
- C adds versioned checked input/lookup and scalar identity under frozen CURRENT
  support. Retained f3bd workers keep exact legacy routes and history-linear checks;
  durable delivery needs a separate supported upgrade. Native witnesses stay intact.
  Identity optimization alone cannot prove healthy delivery <1s.

A focused suite passed via fresh installed Luna/low watcher: 69s wall including Nix;
piquestions 0.661s / web 24.020s. Log:
`/tmp/2026-11-23-pi-message-delivery-A-focused.log`. Later cooperative-cancellation
regression added. Owning `./internal/piquestions ./internal/web -count=1` settled on pre-fairness
source: questions passed, web failed after 514.677s; complete log
`/tmp/2026-11-23-pi-message-delivery-A-packages.log`. Two failing parent tests:
TestCreationEvidenceGapDeletionRetiresTheExactRequest lacked runtime fixture env
(authority/tmux/Codex/portal command); TestPiAcceptanceFollowupScope could not
resolve Playwright in plain devShell. This is a failed setup run, not full-suite
proof. No A test failure reported. Owner checking declared packaged setup once;
final combined packaged suite with proper fixtures remains required after review.
Accepted fairness/parent-budget delta is implemented; final affected quick tests
next. Watcher confirms original command and processes settled. No final-head result.

Two team-assignment attempts hit transient session-command contention; unchanged
message ID retried successfully. No identity or application-access failure.

## Documentation, risks and next

Lead applied dev-session-documentation/handoff and the user-facing writing skill
directly to A's docs/pi-questions.md, including retry/foreground/fairness limits;
implementer checks factual fidelity. Permanent contracts stay in owning projects;
actual measurements and temporary revision evidence stay here.

Next: C delivers native ports/scalar proof; B continues independent work and
consumes C for production dispatch. Then consolidate full history, complete quick
checks and docs, invoke reviewer0, run longer fixtures/CI, publish/verify branches.
No actual latency result yet. Exact native witness/background costs may miss targets;
measure rather than weaken proof or relabel Queued as Sent.

No lead-owned disposable services or fixtures created. Member test artifacts are
local/untracked; retain compact evidence. Leave session and feature refs open.

B first milestone (uncommitted): additive neutral DurableDeliveries API/types,
HTTP validation and scope-bound browser create-or-get helper implemented. Focused
codex-web Go HTTP/legacy-wire/embedding and browser contracts passed in Nix;
exact commands/revisions pending final package evidence. Indexed queue v1 store
written (WAL/FULL, immutable exact key/CAS), tests next. Feature not advertised;
production native dispatch still depends on C. B avoided A's web Go check inputs.

B queue store focused tests passed; shared mount and integration remain in progress.
Lead writing pass applied directly to shared deliveries.js. During visible-path
inspection, sent owner three fixes: truthful presentation of recovered terminal
states, original legacy retry path when new capability appears, and explicit
supported-mode selection. These remain owner implementation/test work.

Retained-queue preflight clarification accepted: copy DB+WAL only under existing
exclusive transition writer exclusion covering writes/close/checkpoint, then open
SQLite only on disposable copy. Source must remain byte/name/mode unchanged,
including WAL-only committed rows with absent SHM; cleanup on failure/cancel.
Actual lock/order proof and tests required in final packet.

A final affected/repaired-environment check passed (fresh watcher): 77s wall,
questions 0.373s / web 40.793s; both previously setup-failing tests included.
Log `/tmp/2026-11-23-pi-message-delivery-A-final.log`. Correct environment uses
repo-selected playwright NODE_PATH and DEV_SESSION_REQUIRE_RUNTIME=0 only for
disposable Ruby fixture; verified session markers unchanged. Whole packaged suite
still remains for final combined source. Final small shutdown-waiter cleanup and
known-short focused regression next, then A-only commit/evidence.

A accepted at e50ff02ea8961e9afcd96a3a4063ed5bbbac6cd9 (parent f3bd):
six paths, 947 insertions/59 deletions including 546 regression-test lines. Lead
inspected commit/boundary and terminal logs. Final shutdown/foreground delta
passed web 8.939s: `/tmp/2026-11-23-pi-message-delivery-A-foreground-final.log`.
No schemas/wires/migrations; all command effects settled; index empty. C assigned
after explicit capacity confirmation. Next dev-workspace commit window C then B;
B's codex-web window independent. No merge/deploy/publication yet.

C exported optional queued-input types/interface are available to B; no legacy
Controller expansion/stubs. Lead accepted narrow manager.go capability-reader
fields/defaults matching existing per-Manager test injection, for faithful new/
retained package tests without global overrides or store writes. C implementation
and checks remain in progress.

B shared mount fixes now reported with passing draft/state contracts. Lead applied
reference-section writing pass directly, preserving original-ID/retry/native facts
and restoring existing optional-operation paragraphs outside the new heading.
Codex complete commit/check packet and provider publication/pin remain pending.

Codex-web dependency milestone accepted/published:
`0b3237f4f8e8b8e4ffeefeb4e112eb4b953c9952`, one logical commit above3209aa7b,
12 files +598/-16, clean worktree. Go conversation suite and 113 Node browser
contracts pass; syntax/diff checks pass; no hooks declared. Fresh fetch confirmed
0 behind/1 ahead default; SSH feature push and fresh ls-remote equality verified.
B now owns matched Go/Nix/browser pin update; no merge/deploy. Provider still in
combined final review scope. CI run45291117337, workflow354268218, attempt1,
exact head0b3237f. Runtime monitor start e8d2239b-1c7a-4696-a37d-af49cd03a56b
refused caller ownership; no observer registered. Use bounded parent read-only
run-attempt checks, not a replacement native CI driver or automatic-wake claim.

Codex-web CI attempt1 completed success at exact published head0b3237f:
[Check run45291117337](https://github.com/aither64/codex-web/actions/runs/45291117337).
Confirmed via bounded exact-attempt API read at 2026-11-23 23:44:40 UTC. No native
CI watcher/observer exists and no outstanding CI command remains for this run.

B selected-tuple correction: actual portal captures pre-refresh scope/selection,
visible model/effort and exposed policy mode; refresh disagreement refuses POST
and preserves draft. Metadata cannot auto-adopt settings. Shared mount needs the
same necessary fix/test; lead accepted owner amendment into single unmerged
provider commit before final review. Published0b3237f has only this initiative's
uncommitted consumer pin/quick use, no deployed/merged supported boundary. Owner
will report final head/checks; lead republishes with fresh lease, final B pin stream
contains only final source. Old CI proof stays bound to old0b, not reused for fix.

Provider amended/consolidated:0b3237f→2459f8cbbc141fab500b9d76c115833b55ad08b6,
same3209aa7b base, one12-file commit +602/-16. Necessary pre-refresh selection/
scope/visible-mode fix and loaded-tab regressions; not patch-equivalent. Fresh
conversation Go suite, Node syntax and affected mount/durable contracts pass;
unchanged browser modules retain old113-test evidence. Lead inspected range-diff,
fresh-fetched and published with exact-old-head force-with-lease; fresh remote
head equality verified. B updates only final uncommitted consumer pin stream.
Old CI success remains old-head only; no stale active CI run to cancel. New CI
registration pending at immediate post-push list. Full final review uses2459f8c.

Bounded D acceptance audit requested: expected outcomes for queued-before-claim
vs ambiguous phases across portal/native restart. Assess whether execution
replacement alone needlessly terminates definitely-unsent queued work while exact
logical target/settings stay intact; no post-claim replay or implicit load/start.
Architect owns evidence/clarification, material change awaits lead acceptance.

D restart audit accepted: full original runtime equality would unnecessarily fail
definitely-unsent queued work after a legitimate successor. Before the one dispatch
claim only, permit strict original-full-ref ancestry to exact ready CURRENT with
unchanged logical conversation/nativeID/incarnations/settings/policy/instructions/
access/files. Keep original admission/selection/ref/input/ID immutable; save actual
DispatchRuntime/Handle/Generation at CAS. Current binding revision is fresh owning
evidence, not a replacement logical target; exact selected joins remain required.
Unavailable/unloaded/preparing waits queued/backoff; no implicit load/start. C
checks old ref lineage/digest against new execution evidence. All phases after
claim remain original-ref lookup-only, including crash before wire. B/C own focused
restart/race tests and final v1 schema directly; no obsolete iteration migration.

Corrected provider2459f8c CI succeeded, run45292814308 attempt1 (workflow354268218),
confirmed at2026-11-23 23:56:35 UTC. No stale active provider run to cancel.

B production-path milestone: local HTTP admission tests pass under a held
exclusive runtime lock with zero Bind/dispatch/lookup/additional Host.Inspect;
original-ID statuses survive changed selection/capability while fresh stale
admission refuses. Store/dispatch/gate/WAL-copy tests pass. Final provider2459
pins matched locally; only codex input changed, obsolete0b sums removed. Vendor
hash calculated from authoritative mismatch log (not truncated watcher prose):
sha256-sxziD0je03Co87gaTKnMUB8bmYESAShAxMYb9vaB5sQ=. Corrected bounded module
verification running. Remaining B tests: actual composer/uploads/preflight/host
and successor/claim races; docs and final quick evidence/commit. No timing result.

History preparation: prefer C scalar proof then checked-input/continuation ports
as separate buildable logical commits; owner may justify inseparability. B keeps
one final dependency/pin commit, then queue/browser/retention behavior. Preserve
supported inherited eight commits and avoid obsolete iteration/fixup history.

Two concrete compatibility/recovery corrections accepted before final review:
- Existing explicit retirement preserves original Unknown forever but permits a
  distinct later input. New typed queued lookup carries owner-proved RetiredUnknown
  without changing legacy bytes. Monotonic queue disposition releases only that
  row's barrier/capacity; shared optional retired=>unknown stays non-acceptance,
  bounded recent window100 and exact-ID dedup retained. Full owner/ref/receipt SHA/
  source/current-lineage/terminal stop/recovery proof required; no reason-string
  authority or ordinary Unknown bypass.
- Browser definitive admission rejection otherwise strands immutable saved attempts.
  Same SQLite identity authority commits exact-request refusal tombstones atomically
  against Admit; valid scope/auth/syntax required. Only typed durable notQueued proof
  bound to the complete original attempt lets helper clear local admission while
  preserving draft/files for explicit later new-ID Send. Missing/auth/transport
  failures remain ambiguous; native NotSubmitted unchanged. Retain negatives in
  package preflight/dedup. Concurrent/lost-reply/restart/mismatched-proof tests required.
Architect records exact seams first; B/C retain existing ownership. Batch shared
provider amendments into one final tested commit/pin, final queue v1 directly;
no obsolete interim schema migration. C identity prerequisite is independently
snapshotted/tested while second port delta settles.

C scalar prerequisite committed60900b4ae7f8e813c6e5b7f998283a95c6bc8a48
(parentA e50ff02), exact isolated tested tree2b0fac8b9ffd002088c4b86eec692dcfae6d4624.
GOWORK=off identity/selection Go tests passed0.496s; Node22 protocol5/5 passed566ms.
Thirteen C paths, identity flag only; B and checked-port content unstaged/index empty.
Full C still executing; native/strict prior-input watcher accounted separately,
final retirement-result delta requires affected Go checks. Lead applied C/B runtime/
portal/backend docs and fixed user-facing refusal strings; owners reconcile facts.

Retirement/negative seams recorded before implementation: new queued lookup
QueuedInputLookupResult{Status,RetiredUnknown}; new DeliveryNotQueuedProof{Version,
Scope,Request}, optional DeliveryError.NotQueued, exact HTTP/browser proof validation.
Negative identities retain authentic private ConversationRef scope for existing
portal_delivery preflight, not fabricated SubmissionRef or browser authority;
negative-only DBs require capability fence. B batches final provider amendment;
no new provider head yet,2459 remains last published/green.

C accepted at74f4a6f4fbc9d62575defa5a33b44dc5563ee2ae (tree8a8373aa...),
two buildable commits aboveA;17 paths1699 additions/15 deletions (882 tests,
69 docs). Lead inspected final8-path commit, optional port signatures, empty index
and native retirement log. Final affected batch13.513s/wall34s passed, log
`/tmp/2026-11-23-pi-message-delivery-C-retirement-go.log`; pre-delta native Go8.652s
and unchanged Node27/27 in3.994s remain scoped evidence. All C effects settled;
capacity confirmed. B now owns dev dependency/feature commit windows. Architect
prepares disjoint tagged V native campaign fixture brief from existing central/P6
harness; C can own it only after explicit release. Long execution follows review.

Final provider9bf8c58272b3b6068948f007392936bfa1e6431f published with exact2459
lease and fresh remote equality; one final12-file commit +763/-16, Go conversation
and114 Node quick checks pass plus narrow negative guard. CI45297380836 attempt1
FAILED in unchanged codex TestConditionalSteerConcurrentClientsShareOneClaim/
database=true at conditional_steer_test.go:543 SQLITE_BUSY; conversation passed.
Exact failed log `/tmp/2026-11-23-pi-message-delivery-provider-ci-45297380836.log`
retrieved/inspected. B owns bounded root-cause/repro and minimal correction or
justified evidence before rerun. No stale active prior-head run to cancel, no
blind green rerun or all-CI success claim. Final consumer pin/hash still pending.

V explicitly released to implementer0 after C acceptance/capacity, fresh roster
and full sufficient V brief read. New tagged internal/external native delivery
fixture files, narrow default-preserving test context seam only if needed; reuse
central/P6 actual paths and authentic five-conversation fixture. Source + compile
only before review; actual Recovery/Performance afterward. B retains untagged/
hydrated browser/upload/store/preflight and current index/commit windows; V commits
following B. No latency/fixture execution claim from compile alone.

Provider redCI diagnosis reproduced3/30 in1.946s, unchanged native-source race in
first-open connection/WAL/schema initialization. Narrow init-only existing private
context-aware file gate authorized, released before predecessor migration/native/
normal transactions. Focused fresh16-client/cancellation/existing-store batch30
iterations passed11.031s; lock-order test and full native suite running. Separate
focused fix commit/pin planned. Lead applied submission-storage.md init-gate prose.

## Superseded native gate checkpoints (through 389c)


R1 architecture clarification is recorded: observe actual host.input under its
existing serialization, preserve concrete endpoint and callback/Close behavior;
do not reacquire writeMu. Count actual full/failed writes accurately. Native
acceptance hook qualifies only after successful full delegated input_commit write
following exact Accepted persistence; original Lookup/witness remains decisive.
Public Sent and HTTP durable receipt are separate upper bounds. Positive Pending
observes within persisted first-second window then2s; GET/restart cannot renew it.

Canonical four-member-plus-lead fixture prepared through existing Nix generator:
ignored/untracked `v-fixture/catalog.json`; JSON SHAadb05d10ba504cd3951631f07c450d16a753f75856b41d9c6ad50ecdaaa91aed.
Regeneration/input validation in design.md and v-fixture/validation.json.
Immutable Pi SDK/nodes and exact candidate validation remain required. Candidate
app build, native bootstrap/recovery/performance, hydrated browser and selected
pi-runtime-host/session-creation VMs remain unexecuted. Fake host/systemd/drain,
offline faux model and in-process HTTP omit real host/model/TLS costs; report limits.

Candidate build utility /root/candidate_build_ab3 passed88s, all effects joined.
Actual argv had installables .#default and an extra current-flake dot from lead
brief punctuation; all outputs equal. Independent exact-default evaluation proved
/nix/store/wbaga2kl6p6dbvi0i1dbhw6fjv5lqjfd-dev-workspace-0.2.0 for clean ab3.
Full log /tmp/2026-11-23-pi-message-delivery-candidate-ab3-build.log. No activation;
selected profile remains60kkim. Worker sf66v6yynkrri5m3g45x1az9h0lq4ggg, protocol2,
Node22.23.2/Pi1.5.2 match declared immutable inputs.

Fresh native utility /root/native_bootstrap_ab3 ran only
TestPiMessageDeliveryNativeBootstrap, -timeout=5m, exact Nix wrapper/curated env,
candidate above, prepared catalog and /tmp/pi-message-delivery-bootstrap-ab3.o7jNH4.
Log /tmp/2026-11-23-pi-message-delivery-bootstrap-ab3.log. Fresh installed utility
Luna/low/full_access policy validated for each launch; parent remains active.
Gate FAILED14.9s: p2_central_workflow_integration_test.go216, Pi creation team
disagrees with reserved identities. All effects joined, no full campaign. I0 owns
fixture setup correction, no production guard weakening; pure setup validation/
compile precedes next bootstrap. H prepares browser prerequisites independently.
H then ran independently on unchanged reviewed web inputs: both browsers passed
actual hydrated delivery subtest, zero legacy sends/page errors/unexpected requests.
UI HTTP results are controlled; no native/storage/p95 claim. Shared utility slot free.

Seed corrected only in two V files: owning ProjectPiPreset once, exact per-member
frozen models/efforts and history attribution; no production/central guard change.
Pure strict intent/binding/mismatch/catalog-immutability test passed0.080s and tagged
compile0.061s. V amended ab3→cdd5, same B835aad parent. H web source unchanged.
Rebuilt actual cdd5 candidate /nix/store/sr8xyssppyv34m9pf7gwfzwc9wjjh43q-dev-workspace-0.2.0
passed86s, same declared worker/SDK. Second single Bootstrap FAILED15.2s at first
real member assignment HTTP409 session backend binding conflict. No matrix/samples;
all utility effects joined. Log /tmp/2026-11-23-pi-message-delivery-bootstrap-cdd5.log,
artifacts /tmp/pi-message-delivery-bootstrap-cdd5.MljSij. I0 owns exact join diagnosis
before further source change/repeat; no guard weakening or guessed setup iterations.
Progress response native-bootstrap-fixture-preflight: source/SDK diagnosis reproduced
selected xhigh clamped to high by the synthetic model lacking thinkingLevelMap.
Creation-proof full-settings rejection is the matching inferred409 path; old stage
logger was discarded. Before another build/gate require actual generated-model SDK
capability preflight for every lead/member tuple plus exact create-stage diagnostics.
All local binding/authority/roster/projection/IDs inspected together; no production
guard change. Only bootstrap may follow these seconds-scale checks; matrix held.
Input retention correction: both earlier --no-link app outputs are now absent
(independently checked); SDK/Node remain. Their passed build receipts remain
historical, not available candidate inputs. Next candidate uses a unique owned
Nix --out-link GC root and verifies root/output presence before native launch.
SDK-only preflight drops unnecessary app prerequisite and uses exact SDK wrapper
Node; native suite still requires actual app metadata/source, no fallback.

Final SDK correction in two V files only, cdd5→2e9 (same B835aad parent): one
generated model-runtime factory shared by actual worker and preflight, explicit
synthetic thinking support, unchanged expected settings. Pure intent+all-five
actual SDK selection checks passed1.834s (SDK1.75s), tagged compile0.055s, Node
syntax passed. New Bootstrap preflights before Ensure and retains full actual
Create tuple/stage diagnostics plus real team joins. H web source/pins unchanged.
Fresh Luna utility /root/candidate_rooted_2e9 builds exact2e9 with --out-link
/tmp/pi-message-delivery-candidate-2e9 and verifies that GC root/output; no activation.
Log /tmp/2026-11-23-pi-message-delivery-candidate-2e9-build.log. Next only Bootstrap.
Rooted2e9 build passed86s: /nix/store/qlykrbdv9d7b4mrqq10g0j2r9as70xwa-dev-workspace-0.2.0,
own GC root /tmp/pi-message-delivery-candidate-2e9 verified; worker/SDK unchanged.
Third exact Bootstrap FAILED19.9s wall/test4.716s. All5 SDK tuples match; later real
architect0 assignment/publication reports unresolved work/runtime unavailable.
Log /tmp/2026-11-23-pi-message-delivery-bootstrap-2e9.log; artifacts
/tmp/pi-message-delivery-bootstrap-2e9.DQB3Zv. All effects joined. I0 owns precise
underlying-operation diagnosis before further edits/native repeat; matrix held.
Rooted app remains explicit input for fixture-only diagnostics if production
modules stay unchanged; no claim of a new-head build or result reuse. Final exact
candidate/CI remains required for readiness. Fresh remote defaults still0abe/3209.
Diagnostic e1e (only2Vtestfiles, unchanged production/JS) +rooted2e9 app ran once,
FAILED19s. Retained20,887byte setup_failure artifact now survives cleanup:
/tmp/pi-message-delivery-publication-diag.TU8YMG/TestPiMessageDeliveryNativeBootstrap.jsonl.
Full /tmp/2026-11-23-pi-message-delivery-publication-diag-e1e.log shows architect0
original receipt Unknown→Accepted/witness=true twice, then binding publication
unavailable; lead original Accepted/VerifyCreation persisted+bootstrap also pass.
No later native lookup/verify log after recipient Accepted. I0 resumes exact
publication-branch diagnosis from retained evidence; no replay, guess, rebuild or
full matrix. Rooted2e9 app remains available; no final/performance claim.
Progress response native-bootstrap-fixture-preflight: retained snapshot/source
pinpoints FIRST publication guard PiCreation.available()==false. Fixture had only
Catalog+Runtime, missing Selection+StartRequest; no valid async-wait or production
defect demonstrated. I0 supplies strict exact-intent/policy/Start callbacks (or
owning constructor) and pure coherent-service preflight; original guard unchanged.
No new native run/rebuild needed for diagnosis. Then only Bootstrap with explicit
rooted2e9 input, no full matrix until valid five-member/shared-unload gate.
Strict creation-service correction/pure negative+zero-effect test passed0.143s;
compile0.057s; owning V amended e1e→138e, onlyone tagged file120+/1-, no production.
Single138e Bootstrap with rooted2e9 app passed actual5-conversation setup and
verified shared detach, then FAILED36.6s at assertion WorkerPID==0 despite
Loadedfalse (recordPID2319302). Log /tmp/2026-11-23-pi-message-delivery-bootstrap-138e.log,
artifact /tmp/pi-message-delivery-bootstrap-138e.ijSjif. I0 checks actual shared PID
retention contract before correction; no forced metadata or weakened detach proof.
Reload/sibling original witness still unverified; no matrix or latency samples.
Owning shared-detach contract confirmed retained historical host PID/topology;
only wrong PID0 fixture assertion corrected. V971 Bootstrap then PASSED9.09s
(wall23.446s), including actual5-native setup, detach/reload, same shared PID/native
IDs/generation, unchanged history and original sibling Accepted witness. All effects
joined. Log /tmp/2026-11-23-pi-message-delivery-bootstrap-9710.log; artifacts
/tmp/pi-message-delivery-bootstrap-9710.Rssh4Q. Native preflight concern resolved.
Exact971 candidate built87s/rooted /tmp/pi-message-delivery-candidate-9710 ->
/nix/store/m8lmvg7jganiqln30h91iy2wbmas1f26-dev-workspace-0.2.0.

First Recovery971/app971 -failfast completed108.554s: TEN named cases passed
(reply loss, both dispatch crash sides/native loss, ready successor, settings,
policy/instructions/access), then preclaim_member_incarnation failed because normal
CAS correctly refuses immutable identity replacement. No subsequent cases ran.
Log /tmp/2026-11-23-pi-message-delivery-recovery-9710.log, artifacts
/tmp/pi-message-delivery-recovery-9710.saxdzD. Corrected V fault proves CAS refusal/
unchanged bytes, validated private injected identity fault with original authority/
roster/native owner, immutable Admission and zero sends/appends. Pure0.075s and
compile0.057s pass; no production change or supported replacement claim.

Remote fast CI raw log downloaded/diagnosed (not rerun): lifecycle_access_test.rb
plain File.write underumask022 creates0644, private guard precedes unfinished check.
Both exact namespaces failed2/6 then passed2/8 after explicit0600 in0.118s.
Separate focused F26dbaf8447431bb598877464d3cd7b7720b0882e inserted afterB835aad,
V replay389c0503 patch-equivalent to local e4d6f3ec. Main/prep clean; no guards/pins
changed. Raw /tmp/2026-11-23-pi-message-delivery-ci-45319857029-fast.log;
F exact commands/results and tree proofs in B-evidence.md.

Fresh Luna utility /root/native_recovery_tail_389c runs failed+remaining8 ONLY,
testhead389c plus explicitly pinned rooted971 app, unchanged production/JS.
-timeout15m/-failfast; log /tmp/2026-11-23-pi-message-delivery-recovery-tail-389c.log,
artifacts /tmp/pi-message-delivery-recovery-tail-389c.LLxuQN. Ten unchanged passing
case results retained in scope. No performance samples yet; final exact-head
candidate/publication/CI follow stable source checkpoint. No merge/deploy/lifecycle.

Next: retain exact immutable app output, prove only bootstrap/shared unload-load
first, then bounded monitored recovery/performance and applicable longer checks.
No latency target is claimed met. No live runtime/profile/session mutation or
lead-owned temporary service. Leave session and feature refs open.


## Retained detailed lead checkpoints before P4 implementation

Historical working-state snapshot; current phase and ownership are in [state.md](state.md).

# Pi message delivery

Phase: corrected 10k/team 200-sample cell completed and failed both latency bounds;
all200 exact Sent/witness proofs and genuine foreground-time question progress passed.
P4 sufficient design is complete and released to I0 for post-input scalar metadata; larger cells held.
No merge, deployment, reported-live-session change or session closure.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/)
· [Plan](plan.md) · [Design](design.md) · [Review packet](review-packet.md)
· [Independent findings](review.md) · [B/F/H evidence](B-evidence.md)
· [Historical implementation/gate evidence](implementation-evidence.md)

## Phase checklist

- [x] Identity and retained roster verified; initial plan/state committed18e40f0dc before project/external changes.
- [x] Sufficient architect design; A/B/C/V committed with scoped quick checks.
- [x] Independent reviewer0 completed all four lanes, complete history/migration and documentation conclusions.
- [x] R1 concrete worker preservation, R2 separate runtime-key prerequisite and R3 single scope encoder corrected and checked.
- [x] Hydrated Chromium/Firefox delivery UI passed; actual five-conversation Bootstrap/shared unload-reload/original witness passed.
- [x] All18 native Recovery cases passed across three scoped batches; all owned effects settled.
- [x] Exact e662 candidate and CI45339578938: fast/archive/creation passed; host skipped by branch policy.
- [x] T0 quick checks/review/R1 remedy and exact1767 candidate/publication.
- [ ] Final-head CI45348306901 (active).
- [ ] Actual200-sample long-history/team p95 durable receipt<250ms/native acceptance<1s.
- [ ] Final remote equality and complete readiness packet; remain active/open awaiting any future integration direction.

## Current revisions

Both feature branches are `2026-11-23-pi-message-delivery`; worktrees are under
`worktrees/2026-11-23-pi-message-delivery/{dev-workspace,codex-web}`.

- dev-workspace local/published head176706a605119b64f4efd24f0b2f25957caa7298, clean; owning T0 amended atop unchanged e662 parent, review/R1 reconciled.
  Exact e662 CI45339578938 attempt1 completed: fast/archive/creation success, host skipped.
  Published176706a6 after normal fast-forward push and fresh SSH equality; exact CI45348306901 attempt1 active.
  Fresh SSH equality verified after exact971 lease force-push. CI45326414962,
  workflow354263807, attempt1 archive/creation passed; fast failed exact F2 fixture
  (repaired; subsequent0668CI45333033093 fast/archive/creation all succeeded). Remote default0abe5fe48955b1bcdc8cc368fcb27e11e0676f70 remains unchanged.
- Stack above deployed-compatible f3bd843f9858b87cef66d0949706f8af16ba9b13:
  A e50ff02 → scalarC60900b4 → checkedC74f4a6f → dependency82de924 →
  runtime-key prerequisiteb4f3f28 → B835aadce → fixtureF26dbaf84 → V79dd02b0.
  All eight inherited default-to-f3bd deployed prerequisites remain intact.
- codex-web published db79231a4e5513bf439493efab75378bc7d84c04; base/default3209aa7bf93e2c7067b07494d1b254741812d714 unchanged.
  Provider21d9c251 + separate init-onlydb792; CI45304027274 attempt1 succeeded.
  One final five-file consumer dependency82de selects matching Go/Nix/browser input;
  vendorHash sha256-AHXwgkh+p23Ecq0MS/gpfVY1x8QnePpWk73kD3yueHk=.

## Packages and ownership

| Package | Owner | Current result |
| --- | --- | --- |
| D design | architect0 | Complete; design.md includes narrow fixture clarifications |
| A/C and V | implementer0 | Complete; retains source/finding fixes ownership, capacity available |
| B/provider/F/H | implementer1 | Complete; retains source/finding fixes ownership, capacity available |
| Independent review | reviewer0 | Original and affected P review complete, no new findings; retained Sol/xhigh/read_only |
| P2/N1 design | architect0 | Complete sufficient local/private-read and one-live-preflight briefs; no extra optimization released |
| F3/N1 fixture/native corrections | implementer0 | Complete1cbe/e662, quickgreen/clean/capacity available |
| P2local admission correction | implementer1 | Complete09f44, racebarriers/quickgreen/clean/capacity available |
| P3 stage comparison | I0/I1/architect0 | Complete; post-write preflight delay remains inclusive, no safe proof deletion established |
| T0 identified post-sync endpoint | implementer0 | Complete b9d19528 atop e662; two tagged files663+/28-, final native-free2.183s/tagcompile0.073s, clean/released/capacity available |
| T0 affected review | reviewer0 | Complete e662..b9d: one Blocking T0-R1 (partial summary behind held Idle audit), other attribution/history/migration/docs conclusions accepted |
| T0-R1 remedy | implementer0 | Complete176706a6, one-file173+/32- remedy, native-free2.581s/tagcompile0.034s; lead direct step9 reconciliation accepted, clean/released/capacity available |
| P4 post-Accepted scalar metadata design | architect0 | Complete sufficient1943 brief; consumed fields share live source, exact witness unchanged; explicit display-only semantic narrowing accepted |
| P4 source/quick checks/docs/commit | implementer0 | Executing, exclusive source/index window; lead wrote9-line runtime paragraph, owner factual comparison before commit |
| Build, CI, measurement and acceptance | lead | Revised1767 exact200 cell completed275.006s: all200Sent but HTTPp95296.507ms/checkpointp953085.647ms fail; final CI45348306901 active |

Retained saved settings/access unchanged. Roster is rechecked before new substantive assignments.
No implicit member work queue. Exact unrecorded transition times remain unknown; overlapping clocks are not summed.

## Verification

Quick evidence remains scoped: A affected Go plus shutdown/foreground tests;
C scalar/strict legacy/native receipt tests and27Node tests; provider115browser
contracts/conversation and exactCI; B focused queue/web/cmd, full Ruby346/5405
with2existing fixture skips. The broad web run completed744 top-level cases with
2setup/import-fixture failures; both exact corrected tests passed5.930s. No broad
Go all-green claim. Exact commands, failures and reused input boundaries are in B-evidence.md.

H: actual hydrated portal/shared modules passed in Chromium and Firefox15.54s;
controlledHTTP replies, no native/storage/latency claim. Web source/pins unchanged.

Bootstrap971 passed9.09s, proving real five-native setup, shared member detach/reload,
stable siblingPID/native/generation, unchanged history and exact original sibling witness.
Full log `/tmp/2026-11-23-pi-message-delivery-bootstrap-9710.log`.

Recovery evidence (not an aggregate one-run pass):

| Source / batch | Result | Log |
| --- | --- | --- |
| 971/app971 first batch | 10passed; incarnation fixture failed at correct immutable CAS guard | /tmp/2026-11-23-pi-message-delivery-recovery-9710.log |
| 389c/app971 failed+tail | 5passed; storage fixture failed on post-Close mutating Load | /tmp/2026-11-23-pi-message-delivery-recovery-tail-389c.log |
| 79dd/app971 final3 | 3passed,0fail/skip/partial | /tmp/2026-11-23-pi-message-delivery-recovery-final3-79dd.log |

Corrections were V-only: prove CAS refusal/byte preservation before explicitly
unsupported disposable owner fault; remove post-Close Load and capture exact
Accepted receipt after existing inputTasks writer join. Production/worker inputs
unchanged; earlier successful cases retained only within that scope. Final3 exact
artifact-root /proc scan found zero matching argv/cwd processes after command exit.
All18 cases now pass. Artifacts remain in the three named /tmp batch directories.

Prior971CI archive and actual packaged session-creation VM passed. Fast failed an
existing0644 lifecycle-journal fixture; F26db proves both namespaces fail before,
pass after explicit0600 underumask022. New79ddCI validates the committed correction;
no blind job rerun. Host VM79dd separately passed153s, real VM ownership/start/stop/drain with its
synthetic Python supervisor. All owned QEMU effects joined; no p95 claim.

## Review, compatibility and limits

Reviewer0 reviewed old b16 full default-to-head series and provider db792 directly.
R1/R2/R3 narrow requested fixes were inspected and focused-tested under mandatory
review step9. Subsequent fixture corrections preserve production guards and the
reviewed boundary; exact old/new ranges and patch/tree proofs stay in review.md,
B-evidence.md and implementation-evidence.md. F is a distinct one-line test fix.
No obsolete intermediate dependency stream remains. Isolated queue schema1 was
introduced directly; no released intermediate queue, native receipt, legacy wire
or Codex schema migration. Strict witnesses, no ambiguous replay and retained
worker capability gates remain unchanged.

Canonical catalog is ignored/untracked v-fixture/catalog.json SHA256
adb05d10ba504cd3951631f07c450d16a753f75856b41d9c6ad50ecdaaa91aed.
Rooted prior candidate971: `/tmp/pi-message-delivery-candidate-9710` ->
`/nix/store/m8lmvg7jganiqln30h91iy2wbmas1f26-dev-workspace-0.2.0`.
Exact79dd build passed78.7s: `/tmp/pi-message-delivery-candidate-79dd` ->
`/nix/store/pbcm3rfxwd8fnfhd9psw292p83ynjvw7-dev-workspace-0.2.0`.
Log `/tmp/2026-11-23-pi-message-delivery-candidate-79dd-build.log`.
Selected live profile60kkim remains unchanged. No activation or live service mutation.

Performance starts with selectable10000/team_activity to validate actual SDK
history seeding before100000/team_activity; each cell has20warm+200measured IDs.
Conservative HTTP-to-durable and HTTP-to-post-persistence-nativeAccepted upper bounds
are separate from publicSent. First measured result below misses both targets. Fake host/systemd/drain, offline
synthetic model and in-processHTTP exclude physical host/model/TLS cost. Report these
limits and all failures/partials. Keep exact native witness cost.

First performance run completed267.575s using exact79dd source/app and canonical catalog,
30m Go budget,20warm+200measured IDs. All200 measured messages reached Sent; no failed native writes.
Durable HTTP p50/p95/p99/max333.6/378.4/425.0/474.0ms; nativeAccepted upper
2208.4/3566.6/3747.1/3918.6ms; publicSent upper p953877.4ms. Both targets unmet.
Each member delivered40; background250requests/4failures; questionID empty and no
question acceptance observed. Shared workerRSS~1.55GB. The emitted8.34/s Host.Inspect rate mixes warmup counts
with measured elapsed and is not a valid measured-only rate; correct diagnostic before reuse.
Utility joined command/effects and exact private workspace-root process audit found none.
No100k/matrix expansion before existing-artifact diagnosis and affected200sample rerun. Log `/tmp/2026-11-23-pi-message-delivery-perf-10000-team-79dd.log`,
artifacts `/tmp/pi-message-delivery-perf-10000-team-79dd.Qvjj6W`. CI observation
registration refused caller ownership; bounded parent read-only status checks are
used instead, no duplicate watcher/job rerun. No stale active old-head runs existed.

P diagnosis assignments released immediately after failed measurement with live
roster verified. One bounded artifact/source pass each; architect owns sufficient
consequential correction brief, I0 owns native/question stages, I1 local admission/
queue/dispatch. No speculative framework, weakened witness, broad/native repeat or
source edit authorized by diagnosis alone. Observer concern delivery-performance-and-fairness
accepted with concrete measured failures. Host VM passed while diagnosis
used existing evidence; log `/tmp/2026-11-23-pi-message-delivery-host-vm-79dd.log`.

P initial facts: admission NativeDial/HostInspect counters stayed zero. QuestionID
is empty because the fixture never observed CanRespond+options; no response-submission
proof exists, so questionAccepted=0 does not establish accepted-intent starvation.
Max checked concurrency1 is consistent with same-session exclusive effect admission,
not independently a four-worker pool defect. Stage attribution remains open.

Exact79dd host VM command nix build --no-link --print-build-logs
.#checks.x86_64-linux.pi-runtime-host passed0 in153s; utility reported VM script
success and QEMU/test-process join. CI45326414962 archive succeeded; fast/creation
still in progress at last bounded read. No local verification operation active.

P owning-stage evidence:220full snapshots are finishInput post-commit observeState,
so they occur after that ID's accepted timing hook but can block sibling work on
the shared Node event loop.440verify_history comprises220production original-ref
lookups plus220independent fixture checks, each linearizes~3.75MB. Counts/path are
proved; duration attribution is still unmeasured. No witness change authorized.
Lead accepted V-only measurement corrections for architect brief: align warm/measured
counters, label10ms polling sleep honestly, report endpoint/status failures, defer
only independent fixture witness until all four timed batch endpoints complete
while retaining every exact assertion. Original79dd result remains failed evidence.
Next minimal diagnostic is one10k/four-input batch plus question eligibility trace,
not another200samplecell. Architect settles precise seam before I0 source release.

P1 diagnosis complete: newPOST performs five full ready-session joins; statusGET
three; collectionGET four, including repeated disk authority/roster/catalog/tracking
reads. SQLite uses one retained connection/mutex, including FULLCOMMIT, but no
native work under it. Empty files still enter upload catalog transactions. No stage
timers prove which cost dominates. Same-sessionEX spans fresh driver admission,
lease/Bind/Verify/uploads/claim/Cport. Architect is settling narrow runtime/trace
regions and exactCOMMIT return marker for the one4input diagnostic; no proof/cache
removal yet. I0 source released for four settled V measurement corrections and
first coherent commit window; I1 has no application source release yet.

Final79dd fastCI FAILED at TestPiMovedTrackingRecoveryPublicEntryAndRealOwners:
nested CLI compile forces-modreadonly in offline vendored package, GOPROXYoff.
Raw job138216973541 log `/tmp/2026-11-23-pi-message-delivery-ci-45326414962-fast.log`
lines9154-9192 inspected before any retry. F1private-mode fixture and all Rubyshards
passed; this is a distinct fixture compilation boundary. I1 assigned narrowF2
fixture-only fix/proof, no network/skip/production change or broad rerun; P1trace
implementation parked explicitly until F2 complete/capacity. I0 first P0commit
window, I1 F2 second; no source overlap. ArchiveCI succeeded; creation stillrunning.

P0 source milestone: four V corrections and precise one-batch diagnostic are in
its two tagged files; pure ObservationEvidence passed0.061s; final affected pure/
compile checks precede first commitwindow release. No native or production change.
F2 exact offlinevendor failure reproduced0.21s in disposable79dd source with pinned
deps, emptyGOMODCACHE/GOPROXYoff/GOSUMDBoff; corrected checkoutreadonly case passed
14.862s with mod/sum unchanged. Remaining repaired offlinevendor proof uses fresh
Luna/low for cold nested CLI compilation; no app/native/performance build. P1
production trace remains unallocated until F2complete/capacity, then immediate release.

F2 source/check complete, awaiting P0 first commitwindow only: repaired checkout
readonly exactcase14.862s; repaired offlinevendor fresh emptycache exactcase41.84s;
faithful before failure0.21s. One testfile7+/1-, no mod/sum mutation, network, skip or
productionhelperchange. Fresh Luna utility joined tool80873, slot free. F2 commit
then explicit P1 release follows; no optional further checks or source expansion.

P0 delivered b0d2411f4737abb24e5c81b26666b6a2949db2b5 above79dd, two tagged Vfiles
488+/37-, normalcommit/indexempty, I1F2source preserved. Focused PipeObservation/
ObservationEvidence/CounterSnapshot passed0.068s; tagged compile0.062s. NoJS/native
run. Firstwindow explicitly released to I1. Exact task/region/frame/HTTP evidence
and oneStageDiagnostic entrypoint are ready; no p95 result is inferred from this
source. PackagedcreationCI79dd now succeeded, archive succeeded, fast remains
failed only at the reproducedF2fixture. P1source release follows F2completion.

F2 delivered ea17a752b27afe1a7a73336b8c100e8fb79e7f48 above P0b0, exactonefile
7+/1-, clean. Accepted after focused diff and both exact modes. P1 instrumentation
explicitly released to I1 on clean ea17 with exclusive indexwindow, exacttwofiles,
no optimization/newAPI/state/lock/SQL change. First dispatch briefly refused session
command contention; unchanged ID/text retry delivered once, native turn verified.
Architect brief is sufficient; next milestone P1 committed/scopedquickgreen before
affected retainedreview and one combined-candidate3mStageDiagnostic. No source
implementation returned tolead. No native/performance operation currentlyactive.

P1 delivered06680120cd3004afe785043c47781e15cbae66b7, exactea17parent, twofiles128+/12-.
Normalstore2.810s/web11.308s/taggedcompile0.061s; trace-enabledstore4cases0.344s and
web2cases2.470s, parsedGoTrace/balancedregions/COMMIT+claimmarkers. Sourcefreeze
76215f60e1a5e286d81cb823e227aeda02c36eb4a1c56918172881e1c31ae999 matchescommit.
Clean tree/index, all effects joined, no schema/API/SQL/order/auth/nativecall change.
Reviewer0 affected review explicitly started native turn01a20bfd-fbc8-78b0-89f0-be84e1f5172b,
savedSol/xhigh/read_only, all four applicable lanes on79dd..0668, complete19commit
inventory and unchangedprovider/migrationlineage supplied. Packet topsection current.
No longnative diagnostic, finalcandidatebuild or post0668 publication yet; required
review first, then rooted candidate and exactlyone3mStageDiagnostic withtrace.

Affected review0668 completed nofindings in all4lanes; identity/settings/native turn
verified and full conclusions retainedreview.md. Source/quick accepted; latency
criteria remain unmet. Application-only .#default build runs inparallelread-only
review via freshLuna, no tests/activation; exactroot candidate-06680120, full log
/tmp/2026-11-23-pi-message-delivery-candidate-06680120-build.log. Nativeprobe waits
for built exactinput/reconciledreview. Normalfeaturepush79dd→0668 verifiedoverSSH;
old79ddCIallterminal, no supersededactivejob tocancel. NewCI discovery follows.

Exact0668 app build passed81s viafreshLuna, output
/nix/store/aijwyqbp8fiwizw2kf9348xjxiz2yfi3-dev-workspace-0.2.0 retainedroot
/tmp/pi-message-delivery-candidate-06680120; allbuilder effects joined. No profile
selection/tests inbuild. After nofindingaffectedreview, source/root/catalog/policy
verified; one StageDiagnostic launched with3mGo budget, ordinarytrace, no otherheavy
localcheck. Log /tmp/2026-11-23-pi-message-delivery-stage-06680120.log; artifacts
/tmp/pi-message-delivery-stage-06680120.KZPkOb; nativeexit/traceparseexit and exact
fixture-root processaccounting required. This is attribution, no p95 acceptance.

StageDiagnostic0668 completed0(test59.68s); standardtraceparse0(~100s). Artifacts
/tmp/pi-message-delivery-stage-06680120.KZPkOb (34MBbinarytrace,3.078GBparsedtrace),
raw /tmp/2026-11-23-pi-message-delivery-stage-06680120.log. No p95/fairnesssuccess
claim from4inputs. Genuinequestionrespondabletrue observed, response/status400/
403/404 outcomes need exactclassification. Utilityterminaltext had SHAtypo and only
artifactroot processscan; lead independently verified setup.provenance exact0668
and candidateaij/catalog/sdk, then scanned /proc argv/cwd under actualprivatefixture
root /tmp/TestPiMessageDeliveryNativeStageDiagnostic909447311:zero matchingworkers.
All sourcecommand/parse cells complete; effectssettled. No retry/extra native run.
P2 bounded analysis assigned with live roster/capacityverified: I1productionlocal/
COMMIT/admission perIDtrace, I0question/Manager/nativeframe validity, architect
crossstage synthesis/sufficient smallestcorrectionbrief. Stream existing3GBparse,
neverloadwholeintotool/memory or reparsebinary. No code/test/build/native/matrix or
speculativeproof/durability/authoptimization authorized. NewexactCI45333033093,
workflow354263807 attempt1 head0668 inprogress; oldheadsallterminal, no stalejob
cancellation. Runtimeobservercallerownershipunavailable, boundedparentCIreads.

P2 complete perIDattribution: actualCOMMIT offsets238.627/279.303/268.225/284.226ms;
five nonoverlapping localjoins191.149/214.284/218.246/227.409ms, ~80%HTTP; COMMIT
regions2.648–3.969ms. COMMIT->nativeaccepted-write upper1477.9/2160.4/809.6/2803.6ms.
Sessionadmissionaggregate160–1835ms includeswait+proof, lease251–542ms; nativeport
ACK107–143ms is notacceptance. All4exactAccepted/witness/oneappend/enqueue proved.
Questionpositivelyinvalidfixture32hexID caused400, statusroute404, noacceptedintent;
403/canceled tail is stopActivitycontextcancellation, no accessregression established.
Bounded~1MB/7496event extraction and four-IDtables retained in diagnosticartifact;
no binaryreparse/full3GBmemoryload. Fullowningresults B-evidence + P0report.

F3correctedUUID/shortallowlistedplaintext evidence+realhandler/store regression
committed1cbeeb50972adf5e2b57ef08961f1550f689631b above0668, twofiles145+/21-;
web0.111s/pure0.069s/taggedcompile0.059s. Leadinspectedexactdiff, no production
validator/proofchange; validUUID202/persistedsequence, invalid400/404unchangedbytes,
duplicate/revisionconflict proved. Directnarrowfixturefixaccepted; validnative
sustainedquestionprogress stillunverified.

SufficientP2localorderingbrief accepted and releasedI1(sourcewebdriver+existingtests,
indexwindow) after attributioncompletion/capacityverified. Rejectedstalepre-Resolve
proofreuse. PrivateSELECT first exposes/mutatesnothing; mandatoryfreshfullverifyCurrent
AFTERResolve gatesALLoutcomes+initialselection; finalafteruploadproofunchanged.
Savesonefulljoinonly; no performanceclaim. I0capacityafterF3confirmed, assignedN0
boundedread-only Bind/Verify/checkedproof+leaseheldlock distinction, preclaimavailability
mustremain soqueued/unavailable neverunnecessarilyclaimedUnknown. Architectowns
consequentialnativebrief; no nativeoptimization/newprotocol/extraexperimentauthorized.

P2local09f44 committed twofiles247+/10-, fullDurablePortal19.558s/tagcompile0.059s;
3prereadguards+36racecells and2oldoverlayredproofs, factualsourceguards accepted.
N1e662 committed5paths349+/10-, ManagerpositivePreflight ctxbefore/Bindonce/ctxafter
atSAMEpreclaimsite, alllease/local/C/native/ACK/callback/witness retained. No newwire/
bit/format/cache/fallback; genericBindVerifyfreshness unchanged. Leadnativeguide
writingpass preserved. ActualManager/refusal/race/legacy/context batch0.029s,
fullDurablePortal30.735s/crashlookup0.220/tagcompile0.058/strict2830.022 passed.
Source/indexclean, all checks joined, capacityavailable; no nativeperformanceclaim.

Required related affectedreviewof0668..e662 (threecommits7paths741+/41-) assigned
retainedreviewer0 Sol/xhigh/read_only withfull22commit/migration/pin/docinventory,
turn01a20c2f-ea04-7872-906a-74a789577f0a. No longnativeuntilreconciled. Application-
only buildinparallelpassed82s, rooted /tmp/pi-message-delivery-candidate-e6626ff6 ->
/nix/store/ar1z2lz18yfxfwidx9jd4lj6q6x19iki-dev-workspace-0.2.0, logcandidate-e6626ff6-build.log
under/tmp/initiativeprefix. This is no activation/tests; allbuildereffectsjoined.
Correctedexistingone4inputStageDiagnostic willverifyvalidquestion/native endpoints
before200samplecell,3mGo budget,binarytraceretained/noautomatic3GBtextparse. No new
source/harness orlargermatrix. Currentremote0668CI45333033093 allfast/archive/creation
jobs succeeded, hostskipworkflow; separate79ddhostVMpassed. NewexactfinalCIstillrequired.

Relatedaffectedreview0668..e662 completed nofindings/all4lanes, savedreviewer/settings
verified; complete22history/migration/doc conclusions retainedreview.md. Freshfetch
defaults0abe/3209 unchanged. Normalpublished0668→e662 andremoteSSH equality verified;
0668CIallfast/archive/creation succeeded, so no staleactivejob tocancel. Corrected
EXISTINGStageDiagnostic launched once onexactar1z candidate/sourcee662, sameSDK/
canonicalcatalog,3mGo budget/binarytrace retainedonly(noautomatic100stextparse).
Artifacts /tmp/pi-message-delivery-corrected-probe-e6626ff6.MrNuiB; full log
/tmp/2026-11-23-pi-message-delivery-corrected-probe-e6626ff6.log. Goalfour native
outcomes+genuinequestionadmission/acceptance before200sample rerun; no percentile
from4. FreshLuna ownsrun/exactfixture-rootprocessjoin, parentactive. No newsource,
harness,diagnosticexpansion/100k/cell beyondthis probe authorized.

CorrectedStageDiagnostice662 passed59.896s, same4exactSent/nativeproofs. HTTPupper
198.6/216.0/209.1/233.3ms; nativeacceptedupper3393.9/1340.2/2577.7/1981.2ms.
RealquestionUUIDce9bef71-295e-4ee8-8d23-be64b9c4e6f0 POST202/persistedsequence1,
laterdelivered/Accepted, accepted42.380s; no p95/sustainedfairnessclaim. Actual
privatefixturetoproot /tmp/TestPiMessageDeliveryNativeStageDiagnostic2380818311
/proc argv/cwdscan found0workers. MachineJSONL/provenance/binary+exit0 retained;
utilitylog is capturedtooltranscript, notdirectrawstdout/stderr (labelnotfullraw).
No rerunforlogging. Correctedbinary34MB retained; no3GBtextfile expanded.

P3 boundedcomparison allocated withroster/capacityverified: I1same4-ID local/
admission/lease/preflight/Cport table, I0realquestion/Manager/nativeframe paths,
architectcrossstage synthesis/minimalsafebrief. Realquestion isnewcompetingeffect,
orderchanged, notsimpleperIDmarginalregression. OnefreshLuna streamingexistingbinary
filter passed0/77.297s, directrawstderrlogcorrected-trace-events-e6626ff6 under/tmp
initiativeprefix; events.txt7975lines/1140078bytes nowreadyinnewartifactroot, all
extractioneffectsjoined. Readinesssentall3peers, oneCLIlockrefusalretriedunchangedID.
No source/newnative/profiler/marker/200/100k authorized duringcomparison; no authority/
positivepreclaim/EX/witnessweakening. Next concrete remainingcost/correctionorconstraint,
then affected200sample acceptance. Exact e662 CI45339578938 attempt1 subsequently completed fast/archive/creation success; host skipped.


P3 closed with a measured constraint: three slow preflights spend 299.7–394.3ms
after full identity request writes. Existing evidence does not split worker/control
reply wait from Manager post-reply proof, and no further safe check deletion was
established. The corrected four-input probe proves real question POST202/sequence1
and later Accepted, but establishes no p95 or sustained fairness. Detailed tables
remain in design.md P3 and B-evidence.md.

T0 milestone: registration and outer checkpoint composition are in place; callback
uses the already-held engine mutex, nonlocking strict receipt read and a short
counter lock, with no conversation lock or native call. I0 is completing sample
wiring and actual receipt-writer fault/restore tests before quick checks and a
normal two-file commit. Review and one corrected 200-sample 10k/team cell follow;
no new component attribution or larger matrix is released.

T0 b9d195283cbd25d5fb696575aa24a746109e919b committed normally atop e662,
clean tree/index and exactly two tagged files. Final actual-writer/finishInput
native-free checks2.183s and tagcompile0.073s; source owner transcript session40200
completion chunk81672c is evidence (no standalone raw log). Retained reviewer0
assigned related four-lane review, turn01a20c64-1403-77c1-8a01-1d3c43592aaf. Fresh
Luna candidate_t0_b9d19528 owns one application-only build with direct raw log
/tmp/2026-11-23-pi-message-delivery-candidate-b9d19528-build.log and owned GC root
/tmp/pi-message-delivery-candidate-b9d19528. Native remains held; one corrected
20-warm/200-measured 10k/team cell follows reconciled review and exact inputs.

Exact T0 candidate build passed87.762s exit0, fresh Luna operation/cells joined.
GC root /tmp/pi-message-delivery-candidate-b9d19528 points to
/nix/store/082h4l2402kcsbjdmsbqy35wds7cxlz2-dev-workspace-0.2.0. Direct raw build
log retained at the path above; no activation/native test. Metadata protocol2,
worker sf66, SDK9hf and Nodegf597 agree; catalog SHA remains adb05d10...aa91aed.
Review remains the sole acceptance-run gate; no more source work is allocated.

T0 affected review completed one Blocking R1; full fidelity report retained in
review.md, original in lead conversation. Lead confirmed unconditional Idle precedes
only summary. I0 assigned direct narrow remedy, turn01a20c6f-4c68-7972-bb05-0e29310bc148;
no new measurement design/native experiment. Known failed/held cell must retain
partial intervals/counters/late-health and explicit skipped audit without idle wait;
successful cells retain every final audit. Direct review-step9 verification follows
quick checks; no automatic reviewer rerun. Unpublished b9d amendment preserves e662
parent; revised exact candidate needed before acceptance cell.

T0-R1 corrected owning head176706a605119b64f4efd24f0b2f25957caa7298, e662 parent
unchanged. Lead direct diff and actual held/fatal-audit regression/log inspection
resolved Blocking finding under step9, no design expansion/re-review. Full23-commit
lineage/migration and prior conclusions retained in review.md. Normal fast-forward
feature publication e662→1767 and fresh SSH equality verified; default0abe unchanged.
Fresh Luna candidate_t0_176706a6 owns revised app-only GC-root build/direct raw log.
One exact10000/team_activity cell follows candidate input verification; no larger
matrix/component audit/native probe.

Revised exact1767 app build passed85.549s exit0, direct log
/tmp/2026-11-23-pi-message-delivery-candidate-176706a6-build.log, GC root
/tmp/pi-message-delivery-candidate-176706a6 ->
/nix/store/75sbqgl6xqg1626hml6qf9i1i47p9mkr-dev-workspace-0.2.0. Metadata
protocol2/worker sf66/SDK9hf/Nodegf597 and canonical catalog hash verified.
Fresh Luna performance_10k_team_176706a6 owns exactly anchored
^TestPiMessageDeliveryNativePerformance$/^10000$/^team_activity$, count1, Go30m
budget/expected4–6min; no trace/profiler/additional cell. Direct raw log
/tmp/2026-11-24-pi-message-delivery-perf-10000-team-176706a6.log. All checkpoint/
commit-write/public-Sent/observer-overhead/failure/witness/fairness evidence retained.
Parent active, no duplicate benchmark log polling; terminal fixture-top process
accounting required before utility slot reuse.

### Corrected T0 actual200 result (176706a6)

Fresh utility performance_10k_team_176706a6 completed exit1 in275.006s (Go260.630s),
exact anchored10000/team_activity only. Both preliminary and final summaries retained;
final partial:false/passing:false/auditCompleted:true.20warm+200measured allSent,40
per member,200 independentAccepted original witness proofs, no sample failures.

| Complete-body HTTP-start upper | p50 | p95 | p99 |
| --- | --- | --- | --- |
| Durable HTTP |254.699ms|296.507ms|318.902ms|
| Identified post-sync checkpoint |2027.673ms|3085.647ms|3383.749ms|
| Later commit-write |2030.083ms|3086.875ms|3385.159ms|
| Public Sent |2528.885ms|3488.572ms|3746.207ms|

Both target assertions failed. Earlier/later uppers nearly agree here; still not
literal fsync completion or worker CPU attribution. No percentile subtraction.
Measured observer200calls/reads,0errors,378.113111ms verification total/1.890566ms
mean,7.225136ms maximum; observed live/pending maxima1. Observer occupancy can
perturb siblings, no zero-overhead claim.0late holds, failedcommitwrites and
receipt-delegate errors. AdmissionHostInspect/RuntimeDial remain0. Measured native
deltas200enqueue/commit,201snapshot,400verify_history,527identity,151workflow_observe,
23inspect_origin,1ordinary question send.

Real question response adffeb5c-bec2-4d74-aacc-5b1492578d38 POST202/exact persisted
sequence1/pending thenAccepted during measured foreground; fairness assertion passes.
All9background HTTP failures have explicit contextcanceled stop-tail evidence.
Successful final history/receipt/at-most-once audit completed. Native effects settled:
JSONL-derived top root /tmp/TestPiMessageDeliveryNativePerformance10000team_activity45167363
/proc argv-or-cwd scan0, all utility cells/session9735 joined.

Direct raw /tmp/2026-11-24-pi-message-delivery-perf-10000-team-176706a6.log; JSONL499
records at /tmp/pi-message-delivery-perf-10000-team-176706a6.rd3wbgfz/
TestPiMessageDeliveryNativePerformance-10000-team_activity.jsonl. No retry, trace,
100k or broader cell. P4 assigned architect0 only, turn01a20c7f-0f9e-7051-b8a7-9fc4dc90d649:
assess whether known post-Accepted full snapshot can preserve its exact required
state/proof at narrower owning seam, or report constraint. No duration inferred
from counts, no new instrumentation/permission/witness/EX weakening. I0/I1 available
but unallocated until sufficient brief; source remains clean1767.

P4 architect source proof confirms observeState consumes scalar metadata fields
already present in identity_v1, not display entries/hash/paging. Lead accepted
post-input-only semantic narrowing: metadata refresh omits incidental display
limits; real full transcript/state reads retain them. Frozen launch capability,
actual Thinking/HistoryFile/Persisted refresh and all mapping/held/pending/callback
errors retained, exact native durability/witness and Lookup unchanged. No duration
claim from call counts. Sufficient design.md1943 brief released to I0 at
turn01a20c86-f46e-7381-9a05-edec12411c66, base1767, only allocated Go/runtime tests,
private supervisor reader seam, existing Node protocol tests and docs. Lead direct
writing pass adds9lines under Live identity proof; I0 preserves/factually compares
and includes only after final agreement. No native/build/profiler/200 by owner;
focused checks/normal commit then affected review/exactcandidate/affected200.

## P7 profile-driven serialization reuse at75c810a2

User supplied successful unprivileged profile /tmp/pi-node-sample-ybjldlex/findings.md
and directed exact-proof-preserving serialization reduction +200 rerun. Architect
sufficient P7 brief in design.md accepted; I0 allocated turn01a20cf5-5293-7043-8316-be68f3a7ffbb
with sole two-file source/index window. Final commit75c810a2eb0f8631dd4450e9dc3947bd491f501d
parent474872b602afa0813e6a17a951646b5cf5a91a06 tree71205b34931effb5defe4e29fe1bc0736119f93e.
Session.mjs12+/4-, input-delivery.test.mjs99+/2-, clean/released/capacity available.
One fresh current JSON per synchronous observePersisted reused for exact count/
prefix+comma-boundary and fresh complete independent disk serialization comparisons.
Frozen admission/native proof/sync/witness/originalLookup/no-replay unchanged.
No new protocol/pin/schema/capability/Go/V/metrics/cache/framework. Current serialization
exceptions hold Unknown. Comment owns code-unit boundary; product contract unchanged.

Final exactsource quick: Nix environment + pinnedNodegf597/SDK9hf; --check bothfiles;
node --test pi-runtime/src/input-delivery.test.mjs pi-runtime/src/lineage.test.mjs
pi-runtime/src/persistence.test.mjs pi-runtime/src/protocol.test.mjs PASS54/54,0skip,
2685.606ms; selectedsession ordinary freshandretained input + nativesyncfailure
PASS2/2,0skip1980.900ms.32case actual makeInput/observePersisted oracle and successive
fresh/serializationfault regressions, real SDK legacy/queued/witness/reload/syncfault.
Normal hooks/no bypass/no declaredframework; diff/cachedchecks clean. Log
/tmp/2026-11-24-pi-message-delivery-p7-quick.log SHA256
96b9ada50f833b16034e2e3ab62853453e4ae1acf4d37b970d39714e4f78f842. Owner
tool99098 chunksde64ec/710d95 exit0; commit432408 exit0 joined. Source sessionSHA
5166dfc3d8a8c346c29bceb88fbc8f06a65b4be30dbff0adde4819d7a1d4c8f3; inputtestSHA
e2a67ab4a098a41863b57daca70e15b7d25ed8b873441933b21291af2eb5b22b.

Retainedreviewer0 sameSol/xhigh/read_only all4lanes final75c810 review nofindings,
full26history/no-newmigration/solepin82de/docs7 conclusions savedreview.md. No quick
rerun by reviewer/lead. FreshLuna candidate build exact75c810 PASS81.9s; root
/tmp/pi-message-delivery-candidate-75c810a2 -> /nix/store/2vk8nlip55qvr99qis1fhac60sc76psf-dev-workspace-0.2.0.
Directlog /tmp/2026-11-24-pi-message-delivery-candidate-75c810a2-build.log, operation
77252/allcells joined, cleanhead before/after. Worker c2j95cws30apvasfqv7klib5f43pwj72,
protocol2/Nodegf597/SDK9hf; lead packagedsessionSHA matches exactsource. NormalSSH
push4748->75c810 and freshremote equality/default0abe verified. ExactCI45369874954
attempt1 started; runtime monitor owner refused, boundedparentGHfallback/no duplicate
watcher. One unchanged20warm+20010k/team nativeperformance assigned freshLuna, no
profile/overlay/proof/metrics change. No new native result claimed before completion.

P7 sole200 COMPLETE exit1/267.59s wall (Go248.998s), all20warm+200measuredSent/
40permember,200 measured independent proofs retained. Preliminary summary partialtrue/
auditCompletedfalse; Fatalintegration2414 Pi runtime unresolved work. Exactp95ns
HTTP296721835/post-sync3064622950/commit3065897277/publicSent3445768218; both budgets
miss. Questiona52d8b86-ab14-4f9c-99dd-70ce8cad91d2 POST202/sequence1 persistedpending,
AcceptedNS0; no fairnesspass/finalnativeappendaudits claimed. PreAudit latehealth0,
measuredobserver200reads0errors404802083ns sum, complete counts/distributions in
retainedpartial. Actualfinal audit fields nil, per-ID/batchproof rows preserved.
Raw /tmp/2026-11-24-pi-message-delivery-perf-10000-team-75c810a2.log SHA256
aa3062c9f964912688a73eaa2d21225d5a2ebbd22172edf95fc83280a7392a16; JSONL
/tmp/pi-message-delivery-perf-10000-team-75c810a2bw8wybm3/TestPiMessageDeliveryNativePerformance-10000-team_activity.jsonl
SHA256b5296136249478ae7fda42fb1997ff87fdc01823b2216b2c577adb86aa82be63.
Allcells/session59870/wrapper807854/Go807875 joined; actualfixturetop472835251 gone,
/proc argv+cwd0. No cancellation/cleanup/retry. I0 assigned bounded readonly
auditfailure diagnosis, no edit/native/newrun authorized. FinalCI archivepass,
fast/creationrunning at latestread. Source clean75c810.

I0 bounded failed-audit diagnosis: integration2414 Idle -> fixture633/waitIdle ->
supervisor_test185 Manager.Load typedErrHeld, not deadline/stateassertion. Shared
loopline/no membermarker means exact member/iteration/innerHeld branch unknown.
No product-vs-fixture or pendingquestion cause established, no production fix
allocated.220samples ProofPhaseAccepted/no errors+55 independentgroups and original
enqueue1/checked1 counts retained; missing final nativeappend/receipt/history/memory/
postAudithealth audit cannot be synthesized. Latency/fairness assertions not reached,
retained distributions still miss budgets. Question valid202/exactseq1 remains
pending lastGET237.0174..237.1449s, noAccepted/fairness proof, not starvationproof.
All16HTTPerrors are canceledstop-tail. Reportfailed result before further work.
No new tests/build/native/source/profiler action; owner released/capacityavailable.
## P8 development continuation: committed quick-green package

Finalb07 artifactbuild0/82.728s `/nix/store/yfkkdq85248gwdbmh0hbffkic8mgsnq4-dev-workspace-0.2.0`,
root `/tmp/pi-message-delivery-candidate-b07fec04`, completebuildlog sameprefix
`/tmp/2026-11-24-pi-message-delivery-candidate-b07fec04-build.log`.
Inventory has noadded/missingpaths, exactsameportalbinary32388912bytes
SHA1e751929317d01e463dab68adbd214e9eb24d0cc92f9975f66dc0ba75a53de04,
sameworkerJSON/SDKnvwxl/Nodegf597/worker74ka. Eightdifferences are fourwrappers
withonlyapp-rootrelocation, three skill symlinkswithonlyself-sourcepathrelocation
(alltargetfiles byte-equal), and extensionJSONwithonlythree skill-sourcepaths
relocated. Leadcheckedallrawbytesafteronlythetwoexactrecordedpathsubstitutions,
no generalnormalization. `/tmp/pi-p10-final-artifact-inventory.json` and
`/tmp/pi-p10-final-artifact-equivalence.json` bindold0226/newb07/storepaths/scope.
NativefixtureGo/test/runtime/SDK/Node andportalbinary unchanged; old0226performance
remainsqualifiedcorrespondingevidence, notliteralb07nativeexecution/fullstoreidentity.
Noautomatic200repeat. Alllocal88435/tool/build/comparison effects joined.

Normalfeatureforce-with-lease0226→b07f verifiedfreshSSH, master3961 untouched.
Superseded0226CI45403167502authoritativelycancelled. New45407328539 onb07 passed
sourceprep+all-checkevaluationcoldrunner, remainingpackage/creation/archiveactive.
All4laneaffectedamendmentreviewnofindings/full11file3commit/migration/doc conclusions
inreview.md. No deployedprofile/system/worker change, no claims/integration/lifecycle.

P10-SDK actual200 completeexit1/248s at0226: all20warm+200measuredSent,
40measured/member,55independentproofgroups, all220nativeappendsexactly1,
auditCompleted:true/partial:false/passing:false, all32auditboundaries. Question
POST202/sequence1 admitted and Accepted at75.4249s duringforeground; fairness
assertionpassed. Onlylatencycriteriafailed; latehold/commitwrite/delegateerrors0.

| Endpoint | p50 ms | p95 ms | p99 ms |
| --- | ---: | ---: | ---: |
| Durable HTTP upper |242.623|282.851|288.700|
| Post-sync acceptance upper |1772.127|2820.310|3029.539|
| Commit-write upper |1773.404|2822.232|3030.783|
| Public Sent upper |2173.199|3127.096|3379.460|

Modestlowernumbersvs3054 do not isolatecausalSDKsaving; workload/question/hostnoise
differ. Targetsremainunmet, noadditionalperformance/profilecampaignallocated.
Measuredobserver200reads/0errors337322402ns total;754identity/400verify_history/
200enqueue+commit/172workflow/34inspect_origin/1snapshot. All12backgroundHTTPerrors
contextcanceledstop-tail. Raw `/tmp/2026-11-24-pi-message-delivery-perf-10000-team-022646d7.log`
SHA91b4137eaf3f8a38edfe2666353f6ab7e6415f7a25950f46d6d1daa0827e17a1;
JSONL `/tmp/pi-message-delivery-perf-10000-team-022646d7/TestPiMessageDeliveryNativePerformance-10000-team_activity.jsonl`
SHA249abd68edc4ee9416ad372185ffc0d962e373ef17737d4c33e2f75d7bd31818.
Fixture943996999absent/parentargvORcwdscan0, allutility68044/test/child/cellsjoined.

CI45403167502 fastfailedBEFOREbuild at unchanged `nix flake check --no-build`:
upstreammetadata/importNpmLock readsderivedpatchedsource, unavailable inno-build
evaluationstore; localrealizedsourcebuilt successfully. This wasnotnix-eval-jobs
(earlyhypothesiscorrected). Rawjoblog `/tmp/2026-11-24-pi-message-delivery-0226-ci-fast-job.log`.
Architect ownsminimum explicitexisting-source-preparation target/CIstep brief,
preservingSDK+appderivation/proofequivalence; no unmodifiedCIrerunorignoredfailure.

P10-SDK final independentreviewer0 all4lanes nofindings, fullcurrent3commit
history/no obsolete update/no migration/docs conclusions retainedreview.md.
NormalSSHfeaturepush3054→0226 andexactremoteequality verified; master3961 unchanged.
CI45403167502 active. Exactnewappbuild0/78s once, allcellsjoined, root
`/tmp/pi-message-delivery-candidate-022646d7` →
`/nix/store/b7nb8irr700aib3l1mj7sb3b88kcw91y-dev-workspace-0.2.0`.
ManifestbindsNEWSDKnvwxl/Nodegf597/worker74ka42h; exactsourcehead/treeclean.
Buildraw `/tmp/2026-11-24-pi-message-delivery-candidate-022646d7-build.log`.
Oneunchanged20warm+200measured10k/team allocated freshLunaCLI68044 withcanonical
appstorepath/newSDK/originalcatalog, originalendpoints/receipt/fairness/finalaudits.
Outcome pending; no speedprediction/deploy/merge/profile/largermatrix.

P10-SDK source complete022646d73bde4fbc468ed68835499158e8727b2c atop3054,
tree9d2b35c840dccc5cd82c7ad09fc585e70a7c317b clean. Five files179+/7-, one TS
source guard via normal upstream source override, public-SDK regression and lead
README/runtime prose. No locks/input revision/NAR/npm/catalog/version/Node change.
Upstream4462 source files differ only sdk.ts guard. Actual compiled sdk.js only
new condition; runner/AgentSession/types/manifests byte-identical. All eight
workspace packages rebuilt coherently with actual tsc/offline build, no installed
JS/WorkerSession monkeypatch or extra export.

Selected prerequisite SDK build0/144.979s, exact new path
`/nix/store/nvwxl97fj19gvy9bnvr8s485jpn5hjmm-pi-1.5.2`, rooted
`/tmp/pi-p10-sdk-dependency-root`; NARsha256-olnZQwmLmbvsozq+cwG1mi6xtfSetZthzrCRcKSr/6A=.
Derived sourcexs767f5/NARsha256-X3eyG/ZKadUUtVVpYa24tjBwCbg30ROI6tLc4A3ucq0=.
Build logSHA3774a9827c172271c885fafb61a5886f13e8db2717240d55448554be98607063;
provenance log `/tmp/2026-11-24-pi-message-delivery-p10-sdk-provenance.log`
SHA854f9dff03b0a5bdc9735de4e73adcf0fe4c9bb7feb849b0e8ba424555f41447.
New-artifact quicks9context/54proof-policy/3session all pass/no skips,
2.420/2.857/2.161s. Log hashes and commands in top review packet; no oldSDK fallback.
Normal focused commit, hook policies preserved, all effects joined. Reviewer0
assigned final all4lanes/complete3commit history; fullapp/native not yet started.

P10 current profile: original test PASS0/60.34s, runner1 recorded identity mismatch
and original analyzer1 refused. All children settled, actual fixture603535069 absent.
No rerun. I0 read-only diagnosis found2181 stable accepted PID2322417/born212635123
rows (test2322360) covering full profile and every four-input endpoint; raw rejected
tuple was not saved, cause unproved. Error occurs after last stable row, >18.847s
after profile end. Separate positive validator binds all raw/prep hashes, current
candidate/modules/binary/catalog, accepted identity predicate, monotonic CSV,
profile clocks and four complete original proof/appends/final audits. It passed
WINDOWVALIDATED only; original runner/analyzer remain FAILED without edits.

ROOT `/tmp/pi-node-sample-3054dda3.imi51nn8`; exact window2.875925s, profile covers
it with5.398s/.769s margins, offset drift-0.104ms, millisecond wall/microsecond
profile precision disclosed. Shared-worker sampled SELFms: idle834.815,
SDKparse414.907, structuredClone380.961, observePersisted277.934,
makeInput231.184, GC212.907, linearEntries52.333, getBranch46.178. Parent stacks
are context, not additive: clone principally SDK extension emitContext/transform;
parse in fresh SessionManager.open under verifyHistory and observePersisted.
Passive same-window mainCPU2026.941..2054.290ms, runqueue0.724ms,25ms bracket
uncertainty. Not per-input exclusive CPU, production p95, native completion,
isolated causal P7/P8 saving or P9 tab delay evidence.

Window validator/log/receipt SHA256a8e2453115d1da2fae490a1ed1e640ff627398c1176f89f4a62166ff8ef5d2c3 /
fd4731a223e51472610f52f801f8e9c80893333c2ee250c47549cccc184321b7 /
358b1c02efe0004086fe0d11ed853060892da89beafba6b2ed411e18b8d4839e.
Original profileSHA93aa076c124886a653107aaa8c5e8b2735dd279950d16fdb460bfb2bb7da38cd,
CSVSHA8a9f4d4d8362a35c038071e1724e8fde437d4b1279d90740b2f756dbd566a31f,
JSONLSHA15dbca6925bab46e3f79943502929cbb38a90ad3709e6fe655448d835faa0315.
Source3054 remains clean. Architect owns one bounded conventional opportunity
selection or explicit constraint closure; no further native run/source edit released.

Actual canonical200 result: exit1/252s (Go249.283s), complete audit and failed
latency/question fairness. All20warm+200measuredSent,40measured/member,55 independent
proof groups and all220 native append counts exactly1. Full32 audit boundaries,
auditCompleted:true/partial:false/passing:false. No late hold, commit-write or
receipt-delegate errors. The previous auditHeld did not recur; its cause remains
unknown. No unmodified rerun allocated.

| Endpoint | p50 ms | p95 ms | p99 ms |
| --- | ---: | ---: | ---: |
| Durable HTTP upper |249.804|286.087|328.081|
| Post-sync acceptance upper |1892.884|2979.109|3072.211|
| Commit-write upper |1894.027|2982.772|3073.491|
| Public Sent upper |2357.406|3389.812|3587.340|

QuestionIDempty/Postnull/AcceptedNS0: all31successful lead polls remained pending
and unrespondable. All15background HTTP failures are context-canceled stop-tail;
no permission/starvation cause established. Measured observer200reads/0errors,
379427592ns total;741identity/400verify_history/200enqueue+commit/162workflow calls.
Current workerRSS407440kB is uncontrolled one-run evidence, no GC/heap or causal
speedup claimed. Existing targets remain unmet.

Raw `/tmp/2026-11-24-pi-message-delivery-perf-10000-team-3054dda3-canonical.log`
SHA256f13f78c5913b70bc72ebc600e9ec645b31c168dab930f0042b069743e908cf5d.
JSONL `/tmp/pi-message-delivery-perf-10000-team-3054dda3-canonical/TestPiMessageDeliveryNativePerformance-10000-team_activity.jsonl`
SHA2560636e61cbdf6323161451e678929e293a096bd7270c1bfb21bea15aa5ce3d52c.
First symlink-app attempt failed before samples; original wrapper-time failure
also launched no benchmark. Canonical actual run executed once, native fixture
978519265 removed by its normal test cleanup; parent argv OR cwd scan0. All CLI,
tool38736/session83983 and owned children joined. Watcher incorrectly named the
catalog as fixture root in its report; authoritative setup execution workspace
established the actual root for final scan. P10-D and P8-Q separately allocated
bounded current CPU attribution and question evidence diagnosis; no live effects.

Final independent reviewer0 Sol/xhigh/read_only assessed all four lanes for
3961..3054 with no findings; complete report retained in review.md. Exact candidate
build passed81s once, all original build effects joined, root
`/tmp/pi-message-delivery-candidate-3054dda3` →
`/nix/store/pxw8ngf2aknagbg2s2a1wc3w50jdaa82-dev-workspace-0.2.0`.
Worker157f5yaw/SDK9hf/Nodegf597 metadata retained; packaged session hash equals
reviewed sourceda0640e1. Log `/tmp/2026-11-24-pi-message-delivery-candidate-3054dda3-build.log`.
Initial watcher interruption was reconciled by joining the original session,
exit0; no repeated build. Runtime monitor registration refused exact caller,
documented fresh Luna/low native fallback used. No uncertain build effects remain.
Normal SSH development-branch push3961→3054 and fresh exact remote equality
verified; master remains3961. CI45392785202 attempt1/workflow354263807 started.
One exact200 cell assigned fresh Luna utility, no profiler/overlay, same catalog
SHAadb05d10 and unchanged20warm/200measured10k/team endpoints/audits. Outcome pending.

Merged baseline3961 → test-only ca7637c9 → private prefix cleanup3054dda3,
tree0abda897bbe523d868aedab22677516995e48b74. Complete new range has two distinct
commits, five files270+/24-, no pins/migrations/protocol/schema change. Source
and index clean; both implementers explicitly released windows and joined effects.

P8-M clears only prefixJSON after successful queued-input committed transition.
Same active/accepted object and every other provenance field survive. No pending,
Accepted-before-commit, legacy, Unknown, error or abort behavior changes. Actual
pinned-SDK tests prove retained callback origin, fresh independent history witness,
no native replay and zero prefix strings in twenty committed retained entries;
an independent pending input preserves its original bytes. This proves reference
release, not collection, RSS reduction or a measured speedup.

Declared Nix/SDK9hf/Nodegf597 quicks: syntax and input-delivery/lineage/persistence
51/51 pass2.946s; exact persistence/reload and sync-failure2/2 pass2.032s; no skips.
Raw `/tmp/2026-11-24-pi-message-delivery-p8-prefix-quick.log` SHA256
19a26e7a9f1cccaf29a4dfcd4522183351442ec5a55051191d0c0c7eb354122a;
`/tmp/2026-11-24-pi-message-delivery-p8-persistence-quick.log` SHA256
fc4f07e4cfbbeff434241602f23c69e9dad62633680169a7289de9b24d144323.
Final source SHA256 sessionda0640e10fd01ed9c457f7b6574dd271b1ce639754fcc88ca67535be5a39874a,
inputtest325c5d3846d78ec0a54eecb3978bf679b4869385fd86e4d1b02ca27fe04c5ced.

P8-F retains synced audit begin/end member/fullhandle/stage and the same failing
Load's state/iteration/context/error type/class/bounded detail before unchanged
Fatal. Shared loop retains original call/wait behavior. Six child-fatal cases pass
0.442s, tagged compile-only0.063s; normal focused commit and final diff check clean.
Raw `P8-F-final-commit.log` under session Files. No new RPC/retry/drain/observer,
changed acceptance clocks or removed final/fairness audits. Exact old failure
cause remains unknown. See top review packet for complete source and check scope.

P9 read-only source pass: shared hide/show scheduler requests immediately;
Pi transcript does full-branch digest and receipt projection, while SSE-open may
cancel/restart an in-flight read. These are unmeasured opportunities, not an
explanation of the reported5–10s. Accepted design.md P9 requires actual-tab timing;
target/capture route pending. No browser/native/live effect or tab fix claimed.


## D3-F frontend source comparison (read-only)

I0 inspected owning runtimee61/providerdb792 browserfiles, clean/no edits/tests/
browser/live/native/profileeffects. Report directarchitect d26a3dfa-8004-4903-9be1-a1a5dec348d2;
leadaccepted sourcefacts, no measuredcause. Pi app.js7324 mounts deliverypanel;
shared deliveries.js87–128 immediately reads then polls2000ms AFTER eachcompletion
evenempty/terminal/error; singleflightownreads, no in-flight abort on hide/destroy,
return joins pre-hideGET. Collection success rebuildsstatuscards90–109.
Checked Pi submit app.js7391–7412 awaits pre-read/selection/scope/settings/mode
validation, then savedoriginalID/POST, only then clearsdraft/showsstatus, followed
by anotherread. Codexordinary7430–7492 capturesdurablewaitingID/clearsdraft before
asyncdispatch. Preserve positivefreshness/durableoriginalID/no-replay/Queuedtruth.
Actual retainedcapability/route must be observed before claiming alltabs checked.

New workflowredundancy: app.js8020 refresh aftereverytranscriptapply;8040–44 again
onconnected; createPiWorkflowPage1685–1704 can duplicate mountautomaticread.
pi-workflow-ui.js221–233 launches question+plan concurrently EACHrefresh;refreshID
dropssupersededresults butdoesnotcoalesce/abortrequests (destroyonly33–49/240–244).
Epoch/sequence62–73 freshnessguards remainrequired. These reads are fire-and-forget
AFTERtranscriptDOM, not awaitedfirstpaintbarrier. Conventional candidate only
scoped/mutation-aware readcoalescing with dirtyrerun/freshguards, notcache.

Sharedsync startsimmediatelyonvisible/SSE,focus250ms,onopen cancels+freshread to
preserveeventgap, activecalls dirtycoalesce, errorsbackoff800–1000ms then<=30s.
NoPi-onlyfixed5–10stimerproved. Sharedkeyedrender6020–6129/5851–5920; Pi livekeys/
planjoins extra, allunmeasured; receiptsasyncnotrendergate. Sharedactivity5/30s and
details15s runparallel. No actualuserbrowser connector/capture; one normal real
navigation/hide-return with Network+Performance must split event/request/TTFB/body/
parse/apply/paint and overlappingdelivery/workflowrequests. HTTPprobeisnotbrowser
latency. Fullreport retainedinlead/memberconversation, architect owns synthesis.

## D3 read comparison: completed bounded result

The first sampler stopped after one shell GET (200,1.520534s): its global scope
attribute search was ambiguous because the template has body and descendant team
scopes. That is a diagnostic parser defect, not deployed refusal. Original raw
`/tmp/pi-d3-reads-a8rwk01t/` retained unchanged. Standard body-only HTMLParser was
locally proved with2positive/7negative cases; no application change. Next utility
65201 used a wrong script path and exited2 before sampler,0newGET; its original
raw `/tmp/pi-d3-r2-ev89ayyx/run.*` retained. Literal prepared launcher removed
ROOT substitution and checked frozen sample SHA256c87ebb716715942ee45cc03a1d8d71334aa1b9e79f2f23f2abbc046ed421828b.

Fresh Luna/low utilityCLI6620 completed exactunchanged sampler in4.523578s, exit0,
11GETall200, allclients/tool/watcher effects joined. No body/target/scope retained
in metrics; privateconfig remains0600/ignored/untracked. Raw `/tmp/pi-d3-r3-run.log`
SHA256acebf6b5621010460f3a62d99646450b8ea426c5f86b0cbaf520df2802e1b678,
result `/tmp/pi-d3-r3-run.result`, timings `/tmp/pi-d3-r2-ev89ayyx/timings.json`.

| Endpoint | Serial total (s) | Concurrent total (s) |
| --- | ---: | ---: |
| page | 1.211839 | 1.309754 |
| activity | 0.786367 | 0.808882 |
| deliveries | 0.149735 | 0.218275 |
| questions | 0.166452 | 0.145808 |
| plan | 0.105835 | 0.146410 |

Scope shell0.557867s. Samepage67706bytes, bodytransfer negligible. Page existing
Server-Timing1210.35→1307.88ms; activity785.14→807.62ms, side routes absentheader.
One same-target serial/concurrent sample, not browser/p95/sustainedload/causal
attribution. Side overlap adds about98ms page/23msactivity here, not multi-second
amplification. Prior source redundancy remains real but unprovenremedy. Prioritize
page/activity substage attribution; architect owns final synthesis, no sourcefix
or automaticnextcampaign. No sends/sessionupgrades/nativeinput/profile/buildtest/
application/index/lifecycle actions.
