# Risk and compatibility review

Reviewed with the mandatory-change-review risk lane at `xhigh` effort:

- vpsAdmin `791ab3aa89e2f613979da6090b89785c78245db5..8769884ae69b03c22d8532fd09acf6de85542015`
- vpsfree-notification-templates `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..4dc2706df6332d235cad18c1202602004b75d63c`
- current configuration topology at `249bed1ee28e69a907edd09ea97a1144dbcdefeb`

## Findings

### Advisory: the registered daily-report variable contract omits the new payload keys

At vpsAdmin commit `8769884ae69b03c22d8532fd09acf6de85542015`,
`api/models/mail_template.rb:244-253` still describes the daily-report variables
as only `date`, `users`, `vps`, `datasets`, `snapshots`, `downloads`, `chains`,
and `transactions`. The generator now adds `user_sessions`, `password_changes`,
`password_recoveries`, and `failed_logins` at
`api/models/transaction_chains/mail/daily_report.rb:39-40`, and the independent
organization template consumes them starting at
`templates/daily_report/email/en.html.erb:268`.

This does not break current rendering: `TemplateBuilder` accepts the supplied
hash dynamically, the populated render specs passed, and all new template
sections guard absent values. It does leave the registry's documented variable
interface stale for template authors, introspection, or future validation.
Add the four `Hash` entries to the `register :daily_report` declaration when
practical.

No Blocking or Important risk/compatibility findings were found.

## Compatibility and security assessment

The report is read-only and emits aggregate counts. It does not retain or add
credential values, client addresses, account identifiers, or recovery tokens
to the mail payload. Dynamic failed-login mechanisms and reasons are escaped in
the HTML template at `templates/daily_report/email/en.html.erb:351-356`.

The active-session projection at
`api/lib/vpsadmin/api/daily_report_authentication.rb:54-79` currently matches
the authentication paths: token and OAuth2 access expiry use the same inclusive
comparison as `ResumeToken` and `ResumeOAuth2`, refresh expiry uses the same
strict comparison as OAuth2 refresh lookup, and account state, lockout,
password-reset, and per-mechanism enable flags are included. The recovery
projection at `api/lib/vpsadmin/api/daily_report_authentication.rb:88-106`
also matches the model's email/session stage selection, completion precedence,
and strict deadline behavior. The half-open report interval intentionally
assigns a deadline equal to `to` to the next report and does not call it pending
at the current snapshot.

Those predicates duplicate security-sensitive runtime and cleanup behavior, so
future changes could drift. There is no concrete mismatch in the reviewed
heads. Refactoring authentication callers or cleanup behavior into shared code
inside this reporting change would broaden its security boundary and require a
larger review and validation surface. Treat shared predicate work as a separate
change, or keep bounded parity coverage with the authoritative paths.

The four indexes in
`api/db/migrate/20260914120000_add_daily_report_authentication_indexes.rb:1-8`
are additive. Old application code can use the indexed schema, and new report
code remains functionally correct before the indexes are installed. Rollback
can safely leave the indexes present; removing them is optional and has its own
live-table locking and I/O cost. The synthetic MariaDB EXPLAIN evidence selects
all four indexes, but it is not a production-cardinality or latency benchmark.

## Deployment and pin contract

The configuration topology supports the proposed exact pins:

- `flake.nix:69-73` maps the `vpsadmin` channel to `vpsadminServices`.
- `flake.nix:31-34` makes `vpsfreeNotificationTemplates` follow that exact
  vpsAdmin input.
- `int.api1/module.nix:5-10` consumes both channels and
  `int.api1/config.nix:21-29` owns the scheduler and replacement organization
  templates.
- `int.api2/module.nix:5-9` consumes the vpsAdmin channel but not the template
  channel.

The final pin check should prove that `vpsadminServices` resolves to the pushed
reviewed vpsAdmin head, `vpsfreeNotificationTemplates` resolves to the pushed
reviewed template head, its `vpsadmin` input still follows `vpsadminServices`,
and no staging or production vpsAdmin channel moved. Building both
`cz.vpsfree/vpsadmin/int.api*` configurations is the correct mixed-consumer
validation: API1 validates generator plus managed template and API2 validates
the generator alone.

Deployment remains compatible across a rolling API update. Both API instances
may serve requests from old or new code because authentication behavior and the
database record formats are unchanged; only API1 schedules this report. A new
template rendered by an older generator suppresses the new sections, while a
new generator rendered by an older template ignores the additive payload.
Nodes and vpsAdminOS require no coordinated update.

The live configuration sets `vpsadmin.databaseSetup.autoSetup = false` in
`cluster/cz.vpsfree/vpsadmin/common/api.nix:39-47`; activating an API build does
not run this migration automatically. Before relying on indexed production
queries, an operator must explicitly run `vpsadmin-api-migrate-db.service` once
from the new package and monitor the four live index builds for metadata-lock
waits and I/O load. Omitting that step does not change report results, but can
turn the new daily aggregation into full scans. No deployment is authorized by
this initiative.

## Residual test gaps

- Production table sizes, open-session selectivity, and concurrent index-build
  behavior have not been benchmarked; only a 5,000-row synthetic EXPLAIN was
  captured.
- Long integration coverage for actual scheduled delivery has not yet run.
- The configuration revisions have not been generated yet; exact remote pins
  and their final lockfile diff therefore remain for the planned final check.
