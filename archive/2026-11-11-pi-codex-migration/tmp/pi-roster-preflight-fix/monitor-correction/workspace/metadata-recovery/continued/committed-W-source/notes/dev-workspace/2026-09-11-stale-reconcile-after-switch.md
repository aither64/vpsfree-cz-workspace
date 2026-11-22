# Scheduled reconciliation can cross a package switch

Related initiative: `work/2026-09-11-devcluster-packaging-investigation/`.

A timer invocation of `workspace-codex-reconcile-pending.service` waited across a
successful `workspace-host switch` and exited with the intended diagnostic:
`workspace package transition completed while this command waited; rerun it`.
The portal, router and Codex services were active on the new profile. Re-run
`systemctl --user start workspace-codex-reconcile-pending.service` after the switch;
it loads the current generation and clears the failed result on success. Do not
bypass the generation check or roll back a healthy profile just for this refusal.
Verified Result=success and ExecMainStatus=0 after retry.
