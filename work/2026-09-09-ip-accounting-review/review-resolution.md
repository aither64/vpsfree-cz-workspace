# Review reconciliation

Reviewed implementation: `9ec505df9b67bc19f7983c1bb5c34ad160eddd05`.
Final remediation commit: `0e4531b2a9839152c74a970c472bf65a3cc3c0c9`.
All reviewers use gpt-5.6-sol / xhigh as required.

General and scope lanes reported no findings. Architecture reported three
Important findings, reconciled as follows.

## Unresolved ownership chains

Accepted as a scope limitation, with README clarification. The requested output
is discrepancies for user accounts, and the plan explicitly excludes a general
inventory-integrity framework. An IP whose owner no longer exists cannot be
assigned to a report user without broadening that contract. The audit also
intentionally excludes hard-deleted users and follows vpsAdmin's VPS scope.
The review packet's broad sentence about all broken references overstated the
boundary: checks apply to records reached while auditing existing users.
The README now explicitly says that orphaned IP ownership, interface and VPS
chains are not discovered. No global orphan scan or repair is introduced.

## Duplicated recorded-use semantics

Fixed by delegating the recorded total to `UserClusterResource#used`. Evidence
continues to include associated pending/disabled rows. The state-filtering spec
also compares the reported total with the provider method. Removed redundant
`User.order(:id)` because find_each already orders by primary key.

## Per-user query cost

Accepted as a measured operational tradeoff for a one-off task. `benchmark.rb`
uses the disposable API test database and creates 1,000 synthetic users with
six IP resource rows, one assigned package, one confirmed usage row and one
owned IPv6 allocation each. The corrected implementation scanned 1,004 total
users using 14,046 non-schema SQL statements in 43.259 seconds and reported no
false discrepancies. This includes the new calls to the authoritative `used`
method. Query cost is linear and production runtime/load remain unmeasured.

The script is run on the API host against its configured database, reads indexed
relations, and holds no write locks. A finite consistent snapshot is a reasonable
cost for this dated audit. Batch preloading could reduce association queries, while calls to the provider
would remain per-resource. Keep the current traversal rather than add another
batch/grouping layer without a demonstrated runtime failure or specified
latency budget. No claim of constant query count or production-scale load
validation is made. The current README's review/rerun requirement still applies
when active transaction chains span several commits.

These are direct review remediations and clarifications inside the already
reviewed user-account/report boundary. They do not change the JSON schema,
snapshot/publication design, supported input scope, or deployment contract.
Focused verification is sufficient; no reviewer rerun is required by the skill.

Final focused verification: 16 examples, 0 failures (seed 65333); script
RuboCop and diff checks passed. All changes are committed.

## Risk review reconciliation

The risk lane corroborated the Important query/snapshot-cost finding above.
The final README removes the blanket maintenance-window statement and specifies
running during a quiet period. It documents Ctrl+C as the way to stop the audit
and release the snapshot when database load becomes excessive. This preserves
the implementation tradeoff without assuming an unmeasured production load is
acceptable at all times. An operator chooses the actual execution period; this
initiative does not execute the production scan.

The risk lane also reported an Advisory documentation error: a summary-write or
temporary-file cleanup failure after publication can return failure while the
complete report remains. Fixed the README's overly broad no-file-on-failure
promise. It now describes the actual distinction between successful collection/
publication and later errors. No runtime change or new output schema is needed.
The final documentation-only diff was inspected and passed git diff --check;
repeating runtime tests or reviewer lanes for this clarification is unnecessary.

All findings are now fixed or explicitly accepted as recorded above. No Blocking
findings or unresolved review actions remain.
