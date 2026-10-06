# Markdown wrapping assertion fix

Implementer0 made the assigned test-only correction in
`worktrees/2026-10-04-session-modes-review-timing/workspace/test/agent_instructions_test.rb`.

Six text reads now apply `.gsub(/\s+/, ' ')` before the existing assertions:

- `test_final_review_timing_and_substantive_documentation_are_consistent`:
  normalize each policy document, including a wrap between `never` and `trigger`.
- `test_default_sol_policy_documents_exact_requested_model`: normalize the
  core and team guide, including a wrap before `their saved model`.
- `test_team_ownership_and_progress_policy_is_routed_consistently`: normalize
  core, session guidance and team guide, including a wrap after `delegated`.

All existing assertion patterns, expected policy wording and exact model
identifiers are preserved. No policy or documentation was changed to satisfy
the tests. All unrelated work was preserved; no other application file changed
during this follow-up.

`dev-session current` confirmed the bound session; both identity environment
variables were absent. `git diff --check` passed in the workspace worktree.

Ruby verification remains pending with the parent. Resolving the pinned binary
with `nix eval --offline --raw --inputs-from . nixpkgs#ruby.outPath` still failed
with `cannot connect to socket at /nix/var/nix/daemon-socket/socket: Operation
not permitted`. No realized pinned Ruby path was available in the session
evidence. No ambient interpreter fallback, long check or subagent was used.

The parent can rerun its realized pinned Ruby binary with
`test/agent_instructions_test.rb` from the workspace worktree, or use:

```sh
nix shell --inputs-from . nixpkgs#ruby -c ruby test/agent_instructions_test.rb
```

No commits, pushes, pin updates, deployments or lifecycle actions performed.
Parent plan/state/manifest remain untouched.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-04-session-modes-review-timing/
