---
lifecycle: active
---

# 2026-09-13-portal-file-links

## Repositories

- Shared coordination checkout: /home/aither/workspace/ai/vpsfree.cz, master.
- Feature slug/branch: 2026-09-13-portal-file-links.
- Generic worktree: worktrees/2026-09-13-portal-file-links/dev-workspace,
  base origin/master (8f75ece30462b184065f21867508af5e14365c4a).
- Planned consumer worktrees: vpsfree-dev-workspace and workspace under the same
  worktree group. Exact heads and bases will be recorded before review.

## Status

Initial implementation planning complete; no project code committed yet. This
conversation owns the implementation. Created a shell-only managed session to
avoid starting a second Codex writer.

## Commands run

- Inspected current implementations, local AGENTS.md files, generic and Codex
  repository refs, workspace package pins and previous deployment notes.
- dev-session current initially reported no current session. Started
  dev-session start portal-file-links --no-codex --no-attach --json.
- Verified current with DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE set to this
  exact session and workspace. Read mandatory review, handoff, writing and
  English humanizer skills.
- Fetched workspace and generic origin. Shared master matches origin/master;
  unrelated dirty tracking records are preserved.

## Results

Root cause: shared portal Markdown renderer keeps absolute file destinations as
site paths; routing has no corresponding handler. Existing review editor already
supports full-file mode and highlighted line reveal. Existing artifact opening
and repository resolution provide the boundaries to reuse.

## Open questions

None. User chose current worktree content with archived-final fallback and
verified repositories plus curated artifacts. Aitherdev deployment is authorized.

## Cleanup

Retain branches and session. No archive, delete or integration authorization.
Stable portal URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-13-portal-file-links/
