# Mandatory change review packet: primary-first recovery closure

## Scope and exact ranges

Review these exact immutable feature ranges after the v13 General remediation:

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`); unchanged.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..8482e01fce2d1e6160da72124f9a445bc0554ffd`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `2a90e71`, `f5b0267`,
  `654d7f3`, `fde32c8`, `23a879f`, `7dfee33`, `8482e01`).
- `vpsfree-cz-workspace`: `91b85b48b35cef51fd8920cd3445ca23a0023648..ad20f1cfab8be817c800d2ad2a2b09b6075fad5f`
  (`d307982`, `ad20f1c`).
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..b5bbe1e73712127f4af9e59b910573840299413e`
  (`3420206f`, `b5bbe1e7`).

All worktrees are clean and equal their remote feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@ad20f1c -> dev-workspace@8482e01 -> codex-web@e8655b7`

Configuration `b5bbe1e7` pins `dev-workspace@8482e01` with NAR
`sha256-b/BUUlAk4r44yuqTwh1JfMfcru62Oj8l+ROgq6q3OSE=` and the unchanged nested
`codex-web@e8655b7` pin.

## Delta since v13 review

The v13 Architecture and Risk lanes were clean. General found one Important
issue on the expanded restoration helper boundary: unregister, suspend and
partial quiesce attempted terminal restoration before a bare re-raise, so an
aggregate restoration failure could replace their primary error.

The remediation is folded into host commit `2a90e71`:

- one `reraise_after_terminal_restoration` helper attempts the full restoration
  batch, re-raises the original exception unchanged when restoration succeeds,
  and otherwise reports the primary message first followed by the aggregate
  per-session restoration message;
- unregister, suspend and partial-quiesce rescue paths use that boundary;
- rollback's compensation and successful-target handling retain their more
  detailed generation-specific behavior from v13;
- a focused regression injects both a primary failure and a sync failure and
  asserts the exact primary-first combined diagnostic;
- the exact-head host suite now passes 58 tests and 368 assertions.

The final dev-workspace, workspace and configuration flakes pass no-build
evaluation. Downstream pins were regenerated and republished; configuration
was changed only through `confctl`, whose hooks passed. The v13 two-session
generation/path/token tests and clarified bootstrap documentation remain.

All other v13, v12 and v11 contracts remain unchanged. Default-branch
integration, release, archive, delete and session stop remain out of scope.

## Review request

Risk remains high. Rerun General, Architecture/repetition and
Risk/compatibility against the primary-first rescue propagation, and run the
pending Scope/proportionality lane, with `gpt-5.6-sol` at `xhigh`. Focus on
primary-error preservation, all-client recovery, generation ownership, test
coverage, scope, commit cohesion and exact pins. Report Blocking, Important or
Advisory findings with evidence and remediation; explicitly report clean lanes.
