# Run migration and application specs separately

## Symptom

Running an API route spec and a migration spec in one RSpec process caused the
route examples to fail because core tables such as `sysconfig` were missing
from `vpsadmin_test_migration`.

## Cause

`api/spec/migration_helper.rb` changes the process-wide ActiveRecord connection
to the stripped migration test database. Migration examples reset that schema,
so ordinary application specs in the same process no longer have the complete
core schema loaded by `spec_helper.rb`.

## Workaround

Run `api/spec/migrations/*` separately from API, model, and other application
specs. Smoke schema specs may run with migration specs when they do not use the
application models.

## Verification

The new password-recovery migration spec and core-schema smoke spec passed
together. The password-recovery route spec is verified in a separate RSpec
process.

Related initiative: `work/2026-08-18-vpsadmin-password-reset/`
