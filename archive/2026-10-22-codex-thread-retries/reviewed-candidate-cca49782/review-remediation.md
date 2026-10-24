# Affected independent final review

## Findings

### Important I3: New queue admissions after a settings boundary can never acquire retry proof while the current turn remains active

Lanes: general, architecture, risk/compatibility.
Commit: dev-workspace c493a41a75de6e1ff857c32b29620ee7862d362a.
Locations: portal/internal/turnretry/state.go:172-181; portal/internal/workspacecodex/turn_retry.go:235-240 and 325-348; portal/internal/workspacecodex/turn_retry_proof.go:82-83.
Coverage gap: portal/internal/workspacecodex/turn_retry_test.go:299-304.

The settings correction advances the epoch and clears State.Binding. A subsequent managed queue admission captures the new epoch, but its BindingDigest stays empty. QueueWithPolicy establishes a binding only if ActiveTurnID is empty. When an earlier manual turn is still active, it skips that branch and delegates queue admission without saving a current binding. Neither UpdateThreadSettings nor successful active queue admission creates it elsewhere.

Concrete scenario: an ordinary managed turn is active; the user changes the next mode/model/effort; the settings call completes; the user queues a new independent task after that boundary; the original turn ends and the native queue automatically executes the new task. If the new task fails with serverOverloaded or cyberPolicy, exact client-ID/content/native context are available and its epoch is current, but Prove rejects its empty BindingDigest. The controller marks that failure handled/manual. This misses the expressly accepted requirement that newly admitted managed queue entries remain eligible after the boundary. It is conservative rather than an unsafe retry, but it is a supported-path regression.

The new test calls captureRetry and then recordRetryBinding directly, bypassing the actual active QueueWithPolicy branch. It therefore proves that helpers can construct a valid new-epoch snapshot, not that production queue admission does so.

Resolve how the explicit managed settings/admission owner establishes valid current binding authority for a new queue entry while existing work is active. Preserve exclusion of every pre-boundary input, old immutable receipt tuples, native queue/FIFO, and the prohibition on retry-time rebind/resume or display-cache authority. Add a focused regression through the real UpdateThreadSettings and QueueWithPolicy calls with an active turn, then exact automatic queue execution/failure. Assert old queued input remains manual and the newly admitted task can prove settings and schedule. Cover the selected handling of failed/uncertain settings replies. If the desired contract instead requires an additional explicit binding operation, record that reduced behavior through the lead and document it; the current packet and docs claim new managed input eligibility without such an extra step.

No Blocking findings. No additional Advisory findings.

## Original finding dispositions

B1's unsafe old-task continuation is corrected. Under the admission lock, settings intent reads the exact thread/latest-turn identity, advances and saves the nonzero epoch, consumes the current active or failed turn even when Pending is nil, and invalidates the loaded binding before the settings effect. Overflow or failed identity/persistence prevents that effect. Failed replies preserve invalidation. Snapshot/binding digests include epochs; current dispatch and contributor proof reject old epochs; current binding establishment cannot fill old empty snapshots. Old uncertain Pending snapshots retain their original identities and can reconcile without becoming current proof. I3 is the remaining post-boundary production-admission gap, not evidence that the original unsafe dispatch still occurs.

I1 is corrected. Server.stepTurnRetry first invokes the separate internal reconcileTurnRetry path. It retains transition/runtime/roster/conversation/thread ordering, checks retained manifest/root/member/current package identity and lifecycle/creation receipts, and only invokes Controller.ReconcileOnly on an exactly owned uncertain record. ReconcileOnly can recover the exact accepted tuple or discard only its positively unsubmitted prepared native entry; it cannot enroll, Check/Continue, load, steer, write settings or activate queues. Fresh execution releases that pass and reacquires the unchanged ordinary resolver and its full-team uncertainty/execution holds. Accepted bookkeeping may recover while stopped or cold, while fresh execution remains held. Unrelated unknown entries are not discarded. The root/member resolver regression uses the real schema-3 client ledger and composed worker path, addressing the original test gap.

I2 is corrected. Charges are keyed by stable UUID, not timestamp. Both fresh and restarted possible dispatch reconcile and require positive unsubmitted proof; restart renews only that UUID at current clamped time, counts other live IDs, and preserves the unique attempt count/options. Native submitting uncertainty stays reconcile-only. Accepted or recovered acceptance reanchors the same charge once to receipt observation time, covering preflight/network delay before subsequent work can dispatch. Equal-time IDs remain distinct, duplicate receipts do not add charges or move the accepted anchor, quota exhaustion remains manual, and capacity scheduling retains its prior behavior. Focused tests cover the original stale-reservation case, 299/301-second delays, 29/30 other IDs, equal timestamps, backward clocks, delayed receipt and unknown no-resend.

## Scope and reviewed identity

Reviewer: same retained reviewer0, gpt-6.1-sol/xhigh/read_only, ready review-purpose identity confirmed in the live same-session roster. No override or fallback. dev-session current returned 2026-10-22-codex-thread-retries from the bound directory; both DEV_SESSION markers were absent and the trusted developer binding matched the workspace. Review remained read-only.

HIGH risk; affected general, architecture and risk/compatibility lanes performed directly after reading the skill and lane references. Original unchanged A and scope conclusions remain in force. Read the remediation packet, original review, architect's Accepted final-review corrections, old/new complete range comparison, final relevant source/tests/docs, and quick-check receipts. No nested agents, source edits, long/native tests, claims, deployment, integration or lifecycle action.

Repository: git@github.com:aither64/dev-workspace.git, target master.
Common base: bf6d4b0c49600c15e17fe71248807ef43424e932.
Original reviewed head: 85f6f7327e6948a13ad110c4c058d8b96b6ab2b9.
New reviewed head: cca49782ebd2d5135352cea4cb140548b36f7de9.
Final tree independently confirmed: 8bbdd72dde0b8c7046d1b6fea7859318b9fd6b1f.
HEAD, common merge base, clean working tree and final diff whitespace independently checked.

## Whole-branch history, pins and migrations

Inspected the complete final four-commit series from the common base:

1. 7262c24e4fbe9dbf8604e73590f9b5ef3d5dce99: durable core/store/policy and tests.
2. b3c7187c6e26e269994433716a0ee719d0a7edf7: package capability.
3. c493a41a75de6e1ff857c32b29620ee7862d362a: runtime/admission/fixture/docs.
4. cca49782ebd2d5135352cea4cb140548b36f7de9: final codex-web dependency pin.

Corrections are folded into the owning core/runtime commits. The logical split remains adequate. No obsolete branch history, fixups, transitional migrations or compatibility shims for abandoned iterations remain. Old/new core/runtime behavior deliberately differs; this report makes no equivalence claim. The unchanged capability and pin patch IDs independently match the packet: c98df1ec8b8d41855d9263096f4fddebc5d45c76 and 54bed62a7a4a2053fde96119c5b8d6f018a21082.

The B dependency stream is still one consolidated codex-web update to d2d74f931cc50e39345c6c15931748062ee51951 across Go/Nix/vendor metadata. No repeated superseded pins remain in B. A's reviewed range is unchanged. Final workspace/configuration repins are outside this B review unit; the lead must confirm their exact final series, diffs and graphs before overall readiness. This report does not approve deployment with old85f pins.

No migrations: no database migrations or retry-state upgrade sequence. The final prerelease private schema1 directly introduces required nonzero State/Binding/Snapshot epochs and UUID-keyed charges. Decoding rejects preliminary missing-epoch/anonymous-charge shapes and invalid duplicate/reference shapes instead of migrating/defaulting/resetting. Old-epoch snapshots remain valid retained data only for reconciliation. Existing native submission schema3, roster and history formats remain unchanged. Supplied provenance states no preliminary retry shape was merged, released, deployed or externally consumed; only disposable fixtures used it. Keeping turnRetryStateSchema=1 is appropriate for this direct prerelease definition. No supported predecessor requires a transitional format.

## Documentation, architecture and verification

Provider ownership and the public managed-authority/no-CAS boundary remain unchanged. The new reconciliation pass has a distinct bookkeeping purpose and does not grant an execution bypass; shared state transitions and existing A ledger primitives remain authoritative. No new public A/API contract or arbitrary-native-writer guarantee is introduced.

Documentation remains in the correct owning locations: generic A behavior/reference unchanged; runtime portal/recovery guide explains epochs, reconciliation-only admission and keyed charges; rollout/test execution stays in session records. The added recovery guide accurately describes old-proof exclusion, immutable reconciliation and conservative quota anchoring. Its new-input eligibility claim needs the I3 correction or an explicit revised boundary. Placement/discoverability otherwise remains adequate.

Provided final focused race logs pass core4.152s/workspacecodex2.423s/web7.185s; affected web checks pass5.127s. Native fixture compile/list passes and lists TestNativeTurnRetryController, without executing it. I inspected these receipts and regression source; I did not rerun tests. The native fixture now forces real accepted-response/history uncertainty and recovers through the actual portal scheduler/resolver, rather than manufacturing an accepted ledger and calling Controller.Step directly.

The complete pinned-native campaign and package checks remain post-review gates. Native-direct busy behavior remains an explicit compatibility gate and cannot prove global exclusion. No deployed behavior, user acceptance or integration is certified here.

Disposition: I1/I2 and the unsafe part of B1 are resolved; Important I3 remains. Address it or record the required explicit decision before proceeding under the mandatory-review workflow. Preserve original review.md and this affected report. Keep the same reviewer for relevant new authority/contract changes; narrow direct fixes may follow the skill's direct-verification rule.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
