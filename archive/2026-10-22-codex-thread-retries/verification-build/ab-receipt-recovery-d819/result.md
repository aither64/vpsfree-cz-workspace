# A/B derivation receipt recovery result

Result: INCOMPLETE.

Session binding matched `2026-10-22-codex-thread-retries` at `/home/aither/workspace/ai/vpsfree.cz`. Before the operation, A and B matched the packet's exact HEAD and tree identities, both working trees were clean, and both current `flake.lock` hashes matched the preserved original lock copies.

The A recursive derivation command ran once from the A source root. Exit status: 0. Elapsed: 43.182 seconds. Full command is in `A.command.txt`; stdout is retained in `A-recursive-derivations.json` (3,978,433 bytes); stderr is in `A.stderr.log`; timing and exit are in `A.status`.

The immediate root comparison command exited 5 and produced no root-match result. Its stderr is retained in `A-compare.stderr.log`; comparison output is `A-root-match.txt`. Under the released packet's stop-on-first-failure rule, no B reconstruction or further evidence collection was run. The A reconstructed roots therefore remain unconfirmed against the original successful result pairs. No output closure receipts, selector inventory, Ruby shard graph inventory, or supplementary platform/Nix metadata were collected.

The original successful test/build evidence was not modified. This recovery operation is not a new test success. No build, realization, test repetition, source/ref edit, retry, deployment, or cleanup was performed.
