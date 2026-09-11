# Mandatory change review packet: authoritative recovery-write state

## Scope and exact ranges

Review these exact immutable feature ranges after the v17 remediation:

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`); unchanged.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..b3040c5011e181df2892c802508f7b01766bd1b1`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `21831fd`,
  `f8b2b0c`, `9ff2b54`, `c804c83`, `32cb196`, `d5e0f62`,
  `b3040c5`).
- `vpsfree-cz-workspace`: `ecbfb9a8a0d5fda49da1a2171e5c93449f8937cb..9ddf62f1fec3de8fb94cebdee199085bddd5d53b`
  (`a573dff`, `59b9948`, `9ddf62f`). It remains based on current shared
  `master`.
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..5f0415b25ec24586094ae3813499b9df57769726`
  (`986a93d7`, `710a2fba`, `5f0415b2`).

All worktrees are clean and equal their remote feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@9ddf62f -> dev-workspace@b3040c5 -> codex-web@e8655b7`

Configuration `5f0415b2` pins `dev-workspace@b3040c5` with NAR
`sha256-LRk4Ui9i5/U7dw9QHjxaVTLXVkM1vjst+RAeZ2QJIEQ=` and the unchanged nested
`codex-web@e8655b7` pin.

## Delta since v17 review

The completed v17 General, Architecture and Risk lanes identified two related
Important gaps. A genuinely absent registration still reclaimed its retired
runtime even though the public name had no owner, allowing a later replacement
to encounter the old authority. A recovery `Registry#register` exception was
also classified as absent without rereading even though its atomic replacement
could already be visible before a directory-fsync error.

The remediation is folded into host commit `b3040c5`:

- only `original` or fully returned `restored` registration states may move the
  retired runtime back into the active name-scoped path;
- `absent`, `foreign`, `unverified` and `unknown` states keep the old runtime
  quarantined, so a later registration cannot adopt its sockets or authority;
- after a failed recovery registration, a second fresh registry instance
  classifies the observed entry as absent, foreign or exact-but-unverified;
- an unreadable second observation remains unknown and retains both the write
  and verification errors in the recovery diagnostic;
- the true-absent regression proves runtime restoration is not called and the
  retired directory remains present, then registers a same-name replacement
  and proves the hidden old runtime is not adopted;
- a second regression makes the recovery registration replacement visible and
  then raises, proves the exact entry is observed, services and clients remain
  gated, and the old authority stays quarantined;
- the exact-head host suite passes 63 tests and 423 assertions in the Nix
  development environment.

The workspace pin was amended. The superseded generated configuration pin was
removed before `confctl inputs channel set --commit` produced the single final
exact pin, and all hooks passed. All prior transaction, rollback, path/token
ownership, all-client restoration, compatibility and deployment behavior
remains unchanged.

Default-branch integration, release, archive, delete and session stop remain
out of scope.

## Review request

Risk remains high. Rerun General, Architecture/repetition,
Scope/proportionality and Risk/compatibility with `gpt-5.6-sol` at `xhigh`.
Focus on the recovery-write reread, durability classification, quarantined
runtime ownership, dependent gates, primary-first diagnostics, regression
realism, minimality, commit ownership and exact downstream pins. Report
Blocking, Important or Advisory findings with evidence and remediation;
explicitly report clean lanes.
