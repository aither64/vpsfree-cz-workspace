# 2026-09-02-kb-runtime-reliability

## Goal

Make vpsAdminOS test-framework consumers tolerate a small set of demonstrated
transient APT, APK, and Guix external-service failures without hiding genuine
failures or requiring helpers inside guest containers.

Keep the current Guix image strategy: build from a revision for which upstream
Guix reports substitutes, and keep test-induced builds minimal. Do not operate
a vpsFree.cz Guix mirror or substitute cache in this initiative.

## Affected repositories

- `vpsadminos`
  - add a generic, classified, observable retry primitive to the test
    framework;
  - package conservative APT and Guix classifiers with test-runner;
  - expose `container_apt_get` so test consumers do not repeat command
    construction, native retry settings, classification, or backoff;
  - expose `container_apk` with classified APK v2/v3 transport retries and
    migrate every direct Alpine test operation;
  - migrate its Docker, Incus, Podman, and Snap APT setup phases;
  - add focused driver and classifier coverage.
- `vpsfree-kb-contracts`
  - use the packaged classifiers for firewall and KVM APT operations;
  - use it to make the Guix channel/time-machine preparation retry short-lived
    upstream failures before running long reconfigure/deploy operations.

The fetched default branches of all direct workspace consumers were checked:
`confctl`, `terraform-provider-vpsadmin`, `vpsadmin`, `vpsadminos`,
`vpsf-status`, `vpsfree-irc-bot`, `vpsfree-kb-contracts`, and `web`. Only
`vpsadminos` and `vpsfree-kb-contracts` contain matching direct test
operations. Only `vpsadminos` contains direct APK operations.
`vpsadmin-kb-captures` is a duplicate clone of
`vpsfree-kb-contracts`, not a separate consumer.

The managed-page workflow and test-selection policy are out of scope. The full
runtime suite will continue to run as it does now.

## Approach

### Test-framework primitive

Add a bounded block-level retry helper to the vpsAdminOS test evaluator. The
helper stays outside the VM/container and reruns the supplied operation, which
can be a complete command such as `osctl ct exec ...`. Nothing has to be
installed or distributed inside guest images.

The helper must:

- require a positive attempt count;
- accept a predicate which explicitly classifies an exception as retryable;
- support a fixed delay or caller-provided backoff;
- raise an unclassified failure immediately;
- raise the last failure when attempts are exhausted;
- emit the operation name, attempt count, exception class, and concise reason
  before every retry so recovered flakiness remains visible in CI logs.

Ship `TestRunner::RetryClassifier` with test-runner. Its `apt`,
`guix_operation`, and `guix_preparation` methods return a concise retry reason
only for a recognized terminal transient failure and return `nil` otherwise.

Do not use `wait_until_succeeds` for this purpose. It is a polling primitive
which repeats every non-zero result until a deadline. The existing
`succeeds_with_retries` also retries all non-zero exits without classification.

### APT

Wrap every direct Debian/Ubuntu package operation found in vpsAdminOS's Docker,
Incus, Podman, and Snap tests and in the KB firewall and KVM suites. Add APT's
native `Acquire::Retries` to test-only commands and use the outer framework
helper for known mirror-publication and network failures, including the
observed `File has unexpected size ... Mirror sync in progress` failure.

Callers use `container_apt_get` with the host machine, container id, apt
arguments, operation name, optional environment, and timeout. The helper owns
safe command construction and APT's native retries. It delegates the
conservative classifier, three outer attempts, progressive backoff, and retry
logging to `retry_apt_operation`, which is also available for opaque,
byte-stable fixture execution.

Keep executable KB documentation fixtures byte-for-byte unchanged. Retry the
host-side fixture invocation so page hashes and reader-visible commands remain
stable.

Dependency, signature, configuration, package-not-found, and other
unclassified errors must fail on the first attempt.

### APK

Wrap every direct Alpine APK update/install operation in vpsAdminOS tests with
`container_apk`. The helper owns shell-safe `osctl ct exec` construction,
non-interactive operation, a 60-second native no-progress timeout, and three
classified attempts with progressive backoff. Global APK options are placed
before the operation for APK v3 compatibility.

Classify only terminal APK v2/v3 diagnostics for transient DNS, connection or
no-progress timeouts, connection failures, network unreachability, and HTTP
408/500/502/503/504 responses. Mixed output and all signature, TLS,
repository, missing-package, solver, integrity, hook, and package-script
failures remain terminal. Do not classify a test-runner `OsVm::TimeoutError`.

Split the stateful ZFS ugidmap ACL test around `apk add acl`, so only the
package operation can be retried. Image builders remain outside this helper.
DNF/YUM retries are deferred until a real transient failure is captured across
DNF4 and DNF5. Portage is deferred because it has no direct test-framework
consumer and already has downloader, mirror, and resume recovery.

### Guix

Keep using the channel revision recorded in the Guix image, which the image
builder selected through upstream substitute availability. Before the long
reconfigure/deploy examples, run a small `guix time-machine ... describe`
preparation command with bounded retries. This isolates channel checkout and
time-machine profile preparation from the system operation and populates the
container's local Guix caches.

Classify only demonstrated upstream Git, DNS/transport, substitute-download,
and Software Heritage fallback failures. Use a short per-attempt timeout for
the preparation command so a stalled Software Heritage vault request does not
consume the existing two-hour system-operation timeout. The long system
operations retain their current timeout and are not blindly rerun after an
unclassified build or configuration failure.

## Compatibility and deployment

- The retry helper is additive and does not change existing
  `succeeds_with_retries` or polling behavior.
- Changes affect tests only. They do not alter vpsAdminOS runtime protocols,
  persistent state, published container formats, or production deployment.
- No coordinated vpsAdminOS node update is required.
- Guix continues to trust and consume upstream channels and substitutes. No new
  endpoint or signing key is introduced.
- Retrying an `osctl ct exec` block does not require mixed-version support in
  the guest. Commands used here are idempotent package metadata/profile
  preparation operations.
- APT, APK, and Guix calls inside production image-builder scripts are
  excluded.
  Those scripts run outside test-runner, and replaying an enclosing image test
  is not a safe substitute for builder-level recovery.

## Testing plan

### vpsadminOS

- Cover immediate success, classified recovery, unclassified failure,
  exhaustion, retry delay/backoff, and visible retry reporting in the driver
  tests.
- Cover positive APT/APK/Guix diagnostics and mixed-output permanent failures
  in focused classifier specs.
- Run repository formatting/lint checks and Overcommit.
- Run one representative direct consumer, `podman/debian#latest`; rely on the
  repository CI suite for the remaining Docker, Incus, Podman, and Snap matrix.
- For APK, run only `docker/alpine#latest`, one cgroups-v2
  `kernel/vpsadminos` script, and `zfs/ugidmap`; rely on CI for the remaining
  direct consumers.

### vpsfree-kb-contracts

- Run repository checks and tests for managed-page sources.
- Evaluate/list the affected scripts against the updated vpsAdminOS worktree.
- Run `kb/firewall#iptables` as a representative downstream APT sample; rely
  on managed runtime CI for the remaining firewall, KVM, and Guix scripts.

After quick local verification and commits, run the mandatory change review
before long integration tests.
