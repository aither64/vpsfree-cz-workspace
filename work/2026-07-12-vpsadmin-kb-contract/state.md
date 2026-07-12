# vpsAdmin KB documentation contract state

## Session

- Initiative slug: `2026-07-12-vpsadmin-kb-contract`
- Started as the explicitly planned follow-up after completing the Czech and
  English screenshot publications.
- The current shell still carries the previous completed session slug; all new
  work is isolated under this initiative's tracking directory, branches, and
  worktrees. The global KB staging container is stopped and unowned.

## Repositories

- `vpsadmin-kb-captures`: branch `2026-07-12-vpsadmin-kb-contract` in
  `worktrees/2026-07-12-vpsadmin-kb-contract/vpsadmin-kb-captures`, based on
  `origin/master` `951a5e6`, at `7185b17` and pushed. Review fixes remain
  folded into the first two logical commits; a third integration-found commit
  closes lingering proxy tunnels after successful captures.
- `vpsadmin`: branch `2026-07-12-vpsadmin-kb-contract` in
  `worktrees/2026-07-12-vpsadmin-kb-contract/vpsadmin`, based on
  `origin/master` `af3b885`, at `f76c0cf` and pushed.
- `vpsfree-cz-configuration`: branch `2026-07-12-vpsadmin-kb-contract` in
  `worktrees/2026-07-12-vpsadmin-kb-contract/vpsfree-cz-configuration`, based
  on current `origin/master` `606ab08`, at `f2a98c23` and pushed. It carries the
  four still-unmerged but deployed KB staging commits as separate cherry-picks
  before the new plugin packaging commit.
- `dokuwiki-plugin-vpsadmindoc`: branch
  `2026-07-12-vpsadmin-kb-contract` in
  `worktrees/2026-07-12-vpsadmin-kb-contract/dokuwiki-plugin-vpsadmindoc`,
  initial commit `ed92a4d` and pushed to the user-created repository. The same
  reviewed root commit is now also `master`; GitHub still considers the feature
  branch default because the available token cannot change repository settings.
- Top-level workspace: plan/state tracking on shared `master`; KB tooling
  changes, if any, will be staged path-by-path around unrelated shared changes.

## Current findings

- Production and staging configurations package the same explicit DokuWiki
  plugin list with fixed GitHub revisions and hashes, so the new plugin must be
  added to both lists.
- Existing `<page>` translation mapping is provided by `mlfarm`; the proposed
  plugin owns only vpsAdmin documentation annotations and does not replace the
  language-pairing plugin.
- `vpsadmin-kb-captures` schema 5 already provides stable semantic screenshot
  concepts, checkpoints, bilingual source pages, media IDs, hashes, and pinned
  vpsAdmin provenance. It is the natural owner for the cross-repository impact
  checker.
- The legacy PHP WebUI builds sidebar labels and routes together at distributed
  `sbar_add()` call sites. Stable landmarks should be added through explicit
  contracts/helper parameters rather than inferred permanently from translated
  text.

## Implemented

- Added optional, validated documentation-ID parameters to vpsAdmin's menu,
  sidebar, and table-title helpers and annotated the initial documented
  controls. No routes, labels, API contracts, or persisted state changed.
- Added a capture-owned YAML contract with 29 controls, 22 navigation paths,
  bilingual labels, page bindings, source fingerprints, and 32 screenshot
  concept bindings. The checker validates it against the pinned vpsAdmin Czech
  catalog, source tree, rendered landmark declarations, and capture inventory.
- Changed the Features and rescue-mode captures to select their sections via
  semantic IDs as an initial end-to-end use of the landmarks.
- Implemented the standalone `vpsadmindoc` DokuWiki syntax plugin. It preserves
  and escapes human-authored bodies, emits `data-vpsadmin-doc-id`, records page
  metadata, and visibly diagnoses malformed IDs. The test suite includes a
  render through the real nixpkgs DokuWiki parser.
- Pinned plugin commit `ed92a4d` and its fetched content hash in both the
  production KB and on-demand staging plugin lists. This prepares closures only;
  neither machine nor page content has been changed.

## Quick verification

- vpsAdmin WebUI PHPUnit: 65 tests, 246 assertions; PHP CS Fixer dry run passed;
  all Overcommit hooks passed for `f76c0cf`.
- `vpsadmin-kb-captures`: `nix develop -c bin/check` passed with 8 contract
  tests/50 assertions and strict validation of 59 concepts, 118 variants, and
  118 PNGs.
- `dokuwiki-plugin-vpsadmindoc`: `nix develop -c bin/check` passed PHP syntax,
  isolated behavior checks, and a real DokuWiki parser/render integration.
- `vpsfree-cz-configuration`: Nix formatting passed and `confctl ls` evaluates
  both affected targets. Repository hooks passed for `f2a98c23`.

## Compatibility and deployment

- WebUI attributes and DokuWiki syntax are additive; there are no schema,
  protocol, API, or on-disk-format changes and mixed WebUI versions are safe.
- The plugin must be deployed before annotated pages. Existing pages are
  unaffected by installation. Production rollback must not remove the plugin
  while annotated tags remain published unless fallback behavior is first
  proven.
- Configuration can be built here, but only the operator can deploy aitherdev
  or the production KB container.
- Long `confctl` builds and staged page rendering were deferred until the
  mandatory standalone review; builds are now authorized, while staging still
  waits for deployment and local page candidates.

## Mandatory review

- The exactly one standalone fresh-context review found one blocking checker
  weakness: labels, route fragments, and landmarks were checked independently,
  so stale PO entries, prefix routes, or test-only ID references could hide
  production drift. It also requested accumulated impact output and explicit
  semantic-selector bindings, and advised stricter page-array validation.
- Fixed all findings before long builds. Each control now fingerprints the
  normalized production source context coupling its ID, label, and route;
  `member.edit-profile` also fingerprints its label assignment. Runtime lookup
  is restricted to the declared production paths. Tests mutate real copied
  vpsAdmin source for route, label, and landmark drift and reproduce the
  reviewer's failure modes.
- The checker now accumulates every discrepancy and prints the affected Czech
  and English pages and screenshot concepts. Three migrated selectors have
  exact machine-readable source declarations, with a regression test proving a
  translated-selector reversion fails. Page bindings must be non-empty string
  arrays in language-appropriate namespaces.
- Rewrote the unmerged capture branch so the generic hardened contract remains
  in commit `1fe6457`, while selector declarations/tests remain with their
  scenario implementation in `41d5cd9`. The final full check passes.
- The review found no plugin security/escaping issue and independently verified
  nested DokuWiki bold/link rendering. Residual integration gaps are the long
  Nix builds, Playwright capture exercise, real metadata persistence, live
  staging rendering, and eventual annotated page inventory.

## Integration verification

- `confctl build -y cz.vpsfree/machines/aitherdev` passed and created generation
  `2026-07-12--18-02-23` with the updated on-demand staging container.
- `confctl build -y cz.vpsfree/containers/int.kb` passed and created generation
  `2026-07-12--18-04-34` for the production KB container. Both Czech/English
  packages in both closures contain `lib/plugins/vpsadmindoc/syntax.php` with
  identical SHA-256
  `a538a08b0a6e50d438b0f274b75f2d1f042d26672709ff50154895322af71cda`.
- The first confctl build attempt reached its interactive confirmation and
  received EOF; reran with the documented noninteractive `-y` option. The first
  ambient configuration push was rejected by its Overcommit hook's missing
  gems; pushing inside `nix develop` passed, as required by the repository.
- The bridge capture cluster refused to start because its reserved frontend IP
  already responded. To avoid disturbing another initiative, used the supported
  `--network local` fallback and recorded that bridge unavailability here.
- The isolated `kb-contract` screenshots topology started successfully. English
  captures passed for `vps-management/feature-settings`,
  `vps-details/feature-settings`, and `rescue-mode/boot-form`, proving all three
  semantic selector declarations against the real WebUI.
- The first feature capture changed 774 pixels despite identical dimensions;
  the other two were byte-identical. Since this phase changes selectors rather
  than reviewed bitmap content, restored the generated feature PNG to its
  reviewed inventory hash `6acd27dc...` and strict validation passed.
- The second successful capture then waited indefinitely while closing an open
  HTTP CONNECT tunnel. Added explicit proxy-socket tracking and teardown plus a
  regression test in capture commit `681ebef`. The rescue capture subsequently
  completed and exited normally. The full `bin/check` passes, and the cluster
  is stopped with its GC root removed.
- vpsAdmin GitHub WebUI PHPUnit and i18n-health workflows passed at `f76c0cf`.
  The broader selected integration-test workflow remains in progress; no rerun
  has been requested.

## Production approval gate

- Production `int.kb` deployment and every production KB content update still
  require separate explicit approval. No production configuration or page was
  changed by this initiative.

## Staging annotation release

- User deployed aitherdev configuration `f2a98c23` and changed the plugin
  repository default branch to `master`. Verified both states and started the
  stopped `kb-staging` container on the new generation without resetting its
  mirrored content.
- The staging controller remains owned by the verified active development
  session `2026-07-10-kb-czech-fixes`; the semantic-contract work and artifacts
  remain tracked under this follow-up initiative.
- Created paired disposable staging pages to exercise the real packaged plugin.
  Both language sites rendered `data-vpsadmin-doc-id`, nested bold text, and
  internal links correctly, and the language plugin linked the pair in both
  directions. Deleted both disposable pages after the check.
- Refetched exact current production sources for all 18 Czech and 16 English
  contract-bound pages, including production revision IDs and SHA-256 hashes.
- The candidate builder prepared 55 annotations across 33 changed pages. It
  also corrected stale English labels to current vpsAdmin terminology:
  `Session log` to `Sessions`, `Boot from VPS template` to
  `Boot VPS from template (rescue mode)`, DNS label casing, and several
  navigation descriptions that omitted current submenus/forms.
- Added previously missed `member.advanced-email-configuration.open` and
  `member.totp-devices.open` paths. Capture contract commit `7185b17` records
  51 page/path bindings and six explicit exceptions where an affected page has
  no in-prose navigation phrase. Its checker rejects unknown/malformed tags,
  count drift, and unclassified affected pages; 4 tests/10 assertions pass in
  addition to the existing contract and inventory suites.
- Generated review ledger `kb-candidates/review.md`, guarded Czech/English
  release manifests, and reproducible fetch/build/render-verification helpers.
  Top-level commits `228dc2b` and `d661da9` separate tooling from generated
  source/candidate/release artifacts.
- Staged 18 Czech pages and 15 English pages at their production IDs. Both
  manifests verify byte-for-byte, 31 language pairs verify bidirectionally,
  and live HTTP rendering verifies all 33 pages and all 55 expected semantic
  IDs with no invalid-tag warnings. The English manifest is the current pending
  release because it was staged second; both language page contents remain in
  staging for review.
- Source snapshots intentionally preserve pre-existing production trailing
  whitespace and EOF layout. `git diff --cached --check` therefore reported
  those inherited lines in both source and byte-preserving candidate copies;
  the candidate builder changes only its exact counted replacements.
- Production remains untouched. Staging review URLs are the normal page URLs
  under `http://kb-cs.aitherdev.int.vpsfree.cz/` and
  `http://kb-en.aitherdev.int.vpsfree.cz/`; the complete replacement ledger is
  `work/2026-07-12-vpsadmin-kb-contract/kb-candidates/review.md`.

## Approval boundaries

- Read-only production KB inventory is allowed.
- No staging KB mutation is planned until plugin packaging and annotated local
  candidates have passed review.
- Every production KB update requires a new explicit user approval.
- Machine deployment remains operator-only; this initiative may prepare and
  build configuration but cannot deploy it.

## Complete-inventory review follow-up

- A second standalone review found that the first annotation inventory was
  circular: production fetching started from already-curated contract pages.
  It also identified missing standalone Edit profile references, both User data
  entry routes and the full deployment path, Mount in both impermanence pages,
  and the previously unfetched current exports articles. The English payment
  annotation also covered more prose than the navigation phrase.
- Production fetching now begins with `core.listPages` and snapshots all 116
  Czech and 70 English pages before applying any curated replacements. The
  capture repository independently scans every candidate page and records 108
  navigation-shaped paragraphs as bound paths or explicit classifications;
  candidate validation rejects partial page sets, new unclassified paragraphs,
  stale classifications, and tag/path mismatch.
- vpsAdmin commit `870d16773` adds stable landmarks for the VPS menu, User data
  entry, Exports menu, and Export dataset action. WebUI PHPUnit passed with 65
  tests and 248 assertions, and all repository hooks passed. The branch is
  pushed.
- Capture commits `9d24744`, `8bc56cb`, and `ba3fdcc` pin vpsAdmin
  `870d16773`, add the
  independent inventory/checker, and bind the missed paths. Full `bin/check`
  passes: 33 controls, 29 paths, 65 annotation bindings, 6 path exceptions,
  8 contract tests/50 assertions, 5 annotation tests/13 assertions, and the
  unchanged 59-concept/118-variant screenshot inventory. The branch is pushed.
- The unpaired legacy English page `manuals:vps:vpsadminos:storage` remains in
  the complete scan with explicit classifications, but is not annotated: it has
  no Czech counterpart and the release workflow correctly rejects an unpaired
  English page. The current paired `navody:vps:exporty` and
  `manuals:vps:exports` pages are annotated.
- Reset only the owned staging mirror after its baseline guard rejected
  layering over the old candidate. Staged and verified the corrected release:
  19 Czech pages, 16 English pages, 35 rendered pages, and 75 semantic tags.
  The English manifest is pending for review. Production remains untouched.
- The exactly one fresh mandatory follow-up review reproduced three blocking
  checker defects: the heuristic missed 14 annotated source paragraphs, count-
  only page validation accepted duplicate/omitted identities, and the legacy
  export page had false generic classifications while being removed from its
  affected paths. It found the 35-page/75-tag staging content itself correct
  and confirmed that production was untouched.
- Fixed all three findings. Discovery now runs on immutable production sources,
  every candidate paragraph containing a tag must have been independently
  discovered, and the inventory pins exact sorted page IDs while rejecting
  duplicate IDs and files. Regression coverage reproduces the duplicate-page
  bypass. The legacy storage page is again associated with `exports.open`,
  `exports.export-dataset.open`, and `backups.vps.open` through truthful per-path
  exceptions explaining why the unpaired duplicate is not annotated/released.
- Final validation passes with 175 independently discovered source paragraphs,
  65 annotation bindings, 9 path exceptions, 75 candidate tags, 8 contract
  tests/50 assertions, and 6 annotation tests/16 assertions. Rewrote the
  unmerged vpsAdmin/capture correction commit messages to satisfy the 80-column
  rule and force-pushed with lease. Shared top-level master history was not
  rewritten; its already-committed overlong correction bodies remain the
  review's advisory exception to avoid disrupting concurrent workspace users.
- GitHub WebUI PHPUnit and i18n-health workflows pass for final vpsAdmin commit
  `870d16773`. Superseded selected-integration runs were cancelled after each
  force-push; final CI run `29202530426` is still in progress.

## Durable workflow handoff

- User accepted the staged result and requested a durable workflow that future
  agents will discover. Added the canonical end-to-end guide at
  `vpsadmin-kb-captures/docs/webui-change-workflow.md` in capture commit
  `ddcb038`. It covers the trigger, semantic-ID decisions, revision pinning,
  impact reports, bilingual recapture, immutable KB source validation, staging,
  and the explicit production approval boundary.
- Added a pointer to that guide in the capture repository README/AGENTS and in
  vpsAdmin AGENTS commit `cd8344cc4`. Added `vpsadmin-kb-captures` to the
  top-level project map and linked the guide from the workspace KB instructions
  without staging the unrelated pre-existing AGENTS change.
- Promoted reusable preparation logic to stable workspace commands:
  `bin/kb-contract-fetch`, `bin/kb-contract-build`, and
  `bin/kb-contract-manifest`. Exact replacement plans are data, while fetching,
  candidate construction, review ledgers, counterpart checks, source/candidate
  checksums, and guarded manifests are reusable code.
- `test/kb_contract_tools_test.rb` passes with 3 runs/18 assertions. Existing
  KB page, stage, and cleanup suites also pass with 58 runs/214 assertions. A
  live read-only fetch reproduced 116 Czech and 70 English page identities.
- No configuration deployment or production KB write was performed. The next
  operational decisions remain feature-branch integration, production plugin
  deployment, and separately approved Czech/English manifest promotions.
- The exactly one fresh mandatory review found three blocking issues in the new
  handoff: manifests could combine stale candidates with a newer source
  baseline, explicit replacements hid surrounding edits in the review ledger,
  and the guide's two-language promotion sequence could not satisfy the single
  pending-manifest guard. It also requested containment checks for IDs/indexed
  paths and an explicit staging-ownership closeout.
- Fixed all findings. Manifests now require the candidate's recorded source hash
  to equal the chosen source snapshot, explicit replacement tag bodies must
  equal their declared bodies and the ledger displays the complete replacement,
  and all remote/index-derived paths and semantic/page IDs are validated before
  access. Duplicate page IDs/files and English counterparts are rejected.
- Guide commit `704f16d` now explains that both languages remain visible on
  staging but only one manifest is pending. After approval, each language is
  restaged, verified, and immediately promoted before staging ownership is
  released; abandoned pending reviews require explicit discard.
- Expanded tooling coverage passes with 7 runs/33 assertions, including source
  snapshot mismatch, explicit ledger text, path escape, and malformed semantic
  ID regressions. The existing 58 KB tests/214 assertions and live read-only
  116/70-page fetch also pass.

## Feature integration

- User authorized integration. Fetched all three upstream repositories; each
  feature branch was already a direct descendant of current `origin/master`, so
  no rebase or conflict resolution was needed.
- Created fresh detached merge worktrees under
  `worktrees/2026-07-12-vpsadmin-kb-contract-merge/`, fast-forwarded them with
  `git merge --ff-only`, tested the exact merge heads, and pushed:
  - vpsAdmin `master` to `cd8344cc4`;
  - vpsadmin-kb-captures `master` to `704f16d`;
  - vpsfree-cz-configuration `master` to `f2a98c23`.
- Merge-head verification passed: vpsAdmin WebUI PHPUnit 65 tests/248
  assertions; the full capture `bin/check`; and configuration evaluation of
  `cz.vpsfree/machines/aitherdev` and `cz.vpsfree/containers/int.kb`. Earlier
  full `confctl build -y` results apply to the identical configuration head.
- Removed merge-worktree PHPUnit and Nix-shell caches, then removed all three
  temporary merge worktrees. Feature branches remain locally and remotely as
  required.
- This integration does not deploy `int.kb`. The operator must deploy production
  configuration from the build machine before any annotated production page is
  promoted. Both production KBs remain untouched.
- Removed the four merged project feature worktrees (vpsAdmin, captures,
  configuration, and DokuWiki plugin) after confirming they were clean. Their
  local and remote feature branches remain; canonical bare repositories retain
  the merged refs.
