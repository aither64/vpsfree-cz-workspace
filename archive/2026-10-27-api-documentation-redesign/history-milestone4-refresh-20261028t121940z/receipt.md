# Milestone 4 history refresh receipt

The five-group reconstruction is complete on the existing baseline. A/B retain
their exact commits. C includes all final milestone 4 UI and compact search
changes; D restores only the existing optional authentication presentation;
E retains the separate performance/cache change. No application repair occurred.

- Baseline: `2f5156262baaf137800c17a9321e617c2b5df1d5`.
- Previous final head: `09ef7905430e67042a6f047a0eb78c587189ff75`.
- Reconstructed feature head: `4f80b23c2ad02f0d227a000ced1b99d6d42a57f3`.
- Both final trees: `0f551c74ceb590cdff9b19980fc480ceb9d314e5`.
- The full previous-final-to-reconstructed diff is empty.
- Aggregate binary diff SHA-256 from the same baseline is identical:
  `ea0f7ef5d5f57278ff21a439156e7684c869a55b7171fd67da503e59e0d1d5f6`.
- Equality and clean original/scratch indexes were proven before the atomic,
  expected-old-SHA feature ref move. See `proof.pre-move.json`.

## Upstream reconciliation remains pending

A fresh SSH fetch from `git@github.com:vpsfreecz/haveapi.git` found master at
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`, rather than the baseline above. Its three commits
isolate maintenance-lineage test versions, synchronize components to 0.31.0,
and enforce the master-version release policy. The delta changes 24 paths,
including VERSION, generator/server gem dependency constraints, component
versions, JavaScript package/runtime version and Python package metadata.

This material source/input delta was reported before intervention. Per the
lead's instruction, no rebase or local lock/bundle graph mutation was attempted.
Architect0 owns the bounded reconciliation brief. The current five-commit head
is therefore the exact same-baseline result, not the final refreshed review
range. See `upstream-series.txt`, `upstream-paths.txt` and `upstream-delta.patch`.

## Final same-baseline series

- A: `b6a60aa7461af957bdb16e5b44dbb5a2a723df15` servers/ruby: add simple and detailed client examples
- B: `2053a5b2aefc7d2b52089e7a7a4ca49425b4ef8f` clients: simplify generated SDK documentation examples
- C: `8899488fb13c48be4bc6c6079d391f3eee6a0f0a` servers/ruby: redesign HTML documentation navigation
- D: `4922415fee56101818d200c76b5536e4f6209dd9` servers/ruby: add optional OAuth documentation sessions
- E: `4f80b23c2ad02f0d227a000ced1b99d6d42a57f3` servers/ruby: preserve documentation performance contracts

## Hooks, isolation and retained evidence

New C/D/E commits ran ordinary HaveapiI18n and RuboCop pre-commit hooks and
SingleLineSubject, TrailingPeriod and TextWidth commit-message hooks in the
repository's prescribed Nix shell. All passed. C's verbatim main-approved
message produced only the existing advisory for lines longer than 72 columns;
no line exceeds 80 columns. D/E passed without warnings. A/B were preserved
and their earlier actual hook results remain in the preceding receipt.

C uses the exact main-authored `final-ui-milestone4-commit.message`; D/E use
the unchanged accepted messages. Exact committed messages, hashes and group
path/source mapping are retained here and in `provenance.json`.

Owner0's four-partial Basic/final projections were verified against their
hash manifests and current source bytes. The restoration patch SHA-256 is
`c65ea2c5c0f4c4e5c734de9c184a67e1d043faeb2c05fc6b7235d0c145708568`.
It applied with fuzz 0 and no offsets, and all four results equal final source.
The original OAuth require/config/helper/mount seams and performance cache
were isolated by unique literal original-owner changes. Ambiguity checks
completed before scratch writes. The OAuth module, auth-chain source, both
OAuth specs and OAuth guide remain byte-identical to the previously accepted
D group. No authentication flow or TLS activation occurred.

The backup ref
`refs/heads/2026-10-27-api-documentation-redesign-pre-milestone4-20261028t121940z`
retains the previous final head. The scratch ref
`refs/heads/2026-10-27-api-documentation-redesign-m4-history-20261028t121940z`
and its same-session worktree retain the reconstructed series. Both the feature
and scratch working trees and indexes are clean; see `final-state.json`.

All earlier backup/scratch refs, receipts and prepared inputs remain. Original
base `2fc2b8f86c71a6062434bb60a24e174b20c1a520`, initial old final
`e60bbd01f3653141c3bfa87ccc209aa569324c7b`, and the prior reviewed range ending
`82a7f2abcc1ecfc361097d30de39e93aca026d64` retain their existing provenance.
See `../history-consolidation-20261028t100455z/` and
`../history-final-refresh-20261028t105801z/`. Earlier HTTP preview SHAs and
runtime digests remain historical review snapshots; no rewritten nonancestor
SHA is claimed literally integrated. Local preview serving was review only.

The prior generated-input declaration, lock, adapter/runtime and independent
MSRV binary hashes were reobserved unchanged; see
`prepared-inputs-preserved.json`. Root/server/component, frozen benchmark,
live preview, local JavaScript and separate published-runtime graphs remain
separate. This receipt does not certify those graphs against the new 0.31.0
upstream source.

## History inventory and next action

The complete same-baseline feature diff has 109 paths, no database migrations,
no schema/seed lineage, and no dependency or channel update streams. There
are no feature migrations to classify as merged, released, deployed or
externally consumed. The original and user-added UI iterations are folded
into final C; the Go full-program fixture remains in B; optional auth and
performance remain separate. The compact-search JSON is a test fixture.

This package made no push, default-branch integration, release, production
deployment, dependency update, lifecycle action or deletion. All owned commit
and fetch commands have returned; no owned watcher or check process remains.
No application quick check was repeated for history identity alone, and no
long gate started. Earlier owner check evidence retains its original scope.

Next: architect-owned material upstream/input reconciliation, then the
lead-granted execution, packaging and final independent review. Independent
review must cover the final refreshed range, whole-branch history, migration
conclusion and supported optional-auth hold before long acceptance gates.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
