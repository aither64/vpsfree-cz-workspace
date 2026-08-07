# 2026-08-06-node-kernel-history

## Goal

Make node kernel history describe effective livepatch lifecycle changes instead
of treating module availability as a public kernel change. Record when a patch
is first observed loaded, enabled, and stable, and when such a patch disappears.
Make inferred timestamps compact in kernel, system, software deployment, and
sysctl history without losing the full observation interval.

## Affected repositories

- `vpsadmin`: classify lifecycle and inventory observations, migrate existing
  history, expose lifecycle actions, and update WebUI rendering and tests.
- `vpsfree-cz-configuration`: pin the final vpsAdmin revision and the existing
  vpsAdminOS livepatch release, and document deployment and rollback.
- `vpsadmin-kb-captures`: pin the final visible WebUI revision and validate the
  documentation contract.
- `vpsadminos`: no feature diff remains. Revision `008aa460` supplies the real
  livepatch payload and retains its release-specific certification test.

## Design decisions

### Effective lifecycle

- Keep the public wire event type `livepatch` and database event type
  `livepatch_change` for compatibility.
- Public lifecycle actions are nullable `applied` and `removed`. A null action
  remains the fallback for ambiguous historical rows and old consumers.
- A patch becomes effective at the first node report where it is loaded,
  enabled, and not transitioning. Since the exact transition instant is not
  observed, application has inferred confidence, no `effective_at`, and the
  interval between the last old report and first stable report.
- A patch already stable in the first report after boot is boot state and does
  not create a second public event.
- Replacing one effective patch with another is an application event for the
  newly effective set. Losing an effective patch without replacement is a
  removal event.
- Availability, metadata, and transition-only changes remain internal evidence
  and do not replace the public/current kernel event.

### Existing data

- Add a nullable action column without renumbering existing enums and append
  the internal `livepatch_inventory_change` event type.
- Reclassify only safely identifiable availability-only public rows as internal
  inventory events. Preserve all evidence records.
- Historical stable rows whose exact event timestamp matches the old
  application marker become inferred `applied` rows and lose the misleading
  exact effective timestamp. Ambiguous and later metadata rows remain generic.
- Retain the optional `verified_at` evidence field for protocol/schema
  compatibility, but do not use it to infer lifecycle or exact timing.
- Recompute public `current` markers for affected nodes. The corrective data
  migration has a no-op rollback because the original interpretation cannot be
  reconstructed safely.

### WebUI

- Label public actions as “Live patch applied” and “Live patch removed”, with
  “Live patch change” as the generic fallback.
- For `(observed_after, observed_before]`, visibly show only
  `after <observed_after>`. Expose the complete interval and boundary semantics
  through the existing keyboard-accessible hover/focus detail.
- If only an upper bound exists, display `by <observed_before>`.
- Reuse compact interval rendering in kernel, software deployment, and sysctl
  history. Compact system-history observation spans separately while retaining
  their full accessible detail.

### vpsAdminOS test scope

- Do not add a service or marker protocol solely to manufacture an exact
  application timestamp. Ordinary livepatch sysfs evidence is sufficient.
- Keep `tests/suite/kernel/livepatch-6.12.95.nix` unchanged. It is not a generic
  livepatch unit test; it certifies the concrete 6.12.95 cumulative patch
  release and its predecessor/replacement behavior. A future kernel release
  should add or update release certification intentionally rather than pretend
  that one pinned fixture validates every kernel.

## Compatibility and deployment

- Persisted changes are additive. Old enum values and `event_type=livepatch`
  retain their meanings, and the action is nullable.
- Old and new node reporters interoperate because classification uses existing
  loaded/enabled/transition fields. Reporters may still send `verified_at`; new
  API code accepts but ignores it for lifecycle timing.
- No coordinated vpsAdminOS rollout, all-node restart, or reboot is required
  for the history semantics. Nodes can receive the actual livepatch release
  independently through the normal rolling procedure.
- Deploy the WebUI before the API. Quiesce old supervisors while switching both
  API hosts and applying the one-way classification migration so they cannot
  recreate availability-only public events.
- After an application rollback, keep old supervisors paused until the new
  recorder is restored or an explicit semantic-regression plan is approved.
- Production deployment and production KB publication require separate direct
  operator approval and are outside this implementation request.

## Testing plan

- vpsAdmin recorder/model/API and migration specs for availability, boot state,
  transition-to-stable application, replacement, removal, legacy markers,
  current markers, serialization, and public filtering.
- WebUI localization, PHP regressions, and real-browser hover/focus coverage for
  lifecycle labels and compact intervals.
- vpsAdminOS must be byte-clean against `008aa460`; its release-specific test
  remains unchanged rather than being generalized falsely.
- Validate exact configuration pins and build the deployment documentation.
- Run the capture contract; regenerate screenshots only if it reports an owned
  administrator-history concept.
- After quick checks and commits, run the mandatory fresh-context change review
  before long integration tests. Then run relevant integration tests, monitor
  final-head GitHub Actions, and restart the bridge-network development cluster
  on the reviewed revisions.
