# Run migration specs in their isolated process

Related initiative:
`work/2026-07-13-security-advisory-automation`

## Symptom

Running `api/spec/migrations` together with ordinary API examples in one RSpec
process caused broad failures about missing application tables. The ordinary
examples passed when run alone.

## Cause

The migration spec helper manages a purpose-specific migration database and
drops/recreates its schema. It is not compatible with the regular API spec
helper in the same RSpec process.

## Workaround and verification

Run migration specs through the repository's `MigrationSpecs` hook or in a
dedicated RSpec invocation, then run ordinary API examples separately. The
isolated regular suite passed 102 examples, and the complete Overcommit run
passed both MigrationSpecs and the remaining hooks.
