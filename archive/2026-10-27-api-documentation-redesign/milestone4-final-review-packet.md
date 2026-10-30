# Final milestone4 review packet

Review completed on the range below; see `milestone4-final-review.md` for the
independent report and lead narrow-fix addendum. R2's history-only correction
produces current head `9f68dad5436799d82e9c9e1c69e73866a279e9a6` with the exact
same final tree. C is now `0f0399141d23cfecc33f7ba209e5acacc81e60c2`, D
`aafcfa0975ee0d19a57797b5e7c4c9150a8a38a5`, E the current head; A/B and base
are unchanged. The original packet range and findings remain historical below.
R2 is closed by focused committed-boundary/load/final-tree/input proof. R1 stays
open/held. This status adds no new review or integration approval.

Committed source, source-bound 0.31 inputs, profile correction and quick
packaging checks are complete. This packet is ready for lead assignment.
Remaining performance export preparation does not change source or inputs and
runs separately from review. The earlier `review-packet.md` and
`final-review.md` bind only the 82a7 checkpoint and remain unchanged.

## Outcome and scope

Redesign HaveAPI's HTML reference and provide a real vpsAdmin development
preview. Retain straightforward default examples, separate error-handling
detail, compact global language/client variants, scroll continuity, themes,
resource pages, directory, breadcrumbs and synchronized action navigation.
Keep dynamic and configured generated clients discoverable. Preserve mounted
and legacy links, filtered metadata, API/OPTIONS and generated request contracts.
Python examples omit unnecessary main guards. Shared internal guides use the
same shell and readable fenced code.

The user's latest milestone adds top account controls beside a compact theme
dropdown, a visible current-resource label, validator subtables, a search
placeholder, resource/action/parameter priority and explicit phone/tablet use.
They rejected downloading the whole API description on every page navigation.
Final acceptance includes 390/768/1024/1440 px widths, touch/keyboard, useful code and
validator widths, local scrolling and no document-wide horizontal overflow.

Search lazily loads a compact whitelist projection. Fresh versioned HTML derives
one content key from its authorized description; private HTTP caching can reuse
the matching representation across navigation. Ruby fallback and browser matching
use the same projection and representative ordering fixture. No server snapshot
cache, SPA, bulk page-load fetch, service worker, Cache API or JavaScript index/
query/result persistence is introduced. Ordinary GET/no-JS search remains.

The accepted freshness contract is the page's authorized snapshot. Open pages
can retain it; navigation/reload derives a fresh key and result destinations
reauthorize. Cold/conditional index requests authenticate and describe before
key equality/cache success. Mismatch returns 409 without data. Neutral pages and
BFCache restores bootstrap no-store on intent. Browser retention is private,
not physical erasure at logout or instant permission-revocation delivery.

Full behavior/interfaces/ownership are in design.md's milestone4 and bounded
upstream 0.31 sections. Main owns final visible wording and the UI guide.

## Exact source and history

Session: 2026-10-27-api-documentation-redesign. Plan/state/design and evidence are
alongside this packet. HaveAPI worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi`.
Remote: `git@github.com:vpsfreecz/haveapi.git`.

- Base: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
- Head: `ab5b11188941d1c8c918951cdee162e9aa9f68cf`.
- Tree: `c3c3e04337bcf9669dbb79611d72a65c686af9e0`.
- Complete feature diff: 110 files, 6,488 insertions and 711 deletions.

| Group | Commit | Purpose |
| --- | --- | --- |
| A |4363d1114f31cbb5d61411a95f6501bda17b50c0| Simple/detailed dynamic examples and Context |
| B |260e3ea8a469c8840164bd8a0f5044238f5472e1| Generated adapter examples and complete-program Go fixture |
| C |d25dd61260a5768552bac5f6a8a201bb4c28d540| Final HTML/common shell/navigation/search/browser/validator/identity UI |
| D |6049fc333e57baca4c97e9eb482f0c6b332041ba| Existing optional OAuth documentation sessions, held |
| E |ab5b11188941d1c8c918951cdee162e9aa9f68cf| Request-local resource ownership/cache and performance contracts |

C's server projection, forms/anchors, browser matcher and common DOM implement
one reference UI contract. Obsolete HTML-query enhancement and intermediate
layouts are folded into final C. Core examples, generated adapters, optional
auth and performance remain separate. Shared JSON ordering data is a test
fixture, not a behavioral registry. All recreated commits passed ordinary hooks;
C retains permitted 72-column message advisories within the repository's
80-column limit.

History proofs are in `history-milestone4-refresh-20261028t121940z/` and
`history-upstream-031-20261028t123743z/`. Same-baseline 09ef7905 and 4f80b23c
trees match exactly. The upstream refresh to a0c78 preserves all five patches/messages:
range-diff reports all `=`, with aggregate feature patch SHA256
`ea0f7ef5d5f57278ff21a439156e7684c869a55b7171fd67da503e59e0d1d5f6`.
Old-final→new-final delta equals upstream 2f515626→f6e5c375, SHA256
`426ab56641ee6c91a1cc596a5d46f318eeaff081b6a2d0bb6f64d8ec85c96cf3`.
Owner2 independently reconstructed that exact new tree. Lead independently
verified both patch/delta equalities. Trees differ across the upstream refresh.
All older refs/receipts and original-range proof remain linked and retained.

The subsequent one-spec route correction is folded into C; see
`history-profile-mount-fold-20261028t132040z/receipt.md`. Final ab5b1118 and
sidecar c5badd trees match exactly. The a0c78→final delta is only that accepted
test patch, SHA256
`74ddf85e523065f7a245b00e70457a76936191377986330149a38ce904e8ce23`.
Lead independently verified that digest and c5badd→final empty diff. A/B are
preserved; D/E patches and all 310 protected input hashes/graph inventories are
unchanged. Current aggregate feature patch SHA256 is
`2907070a7852ee24c31fa8efe9572c0a6336ae4ac21cc8823ce8f502179039c1`.

No feature migrations, schema/seed lineage or dependency/channel/pin update
streams exist. None need classification as merged/released/deployed/externally
consumed. Upstream's version synchronization is baseline provenance. No feature
release, default integration or external SDK publication occurred. Old HTTP
captures are review snapshots; rewritten nonancestor SHAs are not called merged.
Independently conclude on full-series consolidation, migrations and streams.

## Ownership, compatibility and inputs

HaveAPI owns Context/renderers, authorized documentation routes, presentation
and generator-gem adapters. Actual vpsAdmin consumer is the same-session clean
worktree at 08c3bd7e3cb4dc324a0381df6a1eec190daab1a7; its API pins haveapi
~> 0.29.9. No vpsAdmin code/pin changed. Preview chooses matching source packages
explicitly; a mount alone does not select candidate gems. Discover consumers
from current imports/manifests and reuse prior actual-consumer evidence only at
its recorded scope. No cross-session records/team/cluster access is authorized.

Upstream added release-lineage fixtures, synchronized 0.31.0 package metadata
and master-version policy in 24 paths, with zero overlap against 109 feature paths.
No conflict/application repair occurred. Root tool graph has no HaveAPI package.
Affected local server/Go-acceptance/Rust path locks, JS build/install metadata
and Python editable metadata require fresh 0.31 proof; old 0.30 inputs cannot be
relabeled. External resolutions stay exact. Separate published TS runtime
0.30.2 fixed SHA and independent Rust 1.95 remain prescribed external inputs.
Frozen benchmark graph/budgets/reference are unchanged. Final manual quick pair
is fresh upstream f6e5c375 versus final candidate; old exports are historical.

The preview has its own five-source-gem graph. Owner4 will refresh only that graph
and the HTTP unit after review, preserving external resolutions and proving 0.31
loaded paths. Current HTTP preview still serves its earlier milestone3 capture.
HTTPS/OAuth/private fixtures remain held. Live review URL:
http://172.16.106.40:4567/v7.0/ . Individual runtime/recovery receipts live in
`preview-infrastructure.md`, `preview/` and `browser/`.

## Known finding and explicit hold

Previous reviewer0 found Important R1: invalid/missing/replayed OAuth callback
can clear an existing documentation session without logout CSRF. No token
disclosure/API authorization bypass was shown. Lead explicitly defers the narrow
fix under the user's OAuth hold; this is not correctness acceptance. Preserve
R1 open and block OAuth integration/rollout. Non-OAuth verification may continue.
OAuth module/provider/spec/guide bytes remain unchanged; moved control markup
uses original-owner Basic projections and exact zero-fuzz restoration. No new
OAuth implementation/preparation/TLS/cross-session action is authorized.

## Documentation and checks

Owning guides: doc/documentation-ui.md (main's snapshot/cache/control/table copy),
doc/client-examples.md, doc/documentation-oauth.md, doc/performance.md and the
three generator guides. Protocol content is unchanged. Review placement and
discoverability; temporary rollout/source facts belong in session receipts.

Milestone4 source quicks: presentation 56/0 plus 6 Ruby lint/4 ERB checks;
search 28/0 plus 6 Ruby lint; all 3 asset scripts/syntax/whitespace pass.
Includes authorized
view/key/header/selector/exclusion/shared-order cases and browser unit validation/
matching/loading/reset/error cases. Old compiler/profile/80 Go/191 generated and
packaging evidence retains its exact scope; it is not a new 0.31 integration pass.

Source-bound input refresh passed all nine stages in 28.44s; see
`verification/upstream-031-inputs-a0c78d1c/receipt.md`. Local loaded packages,
rebuilt JS runtime/declarations and installed Python editable package are 0.31
from this worktree. External Ruby/npm/Python graphs are unchanged, including
distinct Go JSON3.1.0 versus server/Rust JSON2.21.2; 97 protected input hashes
are unchanged. First attempt stopped on a comparison of local PATH checksum
version labels; the lead inspected the exact diff and authorized one narrow
corrected fresh-watcher resume. Both operations/locks remain. No product/source
repair, external dependency update or integration test ran in that preparation.

Final-head extracted-gem packaging PASSED: three examples, zero failures,
9.75s wall (2.85s examples +1.03s load), seed60317. Exact final ab5b1118/treec3c3
is recorded in `verification/quick-packaging-ab5b1118/05-packaging.log`, read
independently by lead. It builds haveapi0.31.0, extracts/serves shared routes and
rejects missing/empty shared documentation. Exact command in the root Nix shell:
`cd servers/ruby; BUNDLE_GEMFILE="$PWD/Gemfile" bundle exec ruby
-I../../clients/ruby/lib -I../../clients/typescript/lib -S rspec
spec/packaging_spec.rb --format documentation`.

An additional evidence-only metadata/extraction helper omitted standard
`require 'fileutils'` and stopped after the successful packaging tests. That
helper error is retained in `06-package-metadata.log`; a narrow correction and
remaining metadata/export/frozen-availability preparation are authorized without
repeating the successful tests. No application/source/input changes are needed.
New `performance-ab5b1118` exports are not yet claimed prepared or measured.

First focused batch: make doc, metadata and loaded-source checks passed;
51 lineage/profile examples had two failures. Existing specs requested the
overview but expected action prose/private samples now served on resource pages.
Owner1 preserved overview package/init coverage and moved resource-specific
locale/private/admin/member assertions to the mounted widget resource route.
All seven profile-mount examples now pass, including both detail levels; lint
is clean. The other 44 examples' files and all application/input bytes remain
unchanged. This correction is committed/folded into C, with successful hooks.
Packaging/export stages did not run after the failure. See
`verification/quick-packaging-a0c78d1c/receipt.md`; no application regression or
version repair is implied by that stale assertion boundary.
The fix evidence is `verification/profile-mount-route-fix-a0c78d1c/receipt.md`.
Only unrun metadata/export/frozen-availability preparation resumes against
final ab5b1118; successful input preparation and unrelated quicks are retained
at their proved file/runtime/input scope, without claiming a whole-batch rerun.

Postreview required gates remain: full documentation/asset bundle, Python
encoder and installed local npm+wheel/sdist snippets, generated Go/TS wire/Rust
development+MSRV acceptance, ordinary deterministic performance, all-client/
both-detail/both-scaling contracts and exact paired quick run. Postreview also
includes final HTTP/responsive/cache browser acceptance; ordering among batches
is lead-coordinated with one fresh operation-scoped watcher at a time. No broad
unchanged JS runtime suite, full SDK runtime campaign or release build is added.
Warm search diagnostics do not replace calibrated performance policy. No claim
of equal simple/thorough real-wire coverage: dynamic installed harness extracts
thorough panels; simple fragments have focused syntax/type/shared-body coverage.

## Reviewer selection

Risk: HIGH (authorization-filtered retained metadata and existing optional
cookie/token isolation). Select retained eligible independent reviewer0 with
saved Sol/xhigh/read_only; verify native identity/settings on assignment, no
overrides/nested reviewers. General, architecture/repetition, scope/proportionality
and risk/compatibility lanes all apply. Read mandatory-change-review and all four
references. Inspect affected milestone4/cache/input behavior plus the complete
final range/history/migration disposition. Earlier 82a7 review is context, not
coverage of this deliverable. No integration approval is supplied by review.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
