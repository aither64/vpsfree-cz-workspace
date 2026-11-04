# Package S schema capture

Captured from clean committed API source
`610a96f8ce523afbcd3e4374a70047dbe3264b0d` in the assigned worktree using
the existing controlled exporter. No deployed API/database was contacted and
no API files changed. Hook configuration and custom hooks were read before
normal Overcommit installation/signing; both succeeded.

Preparation passed in about 91 seconds; see `prepare.log`. The source capture
batch passed in about 81 seconds; see `export-batch.log`. The latter ran the
prepared tooling bundle's database-free exporter checks: 14 examples, zero
failures. Two independent temporary MariaDB databases produced the exact same
`schema.json`, `provenance.json` and `tooling.Gemfile.lock` bytes in `export-1/`
and `export-2/`.

The schema is also byte-identical to the SDK's prior saved schema:

- API 7.0, protocol 2.0, `vpsadmin-full-fixture`, mount `/`.
- 151 application resources, 519 actions, 8,720 parameters; authentication
  coverage remains separate.
- Six plugins: monitoring, newslog, outage_reports, payments, requests, webui.
- Schema SHA256:
  `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794`.
- Provenance SHA256:
  `b20bd20c83e6316c02befdf02e5f4a66c89348337f549bf357113bd488efdb0b`.
- Export lock SHA256:
  `56541da8b42745ab4f392b5d4183f330b3e9d5cd44559d05373c152946ba1053`.

Compared with old API source `bcfa95eb136c50d25024f53a6b1af557d1173d56`,
the recorded fixture, core database schema and tracked configuration inputs are
unchanged. The test-database runner changed. The outage_reports plugin's source
digest changed with its utility Gemfile; the other five plugin digests and all
plugin migration inventories are unchanged. Export tooling now records the
released HaveAPI server/client/generator gems at 0.32.0, plus their complete
resolved dependency graph. Exporter Ruby is 3.4.9, Bundler 4.0.23 and MariaDB
11.4.12; these are distinct from the SDK's separately pinned developer tools.
The exact generated provenance and lock preserve their installed gem hashes.

Cleanup was checked independently because the watcher's summary mentioned
PostgreSQL. The actual native runner is `tools/test_db.rb`: `auto_start!`
creates an owned temporary directory and registers `instance.stop` followed by
`instance.prune` in an `at_exit` ensure block. The export process exited zero.
An authoritative `/proc` inspection found no `mariadbd` or `mysqld` processes;
no current-day `vpsadmin-test-db-auto-20261101-*` directories were found under
`/tmp` through depth three. Old unrelated temporary directories were untouched.
No export operation remains running or uncertain.

The exact three output records were copied into SDK `schema/`. Schema bytes
therefore produce no Git diff; provenance and lock do. Final SDK generator
identity, npm tool graph and generated output remain pending at this checkpoint.
