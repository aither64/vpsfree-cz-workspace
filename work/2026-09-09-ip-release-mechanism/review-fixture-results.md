# CI fixture repair review

Reviewed vpsAdmin `be21bc8b9..46acba869d319726126e8d9337e9d53fcea7aa6d` after
quick verification. Low risk: reversible test fixture logic only. Required
general and architecture lanes ran in fresh read-only ephemeral Codex contexts,
`gpt-6-astra`, `xhigh`, because the collaboration retained-thread limit had been
reached. Both completed with no findings. Scope/risk production boundaries are
unchanged from the completed refinement reviews.

The shared helper owns default candidate selection; it now skips occupied IPs
and keeps explicit addresses unchanged. The deterministic regression failed
before the fix and passed afterwards. The incident task and campaign model
consumer checks passed: 48 examples, zero failures, seed55211. Ruby lint and
all commit hooks passed. Reviewers confirmed the new spec belongs to exactly
one existing engine topic. The fixture fix is a separate ninth commit; the
first eight feature commits retain their hashes and no runtime locking changes.

Residual gaps: no direct wraparound/exhaustion regression; other helpers that
supply an explicit generated address keep their own existing behavior. These
are outside this bounded correction. Full engine rerun with the original CI
seed and isolated WebUI integration started after reconciliation.

Original failure: API Specs run35000486221, engine job104488002326, one failure
among1165 examples and three expected pending, seed55211. The failure happened
before IncidentReport task execution. Rolled-back examples advance MariaDB's
auto-increment sequence, so maximum(id) modulo200 was insufficient to guarantee
an unused default address. Original logs were inspected; no blind rerun was used.

Full local engine rerun subsequently passed:1166 examples, zero failures, three
expected pending, seed55211. Final-head hosted full/core engine jobs also pass.

Final API Specs workflow35002860902 is green, including all26 full/core topic
jobs and topic coverage. The ninth commit is published and no failure remains.
