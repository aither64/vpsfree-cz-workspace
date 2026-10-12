# Scope and proportionality review

Reviewed the complete committed functional ranges and their two-commit series:

- `vpsadmin`
  `5ac49802f892da6fd37a88c8349b9cc7ea826538..014fbc78422f3660b295add7a50f35cc7acdf0c8`
  (baseline `f7996f5df67d82c9627c73aae8e2b40101609570`,
  follow-up `014fbc78422f3660b295add7a50f35cc7acdf0c8`)
- `vpsfree-notification-templates`
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333`
  (baseline `08402ffd8010384f950b1ec4a1b95de8e5410ba3`,
  follow-up `6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333`)

I compared both series and final trees with `plan.md`, `state.md`, the review
packet, the explicit non-goals, prior review reconciliation, and each
repository's `AGENTS.md`. The configuration head
`5036135728832d5c375705e3b69949c33460ff7e` still pins the baseline source
heads by design; final pin commits belong to the planned post-review phase.

## Findings

No Blocking, Important, or Advisory scope/proportionality findings.

## Proportionality assessment

The baseline remains a bounded report feature. One report-specific object at
`api/lib/vpsadmin/api/daily_report_authentication.rb:1-148` owns the new
projection and is called only by the existing daily-report generator. Its four
indexes, additive payload keys, text consumer, HTML consumer, selector entry,
and delivery-test extension correspond directly to the approved metrics. It
does not add an event store, public endpoint, scheduler, authentication-policy
change, historical-replay framework, or cross-project rendering abstraction.
The prior decision to retain report-local session and recovery projections is
still proportionate: refactoring authentication and cleanup callers would
broaden this reporting change into security-sensitive domain work.

The follow-up adds the smallest credible event-list mechanism. The existing
period relations are reused at
`api/lib/vpsadmin/api/daily_report_authentication.rb:84-88` and
`:127-137`; the shared helper at `:140-145` selects only the fields needed by
the requested rows, delegates filtering, ordering, and projection to
ActiveRecord/SQL, performs one unscoped batch lookup for current logins, and
retains the recorded user ID when no user exists. It has two immediate
consumers and does not introduce a registry, compatibility layer, fallback
identity source, PTR lookup, user-agent lookup, inferred client address, new
logging, or schema change. Keeping the record ID in the internal event hash is
reasonable support for deterministic tie-order verification and adds no new
rendered or public contract.

The built-in text additions at
`api/notification_templates/templates/daily_report/email/en.text.erb:28-70`
and the organization HTML additions at
`templates/daily_report/email/en.html.erb:99-105,315-397` render the same two
requested lists beneath their summaries. The small `action_user` helper avoids
duplicating the linked/missing-user branch across both HTML tables. The
`events&.any?` guards are the exact mixed-version requirement: they accept both
absent and empty arrays without inventing broader payload normalization.

The focused spec growth is proportional to owned behavior. The examples at
`api/spec/models/transaction_chains/mail/daily_report_spec.rb:340-469` cover
the stated window and tie ordering, repeated actions, recorded-IP-only rule,
hidden and missing users, HTML escaping/linking, empty lists, and
aggregate-only generators. The existing delivered-mail scenario adds one
action of each kind at
`tests/suite/alerts/lifetime-and-daily-report.nix:68-113`; it does not duplicate
the full unit-level matrix. Test discovery still selects the existing
`alerts/lifetime-and-daily-report` scenario, and the post-rebase focused run
completed with 19 examples and 0 failures.

The commit split is coherent. vpsAdmin keeps the projection, built-in text
consumer, focused specs, and delivered-mail assertion together; the independent
HTML template remains a separate consumer commit. No obsolete implementation
iteration or speculative mechanism remains in the reviewed series.

## Residual risks and pending checks

- Both event arrays intentionally materialize every matching action. Report
  size and memory therefore scale with a day's recorded activity. This follows
  the user's explicit no-limit decision and is not a scope finding; adding a
  cap, pagination, or delivery framework would change the accepted contract.
- The existing report-local authentication and recovery projections can drift
  if those domain rules change later. Current parity coverage and comments are
  appropriate; a shared domain refactor remains outside this initiative.
- The follow-up delivered-mail integration run, final pushed source revisions,
  generated configuration pins, pin review, and API builds remain in their
  planned later phase. Their absence from this functional review is not a
  proportionality defect.
