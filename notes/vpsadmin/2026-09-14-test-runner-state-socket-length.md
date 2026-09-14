# Use short state paths for local integration tests

Passing a full dated coordination-directory path to `./test-runner.sh test
--state-dir ...` caused OsVm::Shell#prepare to fail at UNIXServer.new before any
example: socket path 129 bytes, maximum 108. Build output was valid.

Use a dedicated short `mktemp -d /tmp/kh-sup.XXXXXX` (or equivalent) state directory
for each runner. Record its path in initiative state, redirect main logs to the
tracking directory, and retain the failure reason before retrying. A symlink may
be resolved by tooling, so a short real directory is preferable.

Related initiative: work/2026-09-14-kernel-history-fix. Supervisor/runtime-ingestion
and webui#admin-cluster were restarted with short paths; verification results
are recorded in the initiative state.
