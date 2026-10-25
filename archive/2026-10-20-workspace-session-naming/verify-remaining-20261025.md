# Prepared remaining verification driver

[verify-remaining-20261025.py](verify-remaining-20261025.py) is prepared only.
It has not run. Main inspects it and selects a fresh Luna watcher after the
current source/creation batch closes successfully. That existing operation and
all active logs/handles remain owned by its watcher; do not poll or duplicate it.
Old verify-packages.py and existing evidence are unchanged.

The new driver requires a separate main release before it runs any commands.
Main writes a new JSON receipt such as
`forward-review-20261025/remaining-verification-release.json` only after accepting
the actual closed source-batch result. This is the receipt shape, not a release:

```json
{
  "schema": 1,
  "purpose": "remaining-checks-20261025",
  "approved": true,
  "client": "801099102ef9af4a82c1f3853c53d6b442ecd4dc",
  "runtime": "529e075ad07e2d967a8af4902584e37527115454",
  "preceding_result": {
    "path": "verification-source-20261025-801099-529e075a/result.json",
    "sha256": "<SHA256 of the exact completed source-batch result>"
  }
}
```

It validates that exact result directly: matching `heads`, integer `exitCode:0`,
a timezone-bearing `finishedAt`, and exactly one successful step each named
`client-source`, `client-source-root`, `native`, `message-delivery-browsers`,
`creation-inputs`, `creation`. `restoredSourceProof` must match the final A
source/NAR/catalog and name its retained root. Missing, duplicate, failed or
unknown shapes refuse before evaluation. No normalized second success receipt
is accepted. The release and original result are copied byte-for-byte into the
new run directory and their hashes rechecked between commands.

The future watcher runs once, after main release, from any directory:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/verify-remaining-20261025.py \
  --release forward-review-20261025/remaining-verification-release.json \
  --output verification-remaining-20261025-801099-529e075a
```

The output directory must be new and remain under this session. All output
directories are0700 and files0600. Session environment values must both be absent
or match the bound slug/workspace; `dev-session current` must match. Both A801099
and B529 must be exact and clean before/after every command. No fetch or rebase
is performed. Run identity includes the actual trees, commands, exit codes,
times, logs, hashes and per-command structured receipts. Failure stops the batch;
there are no retries, generic deadlines or reuse/acceptance decisions.

Before each repository's first build/check it captures all root check drv paths
with `nix eval --json --no-write-lock-file .#checks.x86_64-linux --apply
'checks: builtins.mapAttrs (_: drv: drv.drvPath) checks'`, then
`nix derivation show --recursive` over those exact paths. Raw complete JSONv4
derivations stay private and are never printed. Root membership and recursive
input references are checked; the capture is evidence for later exact-input
comparison, not automatic permission to reuse a result. B capture precedes the
collector because the probe itself uses B's Nix shell. A capture precedes A check.

The five selected checks run in order:

1. Existing run-collection-probe.sh with the final B529 source and exact head.
2. A `nix flake check --no-write-lock-file --print-build-logs`.
3. B `nix build --no-link --no-write-lock-file --print-build-logs --max-jobs 1 .#checks.x86_64-linux.package`.
4. The same B build command selecting `.#checks.x86_64-linux.session-archive-lifecycle`.
5. B `nix flake check --no-write-lock-file --print-build-logs --max-jobs 1`.

No standalone creation command is included; the full flake may normally realize
its exact cached derivation. USER DEPLOYMENT HOLD remains active. This driver
never operates on C/system builds, claims, copy/activation, profile selection,
default branches or lifecycle. C113d/7510 remains stale and frozen.

Preparation validation is Python syntax/AST only, without executing the driver,
queries, metadata generation, evaluation or any check.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
