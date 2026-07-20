# 2026-07-20-security-advisory-review

## Goal

Register `security-advisories` in the workspace project map and prepare an
isolated feature worktree for reviewing security advisories against current,
typed vpsAdmin Node evidence once the user supplies an authentication token.

## Affected repositories

- Top-level coordination repository: project-map documentation only, committed
  directly on `master`.
- `security-advisories`: isolated review branch and worktree, initially with no
  source changes.
- vpsAdmin: authenticated API data is an external read-only review input; no
  vpsAdmin source or production data changes are currently planned.

## Approach

1. Add `security-advisories` to the top-level `AGENTS.md` project map.
2. Fetch its canonical SSH bare clone and create
   `2026-07-20-security-advisory-review` from the current upstream default
   branch in the matching initiative worktree directory.
3. Keep the authentication token ephemeral: do not write it to initiative
   notes, repository files, command-line URLs, commits, or captured output.
4. After the token is supplied, verify its identity and permissions, inspect
   the repository's API and evidence documentation, then perform the requested
   read-only advisory review against typed vpsAdmin data.
5. Do not synchronize drafts, modify vpsAdmin data, or publish advisories
   without a separate explicit user request and the repository workflow's
   required review gates.

## Compatibility and deployment

This preparation changes only workspace documentation and creates a Git
worktree. It changes no API, schema, protocol, persistent state, generated
configuration, or deployed system. There are no mixed-version, deployment
ordering, or rollback concerns at this stage. The later review is intended to
be read-only and therefore must not change production state.

## Testing plan

- Verify the top-level documentation diff contains the intended project-map
  entry while preserving unrelated shared-worktree edits.
- Verify the advisory worktree uses the initiative branch at the fetched
  upstream default-branch commit and starts clean.
- Record exact branch, worktree, base commit, commands, and results in
  `state.md`.
