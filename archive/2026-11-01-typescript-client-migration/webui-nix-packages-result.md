# Nix package verification result

- Result: failed (exit status 1)
- Source revision: `1ab9853312a95b5448e99fd6f83f846453de17a5`
- Checkout: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui` (clean at pre-run check)
- Command: `nix build --no-link --print-out-paths .#frontend .#bff .#checks.x86_64-linux.provenance .#checks.x86_64-linux.source-contents .#checks.x86_64-linux.package-contents`
- Log: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-nix-packages.log`
- Exit status artifact: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-nix-packages.exit`
- Elapsed time: approximately 12 seconds.

The frontend derivation failed with exit code 101 while `npmConfigHook` validated package lock consistency: `thread 'main' panicked at src/main.rs:253:30: dependency should have a hash`. Therefore the requested combined graph did not pass, and all five output paths were not produced as a successful build result. The BFF derivation was also scheduled, but the combined build stopped on the frontend error. No retry or diagnosis was performed.
