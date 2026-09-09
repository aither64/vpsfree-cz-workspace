# Scope and proportionality review

Reviewed the complete committed series
`41af23e207478af2469e1d6423312930e720ba87..19971f039771500d5d0304610f91fe6f4af5fed3`
against the requested outcome, initiative plan/state, review packet, repository
instructions, HaveAPI 0.29.8 pagination implementation, generated dependency
workflow, and the current PHP WebUI payment-history consumer.

## Findings

No Blocking, Important, or Advisory findings.

## Assessment

- The payment feature adds only the two requested optional bounds and the
  resource-specific keyset predicate needed for its existing
  `created_at DESC, id DESC` order. It delegates limit enforcement and input
  handling to HaveAPI's `ar_with_pagination` hook instead of introducing a new
  pagination framework (`plugins/payments/api/resources/user_payment.rb:50-90`).
- Resolving the cursor through the same restricted, filtered relation is a
  necessary part of the accepted authorization and filter contract. Returning
  an empty relation for nonexistent, foreign, or filter-excluded cursors is
  explicitly documented and covered by focused cases; it is not speculative
  fallback behavior.
- The action-local `from_id` metadata patch is the smallest change that fixes
  the misleading inherited description while preserving HaveAPI-owned labels,
  types, validation, and other actions. The bilingual OPTIONS assertions are
  proportionate because the exact localized contract was part of the requested
  outcome.
- The `json < 3` constraint responds to a reproduced API startup failure and is
  confined to the approved API bundle. The packaged Gemfile, lockfile, and Nix
  gemset are generated representations of the same dependency decision. The
  series adds no Rails upgrade, monkey patch, compatibility framework, or
  unrelated package update.
- The secondary index and its up/down spec are a focused operational measure for
  the new timestamp query. The request specs cover the implementation's owned
  filtering, tenant scope, ordering, cursor, and metadata behavior without
  duplicating exhaustive ActiveRecord or HaveAPI conformance tests.
- The three commits remain coherent and reviewable: the preserved feature,
  narrowly approved runtime dependency repair, and action-specific metadata
  correction each have a distinct purpose. No obsolete implementation
  iteration or abandoned defensive layer remains in the committed range.

## Residual gaps

- Production-scale index build timing and query plans were not measured for the
  global, user-filtered, and `accounted_by`-filtered workloads.
- No companion WebUI Next revision or end-to-end consumer test was available.
  The current PHP WebUI consumer was inspected and follows the documented
  last-row cursor convention.
- Equal-timestamp traversal and standalone/date-format boundary cases passed the
  retained review probes but are not all permanent project regression cases.
  Expanding the committed suite to reproduce every framework parsing and filter
  combination would be disproportionate unless a concrete failure appears.
- This lane performed source and history inspection only, as requested; it did
  not run Nix, Bundler, database, or test jobs.
