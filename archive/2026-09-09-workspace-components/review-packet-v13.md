# Mandatory change review packet: all-client rollback recovery

## Scope and exact ranges

Review these exact immutable feature ranges after remediating the v12 findings:

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`); unchanged.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..a9f9c8e050e4ed9bf533b15744851ffd914dbfc8`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `44fdc05`, `54d5eca`,
  `1feaf16`, `e930d39`, `06a5b8b`, `feeb920`, `a9f9c8e`).
- `vpsfree-cz-workspace`: `91b85b48b35cef51fd8920cd3445ca23a0023648..94ed0fb34b517dc841ec5be8f07a1eeed93267e8`
  (`7176f8a`, `94ed0fb`).
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..6e2f48fef35033f36b970676923dbb34505346d5`
  (`7d924667`, `6e2f48fe`).

All worktrees are clean and equal their remote feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@94ed0fb -> dev-workspace@a9f9c8e -> codex-web@e8655b7`

Configuration `6e2f48fe` pins `dev-workspace@a9f9c8e` with NAR
`sha256-LWBCMZspUCbA5gD4u6uuXJUs/y8iI98EiIsW8P588zg=` and the unchanged nested
`codex-web@e8655b7` pin.

## Delta since v12 review

Architecture and Risk each reported the same Important issue: restoration was
still fail-fast, so one broken session could prevent later quiesced clients
from being attempted and could mask the primary transition error. General
reported the corresponding unrealistic test gap and an Advisory that the
deployment example did not clearly distinguish migration from bootstrap.

The remediation is folded into the owning host and documentation commits:

- terminal restoration attempts every `[workspace, slug]`, captures only a
  single-line diagnostic for each failure, and raises one aggregate error after
  all attempts;
- failed-transition recovery independently attempts profile compensation and
  every terminal restoration, preserves the original transition error first,
  and appends compensation and aggregate restoration errors;
- successful rollback keeps the healthy selected generation active if only
  client restoration fails and tells the operator to retry `dev-session sync`;
- successful rollback explicitly restores through the selected target profile,
  while compensation explicitly restores through the outgoing/original package
  after reselecting it;
- a two-session test injects failure into the first sync, proves the second is
  attempted, and verifies the target `dev-session` helper,
  `--expected-host-generation`, profile identity token, portal command and both
  cluster commands all come from one target generation;
- separate regressions verify successful rollback is not reversed by a client
  sync failure and that a failed transition reports both the primary and
  restoration errors while using the original generation for recovery;
- the deployment guide now explicitly describes aitherdev as an
  existing-profile migration, points fresh installations to the README's
  `nix run` bootstrap, and reserves stable `workspace-host register` for adding
  a workspace after installation.

The focused exact-head host suite passes with 57 tests and 366 assertions.
The final dev-workspace, workspace and configuration flakes pass no-build
evaluation. Downstream pins were regenerated and republished; configuration
was changed only through `confctl`, whose hooks passed.

All other v12 and v11 contracts remain unchanged. Default-branch integration,
release, archive, delete and session stop remain out of scope.

## Review request

Risk remains high. Rerun General, Architecture/repetition and
Risk/compatibility against the remediated all-client boundary, and run the
still-pending Scope/proportionality lane, with `gpt-5.6-sol` at `xhigh`.
Focus on error preservation, best-effort restoration, generation/path
consistency, test realism, documentation clarity, commit cohesion and exact
pins. Report Blocking, Important or Advisory findings with evidence and
remediation; explicitly report clean lanes.
