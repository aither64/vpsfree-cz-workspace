# 2026-08-22-osctld-boot-failures

## Repositories

- `vpsadminos`
  - branch: `2026-08-22-osctld-boot-failures`
  - worktree:
    `worktrees/2026-08-22-osctld-boot-failures/vpsadminos`
  - base/head before implementation: `97a8c8fc6` (`origin/staging`)
- `vpsadmin`
  - branch: `2026-08-22-osctld-boot-failures`
  - worktree:
    `worktrees/2026-08-22-osctld-boot-failures/vpsadmin`
  - base/head before implementation: `d8ce525fa` (`origin/master`)
- `vpsfree-cz-configuration`
  - branch: `2026-08-22-osctld-boot-failures`
  - worktree:
    `worktrees/2026-08-22-osctld-boot-failures/vpsfree-cz-configuration`
  - base/head before implementation: `3bd35c6c` (`origin/master`)

The earlier `2026-07-24-ct-start-hang` worktrees and branches are reference
material and will remain untouched. Its reviewed vpsadminOS lifecycle series
ends at `9b88a3903`; its vpsAdmin structured recovery-cleanup change is
`e8c79b343`.

## Status

- Active initiative verified through both `bin/dev-session current` and the
  matching `VPSFREE_DEV_SESSION_SLUG` environment variable.
- Log/source investigation and affected-container verification are complete.
  Detailed evidence remains in `investigation.md`.
- The prior container-lifecycle initiative was independently compared with
  this incident. The reconciled implementation plan adopts its reviewed
  generation-fencing foundation and adds the missing drain, upgrade handoff,
  startup reconciliation, and activation-ordering work.
- The user authorized implementation in feature branches and permitted
  vpsfree-cz-configuration feature pins. Node deployment or activation is
  expressly excluded.
- Local repository `AGENTS.md` files for all three worktrees have been read.
- The reviewed July vpsAdminOS series was replayed as nine commits ending at
  `af3dc0fbf`; the July vpsAdmin structured cleanup commit was replayed as
  `9f4d3d570`.
- The first mandatory standalone review and its iterative follow-up audited the
  dirty implementation before long VM tests. Its findings covered unmanaged
  runtime ownership, lifecycle admission, legacy compensation, startup
  ordering, durable handoff recovery, cgroup inventory, stale manager identity,
  nodectld pause persistence, missing-veth intent, hook bounds, and exception
  containment.
- A second fresh committed-tree review found that unowned cgroup processes were
  still selected for TERM/KILL, the first August commit order was not deployable
  at every intermediate revision, nodectld pause failure was not a checked
  barrier, a console removal/client race could create an unreachable TTY, and
  same-destination legacy or foreign routes needed an explicit claim policy.
  All five findings are now fixed and covered by focused specs or VM scenarios.
- A third committed-tree review found indirect broad generation killing,
  non-durable nodectld pause state, incomplete same-destination route conflict
  detection, an overly broad commit series, startup reconciliation outside the
  drain barrier, and safety-critical capability probes. All findings are fixed
  in the current committed trees and covered by focused specs or VM scenarios.
- A fourth fresh committed-tree review found four restart-boundary defects:
  runit's transient one-run request did not survive a dead runsv supervisor;
  an active autostart which settled stopped could lose its rollback intent;
  shaper reconciliation could replace unowned CAKE/IFB state; and malformed
  current-boot handoff state could be discarded. Those corrections were
  committed and passed focused verification.
- The required fresh follow-up review found one remaining blocking crash window:
  the exact legacy nodectld identity was persisted only after the owned runit
  hold. It also found incomplete current-boot handoff field/duplicate validation
  and a disabled routed interface retaining an osctld-owned route with the right
  destination but wrong gateway. All three findings are corrected and committed;
  long VM tests remain gated on one more fresh standalone review.
- The next fresh review found that the legacy stability loop treated every
  nonterminal state as start-direction work, so a direct `stopping -> stopped`
  operation could become a stale desired-running handoff. The coordinator now
  captures only legacy `starting`/`aborting` work as start intent. Focused and
  full specs cover the distinction, and the system-switch VM scenario now keeps
  an autostart-configured container blocked in `stopping`, proves it never enters
  the handoff, and verifies it remains stopped after upgrade. This correction is
  committed and awaiting the required final fresh review.
- The final fresh mandatory review of vpsAdminOS `7bfa4c402` and vpsAdmin
  `0c9c2f20e` reported no Blocking or Important findings and explicitly cleared
  the long VM suites. Its only Advisory finding is that
  `@current_handoff_observed` is now write-only rollback bookkeeping with
  misleading nearby wording. It has no behavioral effect; cleanup is deferred
  to avoid changing the reviewed tree before integration tests.
- The reviewed vpsAdminOS series was rebased from `97a8c8fc6` onto current
  `origin/staging` `80a0017d7`. `git range-diff` marked all 19 feature commits
  unchanged; the only tree difference was the upstream `flake.lock` update.
- The August vpsAdminOS work was rebuilt from the preserved final tree as ten
  dependency-safe commits on top of the nine reviewed July commits:
  - `b2a533630`: lifecycle ownership, drain, durable intent, and readiness core;
  - `be82ba390`: strict legacy runtime handoff ingestion and provenance;
  - `f49b9fa3e`: startup barrier and fail-closed fixed safety contracts;
  - `d6f7ea271`: owned host network reconciliation and route validation;
  - `2d7504147`: per-container console recovery and removal tombstone;
  - `ac26d2934`: new-to-new activation coordination;
  - `d9a713b42`: legacy handoff, phased runit/nodectld journal, strict handoff
    validation, and rollback;
  - `da3fc6081`: lifecycle-state compatibility VM coverage;
  - `713e03ed6`: runtime restart and reconciliation VM coverage;
  - `2dbf7c299`: configuration-switch VM coverage.
- Long-test evaluation exposed an osctld helper-runtime defect after the
  upstream Ruby update: helper executables selected unpatched Ruby through
  `/usr/bin/env` and could not load `libosctl/native`. Commit `529fa43ec` puts
  `ruby_vpsadminos` in the osctld service PATH. Current vpsAdminOS feature head
  is `529fa43ec` on base `80a0017d7`.
- A fresh standalone mandatory review of `529fa43ec`, the rebased vpsAdminOS
  series, and unchanged vpsAdmin integration reported no Blocking or Important
  findings and cleared the VM suites. It confirmed that runit prepends the
  patched Ruby before inherited PATH entries, that every osctld helper and hook
  preserves that PATH, and that generic runit, `sv`, and switch semantics are
  unchanged. Its only Advisory finding repeated the deferred write-only
  `@current_handoff_observed` cleanup; no code change is warranted before
  integration tests.
- The lifecycle VM rerun proved the Ruby correction: legacy freeze completed,
  the target daemon adopted the frozen runtime, retained the veth and created a
  lifecycle generation. It then exposed a second real adoption defect: startup
  inventory discarded the init PID returned alongside LXC state, so the adopted
  frozen container reported `init_pid: nil` even though the preserved PID was
  still running. Commit `f9cfb94c9` carries the full state observation through
  inventory and attaches its PID to the selected run configuration before
  adoption. Current vpsAdminOS feature head is `f9cfb94c9`.
- A second fresh standalone mandatory review reported no Blocking or Important
  findings and cleared the VM suites at `f9cfb94c9`. It confirmed that the
  persisted active generation is selected before the synchronized init-PID
  assignment, lifecycle admission remains closed during the operation, and a
  raw PID should stay a fresh LXC observation rather than durable lifecycle
  identity. Its only Advisory finding again concerns the deferred write-only
  handoff bookkeeping.
- The next lifecycle VM rerun showed why `f9cfb94c9` did not yet receive an init
  PID: a frozen container's persisted state bypassed the LXC query, so the full
  state observation still contained no PID. The other three lifecycle examples
  passed. Commit `a459b7b32` now queries LXC authoritatively during startup
  inventory before legacy or managed runtime adoption. Ordinary cached-state
  callers are unchanged. A pool-level regression covers cached frozen state and
  init-PID retention.
- The mandatory review at `a459b7b32` reported no Blocking findings and one
  Important compatibility defect: legacy activation skipped the nodectld pause
  when the service was absent, but then waited unconditionally for its socket.
  Commit `7fb75d10a` makes the pause result an explicit barrier decision, skips
  the idle wait only when nodectld genuinely is not supervised, and still fails
  closed if a durable barrier outlives supervision. The full public preparation
  path and stale-barrier path have regressions. Current vpsAdminOS feature head
  is `7fb75d10a`.
- The fresh follow-up review at `7fb75d10a` reported no Blocking or Important
  findings and cleared all three long VM suites. It confirmed that absent
  nodectld returns `false` only when neither supervision nor a durable barrier
  exists, while identification, pause, idle-status, and stale-barrier failures
  still abort before osctld stops. Its plan-wording advisory was applied; the
  behavior-neutral `@current_handoff_observed` cleanup remains deferred.
- The first `osctld/restart` invocation failed during Nix evaluation before a
  VM started: the module's new restart timeout values had normal definition
  priority and conflicted with the fixture's bounded values. Commit
  `e8d75b037` marks these values with `mkDefault`, preserving production
  defaults while allowing machine configuration through the existing freeform
  `osctld.settings`. The fixture now evaluates and is listed, Nix parsing and
  nixfmt pass, and Overcommit passed. Current vpsAdminOS feature head is
  `e8d75b037`.
- A fresh standalone mandatory review of `e8d75b037` reported no Blocking,
  Important, or Advisory findings and cleared the remaining restart and
  configuration-switch VM suites. Direct module evaluation confirmed that the
  defaults remain `300/60/300/30`, ordinary machine definitions can override
  all four settings, and the Ruby fallback values still match.
- The first post-review `osctld/restart` VM reached the runtime examples and
  exposed three integration defects. A graceful restart closed a subscribed
  event client without its `osctld_shutdown` event, because closing the public
  server released the main setup thread while signal-driven cleanup was still
  running in a helper thread. Commit `3ef73e39c` retains that helper identity
  and joins it from setup, preventing process exit before management-client and
  callback cleanup completes. Commit `4f0fa595d` reads supervised identities
  from the actual `/service` runsv tree instead of the unrelated
  `/run/service` one-shot state directory, updates the VM assertions, and keeps
  all new container IDs within osctld's 27-character limit.
- The next fresh mandatory review found a blocking race between successful
  restart preparation and the stopping-phase commit: a concurrent public
  `resume` could reopen hooks, lifecycle admission, and autostarts after the
  final drain. Commit `8bd248e07` now holds the preparation mutex through the
  atomic `prepared -> stopping` transition, and a deterministic concurrent
  regression proves `resume` waits and then rejects the stopping phase. The
  review also requested that the mixed runit/test-fixture commit be split.
  Commit `cea9ec081` now contains only the authoritative `/service` correction
  and matching PID assertions; `7da2861bc` contains only the four shortened VM
  container IDs. The rewritten head is byte-for-byte identical to the
  pre-split tree at `bd75c6a86`; current vpsAdminOS feature head is
  `8bd248e07`.
- The fresh follow-up review cleared the serialized stop transition and split
  history, but found two more blocking nodectld replacement windows. The
  ordinary post-resume hook cleared its marker after one acknowledged resume
  without proving that a replacement process was also unpaused. Initial legacy
  acquisition also trusted the current occupant of a potentially stale runit
  PID file before proving that it belonged to nodectld. Long VM tests remained
  gated and neither finding was deferred.
- The vpsAdmin feature series was rebased unchanged onto current `origin/master`
  `b12f41859`, which adds VPS autostart convergence monitoring. Commit
  `e3ebfb4aa` now clears an ordinary barrier only inside a bounded
  resume/status loop, repeats resume for a replacement process, and rearms the
  marker plus pause on verification failure. Current vpsAdmin feature head is
  `e3ebfb4aa`.
- vpsAdminOS commit `1195b7031` accepts initial nodectld signal authority only
  when the stable supervised PID has a live `runsv` parent for the named
  service and belongs to nodectld's runit service cgroup. A stale or reused PID
  aborts before the journal is written. The verified PID/start-time identity is
  still retained for recovery after a later supervisor loss. Current vpsAdminOS
  feature head is `1195b7031`.
- The next fresh review cleared runit PID attribution but found that the first
  ordinary resume RPC still had an indeterminate-result window: nodectld applies
  resume before replying, so a lost reply or killed hook could leave the current
  process admitting transactions while the file marker remained. Commit
  `79f6a73f7` makes the durable barrier an active admission predicate in
  nodectld's `run?` and `paused?`, not only a startup initializer. Every failed
  attempted resume also rearms the marker and pause request. Thus an interrupted
  hook remains closed while the marker exists, and marker removal is the durable
  commit point which a later hook retry can finish idempotently. Current
  vpsAdmin feature head is `79f6a73f7`.
- The latest fresh review cleared the dynamic admission barrier and runit PID
  attribution, but found one blocking cross-repository ownership defect: an
  ordinary pre-stop hook could overwrite a current-boot legacy, unknown, or
  malformed marker. That could convert the first legacy-to-new upgrade marker
  to ordinary ownership and let post-resume clear it. Ordinary marker
  acquisition and release are now reason-checked under a file lock shared with
  the configuration coordinator. Coordinator-owned and fail-closed markers are
  preserved, including if ownership changes during resume; legacy pre-stop
  still reaffirms the idempotent remote pause. The synthetic system fixture now
  follows the same protocol and asserts that the legacy reason survives the old
  daemon's pre-stop. This correction has passed focused/full specs and awaits a
  committed-tree follow-up review before long VM tests resume. It is committed
  as vpsAdmin `b12ddfef2` and vpsAdminOS `9733e913d`; these are the current
  ownership commits.
- The fresh committed-tree follow-up review reported no Blocking or Important
  findings and cleared `osctld/restart` and `system/switch-to-configuration`.
  Its documentation advisory found that the `pre-stop` man page described the
  final stopping phase even though the hook runs during restart draining.
  Commit `ef3d60728` now documents closed lifecycle admission, available
  management clients, the pending active-work drain, and the public
  `OSCTL_DAEMON_STATE=stopping` value. The required user-facing writing skill
  was applied. A narrow fresh review of that documentation tail reported no
  Blocking, Important, or Advisory findings and kept both VM suites cleared.
  The behavior-neutral `@current_handoff_observed` advisory remains deferred.
- The first cleared `osctld/restart` VM run reached 7 of 16 examples. Its first
  six scenarios passed, including a start which drained after the short `sv`
  client timeout. The next scenario exposed a missed readiness wake-up: the
  replacement daemon served its socket and pool, but remained in `blocked`
  after the preceding start had converged, so triggered autostart was rejected
  before its blocking hook ran. Readiness could take a blocker snapshot, lose
  the final lifecycle notification before publishing `blocked`, and then have
  no callback with which to retry; runtime cgroup process exits likewise need
  not notify osctld. Commit `f074f1dec` scheduled the coalesced readiness worker
  whenever readiness remained incomplete, polled once per second while the
  exceptional blocked phase persisted, and made the VM helper require daemon
  readiness rather than only a socket and imported pool. Its fresh mandatory
  review found a blocking dirty-flag race: a notification just before readiness
  publication could cause one extra evaluation after autostarts opened and
  close admission on that legitimate work. Amended commit `a366673f0` removes
  dirty re-entry, polls only while phase remains `blocked`, and restricts retry
  evaluation to `blocked` under the lifecycle-admission fence. A deterministic
  interleaving regression creates ready-service work and proves the stale
  notification is discarded. The fresh follow-up then found a narrower exit
  handoff: phase could return to `blocked` after the worker's first exit check
  but before it cleared its registered thread, allowing the matching lifecycle
  notification to observe an apparently live worker and be lost. Amended commit
  `358474a5f` rechecks phase while holding the retry-registration mutex; either
  the existing worker retains ownership and polls again, or it unregisters
  before a later notification can inspect it. A deterministic regression forces
  that exact interleaving. Full-suite verification also exposed that the frozen
  legacy inventory example added by this initiative depended on unrelated specs
  to load its constants and initialize logging. Commit `b732f1d70` makes that
  example independently runnable. The fresh review cleared the retry worker's
  exit handoff and lock ordering, but found that a drain which won during
  ready-service activation could be overwritten back to `blocked` if activation
  then raised. A retry could consequently reopen admission while preparation
  continued. Commit `29c8a14fd` preserves every stop-side phase in readiness
  exception handling, always closes admission, and deterministically covers an
  activation failure after the daemon has reached `prepared`. Current
  vpsAdminOS feature head was `29c8a14fd`. Its fresh follow-up review reported
  no Blocking or Important findings, accepted the linear commit history, and
  explicitly cleared both remaining VM suites.
- The cleared `osctld/restart` rerun again passed examples 1 through 6. Example
  7 reached the triggered autostart but its start was rejected because the
  daemon had moved from `ready` back to `blocked`; the hook therefore never
  started and the example timed out after 62.55 seconds. The preserved log at
  `/tmp/os-test-runner/os-test-osctld__restart-b891f158` shows `wait-ready`
  succeeding immediately beforehand and the later start rejection at
  14:17:24. A late readiness completion had rescanned an already-ready daemon
  while ordinary autostart lifecycle work was active, misclassified that work
  as a startup blocker, and withdrew admission. Commit `a3ea8014f` restricts
  readiness completion to `starting` and `blocked`; explicit recovery failures
  and orphans still move `ready` to `blocked` through their dedicated paths.
  The regression proves an established ready daemon neither scans ordinary
  lifecycle blockers nor closes admission. Current vpsAdminOS feature head is
  `a3ea8014f`. Its fresh review reported no Blocking or Important findings and
  cleared both remaining VM suites; the only Advisory observation was the
  already-deferred write-only `@current_handoff_observed` bookkeeping.
- The next cleared `osctld/restart` VM run passed examples 1 through 9,
  including the formerly failing triggered-autostart scenario. Example 10 then
  reproduced a real internal restart defect while repairing a missing host
  veth. Runtime network recovery did not supply `stop_method`, and Restart
  forwarded that omission as an explicit `nil`, defeating Stop's
  `shutdown_or_kill` default and failing the controlled generation restart
  with `unknown stop method ''`. Commit `2404cb2a2` supplies the same default at
  Restart's internal command boundary and adds a regression for the recovery
  call shape. The lifecycle command spec was also made independent of suite
  load order after the focused invocation exposed its implicit Daemon
  dependency. Current vpsAdminOS feature head is `2404cb2a2`; a fresh review is
  required before resuming VM tests. The latest VM artifacts are preserved at
  `/tmp/os-test-runner/os-test-osctld__restart-b891f158`.
- The fresh review of `2404cb2a2` reported no Blocking or Important findings
  and explicitly cleared both remaining VM suites. It confirmed that the
  internal default matches Stop's established behavior, preserves every
  explicit stop mode, and changes no generic runit, activation, persisted-state,
  API, vpsAdmin, or configuration-pin behavior. Its only Advisory finding is
  the unchanged, deferred `@current_handoff_observed` bookkeeping.
- The cleared `osctld/restart` rerun at `2404cb2a2` passed examples 1 through
  9. Examples 10 and 11 then failed before their intended assertions because
  their direct post-`sv restart` `wait-ready` calls raced the brief absence of
  the replacement management socket. The shared fixture helper already waits
  for runit, socket creation, daemon readiness, and pool import; commit
  `390d56a8d` uses it consistently for all three explicit restart scenarios.
  Logs after example 10's early assertion show missing-veth recovery itself
  completing, with the old generation stopped and a new generation running.
- The failed example cleanup allowed the next context setup to expose another
  implementation defect before example 12 started: a freshly created veth
  reports the kernel `noqueue` root qdisc, which strict ownership validation
  treated as foreign and rejected when RX shaping was configured. Commit
  `2f49755f0` treats only the exact kernel default (`noqueue`, root, handle
  `0:`) as replaceable missing state. Arbitrary foreign and legacy qdiscs remain
  fail-closed. A focused regression covers the exact default shape; the same
  shape was confirmed read-only on a host veth with `tc -json`.
- Current vpsAdminOS feature head is `390d56a8d`. Both follow-up commits passed
  their active Overcommit hooks. The fresh review found no Blocking or
  Important issues and cleared both remaining VM suites. It verified that the
  qdisc exception requires the exact `noqueue`/root/`0:` shape and that other
  unowned roots remain blocked. Its non-gating coverage Advisory suggests an
  additional near-miss `noqueue` unit case; the exact accepted shape and a
  foreign-root rejection are already covered, so this is deferred with the
  behavior-neutral `@current_handoff_observed` cleanup.
- Safety branch `2026-08-22-osctld-boot-failures-pre-rewrite` retains WIP commit
  `9b4f3f668`. The final feature tree was byte-for-byte compared with that WIP
  tree after the rewrite and matched.
- Safety branch
  `2026-08-22-osctld-boot-failures-pre-review2-rewrite` retains the second
  reviewed WIP tree at `bfacbf15a`. Its tree and final feature head
  `071d8d3cb` are byte-for-byte identical.
- The vpsAdmin integration is split on top of cleanup commit `9f4d3d570`:
  - `d0c6e03bd`: checked pre-stop and post-resume hook contract;
  - `392e3cfd8`: early daemon-hook refresh timing;
  - `0c9c2f20e`: boot-bound marker, coordinator deferral, and status capability,
    and current feature head.

## Confirmed implementation decisions

- Keep the osctld CLI supervisor and make its forwarded TERM use the same drain
  coordinator as the management API.
- Keep osctld as a normal runit service. Direct `sv restart` may outlive the
  short sv-client wait but continues draining under runsv.
- Special-case only osctld ordering in `switch-to-configuration`; leave generic
  service exit-status, timeout, failure, and rollback behavior unchanged.
- Do not use `killMode` as the explanation for container survival.
- Support runtime legacy-to-new upgrade and adoption of already-running
  containers. Do not support runtime downgrade after new lifecycle state is
  written.
- Preserve a live runtime when ownership is unambiguous; block readiness rather
  than killing runtime whose ownership cannot be proved.
- Treat daemon pre-stop hooks as checked barriers. If nodectld cannot pause,
  abort restart preparation, run the safe post-resume path, and leave osctld
  running without stopping or activating services.
- Keep a legacy-upgrade nodectld pause durable across supervisor restarts with
  a boot-bound phased journal written before runit mutation, an owned runit
  `down` file, and the exact legacy process identity. Replace the legacy process
  with a marker-aware target before osctld starts, and let only the
  configuration coordinator resume it after osctld readiness.
- Treat the marker reason as ownership. Ordinary hooks and the configuration
  coordinator serialize marker mutations through
  `/run/osctl/nodectld-upgrade-pause.json.lock`; each side removes only the
  current-boot reason it owns, and unknown or malformed state stays fail-closed.
- Register the whole osctld startup recovery path as lifecycle work so direct
  restarts cannot pass the drain barrier during partial reconciliation.

## Commands and results so far

- fetched SSH remotes for all affected repositories;
- created the three initiative feature worktrees listed above;
- inspected current activation, osctld supervisor/signal/shutdown/autostart,
  lifecycle recovery, console, network, nodectld hook, and pin-update paths;
- compared all reviewed July lifecycle commits with current vpsadminOS staging;
- the reviewed July vpsAdminOS series replayed cleanly onto current staging;
- implemented daemon phases and lifecycle admission, bounded drain with
  TERM/KILL escalation against exact recorded processes, readiness/status API,
  boot-bound legacy handoff, two-pass container inventory, autostart intent
  persistence/cancellation, console lock narrowing, and runtime network
  reconciliation;
- implemented osctld-specific activation ordering without changing generic
  runit service behavior; a short `sv restart` client timeout remains visible
  while runsv continues the requested drain/restart;
- added legacy-to-new and new-to-new configuration-switch scenarios which
  retain the running container's init PID, cgroup, lifecycle generation, host
  veth, routes, console socket, data, and connectivity;
- the first-upgrade scenario kills the configuration coordinator after legacy
  osctld has stopped, verifies boot-bound handoff and nodectld pause markers,
  and proves that rerunning the switch adopts both running and pending work;
- changed and unchanged nodectld cases use an actual runit service, daemon hook
  files, and the UNIX remote-control protocol to assert pause/resume and deferred
  restart order;
- moved nodectld daemon-hook refresh directly after RemoteControl startup and
  added a post-resume hook;
- `nixfmt` completed on all changed Nix files;
- final vpsAdminOS RuboCop: 1,482 files, 0 offenses;
- osctld RSpec: 1,355 examples, 0 failures;
- final osctld RSpec after drain/recovery refinements: 1,360 examples,
  0 failures;
- post-review osctld focused RSpec: 158 examples, 0 failures;
- post-review full osctld RSpec: 1,375 examples, 0 failures;
- final follow-up focused osctld RSpec: 61 examples, 0 failures;
- final follow-up full osctld RSpec: 1,384 examples, 0 failures;
- ownership-precision full osctld RSpec: 1,385 examples, 0 failures;
- final full osctld RSpec: 1,422 examples, 0 failures;
- post-second-review full osctld RSpec: 1,428 examples, 0 failures;
- final post-third-review full osctld RSpec: 1,434 examples, 0 failures;
- post-fourth-review-fix full osctld RSpec: 1,453 examples, 0 failures;
- post-follow-up-review focused osctld RSpec: 56 examples, 0 failures;
- post-follow-up-review full osctld RSpec: 1,459 examples, 0 failures;
- post-legacy-stop-fix focused osctld RSpec: 32 examples, 0 failures;
- post-legacy-stop-fix full osctld RSpec: 1,460 examples, 0 failures;
- post-rebase full osctld RSpec: 1,460 examples, 0 failures;
- authoritative startup-inventory osctld RSpec: 1,461 examples, 0 failures;
- optional-nodectld activation focused RSpec: 34 examples, 0 failures;
- post-review-fix full osctld RSpec: 1,463 examples, 0 failures;
- shutdown-completion focused osctld RSpec: 57 examples, 0 failures;
- post-VM-fix activation RSpec: 34 examples, 0 failures;
- post-VM-fix full osctld RSpec: 1,464 examples, 0 failures;
- prepared-to-stopping focused daemon RSpec: 35 examples, 0 failures;
- post-race-fix full osctld RSpec: 1,465 examples, 0 failures;
- nodectld replacement-resume focused RSpec: 10 examples, 0 failures;
- runit process-attribution activation RSpec: 36 examples, 0 failures;
- post-attribution full osctld RSpec: 1,467 examples, 0 failures;
- rebased post-resume full libnodectld RSpec: 493 examples, 0 failures;
- indeterminate-resume focused libnodectld RSpec: 22 examples, 0 failures;
- dynamic-barrier full libnodectld RSpec: 494 examples, 0 failures;
- marker-ownership focused libnodectld RSpec: 30 examples, 0 failures;
- marker-ownership full libnodectld RSpec: 504 examples, 0 failures;
- marker-ownership activation RSpec: 38 examples, 0 failures;
- marker-ownership full osctld RSpec: 1,469 examples, 0 failures;
- readiness-retry focused daemon RSpec: 36 examples, 0 failures;
- readiness-retry full osctld RSpec: 1,470 examples, 0 failures;
- post-review readiness focused daemon RSpec: 37 examples, 0 failures;
- post-review readiness full osctld RSpec: 1,471 examples, 0 failures;
- retry-worker exit-handoff focused daemon RSpec: 38 examples, 0 failures;
- isolated frozen-inventory RSpec at the failing full-suite seed: 1 example,
  0 failures;
- final readiness full osctld RSpec at seed 20424: 1,472 examples, 0 failures;
- drain-versus-readiness focused daemon RSpec: 39 examples, 0 failures;
- post-drain-race full osctld RSpec: 1,473 examples, 0 failures;
- stable-ready focused daemon RSpec: 40 examples, 0 failures;
- stable-ready full osctld RSpec: 1,474 examples, 0 failures;
- internal-restart focused lifecycle RSpec: 44 examples, 0 failures;
- internal-restart full osctld RSpec: 1,475 examples, 0 failures;
- post-qdisc focused veth/lifecycle RSpec: 63 examples, 0 failures;
- post-qdisc full osctld RSpec: 1,476 examples, 0 failures;
- final `osctld/lifecycle` VM: 4 examples passed, including frozen legacy
  adoption with the preserved init PID and residual-generation quarantine;
- dependency-safe core revision osctld RSpec: 1,392 examples, 0 failures;
- dependency-safe network RSpec: 31 examples, 0 failures;
- dependency-safe console RSpec: 19 examples, 0 failures;
- dependency-safe activation RSpec: 15 examples, 0 failures;
- final commit-boundary core RSpec: 1,386 examples, 0 failures;
- final commit-boundary legacy-handoff RSpec: 1,392 examples, 0 failures;
- final commit-boundary fail-closed RSpec: 212 examples, 0 failures;
- final commit-boundary network RSpec: 33 examples, 0 failures;
- final commit-boundary console RSpec: 19 examples, 0 failures;
- final commit-boundary new-to-new activation RSpec: 6 examples, 0 failures;
- final commit-boundary legacy activation RSpec: 18 examples, 0 failures;
- final focused daemon/autostart RSpec: 45 examples, 0 failures;
- osctl RSpec: 189 examples, 0 failures;
- post-review libnodectld RSpec: 466 examples, 0 failures;
- final libnodectld RSpec: 472 examples, 0 failures;
- post-fourth-review-fix libnodectld RSpec: 478 examples, 0 failures;
- final vpsAdmin RuboCop: 2,090 files, 0 offenses;
- vpsAdminOS Overcommit pre-commit hooks passed on every rewritten commit;
- vpsAdmin Overcommit pre-commit hooks, including API/WebUI localization and
  migration checks: passed on the feature commit;
- `./test-runner.sh ls` successfully evaluated and listed `osctld/lifecycle`,
  `osctld/restart`, and `system/switch-to-configuration` from the final tree;
- `nix-instantiate --parse` and `nixfmt --check` accept all three changed VM
  definitions;
- `git diff --check` passes and both implementation worktrees are clean;
- post-timeout-fix mandatory review: no Blocking, Important, or Advisory
  findings; the reviewer independently evaluated unchanged defaults and all
  four ordinary-priority overrides;
- the corrected switch fixture evaluates and is listed as
  `system/switch-to-configuration`; `nix-instantiate --parse` and
  `nixfmt --check` pass;
- repository-wide vpsAdminOS and vpsAdmin Overcommit runs pass after the
  corrective changes; the first ambient-shell commit attempt was rejected
  because RuboCop was absent and was rerun successfully through `nix develop`;
- the first `osctld/lifecycle` VM run failed only when the successfully adopted
  legacy container was frozen: the helper loaded `libosctl/native` with the
  unpatched Ruby and reported the missing `rb_thread_start_timer_thread`
  symbol. The remaining three lifecycle examples passed. The service PATH fix
  passes `git diff --check`, Nix parsing, `nixfmt --check`, and the active
  Overcommit hooks. The ambient-shell commit attempt was rejected because its
  hook could not find `nixfmt`; the commit was then made through `nix develop`
  and the real hook passed;
- the second `osctld/lifecycle` run passed the earlier freeze boundary and then
  failed the preserved-init-PID assertion (`expected: 3569`, `got: nil`); its
  other three examples passed. The init-PID correction passes its focused
  container regression (44 examples), changed-file RuboCop, active Overcommit
  hooks, and the full osctld suite (1,460 examples, 0 failures). A combined
  partial `container_spec`/`pool_spec` selection hit an existing spec load-order
  limitation because the real `CGroup` constant was not loaded after a stub was
  restored; the authoritative full randomized suite loads the normal graph and
  passed;
- no node, container, daemon, or system configuration was modified.
- the first post-review `osctld/restart` VM passed four of its first six
  examples before fixture setup aborted. It proved idle-client closure,
  explicit drain/resume admission, and abrupt-death client exit. The subscribed
  monitor disconnected without the shutdown event, the active-start example
  used the nonexistent `/run/service/osctld/supervise/pid`, and the next
  context used a 28-character container ID. Logs stopped after the daemon's
  successful lifecycle drain and before its cleanup-complete message, leading
  to the signal-helper/main-thread exit fix described above;
- Ruby lint, Nix parsing and formatting, test enumeration, `git diff --check`,
  and active Overcommit hooks pass for commits `3ef73e39c` and `4f0fa595d`;
- changed-file RuboCop and active Overcommit hooks pass for the serialized stop
  transition and both split replacement commits; `git range-diff` confirms the
  split and `git diff --exit-code bd75c6a86 8bd248e07` confirms exact final-tree
  identity;
- changed-file RuboCop and active Overcommit hooks pass for commits
  `e3ebfb4aa` and `1195b7031`; the vpsAdmin rebase range-diff marks all four
  pre-existing feature commits unchanged;
- changed-file RuboCop and active Overcommit hooks pass for dynamic admission
  barrier commit `79f6a73f7`;
- changed-file RuboCop, `nixfmt --check`, `git diff --check`, and the active
  Overcommit hooks pass for amended readiness-retry commit `358474a5f` and
  inventory-test isolation commit `b732f1d70`;
- changed-file RuboCop, `git diff --check`, and active Overcommit hooks pass for
  drain-phase preservation commit `29c8a14fd`;
- changed-file RuboCop, `nixfmt --check`, `git diff --check`, and active
  Overcommit hooks pass for stable-readiness commit `a3ea8014f`;

The third review follow-up additionally:

- removes broad generation-tree killing and escalates only exact recorded
  process identities, including when owned and unowned blockers coexist;
- makes the nodectld pause survive supervision with a boot-ID-bound marker,
  marker-aware daemon startup, and `svc -o`/`svc -u` activation control;
- validates foreign and conflicting same-destination routes even when the exact
  owned route is also present;
- covers the complete startup recovery sequence with the drain lifecycle task;
- replaces internal capability probes with explicit safety interfaces and
  explicit no-op test doubles;
- splits the implementation into focused dependency-safe commits and verifies
  the significant intermediate boundaries.

The second fresh-review fixes additionally:

- report unowned live container-cgroup processes as persistent restart blockers
  and never signal them during either drain escalation;
- make nodectld's pre-stop hook raise on rejection or transport failure, abort
  osctld preparation, and complete the post-resume path before admission can
  reopen;
- tombstone console containers under the per-container mutex so a client racing
  registry removal cannot allocate an unreachable TTY;
- claim only exact matching unmarked legacy routes, while foreign and
  conflicting same-destination routes block reconciliation and remain intact;
- make every August intermediate commit deployable by combining the mutually
  dependent lifecycle-generation and daemon-admission work before the network,
  console, activation, and VM-test commits.

The review follow-up fixes additionally:

- scan live osctl container cgroups independently of configured containers and
  block readiness for unconfigured or adopted-but-unowned runtime;
- admit only explicitly tagged recovery work before global readiness and start
  ordinary autostarts only after every pool has been imported, runtime network
  reconciliation has been scheduled, and the checked post-resume hook passes;
- serialize post-resume hook attempts and retry failures while readiness and
  lifecycle admission remain closed;
- target the exact residual generation named by drain diagnostics;
- finalize legacy start intent after the old daemon has exited and compensate
  only successfully cancelled queues, idempotently retaining durable handoff
  state on any restoration failure;
- keep nodectld available while osctld drains, resume it through the target
  daemon hook before readiness opens, then restart it through the deferred
  ordinary service pass when its definition changed;
- add focused ownership, autostart gate, hook retry, residual escalation,
  network drift, parallel console, activation ordering, and compensation
  coverage.

The second review follow-up additionally:

- keeps `initialized` false until global inventory, handoff persistence, and
  every pool's runtime reconciliation have completed;
- persists handoff start intent for containers which settled stopped and
  retains current-boot inherited entries across coordinator reruns or rollback;
- blocks readiness for live processes in configured non-running cgroups and
  live containers without a lifecycle generation;
- prevents missing-veth recovery from reversing a durable stop intent;
- removes only shaping filters and protocol-230 routes carrying osctld ownership
  markers before reapplying exact desired state; ambiguous legacy and foreign
  state is preserved;
- retries readiness while runit is up but the target socket is not created yet;
- adds VM scenarios for interrupted autostart, stopped/live cgroup ownership,
  missing veth during stop, in-place route/shaper/bridge repair, and a legacy
  start which settles stopped before replacement.

Non-obvious local test setup findings:

- invoking osctl RSpec without exporting the prepared component-local
  `GEM_HOME`, `GEM_PATH`, `BUNDLE_PATH`, and `BUNDLE_GEMFILE` selected no usable
  `rspec`; the prepared environment under
  `/tmp/osctld-build-artifacts-D4ikLcPl/.gems` is the working path;
- running repository-root RuboCop in a shell which still exported osctld's
  `BUNDLE_GEMFILE` selected the wrong bundle; run root RuboCop in a fresh
  `nix develop --command bundle exec rubocop` invocation;
- libnodectld's component shell changes directory and its component Gemfile does
  not contain RuboCop; use the vpsAdmin repository-root lint for style checks.
- the first post-follow-up full osctld run loaded the path-based ruby-lxc source
  without its native extension and stopped before examples; placing the already
  prepared ruby-lxc gem's `lib` directory on `RUBYLIB` selected its matching
  native extension, and the full 1,459-example rerun passed;
- running the vpsAdmin pre-commit hook from the ambient shell failed because
  RuboCop, gettext, and MariaDB were absent; retrying the commit through the
  repository-root `nix develop` shell passed every hook;
- running two rewrite-worktree Bundler preparations concurrently against a
  shared gem cache produced an incomplete local bundle and hid the prepared
  `libosctl` native extension. The intermediate revision checks were rerun
  serially with the preserved native library paths and passed.
- the rebased full libnodectld suite initially stopped before examples because
  the fixed shared `/tmp/dev-ruby-gems` cache contained Prometheus and Bundler
  gemspecs but incomplete installed files. A task-specific bundle cache,
  bootstrapped with `RUBYOPT` unset, ran all 493 examples successfully. The
  reusable workflow is recorded in
  `notes/vpsadmin/2026-08-23-incomplete-shared-bundler-cache.md`.
- a detached boundary-check worktree needed its own `libosctl` native build;
  the initial missing-extension failure was environmental. The generated
  artifacts were confined to that transient worktree, and it was removed after
  the boundary checks.
- the first 1,472-example readiness rerun failed at seed 20424 because the new
  frozen legacy inventory example used constants and logger initialization
  supplied by earlier examples. Running it alone exposed both dependencies;
  explicit component requires plus a local logger stub now make the example
  pass independently and the same full-suite seed passes.
- the first post-final-review lifecycle invocation failed during Nix evaluation,
  before any VM started, because component-local Bundler checks had recreated
  ignored `osctld/.gems`; the generic gem builder recursively discovered
  Bundler's installed gemspecs and rejected their incomplete installed-source
  tree. The cache was moved recoverably to
  `/tmp/osctld-vm-contaminating-gems.Q7dEsq/osctld.gems`; the reusable lesson is
  in `notes/vpsadminos/2026-08-23-component-gems-contaminate-nix-source.md`.

## First complete restart VM run and follow-up

`./test-runner.sh test osctld/restart` at vpsAdminOS `390d56a8d` used
substituted Linux 6.12.95 and did not start a local kernel build. Artifacts are
under `/tmp/os-test-runner/os-test-osctld__restart-b891f158`. Examples 1-11
and 13 passed, including interrupted autostart, controlled missing-veth
recovery, parallel missing console sockets, and missing veth during a desired
stop.

The remaining failures had two independent causes:

- the repairable network-drift example exposed a real adoption-order bug;
  ordinary running state is not persisted in container configuration, so veth
  setup ran while the container was still `unknown`. The later authoritative
  LXC inventory found the running runtime but did not refresh network-interface
  objects. Reconciliation therefore classified existing veths as missing and
  performed controlled generation restarts instead of in-place repair;
- the stopped-container cgroup example correctly reached `drain_failed`,
  reported `unowned_container_cgroup_processes`, and left the foreign process
  alive through TERM/KILL escalation. Its assertion sent a literal
  `#{pid_path}` to the guest because a single-quoted Ruby string disabled
  interpolation, producing invalid shell syntax. That aborted example then
  left the daemon in `drain_failed`, cascading into the readiness and active
  copy examples.

Follow-up commits:

- `6abfdae63` (`osctld: observe veths after runtime inventory`) adds an explicit
  post-inventory host runtime observation for network interfaces, with veth and
  pool regressions. Runtime upgrades now discover already-running containers'
  existing veths before ownership-aware repair;
- `c6c762957` (`tests/osctld: expand the cgroup PID assertion`) fixes the guest
  process-liveness assertion so the intended unowned-process behavior is
  actually verified.

Quick verification after the follow-up:

- focused veth: 20 examples, 0 failures;
- focused pool: 19 examples, 0 failures;
- full osctld: 1,477 examples, 0 failures, seed 32586;
- changed-file RuboCop, `nixfmt --check`, and `git diff --check` pass;
- active Overcommit pre-commit and commit-message hooks pass for both commits.

The Bundler cache created by the hook-backed commits was moved recoverably to
`/tmp/vpsadminos-post-runtime-netif-gems.IF9JwN/root.gems` before further Nix
evaluation.

Fresh mandatory review of `390d56a8d..c6c762957` found no Blocking or
Important issues and cleared both `osctld/restart` and
`system/switch-to-configuration`. The reviewer confirmed from preserved logs
that the unowned process survived exact-owned escalation and that only the
literal fixture placeholder failed. One non-gating advisory suggested making
the pool unit expectation explicitly ordered/stateful. That improvement is
deferred because production has the direct authoritative-observation then
netif-observation sequence, while the VM drift example verifies unchanged init
PIDs across real in-place repair. The unchanged behavior-neutral
`@current_handoff_observed` bookkeeping was repeated as an advisory.

The complete `osctld/restart` rerun at `c6c762957` again used substituted
kernel outputs and did not build a kernel locally. Examples 1-14 passed. In
particular, the current head proved both controlled generation replacement for
a genuinely missing veth and in-place route/qdisc/bridge repair with unchanged
init PIDs. The corrected drain example proved the unowned process survived
exact-owned TERM/KILL escalation and the desired stop remained authoritative
when its veth disappeared.

Examples 15-16 exposed two remaining fixture races, not daemon contract
failures:

- after removing the startup blocker and SIGKILLing the blocked daemon, the
  helper accepted the still-running runit status and stale socket. Its single
  `wait-ready` connection then crossed replacement socket turnover and failed;
  the replacement daemon became ready immediately afterward;
- a copy-state hook was intentionally held beyond the 5-second drain and
  2-second cleanup deadlines. Exact-owned escalation terminated it correctly,
  and its client received the precise hook-cancellation error before the old
  socket disappeared. The older fixture accepted only a transport disconnect.

The initial combined fixture commit `c388d9b83` was split after mandatory review
required the two independent corrections to remain separately reviewable:

- `335dc524f` (`tests/osctld: retry replacement readiness`) retries through
  socket turnover;
- `22da03ef6` (`tests/osctld: accept exact copy interruption`) narrows the
  additional accepted outcome to the active copy scenario's exact hook path.

The split head has byte-identical tree content to `c388d9b83`. `nixfmt --check`,
`nix-instantiate --parse`, `git diff --check`, and the active Overcommit hooks
pass for both commits. Hook Bundler artifacts were moved recoverably to
`/tmp/vpsadminos-post-restart-fixture-gems.sd79tJ/root.gems` and
`/tmp/vpsadminos-post-split-fixture-gems.zhjmkl/root.gems`.

The final fresh split-boundary review found no Blocking, Important, or
Advisory issues. It independently confirmed clean commit separation, identical
tree `ad79d27069913cb79065016c968a80f5b3eecfe9`, bounded readiness retry, and
the active-copy-only exact hook oracle, then cleared both long VM suites.

The next complete `osctld/restart` run at `22da03ef6` passed examples 1-15.
Example 16 then exposed a remaining daemon bug rather than a fixture race. A
local state copy had durably requested that its source stop and was blocked in
the source's pre-stop hook. Restart draining correctly sent TERM only to the
recorded hook child, but the surviving stop worker handled that intentional
interruption as an ordinary stop failure. `Lifecycle#fail_stop` consequently
changed the durable desired state back to `running`; the replacement daemon
faithfully adopted the still-running source and had no stop intent to resume.

Initial commit `66d29cdb1` (`osctld: preserve intents across restart
escalation`) attempted to mark an exact lifecycle effect before restart
draining signals any of its owned processes. Its intended behavior was:

- an interrupted start keeps its original desired-running intent so the
  replacement can launch it;
- an interrupted stop keeps its original desired-stopped intent and becomes a
  quiescent restart handoff which no longer blocks the old daemon;
- an interrupted exact cleanup can likewise be handed to startup recovery;
- ordinary start, stop, hook, and cleanup failures retain their existing
  behavior.

Quick verification at `66d29cdb1`:

- focused lifecycle and daemon specs: 125 examples, 0 failures, seed `36366`;
- full osctld suite: 1,481 examples, 0 failures, seed `2275`;
- changed-file RuboCop and `git diff --check` pass;
- active Overcommit Nixfmt, RuboCop, and commit-message hooks pass.

The commit hook's recreated Bundler cache was moved recoverably to
`/tmp/vpsadminos-post-intent-commit-gems.2s6BGy/root.gems` before further Nix
evaluation.

The mandatory fresh review of `22da03ef6..66d29cdb1` found three Blocking and
one Important issue, so the long VM gate remained closed:

- failure reducers removed the effect worker identity before its actual thread
  exited; the old daemon could therefore detach a still-running start cleanup
  worker and race replacement startup;
- a signalled start which had already published its wrapper used
  `finish_dead_wrapper`, not `fail_launch`, and could still convert its launch
  intent to stopped during recovery;
- an interrupted stop belonging to `ct restart` stamped the newer restart
  intent onto the old still-running generation, falsely fulfilling the
  requested replacement;
- effect marking used only the run ID after taking the blocker snapshot, so a
  concurrent transition could mark replacement work or signal without a
  successful exact-effect fence.

The unmerged commit was rewritten as `1195b458d`. Its final design atomically
validates the blocker effect ID and snapshots only exact live owned processes
under the lifecycle reducer lock before returning identities to be signalled.
The durable handoff retains the exact effect worker until
`effect_worker_exited`; history and active runs remain restart blockers while
that thread is alive. The marker also survives the published-wrapper path,
creates a new running intent only when that interrupted generation actually
stops, and clears when the generation is instead recovered running. An
interrupted restart stop retains the old launch ID, so replacement recovery
recognizes and completes the pending stop/start sequence. Stale effect
snapshots return without signalling.

Quick verification at rewritten head `1195b458d`:

- focused lifecycle, daemon, and lifecycle-command specs: 175 examples,
  0 failures, seed `62145`;
- full osctld suite: 1,487 examples, 0 failures, seed `57170`;
- changed-file RuboCop and `git diff --check` pass;
- active Overcommit Nixfmt, RuboCop, and commit-message hooks pass.

The rewritten regressions deterministically cover the worker-exit boundary,
the post-wrapper start path, desired-stopped and restart-intent stop paths,
healthy running adoption, and stale effect rejection. Hook Bundler artifacts
were moved recoverably to
`/tmp/vpsadminos-post-intent-rewrite-gems.ooefT8/root.gems`. A new fresh
mandatory review of the rewritten exact head is required before VM testing.

The fresh review of `22da03ef6..1195b458d` cleared the prior four findings in
their direct reducer paths, but found two further Blocking transition races.
Long VM tests therefore remain gated:

- `prepare_daemon_restart_interruption` released the reducer lock before the
  daemon delivered signals. A start could become stably running in that gap
  while retaining the snapshotted wrapper PID, after which stale escalation
  would terminate the stable container.
- a successful interrupted stop could let its original worker exit and then
  call `complete_run` before the finalizer removed compatibility LXC/run
  configuration. This removed the cleanup effect from restart blockers while
  the finalizer was still active; daemon exit in that window could leave a
  stopped legacy run to overwrite a pending desired-running restart intent on
  reload.

The follow-up implementation keeps validation, marking, and exact signal
delivery inside one lifecycle reducer fence. `complete_run` now retains a live
cleanup effect worker as a completed terminal owner, including after the run
moves to history, until `effect_worker_exited` publishes its exact boundary.
This keeps drain blocked through compatibility artifact removal and the
replacement-start attempt. Startup also recognizes a stopped compatibility
run file whose exact lifecycle generation is already clean, removes it instead
of adopting it, and preserves the pending desired-running intent. Clean-run
pruning likewise waits for a completed effect worker to exit.

Deterministic regressions prove that a concurrent effect transition cannot
cross signal delivery, that completed cleanup ownership survives persisted
lifecycle reload, that stale stopped compatibility state does not overwrite a
pending restart intent, and that pool inventory discards that stale run
configuration. Quick verification of the uncommitted follow-up passes:

- focused lifecycle, finalizer, daemon, and pool specs: 162 examples,
  0 failures, seed `53356`;
- full osctld suite: 1,490 examples, 0 failures, seed `64354`;
- changed-file RuboCop and `git diff --check` pass.

The follow-up was folded into the same focused feature commit, now
`513f112b4` (`osctld: preserve intents across restart escalation`). Active
Overcommit Nixfmt, RuboCop, and commit-message hooks pass; the text-width hook
reported only its advisory 72-column warning and every message line remains
within the workspace's required 80 columns. Hook Bundler artifacts were moved
recoverably to
`/tmp/vpsadminos-post-intent-fence-gems.KSKV6e/root.gems`. The worktree is
clean. Because the commit was rewritten after a Blocking review, one further
fresh mandatory review of `22da03ef6..513f112b4` is required before VM tests.

The next fresh review of `22da03ef6..513f112b4` confirmed that effect-present
signal fencing and successful-finalizer ownership were sound, and found no
lock-order issue. It nevertheless found two Blocking gaps and one Important
reload issue, so the VM gate remained closed:

- managed pre-start releases the start effect while the generation is still
  `starting`; a nullable effect match could signal exact processes without
  writing the interrupted-start marker, allowing a later stopped observation
  to erase desired-running;
- a startup state observation of `error` could adopt an exact clean generation
  as a stopped legacy run and erase a pending restart intent;
- an abruptly dead `status=completed` worker was inert but remained persisted,
  which could indefinitely make an otherwise drained lifecycle record
  non-discardable across an incarnation change.

The follow-up now fences both the expected effect ID and expected generation
phase. An effect-less managed `launching`/`starting` generation receives an
explicit start handoff marker under the same lock before exact signal delivery.
Exact clean-generation adoption returns an uncertain result for any state
other than authoritative stopped/running/frozen; pool startup records a
readiness-blocking recovery failure without mutating the clean history or its
pending intent. After schema validation and before incarnation validation,
reload removes only terminal completed effects on clean history whose exact
worker is absent or dead; live completed workers remain blockers.

Quick verification after these follow-ups:

- focused lifecycle, finalizer, daemon, and pool specs: 167 examples,
  0 failures, seed `24313`;
- full osctld suite: 1,495 examples, 0 failures, seed `6243`;
- changed-file RuboCop and `git diff --check` pass.

The regressions now cover managed pre-start effect release, uncertain
post-completion observation, same-incarnation dead-worker normalization,
different-incarnation archival, clean-history pruning after worker death, and
continued retention of a live completed worker. A combined shell command
initially scoped the prepared Ruby environment only to RuboCop, so its trailing
`rspec` command was not found; the full suite was rerun separately with the
correct environment and produced the result above.

These changes were folded into the focused commit, now `ec7502ec3`. Active
Overcommit Nixfmt, RuboCop, and commit-message hooks pass; the advisory
text-width warning remains within the workspace's 80-column requirement. The
worktree is clean, and hook Bundler artifacts were moved recoverably to
`/tmp/vpsadminos-post-stage-fence-gems.7KPhUS/root.gems`. A fresh review of
`22da03ef6..ec7502ec3` is required before the VM gate can open.

The fresh review of `22da03ef6..ec7502ec3` cleared the three preceding
findings, but found one final Blocking reducer path. A failure after
`complete_run` called ordinary `fail_cleanup`, which converted clean history
to ownerless `cleanup_failed` history and cleared its terminal worker. That
state was neither a restart blocker nor recoverable, and a surviving stopped
run configuration could again be adopted and erase the pending restart
intent. The review otherwise found no Important issues and confirmed the
signal fence, no-effect start marker, live adoption, and dead-worker
normalization. It classified the lack of an in-process retry for an uncertain
runtime observation as Advisory because readiness stays closed and a later
daemon restart re-observes the untouched state safely.

`fail_cleanup` now treats a `status=completed` effect as a post-completion
artifact/replacement failure: it records the error on the clean history and
effect, preserves the desired intent and terminal worker barrier, and lets
`effect_worker_exited` publish the final boundary. The regression injects that
failure with a pending restart, proves the clean history remains a drain
blocker, then reloads and proves a surviving stopped run configuration is
recognized as stale without changing desired-running.

Quick verification after this reducer fix:

- focused lifecycle, finalizer, daemon, and pool specs: 168 examples,
  0 failures, seed `15516`;
- full osctld suite: 1,496 examples, 0 failures, seed `58578`;
- changed-file RuboCop and `git diff --check` pass.

The post-completion fix was folded into the focused commit, now `d2640a9fa`.
Active Overcommit Nixfmt, RuboCop, and commit-message hooks pass; the advisory
text-width warning remains within the workspace's 80-column requirement. The
worktree is clean, and hook Bundler artifacts were moved recoverably to
`/tmp/vpsadminos-post-completion-failure-gems.uQ6ieo/root.gems`. A fresh review
of `22da03ef6..d2640a9fa` is required before starting VM tests.

The fresh mandatory review of `22da03ef6..d2640a9fa` found no Blocking or
Important issues and cleared the long VM gate. It confirmed that
post-completion errors retain clean history, desired intent, and the exact
worker barrier until `effect_worker_exited`; dead-worker normalization and
stopped/uncertain/live adoption remain coherent. The accepted Advisory is that
a persistent uncertain runtime observation has no in-process retry: readiness
stays closed, state remains untouched, and an operator must correct the
observation problem and restart osctld. The review found the one-commit history
focused and all message lines compliant with the 80-column rule.

The complete `osctld/restart` VM suite passed at `d2640a9fa`: all 16 examples
and the enclosing test script succeeded in 844.28 seconds. This includes the
`sv` timeout drain, interrupted autostart, abrupt-death restart, missing-veth
controlled replacement and desired-stop cases, unowned-process fail-closed
cases, and the active local-copy scenario which originally exposed the lost
stop intent. Nix built only test-harness/osctld-related derivations; no kernel
was built locally.

The first `system/switch-to-configuration` evaluation exposed that its legacy
osctld wrapper was constructed outside the vpsAdminOS module package overlay,
where `pkgs.osctld` is absent. The wrapper now lives in the legacy machine
module's `let`, matching the established legacy-fixture pattern. Evaluation
then reached the VM and exposed three independent follow-up defects:

- `Services#restart_before_osctld` compared every changed service to a missing
  deferred nodectld service; the real `Service#==` dereferenced `nil` during
  dry activation. The deferred service is now computed once and compared only
  when present, with a focused regression.
- the legacy `osctl ct start --queue` fixture client was synchronous and held
  the setup shell for its 120-second client timeout, so the concurrent stop was
  not launched in time. It is now detached with redirected descriptors. The
  stop assertion uses the old daemon's observable pre-stop hook marker; that
  daemon reports the container as `running` until the hook returns. Later
  assertions still require the stop to finish and remain stopped after upgrade.
- the nodectld handoff called `/run/current-system/sw/bin/svc`, which is not
  provided by vpsAdminOS. It now calls `sv` with one-letter `o`, `u`, and `d`
  controls. These controls report whether the runit control request was
  delivered without waiting for a service transition and therefore do not
  inherit `sv start`/`sv restart`'s short transition timeout.

The follow-up was first committed as `51639b85f`, then rewritten without tree
changes into five independently reviewable commits:

- `5dc4a68c6` — nil-safe unchanged-nodectld service ordering and regression;
- `d4f38fbf2` — installed non-waiting `sv` controls and regression;
- `688f6a378` — build the legacy wrapper within the machine package overlay;
- `8344b25f1` — detach the blocked legacy start client for concurrency;
- `9a71ade65` — use the legacy pre-stop hook as the in-flight stop oracle.

Quick verification at the tree now committed as `9a71ade65`:

- activation RSpec: 40 examples, 0 failures, seed `52235`;
- changed-file RuboCop: 2 files, 0 offenses;
- switch VM Nix parse, Nixfmt, Ruby syntax, and `git diff --check` pass;
- active Overcommit Nixfmt, RuboCop, and commit-message hooks pass.

Three failed switch VM attempts were investigated rather than accepted on
rerun. The first stopped at the package-scope evaluation error. The second
proved the nil comparison and synchronous fixture-client timeout. The third
proved the legacy daemon's pre-stop state reporting, then exposed the missing
`svc` executable before `supervision-held` or the container handoff was
recorded. Failures after the handoff example were shared-VM contamination from
its unreleased hook barriers, not treated as independent results. No attempt
built a kernel locally.

The mandatory review of `d2640a9fa..db420ec99` found no production-code defect
or Important issue. It found one Blocking history issue: the test-only commit
still bundled three independently reviewable fixture corrections. It also
advised correcting the `sv` commit message, because the acquiring-supervision
marker and owned down file precede control delivery even though
`supervision-held` and container handoff state do not. The five-commit rewrite
above addresses both findings without changing the final tree. A fresh review
of `d2640a9fa..9a71ade65` is required before rerunning the long switch VM.

The fresh mandatory re-review of `d2640a9fa..9a71ade65` found no Blocking,
Important, or Advisory issues and cleared the switch VM gate. It independently
confirmed the five-commit split, corrected acquisition-versus-handoff wording,
one-letter runit 2.3.1 control semantics, unchanged generic service behavior,
final-tree identity, and the quick checks. Its remaining gate is the full
`system/switch-to-configuration` VM for installed `sv`, legacy nodectld
replacement, interrupted recovery, and running/queued/stopping preservation.
Runtime downgrade remains intentionally unsupported.

The clean switch VM at `9a71ade65` reached the legacy-handoff example after
the first three examples passed, then failed its early check for the in-flight
stop after 90.5 seconds. The check searched the whole handoff file. The pinned
legacy daemon still truthfully exposes the pre-stop-blocked container as live,
so the coordinator temporarily included it in `runtime_containers`; that
section is provenance for conservative in-place network ownership and cannot
create desired-running intent. The distinct `containers` section did not need
to contain the stop. The fixture now checks only that desired-start section
before releasing the hook, while its later whole-file check still requires the
runtime provenance to disappear after the container becomes stopped. The run
was interrupted after this first failure because unreleased shared-VM hook
barriers would contaminate later examples. No kernel was built locally.

The fixture correction is committed as `26d164740` (`tests/system: distinguish
intent from runtime handoff`). Its active Overcommit Nixfmt and commit-message
hooks passed; Nix parsing, standalone Nixfmt, and `git diff --check` also pass.
A fresh mandatory review of `9a71ade65..26d164740` is required before rerunning
the switch VM.

That fresh review found no Blocking issue and confirmed the early assertion's
semantics: only `containers` creates desired-running intent, while
`runtime_containers` is live network-reconciliation provenance. It found one
Important fixture race in the later whole-file assertion: legacy `state=stopped`
can become visible just before the coordinator's next one-second atomic handoff
rewrite removes runtime provenance. That eventual assertion now polls for up to
30 seconds. It will be folded into the same unmerged fixture-correction commit,
then quick checks and a new fresh mandatory review must pass before the VM gate
reopens.

The eventual assertion was folded into the focused commit, rewritten as
`315ead2e1`. Active Overcommit Nixfmt and commit-message hooks pass; standalone
Nixfmt, Nix parsing, and `git diff --check` pass at the rewritten head. The
worktree is clean. A fresh review of `9a71ade65..315ead2e1` is now required.

The fresh review of rewritten head `315ead2e1` found no Blocking, Important, or
Advisory issues and cleared the full switch VM gate. It independently confirmed
that the early assertion reads one atomically published snapshot and checks
only desired starts, the later 30-second whole-file poll spans the one-second
snapshot cadence while remaining inside the 60-second stability window, and
only desired entries are converted into durable running intents. The remaining
gap is the complete VM run at this exact head.

The next clean VM at `315ead2e1` passed examples 1-3 and advanced beyond both
corrected handoff-section assertions. Example 4 then failed after 104.28 seconds
when it immediately expected `/service/nodectld/supervise/pid` to differ from
the orphaned legacy nodectld PID after killing its `runsv` parent. The preceding
checks proved the old nodectld process and socket stayed live and `sv check`
correctly failed. Runit's `runsvdir` scans periodically; the fixed one-second
sleep raced creation of the replacement down supervisor and its
atomic pid-file rewrite. The fixture now waits up to 30 seconds for that
observable rewrite. The run was interrupted after the first failure to avoid
contamination from unreleased barriers. No kernel was built locally.

The runsvdir fixture correction is committed separately as `cc64a5201`
(`tests/system: wait for replacement runsv`). Active Overcommit Nixfmt and
commit-message hooks pass; standalone Nixfmt, Nix parsing, and
`git diff --check` pass. The vpsAdminOS worktree is clean. A fresh mandatory
review of `315ead2e1..cc64a5201` is required before another long VM run.

That review found one Blocking inverse race: a replacement down supervisor can
already make `sv check nodectld` succeed after the fixed sleep, so requiring a
transient check failure was invalid. It also corrected the timing description:
runsvdir uses a periodic scan, not a fixed one-second scan. The fixture now
captures the old runsv PID before killing it, waits for that exact PID to
disappear, and then waits for the affirmative replacement state where
`sv check nodectld` succeeds and `supervise/pid` no longer names the live orphan.
This preserves the old-process/socket checks without depending on a transient
supervisor gap.

The stable-identity design and final commit message were folded into the same
focused commit, rewritten as `06ebcafb5`. Active Overcommit Nixfmt and
commit-message hooks pass; standalone Nixfmt, Nix parsing, and
`git diff --check` pass. The worktree is clean. A fresh review of
`315ead2e1..06ebcafb5` is required before the VM gate can reopen.

The fresh review of `06ebcafb5` found no Blocking, Important, or Advisory
issues and cleared the full switch VM gate. It confirmed exact old-runsv
capture/disappearance, survival of the legacy nodectld process and socket,
affirmative replacement-down supervision, and retained end-to-end recovery
assertions. Independent Nix parse, Nixfmt, diff, ancestry/message, and clean
worktree checks passed; its transient review artifacts are recoverable at
`/tmp/vpsadminos-review-nixfmt-artifacts.wDavZ0`. The remaining gap is the
complete VM at this exact head.

The clean switch VM at `06ebcafb5` passed examples 1-3 and carried example 4
through every previous fixture boundary. Its interrupted-activation retry then
failed after 264.06 seconds because `stop_recorded_legacy_nodectld` waited the
full 60-second service timeout for the orphaned legacy nodectld. The exact
switch invocation took 63.98 seconds and raised `recorded legacy nodectld
process did not stop before replacement`. The test server exits on TERM, but
its runsv parent had intentionally been killed; the child therefore remained
as an unreaped zombie. The coordinator's PID/start-time check followed by
`kill(0)` treated that terminal process as live. The saved failure diagnostics
were collected only after the shared VM continued and no longer retained the
orphan at the failure boundary, so later examples were treated as contaminated
and the VM was stopped. No kernel was built locally.

Production process identity now reads the state field from `/proc/PID/stat`
and treats only Linux zombie/dead states (`Z`, `X`, and historical `x`) as no
longer running. PID reuse remains guarded by start time, and live states such
as uninterruptible sleep still block replacement. The existing orphaned-runsv
regression now deliberately leaves the terminated child unreaped until after
the coordinator returns, reproducing the VM failure instead of racing an eager
waiter. The correction is committed separately as `46acf2338`
(`switch-to-configuration: recognize dead legacy services`). Quick checks at
that head:

- activation RSpec: 40 examples, 0 failures, seed `61030`;
- isolated zombie regression: 5 consecutive examples, 0 failures, seeds `101`,
  `202`, `303`, `404`, and `505` (about 0.22 seconds each);
- changed-file RuboCop: 2 files, 0 offenses;
- Ruby syntax and `git diff --check` pass;
- active Overcommit Nixfmt, RuboCop, and commit-message hooks pass; its
  72-column text-width hook emitted advisory warnings, while every commit
  message line satisfies the workspace's mandatory 80-column limit.

A fresh mandatory review of `06ebcafb5..46acf2338` is required before the next
full switch VM run.

That review kept the VM gate closed. It found one Blocking service-level gap:
the recorded runit PID is nodectld's wrapper, so observing that wrapper as a
zombie does not prove its forked daemon or another live thread has left the
runit service cgroup. A replacement down supervisor could then satisfy the
named-service check while old nodectld work remains. The fix must additionally
require the legacy nodectld service cgroup to be unpopulated and must cover a
zombie wrapper with a surviving child. The review also found an Important
pre-existing PID-reuse race between the PID/start-time check and `Process.kill`;
the exact-process contract calls for opening and validating a pidfd, then
signalling through that stable descriptor. It found no Advisory issue and
confirmed malformed and non-terminal process states remain fail-closed. Commit
`46acf2338` will be rewritten to address both findings before another fresh
review; no VM will run at the blocked head.

Both review findings are addressed in the rewritten focused commit
`22136bfd1` (`switch-to-configuration: verify legacy nodectld exit`), whose
parent remains `06ebcafb5`; blocked commit `46acf2338` is no longer referenced
by the feature branch. The coordinator now opens a Linux pidfd for the recorded
wrapper, revalidates its `/proc` start time and membership in the nodectld runit
service cgroup, and sends TERM through the stable descriptor. It accepts a
terminal wrapper only after cgroup-v2 `cgroup.events` reports `populated 0`, or
the cgroup-v1 task list is empty. Missing or malformed cgroup state fails
closed. The successful orphan regression retains a wrapper zombie until it is
observed; a second real wrapper-plus-child regression proves that a surviving
child keeps the stop incomplete; and a pidfd regression proves a changed
post-open identity is not signalled.

Quick verification at `22136bfd1`:

- activation RSpec passed 42 examples with 0 failures in five complete random
  orders, seeds `61030`, `11111`, `22222`, `33333`, and `44444`;
- no wrapper, child, or RSpec processes leaked after those runs;
- changed-file RuboCop: 2 files, 0 offenses;
- Ruby syntax, `git diff --check`, and the 80-column commit-message requirement
  pass;
- active Overcommit Nixfmt, RuboCop, and commit-message hooks pass; its
  72-column text-width hook emitted advisory warnings only.

The durable plan now records pidfd signalling and whole-service cgroup
quiescence as part of the legacy runtime-upgrade contract. A fresh mandatory
review of `06ebcafb5..22136bfd1` is required before the switch VM gate can
reopen.

The fresh review of `22136bfd1` accepted the pidfd ABI, descriptor lifecycle,
post-open identity/cgroup validation, wrapper-child handling, and upgrade
sequencing. It found one Blocking fail-closed parser defect: absence of both
cgroup-v2 `cgroup.events` and the cgroup-v1 `tasks` file fell back to an empty
`cgroup.procs`, and duplicate or extra-field `populated` records could be
accepted. It found no Important or Advisory issue and kept the VM gate closed.

The parser now accepts exactly one well-formed `populated 0` record from an
otherwise two-field cgroup-v2 event file. Without that file, it requires an
explicitly present and empty cgroup-v1 `tasks` file; `cgroup.procs` is used only
for live process attribution, never as hierarchy-quiescence proof. Regressions
cover populated and empty v2 state, duplicate and extra-field records, missing
events/tasks despite empty `cgroup.procs`, and empty/nonempty v1 task lists.
The rewritten commit is now `09cf3ab06` with unchanged parent `06ebcafb5`;
`22136bfd1` is no longer referenced by the branch. Quick verification after
the parser correction:

- activation RSpec: 44 examples, 0 failures in seeds `55555`, `66666`, and
  `77777`;
- changed-file RuboCop, Ruby syntax, and `git diff --check` pass;
- active Overcommit Nixfmt, RuboCop, and commit-message hooks pass; every
  message line remains within 80 columns.

A new fresh mandatory review of `06ebcafb5..09cf3ab06` is required before the
switch VM gate can reopen.

The new fresh review of `09cf3ab06` found no Blocking, Important, or Advisory
issues and cleared the full `system/switch-to-configuration` VM gate. It
confirmed pidfd identity/signal safety and descriptor cleanup, exact terminal
state handling, whole-service cgroup quiescence, strict v2 and v1 evidence,
flat runit service-cgroup coverage of wrapper/daemon/threads, owned-down-marker
ordering, unchanged generic runit behavior, retained osctld CLI supervision,
focused history, and a clean worktree. The remaining risk is integration timing
of the real guest's `cgroup.events` transition after the runsv-orphaned wrapper
exits; the complete switch VM must now cover it.

The clean switch VM at `09cf3ab06` used the cached Linux 6.12.95 image and did
not build a kernel. Examples 1-3 passed. Example 4 crossed all prior fixture
boundaries, but its interrupted-recovery switch again took 64.63 seconds and
raised `recorded legacy nodectld process did not stop before replacement`; the
example failed after 231.97 seconds. The suite was interrupted immediately
after that first meaningful failure, so example 5's partial result is shared-VM
contamination and is not treated independently. A host cgroup-v2 probe then
confirmed that an unreaped zombie alone produces `populated 0` and disappears
from `cgroup.procs`. A temporary, uncommitted VM-fixture diagnostic now captures
the guest cgroup version, `cgroup.events`, `cgroup.procs`, cgroup-v1 `tasks`, the
pause journal, and nodectld/runsv process states after the retry failure. It
passes Nix parse, Nixfmt, and diff checks and will be removed or converted into
focused coverage after the live guest evidence is understood.

The diagnostic rerun reproduced the timeout and showed the production guard
was correct. The guest uses cgroup v2; `cgroup.events` reported `populated 1`,
`cgroup.procs` contained only recorded PID 849, and that same start-time
identity was still live as `Sl` with PPID 1 after 60 seconds. A host-side
minimal reproduction of the fixture's Ruby 3.4 `UNIXServer` loop confirmed
that closing the server directly from the TERM trap leaves the main thread
blocked in `accept` indefinitely. Moving the close into a separate thread wakes
`accept` and transitions the child to `Z` immediately. Real nodectld likewise
delegates TERM handling to a stop thread and exits after its daemon child
unblocks the main loop.

The temporary cgroup/process dump was removed. The test server now starts a
thread from its TERM trap and closes the server there; this focused fixture fix
is committed separately as `009aa81ec` (`tests/system: wake nodectld server
outside signal trap`). Nix parse, Nixfmt, `git diff --check`, and the active
Overcommit Nixfmt/commit-message hooks pass; all message lines are within 80
columns. A fresh mandatory review of `09cf3ab06..009aa81ec` is required before
rerunning the complete switch VM.

The fresh review of fixture commit `009aa81ec` found no Blocking, Important,
or Advisory issues and cleared the full switch VM gate. It confirmed the change
is test-only, sets `stopping` before starting the close thread, contains
concurrent/repeated-close errors, matches real nodectld's delegated TERM/child
shutdown pattern, retains independent surviving-child production coverage,
and has focused clean history. Independent Nix parse, pinned Nixfmt, diff,
commit-message, and clean-worktree checks passed. The remaining integration
gap is the complete guest scheduling and service-cgroup transition at this
exact head.

The complete switch VM at `009aa81ec` used the cached system inputs and did not
start a kernel build. Examples 1-3 passed. The interrupted legacy recovery in
example 4 completed successfully at the service and lifecycle level: the
replacement osctld became ready, nodectld resumed, the queued container became
running, the concurrent stop remained stopped, and the original container kept
its PID, cgroup, network, console, and in-container state. The example then
failed after 199.81 seconds because its final state assertion generated the
malformed shell command `test "$(...)\" = preserved`. The opening quote was in
a Ruby double-quoted fragment, while the closing `\"` was in a single-quoted
fragment and therefore survived literally. The suite was interrupted promptly
after the already-started example 5 completed; later results are not treated as
independent evidence. The assertion now uses double-quoted Ruby fragments on
both sides. Nix parse, pinned Nixfmt, a standalone Ruby expansion check, and
`git diff --check` pass. The test-only correction is committed as `45dea0306`
(`tests/system: fix runtime state assertion quoting`); active Overcommit
Nixfmt and commit-message hooks pass. It must pass a fresh mandatory review
before the complete VM is rerun.

The fresh mandatory review of exact range `009aa81ec..45dea0306` found no
Blocking, Important, or Advisory issues and reopened the full switch VM gate.
It independently confirmed the focused ancestry, clean worktree, Nix parse,
pinned Nixfmt, diff check, Ruby expansion, shell parsing, comparison behavior,
and effective `machine.all_succeed` failure propagation. The change has no
production or compatibility effect; the only remaining gap is a complete VM
run at exact head `45dea0306`.

The complete `system/switch-to-configuration` VM suite passed all 10 examples
at exact reviewed head `45dea0306` in 717.32 seconds. The interrupted legacy
handoff and recovery example passed end to end in 234.58 seconds. The remaining
examples covered restart triggers, firewall/module ordering, module load and
unload policy, nodectld restart after osctld readiness, pause failure before
service changes, and stopped kernel-modules handling. The runner built only the
expected source-dependent Ruby and test-runner derivations; no kernel build was
started.

After verification, all affected repositories fetched `origin`. The vpsAdminOS
head already descends directly from current `origin/staging` `80a0017d7` with
no upstream-only commits, and vpsAdmin already descends directly from current
`origin/master` `b12f41859` with no upstream-only commits, so neither branch
needed rebasing or SHA changes. Both clean feature branches were pushed over
SSH for the first time: vpsAdminOS at `45dea0306` and vpsAdmin at `b12ddfef2`.
The configuration feature worktree still has no commits and is six commits
behind current `origin/master`; it will be fast-forwarded before exact pins are
created.

The repository-mandated `tools/update_vpsadminos_flake.sh` then pinned the
vpsAdmin feature's test/development input to exact vpsAdminOS revision
`45dea0306bc6cf29ce7023c3bb709da6cebb6632`. It changed only `flake.lock`,
resolved back to that exact revision, and committed through all active hooks as
mechanical dependency commit `ffc226c7d` (`flake: vpsadminos 67fcc1737 ->
45dea0306`). The updated branch was pushed over SSH. Superseded old-head
vpsAdmin CI run `32666734027` was still active and was cancelled; completed
old-head RuboCop and libnodectld runs were left intact. New-head workflows are
running at `ffc226c7d`. The configuration branch fast-forwarded cleanly to
`origin/master` `7cd45c86`; its post-merge hook printed the already-documented
ambient-shell missing-gems warning, so all subsequent hook-triggering commands
will run through its Nix development shell.

`confctl inputs channel set --commit --no-editor` generated two isolated
configuration commits: `8f8eb929` pins vpsAdminOS `45dea0306` in `staging` and
`os-staging`, and `c5b86c2d` pins vpsAdmin `ffc226c7d` in `staging`. Generated
messages remain unmodified. `confctl inputs channel ls` and flake metadata
confirm the complete exact revisions. Production remains on vpsAdminOS
`3bf14ec67` and vpsAdmin `c28b0b447`; the separate vpsAdmin services channel
remains on `b12f41859`.

Configuration validation did not deploy or activate any system:

- `confctl build --max-jobs=0 --yes cz.vpsfree/nodes/stg/node1` evaluated the
  expected `vpsadminos-system-node1.stg.vpsfree.cz-26.05.git.45dea03`
  derivation, then stopped at the known external
  `/secrets/nodes/initrd/ssh_host_ed25519_key` dependency; no build started;
- the first max-jobs-zero os-staging consumer attempt composed the pinned
  inputs, then stopped because an unrelated vpsfree-irc-bot source was not
  cached and local builds were disabled;
- a bounded `confctl build --max-jobs=4 --cores=4 --yes
  cz.vpsfree/containers/int.vpsfbot` then built generation
  `2026-08-23--23-20-38` successfully. Its 62 local derivations were all
  user-space/configuration work; no Linux or ZFS derivation appeared;
- repository-wide Overcommit passed Nixfmt and RuboCop.

Dev-shell `.bin`, `.bundle`, and RuboCop caches were moved recoverably outside
the worktree to `/tmp/osctld-config-dev-caches.DuVgTx` and
`/tmp/osctld-config-verification-caches.Pcmqog`. The configuration worktree is
clean at `c5b86c2d` and ready to push.

The configuration branch was pushed over SSH at `c5b86c2d`; GitHub has no
workflows configured for that feature branch. Its push-time dev-shell caches
were moved recoverably to `/tmp/osctld-config-push-caches.uFjfkS` and the
worktree is clean.

GitHub Actions at the first published implementation heads reported vpsAdminOS
RuboCop success but RSpec run `32666734669` failure. The failed-attempt logs
were inspected before any rerun. All suites except osctld passed; osctld had 11
failures at seed `49411`, all in bridge/routed runtime-reconciliation specs and
all caused by a real `tc -json qdisc show dev veth0` call against their
synthetic, nonexistent veth. The network tests stubbed route/link observation,
but unlike the dedicated veth shaper specs they did not stub the qdisc/filter
observation boundary introduced by runtime reconciliation. This explains why
the failures all returned the same `Cannot find device "veth0"` error instead
of exercising the route or bridge behavior under test.

The bridge and routed spec setup now returns empty qdisc/filter inventory,
matching an unshaped synthetic veth and keeping all qdisc ownership behavior in
the dedicated veth specs. Focused bridge+routed RSpec passes all 21 examples at
the exact CI seed `49411`; changed-file RuboCop, Ruby syntax, and
`git diff --check` pass. The correction is committed as `08cbbe6ea`
(`tests/osctld: isolate network reconciliation specs`); active Overcommit
Nixfmt, RuboCop, and commit-message hooks pass and all message lines remain
within 80 columns. A fresh mandatory review is required before the full
CI-equivalent RSpec suite is run.

The fresh mandatory review of exact range `45dea0306..08cbbe6ea` found no
Blocking, Important, or Advisory issues and reopened the full CI-equivalent
RSpec gate. It confirmed that bridge/routed now mock the same observation
boundary as their existing link/route fixtures, production reconciliation is
unchanged, and the byte-identical dedicated veth suite still covers missing,
healthy, owned, foreign, legacy, kernel-default, stale-IFB, and filter-conflict
paths. Its independent bridge+routed+veth run passed 41 examples at seed
`49411`; syntax, diff, scope, message, and clean-worktree checks also passed.

The exact CI-equivalent aggregate RSpec command then passed all 13 component
suites at `08cbbe6ea`. In particular, osctld passed all 1,502 examples and the
test-runner passed all 182 examples; every suite in the command's final summary
reported `PASS`. The local invocation supplied the worktree as
`GITHUB_WORKSPACE`, which is normally set by GitHub Actions. It built only Ruby
native extensions and test dependencies; no kernel build was started.

The reviewed vpsAdminOS follow-up was pushed at final head `08cbbe6ea`; it
still descends directly from current `origin/staging` `80a0017d7`. The
repository-managed vpsAdmin pin helper then generated dependency-only commit
`48b91cc1c` (`flake: vpsadminos 45dea0306 -> 08cbbe6ea`). It changed only
`flake.lock`, resolved the input to the complete `08cbbe6ea850006030d53ab0f3c1d6c0d90dabf9`
revision, and passed all active hooks. The vpsAdmin branch was pushed at that
head and still descends directly from current `origin/master` `b12f41859`.

`confctl inputs channel set --commit --no-editor` generated final follow-up
configuration commits `cc6861a1` for vpsAdminOS `08cbbe6e` in `staging` and
`os-staging`, and `bc0c96b5` for vpsAdmin `48b91cc1` in `staging`. The channel
table confirms those exact feature revisions. Production remains on
vpsAdminOS `3bf14ec6` and vpsAdmin `c28b0b44`; `vpsadminServices` remains on
`b12f4185`. Both generated commits passed active hooks with the expected
generated-message width warnings and the configuration branch was pushed at
`bc0c96b5`. A first ambient-shell push attempt was rejected before updating
any ref because the moved gem cache was unavailable; the retry through the Nix
development shell passed the push hook.

No-build evaluation of the exact final configuration reached derivation
`vpsadminos-system-node1.stg.vpsfree.cz-26.05.git.08cbbe6` and stopped only at
the expected external `/secrets/nodes/initrd/ssh_host_ed25519_key` boundary.
The final os-staging consumer evaluation also completed composition and
reported its five remaining local configuration derivations; `max-jobs=0`
prevented them from building. Neither command deployed or activated anything,
and no kernel build was started.

Current-head GitHub Actions have already passed vpsAdminOS RuboCop and RSpec,
including the formerly failing aggregate RSpec workflow. vpsAdmin Client
Specs, Webui PHPUnit, i18n health, and libnodectld Specs have also passed at
`48b91cc1c`. The two long current-head CI workflows remain queued. Superseded
queued/in-progress CI runs `32666734679` (vpsAdminOS `45dea0306`) and
`32666902596` (vpsAdmin `ffc226c7d`) were cancelled; completed runs were left
unchanged.

## Verification still required

- the two long current-head GitHub Actions CI workflows after their runners
  become available.

## Cleanup

- Keep all feature worktrees until branches are reviewed/merged or explicitly
  abandoned.
- Do not remove the July initiative's worktrees or refs.
- Earlier failed investigation test artifacts remain recoverably outside the
  worktree at `/tmp/osctld-investigation-cleanup-20260822`.
- Native test and hook artifacts from quick verification were moved
  recoverably to `/tmp/osctld-build-artifacts-D4ikLcPl` and
  `/tmp/osctld-hook-artifacts-Agc0RnX4`.
- Transient rewrite-worktree gem artifacts were moved recoverably to
  `/tmp/osctld-rewrite-gems.b0P9uG` and
  `/tmp/osctld-rewrite-hook-artifacts.CzxBTt`; the temporary rewrite worktree
  and branch were removed after the final tree comparison.
- Bundler caches recreated during post-VM verification were kept out of the
  Nix source tree and moved recoverably beneath
  `/tmp/osctld-post-vm-gems.0CqLrS`,
  `/tmp/vpsadminos-post-vm-root-gems.cMtOTr`,
  `/tmp/vpsadminos-post-nixfmt-gems.uCksRM`,
  `/tmp/osctld-post-full-spec-gems.pcTkxP`,
  `/tmp/vpsadminos-post-signal-commit-gems.jWc1Gl`, and
  `/tmp/vpsadminos-post-runit-commit-gems.OIclR2`.
- Marker-review osctld build artifacts were moved recoverably to
  `/tmp/osctld-marker-review-artifacts.c8mkZU` before the remaining VM runs.
- Stop-race and tail-rewrite Bundler artifacts were moved recoverably beneath
  `/tmp/osctld-stop-race-gems.SqJMHk` and
  `/tmp/vpsadminos-tail-rewrite-gems.XwIHmQ`. The temporary rewrite worktree
  was removed; its safety branch remains at `7da2861bc`.
- The runit-attribution verification artifacts are recoverable beneath
  `/tmp/vpsadminos-identity-review-gems.DENsK9`; the isolated libnodectld bundle
  is beneath `/tmp/vpsadmin-libnodectld-gems.rVXFkS`.
- Bundler caches recreated while validating the qdisc follow-up were moved
  recoverably beneath `/tmp/vpsadminos-post-shaper-gems.ETMQSs` and
  `/tmp/vpsadminos-post-shaper-commit-gems.zXZo6U`.
- Aggregate CI RSpec Bundler caches, generated lockfiles, native extensions,
  and result links were moved recoverably beneath
  `/tmp/vpsadminos-ci-rspec-artifacts.R37OByZl`.
- Final vpsAdmin pin helper artifacts were moved recoverably beneath
  `/tmp/vpsadmin-final-pin-artifacts.I1X4IkEE`.
- Final configuration pin, evaluation, and push artifacts were moved
  recoverably beneath `/tmp/osctld-config-final-pin-artifacts.uPsVbuRn` and
  `/tmp/osctld-config-final-push-artifacts.c690ChmX`.
