# Focused integration wait general review

Reviewed the committed test-harness correction from obsolete amended head
`2a312616b0bf10465c33bbca97c79b31b22e8ec8` to current head
`b851ea971ed1cdcec2548395ec1ea493e8344cb6` in the general lane. Both commits
have parent `7b4aec6bb9b948ab3d1bdf90a886b99a4ebd4ff5`; the amendment changes only
`tests/suite/supervisor/runtime-ingestion.nix` (5 insertions and 5 deletions).
The worktree was clean, the repair commit message remains accurate, and the
correction belongs with the integration coverage owned by that commit.
Model/effort: gpt-5.6-sol, xhigh.

## Findings

No Blocking, Important, or Advisory findings.

The failure evidence shows that both examples stopped before publishing or
asserting because runit's default seven-second `sv stop` wait expired. The
node log confirms the nodectld wrapper receives TERM and permits its child up
to 60 seconds before SIGKILL escalation. `sv -w 90 stop` therefore covers the
known wrapper shutdown window, while the test-runner's 120-second command
timeout leaves an additional outer margin. The same timeout layering is valid
for restart, and the existing readiness helper checks the restored runit
service after each example.

Moving each stop into its existing `begin`/`ensure` scope correctly makes
restoration run when the stop command fails or times out. This also prevents a
failed first example from leaving nodectld down for the second example and the
remainder of the scenario. The delta does not change production daemon,
schema, repair, protocol, or kernel behavior.

## Residual validation limits

The corrected commands have not yet completed the planned local integration
rerun. That run remains the direct proof that each stop reaches the down state,
each ensure restarts nodectld, and all 11 examples pass within the new bounds.
The existing nodectld wrapper SIGKILL/ESRCH shutdown race seen after the two
overlapping old stop attempts is outside this test-only correction. The wrapper
code does not indicate that this exception can strand the wrapper: after
waiting for the child it joins the stop thread, and Ruby propagates an ESRCH
from that join, terminating the wrapper process so runit can observe it down.
Any repeat that nevertheless prevents a single 90-second stop/start cycle from
completing should be investigated rather than hidden with a larger timeout.
