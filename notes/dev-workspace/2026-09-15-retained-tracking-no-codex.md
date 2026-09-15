# Retained tracking cannot restart as a shell-only session

- Date: 2026-09-15.
- Initiative: `work/2026-09-15-session-documentation-review/`.
- Workflow: commit initial plan/state, then run `dev-session start SLUG --as-is
  --no-codex --no-attach --json`.
- Symptom: `restarting retained tracking requires a Codex conversation`.
- Cause: existing committed plan/state with no portal manifest uses the retained
  tracking restart path. Unlike fresh shell-only creation, it requires a shared
  conversation. `docs/dev-sessions.md` documents this distinction.
- Workaround: restart the exact owned slug with `--goal-file FILE --no-attach`.
  When the originating external conversation continues to own the task, give
  the managed conversation an explicit idle-only request to avoid duplicate
  work, then verify it stays idle. Do not submit the actual work twice.
- Verification: restart completed, `dev-session current` matched the owned slug
  with both required environment variables, and the managed pane returned to
  its prompt after the idle acknowledgment without running tools.
