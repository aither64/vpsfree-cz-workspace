# Post-merge archive failure

## Post-merge archive CI follow-up: worktree registration

Master CI 40229910427 failed only archive (job 121279205759); creation, fast and
host passed. Exact b974f2f3. Failure is worktree add immediately after native
session start: "another dev-session command is changing ...". Earlier archive
run at the exact same head passed. Do not rerun unexplained failures. Historical
holder PIDs are not present in the retained VM log; diagnostics also show a
portal shutdown timeout, recorded separately without assuming it caused this lock.

The worktree command intentionally rejects competing exclusive session writers;
Ruby test_worktree_mutations_use_the_slug_lock asserts this. A blind wait:true
would change that contract. Reproduce with an identified actual portal
queue/reconcile SH admission on the same device/inode, then scope the fix to
worktree-add: on EX/NB contention, a successful SH/NB probe identifies compatible
readers and permits waiting for EX. A failed SH probe keeps writer refusal.
Use the existing host-lock helper with one optional internal flag, passed only
from worktree-add via with_slug_lock. Keep all actual validation after EX, retain
existing provider/lifecycle/generation locks and refusal behavior, and introduce
no new lock file, state format, restart, global lease or generic retry loop.
Other commands retain their current behavior.

Quick acceptance: deterministic Go/Ruby boundary regression with real Git
worktree creation and identified Go SH holder; prove no mutation before release,
unrelated slug worktree registration remains usable, and writer EX still refuses.
Run focused Ruby worktree/lock tests and related Go tests. Record pre-fix failure.
Commit one forward-only fix (b974f2f3 is already merged), run applicable independent
review before the archive VM/CI. Reconcile exact tested source, downstream pins,
deployment need and approved integration scope after the fix is concrete.
No machine or repository claim is held for this work. Earlier three merges and
machine release remain complete. Initiative stays active until follow-up settled.
