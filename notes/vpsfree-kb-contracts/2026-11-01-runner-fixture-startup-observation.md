# Immediate process-identity checks can race fixture startup

A strict check failed in the closed-client acknowledgement fixture immediately
after spawning its runner. The fixture snapshots `/proc` before waiting for
readiness; cleanup then relies on that tuple. A startup/exec race is supported
by source and the later settled identity, but the failing tuple was not saved.
Fixture/runtime/checker blobs were unchanged across a prior passing and failed
pin check.

The watcher initially missed an orphan fixture. Fresh full process identity and
native process-tree reconciliation stopped only that owned runner and child;
both were verified absent. One unchanged fresh strict check then passed. Retain
the initial failure and this limitation instead of calling a green retry proof
of its precise cause or trusting a blanket no-process report.

Evidence: work/2026-11-01-published-advisory-corrections/api-acceptance.md.
