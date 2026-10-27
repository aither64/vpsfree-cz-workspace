# Corrected host VM batch: passed and settled

The single authorized batch exited **0** after **995s**, from
`2026-10-27T11:05:57Z` to `11:22:32Z`. Both requested outputs are valid.
The original command and fresh Luna/low/full-access watcher
`/root/host_352a_watcher` settled; no running or uncertain operation remains.
Lead accepted the original log, metadata and output receipts. The utility slot
is free. Old29d/6959 consumer builds remain held until their corrected-source
refresh; this result alone does not release those builds.

```sh
nix build --no-link --print-build-logs .#checks.x86_64-linux.host-module-idempotency .#checks.x86_64-linux.session-recovery-boot
```

The checkout stayed clean at
`352aa4c60457d682207b900fa5835dec82e5d064`, tree
`9dc1a1320d4cfa8034845c063fb796afa1f989c0`. Fresh independent SSH proof found
this feature head and unchanged default `fffbd0d59fffc09667cb39878d9f7da8bdcd3806`.
Nix source `/nix/store/07qi560549nhnfsirk629klyg02qv409-source` has NAR hash
`sha256-n9y+dtsffYr4cc04rg97i3UMPy53HrbvU8nITtl89hw=`.
[Full input graph](flake-metadata.json) records client
`255f0b4f74951ebbd0a5ab15eea7a3142be0ab93`, llm-agents
`ea188d2f072e0ec8d5b71245e228803672801a22` and nixpkgs
`f20cd90e28fe0403873f473b29e42662cd86e8c4`, with their exact input NAR hashes.
The matched policy catalog is
`3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`.

| Check | Derivation | Valid output |
| --- | --- | --- |
| host-module-idempotency | `/nix/store/m9q5gqjfn8yqcvyw05l78hg775l64w8d-vm-test-run-dev-workspace-host-module-idempotency.drv` | `/nix/store/apfrvraxc5szzskp68bigip5i0i3vypr-vm-test-run-dev-workspace-host-module-idempotency` |
| session-recovery-boot | `/nix/store/2i58mcav71v8sq5vhfc04sgxda6a2yj0-vm-test-run-dev-workspace-session-recovery-boot.drv` | `/nix/store/ymnk0844s835x70vzw99lsd3k0aqlmdy-vm-test-run-dev-workspace-session-recovery-boot` |

The original log records the workspace-host dependency passing 235 runs and
2677 assertions, zero failures/errors and three skips. Host-module test script
finished in 234.95s; session-recovery script in 331.75s. The recovery scenario's
provider-state assertion traces occur inside successful waiting commands; its
final script and output passed. VM cleanup completed normally. No unexpected
local kernel derivation build, cancellation, retry, extra check, native/vendor
replay, live operation or source mutation occurred.

Evidence: [complete combined output](host-module-idempotency-session-recovery-boot.log),
[timing and exit](host-module-idempotency-session-recovery-boot.meta),
[exact derivations](check-derivations.json), [valid outputs](outputs.json).
The [original35d6 failure](../host-vm-35d6/result.md) remains failed at its own input
scope. This successful corrected batch does not relabel that attempt.

Lead and owners1/2 received the success and actual combined settlement directly.
Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-codex-upgrade-naming/
