# Risk and compatibility review

Reviewed vpsAdmin commits `791ab3aa89e2f613979da6090b89785c78245db5`
through `6682da3bafc1212f30c395707319147a8c51fcc9` using the mandatory
risk/compatibility lane at high risk and `xhigh` effort.

## Findings

### Important: repair can trust previously altered snapshot components as positive evidence

Commit: `6682da3bafc1212f30c395707319147a8c51fcc9`

Files:

- `api/lib/vpsadmin/api/operations/node/repair_kernel_history_bounds.rb:62-83`
- `api/lib/vpsadmin/api/operations/node/repair_kernel_history_bounds.rb:99-105`
- `api/lib/vpsadmin/api/operations/node/repair_kernel_history_bounds.rb:121-138`
- `api/models/node_kernel_evidence.rb:39-45`
- `api/models/node_kernel_module.rb:1-7` (representative normalized child)
- `api/spec/models/operations/node/repair_kernel_history_bounds_spec.rb:144-159`

The repair treats an `event` snapshot and its normalized child rows as immutable
historical proof. The model only rejects updates to the `NodeKernelEvidence`
parent; normalized children such as livepatches, modules, and evidence errors
remain writable. The concurrency spec demonstrates this directly by creating a
module on an already persisted event snapshot.

The proposal fingerprint detects a child-row change made between the unlocked
scan and the under-lock recheck. It does not detect content that had already
drifted before the first scan: both reads then agree, and `APPLY=1` can tighten
`observed_after` from evidence that no longer represents the recorded report.
That turns pre-existing invalid state into an unsupported public-history write.

Make the repair fail closed when an event snapshot's normalized content cannot
be proven to be the originally recorded content, or enforce immutability for the
full event-snapshot aggregate and account for existing rows before relying on
that invariant. Add a regression in which a snapshot child is altered before
the repair starts; it must be skipped and reported rather than applied. This
must be fixed or explicitly accepted and recorded before long integration
testing.

No Blocking findings were found.

## Compatibility and residual risk

- The migration is additive: one nullable `datetime`, with no default, guard, or
  data rewrite. The isolated migration test covers up, existing-row preservation,
  and down. The generated schema records the new version and column.
- Recorder confirmations and repair writes use the same `Node#with_lock` boundary.
  Confirmation uses `update_columns` so `updated_at`, evidence, and public
  revisions remain stable; repair uses `update!` so an intentional history edit
  invalidates revisions. Proposal reinspection covers target, predecessor,
  selected evidence, and normalized evidence contents.
- Mixed old/new application code is compatible with the additive column, but an
  old supervisor can still create the original broad bounds. The prepared rollout
  correctly depends on masking both known supervisor writers before activating
  new code, migrating between API host activations, and restarting writers only
  after both hosts are updated. An application rollback must leave the column and
  repaired bounds in place; running the reversible schema downgrade would discard
  accumulated confirmation metadata.
- The long supervisor/RabbitMQ integration scenario is still pending by design.
  It remains necessary to validate process restart behavior and the repair path in
  the packaged runtime.
- Exact configuration and KB pins are outside this checkpoint and require the
  planned follow-up review against their final committed revisions.
