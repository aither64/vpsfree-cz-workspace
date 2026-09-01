# API migration specs require a separate RSpec process

Related initiative: `work/2026-09-01-dataset-expansion-bug`.

## Symptom

Running every `api/spec/**/*_spec.rb` file in one RSpec process caused normal
API examples to fail with missing core tables in `vpsadmin_test_migration`.
The failures appeared unrelated to the selected examples and began as soon as
the suite attempted to create ordinary records such as users.

## Cause

Loading any migration spec also loads `api/spec/migration_helper.rb`. Its
global `before(:suite)` hook changes the Active Record connection to the
dedicated migration database. That hook applies to all examples loaded in the
same process, including ordinary API specs, whose expected schema is not
present in that database.

## Workaround

Run ordinary API specs and migration specs in separate RSpec processes. For a
local ordinary-suite run, explicitly exclude `spec/migrations/`; use the
repository's migration-spec command or pre-commit hook for the migration
files. The GitHub Actions topic-parallel workflow already keeps these suite
boundaries separate and checks coverage of the selected spec files.

## Verification

Focused ordinary API specs passed in the normal database, and all migration
specs passed through the repository's Overcommit hook. The topic-parallel
GitHub Actions jobs for the pushed feature head kept the suites isolated and
reported the affected storage, mail, and supervisor topics successful.
