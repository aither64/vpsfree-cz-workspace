# vpsAdmin test database socket path length

Related initiative: `work/2026-06-15-vpsadmin-events`

Starting `tools/test-db` with a state directory inside a deeply nested
initiative worktree can fail after initialization because MariaDB limits the
Unix socket path to 107 bytes. The log reports:

```text
The socket file path is too long (> 107)
```

Use a short state directory under `/tmp`, while keeping a distinct port and
directory per session, for example:

```sh
VPSADMIN_TEST_DB_PORT=39857 \
VPSADMIN_TEST_DB_STATE_DIR=/tmp/vpsadmin-mute-db \
  nix develop .#api -c ../tools/test-db start
```

The 2026-07-31 failure also exposed a pre-existing error-reporting bug in
`tools/test-db`: its CLI rescues an unqualified `Error`, so the original
`VpsAdmin::TestDb::Error` is followed by a `NameError`. The MariaDB log still
contains the useful root cause. Retrying with the shorter path is the relevant
workaround; no repository code was changed for this unrelated CLI defect.
