# Scope and proportionality review

Reviewed `3a64784708faef5e9f4f093255954b14e396904c..44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1`
against the review packet, initiative plan/state, and repository `AGENTS.md`.

## Findings

No Blocking, Important, or Advisory findings.

## Proportionality evidence

- The new API surface is limited to the two requested optional datetime inputs
  and their inclusive predicates
  (`plugins/payments/api/resources/user_payment.rb:27-32,53-59`). It does not
  introduce a compatibility layer, registry, fallback, or reusable framework.
- The custom cursor is required by the stated ordering contract. HaveAPI
  0.29.8's stock descending helper compares only the primary key
  (`api/.gems/ruby/3.4.0/gems/haveapi-0.29.8/lib/haveapi/model_adapters/active_record.rb:56-59`),
  whereas this endpoint orders by `created_at DESC, id DESC`. The PR uses the
  framework's existing `ar_with_pagination` callback and adds the matching
  lexicographic predicate
  (`plugins/payments/api/resources/user_payment.rb:71-86`); this is necessary
  endpoint behavior, not duplicated framework infrastructure.
- The schema change is one directly related, reversible index
  (`plugins/payments/api/db/migrate/20260905180000_add_user_payments_created_at_index.rb:1-5`).
  Its focused spec checks both directions
  (`api/spec/migrations/20260905180000_add_user_payments_created_at_index_spec.rb:19-26`).
- The added API examples cover distinct parts of the owned contract: metadata
  discovery (`api/spec/api/plugins/payments/user_payment_spec.rb:104-112`),
  tenant scope (`:163-187`), inclusive range and filter composition
  (`:209-261`), and out-of-order-ID cursor traversal (`:263-299`). The test
  surface is proportionate to the authorization and pagination consequences.

## Residual test gaps (not findings)

- The OPTIONS example at
  `api/spec/api/plugins/payments/user_payment_spec.rb:104-112` asserts parameter
  presence but not the localized label/description values added at
  `api/lib/vpsadmin/api/locales/en.yml:424-429` and
  `api/lib/vpsadmin/api/locales/cs.yml:423-428`. The literals are directly
  inspectable, so this does not justify broader test machinery.
- The pagination example at
  `api/spec/api/plugins/payments/user_payment_spec.rb:263-299` demonstrates
  out-of-order IDs with distinct timestamps, but does not put equal
  `created_at` values across a page boundary. The tie-break branch is explicit
  at `plugins/payments/api/resources/user_payment.rb:75-81`; a focused external
  probe can cover it without expanding the committed suite.

No Nix, Bundler, or database jobs were run in this lane.
