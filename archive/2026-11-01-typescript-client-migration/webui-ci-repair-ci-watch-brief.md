# Exact-head required CI observation

This is a single verification-watcher operation. Read the current
dev-session-monitor skill. Session binding is2026-11-01-typescript-client-migration
in /home/aither/workspace/ai/vpsfree.cz; verify dev-session current and environment.
Worktree is worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui.

Repository: vpsfreecz/vpsadmin-webui; existing PR126; feature
dev/typescript-client-migration. Observe only exact head
`d3d5efbef53af8eb1caec025737dc47ecbc67e96` after the publication handoff.
The parent will supply registered run IDs, or authorize bounded registration
lookup for that branch/head. Never observe a moving latest run as the identity.

Required workflows are the unchanged ci.yml (CI) and e2e-smoke.yml (Playwright
smoke). CI has three20-minute jobs: nonbrowser checks, production build and
Chromium script regression. Playwright has three40-minute jobs: Chromium,
mobileChrome and actual mobileWebKit. The desktop comment estimates30minutes
before setup/reporting; quiet execution is not failure. Poll about30seconds,
using interruptible waits of at most60seconds. Queued/resource waits are not
test failure. Escalate if registration remains absent after five minutes or an
active job exceeds its declared limit plus artifact-upload headroom; retain
ownership and report actual status instead of inventing a timeout conclusion.

Use native gh read-only commands through the repository Nix environment if
needed. Track exact run IDs/attempts/headSHA and all six job conclusions. Remote
GitHub status/logs are independent observation interfaces. Keep compact native
metadata/status receipts and complete failed-job logs when available. On first
terminal failure, notify the parent with the job/step/error evidence while
continuing to account for the remaining owned workflows. No diagnosis or rerun.

No cancellation, dispatch, retry, source/Git mutation, installs, package builds,
merge, deployment, SDK publication, session cleanup or lifecycle action. Do not
increase CI limits, change selection, edit tracking state or spawn another agent.
Requested watcher logs/results under this session directory are allowed.
Never print credentials, environment dumps or full sensitive headers.

Return a compact final result in webui-ci-repair-ci-native-result.md and report
to the parent: passed/failed/incomplete, exact head, run/job IDs and conclusions,
elapsed times, bounded error excerpts, artifact/log locations and any ongoing
operation. A successful local news5/remaining98 or Nix result does not make CI
pass. Earlier run41366168907/attempt1 remains a failed/incomplete historical run;
do not add its partial case counts to this head's results.

Retained utility policy: catalog495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7,
gpt-6-luna/low, operation lifetime, max_concurrent1, full_access/approval never.
Native identity dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96;
configuration in the selected package's
share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml.
