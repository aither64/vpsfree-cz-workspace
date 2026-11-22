# Test runner flake overrides and generated inputs

- Date: 2026-06-01
- Initiative: `work/2026-05-29-security-advisories/`
- Command/workflow: `nix run .#test-runner -- test <suite>` in repositories
  that use the vpsAdminOS test runner.
- Symptom: Passing `--override-input vpsadmin path:/path/to/worktree` to
  `nix run` did not affect the VM test definition. The test runner still built
  from the repository `flake.lock`, so the VM used an older vpsAdmin source and
  missed new API model files.
- Cause: The flake app only provides the `test-runner` binary. At runtime,
  `test-runner` calls `nix-build` on its own evaluation helper, which runs
  `builtins.getFlake(repoRoot)`. CLI overrides from the outer `nix run` are not
  forwarded to that inner evaluation.
- Fix/workaround: For temporary cross-repository integration tests, copy the
  involved worktrees to a throwaway directory, make throwaway Git commits, and
  update the temp repo's `flake.lock` with `nix flake lock --override-input`.
  If vpsAdmin is copied into a fresh Git repo, force-add ignored generated
  package inputs such as `packages/*/Gemfile.lock` and `webui/composer.lock`;
  otherwise vpsAdmin package builds can fail before the VM boots.
- Verification: The `vpsfree-irc-bot` `vpsadmin-events` suite passed from a
  throwaway Git source after locking the temp IRC bot flake to the temp
  vpsAdmin source and including the ignored generated lock files.
