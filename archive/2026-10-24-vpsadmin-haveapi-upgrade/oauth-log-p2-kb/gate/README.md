# P2 pre-implementation native-error duplication gate

Pinned DokuWiki inspection source from the approved plan, unmodified. Real
`ErrorHandler`, `Logger`, `Event`, `EventHandler` and `io_saveFile` execute in
isolated processes. An empty plugin registry and HTML escaping are fixture
bootstrap only. A synthetic fixed-category `LOGGER_DATA_FORMAT` handler is
registered through the real event system, then actual log files are inspected.
The public sentinel is deliberately not a credential. No product fix exists yet.

`python3 oauth-log-p2-kb/gate/run-gate.py` completed0 in0.15s on the already
available PHP8.4.27 CLI (absolute store path and source hashes in results.json).
Five bounded cases, no retry or daemon/network/login/production request:

- User warning: fixed wiki entry, raw message still reaches native PHP error log.
- Native warning: `hidewarnings=true` prevents its native fallback; wiki remains
  fixed. This exception applies only to E_WARNING, not user warning/error.
- Uncaught RuntimeException: fixed wiki entry, no native duplicate under the core
  exception handler. Core-generated HTML still displays its raw message;
  display_errors=0 does not control that explicit application output.
- User fatal error: fixed wiki entry, raw native message remains; expected native
  exit255. The driver treats this as evidence, not a passing protection test.
- Benign unrelated warning: original useful message remains in wiki and native
  logs. There is no global disabling of DokuWiki facilities in this experiment.

Source: ErrorHandler.php44–47 registers selected warning/error classes;
155–184 logs then returns false except E_WARNING+hidewarnings. Logger.php126–160
runs LOGGER_DATA_FORMAT around wiki formatting only. ErrorHandler.php49–79
handles uncaught Throwable and manually renders HTML; fatalShutdown at104–126
runs too late to intercept native fatal output. init.php221–248 registers the
core handler before action plugins and authentication. Ordinary oauth auth.php
catches OAuthException and helper.php111–133 displays it, without logger calls.

FPM transport is source-traced only: available PHP php.ini817–819 documents
FastCGI logging enabled by default. Its www.conf.default427–439 documents worker
stderr capture and default-off catch_workers_output. The selected NixOS FPM
module sets master error_log=syslog; selected DokuWiki pool config does not add
catch_workers_output. No actual FPM process/socket or installed stack was run,
so this gate does not claim an observed journal/FastCGI/worker transport result.
Later authorized installed-fixture acceptance must bind effective pool settings.

Architect received the native duplicate gap and the proposed narrowly scoped
owning seam. LOGGER_DATA_FORMAT alone is insufficient; a callback-only native
policy must close the demonstrated duplicate while preserving unrelated logs.
The per-site auto_prepend_file PHP option is a possible early seam, not an
implemented/accepted design. Await architect path/import brief and E1 prep-ready
before repository edits. E1 owns shared allowdebug/phpOptions/Matomo wiring and
all Git/index/ref operations. Matomo must omit the whole JS and noscript
injection on callback/error documents; normal clean navigation remains tracked.

All case logs/stdout, hashes, scripts and results are retained here. No active
fixture process/effect remains. No changes to pinned sources, refs, inputs,
product/config worktrees, staging, cluster, runtime or existing operations.
