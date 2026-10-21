# Verification operation

Source client 4b73d71140d1fc6ba5e43f7144bad45d7c48af9f and runtime
52f87e18e21b0e878f1255326d72cfdff61f4e09. Observe existing Actions run
39436163070 in aither64/dev-workspace and completed client run 39435851092 in
aither64/codex-web; do not relaunch CI. Save compact exact-SHA results and failed
logs if needed. Existing failed attempts are diagnosed in original state.md.

Observe parent-launched preparation through preparation-progress.json,
preparation-result.json, machine-prepare.log, profile-prepare.log, and driver PID.
Do not launch the driver or any prepare/deploy mutation. It only calls coordinator
prepare, never approve/reserve/submit/activate. Build diagnostics may be retained
privately by the coordinator and need not stream to these logs.

Read ~/.codex/skills/dev-session-monitor/SKILL.md and workspace verification
procedure. Watcher policy: installed catalog ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376,
gpt-6-luna/low, utility dw_91978c240a6a43c2168b5be643cb58668a0bdf42d703ed0e.
Full-access execution, approvals never. No edits except requested logs/results,
no diagnosis, retries, approvals, deployment, or nested agents. If an unexpected
Linux kernel build occurs, report and stop only this owned preparation process
under the workspace kernel escalation rule. Silence alone is not cancellation.

Return passed/failed/incomplete, exact run/revision identities, elapsed time,
logs/artifacts, bounded failure evidence, and any still-running work. Parent
interprets results and continues automatically.
