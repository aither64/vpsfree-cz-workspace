# Mandatory change review packet: unregister transaction boundary

## Scope and exact ranges

Review these exact immutable feature ranges after the v15 remediation:

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`); unchanged.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..0f9d96b0d74ec939e3f279769ee9bb9d0e75423a`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `21831fd`,
  `f8b2b0c`, `9ff2b54`, `c804c83`, `32cb196`, `d5e0f62`,
  `0f9d96b`).
- `vpsfree-cz-workspace`: `ecbfb9a8a0d5fda49da1a2171e5c93449f8937cb..ad19e8a7543550d2a4355accbe93bffbafdab708`
  (`a573dff`, `59b9948`, `ad19e8a`). It is rebased onto current shared
  `master`; its feature trees are unchanged.
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..a804fda7161ec0367b52e62876a3cf4c16c1247d`
  (`986a93d7`, `710a2fba`, `a804fda7`).

All worktrees are clean and equal their remote feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@ad19e8a -> dev-workspace@0f9d96b -> codex-web@e8655b7`

Configuration `a804fda7` pins `dev-workspace@0f9d96b` with NAR
`sha256-rFEYhvJIVvAbNGJW677/SIlzNfHAgXS1v2wXQaUOyH8=` and the unchanged nested
`codex-web@e8655b7` pin.

## Delta since v15 review

The v15 Risk lane found an Important transaction-boundary gap: the registry
replacement could persist before `Registry#unregister` returned, so a local
success flag was not authoritative. The method-wide rescue also included
retired-runtime deletion and success output, allowing a post-commit output
failure to begin invalid compensation. General identified the related recovery
ordering issue: unit, router and terminal recovery could proceed after registry
or runtime restoration failed.

The new focused commit `0f9d96b` closes both findings:

- compensation reopens the registry from disk and compares the exact original
  entry instead of consulting a cached object or success flag;
- absent registrations are restored without replacing a concurrent different
  entry, and router recovery runs only after an actual restoration;
- registry and runtime recovery remain independent, while unit enablement and
  client restoration require both invariants to be ready;
- the primary exception remains first, followed by labeled recovery failures
  in execution order;
- the reversible transaction ends before retired-runtime disposal and success
  output, so cleanup warnings or `EPIPE` cannot resurrect an unregistered
  workspace;
- regressions model an on-disk replacement with stale cached registry entries,
  a late router primary followed by failed registry and runtime recovery, and a
  broken stdout after the committed state;
- the exact-head host suite passes 61 tests and 400 assertions in the Nix
  development environment.

The workspace and configuration exact pins were regenerated and pushed.
Configuration was changed only through `confctl`, whose hooks passed. All v15
generation, path/token ownership, all-client restoration, compatibility and
deployment behavior remains unchanged.

Default-branch integration, release, archive, delete and session stop remain
out of scope.

## Review request

Risk remains high. Rerun General, Architecture/repetition,
Scope/proportionality and Risk/compatibility with `gpt-5.6-sol` at `xhigh`.
Focus on the authoritative commit boundary, dependency-gated recovery,
primary-first diagnostics, stale-cache and output regressions, minimality,
commit ownership and exact downstream pins. Report Blocking, Important or
Advisory findings with evidence and remediation; explicitly report clean
lanes.
