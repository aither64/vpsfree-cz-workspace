# Development Notes

Use this directory for durable development notes that should save time in
future work. Keep initiative-specific command history in
`work/<slug>/state.md`; copy only reusable lessons here.

Create a separate file for each durable lesson so multiple Codex instances can
add notes concurrently without editing one shared notes file.

## Layout

- `notes/cross-project/<yyyy-mm-dd-short-topic>.md`: lessons that apply across
  multiple repositories or the whole workspace.
- `notes/<project>/<yyyy-mm-dd-short-topic>.md`: lessons that apply to one
  repository.

## How To Add A Note

Add a note when a command, shell, test, build, deploy, hook, or worktree
operation fails in a non-obvious way, or when an investigation finds a useful
dead end. Prefer short, practical entries that explain how to recognize the
problem and what worked.

Each note should include:

- project or repository;
- date;
- command or workflow;
- symptom;
- cause, if known;
- fix or workaround;
- verification command and result;
- related initiative path, if any.

Summarize long logs instead of pasting them. Redact secrets, tokens, host keys,
API credentials, private customer data, and unrelated local details. Avoid
recording temporary local paths unless they are part of the problem.

## Troubleshooting Template

```markdown
# <project>: <short symptom>

- Date: <yyyy-mm-dd>
- Initiative: `work/<yyyy-mm-dd-slug>/`
- Command/workflow: `<command or workflow>`
- Symptom: <what failed and how to recognize it>
- Cause: <root cause, or "unknown" if not established>
- Fix/workaround: <what to do next time>
- Verification: `<command>` passed, or <manual check result>
```
