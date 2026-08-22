# 2026-08-22-multiple-kernel-scopes

## Goal

Allow eBPF livepatch programs to declare multiple disjoint kernel-version
ranges. A program must be selectable when any range matches the configured
kernel, while existing 6.12 behavior and monitoring interfaces remain
unchanged.

## Affected repositories

- `vpsadminos`

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

## Compatibility and deployment

- No NixOS option, API, protocol, persistent-state, or metric schema changes.
- Existing 6.12 program selection is unchanged.
- Old and new systems emit the same eBPF monitoring JSON fields, so mixed
  deployments and rollback remain compatible.
- The implementation does not change kernel sources or configuration and does
  not require a coordinated machine update.

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
