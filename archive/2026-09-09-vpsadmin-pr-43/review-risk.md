# Risk and compatibility review

Reviewed commit `44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1` against
`3a64784708faef5e9f4f093255954b14e396904c` in the risk and compatibility
lane.

## Findings

No Blocking or Important findings.

### Advisory: `from_id` metadata still promises the old ID-threshold behavior

- Location: `plugins/payments/api/resources/user_payment.rb:71-81`, commit
  `44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1`.
- Contract source: HaveAPI 0.29.8
  `servers/ruby/lib/haveapi/actions/paginable.rb:7-10` supplies the inherited
  parameter, while `servers/ruby/lib/haveapi/locales/en.yml:138-141` describes
  it as: "List objects with IDs greater or lower than this value." vpsAdmin
  pins HaveAPI 0.29.8 at `packages/api/gemset.nix:343-366`.

The PR intentionally corrects payment pagination to follow the declared
`created_at DESC, id DESC` result order. `from_id` is consequently no longer a
numeric ID boundary: the implementation first resolves that ID inside the
current tenant- and filter-scoped query, returns an empty relation when it is
absent, and otherwise continues after its `(created_at, id)` tuple. For
example, an arbitrary or deleted `from_id` that previously produced
`id < from_id` results now produces an empty page; a cursor excluded by the
current `user`, `accounted_by`, or creation-period filters does the same.

This is not a defect in the intended ordering correction. The in-tree WebUI
passes the last returned payment ID and preserves the current filters
(`webui/forms/users.forms.php:1007-1028` and
`webui/lib/pagination.lib.php:219-235`), and no current caller relying on an
arbitrary ID threshold was found. The API description is nevertheless false
for this action and can mislead third-party clients or operators into silent
history truncation. Override the inherited `from_id` description for this
action to define it as an exclusive payment-row cursor that must belong to the
same filtered result set, and assert that description in the OPTIONS spec
(`api/spec/api/plugins/payments/user_payment_spec.rb:104-112`).

## Compatibility and safety assessment

- Normal-user scoping remains on the base relation at
  `plugins/payments/api/resources/user_payment.rb:39-50`. Both the period
  predicates and cursor lookup reuse that relation, so neither the new filters
  nor a foreign payment ID bypass tenant isolation. All timestamp and cursor
  values are bound parameters.
- The new inputs are optional. Existing clients continue to work, and the new
  API code remains functional before, during, and after the index migration.
  Old API code also works with the index present, so the schema/API change is
  compatible in either deployment and rollback order. A consumer that sends
  the new inputs must still wait until all API instances serving it have been
  updated, as already assumed by the initiative plan.
- `plugins/payments/api/db/migrate/20260905180000_add_user_payments_created_at_index.rb:1-5`
  adds only a secondary index to the exact predecessor table, contains no
  stale-schema guards, and is reversibly removed without changing payment
  rows. Its remaining operational risk is the normal index-build lock/load,
  covered by the stated migration window.
- The checked `vpsadmin-go-client` head does not yet expose `created_from` or
  `created_to` in `ActionUserPaymentIndexInput`; this does not break the old
  client, but consumers of that generated client need a later regeneration to
  use the new filters. No such consumer was part of this PR.

## Residual test gaps

- The pagination spec proves out-of-order IDs with distinct timestamps, but
  does not cross a page boundary where two payments share the same
  `created_at`. The SQL includes the correct `id < from_id` tie-break, so this
  is a coverage gap rather than a finding.
- The empty-page behavior for a missing, deleted, foreign, or currently
  filtered-out cursor is not tested. No in-tree caller triggers it, but the
  behavior should be covered if it is retained as part of the documented
  cursor contract.
- Period tests use UTC `Z` timestamps only. HaveAPI 0.29.8 parses ISO 8601
  offsets before ActiveRecord binds the values, but an offset-bearing boundary
  test would make that externally visible expectation explicit.
