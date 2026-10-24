# I-B1 direct remediation verification

Disposition: ACCEPTED under mandatory-change-review step9 on
B45e14be3d34a9ca2d3b418c310da927351b7f330,
tree edb3f41dec072a44e03a4f4a7a4c4e8894b440f4. This closes I-B1 for the
reviewed source boundary; it does not certify longer verification or use.

Lead read the complete85eb delta and normal/race receipts and independently
checked exact clean head/tree, delta byte equality, the two changed paths and
first13-commit equality in the complete14-series. All original58 packet hashes
remain unchanged. Owner scope proof records all other578 blobs/modes identical.

Production correction is ten inserted lines in the existing read-only view.
It only downgrades an exact count to null/unavailable when an accepted current
Pending lacks its LastConfirmed checkpoint, or an unconfirmed checkpoint
Pending has retired/changed. It preserves partial/unavailable evidence and
caught-up exact counts. Comparisons read existing identities; no writes,
inferred count, action/phase/timing change, state/schema/DTO/provider/controller
change or new optional-store execution precondition is introduced.

Focused tests reproduce the old defect before the fix. Normal2.306s/race5.180s
now pass all five selected top-level tests and21 tests/subtests, zero skips or
failures. Lead parsed both complete JSON logs. The ten view cases include four
gaps and continuous/already-degraded controls, with before/after byte equality.
Actual root/member HTTP uses the real managed client and strict private native
wire: accepted original receipt with failed checkpoint, repeated GET without
ledger/sidecar identity or byte changes, successful Stop with its checkpoint
unwritable, manual retirement and exact recovery with only the original native
start. Existing exact-token/own-unknown tests remain in the focused selection.

The extracted test fixture reuses the existing strict setup; existing assertions
remain. No new design or public boundary requires affected-lane review. The
retained independent report in ../review.md applies with this directly verified
narrow correction; no confirmation-only reviewer rerun is needed.

Required pressure/retention and accepted-fork actual integration remain unrun.
Pressure wrapper is rebound to exact45e and clean source, retains all19 top-level
names/14 required pressure leaves and finite Go180s/JSON/zero-skip validation.
Original85eb script and its failure/provenance remain preserved. Fresh watcher
execution may now proceed. Separate CI9f/207/e7 failures, later package/native,
real-template/composition/build/deployment/use acceptance remain open.
