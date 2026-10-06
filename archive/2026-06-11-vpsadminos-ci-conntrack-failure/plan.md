# 2026-06-11-vpsadminos-ci-conntrack-failure

## Goal

Find the root cause of failed vpsAdminOS CI run
https://github.com/vpsfreecz/vpsadminos/actions/runs/27363633690 and implement
a fix.

## Affected repositories

- `vpsadminos`

## Approach

- Inspect the failing GitHub Actions run and uploaded test logs.
- Reproduce the failure path from logs before editing code.
- Fix the readiness race that lets tests and callers observe the firewall
  service as ready before its ruleset has been installed.
- Cover the underlying runit service contract so custom `check` scripts inherit
  service `path` and `environment`.

## Compatibility and deployment

- The runit service generator changes only generated service `check` scripts.
  Existing checks that use absolute paths continue to work; checks can now also
  rely on the service `path` and `environment` options like `run`, `finish`, and
  `control` scripts already do.
- The firewall service check becomes stricter: `sv check firewall` succeeds
  only after the `INPUT -> nixos-fw` jump is installed and the temporary
  reload drop chain is absent. This changes readiness reporting, not firewall
  packet policy.
- Mixed-version operation is unaffected. The change is local to each booted
  system's generated runit service files and does not alter persisted state,
  database schemas, API contracts, or on-disk formats.
- Rollback is safe: older systems simply revert to the previous less-specific
  runit check behavior.

## Testing plan

- Run `./test-runner.sh test firewall/conntrack#conntrack` to verify the
  original failing script no longer races.
- Run `./test-runner.sh test system/boot/runit` to verify custom runit check
  scripts inherit service `path` and `environment`.
- Run repository Overcommit hooks before committing.
