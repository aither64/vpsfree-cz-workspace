# Explicit archive can reject an active native verification watcher

Observed in `2026-10-28-observer-progress-guidance`, runtime `4a002f52`: all six
readiness checks passed, but `thread quiesce-explicit` failed with
`managed admission is outside the retained team`.

Archive proved the active `/root/master_ci_finish` utility's parent relationship,
then called `workspacecodex.Client.Interrupt`. The October 22 retry-admission
wrapper requires the root or a retained roster member, rejecting native utilities
that archive is nevertheless required to stop. Completed children avoid this
branch. Existing focused tests omit the production retry resolver or active-child
metadata and therefore do not expose the composition bug.

Proposed correction: separate ancestry-authorized lifecycle interruption from
managed work admission, preserving retry cancellation and uncertainty fencing for
managed threads. Test through the configured command with an active native child.
Do not add watchers to retained teams or accept ownership from CWD alone.

Waiting for the watcher to finish before ordinary archive retry may avoid this
trigger; recovery was not executed or verified. No worktrees were removed in the
observed attempt. Preserve browser receipts, recovery state and held prompts.
Full evidence: `work/2026-10-28-archive-observer-investigation/findings.md`.
