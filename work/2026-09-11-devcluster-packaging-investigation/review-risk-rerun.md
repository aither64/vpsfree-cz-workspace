# Mandatory change review rerun: risk and compatibility

Lane: risk and compatibility
Model/effort: `gpt-5.6-sol`, `xhigh`
Reviewed repository: `vpsfree-dev-workspace`
Reviewed range: `0a9c974994746e2a6d9d74e83cde8abbf0e65f0a..d2380cbe77f711627ba461ef9359724b6255a5db`
Owning remediation commit: `447d37c60b89e61491e9e051fa256d410c3daa3a`

This rerun reviewed the changed source-compatibility boundary introduced after
the first risk review: the public vpsAdminOS overlay, shared runner builder,
minimum supported source revision, early validation behavior, documentation and
operator action. It also inspected the direct readiness/config remediations and
the recorded reconciliation decisions; those narrow fixes did not introduce a
new design requiring a broader rerun.

## Blocking

None.

## Important

None.

## Advisory

None.

## Assessment

- `dev-clusters/lib/runner.nix` now consumes the owner-provided
  `vpsadminos.overlays.all` interface and constructs one dependency bundle for
  both provider entry points. vpsAdminOS commit
  `6f9b2c755143197bd9c3452e1c0121b22e978c4d` exports that public overlay and is
  a descendant of `b0c2ea2552ab9b3bcb493a6bdad5f23c698addcc`, which introduced
  `vpsadminosRubyGemConfig` and the source-gem configuration used by the builder.
  The documented minimum therefore contains both sides of the declared
  dependency contract.
- Both provider flakes sequence runner evaluation before constructing
  `cluster-config`. A direct packaged-flake probe over retained pre-minimum
  vpsAdminOS worktree `d9c4552dd0351a3a79ecd575dec95a0deba223fe`
  exited nonzero before configuration evaluation and reported the explicit
  `6f9b2c755` minimum plus the required worktree update. This confirms that Nix
  laziness does not defer the check until runner launch.
- Both provider READMEs and the initiative plan state the minimum revision,
  require older worktrees to rebase before `start` or `update`, and state that
  retained provider state and VM disks need no conversion. The incompatibility
  is deliberate, fails before host or guest mutation, and has a concrete
  operator recovery path. Existing running clusters can still be stopped under
  the unchanged CLI/state/socket contract; no coordinated machine update is
  required.
- Packaging installs and compares both shared assets in each provider subtree.
  The final packaged smoke completed successfully at `d2380cb`: both providers,
  bridge and local networking, defaults and overrides (eight configuration
  evaluations total), and both built/loaded runner entry points passed. The
  provider-specific executable names and `RUBYLIB` paths remain unchanged.
- The retained-readiness failure regression and checked preparation calls pass
  in the focused command suite (7 runs, 118 assertions). The vpsAdmin config
  temporary is now created beside the destination and removed after failed
  parsing or replacement, restoring same-filesystem atomic rename semantics.

## Accepted residuals and remaining coverage

- Forced certificate initialization/import and the encrypted-CA fallback still
  remove the existing regenerable development certificate set before a complete
  replacement is available. The reconciliation explicitly accepts this
  pre-existing behavior outside the packaging/control-flow scope and does not
  claim transactional credential replacement. Live acceptance must not invoke
  forced replacement or alter another session's shared CA.
- Pre-`6f9b2c755` vpsAdminOS worktrees cannot start or update through the new
  package until rebased. This is the documented compatibility boundary rather
  than an automatic historical adapter; their retained state is not rewritten
  by the failed check.
- No VM was launched during review. Real bridge startup, readiness,
  copy/activation ordering, update/stop/restart and retained-data behavior remain
  integration acceptance work. The reported live-config dry runs found both
  expected kernels substitutable and did not begin kernel compilation.
- The source worktree consumer still needs its generated final extension pin.
  It must select the pushed, reviewed `d2380cb` tree (or an exact equivalent
  final head after bookkeeping-only commit rewrites) while retaining the generic
  runtime pin and existing deployment constraints.
