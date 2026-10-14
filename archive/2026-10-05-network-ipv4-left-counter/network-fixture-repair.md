# Bounded fixture repair, 2026-10-06

Prepared from the lead's direct verification brief. No commands below have run.
No application admission code, W adapter, copy, schema or pin changed.

## Evidence

- `post-review-sql-admission.log:1016`: the parallel example fails while creating
  a chain without its required STI `type`, before admission. Four other tagged
  examples passed.
- `ci-current-core-foundation.plain.log:4225` and
  `ci-current-full-foundation.plain.log:4413`: the same first fixture failure.
  Subsequent concurrency failures are before-hook duplicate `192.0.2.248`
  allocations. Core seed 36954 also selected public IP 352 instead of fixture
  375 in the Create batch case (line 4590).
- `review-original-ci-api-failed.log:4630`: original full seed 16926 has the same
  type failure followed by duplicate pool address failures at line 4803 onward.
  Original core seed 60623 failed only the type fixture. The later original
  full quota failures are not diagnosed or changed by this packet.
- `api/spec/support/storage_chain_spec_helpers.rb:126` supplies the established
  typed chain fixture and initializes its lock arrays and destination chain.
  The former manual fixture supplied neither its type nor all lock state.
- HaveAPI 0.29.8 `lib/haveapi/action.rb:213` describes actions with method, scope,
  input, output and other metadata. `lib/haveapi/server.rb:775` selects the OPTIONS
  action using `method=PUT`. The former W fixture returned only `input`; the
  generic unwrapping in `src/lib/api/haveapi.ts:234` treated that sole key as a
  namespace. The current test fixture retains real action metadata and asserts
  the requested method and the rendered enabled checkbox before interaction.

## Draft scope and limits

The concurrency spec reuses the typed chain helper. Its teardown joins every
connection thread without allowing one failed join to skip remaining joins or
cleanup. It captures created pool identity immediately, restores original seed
availability and affected quota rows, and checks after every example that owned
allocations/hosts/pool are gone, reservations did not survive, and seed allocation
attributes and quota state match their original values. Worker errors still fail
the example after cleanup. The exact old leak path remains unproven; the new
checks are intended to make a remaining isolation fault visible at its owner.

W changes only `e2e/specs/admin/network_availability.spec.ts`. Both modern and
old-API fixtures now have method, scope, input and output metadata. Both assert
the OPTIONS query selects PUT; the old-API test waits for that successful lookup
before testing unsupported-field omission. No UI prose changed.

## Frozen proposed execution

The lead should inspect the wrapper and manifest, then give a fresh verification
watcher this single command from the bound tracking directory:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/run-network-fixture-repair-quick1.sh
```

It stops at the first failure, preserves separate new logs/exits, and does not
retry. It checks scoped Ruby syntax/RuboCop in the declared root shell, all 13
concurrency and 5 Create examples in isolated core/full MariaDB processes at the
current failing seeds 36954/9346, then the W full `ci:quick` gate for the adopted
browser source. This is a bounded two-file API reproduction, not a full
foundation rerun. The spec assertions check fixture restoration on each example,
regardless of its position in the randomized order.

Browser reruns remain a separate lead-owned operation using the already resolved
locked Chromium setup. No browser, build, CI, commit, rewrite, push, pin or
lifecycle operation is launched by this packet.
