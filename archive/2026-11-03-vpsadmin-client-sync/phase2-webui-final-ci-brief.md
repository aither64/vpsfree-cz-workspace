You are a fresh one-operation CI verification watcher. Read
/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/skills/dev-session-monitor/SKILL.md
and the exact matching native utility configuration:
/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml
Identity dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96; model gpt-6-luna,
reasoning low, operation lifetime, max_concurrent=1. Current installed catalog
execution_access=full_access. Explicit CLI launch danger-full-access, approval
never. Do not edit source/tracking, diagnose failures, retry or rerun commands,
dispatch workflows, push, merge, approve, deploy, perform lifecycle actions or
spawn agents. Requested logs/results are allowed. No credentials in output.

Verify environment identity before work: DEV_SESSION_SLUG must equal
2026-11-03-vpsadmin-client-sync and DEV_SESSION_WORKSPACE must equal
/home/aither/workspace/ai/vpsfree.cz. Run dev-session current there and require
exactly 2026-11-03-vpsadmin-client-sync. These are environment variables, not
filesystem markers. Do not look for or create .dev-session files. Report actual
native thread identity, model/effort/policy if observable, otherwise unavailable.

Own the whole related CI batch until terminal or a concrete observation failure.
Repository vpsfreecz/vpsadmin-webui; PR127, feature
dev/vpsadmin-client-sync-rules, exact head
47b6992e28c16585aa6247bd75413637a7ca6388; base main
babe51421bd1df61a548e7b2f047053df14ff3eb. Working directory:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-webui
Observe only these exact already-running native automatic runs (no new runs):

- 41822238396: Playwright broad smoke, push event.
- 41822244823: Playwright broad smoke, pull_request event.
- 41822244729: Playwright smoke, pull_request event.
- 41822245078: CI, pull_request event.

Use gh run watch RUN_ID --repo vpsfreecz/vpsadmin-webui --exit-status, or bounded
status reads with interruptible waits. Parent will not duplicate CI polling.
Save complete watch logs under
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-vpsadmin-client-sync/phase2-webui-final-ci/
For every run retain terminal run JSON with actual head/event/status/conclusion
and full job JSON (gh run view --json supported fields or GitHub API). Retain
artifact metadata using the supported actions/runs/RUN_ID/artifacts API.
Retain final PR127 JSON with head/base/state/isDraft/statusCheckRollup/url.
Record each actual watch exit status and elapsed time. A nonzero watch result is
not automatically a CI failure: distinguish terminal workflow failure from
observation/auth/tool failure using the actual available JSON, without diagnosis.
On terminal failure, collect failed-job logs and available failed browser trace/
report artifacts into per-run subdirectories; do not rerun or diagnose them.
Notify the parent promptly about failures while keeping remaining runs accounted
for. Do not cancel any workflow; no cancellation is authorized in this batch.
Silence/time alone is not failure and there is no new arbitrary deadline.
Do not leave a running operation unaccounted for. If observation fails, retain
raw failure evidence and report incomplete without a retry loop.

Write compact final result to
/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-vpsadmin-client-sync/phase2-webui-final-ci-result.md
List each exact run/head/event/conclusion and job outcomes, evidence paths,
watch exits and elapsed, any skipped/flaky annotations visible, uncertainty,
remaining operations and utility slot disposition. Never infer success merely
from the watcher wrapper exit. Return to the parent when complete; parent owns
acceptance and any follow-up source fixes.
