# Independent review of maintenance fixture isolation

No findings in committed follow-up
`d23a0e302246c2e3929d0856cf62f92eaf7ccea8..d2cb9975a88079d79f361c5b4c65836ba0835821`.
The correction is suitable for exact-head creation verification. This is source
review, not evidence that the corrected integration test has passed.

## Diagnosis and test correctness

The CI failure is in setup for `startup-failure`, before that case installs its
target-startup fault. The log shows the preceding `deadline-stop` case completing
at 23:30:43, then native `turn/steer` refusing with “no active turn to steer” at
23:30:59. Its same-ID retry refuses with “prepared message no longer matches the
thread state” at 23:31:00. Those are definite setup refusals, rather than evidence
of a retry-store capacity failure or lost delivery acknowledgment. The exact
goal-driven origin of the completing turn is inferred from the fixture source;
the log alone does not identify that causal origin.

The source supplies the relevant isolation defect: each maintenance case creates
an active root goal, proves that goal survives the transition, releases the
external model hold, and reuses the same root/member conversations in the next
case without quiescing them. A resumed or goal-driven turn can therefore finish
while the next input is selecting its steer action. The earlier case boundary
does not establish an idle conversation.

The ten added lines at `nix/tests/session-creation.nix:1042` address that boundary
without modifying delivery behavior. Cleanup runs after all retained-goal/queue,
native source outcome, continuation identity, client restoration and repeated
recovery assertions, and after saving the case's evidence. It pauses the same
fixture-owned root goal through the ordinary native API, retaining its objective,
then uses the established `retry` helper to wait for no `inProgress` root or member
turns. The callback is consumed synchronously inside each loop iteration, so its
thread variable does not escape to another iteration. Failed RPCs/reads remain
errors, rather than being accepted as settled state.

The model hold has already been removed before these waits, so they do not wait
on the fixture's own response barrier. There is no new message retry loop, new
UUID, interruption, fabricated state, deleted receipt or relaxed acceptance
assertion. Failure before preservation does not reach goal cleanup. The narrow
comment explains the lasting fixture invariant; product documentation needs no
change for this test-only correction.

## History and prior-review applicability

The complete current runtime series from merge base
`32a5e31bc32362b436ccc0cfc45b5d1b74f64cb6` is:

1. `c96503ea15eb571b3aa8cfbeee08ebbc7ed40a6b` — delivery/evidence storage.
2. `986261acebbc564a988a1fa5bed41a80bcd48ba3` — interruption settlement,
   including the folded R3 remediation.
3. `d23a0e302246c2e3929d0856cf62f92eaf7ccea8` — streamed packed-ref lookup.
4. `d2cb9975a88079d79f361c5b4c65836ba0835821` — baseline maintenance-fixture
   isolation.

The range comparison with the previously reviewed three-commit series shows
unchanged delivery/storage and packed-ref patches. The interruption difference
is the requested existing `retryAdmissionUnfenced` call plus focused coverage
with retry enabled and disabled. This is a narrow R3 correction, as recorded in
state; it introduces no new behavior boundary. The new fourth commit changes
only the pre-existing maintenance fixture and is independently reviewable from
the product changes, so keeping it separate is justified.

Prior full-review conclusions remain applicable with R3 corrected. No obsolete
branch approach, fixup-only commit or intermediate migration remains. There are
no repeated dependency or generated-update streams in the runtime series. The
companion pins currently select `d23a0e30`; their announced replacement must
remain one final mechanical update per stream and select the final runtime head
before deployment or integration. This report does not certify future pin diffs.

No migrations in this follow-up. The whole branch still contains the single
direct JSON schemas 1/2 to schema-3 marker/SQLite migration reviewed previously,
with unchanged lineage and forward-recovery requirements. The assignment/state
record no feature merge, release, deployment or external consumption. No new
schema, dependency, public interface or production code changes appear here.

## Evidence and limits

Same independent reviewer: `/root/final_review_nov8`, retained configured
`gpt-6.1-sol` / `xhigh`. Reviewed affected general and architecture concerns,
plus bounded scope/risk implications, under mandatory-change-review and all four
lane references. I reread applicable repository/workspace guidance, the design
brief, state, prior report, complete current history, exact follow-up diff,
surrounding fixture/helpers, and failure-log evidence. Source worktree was clean.

Nix parsing, embedded Python compilation and whitespace success are supplied
lead evidence; I did not rerun them. No tests, builds, CI retries, deployment,
source changes or nested agents were performed. This report is the only file
written in this follow-up. Exact-head creation verification remains necessary;
prior CI failure cannot be treated as a successful test of the correction.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-portal-message-delivery/>.
