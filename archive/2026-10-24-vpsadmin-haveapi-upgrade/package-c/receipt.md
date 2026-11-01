# Package C implementation receipt

Owner: implementer1. Session identity and environment matched
`2026-10-24-vpsadmin-haveapi-upgrade` in `/home/aither/workspace/ai/vpsfree.cz`.
Repository: `git@github.com:vpsfreecz/vpsadmin-webui.git`; target: `main`.
Own branch: `dev/vpsadmin-haveapi-upgrade`; initial/fresh remote base:
`5a2d2bdc3ad7a827038f877d75959916528db844`.

## Source reconstruction

Carried final production content from `8772bab21cd8739bf4672cdf4976aea2a6e59de3`
relative to old base `7860521f30826c3886c89c35e8ab6f4e082e0a4b`, preserving
original author Jakub Skokan <jakub.skokan@havefun.cz>. Old published range:
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..5dd2333b9af230d4a81c8f772cbbb08d39b14913`.
Old local range:
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..8772bab21cd8739bf4672cdf4976aea2a6e59de3`.

The old series contains a pilot, pilot proof, vendor pin and production successor.
Only final production source/tests/current contracts were carried. The pilot,
private vendor tarball/override and obsolete archive checks were never added to
this branch. Historical pilot/production work logs stay in their original source
rather than representing their prior checks as new evidence. `source-paths.json`
and `carried-content.patch` capture the exact original final delta and initially
selected source paths. Reconciled the seven architect-identified overlaps:
current root work log and contracts retained; current node tests migrated to
controlled XHR; current E2E coverage union retained; resolved HaveAPI structural
exception removed without changing other entries. Current main's node overview,
member administration and other product changes remain.

## Dependency/provenance

Exact npm dependency `haveapi-client@0.30.1`, ordinary registry lock.
Lock diff adds only root dependency, HaveAPI and XMLHttpRequest 1.8.0 entries.
Node 24.21.0 / npm 11.19.0 from locked `nix develop`.
Tarball SHA512 verified against registry integrity and attestation subject;
53 packed files inventoried. Tarball SHA256:
`7760acdc16631c6eafe70586e76aa8508307bb16fc41a834fbb5e2bb0b150044`.
Registry SLSA statement binds tag `refs/tags/v0.30.1` to source
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`, release run `40114719358`.
The source package lacks gitHead. Registry metadata, attestations, decoded
statement and packed-file inventory are retained here. Cryptographic registry
signature verification is not claimed by the source checker.

## Verification to date

- npm lock update and clean `npm ci` passed under fresh Luna/low watcher.
- Installed package declarations typecheck passed.
- Focused adapter/session/public/node regressions: 5 files / 83 tests passed.
- All domain API tests: 45 files / 324 tests passed (watcher quick batch).
- Package-source checks: 6 tests passed, including substituted registry artifact,
  absent transitive integrity, Gitless source and private/symlink boundaries.
- Design inventory: 257 routes, 64 API modules. Design audit passed (134 docs,
  75 requirements); structural audit passed (33 accepted exceptions).
- E2E core type coverage: 72 adopted, 195 deferred; typecheck passed.
- Scoped lint passed. Format gate identified tsconfig.e2e.json expanded arrays;
  formatting corrected with repository Prettier. Remaining checks pending.

Pinned watcher catalog `840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`;
separate utility `gpt-6-luna`/low,
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`, explicit full access
and never approval from matching installed native config. Each operation gets a
fresh watcher. No long integration/build suite before independent final review.

## Boundaries

No schema/database/persisted-format migration, deployment, released consumer
boundary or externally consumed new source is introduced. Old WebUI work has
not been merged or deployed according to the accepted design/source records;
no remote ancestry claim is made for its nonancestor source commit. This branch
reconstructs content and source authorship, not literal old-commit ancestry.
No BFF edits, old session mutations, merge or deployment. PR74 and PR63 untouched.
Final publication/review packet and exact new head will follow quick checks/commits.

Follow-up provenance: all 53 packed registry files are byte-identical to their
tracked `clients/js` files at attested source commit
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`; see `npm-source-comparison.json`.
Follow-up verification: final installed declarations typecheck and 62 focused
adapter/session/node cases passed after retaining AsyncError causes, including
real timeout and protocol/API receipt assertions. Six package-source tests passed
again. Formatting, design/structural audits and E2E core typecheck passed after
correcting tsconfig formatting; adapter timeout-only batch passed 22 cases.
No hook framework is declared in repo manifests/instruction paths; canonical
hooks directory contains sample files only, and core.hooksPath is unset.
Actual checkout Git author/committer identity is configured as Jakub Skokan
<jakub.skokan@havefun.cz>, matching the carried production source author; no
identity configuration was changed.

Final quick remainder passed under fresh metadata watcher (exit 0, 141 seconds):
BFF npm setup, `npm run ci:quick` (all lint/format/audit/typecheck gates),
production `npm audit --omit=dev --audit-level=critical` (0 vulnerabilities),
`npm audit signatures` (409 signatures and 101 attestations verified), and
`prefetch-npm-deps package-lock.json`.
Root npmDepsHash: `sha256-yz+FSmc+aZDCwoNF6PiI9VUAbAXlMwzRqyi6Mjdt+e0=`.
The six unresolved optional/bundled-package URLs are unchanged existing warnings;
Nix package builds after review will verify cache completeness. Full dependency
install still reports seven existing dev-toolchain audit findings; the supported
production gate reports zero. No forced unrelated dependency update was made.

All intended dependency/source changes are now committed; exact series and final
source mapping are in the adjacent inventory/review packet. Source/docs change
quick checks pass. Full tests/build/Nix/browser workflows await lead-coordinated
independent final review. Own branch and PR74 are still unpublished/unchanged.

Final dependency commit: `cd3577a6365685273c1b39a724814f7d67931508`.
Final production commit/head: `39f8fd7d2bee0c4754f0f9921d97855da7fbdddf`.
The worktree is clean. `final.diff`, `commit-series.txt`, `final-stat.txt`,
`content-mapping.json`, `remote-before-review.txt`, `review-packet.md` and
`pr74-publication-plan.md` are complete lead/reviewer inputs. Stable session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/

R2 final narrow correction supersedes the prior final head:
`014f7b9c9f451d6275af73c4af30a24668b77b7b` (production commit amended,
original author/date retained; dependency `cd3577a6` unchanged). Four focused
files/67 cases and installed types/direct+scoped lint/format/design/structural
checks passed. See `review-r2.md`, `review-r2.diff` and
`review-r2-range-diff.txt`; final packet/map/PR74 plan refreshed, original
reviewed artifacts preserved. No migrations, deployment or publication.

2026-10-26 C3 supersedes the selected dependency identity with released0.30.2.
Current finalhead `757f7fd8c2d5d3a4d1f6ee464acd29a5a2502176`, dependency
`02b45a7de7eec8966b6a2ade16a46fbb9e1b6c83`, unchangedbase5a2d2bdc.
Old reviewed/R2-closed014f7b9c retained at ownreviewref; see0.30.2/receipt.md
and range-diff/tree/author/source proof. Existing adapter+R2source unchanged.
123focusedcases+6sourcechecks/fullciquick/audit/signatures passed; actualcleaned
source check passed. Fullunits/build/Nix/browser waits for finalreview. No pushes.
