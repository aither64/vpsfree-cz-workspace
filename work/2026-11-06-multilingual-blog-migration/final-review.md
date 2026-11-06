# Final source-preparation review packet

R0 owner: `implementer2`. **FINAL packet, ready for lead completeness check.**
All intended source is committed, owner quick checks passed and final histories
are bound below. This is evidence assembly, not an independent review. The lead
checks completeness and invokes the retained reviewer; no review has been
invoked or certified by R0. User authority expressly excludes merges and
production transition; this packet supplies neither. Final immutable artifact,
longer system checks and exact runtime verification remain later work.

## Outcome, boundary and acceptance

Session: `2026-11-06-multilingual-blog-migration`. Read [plan](plan.md),
[state](state.md) and [design](design.md), particularly D6 and D8. Earlier prose in
those living records may describe superseded checkpoints; exact owner receipts
and the ranges below delimit evidence.

Prepare a Hugo replacement for the existing WordPress blog: recognizable Flat
design; all 125 Czech articles at original paths, six original bylines, 107
approved historical comments/43 reply links, original media and feed identities;
125 complete English drafts on a separate `.org` host root; standalone authoring
instructions and a registered VPN preview. Future CS/EN comments share one
original Czech discussion identity through default-off native Discourse embedding.
Prepare, without enabling, an independently released static artifact/hosting
candidate and the internal `blog.int.vpsfree.cz` DNS entry.

Source acceptance requires complete public projection/hash/privacy evidence,
full draft/source fidelity, stable URLs/GUIDs/anchors, source-controlled disabled
runtime boundaries, documented recovery, a coherent complete branch series and
the quick checks for each final source. Human translation approval, public DNS/TLS,
actual forum behavior, production release admission and final immutable artifact/
runtime evidence are separately identified gates, not implied successes.

The user approved one-time blog `main` initialization at `0354dac` only. No later
merge/default advance or current-blog change is authorized. No production forum
requests/writes, transition, machine claims or activation belong to this review.
The user waived a formal WordPress freeze: a brief pre-switch delta check and
refresh only on detected changes remain the later capture contract. Historical
comments remain in their source language; English publication requires actual
human review. The `.org` production host replaces the abandoned `/en/` proposal;
VPN preview's `/en/` home is a separate native single-origin arrangement.

## Review policy and selection

Overall risk: **high**, because this crosses public URL/feed contracts, public
data projection/privacy, persisted release state, artifact identity, host/network
boundaries and rollback. Default-off behavior limits current runtime effects but
does not remove these source-review concerns.

Use all four lanes in one independent assignment:

- General: correctness, scope, complete commit series and dependency-stream history.
- Architecture and repetition: importer/render/artifact/hosting ownership and
  finite interfaces; avoid duplicated release policy or speculative frameworks.
- Scope and proportionality: compare the implementation with actual user
  decisions, including preservation and explicit no-transition boundaries.
- Risk and compatibility: sanitization, public identifiers, release integrity,
  disabled-state preservation, interruption/retry and rollback/admission limits.

Policy: [mandatory-change-review](/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/skills/mandatory-change-review/SKILL.md),
including all four `references/*-review.md` lane files. R0 read the skill and all
four references. Retained selection verified from the same-session roster:
`reviewer0`, purpose `review`, model `gpt-6.1-sol`, saved effort `xhigh`, access
`read_only`, state `ready`, thread `01a1b293-016d-7f41-95f0-b2c1da14ee3e`.
It authored no package implementation. The lead must recheck eligibility at
invocation and omit model/effort overrides. No fallback or reviewer launch has
occurred in R0. Review findings and explicit whole-history/migration/stream
conclusions remain for that reviewer, not this packet assembler.

## Repositories and current ranges

All worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/`;
all feature branches are `2026-11-06-multilingual-blog-migration`.

| Repository / worktree | Review base | Final source head |
| --- | --- | --- |
| `git@github.com:vpsfreecz/blog.git` / `blog` | Published `main` baseline `0354dac281978867ea8c1553b092ce19bccb5ccd` | `aeed3a018d895b797e1b8d9b2863dd20c0dec8e0` |
| `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` / `vpsfree-cz-configuration` | Refreshed `origin/master` `5941cdb3dda259e91c6a988a7dbf08c84700b326` | E0 `7bab9781d0a5eb1aed5914f0aed99f6d7d491632`, after DNS successor `b4a7f22a46c16be453052a37ac98fc4c39401a9f` |
| `git@github.com:aither64/vpsfree-cz-workspace.git` / `workspace` | W's local base `c122387075f6109135db2f53845aa77b8cf2838e` | Unchanged W `c3799bb22e7ead2a3738105bad96bfc34d3b8641` |

These exact HEAD/tree identities were read from Git during final binding; owners
report clean final blog/configuration source and yielded indexes. R0 made no
application/index/ref mutations or source-test runs. This is not fresh remote
ancestry or deployed-baseline proof. Local blog `origin/main` remains `0354dac`; configuration
`origin/master` is the refreshed base above. Workspace's retained remote base is
`2b5944e8df2ba06fb3193264c231adafa8329b5c`; its 19 inherited coordination commits
are classified by paths only, without reading or semantically reviewing peer
session records. Preserve unrelated shared work and all feature refs.

### Blog complete final series

The complete `0354dac..aeed3a0` series, in order:

```text
d7b90f09e1edd6fb2b032057205c91d6df5c94ee Import the captured Czech WordPress corpus and public assets
46286f9c7c9e4d1735ac598fa57d9446d1d992ae Preserve the original Flat design around the imported archive
57feaa92ceb6ce7fb96d479bb5b5a823a24cd7fd Align authoring instructions with the imported blog
b16c7f46af7424cf3e8d1fcb0ed8227981b71033 Translate 63 archived articles into English drafts
ea8441f2f3cbd01e105798674caf0c3ce132e580 content: draft 62 English archive translations
f464781e488c66a0f4cf61c50eb4249240ad94a3 Prepare opt-in native discussions for production articles
aeed3a018d895b797e1b8d9b2863dd20c0dec8e0 Prepare checked immutable blog release artifacts
```

Logical split: A1 keeps importer and its deterministically generated public
projection together; V1 owns theme/native rendering and its checks/provenance;
D7 reconciles standalone authoring instructions; T3/T2 are disjoint complete
editorial batches; C0 owns opt-in discussion rendering and its documentation.
Tests/docs supporting each behavior stay with it. E0's artifact workflow,
packager, fixture check and operating docs form the final checkpoint commit.
V1 now includes both bounded V1-L and V2 corrections; no standalone obsolete
correction commit remains in this final series. The following immutable mappings
retain the source/check lineage for independent assessment.

The final diff has 985 files, 23,041 insertions and 117 deletions. Inventory:
125 native Czech HTML bundles, 125 English drafts, 125 historical-comment JSON
files (including empty arrays), 569 byte-preserved uploads, public article/author/
taxonomy/manifest JSON, three `tools/import-wordpress*` files and migration docs;
theme CSS, archive adapter, HTML/RSS/partial layouts, Hugo/i18n configuration,
theme license/notice/four images; `bin/check`; standalone AGENTS/README/authoring
guide/skill; discussion documentation; release workflow, packager, fixture check
and deployment guide. No binary/media contents are dumped here.
The exact reviewer inventory/diff is `git diff --name-status BASE..FINAL` and
`git diff BASE..FINAL` in the named worktree, with the exact table revisions.
E0's eight-file commit adds `.github/workflows/build.yml`, `bin/package-release`,
`bin/check-release` and `docs/deployment.md`, and reconciles the four existing
standalone authoring files.

V1-L obsolete follow-up disposition is already evidenced in
[theme-receipt](theme-receipt.md): old V1 `c2103bcce91d2c93e2d7032c05a92c1375c6693a`
plus correction `0ba7ca99fe3f58150e82421b7a698869c236aa35` became `818202f`;
old D7 `2635a3e6606a555442916ba1f3dc71d948dc39dc` became `e9c286b`, patch ID
`f14abbfde5962d8289f6780e2698b1bdfc5c734a`. Old/new final tree was identical,
`db3cf07edd6924544899fe454d5cc7767cc8d151`. The published baseline and A1 were
unchanged. Preserve this mapping and the earlier baseline preview/review history.
V2 corrected Czech-only taxonomy display labels on English pages through the
existing term-name partial, `i18n/en.toml` and narrow `bin/check` assertions,
without callsite/data/schema changes. Focused checks passed for nine category/32 tag English sidebar
and archive labels, proper-name/source fallback and 125 English article
association labels. Czech production's 1,052 files were byte-identical; 860
preview HTML paths and 252 source/taxonomy/manifest hashes were unchanged.
V2 was committed as `13528a36342b557a61482ac7207d6e5aadc0ac3d` atop
`c4cf0220e313600f568524fc040cd13159669df3`, then folded into unpublished V1.
The final entire tree equals that pre-fold V2 tree:
`11ad8cd6f6ed97ecccad1f2ac7f7e3108663cac7`. All 250 article blobs and working
bytes were preserved. The owner receipt retains the exact mapping and
[range-diff output](v2-history-range-diff.txt):

| Logical commit | Before final fold | Final |
| --- | --- | --- |
| V1 + V1-L | `818202f7b48e8031acb49641360b2402bc4e679b` | `46286f9c7c9e4d1735ac598fa57d9446d1d992ae` |
| D7 | `e9c286b2f403603907265ac28f4bd38b3ae00227` | `57feaa92ceb6ce7fb96d479bb5b5a823a24cd7fd` |
| T3 | `e8aed2ef787217e8085d782e38a760cd51ddbd90` | `b16c7f46af7424cf3e8d1fcb0ed8227981b71033` |
| T2 | `c3786b74af9ee9382af4cc44428e7e77965753ea` | `ea8441f2f3cbd01e105798674caf0c3ce132e580` |
| C0 | `b6b76192c61802c37fbc6cfdc0133c0bec1b3f07` | `f464781e488c66a0f4cf61c50eb4249240ad94a3` |
| E0 | `c4cf0220e313600f568524fc040cd13159669df3` | `aeed3a018d895b797e1b8d9b2863dd20c0dec8e0` |

Published `0354dac` and A1 `d7b90f0` are unchanged. D7/T3/T2/E0 have identical
old/new standard stable patch IDs (recorded in theme-receipt). C0's standard
patch ID changes only because of deterministic check-function placement/context;
its old/new zero-context stable patch ID is identical,
`19bcef87a73a724def31ec22ece35967d41f7266`. The final check file equals the saved
pre-fold version. Do not call C0 literally standard-patch-identical. No merged
history was rewritten. Full final review still covers the actual final series.

### Configuration complete final series and refresh provenance

The complete refreshed configuration series is:

```text
b4a7f22a46c16be453052a37ac98fc4c39401a9f internal-dns: add the blog container address
7bab9781d0a5eb1aed5914f0aed99f6d7d491632 blog: prepare disabled static hosting and release validation
```

The DNS commit changes only `configs/internal-dns/zone.vpsfree.cz.` (+2/-1).
The separate E0 commit changes six files: `int.blog/config.nix` imports the
default-off `static-blog.nix`; configuration owns `tools/blog-static-release.py`,
`tests/blog-static-release.py`, `tests/blog-static-module.nix` and
`docs/operations/blog-static.md`. The owner reports a clean configuration
worktree/index, no WordPress/health/proxy/forum/public-DNS/input changes and no
activation. [release-preparation](release-preparation.md) binds this checkpoint.
The complete final configuration diff is seven paths, 906 insertions and one
deletion. Final tree: `c8e1683212751f52a421cebf4d75cacced0798f6`.

Old independently reviewed range:
`85b38f1cd07d6b3a0fde3eefd32258f747e757e5..133a94b62b3c2161c126fa347cab61ae1b819001`.
Refreshed DNS range:
`5941cdb3dda259e91c6a988a7dbf08c84700b326..b4a7f22a46c16be453052a37ac98fc4c39401a9f`.
[configuration-refresh](configuration-refresh.md) retains the reviewed old ref
`2026-11-06-multilingual-blog-migration-dns-reviewed`, the exact A/TTL/public-CNAME
boundary and payload hash. Predecessor SOA changed `2026093000` → `2026110200`;
feature SOA remains newer at `2026110600`. This is **semantic equivalence, not
literal patch equivalence**. No prior review/build reuse is claimed. In particular,
the old DNS systems in [dns-rollout](dns-rollout.md) do not certify refreshed
configuration or E0. Fresh offline zone parsing for exact `7bab9781` is recorded
below; no fresh full-system build/store or deployed-state evidence is claimed.

### Workspace complete W history

W's own range is one commit:
`c3799bb22e7ead2a3738105bad96bfc34d3b8641 Document the bilingual blog in the workspace project map`.
Only `docs/agent-instructions/projects.md` changes, five inserted lines. The
complete retained remote-base-to-head 20-commit list and final diff counts are in
[w-project-map-review](w-project-map-review.md). Its 19 predecessors change only
`archive/`, `notes/` and `work/` paths. That is path classification, not semantic
peer-record review or permission to rewrite inherited shared-master history.
W's own source/review range stays `c122387..c3799bb`; no extension-repository edit
was made after the user selected the workspace map as the destination.

### Final inventory and complete input-graph bindings

These metadata bindings were read without tests, builds, fetches or ref changes:

| Repository | Final changed-path inventory SHA-256 | Complete `flake.lock` SHA-256 |
| --- | --- | --- |
| Blog (985 paths) | `186e37ea8d20ae3d5b7d4b84618014628af2e98c1830bec9d20183f40c957584` | `865a3c07a35f43f024ce7c01614be82cb795707edac8e27092bdbba42519cd75` (2 nodes) |
| Configuration (7 paths) | `186b27984dd0c1c63d55533791dcb85f10155cbe0f79149f6378d5cf29156c1f` | `9ed71bd9511c7b4e16e0fd9f4de483e0fe4cf54d2556e715392d28e6e60eacd8` (64 nodes) |
| W (1 path) | `b986ee55cfbea619fd48fbe79f2cf2cabf1f4ebe41c711c6bab6eb8839032d9a` | No input change; W is the project-map entry only. |

Inventory digest method: SHA-256 of the newline-terminated stdout of
`git diff --name-only BASE HEAD` with ordinary Git path quoting at the exact
ranges above. It binds names, not contents. The exact source commits/trees and
their committed lockfiles bind content and the complete input graph/follows
edges; do not reduce these graphs to selected pin names. Final artifact metadata,
derivation/system store paths and runtime receipts remain later evidence.

## Migration and dependency-stream inventory

**No application/database migrations** in final A1/V1/V2/D7/T2/T3/C0/E0, refreshed
DNS or W. Historical migration narratives in articles are content, not new
migrations. No schema migration has been merged, released, deployed or externally
consumed by these feature packages. Generated native content schema 1 and planned
release receipt/state formats are persisted contracts for review, not database
migration files. E0 reports no migrations; its new release-state/recovery
contracts are described in release-preparation and the owning operating docs.

No repeated dependency/channel/input bump streams in the final series. The blog
flake inputs remain those of its published baseline; configuration refresh is a
new upstream base, not a feature pin-update stream. No generated metadata update
stream is being retained as redundant history. A1's initial projection and the
separate language batches have distinct ownership and behavior. E0 final pin and
generated-history disposition is confirmed as no migrations/new pin streams in
release-preparation. Its workflow pins existing actions at the verified upstream
revisions below; it does not bump blog/configuration flake inputs. Require the independent
reviewer's explicit complete-series, obsolete-history, migration-lineage and
repeated-stream conclusions; this assembly does not supply those conclusions.

E0's upstream-verified action pins from its owner receipt (source declarations, not a
claim that GitHub Actions ran):

| Action | Verified tag | Pinned commit |
| --- | --- | --- |
| `actions/checkout` | `v7.0.1` | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| `cachix/install-nix-action` | `v31.11.3` | `75c75c31ebece974e48ebc36b4ad125bd97bd97b` |
| `actions/upload-artifact` | `v7.0.2` | `cf430e030ddbb5b0abf93d22962f4752f3646cd9` |

Requested artifact retention is 90 days subject to repository policy. Locally
retained exact archives/releases/receipts, not Actions retention, are the backup
contract. Missing current-SHA artifacts require a trusted exact-source rebuild.

## Ownership, documentation and evidence

- A1 importer/public schema lives in `blog/tools/import-wordpress*`,
  `docs/migration.md` and `data/migration/source-manifest.json`. Consumers are
  the native Hugo templates/adapters, translation source hashes and later
  artifact checks. Private recovery inputs remain outside this packet and Git;
  no private snapshot was accessed for R0.
- V1/C0 rendering and shared discussion identity live in blog layouts/config;
  [theme-receipt](theme-receipt.md) is the owner receipt for visual/media/route
  checks, V1-L history and C0. `docs/discussions.md` owns activation prerequisites;
  actual forum settings are not represented by invented Nix options.
- [T2 evidence](t2-translation-review.md) and
  [T3 evidence](t3-translation-review.md), together with
  [batch IDs](translation-batches.json), bind all 125 drafts. T2 inventory digest
  is `ff6ebefe2f8377ca62796917283ededb2caa54ec29e64a5d2ad9de81665d4ce3`
  (canonical JSON path/hash list); T3 is
  `b522ed1cde36f23be33c456e9cb1d4f02bb3ab52d070651d86ec3b46eb79977b`
  (assigned-order path, TAB, file hash, LF). Their distinct methods are recorded
  in their receipts; do not compare the digest strings as if methods matched.
- D7's root `AGENTS.md`, `docs/authoring.md`,
  `skills/blog-authoring/SKILL.md` and README work from a standalone clone.
  W's site-specific project entry belongs to this workspace.
- E0 interface per D8: blog `cs/`, `en/`, schema-1 metadata and a checked archive
  envelope feed a configuration-owned unprivileged pull/validation/filesystem
  helper. Default-off `static-blog.nix` prepares port 8080 while preserving
  WordPress/port 80. `docs/deployment.md` and configuration
  `docs/operations/blog-static.md` are the owning reusable procedures.
  [release-preparation](release-preparation.md) binds final E0 checkpoint paths,
  local checks and runtime limits. Final artifact/input/store evidence remains
  due after source review; no final deployed graph is claimed.
- [preview-receipt](preview-receipt.md) and
  [b0-scaffold-review](b0-scaffold-review.md) retain earlier baseline history,
  exact artifact and review evidence. They are not final D6/C0/E0 evidence.

## Completed verification, with exact limits

These are owner-reported checks read from current receipts, not new R0 tests.

| Area | Evidence and scope |
| --- | --- |
| A1 public projection | Counts/hash/privacy/text/asset checks and repeat-import determinism passed: 125 articles, six authors, 107 comments/43 replies, 144 attachment records, 569 uploads/50,375,369 bytes. Public manifest SHA-256 `e3c56173acbc2dd018da1d7ce5cd8b73d52e5ef83847a0353b17b107e5a36ab4`; `wptexturize_not_applied` is explicit for every article. See migration docs/manifest and accepted A1 checkpoint. |
| V1 | `nix develop -c bin/check`, native strict renders, real corpus archives/comments/full RSS and 152 locally served asset hashes passed at the recorded checkpoint. Desktop/mobile screenshot and keyboard checks are in the theme receipt. Lead's identity/layout inspection is not user visual acceptance. |
| T2/T3 | Complete source-file hashes, metadata/draft state, structure/code/URL/media/numeric checks and main contextual wording acceptance passed. T3 repaired text-mode CRLF damage from exact source before commit; T2's 31 pre/50 code spans passed raw bytes without repair. All remain drafts with no fabricated human reviewer/date. |
| C0 final 125 | `nix develop -c bin/check` passed at original `b6b76192`, then once again at clean final `aeed3a0`: 125 CS +125 EN, fresh source hashes/dates/taxonomy/media parity, 250 unique paths, 750 route/canonical/paired-link checks over production/dual-loopback/VPN, 54 known-anchor assertions, and an unreviewed notice on all 125 English pages. These draft-inclusive outputs are not a release artifact. |
| C0 embed | Disabled/default/draft/preview and explicit enabled-production synthetic cases passed. Cached Chromium used only `.invalid` fixture origins with every request blocked; neither actual forum behavior nor production embedding was tested. |
| W | Existing agent-instruction tests passed: 10 tests/217 assertions, range whitespace check passed; unchanged five-line feature source was independently reviewed per lead records. |
| Old DNS only | Both `@fqdn@` materializations passed `named-checkzone`, commit hooks passed, and old exact PRG/BRQ system builds passed. These results apply only to the old range and store paths in dns-rollout; they are not refreshed/E0 validation. |
| Refreshed DNS source | Exact `7bab9781` source was separately parsed through two offline BIND 9.20.29 `named-checkzone -D` materializations, PRG and BRQ, both exit 0/serial `2026110600`. Both show `blog.int.vpsfree.cz. 3600 IN A 172.16.8.4` and unchanged `blog.vpsfree.cz. 3600 IN CNAME proxy.vpsfree.cz.`. Tool, source and materialized hashes are in release-preparation. No live DNS/network/build/activation was involved. |
| E0 | `nix develop -c bin/check-release` producer fixture passed; Ruby parsed workflow YAML/read-only permissions/seven steps. Target `python3 tests/blog-static-release.py`: six mocked acquisition/transaction tests passed. Pinned Nix module fixture passed disabled-state identity with hardened WordPress, separate 8080 roots/feed/PHP denial/unknown-host rejection and refused scheduler. Normal Overcommit passed; nonblocking 72-column message warnings remained within 80 columns. No hook bypass. Full details and test boundaries are in release-preparation. |
| V2/final source | Focused label/fallback/association checks and unchanged Czech output/source evidence passed as detailed above. Owner committed/folded V2, proved full-tree equality and all 250 article blobs unchanged, then ran `nix develop -c bin/check` and `nix develop -c bin/check-release` once at clean final `aeed3a0`; both passed. |

Exact already-executed E0 module fixture command, from the configuration worktree:

```sh
nix eval --impure --json --expr 'import ./tests/blog-static-module.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }'
```

Reported results include `disabledEffectiveStateIdentical=true`,
`existingWordpressPreserved=true`, `scheduledActivationRefused=true`,
`newListenerPorts=[8080]`, correct CS/EN roots/feed and
`phpDenied=true`/`unknownHostRejected=true`. These are local evaluation/fixture
results, not service/target validation. Refreshed DNS source SHA-256 is
`f0287f6c9d8950e286155451d15d6724b0018a1967327272ee4da2c705b54087`;
PRG/BRQ materialized hashes and the exact tool path remain in the linked receipt.

Whitespace is **not** a blanket pass or hook waiver. The 519 locations comprise:
A1's 322 intentionally preserved original Czech HTML/code/prose/CRLF locations,
T3's 43 raw source-identical protected-code locations, and T2's 154 raw
source-identical protected-code locations. Only the translation diagnostics are
classified here as protected code; that description does not apply to all 519.
T2's 25 CRLF pre spans and 154 line diagnostics are different counts; T3's
restored spans and per-file diagnostics are in its receipt. New unprotected EOF
blank lines were removed before the translation commits. Reviewer must preserve
byte/source fidelity rather than normalize code to silence checks.

## Compatibility, recovery and unresolved runtime gates

Czech permalink/more/comment anchors, original feed GUIDs
`https://blog.vpsfree.cz/?p=<id>` with `isPermaLink=false`, dates, author/taxonomy
slugs and legacy upload bytes are public contracts. English has independent
root paths and stable URNs, but shares the original Czech discussion URL.
Render-time correction of known English links does not rewrite protected source.
Preview enables drafts with a human-review notice; normal production excludes them.

Native HTML trust is bounded by A1 sanitization and finite allowed iframe hosts;
Goldmark remains unsafe=false. Approved historical comments retain original
language and threading, with no local posting form or commenter account creation.
Default-off Discourse rendering neither proves the installed forum's behavior
nor authorizes configuration. Dedicated category/permissions, source-path
allowlist, extraction/redirect behavior, duplicate-free shared topics, notification
effects, `.org` framing and top-level login/reply tests remain later gates.

E0 must preserve existing hardened WordPress80/DB/PHP/cron and proxy header/network
rules. The source-only listener is a separate default-off 8080 candidate; no
public proxy/TLS/.org DNS transition is included. Artifact eligibility, safe
extraction, full hashes, stale-run rejection, cached immutable assets,
pointer/receipt interruption reconciliation and retained-release rollback require
final source/local-fixture evidence. Missing/expired eligible artifacts must not
fall back to an older SHA or build on the production VPS.

E0's checkpoint/local tests bind the reported production pull/activation/rollback
CLI refusal (`machine-admission-unavailable`) and failed timer-enable assertion.
A filesystem lock is not machine-coordinator ownership.
Automatic activation cannot be released until authoritative admission, branch
protection, trusted workflow identity, artifact-read credentials/outbound route,
retained backup and recoverable WordPress state are established.

Before any eventual transition: approved public `.org` DNS/TLS/proxy setup,
manifest query/alias handling, actual deployed baseline/profile paths, original
recovery prerequisites and a brief source delta check remain due. Content release
rollback and system generation rollback are separate. Retain current/previous
archives, immutable assets and receipts. Initial serving rollback returns proxy
traffic to preserved WordPress80; new static articles and Discourse replies still
need reconciliation, never forum database rollback or topic deletion. Removing an
activated DNS record requires a serial above all published serials.

The earlier immutable artifact in preview-receipt certifies `0354dac` only.
The current registered real preview `621e26d1-801f-4fbf-b1b7-72441fab0fe3` runs
`nix develop -c bin/preview --vpn` from a changing source tree. It is not proof
of a clean final artifact, final input graph or a separate VPN client's path.
After final source/review, the lead owns exact final artifact/build metadata,
store paths and authorized preview usability verification. No CI success or
production activation is claimed here.

## Completion and next gates

- [x] E0 source/local checks and coherent blog/configuration commits complete;
  final blog `aeed3a0`, configuration `7bab9781`, W `c3799bb` are bound.
- [x] V2 correction/checks/fold complete; both rounds of old/new mappings and
  tree/patch evidence retained, including C0 context-only and DNS semantic-only
  equivalence distinctions. Earlier immutable receipts remain unchanged.
- [x] Complete final series, diff inventories/graphs, owner quick results,
  source completion/cleanliness reports and runtime/recovery limits assembled.
  No R0 application/index/ref mutation, source test or build was performed.
- [ ] Lead checks packet completeness and current reviewer independence/settings,
  invokes reviewer0 with all four lanes, and records findings/reconciliation.
- [ ] After review, final artifact/runtime checks use exact final source/input
  identities. No merge, default advance, DNS activation or production transition
  occurs without separate explicit user direction.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.

## Post-review extension: V3-R and verification state

This addendum preserves all reviewed ranges, history mappings and the independent
report above. The lead reports reviewer0 completed the high-risk, four-lane
review without findings, including explicit complete-history/no-migrations/
no-repeated-stream conclusions. The following is the lead-accepted narrow
post-review correction, not a renewed independent-review invocation.

- Repair commit: `3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb`.
  Parent: `aeed3a018d895b797e1b8d9b2863dd20c0dec8e0`.
  Tree: `b5cc92ab3976a1edef6a945dd0e6e5b0f0c022c7`.
  Exactly `bin/preview` and `bin/check`, 57 additions/four deletions.
- V3 observed the real VPN English output serving a `localhost:1314` canonical
  and old labels despite clean `aeed3a0` source. The protected published `0354dac`
  runner's shared publish directory was the underlying boundary. Keep one
  coherent repair commit above the seven accepted feature commits; do not rewrite
  that protected baseline or perform a redundant rebase.
- The lead inspected the complete focused diff and accepted it under mandatory
  review workflow steps 9/10. Source-isolation regression and normal `bin/check`
  passed. This targets real `--vpn` content, not the fixture preview. No production
  contract, design, article/data content, input pin or migration changed.
- The corrected-source, retained/rooted artifact build passed using the known
  cached quick command in a non-login parent shell. Candidate:
  `/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0`, retained by the
  blog worktree's `result` link. Owner0 completed the immutable proof and the
  lead accepted it: all 1,655 served-file hashes, 125 Czech article routes,
  107 comment anchors, 1,138 upload copies and ten exact full-content Czech RSS
  items passed. All 125 English drafts are excluded, with zero English feed
  items; canonicals on all 430 Czech and 22 English HTML pages are correct,
  and scripts/forum frames are absent. This proves the local immutable artifact,
  not actual HTTP/browser delivery or an eligible GitHub release artifact.
  [release-preparation](release-preparation.md) retains the exact source/NAR,
  derivation, Nixpkgs path, complete two-node input graph and file evidence.
  The earlier
  unrooted `aeed3a0` artifact disappeared before full verification and remains
  superseded/incomplete, not an established content failure.
- Configuration stays at `7bab9781d0a5eb1aed5914f0aed99f6d7d491632`. The lead
  accepted its disabled-system build/receipt integrity: generation
  `2026-11-07--00-29-17`, receipt SHA-256
  `829923f159788d7b46a6a90e9abf3f0f8e13bf144b5e3fc94086f5775bcac96f`,
  toplevel
  `/nix/store/pa6j6jvzf8ic3z7bqvzskdgmk2b7mk0z-nixos-system-blog-26.05.20261026.718f670`.
  The build command exited 0; outer-shell exit 127 is separately reconciled
  `bash_logout` bookkeeping, not build failure. Full source/materialization,
  derivation, 64-node graph and effective inputs are in release-preparation.
  No rebuild, deployment or active system/profile claim follows from this receipt.

Owner1 retains the narrow repair of registered VPN service
`621e26d1-801f-4fbf-b1b7-72441fab0fe3` and subsequent HTTP/browser verification;
those results remain pending at this addendum. Follow the latest
[theme receipt](theme-receipt.md) for exact runtime/source and usability evidence.
Do not extend the earlier runtime success to the corrected final source without
that proof. Publication remains paused. Human editorial approval, CI/push/default
updates, DNS activation and production transition are not claimed or authorized.
R0 performed only this factual record extension, with no new application/index/
ref/test/build/service or review work.

## Final verification addendum: publication, CI and V3 usability

This records subsequent verification and supersedes the pending publication,
CI and V3 runtime statements above. The independently reviewed ranges, original
report and accepted narrow-fix mapping remain unchanged.

Owner0's [publication receipt](release-preparation.md#final-verified-feature-publication)
records the original blog SSH push exiting 0, with no retry: feature branch
`2026-11-06-multilingual-blog-migration` advanced normally from `0354dac` to
`3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb`. Immediate canonical remote proof
confirmed that feature SHA and unchanged `main`/HEAD at
`0354dac281978867ea8c1553b092ce19bccb5ccd`. Configuration's feature was also
published at `7bab9781d0a5eb1aed5914f0aed99f6d7d491632` using the exact old
`133a94b6` lease; `master`/HEAD stayed at
`5941cdb3dda259e91c6a988a7dbf08c84700b326`, and the old reviewed DNS ref was
retained. Its declared Daily update workflow has manual/schedule events, with
no push trigger. Publication did not integrate either feature.

The exact blog **Build blog** workflow completed successfully:

| Field | Observed value |
| --- | --- |
| Run | [42314975595](https://github.com/vpsfreecz/blog/actions/runs/42314975595), attempt 1 |
| Head | `3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb` |
| Event / branch | `push` / `2026-11-06-multilingual-blog-migration` |
| Status / conclusion | `completed` / `success` |
| Run timestamps | Created/started `2026-11-06T23:55:09Z`; final update `2026-11-06T23:55:56Z` |
| Job | [build, 128225246070](https://github.com/vpsfreecz/blog/actions/runs/42314975595/job/128225246070), success; `23:55:12Z`–`23:55:55Z` |
| Passed commands | `nix develop -c bin/check`; `nix develop -c bin/check-release`; `nix build .#site` |
| Trusted-main steps | `Package trusted main build` and `actions/upload-artifact` both **skipped** |

The feature ref makes the trusted-main guards false. This run supplies check
and build evidence; it supplies no eligible main-release artifact or proof of
branch protection or credential provisioning. Final run/job/step metadata came
from `gh run view 42314975595 --repo vpsfreecz/blog --json ...`.
A fresh pinned Luna/low operation watcher ran
`gh run watch 42314975595 --repo vpsfreecz/blog --exit-status` and returned 0;
the run was already complete when watched. Its execution policy was
`danger-full-access`/`never`, with retained utility catalog
`a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958`.
Transient watch output is
`/tmp/vpsfree-blog-ci-42314975595-implementer2-watch.log`. No watch remains
running, and no retry or cancellation occurred.

Owner1's [final V3 receipt](theme-receipt.md#v3-final-vpn-usability-and-v3-r-correction)
binds the same clean `3aec4d6b` source/tree to real preview service
`1c3a8df4-d6f2-4245-9fe7-1f3714e8568d`, command
`/run/current-system/sw/bin/nix develop -c bin/preview --vpn`, on
`172.16.106.40:4567`. The lead accepted `bin/check --real-vpn`, eight HTTP
endpoints returning 200 without redirects, and eight desktop/mobile browser
views. Canonicals/pairs, localized labels, draft notice, keyboard navigation,
contained code scrolling and representative media hashes passed; no localhost
leak, document overflow, broken local images or active Discourse was found.
Off-origin browser requests were intercepted. This proves local VPN-listener
usability, not access from a separate VPN client or actual forum behavior.

The accepted retained production artifact remains
`/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0` at exact
`3aec4d6b`, with all 1,655 file hashes and the route/feed/content proofs above;
its complete source/input identity is in [release-preparation](release-preparation.md).
The accepted exact `7bab9781` disabled-system receipt is unchanged. Neither was
rebuilt for this CI package.

Implementer2 changed only this verification record and observed exact feature
CI. No application/index/ref/default/service mutation or source test occurred.
Human translation review, eligible trusted-main artifacts, authoritative machine
admission and all production transition gates remain outstanding. CI and local
usability grant no merge, DNS activation or production authorization. Registered
previews, feature/recovery refs, retained artifact and session remain available.
