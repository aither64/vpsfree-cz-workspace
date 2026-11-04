# TypeScript corrected history review packet

Final content is unchanged; complete corrected history needs independent review.
Lead has assigned reviewer0 under the general history gate. Do not repeat the
product-content review or local build solely because commits were split.
Earlier original review/history acceptance remains preserved in
[typescript-review-result.md](typescript-review-result.md); its single-commit
coupling rationale was challenged by the user and rejected by lead/owner.

## Requested result and complete series

Repository `vpsfreecz/vpsadmin-typescript-client`, target `main`, feature
`2026-11-03-vpsadmin-client-sync`, own worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-typescript-client`.

Base: `d354491537f8b654b4d2c33a705cad84474f95d6`.
Old head: `a4fc2449a1b5255b93b0c669ea9c454fac990536`.
Final new head: `2256ea46a8d8d135f352a524fbf048869d6eddf4`.

1. `d73eb93b27125932b5eaa09b3462ade12fa84765` — Refresh generated advisory
   operations from the current API schema. One consolidated snapshot/input/
   provenance/generated update and saved inventory docs (17 files).
2. `96c884b884fd8267f3f9b5b5d9ce26ccbfb8741e` — Cover guarded advisory
   mutations through the published runtime. Handwritten runtime/strict types
   consumer assertions and expected schema hash (2 files).
3. `2256ea46a8d8d135f352a524fbf048869d6eddf4` — Prepare version 0.4.0 for the
   added advisory operations. Package/lock version, changelog/README (4 files).

The generated commit records the existing wrapper's final release lockfile hash;
the separate release metadata commit supplies that lockfile version. This is the
minimal identity coupling, not a reason to bundle other changes. No intermediate
pin/schema/generated updates or duplicate generation were introduced. Consumer
coverage depends on generated methods, so follows the source refresh; release
metadata is last. Reviewer independently judges the actual complete series.

Final diff from base remains 23 files, 987 insertions/40 deletions. Both old/new
heads have tree `c85e30b1fc1ae27bba9c08884e11fa78bbb15f7b`, and exact final diff
between them is empty. Full ranges, range-diff, ref proof and immutable old
archive proof: [typescript-history.md](typescript-history.md),
[typescript-history-proof.json](typescript-history-proof.json),
[typescript-history-range-diff.txt](typescript-history-range-diff.txt).
No migrations, obsolete branch content, transitional compatibility paths or
repeated generated/input update streams. Historical plugin migration versions
remain provenance only. No new head is merged, tagged, deployed or published.

## Preserved content contract and evidence

The user requested all three client refresh/releases before Phase 2 rules;
TypeScript defaults to next minor, hence 0.4.0. No Phase 2 subsystem, WebUI WIP,
API/HaveAPI source edit, deployment or publication in this package.

Full schema comparison is exactly two new actions (advisory Retract/Delete) and
seven optional non-null `expected_state` fields; no existing values/types/routes/
defaults changed or removed. Raw full-fixture inputs, six-plugin coverage,
source/exporter graph, generator and runtime are unchanged by history rewriting.
API source `942c6eaed41331f823d8e0f670ed239e2b308440`; HaveAPI generator
`1ef9b204ba45bb261d3334be5c555cc1856b713b`; runtime0.32.0. Schema SHA256
`d6ec617653913c56e92398a6032aa350118597a0e3f45c599bc92b6071ea0a26`, provenance
`c85815abd315f53a5ef05f324abe377760293786a13a25b7a127ec804c50e0c1`.
151 resources/521 application actions, separate authentication1/5. Generated
runtime unchanged; 677 owned hashes/set checked on old exact final content.

Original all-four-lane product review and focused fixture remediation remain in
[typescript-review-result.md](typescript-review-result.md). Fixture fix preserved
all nine request assertions and was verified on original tested head. Lead
approved all prose. No product change now requires a fresh content review.

Old successful local checks and CI41665146322 bind old head a4fc244. Keep original
logs/receipt immutable; do not claim they executed on new head or that tree
equality proves Nix verification. No local suite/setup/build repeated. New-head
native CI41667969378 must independently pass its existing full matrix and retain
new archive/receipt; lead queues its observation after Rust utility completion.
Tag publication later requires its own exact tagged native archive/receipt, not
relabeling the old local tarball.

Corrected feature comparison captured at exact base/new head. Fresh remote main
and clean detached integration target remain at base; remote feature is new head.
No claim or default mutation. Scope and overall content compatibility remain as
original review: new methods require deployed API support/permissions, and
publication alone does not prove availability. Roll back matching inputs/pins/
generated source together; preserve published versions.
