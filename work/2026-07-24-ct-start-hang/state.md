# 2026-07-24-ct-start-hang

Status: implementation published and all exact-head workflows green.

## Repositories

- `vpsadminos`
  - branch: `2026-07-24-ct-start-hang`
  - worktree:
    `worktrees/2026-07-24-ct-start-hang/vpsadminos`
  - base: `origin/staging`
  - current base commit:
    `23cf4fc36f15ce510c63b5134f4ea8038b706e31`
  - initial base commit:
    `4476942c4e33092e20e4faa91f32dfcca9a3ea7d`
  - exact published implementation head:
    `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`
  - reviewable commit series:
    - `e7b17285486fa4aac1bec774484eef3326c3a221`
      `osctld: add durable container lifecycle reducer`
    - `bf8b62eb72e77d64105cebf4e4d5b080c21a69f7`
      `osctld: route operations through lifecycle generations`
    - `64bcf9107825eb9eb02016f15cd0c814de77f261`
      `osctld: transact cpuset hierarchies`
    - `ef5583c1ce6007e58a316a28d8e968d78f5bf5ab`
      `osctld: order CPU bandwidth hierarchy updates`
    - `7e5440c987926d7c7e223d4fa2d141105ccf0b9a`
      `osctld: transact group cgroup policies`
    - `257e486c27f154f85a44b67ac817b2dff0e06baa`
      `osctld: keep CPU limits on stable policy roots`
    - `25965362d6d6d5d2abc32e59be7185c88c425f43`
      `osctld: wait for LXC payload before mirroring limits`
    - `ee0fa2d970f7491050333e394ca64658fc840217`
      `tests: isolate osctld-disrupting CPU view coverage`
    - `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`
      `osctld: reset cgroup v2 swap limits transactionally`
  - published feature head:
    `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`
  - local pre-staging-rebase backup:
    `2026-07-24-ct-start-hang-pre-staging-23cf4fc36` at
    `4734807f77a198bc31a4dda9590eb8277e4dc009`
  - local pre-final-rewrite backup:
    `2026-07-24-ct-start-hang-pre-final-fixes` at
    `6482b6f245e8e74986e57b32eda1ed74c537cc0c`
  - local pre-VM-load-fix backup:
    `2026-07-24-ct-start-hang-pre-vm-load-fix` at
    `3242856faddeefb0c09c29cf8a8b721855322b3e`
  - local rejected retirement-fix backup:
    `2026-07-24-ct-start-hang-pre-stable-cpu-root-redesign` at
    `2b4a91864ee5bf1ff4ac02ca2ce04addf7c5bcfa`
  - local pre-cgroup-v2-test-fold backup:
    `2026-07-24-ct-start-hang-pre-cgv2-test-fold` at
    `15a4599f009dfd92ed78622db14f4c8c2335cc3c`
- `vpsadmin`
  - branch: `2026-07-24-ct-start-hang`
  - worktree:
    `worktrees/2026-07-24-ct-start-hang/vpsadmin`
  - base: `origin/master`
  - feature base commit:
    `eb2ccde5cd709a42a802589419ba8cf525c97f34`
  - `origin/master` observed at final publication:
    `52933ca65c1bacdc005f2f38ee8f62f845f95771`
  - exact published final head:
    `807e9d7f1277217d3cf2d49b7c4b2525dc441c10`
  - structured cleanup commit:
    `e8c79b34315b2bea63998412ca1300670754ba8c`
  - initial vpsadminOS pin commit:
    `c457da3cf2c56b6f43d07ac2092b546454a16ce4`
  - Playwright packaging commit:
    `fc2c413871e8d9c7a33dabafd7fbd91e747e3444`
  - API example compatibility commit:
    `e0407c301c53112f6ebb92cc8005605561eef7bb`
  - exact final vpsadminOS pin commit:
    `6f4e7de8fb90e03192867f1e56c8f454f6b7327f`
  - incident-report test isolation commit:
    `807e9d7f1277217d3cf2d49b7c4b2525dc441c10`
  - local pre-final-pin-fold backup:
    `2026-07-24-ct-start-hang-pre-final-vpsadmin-pin` at
    `1c8bde6163ffbb2af3dafc2cdb6d574ebf0d7885`
- The rejected timeout-free prototype is backed up locally and remotely as
  `2026-07-24-ct-start-hang-prototype` at
  `078afb23788a260393190c1b582b66dca76d2016`.

## Root cause

- At `00:23:44`, container `tank:26108` exited. `lxc-monitor` reported
  `STOPPING` and `STOPPED` by `00:23:45`, before the old `ct_post_stop` hook
  and console cleanup had completed.
- An external `ct start` arrived at `00:29:37`. It trusted the name-only
  `STOPPED` observation, acquired the manipulation lock, and began another
  start while the previous run still owned runtime and cgroup resources.
- That start collided with busy cgroups and then waited for a state transition
  while retaining the manipulation lock.
- The old post-stop path reported `Reboot requested` at `00:29:46` and tried
  to start the replacement, but it blocked acquiring the same lock.
- The thread dump shows this circular ownership. The external start waited for
  a transition that only the queued reboot/start path could produce, while the
  queued path waited for the lock held by the external start.
- `ct recover state --no-lock 26108` supplied the missing observation and
  released the external start; the queued reboot could then proceed.
- The fundamental flaw was treating a container name and current monitor state
  as lifecycle identity. LXC reports `STOPPED` before all osctld-owned effects
  for that exact run are finished, and late console, callback, process, or
  monitor events can otherwise act on a replacement run.

## Implemented design

- A per-container reducer stores desired state, exact run generations, owned
  effects, process identities, observations, recovery leases, residual
  generations, and policy hazards in an atomic runtime record under `/run`.
- Start, stop, restart, direct reboot, and in-container reboot are intents
  reduced against that record. Duplicate or overlapping starts join the same
  replacement generation. Long LXC, kernel, mount, hook, console, and cleanup
  effects run outside the short reducer critical section and report exact,
  revision-fenced results.
- Every normal start and stopped-container execution receives a random run ID
  and disjoint wrapper, delegated, payload, monitor, pivot, inner, host-effect,
  and accounting cgroups below the stable `ct.<id>` policy root.
- Manual `lxc-start` and `lxc-execute` using osctld configuration are
  unsupported. The pre-start callback requires a one-use authorization bound
  to the exact osctld wrapper process and ancestry.
- A launch remains owned until the exact authorized pre-start callback has
  completed mount, AppArmor, cgroup, device, start-menu, and hook setup. Stop
  intent may be recorded before this boundary but cannot overtake a child that
  has not yet crossed it.
- LXC monitor messages are reconciliation triggers, not run identity. Exact
  post-stop finalization, wrapper death, console EOF, hooks, TTYs, external
  attaches, stopped-container executions, and internal runner children all
  carry generation leases. Runner children use parent-death signaling plus a
  parent-PID race check.
- State recovery and observation reconciliation are reducer-leased so they
  cannot release a run concurrently with policy work or exceptional cleanup.
- Direct-libLXC reboot keeps its reservation until exact post-stop evidence.
  A failed runner reply is recorded as `delivery_unknown`, because the reboot
  signal may already have been delivered. Explicit stop can deliberately
  supersede that reservation and records the ambiguity.
- The stable container cgroup is the policy root. Cpuset changes traverse the
  actual subtree in safe order, use an intermediate union for disjoint masks,
  verify effective values, and roll back transactionally.
- Configured group cpusets are reconstructed as one hierarchy transaction.
  Parent masks are made valid before children on cgroup v1, while cgroup v2
  controller boundaries and effective masks are verified before descendant
  starts or stopped execution.
- CPU bandwidth changes use the same lifecycle policy lease as cpuset changes.
  Cgroup-v1 quota/period changes are preflighted against the complete live
  hierarchy before the first kernel write. Each accepted intermediate keeps
  every effective grant between its old and target bandwidth; impossible live
  two-file pairs are rejected with zero writes and can be applied while the
  container is stopped. Accepted plans expand parent-first, restrict
  child-first, and roll back an exact write journal in reverse. Cgroup-v2
  `cpu.max` uses the same stable-root and active-generation transaction.
  Residual generations are never broadened.
- A failed container policy rollback creates a sticky runtime taint. It clears
  only when explicit cleanup removes and verifies the stable cgroup root in all
  hierarchies. A failed group transaction writes persistent structured
  `cgroup-policy.yml` evidence and fences descendant starts, executions, group
  moves, and deletion until a successful reconstruction/apply clears it.
- `recover kill`, `recover state --no-lock`, and `recover cleanup` accept an
  exact optional run ID and return structured, idempotent outcomes. Cleanup can
  quarantine an unkillable stopped generation, retain all known hazards, and
  allow a bounded-risk replacement in a disjoint cgroup path.
- Stopped-only configuration, reinstall, image-config, mapping, ownership, and
  group mutations require both stopped LXC state and no active or residual
  reducer generation. Hard deletion repeats the exact-drain check after stop,
  so a newly quarantined unkillable generation cannot lose its dataset.
  Consistent export/send/local-transfer cutovers use the same boundary.
  Best-effort inconsistent copy/send-as-new-ID remains available. vpsAdmin VPS
  replacement records structured cleanup warnings while retaining its existing
  recursive snapshot/copy/send behavior.
- No lifecycle timeout or watchdog was added. Infinite lifecycle waits remain
  intentional. Existing finite values are client wait budgets, not authority
  to abandon an effect whose kernel-side outcome is unknown.

## Operator recovery

- Inspect lifecycle and residual run IDs with `osctl ct show`.
- For an unkillable run, use:
  `osctl ct recover kill --run-id <run-id> <ctid>`,
  `osctl ct recover state --no-lock --run-id <run-id> <ctid>`, then
  `osctl ct recover cleanup --run-id <run-id> <ctid>`.
- Only a structured `cleaned` outcome proves cleanup. A `quarantined` outcome
  deliberately retains the old generation and permits a new random cgroup
  path; it does not claim the unkillable processes or kernel work are gone.
- Container policy taint clears only after cgroup-inclusive cleanup verifies
  removal of the unused stable root in every hierarchy.
- Recover group policy with a full `osctl group cgparams apply <group>`, or a
  transactional set, unset, or replace that reconstructs the recorded
  parameter set. Never delete `cgroup-policy.yml` by hand.
- A direct reboot with a lost runner reply remains delivery-unknown until
  post-stop evidence. Use an explicit stop to supersede it; do not edit the
  runtime lifecycle record to force admission.

## Compatibility and deployment

- Runtime lifecycle state and container policy taint survive daemon restart
  under `/run` and intentionally clear on host reboot. Persistent container
  configuration adds only an optional incarnation ID.
- An existing container's incarnation ID is immutable. Low-level config reload
  and replacement reject a differing supplied ID, preserve the current ID when
  omitted, durably backfill an omitted on-disk ID, preserve the one reducer
  object, and are blocked while active or residual generations remain.
- Daemon startup validates lifecycle identity before configuring or registering
  a container. An incarnation mismatch is archived only for a provably drained
  record; active, residual, recovery, worker, or quarantined-policy evidence
  makes startup refuse the edited configuration and retain the authoritative
  record.
- Group policy quarantine persists across host restart at
  `<pool-config>/group/<group>/cgroup-policy.yml`.
- New osctld adopts legacy running containers and inventories legacy cgroups.
  New vpsAdmin accepts old cleanup replies as `legacy_unknown`; old vpsAdmin
  continues because partial and quarantined outcomes remain successful replies.
- An old osctld ignores generation state and group quarantine. Downgrading a
  live or tainted node is unsafe. Before rollback, drain lifecycle work, stop
  containers, clean all exact generations, prove there are no owned effects,
  recovery leases, residuals, container taints, or group policy markers, and
  remove generation cgroups. Otherwise roll forward.
- Nodes can roll independently. vpsAdmin-first deployment is preferred so it
  retains cleanup warnings, but simultaneous fleet deployment is not required.
- Raw LXC settings that replace osctld-owned hook/cgroup plumbing, including
  raw `lxc.include`, are rejected at managed start.

## Review

- The user-requested independent architecture reviewer examined lifecycle,
  console, callback, attachment, direct-reboot, recovery, group-policy, cgroup,
  launch-boundary, and process-ownership behavior throughout implementation.
- Findings fixed during review include:
  - prelaunch full-hierarchy application on cgroup v1;
  - group-change admission races;
  - missing stopped-execution and attachment generation leases;
  - TTY exceptional cleanup and hook ownership;
  - policy reconciliation races;
  - wrapper child ownership and parent-death races;
  - premature start/execute effect release before exact pre-start completion;
  - lost direct-reboot reply opening admission;
  - standalone spec load dependencies and randomized logger state.
- The reviewer accepted the exact pre-start completion boundary and durable
  delivery-unknown reboot reservation.
- Its final current-diff disposition found no Blocking, Important, or Advisory
  findings. Its independent final isolation set passed 66 examples with seed
  `17653`; all 123 changed/untracked Ruby files parsed and the plan/state
  matched the implementation.
- The workspace-mandated fresh standalone review of committed heads found a
  blocking group-policy admission race: `ct chgrp` or a newly registered
  container could enter below an ancestor after its membership snapshot but
  before the policy marker was visible.
- The amended design publishes the persistent marker before enumeration,
  restores the prior marker on failures before any kernel write, and makes
  `ct chgrp` lock every unique ancestor on both old and new paths. A
  deterministic thread race and marker-order/restore regression cover both
  sides. The reviewer rechecked the amendment and found no Blocking finding
  remaining.
- The mandatory review accepted the cohesive vpsadminOS commit and vpsAdmin
  commit split. It retained two pre-delivery gates: final exact dependency pin
  and a strictly drained old/new daemon compatibility VM case. The latter is
  now part of `osctld/lifecycle`.
- The same reviewer cleared the test-only amendment at exact source head
  `6630b043d3174a272db3138663c5e3c88f8a1335` with no new findings. It verified
  the fixed base source, legacy Ruby load path, service transitions, drained
  assertions, adoption/finalization, and explicit no-live-downgrade wording.
- The final committed-head review found one Blocking bypass: supported
  `ct config replace` could supply a new `incarnation_id`, causing LXC
  reconfiguration to archive the authoritative lifecycle record and substitute
  an empty record. Residual guards could then be bypassed. Config reload had
  the same identity mutation primitive through a manually edited file.
- The fix rejects differing incarnation IDs before any container mutation,
  preserves the current ID when omitted, and blocks both config reload and
  config replace while residual generations exist. Real-container regressions
  prove rejected replacement/reload retain the same lifecycle object and
  residual, while omission reloads the same residual record.
- A follow-up review of the first identity fix found three remaining blocking
  paths: image-config patches still admitted a differing ID; stopped LXC state
  could race ahead of an active reducer finalizer; and omitted/rejected IDs on
  disk could rotate identity after daemon restart.
- Exact head `bebeba8f1067fbdbe0ff707607e8e88ffb531477` fixes all three:
  every existing-container config ingestor preserves identity; stopped-only
  mutators atomically require no active or residual generation after their
  stopped check; reload durably backfills omission; and startup refuses to
  archive any mismatched record with runtime, recovery, worker, or
  quarantined-policy evidence. Deletion and consistent transfers also recheck
  exact drain after stop so a quarantined outcome is not mistaken for clean
  shutdown.
- A later fresh committed-head review found that the single 170-file lifecycle
  commit was too large to review or bisect safely. The exact final source tree
  is now split into the four functional commits recorded above. Every
  intermediate commit has its own passing full osctld suite.
- That review also found two consistent-transfer cutover defects. A source
  which was running when base export began could stop during the base phase
  and incorrectly skip the stop/incremental/start cutover. Export now captures
  that decision before the base phase and always performs the exact cutover
  sequence. Conversely, a source with a quarantined residual plus a healthy
  replacement could be stopped before the operation rejected the residual.
  Export, remote send, and local transfer now reject known residuals before
  their expensive base phase and repeat the all-runtime check after stop to
  catch newly quarantined generations.
- Regressions cover `base, stop, incremental, start` ordering, residual
  preflight for all three transfer paths, and a generation which becomes
  quarantined during stop. The final four-commit tree is byte-for-byte
  identical to the backed-up reviewed monolithic tree at
  `70b09f9185a5307ffadd400412047662255ceab7`.
- The next standalone committed-head review found three blocking delivery
  issues. First, `Container#lifecycle` always acquired an exclusive container
  lock, including from routed and bridge address changes already holding the
  inclusive lock. Second, expanding the stable CPU-bandwidth root could
  broaden an unlimited or wider residual request, and cgroup-v2 `cpu.max`
  bypassed the hierarchy policy entirely. Third, the general lifecycle VM
  scenarios were introduced in the cpuset commit instead of the lifecycle
  integration commit.
- Provisional vpsAdmin GitHub run `30181743840` independently reproduced the
  lock upgrade in `webui#vps-user-core`, transaction `#113 add_host_ip`.
  `node1-shell.log` showed `attempted to acquire exclusive lock while holding
  inclusive lock` through `NetInterface::Routed#add_ip`,
  `Runscript#with_execution_mode`, and `Container#lifecycle`. All other WebUI
  scripts in that run passed.
- Exact head `73abf97e709bb1810e4f599ea1dd40363373b45e`
  fixes those findings. An initialized reducer reference can be read while the
  container is inclusively locked; real-container routed and bridge
  regressions reproduce the call site. CPU policy now computes each
  generation's pre-transaction effective bandwidth, pins residual requests
  before relaxing ancestors, and restores ancestor caps before broad residual
  requests during rollback on both cgroup versions. `cpu.max` is selected by
  the same stable-root policy instead of the generic writer.
- The four-commit history was rewritten so `osctld/lifecycle` is registered
  with the lifecycle integration commit. Manual-launch rejection,
  unkillable-residual replacement, and drained downgrade/re-upgrade are
  present there; the cpuset commit contributes only its 57 cpuset-specific VM
  lines. The final source tree is byte-for-byte identical to the backed-up
  pre-rewrite review-fix tree
  `2026-07-24-ct-start-hang-review-fixes-pre-rewrite`.
- A new standalone mandatory review will inspect exact vpsadminOS head
  `73abf97e709bb1810e4f599ea1dd40363373b45e` and the vpsAdmin head before
  long exact-head VM reruns.
- That review found two remaining CPU-bandwidth blockers. Ordinary
  `ct cgparams apply` called the hierarchy policy without reserving lifecycle
  topology, and resetting a local limit to unlimited was rejected below a
  finite external group even though inheriting that group limit is supported.
  It also identified invalid negative quotas being normalized to unlimited and
  incomplete vpsAdmin `cleaned` replies being accepted as proof.
- Exact vpsadminOS head
  `c61f4f80f50d8190027be8bcc2a57e9b6082b59a` now admits configured CPU
  reapplication as policy reconciliation and holds a durable reducer lease
  around the hierarchy scan, writes, verification, and rollback. A rollback
  failure is persisted through the existing sticky policy taint. Local
  unlimited requests are allowed below finite external parents on cgroup v1
  and v2 because the ancestor still bounds the effective grant. Only v1 `-1`
  and v2 `max` denote unlimited; other negative quotas are rejected.
- vpsAdmin cleanup commit
  `e8c79b34315b2bea63998412ca1300670754ba8c` accepts `cleaned` only with the
  complete typed osctld envelope, empty hazards, and matching requested,
  completed, and evidenced operation sets. Truncated or inconsistent replies
  remain continuable `legacy_unknown` warnings and retain the untrusted
  structured reply for operators.
- The next fresh review of committed head `c61f4f80f50d8190027be8bcc2a57e9b6082b59a`
  found three further issues before long VM tests. The pre-start callback used
  the ordinary CPU policy lease, which is inadmissible while an exact run is
  preparing. A cgroup-v1 quota/period example transiently overshot an endpoint
  even though it remained parent/child-valid. Force-stop could leave its
  generation frozen when process enumeration or signalling raised.
- Exact head `a28afea049491d4740ad25c105aa4a33ca535b8b` records CPU policy
  application against the exact launch generation, including rollback taint,
  and reapplies persisted limits during start and restart on cgroup v1 and v2.
  The v1 policy now simulates the complete operation before its first kernel
  write, rejects mathematically impossible live two-file transitions with zero
  writes, and rolls back successful writes in exact reverse order. Force-stop
  thaws on exceptional enumeration/signalling while it still owns the effect;
  if exact recovery has superseded that ownership, recovery owns the existing
  freeze/thaw sequence.
- Quick verification at the rewritten commit series passed: lifecycle
  integration commit `c00bbe72fb43fec0e55ee49bc3251b1a97e5ce6d`
  has 105 lifecycle examples passing with seed `39690`; cpuset commit
  `53859abe9e2db2e801ed60786a5fa5f2c49b4358` has 79 focused examples
  passing with seed `5821`; the final tree has 159 focused examples passing
  with seed `25638` and all 1,271 osctld examples passing with seed `51931`.
  Nixfmt and RuboCop hooks pass. An initial commit attempt outside the Nix
  environment failed because RuboCop was absent; no commit was created, and
  the same staged changes then passed the active hook from the repository
  development environment.
- A further fresh standalone review will inspect these exact amendments before
  long exact-head VM reruns.

## Verification so far

- The first two local `osctld/lifecycle` VM attempts failed during evaluation
  of the `ruby3.4-osctld` derivation, before any VM assertion. The ignored
  repository-local `osctld/.gems/` Bundler cache was included in the gem
  source and introduced an invalid nested `bundler.gemspec`. The first cleanup
  found only the top-level generated directories; the retained log then
  identified the package-local cache. All generated `.gems/`, `.native/`, and
  `tmp/` directories were moved recoverably to
  `/tmp/vpsadminos-local-build.KU8TzN` before the next retry.
- The first completed VM execution found that LXC creates the namespaced
  `payload/inner` cgroup after `pre-start`: stopped execution inherited the
  correct effective mask but exposed an empty configured `cpuset.cpus`. The
  leased `start-host` callback now repeats the exact launch-policy transaction
  after that cgroup exists. The same run also found that the compatibility
  container ID exceeded osctld's 27-character limit.
- The following VM execution proved the start-host fix, manual-launch
  rejection, and unkillable-residual/disjoint-generation recovery. Its drained
  downgrade case stopped before switching daemons because both osctld
  supervisor and worker replace their process titles, so `/proc/PID/cmdline`
  no longer contains `--config`. The test now reads the generated config path
  from `/service/osctld/run`.
- Subsequent compatibility harness failures were test-environment defects:
  the legacy wrapper first targeted a nonexistent ambient osctld path, then
  lacked the service PATH needed by old osctld, and a shell-bound background
  process could leave user-control sockets behind. The wrapper is now built
  against the machine's overlaid `pkgs.osctld`, inherits the generated service
  PATH and locale, and runs detached under its normal osctld supervisor so
  TERM forwarding and socket cleanup match production.
- A completed old-daemon import was initially mistaken for a startup failure
  because the test polled `/run/osctld.sock`; osctld was listening normally on
  `/run/osctl/osctld.sock`. After correcting the path, the VM reached the
  substantive handoff boundary and exposed a real compatibility defect:
  legacy LXC post-stop hooks do not send a run ID, so the new exact-generation
  callback fence rejected the adopted run's final callback and `ct stop`
  correctly kept waiting for post-stop evidence.
- Only `ct_post_stop` can now resolve a missing run ID, and only from the exact
  active run explicitly marked `legacy_callbacks` by `adopt_legacy`. It then
  acquires the normal exact callback lease. New hooks, manual launches, and
  caller-supplied run IDs retain strict generation fencing.
- Live VM diagnostics then showed why the compatibility callback still did not
  reach that fallback: pool setup repoints the hook symlink to the new
  executable, while the already-running legacy LXC config invokes it without
  an argument. The new script aborted at `ARGV.fetch(0)` before connecting.
  `ct-post-stop` now accepts an absent argument so only the daemon-side adopted
  legacy resolver can supply it; current generated configs still pass and
  fence their exact run IDs.
- osctld final full suite after the admission fix: 1,210 examples, 0 failures,
  seed `5802`.
- osctld group/chgrp admission set: 30 examples, 0 failures, seed `8337`.
- osctld final spec-isolation set: 41 examples, 0 failures, seed `14054`.
- osctld cgroup focused suite: 18 examples, 0 failures, seed `17155`.
- osctld group-policy focused set: 75 examples, 0 failures.
- osctld launch/reboot review set: 106 examples, 0 failures.
- osctld recovery/TTY/attachment/runner/CLI review set: 45 examples,
  0 failures.
- osctld standalone runscript plus cgroup set: 25 examples, 0 failures,
  seed `41234`.
- Pre-review osctld full suite: 1,223 examples, 0 failures, seed `61218`.
- Post-review osctld full suite: 1,228 examples, 0 failures, seed `62927`.
- Final exact-head osctld full suite: 1,243 examples, 0 failures, seed `22587`.
- Final reducer/container identity and restart set: 107 examples, 0 failures,
  seed `31597`.
- Final command/configuration/provisioning set after admission regressions:
  36 examples, 0 failures, seed `62872`.
- Final broad lifecycle/configuration/deletion/transfer set: 223 examples,
  0 failures, seed `61271`.
- Incarnation/configuration focused set: 55 examples, 0 failures,
  seed `53629`.
- Final CPU/group hierarchy focused suite: 47 examples, 0 failures,
  seed `5272`.
- New CPU-bandwidth and group-cpuset policy specs passed standalone: 7
  examples, 0 failures, seed `34062`. The first isolated run exposed and fixed
  an order dependency on another spec loading `Container::Lifecycle`.
- libosctl full suite: 192 examples, 0 failures, seed `49892`.
- osctl full suite: 186 examples, 0 failures, seed `129`.
- vpsAdmin libnodectld structured cleanup spec: 13 examples, 0 failures,
  seed `50415`.
- Post-VM lifecycle/cgroup regression set: 100 examples, 0 failures,
  seed `31642`.
- Adopted-legacy callback and lifecycle focused set: 72 examples, 0 failures,
  seed `19398`.
- Ruby compilation and `git diff --check` passed.
- Final repository-wide `overcommit --run` at the amended patch passed Nixfmt
  and RuboCop.
- Commit-time Overcommit passed Nixfmt, RuboCop, and all commit-message hooks
  for exact head `bebeba8f1067fbdbe0ff707607e8e88ffb531477`.
  Text-width emitted advisory 72-column warnings; every line is at most the
  workspace-required 80 columns.
- `osctld/lifecycle`: 1/1 VM script passed in 406.33 seconds. It covers manual
  launch rejection, stopped execution policy, unkillable residual quarantine
  with a disjoint replacement generation, and a strictly drained old/new
  daemon downgrade/re-upgrade.
- `kernel/vpsadminos#cpu-view-cgroups-v1`: 147/147 examples and 1/1 test
  passed. The script completed in 963.96 seconds and the test in 1,053.41
  seconds. It covers configured group reconstruction, the previously failing
  400% to 250% parent/child quota restriction, finite expansion, unlimited
  reset, and combined cpuset/bandwidth policy.
- `kernel/vpsadminos#cpu-view-cgroups-v2`: 147/147 examples and 1/1 test
  passed. The script completed in 968.49 seconds and the test in 1,029.26
  seconds.
- The first final libosctl invocation inherited stale `GEM_HOME`, `GEM_PATH`,
  and `RUBYLIB` values after the ignored in-tree gem cache had been moved.
  Bundler 2.6.9 then emitted duplicate RubyGems constant warnings into four
  child-command output assertions. Suppressing warnings proved inappropriate
  because one spec intentionally checks a deprecation warning. Unsetting the
  stale gem variables selected the packaged Bundler 4.0.14 and the complete
  suite passed with warnings enabled.
- The final hook pass initially reported one unformatted Nix test and five
  correctable Ruby style offenses. After canonical Nixfmt and anonymous block
  forwarding/string-literal corrections, Nixfmt and RuboCop both passed. The
  hook-created ignored `.gems` directory was moved recoverably to
  `/tmp/vpsadminos-overcommit-gems-20260726` before further Nix evaluation.
- Commit-time hooks inspected the previously untracked policy files after they
  were staged and found additional correctable style/test-structure offenses.
  After fixing all findings, Nixfmt, RuboCop, subject, trailing-period, and
  text-width hooks passed for committed head
  `6c1d2869b460c777067864e66f80a2865d52680a`. The text-width hook emitted its
  advisory 72-column warnings; every commit-message line remains within the
  workspace's required 80-column limit.
- A final fetch found `origin/staging` advanced from `fc6c9fe67d` to
  `4476942c4` through one mechanical `flake.lock` update. The feature rebased
  cleanly with the installed pre-rebase hook enabled. New head
  `32c31af40c00d7424cfcc5f7618dbf7708099207` has the same stable feature
  patch ID `78dad4da260468d168ad78fb12045e7d91076aeb` as pre-rebase head
  `6c1d2869b460c777067864e66f80a2865d52680a`.
- `nix flake check --no-build` on the rebased tree evaluated until the
  unchanged `overlays.all = osOverlays` output. Nix rejects that output because
  it is a list where generic flake checking expects one overlay function. The
  feature does not modify `flake.nix`; this is a baseline repository
  limitation, not a change failure.
- Full osctld suite at reducer-only commit `a23a6da134c24c44f54dc1484f406f86d9721415`:
  1,085 examples, 0 failures, seed `18798`.
- Full osctld suite at lifecycle-integration commit
  `ec523ba27cb8eac56d054db47df05d9f8268ffbe`: 1,172 examples, 0 failures,
  seed `49023`.
- Full osctld suite at cpuset-hierarchy commit
  `74276404135a4acf1f8cf54452bcd8f6c2afbbd6`: 1,242 examples, 0 failures,
  seed `53318`.
- Full osctld suite at final CPU-bandwidth head
  `12cb223c531348fecd814be062ab0952c89008b0`: 1,248 examples, 0 failures,
  seed `51013`.
- Transfer/export focused suite after the cutover fixes: 48 examples,
  0 failures, seed `17360`.
- Repository-wide `overcommit --run` at exact final head
  `12cb223c531348fecd814be062ab0952c89008b0` passed Nixfmt and RuboCop.
- Exact final-head libosctl suite: 192 examples, 0 failures, seed `8659`.
- Exact final-head osctl suite: 186 examples, 0 failures, seed `13373`.
- A 2026-07-26 fetch confirmed both bases remain current:
  vpsadminOS `origin/staging` at `4476942c4` and vpsAdmin `origin/master` at
  `eb2ccde5c`. Both worktrees are clean.
- Full osctld suite at rewritten lifecycle-integration commit
  `9928c9eb2be22d8eca7406fa8e5fe2a9d03e713c`: 1,175 examples, 0 failures,
  seed `9499`.
- Full osctld suite at rewritten cpuset-hierarchy commit
  `5b813940658ff634cb7dff2d39695568a79a7ee9`: 1,245 examples, 0 failures,
  seed `38684`.
- Full osctld suite at exact final CPU-bandwidth head
  `73abf97e709bb1810e4f599ea1dd40363373b45e`: 1,256 examples, 0 failures,
  seed `61601`.
- Exact final-head libosctl suite: 192 examples, 0 failures, seed `30362`.
- Exact final-head osctl suite: 186 examples, 0 failures, seed `51562`.
- Repository-wide `overcommit --run` at exact head
  `73abf97e709bb1810e4f599ea1dd40363373b45e` passed Nixfmt and RuboCop.
- The first temporary-worktree lifecycle run loaded no examples because the
  ignored compiled `libosctl/native` extension was absent. It was rerun with
  the prepared native-only staging path after the exact commit source path;
  the successful 1,175-example result above is the validation result.
- CPU policy, container parameter, and command focused set after the final
  review fixes: 58 examples, 0 failures, seed `40831`; the final style-only
  adjustment reran the same set with 58 examples, 0 failures, seed `8621`.
- Full osctld suite before amending exact head
  `c61f4f80f50d8190027be8bcc2a57e9b6082b59a`: 1,262 examples, 0 failures,
  seed `7895`.
- vpsAdmin structured cleanup evidence suite: 34 examples, 0 failures, seed
  `3803`.
- Repository-wide vpsadminOS Overcommit passed Nixfmt and RuboCop before and
  during the exact-head amendment. Repository-wide vpsAdmin Overcommit passed
  Nixfmt, RuboCop, migration specs, API/WebUI i18n, and PHP CS Fixer. Its local
  API-i18n plugin signature first required the standard
  `overcommit --sign pre-commit` refresh; no hook was bypassed.
- A direct vpsadminOS focused-suite invocation outside the prepared Nix shell
  lacked `NETLINKRB_PATH`, and one direct hook invocation lacked `nixfmt`.
  Both were harness-only failures; the suites and hooks passed in the
  initialized repository shell.
- The mandatory review of exact vpsadminOS head
  `a28afea049491d4740ad25c105aa4a33ca535b8b` accepted the lifecycle
  architecture, force-stop ownership handoff, container-local CPU transaction,
  four-commit split, and vpsAdmin cleanup evidence. It did not clear long
  integration tests because group CPU `set`, `unset`, `replace`, and full
  `apply` still use generic writes. Those writes neither fence descendant
  lifecycle topology nor transact nested group/container cgroups, so a v1
  restriction can fail after configuration persistence and an expansion can
  broaden a residual. The next amendment must extend durable group quarantine,
  descendant leases, ordered preflight, and rollback to CPU bandwidth.
- Exact-head test-runner evaluation after that review rebuilt successfully and
  lists `osctld/lifecycle`,
  `kernel/vpsadminos#cpu-view-cgroups-v1`, and
  `kernel/vpsadminos#cpu-view-cgroups-v2`; no VM was started.

## Remaining work

1. Rerun
   `osctld/restart`, `osctld/lifecycle`, and both sequential cgroup-v1/v2 VM
   cases on the exact reviewed head.
2. Force-push vpsadminOS with lease, then rewrite the provisional vpsAdmin
   input commit and update the vpsAdmin
   vpsadminOS flake input using `tools/update_vpsadminos_flake.sh`.
3. Force-push the final vpsAdmin head with lease. Cancel only
   superseded workflow runs whose `headSha` differs from the new branch head,
   and monitor all exact-head workflows, including integration tests, through
   terminal completion.
4. Finalize and commit the initiative plan, state, and durable test-runner note
   on the shared workspace `master`, staging only those paths.

## Commands and evidence

- Failed pre-VM logs:
  `/tmp/os-test-runner/os-test-osctld__lifecycle-000573c0/test-runner.log`.
- Verified the active session with `bin/dev-session current` and the matching
  `VPSFREE_DEV_SESSION_SLUG`.
- Inspected both `osctl debug threads ls` screenshots and filtered
  `node21-osctld-log.log` around `tank:26108`.
- Read workspace and repository `AGENTS.md` files and inspected lifecycle,
  console, monitor, callback, cgroup, process, recovery, and vpsAdmin cleanup
  paths and their history.
- Built the local ruby-lxc extension and used the repository Nix shell for
  Ruby suites and review-focused randomized runs.
- Used `./test-runner.sh ls` to evaluate the new lifecycle test definitions.

## Group controller transaction amendment

- Added commit `5094efad2db1b4c7458bb68ffecf7429c872f98e`
  (`osctld: transact group cgroup policies`) on top of the previously reviewed
  lifecycle series.
- The amendment replaces generic group CPU-bandwidth writes with a fenced
  subtree transaction. It preflights all configured descendants, journals
  exact kernel state, orders v1 expansion/restriction safely, retains wider v2
  requests behind ancestor caps, and pins residual generations before an
  ancestor is broadened.
- Group CPU and cpuset mutations now share descendant lifecycle leases,
  persistent write-ahead quarantine markers, exact compensation, and
  requested-path-only reconstruction. Generic parameter recovery has a
  separate marker and cannot clear or infer controller-policy recovery.
- Added v1/v2 kernel integration coverage for stopped-path reconstruction,
  ignored stopped siblings, live start/restart inheritance, ordered
  expansion/restriction, v1 wider-child rejection, v2 wider-child retention,
  and unlimited child inheritance. Extended the unkillable residual VM case
  to verify the old generation remains pinned while a disjoint replacement
  receives a wider group CPU policy.
- Quick verification for the committed design:
  - affected osctld set: 241 examples, 0 failures, seed `4513`;
  - full osctld suite: 1,310 examples, 0 failures, seeds `4514` and `4515`;
  - standalone new group CPU policy spec after commit-hook cleanup:
    19 examples, 0 failures, seed `4516`;
  - `nixfmt --check` passed for both changed VM definitions;
  - `./test-runner.sh ls` evaluated the suite and listed all four intended VM
    cases;
  - repository-wide Overcommit passed Nixfmt and RuboCop;
  - commit-time Overcommit passed Nixfmt, RuboCop, and all message hooks.
    The 72-column text-width hook was advisory; every commit-message line is
    within the workspace-required 80 columns.
- An initial standalone Overcommit invocation used the recovered gem directory
  as the only `GEM_PATH` and could not find Ruby's default `rexml` gem. Adding
  the Nix Ruby default-gem path restored the intended hook environment. No hook
  was bypassed.
- The first commit attempt found offenses in the newly staged spec which the
  earlier run did not inspect while that file was untracked. The test helpers
  now use RSpec-restored stub constants and message spies, and the exact staged
  tree then passed the hooks before the successful commit.
- Post-commit exact-head quick suites also passed:
  - osctld: 1,310 examples, 0 failures, seed `4517`;
  - libosctl: 192 examples, 0 failures, seed `4518`;
  - osctl: 186 examples, 0 failures, seed `4519`.

## Mandatory review of `5094efad`

- Fresh standalone reviewer
  `/root/mandatory_change_review_5094efad` inspected both committed repository
  ranges and did not start nested reviewers or make changes.
- The review accepted the five-commit vpsadminOS split, including the common
  group-controller transaction protocol in `5094efad`, and accepted the
  vpsAdmin structured-cleanup parser and separate Playwright packaging repair.
  It found no additional security or tenant-isolation issue.
- Long VM tests remain blocked on two correctness findings:
  1. partial cgroup-v1 CPU quota/period unset and replace lose the distinction
     between an unspecified live component and an explicitly removed
     component, so the removed runtime value can remain active;
  2. requested-path reconstruction can create cgroups or change v2 delegation
     outside the parameter journal, while transactional mutation currently
     claims exact rollback and may clear the persistent marker after a later
     failure.
- The reviewer also marked the missing shipped operator documentation as
  Important: `osctl.8` must describe persistent group quarantine and exact
  `group cgparams apply` recovery, and lifecycle warnings must not call every
  controller failure a cpuset failure.
- Decision: fix both blockers and the operator guidance, amend the fifth
  unmerged commit, rerun quick verification, and obtain a fresh exact-head
  review before starting any VM.

## Review fixes in `6122d45a`

- Partial cgroup-v1 CPU quota/period removal now carries explicit reset intent
  into the hierarchy policy instead of treating the removed component as
  unspecified. The durable group marker records both the reset parameters and
  a fingerprint of the intended persisted CPU configuration.
- Recovery replays a recorded reset only when the current configuration
  matches that fingerprint. This distinguishes a crash after the staged
  configuration commit from a crash before it or a failed transaction which
  restored the old configuration.
- Requested-path CPU and cpuset reconstruction is conservatively
  non-compensable because it can create cgroups or change cgroup-v2 controller
  delegation outside the parameter journal. A failure after reconstruction
  now carries a rollback error, retains the persistent quarantine, and
  requires an exact `osctl group cgparams apply <group>` recovery.
- Added shipped `osctl(8)` guidance for persistent group quarantine, fenced
  operations, exact recovery, and the `cgroup-policy.yml` safety record.
  Lifecycle admission errors now name the exact group apply command instead
  of referring generically to cpuset recovery.
- Verification before the exact-head review:
  - focused group controller policy set: 83 examples, 0 failures, seed
    `4523`;
  - affected controller and lifecycle set: 249 examples, 0 failures, seed
    `4524`;
  - standalone group cpuset policy: 4 examples, 0 failures, seed `4525`;
  - full osctld suite: 1,318 examples, 0 failures, seed `4526`;
  - exact-head libosctl suite: 192 examples, 0 failures, seed `4527`;
  - exact-head osctl suite: 186 examples, 0 failures, seed `4528`;
  - Ruby syntax checks passed for every changed daemon source;
  - repository-wide Overcommit passed Nixfmt and RuboCop, both before and
    during the amend commit.
- `nixfmt --check` passed for all three changed VM definitions and exact-head
  `test-runner.sh ls` evaluation lists `osctld/restart`,
  `osctld/lifecycle`, `kernel/vpsadminos#cpu-view-cgroups-v1`, and
  `kernel/vpsadminos#cpu-view-cgroups-v2`.
- Commit `5094efad2db1b4c7458bb68ffecf7429c872f98e` was amended to exact head
  `6122d45a495e81f4745f577757d060dad03d1309`. No VM has been started on the
  revised head pending the required fresh standalone review.

## Mandatory review of `6122d45a`

- Fresh standalone reviewer `/root/mandatory_change_review_6122d45a`
  inspected the full vpsadminOS and vpsAdmin series without edits or nested
  reviewers.
- It accepted the five-commit vpsadminOS split, vpsAdmin cleanup parser, and
  separate Playwright repair, and found no additional security or
  tenant-isolation issue.
- It found one Blocking exception-propagation path: direct policy failure was
  wrapped twice without retaining its reconstruction rollback error, so a
  transactional group mutation could incorrectly clear the WAL marker after
  non-compensable path/delegation changes.
- It also requested pool-qualified recovery guidance and an explicit rollback
  checklist covering container policy taints, persistent group markers, and
  generation cgroups. VM tests remained blocked.
- The fifth commit was amended again to
  `3242856faddeefb0c09c29cf8a8b721855322b3e`:
  - both parameter-policy wrappers now preserve and combine original and
    secondary rollback errors;
  - `policy_compensated` is true only when every policy compensation is
    proven;
  - the group command regression now traverses the real
    `Params#transactional_set` boundary, restores the old configuration, and
    proves the persistent marker is tainted instead of cleared;
  - lifecycle warnings use `pool:group`, and the downgrade checklist names
    every new hazard which an older daemon cannot interpret.
- Post-fix verification:
  - focused policy/command/lifecycle set: 138 examples, 0 failures, seed
    `4529`;
  - parameter/group command set: 46 examples, 0 failures, seed `4530`;
  - affected controller/lifecycle set: 249 examples, 0 failures, seed `4531`;
  - full osctld suite: 1,318 examples, 0 failures, seed `4532`;
  - repository-wide and commit-time Overcommit passed Nixfmt and RuboCop.
- No VM has been started on `3242856f` pending a final fresh exact-head
  mandatory review.

## Mandatory review of `3242856f`

- Fresh standalone reviewer `/root/mandatory_change_review_3242856f`
  reviewed the exact committed vpsadminOS and vpsAdmin ranges without edits
  or nested reviewers.
- Disposition: no Blocking, Important, or Advisory findings. The reviewer
  confirmed that both parameter-policy wrappers preserve and combine rollback
  evidence and that the real group-command regression keeps the persistent
  marker tainted.
- The pool-qualified recovery command, downgrade checklist, five-commit
  vpsadminOS split, vpsAdmin cleanup parser, Playwright repair, compatibility
  model, and security/tenant-isolation posture were accepted.
- Long VM tests are cleared, strictly sequentially, on exact head
  `3242856faddeefb0c09c29cf8a8b721855322b3e`.
- Residual review risks are power loss at persistence boundaries not covered
  by every possible injection point, intentionally unbounded libLXC/hook waits
  which still rely on exact recovery or daemon restart, and the provisional
  vpsAdmin input pin which remains an explicit delivery gate.

## Packaged daemon load-order fix

- The first sequential `osctld/restart` attempt on reviewed head `3242856f`
  built and booted the VM, but osctld never became ready. The immutable package
  repeatedly failed in `container/run_id.rb` with
  `uninitialized constant OsCtld::Container`.
- The complete console traceback in
  `/tmp/os-test-runner/os-test-osctld__restart-b891f158/machine-console.log`
  showed the exact chain: `osctld.rb` intentionally loads
  `osctld/utils/container.rb` before the root `Container` class, while the new
  utility code eagerly required `container/run_id.rb`. Unit specs had hidden
  the defect because `spec/support/namespace_bootstrap.rb` predefines
  `OsCtld::Container`.
- The failed VM was stopped after the repeating crash traceback was captured;
  waiting longer could only exhaust the service-readiness budget. The runner
  returned status 1 and QEMU cleanup completed.
- The fix removes the unnecessary eager require and adds a subprocess
  regression which loads `Utils::Container` before `OsCtld::Container` exists.
  A full top-level require on the development host passed the original failure
  point and then stopped at the unrelated production-only `repository` system
  account lookup; the packaged VM remains the full daemon-load check.
- Before history cleanup, the fresh-process/run-ID set passed 6 examples with
  seed `4533`, the focused load spec passed with seed `4535`, and the complete
  osctld suite passed 1,319 examples with seed `4534`. Repository-wide
  Overcommit passed Nixfmt and RuboCop.
- An initial non-login commit and rebase invocation did not inherit the local
  Overcommit/RuboCop gem path and were refused by the active hooks. Repeating
  them inside the prepared Nix shell used the same declared gem tree as the
  successful repository-wide hook. No hook was bypassed; the existing durable
  environment guidance is in
  `notes/vpsadminos/2026-06-14-overcommit-missing-ambient-shell.md`.
- The hook then found two offenses in the newly staged regression which the
  earlier unstaged hook run did not inspect. They were corrected, and the
  focused spec plus staged and commit-time Nixfmt/RuboCop hooks passed.
- The fix was autosquashed into the lifecycle-routing commit, preserving the
  five-commit split. The rewritten exact head is
  `26cab6920be13538d48f92e1cf0c9a0e8db40430`; the pre-fix reviewed tree is
  preserved by the backup branch recorded above.
- Exact-head quick verification after the rewrite passed:
  - osctld: 1,319 examples, 0 failures, seed `4536`;
  - libosctl: 192 examples, 0 failures, seed `4537`;
  - osctl: 186 examples, 0 failures, seed `4538`;
  - repository-wide Overcommit: Nixfmt and RuboCop passed;
  - Nixfmt passed for all three changed VM sources;
  - `test-runner.sh ls` evaluated and listed `osctld/restart`,
    `osctld/lifecycle`, and both cgroup v1/v2 VM cases;
  - `git diff --check` passed and the vpsadminOS worktree is clean.
- Fresh SSH fetches immediately before the exact-head review confirmed that
  vpsadminOS `origin/staging` remains at `4476942c4e33092e20e4faa91f32dfcca9a3ea7d`
  and vpsAdmin `origin/master` remains at
  `eb2ccde5cd709a42a802589419ba8cf525c97f34`; both are ancestors of the
  respective feature heads.

## Mandatory review of `26cab692`

- Fresh standalone reviewer
  `/root/mandatory_load_order_review_26cab692` reviewed both complete committed
  repository ranges without edits or nested reviewers.
- Disposition: no Blocking, Important, or Advisory findings. The reviewer
  confirmed the intentional utility-before-container load order, the targeted
  removal of the premature `RunId` dependency, and that the subprocess
  regression neither loads the spec namespace bootstrap nor predefines
  `OsCtld::Container`.
- The five-commit vpsadminOS split, exact-generation lifecycle/recovery model,
  quarantine and cgroup transactions, vpsAdmin cleanup evidence, separate
  Playwright packaging repair, deployment compatibility, security boundaries,
  and rollback guidance remain accepted.
- All four long VM cases are cleared strictly sequentially on exact head
  `26cab6920be13538d48f92e1cf0c9a0e8db40430`, beginning with
  `osctld/restart`.
- Residual risks are the not-yet-repeated packaged-daemon boot, incomplete
  crash injection across every persistence boundary, and the explicitly
  provisional vpsAdmin flake pin.
- Exact-head `osctld/restart` passed all 8 RSpec-style VM examples and the
  single test in 387.53 seconds. The rebuilt packaged daemon booted without the
  prior load exception. Coverage includes graceful and abrupt osctld restart,
  active start/restart/local-copy ownership, and the original in-container
  reboot racing an external start converging on one replacement generation.
- Exact-head `osctld/lifecycle` passed all 4 RSpec-style VM examples and the
  single test in 346.43 seconds. It proved unkillable-generation quarantine
  with a disjoint replacement, namespaced stopped-execution cpuset policy,
  rejection of unauthorized manual `lxc-start`, and a strictly drained
  old-daemon downgrade/re-upgrade with legacy-run adoption.
- The first exact-head cgroup-v1 attempt passed its first 19 of 155 examples,
  then failed before evaluating the new persisted CPU-bandwidth cases. The
  retained runner log at
  `/tmp/os-test-runner/os-test-kernel__vpsadminos-f1b75a4a/test-runner.log`
  reports `Machine#succeeds: wrong number of arguments (given 2, expected 1)`.
  The new setup passed two command strings to the single-command API; no guest
  command or policy assertion failed.
- An AST audit of every fully rendered test script in the retained JSON found
  this same misuse in only the cgroup-v1/v2 renderings of the shared source.
  The setup now uses the existing multi-command `machine.all_succeed` API.
  This test-only correction belongs in the CPU-bandwidth commit which added
  the persisted-limit cases. It requires history cleanup, quick validation,
  and a fresh mandatory review before any VM rerun.

## Cgroup VM harness correction and rewritten head

- The previously reviewed head `26cab6920be13538d48f92e1cf0c9a0e8db40430`
  is preserved as local backup branch
  `2026-07-24-ct-start-hang-pre-cgroup-vm-fix`.
- The one-line test correction was committed through the active Nixfmt hook
  and autosquashed into `osctld: order CPU bandwidth hierarchy updates`.
  The five-commit split is preserved. The rewritten exact vpsadminOS head is
  `44f551432dc19f5a65b7c76810a52b3cf6d992b3`.
- The tree difference from `26cab692` is exactly the replacement of
  `machine.succeeds` with `machine.all_succeed` in the shared persisted CPU
  bandwidth setup. No production Ruby or Nix source differs.
- Exact-head quick verification after the rewrite passed:
  - repository-wide Overcommit passed Nixfmt and RuboCop;
  - Nixfmt passed for `tests/suite/kernel/vpsadminos/cpu-view.nix`;
  - `test-runner.sh ls` evaluated and listed both osctld VM cases and both
    cgroup CPU-view variants;
  - a fresh `evaluate-tests.nix` rendering produced all 14
    kernel/vpsadminos scripts, and a Ruby AST audit found no multi-positional
    `machine.succeeds` calls;
  - `git diff --check` passed and the vpsadminOS worktree is clean.
- The complete Ruby unit suites were not repeated for this rewrite because
  their exact tested source tree is unchanged from `26cab692`; the earlier
  1,319 osctld, 192 libosctl, and 186 osctl examples therefore remain
  applicable. The long VM matrix will be repeated on the rewritten commit
  after a fresh mandatory review.

## Mandatory review of `44f551432`

- Fresh standalone reviewer
  `/root/mandatory_cgroup_harness_review_44f551432` read the mandatory review
  skill, both complete tracking files, repository instructions, and both
  complete committed ranges. It made no edits and used no nested reviewers.
- Disposition: no Blocking, Important, or Advisory findings.
- The reviewer independently rechecked reducer/lifecycle effect fencing,
  exact callback/process/console/monitor ownership, recovery and unkillable
  generation quarantine, cgroup transaction/WAL/rollback behavior,
  incarnation and rolling downgrade compatibility, security boundaries,
  vpsAdmin cleanup evidence, commit separation, tests, and documentation.
- It confirmed that the tree delta from the previously reviewed vpsadminOS
  head is confined to the valid test-harness API correction and that both
  worktrees remained clean at the reviewed heads.
- Long sequential VM validation is cleared on exact head
  `44f551432dc19f5a65b7c76810a52b3cf6d992b3`, in order:
  `osctld/restart`, `osctld/lifecycle`,
  `kernel/vpsadminos#cpu-view-cgroups-v1`, then
  `kernel/vpsadminos#cpu-view-cgroups-v2`.
- The provisional vpsAdmin flake pin remains an explicit delivery gate and
  must be rewritten to the final pushed vpsadminOS revision before vpsAdmin is
  pushed.
- Exact-head `osctld/restart` passed all 8 RSpec-style VM examples and its
  single test in 378.73 seconds. The packaged daemon booted, active work
  survived graceful/abrupt daemon restart, and the original in-container
  reboot plus concurrent external start converged on one replacement
  generation.
- Exact-head `osctld/lifecycle` passed all 4 RSpec-style VM examples and its
  single test in 329.21 seconds. It proved managed-launch rejection of manual
  `lxc-start`, drained downgrade/re-upgrade adoption, quarantine of an
  unkillable residual generation followed by a disjoint replacement, and
  namespaced cpuset application for stopped execution.
- The first exact-head cgroup-v1 rerun cleared the former harness failure:
  examples 20 and 21 executed and proved persisted CPU bandwidth on start and
  restart. It passed 23/155 examples before the setup for the next new context
  failed, before any example in that context.
- The retained log at
  `/tmp/os-test-runner/os-test-kernel__vpsadminos-f1b75a4a/test-runner.log`
  reports that direct `rmdir` of the configured child CPU controller cgroup
  returned `EBUSY`. Captured diagnostics show the exact cause: moving the
  stopped container into the child group had started its group monitor and
  created nested user/monitor cgroups while osctld was still running. The
  production group CPU transaction was not invoked.
- The context is intended to simulate missing controller hierarchy after a
  daemon restart. Its setup now stops osctld first, recursively removes the
  isolated CPU-controller group subtree from leaves to root, and starts
  osctld again. This drains the monitor owners before removing their cgroups
  and applies to both the v1 CPU hierarchy and the v2 unified subtree.
- Reviewed head `44f551432dc19f5a65b7c76810a52b3cf6d992b3`,
  including its two passing exact-head osctld VMs and the diagnosed cgroup-v1
  failure, is preserved by local backup branch
  `2026-07-24-ct-start-hang-pre-cgroup-tree-vm-fix`.
- The setup correction was committed through the active Nixfmt hook and
  autosquashed into `osctld: transact group cgroup policies`. The rewritten
  exact vpsadminOS head is
  `931fc956b78bb0d2d44a5685df5b8cdf8227a766`; the other four commit IDs and
  all production source remain unchanged.
- Exact-head quick validation passed repository-wide Overcommit, Nixfmt,
  test-catalog evaluation, `git diff --check`, Ruby parsing of all 14 rendered
  kernel/vpsadminos scripts, and shell syntax checks for the concrete v1/v2
  cleanup commands. The fully rendered scripts contain the intended
  stop/remove/start sequence in both variants.

## Review and exact monitor cleanup for group CPU VM setup

- Fresh standalone reviewer `/root/mandatory_cgroup_tree_review_931fc956b`
  found one Blocking issue in the corrected VM setup and no Important or
  Advisory issue. The complete production design, compatibility, security,
  recovery, vpsAdmin evidence, and commit split otherwise remained accepted.
- The reviewer confirmed from code and retained diagnostics that daemon stop
  terminates and joins each `lxc-monitor` client, but intentionally does not
  call the per-group `lxc-monitor --quit` path. Its daemonized
  `lxc-monitord`, shown with PPID 1 in the target child group, could therefore
  remain after `sv stop` and keep the hierarchy busy. VM resumption on
  `931fc956b` was rejected.
- The setup now captures osctld's exact post-`chgrp` `lxc_path` and exact
  system username before daemon shutdown. After stopping osctld, it invokes
  `lxc-monitor -P <exact-path> --quit` through `chpst` as that user, then
  removes the isolated group hierarchy leaf-to-root. The removal remains the
  hard check: if the quit did not drain the owner, setup still fails rather
  than masking it.
- Nixfmt and test-catalog evaluation pass. Freshly rendered cgroup-v1/v2
  scripts contain the exact query/stop/user-switch/quit/remove/start sequence;
  all 14 rendered scripts parse as Ruby, the concrete monitor and cleanup
  commands parse as shell, and the guest system path includes runit's
  `chpst`.
- Rejected head `931fc956b78bb0d2d44a5685df5b8cdf8227a766` is
  preserved by local branch
  `2026-07-24-ct-start-hang-pre-monitord-vm-fix`.
- The exact-monitor correction was committed through the active Nixfmt hook
  and autosquashed into `osctld: transact group cgroup policies`. The new
  exact vpsadminOS head is
  `52fde42a47211b64904197f5914d12c3dfee8f80`; all production source and
  the first four commit IDs remain unchanged. Repository-wide exact-head
  Overcommit and `git diff --check` pass, and the worktree is clean.

## Review and deterministic cgroup-drain VM setup

- Fresh standalone reviewer `/root/mandatory_monitord_review_52fde42a4`
  found two Blocking test-harness issues and no Important or Advisory issue.
  The reviewer again accepted the complete production design, compatibility,
  security, recovery, vpsAdmin evidence, and commit split.
- First, `lxc-monitor --quit` sends the quit message and exits without waiting
  for an acknowledgement from `lxc-monitord`. Immediate hierarchy removal
  could therefore race daemon exit. The setup now waits, for at most 120
  seconds in the VM harness, until all target-subtree task files are empty:
  `tasks` on cgroup v1 and `cgroup.procs` on cgroup v2. The subsequent
  leaf-to-root `rmdir` remains a hard assertion.
- Second, cgroup v2 daemon startup intentionally reconstructs all configured
  unified paths for device policy, including the unrelated stopped group. Its
  absence was therefore not a valid v2 assertion. The v2 case now verifies
  that this recreated group retains default unlimited CPU bandwidth; the v1
  case continues to verify that the unrelated CPU-controller path is absent.
- These are bounded VM-runner synchronization and assertions only. No
  production lifecycle effect, start, stop, restart, or reboot path gains a
  timeout or watchdog; production waits remain intentionally unbounded.
- Nixfmt, test-catalog evaluation, and `git diff --check` pass. A fresh
  `evaluate-tests.nix` render contains all 14 kernel/vpsadminos scripts.
  Every rendered script parses as Ruby, the concrete v1/v2 drain and removal
  commands parse as shell, and inspection confirms the intended
  v1/v2-specific task files and stopped-group assertions.
- Rejected head `52fde42a47211b64904197f5914d12c3dfee8f80` is
  preserved by local branch
  `2026-07-24-ct-start-hang-pre-cgroup-drain-vm-fix`.
- The deterministic-drain correction was committed through the active Nixfmt
  hook and autosquashed into `osctld: transact group cgroup policies`. The
  rewritten exact vpsadminOS head is
  `ec2eadbd5c79f45c1b8f4745d004eab194e358bf`; the first four commit IDs and
  all production source remain unchanged. Repository-wide exact-head
  Overcommit and `git diff --check` pass, and the worktree is clean.
- Fresh SSH fetches before the exact-head review confirmed vpsadminOS
  `origin/staging` is still
  `4476942c4e33092e20e4faa91f32dfcca9a3ea7d` and vpsAdmin
  `origin/master` is still
  `eb2ccde5cd709a42a802589419ba8cf525c97f34`; each remains an ancestor of
  its feature head.

## Mandatory review of `ec2eadbd5`

- Fresh standalone reviewer
  `/root/mandatory_cgroup_drain_review_ec2eadbd5` reviewed the complete
  vpsadminOS and vpsAdmin committed ranges without edits or nested reviewers.
- Disposition: no Blocking or Important findings. Exact vpsadminOS head
  `ec2eadbd5c79f45c1b8f4745d004eab194e358bf` was cleared for the four
  long VM cases in strict sequence.
- The reviewer independently rendered and parsed all 14 kernel/vpsadminos
  scripts and confirmed the exact-monitor shutdown, controller-specific task
  drain, hard removal, and v1/v2 assertion behavior. It also reconfirmed that
  production has no lifecycle timeout or watchdog and accepted the complete
  reducer, ownership, recovery, quarantine, cgroup transaction, compatibility,
  security, documentation, vpsAdmin evidence, and commit-series design.
- One Advisory finding noted that `ProcessIdentity.load` accepts a prototype
  `start_time` persistence key even though the base branch has no such records
  and the feature writes only `start_time_ticks`. Repository history confirms
  the alternate key exists only on unmerged prototype/backup feature commits;
  there is no deployed or documented consumer. Keeping it would mask malformed
  current records, so the advisory will be fixed before the VM matrix.
- Reviewed head `ec2eadbd5c79f45c1b8f4745d004eab194e358bf` is
  preserved by local branch
  `2026-07-24-ct-start-hang-pre-process-identity-schema-cleanup`.
  Removing the fallback and its compatibility spec rewrites the reducer
  commit, so focused checks, hooks, and a fresh mandatory review are required
  before the long VM gate reopens.
- The fallback and its sole compatibility example were removed. The focused
  process-identity spec passed 4 examples with seed `4540`; repository-wide
  Overcommit passed Nixfmt and RuboCop, and `git diff --check` passed.
- The correction was committed through the active hooks and autosquashed into
  `osctld: add durable container lifecycle reducer`. Because it changes the
  first commit, all five feature commit IDs were rewritten. The new exact
  vpsadminOS head is
  `b7bf1cb7940f67e79d052a7ee5c1d518c63ce668`; the worktree is clean.

## Mandatory review of `b7bf1cb79`

- Fresh standalone reviewer
  `/root/mandatory_process_identity_review_b7bf1cb79` reviewed both complete
  committed ranges without edits or nested reviewers.
- Disposition: no Blocking, Important, or Advisory findings. The previous
  ProcessIdentity advisory is resolved, and exact vpsadminOS head
  `b7bf1cb7940f67e79d052a7ee5c1d518c63ce668` is cleared for the strict
  four-VM sequence.
- The reviewer confirmed that the base/default tree and release tags have no
  ProcessIdentity persistence, all feature writers and other readers use only
  `start_time_ticks`, no unmerged prototype wrote the old key, and drained
  old-daemon compatibility does not consume this schema. A malformed record
  now raises and preserves ownership instead of being mistaken for a dead
  process.
- Range-diff confirms only the first reducer commit changed from the prior
  cleared series; the other four commits are patch-equivalent. The complete
  lifecycle, recovery, cgroup, security, deployment, vpsAdmin evidence, and
  commit-series assessments remain accepted.
- Residual risks are the not-yet-run exact-head VM matrix, incomplete crash
  injection across every persistence boundary, intentional recovery reliance
  for indefinitely blocked production effects, and the provisional vpsAdmin
  flake pin.
- Exact-head `osctld/restart` passed all 8 RSpec-style examples and its single
  test in 392.13 seconds. The packaged daemon booted cleanly; the original
  in-container reboot plus concurrent external start converged on one
  replacement generation, and graceful/abrupt daemon restart, active
  start/restart, monitor/top clients, and local-copy ownership all completed.
- Exact-head `osctld/lifecycle` passed all 4 RSpec-style examples and its
  single test in 343.95 seconds. It proved stopped-execution cpuset policy,
  drained downgrade/re-upgrade adoption, quarantine plus a disjoint
  replacement for an unkillable residual generation, and rejection of manual
  `lxc-start` without managed-launch authorization.
- The first exact-head cgroup-v1 run cleared the previously failing harness
  setup and passed all new production-policy examples 20 through 29. It then
  failed after 50/155, while entering the existing 201% CPU-view context.
- Retained evidence at
  `/tmp/os-test-runner/os-test-kernel__vpsadminos-f1b75a4a/test-runner.log`
  shows a real cgroup-v1 kernel rejection, not a runner error:
  the 250% to 201% restriction wrote the active payload first, then
  `cpu.cfs_quota_us=201000` at the stable container policy root returned
  `EINVAL`; rollback restored the payload to 250%. The runner captured
  diagnostics and powered off cleanly.
- Exact kernel source `a2384967` validates both the proposed task group's
  quota and the complete v1 task-group hierarchy before a write. The current
  unit model covers parent/child quota ordering but the retained diagnostics
  do not include every live quota/period/burst file, so a blind rerun is not
  accepted. A focused interactive reproduction and complete controller-tree
  snapshot are required before deciding whether the policy topology scan or
  VM environment is at fault.

## Retired cgroup-v1 CPU scheduler diagnosis

- An interactive reproduction in the same cgroup-v1 VM proved that a simple
  250% to 201% policy change succeeds before a managed restart and consistently
  fails after `stop`/`start`/`restart`.
- Complete visible quota/period/burst enumeration under the stable container
  root showed only the stable root and current payload at 250%. The prior
  generation directories were already absent. Waiting did not change the
  result.
- Setting the current payload quota to unlimited by hand did not allow the
  stable root to be restricted to 201%. This rules out write ordering against
  the current generation.
- The exact vpsAdminOS kernel keeps a removed cgroup-v1 scheduler task group in
  the parent hierarchy while its CSS is released asynchronously. Hierarchy
  validation therefore still sees the removed generation's finite 250% child
  even though userspace can no longer enumerate or modify it. The invisible
  child rejects the new 201% stable-parent quota with `EINVAL`.
- This is the root cause of the exact-head VM failure. The CPU transaction and
  rollback behaved correctly; generation retirement failed to neutralize a
  finite quota before removing a task-free v1 cgroup.
- Rejected head `b7bf1cb7940f67e79d052a7ee5c1d518c63ce668` is
  preserved by local branch
  `2026-07-24-ct-start-hang-pre-dying-cpu-cgroup-fix`.

## Drained generation retirement fix

- `CGroup.retire_tree` now serializes retirement with all osctld cgroup
  transactions, prevents forks, and enumerates `cgroup.procs` throughout every
  controller. It raises `EBUSY` before changing CPU policy if any process
  remains.
- A proven-drained cgroup-v1 tree has every finite `cpu.cfs_quota_us`
  neutralized to unlimited in leaf-to-root order before removal. This ensures
  an asynchronously dying task group cannot constrain the stable parent.
  Cgroup v2 retirement does not alter `cpu.max`.
- Exact-generation cleanup and adopted/untracked legacy cleanup use the same
  retirement boundary. An unkillable or partially attached process therefore
  preserves its quota and causes the existing blocked/quarantined recovery
  path; the change does not make residual workloads less constrained.
- The cgroup-v1 CPU-view VM now has an explicit regression example which
  restricts a persisted 250% limit to 201% immediately after a managed restart.
- Focused cgroup/recovery specs passed 47 examples with seeds `4541` and
  `4543`, then 48 examples with seed `4544` after adding the exact-generation
  routing assertion. The full osctld suite passed 1321 examples with seed
  `4542`.
- `git diff --check`, Nixfmt, test-catalog evaluation with
  `./test-runner.sh ls`, and repository-wide Overcommit all pass. An attempted
  `./test-runner.sh list` was rejected because the command is named `ls`;
  the corrected catalog evaluation passed.
- The fix was committed as
  `2b4a91864ee5bf1ff4ac02ca2ce04addf7c5bcfa`
  (`osctld: retire drained v1 CPU cgroups safely`). The hook framework ran
  Nixfmt and RuboCop successfully; all commit-message lines satisfy the
  workspace's 80-character limit. The vpsadminOS worktree is clean.

## Rejected teardown-time retirement and stable CPU policy roots

- Fresh standalone reviewer
  `/root/mandatory_retired_cgroup_review_2b4a91864` rejected exact head
  `2b4a91864ee5bf1ff4ac02ca2ce04addf7c5bcfa` with two Blocking findings
  and no other Important finding.
- The pinned LXC teardown removes its payload cgroup before `lxc-start`
  exits. Osctld's generation finalizer therefore runs too late to make that
  payload unlimited, and the invisible finite cgroup-v1 scheduler object can
  already exist.
- Snapshotting tasks, clearing a finite quota, and removing the cgroup is not
  atomic against concurrent task migration. A failed removal could leave a
  residual workload locally unlimited. This conflicts with the requirement
  that unkillable generations retain their prior effective constraint.
- The rejected commit is preserved by local branch
  `2026-07-24-ct-start-hang-pre-stable-cpu-root-redesign`. Its
  `CGroup.retire_tree` implementation, callers, and tests were removed from
  the feature head rather than retained as reversal history.
- A focused cgroup-v1 VM diagnosis proved that the stable container root alone
  can hold the finite CPU policy. With the active LXC payload explicitly
  unlimited and the stable root at 201%, the guest still observed three CPUs
  consistently through `nproc`, `/proc/cpuinfo`, `/proc/stat`, and
  `/sys/devices/system/cpu/online`. CPU enforcement is inherited from the
  stable ancestor.
- The replacement design never puts finite CPU bandwidth on an LXC-owned
  ephemeral payload. Active payloads are unlimited and the osctld-owned
  stable container root holds their policy. LXC configuration omits
  `cpu.cfs_period_us`, `cpu.cfs_quota_us`, and `cpu.max`, so even a failed
  start cannot leave a finite payload before the managed pre-start callback.
- A residual generation first has its current effective bandwidth pinned at
  its osctld-owned generation root. Descendants are then made locally
  unlimited below that pin before any ancestor is expanded or restricted.
  An unkillable residual therefore keeps its effective limit in a disjoint
  osctld-owned root, while later LXC payload removal cannot leave an invisible
  finite scheduler child.
- Unit regressions cover active-payload unlimited policy, residual-root
  pinning, descendant neutralization, transaction ordering, and rollback.
  The cgroup-v1 VM regression covers both a managed restart followed by a
  250% to 201% restriction and a start that fails in a user pre-start hook
  after LXC configured cgroups, followed by the same restriction. Both would
  expose an invisible finite payload.
- The full osctld suite passed 1321 examples with seed `4548` on this design
  before a final branch-only refactor. Focused CPU/group specs then passed
  42 examples with seed `4550`, and the final focused CPU/group/recovery set
  passed 68 examples with seed `4551`. Repository-wide Overcommit passed
  Nixfmt and RuboCop; `git diff --check`, ERB compilation, and test-catalog
  evaluation pass.
- The six-file replacement was committed by amending the unpublished sixth
  commit through active hooks. Exact implementation head is
  `3c4a40956e9d8ff82f7f809908da2f9f84e9e794`
  (`osctld: keep CPU limits on stable policy roots`). The commit message's
  longest line is 78 characters. No long VM was resumed before a fresh
  mandatory review.
- The full osctld suite on exact committed head `3c4a40956` passed all 1320
  examples with seed `4552`. The count is one lower than the intermediate
  run because the final amendment removed an unrelated retirement-routing
  example together with the rejected teardown-time implementation.

## Mandatory review of stable CPU policy roots

- Fresh standalone reviewer
  `/root/mandatory_stable_cpu_root_review_3c4a40956` reviewed exact head
  `3c4a40956e9d8ff82f7f809908da2f9f84e9e794`. It accepted the lifecycle
  reducer, generation fencing, recovery/quarantine model, stable-root CPU
  inheritance, unbounded production waits, vpsAdmin evidence path, and the
  overall architecture, but kept the long-VM gate closed with three Blocking
  upgrade/ordering findings.
- A running container adopted from old osctld could retain the legacy finite
  quota on its LXC-owned payload. The new daemon now reconciles the exact
  adopted run before monitoring resumes: it acquires the ordinary durable CPU
  policy lease, rechecks the exact adopted run ID, moves configured bandwidth
  to the stable osctld root, and makes the payload unlimited. Failure records
  an explicit rollback hazard and leaves lifecycle fenced or policy
  quarantined; stop and exact recovery remain available.
- The generic CPU transaction previously pinned residual generation roots but
  could expand a stable ancestor before releasing finite active/residual LXC
  descendants. A dedicated deepest-first release phase now makes active
  payloads and residual descendants unlimited below their stable/generation
  pins before any ancestor changes. A regression removes a payload during the
  release write and proves that the stable ancestor is not written.
- Raw LXC configuration could append `cpu.cfs_period_us`,
  `cpu.cfs_quota_us`, or `cpu.max` after generated configuration and recreate
  finite payload policy. These keys are now protected and rejected. Operators
  with such raw settings must remove them before upgrading; affected
  configurations are intentionally rejected when osctld next loads or
  generates them.
- Mixed-version VM coverage now starts a 250% container with legacy osctld,
  adopts it with new osctld, proves the legacy payload is unlimited before
  managed stop, starts a replacement, restricts the stable root to 201%, and
  confirms the replacement payload remains unlimited. The existing v2
  downgrade/re-upgrade case also proves adopted `cpu.max` is unlimited.
- The review packet's accidentally guessed expanded SHA was corrected to the
  actual exact `3c4a40956e9d8ff82f7f809908da2f9f84e9e794` everywhere in this
  state file. That reviewed head is preserved by local branch
  `2026-07-24-ct-start-hang-pre-legacy-cpu-reconciliation`.
- Focused cgroup/lifecycle configuration specs passed 141 examples with seed
  `4554`; the full osctld suite passed 1325 examples with seed `4555`.
  Repository-wide Overcommit passed Nixfmt and RuboCop. `git diff --check`,
  test-catalog evaluation, and direct cgroup-v1/v2 rendered-script Ruby
  parsing pass. Inspection of the latest v1 render found and corrected a
  test-only placement mistake so the 250% setup belongs to the legacy
  adoption fixture, not the manual-`lxc-start` fixture. No VM has been run on
  the uncommitted follow-up.
- The follow-up was committed by amending the unpublished sixth commit through
  active Nixfmt, RuboCop, and commit-message hooks. Exact implementation head
  is `c199309facd2bfb1de342240075dbf904d4c330e`; the vpsadminOS worktree is
  clean. The exact head requires a new standalone mandatory review before the
  four-VM gate can reopen.

## Mandatory review and adopted-policy lease race at `c199309fa`

- Fresh standalone reviewer
  `/root/mandatory_stable_cpu_adoption_review_c199309fa` accepted the overall
  architecture and every previously blocked stable-root, raw-key, residual,
  cgroup-v1/v2, recovery, compatibility, vpsAdmin, and commit-series area. It
  found no Important or Advisory issue, but kept the VM gate closed for one
  Blocking import race.
- Osctld serves commands while pools are importing, and a container is
  published before adopted CPU reconciliation. If another container or parent
  policy worker held the reducer lease, adoption failed to acquire it.
  `record_policy_hazard` then returned false while that worker was live; the
  worker could finish cleanly and erase its marker, leaving neither a retry
  nor a durable taint while the legacy payload remained finite.
- The correction does not wait for or time out the competing worker. Instead,
  the failed adoption hazard is appended atomically to the live policy-update
  record. Container and parent-policy completion must carry every pending
  hazard into a sticky local container-policy taint. A dead worker also
  preserves the pending hazards. If policy was already tainted, the new hazard
  is appended rather than replacing earlier evidence.
- Deterministic reducer regressions cover a live container cpuset lease and a
  live parent/group cpuset lease. Both workers finish successfully, yet the
  promoted adopted-CPU hazard remains visible with its target and rollback
  warning and blocks a new start. This is conservative: stop, finalization,
  and explicit recovery remain available, and no production wait or watchdog
  was added.
- The two new examples passed with seed `4557`; the final selected hazard
  examples passed 3/3 with seed `4560`. The standard focused CPU/configuration/
  lifecycle set passed 143 examples with seed `4558`. The full osctld suite
  passed 1327 examples with seeds `4559` and `4561`, before and after the final
  evidence-preservation refactor. Repository-wide Overcommit passes Nixfmt and
  RuboCop, and `git diff --check` passes.
- Running only `container/lifecycle_spec.rb` exposed an existing test-load
  dependency: three incarnation examples reference `OsCtld::ConfigError`
  without loading its definition. The normal focused/full sets load it and
  pass; the selected new examples also pass alone. The finding and workaround
  are recorded in
  `notes/vpsadminos/2026-07-27-isolated-lifecycle-spec-exceptions.md`.
- Rejected head `c199309facd2bfb1de342240075dbf904d4c330e` is preserved by
  local branch
  `2026-07-24-ct-start-hang-pre-adoption-policy-hazard-merge`. The two-file
  correction was amended through active hooks into exact head
  `1ced7a1439034a429f573106122d23224d38e0ea`. The worktree is clean; a new
  standalone review is still required before the VM gate can reopen.

## Exact-launch adoption hazard at `1ced7a143`

- Fresh standalone reviewer
  `/root/mandatory_adoption_hazard_review_1ced7a143` confirmed that ordinary
  container and parent policy completions correctly preserve pending adoption
  hazards, but found one Blocking exact-launch path and two Advisory evidence
  gaps. It found no other Important issue and continued to accept the broader
  architecture and both repository ranges.
- An adopted run can stop after adoption's exact-run precheck. A waiting
  `ct exec -r` is not gated on pool activation and can create a stopped
  execution generation with a launch-scope policy lease. Adoption can then
  fail its ordinary lease and append the finite-payload hazard to that launch
  marker, but `record_launch_policy` previously ignored pending hazards and
  could complete untainted.
- Ordinary and exact-launch completion now call the same reducer helper. The
  helper promotes a pending hazard when the worker itself rolled back safely,
  preserves prior taint and all structured hazards during reconciliation, and
  keeps the worker result as `last_reconciliation`. Parent completion uses the
  same durable hazard representation. Thus no policy-update scope can finish
  successfully by discarding an adopted finite-payload hazard.
- A directly installed first hazard is now also placed in the structured
  `pending_hazards` list. Deterministic tests cover successful ordinary,
  parent, and exact-launch workers, plus dead ordinary and dead parent workers.
  The promoted hazard blocks a new start while leaving stop/finalization and
  explicit recovery available. No wait, timeout, retry loop, or watchdog was
  added.
- All six selected hazard examples passed with seed `4562`; the focused
  CPU/configuration/lifecycle set passed 146 examples with seed `4563`.
  The full osctld suite passed 1330 examples with seed `4564`, and
  repository-wide Overcommit passes Nixfmt and RuboCop.
- Rejected head `1ced7a1439034a429f573106122d23224d38e0ea` is preserved by
  local branch `2026-07-24-ct-start-hang-pre-launch-policy-hazard-merge`.
  The two-file correction was amended through active hooks into exact head
  `19ac0d72ff5d17b849a6b80ff8619a33cf8d0c35`. The worktree is clean; another
  standalone review is required before the VM gate can reopen.

## Promoted-hazard crash retention at `19ac0d72`

- Fresh standalone reviewer
  `/root/mandatory_all_policy_hazards_review_19ac0d72f` accepted the
  exact-launch fix and all broader lifecycle, stable CPU-root, recovery,
  compatibility, vpsAdmin, and commit-series areas. It found no Important or
  Advisory issue, but kept the VM gate closed for one Blocking crash-evidence
  path.
- A directly promoted adoption hazard could already be the sticky policy
  taint when an ordinary reconciliation began. If that later policy worker
  died, the dead-worker path kept lifecycle admission blocked but replaced the
  previous policy record and discarded its structured `pending_hazards`
  evidence.
- Dead ordinary and launch policy workers now use the same completion helper
  as explicit ordinary and exact-launch completion. An already-promoted
  adoption hazard therefore remains in `pending_hazards`, its primary
  error/rollback evidence remains visible, and the worker disappearance is
  recorded independently as `last_reconciliation`.
- The exact already-tainted/dead-worker regression passed together with the
  two existing dead-worker cases: 3 examples, 0 failures, seed `4565`. The
  focused lifecycle/CPU-policy set passed 156 examples with seed `4566`; the
  full osctld suite passed 1331 examples with seed `4567`.
- Repository-wide Overcommit passed Nixfmt and RuboCop, and `git diff --check`
  passed. An initial amend attempt outside the active Nix shell was stopped by
  the mandatory hook because RuboCop and nixfmt were unavailable there. The
  amendment was then run inside the active development shell; pre-commit and
  commit-message hooks completed without bypass.
- The unpublished sixth commit was amended to exact head
  `1534b2d8b35d726ea2a4d78f6b365e0072b9af73`. The first five commits are
  unchanged, the vpsadminOS worktree is clean, and the strict VM gate remains
  closed pending one fresh standalone review of this exact committed head.
- Fresh standalone reviewer
  `/root/mandatory_promoted_hazard_review_1534b2d8b` reviewed exact
  vpsadminOS head `1534b2d8b35d726ea2a4d78f6b365e0072b9af73`
  and provisional vpsAdmin head
  `53c0f74e8e698f24611261194f42d9d2d5a93421`. It reported no Blocking or
  Important findings and cleared the strict long-VM gate.
- The reviewer accepted all ordinary, parent, and exact-launch live/dead
  policy exits, sticky admission fencing, stop/recovery availability,
  stable-root CPU policy, upgrade adoption, compatibility, and commit
  separation. Its sole Advisory is that there is no direct combined regression
  for a pending adoption hazard followed by an exact-launch worker death.
  This is accepted for this change because launch and ordinary dead workers
  now enter the same tested `complete_policy_update_locked` path; inspection
  confirmed that it retains the hazard and taint. The existing launch success,
  ordinary death, and already-tainted ordinary death cases exercise the
  distinct boundaries.
- Residual test limitations remain crash/power-loss coverage at every
  persistence boundary and the intentional need for exact operator recovery
  after an unrecoverable unbounded worker or kernel stall. Neither is changed
  into a production timeout or watchdog.

## Exact-head strict VM verification

- On exact vpsadminOS head
  `1534b2d8b35d726ea2a4d78f6b365e0072b9af73`,
  `./test-runner.sh test osctld/restart` passed all 8 examples in 389.12
  seconds. This includes the original in-container reboot racing an external
  start, which converged on one replacement generation, plus graceful/abrupt
  daemon restart and local-copy cleanup cases.
- The first `osctld/lifecycle` attempt passed manual-launch rejection,
  unkillable residual quarantine/disjoint replacement, and stopped-execution
  cpuset handling, then failed its downgrade/re-upgrade example after 347.04
  seconds. The retained artifact is
  `/tmp/os-test-runner/os-test-osctld__lifecycle-000573c0`.
- The failure was investigated before rerun. The daemon log proved adopted CPU
  reconciliation successfully wrote the legacy LXC-owned `cpu.max` from
  finite `250000` to `max`. The original assertion nevertheless failed with
  `ENOENT`.
- A first attempted correction generalized the assertion to the durable
  invariant, but retained the same malformed mount path and failed again after
  all other examples passed. The second failure output exposed the exact cause:
  lifecycle resources are relative (`osctl/...`), while the test concatenated
  them as `/sys/fs/cgrouposctl/...` without a separating slash. The daemon had
  correctly written `/sys/fs/cgroup/osctl/...`; no cgroup or controller
  interface had disappeared.
- The corrected v2 compatibility assertion uses
  `/sys/fs/cgroup/<resource>`, proves the osctld-owned stable root retains
  `250000`, and proves every descendant `cpu.max` interface still observable
  is locally unlimited. The later cgroup-v1 VM remains responsible for the
  stronger invisible-scheduler-object regression by restricting the
  replacement stable root to `201000`. Overcommit passed Nixfmt and RuboCop
  after the initial test correction; hooks will be rerun after the final path
  fix.
- With the explicit separator, `osctld/lifecycle` passed all 4 examples in
  444.39 seconds. The examples ran in a third randomized order and covered
  manual-launch rejection, unkillable residual quarantine/disjoint
  replacement, stopped-execution cpuset handling, and drained
  downgrade/re-upgrade adoption.
- The test-only correction was amended through active Nixfmt, RuboCop, and
  commit-message hooks into unpublished exact head
  `40a6be692bd3a9188ef68b43c9cd1d3cc6ca9cf9`. The first five commits remain
  unchanged, `git diff --check` passes, and the worktree is clean. The earlier
  restart result exercised identical runtime code, but the strict four-VM
  sequence will be restarted after fresh mandatory review so every recorded
  final result is tied to the same exact commit.
- Fresh standalone reviewer
  `/root/mandatory_lifecycle_path_review_40a6be692` reviewed exact head
  `40a6be692bd3a9188ef68b43c9cd1d3cc6ca9cf9`. It found no Blocking,
  Important, or new Advisory issue and cleared the strict four-VM sequence
  from the beginning.
- The review independently verified that the amendment is test-only, the first
  five commits are unchanged, the absolute path is safely shell-escaped,
  `-mindepth 2` excludes only the stable root's own `cpu.max`, and every
  observable descendant accepts both cgroup-v2 unlimited forms (`max` and
  `max <period>`). It accepted the existing exact-launch/dead-worker coverage
  advisory on the same shared-helper basis as the previous review.
- Final exact-head sequence, VM 1:
  `./test-runner.sh test osctld/restart` passed all 8 examples in 404.58
  seconds on `40a6be692bd3a9188ef68b43c9cd1d3cc6ca9cf9`.
  The original in-container reboot/concurrent external start case again
  converged on one replacement generation.
- Final exact-head sequence, VM 2:
  `./test-runner.sh test osctld/lifecycle` passed all 4 examples in 326.82
  seconds. It covered the corrected drained downgrade/re-upgrade adoption
  invariant, stopped-execution cpuset, unkillable residual quarantine and
  disjoint replacement, and rejection of unmanaged `lxc-start`.
- Final exact-head sequence, VM 3:
  `./test-runner.sh test 'kernel/vpsadminos#cpu-view-cgroups-v1'` passed all
  158 examples. The script completed in 1164.03 seconds and the full
  two-machine test completed in 1239.13 seconds. Critical cases passed for
  failed-start payload cleanup, legacy finite-payload adoption and
  neutralization, managed 250% to 201% narrowing, stable-root restart
  persistence, cgroup-v1 ancestor/descendant ordering, inherited group limits,
  and the full CPU-view/cpuset matrix.
- Final exact-head sequence, VM 4 initially ran all 157 cgroup-v2 examples and
  passed 156. Example 26, `Configured group CPU bandwidth hierarchy
  reconstructs only the requested path for stopped execution`, expected the
  persisted stopped sibling group to be locally unlimited but observed its
  configured 200% policy. The script completed in 1270.27 seconds and the
  full two-machine test in 1360.22 seconds. The retained artifact is
  `/tmp/os-test-runner/os-test-kernel__vpsadminos-f1b75a4a`.
- The failed attempt was investigated before rerun. Cgroup v2's unified
  hierarchy causes the device-BPF configurator to recreate all persisted group
  cgroups during daemon import, including the stopped sibling, but its local
  CPU policy initially remains unlimited. Before requesting a stopped
  execution generation, `Runscript::Frontend#with_execution_mode` explicitly
  invokes `Group::CGParamApply` with `only_policies`. The
  `GroupCpuBandwidthPolicy` transaction intentionally scans the anchored group
  and all existing descendants so that ancestor/descendant ordering stays
  valid. It therefore applies the stopped sibling's configured 200% policy on
  v2. Cgroup v1 has a separate CPU hierarchy, so the absent sibling is not
  reconstructed by that transaction and remains absent. The later cgroup-v2
  start/restart, ordering, wider-child, and inheritance examples all passed.
- The first corrected cgroup-v2 rerun reached example 26 after 25 passes and
  disproved an interim assumption that the 200% value existed before stopped
  execution: the live shell transcript read `max 100000` immediately before
  the command. That already-invalid run was stopped after example 37. A second
  attempted synchronization waited for an independent import-time CPU-policy
  apply which does not exist; it timed out after 120 seconds and that
  already-invalid run was stopped after example 31. Both failures were
  investigated before another rerun.
- The test now states the actual per-hierarchy invariant: on cgroup v2, require
  the existing stopped sibling to be locally unlimited before execution and
  require the explicit subtree transaction to apply its configured 200%
  policy; on cgroup v1, require the sibling CPU cgroup to remain absent before
  and after execution. This is a test-only semantic correction and does not
  change osctld runtime behavior. `git diff --check` and repository-wide
  Nixfmt and RuboCop hooks pass.
- The third full cgroup-v2 rerun passed all 157 examples. The corrected
  configured-subtree example passed in 5.74 seconds, the script completed in
  1138.94 seconds, and the full two-machine test completed in 1225.74 seconds.
  The sixth commit was amended through active Nixfmt, RuboCop, and
  commit-message hooks to exact unpublished head
  `15a4599f009dfd92ed78622db14f4c8c2335cc3c`; the worktree is clean and the
  first five commits are unchanged. The first amend invocation intentionally
  caught an unstaged test correction in its post-commit status; only after
  staging that exact file was the candidate amended and accepted. A fresh
  standalone mandatory review is pending. Because the exact SHA changed, the
  strict four-VM exact-head sequence will then restart from the beginning.
- Immediately before the final review gate, both upstreams were fetched over
  SSH. `origin/staging` for vpsadminOS remains
  `4476942c4e33092e20e4faa91f32dfcca9a3ea7d`, `origin/master` for vpsAdmin
  remains `eb2ccde5cd709a42a802589419ba8cf525c97f34`, and each remains an
  ancestor of its feature head. No rebase or source change is required.
- Fresh standalone reviewer
  `/root/mandatory_cgv2_semantics_review_15a4599f0` independently confirmed
  that the corrected cgroup-v2 expectation matches the implementation and
  does not mask a runtime or transient tenant-policy flaw. It accepted the
  lifecycle reducer, exact generation/effect ownership, manual-LXC rejection,
  console/process fencing, stable CPU roots, transactional cgroup policy,
  adoption, quarantine, disjoint replacement, recovery, and compatibility
  design.
- The reviewer nevertheless kept the long-VM gate closed on commit-series
  integrity: the group-policy assertion belonged in the fifth group-policy
  commit where both the test context and transaction were introduced, not in
  the sixth stable-root commit. It also reiterated that the vpsAdmin flake pin
  must be rewritten from its provisional revision after the final OS head is
  pushed. The latter does not block the OS-only VM sequence.
- The reviewed pre-fold tree is preserved at local backup branch
  `2026-07-24-ct-start-hang-pre-cgv2-test-fold`. The first rebase invocation
  was refused by the active pre-rebase hook because its ambient shell lacked
  the Overcommit gem; it changed no history. Repeating the operation with the
  prepared Nix/Ruby gem environment ran the hook without bypass.
- The cgroup-v2 test correction and its matching commit-message clarification
  were folded into rewritten group-policy commit
  `cc57de8fbea43abeb3ec2393088b2c2f46dc39cf`; blame attributes the corrected
  assertions to that commit. The stable-root commit was rebuilt and amended
  through active hooks as exact unpublished head
  `8a5257de8ed23e3fb8b34c92ce8588135b6d7711`.
- `git diff --exit-code
  2026-07-24-ct-start-hang-pre-cgv2-test-fold..HEAD` proves the rewritten
  final tree is byte-identical to the reviewed pre-fold tree. The focused
  group CPU policy, container policy, group command, and stopped-execution
  runscript set passed 87 examples with seed `4568`; repository-wide Nixfmt
  and RuboCop passed both before and during the final amendment. The worktree
  is clean. A new standalone mandatory review of the rewritten exact series
  remains required before the strict four-VM sequence restarts.
- The standalone-agent thread limit prevented allocating an entirely new
  reviewer process after the fold, so an earlier mandatory reviewer which did
  not perform the immediately preceding cgroup-v2 review was reactivated with
  a complete exact-head packet and an instruction to perform a new full-range
  audit rather than inherit its earlier conclusions.
- That independent re-audit reported no Blocking or Important findings and
  cleared exact head `8a5257de8ed23e3fb8b34c92ce8588135b6d7711`
  for the strict four-VM sequence. It independently verified the range-diff,
  fifth-commit blame and rationale, byte-identical final tree, lifecycle and
  recovery authority, policy journals/leases/rollback, adoption/quarantine,
  compatibility, and vpsAdmin evidence parsing.
- The only retained Advisory is the already documented lack of a direct
  combined pending-adoption-hazard plus exact-launch-worker-death example.
  Both branches converge on the same tested durable completion helper, so the
  reviewer accepted it as non-gating. Exhaustive crash/power-loss injection at
  every persistence boundary remains follow-up hardening. The vpsAdmin pin is
  still a final delivery gate, not a blocker for the OS-only VM sequence.
- Final exact-head sequence on
  `8a5257de8ed23e3fb8b34c92ce8588135b6d7711`, VM 1:
  `./test-runner.sh test osctld/restart` passed all 8 examples and the
  single-machine test completed in 461.15 seconds. The original in-container
  reboot racing an external start converged on one replacement generation;
  graceful and abrupt daemon restart, idle clients, active start/restart, and
  local-copy cleanup ownership also passed.
- Final exact-head sequence, VM 2:
  `./test-runner.sh test osctld/lifecycle` passed all 4 examples and the
  single-machine test completed in 460.77 seconds. It proved rejection of
  unmanaged `lxc-start`, drained downgrade/re-upgrade legacy adoption,
  cpuset-constrained stopped execution, and quarantine of an unkillable
  residual generation followed by replacement in a disjoint generation
  cgroup.
- Final exact-head sequence, VM 3:
  `./test-runner.sh test 'kernel/vpsadminos#cpu-view-cgroups-v1'` passed all
  158 examples. The script completed in 1332.47 seconds and the full
  two-machine test completed in 1384.92 seconds. It passed the legacy
  finite-payload adoption/neutralization regression, failed-start payload
  cleanup, stable-root persistence and 250% to 201% restriction after restart,
  v1 group hierarchy reconstruction/ordering/inheritance, and the complete
  CPU-view/cpuset matrix.
- Final exact-head sequence, VM 4:
  `./test-runner.sh test 'kernel/vpsadminos#cpu-view-cgroups-v2'` passed all
  157 examples. The corrected existing-subtree group-policy example passed in
  5.64 seconds, the script completed in 1157.94 seconds, and the full
  two-machine test completed in 1223.13 seconds. Persisted/stable-root CPU
  policy, failed-start cleanup, unified hierarchy reconstruction, v2
  ancestor/descendant ordering, wider-child semantics, inheritance, and the
  full CPU-view/cpuset matrix all passed.
- The strict four-VM sequence on exact head
  `8a5257de8ed23e3fb8b34c92ce8588135b6d7711` is complete and green in the
  required order, with no VMs run in parallel.
- After a final SSH fetch confirmed `origin/staging` was unchanged and the
  published feature branch still exactly matched leased old head
  `f7102f1d03200310a4449bd181770625bd5a61e4`, vpsadminOS was force-pushed
  only to `refs/heads/2026-07-24-ct-start-hang` with an explicit
  force-with-lease. GitHub accepted exact pushed head
  `8a5257de8ed23e3fb8b34c92ce8588135b6d7711`.
- Exact-head vpsadminOS workflow runs started as:
  - RSpec `30239730029`;
  - RuboCop `30239729995`;
  - CI `30239729966`.
  No superseded queued or in-progress run existed. RuboCop and RSpec have
  completed successfully; CI remains in progress.
- The required `tools/update_vpsadminos_flake.sh` updated vpsAdmin's
  `flake.lock` from provisional OS revision `f7102f1d0` to exact pushed
  revision `8a5257de8`. Its generated commit was initially stopped by
  Overcommit because the new flake closure changed the custom
  `VpsadminApiI18n` hook signature. The staged change contained only
  `flake.lock` and metadata resolved the exact requested revision.
- Following the repository's documented recovery, the hook was inspected,
  signed, and run in the same new root Nix shell. Migration specs, WebUI/API
  i18n, Nixfmt, RuboCop, and PHP CS Fixer all passed. The updater's generated
  `f7102f1d0 -> 8a5257de8` commit then passed the same commit-time hooks.
- The final updater delta was folded into the earlier provisional pin and the
  separate Playwright repair replayed on top. Final vpsAdmin history is:
  - `e8c79b34315b2bea63998412ca1300670754ba8c`
    `libnodectld: retain VPS recovery cleanup evidence`;
  - `c457da3cf2c56b6f43d07ac2092b546454a16ce4`
    `flake: vpsadminos 736f68939 -> 8a5257de8`;
  - `fc2c413871e8d9c7a33dabafd7fbd91e747e3444`
    `tests: package WebUI version for Playwright`.
- Backup branch `2026-07-24-ct-start-hang-pre-final-vpsadmin-pin` preserves
  the temporary four-commit state at `1c8bde6163`. The final three-commit tree
  is byte-identical to that backup, the worktree is clean, flake metadata
  resolves exact OS revision `8a5257de8ed23e3fb8b34c92ce8588135b6d7711`,
  and `git diff --check` passes.
- Exact final-head repository-wide vpsAdmin Overcommit passed migration specs,
  WebUI/API i18n, Nixfmt, RuboCop, and PHP CS Fixer. The updated test catalog
  evaluated successfully and listed all 18 `webui#*` Playwright scripts,
  including `webui#navigation-readonly`.
- The targeted final-head `webui#navigation-readonly` integration run passed.
  Its Playwright example completed in 172.56 seconds, the script completed in
  500.9 seconds, and the full test completed successfully in 746.91 seconds.
  The browser suite consumed the packaged version metadata added by
  `fc2c413871e8d9c7a33dabafd7fbd91e747e3444`.
- A final SSH fetch confirmed `origin/master` was still
  `eb2ccde5cd709a42a802589419ba8cf525c97f34`, remained an ancestor of the
  vpsAdmin feature head, and the published feature branch still exactly
  matched leased provisional head `f294ee455a82cc02985784a08504b4ed74e0f9e5`.
  The branch was then force-pushed only to
  `refs/heads/2026-07-24-ct-start-hang` with an explicit force-with-lease.
  GitHub accepted exact vpsAdmin head
  `fc2c413871e8d9c7a33dabafd7fbd91e747e3444`.
- Exact-head vpsAdmin workflows started as:
  - libnodectld Specs `30241171022`;
  - i18n health `30241171009`;
  - RuboCop `30241170999`;
  - Webui PHPUnit `30241171004`;
  - Client Specs `30241171011`;
  - CI `30241170989`.
  All six are initially in progress. No superseded queued or in-progress
  vpsAdmin run exists, so there is nothing to cancel.
- Exact-head i18n health run `30241171009` failed in its API job while the
  WebUI job passed. Its failed-step log showed that a fresh bundle resolved
  HaveAPI 0.29.8 and its strict documentation validator rejected
  `Location::Index` example #1 because `created_at` and `updated_at` were not
  declared output parameters. The run produced no artifacts. This was
  investigated before any rerun.
- Local hooks had passed because the ignored `api/Gemfile.lock` retained
  HaveAPI 0.29.6. A clean runner has no such lock and the existing
  `~> 0.29.6` constraint resolves 0.29.8. A separate unmerged feature branch
  already carries commit `9ad43e4ec190298cd0a97550f94f27848919bf01`
  correcting both stale examples exposed by the stricter validator. The same
  two-file correction was applied byte-for-byte here: Location timestamps
  outside its declared output were removed and the IP address example was
  aligned with its declared network-interface, network, and prefix fields.
- After moving the ignored 0.29.6 lock out of resolution, the exact CI command
  resolved HaveAPI and haveapi-client 0.29.8, created a fresh MariaDB test
  database, and `bundle exec rake vpsadmin:i18n:health` passed.
- Repository-wide Overcommit then passed MigrationSpecs, WebUI/API i18n,
  Nixfmt, RuboCop, and PHP CS Fixer with the locally resolved 0.29.8 bundle.
  Commit-time hooks repeated the relevant checks successfully. The focused
  correction is committed as
  `e0407c301c53112f6ebb92cc8005605561eef7bb`
  (`api: correct location and address examples`); its message respects the
  workspace's 80-column limit, `git diff --check` passes, and the vpsAdmin
  worktree is clean.
- A fresh standalone mandatory review was started for this post-CI code
  correction before it is published. The prior exact-head libnodectld Specs,
  RuboCop, Client Specs, and Webui PHPUnit runs passed; its i18n failure is
  superseded by the local correction, while its long CI remains active until a
  reviewed replacement head is pushed.
- Fresh standalone reviewer
  `/root/mandatory_vpsadmin_i18n_ci_fix_review` cleared exact vpsAdmin head
  `e0407c301c53112f6ebb92cc8005605561eef7bb` with no Blocking or Important
  findings. It independently confirmed the failing log and clean dependency
  resolution, declared-schema alignment, stable patch identity and blob
  identity with `9ad43e4ec`, focused commit ownership, unchanged OS pin, and
  absence of runtime/API-contract, persistence, authorization, lifecycle, or
  rollback impact.
- The reviewer found no need to repeat browser, VM, or lifecycle integration
  testing for the metadata-only fourth commit. Its only advisories were to
  refresh the tracking summary, use a normal fast-forward push (or an explicit
  lease against `fc2c41387`), record the final outcome, and cancel prior-head
  CI run `30241170989` if it remains live after replacement.
- vpsAdmin head `e0407c301c53112f6ebb92cc8005605561eef7bb` was
  fast-forward pushed. Exact-head RuboCop run `30242103097` and i18n health
  run `30242103129` passed; API Specs run `30242103131` and CI run
  `30242103111` remain in progress. Superseded long CI run `30241170989` on
  `fc2c41387` was cancelled and is terminal.
- vpsadminOS CI run `30239729966` completed with failure after its build/cache
  job and 74 of 76 integration groups passed. The complete
  `os-test-logs-30239729966` artifact was downloaded to
  `/tmp/vpsadminos-ci-30239729966` and inspected before any rerun.
- The artifact proves two independent defects. First,
  `kernel/vpsadminos#memory-view-cgroups-v2` aborted the initial
  `kmemv2-mem512` start in `CtPreStart`: the stable-root `memory.max` and
  `memory.swap.max` writes succeeded, then `ContainerParams` attempted
  `runs/<generation>/user-owned/payload/memory.max` before LXC had created
  and delegated its payload hierarchy. This came from treating a preparing
  lifecycle generation as payload-runtime-active.
- Second, the CPU-view scripts intentionally stop, replace, and restart
  `osctld` while `kernel/vpsadminos` runs six scripts concurrently against
  the same cgroup-v1 and cgroup-v2 machines. Sibling uptime, tmpfs, loadavg,
  memory, and OOM scripts consequently observed a missing
  `/run/osctl/osctld.sock` or transient start failures. The test runner has a
  per-test `testScriptJobs` limit but no per-script exclusivity primitive.
- The pending runtime correction distinguishes the preparing generation from
  an existing LXC payload. Stable-root, cpuset, and CPU-bandwidth policy
  writes still occur during exact pre-start, while ordinary payload mirroring
  and resets require `owner.running?`. A focused
  `ContainerParams` regression passes as part of 25 examples and proves that
  pre-start writes `memory.max` only to the stable root.
- The pending test correction moves both complete CPU-view scripts to a
  dedicated `kernel/vpsadminos-cpu-view` group with its own cgroup-v1 and
  cgroup-v2 machines. Test discovery lists 12 non-CPU scripts under
  `kernel/vpsadminos` and only the two CPU scripts under the isolated group.
  All three edited Nix expressions parse successfully. The cgroup-v2
  memory-view VM is now running as the direct regression gate.
- The direct local
  `kernel/vpsadminos#memory-view-cgroups-v2` regression passed all 262
  examples. The script completed in 671.17 seconds and the full
  two-machine test completed in 800.28 seconds. This proves that limited
  containers now pass pre-start and that stable-root enforcement still
  produces the expected in-container `/proc/meminfo`, `/proc/swaps`, and
  `sysinfo()` views.
- Repository-wide Overcommit passed Nixfmt and RuboCop. The initial commit
  attempt from the ambient shell was correctly refused because RuboCop was
  not on that shell's path; it made no commit. Both final commits were made
  from the prepared Nix/Ruby shell through active pre-commit and commit-msg
  hooks:
  - `7cd833a94c6d1b33f27ab4fc691c809554c5af3b`
    `osctld: wait for LXC payload before mirroring limits`;
  - `9b1a9837f22b629882dc43c321a9873dbfc89198`
    `tests: isolate osctld-disrupting CPU view coverage`.
  The first contains only the production phase correction and direct spec;
  the second contains only the test-group/machine isolation. The vpsadminOS
  worktree is clean and exact head is two commits ahead of the published
  `8a5257de8` branch.
- Fresh standalone reviewer `/root/mandatory_os_ci_followup_review` was
  launched with the complete exact-head packet. The remaining long local VM
  gates will not start until that review is resolved.
- Exact vpsAdmin head `e0407c301` API Specs run `30242103131` completed
  successfully. Its RuboCop, i18n health, and API Specs workflows are now
  green; long CI run `30242103111` remains in progress and will become
  superseded when the final reviewed OS revision is pinned.
- Fresh standalone mandatory reviewer
  `/root/mandatory_os_ci_followup_review` cleared exact vpsadminOS head
  `9b1a9837f22b629882dc43c321a9873dbfc89198` with no Blocking,
  Important, or Advisory findings. It confirmed that ordinary payload
  mirroring now uses the correct LXC phase boundary on cgroup v1 and v2,
  live updates/resets remain strict, stable-root start-time enforcement and
  launch-fenced CPU/cpuset policy are unchanged, and no lifecycle reducer,
  recovery, authorization, persistence, or production timeout path changed.
- The reviewer also confirmed that the dedicated CPU-view group preserves
  both full scripts, keeps the legacy daemon package only on its cgroup-v1
  machine, retains loadavg configuration in the non-CPU group, and introduces
  no production watchdog. The two follow-up commits are independently
  reviewable and correctly split by the two CI causes.
- Publication remains conditional on three serial exact-head local gates:
  `dist-config/systemd-rundir-limits`, which was another artifact failure
  through a stopped-execution generation; complete `kernel/vpsadminos`, which
  covers cgroup-v1 memory starts and non-CPU concurrency; and complete
  `kernel/vpsadminos-cpu-view`, which validates the new dedicated test and
  both machines. The acceptance-critical lifecycle suites already passed on
  `8a5257de8`, and the reviewer found these two commits do not modify their
  implementation paths.
- The first `dist-config/systemd-rundir-limits` attempt passed its cgroup-v1
  machine, but failed deterministically on cgroup v2 when
  `osctl ct unset memory cgv2-testct` returned
  `no runtime reset value is known for memory.swap.max`. The complete
  attempt logs and failure diagnostics in
  `/tmp/os-test-runner/os-test-dist-config__systemd-rundir-limits-b86f20e1`
  were inspected before rerunning.
- The failure exposed an older reset-table omission through the new strict
  transaction. `osctl ct set memory` configures both `memory.max` and
  `memory.swap.max`, but `CGroup::Params#reset_value` only knew the unlimited
  value for `memory.max`. Earlier code silently removed the saved swap
  parameter without restoring the live cgroup value; strict validation
  correctly prevented that partial transaction.
- `memory.swap.max` now resets to the kernel's unlimited value, `max`. A
  direct stopped-container regression proves that transactional unset writes
  the stable root, does not look for a nonexistent LXC payload, removes the
  saved parameter, and persists only after the runtime transaction succeeds.
  The focused `ContainerParams` spec passes all 26 examples.
- The corrected `dist-config/systemd-rundir-limits` rerun passed both
  cgroup-version machines and completed successfully in 555.85 seconds. It
  covers stopped execution with no memory limit, configured container memory,
  successful v2 swap-limit reset, and default/root group memory limits.
- Repository-wide Overcommit passed Nixfmt and RuboCop, and the commit-time
  pre-commit and commit-message hooks passed. The focused correction is
  committed separately as
  `4734807f7` (`osctld: reset cgroup v2 swap limits transactionally`).
  Because this production correction was discovered after the previous
  mandatory review, a fresh standalone review is required before the two
  remaining long VM gates and publication.
- Fresh standalone mandatory reviewer
  `/root/mandatory_swap_reset_review` cleared exact vpsadminOS head
  `4734807f77a198bc31a4dda9590eb8277e4dc009` with no Blocking, Important,
  or Advisory findings. It independently checked the exact pinned kernel's
  documentation and implementation: `max` is the default/unlimited value for
  `memory.swap.max`, and expanding to it has no invalid hierarchy-order
  constraint.
- The reviewer confirmed the regression models a stopped container with an
  extant osctld-owned stable root, performs exactly the stable
  `memory.swap.max=max` write with no payload access, removes the staged
  parameter, and persists once. Runtime reset still precedes persistence;
  failures restore both saved parameters and live/config state through the
  existing transaction rollback.
- No lifecycle fencing, authorization, manual-LXC rejection, recovery,
  quarantine, generation-root, unkillable-task handling, wait, timeout,
  persisted-format, or protocol behavior changed. Rolling deployment and the
  documented drained-downgrade restriction remain unchanged. The reviewer
  found the separate follow-up justified because the omission was discovered
  after the earlier OS head had already been published.
- Gate disposition is to proceed serially on this exact head with complete
  `kernel/vpsadminos`, followed by complete
  `kernel/vpsadminos-cpu-view`. Publication remains conditional on both.
- The bare `./test-runner.sh test kernel/vpsadminos` selector selected zero
  script-level paths and therefore produced no test evidence. Test discovery
  confirmed 12 paths under `kernel/vpsadminos#*` and two paths under
  `kernel/vpsadminos-cpu-view#*`; the quoted wildcard form is required for a
  complete multi-script group.
- `./test-runner.sh test 'kernel/vpsadminos#*'` then ran all 12 non-CPU
  scripts together against the group's dedicated cgroup-v1 and cgroup-v2
  machines. The complete group passed in 1843.68 seconds. Both 270-example
  tmpfs scripts passed in 1251.39 and 1256.43 seconds, cgroup-v1 memory view
  passed all 262 examples in 550.23 seconds, and loadavg passed all 135
  examples in 1768.7 seconds. The remaining memory, OOM, uptime, syslog
  namespace, proc, attrs, mknod, and nice coverage also completed
  successfully.
- Crucially, the concurrent non-CPU scripts saw no missing osctld socket or
  daemon transition. This validates that moving the osctld-disrupting CPU
  view scripts out of the shared group fixes the CI isolation defect without
  serializing or dropping the non-CPU concurrency coverage.
- `./test-runner.sh test 'kernel/vpsadminos-cpu-view#*'` selected exactly the
  two complete CPU-view scripts and ran them against the dedicated cgroup-v1
  and cgroup-v2 machines. The complete isolated group passed in 1380.71
  seconds. Cgroup v2 passed all 157 examples in 1277.3 seconds and cgroup v1
  passed all 158 examples in 1317.58 seconds.
- The isolated gate passed legacy finite-payload adoption/neutralization,
  daemon reconstruction, failed-start LXC payload cleanup, stable persisted
  CPU bandwidth across managed restart, ancestor-first expansion,
  descendant-first restriction, wider-child and inheritance semantics,
  dynamic/disjoint cpuset transactions, fractional and sub-CPU limits,
  affinity, and limit expansion/unset on both cgroup versions.
- All three reviewer-required exact-tree VM gates are now green in serial
  order on committed head
  `4734807f77a198bc31a4dda9590eb8277e4dc009`:
  `dist-config/systemd-rundir-limits`, complete non-CPU
  `kernel/vpsadminos#*`, and complete isolated
  `kernel/vpsadminos-cpu-view#*`.
- The required pre-push SSH fetch found that `origin/staging` advanced from
  `4476942c4` to `23cf4fc36` through one automated
  `flake: update nixpkgs, nixpkgsUnstable` commit. It changes only
  `flake.lock`; no feature-owned path overlaps. Exact upstream commit
  `23cf4fc36f15ce510c63b5134f4ea8038b706e31` has a successful
  `Build all kernel versions` workflow run `30243310398`.
- Local backup branch
  `2026-07-24-ct-start-hang-pre-staging-23cf4fc36` preserves fully reviewed
  and tested head `4734807f77a198bc31a4dda9590eb8277e4dc009`.
  The nine feature commits were rebased cleanly onto current staging, creating
  new exact head `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`.
- `git range-diff` maps all nine old/new feature commits exactly. Every
  non-lock file is byte-identical to reviewed head `4734807f7`; the
  `flake.lock` delta has the same SHA-256 as the upstream
  `4476942c4..23cf4fc36` patch, and the rebased worktree is clean.
  The mandatory application-code reviews therefore remain applicable; the
  new base is a dependency-only mechanical update. Exact-rebased-tree hooks,
  focused specs, and the three serial VM gates will nevertheless be repeated
  before publication.
- Exact-rebased-tree Overcommit passed Nixfmt and RuboCop. The focused
  `ContainerParams` spec passed all 26 examples under the updated development
  closure.
- The first rebased `dist-config/systemd-rundir-limits` attempt failed during
  Nix evaluation/build after 39.81 seconds, before any VM or test assertion.
  Its complete build log was inspected before rerunning. `gem build` found
  cached dependency gemspecs below `osctld/.gems` and rejected Bundler's
  incomplete cached file list.
- The focused-spec invocation had entered `nix develop` from `osctld/`, while
  the shell sets `GEM_HOME="$(pwd)/.gems"`. This created a 19 MiB ignored
  `osctld/.gems` cache that Nix then included in the osctld source. After
  confirming it was ignored and contained no tracked file, the generated
  cache was moved recoverably to `/tmp/osctld-gems.VDbFAt/.gems`. No code or
  dependency change is involved. The reusable trap is documented in
  `notes/vpsadminos/2026-07-27-subdirectory-gems-nix-source.md`.
- With the worktree source clean, the identical exact-rebased
  `dist-config/systemd-rundir-limits` rerun passed both cgroup versions in
  603.6 seconds. Cgroup v2's `ct set memory`, stopped execution, and
  `ct unset memory` all returned successfully under the updated dependency
  closure.
- The complete exact-rebased `kernel/vpsadminos#*` group passed all 12
  non-CPU scripts in 2040.69 seconds under the updated dependency closure.
  Loadavg passed all 135 examples in 1415.88 seconds; both memory views,
  both tmpfs matrices, uptime, syslog namespace, OOM, proc, attrs, mknod, and
  nice also completed. No concurrent script observed osctld disruption.
- The exact-rebased isolated `kernel/vpsadminos-cpu-view#*` group passed in
  1390.77 seconds. Cgroup v2 passed all 157 examples in 1277.48 seconds and
  cgroup v1 passed all 158 examples in 1326.74 seconds. Legacy adoption,
  reconstruction, failed-start cleanup, ordered hierarchy transactions,
  restart persistence, dynamic cpusets, fractional/sub-CPU limits, affinity,
  and limit expansion/unset all remain green under the updated dependency
  closure.
- Exact rebased head
  `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44` has therefore passed the
  complete serial publication sequence locally after the dependency rebase:
  hooks, focused spec, dual-version stopped-execution memory gate, complete
  12-script non-CPU group, and complete two-script isolated CPU-view group.
- A final SSH fetch confirmed `origin/staging` remained
  `23cf4fc36f15ce510c63b5134f4ea8038b706e31` and the remote feature branch
  still matched the expected leased old head `8a5257de8`. The feature branch
  was force-updated only with an explicit lease after the permitted rebase.
  GitHub accepted exact published vpsadminOS head
  `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`; local and remote refs match.
- Exact-head vpsadminOS workflows started as:
  - RSpec `30256514274`;
  - RuboCop `30256514441`;
  - CI `30256514753`.
  All three are initially in progress.
- The repository-provided vpsAdmin pin updater changed the vpsadminOS input
  from `8a5257de8` to exact published head `9b88a3903` and refreshed the
  followed Nix inputs from that OS revision. Its Nixfmt, migration-spec,
  WebUI-i18n, API-i18n, subject, trailing-period, and text-width hooks all
  passed. It created the generated, dependency-only commit
  `6f4e7de8fb90e03192867f1e56c8f454f6b7327f`.
- The generated commit changes only `flake.lock`, whose vpsadminOS metadata
  resolves to `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`.
  A final SSH fetch found unchanged vpsAdmin `origin/master`
  `eb2ccde5cd709a42a802589419ba8cf525c97f34` and remote feature head
  `e0407c301c53112f6ebb92cc8005605561eef7bb`; both are ancestors of the
  clean local head.
- vpsAdmin accepted the normal fast-forward SSH push to exact final head
  `6f4e7de8fb90e03192867f1e56c8f454f6b7327f`; local and remote feature refs
  match. Exact-head workflows started as CI `30256755962`, Webui PHPUnit
  `30256755964`, Client Specs `30256756051`, libnodectld Specs
  `30256756059`, and i18n health `30256755997`.
- The superseded vpsAdmin CI run `30242103111`, which targets prior head
  `e0407c301`, was still in progress after the final-pin push. Its cancellation
  was requested in accordance with the workspace rule. Other superseded-head
  workflows were already successful. Only final-head runs are publication
  evidence from this point.
- Superseded run `30242103111` subsequently reached terminal `cancelled` state
  on the expected prior head; no current-head workflow was cancelled.
- On initial final-head inspection, vpsadminOS RuboCop `30256514441` is
  successful while RSpec `30256514274` and CI `30256514753` remain in
  progress. All five final-head vpsAdmin workflows are initially in progress.
- Final-head vpsadminOS RSpec `30256514274` completed successfully. Final-head
  vpsAdmin Webui PHPUnit `30256755964`, Client Specs `30256756051`,
  libnodectld Specs `30256756059`, and i18n health `30256755997` also
  completed successfully. The only remaining runs are the exact-head
  vpsadminOS CI `30256514753` and vpsAdmin CI `30256755962`.
- Final-head vpsadminOS CI `30256514753` completed successfully after its OS
  build/cache job and full test-suite job. All three workflows on exact
  published OS head `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`
  are now terminal green. Only vpsAdmin CI `30256755962` remains in progress.
- Final-head vpsAdmin CI `30256755962` completed with one unexpected failure
  after 17,673.68 seconds: 116 of 117 tests succeeded and only
  `alerts/incident-report-process` failed. Failed-step logs and artifact
  `vpsadmin-test-logs-30256755962` (`8657693939`) were inspected and retained
  at `/tmp/vpsadmin-ci-30256755962` before considering a rerun.
- The failure was a deterministic test race, not an osctld/LXC lifecycle
  failure. The test inserted its pending incident at `13:15:57 +0200` while
  the production-like `vpsadmin-api-incident-reports.timer` independently
  started the same task at `13:15:56`. One invocation created queued
  `TransactionChains::IncidentReport::Process` chain 4 and acquired the
  `Vps-1` resource lock; the test's direct invocation then raised
  `ResourceLocked` on the duplicate unique key. The retained service journal,
  transaction/resource-lock tables, and Ruby backtrace all agree on this
  sequence.
- The test explicitly exercises the task through `run_api_task`, so its
  machine definition now force-disables only the automatic
  `incident-reports` timer. The rake task and direct invocation remain
  available. This removes the second scheduler without weakening the
  assertions for chain completion, VPS stop, report state, mail log, or
  delivered mail. A targeted local integration rerun is required before
  committing and reviewing this CI follow-up.
- `git diff --check` and Nixfmt check passed for the follow-up. The exact
  `./test-runner.sh test alerts/incident-report-process` scenario then passed
  locally in 878.05 seconds; its single example completed in 212.67 seconds
  with the report processed, VPS stopped, and mail delivered. No timer raced
  the direct task invocation.
- Repository-wide Overcommit passed MigrationSpecs, WebUI/API i18n, Nixfmt,
  RuboCop, and PHP CS Fixer. An initial commit invocation outside the Nix shell
  was correctly blocked when commit-time hooks could not find Nixfmt, gettext,
  or MariaDB; no hook was bypassed. Repeating `git commit` inside
  `nix develop` reran all applicable hooks successfully and created focused
  test-only commit `807e9d7f` (`tests: isolate incident report task
  scheduling`).
- Fresh standalone mandatory review of exact follow-up
  `807e9d7f1277217d3cf2d49b7c4b2525dc441c10` found no blocking, important,
  or advisory issues. It confirmed that task `enable` retains the rake
  service while `timer.enable = false` removes only the second scheduler in
  this ephemeral VM, and that the direct task, transaction, stopped VPS,
  report state, mail log, recipient, subject, and body assertions remain
  intact. The retained failed-CI evidence proves the race happened before any
  osctld/LXC lifecycle operation.
- The review found the separate test-only commit correctly placed after the
  already-published generated pin and identified no persisted-state, schema,
  API, protocol, production configuration, deployment-order, mixed-version,
  or rollback impact. Its only explicit residual scope is that this direct-task
  scenario does not test timer activation or concurrent manual rake
  invocations, neither of which this test is intended to cover. The gate is
  clear to push and monitor exact head `807e9d7f`.
- The pre-push SSH fetch found that `origin/master` advanced during the
  five-hour integration run from `eb2ccde5c` to `52933ca65` through generated
  Ruby and WebUI dependency updates `575ff7937` and `52933ca65`. They touch
  neither the incident test nor `flake.lock`, and the reviewed feature applies
  without conflicts. They also have no exact-master workflow evidence.
  Rebasing would replace the independently reviewed tree with a new dependency
  closure unrelated to this follow-up, so this publication retains the
  reviewed base. The remote feature is still exactly `6f4e7de8`, making the
  reviewed update a normal fast-forward rather than a history rewrite.
- A final SSH fetch confirmed the remote feature was still the reviewed parent
  `6f4e7de8`. The normal fast-forward push succeeded, and local plus remote
  feature refs now match exact published vpsAdmin head
  `807e9d7f1277217d3cf2d49b7c4b2525dc441c10`. Because every workflow on the
  parent head was already terminal, there was no superseded queued or running
  workflow to cancel.
- The test-only path triggered exact-head vpsAdmin CI run `30280858867`; it is
  initially in progress. Other workflow files did not select this path on the
  initial enumeration. This run must reach terminal success before the
  initiative can be finalized.
- Exact-head CI `30280858867` selected the affected integration scenario,
  completed its test and result-evaluation steps successfully, and reached
  terminal success in 15 minutes 5 seconds. The commit check API reports
  exactly one check, `Run selected ci-tagged tests`, completed successfully;
  no delayed workflow appeared for this path.
- Final publication evidence is complete:
  - vpsadminOS exact head
    `9b88a3903404ea6b5d14b2c0624bd75a69eb5d44`: RSpec
    `30256514274`, RuboCop `30256514441`, and CI `30256514753`, all terminal
    success;
  - vpsAdmin exact head
    `807e9d7f1277217d3cf2d49b7c4b2525dc441c10`: CI
    `30280858867`, terminal success;
  - local and remote feature refs match both exact published heads, and both
    project worktrees are clean.
