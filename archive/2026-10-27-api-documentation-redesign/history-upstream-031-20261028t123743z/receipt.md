# Upstream 0.31 feature refresh

Replayed the approved five logical feature patches onto exact fresh SSH upstream
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`. Every per-commit full-index patch and message is byte-identical to its
previous counterpart; range-diff reports all five equal. All five recreated
commits passed ordinary mandatory hooks. No source conflict or repair occurred.

- Old range: `2f5156262baaf137800c17a9321e617c2b5df1d5..4f80b23c2ad02f0d227a000ced1b99d6d42a57f3`.
- New range: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0..a0c78d1c0e5ef84b5e746d9bba4bc51830c77139`.
- Old final tree: `0f551c74ceb590cdff9b19980fc480ceb9d314e5`.
- New final tree: `3c62ce89c1ac356116aef9c59cf34398bd3130bf`.
- Old/new aggregate feature patch SHA-256:
  `ea0f7ef5d5f57278ff21a439156e7684c869a55b7171fd67da503e59e0d1d5f6`.
- Old-final/new-final delta equals the exact upstream delta byte-for-byte:
  `426ab56641ee6c91a1cc596a5d46f318eeaff081b6a2d0bb6f64d8ec85c96cf3` (SHA-256).

The old and new final trees differ because upstream advanced. Independently
applying the upstream binary patch to the old final in a temporary index
produced the exact new final tree. See `independent-upstream-tree.json`,
`equivalence.before-move.json`, `range-diff.txt`, both feature patches and
`old-final-to-new-final.patch`.

## Final five commits

- A: `4363d1114f31cbb5d61411a95f6501bda17b50c0` servers/ruby: add simple and detailed client examples
- B: `260e3ea8a469c8840164bd8a0f5044238f5472e1` clients: simplify generated SDK documentation examples
- C: `54e5cc6ad1253f6bf23929ef9a61f2badb7c84bb` servers/ruby: redesign HTML documentation navigation
- D: `4a2e0164cff00d26c2980bdb4b880ced0db23d67` servers/ruby: add optional OAuth documentation sessions
- E: `a0c78d1c0e5ef84b5e746d9bba4bc51830c77139` servers/ruby: preserve documentation performance contracts

## Upstream and inputs

Fresh SSH master matched the exact approved baseline. The three upstream
commits isolate historical maintenance-version test fixtures, synchronize source
metadata to 0.31.0 and enforce the master-version release policy. Their 24 paths
have no overlap with the feature's 109 paths. Exact upstream history, paths and
patch are retained. No version bump, source metadata rollback, release command
or publication was performed.

The root Gemfile and Nix declarations are unchanged and the retained root tools
lock contains no HaveAPI package. Root availability passed with Ruby 3.4.11,
Bundler 4.0.23, JSON 2.21.2, Overcommit 0.73.0 and RuboCop 1.85.1. Root shell
installation was disabled using its declared tools-only mode, and Bundler was
frozen; no dependency resolution or installation was requested. Nix substituted
ordinary shell outputs using unchanged pins. No kernel build occurred.

The new scratch checkout initially refused the unsigned Overcommit configuration
after creating the worktree. The worktree remained at exact upstream with clean
source/index. Its configuration matched the accepted source exactly; ordinary
`overcommit --sign` resolved the signature gate using the verified root bundle.
No hook was bypassed. All five commits then ran HaveapiI18n, RuboCop and normal
commit-message hooks. Only C's approved verbatim message produced the retained
72-column advisories; every line is within 80 columns. See `commit-A.log`
through `commit-E.log`, `root-tools-availability.log` and
`scratch-hook-setup.log`. Exact accepted messages and hashes are retained.

Ignored server, Go-acceptance, Rust, JavaScript, Python and frozen-benchmark locks
were preserved byte-for-byte, with before copies and hashes. No component graph,
live preview bundle or compiled/installed artifact was refreshed. Root input
hashes remain identical. The source now follows upstream 0.31.0; old component
path locks/install metadata remain historical 0.30 preparation and must be
refreshed by owner1 before current-source checks. Separate published TypeScript
runtime 0.30.2 and independent Rust MSRV evidence retain their existing contract.
No application compilation, wire, runtime, packaging or performance result is
claimed by this history operation.

## Source move, ownership and recovery

Before moving the feature ref, both original and scratch worktrees/indexes were
clean, the feature still pointed to the expected old head, and all equivalence,
independent tree, message, input and held-OAuth assertions passed. The exact
upstream patch was applied to the original worktree/index, its resulting tree
was verified against the scratch final, and the feature ref moved atomically
with its expected old SHA. This touched only committed upstream paths; no
repository-wide reset, stash, clean, deletion or inferred repair was used.

Backup ref `refs/heads/2026-10-27-api-documentation-redesign-pre-upstream-031-20261028t123743z` retains the old final head.
Scratch ref `refs/heads/2026-10-27-api-documentation-redesign-upstream-031-20261028t123743z` and worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi-upstream-031-20261028t123743z` retain the new final series.

All prior refs, original ranges, reconstruction receipts and HTTP preview
snapshots remain intact. The preceding same-baseline exact-tree proof remains
at `../history-milestone4-refresh-20261028t121940z/`; original-base provenance
continues through the linked earlier receipts. Runtime snapshot SHAs remain
historical review evidence; no nonancestor is claimed literally merged.

The complete authentication-provider subtree, OAuth module, both OAuth specs
and OAuth guide objects are identical between old and new feature heads.
Owner0's exact four-partial Basic/final artifacts and zero-fuzz/no-offset
restoration remain retained in the preceding receipt. D behavior is unchanged;
R1, OAuth/TLS activation and cross-session work remain held.

## History inventory and handoff

The final feature range contains no migrations, schema/seed lineage or feature
dependency/channel update streams. There are no feature migrations to classify
as merged, released, deployed or externally consumed. Upstream's version
synchronization remains upstream provenance, not an added feature update
stream. The five groups preserve core examples, generated adapters, final UI,
optional authentication and performance separately. C includes all final
milestone4 presentation and compact-index changes; B includes its full-program
Go fixture. No obsolete UI iteration commit remains in this feature series.

Both original and scratch full worktrees/indexes are clean. All owned commands
returned; no owned watcher, check process or background work remains. No gates,
dependency refresh, preview changes, publication, default integration or
lifecycle action occurred. The Git slot is released to lead with the report.

Next: owner1 bounded input refresh, owner0 assigned quick/packaging checks,
then retained independent final review of this exact final range and material
input boundary before long acceptance gates. Source/input identity preserves
prior evidence at its actual scope; it does not turn earlier results into
checks of the new 0.31 source/input graph. Lead owns state/review coordination.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
