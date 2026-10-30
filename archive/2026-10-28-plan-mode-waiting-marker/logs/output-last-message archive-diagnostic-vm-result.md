Result: failed (acceptance failure); Nix build exit status 0.

- Runtime `5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3`; fixture/worktree `08f3dbb92bc8585929edee85a824d44dfb3b0846`.
- Check derivation `/nix/store/w3pwbnfc8afpc6d8rgl8ylplwjy24xn2-vm-test-run-dev-workspace-session-archive-lifecycle.drv`; driver `/nix/store/gr2j8vakpy61jhbm2vk5cfc9vh1y74bb-nixos-test-driver-dev-workspace-session-archive-lifecycle.drv`; output `/nix/store/spz3nyvgpvg86nngks6fxwx8zjzhwp09-vm-test-run-dev-workspace-session-archive-lifecycle`.
- Command: `nix build --no-link --print-out-paths --print-build-logs --max-jobs 1 /nix/store/w3pwbnfc8afpc6d8rgl8ylplwjy24xn2-vm-test-run-dev-workspace-session-archive-lifecycle.drv^out`
- Elapsed: 1037 seconds. Full log: `archive-diagnostic-vm.log`; raw result: `archive-diagnostic-vm-result.json`.
- Failure excerpt: repeated Python assertion `d.get('state') in ['complete','failed','paused']` raised `AssertionError` during post-revive operation polling. VM test script ended after 1030.91 seconds; QEMU cleanup completed. Nix derivation itself returned exit 0.
- No operation remains running; no cancellation taken.
