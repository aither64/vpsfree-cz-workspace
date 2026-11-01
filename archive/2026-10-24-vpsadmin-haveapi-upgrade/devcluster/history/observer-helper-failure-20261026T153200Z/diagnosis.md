# Read-only observer helper failure

The fresh Luna/low observer's helper exited 125; this does not establish failure
of the parent's native start. Original driver 1830a590, observer artifacts,
identity and actual-policy proof are preserved here. No code was changed during
this diagnosis and neither helper main nor startup was retried.

Original observer evidence confirms workspace PWD and both session environment
values matched. Individual checks at 15:38:32 UTC confirm attempt/scope identity,
existing populated cgroup, 32 GiB / 12 CPU limits, zero OOM counters, four scope
PIDs and no process-read exceptions. The native result file was absent. These
observations do not establish guest readiness or native completion.

The exact failing path is `observe()` line 101, which calls canonical public
native status through `captured()`; line 39 rejects every nonzero result. The
selected runtime's public command returns generic exit 1 while this operation
is locked. A read-only call to the current installed public provider returns
75 with no stdout/stderr, the runtime contract's documented busy code. Native
status uses a nonblocking exclusive per-cluster lock, also held by the parent
start (`lib/runtime.sh:836`, `:899`). The runtime wrapper does not preserve that
provider exit code in this public CLI error. Thus ordinary busy observation
becomes the helper's generic 125. No secret or raw native status was dumped.

Proposed bounded correction, awaiting lead disposition: in `observe()` only,
defer canonical public native status while the exact owned attempt lacks
`result.json`; report native status unavailable during parent start, with
readiness unknown. Continue cgroup/tuple/accounting/kernel observation. After
result exists, run unchanged strict canonical status and retain all errors.
Do not weaken global `captured()`, assume all exit-1 errors mean busy, bypass
generation checks or change native/provider/resource behavior. A synthetic
missing-result check should prove no native status invocation; completed-result
checks should preserve strict status success/error behavior.

Evidence: [individual checks](individual-checks.json), [provider return](provider-check.json),
[public refusal classification](public-refusal.json), preserved observer outputs.
Parent handle 72217 remains lead-owned; no startup, signal, stop, reset, scope
teardown, source/lock/host/foreign/lifecycle mutation or new utility occurred.

Lead released the proposed correction after diagnosis. Only `observe()` was changed: missing owned result defers native status with readiness null; present result retains strict canonical status/error behavior. Focused synthetic checks pass, and one authorized read-only observation completed exit 0. Exact facts are in `corrected-one-shot-observation.json`; startup remained in progress, without native result or runner PID. This does not establish readiness or native completion. No additional watcher, native invocation or signal occurred.
