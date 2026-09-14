# API shell and core schema checks

For `work/2026-09-14-kernel-history-fix`, the first shell command failed with
`cd: api: No such file or directory`: `nix develop .#api -c ...` already enters
`api/`. Run the component commands directly.

Standalone scripts using `SpecDbSetup` need `RACK_ENV=test` to start a disposable
MariaDB automatically. Use `VPSADMIN_PLUGINS=none` when regenerating the core
schema. Load the existing core schema, run the migration context, then use
`ActiveRecord::SchemaDumper.dump(ActiveRecord::Base.connection_pool, file)`.
The resulting dump may reorder existing table, column, and index definitions;
compare their contents before attributing all textual changes to the migration.

Migration specs use `bundle exec rspec --options /dev/null --format documentation
spec/migrations/..._spec.rb`, as in the migration CI workflow. The API's normal
`.rspec` otherwise loads the full application spec helper and plugins first.
The migration coverage checker considers tracked specs, so stage a new spec
before running `ruby tools/check_migration_specs.rb`.

Verified: core migration and schema dump succeeded; the isolated migration spec
passed with no backfill and successful rollback.

Git hooks need the root Nix development shell, which includes Overcommit.
A push after successful specs inside `.#api` failed because that component
bundle does not include Overcommit. Re-run the push from `nix develop -c git
push ...`; do not install hook gems into the API bundle or bypass hooks.
