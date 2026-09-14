# Regenerating fixed Go vendor hashes

Initiative: work/2026-09-14-portal-review-fixes.

After updating a provider revision in Go and Nix, temporarily set vendorHash
to lib.fakeHash and build the consumer's goModules output. Building with the
previous fixed hash can reuse a cached old output and hide a mismatch with the
new go.mod. Restore the reported hash before committing or deploying.

Verified for codex-web -> dev-workspace: the expected fixed-output mismatch
reported the new hash, and the final package and CI passed with it.
