# Keep vpsAdmin Migration Specs Separate

Initiative: `work/2026-07-13-security-advisory-automation`

## Symptom

One RSpec invocation containing both `api/spec/migrations/*_spec.rb` and
ordinary API/model specs produced widespread missing-table errors in
`vpsadmin_test_migration`.

## Cause

Migration specs use a dedicated migration database and change the active
database connection. With randomized example ordering, ordinary examples can
then run against that deliberately partial schema.

## Workaround

Run migration specs in their own RSpec process. Run API, model, and supervisor
specs in a separate invocation. Also avoid starting parallel
`nix develop .#vpsadmin` shells in one worktree; the existing
`2026-06-15-parallel-nix-develop-bundler-race.md` note explains their shared
`.gems` race.

## Verification

The separated migration and application spec invocations passed for the Node
kernel evidence changes.
