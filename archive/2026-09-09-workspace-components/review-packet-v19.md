# Mandatory change review packet: substrate reconciliation idempotency

## Scope and exact ranges

Review these exact immutable feature ranges after post-deployment validation:

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`); unchanged.
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..a005e31409810ff5550616344c7f5e3b66c6c322`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `de0441b`, `21831fd`,
  `f8b2b0c`, `9ff2b54`, `c804c83`, `32cb196`, `d5e0f62`,
  `b3040c5`, `a005e31`).
- `vpsfree-cz-workspace`: `ecbfb9a8a0d5fda49da1a2171e5c93449f8937cb..88659556fadee30c1ab8025fcef23488206350db`
  (`a573dff`, `59b9948`, `8865955`). It remains based on current shared
  `master`.
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..2f59e38ec2cf7de9028df693784938a51f1d2ccb`
  (`986a93d7`, `710a2fba`, `2f59e38e`).

All worktrees are clean and equal their remote feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@8865955 -> dev-workspace@a005e31 -> codex-web@e8655b7`

Configuration `2f59e38e` pins `dev-workspace@a005e31` with NAR
`sha256-Cr1Io+M1kesHNCYhNNsi5NaWAQXeaUy86XpzGRFpjAs=` and the unchanged nested
`codex-web@e8655b7` pin.

## Delta since v18 review

Mandatory review v18 was clean in all four lanes. Full provider and wrapper
builds then passed. Exact aitherdev dry activation and live deployment passed
without a kernel build. User-profile generation 16 passed service, socket,
API, authenticated TLS, retained-thread and empty generic-workspace checks.
The corrected rollback to generation 15 restored all eight affected terminal
clients, and the second forward switch succeeded.

Final persistent-state comparison found an idempotency defect in the NixOS
substrate reconciliation:

- the persistent generated password and CA remained byte-identical;
- the old inline configuration and extracted module both regenerated the
  derived bcrypt entry with a new random salt on every activation, even when
  the password was unchanged;
- the module's exact SAN-set comparison used host-locale `sort`, while the Nix
  expected value used byte ordering. On aitherdev, the locale placed the
  wildcard after letters, so every activation renewed an already valid leaf;
- a direct second reconciliation reproduced another leaf generation. The
  original certificate/key pair remains in the persistent pairs directory.

Focused commit `a005e31` remediates both behaviors:

- an existing private, correctly owned, single-entry bcrypt file is verified
  against the configured user and persistent password with `htpasswd -vi`;
- the password is supplied on standard input and never exposed as an argument;
- only a missing, malformed, misowned or nonmatching bcrypt entry is replaced;
- observed certificate SANs are sorted with `LC_ALL=C`, matching Nix's expected
  byte order and preventing locale-dependent renewal;
- the generated example check requires both verification and C-locale sorting;
- the focused Nix host-module build and generated-script ShellCheck pass.

The previous derived bcrypt bytes were replaced during authorized activation
and cannot be reconstructed, but the password itself is exact and authenticated
TLS verifies the same credential. After review, deployment will restore the
retained exact original TLS pair, run reconciliation twice, and prove bcrypt,
CA and leaf hashes remain stable.

Default-branch integration, release, archive, delete and session stop remain
out of scope.

## Review request

Risk remains high. Rerun General, Architecture/repetition,
Scope/proportionality and Risk/compatibility with `gpt-5.6-sol` at `xhigh`.
Focus on password secrecy, bcrypt verification and file safety, locale-stable
SAN equality, renewal compatibility, restoring retained leaf state, test
adequacy, commit ownership and exact downstream pins. Report Blocking,
Important or Advisory findings with evidence and remediation; explicitly
report clean lanes.
