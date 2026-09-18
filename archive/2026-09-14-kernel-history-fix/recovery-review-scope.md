# Recovery scope and proportionality review

Blocking: none. Important: none. Advisory: none.

Reviewed the committed series and final trees with `gpt-6-astra` at `xhigh`,
following the user's model override and the mandatory change review scope lane:

- vpsadmin: `014fbc78422f3660b295add7a50f35cc7acdf0c8` to
  `268f7d09b9e3ca59d2b8f286e6666f72f9f7a9ff`, including both `cccf59c06`
  and `268f7d09b` separately.
- vpsfree-maintenance-tasks: `6eea682ede8d8e2634b2d41e5b11cf0f02231bc6`
  to `c77ff3742f623afd23c0be26c0f6ddbc026f1ba4`.

Read workspace and repository instructions, the review packet, accepted follow-up
in `plan.md`, `state.md`, the reproduced status-history audit, task documentation,
and prepared rollout. No code, state, production, or lifecycle changes made.

The implementation fits the accepted scope:

- Both migrations contain only additive schema operations. The nullable
  confirmation has no default; the checkpoint table starts empty. There is no
  migration-time repair, reconstruction of discarded reports, or artificial
  observation timestamp. The migration tests directly check these boundaries.
- The private checkpoint addresses the demonstrated loss of the last valid
  report through rejected evidence. `status.rb:202` retains one normalized
  report and its actual observation time before overwriting current evidence;
  `snapshot_reader.rb:20` adds its narrowly bounded fallback while preferring a
  newer retained event. It reuses `Report` serialization and the existing node
  lock/transaction, with no new snapshot category, public endpoint, protocol,
  generic persistence layer, or compatibility framework. Tests cover the six
  affected change categories, repeated invalid/missing/stale reports, restart,
  incomplete comparable evidence, failed recovery, reboot, stale checkpoint,
  and public-resource invisibility.
- The application fallback correction preserves the original preceding-report
  rule while retaining a newer proven kernel confirmation. The shared
  `StableState` comparator has two current consumers: permanent recording and
  this maintenance task. It is appropriately limited to their common proof
  requirements.
- The final vpsAdmin commit series contains no one-time repair entrypoint,
  implementation, tests, operator documentation, or integration invocation.
  The complete repair lives in the single dated maintenance directory. Its
  default all-node preview, explicit apply, repeated node filters, inactive
  host inclusion, candidate capture, evidence verification, and per-write
  revalidation are all requested behavior. The local runner/helper split does
  not create a general repair framework.
- Maintenance tests exercise owned repair behavior and the executable against
  disposable data. The expanded synthetic supervisor scenario covers actual
  restart and recovery across the affected histories without requiring a real
  patch unload. No disproportionate upstream-tool conformance tests or obsolete
  Rake-path tests remain.

Residual limits and validation gaps are already explicit: discarded observations
cannot be reconstructed; mutable evidence and checkpoints cannot justify a
historical repair; non-kernel historical repair remains excluded; and a preview
does not reserve proposals for a later apply. Pausing writers for an approval of
identical output is a proportionate operational solution. The new-head long
integration run, CI, final downstream pins, updated exact rollout assertions,
consumer builds, and KB impact validation remain subsequent delivery work, as
the packet states. This review inspected code and tests and relied on the
packet's recorded quick-test results; it did not rerun tests or validate the
superseded rollout pins.
