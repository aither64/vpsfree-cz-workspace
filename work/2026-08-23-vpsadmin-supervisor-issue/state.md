# 2026-08-23-vpsadmin-supervisor-issue

## Repositories

- Canonical bare clone: `repos/vpsadmin.git`
- vpsAdmin base: `6610c6789c3d567ba0c67fdbf8392904b9f266ba`
- vpsAdmin branch: `2026-08-23-vpsadmin-supervisor-issue`
- vpsAdmin worktree:
  `worktrees/2026-08-23-vpsadmin-supervisor-issue/vpsadmin`
- Configuration base: `b615d1eafe0dc763a9f90dfc8c78bdff9bd6067a`
- Configuration branch: `2026-08-23-vpsadmin-supervisor-issue`
- Configuration worktree:
  `worktrees/2026-08-23-vpsadmin-supervisor-issue/vpsfree-cz-configuration`
- Diagnosed deployed vpsAdmin commit:
  `b3d63c005bef30be52165cd80ef4978bbf0e72b2`

## Status

Implementation is committed and pushed in vpsAdmin. The second mandatory review
confirmed the first-review corrections and found two new blockers: an ungated
console-output publisher and feature branches behind their upstream defaults.
Both are resolved. vpsAdmin is rebased onto current `master`, console output now
uses the recovery gate, and focused verification is green. The regenerated
configuration pin is committed and pushed for all three approved channels on
current configuration `master`; both narrow API configuration builds are green.
The final fresh-context review found no blocking, important, or advisory issues.
Six final-head CI workflows are green and the long integration workflow remains
in progress. Node configuration evaluation remains blocked in this workstation
by the unavailable operator initrd SSH host key. No production state has been
changed and deployment is explicitly out of scope.

The incident contains three independent or partially independent failure
modes:

1. API supervisor OOM-report persistence fails on an undersized integer
   column. This predates the DDoS.
2. The DDoS-related network interruption caused the transaction loop on a
   subset of nodes to remain in the database reconnect/initialization path.
   Status reporting continued in its separate thread, and the watchdog
   intentionally classified the stale transaction check as unresponsive.
3. Node5 also entered a RabbitMQ connection/channel recovery loop caused by
   publishing while Bunny had reopened the connection but had not yet reopened
   and recovered its channels.

## Commands run

- Verified the active development-session slug with `bin/dev-session current`
  and `VPSFREE_DEV_SESSION_SLUG`.
- Inspected logs over read-only SSH as root on `log.int`, including API1/API2,
  node fleet, database and all three RabbitMQ brokers.
- Grouped 2026-08-23 supervisor errors by VPS and correlated node5 kernel OOM
  reports with supervisor queue failures.
- Compared database connection attempts, watchdog warnings, TERM/SIGKILL
  escalation and post-restart behavior across affected and recovered nodes.
- Inspected deployed vpsAdmin source with `git show`, including supervisor OOM
  persistence, schema/migration, the kernel OOM parser, daemon transaction and
  status loops, watchdog logic, database reconnect logic and `NodeBunny`.
- Inspected deployed Bunny 2.24.0 recovery ordering and mysql2 0.5.7 native
  `mysql_real_connect` handling from their Nix store paths.
- Fetched current upstream refs and created isolated vpsAdmin and configuration
  feature worktrees from their respective `origin/master` revisions.
- Configuration worktree creation completed, but its post-checkout Overcommit
  hook returned 78 because the ambient shell lacked the locked gems. Installed
  and signed the repository hooks from its Nix shell before any configuration
  commit.
- Prepared the root, API, libnodectld and nodectld Nix development shells.
- Installed and signed the vpsAdmin Overcommit hooks from the root development
  shell. All four commits passed Nixfmt, migration-spec selection, API/WebUI
  i18n and RuboCop pre-commit hooks.
- Generated the core-only schema using `VPSADMIN_PLUGINS=none` and an isolated
  temporary MariaDB instance. Removed unrelated schema-dumper ordering noise.
- Ran the new migration spec: 4 examples, 0 failures.
- Ran OOM supervisor and API resource specs: 69 examples; the API resource
  coverage passed, while the first run exposed an outer-transaction rollback
  edge in the new atomicity spec. Changed the report transaction to use a
  savepoint and reran the supervisor spec: 11 examples, 0 failures.
- Ran NodeBunny, watchdog, remote-command, CLI and daemon specs: 25 examples,
  0 failures. An earlier run hung because two concurrency specs notified the
  lazily initialized Bunny session before callbacks were registered; the specs
  now initialize explicitly and bound all waits.
- Ran API RuboCop on all touched API files and root RuboCop on all touched
  libnodectld/nodectld files: no offenses.
- Fixed all mandatory-review findings and autosquashed the fixes into the four
  functional commits. The final RabbitMQ gate uses a reentrant `Monitor`, the
  large-counter supervisor example is in the schema commit, and the watchdog
  RPC uses one absolute ten-second deadline for connect, greeting and response.
- Reran the OOM supervisor spec separately after an invalid combined invocation
  with the isolated migration spec reset its database: 11 examples, 0 failures.
- Reran the complete focused NodeBunny/watchdog/daemon suite: 27 examples,
  0 failures.
- Reran API RuboCop on five touched source/spec files and root RuboCop on all
  thirteen touched libnodectld/nodectld files: no offenses.
- Ran `./test-runner.sh test services-up`: all 27 examples and the test script
  passed.
- Ran `./test-runner.sh test cluster/1-node`: both examples and the test script
  passed. Both integration tests used cached kernels; no local kernel build was
  started.
- Refetched `origin/master`; it remains at the recorded base and is an ancestor
  of the clean feature head.
- Rewrote the four commit subjects to follow the repository's scoped-subject
  convention. All hooks passed for every message-only amend, the final tree
  hash remained identical, and the corrected history was force-pushed. Canceled
  only the two still-running workflows for the superseded head; four workflows
  on that head had already succeeded.
- The first final-head CI integration attempt ran all 118 selected tests for
  5h55m. It passed 116 and failed `storage/repeated-rollback-branching` plus
  `vps/clone-remote-consistent`; both isolated service VMs lost healthy API
  backends and returned 503/504 responses while their units stayed running.
- Downloaded and inspected the complete CI artifact instead of blindly
  rerunning. The logs showed no OOM, RabbitMQ recovery, failed systemd unit or
  exception in any changed path. An exact-base `master` CI run from earlier the
  same day passed the clone test while failing a different long integration
  test.
- Reproduced `storage/repeated-rollback-branching` locally on the feature head:
  its second example failed on an immediate API 503 after all preceding
  transaction rows completed successfully. Created a temporary detached
  worktree at base `b12f41859a9ae198224cd6ca63eddbcdd0371db8` and reproduced
  the same example there with a 504 after 74 seconds. This establishes that
  failure as pre-existing rather than branch-induced.
- Started the base clone comparison, then stopped it cleanly when the runner
  warned that another workspace session's active VM tests left insufficient
  shared-memory headroom. Removed the clean temporary base worktree. No other
  session's processes or state were changed.
- Requested one failed-job rerun for CI run `32652787707` only after the above
  investigation. Attempt 2 completed in 11 seconds without running tests: the
  preserved push event's before revision and the message-only rewritten head
  have identical trees, so selection reported `mode=skip` and `reason=no
  changed files`. This nominally green attempt is not branch validation; the
  original 116/118 result remains the applicable full-integration evidence.
- Ran `confctl inputs channel set --commit 'vpsadmin,staging,production'
  vpsadmin b9ba01bd994a838579e5ec0fafd999837c808209` in the configuration
  development shell. Its generated commit changes only the three approved
  `flake.lock` inputs, and all three resolve to the exact vpsAdmin feature head.
- Verified the `vpsadmin`, `staging`, and `production` channel mappings
  sequentially. Parallel `confctl` invocations contend on shared evaluation
  cache, Bundler-lock, and log paths, so the sequential rerun is authoritative.
- Built the `cz.vpsfree/vpsadmin/int.api1` and
  `cz.vpsfree/vpsadmin/int.api2` scopes successfully without activation.
- Evaluation of `cz.vpsfree/nodes/stg/node1` stopped before building because
  `/secrets/nodes/initrd/ssh_host_ed25519_key` is unavailable in this
  workstation. The other node scopes share that operator-only input and were
  not retried blindly. No secret substitute was fabricated and no activation
  or deployment command was run.
- Ran the second standalone mandatory change review. It confirmed all four
  first-review corrections and the four-commit split, then found that console
  output still bypassed the NodeBunny publisher gate and that both feature
  branches had fallen behind their upstream defaults.
- Rebased vpsAdmin onto `6610c6789c3d567ba0c67fdbf8392904b9f266ba`.
  Changed `Console::Server#publish_output` to use `NodeBunny.publish_wait` and
  added a regression example that holds console output until simulated channel
  recovery completes.
- The first fixup commit attempt was blocked because it ran outside the full
  repository development shell and lacked RuboCop, gettext, and MariaDB. The
  same staged commit was rerun in `nix develop`; every mandatory pre-commit and
  commit-message hook passed, and the fix was autosquashed into the
  `libnodectld:` commit.
- After rebasing, reran the migration spec (4 examples), OOM supervisor/API
  resource specs (69 examples), and the focused NodeBunny/watchdog/daemon suite
  (28 examples), all with zero failures. RuboCop reported no offenses on the
  changed console source and NodeBunny spec.
- Force-pushed the rewritten vpsAdmin feature branch with lease at
  `582f6165b506d655f47397e6e39216da9ac871e6`.
- Dropped the obsolete configuration pin and moved the configuration branch
  onto current `master` at `b615d1eafe0dc763a9f90dfc8c78bdff9bd6067a`.
  Regenerated one `confctl` commit pinning all three roles to the new vpsAdmin
  head. The generated commit message was left unchanged.
- Verified the three channel mappings sequentially and rebuilt
  `cz.vpsfree/vpsadmin/int.api1` (87 derivations) and
  `cz.vpsfree/vpsadmin/int.api2` (8 derivations) successfully without
  activation. Pushed the configuration feature branch.

## vpsAdmin commits

- Base: `6610c6789c3d567ba0c67fdbf8392904b9f266ba`
- `64d283dc0eebb9709094dab0baf1c457d055a4ce` — `api: widen OOM report
  task memory counters`
- `ebbcf52a6171b268e7f59d751abe0612ea81569b` — `api: persist OOM reports
  atomically`
- `48b206d9e545fadf457450822975311a9d70426a` — `libnodectld: gate
  publishers during channel recovery`
- `582f6165b506d655f47397e6e39216da9ac871e6` — `nodectld: make
  watchdog use poll staleness`
- Final rebased head after resolving the second-review findings:
  `582f6165b506d655f47397e6e39216da9ac871e6`

The configuration channel pin is a generated mechanical follow-up and is not
part of the first pre-integration code review.

## Configuration commit

- Base: `b615d1eafe0dc763a9f90dfc8c78bdff9bd6067a`
- `7eaaf7d5f22825b3350eec960578b04651d96196` — generated `confctl`
  update of `vpsadminProduction`, `vpsadminServices`, and `vpsadminStaging`
  to `582f6165b506d655f47397e6e39216da9ac871e6`
- No deployment, activation, migration, service restart, or merge was run.

## Mandatory change review

The fresh-context review reported two blocking findings, one important finding
and one advisory note:

- The Mutex-based publisher gate could recursively deadlock when Bunny starts
  recovery synchronously from the thread in `exchange.publish`.
- Large-counter supervisor coverage belonged in the schema commit rather than
  the atomic-persistence commit.
- Greeting and response reads each received a fresh 10-second watchdog RPC
  timeout instead of sharing one end-to-end budget.
- Deployment notes needed to mention ActiveRecord schema caches in already
  running API supervisors.

Decision: all findings were fixed before integration tests. The Bunny gate now
uses a reentrant Monitor with a same-thread recovery regression spec, the commit
split was rewritten, the RPC has one absolute deadline guarded by one
end-to-end timeout, and the supervisor restart requirement is recorded in the
compatibility plan.

## Second mandatory change review

The second fresh-context review confirmed that all first-review corrections
were present and that the four functional commits were focused, ordered, and
properly scoped. It reported two blocking findings and no important or advisory
findings:

- `Console::Server#publish_output` still called `Exchange#publish` directly and
  could reproduce the connection-open/channel-recovered race during an active
  console session.
- vpsAdmin and configuration had both advanced upstream. The old configuration
  pin could not fast-forward and would have replaced the newer services input.

Decision: both blockers were fixed before advancing the configuration branch.
Console output now uses the recovery gate with call-site recovery coverage.
Both branches were rebased onto current upstream revisions, the vpsAdmin branch
was revalidated and pushed, and the three-role configuration pin was regenerated
from current configuration `master`.

## Final mandatory change review

The final standalone fresh-context review inspected the post-fix pushed heads
`582f6165b506d655f47397e6e39216da9ac871e6` and
`7eaaf7d5f22825b3350eec960578b04651d96196`. It reported no blocking,
important, or advisory findings. It confirmed:

- the four vpsAdmin commits are focused, correctly ordered, and based directly
  on current upstream;
- exactly the seven kernel unsigned-long counters are widened with guarded
  upgrade and downgrade behavior;
- OOM report rows and related counters are enclosed in one savepoint-backed
  transaction;
- all libnodectld publishers route through the NodeBunny gate, including console
  output, and no direct exchange publisher remains outside the gated methods;
- watchdog freshness advances only after a successful transaction metadata poll
  and no transaction selection, age, eligibility, or drag logic was introduced;
- the generated configuration commit is directly based on current upstream and
  changes only the three approved vpsAdmin inputs to the exact reviewed head.

Residual gaps are the still-running final integration workflow, simulated
rather than broker-backed RabbitMQ recovery coverage, no static prohibition on
future raw publishers, no production-scale migration locking measurement, the
operator-key-blocked node evaluation, and the need for a real future watchdog
backtrace to identify the exact stuck Connector/C native frame.

## Results

### API2 supervisor backtraces

- By approximately 15:52 CEST, API2 had emitted 314
  `VpsAdmin::Supervisor::Node::OomReports::TaskRangeError` events for the day:
  312 for VPS 23629 and one each for VPSes 28444 and 25551.
- The dominant payload contains a `mariadbd` task whose kernel `total_vm` is
  approximately 2,148,035,000 pages. This is a virtual address-space size of
  roughly 8 TiB, not 8 TiB of resident memory.
- `oom_report_tasks.total_vm` remains a signed four-byte `integer`, whose
  maximum is 2,147,483,647. ActiveModel therefore rejects the payload before
  SQL insertion. The explicit diagnostic exception was added on 2026-08-09,
  but the schema mismatch is older and the same VPS produced these errors on
  multiple days before the DDoS.
- Report, usage and statistic rows are inserted before task rows and are not
  wrapped in a common transaction. A rejected task list can therefore leave a
  partially persisted OOM report.

Root cause: a kernel page-count field was modeled as a signed 32-bit database
integer. The correct primary fix is a `bigint` migration, accompanied by an
audit of the other kernel-sized task fields and atomic report persistence.

### Transaction-loop stalls

- The first node5 database connect timeout occurred at 15:16:48 and RabbitMQ
  channel creation timed out at 15:16:54. API and fleet clients then reported
  database and RabbitMQ TCP/handshake failures through roughly 15:24.
- The database and all RabbitMQ services continued running and logged no
  restart, OOM or comparable resource failure during 15:00-16:00. Brokers
  continued accepting connections. This points to disrupted network
  reachability/packet delivery during the DDoS, not a database or broker
  process crash.
- `nodectld` updates `last_transaction_check` only after its main loop completes
  the metadata query used to poll transactions. Status updates run in a
  separate thread. The watchdog's behavior is therefore intentional: a valid
  local status response is not considered alive once the transaction check is
  more than 600 seconds old.
- Several daemons logged a database `Trying to connect` with no corresponding
  completion even though other database-using threads in the same process
  reconnected. Staging nodes 1 and 2 and `pgnd/node1` reached the 900-second
  watchdog limit. `prg/node22` and `prg/node25` were restarted earlier. These
  processes did not exit after TERM and required SIGKILL after 60 seconds.
- Node5's watchdog reported that its transaction check recovered after
  360 seconds at 15:22:52. It still did not resume useful transaction work and
  its RabbitMQ recovery loop continued, so it was manually restarted at
  15:26:29. It exited promptly on TERM and started again at 15:26:30.
- Other nodes completed all reconnect paths and resumed without restart. No
  further fleet watchdog warnings appeared after the affected restarts.

Best-supported root cause: one database connect/initialization sequence per
affected transaction loop remained blocked in native mysql2/MariaDB Connector/C
code after connectivity returned. `Db#connect` retries forever and emits no log
between starting `Mysql2::Client.new` and completing the initial `SET NAMES`,
so logs cannot distinguish those two native operations. The configured
15-second connect/read/write timeouts did not bound this failure mode. The
SIGKILL requirement strongly supports a native call that did not return, but a
thread dump was not captured before termination, so the exact native frame is
an inference rather than directly observed evidence.

### Node5 RabbitMQ recovery

- From 15:20:55 until the restart, node5 repeatedly logged
  `CHANNEL_ERROR - expected 'channel.open'`. Broker logs independently show
  authenticated node5 connections sending `basic.publish` on channels that had
  not been opened. The brokers closed each such connection, perpetuating the
  recovery loop.
- Bunny 2.24.0 marks the connection as no longer recovering immediately after
  the transport/session reopens, before `recover_channels` completes and before
  the recovery-completed callback.
- The deployed `NodeBunny#create_channel` has a generation/condition barrier
  for the channel-creation timeout path. `publish_wait` and `publish_drop` do
  not use that barrier; they publish directly and rescue only
  `Bunny::ConnectionClosedError`.
- Concurrent publishers can therefore observe an open connection and use an
  exchange whose channel has not yet been reopened. The broker then rejects
  `basic.publish`, causing another connection recovery. Restarting node5
  cleared this poisoned recovery state immediately.
- This persistent AMQP failure is the distinguishing evidence for node5: its
  transaction freshness briefly recovered, unlike the nodes that subsequently
  reached the watchdog limit, but the daemon remained operationally unusable
  until restart.

Root cause: a connection-open/channel-recovered race in the custom NodeBunny
recovery wrapper. All publishers need to be gated by the recovery generation;
drop-mode publishers should drop while recovery is incomplete and wait-mode
publishers should wait for the recovery-completed callback.

### DDoS relationship

- The network disruption is the trigger for the fleet database and RabbitMQ
  recovery paths.
- The API OOM-report range failures are unrelated and pre-existing. Node5's
  repeated OOM reports were dominated by VPS 23629, whereas the observed
  high-rate SYN/port-scanner traffic was logged for a different VPS.

## Open questions

- Capture an all-thread backtrace from a future stale daemon before watchdog
  termination to identify whether it is in `mysql_real_connect`, the initial
  query or another Connector/C frame.
- Determine whether any OOM publications were lost during the RabbitMQ outage.
  Node5 parsed more kernel OOM events than API2 recorded supervisor failures,
  but the live counts and interrupted publication path do not prove the exact
  loss count.
- After a future real watchdog intervention, evaluate the captured transaction
  thread backtrace to decide whether a lower-level mysql2/Connector-C timeout
  fix is also needed.

## Cleanup

Feature worktrees and branches are active. Remove worktrees only after the work
is merged or abandoned; retain branch refs. The shared top-level workspace
contains unrelated changes and untracked files which must remain untouched.
