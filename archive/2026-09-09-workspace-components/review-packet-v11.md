# Mandatory change review packet: compatibility allowlist closure

## Scope and exact ranges

The planned component split, persistence/authentication contracts, deployment
ordering and exclusions are unchanged from packet v10. Review these exact
immutable feature ranges:

- `codex-web`: `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8..e8655b7b2689da9b1aabe10df69858c32725dd61`
  (`690ff7d`, `a1721f5`, `a44ec2b`, `994b636`, `e8655b7`).
- `dev-workspace`: `f39f8e62097b5e9da9de8a5eb678131b1e478e35..7763a020adcbfbecb4c42ffbb11d9aaf5412cd8a`
  (`a695d7e`, `f36bd84`, `fa5f7d4`, `6c782a9`, `c56706a`,
  `0bef1a4`, `99dcbd9`, `bad9956`, `9872861`, `7763a02`).
- `vpsfree-cz-workspace`: `91b85b48b35cef51fd8920cd3445ca23a0023648..4b4cf06746beb20e44ee396c5732a5d15caed82f`
  (`5ee43e9`, `4b4cf06`).
- `vpsfree-cz-configuration`: `7481618dacab04bfd5b09bc730c373c2d2bf14d7..c6d3fb1b0bf8bcbe2215725bc163486cf4d798d8`
  (`99a845f`, `c6d3fb1`).

All worktrees are clean and equal their remote feature refs. Exact dependency
direction and pins are:

`vpsfree-cz-workspace@4b4cf06 -> dev-workspace@7763a02 -> codex-web@e8655b7`

Configuration `c6d3fb1` pins `dev-workspace@7763a02` and nested
`codex-web@e8655b7` with matching NAR hashes.

## Delta since v10 review

The v10 General, Architecture and Risk lanes were clean. Scope had one
Advisory: per-session `models` and `collaboration-modes` legacy aliases served
only an intermediate design. The final browser uses global `/api/models` and
`/api/collaboration-modes`.

Remediation is folded into the behavior-preserving dependency commit
`dev-workspace@fa5f7d4`:

- retain the original global collaboration-mode lookup throughout the series;
- remove both unused per-session GET aliases and their test rows;
- retain only the legacy conversation operations with real old-tab consumers;
- keep final mode-catalog rendering in `7763a02`, which no longer repairs the
  lookup location.

The exact dependency commit and final dev-workspace tree both pass every portal
package with `-count=1 -mod=mod -race` and Node available. This proves the
served reusable module, global mode endpoint, method-disambiguated `start`
queue ID and bounded legacy adapter without Go test-cache reuse. `codex-web`
still passes every uncached race-enabled Go package, the shared Node path corpus
and its no-build flake check. All four final flakes evaluate; configuration pins
were again produced only through `confctl`, whose hooks passed.

All other v10 contracts remain:

- one provider-owned Go/Node path fixture;
- exact RawPath spelling before resolution;
- shared Unicode/byte/whitespace queue-ID validation;
- DELETE versus POST dispatch for opaque queue ID `start`;
- quoted decoded paths in logs;
- unchanged schema-3 ledger, permissions, locks and paths;
- unchanged host credential, CA, TLS, profile and rollback paths;
- no default-branch integration, release, archive, delete or session stop.

## Review request

Risk remains high. Rerun General, Architecture/repetition, Scope/proportionality
and Risk/compatibility with `gpt-5.6-sol` at `xhigh`, focused on this final
allowlist/history remediation plus retained-boundary and exact-pin regressions.
Report Blocking, Important or Advisory findings with evidence and remediation;
explicitly report clean lanes.
