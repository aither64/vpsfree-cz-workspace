# Recompute a Go vendor hash when an older output is cached

In `work/2026-10-14-i-d-like-the-dev-workspace`, building the package's
`goModules` derivation after changing go.mod/go.sum exited successfully but
returned the old dependency output. The old `vendorHash` identified an existing
fixed-output store path, so Nix did not recompute the new module content.

That successful lookup does not verify the new graph. Override only the
dependency derivation's `outputHash` with a fake SHA-256 and build it again:

```nix
package.goModules.overrideAttrs (_: {
  outputHash = "sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=";
})
```

The expected hash mismatch reports the actual content hash. Update the owning
package's `vendorHash`, then verify the dependency derivation with that hash.
Calculate it from the final tracked source: Git-backed flakes omit untracked
files, and `go mod vendor` selects packages from the imports it can see. A hash
calculated before tracking new Go import files may describe an incomplete vendor
tree even when go.mod/go.sum already contain the dependency.
This dependency-only operation runs no application integration tests. Keep its
logs with the initiative and use the ordinary monitoring policy for uncertain
build duration. Do not change module source or bypass a dependency check merely
because the original cached output succeeded.
