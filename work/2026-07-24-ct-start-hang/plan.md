# 2026-07-24-ct-start-hang

## Goal

Replace osctld's overlapping container lifecycle paths with one per-container
coordinator. Starts, stops, restarts, in-container reboots, console ownership,
state observations, cleanup, and exceptional recovery must be generation
fenced and must not deadlock.

Preserve intentional unbounded waits. Recovery must still permit an operator to
isolate unkillable processes, recover state, clean what is possible, and
sometimes start a new generation in disjoint cgroups.

## Affected repositories

- `vpsadminos`
  - lifecycle coordinator, run generation resources, hooks, console, recovery,
    CLI/man pages, and VM coverage;
- `vpsadmin`
  - parse and record structured recovery-cleanup outcomes used by VPS replace
    while preserving its best-effort snapshot/copy behavior.

## Design

- Assign a persistent container incarnation ID and a random ID to every run.
- Make the incarnation ID immutable for an existing container. Configuration
  reload/replace may omit it or repeat the exact value, but cannot rotate it
  and archive live lifecycle/recovery evidence. Persist an omitted value during
  reload, preserve the existing reducer object, and refuse daemon-start
  identity mismatches while runtime, recovery, worker, or quarantined-policy
  evidence exists.
- Store one atomic runtime lifecycle record per container under `/run`.
- Serialize only short reducer commits. Run LXC, ZFS, mount, cgroup, hook,
  process, and console effects outside the reducer and fence their results by
  incarnation, run, effect, and record revision.
- Express start, stop, restart, and reboot as desired-state intents. Duplicate
  starts join one launch and an external start overlapping an in-container
  reboot cannot create a second replacement run.
- Preserve `wait: false` as a durable acknowledgement and preserve finite wait
  values as client deadlines only. Do not add lifecycle/watchdog timeouts.
- Separate console transport from lifecycle state. Treat monitor, hook, process,
  console, and LXC state messages as observations for an exact run.
- Persist exact user-control callback and hook-child ownership. Attach hook
  children and descendants to a per-generation host-effects cgroup before
  releasing them to exec, and do not release the run while these workers live.
- Treat name-only `lxc-monitor` messages only as reconciliation triggers.
  Qualify non-terminal state against the current generation init cgroup,
  publish each per-run transition idempotently, and perform stop hooks and
  mount cleanup only from the exact run-ID post-stop finalizer.
- Lease state recovery/reconciliation in the reducer so it cannot overlap an
  exceptional cleanup that releases the active generation.
- Require an osctld-issued managed-launch authorization. Manual `lxc-start` is
  unsupported and rejected by the internal pre-start hook.
- Keep the launch effect through the wrapper authorization and callback-return
  window. Release it only when the exact LXC pre-start callback has completed
  mount, policy, device, and hook setup. A stop requested before that boundary
  records desired state but cannot overtake a child that has not yet executed
  `lxc-start` or `lxc-execute`.
- Give every run exact wrapper, payload, monitor, pivot, delegated, and
  accounting cgroup paths. Track AppArmor, mount/dataset, network, console, and
  process identities per generation.
- Keep the stable `ct.<id>` cgroup as the container's policy and accounting
  parent. Put normal LXC payloads and stopped-container `lxc-execute` sessions
  in distinct generation children; never move the stable parent into one
  generation.
- Model stopped-container `ct exec` and `ct runscript` as transient execution
  generations. Authorize their `lxc-execute` pre-start hook separately, use
  their exact generated LXC configuration, keep the logical container state
  stopped, and serialize them with normal start and recovery cleanup.
- Treat commands attached to an already running container as exact-generation
  process leases. Fence the generation before releasing the child to enter its
  cgroup, then keep final cleanup waiting until the child has reaped.
- Normal starts wait indefinitely for predecessor cleanup. An explicit
  `ct recover cleanup` may instead quarantine a stopped run whose exact
  surviving processes were killed but remain uninterruptible.
- A quarantined run keeps its resources and hazards in the lifecycle record.
  Starting the same dataset is an explicitly audited bounded-risk operation:
  already-entered kernel or ZFS work can still complete later.
- Keep `recover kill`, `recover state --no-lock`, and `recover cleanup`
  usable without an additional quarantine flag. Add optional `--run-id`,
  unambiguous target selection, idempotency, and structured outcomes.
- Treat the stable container cgroup as the authoritative cpuset policy root.
  Fence live policy changes in the lifecycle reducer, scan the complete actual
  subtree, expand root-to-leaf, restrict leaf-to-root, and use an intermediate
  union for disjoint masks. Never broaden a quarantined residual generation.
- Treat CPU bandwidth as another lifecycle-fenced hierarchy policy. On cgroup
  v1, preflight the complete quota/period write plan before changing the
  kernel. Every intermediate effective bandwidth must remain between the old
  and target grants and every child must remain valid below its parent.
  Reject a mathematically impossible live pair with no writes; stopped
  configuration remains the offline path. Execute accepted plans from parents
  to children for expansion and children to parents for restriction, with an
  exact reverse write journal for rollback. Never broaden a quarantined
  residual generation. Apply and reset cgroup-v2 `cpu.max` through the same
  stable-root and exact-generation transaction boundary.
- Reconstruct configured group cpuset hierarchies as one parent/child
  transaction. A full group apply may recreate missing controller paths only
  as an explicit recovery of that exact quarantined path; an ordinary apply
  must not invent unrelated controller paths.
- Validate and record effective masks rather than requested masks. A scheduler
  package is always intersected with the effective parent, including reset and
  unset paths.
- Apply launch cpusets in two exact-generation phases: prepare the stable and
  generation parents before LXC, then reconcile LXC-created payload/inner
  children from the authorized pre-start hook. Normal starts and transient
  stopped executions use the same path.
- Make mixed cpuset/CPU-bandwidth/non-policy runtime writes strict and
  transactional. A rollback failure durably taints the lifecycle policy,
  exposes the hazard to operators, and blocks new starts, executions, and
  ordinary manipulation.
  Stop/finalization and explicit recovery remain available. A container policy
  taint is sticky and clears only when explicit recovery removes and verifies
  the stable policy cgroup root in every hierarchy. A group transaction writes
  a persistent `cgroup-policy.yml` quarantine before touching the hierarchy;
  a full successful group apply, or a transactional set/unset/replace that
  reconstructs the recorded runtime parameters, clears that group marker.
- Keep direct-libLXC reboot ownership durable until exact post-stop evidence.
  A failed runner reply is ambiguous because the reboot signal may already have
  been delivered, so it records `delivery_unknown` without opening admission.
  An explicit stop may deliberately supersede this reservation and records the
  hazard.
- Allow best-effort inconsistent copy/send-as-new-ID from a recovered source.
  Block hard deletion, reinstall, rename/re-ID, ownership/map changes,
  destructive dataset replacement, and consistent transfer cutovers while any
  active or residual generation exists. Recheck exact drain after stop so a
  quarantined unkillable generation is not treated as clean shutdown.
- Keep VPS replace's current network-only recovery cleanup and recursive
  snapshot/copy/send strategy. Record cleanup warnings in transaction output
  and continue on qualified partial or quarantined outcomes.

## Compatibility and deployment

- Runtime lifecycle data, including container policy taint, is daemon-restart
  durable under `/run` but intentionally cleared by host reboot. The persistent
  container config gains only an optional incarnation ID.
- Group policy quarantine is different: it is a root-owned sidecar at
  `<pool-config>/group/<group>/cgroup-policy.yml` and survives daemon and host
  restarts. It contains transaction status, error/rollback evidence, and the
  structured parameter set needed for a full recovery apply. New osctld loads
  it and blocks starts/executions below that group, group deletion and moves
  into the subtree until recovery succeeds.
- New osctld adopts running legacy containers and inventories legacy cgroup
  paths. New vpsAdmin treats old cleanup replies as `legacy_unknown`; old
  vpsAdmin continues because qualified partial/quarantined cleanup exits
  successfully. An old osctld ignores the new group sidecar and cannot enforce
  generation or policy quarantine, so downgrading a live/tainted node is
  unsafe even though the normal group `config.yml` remains readable.
- Nodes can be updated independently. Deploying vpsAdmin first is preferred so
  warnings are retained, but no all-node coordination is required.
- Live rollback is unsupported. Before rollback, drain lifecycle work, stop
  all containers, run exact-generation cleanup, prove that no effect, recovery,
  residual generation, container policy taint, or group
  `cgroup-policy.yml` marker remains, and remove all generation cgroups. If
  that cannot be proven, roll forward and recover with the generation-aware
  daemon. Older osctld cannot enforce generation fencing, recognizes neither
  quarantine kind, and cannot safely manage live generation-qualified
  resources.
- Raw LXC settings that override osctld-owned hook or cgroup plumbing are
  reported and rejected when osctld next generates or reloads the container
  configuration. This includes `cpu.cfs_period_us`, `cpu.cfs_quota_us`, and
  `cpu.max`: finite bandwidth belongs only on osctld-owned stable/generation
  roots, never an LXC-owned payload. Raw `lxc.include` is also rejected because
  included files can hide those protected keys. Before upgrading, operators
  must remove raw CPU-bandwidth keys and inline only safe custom settings from
  raw includes. Generated osctld template includes remain supported.
- During a rolling upgrade, new osctld adopts an already-running legacy
  container by exact run ID and transfers configured CPU bandwidth from the
  legacy LXC payload to the osctld-owned stable root before monitoring resumes.
  The payload is made unlimited before an ancestor is changed. Any failed or
  unprovable transfer durably quarantines container policy and blocks new
  starts while stop and explicit recovery remain available.

## Operator recovery

- Inspect exact runs and hazards with `osctl ct show` lifecycle columns and
  select a residual explicitly when more than one exists.
- For an unkillable generation, use
  `osctl ct recover kill --run-id <run-id> <ctid>`, then
  `osctl ct recover state --no-lock --run-id <run-id> <ctid>`, and finally
  `osctl ct recover cleanup --run-id <run-id> <ctid>`. Cleanup may quarantine
  processes with SIGKILL pending when the kernel cannot reap them; a replacement
  generation then uses a disjoint random cgroup path. Cleanup is considered
  complete only from its structured `cleaned` outcome and evidence.
- A container policy taint clears only when `ct recover cleanup` includes
  cgroups, no other runtime generation uses the stable root, and removal of
  that root is verified in every cgroup hierarchy. A blocked/partial outcome
  leaves the taint and must not be bypassed.
- Recover a group quarantine with a full
  `osctl group cgparams apply <group>`. Transactional cpuset set, unset, or
  replace is also allowed when it can reconstruct the structured cleanup
  record. Success must clear the group policy status before descendants are
  started. Do not delete `cgroup-policy.yml` by hand: the file is the evidence
  that a possibly partial kernel write still needs reconciliation.
- If a direct reboot reports a lost/failed runner reply, treat delivery as
  unknown. Wait for exact post-stop handling or use an explicit `osctl ct stop`
  to supersede the reservation; do not force a new start by editing lifecycle
  state.

## Verification and delivery

- Add reducer, persistence, fencing, recovery, console, hook, cgroup-v1/v2, and
  mixed-version specs.
- Add VM coverage for the original reboot/start race, daemon restart at
  lifecycle boundaries, a deliberately non-exiting old generation, exact
  residual cleanup, manual LXC start rejection, and a drained daemon
  downgrade/re-upgrade. The downgrade case must first prove that no active,
  residual, tainted, or generation-owned state remains; it then verifies that
  old osctld loads the optional new container config, starts through legacy
  paths, and new osctld can adopt and clean that legacy run. It does not test
  or imply support for live downgrade.
- Add vpsAdmin unit and integration coverage for old and structured cleanup
  responses and run the existing local/remote VPS replace scenarios with data
  integrity checks.
- Run quick checks and repository hooks, commit focused changes, then run the
  mandatory standalone change review before long integration tests.
- Run relevant local VM integration tests. After they pass, push feature
  branches over SSH and watch every GitHub workflow for both head commits,
  including multi-hour integration tests, to terminal completion.

## Delivery result

- Published vpsadminOS head:
  `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`.
- Published vpsAdmin head:
  `807e9d7f1277217d3cf2d49b7c4b2525dc441c10`.
- Required standalone reviews cleared the final lifecycle, cgroup, recovery,
  test-isolation, and CI follow-up changes.
- All selected local unit, hook, cgroup-v1/v2 VM, lifecycle, and recovery
  gates passed.
- All workflows on both exact published heads reached terminal success.
