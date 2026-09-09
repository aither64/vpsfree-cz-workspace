# Architecture and repetition review

Reviewed the complete committed series
`41af23e207478af2469e1d6423312930e720ba87..19971f039771500d5d0304610f91fe6f4af5fed3`
for the architecture and repetition lane, including the three commits
`ed8121659`, `a22f37263`, and `19971f039`. The project worktree was clean at
the reviewed head.

## Findings

No Blocking, Important, or Advisory findings.

## Assessment

- Payment filtering, authorization-aware cursor resolution, ordering, and the
  supporting migration remain owned by the payments plugin. The implementation
  does not introduce a registry, cross-plugin conditional, or parallel source
  of authorization or filter rules.
- `UserPayment::Index#exec` reuses HaveAPI 0.29.8's `ar_with_pagination` boundary
  for limit validation and applies only the resource-specific two-column
  keyset predicate that `with_desc_pagination` cannot represent. Resolving the
  cursor through the same `query` relation keeps tenant restrictions and all
  selected filters authoritative in one place.
- The similar keyset implementations in node-system-state and security-advisory
  resources have different ordering keys and cursor visibility rules. A shared
  abstraction would add a generalized query DSL without eliminating a current
  repeated business rule.
- The action-local `from_id` metadata patch preserves HaveAPI's parameter type,
  label, and validation. The generated locale catalog uses the repository's
  existing compaction rules, and request coverage verifies that another
  inherited `from_id` parameter retains its HaveAPI-owned description.
- The JSON constraint is declared at the API bundle boundary. The packaged
  Gemfile, lockfile, and Nix gemset are generated representations of that same
  dependency decision rather than independent configuration authorities; no
  unrelated package resolution changed.
- The existing WebUI payment-history consumer supplies the last returned
  payment ID and preserves its active filters in pagination links, which fits
  the new continuation contract. No current consumer requires the former
  arbitrary numeric-threshold behavior.

## Residual gaps

- No production-scale query plan or timing evidence was available for the
  `created_at` index under global, user-filtered, and `accounted_by`-filtered
  workloads. This is a deployment-performance gap, not evidence of an
  architectural defect in the reviewed series.
- No companion WebUI Next revision or end-to-end consumer test was supplied.
  The repository's current PHP WebUI consumer was inspected directly, and the
  focused API tests plus retained review probes cover filter preservation,
  tied timestamps, scoped cursors, includes, and empty-page behavior.
