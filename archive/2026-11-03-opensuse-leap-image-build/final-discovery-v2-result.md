# Final source v2 discovery result

- Result: failed, with uncertainty limited to native listing unavailable from this host's store state.
- Tested revision: `742eb30cb1a8b6766c85e915d26b0400e38244b1` in the vpsadminos worktree.
- v2 module SHA-256: `f6bebf53ebdb690c996fd325ced3db201403d97dc1e525731ea9178b849fd90d`.
- Exact first shell block: passed (exit 0). Parsed and evaluated priority result `{ image = 8192; namespaces = 4096; }`.
- Exact second shell block: failed (exit 1) before listing targets. Nix reported that `/nix/store/m1n49nc1qdf1f3j298zcmjjb5ni43iag-source` does not exist, then `unable to resolve and GC-root repository source (1)`.
- The `systemd/device-units#opensuse-*` listing was not run after this failure, per the no-retry/stop-on-failure instruction.
- Full captured output: [final-discovery-v2.log](final-discovery-v2.log).
