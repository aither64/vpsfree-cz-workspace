# Emergency provenance retention: independent final review

Recorded by lead from reviewer0's final report. Reviewer: retained
gpt-6.1-sol/xhigh/read_only; same-session ready/review identity independently
verified; no override/fallback/nested agents. HIGH persisted-state/replay risk.
General, architecture, scope/proportionality and risk/compatibility lanes completed.
The reviewer ran no tests, builds, native, source/session edits, claims,
deployment, integration or lifecycle operations.

Reviewed B basebf6d4b0c49600c15e17fe71248807ef43424e932 to frozen
570d900a4b7bbfe5c716cfd234f9dc89bbedc746,
treef877578a730f0d61a5d6aa2dcc18332cb9712c07. Actual deployed predecessor
d819ad044ef7fcc7bb4a111dc7676fe251383249,
tree6f1f05da60b09743d3716eb1a0adf794b90cf5a3. A remains unchanged
c1f415ad5602c23e6443cced73cb59267a796f05,
tree7e3523236dc4500b68a008398305b2290beabcc8.
Reviewer checked clean heads/trees, merge base, complete series, exact8file delta,
fresh SSH feature/default refs, verified deployed bundle and owner final receipts.

## Important H1: preflight capacity refusal discards protected Pending

General/risk; controller.go:235-236 and retention_test.go:183-188 at570.
Controller.preflightAccepted runs only after positive never-submitted proof.
On ErrSnapshotCapacity, it records correct blocked/settings_unproven, Cancelled,
zero DeadlineMS and Handled=failure but also sets Pending=nil. The saved contract
protects that exact immutable Pending identity even when execution never began.
For63protected unbound snapshots plus source proof, or protected encoded-byte
pressure, refusal detaches UUID/action/failure/settings and reservation correlation.
This violates identity preservation; no duplicate dispatch was demonstrated.

Required narrow remedy: remove only the Pending=nil assignment. Retain the exact
Pending, empty ResultTurn and existing ChargedAtMS. Keep blocked/settings_unproven,
Cancelled=true, Handled=Pending.Failure and DeadlineMS=0. Replace the nil expectation
with exact preservation, save/reload and repeated Controller.Step on the same
failure; assert zero native dispatch and unchanged quota.

Reviewer assessed this remedy: existing schema1 permits this Pending in blocked
state; Uncertain=false, Handled skips exact failure and dispatch requires scheduled
state. It is a narrow preservation correction within the reviewed design. Lead may
inspect and focused-test directly under mandatory-change-review step9; broader
behavior requires ordinary affected-lane handling. H1 was not fixed in reviewed570.

No Blocking, other Important or Advisory findings. Final affected source review
is complete with H1 required before verification;570 has no clean-pass certificate.

## Reviewed correctness and recovery

Retention plans a separate candidate slice and validates count+encoded bytes,
including newline/reserve, before installing it. Only positively bound accepted
non-proven/non-executed snapshots can retire; new/unbound/pending identities and
source turn stay protected. No omission/cap increase; original64/1MiB/256KiB limits.
Failed capacity planning leaves original state intact.

Current-turn retirement durably consumes exact Handled and invalidates all cached
eligibility before send. Prove checks Handled before cache; preference/settings
changes do not revive that turn. A later independently admitted turn can prove
normally. Epoch/binding/provider/incarnation/preference/quota authority preserved.
Every production addition inspected: AdmitSnapshot, RetainProof with pending-copy
budget, Accepted result budget and PreflightAccepted only after never-submitted
proof. Aggregate proof cannot discard its own contributors to manufacture proof.

Known accepted settlement preserves exact Pending/ResultTurn and keyed charge,
reanchoring once. Missing result-proof room yields blocked/settings_unproven,
Cancelled/zero deadline/Handled=result. It never Cancel-clears Pending, appends65,
replays accepted dispatch or rearms after restart/free space. Persistence failure
keeps durable uncertain tuple+generic receipt for same-ID reconciliation.

Managed Send reconciles original UUID/text/action/options before cancellation,
capture or rebinding. Generic SendAttempted distinguishes prepared from absent;
missing managed proof cannot retrobind a prepared attempt. Retired accepted input
returns original receipt, including acknowledged history recovery. Existing unbound
evidence binds only exact accepted receipt; conflicting turns refused. Queue replay
precedes capture, protected unbound identities/FIFO remain. Shared admission fences
still span persistence/native/receipt. Unknown remains reconciliation-only; no
recovery/provider/roster/lifecycle/queue/ledger/settings bypass. Public503 remains
conservative; postacceptance-save failure remains uncertain.

## Test evidence inspected, not rerun

Actual root/member wrappers/controller/backend and generic ledger/history cover
64-to69steers; accepted replay/ack/restart/no extra send; changed tuples require
identity error;64protected queues/FIFO/refusal; prepared-without-proof; pre-save,
post-admission, submitting/lost reply and post-generic-acceptance crashes; cached
proof suppression across settings/optout/restart; independent new queue eligibility;
63/64slot+encoded-byte proof/result limits; unknown hold/accepted settlement;
keyed quota anchoring/conflict/save failure/no repeat dispatch.

Focused core0.241s/wrappers43.774s; core races7.637s; controller/authority/resolver
races88.445s/7.346s; protectedFIFO/crash individual passes; corrected replay37.185s;
byte/proof/receipt1.503s. Original fixture failures retained. Replay context was
started before durable setup; final starts at replay and asserts identity errors.
Invalid Go negative-lookahead selector replaced with supported selectors. H1 test
encoded the wrong nil expectation and must be corrected despite these passes.

No current hotfix native/package/build/deployment success. After H1: exact B
package/Ruby, pinned0.163 B recovery/controller and downstream checks/builds required.
Unchanged A exact native evidence retained; not evidence for changed B. No concrete
changed host/lifecycle/archive/creation VM contract requires a new full VM campaign.

## Whole history, streams, migrations and docs

Full5commit series:7262c24e core; b3c7187c capability; aafaf419 runtime/tests/docs;
d819ad04 sole A pin (actually deployed);570d900a retention/replay successor.
Original four exact. Substantive successor properly separate from supported deployed
state; no obsolete iteration/equivalence claim, unrelated UI/API/framework, unused
compatibility path, transitional fixup or redundant update. Fold H1 into hotfix;
preserve570review evidence.

B's one A stream remains consolidated atc1f across Go/Nix/vendor;570adds no update.
No repeated B stream. W/C moving preparation deliberately unread; exact final
published graphs/history/single-stream conclusions still required before readiness.
No stale W/C approval.

No migrations: schema1/capability1 retry and native submission3 unchanged; no
database migration/conversion/eager rewrite/invented format. Unlike initial reviews,
d819was deployed and is a supported recovery boundary. Valid64state loads directly;
unknown tuples retained. Older readers decode state but retain original defect;
forward package recovery stays supported. Disposable old iterations are distinct.

B owns provenance and consumes unchanged A receipt/ack/history APIs. Root/member
share retention owner. Scope proportionate to observed64failure and bounded proof/
receipt consequences; UI deferred. Recovery guide accurately explains retained
contracts, manual-only turn consequences, protected identities, reconciliation
before provenance and conservative accepted settlement, subject to H1 correction.
README/portal links discover it. Lasting project docs and session rollout evidence
placement accepted.

Next: owner fixes H1; lead directly verifies exact delta and focused result, then
releases separately gated verification/composition. This report grants no deployment,
integration, resource release or lifecycle action.

## Lead H1 resolution

Final B5a5583ae7559bb038e6c8c684a6484d425d11e64,
tree453e12d9a216c9fb98a3b385e33721d12dfd4f6d, parent exact deployedd819.
Lead inspected complete570→5a delta: only controller.go assignment drops the
Pending=nil operand, and retention_test.go preserves originalPending/Cyber then
checks exact equality after save/reload and two fresh controller steps. Empty
ResultTurn/ChargedAtMS, blocked/Uncertain=false/Handled and zero sends checked.
Only two files14insertions/2deletions; no design or contract expansion. Exact
focused log implementer1-hotfix-h1-quick-race.log passes quick0.185s/race1.981s.
Clean head/tree and exact parent verified. H1 resolved under skill step9; no
redundant reviewer rerun. Final5a is released for separate exact verification;
native/build/deployment success is still not established by source acceptance.

## Lead CI fixture resolution and final source

Superseded570CI fast/archive/creation logs independently diagnosed by owner:
TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery fails
both active states because the test fake lacks supported thread/items/list,
now called by exact reconciliation. No product failure shown. Final B
ed2a75b98a75f9b37b7a359e9091a94e9846644e,
tree63eba6140c340d28f38c39b010d0a5b2874b7680, parentd819.
Lead inspected complete5a→ed delta: exactly2added lines returning empty items
page/nextCursor=nil; all settings/steer/native-count/owner assertions unchanged.
Exact previously failed selector both active cases passes normal0.184s/race1.485s
in implementer1-hotfix-coordination-fixture-quick-race.log. Narrow step9 fixture
remedy accepted, no new behavior/lane rerun.570/5a receipts/bundles/ranges preserved.
Final source has9affected files; no production change after H1. Package/native
verification pending. CurrentedCI left running, superseded5a cancellation denied403.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
