# U5: CI diagnostic visibility; input change rejected by user

Current scope supersedes the original candidate below. User directed waiting for
the upstream workflow's exact cached kernel outputs, then rerunning the status
test, rather than changing the input graph. Only integration workflow diagnostics
and a five-line tests README note remain (two files, ten additions / four
deletions). `flake.nix` and `flake.lock` were restored byte-for-byte to accepted
head c112594. The complete original graph and exact C5/C6 cache targets remain.

No U5 evaluation command ran. Watcher e477f386 stopped before launch after using
the wrong receipt digest framing; source/script hashes were independently
rechecked with zero differences. Frozen C7 snapshot and script are retained only
as rejected, unexecuted proposal evidence, and must not be used for the full run.
No replacement watcher or build was launched. The original gate/graph discussion
below is historical context, not final deliverable scope.

Narrowed checks: workflow YAML parse and diff check passed; modern root Go1.26.10
and i18n health passed. Final source/hash receipt: `u5-diagnostics-inputs.json`.
Lead directly approved the actual narrowed README prose unchanged. Final
diagnostic commit `c4e11ec3f933de75f782b95bb3034ca31e3034d5`, parent
`c1125948c53c0a36dbf695459221844702408365`; two files only, ten additions / four
deletions. Required Nix/Lefthook 2.1.5 i18n check passed (0.40s; total 0.42s),
gofmt correctly skipped without Go files. All four narrow receipt hashes match
after hooks; both flake files exactly match the U6 base. No bypass or unexpected
hook effects; worktree/index clean and exclusive window released. UI/preview
commits remain unchanged, with one separate logical diagnostics commit; no
obsolete input-change commit or migrations exist. No source push by U5.

Full test rerun remains blocked on exact upstream output/cache evidence and
independent final review. Lead reports the latest upstream kernel workflow has
passed but its newer OS kernel config differs, so completion alone does not
establish substitutes for the original four kernel paths. Any new dependency
refresh needs its own sufficient brief; it is outside this completed package.

## Withdrawn C7 proposal (historical only)

Before the user's decision, a generated candidate separated root app nixpkgs
ac588 from the original OS's ee48 package composition. It was never committed
or evaluated. Both flake files were restored completely, and that candidate's
isolated snapshot/script remain historical artifacts only. U5's actual source
scope is solely the two-file diagnostics correction recorded above. The later
ordinary upstream dependency refresh is separately owned and documented in
[u7-os-refresh-evidence.md](u7-os-refresh-evidence.md).

## Committed diagnostics rationale

CI adds `--verbose`, stderr capture under pipefail, and best-effort test.log/
per-test log upload on failure or cancellation. Official upstream release checks
found checkout v7.0.1; it uses Node24 like v6 and retains minimum runner 2.327.1.
The existing run log proves runner 2.338.0, so checkout ref updates to v7.0.1.
Existing vpsAdminOS action refs `staging` verified at
`650170d699e3033c5279b911a2ef0a355439613c`; unchanged in this patch.

## Final checks and history

Workflow YAML parsing, diff checks, Go1.26.10 and i18n health passed. Required
hooks passed during commit c4e11ec as recorded above. The discarded C7 watch
stopped before any source command because of a receipt-framing disagreement;
per-file identities were subsequently reverified with zero mismatches. No U5
kernel config, build, store copy, VM or full test run occurred.

The final branch retains preview and UI commits plus one separate logical
U5 diagnostics commit. No input-graph change, migration or data conversion is
part of U5. Reverting U5 removes only diagnostic visibility improvements and
the compatible checkout refresh; it does not change cache identities. U7 owns
any subsequent ordinary upstream lock update. No default-branch integration,
source push, services or session lifecycle actions by U5.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-status-theme-responsive-preview/)
