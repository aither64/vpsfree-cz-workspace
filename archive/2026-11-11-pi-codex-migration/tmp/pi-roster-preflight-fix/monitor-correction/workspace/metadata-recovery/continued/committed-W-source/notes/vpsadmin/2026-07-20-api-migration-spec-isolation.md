# Keep API migration specs isolated from ordinary API specs

## Symptom

Running every `api/spec/**/*_spec.rb` in one RSpec process produces thousands
of missing-table failures against `vpsadmin_test_migration`, even though
focused and CI topic suites pass.

## Cause

`api/spec/migration_helper.rb` registers a suite-wide hook that switches
`ActiveRecord::Base` to a dedicated migration database. That database is
deliberately reset and populated only with the minimal schema required by each
migration example. When migration and ordinary specs share one process, the
ordinary examples inherit that connection and cannot see the normal schema.

This is deterministic test-harness isolation, not flaky database startup and
not a product regression.

## Workflow

Match GitHub Actions: run `spec/migrations/*` as its own suite, and run the
complete ordinary API spec inventory without that directory. Treat both
results together as full API validation. Do not accept a rerun until the first
failure's database name has been checked.

Verified in `work/2026-07-20-kernel-boot-evidence-history/` after focused API
and migration suites had passed independently.
