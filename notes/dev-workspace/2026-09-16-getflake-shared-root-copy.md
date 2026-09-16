# Avoid implicit path flakes for the shared coordination root

During work/2026-09-16-archive-retirement-timeout/, an exploratory
nix eval --impure expression using builtins.getFlake (toString ./.) from the
shared coordination root took unexpectedly long. It treats the root as a path
flake and can copy its large local repositories/worktrees instead of using the
small Git source view. The task-owned evaluation was terminated.

Use the isolated feature worktree and nix commands with --inputs-from . for
pinned tool lookup, or an explicit Git flake reference. Pinned playwright-test
and playwright-driver.browsers outPath evaluations then finished normally.
