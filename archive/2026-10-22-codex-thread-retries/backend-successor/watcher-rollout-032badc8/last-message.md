**Result:** Failed; `public-failed-creation-recovery` recorded exit 1. The recovery status says effects are durable at `thread_retiring` and exact operation reconciliation is required. Its error reports that the expected Codex thread was absent from active discovery; `replayGETSwitch` is held.

- Evidence: [recovery-worktree.status.json](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/backend-successor/rollout-032badc8/recovery-worktree.status.json)
- The rollout operation was not cancelled. I stopped only my observation loop after seeing the nonzero exit.
- I did not inspect private recovery bodies or logs. Other status artifacts and `rollout-finished.json` had not appeared in the initial read.
- Session check matched `2026-10-22-codex-thread-retries`; the required monitor procedure was read. No source edits, retries, deployment or lifecycle actions were performed.