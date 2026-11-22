# Bundix on clean GitHub runners

## Symptom

The daily update workflow reached the package dependency refresh but Bundix
failed on the Git-sourced `syslog-exporter` gem. Bundler tried to create its Git
cache below a read-only Nix store path. A first repair then failed only on the
hosted runner with `bundle: command not found`; the workstation's ambient PATH
had hidden that problem.

## Cause

Bundix removes `BUNDLE_PATH` before invoking Bundler. Its package exposes the
`bundix` command but does not make a standalone `bundle` command available to a
clean shell. Testing with ambient workstation tools can therefore give a false
positive.

## Fix

Add Bundix to the repository's `mkConfigDevShell` `extraPackages`, run the
entire package update through `nix develop`, and persist Bundler's path with a
runner-temporary `BUNDLE_APP_CONFIG` before calling Bundix. This keeps all tools
on the flake-pinned dev shell and gives Bundix a writable Git cache location.

## Verification

Use an environment without ambient package tools, confirm `command -v bundix`
points into the Nix store, then reproduce the nested package invocation in a
temporary directory. For this incident, `bundix -l`, `nixfmt gemset.nix`, and
the generated source check all passed for `syslog-exporter`.

Related initiative: `work/2026-07-16-codex-lb-update/`.
