# Mandatory change review packet: unregister recovery closure

## Scope and exact ranges

Review these exact immutable feature ranges after the v14 Risk remediation:

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`); unchanged.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..d5e0f624ee065a9dc865bfe2a3fe40cd902afe3c`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `21831fd`,
  `f8b2b0c`, `9ff2b54`, `c804c83`, `32cb196`, `d5e0f62`).
- `vpsfree-cz-workspace`: `91b85b48b35cef51fd8920cd3445ca23a0023648..2a31b6431ddf151ae0bcbc27a0b6bf360cb72557`
  (`db04fbf`, `2a31b64`).
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..710a2fba05745bd980c0cd815b7fbdccceb076be`
  (`986a93d7`, `710a2fba`).

All worktrees are clean and equal their remote feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@2a31b64 -> dev-workspace@d5e0f62 -> codex-web@e8655b7`

Configuration `710a2fba` pins `dev-workspace@d5e0f62` with NAR
`sha256-AQhetTnAZMJK+4cEgDTOZtFh2QuPRmbH52Cv5eI7Gfs=` and the unchanged nested
`codex-web@e8655b7` pin.

## Delta since v14 review

The v14 General, Architecture and Scope lanes were clean. Risk found one
Important gap in unregister compensation: recovery stages before terminal
restoration were still sequential and unprotected, so an early recovery failure
could replace the primary unregister error and prevent later safe recovery.

The remediation is folded into host commit `de0441b`:

- unregister captures recovery failures independently for registry
  re-registration, runtime restoration, unit re-enable, router restart and the
  full terminal-restoration batch;
- each eligible stage is attempted even when an earlier recovery stage fails;
- the original unregister error remains first, followed by labeled single-line
  recovery diagnostics in execution order;
- when every recovery stage succeeds, the original exception object is
  re-raised unchanged;
- the path-level unregister regression injects the primary partial-disable
  failure, an eligible unit re-enable failure and a terminal-restoration
  failure, proves both later stages were attempted, and checks primary-first
  diagnostic ordering;
- the exact-head host suite passes 58 tests and 375 assertions.

The final dev-workspace, workspace and configuration flakes pass no-build
evaluation. Downstream pins were regenerated and republished; configuration
was changed only through `confctl`, whose hooks passed. All v14 rollback,
all-client restoration, primary-first helper, generation/path/token, docs and
compatibility behavior remains.

Default-branch integration, release, archive, delete and session stop remain
out of scope.

## Review request

Risk remains high. Rerun General, Architecture/repetition,
Scope/proportionality and Risk/compatibility with `gpt-5.6-sol` at `xhigh`,
focused on stage-by-stage unregister recovery, safe eligibility, primary-first
diagnostics, regression realism, minimality, commit ownership and exact pins.
Report Blocking, Important or Advisory findings with evidence and remediation;
explicitly report clean lanes.
