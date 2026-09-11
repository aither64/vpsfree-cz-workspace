# Mandatory change review packet: live rollback restoration fix

## Scope and exact ranges

Live deployment testing after the clean v11 review exposed one rollback defect.
Review these exact immutable feature ranges:

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`); unchanged
  from v11.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..4881eb7d7db78f2214833190770b722181cdaeb0`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `9a13d62`, `36c7346`,
  `6eb1b4e`, `f585cb0`, `b094625`, `6d66563`, `4881eb7`).
- `vpsfree-cz-workspace`: `91b85b48b35cef51fd8920cd3445ca23a0023648..7590391e74fce6176cf1f49b1d828c983dd2c0f1`
  (`e81e7f2`, `7590391`).
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..afbda8cb7887e9bb7f57d9316a26082fe49dab6d`
  (`c6044f31`, `afbda8cb`).

All worktrees are clean and equal their remote feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@7590391 -> dev-workspace@4881eb7 -> codex-web@e8655b7`

Configuration `afbda8cb` pins `dev-workspace@4881eb7` with NAR
`sha256-RpLEIkXZ81OsfsLXQkCRZC6hDJWa8vUvM9HvH00tDK0=` and the unchanged nested
`codex-web@e8655b7` pin.

## Delta since v11 review

The provider and host closure built successfully. The NixOS substrate dry
activation and live switch passed both health checks. The user-profile switch
to generation 15 succeeded, all four user services and both runtime sockets
were healthy, the local API retained the existing thread, and authenticated
TLS routing at the stable hostname returned a healthy response.

The subsequent `workspace-host rollback` selected retained generation 14 and
its Codex root, restarted the router and consumers, then failed while restoring
the first quiesced terminal client. The outgoing generation constructed the
`dev-session sync` command with its own fixed package path and expected package
identity after the profile link already pointed at generation 14. The
generation guard correctly rejected that stale helper. Services remained
healthy on generation 14, but rollback returned failure and did not restore the
remaining quiesced terminal clients.

The fix is folded into the original host-ownership commit `9a13d62`:

- `dev_session_invocation` accepts an internal package generation, defaulting
  to the command's own generation for every existing caller;
- successful rollback restores quiesced clients through the already-validated
  and selected target profile generation;
- the private invocation uses that same package for the helper, expected host
  generation, portal and cluster command paths;
- compensation still restores through the outgoing/original generation after
  selecting it again;
- the rollback regression requires the explicit selected profile generation;
- the deployment example now uses the stable selected `workspace-host` for
  updates to an existing installation, matching the top-level installation
  instructions and generation guard.

The focused host suite passes with 55 tests and 338 assertions, and the final
dev-workspace, workspace and configuration flakes pass no-build evaluation.
The workspace and configuration pins were regenerated and republished; the
configuration input was changed only through `confctl` and its hooks passed.

All v11 conversation, path, persistence, authentication, cluster-contract and
deployment constraints remain unchanged. Default-branch integration, release,
archive, delete and session stop remain out of scope.

## Review request

Risk remains high because this changes rollback restoration across selected
package generations. Rerun General, Architecture/repetition,
Scope/proportionality and Risk/compatibility with `gpt-5.6-sol` at `xhigh`.
Focus on target-generation trust, helper/path consistency, compensation,
mixed-version behavior, test realism, documentation and exact downstream pins.
Report Blocking, Important or Advisory findings with evidence and remediation;
explicitly report clean lanes.
