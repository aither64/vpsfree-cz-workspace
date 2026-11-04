# Phase 2 native CI observation operation

You are an operation-only verification watcher. Read the dev-session-monitor
skill at /home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/skills/dev-session-monitor/SKILL.md.
Use exact policy gpt-6-luna/low, fresh context, full_access/danger-full-access,
approval never, native utility identity dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96.
Matching config /nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml;
catalog495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7.
Bound session2026-11-03-vpsadmin-client-sync, workspace/home/aither/workspace/ai/vpsfree.cz.

Observe ONLY the9exact repo/run/head entries in phase2-ci-runs.json alongside
this file. Do not launch tests/workflows, edit source, retry, approve or deploy.
Do not spawn agents. Parent source/package owners have selected these existing
automatic runs after independent final documentation review. Several are already
terminal success; collect each once then stop polling completed runs. Verify
head matches the listed exact source. Do not follow moving latest branch runs.

Retain structured final run/job metadata and failure logs/artifacts under
phase2-ci/. Status can be read with gh run view --json headSha,status,conclusion,jobs,url;
use gh run view --log-failed/download only for actual failures. Avoid full-log
output to parent; no credentials. For remaining active runs use bounded sleeping
or native waiting, not busy polling. Reassess progress at10min with a compact
current job/queue/result checkpoint; no arbitrary timeout/cancel for silence.
Expected remaining native runtime5-20min including API queue/browser/performance.
On failure promptly report evidence and retain accounting for other runs; never
retry or waive a check. Finish when all runs terminal or return explicit incomplete
status/accounted running IDs on parent direction. No local runner is owned.

Return compact phase2-ci-result.md with exact heads, run conclusions, log/artifact
paths, elapsed time and any remaining operations. Writing these local evidence
files is allowed, but no state.md/project edits. Parent resumes automatically.
