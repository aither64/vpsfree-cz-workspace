# Stale lower bounds in vpsAdmin kernel history

## Result

The API confuses the first observation of the previous public kernel event with
the latest observation confirming that state. The former can be weeks old even
when the node has continued reporting normally. The UI renders the stored bounds
and describes the stale lower bound as the last previous observation.

Inspected vpsAdmin revision: `791ab3aa89e2f613979da6090b89785c78245db5`, matching
the `vpsadminServices` pin in configuration revision
`3d9ffa45c7e0388c96434fd3a6127d0a54c0b9ea`. No production database query or
verification of the running supervisor build was performed. The source and
reproduction establish the bug and explain the reported symptom; they do not
establish the exact final pre-change observation for node1.

## Data flow and cause

All file references below are in vpsAdmin at the inspected revision.

1. `libnodectld/lib/nodectld/node_status.rb` includes security evidence in
   status reports. The default status interval is 30 seconds in
   `libnodectld/lib/nodectld/config.rb:105`. This is a default, not a measured
   node1 interval.
2. `api/lib/vpsadmin/supervisor/node/status.rb:68–73` reads the previous
   current evidence and its observation timestamp. Lines 120–129 pass them
   into the recorder before replacing the current snapshot.
3. `api/lib/vpsadmin/api/kernel_evidence/snapshot_reader.rb:7–13` returns the
   current snapshot timestamp when the report is comparable. Thus the fresh
   observation timestamp can be available to the recorder.
4. `api/lib/vpsadmin/api/operations/node/record_kernel_evidence.rb:93–97`
   selects the current public kernel event and assigns:

   ```ruby
   stable_observed_at = stable_event&.observed_before || previous_observed_at
   ```

   `observed_before` is the first observation containing that historical event.
   It is not updated when later status reports confirm the unchanged state.
5. Lines 101–111 use this stale timestamp for removals. Applications have a
   special case that uses `previous_observed_at` if the previous livepatch report
   is complete. Lines 117–123 also use the stale timestamp for release changes.
6. Line 128 returns without creating a kernel event for an unchanged report.
   Updating the current snapshot on every report does not update the historical
   event used as the stable baseline.
7. Lines 399–400 persist the selected timestamps as `observed_after` and
   `observed_before`. `webui/forms/node.forms.php:612–633` renders these fields;
   it does not derive the bad bound itself.

This was introduced by commit `988ce4a0d1c0bbbe495963c5e8e3ed2190eaba1d`
(`api: record observed livepatch lifecycle`, August 7, 2026). Keeping a stable
state across transient reports was intentional. Its historical event timestamp
was incorrectly reused as the most recent observation of that state.

## Reproduction

Run from the workspace root:

```sh
ruby work/2026-09-14-node1-stg-livepatch-unload/reproduce-kernel-bound.rb
```

The diagnostic loads the unmodified recorder from the pinned Git revision and
runs its boundary-selection method with in-memory report/event/persistence
adapters. It does not use a database or simulate node1's actual raw reports.

Synthetic inputs deliberately use the user-provided old/new dates:

- Previous public event: August 22 at 17:33:29 CEST.
- Later report confirming the same state: September 13 at 19:58:20 CEST.
- First report containing the change: September 13 at 20:00:36 CEST.

| Scenario | Actual lower bound | Result |
| --- | --- | --- |
| Direct removal | August 22 17:33:29 | Stale despite fresh previous report |
| Removal after reverse transition | August 22 17:33:29 | Last stable confirmation not retained |
| Release change without lifecycle event | August 22 17:33:29 | Same stale bound |
| Application control | September 13 19:58:20 | Existing special case uses fresh timestamp |

All diagnostic assertions passed. This confirms selection behavior, not database
serialization or the proposed fix. No repository tests or production mutations
were needed for this diagnosis.

The existing removal test at `api/spec/models/operations/node/record_kernel_evidence_spec.rb:482`
and release test at line 527 create a baseline event and immediately move to a
transition. In those fixtures, the event timestamp and last stable observation
are identical. There is no intervening unchanged observation exposing the bug.

## Recommended fix

Keep a separate persisted timestamp for the most recent valid observation
confirming the stable kernel state. A small implementation can add a nullable
`last_confirmed_at` to the current public kernel event. Treat this as observation
metadata; preserve the event's original bounds and immutable evidence snapshot.

- On each accepted report, advance this timestamp only when a complete,
  non-transitioning observation confirms the same boot, reported release, and
  effective livepatch state as the baseline. Compare semantic runtime state,
  excluding volatile verification timestamps. Preserve the existing protection
  against old reporters hiding a still-active patch.
- Retain the timestamp through unknown/invalid samples, reverse transitions,
  and unrelated module, sysctl, or deployment changes. Persist it so a supervisor
  restart during the transition does not lose the last stable confirmation.
- For removal and reported-release events, use that last confirmed old-state
  time as `observed_after`. Where the immediate previous report positively
  confirms that same baseline, its timestamp can also establish/advance the bound.
- Keep the application-specific use of a complete preceding non-effective
  observation, where it supports a tighter valid completion bound. Do not replace
  all event bounds blindly with the latest report time.
- Update the timestamp and record events under the existing node lock and
  transaction. New public events establish their own observation state. Never
  advance across a reboot, an ambiguous observation, or a report rejected as stale.
- On an incomplete initial boot observation, preserve conservative behavior
  until a comparable stable state is established; do not fabricate confirmation
  from an unreadable baseline.

Why a one-line replacement is insufficient: during a transition, `uname` may
already contain the new release. Using a later transitioning report as the lower
bound for that release change could claim the change happened after it had
already been observed. The current snapshot also overwrites the older stable
observation, so the last stable time must survive separately.

Regression coverage should include repeated unchanged observations over days,
direct removal, removal through several transition reports, release changes
whose new value appears during transition, unreadable reports, recovery after a
supervisor restart, stale/out-of-order reports, reboots, and legacy inventory
ambiguity. The distinguishing assertion is that the lower bound advances with
valid confirmations while original event timestamps remain unchanged.

## Compatibility and existing history

This can be an API/supervisor fix with an additive nullable database column.
No node protocol, vpsAdminOS change, reboot, or coordinated node upgrade is
needed. Apply the migration first, then update/restart all supervisor consumers
so old writers no longer produce stale bounds. API clients can retain the current
event fields. Old code can ignore the new column on rollback, although its old
timing behavior will return. Use conservative fallback bounds for existing rows
until a newer matching observation confirms the current state; do not initialize
the field to the migration time.

A separate bounded repair can tighten historical intervals only from retained
evidence that positively confirms the old state within the same boot and before
the change. Immutable snapshots on internal events may help even when they are
hidden from public history. Historical node-status rows can establish release
bounds, but a release string alone does not always prove a particular module's
lifecycle state. Central logs can support a separately attributed operator repair.
Do not silently assign exact log times to inferred API observations.

The August 22–September 13 interval still contains the actual event, but it is
unnecessarily broad and the description falsely presents its lower bound as the
latest prior observation. A UI follow-up could display `observed by <upper bound>`
or both endpoints, keeping the full uncertainty interval accessible. Fixing the
recorder is the primary change; changing only the label leaves incorrect history
bounds in API consumers.

No fix has been implemented or deployed. The requested outcome of this phase
is the root-cause diagnosis and proposed implementation above.
