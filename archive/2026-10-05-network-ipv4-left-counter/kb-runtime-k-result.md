# Portable KB source checkpoint

The runtime branch is committed and published at
`93a16d6cecb6bc847ec9335a3f170eb8b301ab56`. It contains the inherited exact-V
pin `a50f8c1a` and one coupled launcher/capture commit above the retained default
`873758fd`. The original network KB branch is unchanged.

Root inspected the 54 owned paths, mandatory hook context and staged byte
hashes. The normal commit preserved the checked tree; its worktree is clean.
Fresh SSH default ancestry and the remote feature head were verified. No PR,
default integration, installed activation or cluster operation occurred.

## Local evidence

The owning-shell quick checks pass. The canonical `nix develop --command
bin/check` also passed on the clean committed tree in about 52 seconds:

- Runtime: 20 tests, 112 assertions; closure transport: 12/51; pinned OSVM
  driver: 4/20; allowlisted artifact export: 4/18.
- Connection: 12 Node cases; artifact roots: four Node cases; retained contract
  suites and source/browser helpers pass.
- All 11 standalone profile cases and syntax for all four rendered standalone
  scenarios pass. The two profile fixture failures remain in quick6/quick7;
  quick8 resolves evaluator materialization/context without relaxing validation.
- Strict inventory validates 60 concepts, 120 variants and 120 existing PNGs.

Complete canonical output is [kb-runtime-k-canonical.log](kb-runtime-k-canonical.log),
with exit 0 in its matching receipt. Source scope and hashes are retained in
the `kb-runtime-k-final2-source` packet; full branch diff/history and publication
proof are retained under `kb-runtime-k-source` and `kb-runtime-k-publication`.

The exact published `runtime-source` metadata derivation built in about five
seconds, selecting no VM, runner or capture-package target. Root verified its
revision, lock digest, V `5d5527a6` and OS `6bdf458f` pins and all 53 extant
checked files. E's selected-source tests can consume that immutable receipt;
the output path is in `kb-runtime-k-metadata.path`.

## Remaining work

Complete E's input composition and committed-source inventory, then independent
review of K/E/D before long package/VM verification. D's upstream-based final
feature head is now published with its new-base quick checks passing.
The real standalone selectors,
root/data/credential continuity, traffic isolation and CS/EN captures have not
run. Required KVM, capacity, disk and cached-kernel prerequisites still apply.
Existing PNG validation does not prove the two pending refreshed images.
