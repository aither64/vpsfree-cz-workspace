# Initialize guarded artifact directories before opening logs

The retained-services fixture entrypoint checked that its artifact directory
was private and empty, opened `test-runner.log` there, then constructed a
fixture whose constructor repeated the empty-directory check. The constructor
refused its own newly created log, before any guest started.

Construct the fixture before opening its owned log. Keep both original
private/empty checks intact. Constructor failures remain in the caller's
private stderr capture; later test output goes to the fixture-owned log.

A focused check loaded the actual entrypoint with its pinned native Ruby,
dependencies and sealed fixture configurations. It stopped at the inherited
evaluator's run boundary, checking initialized state, a private log and an
empty machine registry. This proves bootstrap only; it must report zero guests
and no scenario success. Full guest assertions remain a separate integration
result. Evidence is linked from
[the storage redesign state](../../work/2026-09-23-storage-redesign/state.md).
