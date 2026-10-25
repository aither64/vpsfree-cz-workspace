# Follow-up verification handoff

All eight authorized phases passed at `090a188cb4ef3477324718627f4ae3415d1c0975`,
tree `e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2`. The reviewed six-commit series
and tracked source/index remain unchanged. No owned verification process remains.

The [final receipt](followups-verification-final-phases-090a188c-20261023T165049Z/final-verification-receipt.json)
and [combined phase results](followups-verification-final-phases-090a188c-20261023T165049Z/combined-phase-results.json)
record actual successful dependency setup, JSDoc generation, release build, full
tests, retained npm smoke, Python package smoke, generated Rust naming checks
under development and independent 1.95 toolchains, and artifact verification.
The [warning summary](followups-verification-final-phases-090a188c-20261023T165049Z/warning-summary.json)
found none of the named warning categories and no other warning/deprecation lines.

Phases 01–02 retain their original execution in
`followups-verification-090a188c-20261023T163216Z`; phases 03–04 retain theirs in
`followups-verification-resume-090a188c-20261023T163855Z`. The final directory
contains phases 05–08. The [reuse proof](followups-verification-final-phases-090a188c-20261023T165049Z/prior-phases-reuse-proof.json)
binds complete tracked inputs, eleven lock/input files, eight generated JS
outputs, tool identities and full development/MSRV derivation graphs. Earlier
executions are neither repeated nor relabelled.

The [artifact copy proof](followups-verification-final-phases-090a188c-20261023T165049Z/final-artifact-copy-proof.json)
confirms twelve retained development artifacts and their evidence copies have
equal hashes. Their manifest names this exact source. These unchanged-version
0.30.0 development artifacts never replace the official release bytes.
The 302 baseline cache paths, 69 generated documentation files and one exact
PHPUnit cache are separately inventoried and preserved.

Limits: the unchanged Rust runner removes temporary generated input trees, so
no saved generated-input graph is claimed. Independent Rust 1.95 executable
identities, derivation roots and full graph are retained; its historical
nixpkgs revision is unknown. Python package smoke installs temporary wheel and
standalone sdist builds rather than the exact retained wheel.

Independent review: [final review](followups-final-review.md), all four lanes,
no findings. Current authorization permits development-branch publication and
automatic build-only CI only. Default integration and another release remain
outside this package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
