# Packaged checks watcher result

- Result: failed (exit status 1)
- Tested revision: `f094a94b50836028a62920c75f2ebd2a9ea97d94`; worktree was clean at launch.
- Execution policy: gpt-6-luna / low, native utility `dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`; full access (`danger-full-access`, approval `never`).
- Command: `nix build --no-link --print-build-logs .#checks.x86_64-linux.session-archive-lifecycle .#checks.x86_64-linux.session-recovery-boot .#checks.x86_64-linux.host-package-contract .#checks.x86_64-linux.package`
- Elapsed: 106 seconds. No process remains running; no cancellation was taken.
- Full output: `packaged-checks.log`
- Failure excerpt: `WorkspaceHostTest#test_workspace_host_loads_dev_session_only_for_archive_recovery` failed at `source/test/workspace_host/archive_recovery_test.rb:39`; packaged `.dev-session-wrapped` could not load `workspace-archive-check` (`LoadError`). Summary: `229 runs, 2515 assertions, 1 failures, 0 errors, 3 skips`. Failed derivation: `/nix/store/zjl8lcazbw5vx6xkh7m3lzgxi1d4mlyz-dev-workspace-workspace_host-0-of-1.drv`.
