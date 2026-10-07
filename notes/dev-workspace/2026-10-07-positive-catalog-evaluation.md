# Force the catalog package derivation path for positive evaluation fixtures

The catalog fixture's evaluate helper deep-forced the full mkPackage derivation.
This worked for rejected configurations because validation threw first, but a new
valid lead-owned configuration reached the derivation graph and caused stack
overflow during nix flake check --no-build.

Force (mkPackage { ... }).drvPath with builtins.seq instead. The path forces
package evaluation and its catalog validation without recursively traversing
derivation attributes. Valid and invalid catalog assertions then evaluate, and
the packaged catalog remains covered by its build-time jq assertions.

Verified by the generic Nix evaluation and composed workspace evaluation in
work/2026-10-07-lead-review-defaults/. Avoid treating deepSeq on a complete
package as a pure configuration validator.
