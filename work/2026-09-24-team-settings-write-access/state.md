---
lifecycle: active
---

# Team settings drafts and member write access

The plan is recorded. No project code has changed yet. The shared checkout is
dirty with unrelated work; only this initiative's paths will be staged. This
shell has no trusted development-session binding, so this is a separate
initiative.

## Next actions

1. Commit the initial plan and state, then create the initiative session and
   dedicated `dev-workspace` and workspace feature worktrees.
2. Implement the portal, CLI lock, and site catalog changes with focused tests
   and documentation.
3. Complete the required review, longer checks, live canary, and aitherdev
   user-profile deployment. Await explicit approval before default-branch
   integration.

## Evidence and decisions

- `architect0` in the observed team has a saved `read_only` policy;
  `implementer0` has `workspace_write` in both the roster and Codex rollout.
- The implementer's `dev-session current` fails opening
  `/home/aither/.local/state/dev-workspaces/transition.lock` for writing from
  its workspace-write sandbox. That failure does not prove its worktree is
  read-only.
- The user explicitly chose not to migrate existing architect members.
- OpenAI documentation confirms workspace-write permits edits within the
  writable workspace, while protected paths and paths outside it remain
  constrained. See <https://learn.chatgpt.com/docs/agent-approvals-security>.

## Repositories

Feature branches and exact heads will be recorded here after worktree setup.

## Verification

No checks run yet.
