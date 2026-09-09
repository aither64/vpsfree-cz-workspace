# Architecture and repetition review

Reviewed commit `44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1` against
`3a64784708faef5e9f4f093255954b14e396904c`.

## Findings

No Blocking, Important, or Advisory findings.

The implementation remains in the owning payments plugin: the API behavior is
in `plugins/payments/api/resources/user_payment.rb` and its schema change is in
the plugin migration directory. The core locale catalog and migration spec are
the repository's established integration points for plugin metadata and
migration verification.

The compound cursor at
`plugins/payments/api/resources/user_payment.rb:71` is resource-specific but
still delegates common limit validation/application to HaveAPI's
`ar_with_pagination`. Its predicate at lines 75-81 matches the ordering at
lines 84-86, including the `id` tie-breaker. Comparable compound cursors in
`api/lib/vpsadmin/api/node_system_state_data.rb:35` and
`api/lib/vpsadmin/api/resources/security_advisory.rb:203` use different sort
tuples, visibility scopes, and directions, so extracting a generalized helper
in this PR would be speculative. The existing WebUI consumer
`webui/forms/users.forms.php:1003` treats `from_id` as an opaque ID cursor and
passes the last returned payment ID, which remains compatible with the changed
ordering boundary.

The `created_from`/`created_to` query clauses resemble other resource-local
datetime filters, but they are small query-specific glue rather than a repeated
business rule that must evolve in lockstep. The locale catalog's broad
`vpsadmin.attributes` placement is produced by its unambiguous-key compaction;
the catalog can promote conflicting future metadata to resource-specific keys.

## Residual test gaps

- `api/spec/api/plugins/payments/user_payment_spec.rb:263` exercises two pages
  with IDs created out of timestamp order, but it does not split a page within
  several rows having exactly the same `created_at`. The predicate explicitly
  handles that case with `id < from_id`, so this is a coverage gap rather than
  evidence of a defect.
- There is no focused assertion for a nonexistent or filtered-out `from_id`.
  `plugins/payments/api/resources/user_payment.rb:72-73` deliberately returns an
  empty relation in that case; the omission does not indicate incorrect current
  behavior.

No Nix, Bundler, database, or other test processes were run in this lane.
