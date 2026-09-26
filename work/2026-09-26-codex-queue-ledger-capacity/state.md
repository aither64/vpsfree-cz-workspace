---
lifecycle: active
---

# Codex submission-ledger capacity

Initial plan prepared; no source changes or deployment yet. This conversation
has no inherited session binding, so the user-requested fix uses its own dated
initiative. The shared workspace checkout has extensive unrelated changes;
stage only this initiative's owned paths.

## Next actions

1. Commit this initial plan/state, then start the exact session and register
   dedicated worktrees for all four repositories.
2. Implement ledger capacity and compaction, member lifecycle cleanup, and
   exact downstream pins; review, verify, deploy, and smoke-test assignment.

## Baseline

- Generic `dev-workspace` pins `codex-web` `01e75798654b` in `flake.nix` and
  `portal/go.mod`; the installed user-profile package is
  `/nix/store/rvnahc2nfixg7v2brzm04v6cfri2ibaz-dev-workspace-0.2.0`.
- Prior Team-settings heads are unmerged: generic `9e97536`, extension
  `1a022c2`, workspace `ff0cc0a`. New downstream branches will stack on them
  to preserve currently deployed behavior without changing those initiatives.
- The active ledger was 1,048,127 bytes. Only aggregate counts and sizes were
  inspected; no messages, IDs, digests, or raw JSON were output.
