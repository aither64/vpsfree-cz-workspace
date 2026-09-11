# Architecture and repetition review rerun

Reviewed the shared-runner remediation in organization range
`0a9c974994746e2a6d9d74e83cde8abbf0e65f0a..d2380cbe77f711627ba461ef9359724b6255a5db`,
with the owning design change in
`447d37c60b89e61491e9e051fa256d410c3daa3a`. The supplied review head
`44c3e4647e0834e971a5167d8019228f35f6f0b7` and remediation commit
`9cc72e1467d622423f054b4a92480814ed0b8f50` were rewritten only to correct
commit messages; their trees are unchanged. The review covered the two packaged
provider flakes, their organization-owned shared runner builder, the package
copy boundary, and the pinned vpsAdminOS public overlay and test-runner
dependencies. Direct lifecycle and documentation fixes were outside this rerun.

## Findings

No Blocking, Important, or Advisory findings.

## Resolution of the previous Important finding

Commit `447d37c60b89e61491e9e051fa256d410c3daa3a` removes the two independent
copies of the vpsAdminOS overlay and runner dependency construction. The single
source at `dev-clusters/lib/runner.nix:9-34` now consumes the owning
vpsAdminOS `overlays.all` export and constructs one Bundler environment from
the selected vpsAdminOS source. The provider flakes retain only their runner
name and provider-specific Ruby library path at
`dev-clusters/vpsadmin/flake.nix:100-109` and
`dev-clusters/vpsadminos/flake.nix:65-74`. Adding or changing source-gem overlay
wiring therefore has one organization-side integration point instead of two
provider implementations that can drift.

The package boundary does not create a second owner. `nix/organization-tools.nix:90-96`
materializes the same organization-owned `runner.nix` into each standalone
provider subtree, and `nix/organization-tools.nix:150-158` checks both installed
copies byte-for-byte against that source. The installed vpsAdmin and vpsAdminOS
copies were also compared directly and were identical.

Both configuration outputs force the runner interface during evaluation at
`dev-clusters/vpsadmin/flake.nix:89-98` and
`dev-clusters/vpsadminos/flake.nix:54-63`. A focused evaluation against the
pre-interface vpsAdminOS parent `6b768aaae94be19e0d0a78d661c5033e49a72512`
failed at this boundary with the explicit requirement for commit `6f9b2c755` or
a compatible newer `overlays.all`. Evaluation of both supported provider
runners resolved the same `devcluster-runner-deps` derivation. These checks
cover the concrete failure modes behind the original finding: a stale retained
vpsAdminOS worktree fails before a cluster configuration build, while the two
providers cannot silently select different runner dependency recipes.

The generic runtime remains a dispatcher and does not acquire runner dependency
knowledge. The workspace consumer continues to select the organization package
and vpsAdminOS source through its existing package and environment contracts;
its later revision pin is mechanical and does not add another implementation.

## Validation

The post-remediation `devcluster-check` for this unchanged tree completed with
exit 0: all eight provider/network/default-or-override configuration evaluations
and both runner builds and loads passed. `git diff --check` also passed for the
reviewed organization range.

## Residual gaps

- Per the review constraint, no live VM start, update, stop, restart, retained
  disk, or mixed-generation exercise was performed.
- The one shared organization helper still follows the selected vpsAdminOS
  test-runner's Gemfile, lockfile, gemset, and source-library layout because the
  owning flake does not export a generic alternate-entry-point runner builder.
  This coupling is localized, checked during configuration evaluation, and
  exercised for both packaged consumers; it is a remaining dependency boundary,
  not repeated provider logic.
