# R1 isolated source handoff

The two-file incremental correction is complete, uncommitted and frozen in the ordinary `dev-workspace-recovery-review` worktree, based on reviewed B8e9186132efc0636d6bcaaccf663dad43a799bf4/tree68de977e4ae31ba524206e1ca1a7d78b417f2963. Main remains unchanged. Implementer1 owns all Git and incorporation; this owner performed no Git/index operation or live state read/mutation.

`final.json` inventories both exact base/final hashes. `final.patch` is incremental against the immutable reviewed snapshots in `base/`. A complete source snapshot was retained before owner1 supplied the ordinary isolated worktree; comparison proves only the two released paths differ.

The existing canonical removal history hash now accepts a private optional exclusion, preserving every old caller's default behavior. Failed-creation recovery validates the entire inventory before applying the accepted epoch rule. Live journal anchors the exact operation; live tracking without a journal selects no old completion; completed replay requires one uniquely matching operation and recovery location. Existing private root/request/roster/creation/start/phase validators still decide eligibility. No timestamp/latest inference, missing-target success or no-effect claim is introduced.

Implicit preparation discovery ignores historical receipt/epoch identities; explicit UUID still validates exactly. The public regression retains the previous handed-off preparation records because ordinary failed receipt retirement does not compact them. Current ambiguity and malformed records still refuse. Old preparation and recovery bytes are checked unchanged.

The new public cases cover 0/1/2 historical completions, completed exact replay, 1/2-history tracking-moved interruption with the same operation, missing current removal with only historical evidence, changed accepted epoch, extra distinct completed operation, duplicate recovery locations, malformed history, wrong private root, explicit old request UUID, malformed old preparation and ambiguous current preparation. Original zero-history phase interruptions and all unknown-native/current-provenance guards remain intact.

## Evidence

- `regression-before.{json,stdout,stderr}`: exact reviewed producer reproduced failure on the first reused slug (1 test/10 assertions/1 failure), exposing historical preparation identity selection before removal selection.
- `focused-1.*`: intermediate 12 tests/339 assertions PASS; preserved, not final evidence.
- `focused-final.*`: 13 tests/388 assertions PASS, no failures/errors/skips; command wall 37.834 seconds.
- `executor.*`: 5 tests/27 assertions PASS, 1.977s; source unchanged.
- `unchanged-guards.*`: 8 tests/45 assertions PASS, 2.731s; source unchanged.
- `syntax.*`: both changed Ruby files syntax OK, 0.568s.

Final selected suites total 26 tests/460 assertions; all before/after source hashes match. This is focused disposable producer evidence with synthetic external effects, not a full-system pass or a repeat/waiver of consumer/native/browser/CI gates. The private helper signature is the only reusable producer delta; default completed-history behavior and removal/completion serialization stay unchanged. Owner1/lead decides any bounded Go consumer evidence reconciliation for final incorporation.

Main-agent prose pass accepted the one new error and comment unchanged. No docs, schema, phase, public API, native, pin or accepted UI changes. Existing approved recovery explanation still describes the exact-operation contract.

Pending: lead step9 disposition and sole owner1 incorporation into logical recovery18. No main apply, commit, profile selection, receipt reconciliation, live deletion, retry, creation or lifecycle operation is authorized/performed by this handoff.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
