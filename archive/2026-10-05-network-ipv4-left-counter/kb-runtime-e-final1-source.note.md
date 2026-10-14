Proposal only; no source/Git mutation, commit wrapper or test launch.

The final candidate has exactly 23 extant regular source paths: the 22 frozen
functional/docs paths plus the canonical generated flake.lock. The .diff records
tracked changes, .new-files.diff records all extant untracked files, and .full.diff
combines them without staging. All content hashes, modes, sizes, full status,
empty actual index and exact original HEAD/branch are retained.

Proposed normal commit order:
1. Input selection: only the two selected URL declarations in flake.nix and
   canonical flake.lock, partially staged by the root from exact original base.
   This commit does not include the new provider body or missing draft files.
2. Optional provider: the remaining 22 source/docs paths, including the flake
   body, new public/SDK tests and approved owning prose.

The root owns partial-flake staging, normal commits, exact-tree proof, publication
and final package-derivation evaluation. No helper executes those operations.
The inputs and provider messages are separate files and contain no check logs.
No hook framework is declared; ordinary Git hooks must remain enabled.

Root-interpreted local evidence: six integrated suites 34 tests/215 assertions;
public composition 5/58; total 39/273 with no failures/errors/skips. These are
synthetic CLI/process boundaries plus exact selected read validators. Canonical
input generation/checks passed, retaining all five unrelated root input graphs
and matching D17/K45 semantic paths, including D's selected own dependencies.
Source freezes match those accepted receipts. No passing suites repeat.

Enabled/default package derivation evaluation is still pending on the clean
committed candidate. It proves configuration/derivation contracts, not package
execution. Package build/install checks, real guest lease/capture, standalone
resume/update and activation are separate post-review evidence. No additional
local source gap was identified; the synthetic private lease deliberately does
not exercise guest attestation. K93/D51 sources remain held and unchanged.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/
