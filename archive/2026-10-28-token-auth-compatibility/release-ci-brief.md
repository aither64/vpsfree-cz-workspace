Observe existing HaveAPI release-feature CI only. Read dev-session-monitor skill.
Managed watcher policy pinned catalog 3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41;
model gpt-6-luna/low, native utility dw_261a10738ad06c003118fa86a9c9a7ce71a28ba2529d3b2b,
selected execution_access full_access (danger-full-access, approval never).
CWD /home/aither/workspace/ai/vpsfree.cz. Session identity verified by parent:
2026-10-28-token-auth-compatibility, same absolute workspace. Check identity if
using owned resources. No source edits, diagnosis, retries, publication, deployment,
acceptance decisions or nested agents.

Exact source 819bba5110e089465535ecd71ca2eb37a7d39caa on feature branch
2026-10-28-token-auth-compatibility-0.31. Existing run IDs and names in
work/2026-10-28-token-auth-compatibility/release-candidate-runs.json. All 11 runs
belong to this head; observe each exact run (already launched by push). Reuse
completed results and gh run watch --exit-status for running ones; do not relaunch.
Keep logs under session release-ci-<run>.log and a compact release-ci-watch.md.
Expected full release build ~7 minutes, performance 6 minutes. At 15 minutes
report any running operation with last phase, retain ownership; no cancellation
or retry authorized. On failure collect bounded failed log evidence and return
without diagnosing/retrying; other run ownership stays accounted for. Return
pass/fail/incomplete, run identity/revision, elapsed, logs and still-running work.
Stop automatic monitoring only once all specified runs finish or parent direction.
