# Scope and proportionality review

Reviewed the complete committed functional ranges:

- `vpsadmin`
  `791ab3aa89e2f613979da6090b89785c78245db5..8769884ae69b03c22d8532fd09acf6de85542015`
- `vpsfree-notification-templates`
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..4dc2706df6332d235cad18c1202602004b75d63c`

The review compared both commit series and final trees with `plan.md`, the
review packet, the explicit non-goals, repository guidance, and the existing
authentication and password-recovery implementations. The later configuration
pin commits are outside this functional review phase.

## Findings

No Blocking, Important, or Advisory scope/proportionality findings.

## Proportionality assessment

Commit `8769884ae` adds one report-specific aggregation object at
`api/lib/vpsadmin/api/daily_report_authentication.rb:1-133` and invokes it only
from the existing daily-report generator at
`api/models/transaction_chains/mail/daily_report.rb:39-40`. It exposes only the
approved aggregate keys. It does not add an event store, telemetry framework,
public endpoint, scheduler behavior, historical-replay promise, credential
data, or changes to authentication code. This is a bounded implementation of
the accepted report contract rather than a generalized capability.

The usable-session query at
`api/lib/vpsadmin/api/daily_report_authentication.rb:54-79` necessarily restates
the stored-state portions of token and OAuth2 eligibility. Calling the
authoritative resume operations would not be a proportional substitute: those
operations require presented token values, use `Time.now`, mutate request
counters and last-request timestamps, can renew tokens, and set thread-local
authentication state. Extracting and adopting a shared, time-parameterized
domain relation across the login and cleanup paths would change
security-sensitive production behavior and substantially broaden this feature,
contrary to the accepted requirement to preserve authentication behavior. The
read-only SQL projection plus focused parity examples at
`api/spec/models/transaction_chains/mail/daily_report_spec.rb:188-246` is the
smallest credible boundary for this report.

The recovery classification at
`api/lib/vpsadmin/api/daily_report_authentication.rb:88-106` is similarly
bounded to historical classification at the report cutoff. Existing model
predicates answer current per-record usability, while cleanup mutates expired
records using wall-clock time. Neither can supply the requested half-open
historical totals, completion precedence, or pre-cleanup expiry counts. A
report-local aggregate query is proportionate; introducing a generalized
recovery-state query API and changing cleanup to consume it is outside the
requested outcome. The focused examples at
`api/spec/models/transaction_chains/mail/daily_report_spec.rb:279-329` cover
the report-owned temporal behavior without attempting exhaustive framework or
database conformance testing.

The four single-column indexes in
`api/db/migrate/20260914120000_add_daily_report_authentication_indexes.rb:1-8`
were explicitly accepted and correspond directly to the period and open-session
queries. The recorded MariaDB EXPLAIN exercise selected all four indexes. The
single rollback spec verifies the feature's schema and data-preservation
contract; it does not build a generalized migration harness.

The built-in text and organization HTML changes are appropriate independent
consumers of the same additive payload. Their local layout and label mappings
do not justify a shared cross-repository rendering abstraction. Old-generator
guards implement the stated mixed-version requirement. The selector update and
existing delivery-test extension are narrowly tied to the new generator and
mail content.

The commit split is coherent: vpsAdmin keeps aggregation, its schema support,
built-in consumer, and directly coupled tests together; the independent
template repository has one consumer-only commit. The unchanged configuration
head correctly defers exact remote pins until the functional commits are
reviewed and pushed.

## Residual risks and pending checks

- The report's eligibility and recovery projections can drift if the runtime
  authentication or recovery state machines change later. Current reviewed
  predicates match those paths, and expanding this feature to refactor those
  authorities would be disproportionate. Preserve the parity tests and assess
  the report whenever those domain rules change.
- Long delivered-report integration coverage has not run yet.
- Exact configuration pins and both API configuration builds remain for their
  planned post-push check; they were not present in these reviewed heads.
