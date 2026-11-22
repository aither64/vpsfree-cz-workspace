# API development shell changes the working directory

## Symptom

A command such as `nix develop .#api --command ruby api/tmp/check.rb` fails with
`No such file or directory`, even though the script exists from the repository
root.

## Cause

The API development shell's entry hook changes the working directory from the
vpsAdmin repository root to `api/` before it runs the command.

## Workaround

Pass paths relative to `api/`, such as `tmp/check.rb`, or use an absolute path.
When a disposable check combines `SpecDbSetup` with `require "vpsadmin"`, use
the automatically isolated test database without `db_name_suffix`: vpsAdmin's
configuration load re-establishes the connection from the base `DATABASE_URL`
and otherwise leaves the suffixed schema behind.

## Verification

The disposable charged-environment repair check booted its schema and passed
after using the API-relative path and the base isolated test database. Related
initiative: `archive/2026-09-07-fix-ip-charged-environments`.
