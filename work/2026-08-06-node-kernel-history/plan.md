# 2026-08-06-node-kernel-history

## Goal

Make node kernel history describe effective livepatch lifecycle changes instead
of treating module availability as a public kernel change. Record when a patch
is first observed loaded, enabled, and stable, and when such a patch disappears.
Make inferred timestamps compact in kernel, system, software deployment, and
sysctl history without losing the full observation interval.

## Affected repositories

- `vpsadmin`: classify lifecycle and inventory observations, migrate existing
  history, report loaded livepatches, expose lifecycle actions, and update
  WebUI rendering and tests.
- `security-advisories`: collect lifecycle actions, require exact accepted
  livepatch identities, and evaluate mitigation using observation intervals.
- `vpsfree-cz-configuration`: pin the final vpsAdmin revision and the existing
  vpsAdminOS livepatch release, and document deployment and rollback.
- `vpsadmin-kb-captures`: pin the final visible WebUI revision and validate the
  documentation contract.
- `vpsadminos`: no initiative-specific feature diff remains. Current revision
  `8d5fe005` supplies cumulative patch 3 and includes the earlier patch-2
  release.

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
- `/sys/kernel/livepatch` is authoritative for the reporter inventory. Loaded
  modules are enriched from booted/current closure metadata; configured but
  unloaded patches are omitted.
- A loaded module without matching closure metadata remains valid inventory
  with unknown enrichment fields and an evidence error. Unreadable module
  enumeration or state flags are incomplete observations and cannot create a
  lifecycle event.
- During rollout, an old reporter that replaces active patch 2 with unavailable
  patch 3 at the same reported release is inventory drift, not removal.

### Existing data

- Add a nullable action column without renumbering existing enums and append
  the internal `livepatch_inventory_change` event type.
- Reclassify only safely identifiable availability-only public rows as internal
  inventory events, including a different-ID inactive successor at an unchanged
  reported release. Preserve same-ID removal candidates and all evidence.
- Implement the correction as named stages: select inactive candidates, find
  each candidate's immediately preceding public event in observation order,
  load their livepatch evidence, and apply explicit runtime/effective-state
  predicates. Keep the old reporter's patch-2-active/patch-3-inactive rule in a
  migration comment instead of encoding it in one nested anti-join.
- Historical stable rows whose exact event timestamp matches the old
  application marker become inferred `applied` rows and lose the misleading
  exact effective timestamp. Ambiguous and later metadata rows remain generic.
- Retain the optional `verified_at` evidence field for protocol/schema
  compatibility, but do not use it to infer lifecycle or exact timing.
- Recompute public `current` markers for affected nodes. The corrective data
  migration has a no-op rollback because the original interpretation cannot be
  reconstructed safely.
- Treat kernel and software revisions as opaque identities, never as monotonic
  version order. A later boot into an older unpatched system remains the current
  public event, its older software rows remain attached to its evidence, and an
  earlier livepatch application remains historical. Advisory evaluation follows
  that current boot and therefore becomes vulnerable again.

### Security advisory evidence

- Carry `livepatch_action` in normalized history and historical event digests.
- Evidence schema 8 forces cached schema-7 evidence to be recollected.
- Accept livepatch mitigation only for the reviewed ID, patch version, kernel
  version/source, and exact clean booted or current vpsAdminOS revision.
- Treat `applied_at` as provenance, not an exact transition time. Livepatch
  mitigation uses `(observed_after, observed_before]`; fixed kernels and eBPF
  mitigations retain exact timing where available.

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
- Old and new node reporters interoperate when the API is upgraded first. The
  recorder suppresses false removal for the old different-ID/same-release
  shape; new reporters then expose only modules present in kernel sysfs. The
  API also accepts the reporter's nullable unknown-metadata/state shape before
  reporters begin sending it.
- No coordinated vpsAdminOS rollout, all-node restart, or reboot is required
  for the history semantics. Nodes can receive the actual livepatch release
  independently through the normal rolling procedure.
- Deploy the WebUI, then quiesce old supervisors while switching both API hosts
  and applying the one-way migration, then roll node reporters. This ordering
  prevents old API code from interpreting the complete inventory as a new
  application.
- After an application rollback, keep old supervisors paused until the new
  recorder is restored or an explicit semantic-regression plan is approved.
- A node rollback to an older kernel/system is independently supported: the
  next boot observation supersedes the patched state without rewriting earlier
  evidence or comparing revision strings. No special deployment ordering is
  required for this node-side rollback.
- Production deployment and production KB publication require separate direct
  operator approval and are outside this implementation request.
- Land the security-advisories tooling before rebasing the paused
  `2026-08-07-security-advisories-6-12-95-2` branch. That branch must recollect
  evidence, regenerate evaluations, and resynchronize unpublished drafts.

## Testing plan

- vpsAdmin recorder/model/API and migration specs for availability, boot state,
  transition-to-stable application, replacement, removal, mixed reporters,
  staging patch 2/3 history, current markers, serialization, filtering, and a
  later rollback boot with descending software revisions.
- libnodectld reporter specs for booted patch-2 metadata, current patch-3
  metadata, and only patch 2 present in kernel sysfs.
- security-advisories collector, schema, identity, attestation, active-state,
  interval-timing, and patched-then-unpatched rollback specs.
- WebUI localization, PHP regressions, and real-browser hover/focus coverage for
  lifecycle labels and compact intervals.
- vpsAdminOS has no initiative-specific feature diff; its release-specific test
  remains unchanged.
- Validate exact configuration pins and build the deployment documentation.
- Run the capture contract; regenerate screenshots only if it reports an owned
  administrator-history concept.
- After quick checks and commits, run the mandatory fresh-context change review
  before long integration tests. Then run relevant integration tests, monitor
  final-head GitHub Actions, and restart the bridge-network development cluster
  on the reviewed revisions.
