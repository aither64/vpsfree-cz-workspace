# 2026-08-05-nodectld-crash-reports

## Repositories

- `vpsadmin`
  - Branch: `2026-08-05-nodectld-crash-reports`
  - Worktree:
    `worktrees/2026-08-05-nodectld-crash-reports/vpsadmin`
  - Base: `origin/master` at `0b066c42814d3a9f5b0b8f8e3ed7910ae20a4fac`
  - Head: `9b391055c3654710760c0f58679b75c1cf84d94a`

## Status

- Root cause identified and the revised vpsAdmin fix is committed. The
  Connector/C override is node-only, nodectld disables TLS at its connection
  site, and a focused mysql2 patch makes that option effective with
  Connector/C 3.4.9. Fresh mandatory review found no findings, and final
  package, unit, integration, and malformed-response validation all pass.
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
- Built revised `nodectld` and `vpsadmin-api` packages and inspected their
  recursive closures and mysql2 shared-library linkage.
- Ran the official CONC-709 malformed-server reproducer against the rebuilt
  nodectld mysql2 extension.
- Initialized the root and API development shells and ran all declared
  Overcommit pre-commit hooks.
- Initially committed the fix as `8a71a3b79`, then amended it to `9b391055c`
  (`nodectld: update MariaDB connector to 3.4.9`) after moving TLS behavior
  out of Connector/C's global CMake flags.
- Ran the initial mandatory change review with one standalone fresh-context
  reviewer.
- Verified that upstream mysql2 master and release 0.5.7 only clear
  `MYSQL_OPT_SSL_ENFORCE` for `ssl_mode: :disabled`, leaving Connector/C 3.4's
  `MYSQL_OPT_SSL_VERIFY_SERVER_CERT` default enabled.
- Ran the focused `NodeCtld::Db` connection-option spec.
- Queried a real plaintext MariaDB server with the final packaged mysql2 and
  confirmed `ssl_cipher` is nil.
- Ran the CONC-709 malformed-server reproducer with the final packaged mysql2
  and explicit `ssl_mode: :disabled`.
- Built the API independently and confirmed it retains mysql2 0.5.7 linked to
  Connector/C 3.3.5.
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
- The vpsAdmin overlay builds Connector/C 3.4.9 only for node-side mysql2. It
  clears obsolete nixpkgs patches already present upstream and adapts
  nixpkgs's `mariadb_config` substitutions for new compiler warnings.
- Connector/C is built with its upstream
  `DEFAULT_SSL_VERIFY_SERVER_CERT=1`; there is no global TLS CMake override.
  Nodectld passes `ssl_mode: :disabled` at the connection site.
- mysql2 0.5.6's MariaDB compatibility path is patched to clear both
  `MYSQL_OPT_SSL_ENFORCE` and `MYSQL_OPT_SSL_VERIFY_SERVER_CERT` for disabled
  mode. It also restores the documented non-verifying behavior of
  `ssl_mode: :required`.
- The final node closure is
  `/nix/store/7k56v7vkpcrvdsdj0ayq31h2mb6x180w-nodectld-4.2.1`, with mysql2
  `/nix/store/v4h3yvch7w42wxd3bidhqdsnjqfjcyag-ruby3.4-mysql2-0.5.6` linked
  to stock Connector/C 3.4.9 at
  `/nix/store/dcvhgzfgm8xzhwazzx0fcdxksskdpj6k-mariadb-connector-c-3.4.9`.
- The API closure is
  `/nix/store/76psr2r0rl61pc5612rlk74h7v1h7kg3-vpsadmin-api-unknown`; its
  mysql2 0.5.7 remains linked to Connector/C 3.3.5, so API TLS behavior is
  unchanged.
- The malformed-server reproducer completes the plaintext handshake and
  returns `Mysql2::Error` instead of SIGSEGV. A real query returns successfully
  with `ssl_cipher == nil`.
- The focused connection-option spec passed: 1 example, 0 failures.
- All Overcommit hooks passed: Nixfmt, MigrationSpecs, VpsadminApiI18n and
  VpsadminWebuiI18n. The custom API i18n hook signature was stale but its
  configuration and source matched `origin/master`; it was verified and
  re-signed before the hook run.
- The final MariaDB-backed libnodectld suite passed: 424 examples, 0 failures,
  seed 52018. This includes the new connection-policy spec and transaction
  selection and rollback ordering.
- The final `services-up` integration test passed all 27 examples in 407.92
  seconds using the default bridge network. MariaDB responded and was
  populated, API responded, and the mailer node's packaged nodectld reported a
  running state.
- The vpsAdmin worktree is clean and one commit ahead of `origin/master`.

## Superseded mandatory review

- Blocking: none.
- Important: the original review required retaining
  `DEFAULT_SSL_VERIFY_SERVER_CERT=OFF` when the source pin expired. The user
  rejected that global package policy as brittle; the revised design removes
  the CMake flag entirely and therefore requires a new fresh-context review.
- Advisory: consider committing the malformed-server reproducer as a Nix CI
  check. Decision: keep this as manual package validation because it is an
  upstream Connector/C parser regression and would require vendoring a
  third-party protocol server into vpsAdmin. The initiative plan now records
  this boundary explicitly.
- The previous MariaDB-backed libnodectld suite and `services-up` integration
  test passed for the superseded global-CMake design. Both were subsequently
  rerun against commit `9b391055c`.

## Revised mandatory review

- Exactly one fresh-context standalone reviewer inspected commit `9b391055c`.
- Blocking: none.
- Important: none.
- Advisory: none.
- The reviewer independently confirmed the private Connector/C 3.4.9 node
  closure, unchanged Connector/C 3.3.5 API closure, stock Connector/C TLS
  default, C patch semantics, removal comments, focused commit split, and
  rolling/rollback safety.
- Review-time residual gaps were the deferred full libnodectld and
  `services-up` runs, the unknown malformed-packet producer, manual rather than
  CI-owned parser reproduction, intentional plaintext database traffic, and
  rollback restoring the vulnerable client. Both deferred test runs now pass.

## Open questions

- Which database server or intermediary emitted the malformed metadata and
  whether it correlates with maintenance, failover, or another overnight job.
  Server/proxy logs or a packet capture around the listed crash timestamps are
  needed to identify the source of the invalid `0xfb` schema-name field.

## Cleanup

- Keep the feature worktree until the branch is reviewed, tested and merged.
- Root and API `.gems/` directories in the worktree are transient development
  shell output and can be removed with the worktree after integration.
