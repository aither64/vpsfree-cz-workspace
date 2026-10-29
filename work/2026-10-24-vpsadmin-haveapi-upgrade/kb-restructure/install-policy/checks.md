# Version-independent installation and separate wiki edits

Prepared from lead-owned final bilingual prose and the accepted
[technical brief](../../design.md#2026-10-29-kb-installation-versions-and-obsolete-header-warning).
The prose is byte-identical to the released inputs: CS
`933c4a1e565d75b092cc9854f11cb0aa08e7ce66109b2d6bff12155b75e02fc9`, EN
`fea084c46c5e3b998f6b4fd7add5827390600d409528e5335487bdfb54b0dd20`.

The existing `package-d/prepare-release.rb` canonical build passed:191 pages,
2 changed,189 preserved, unchanged actual captured production guards. The
installed d50 `KbRelease::Manifest` schema5 parser and all candidate checksums
passed. Root aggregate manifests are preview/check inputs only.

Focused byte checks passed: all non-install code blocks unchanged (34CS/31EN),
API7 semantic values and Go literal escaping preserved; five old installation
blocks replaced by six version-independent blocks per language. No registry,
compiler, SDK, browser, network-link or client execution campaign was needed.
The architect's retained package/dependency findings supply the command contract.

All seven publication diffs apply exactly and match their chained content
hashes. Steps01/02 are unchanged. Step03 introduces the final versionless client
text directly; Czech step04 removes exactly377 bytes of obsolete warning.
There is no English step04/no-op. Prior source/chain/manifests/summaries are
retained in `prior/`; prior staging evidence hashes are unchanged. Detailed
local results: [quick-checks.json](quick-checks.json),
[canonical build](canonical-build.log), [bindings](binding.json).

`git diff --check` passes for page and metadata changes. Unified `.diff` files
contain literal one-space blank context records; ordinary Git whitespace
checking reports those records (including an English final context record),
not newly added article whitespace. With only blank-at-EOL/EOF diagnostics
excluded for those generated diff files, their check passes. Exact patch
application remains required and passed. No source whitespace was normalized.

Preparation-only failures: ambient Python lacks PyYAML, so the unchanged
installed Ruby YAML reader was used before any preparation mutation. A first
README patch had stale final context and applied no changes; the corrected
patch applied normally. No product/tool repair or live retry resulted.

The [publication README](../publication/README.md) records verified installed
capability, staging baseline restoration and the ordered public-save plan.
The old three-step checks and receipts retain their historical pinned scope;
this followup supersedes only the install/header text and staging mechanism.
NO MIGRATIONS; no application, dependency, API, config, auth, cluster or
production mutation. Lead owns state, independent review assignment and handoff.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
