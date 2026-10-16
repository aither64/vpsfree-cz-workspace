# Session-recovery VM failure: bounded investigation

Status: bounded source/evidence investigation complete; root cause remains unproved.
Owner: architect0, 2026-10-15. Session binding and retained design/workspace-write
access verified. This record leaves the reviewed `design.md` intact.
Latest follow-up: the single exact-package diagnostic succeeded with active,
untruncated observation and no matching raises. It did not reproduce the failure.
The final section records the evidence limits and a diagnostics-only proposal
for the lead; no further execution or product change is authorized by this record.

Frozen composition: dev-workspace
`b8a6be26a75347dcc9ec0fd1330dff886e47c93f`, workspace `e6aaa9c7`,
configuration `c4fb5da4`. The lead reports native provider/worker checks and CI
passing, but the local flake watcher reports the first provider-switch subtest
ending `failed`, stage `shared-start`, blockers `[]`, with “Provider switch
failed. Original routing was restored.” The utility subsequently reported the
exact b8a6 flake command finished with exit 1 after 36m43s; no operation remains.
This investigation did not poll its running log/runtime, run tests, change source
or pins, or perform host/lifecycle actions.
The lead subsequently supplied the frozen
`recovery-failure-diagnostic-snapshot.log` for one-time analysis and authorized
comparison with the preserved passing `runtime-integration-final.log`.
After command completion, the lead authorized the full log and status reads
summarized below. Session binding and saved design access were reverified.

## What the reported state establishes

At the frozen runtime revision, `libexec/workspace-codex-providers.rb`:

- `provider_apply` writes `daemon-stop`, stops the shared daemon, starts an
  isolated target daemon and runs `resume`; then writes target selection and
  `shared-start`, starts the shared daemon, waits for health, and runs `verify`
  (lines 459–498).
- Its outer rescue replaces the original exception with a generic
  `recovery-required` notice and invokes compensation. Recovery **also writes
  `shared-start`**, after selecting the previous provider (lines 501–550).
- The reported final message is written only after recovery's shared startup,
  health, verify and terminal restoration return successfully. `provider_finish`
  clears blockers but does not clear stage (lines 216–220).

Therefore final `failed/shared-start/blockers[]` describes eventually completed
compensation, **not the original failing step**. The original failure may have
occurred in `daemon-stop` or the forward `shared-start` interval. It is not
evidence that the foreign process remained, or that target startup alone failed.
An ordinary terminal-restoration error after a successful apply is handled as
`applied` with a notice; it does not normally produce this result.

The fixture (`nix/tests/session-recovery-boot.nix:84–117`) registers an empty
workspace, puts a disposable `sleep` into the native service cgroup, verifies
`waiting` with blockers, kills that process, then expects `applied`. It creates
no sessions, native conversations or notification subscriptions. Its later
deliberate failing ExecStart drop-in has not yet been installed. Expected
snapshot thread/loaded counts are consequently zero; confirm counts from any
retained VM evidence. With zero threads, resume/verify perform their file and
catalog validation but skip per-thread native RPCs. Recovery success here proves
shared native/protocol readiness, not restoration of a populated conversation.

## Concrete boundaries to distinguish

1. **Stop and isolated startup.** A stop command can fail; target launch can exit
   or fail to create its socket within 30 seconds. The private `resume` helper
   can fail snapshot/catalog validation even with no threads. The final stage
   cannot distinguish these from later failures. Private startup currently
   discards stdout/stderr (`provider_private_server`, lines 435–455).
2. **Shared launch and readiness.** `systemctl start` succeeds for a `Type=simple`
   Ruby launcher before native protocol readiness. `run_codex` checks the
   reservation stage, computes the registration plan, writes its marker and
   execs the selected native binary (`libexec/workspace-host:1461–1471`). The
   wait checks active/activating state and positive MainPID, then exact
   `/proc/PID/exe`, socket existence and helper health
   (`libexec/workspace-codex-providers.rb:558–575`).
   Service exit/auto-restart, an executable lookup race, or failure to become
   ready within 30 seconds can enter recovery. A live launcher still waiting to
   exec is tolerated until that deadline; it is not itself a proven bug.
3. **Protocol health versus verification.** Health has a one-second context and
   requires `thread/loaded/list` to return a present `data` array. Health errors
   are swallowed and retried inside the outer startup deadline. Verify has a
   three-minute context, validates the snapshot and optional target catalog,
   and only resumes originally loaded threads. With the expected empty fixture,
   retained model/policy mismatch is not a supported explanation. See
   `portal/cmd/workspace-portal/codex_provider.go:74–102,111–122,196–272`.
4. **State/helper I/O.** Atomic state/marker writes and captured helper commands
   can raise independently of native readiness. `capture!` retains helper
   stderr in the raised exception, but apply's rescue drops that exception
   (`workspace-host:3154–3173`). Thus an apparently quiet worker journal does
   not exclude a helper failure.

These are branches supported by the code, not diagnosed causes. The following
snapshot narrows which ones merit diagnostics first.

## Frozen-log evidence

The failed snapshot records this VM-monotonic sequence (lines 4166–4250):

| Time | Evidence |
| --- | --- |
| 235.719 s | Explicit `/v1/models` preflight returned 200; state was applying/quiescing. |
| 236.165–236.253 s | Shared daemon stopped. |
| 237.160 s | A shared-daemon start was reported. The journal does not label it forward versus recovery. |
| 237.462 s | Provider worker reported `provider recovery could not be verified` and exited 1; state became recovery-required/shared-start. |
| 239.783 s | Native model refresh requested `/v1/models?client_version=0.160.0` and received 403. |
| 242.545 s | Systemd restarted the provider worker. |
| 244.461–245.183 s | Shared daemon stopped and started again; compensation subsequently reached failed/shared-start with original routing restored. |

This was **not immediate successful compensation**. The first recovery also
failed; `Restart=on-failure`, `RestartSec=5s` and the worker's non-waiting
recovery branch account for the later automatic attempt. That built-in retry
occurred within the existing test; it is not an investigator-triggered rerun.

The initial stop-to-worker-error interval is about 1.3 seconds, and the
start-to-error interval about 0.3 seconds. Neither a newly started 30-second
private-socket deadline nor a full shared-readiness deadline explains that
sequence. Prioritize an **immediate exception** and separate forward failure
from first recovery failure. If the first shared start was forward, recovery's
pre-stop inventory/restart-safety check against a still-starting launcher is a
concrete secondary boundary; the excerpt shows no intervening second stop.
The original exception and start direction are absent, so this is not a root
cause finding or justification to relax ownership checks.

The same query-string model refresh 403 appears in the passing run at line
4059, followed by successful `applied` polling at 4075 and completion of the
foreign-cgroup subtest at 4126. In the failed snapshot its visible occurrence
is **after** the worker's error. The fixture matches raw HTTP paths, so the
query-bearing native refresh differs from the successful exact-path preflight.
The 403 is not evidence for this failure; do not change the fixture based on it.

The completed `runtime-amended-flake.log` adds no original exception beyond
that snapshot. It contains 536 observations of terminal `failed/shared-start`
(lines 4250–8005), followed by the `wait_phase("applied")` assertion's action
timeout at 901.46 seconds (8007–8014). The test then cleans up QEMU normally and
Nix reports only the failed `checks.x86_64-linux.session-recovery-boot`
derivation in its final error. `runtime-amended-flake.status` records
02:44:49–03:21:32 +02:00, exit 1. The 900-second test poll is a **secondary
failure-reporting delay**, not the original provider failure or a daemon-health
timeout. Later deliberate shared-start-failure and reboot subtests were not
reached. The lead reports no local kernel build.

Separate `runtime-amended-browser.status` is exit 0, and its log records
`TestNotificationsBrowser` passing in 9.07 seconds: Chromium synthetic worker
receipt with zero tabs and Firefox template/CSP/permission/worker-route checks.
This is independent browser regression evidence, not provider-switch evidence
or physical OS notification-display proof.

## Notification-monitor interaction

The provider and VM files are unchanged versus passing `e414ed31806d2b91620d5e5fad8b5b5ee56e07ac`.
The complete eight-file diff also leaves notification loop/observation behavior,
activity monitoring, helper implementation and native dependency pins unchanged:
the notification Go delta adds deletion-only cleanup, and the transport delta
adds the exact Chromium staging host. That narrows the incremental change but
does not prove the full feature unrelated to a timing failure.

More specific execution evidence:

- Notification reconciliation calls `requireCurrentHostProfile`, which includes
  provider admission. Applying/recovery reservations stop a new reconciliation
  pass (`notifications.go:68–79`, `server.go:875–880`,
  `codex_providers.go:108–129`). This is a state read, not a provider mutation.
  An already-started pass can cross admission; it does not become a native
  writer through this path.
- `observeAttention` reads owned session identity, cached activity snapshots and
  cached prompts; it performs no thread resume (`attention.go:165–235`). The
  separate existing activity monitor starts native observers only for owned
  sessions (`activity.go:195–234`). The fixture supplies none.
- An empty outbox makes `sendNext` return before Web Push/network work. Fresh
  notification state starts with empty registrations and outbox
  (`notifications.go:150–176`, `notifications_store.go:67–83`). No browser API
  action exercises the amended disable handler or provider allowlist here.

There is no concrete native-read/resume or push-egress collision identified in
this fixture. Normal process startup and filesystem overhead still exist; source
identity or the empty fixture alone cannot establish the cause of a transient
failure. Do not disable the monitor or change timeouts based on this evidence.

## Accepted fixture-only diagnostic brief

Lead direction supersedes the earlier product-logging suggestion: prepare one
standalone diagnostic VM, with **no product source, pin, host-module or live-host
changes**. The existing failed result remains authoritative. Instrumentation is
temporary evidence collection, never a substitute for the original check.

**Files and exact inputs.** Implementer prepares a small session-owned
`recovery-diagnostic/` bundle: wrapper flake/lock, copied VM fixture, Ruby raise
observer and short provenance/readme. Reference the original full b8a6 revision
and its existing locked inputs; use its `nixosModules.host`, its pinned nixpkgs
and `packages.x86_64-linux.dev-workspace`. Do not call `mkPackage` with the
diagnostic directory as source. Before execution require the product output to
equal the original logged package:
`/nix/store/54cv3sm4z10nal6hi4p214vds9cmjddd-dev-workspace-0.2.0`.
Record original and diagnostic derivation identities. If that equality fails,
stop and resolve source provenance; do not silently rebuild a different product.
The wrapper exposes only a named diagnostic VM check, imported with the original
`self`, `pkgs` and `devWorkspace` arguments. Build that attribute alone, not the
original full flake. The existing product closure is reused; only the diagnostic
VM/driver/probe needs realization. Keep all original product/config pins frozen.

**Scenario.** Copy the original node configuration, synthetic provider and setup
through the first foreign-cgroup subtest. Preserve native package, services,
provider URL/path behavior, provider request UUID, foreign-process injection,
waiting/blockers assertion, process removal, `applied`/active-pool assertion and
service checks. Exclude subsequent deliberate-failure/reboot scenarios from this
standalone run. Do not add sessions, subscriptions, sleeps or provider retries.
Keep original VM resource defaults and provider ownership/readiness timeouts.

**Attachment.** Put the probe in the diagnostic VM store closure explicitly
(for example alongside `devWorkspace` in `virtualisation.additionalPaths`).
After original registration/setup and before the first provider request, install
a fixture-user drop-in for only `workspace-codex-provider@fixture.service` with
`Environment=RUBYOPT=-r<probe-store-path>` and reload that user manager. Preserve
ExecStart, Restart, RestartSec, KillMode and every product unit. No shared-native
daemon/portal instrumentation or user-manager-wide environment change.

This attachment is source-supported: `nix/workspace-portal.nix:386–423` replaces
the Ruby shebang and wraps PATH/mode/catalog variables without clearing RUBYOPT;
the worker unit runs the packaged `workspace-host run-provider-worker fixture`.
The probe must first require that exact argument pair, host mode and fixture UID.
After loading, remove only its own injected RUBYOPT value from the worker's child
environment, restoring the fixture's original absent value; do not erase any
pre-existing unrelated Ruby options. Emit one fixed observer-active marker with
PID so coverage across automatic worker restarts can be established.

**Raise observation.** Use Ruby `TracePoint.new(:raise)` to observe exceptions
before existing rescues discard them. No monkey-patched methods, intercepted
returns, additional subprocesses, state mutations or exception replacement.
Filter events to the active call stack containing the original packaged provider
apply/recover methods; ignore normal waiting-loop exceptions. Prefer recovery when both appear
because recovery is nested under apply. Retain safe source frames from the exact
package's provider Ruby and host wrapper files, mapping paths to fixed basenames
and line numbers. This identifies readiness, process-identity, helper-capture,
private-start and recovery-pre-stop boundaries without tracing every line.

Each record contains only a fixed prefix, PID, sequence, monotonic time since
observer load, forward/recovery direction, exception class, numeric errno when
available, and at most six allowlisted source frames/method names. A small fixed
category mapping may recognize known internal errors; never emit the raw error
message, `inspect`, `full_message`, arbitrary locals, argv, URLs, token paths,
snapshots or RPC payloads. In particular `capture!` errors embed argv/stderr and
must remain opaque except for their category/call site. Class/source location
may narrow a helper failure without proving the underlying protocol cause;
report that remaining limitation rather than broadening the observer.

Bound output to 64 records of at most 768 bytes per worker process, at most two
occurrences per direction/class/call-site signature (including the provider
caller, so different helper steps stay distinct), with one truncation marker.
PID/time distinguish the first recovery from a restarted worker. The original
900-second scenario deadline bounds worker restarts; do not change their policy.
The callback does no filesystem/process probes. It writes one sanitized record
to stderr and returns; internal observer failure disables observation with a
fixed marker and must not raise into product execution. Verify the original
exception continues to the same rescue. Observation adds timing overhead: a
non-reproduction cannot exonerate a timing bug.

**Failure collection.** The copied driver polls the same state assertion but
returns an unexpected terminal `failed`/`canceled` to Python so Python raises
immediately. A different nonzero exit fed to `wait_until_succeeds` would still
poll for 900 seconds. Preserve waiting/applying/recovery-required handling and
the original outer deadline; recovery-required can still be compensated by the
existing worker. On terminal failure or timeout, collect at most 64 KiB of the
relevant fixture worker/native-service journal window and selected systemd
ActiveState/SubState/MainPID/Result/ExecMainStatus/restart-count fields. Print
only allowlisted operation metadata and thread/loaded/terminal counts from
validated fixture snapshot paths. Do not print environment or raw state files.
Report the original assertion as failed after collection. Normal VM test-driver
cleanup owns the disposable VM; no host/session cleanup is part of this brief.

**Preparation and one run.** Before launching, inspect the copied-fixture diff
and pinned-input/package identity, syntax-check the probe, and use the same
Ruby interpreter on a tiny synthetic nested-rescue example to verify forward
and recovery event separation, exact worker guard, output caps, secret-canary
omission and unchanged exception propagation. These are fixture quick checks,
not product tests. The lead assigns preparation and the applicable review,
then a fresh utility watcher executes one named diagnostic VM check; architect
executes nothing. Preserve its command, status, provenance, bounded trace and
assertion result. Reproduced failure with a usable original raise is diagnostic
evidence; terminal failure without observer coverage remains inconclusive;
`applied` means the failure did not reproduce. None changes the original failed
suite to pass. Refer any proposed product/fixture remedy back to the lead after
this evidence, with ordinary substantive-change review and final checks.

Acceptance for this investigation is evidence locating the original failing
boundary and explaining its cause or the precise missing observation. Until
then, retain the failed local check as unresolved; CI/native passes and a future
green rerun alone do not resolve it. Any consequential remedy goes through the
lead and affected committed-change review before longer verification. No change
to deployment/recovery policy, persistent formats, frozen pins or feature design
is proposed by this brief. Lead owns tracking/artifact registration and the next
verification assignment.

## Follow-up after the single diagnostic run

Session identity/environment and the retained architect roster were reverified.
Read-only inspection covered the original failed/passing logs, the diagnostic
result/provenance/check log, its observer/fixture and preparation evidence.
All original inputs, results, product sources and pins remain untouched.

**Established evidence.** `recovery-diagnostic/run/status` records exit 0 from
03:45:33 to 04:05:43 +02:00 (20m10s). `run/provenance.json` equals the final
evaluated provenance and names the original product output and derivation,
original check derivation, full b8a6 revision and original nixpkgs revision.
The wrapper imports the original host module and package; this was not a
substitute product build. `run/check.log:1703` shows the observer active in PID
1855 before the switch; lines 1740–1743 show the shared daemon stop/start,
1826 the successful first scenario, and 1831 `observed-no-raises`, with zero
disabled/truncation records. The VM script itself lasted 261.47 seconds; the
20m10s command duration is not provider-switch latency.

`run/result.json` correctly calls this `applied-nonreproduction`, retaining
`originalFailedSuite: unchanged-unresolved` and `rootCause: unproved`.
“No raises” means no events matching the observer's apply/recover stack filter;
normal waiting-loop exceptions are intentionally excluded. The preparation's
synthetic checks cover nested forward/recovery raises, propagation, guards and
output limits. No concrete missing marker, wrong package, disabled observer,
truncation or filtering defect is evidenced. A successful path does not exercise
the original failure, and TracePoint plus fixture setup can affect scheduling.

**No new root cause.** The original run still lacks the original forward
exception and first compensation exception: their classes, precise call sites,
failed helper action and native process state at those instants are unknown.
The final recovery state cannot reconstruct them. An immediate process-identity
lookup/service-state error, helper failure or state I/O failure remains possible
from source; none is established. The first error's short timing still excludes
a full 30-second readiness timeout. There is no evidence to assign the failure
to notification observation, host resource pressure or a particular race.

Two conspicuous messages do not distinguish the failed run: the native
query-string model refresh 403 occurs in the diagnostic as well
(`run/check.log:1759`) and in the older passing run. The setup-time portal
stop timeout/SIGKILL also occurs in all three logs (failed lines 4030/4033,
older passing 3896/3899, diagnostic 1577/1580), before their provider scenarios.
These observations do not prove those behaviors harmless in every context;
they provide no basis for treating either as this failure's cause or widening
this investigation into their repair.

**Recommendation for lead decision.** Do not repeat or broaden the fixture-only
probe merely to seek a failure. Its intended observation was present; no missing
data resulted from a reproduced failure. Extra line tracing, process polling,
delays or stress would add timing effects without a selected hypothesis. A
revised fixture is justified only if a concrete coverage defect or failure
boundary is later identified. Neither fixture revisions nor durable diagnostics
can recover the already-discarded exceptions from the original run.

The smallest useful substantive next change is **safe failure diagnostics owned
by the provider recovery path**, plus prompt failure reporting in its existing
VM test. This fixes an established observability defect, not the unproved
provider failure. It requires a separate lead implementation decision; the
completed exact-package diagnostic and frozen composition remain evidence.

Proposed implementation boundary:

- `libexec/workspace-codex-providers.rb`: before the existing apply/recover
  rescues replace the error, emit one bounded structured stderr record for each
  escaping forward/recovery failure. Include validated operation UUID, direction,
  existing stage, fixed step name, monotonic elapsed time, allowlisted exception
  class/errno and a few package-relative source frames. Keep the two failures
  separate. Use transient context to distinguish shared start, readiness,
  recovery inventory/safety, private resume and verify; do not persist steps or
  modify operation stages. At a readiness failure summarize the last already-read
  MainPID/ActiveState, executable-match/socket booleans and health error category,
  marking unavailable observations explicitly. Remember only the last health
  error; emit no per-poll logs. No extra subprocess/readiness probes are needed.
- Keep logging local to that provider file, with a small fixed-size projection
  (at most 2 KiB per failure). Exclude messages, arbitrary backtraces, argv,
  helper stdout/stderr, filesystem paths and state/payload contents. `capture!`
  includes argv/stderr in its error, so do not print it or change the generic
  host command API to expose it. A helper failure can initially be located by
  step and source category; that may still need separately designed, finite
  helper diagnostics if it is the actual failure. Logging failure must not
  replace either original exception or affect compensation.
- `test/workspace_host/codex_provider_test.rb`: extend existing apply/recovery
  and shared-readiness failure cases to prove separate safe diagnostics and
  unchanged outcomes. `nix/tests/session-recovery-boot.nix`: apply the diagnostic
  fixture's terminal-result return-to-Python technique and bounded fixture
  journal/state-count collection to the existing test. An unexpected terminal
  failure must fail immediately; recovery-required remains nonterminal and the
  existing later compensation/reboot scenarios remain intact. Collect safe
  fields, never raw runtime snapshots. `docs/codex-providers.md`: briefly explain
  where these diagnostics live and their limits.

Invariants and compatibility: retain native ownership proof, service order,
locks, 30-second readiness deadline, health retries, restart policy, terminal
restoration and recovery-required fencing exactly. No provider/notification
behavior change, new process, TracePoint in the product, schema, state field,
receipt, wire/API/CLI-success-output change or migration. Only diagnostic stderr
is additive. Existing state and old/new helpers remain compatible. A future
approved package update follows normal forward-only selection; no special
deployment, pin update or live-host action is part of this proposal. Recovery
from a logging defect uses a corrected successor without editing provider state.

Quick checks, if assigned: fault-inject distinct forward and recovery errors
and verify both records survive while state/service-call order is unchanged;
cover immediate identity lookup failure and health timeout with last-category
reporting, secret-canary omission/unknown-error fallback/output bounds, and a
failing diagnostic sink that cannot change compensation. Verify the VM wait
returns unexpected terminal results to Python and preserves expected recovery
phases. Use the repository's declared Ruby/Nix environment. After committed
quick checks and affected independent review, a fresh lead-assigned watcher can
run the original full recovery VM once on the new diagnostic-capable package,
including its deliberate failure/reboot cases. That is verification of a new
observability change, not a blind retry of b8a6. A passing result proves neither
the original root cause nor its repair; keep the original failure unresolved
until a diagnostic recurrence establishes its cause or another concrete causal
proof exists. Wider
suite/deployment decisions remain with the lead.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
