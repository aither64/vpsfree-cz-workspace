# Risk and compatibility review

Reviewed `41af23e207478af2469e1d6423312930e720ba87..19971f039771500d5d0304610f91fe6f4af5fed3`
as the risk and compatibility lane, including all three commits, the initiative
plan/state, the review packet, repository guidance, HaveAPI 0.29.8 pagination
and authorization helpers, the existing PHP WebUI pagination consumer, and the
generated Go client at its current repository head.

## Findings

No Blocking, Important, or Advisory findings.

## Assessment

- Tenant isolation remains intact. `UserPayment::Index#query` begins with
  `with_restricted`, normal users cannot supply `user` or `accounted_by`, and
  the cursor timestamp is resolved through that same restricted, filtered
  relation (`plugins/payments/api/resources/user_payment.rb:43-76`). A foreign,
  nonexistent, or filter-mismatched cursor therefore produces the same empty
  relation and cannot be used to paginate through or retrieve another user's
  payments. The committed request specs cover all three unavailable-cursor
  cases and the retained probes cover the tenant case independently.
- The date bounds use HaveAPI's typed datetime input and bound SQL parameters.
  They are optional and inclusive, compose with the existing authorization and
  admin filters, and do not alter stored data. Focused specs and retained probes
  cover inclusive boundaries, each bound independently, timezone offsets,
  invalid input, inverted periods, and filtered counts.
- Pagination now matches its public order: `(created_at DESC, id DESC)` is
  continued with the corresponding strict tuple comparison. The `id` tie-break
  makes equal timestamps stable, and that case was exercised with resolved
  associations. The current PHP WebUI takes `from_id` from the last returned
  row and carries query filters in its pagination links, so it is compatible
  with the corrected cursor contract. Existing generated clients can continue
  using the endpoint and cursor; they simply cannot express the new optional
  date inputs until regenerated.
- The migration is an additive, invertible index-only change with no schema
  existence guards or data conversion
  (`plugins/payments/api/db/migrate/20260905180000_add_user_payments_created_at_index.rb:1`).
  New API code works before, during, and after the migration; old API code also
  works with the index present or removed. Rollback therefore does not need to
  interpret state created by the feature.
- Commit `a22f37263` constrains only the API bundle to `json < 3`; its source
  Gemfile, packaged Gemfile, lockfile, and gemset agree on JSON 2.21.2. JSON
  representation and persisted payloads do not change. The recorded package
  build, positional-options decode, serialized-JSON round trip, and packaged
  API boot smoke directly exercise the reported ActiveSupport incompatibility.
- The description change is limited to this action. Bilingual OPTIONS specs
  prove the label, type, validation, and unrelated action metadata remain
  unchanged, while accurately documenting the authorization-safe empty-page
  behavior.

## Residual risks and test gaps

- No production-scale query plan or index-build timing was measured. The index
  should be deployed in the normal migration window, with metadata-lock and
  runtime latency monitoring appropriate to the production table size.
- No dependent WebUI Next end-to-end test was available. Any client that sends
  `created_from` or `created_to` requires the API rollout to finish first; a
  rollback must remove or disable that client behavior before reverting the
  API. The current PHP WebUI does not send these inputs.
- The exact review base packages JSON 3.0.2 and is recorded as unable to boot.
  It is therefore not itself a viable freshly built rollback artifact. A
  future deployment should retain the JSON constraint or designate an earlier
  known-bootable API artifact when planning rollback. This is a pre-existing
  base failure addressed by `a22f37263`, not a regression in the reviewed
  series.
- Long VM integration tests were explicitly excluded from the gate. The
  focused API, migration, localization, packaged-dependency, and boot checks
  cover the changed boundaries, but do not simulate a rolling production
  deployment.
