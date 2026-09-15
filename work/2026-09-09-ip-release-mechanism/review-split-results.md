# Commit split review results

Reviewed runtime heads: vpsAdmin `201c263919049792315598efd4fea5d1a5cfe950`
(base `c38839d5b`), notification overlay `715c0633` (base `6ebfb6f`),
and unchanged KB base `8789cc1`.

High risk: quota accounting, tenant isolation, destructive IP release and
asynchronous cleanup. Four fresh reviewers used gpt-6-astra/xhigh, without
nested agents. General and architecture ran first; risk and scope followed
when concurrency slots became available. No long integration preceded review.

## Findings and remediation

- **Important, general:** `Ip::Free` skipped legacy allocations with no charge
  environment while `User::HardDelete` discarded their accounting. A disposable
  database reproduction demonstrated retained ownership and scheduled quota
  destruction (seed 21765). Teardown now rejects unresolved provenance before
  preparing deletion; environmental resource freeing also rejects matching
  legacy IPs. Ownership, account and quota remain available for reconciliation.
- **Important, architecture:** manual assignment reloaded the IP but read network
  purpose and location userpick from a stale REPEATABLE READ snapshot. Policy
  validation now uses current SQL shared reads. Shared-location picker criteria
  stay in the final locking query rather than materializing stale network IDs.
  Separate-connection tests cover revoked userpick, changed purpose and changed
  primary-location userpick.
- **Important, risk:** automatic assignment/replacement could overwrite the
  charge environment of an already-owned candidate without moving its quota.
  The shared picker now restricts automatic owned candidates to destinations
  with ownership enabled and matching charge environment. Manual AddRoute keeps
  its explicit recharge path. Export picks do not change charge identity and
  retain their existing semantics. Tests cover candidate fallback and current
  rejection; migration replacement uses the same restriction.
- **Important, risk:** HardDelete linked IP cleanup from inside the final NoOp's
  confirmation block, creating sibling dependencies that allowed quota deletion
  before cleanup. Resource-free chains now precede that NoOp. The regression
  checks actual depends_on_id ancestry through host cleanup, disownership and
  quota destruction.
- **Advisory, general:** operational docs were not discoverable. The documentation
  index now links the locking/accounting and campaign rollout guides.
- **Scope:** no findings. The eight commit boundaries, existing consumers and
  bounded domain helpers match the accepted plan.

No generic Lockable/TransactionChain lock interface or node protocol changed.
The fixes are direct remediations within the reviewed contracts; focused
verification is required, with no reviewer rerun unless a new design is needed.

Rejected speculative findings: the migration export path is administrator-only,
and its admin validation bypass is intentional. OS replacement preserves the
same VPS owner and reserves both VPSes; missing extra IP helper calls alone do
not demonstrate an unsafe interaction.

## Verification

Initial four-file remediation run: 14 examples, zero failures, seed 17547.
Expanded run: 36 examples, one test-fixture failure, one existing pending
(multiple-interface migration). The teardown fixture used a numeric IP resource;
production uses object/free_chain semantics. Corrected the fixture to exercise
real Ip::Free dispatch. Focused composite verification subsequently passed as recorded below.
All eight local network/DNS/browser scenarios, the actual node-confirmation
harness (12/0), and all 26 hosted API Specs jobs passed. The review cluster and
fixtures are running; final-head check details are maintained in state.md.

Final focused results: teardown dependency test passes (seed 14562); migration
replacement passes with a real source diskspace usage and source/destination
allowances (seed 54222); 14 allocation examples pass (seed 30622), including
owned same-environment selection and exclusion from ownership-disabled targets.
Touched Ruby lint passes after two test hash-alignment corrections. All four
Important findings are resolved with focused checks; no new design requires
a review rerun. Fixes were folded into commits 4, 6 and 7.

Final publication: API 4d53fa1573bf5d0ba8de5d896153e4ca21dcfb5a and overlay
715c063396fa49277852b98d36347c8bec5160d3. Autosquash retained the exact tested
final tree. The direct remediations reside in helper commit b7e625f87,
cleanup commit e5a7202ef and campaign documentation commit 5188056bd.


The final follow-up form fix and upstream rebase are recorded in
review-form-results.md. Current vpsAdmin head is aa9ac1e3a; remediations now reside
in a23f5c5ec (helpers), c64d630d0 (cleanup) and a9d92c05e (campaign/docs).
API and node code remain byte-identical to the eight-scenario tested series.
