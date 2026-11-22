# Run migration specs separately from ordinary API specs

## Symptom

Combining a spec under `api/spec/migrations/` and an ordinary API spec in one
RSpec process causes the ordinary spec to fail because core tables such as
`users` are missing from `vpsadmin_test_migration`.

## Cause

The migration-spec support switches ActiveRecord to its isolated migration
database and defines only the minimal schema needed by each migration example.
That connection remains active for later examples in the same RSpec process.

## Workaround

Run migration specs and ordinary API specs in separate RSpec invocations. This
preserves the migration harness's isolation and lets ordinary specs use the
normal fully seeded test database.

The separate runs for the auth-token column fix passed: the migration spec had
2 examples and the token-configuration spec had 7 examples.

Related initiative:
`work/2026-07-20-security-advisory-review/`.
