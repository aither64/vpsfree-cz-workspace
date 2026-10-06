# 2026-08-22-multiple-kernel-scopes

## Goal

Allow eBPF livepatch programs to declare multiple disjoint kernel-version
ranges. A program must be selectable when any range matches the configured
kernel, while existing 6.12 behavior and monitoring interfaces remain
unchanged.

## Affected repositories

- `vpsadminos`
- `vpsfree-cz-configuration`

## Approach

- Replace each registry program's single `sinceKernel` and optional
  `untilKernel` pair with an ordered, non-empty `kernelRanges` list.
- Treat `sinceKernel` as inclusive and `untilKernel` as exclusive in every
  range. Reject malformed, unsorted, or overlapping ranges.
- Match a program when exactly one range contains `boot.kernelVersion`.
- Keep the monitor JSON and Prometheus contract unchanged by exporting the
  range that matched the running kernel as `sinceKernel` and `untilKernel`.
- Migrate current programs to one-element range lists. Do not add 6.18 ranges:
  the incoming 6.18 kernel already contains the fixes covered by the current
  guards.
- Leave compiled kernel livepatch selection unchanged. Its `filterFn`
  predicates already support arbitrary version logic.
- After integrating the reviewed vpsAdminOS commit into `staging`, update the
  `vpsadminos` role in the `staging`, `os-staging`, and `production` channels
  through `confctl` to the exact merged revision.

## Compatibility and deployment

- No NixOS option, API, protocol, persistent-state, or metric schema changes.
- Existing 6.12 program selection is unchanged.
- Old and new systems emit the same eBPF monitoring JSON fields, so mixed
  deployments and rollback remain compatible.
- The implementation does not change kernel sources or configuration and does
  not require a coordinated machine update.
- Integrate and publish vpsAdminOS before updating configuration pins so every
  channel resolves a revision reachable from the upstream default branch.
- The three channel pins may be deployed independently. Older nodes remain
  compatible, and rollback consists of restoring the previous vpsAdminOS pin.

## Testing plan

- Extend `tests/suite/ebpf-livepatch.nix` with synthetic disjoint ranges,
  gap and boundary checks, registry validation, manual-selection errors, and
  matched monitoring metadata.
- Run `./test-runner.sh test ebpf-livepatch` as quick verification.
- Run repository pre-commit hooks, commit the complete change, and perform the
  mandatory standalone change review.
- After review, run `./test-runner.sh test ebpf-livepatch-lifecycle` and
  `./test-runner.sh test 'prometheus/exporters#ebpf'`.
- Push the feature branch and monitor GitHub Actions.
- Verify the generated configuration pin mapping, run a no-build flake check,
  evaluate representative staging and production nodes without local builds,
  and build one managed `os-staging` consumer after confirming its build graph
  contains no kernel or ZFS derivations.
