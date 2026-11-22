# Codex App Server advertised Unix socket is an alias

A private verification harness for Codex0.160 rejected its normal advertised
`--listen unix://...` path because it required `lstat()` to return a socket.
The path is a symlink; `stat()` follows it to the owned mode0600 socket under
`/tmp/codex-daemon-<uid>/`. Comparing saved stat() metadata with later lstat()
metadata falsely suggests replacement. Inspect both alias and resolved target
and distinguish their identities. Avoid chmod/restarting the listener to satisfy
a mistaken probe.

The [selected upstream transport source](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/app-server-transport/src/transport/unix_socket.rs)
binds the protected path, sets0600 and publishes the advertised symlink.
The real retained target matched the original kernel-process/socket proof;
prototype correction and acceptance are recorded separately in
`work/2026-10-02-portal-creation-performance/`.
