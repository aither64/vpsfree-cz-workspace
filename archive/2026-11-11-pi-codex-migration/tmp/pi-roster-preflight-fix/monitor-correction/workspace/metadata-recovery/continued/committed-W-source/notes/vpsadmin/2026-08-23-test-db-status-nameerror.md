# `tools/test-db status` raises after reporting a stopped database

## Symptom

When the persistent test database is stopped, `tools/test-db status` first
prints `MariaDB test database is not running` and then raises
`NameError: uninitialized constant VpsAdmin::TestDbCli::Error`.

## Cause

The status branch calls `exit 1`. While handling the resulting `SystemExit`,
Ruby resolves the CLI's `rescue Error` constant. The error class actually lives
at `VpsAdmin::TestDb::Error`, not under `VpsAdmin::TestDbCli`, so constant
lookup raises `NameError` instead of preserving the intended status exit.

## Workaround

Treat the first status line as authoritative, or check the isolated test
database through the RSpec auto-start output. Do not infer that MariaDB is
running from the later Ruby exception.

## Verification

Reproduced from the vpsAdmin feature worktree while checking focused tests for
`work/2026-08-18-vpsadmin-password-reset`. The automated RSpec database had
already stopped normally.
