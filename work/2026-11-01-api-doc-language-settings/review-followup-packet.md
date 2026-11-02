# Affected final review: CI build and provenance corrections

Use the retained same independent reviewer and all four affected lanes, same
Sol/xhigh/read-only settings. This follows the completed [original review](review.md)
and [packet](review-packet.md); do not repeat unaffected translation/UI review.

Repository/worktree unchanged. Base `391b0190241cf195a69b06f7297d3e4eebec5a83`.
Final consolidated committed head `e7ac8578a2ffd07b3ac7da05a27996191619a8f9`,
clean worktree/index. Fresh origin/master still base. Published prior head
`442077694c2439db48051d0a2e11aa58cb94261f` is retained remotely pending final
verification; no default integration/deployment occurred.

Complete final series:

1. `b6760cd01b360ed4f3b23bb35686d060b8d94e29` runtime/UI/catalog, including
   prior one-handler remediation and corrected search locale assertions.
2. `f390c9fdc13dbbc4b67adba3a2a87b7584e8b8f9` translated articles/source move/
   packaging, including workflow paths and standalone schema-generation repair.
3. `e7ac8578a2ffd07b3ac7da05a27996191619a8f9` narrowly reviewed packaging
   normalization in existing performance source receipts, its tests and guide.

No obsolete fixups retained. Old unconsolidated head `c1e47a2033dfcaace071849cd2f80c92e216f20f`
and final have identical tree `dbc8470a294dc57a5a06f2b164f5522701e36d19`.
Old/new range-diff confirms fixups folded and separate guard patch unchanged.
No migrations, dependency pins, budgets or repeated update streams. No previously
deployed/nonancestor lineage claim; the old feature head was only published.

## New evidence and changes

The full old-head local server batch reached 986 examples with two failures.
Release CI independently reproduced the same stale search assertions. Docs now
use browser Accept-Language independently of API X-Language: tests now verify
both Vary fields and explicit custom-header independence. Only tests changed.
Focused search routes: 7/7, scoped RuboCop clean, hooks passed.

Server CI Ruby 3.2/3.3/3.4 failed `make doc` before tests: schema generation bare
required I18n, while application gems lived in component vendor/bundle. Copydoc
now reads its one presentation heading from the canonical YAML catalog using
stdlib YAML+ERB, passing an escaped local to the template. No dictionary/gem
dependency/new runtime behavior. Isolated empty-gem regression failed before and
passes after; root external make doc passed; complete en/cs generated schemas
(including all four code blocks) match prior bytes. Focused packaging/shared-page
38/38, shell syntax, style and hooks passed.

CI all-client documentation contract passed. Paired comparison failed before
timing because full server gemspec text changed only its doc file enumeration;
evaluated dependency projections and every other compared input were equal.
Logs/artifacts under `ci-performance-41345966685/` bind original selection,
source tar hashes and dependency compatibility evidence. See architect's
`design.md` CI follow-up for the bounded policy.

New guard support (33 comparator lines, focused specs, 11-line owning guide):
existing SourceVersions shared capture/validation normalizes only the exact
once-only shallow and recursive+File.file? server files statements. All other
bytes remain strict, with evaluated dependencies/runtime/locks unchanged. Raw
source contents/hashes remain bound; new `file_selection: documentation-files-v1`
marker selects replay reconstruction. Marker-absent legacy receipts retain old
rule; historical maintenance normalization stays unchanged. No generic parser,
whole-gemspec exclusion, environment migration, budget/reference waiver or CI-only
exception. CI/Worker/replay already use shared helper, no wiring changes.

Focused source_versions specs **18/18** after final string-style edits, RuboCop
2/2, make doc/whitespace/hooks passed. Actual retained compatibility receipt
reconstruction proved new normalized baseline/candidate inputs equal while raw
hashes remain original and evaluated gemspecs unchanged. Tests cover exact forms,
unknown/duplicate/outside-byte/dependency/Ruby strictness, CI+Worker inputs,
current+legacy replay, marker/raw/normalized/content/source tampering and strict
maintenance behavior. Guide paragraph passed lead's direct writing skill pass.

## Requested affected assessment

Inspect exact delta from published repaired prior head
`442077694c2439db48051d0a2e11aa58cb94261f..e7ac8578a2ffd07b3ac7da05a27996191619a8f9`:
7 files, 194 additions / 18 deletions, primarily meaningful regression tests.
Confirm build boundary, provenance/replay strictness, compatibility and scope,
plus final whole-series history/no-migration/no-repeated-stream conclusion.
All intended changes committed and quick checks passed. Do not start broad tests,
edit source or spawn reviewers. Report findings/decision to lead for durable save.

After accepted review, rerun broader server/browser checks, all-client contract
and the originally interrupted exact base-to-final paired comparison (CI). Then
start the requested temporary in-memory API preview and provide its URL. No
integration or production deployment permission is supplied by this review.
