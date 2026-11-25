# Package B literal actual run

- Result: passed (exit status 0).
- Command: `bash /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-b-actual-run.sh`
- Source base: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`, with current stable B/D edits in the assigned worktree.
- Elapsed: approximately 9 minutes overall. The cache copy/check completed in under 5 minutes; the remaining time was the nine CLI probe run.
- Full returned stdout/stderr chunks: `package-b-literal-actual.log` (8 lines). The exec interface did not allow redirecting the initial invocation, so this file preserves all chunks returned by the owned exec session, not any output the interface did not return.
- Failure excerpt: none; the command exited 0. Returned evidence includes successful SDK `bzImage`, `vmlinux`, and `fuse.ko` hash checks and successful copied module check.
- Script emitted `package-b-actual-sites.json` and its source SHA receipt as specified.
- Remaining effects: none known; owned process exited. No cancellation or retry.
