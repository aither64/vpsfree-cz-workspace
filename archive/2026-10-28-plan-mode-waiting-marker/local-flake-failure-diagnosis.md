# Local source flake failure diagnosis

Implementer0, 2026-10-29. Read-only diagnosis; no source edits, reruns,
cancellation or ownership transfer. Lead/source utility owns the completed
batch. Exact-head upstream CI passed as reported by lead (run 40923422808,
head 5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3); this is independent evidence,
not an explanation of this local failure.

## Concrete failure

Exact failed derivation:
`/nix/store/vz97cs3j9qy94sv4pa1z0pqqgfp2ad4f-vm-test-run-dev-workspace-session-archive-lifecycle.drv`.
Full retained Nix log: [archive-lifecycle-failure-full.log](logs/archive-lifecycle-failure-full.log).
Extracted once using nix log, no repeated live polling.

The first archive subtest, "preflight lead repair survives portal restart before
agent shutdown", failed before clicking Archive or issuing a lifecycle POST.
The browser diagnostic says phase `open page`, errors `[]`.
`archive_lifecycle_browser.cjs:31` waits for a GET response from the exact
`/api/sessions/2026-10-25-lead-archive-repair/operation` endpoint concurrently
with page.goto. Playwright reports `page.waitForResponse: Timeout 30000ms
exceeded while waiting for event "response"` (full log lines 1274–1277).
The script exits 1; VM wrapper RequestedAssertionFailed and normal QEMU cleanup
follow. This is an actual existing deadline failure, not an inferred quiet-time
hang or production archive failure.

The trace records page 200, all app/Codex JS imports 200, first attention and
coordination 200, and notification settings 200. It has no JavaScript page errors,
no operation response and no archive POST. Later outstanding read requests show
ERR_ABORTED while the browser is closing; those aborts cannot prove the cause.
The trace records responses/failures, not request admission/timing, so it cannot
distinguish a browser-queued operation fetch from a server-side delay.
The browser invocation spans guest monotonic 168.608–252.785 seconds; its
internal operation-response deadline remains 30 seconds. This does not by itself
prove host load or any product deadlock.

## Source boundary and classification

The exact store test script SHA-256 matches source:
`4ef95ca08155f15a233a963f2f8c1bbb223ec21fdeb6c681dd98ea2dc5c8a45b`.
`test/archive_lifecycle_browser.cjs`, its Nix VM definition and static/app.js
are unchanged from base cc0d452a0653a112c8a013492c1734d9554bb909.
App.js installs lifecycle handlers then calls client.operation() around line
4364. There is no awaited unrelated network request between initializing that
client and invoking the lifecycle read. Network reads started earlier can remain
in flight. The request route goes directly to lifecycleStatus; it publishes
coalesced display-refresh demand and reads cached operation state, tracking-sync
and archive progress, rather than awaiting native turn/history or attention.
The feature diff changes only passive attention identity consumption and pinned
library metadata. Its completed source regression suites pass; exact-head CI
archive acceptance also passed. No changed lifecycle path explains this failure.

Classification: initial lifecycle hydration timed out in the local VM browser;
root transport/scheduling cause is unresolved. Concurrency/environment is a
supported hypothesis, not proven: the same local flake batch launched four VM
checks, while exact-head CI archive acceptance ran independently and passed.
No CPU/network timing sample or in-flight operation diagnostic was retained.
Do not label the failure fixed, unrelated with certainty, or accepted merely
because a later rerun passes.

## Exact output accounting

Evaluated the committed final flake's named check drv/output paths and queried
local store validity, without building. Full receipt:
[dev-workspace-check-output-inventory.json](logs/dev-workspace-check-output-inventory.json).
All 25 other named check outputs are valid, including package, complete Ruby
verification aggregate, host-module-idempotency and contract/catalog checks.
The Ruby aggregate receipt establishes successful unique shard coverage for its
exact existing derivation; no inference from partial console text was used.

Three outputs are invalid/unrealized:

- session-archive-lifecycle: concrete failed derivation above, output
  `/nix/store/dl2zyvy4q9n2yj76yw1q94x041zna1ym-vm-test-run-dev-workspace-session-archive-lifecycle`.
- session-creation:
  `/nix/store/syy3qnjfyynbc7bhwv36jlch9haycgld-vm-test-run-dev-workspace-session-creation.drv`,
  output `/nix/store/i9zd1xghwiy21sxrp03ql64rpjnj8cj0-vm-test-run-dev-workspace-session-creation`.
- session-recovery-boot:
  `/nix/store/jbwvzym25xppgjlnqwd6rnva9h5fagdz-vm-test-run-dev-workspace-session-recovery-boot.drv`,
  output `/nix/store/0wj41qx9r4wgc3g1cm3w0nypk5ww588h-vm-test-run-dev-workspace-session-recovery-boot`.

Creation and recovery have no terminal-success receipt in the batch log. They
are incomplete, not failed based on intermediate output and not successful.
Recovery's interim AssertionError occurs inside its documented
wait_provider_result predicate polling until expected/terminal state; it is not
by itself a terminal test failure. Source utility reports the batch ended and
no owned process remains. Host idempotency output
`/nix/store/apfrvraxc5szzskp68bigip5i0i3vypr-vm-test-run-dev-workspace-host-module-idempotency`
is valid, with script-finished/cleanup log evidence.

## Shortest next check proposal

No source change is justified by retained evidence. When the utility slot is
free and the lead authorizes the next operation, isolate only the exact failed
existing derivation, without extending Playwright's original 30s deadline:

```sh
nix build --no-link --print-out-paths --print-build-logs --max-jobs 1 \
  /nix/store/vz97cs3j9qy94sv4pa1z0pqqgfp2ad4f-vm-test-run-dev-workspace-session-archive-lifecycle.drv^out
```

This controls same-command VM concurrency while keeping source/inputs and
acceptance contract exact. Stopping condition is the existing VM/test contracts:
pass and valid output, or first test failure with its existing diagnostics and
normal cleanup. No generic quiet timeout or cancellation is proposed. Run no
other successful check again. Keep interrupted creation/recovery coverage
explicit until lead chooses those existing exact derivations separately.
If isolated failure recurs at hydration, stop reruns and request a small
fixture-only diagnostic amendment: record initiation and terminal phase for
this exact operation request, plus bounded page hydration state. This would
require lead/package review coordination; do not add generalized instrumentation
or raise the deadline. Passing isolation plus existing exact-head CI narrows the
environment hypothesis but does not retroactively prove host load.

## Driver-only dependency preparation

The later isolated archive run needed to rebuild supporting package/Ruby inputs
that had become unrealized. Read-only metadata inspection established that
`checks.x86_64-linux.session-archive-lifecycle.driver.drvPath` is exactly
`/nix/store/pjg4h0rx53b2ga7v2ylm7sd5im2mr36q-nixos-test-driver-dev-workspace-session-archive-lifecycle.drv`.
Its buildCommand type-checks and lints the Python script, copies it and wraps
`nixos-test-driver`; it does not invoke the acceptance driver. Its recursively
inspected graph has 6070 derivations and no `vm-test-run` derivation. The
acceptance derivation `vz97cs3j9qy94sv4pa1z0pqqgfp2ad4f` is a separate consumer
that invokes the wrapped driver with `-o $out`.

Lead accepted this exact dependency-preparation command:

```sh
nix build --no-link --print-out-paths --print-build-logs --max-jobs 4 \
  /nix/store/pjg4h0rx53b2ga7v2ylm7sd5im2mr36q-nixos-test-driver-dev-workspace-session-archive-lifecycle.drv^out
```

It shares Nix output identities/locks with the already owned archive run and
can prepare missing dependencies concurrently without launching another
acceptance VM. The existing archive owner retains `--max-jobs 1` and the original
30-second browser contract. The lead launched preparation through the documented
parent capacity fallback while the single utility slot was occupied. Implementer0
performed metadata reads only and did not launch, cancel or take ownership of any
build. This scheduling change does not certify acceptance or explain the original
hydration failure; final command outcomes remain with the lead's receipts.
