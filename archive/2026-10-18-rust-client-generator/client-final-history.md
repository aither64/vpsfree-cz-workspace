# Final client history and verification inputs

Client branch `2026-10-18-rust-client-generator`, retained neutral empty root
`b67a3ba5eef89b2bd6533050aa8769aaa0574114`.

Final series:

1. `f88d86ae97d335e4c89464a004e882fc7032720e` — handwritten crate packaging,
   sanitized public schema and inventory, provenance, examples, tests, docs and CI.
2. `62753f006d7bd3e5befe1033c49a2c630ca3ff02` — generated source and copied runtime.

Final tree: `7a3167614dae9abd5c73a85df1c0746d18838a32`.

The package commit incorporates the reviewed static acceptance-stage diagnostics
from `d7f46d0`, the token-request numeric HTTP status diagnostic from `7279dd9`,
and the final provenance revision. The generated commit preserves the generated
tree from the passing inputs and records the final HaveAPI revision in its
message. No repeated generated/provenance update stream remains in the feature
history. No migrations were introduced, merged, released, deployed or consumed.
Existing API migration action bindings are unrelated to database migrations.

Compared with the actual-server passing client
`7279dd9916651c68f60123c9164ec74c1a2d9c31`, the final tree changes only the
`schema/provenance.json` generator revision from `e9173e2` to
`9e4c29a0412a25256ce944641f60ba13e9f03c2b`. All 686 generated Rust files, the
generated ownership manifest, the handwritten library and passing acceptance
test, schema/inventory, dependency locks and toolchain configuration are byte
identical. Full logical commit mapping is in
[client-final-range-diff.txt](client-final-range-diff.txt); file hashes and the
existing package inventory are in
[client-final-input-receipt.json](client-final-input-receipt.json).

Final quick checks passed: deterministic generation and read-only `--check`,
`cargo fmt --all -- --check`, `tools/check-provenance`, shell syntax and Git
whitespace/clean-status checks. No compilation, server or live request was run
for this revision-only metadata change. Prior verification evidence remains
bound to its tested heads and unchanged input hashes.

The retained package archive has 697 entries and a VCS stamp for `1a818c4`.
Its ordinary source payload matches the final checkout; its normalized
`Cargo.toml` is Cargo-generated. `schema/provenance.json` is excluded by the
manifest's package include list. A fresh archive can differ because Cargo's
VCS stamp changes: no identical archive-byte claim is made for the final head.

The external public smoke README guard now names the final client head. Its
source and manifest hashes remain unchanged. No requests were repeated.
Feature publication and default-branch integration have not been performed.
