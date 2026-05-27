# Development Notes

Use this file for durable development notes that should save time in future
work. Keep initiative-specific command history in `work/<slug>/state.md`; copy
only reusable lessons here.

## How To Use This File

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

## Cross-Project Notes

### Ruby code packaged as Nix gems must be rebuilt

- Date: 2026-05-27
- Initiative: none
- Command/workflow: vpsAdminOS `make gems` / `make commit-gems`;
  vpsAdmin `rake vpsadmin:gems`
- Symptom: integration tests or deployments may keep using older Ruby code even
  after source files were changed.
- Cause: some Ruby tools are packaged for Nix as gems, so the packaged gem
  output must be refreshed for Nix builds to consume the new code.
- Fix/workaround: rebuild the gems after functional Ruby changes to packaged
  tools such as vpsAdminOS `osctl` components or vpsAdmin `nodectl` programs.
  Commit gem rebuilds separately from functional changes.
- Verification: review the generated gem-package diff and run the relevant
  integration tests using the rebuilt package.

## Repository Notes

No durable repository-specific notes recorded yet.

## Troubleshooting Template

```markdown
### <project>: <short symptom>

- Date: <yyyy-mm-dd>
- Initiative: `work/<yyyy-mm-dd-slug>/`
- Command/workflow: `<command or workflow>`
- Symptom: <what failed and how to recognize it>
- Cause: <root cause, or "unknown" if not established>
- Fix/workaround: <what to do next time>
- Verification: `<command>` passed, or <manual check result>
```
