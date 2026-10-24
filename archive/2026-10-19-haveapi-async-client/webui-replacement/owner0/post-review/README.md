# Prepared post-review verification — not launched

This is a single operation for a fresh retained Luna/low full-access watcher,
after final review acceptance and explicit lead release. It is not a general
runner and does not install dependencies or edit source. Owner1's ordinary
browser operation follows after this watcher releases the sole utility slot.

Frozen inputs:

- WebUI `8772bab21cd8739bf4672cdf4976aea2a6e59de3`, tree
  `3302fcf2bc01f1885426a69c7ddc364b8cdd35ad`, clean.
- HaveAPI `f94e65e35166a0bf8048a27c9d57c7d36957d65b`, tree
  `2f2879b95f4fba789d8a9d52ca914b8876438dae`, clean.
- Root lock SHA-256:
  `0f1d21926f6d3a00527bcd486b7f3dae50134ca1e5316b990e3538e3c99b1a87`.
- Vendored archive SHA-256:
  `41c3c3f16577dd7c8849f11615e3111302513af65a1e5640c9b121f772fb9975`.

Exact ordinary commands, in the owned WebUI checkout:

```sh
nix develop --command npm test
nix develop --command npm run build
nix build --no-link --json --print-build-logs \
  .#frontend .#checks.x86_64-linux.source-contents \
  .#checks.x86_64-linux.provenance .#checks.x86_64-linux.package-contents
```

`verify.sh` guards the exact heads/trees and clean state before and after. It
records hashes of both npm project manifests/locks, archive and provenance;
individual command/exit/stdout/stderr; Nix outputs and complete derivation data;
normal and Nix frontend build-info; and operation start/end/exit. The package
contents check builds the unchanged BFF only as required by the existing check.
No full flake, VM, Ruby suite, browser or old pilot proof is included. Existing
normal npm-ci/482-entry lock evidence is retained; no new npm-ci is planned.

Proposed launch after release:

```sh
EVIDENCE=/tmp/2026-10-19-haveapi-async-client-webui-final-checks-UNIQUE \
  bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-haveapi-async-client/webui-replacement/owner0/post-review/verify.sh
```

The parent chooses a new absolute evidence path. The script requires that
directory to be absent and creates it once. The watcher retains the full outer
operation log and actual exit, stops on the first failure, and does not diagnose,
retry, edit, publish or deploy. An unexpected local kernel compilation must stop
the exact owned operation and be reported. Silence alone is not a cancellation
condition. The parent reconciles raw evidence on completion and releases the
utility slot before owner1's browser batch.

Only `bash -n` ran during preparation. No command above was launched. Review
findings or lead direction can change this prepared operation before release.
