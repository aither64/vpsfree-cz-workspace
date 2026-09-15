This audit records the behavior before the fix. The private invalid-evidence
checkpoint and regression tests are now merged in vpsAdmin
`c38839d5be62e9d40d055b23a84844e2037ba4db`; the one-time kernel repair is in
vpsfree-maintenance-tasks. Deployment and historical repair remain pending.

# Status-history timestamp audit

## Result

The ordinary long-unchanged-period bug was specific to public kernel release and
livepatch history. Software/deployment, sysctl, loaded-module and eBPF inventory
changes compare consecutive accepted evidence reports, using the current
snapshot's observation time. They preserve the latest unchanged observation
across a supervisor restart.

A separate existing defect affects all five of those histories and the
livepatch-application special case after rejected security evidence: replacing the current snapshot with an invalid placeholder
loses the latest valid comparison time. Recovery falls back to an older immutable
event. The resulting lower bound is conservative but unnecessarily old. This
follow-up remains unfixed at delivered vpsAdmin revision
`337c9257f5e11f36afe81eba4951e267b83e2fc7`.

## Why public kernel history differs

A livepatch transition can span several reports, and the reported release can
change before the transition completes. Kernel history therefore compares against
the last stable public kernel event. The old implementation used that event's
first observation (`observed_before`) for the lower bound even after later
reports confirmed the same state. The delivered fix keeps a separate, persistent
`last_confirmed_at` for semantic kernel state.

The other evidence histories do not defer changes across livepatch transitions.
They compare the preceding accepted report with the new report and use its
`previous_observed_at`. They do not select the public kernel baseline's first
observation. This is why ordinary repeated unchanged reports did not expose the
same defect in those paths.

## Reproduced invalid-evidence recovery defect

Real supervisor ingestion and MariaDB persistence, followed by a fresh supervisor
instance, reproduced this sequence independently for those five categories and
livepatch application:

| Observation | Time (UTC) |
| --- | --- |
| First valid state A; immutable baseline created | 2026-04-05 12:00:00 |
| Valid unchanged state A | 2026-04-25 12:00:00 |
| Rejected security evidence, schema version 999 | 2026-04-25 12:00:30 |
| First valid changed state B, after supervisor restart | 2026-04-25 12:02:00 |

Every affected category recorded `(2026-04-05 12:00:00, 2026-04-25 12:02:00]`.
The valid unchanged report had already established the tighter lower bound of
`2026-04-25 12:00:00`. The same sequences without the rejected report recorded
that recent lower bound correctly.

The eBPF example concerns an inferred inventory change. Exact attachment events
also carry an independent `effective_at`; this audit does not claim that a
reported exact attachment time is overwritten.

The mechanism is:

1. `PayloadParser` returns a non-null invalid `Report` with `record_events=false`.
2. `Supervisor::Node::Status#store_current_evidence` writes it over the mutable
   current snapshot. The previous valid snapshot and its observation time are
   no longer available there.
3. `SnapshotReader.comparison` cannot use the invalid snapshot and chooses the
   latest retained node-reported event and its `observed_before`.
4. The deployment, sysctl, module and eBPF paths consume that stale
   `previous_observed_at`.
5. The livepatch-application special case also selects the complete preceding
   report's time. After fallback, this is the older event's time and overrides
   the newer kernel confirmation. The removal/release paths instead retain the
   persisted kernel confirmation and are covered by the delivered fix.

Relevant source at the delivered revision:

- `api/lib/vpsadmin/api/kernel_evidence/payload_parser.rb:17`
- `api/lib/vpsadmin/supervisor/node/status.rb:60` and `:201`
- `api/lib/vpsadmin/api/kernel_evidence/snapshot_reader.rb:7`
- `api/lib/vpsadmin/api/operations/node/record_kernel_evidence.rb:145`, `:182`, `:203`

These comparison/fallback paths are unchanged from upstream
`791ab3aa89e2f613979da6090b89785c78245db5`; the new kernel confirmation field
does not cause the defect. Existing malformed-evidence recovery coverage checked
that recovery did not create a false boot, but did not include a recent unchanged
report followed by a change in another component.

A follow-up should preserve the last valid comparison report and its exact
observation time through rejected reports and supervisor restarts. It must still
expose invalid current evidence honestly. Reusing the kernel's `last_confirmed_at`
for other components would be wrong: kernel state can stay unchanged while
software, sysctls or module inventories change independently.

## Other status data

| Data | Timestamp behavior | Same first/last-observation defect? |
| --- | --- | --- |
| CPU count, total memory/swap, cgroup version | `SystemState::Recorder` advances `last_observed_at` on every matching status; preserves `first_observed_at` | No; tested through restart, rejected security evidence and a later CPU change |
| Running nodectld `vpsadmin_version`, uptime, CPU/load/memory/swap/ARC metrics | Current fields refresh on reports; `NodeStatus` stores periodic samples, with averages for metrics | No old-event interval is calculated; history is sampled rather than an exact transition log |
| Pool health/capacity | Current values and `checked_at` from status messages | No old-event interval is calculated |
| Dataset properties | Current values plus periodic `DatasetPropertyHistory` samples | No old-event interval is calculated |
| VPS runtime status and metrics | Current values plus state-change/periodic status samples | No old-event interval is calculated |
| DNS zone status | Current serial and check/load/expiry/refresh timestamps | No old-event interval is calculated |

Scope: this checks the first-observation-versus-latest-confirmation error. It is
not a general audit of every producer, measurement, message-ordering rule or
status consumer. No production data was read or modified.

## Verification and delivery impact

Run from the vpsAdmin worktree:

```sh
nix develop .#api -c bundle exec rspec /home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-kernel-history-fix/status-timestamp-audit_spec.rb --format documentation
```

Result: 13 examples, 0 failures. Six verify normal recent bounds, six reproduce
the invalid-report fallback defect, and one verifies system-state confirmations.
The reproduction intentionally asserts the current defective result; it is not a
passing regression for a fix. The eBPF fixture was corrected to a valid inactive
inventory entry after parser validation rejected incomplete active metadata.

The audit changed no project worktree or feature head. The recovery gap remains
a follow-up to address before relying on these histories through invalid reports. The delivered repair task
only handles eligible public kernel release/livepatch events; it does not repair
software, sysctl, module or eBPF history. Any extension needs its own implementation,
review and validation. All original final-head CI and consumer builds passed.
