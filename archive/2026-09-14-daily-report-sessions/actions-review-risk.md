# Individual authentication actions: risk and compatibility review

Reviewed directly with the mandatory-change-review risk and compatibility lane
at `xhigh` effort:

- vpsAdmin
  `5ac49802f892da6fd37a88c8349b9cc7ea826538..014fbc78422f3660b295add7a50f35cc7acdf0c8`
  (`f7996f5df67d82c9627c73aae8e2b40101609570` baseline feature followed by
  `014fbc78422f3660b295add7a50f35cc7acdf0c8` individual-action follow-up)
- vpsfree-notification-templates
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333`
  (`08402ffd8010384f950b1ec4a1b95de8e5410ba3` baseline feature followed by
  `6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333` individual-action follow-up)
- current vpsfree-cz-configuration topology and baseline feature pins at
  `5036135728832d5c375705e3b69949c33460ff7e`

The lane remains high risk for the full series because it adds indexes to live
authentication-history tables and expands an administrator report with
authentication-derived data across an API/template/configuration boundary.

## Findings

No Blocking, Important, or Advisory findings.

## Security and data-safety assessment

The follow-up remains read-only. The API projects only record ID, creation
time, user ID, recorded client IP, and the requested source/mechanism/reason at
`api/lib/vpsadmin/api/daily_report_authentication.rb:84-89` and
`api/lib/vpsadmin/api/daily_report_authentication.rb:127-146`. It does not add
credentials, token material, password data, PTR records, user agents, new
logging, or an authorization-policy change. User identity lookup is one
`User.unscoped` batch used for administrator-facing display; an absent user is
retained as an ID rather than causing the report to fail or silently removing
the event.

The organization HTML template escapes the user ID, login, generated link,
source, mechanism, reason, and client IP at
`templates/daily_report/email/en.html.erb:99-105` and
`templates/daily_report/email/en.html.erb:315-400`. The focused rendering spec
injects hostile values into all new string-bearing HTML fields and checks both
escaped output and the absence of raw tags at
`api/spec/models/transaction_chains/mail/daily_report_spec.rb:403-467`.
Plain-text values are placed in the message body, not mail headers; source and
failure-reason values originate from bounded application paths, and stored
client IP fields retain their existing 46-character schema limit.

The daily-report task and recipient configuration are unchanged. The report is
still described and configured as administrator mail; the change does not add
a new delivery path or broaden access. The additional login and IP details
therefore stay within the pre-existing administrative report boundary.

Rows use the same half-open `created_at` relation as their aggregates and are
ordered by `created_at, id`, preserving repeated records and deterministic tie
ordering. The actual-database specs cover both time boundaries, repeats,
default-scope-hidden users, orphaned user IDs, missing client IP without API-IP
fallback, empty arrays, and aggregate-only payloads. Post-rebase evidence in
`actions-final-specs.log` completed with 19 examples and 0 failures.

## Contract and mixed-version assessment

The payload extension is additive: `events` is nested under the existing
`password_changes` and `failed_logins` hashes. Old templates ignore the extra
keys. Both the built-in text template at
`api/notification_templates/templates/daily_report/email/en.text.erb:35-41`
and `:64-70`, and the independent HTML template at
`templates/daily_report/email/en.html.erb:328-341` and `:383-397`, guard empty
or absent event arrays. They therefore preserve rendering with baseline
aggregate-only generators as well as fully older payloads. The existing four
top-level authentication hashes remain registered in
`api/models/mail_template.rb:244-257`.

The follow-up does not alter the baseline active-session or recovery
projections, schemas, public resources, generated clients, CLI/Terraform
behavior, protocols, nodes, or vpsAdminOS. The previously reconciled bounded
authentication projections still have no demonstrated mismatch with runtime
behavior. Their future drift risk remains Advisory context for later policy
changes rather than a new follow-up defect.

The configuration topology continues to support mixed consumers:
`flake.nix:31-34` makes the notification-template checker follow
`vpsadminServices`; `flake.nix:69-73` owns the service API source; API1 consumes
both channels and owns the scheduler/replacement templates, while API2 consumes
the API package alone. Final source revisions are not pinned at the currently
reviewed configuration head, as expected for the stated review-before-push and
`confctl` phase. The generated final pin commits require their planned fresh
general and risk review before long builds.

## Migration and deployment assessment

The baseline migration at
`api/db/migrate/20260914120000_add_daily_report_authentication_indexes.rb:1-8`
adds only four indexes and has no schema-existence guards. Old code tolerates
the indexes and new report code is functionally correct before they are
installed; rollback may safely leave them installed. Removing them is optional
and would itself incur live-table work. No node or coordinated-machine update
is required.

Production keeps `vpsadmin.databaseSetup.autoSetup = false` at
`cluster/cz.vpsfree/vpsadmin/common/api.nix:39-47`. A later authorized rollout
must explicitly run `vpsadmin-api-migrate-db.service` from the new package and
monitor metadata-lock waits and I/O for the live index builds. No migration,
activation, deployment, or integration is part of the reviewed work.

## Residual risks and test gaps

- The explicitly approved no-limit action lists make query result memory,
  template rendering, stored mail content, and outbound message size scale
  directly with all matching 24-hour rows. Failed-login volume can be driven
  by attempts against known accounts, so an unusually large period may slow or
  fail the report task or exceed mail-size limits. This is recorded as an
  accepted consequence of exhaustive reporting, not a request to reintroduce
  a row cap. No production-volume rendering benchmark was supplied.
- Aggregate and detail queries run separately and can observe concurrent
  inserts between queries. A report generated during such a mutation can have
  temporary count/detail disagreement. This is the accepted generation-time
  snapshot behavior, not a historical reconstruction contract.
- Synthetic EXPLAIN evidence validates index selection but does not measure
  production cardinality, query latency, or live index-build locking and I/O.
- The post-follow-up delivered-mail integration and final configuration builds
  have not started yet. They remain the planned long validation after source
  review, push, exact `confctl` pins, and final pin review.
