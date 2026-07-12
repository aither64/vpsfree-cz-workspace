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
  `origin/master` `951a5e6`, at `41d5cd9` and force-with-lease pushed after
  folding review fixes into the two logical commits.
- `vpsadmin`: branch `2026-07-12-vpsadmin-kb-contract` in
  `worktrees/2026-07-12-vpsadmin-kb-contract/vpsadmin`, based on
  `origin/master` `af3b885`, at `f76c0cf` and pushed.
- `vpsfree-cz-configuration`: branch `2026-07-12-vpsadmin-kb-contract` in
  `worktrees/2026-07-12-vpsadmin-kb-contract/vpsfree-cz-configuration`, based
  on current `origin/master` `606ab08`, at `f2a98c23` locally. It carries the
  four still-unmerged but deployed KB staging commits as separate cherry-picks
  before the new plugin packaging commit.
- `dokuwiki-plugin-vpsadmindoc`: branch
  `2026-07-12-vpsadmin-kb-contract` in
  `worktrees/2026-07-12-vpsadmin-kb-contract/dokuwiki-plugin-vpsadmindoc`,
  initial commit `ed92a4d` and pushed to the user-created repository.
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

## Approval boundaries

- Read-only production KB inventory is allowed.
- No staging KB mutation is planned until plugin packaging and annotated local
  candidates have passed review.
- Every production KB update requires a new explicit user approval.
- Machine deployment remains operator-only; this initiative may prepare and
  build configuration but cannot deploy it.
