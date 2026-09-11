# Mandatory change review packet: unregister ownership isolation

## Scope and exact ranges

Review these exact immutable feature ranges after the v16 Risk remediation:

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`); unchanged.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..06947670dcb2d62b0b323885d1be6962ae62f400`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `21831fd`,
  `f8b2b0c`, `9ff2b54`, `c804c83`, `32cb196`, `d5e0f62`,
  `0694767`).
- `vpsfree-cz-workspace`: `ecbfb9a8a0d5fda49da1a2171e5c93449f8937cb..c4db2ca46a0f2060741a91ba763eb7fba372203e`
  (`a573dff`, `59b9948`, `c4db2ca`). It remains based on current shared
  `master`.
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..46f7dd90564ad65e8523a4a7bf3514d8325f9dad`
  (`986a93d7`, `710a2fba`, `46f7dd90`).

All worktrees are clean and equal their remote feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@c4db2ca -> dev-workspace@0694767 -> codex-web@e8655b7`

Configuration `46f7dd90` pins `dev-workspace@0694767` with NAR
`sha256-4OkE53/5mKdnZP4Q+cFrbaoyeWXoHiR2P5amIM7lulo=` and the unchanged nested
`codex-web@e8655b7` pin.

## Delta since v16 review

The v16 General, Architecture and Scope lanes were clean. Risk found one
Important name-ownership isolation gap: a different authoritative registry
entry prevented dependent service and client recovery, but the old retired
runtime was still restored independently to the active path keyed by that same
name. A later service start for the replacement could therefore encounter the
old workspace's sockets and authority.

The remediation is folded into host commit `0694767`:

- registration reconciliation returns an explicit authoritative state:
  `original`, `restored`, `absent`, `foreign` or `unknown`;
- an exact original or successfully restored entry enables normal recovery;
- an absent entry whose re-registration failed may still recover its old
  runtime independently, but services and clients remain gated;
- foreign or unreadable ownership never moves retired runtime into the active
  name-scoped path, leaving it quarantined for safe diagnosis or recovery;
- the existing primary-first error aggregation reports the registration
  conflict without masking the original late failure;
- the new path regression inserts a replacement workspace during the router
  failure, proves the replacement registry entry remains exact, proves the old
  runtime and authority stay in the retired path, and confirms service/router
  compensation is skipped;
- the exact-head host suite passes 62 tests and 409 assertions in the Nix
  development environment.

The workspace pin commit was regenerated. The superseded configuration pin
commit was removed, then `confctl inputs channel set --commit` generated the
single final exact replacement and all hooks passed. All prior transaction,
rollback, path/token ownership, all-client restoration, compatibility and
deployment behavior remains unchanged.

Default-branch integration, release, archive, delete and session stop remain
out of scope.

## Review request

Risk remains high. Rerun General, Architecture/repetition,
Scope/proportionality and Risk/compatibility with `gpt-5.6-sol` at `xhigh`.
Focus on registration-state completeness, name/runtime ownership isolation,
safe independent recovery, primary-first diagnostics, regression realism,
minimality, commit ownership and exact downstream pins. Report Blocking,
Important or Advisory findings with evidence and remediation; explicitly
report clean lanes.
