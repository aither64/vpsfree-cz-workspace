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


## D9 user refinement — final committed review packet

The user requested centered pagination and article images/tables, an English
registration graphic and vpsfree.org links, and a contextual repetition audit of
all English articles. Search was a question only: a static browser index such
as Pagefind was explained; search remains disabled, no dependency or code added.
The architect-owned [D9 brief](design.md#d9-sufficient-briefs-alignment-english-cta-and-prose-audit)
settles scope. No merge/default update, production transition, service replacement
or forum request is authorized.

Final blog head `f0337fb7eae8797efca9254cd7208949cb0f77e4`, tree
`b80d2261d92efe01c51946f97fec5cd45b32b0fe`, clean index/worktree at lead check.
Complete range remains `0354dac281978867ea8c1553b092ce19bccb5ccd..f0337fb7eae8797efca9254cd7208949cb0f77e4`.
The eight prior coherent commits and earlier review/3aec narrow-fix evidence above
remain intact. Three additional independent commits implement this user follow-up:

- `3dff9d7dbf61d7bf7c76e10fd72929711cd2bbf7`: centered pagination/block
  media/tables and localized CTA/footer; five files,53 additions/2 deletions.
- `d6c673c9e6addc8cf4f32f10cd653d8a632f0ddb`:13 existing T3 English articles,
 14 prose lines revised after complete63-article/source-context audit.
- `f0337fb7eae8797efca9254cd7208949cb0f77e4`:14 existing T2 English articles,
 15 prose lines revised after complete62-article/source-context audit.

The incremental diff is32paths,+82/-31. Complete final range has11commits,
987paths,+23,149/-121; newline-separated git diff --name-only inventory SHA256
`b2a317e0a9c4fc577cc6051c9c2da2973ee96286f899d7efd39ddc9c04c7ca98`. The lead read all27 affected full English
bodies and relevant Czech source context and accepted exact wording with three
small refinements. All125 source hashes/drafts/no-human-review fields remain;
raw code/CRLF, metadata, HTML structure/comments/attributes, URLs/media and every
Czech byte are protected. Approved repeated numeric-token removal is classified
explicitly; it is not falsely described as identical numeric sequences. Complete
editor proposals/decisions/checks are in [T2](t2-translation-review.md) and
[T3](t3-translation-review.md); UI source/CTA visual acceptance is in
[theme receipt](theme-receipt.md). All98 other EN drafts are unchanged.

There are no new migrations, persisted formats, APIs or dependency/pin/generated
update streams in this follow-up. Original prior feature contracts and no-migration
provenance above remain applicable. New commits retain separate UI and disjoint
editorial purposes; no superseded new approach/fixup exists. Independent whole
series/history/consolidation conclusions are requested, not assumed from prior
approval. Configuration7bab and workspace ownW remain unchanged from their
accepted complete ranges above; no extra system build is needed for this UI work.

Source checks and whitespace checks for the incremental32paths pass. Existing
full-range519 imported/translated whitespace classifications remain scoped above;
no normalization or hook bypass. UI source normal bin/check passed before commit;
final clean-head combined quickcheck report follows before reviewer dispatch.
No longer integration/build/browser verification is claimed yet for this head.
Older3aec artifact/CI/runtime proofs remain historical supporting evidence.

Review selection: retained independent reviewer0, Sol/xhigh/read_only, unchanged
thread01a1b293-016d-7f41-95f0-b2c1da14ee3e, verified in live same-session roster.
Overall whole branch remains HIGH risk due to artifact/configuration contracts;
all four lanes apply with retained unchanged-source evidence reusable within its
stated boundary. Reviewer must inspect complete actual series/final diff and new
UI/editorial work directly; no nested agents. Source review precedes rooted final
artifact and bounded actual desktop/mobile verification. Actual human translation
approval, external VPN-client route, eligible-main artifact, machine admission,
forum behavior and every production transition gate remain outstanding.


D9 final quick gate: implementer1 reports `nix develop -c bin/check` and
`nix develop -c bin/check-release` PASS at exact cleanf0337fb/treeb80d2261,
unchanged before/after, one offline packager test0.157s. Source/protected parity
and incremental diff-check PASS as above. All intended deliverables committed;
mandatory final review is now released before longer build/browser verification.


### D9 independent final review result

Retained reviewer0 (thread `01a1b293-016d-7f41-95f0-b2c1da14ee3e`,
`gpt-6.1-sol`/xhigh/read_only) independently reviewed the exact final coordinates
above across all four lanes at HIGH overall risk: **no findings**. The report
verifies all125 draft/source-hash fields, all27 changed prose/HTML/protected-byte
boundaries, unchanged Czech bytes and98 other ENfiles, original/derived CTA
identity, intended UI source behavior and complete11-commit history. Explicit
conclusions: no obsolete history/fixups/transitional approaches, further
consolidation, repeated pin/update streams or migrations remain. Existing config
and ownW ranges are unchanged; their previous scoped reviews stand. Prior
reviewed heads remain literal ancestors. Full report is retained in the reviewer's
same-session turn; no report-file write or source mutation by reviewer.

Lead accepted this source gate and released one rooted final artifact build and
the bounded actual UI browser batch. No merge/deployment approval is implied;
artifact/browser/CI for this head still need their actual results.


### D9 exact rooted artifact accepted

Owner0's [release receipt](release-preparation.md) binds clean f0337fb/treeb80d2261
to `/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0` via retained
`result-d9`, derivation `y8z3p3j4apfsqjxd378ahxp8an70hi9s-vpsfree-blog-0.drv`.
Fresh pinned Luna/low watcher `/root/r9_build_watcher` completed the single build
in7.009s, exit0, exact clean pre/post source; no operation remains. Source
`/nix/store/l0bhsk62mndhki3n0pmidsfn5mnpa79x-source` has NAR
`sha256-7ysSUzHR0QGxgX/ZfwUwcrSUSTflHCz6pJ6ws7ZDbzQ=`. Complete unchanged
2-node input graph, effective Nixpkgs store/NAR, all1657 served hashes,125CS
routes/source hashes,107 comment anchors/125 more anchors,1138 upload copies,
430CS+22EN canonical pages and10 fullCS feed item GUID/date/content checks pass.
All125EN drafts remain source-fresh and excluded; ENfeed0. Script/Discourse
frames absent. Original3aec result remains rooted too. Config7bab system proof
is unchanged; no repeated system build or eligible-main CI artifact is claimed.
Lead read the receipt and accepted its completeness/scope. Actual UI/browser and
feature publication/CI remain pending; prior source review remains unchanged.


### D9 actual UI verification accepted

Owner1's [U9 final receipt](theme-receipt.md) binds the same clean f0337fb source
and existing service `1c3a8df4-d6f2-4245-9fe7-1f3714e8568d` to one fresh pinned
Luna/low browser operation,11 views in14.074s, exit0. Desktop1440/mobile390
pagination rows are centered; wp841's275x157 linked image centers and its revised
opening is served. wp367's454px desktop table centers, mobile width stays330px;
wp847 at320px has401px contents in260px table area, and focused Right Arrow
scrolls40px internally. Table/header/cell semantics remain intact. Existing20px
emoji remains inline; bounded browser-only inline/float probes pass. Bilingual
native150x147 CTA/alt/registration/footer/logo/focus/drawer checks pass.
Zero broken images, document overflow, failed local responses or Discourse;
off-origin interception was installed before navigation, no external requests
occurred. No service or source mutation occurred. Lead visually inspected actual
pagination, image, table and narrow320 screenshots and accepted usability.
Separate external VPN-client access and human translation approval remain unproven.

Both artifact and UI gates accepted; lead released exact feature-only publication
and new exact-commit CI. No default advance, production action or lifecycle change
is authorized. Original artifact roots, previews and session are retained.


### D9 feature publication and final CI accepted

Owner0's final release receipt records canonical SSH normal fast-forward publication
from3aec to exact `f0337fb7eae8797efca9254cd7208949cb0f77e4`, exit0/no retry.
Fresh before/after remote proof binds the feature and unchanged main/HEAD at0354.
Config7bab/W remain unchanged. Explicit portal comparison now binds0354..f033.
Lead rechecked final source/tree/clean index and read the complete result scope.

[Build blog run42360486251](https://github.com/vpsfreecz/blog/actions/runs/42360486251)
succeeded at exact f033, push feature event. Job128367627432 passed bin/check,
bin/check-release and Nix build. Trusted-main packaging/upload both skipped;
artifact count0, as required. One fresh pinned Luna/low standalone watcher with
full-access/never owned exact run watch (`--interval 15`); watch/utility exited0,
run already terminal,
no rerun/cancellation/duplicate parent polling. Both build/CI utilities finished.
Detailed job/step/evidence hashes are in release-preparation.md. No new source,
index, history, pin, service, default, production or lifecycle mutation followed.

Requested D9 follow-up is accepted and delivered. Prior independent review and
its whole-history/no-migration conclusions remain bound to this exact head.
All125 EN translations remain drafts pending actual human meaning/voice review.
No eligible-main release, production readiness, machine admission or transition
approval is implied. Previews, original/new artifact roots, refs and session stay
open; integration and public transition retain their separate explicit user gates.


## D10/D11 user follow-up — new source gate pending

The user approved Pagefind, requested a left-side small-screen sidebar control,
then distinct current/usable/disabled pagination states and English equivalents
for blog/KB destinations. Prior D9 review/build/browser/CI proofs remain scoped
to f033; they do not certify this follow-up. Current source commits are U10
`c829fbf4abcd7f7ab47b44386b3d12ec39090b55` and S10
`95a3cae2a1185c096968357e558ee15ad5a2a7f8`. U10's unpublished predecessor957
was amended, preserving its sidebar correction; no published history changed.
S10 introduces Pagefind1.5.2 through the existing locked Nixpkgs, article-only
local language-aware search, indexed files before complete metadata hashing,
localized accessible UI and coherent snapshot previews. Main accepted actual
CS/EN copy and authoring/deployment explanations. Quick normal/release checks
passed; actual artifact/browser/server behavior remains pending. No lockfile,
workflow, configuration, article/prose/code/draft-state change exists here.

D11's exact source inventory [L11-I](language-link-review.md) covers531 hrefs:
55 blog-article occurrences,70 KB,75 media, two taxonomy, two self-fragments,
326 external and one mailto. All original source targets remain identical.
The accepted [KB evidence](kb-link-review.md) and [candidate map](kb-link-map.json)
identify23 pages/nine section pairs, including observed root alias and actual
language-switch authority. Map SHA256
`5b3fee0f5b6ffcf4b80ecedd6fce3967ddc23482e05ec3cf901f14b55a6f1b17`.
Expected52 KB occurrences localize;18 remain exact originals because three source
pages are missing, four historical fragments lack verified counterparts, or the
English-host infrastructure page still contains identical Czech prose. This
finite fallback is explicit; no English destination/anchor is guessed and no KB
repair/translation is authorized. Renderer source is pending final commit/check
at this checkpoint. See architect-owned sufficient D10/D11 briefs in design.md.

All intended source must be committed and quick checks pass before retained
reviewer0's new final assignment. Final rooted result-d10, actual browser/snapshot
and feature-only CI gates then follow. Existing roots/previews/defaults remain;
no merge or production transition is authorized. Config7bab/W remain unchanged.


### D10/D11 complete final source packet

All intended follow-up source is committed at
`b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d`, tree
`15e46f8e619f60c82c07a612ec8360a4a1f286a6`, clean working tree/index.
Full blog range `0354dac281978867ea8c1553b092ce19bccb5ccd..b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d`
has14 commits/997paths,+23,916/-134. New f033..b29 range has three coherent
commits/22paths,+823/-69: U10 navigation c829fbf, S10 search95a3cae, L11 linksb29f21b.
Newline-separated complete git diff --name-only inventory SHA256:
`fe97991c4983eb6c9661396f282ed32410503521e82bd5b9430ffcc62f9df635`.
Prior published source and exact reviewed f033 remain literal ancestors;
U10's unpublished957 amendment is documented, with original sidebar patch retained.
No new obsolete/fixup history, migrations or repeated dependency/pin streams are
proposed; independent whole-series conclusions are required. Pagefind1.5.2 is a
new build dependency selected from the same pinned Nixpkgs, not a lock refresh.
Complete2-node blog lock,64-node config and35-node workspace graphs are unchanged.
Config5941..7bab and ownWc122..c379 remain exact unchanged accepted ranges above.

Owner2 reports final normal bin/check and bin/check-release PASS (60s/1s fresh
pinned Luna/low), all search assertions retained. First release invocation's stray
trailing dot was an inspected unittest-selector error; corrected exact command
passed, with no product fix/retry fiction. An independent final source inspection
then tightened attribute tokenization so href-like text inside other attributes
cannot be rewritten; the final normal/release batch passed after this change.
The earlier S10 dependency watcher's second pure version invocation/logging error
is also recorded in release-preparation; successful dependency realization stands,
no process remains and no repeated build result is invented. Incremental
whitespace checks pass; historic519 source-whitespace classifications remain scoped.

L11 commit owns five files: existing HTML partial, one52-line link partial,
accepted finiteKBdata, link checks and main-accepted concise authoring note.
Real dual/VPN proofs reconcile all55 blog links to rendered EN routes and all70KB
occurrences to52 mapped/18 explicit fallback. All1,055 Czech output files are
byte-identical in the three-mode comparison; production HTML has zero D11 changes,
preview/VPN has62 href-only HTML changes. All250 original article bytes/hashes,
sourceURLs/code/metadata/draftstate, KBmapSHA and unrelated destinations remain.
Published/absent/draft targets, query/entity/quote/protected/legacy exceptions and
shared content/summary/RSS paths are covered by focused checks. See existing
language-link-review.md for exact commit/inventory/check receipt when finalized.

Risk remains HIGH for the complete branch's artifact/release/runtime contracts;
all four review lanes apply, using retained reviewer0 Sol/xhigh/read_only and no
nested agents. Main accepted exact UI/authoring/deployment copy and map evidence;
reviewer independently assesses source correctness, search language/privacy and
recovery boundaries, link authority/fallback and complete history. Bounded
read-only spotchecks of mapped KB pages are permitted if useful; no current
WordPress/forum/API writes or unrelated crawl. Prior unchanged-source review is
reused only within its stated scope. No actual final-head Nix/browser/service/CI
proof is claimed before this gate.

Post-review plan: one rooted build to result-d10 (preserving older roots), then
exact current VPN registration1c-only replacement to load coherent search
snapshot; bounded actual mobile/search/link browser and copy-only edit/add/remove
snapshot proof via registered localhost4568 fixture. Existingb093 remains untouched.
All service/copy mutations stay parent-owned; watcher utility observes/executes
only assigned verification without service authority. Final fixture/preview stay
open. Feature-only publication/CI follows accepted artifact and usability. No
merge/default update, configuration rebuild, production transition or lifecycle
cleanup is authorized.


Reviewer environment exception during D10/D11: an intended quick offline Nix
version read unexpectedly attempted missing pagefind-extended1.5.2 dependency
realization and exited1 before the version command ran. Reviewer requested
interruption when build output appeared; the cell had already completed and no
matching process remained. No source/ref/service mutation or success claim;
no retry/long check. Source review continues using the retained generated loader
and scoped owner evidence. Actual exact-head R10 rooted build after review must
establish the complete dependency closure; this exception does not waive it.


### D10/D11 independent final review accepted

Reviewer0 (retained thread01a1b293-016d-7f41-95f0-b2c1da14ee3e,
Sol/xhigh/read_only) independently reviewed the exact b29/tree15e46f8 complete
14-commit/997-path range across all four lanes at HIGH risk: **no findings**.
Actual source diffs, map byte identity,250 article bytes/drafts/source freshness,
query/attribute/protected boundaries and scoped prior ranges were checked.
Bounded public users-page counterpart/section spotchecks independently confirmed
the corresponding English page and two mapped anchors. Explicit history result:
no obsolete approaches/fixups/transitional shims/further consolidation, repeated
pin/update streams or migrations; prior published f033 is a literal ancestor.
Config7bab/W remain exact unchanged accepted ranges. No long build/browser or
runtime success is inferred; the reported offline dependency exception remains
scoped above. Full review report is retained in the same-session reviewer turn.

Lead accepted the source gate and released R10 rooted exact-head build first,
then parent-owned targeted replacement of only current real preview1c, plus one
isolated archived-copy fixture on127.0.0.1:4568 and its necessary rebuild steps.
Existingb093, old results/outputs and final services/session remain open. Browser
checks follow the one watcher slot after rooted build. Feature publication stays
held until immutable artifact and actual usability acceptance. No merge, current
WordPress, configuration deployment or session lifecycle action is authorized.


### R10 final rooted artifact accepted

The single fresh pinned Luna/low build passed11.6675s at exact clean b29/tree15e46f8;
`result-d10` retains `/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0`,
derivation `/nix/store/r76d4ynzyaqvnimxjhqzq9xqmmicspfl-vpsfree-blog-0.drv`.
Source `/nix/store/4r6isvxjd4nzw83jhv6nnwffdj73sqar-source`, NAR
`sha256-GDdMKj0YdD1xjAVftjHTpkaKI8vggozAsCie4sEXwyQ=`, complete unchanged
2-node lock/effective Nixpkgs and all three native build-input store/NAR identities
are bound in [release-preparation](release-preparation.md). The actual pinned
`/nix/store/zwbwi2iqisisr5190lc3nyxb0fpdmzvw-pagefind-extended-1.5.2/bin/pagefind`
reports1.5.2, consistent with metadata and the derivation. This establishes the
new native package proof; the reviewer's failed offline version read is not reused.

All1802 served digests/exact inventory pass, including141 Pagefind files.
Native entry languagecs-cz has125 pages/version1.5.2; English has no bundle and
explicit empty search state. Both canonical search pages/forms/local hashed
module+SRI are correct; scripts occur only on the two local search pages, no forum
frames. All125 Czech routes/raw source hashes/manifest bytes,107 comment and125
more anchors,1138 upload copies,431CS+23EN HTML canonicals and10 fullCSfeed
GUID/date/link/content matches pass. All125EN drafts are fresh/excluded; ENfeed0.
Older result/result-d9 remain rooted. No unchanged configuration rebuild occurred.
Lead read and accepted the complete receipt. Actual browser/native queries and
snapshot/keyboard/link usability remain pending; feature publication stays held.


Runtime setup exceptions before browser execution: first archived-copy fixture
failed Nix implicit flake resolution before Hugo; explicit reviewed original-flake
devshell with copy CWD produced a running HTTP200 fixture. A subsequent parent
browser wrapper repeated implicit resolution from tracking CWD; owner stopped its
exact Nix PID before Node/driver start. Observer exited1 and finished; no fixtureB
or browser assertion ran. Both failures are scoped launch/environment mistakes,
not product findings or tests that passed. Original logs/exit states are retained.
One explicit-path correction/fresh observer is released; no product-source change,
review rerun, artifact rebuild or repeated source check is warranted. Actual
browser proof remains pending and feature publication is held.


First actual browser attempt began after explicit-flake launch correction. It
passed seven desktop/mobile pagination/navigation views, then stopped on a test
expecting checkbox rectx4. Diagnostic JSON/screenshot shows CSSleft4 plus native
UA margin4 gives rectx8..38, contained inside the visible controlx0..40. The
product placement is correct. Lead accepted the evidence and corrected the
helper criterion to containment plus actual Tab/Space/pointer behavior; no app
change or source/build/review repeat. The remaining runtime flows continue only;
passed exact-b29 evidence and original failure/diagnostic logs are retained.


Runtime no-match diagnostic: after passed navigation/positive CS/blank-query
checks, alphanumeric sentinel u10nomatchzzqx returned47 in both native Pagefind
API and UI, with excerpts highlighting the common Czech letter u. List clearing
and loading were observed; this is not stale adapter state or wrong-form timing.
Engine internals were not independently inferred. The alphanumeric sentinel did
not measure absent-word behavior; lead accepted all-letter negative/fixture
markers with native/API/UI zero required, without a custom query parser or
Pagefind conformance expansion. Any necessary reindexed baseline alters only the
archived fixture. Prior logs/diagnostics stay recorded. No product source,
review/artifact change or pass claim follows from the invalid sentinel alone.


Coordination update: after reviewed b29 and complete immutable artifact acceptance,
lead releases feature-only publication/CI in parallel with the remaining bounded
browser checks. The previous serial publication gate was a lead sequencing choice,
not user integration/production authority. Runtime stops so far are demonstrated
harness/environment or invalid test-token cases, with no source change. Completion
still requires actual runtime success and exact-head CI; no readiness is inferred
from publication. Parent browser fallback consumes no watcher slot; owners must
confirm the single utility slot before CI monitoring. No repository claim is held.


### U10/S10/L11 actual runtime accepted

Exact cleanb29/tree15e46f8 and all250 article/data hashes remained unchanged.
Twelve desktop1440/mobile390/320 pagination/toggle views plus the remaining
29.611s browser driver passed. Native CS/EN KeePassXC search selects the correct
language and root841 article; blank clearing and all-letter absent-word API/UI0,
VPS10-to20 More, forced fragment-load error/clear/reload recovery, no-JS and
English production empty state with zero Pagefind fetches pass. Fixture title/body
inclusion and nav/comment exclusion are proved with all-letter markers. While
archived source edits/additions/removals occur, snapshotA HTML/index stay old;
fresh snapshotB and SAME-tab reload show changed/added and remove old/deleted,
including404 for the removed route. English blog/KB representative attributes
match the accepted map; unknown#cli remains Czech. No external KB/forum link
was opened. Three approved historical YouTube requests were intercepted/aborted
before network; zero external network, Discourse, overflow, broken images or
unexpected console errors. Intentional failure diagnostics stay recorded above.

New real VPN service `8990b341-2956-4c6c-a2d8-8bf314c98d7d` serves exact current
snapshot on172.16.106.40:4567, destination
`/tmp/nix-shell.NRFxdd/vpsfree-blog-vpn.iR0OzDO6`. Final isolated fixture service
`d2293739-8904-46b0-ba1a-2045ff019d5d` serves127.0.0.1:4568 from archived copy
`/tmp/blog-u10-fixture.iclgei_p`, output`/tmp/blog-u10-snapshot.0xY7SWgL`.
Only owned baseline registrations were stopped for necessary refresh; b093 and
older results/outputs are preserved. Parent fallback was explicitly visible when
a fresh monitor interface was unavailable; no substituted model or service
mutation by a watcher. All final services/session remain open.

Lead read theme-reference/u10-runtime-result.json, rechecked final cleanGit and
visually inspected actual320pagination,390drawer,EN/CSsearch andproduction-empty
captures. Runtime is accepted; source review/artifact remain valid with no product
source fix or new review needed. External VPN-client path, human translation
approval and production transition remain separate. Exact feature publication
b29/main0354 and comparison are accepted; finalCI42370490884 is now the last gate.


### R10 final publication/CI accepted — requested follow-up delivered

Canonical SSH feature push f033->b29 completed normally, exit0/no retry/lease/rebase.
Fresh before/after remote proof preserves main/HEAD at0354 and exact published
b29/tree15e46f8; portal comparison binds0354..b29. Other repositories were not
pushed or rebuilt. Exact [Build blog42370490884](https://github.com/vpsfreecz/blog/actions/runs/42370490884)
completed SUCCESS; job128397434394 passed normal/release checks and Nix build,
protected-main packaging/upload skipped, artifact count0. One fresh pinned Luna/low
watcher ran the exact watch command with `--interval 15`,
watch/utility exit0 (already terminal), no CI retries/cancel/parent duplicatepoll.
Its single slot was coordinated after the browser's explicit parent fallback.
All watcher operations are finished. Detailed metadata/evidence hashes are in
release-preparation.md; lead read the final receipt and rechecked clean b29/tree.

Source review, immutable1802-file/native-input proof, actual browser/snapshot/link
usability and exact-head CI are accepted for the requested feature. No product
source changed after review. Human English review, external client route and all
production/admission/forum/cutover gates remain separate; no default update or
merge approval is inferred. Real8990 and fixtureBd229, b093, all original/new roots,
refs and the active session remain open. No lifecycle/cleanup action is requested.


## D12 user correction — source work in progress

User reports wp490's CLI link still Czech, requests semantic reevaluation of all18
KB fallback occurrences, and reports clipped nested scrolling in mobile sidebar.
D11's old-source-anchor rejection was too strict. K12 now examines all8targets/
18contexts, including all9CLI occurrences, and verifies current English content/
IDs/navigation. Main read and accepted candidate SHA256
`c869a107479cb980b2473eb54250686772dc363c87a2af6afdf0f7d99abd2cbe`:
26pages/10same-page fragments/two explicit cross-page fragment_targets;15new matches,
cumulative67/70KB occurrences. The remaining bouncer1/OpenVZ2 lack equivalent
current English documentation after targeted searches and content comparisons;
no unrelated LXC/rescue/archive-bot substitution is made. Exact evidence and
context are in kb-link-review.md D12. The prior infrastructure-language claim was
incorrect: both sources are the same **English Hardware Inventory**, not Czech
prose. Identical source hashes alone never established language. D12 explicitly
corrects that provenance; original review reports remain historical records.

U12source ce0f031a1580e2db6e579ed8afeea3af27d5acf8 above publishedb29 changes
one mobile CSS block (3+/12-) to normal-flow display expansion without fixedheight,
nested overflow or absolute overlay. Left native control/focus and desktop stay.
Its unpublishedc102 refinement was folded before acceptance; no published rewrite.
R12owner2 applies the accepted semantic map and narrow optional cross-page field;
source/check commit pending. All article bytes, Pagefind code/pins, externalURLs
and prior published heads remain protected. Final review follows committed quick
checks; no new runtime/artifact success inferred from priorb29 receipts.


### D12 final committed source packet

All intended corrections committed at
`b5e3ebe54d9c42ab89142a1bcc50192e580fff10`, tree
`4e5248b97e53b7d34b9bf1a1ccf10d3ace54854d`, clean worktree/index. Complete
blog range0354..b5 has16commits/997paths,+23,982/-134; newline inventory SHA256
remainsfe97991c4983eb6c9661396f282ed32410503521e82bd5b9430ffcc62f9df635.
New publishedb29..b5 range is two coherent commits/four paths,+92/-26:
ce0f031 mobile document flow; b5e3ebe verified semantic KB sections/map extension.
Prior publishedb29 remains literal ancestor; only unpublishedc102 refinement was
folded intoce0 before acceptance. No public history rewrite or new update stream.

R12 owns three files89+/14-: KB-only link helper, finite acceptedmap and existing
link checks. Main recomputed/accepted c869a107 candidate and read all18 contexts,
actual target IDs/navigation/content equivalence and the remaining three negative
outcomes. Final normal/release quick checks passed55s/2s with fresh pinned utility;
three-mode fixtures cover full-target precedence, authority restrictions, query
beforefragment, single escaping and unknown/invalid fallbacks. Actual mapped data
asserts all9CLIincludingwp490/both284, bothcross-page anchors, oldstorage/backups
and English Hardware Inventory. All70KB reconciled67mapped/3unchanged, old23targets/
ninefragmentpairs/rootalias/52oldoccurrences preserved. All250 article bytes,
sourcehrefs/code/CRLF/metadata/draftstate, blogrouting, Pagefind and U12 retained.
Existing authoring note remains accurate; no redundant prose edit was needed.
Source/staged/committed whitespace passes; ordinary commit hooks preserved.

Prior D11 semantic classifications are superseded explicitly, not silently
rewritten: infrastructure was shared English inventory, and missing historical
source IDs did not disprove modern English equivalents. Current record shows
why the user example now maps toapi#using_cli and why ZNC/historicalOpenVZ still
lack a defensible equivalent after contextual searches. Reviewer must assess
actual new semantic evidence and current source, not assume earlier fallback
acceptance covers it. Bounded readonly KB spotchecks permitted, no KB writes.

Overall whole branch remainsHIGH/all4lanes; retained reviewer0 Sol/xhigh/read_only.
Full source/range/history/no-migration/consolidation review requested after quick
passes. No new pin/dependency/lock, database/API migration or production activation.
Config7bab/W remain exact unchanged ranges, prior evidence retained. Final B12
rooted result-d12/input/native/Pagefind-byte proof and focused runtime follow
review. Reuse earlier search API/snapshot proof only after verifying unchanged
141index files/adapter/nativeinputs; do not repeat the full search suite. Runtime
covers top/document-scroll-to-last-widget/article/close-reopen/short-landscape/
phone/desktop plus actualwp490/allCLI/moved-link attributes, no externalnavigation.
Only current8990preview may be refreshed under later lead release; d229/b093 and
older roots stay open. Feature-only publication/CI may parallel focused UI after
accepted source/artifact; final readiness requires both. No merge or production.


D12 unresolved-evidence precision: direct native English lookup
`kb-page get --wiki org information:openvz` at12:33:07UTC exited1 with
page-does-not-exist/empty stdout. This closes the possibility of an existing
orphan English counterpart omitted by fulltext search. No candidate/source/hash
change: c869/b5 remain exact. Receipt is in kb-link-review.md; no extra crawl.


### D12 final review accepted

Retained reviewer0, thread01a1b293-016d-7f41-95f0-b2c1da14ee3e,
Sol/xhigh/read_only, independently completed all four lanes at HIGH risk.
No Blocking, Important or Advisory findings. Exact full0354dac..b5e3ebe range,
tree4e5248b9,16commits/997paths and inventoryfe97991c independently reconciled;
newb29..b5 increment is fourfiles92+/26-. Config7bab/Wc379 remain unchanged.
Reviewer independently read all18 contexts and bounded live English target
sections, reconciled70KB=67mapped/3fallback, verified acceptedc869map and
250unchanged source files. Explicit no obsolete history/fixups, no repeated
update streams and no migrations conclusions accepted. Only unpublishedc102
was folded intoce0; published ancestry is intact. Remaining three fallbacks
are scoped absence/equivalence conclusions, not universal absence claims.

Lead accepts source-review gate and releases B12 rooted artifact proof, followed
by focused U12 document-scroll/mobile/link runtime. Prior search proof reuse
requires141Pagefind files/adapter/nativeinput identity. No new runtime, artifact,
featureCI, default integration or production success is inferred from review.


### D12 verification after accepted source review

Exactb5/tree4e5248b9 remained clean. Lead accepted result-d12 rrv49 artifact
with1802digests, complete source/input/native Pagefind proof and141Pagefind/
adapter/nativeinput identity againstb29, permitting scoped reuse of search
runtime. U12 sixCS/EN phone/landscape cases, last archive->article document flow,
scrolled close/reopen/focus, desktop, allnineCLI/two moved anchors and one
ENsearch smoke passed25.432s; actual JSON/captures inspected. New real preview857
is retained with d229/b093 and all old roots. Feature SSH publicationb29->b5
and final CI42373985435 success accepted; defaultmain/HEAD unchanged0354.
Normal/release/Nix steps pass, protected-main package/upload skipped,0artifacts.
No source changes after review, no new review needed for evidence-only receipts.
No default integration/production transition/human translation approval implied.


## D13 final committed whole-branch packet

This section supersedes earlier current-head statements; historical receipts stay scoped. All intended source is committed and quick checks pass. No final artifact/system build or new preview/runtime/CI is yet claimed.
### blog

Base `0354dac281978867ea8c1553b092ce19bccb5ccd` → head `45d04bc2be31b071cfe4011bab60ddf6d45322f5`, tree `f5fddf0e2c6ce577fe8f11fa6096718b3807078c`, clean. 997 files changed, 24188 insertions(+), 140 deletions(-). Complete newline changed-path inventory SHA256 `7f8e527e8ae0a821496a1f120d3a709d7e587bf675805034290484e983e0d1c5`.

```text
d7b90f09e1edd6fb2b032057205c91d6df5c94ee Import the captured Czech WordPress corpus and public assets
46286f9c7c9e4d1735ac598fa57d9446d1d992ae Preserve the original Flat design around the imported archive
57feaa92ceb6ce7fb96d479bb5b5a823a24cd7fd Align authoring instructions with the imported blog
b16c7f46af7424cf3e8d1fcb0ed8227981b71033 Translate 63 archived articles into English drafts
ea8441f2f3cbd01e105798674caf0c3ce132e580 content: draft 62 English archive translations
f464781e488c66a0f4cf61c50eb4249240ad94a3 Prepare opt-in native discussions for production articles
aeed3a018d895b797e1b8d9b2863dd20c0dec8e0 Prepare checked immutable blog release artifacts
3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb Isolate concurrent preview servers and verify real VPN pages
3dff9d7dbf61d7bf7c76e10fd72929711cd2bbf7 Center article media and localize the English registration CTA
d6c673c9e6addc8cf4f32f10cd653d8a632f0ddb Reduce repeated wording in English article openings
f0337fb7eae8797efca9254cd7208949cb0f77e4 content: avoid repeated English article openings
c829fbf4abcd7f7ab47b44386b3d12ec39090b55 Clarify mobile navigation placement and pagination states
95a3cae2a1185c096968357e558ee15ad5a2a7f8 Add local per-language Pagefind article search
b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d Render verified English article and knowledge-base links
ce0f031a1580e2db6e579ed8afeea3af27d5acf8 Expand the mobile sidebar in normal page flow
b5e3ebe54d9c42ab89142a1bcc50192e580fff10 Resolve verified English KB sections across page moves
70631dd0dab3dbc3386a826de6ef95462897b0a6 Keep search inputs and buttons on one row
14da1cfc3e7c22380872d0fa1789edea192d0c0a Organize article bundles by date and English title
45d04bc2be31b071cfe4011bab60ddf6d45322f5 Document workflow verification and WordPress recovery gates
```
### vpsfree-cz-configuration

Base `5941cdb3dda259e91c6a988a7dbf08c84700b326` → head `314f3881366c7315f8c3d64b43ef80a027a52fa0`, tree `95ff7c958c27d85da6b0bfec1aa798c2a98469ca`, clean. 77 files changed, 1077 insertions(+), 14952 deletions(-). Complete newline changed-path inventory SHA256 `19da44452b7c5936896902dfccdc1d550685423625fbf6f0fd5ccbd6d5f26ef4`.

```text
b4a7f22a46c16be453052a37ac98fc4c39401a9f internal-dns: add the blog container address
7bab9781d0a5eb1aed5914f0aed99f6d7d491632 blog: prepare disabled static hosting and release validation
36f1f5678d69086d5274d824e7e023c8f353390d blog: fix the static default virtual host option
314f3881366c7315f8c3d64b43ef80a027a52fa0 blog: retire WordPress services and retain stored state
```
### workspace

Base `c122387075f6109135db2f53845aa77b8cf2838e` → head `c3799bb22e7ead2a3738105bad96bfc34d3b8641`, tree `0b4aff5720f8086ef5e24115f720f03ab8bfefad`, clean. 1 file changed, 5 insertions(+). Complete newline changed-path inventory SHA256 `b986ee55cfbea619fd48fbe79f2cf2cabf1f4ebe41c711c6bab6eb8839032d9a`.

```text
c3799bb22e7ead2a3738105bad96bfc34d3b8641 Document the bilingual blog in the workspace project map
```
### Request, evidence and review scope

User requested one-row search forms, dated English-title source folders, a workflow testing explanation, and WordPress source retirement retaining all disk data. Sufficient D13 in design.md; main accepted all user-facing wording under the writing skill. U13 CSS70631dd is seven additions/seven deletions; preserve U12 document-flow sidebar, pagination and search semantics. P13 is250exactR100moves plus nine tooling/manifest/authoring files; importer must use the existing manifest's explicit assignments, refuse invalid/duplicate/unknown IDs and preserve English/manual-CS fences. No new identity registry/content matching. W13 is one documentation-only commit. New config increment7bab..314f is74paths206+/14986-: source package/theme removal dominates. Separate36f corrects an existing unsupported nginx default option;314f retires WP and retains state/accounts. Source candidate is intentionally not deployable alone: static/pull disabled, proxy unchanged.

[P13 path/byte/output evidence](article-path-review.md), [U13 CSS evidence](theme-receipt.md), and [W13/C13 receipts](release-preparation.md) bind owner findings/checks. P13 all250rawbytes unchanged, only125manifestcs_file and125generatedkeys remapped; native1661production/2110preview outputs fully byte-identical, importer8tests4s/normal53s/release1s/native8s PASS. W13 focused doc links/commands/whitespace pass. C13 pinned full module evaluation PASS: actual composed enabled nginx generation/default444/feed/PHP/proxy safeguards, absent WP/PHP/DB/init/cron/wrappers/oldhealthchecks, disabled server/pull, ownership parity (wordpress allocatedUIDunset; nginx60:60; mysql84:84 with unchanged account settings), no legacy-state activation/tmpfiles rules. Hooks/format/whitespace pass; no hook bypass. Raw local module receipts /tmp/c13-module-check.json and /tmp/c13-old-eval.json; exact hashes in C13 durable receipt. No actual machine retention claim.

Risk HIGH for complete branch/public/feed/release/data-retention/rollback contracts; general, architecture, scope, risk lanes. Retained reviewer0 Sol/xhigh/read_only/thread01a1b293-016d-7f41-95f0-b2c1da14ee3e verified eligible. Reconcile full19commit blog and4commit config histories independently, and unchanged ownW range. All prior accepted heads are literal ancestors, no rewrite. New requests are separate coherent corrections; P13 moves and required tooling/manifest/docs are inseparable for a working rename contract. No obsolete new approach knowingly retained, no dependency/channel/lock updates or repeated generated-pin streams. No application/database migration, schema/state conversion, release/deployed/external migration lineage. Source organization can be reversed from prior Git revision; live data remains in place. Require independent explicit whole-history/consolidation/streams/migration conclusions.

Review complete source and all new diffs (blogb5..45d; config7bab..314f) directly; prior reviews support unchanged source only. Check actual importer, path traversal/overwrite/identity boundaries, meaningful fixture tests and docs. Check account allocation/createHome/mutable-users and pinned stop/activation behavior; no disk data deletion/chown/GC. Check narrow nginx option fix rather than assuming prior fixture certification. No KB research/retranslation needed; map/runtime search sources unchanged. No live WordPress/KB/forum writes, service operations, build/Nix-develop/version probes, long checks or nested agents. No merge/deploy/default or lifecycle authority is supplied.

After accepted review, required exact int.blog build and one rooted blog artifact/input/hash proof follow; then focused single-row CS/EN sidebar/dedicated forms at320/390/desktop and one query. Reuse prior full search/snapshot only with unchanged index/adapter/native identity. Feature publication/final CI follow verified artifacts; default integration and actual protected-main artifact test require later explicit approval.


### D13 independent final review accepted

Retained reviewer0 Sol/xhigh/read_only, verified same-session thread
01a1b293-016d-7f41-95f0-b2c1da14ee3e, completed all four lanes at HIGH risk
with no findings. Exact full blog0354..45d/tree f5fddf0e (19commits/997paths),
configuration5941..314f/tree95ff7c95 (4commits/77paths), and ownWc122..c379
were independently reconstructed. Inventory SHAs match: blog7f8e527e8ae0a821496a1f120d3a709d7e587bf675805034290484e983e0d1c5;
config19da44452b7c5936896902dfccdc1d550685423625fbf6f0fd5ccbd6d5f26ef4;
Wb986ee55cfbea619fd48fbe79f2cf2cabf1f4ebe41c711c6bab6eb8839032d9a.

Reviewer independently proved250R100moves, every dated title normalization,
reverse manifest path-only equality and unchanged IDs/bytes/URLs/draft/source
metadata; examined importer invalid/duplicate/unknown/manual-CS/EN/overwrite
fences and meaningful tests. Reviewed single-row CSS and current workflow
test/recovery documentation. Read pinned account updater and WordPress/MySQL/
PHP/nginx modules: allocated UID retention/createHomefalse/no destructive stop,
legacy account parity and state-path activation/tmpfiles absence agree with
owner evidence. Actual live IDs/data remain unverified. Reviewed independent
nginx option fix and forced enabled generation, default-off unservable candidate
and prohibition on standalone deployment. Full19blog/4config logical series has
no obsolete approaches/fixups/additional consolidation, repeated pin/generated
update streams or application/database migrations/external migration lineage.
No code/report writes or builds/runtime/production requests by reviewer.

Lead accepts source-review gate. Exact final int.blog build, rooted blog
artifact/input/hash proof, focused search-row runtime and feature publication/CI
follow. Prior search runtime reuse still requires index/adapter/native identity.
Main-only real artifact validation and production/default integration remain
separate future approvals; review grants none.


## W15 completed blog milestone: final amended documentation review

Blog final `92ed3dca3120ffa3acae1b6efda6dfa974fb9dce`, tree
`cd8e3e7de8434fefd391e7ccf7706b74801fe019`, clean. Same full0354dac..92ed
19commit/997path series; changed-path inventory remains7f8e527e8ae0a821496a1f120d3a709d7e587bf675805034290484e983e0d1c5.
Only docs/deployment.md differs from independently reviewed45d. The last logical
doc commit was amended on unchanged14da; exact45d retained in recovery ref
recovery/2026-11-06-multilingual-blog-migration-w13-45d04bc. Raw range-diff and
JSON proofs are linked in release-preparation.md. No patch-equivalence claim: the
copy intentionally changes source-retirement policy to active WP coexistence and
future signed webhook-triggered immutable preparation. Publishedb5/U13/P13 literal
ancestry intact. All prior app/rename/importer/quick/output proofs remain exact
for unchanged files; W15 focused doc links/commands/whitespace pass, normal amend
with hooks preserved. Main accepted exact prose under writing skill.

This is a separate completed BLOG deliverable: UI row, dated bundles and accurate
workflow/rollout instructions. Ongoing H15/N15 configuration implementation is an
independent later user addition, not complete or certified by this review. Config
314f retirement was removed from its unpublished lineage after the user's revised
sequence, recoveryref retained; currentC148f restores all activeWP source and is
still being extended by H15/N15. No live deployment. Review blog only plus its
documented D14/D15 contract, not uncommitted config. New webhook documentation
does not claim actual delivery/activation success. Native repository workflow_run
notification -> signed exact HTTPS route -> target independent HTTPS acquisition
-> immutable stage only, no timer/SSH/current switch; actual receiver config and
real operational proof remain separate. Source activation admission stays fenced.

Reuse prior full D13 app/history review for unchanged source; rerun affected
general/scope/risk documentation/contract lanes as needed at HIGH whole-branch
risk with same reviewer/settings. Explicitly reconcile complete final blog series
and no obsolete last-copy/fixups/repeated-update streams/no migrations. Source
artifact+U13 focused runtime may follow BLOG acceptance while unrelated webhook
config work continues. No new full search/snapshot/config review claim or builds
by reviewer. Final config review/build/integration will follow H15/N15 completion.


### W15 final BLOG review accepted

Same retained reviewer0 Sol/xhigh/read_only completed affected general/scope/risk
lanes at HIGH whole-branch risk with no findings. Exact0354..92ed/treecd8e,
19commits997paths and inventory7f8e527e independently reconstructed. Only deployment
doc differs from reviewed45d, same14da parent, recovery45d verified. New current
coexistence/webhook/prepare-only/admission wording is independently accepted,
not claimed patch-equivalent. App/architecture review reused only for unchanged
source. Explicit no obsolete/fixup/amendment approach, repeated streams or
migrations. ConfigH15/N15 excluded; source still in progress and receives its
own final review. Lead releases exact92ed artifact and focusedU13 independently
from that later config addition. No default/production authority or new config
certification is supplied.


## D15 completed CONFIG webhook milestone: final review packet

All intended configuration source is committed and quick checks pass. Exact
base `5941cdb3dda259e91c6a988a7dbf08c84700b326` → head `2aa36562503c8e32f02a308bc70bc9260f5ee120`, tree
`d2ee9e537154e757a6f277cc7fbdd36011ad9a09`, clean. Complete source series:

```text
b4a7f22a46c16be453052a37ac98fc4c39401a9f internal-dns: add the blog container address
7bab9781d0a5eb1aed5914f0aed99f6d7d491632 blog: prepare disabled static hosting and release validation
36f1f5678d69086d5274d824e7e023c8f353390d blog: fix the static default virtual host option
8f122c39f6756860c3f8a6417fa5533561e3c1e8 blog: verify WordPress and static hosting coexistence
d2328a8ad2eeea9aea6eb90968c0bc6f4ae3149c blog: prepare artifacts from signed workflow notifications
2aa36562503c8e32f02a308bc70bc9260f5ee120 blog: wire signed build notifications for artifact preparation
```

Full newline changed-path inventory SHA256 `714792db8449392f743440eb2520f9549378492fdd3bb3e6e1cfe32df4c9708a`, 12 files changed, 2170 insertions(+), 1 deletion(-).
Published7bab and valid36f remain literal ancestors. User superseded retirement
with activeWP coexistence; unpublished314f was removed via native empty-range
rebase and retained only under recovery ref
2026-11-06-multilingual-blog-migration-c13-recovery. Superseded84.397s C13 build
and all earlier roots retained, never deployed and not current proof. New C14
8f122 modifies only docs/coexistence fixture, restoring complete publishedWP
source; no revertstack, service/data removal or ownership-onlymodule remains.
H15d232 adds signed receiver/prepare-only worker/shared-head-recheck/tests;
N15the final commit wires routes/services/credentials/module fixture/docs.

### Accepted contract and quick evidence

D14/D15 in design.md are sufficient accepted briefs. Main accepted all final
user-facing copy under writing skill. User wants signed webhook notification
instead of polling and keeps WordPress80/PHP/MariaDB/init/cron/packages/health
checks/publicproxy while proving generatedstatic site. Exact route is
https://blog.vpsfree.cz/_hooks/github/build through existing PragueHTTPSproxy
and backend80 to loopback127.0.0.1:8091; no new ingress port/SSH/.org dependency.
Both enable defaults off; static enable, verified positive repository/workflow
IDs and distinct external non-store runtimecredential strings required.

Receiver: stdlib, HMAC original body/constant-time,1MiB/type/method/Host/exactpath/
encoding/length/event/repo/workflow/main/nonPR filters, quick202 only after
durable compact hint. No request-side API/commands or payload URLs. Dedicated
user holds onlyHMAC; workerblog-release holds only artifactreadtoken via distinct
LoadCredential. Root/group2770inbox+shared0660hints/stablelocks; pending/processing
.path, bounded crash triggers and no timer. Every hint is onlywake-up: independent
currentprotectedmain/repo-ID/run/artifact/hash acquisition, prestageheadrecheck
under serialization and aftercopy. No hintedSHA/runselection or staleearlyreturn;
delayedold/higherID notification cannot suppress latesthead. Duplicate/sameID
redelivery retryable. Handledfailure records boundedfailed/status and exits0,
no pathspin; crashes retain claim, concurrentpending survives earliercompletion.
Worker ONLY invokes acquire/validate/immutableprepare; never current/switch_fixtureable/
pull/activate/rollback. Existing machine-admission fence intact.

H15 fourpaths634+/6-,14webhooktests~0.934s+7release~0.590s pass, meaningful
auth-beforeparse/rawUnicode/bodyalteration/forgedURL/lengthencoding/durablefsync/
queuefailure/oldhint/retry/idempotence/concurrency/crash/staleheadbeforeandduringcopy/
invalidexpiredolderartifact/currentpointer+receiptpreservation fixtures. Official
HMACdigest transcription in initial test corrected with independentOpenSSL and
stdlib agreement, no product failure. N15 fivepaths489+/8-, both documented
Nixmodule evaluations pass against pinnedStable path z40fynbhnw0d06q05mw2mznn49h1y9pk-source;
force actual nginx/systemd/activation generation at both hops, defaultoff/coexistence/
port80+8080/Host/rawbody/1MiB/timeouts/credential+inboxisolation/noingress/notimer/
noactivation. Receipt hashes in release-preparation.md. Normal hooks/Nixfmt/
commitmessages/whitespace pass without bypass. No liveHTTP/server/build/settings/
credential/webhook/production operations by source owners.

### History, interfaces, scope and required independent conclusions

Wholebranch riskHIGH, all four mandatory lanes. Source/initiation is independent
from completed BLOG milestone0354..92ed/treecd8e,19commits/997paths; its source
review/artifact/UI/publication/CI42390960159 accepted and unchanged. OwnWc122..c379
unchanged/prioraccepted range. Review full final config sixcommit series/finaldiff,
not only newreceiver. Priorreview supports exactunchanged source only; C13retirement
conclusions do not certify currentcoexistence. Compare actual user scope with
~1k receiver/module/test lines plus necessarydocs, no framework/jobbroker, no
automaticactivation. Providercontract is blogpackager artifact and config's
existingvalidator; H15 reuses prepare rather than duplicating policy; N15fixedCLI
interfaces in D15. No workflow source/permissions/secrets changed.

Require explicit final history/consolidation/repeatedstream/migration conclusion.
No oldretirement finalapproach, no redundantfixup/revertstack; source data accounts
unchanged. No dependency/channel/lockupdates or repeated generatedstreams. New
boundedinbox is internal newlyintroduced receiver/worker state at sameversion;
no existingserving schema conversion/database migrations, no merged/released/
deployed/externallyconsumed migration lineage. No actualdeployment anywhere.
Record any current scope or reliability/security defect concretely; don't expand
into upstreamHTTP/GitHub/OSconformance or a generalizedscheduler.

### Remaining verification and permission boundaries

After independent final review: exact native confctl builds for int.blog and
prg/proxy, complete finalsource/input/derivation/systempath proof; H15registered
loopback realHTTP+fixedworker integration using syntheticHMAC and mockedGitHub
factory with realacquire/validate/stage. Preserve sentinel current/receipt/served
bytes and allrealservices. No liveGitHub/tracker or publicrequests in thatcheck.
Sourcefixtures are not actualdeployedproxy/Unixidentity/delivery proof.

Later operational steps still need actual approvedcoexistencedeployment, verified
IDs/runtimecredentials, realprotectedmainartifact after explicitintegration, hook
registration and signedping/completion/redelivery+targetstaging proof. No private
8080/publicpointer activation without supportedmachineadmission; no publiccutover
without userapproval. Retainoriginalgeneration/fullWordPressDB/uploads/fonts/keys/
accountIDs and data; no cleanup. Source review grants no deployment/default/
secretsettings/service/lifecycle action or forum/KBwrite.


### D15 final CONFIG review accepted

Same retained reviewer0 Sol/xhigh/read_only completed all four lanes at HIGH risk
with no findings. Independently matched exact5941..2aa/tree d2ee9e53, six commits,
12paths+2170/-1 and inventory714792db. Receiver/worker/helper/modules/tests/copy
reviewed directly; earlier review only unchanged source. Raw-body HMAC/typed
filters/durableboundedhandoff/current-authoritative acquisition/prestage recheck/
retry/crash/concurrentpending/leastcredential and exact routing/coexistence/fence
contracts accepted within source scope. Independent AST/inventory/ancestry/clean
checks pass; owner14+7Python/twoNixchecks retained for exactscope, no reviewerbuilds.
Explicit no obsolete retirement/revert/fixups/additional consolidation, no repeated
input/generated streams and no database/serving-schema migrations. Published7bab
and36f ancestors preserved;314f not ancestor, WP/account/data/health definitions
unchanged. Bounded newinbox is same-versioninternalstate, no priorserving conversion.

Lead releases final exact int.blog+prg/proxy build batch then registeredloopback
HTTP/fixedworker/mockAPI rehearsal. Real deployed pathunit/user/credential/proxy
recovery and GitHub delivery remain latercoexistenceverification, not claimed
from sourcefixtures or localmock. No activation/default/deploy/lifecycle authority.


## T16 final committed production-only Piwik milestone

User explicitly requests existing Piwik code in production only, no preview;
subsequently supplies English blogsiteID10. Czech existingblogsite4 retained.
This supersedes EN-unset/ID-choice blocker; no admin/SSH/account work needed.
Exact blogbase `0354dac281978867ea8c1553b092ce19bccb5ccd` → head `6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344`, tree
`c28f761c78714715a2c22e455782fa325188f12e`, clean; 998 files changed, 24300 insertions(+), 142 deletions(-).
Complete newline pathinventorySHA `6a96e46010dfce0ec5445e0ff33246d83b2fafcc76df3c3ad011a063adb2d3e4`.

```text
d7b90f09e1edd6fb2b032057205c91d6df5c94ee Import the captured Czech WordPress corpus and public assets
46286f9c7c9e4d1735ac598fa57d9446d1d992ae Preserve the original Flat design around the imported archive
57feaa92ceb6ce7fb96d479bb5b5a823a24cd7fd Align authoring instructions with the imported blog
b16c7f46af7424cf3e8d1fcb0ed8227981b71033 Translate 63 archived articles into English drafts
ea8441f2f3cbd01e105798674caf0c3ce132e580 content: draft 62 English archive translations
f464781e488c66a0f4cf61c50eb4249240ad94a3 Prepare opt-in native discussions for production articles
aeed3a018d895b797e1b8d9b2863dd20c0dec8e0 Prepare checked immutable blog release artifacts
3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb Isolate concurrent preview servers and verify real VPN pages
3dff9d7dbf61d7bf7c76e10fd72929711cd2bbf7 Center article media and localize the English registration CTA
d6c673c9e6addc8cf4f32f10cd653d8a632f0ddb Reduce repeated wording in English article openings
f0337fb7eae8797efca9254cd7208949cb0f77e4 content: avoid repeated English article openings
c829fbf4abcd7f7ab47b44386b3d12ec39090b55 Clarify mobile navigation placement and pagination states
95a3cae2a1185c096968357e558ee15ad5a2a7f8 Add local per-language Pagefind article search
b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d Render verified English article and knowledge-base links
ce0f031a1580e2db6e579ed8afeea3af27d5acf8 Expand the mobile sidebar in normal page flow
b5e3ebe54d9c42ab89142a1bcc50192e580fff10 Resolve verified English KB sections across page moves
70631dd0dab3dbc3386a826de6ef95462897b0a6 Keep search inputs and buttons on one row
14da1cfc3e7c22380872d0fa1789edea192d0c0a Organize article bundles by date and English title
92ed3dca3120ffa3acae1b6efda6dfa974fb9dce Document artifact checks and webhook preparation
6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344 Keep Piwik tracking in static production pages only
```

Increment above published92ed: sixpaths90+/5- (hugo.toml, fixtures/hugo.toml,
layouts/partials/piwik.html, layouts/_default/baseof.html, bin/check, README).
The16linepartial reproduces the public existingblog `_paq` page/link tracker,
async+deferpiwik.js loader and exactnoscriptpixel at fixedpiwik.vpsfree.cz; only
per-language public numericIDs differ. Source requires explicitproduction env,
notHugo.IsServer, positiveconfiguredID; fixtures explicitlyoverridebothIDs0.
No newtrackingoptions/cookiesbanner/framework/sitecreation/backendsettings.
Existinglocal searchmoduleallowlist retained, only exactproductioninline/Piwik
pixel admitted, Hugoaliasredirects excluded because notbaselayout. Mainread/
accepted exacttwo-sentenceREADME under writing skill. User10 authoritative;
mainENcontainer6 is unrelated and notsubstituted.

All intendedsourcecommitted ordinaryhooks/no bypass, indexclean/yielded. Single
final normal+releasebatch PASS on finalcode; normal verifiesactualproduction4/10,
positive91/zero/negativeENmatrix, preview/VPN/fixturesabsence and retainedroots/
routes/hash/draft/link/search/determinism. ReleaseofflinefixturePASS0.187s.
NativeAST/TOML/whitespace pass.125ID/250complete articlebytes/draftstates and all
data/locks/search/build/indexer/assets/environmentconfigs unchanged against92ed,
except declared fixture suppression. No JS executed, Piwikcollector/piwik.js
requested, browser/server/artifactbuild or sourcepush byowner. SourceIsServer
guard is inspected, actualserverruntime stillpostreview. Evidence in existing
theme-receipt.md and theme-reference/t16-final-check.log/.exit plus sourcebeforeJSON.

WholebranchriskHIGH; retained reviewer0 Sol/xhigh/read_only, all applicable
general/architecture/scope/risk lanes. Complete20commit/998path history mustbe
reconciled; prior92ed literalancestor, newcoherentanalyticscommit, no fixup/history
rewrite/repeatedinput or generatedstreams/applicationdatabase migrations. Prior
source reviews applyonlyunchangedfiles. Config5941..2aa/tree d2ee9e53 and ownW
c122..c379 unchanged/reviewed/published, no configbuild/research repeat.

Independently checkactualtrackerparity/IDconfig/strictguards/HTMLescaping/
preview+fixtureprivacy and meaningfulchecks/documentation. Existingruntime
Piwikscript is intentionallyexternal and not part of immutablepayload; compiled
inlineHTML is hashed normally. No new dependency/lock or privatecredential;
allsiteIDs public. No analyticsbackend verification/requests needed forreview.
Explicitno obsoleteapproach/repeatedstreams/no migrations conclusions required.

Afterreview: one rooted result-t16 build with allservedhash/source/fullinput
proof and production4/10 HTML/pixel checks, unchangedPagefind/adapter/CSS/native/
article/feed evidence; reuseunchangedfullAPI/snapshot/UI results. Owner1refresh
onlyregisteredreal7b8 then HTTP-onlyservedpreviewexclusion; boundedactual
production-environmentHugoServer omission mayproveIsServer separately, no tracker
execution. Preservefixtures22b5/d229/b093/roots/session. FinalnormalBLOGSSHFF
publication expectedold92ed/main0354 and oneexactnewCIwatch. No config/default
integration/deployment/secret/site/account/settings/trackerrequests or lifecycle
authority supplied. LiveWordPress and productionroute remainunchanged.


### T16 independent final review accepted

Retained reviewer0 Sol/xhigh/read_only completed allfourlanes atHIGHrisk with no
findings. Exact0354..6dae/treec28f,20commits998paths(+24300/-142), inventory
6a96e46010dfce0ec5445e0ff33246d83b2fafcc76df3c3ad011a063adb2d3e4 independently
matched; published92ed soleparent/unchangedappsource reusedonlyscope. Strict
production/notIsServer/positiveID integerguard, fixedoldPiwikoptions, CS4/EN10
authority, fixture0/0 and bothscript/pixel omission accepted. Narrowexistingcheck
allowlists remainmeaningful; no remote execution or newframework/options.
Independent AST/TOML/250byte-ID/draft/source/input/history/whitespace checks pass.
Ownernormal/release proof retained, no repeatedbuilds byreviewer. Explicit no
obsolete/fixup/revert/historyconsolidation, repeatedstreams, migrations or serving
persisted-contract conversion. Config2aa/ownW unchangedaccepted.
Lead releases exactrootedartifact and registeredservedpreview+productionserver
privacyproof; source review grants no integration/deploy/lifecycle authority.


### T16 final verification and publication accepted

Exact6dae/treec28f remains clean. Rooted result-t16 5bs03cb3 sourceNAR/complete
two-node/nativeinputs/1802hashes accepted.314base-layoutHTMLpages contain exact
CS4/EN10 tracker/pixel;140redirects omit; otherHTMLbytes and1348nonHTML files,
141Pagefind/CSS/adapter/native/feeds/250articlebytes unchanged. Eightregistered
HTTPchecks include normalVPNand production-environment nativeHugoServer; all
omit script/pixel/_paq with configured4/10, noJSortrackerbackendrequest.
Native source/runtime privacy proof accepted; no repeated broadsearch/UI suite.
Normal canonicalSSH FF92ed->6dae, main/HEAD0354 unchanged, comparison0354..6dae
captured. ExactCI42398048773/job128479582616 normal/release/Nixbuildsuccess;
trusted-mainpackage/uploadskipped/0artifacts. Main independently readactual
40charheadSha and terminalmetadata; utilityprose41chartrailing-e typo is only
reporting, retainedraw plus correctlaunch/data proof, no source/CI retry.
AllT16gates complete; no subsequent source changes or furtherreviewrequired.
No integration/production activation/humanEnglishreview/analyticscollection
backend assertion or lifecycleauthority. Finalpreviews/fixtures/roots stay open.

## E18+B18 final BLOG review, 2026-11-07

Accepted independent reviewer0 report, saved gpt-6.1-sol/xhigh/read_only, thread01a1b293-016d-7f41-95f0-b2c1da14ee3e. Mandatory general/architecture/scope/risk lanes at HIGH whole-branch risk: no Blocking, Important or Advisory findings. Reviewed complete0354dac281978867ea8c1553b092ce19bccb5ccd..7fa57c809d828e945b104f5ab3fa74f76a030a51, treeb04e5ee1ffc13882bc04cca7e39328db1f998277, actual22commits/999paths +24569/-142, newline inventory SHA2566f555b587f56b7337456e39daf68aba4047dc0ee1551f6c89dc8f5aef0501a08. Incremental6dae..7fa130paths538+/269-. New06f88d14 records explicit maintainer approval (125EN notdraft/reviewed/currentCS hashes) with all bodies/other metadata/CS exact;7fa57c8 adds only prepared local derivative/bodyCSS/NOTICE. Original photo unchanged; local fingerprint/repeat/maxwidth/provenance accepted. Generic future author review guidance retained.

Reviewer independently inspected all125pairs/rawbytes, AST/whitespace/inventory/ancestry/cleanhead; owner normal+release83.317s and bothroot fixture proof inspected, not rerun. Explicit whole-history conclusion: no obsolete approach/fixup/revert/consolidation need, no repeated dependency/pin streams, no migrations. Draft creation then maintainer acceptance are distinct justified published milestones. Recovery45d not ancestor. Config2aa/workspacec379 unchanged accepted scopes. No source/report writes/build/Nix/network/service/production action by reviewer.

Residual checks: exact rooted artifact/input/hash proof, actual1440/1920 longscroll2+joins and320/390mobile, feature publication/CI. P18 new deployability source (A18 publication/H18hosting/Discourse) is a separate pending deliverable requiring final review; this gate supplies no deployment/integration/lifecycle authority. Lead accepted current E18+B18 source review and will release focused native preview proof independently of config implementation.

## A18/H18/D19 joint final review at9ea9fbd9 and3fb7d25

Reviewer0 retained gpt-6.1-sol/xhigh/read_only directly completed all4lanesHIGH. CONFIG5941..9ea9fbd9f9a436f82249c08d9e3efc485fe8bff8/treed160b48cd08b5bce350610120732edd068685540,8commits18paths+6108/-12, inventory6bf2629421dbfcf465687d9e6ce74a88b08c1d9a4bef29eac6ed2db10bbc9411. BLOG0354..3fb7d25b1ca39dcddf3dcc8a22b2e47bcf0e49a2/tree743521562f0ef6b1e419011e55888ced23637cea,24commits999paths+24756/-149, inventory6f555b587f56b7337456e39daf68aba4047dc0ee1551f6c89dc8f5aef0501a08. Two Important findings; no other Blocking/Important/Advisory findings. Gate held pending corrections.

- A18-R1: root-invoked rollback/reconciliation followed service-controlled content paths, allowing symlinked CSS ancestors/final paths to redirect privileged writes/chmod outside blogroot. Root queue resume also needs same boundary. Owner0 fixes all mutable content/inbox I/O under fixed service identity via a bounded irreversible dropped child; root retains policy/control/same lock and fixed systemctl. Root prepare/pull/activate will be rejected; operator manual publish uses fixed service with LoadCredential. Root maintenance/status/rollback retained. No arbitrary UID/path/exec hook. Focused real isolated outside-sentinel regression required.
- A18-R2: staged payload/archive/files/directories lacked fsync before durable pointer/receipts. Owner0 adds ordered file/archive/bottom-up directory barriers for new/existing stages and retained CSS before pointer eligibility; sync failure prevents pointer commit. Focused ordering/failure regression, no machine crash test.

Independent H18 source540projection/modes/defaultWP/hook/alias behavior and D19 pinned2026.9.1 framing/import/visibility/RSS/pilot docs accepted. Protected source/pins/data/corpus unchanged. Whole-series history coherent, no obsolete stack or repeated dependency/pin streams, no database/schema/transitional conversion migrations; staged schema1 retained/newcontrol additive. Old314f/45d recoveryrefs not ancestors. Newrootprivilegechild adds a process/IPC boundary, so same reviewer will inspect affected general/architecture/risk lanes after committed fix/quickchecks; unaffectedscope conclusions reused. Scope lane has no changes unless remedy expands. Source9ea unpublished/undeployed; oldreviewedhead retained before amend. No builds/integration/deployment/default/lifecycle release from this review.

## R1/R2 affected final review: resolved at15ad7646 /82a1ee3

Retained reviewer0 gpt-6.1-sol/xhigh/read_only completed affected general/architecture/risk directly; both Important findings resolved, no remaining Blocking/Important/Advisory findings. Unaffected scope/H18/D19/corpus conclusions reused. CONFIG5941..15ad7646c369770fbee584c0e248d05ab9a372bc/tree22160d9a56c16ae270b10ef51b4e4403afe8536b,8commits18paths+6516/-12/inventory6bf2629421dbfcf465687d9e6ce74a88b08c1d9a4bef29eac6ed2db10bbc9411. BLOG0354..82a1ee3c90990e56cfde0da28ababed8f0444441/treed23e142cee504f6284ed0bbc4b028be6b8935e8c,24commits999paths+24765/-149/inventory6f555b587f56b7337456e39daf68aba4047dc0ee1551f6c89dc8f5aef0501a08. Sameparents937fd371/5032d82, old9ea/3fb recoveryrefs retained, no patch-equivalence claim. Correction4configpaths461+/53-, onlyBLOGdeploymentdoc13+/4-. Cleanheads/trees/indexes independently verified.

R1 fixed NSS child drops real/effective/saved UID/GID, caller groups/capabilities, sets no_new_privs; fixed required servicegroups retained. Root control/lock remains root; content status/reconciliation/rollback use inherited same lock/no secondflock, bounded JSON pipe and wait/reap. Queue writes service identity outside lock, root onlyfixedsystemctl. Root/wrongUID content CLI rejected; manual service already LoadCredential-backed. Reviewed allcall/error/FD/lock paths and exactdocs. Actualnamespace6/6 executes kernel boundaries/outside-sentinel/positivequeue/rollback/rootCLI, mappedNSSidentity only;21pure release+6namespaceSKIP separate from actual6PASS,19webhookPASS. Reviewer matched allcheckhashes to committedblobs, parsedAST/whitespace/inventories, didnotrun tests/build/network.

R2 flushes payload/archive finalmode, bottom-up directories/releases/root beforecompletedstage/receipt. Oldschema1reuse, explicit/idempotentactivation, CSS and reconciliation receive barriers; injectedfailure preservespriorpointer/receipt/noeligiblepending. Reviewed order, not merelycallpresence. No new Nix/pin/schema/migration; unchangedsettingsmoduleevidence scopedonly wiring, finalnativehelperbinding stillrequired. Same8/24historycoherent/noobsolete stack/repeatedpinstreams/no database/transitional migrations; artifact/stagedschema1 retained/newcontrolsadditive.

Lead accepted corrected source review and released ordered finalverification: owner3two-nodebuild, owner0rootedBLOG, owner3realnginx, owner2synthetic-enabled sourcePackage + registeredprivatefixedCLIintegration. Allfreshutilities serialized; noproduction/default/lifecycleauthority. User-run realcredentials/IDs/protected-maineligibleartifact/TLS/systemd/liveforum/coexistence/cutover remain unproven.

## Runtime-discovered feed correction, narrow-fix acceptance

H18 realnginx at15ad passed540exactaliases+named malformed/nonlegacy/feedalias cases, then /feed/500. Existing file-alias on slashURI triggered nginxindexphase appendindex.html. Owner0 corrected only static-blog.nix + staticmodulefixture: tryFiles /feed/index.xml =404 underbothfixedlangroots, RSSdefaulttype/typesretained/noexternalredirect. Main inspectedexact32+/3- delta, bothlanguage/noalias/generated2directive checks; focusedfixture37.425s exit0, normalhooks/cleanamendedhead. CONFIG1e840b8056bbc700ca3e9cd832f0d9301da52652/tree6f6d2020345f731370698be3ed2ff7fe25ac637e sameparent937fd371; old15ad recoveryretained. No interface/newdesign/policyPython/H18map/proxy/pins change. Directsame-contractfix accepted under mandatorynarrowfixrule, no repeatedindependentreview ofunchangedlanes.

Finalnativeidentityrefreshandrealfeed14remainingcaseprobe released aftercommit. Priorbuild15adreceiptsremainaccurate scopedoldsource; BLOG82aartifact2397hash/sourceinputs/body/media/privacyacceptedunchanged/noBLOGrebuild. H18firstfailure/log/configfrozen,540passedmapsevidence reusedonly aftermapbyteequality; no blindretry. Owner2fixedCLIintegrationwaits successfulrefresh+resumednginxprobe/directslotyield.

## Final verification and publication acceptance

Final CONFIG1e840b8056bbc700ca3e9cd832f0d9301da52652/tree6f6d2020345f731370698be3ed2ff7fe25ac637e and BLOG82a1ee3c90990e56cfde0da28ababed8f0444441/treed23e142cee504f6284ed0bbc4b028be6b8935e8c accepted after corrected source review/narrow feed fix. Native2node refreshed98.235s/full64inputgraph/sourceNAR/pernode/system+rollback compiledproof9fb8163e; BLOGrooted2397hash17.789s/full2node/sourceNAR/125each/feed10/protectedbytes+privacyproof; realnginx540alias+18unchangedcases/14newRSS+modes; actualfixedCLI28obs6.522s with realprivateNSS/fixedexpectedHTTPS syntheticAPI and finalpause accepted. Previoussetup/mode/labelerrors were fixture-only with original evidence retained; actualfeed500 led to committednativefix. Realhostsystemd/LoadCredential/NixOSswitch/liveGitHub/forum/deployment remain user-run, not certifiedbylocalrehearsal.

Bothfeaturebranches normalcanonicalSSHpublished exactheads/defaultsunchanged; BLOGCI42411255497attempt1SUCCESS/check/check-release/Nixbuild, trustedmainpack/uploadskipped0artifacts. CONFIGnopushworkflow/no dispatch. Independentreview/history/migration conclusions preserved; no remaining sourcefinding. User-runproductionplan reconciles finalsource/evidence and the testedroutecoverage limits, credentials/verifiedIDs/mainartifact/TLS/webhook/Discoursepilot/privatechecks/cutover/recovery. No defaultintegration/deploy/lifecycleauthority inferred; allrefs/roots/services/session retainedopen.
