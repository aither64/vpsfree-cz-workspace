# Logger fixture runtime diagnosis

The run at `27be1238eb8779cae76694ff287f31ecbc7eaf3e` is incomplete,
explicitly canceled. Preserve `guarded-verification-01.log` and
`guarded-verification-result.json`; neither proves a natural assertion failure
or a passing VM. Host-build commands 2 and 3 were not run.

Original log: 4030 lines, 485694 bytes, SHA256
`95ad5167e496eb7faa92346d2db9d105717ddde105bc715ffa825d3f6728b3af`.

## Established cause

The fixture sent an RFC3164-shaped packet containing the slash-based cluster
machine name. With the pinned rsyslog and frozen VM configuration, that packet
is parsed with hostname `localhost`, and its cluster name becomes message text.
The resulting file is `/var/log/remote/localhost/log`, rather than the asserted
`/var/log/remote/cz.vpsfree/nodes/prg/node-fixture/log`.

A canonical RFC5424 packet preserves the same machine name, creates the exact
asserted path with mode `0640`, and reaches the exporter. This matches production
NixOS senders in `modules/system/logging/nixos.nix:30-32`, which configure
`LocalHostName` and `RSYSLOG_SyslogProtocol23Format`; node configuration also sets
its logging hostname to `confMachine.name` in `configs/node/base.nix:54`.

The canceled log separately proves a fixture lifecycle problem: stopping rsyslog
causes its single `cat` FIFO consumer to exit (lines 1810-1819), while the active
syslog socket immediately starts rsyslog again. Later pipe suspension appears at
lines 2519-2520. This does not explain the wrong filename: canonical RFC5424 still
creates the expected file with no consumer in the bounded probe.

## Disposable evidence

Both probes ran once inline as explicitly bounded quick checks in the canonical
configuration worktree, guarded on exact head `27be1238`, using a root user
namespace, pinned rsyslog 8.2608.0 and the frozen VM's syslog configuration.
Only disposable paths, ephemeral ports and the namespace group name were replaced.
No live service, secret or log was accessed.

- `logger-rsyslog-probe-01.log`: exit 1. With consumer, the expected path is absent
  but the exporter receives the marker. Without consumer, the expected path is
  also absent. This contradicted the initial sole-cause FIFO hypothesis.
- `logger-rsyslog-probe-02.log`: exit 1 on the separate assertion that a missing
  consumer prevents canonical remote-file creation. Its recorded paths establish
  the RFC3164/RFC5424 distinction above; the FIFO file-absence hypothesis is false.

Each scenario bounds input startup to 3 seconds, local-to-remote spacing to 0.2
seconds and file observation to 2 seconds. Shutdown allows 1 second after TERM,
then kills/reaps only the owned child. Temporary files are removed synchronously.
The second probe script is retained as `logger-rsyslog-probe.py` with its original
head guard and assertion, rather than rewriting the failed evidence as a pass.

## Correction and remaining verification

Only `tests/log-reader-vm.nix` and `tests/log-reader-vm.py` changed: canonical
RFC5424 generation with a real newline, restarting synthetic consumer, actual
socket/service quiescence, UDP listener readiness, and 30-second marker predicates
that emit journal/listener/path evidence and rethrow failures.

Python AST, pinned nixfmt, whitespace checks, actual generated packet-byte checks,
VM derivation evaluation and required commit hooks passed. No whole VM rerun was
started inline. Production logger configuration, auth, permission policy,
ingestion destinations, exporter pipe and rotation rules are unchanged.

The correction is folded into logger commit
`f5f0edbda99754aba915837d501a91a6233bc447`; final branch head is
`5d910028d32ce9305dc8161c51b3ed17ec4179bb`. Range-diff proves the proxy patch is
unchanged. A fresh verification watcher must run the VM against that final head;
the corrected fixture has not yet passed its full runtime acceptance.
