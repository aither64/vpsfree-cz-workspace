# Exact livepatch fixtures are external build artifacts

Related initiative: `work/2026-08-06-node-kernel-history/`

## Symptom

`tests/suite/kernel/livepatch-6.12.95.nix` deliberately checks SHA-256
identities for the corrected, released-v1, and predecessor modules before it
evaluates the VM test. Rebuilding `released-v1.nix` and `predecessor.nix` can
produce valid modules at the same derivation output paths whose file hashes do
not match those recorded by the test.

For example, the released-v1 derivation
`sqwm59mz2ac2840k60adq6qppygj9jba-livepatch_1-6.12.95.drv` is identical at
vpsAdminOS commits `008aa4605` and `a9baea19c`, but a local build produced
`5dfb6bda...` instead of the required `a3f79b22...`. The signed cache artifact
from the original v1 derivation produced `0d7c7722...`, also not the required
fixture. The locally rebuilt predecessor produced `154cd274...` instead of
`70f22f6f...`. The corrected v2 build did match its expected
`88e7aede...` identity.

## Cause and impact

The kpatch build is not content-addressed at the module-file level, and the
fixture hashes identify the exact modules used for the original transition
validation, not merely equivalent rebuilds of their Nix derivations. A valid
Nix output path or signed binary-cache artifact is therefore insufficient.
Changing the expected hashes to a convenient local rebuild would discard the
production transition identity the test is meant to protect.

## Workflow

Retain or publish all three exact `.ko` files when their expected hashes are
introduced. Before running the gated suite, verify each file with `sha256sum`
and pass its store path through:

- `VPSADMINOS_LIVEPATCH_CORRECTED_MODULE`
- `VPSADMINOS_LIVEPATCH_RELEASED_V1_MODULE`
- `VPSADMINOS_LIVEPATCH_PREDECESSOR_MODULE`

Do not weaken or update the assertions merely to accept a rebuild. If the
original files are unavailable, record the exact mismatch and treat the gated
transition test as unavailable; use the ordinary evaluation, hook, reporter,
and application integration checks for the change, and arrange durable fixture
storage before the next transition test update.
