# Keep migration specs separate from ordinary API specs

A combined `bundle exec rspec spec/migrations/... spec/models/...` run failed
ordinary fixtures with missing seed rows. `migration_helper` changes the global
connection and resets the migration database before every example; it cannot
share a process with the normal model/API harness. Run migrations separately.
The separate migration run passed. For manual schema generation with SpecDbSetup,
set `RACK_ENV=test`; use `VPSADMIN_PLUGINS=none` for the core-only schema.
Do not add migration existence guards for disposable database mismatches.

Related initiative: work/2026-09-09-ip-release-mechanism.
