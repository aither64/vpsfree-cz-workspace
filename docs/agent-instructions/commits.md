# Commits and hooks

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

## Commits

Write informative commits. A commit message must explain what is changing and
why it is needed. The subject should summarize the change; the body should
explain the problem, rationale, and deployment or compatibility notes when that
context matters. Do not add command transcripts, "Checks:", "Tests:",
"Syntax checks:", "Validated with:", or local tool availability notes to commit
messages; record validation in `state.md` or PR notes instead.

Rules:

- Wrap every commit message line at 80 characters or fewer. Generated
  `confctl ... --commit` messages in `vpsfree-cz-configuration` are the
  exception: keep them exactly as generated, even when they exceed this limit.
- Always write the commit message to a temporary file and commit with
  `git commit -F <tmpfile>`.
- Do not use `git commit -m` for final commits.
- Pre-commit hooks are mandatory, not advisory. Before the first commit in a
  repository or worktree, verify that the repository's hook framework is
  installed and active when the repository declares one, for example
  `.overcommit.yml`, `.pre-commit-config.yaml`, `lefthook.yml`, or Husky
  configuration. Install hooks with the repository-documented command, or infer
  the standard framework command when documentation is missing.
- Do not commit when expected hooks are absent, fail, or cannot be run. Fix the
  hook setup or the reported offenses first. Only continue without hooks when
  the user explicitly authorizes it for that commit, and record the reason and
  replacement checks in the initiative state.
- Running syntax checks or selected tests is not a substitute for hook-managed
  lint/format checks. If a hook framework cannot be installed but the
  equivalent command is known, run that command manually before committing and
  record that fallback in state.
- Do not bypass git hooks unless the user explicitly authorizes it and the
  reason is recorded in the initiative state.
- Keep commits focused. Split generated updates, dependency bumps, release
  metadata, and functional changes when repository rules or review clarity call
  for it.
- Respect each repository's local commit subject style and special release or
  generated-file rules.
