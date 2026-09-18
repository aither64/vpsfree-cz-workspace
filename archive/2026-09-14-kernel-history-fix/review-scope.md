# Scope and proportionality review

Reviewed vpsAdmin commits
`791ab3aa89e2f613979da6090b89785c78245db5..6682da3bafc1212f30c395707319147a8c51fcc9`
(`22fa7adc3` and `6682da3ba`) against the initiative plan, explicit
non-goals, review packet, rollout, repository rules, and the preceding
diagnosis.

## Findings

No scope or proportionality findings.

The persisted recorder change is the smallest credible implementation of the
requested behavior. One nullable internal timestamp supplies the durable memory
that unchanged observations previously lost. The 54-line `StableState` helper
owns only the semantic predicates that both present consumers need: boot
identity, evidence completeness, transition state, and effective livepatch IDs
(`api/lib/vpsadmin/api/kernel_evidence/stable_state.rb:7-52`). The recorder
updates that field under its existing node lock without changing event bounds,
snapshots, `updated_at`, or public revisions, and it retains the existing
application-specific bound (`api/lib/vpsadmin/api/operations/node/record_kernel_evidence.rb:91-140,294-340`).
This adds no protocol, API, WebUI, vpsAdminOS, or generalized compatibility
surface.

The repair is bounded to the supported historical contract. It requires one
eligible node and defaults to dry-run; freezes the public candidate IDs; accepts
only inferred node-report events with valid uncertain intervals; verifies the
immediate public predecessor and target from their immutable snapshots; handles
only release changes and explicitly classified applications/removals; and
searches only event snapshots referenced by retained events inside the open
interval (`api/lib/vpsadmin/api/operations/node/repair_kernel_history_bounds.rb:9-44,49-139`).
The full proposal fingerprint and node-lock recomputation are proportionate to
the explicit requirement to revalidate the target, predecessor, selected
evidence, and evidence contents before a persisted-history write
(`api/lib/vpsadmin/api/operations/node/repair_kernel_history_bounds.rb:78-84,141-148`).
There is no fallback to mutable current snapshots, raw logs, uname-only status
samples, reconstructed history, cross-boot inference, or migration-time seeding.

The repair's focused examples and one synthetic ingestion scenario are
proportionate to a dry-run/apply tool that changes persisted public history.
They cover the accepted event classes, conservative exclusions, latest evidence
selection, idempotence, and lock-time invalidation rather than duplicating an
upstream tool's conformance suite. The repository documentation records the
same narrow contract and its expected safe no-op behavior. The apparent schema
diff growth is generated table/index ordering; the only semantic schema change
is `last_confirmed_at`.

## Cross-lane issue encountered

### Blocking: prose inside the engine pattern scalar is passed to RSpec as paths

In reviewed commit `6682da3ba`, `.github/workflows/api-specs.yml:56` adds a
comment-looking line inside the `patterns: |` scalar. The workflow's selectors
split every nonempty scalar line with shell word expansion at lines 166-172 and
267-274, so the prose becomes nonexistent RSpec path arguments. This is a CI
correctness issue rather than scope growth, but it must be removed or moved
outside the scalar before long integration/CI validation. It is the same defect
reported by the general lane.

## Residual risks and test gaps

Long integration testing had not run for the reviewed head. Retention may leave
no qualifying immutable snapshot for the production interval, in which case the
repair intentionally makes no proposal; this is an explicit accepted limitation,
not missing scope. Exact configuration and KB pins are outside this commit range
and require their planned exact-head review later.
