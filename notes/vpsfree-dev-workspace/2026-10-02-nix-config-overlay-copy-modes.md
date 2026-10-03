# Replacing files copied from the Nix store

The retained-services fixture failed before guest startup while building its
enabled API config overlay. The builder copied the API test config from a Nix
store source, then copied profile hooks and plans over those destination files.
The first copy retained read-only file modes, so the second `cp` failed with
`Permission denied` despite the builder owning the output directory.

Use `cp --remove-destination` for the exact files replaced by the overlay. This
recreates builder-owned destination files without changing source permissions
or making all copied config writable. Keep the ordinary fixture files intact.

Evaluation and `nix flake check --no-build` do not exercise this copy step.
Verify the actual overlay derivation from the selected configuration's
dependency graph and compare its output files with their authoritative sources.
The corrected actual overlay passed this focused realization and comparison.
The focused realization and later retained-services result are tracked in
[the storage redesign state](../../work/2026-09-23-storage-redesign/state.md).
