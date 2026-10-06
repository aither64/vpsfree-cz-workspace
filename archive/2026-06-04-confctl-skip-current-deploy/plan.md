# confctl skip current deploys

## Summary

Modify `confctl deploy` so a selected machine is omitted from copy,
activation, reboot, and post-deploy health checks when it is already on the
target generation. This includes carried machines, where the deployed state is
the carrier-managed profile. The motivating case is repeated
`confctl deploy --reboot <machine> boot`, which should not reboot a machine
that is already using the target system.

Affected repository:

- `confctl`

## Implementation Plan

- Add a deploy pre-filter in `ConfCtl::Cli::Cluster` after
  `host_generations` are resolved or built, and before the bulk/one-by-one copy
  phase.
- Query runtime state with existing `ConfCtl::MachineStatus` in parallel:
  `current_toplevel` is compared with `generation.toplevel`; the current host
  profile from `status.generations.current&.toplevel` is also available.
- Skip a host only when the target is already active:
  - for `test` and `dry-activate`, `current_toplevel == generation.toplevel`
    is enough because those actions do not intentionally update the profile;
  - for `boot` and `switch`, both `current_toplevel` and the active profile
    must match `generation.toplevel`, so stale boot/profile state is not hidden.
- For carried machines, compare the carrier-managed `machine.profile` resolved
  by `MachineStatus#current_toplevel` with the target generation.
- Leave hosts in the deploy set when status probing fails, the machine is
  offline, or the profile cannot be resolved; the existing copy/activation path
  will handle those failures.
- Keep `--copy-only` behavior unchanged so an operator can still explicitly
  copy a generation even if the current system already matches.
- Print a clear per-host message such as
  `Skipping <host>: already using target generation <name>`.
- Pass filtered `machines` and `host_generations` into the existing
  `deploy_in_bulk` / `deploy_one_by_one` methods. If all hosts are skipped,
  return without activation, reboot, or health checks.
- Update the deploy manpage text to mention that no-op targets are skipped.

## Test Plan

- Add focused RSpec coverage for the skip helper:
  - skips `boot`/`switch` only when runtime and profile both match;
  - does not skip `boot`/`switch` when runtime matches but profile is stale;
  - skips `test`/`dry-activate` when runtime matches;
  - does not skip when status data is missing or `--copy-only` is set.
- Extend the existing deploy integration suite to run a repeated deploy of the
  current generation and assert that output reports the skip and does not print
  a reboot line for `--reboot boot`.
- Extend the carrier deploy suite with a repeated carried deploy and assert
  that carrier profile deployment is skipped.
- Validation commands:
  - `bundle exec rspec`
  - `bundle exec rubocop`
  - `./test-runner.sh test deploy/swpins`
  - `./test-runner.sh test deploy/flakes`
  - `./test-runner.sh test carrier/deploy`

## Assumptions

- "Already using the version" means the resolved Nix toplevel store path is the
  target generation's `toplevel`.
- For actions that update the boot/profile generation, skipping only when the
  profile also matches is the safer default; otherwise ConfCtl should still
  perform deployment work rather than silently leaving a stale profile.
- For carried machines, the carrier-managed profile is the deployment
  authority; `/run/current-system` on the carried machine is not consulted.
- No public CLI flag is needed for this first change. If operators later need
  to force a no-op activation/reboot, that can be added explicitly.
