# Cargo vendor staging and output hashes

Investigation finding from the
[syslog exporter session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/).

At nixpkgs `718f670e845328e9c2cecdd832835712b2cbd065`, comparing
`cargoHash` directly with `nix hash path` of a realized package's `cargoDeps`
reported different hashes despite a successful dependency fetch. This was a
verification mistake, not a bad package recipe.

`pkgs/build-support/rust/fetch-cargo-vendor.nix` has two stages. Its fixed-output
`vendorStaging` derivation uses `cargoHash` and recursive hashing. A subsequent
ordinary derivation transforms that staging directory into the processed vendor
directory used by Cargo. The processed directory has its own NAR hash.

Inspect the processed vendor derivation's `env.vendorStaging`, then hash each
output separately. Bind `cargoHash` to the staging output and record the processed
vendor NAR as a distinct artifact identity. Check the selected nixpkgs
implementation before assuming the same layout in another revision.

In this session both hashes were independently verified. The initial false
equality assertion needed no source edit, hash replacement or package-test rerun.
Native Git reconstruction also confirmed that the consumer changed only its
reviewed provider revision and source hash. Full identities and proof are in the
session's C2 evidence and `lead-i2-pin-reconstruction.json`.
