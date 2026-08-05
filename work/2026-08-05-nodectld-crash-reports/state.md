# 2026-08-05-nodectld-crash-reports

## Repositories

- `vpsadmin`
  - Branch: `2026-08-05-nodectld-crash-reports`
  - Worktree:
    `worktrees/2026-08-05-nodectld-crash-reports/vpsadmin`
  - Base: `origin/master` at `0b066c42814d3a9f5b0b8f8e3ed7910ae20a4fac`
  - Head: `8a71a3b79e61e1f5b633923c19710293da000f4a`

## Status

- Root cause identified and the user-approved vpsAdmin package overlay is
  committed. Mandatory review, package verification, the MariaDB-backed
  libnodectld suite and the service integration test are complete.
- All reports are SIGSEGV in MariaDB Connector/C 3.3.5
  `unpack_fields+0x98`, called through mysql2 0.5.6 `_query` on Ruby 3.4.9.

## Commands run

- `bin/dev-session current` and checked `VPSFREE_DEV_SESSION_SLUG`.
- Inventoried files and sizes under `tmp/nodectld-crash-reports/`.
- Inspected report headers, Ruby backtraces and native backtraces.
- Disassembled both Connector/C builds and mapped `unpack_fields+0x98` to the
  invalid field-length read.
- Compared the failure with MariaDB issue CONC-709 and its upstream fix.
- Compiled and ran the official CONC-709 reproducer on loopback port 13366
  against the Connector/C 3.3.5/mysql2/Ruby packages from a report.
- Fetched `origin/master` and created the vpsAdmin feature worktree.
- Verified MariaDB Connector/C `v3.4.9` is the newest official upstream tag.
- Built Connector/C 3.4.9 from the vpsAdmin overlay.
- Built `nodectld` and `vpsadmin-api` from the overlay and inspected their
  recursive closures and mysql2 shared-library linkage.
- Ran the official CONC-709 malformed-server reproducer against the rebuilt
  nodectld mysql2 extension.
- Initialized the root and API development shells and ran all declared
  Overcommit pre-commit hooks.
- Committed the fix in vpsAdmin as `8a71a3b79` (`nix: update MariaDB connector
  to 3.4.9`).
- Ran mandatory change review with one standalone fresh-context reviewer.
- Simulated a future nixpkgs Connector/C 3.4.9 package and verified that the
  vpsAdmin TLS compatibility flag remains present after the source pin is
  bypassed.
- Ran `nix develop .#libnodectld --command bundle exec rspec`.
- Ran `./test-runner.sh test services-up` using the default bridge network.

## Results

- The current process owns verified session
  `2026-08-05-nodectld-crash-reports`.
- 24 reports are present from node20 through node25 in Prague and node5 in
  Brno.
- All 24 reports have the same native stack and Ruby call path. They span two
  independently rebuilt but version-identical sets of Ruby 3.4.9, mysql2
  0.5.6 and Connector/C 3.3.5 packages.
- Connector/C computes a field length from `row->data[1] == NULL`, underflows
  it, and reads at an address ending in `ffffffff`. Register values in every
  report satisfy that exact calculation.
- A `0xfb` (`NULL_LENGTH`) value in a column-definition packet causes this
  state. This is MariaDB Connector/C issue CONC-709, fixed in 3.1.27, 3.3.14
  and 3.4.4.
- The official standalone reproducer produces the same `unpack_fields+0x98`
  crash with one Ruby thread, excluding nodectld concurrency as a prerequisite.
- The affected nodectld SQL is consistently the second rollback-selection
  query at `libnodectld/lib/nodectld/daemon.rb:244`.
- Reports are concentrated overnight. Node5 and node25 crashed nine seconds
  apart on 2026-08-03, which suggests a shared database/proxy event, but crash
  reports alone cannot establish why malformed metadata was sent.
- The vpsAdmin overlay upgrades Connector/C to 3.4.9, clears obsolete nixpkgs
  patches already present upstream, and adapts nixpkgs's `mariadb_config`
  substitutions for the new compiler warnings.
- Connector/C 3.4 enables server-certificate verification by default, which
  also makes TLS mandatory. The overlay passes
  `-DDEFAULT_SSL_VERIFY_SERVER_CERT=OFF` to preserve the existing database
  connection behavior. Verified TLS remains a separate deployment project.
- Both node-side mysql2 0.5.6 and API-side mysql2 0.5.7 are rebuilt against
  Connector/C 3.4.9. Final checked closures contain no Connector/C 3.3.5:
  - nodectld: `/nix/store/2qx4v3lmgrdp0lrhhq53d0qdf0dbglj7-nodectld-4.2.1`
  - API: `/nix/store/7j5i88izbah2q2c44fqysd8qffymmcqi-vpsadmin-api-unknown`
- The malformed-server reproducer now completes with `Mysql2::Error` instead
  of SIGSEGV. A rebuilt mysql2 client also completes the plaintext handshake,
  confirming the preserved TLS default.
- All Overcommit hooks passed: Nixfmt, MigrationSpecs, VpsadminApiI18n and
  VpsadminWebuiI18n. The custom API i18n hook signature was stale but its
  configuration and source matched `origin/master`; it was verified and
  re-signed before the hook run.
- The first libnodectld RSpec attempt was stopped before tests began because
  the uncached MariaDB server build was long-running and mandatory review must
  precede long validation. The server package is now built as a development
  shell dependency, so the suite can resume after review.

## Mandatory review

- Blocking: none.
- Important: the original version gate would have dropped
  `DEFAULT_SSL_VERIFY_SERVER_CERT=OFF` when nixpkgs reached Connector/C 3.4.9,
  silently changing database connection requirements. Fixed by separating the
  expiring source pin from the TLS compatibility override. The reviewer
  confirmed the correction through the simulated future-version evaluation.
- Advisory: consider committing the malformed-server reproducer as a Nix CI
  check. Decision: keep this as manual package validation because it is an
  upstream Connector/C parser regression and would require vendoring a
  third-party protocol server into vpsAdmin. The initiative plan now records
  this boundary explicitly.
- Reviewer confirmed commit focus, package propagation, current TLS behavior,
  rolling-upgrade and rollback safety, and no tenant-isolation impact.
- The MariaDB-backed libnodectld suite passed: 423 examples, 0 failures, seed
  26326. This includes transaction selection and rollback ordering.
- The `services-up` integration test passed all 27 examples in 434.66 seconds.
  MariaDB responded and was populated, the mailer node's nodectld reported a
  running state, and the API responded through the packaged deployment.
- Final vpsAdmin worktree is clean and one commit ahead of `origin/master`.

## Open questions

- Which database server or intermediary emitted the malformed metadata and
  whether it correlates with maintenance, failover, or another overnight job.
  Server/proxy logs or a packet capture around the listed crash timestamps are
  needed to identify the source of the invalid `0xfb` schema-name field.

## Cleanup

- Keep the feature worktree until the branch is reviewed, tested and merged.
- Root and API `.gems/` directories in the worktree are transient development
  shell output and can be removed with the worktree after integration.
