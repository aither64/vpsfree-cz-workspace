# 2026-09-02-kb-runtime-reliability

## Goal

Make the managed KB runtime suite tolerate a small set of demonstrated
transient external-service failures without hiding genuine failures or
requiring helpers inside guest containers.

Keep the current Guix image strategy: build from a revision for which upstream
Guix reports substitutes, and keep test-induced builds minimal. Do not operate
a vpsFree.cz Guix mirror or substitute cache in this initiative.

## Affected repositories

- `vpsadminos`
  - add a generic, classified, observable retry primitive to the test
    framework;
  - add focused driver coverage for the primitive.
- `vpsfree-kb-contracts`
  - use the primitive around the demonstrated APT mirror-publication race;
  - use it to make the Guix channel/time-machine preparation retry short-lived
    upstream failures before running long reconfigure/deploy operations.

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

Do not use `wait_until_succeeds` for this purpose. It is a polling primitive
which repeats every non-zero result until a deadline. The existing
`succeeds_with_retries` also retries all non-zero exits without classification.

### APT

Wrap only the Debian/Ubuntu package preparation used by the firewall runtime
tests. Add APT's native `Acquire::Retries` for transport retries and use the
outer framework helper for known mirror-publication and network failures,
including the observed `File has unexpected size ... Mirror sync in progress`
failure.

Dependency, signature, configuration, package-not-found, and other
unclassified errors must fail on the first attempt.

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

## Testing plan

### vpsadminOS

- Cover immediate success, classified recovery, unclassified failure,
  exhaustion, retry delay/backoff, and visible retry reporting in the driver
  tests.
- Run repository formatting/lint checks and Overcommit.
- Run the focused vpsAdminOS driver test through the current test runner.

### vpsfree-kb-contracts

- Run repository checks and tests for managed-page sources.
- Evaluate/list the focused `firewall` and `guix` scripts against the updated
  vpsAdminOS worktree.
- Run all three APT-using firewall scripts (`iptables`, `nftables`, and `ufw`)
  plus `kb/guix#reconfigure` as focused integration tests.

After quick local verification and commits, run the mandatory change review
before long integration tests.
