# 2026-10-24-context-copy-performance-tests

## Goal

i'd like to fix haveapi issue described here:

```
HaveAPI repeatedly copies the **entire API description while rendering individual example tabs**.

The initial context owns a frozen copy of the description. But deriving a context for one language or action calls:

```ruby
def with(**changes)
  self.class.new(**all_existing_fields, **changes)
end
```

That constructor recursively copies everything again—including the complete resource/action/parameter tree—even when only the language profile or sample changed.

The renderer does this while checking each language’s availability, then again while rendering its panel, repeatedly across the page. Rust also repeatedly traverses and normalizes the description.

For one administrator request we measured:

| Work | Time |
|---|---:|
| Entire request | 102.4 seconds |
| 639 context derivations | 88.8 seconds |
| Process CPU | 102.3 seconds |

So most time goes into copying objects and associated allocation/garbage collection. It is not waiting for the network or compiling Go/Rust clients.

**These measurements came from our local API test environment, not production.** An earlier uninstrumented run was also extremely slow, supporting the diagnosis, but we haven’t established a production latency or a before/after baseline.

The proposed fix is to share unchanged immutable data between derived contexts and copy only supplied changes, while preserving request-local authorization.
```

additionally, we must introduce performance testing, so that this issue will not be possible in the future. suggest solutions.

## Affected repositories

- `haveapi`: Ruby server documentation example contexts, generators, tests,
  benchmark tooling and developer guidance. No downstream pin/release changes.

## Approach

Have the retained architect inspect context derivation and Rust normalization,
then record a design and independent implementation boundaries in `design.md`.
Implement immutable sharing without broadening request-local authorization.
Introduce regression checks that reject repeated whole-description work and a
representative benchmark reporting allocations, CPU and elapsed time.

## Decisions

- The reported 102.4-second request and 639 derivations are local observations,
  not a production baseline. Establish reproducible before/after evidence.
- Prefer deterministic complexity/allocation checks for CI; timing benchmarks
  complement those checks and require a documented measurement environment.
- Publish a feature branch. Integration, release and deployment require separate
  direction and are outside the present implementation scope.

## Compatibility and deployment

Preserve rendered output, input isolation and request authorization. Assess
cache lifetime and invalidation explicitly. No persistent schema or protocol
change is expected. No deployment or version publication is planned.

## Documentation

Developer readers need the immutable-context contract and repeatable performance
test commands in HaveAPI documentation. Keep measurements and rollout-specific
evidence in this session; lead owns records and architect owns design.

## Testing plan

Run targeted quick Ruby checks and hook-managed lint before commits; run final
independent review after intended commits and quick checks, before longer tests.
Check unchanged subtree identity, defensively copied supplied changes, nested
immutability, output parity and cross-request authorization isolation. Require
the new regression protection to expose the original copying behavior. Use a
fresh policy watcher for long or uncertain verification.
