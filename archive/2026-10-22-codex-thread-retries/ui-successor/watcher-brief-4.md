# Focused browser capture attempt 4

Status: RELEASED. One fresh operation only.

Read /home/aither/.codex/skills/dev-session-monitor/SKILL.md and exact guidance:
/home/aither/workspace/ai/vpsfree.cz/AGENTS.md
/home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/verification.md
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace/AGENTS.md
Verify dev-session current = 2026-10-22-codex-thread-retries. Environment markers
must both match this slug and /home/aither/workspace/ai/vpsfree.cz, or both absent
under the exact trusted binding. Stop on mismatch.

Tracking directory: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries
Repository codex-web commit: 55e0300b27b6927b1693b3792042762f31a385cc
Repository codex-web tree: b89b91b73ad5a028edfe9e72f6ecf056bde086af
Repository dev-workspace commit: e1e165e89b7741a95a5b66dfbd15f8a3c3987285
Repository dev-workspace tree: c9874dd068d2de9431b12114e0fb91b95f1ad186
Check exact heads and clean source. Launch policy is pinned Luna/low/full_access
in ui-successor/watcher-policy.json and explicit CLI arguments.

From the tracking directory, run ONCE:
bash ui-successor/capture-attempt-4.sh

Do NOT create capture-attempt-4 yourself. The wrapper exclusively creates that
output directory, opens stdout.log/stderr.log before launch, writes result.json
with actual exit/elapsed/source and sets screenshots/. It refuses overwrite.
Do not copy/reconstruct logs or rerun. Go timeout360s is the explicit operation
bound. Use blocking waits, no silence-based timeout. Only the three selected
TestQuestionBrowser private template fixtures; no real native/provider/live work.

Completed independent reviews and direct step9 disposition are retained in
review.md, review-frontend-followup.md, review-findings.md,
review-frontend-findings.md and capture3-diagnosis-and-remedy.md beneath
ui-successor. All three prior capture3 cases failed; fixes are test-only,
quickchecked and committed. No empirical pass assumed.

No source/tracking edits, diagnosis, retry, CI, build/native, dependency changes,
claims, deployment, integration, release, lifecycle or nested agents. Only
assigned logs/results allowed. Unexpected local kernel build: stop owned command
and report. Silence alone does not authorize cancellation. Return pass/fail/
incomplete, exact command/revisions/exit/elapsed, evidence paths, bounded failures
and any still-running owned process. Parent owns diagnosis and acceptance.
