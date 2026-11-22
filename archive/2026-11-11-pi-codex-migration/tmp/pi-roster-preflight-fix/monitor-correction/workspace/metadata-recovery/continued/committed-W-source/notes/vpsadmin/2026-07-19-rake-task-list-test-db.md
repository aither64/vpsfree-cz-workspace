# Listing vpsAdmin API rake tasks needs the API database

## Symptom

`bundle exec rake -T` from `api/` fails while loading `SysConfig` when no
database is configured. Starting `../tools/test-db` outside the Nix API shell
also obscures its intended missing-MariaDB error with an uninitialized
`VpsAdmin::TestDbCli::Error` rescue constant.

## Cause

The API loads database-backed model configuration before Rake can list tasks.
The test database helper also expects MariaDB binaries from the repository's
API development shell.

## Workaround

Run the helper and Rake inside the same API Nix shell so the exported database
environment remains active:

```shell
nix develop .#api -c bash -c '
  set -e
  ../tools/test-db start
  trap "../tools/test-db stop" EXIT
  eval "$(../tools/test-db env)"
  bundle exec rake -T vpsadmin:node
'
```

This listed all four history reconstruction/status tasks successfully for
`work/2026-07-13-security-advisory-automation`.
