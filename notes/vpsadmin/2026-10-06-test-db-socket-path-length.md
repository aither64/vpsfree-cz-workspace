# Keep automatic MariaDB temporary paths short

In the network-availability session, exporting a deeply nested tracking
directory as `TMPDIR` prevented API specs from starting. MariaDB rejected its
Unix socket path as longer than 107 bytes; RSpec ran zero examples and reported
an error outside examples.

`tools/test_db.rb` creates an isolated directory with
`Dir.mktmpdir('vpsadmin-test-db-auto-')` and appends `mysql.sock`. Use the
ordinary short `/tmp` root for these automatic databases and keep RSpec JSON
and command logs in session tracking. The helper still owns its unique
directory, random port and normal-exit cleanup. Do not change product database
configuration or shorten paths through symlinks to work around this failure.

Evidence: `work/2026-10-05-network-ipv4-left-counter/visibility-quick2-api-core.log`.
Using `/tmp` allowed the corrected core run to execute all 226 selected
examples. Three API expectation failures were unrelated to database startup;
the full mode remained unexecuted after the stop-on-failure gate.
