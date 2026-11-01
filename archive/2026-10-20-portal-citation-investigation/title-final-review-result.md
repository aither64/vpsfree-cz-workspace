**Accepted. No Blocking, Important or Advisory findings for this title fix.**
The affected general/history and risk/security lanes accept the exact final
ranges below. Architecture, scope and unchanged client-design conclusions are
reused from [rebase-final-review-result.md](rebase-final-review-result.md) and
[workspace-final-equivalence-result.md](workspace-final-equivalence-result.md).

Reviewer: retained standalone thread `01a159bd-c577-7f01-900f-e41294b22209`,
catalog role `lead_reviewed/reviewer`. The current native turn
`01a15b17-a01b-7823-879b-c0b6211538a4` verifies **gpt-6-astra/xhigh**.
Unchanged guidance and prior source inspection were reused.

| Repository | Base | Accepted head | Complete ordered feature series |
| --- | --- | --- | --- |
| codex-web | `738b064a564d4f0050c676a742996cbe7680519c` | `57972192e30fe52ab33b867c8fe4d171f59a7fd5` | `5797219` |
| dev-workspace | `2c29b8019f35f86563ef9725aba7073533eafe67` | `52dcd471186ef874c5c93f4133744195d4815454` | `af4c853dfbd9f6fc71d1b79a10d3c8d4ea2ceedf`, `52dcd47` |
| workspace | `df73a12b2059453dd93e0bd75fd43013e41ce538` | `0ea5682410a38fe19627bc731e13894c1e51db57` | `0ea5682` |
| vpsfree-cz-configuration | `2d7e3550582765c416ea35c5623d08902199ce9e` | `86e19685313270d88e4db30038c056ce4b807abd` | `86e1968` |

**General/history: accepted.** I verified all heads, clean worktrees, complete
series/messages and complete final diffs against `title-final-inventory.json`
and the saved diffs. Compared with the accepted runtime, the only source changes
are the anchor-title policy in `portal/internal/web/server.go:458` and its
regression assertions in `portal/internal/web/citations_test.go:14`.
The correction restores the already required hover title; no browser asset
changed, so another JavaScript cache-version bump is unnecessary.

The fix is folded into the owning citation commit. Runtime still selects the
client exactly once in `af4c853`, across the five existing pin/module/vendor
files; `52dcd47` does not edit them. Workspace has one final runtime-pin commit,
and configuration has one regenerated confctl update with its generated message
retained. Client is unchanged. **Whole-branch history and consolidation are
accepted:** no redundant pin stream, superseded approach or fixup-only commit
remains. Workspace's inherited tracking-only base retains the prior equivalence
conclusion; unrelated tracking/archive content was not reread.

The prior runtime, workspace and configuration heads remain reachable through
their `2026-10-20-portal-citation-before-title-fix` refs. The unchanged client
head remains the final client selection. Deployment provenance does not require
retaining obsolete pin commits in the new series.

**Risk/security: accepted.** I inspected Bluemonday v1.0.27's default
`Paragraph` regexp, element-specific attribute-policy handling and output
serialization. The default regexp excludes middle-dot and double quotes.
`AllowAttrs("title").OnElements("a")` permits those characters in anchor
title values without changing the allowed URL schemes, other attributes,
elements or origin checks. Bluemonday still tokenizes, filters and serializes
attributes with escaping; quotes and script-looking text remain attribute text.
Goldmark raw-HTML handling, sanitization and nofollow/noreferrer requirements
remain unchanged.

Because the sanitizer is shared, ordinary Markdown links and artifact-preview
links also retain these title characters. That is a bounded text-presentation
effect, with no new executable attribute or URL permission. The extended test
checks the escaped Unicode/quoted/script-looking title, preserved raw text and
literal code, script removal and rejection of a `javascript:` citation URL.
The existing artifact-preview security test also passes.

Both downstream locks select runtime
`52dcd471186ef874c5c93f4133744195d4815454` with matching content hash
`sha256-HjVzqCVJ+VJr9cByJD4esv1S7BEKin2d441nVwBBfhA=`. Only the runtime
node changes relative to the previously accepted downstream locks. Provider
`5797219`, extension `767dfd587e346168e1443e65ccdb67ce748f3fe3`, vendor hash,
native Codex inputs, claims capability and recovery behavior are preserved.

**No migrations; migration lineage accepted at all four final heads.** The
complete ranges introduce no database migration, durable schema/format change,
native version change or transitional migration. There is no migration version
requiring merge, release, deployment or external-use provenance. Existing
package-transition and claims/recovery constraints remain applicable.

Independent quick checks passed using the retained Nix toolchain:

- Complete-range `git diff --check` for all four repositories.
- `go test -mod=readonly ./internal/web -run TestCitationMarkdownPresentation
  -count=1 -v`.
- `go test -mod=readonly ./internal/web -run
  '^TestArtifactPreviewRendersSanitizedMarkdownAndEscapedText$' -count=1 -v`.
- Composed `bin/check-dev-workspace-deployment` against the final workspace and
  configuration worktrees, selecting runtime `52dcd471`.

The packet reports successful historical-page citation acceptance and first
deployment continuity checks; I did not repeat live operations. Those results
do not certify the corrected artifacts. New exact-revision artifacts, CI and
live title/continuity verification retain their separate evidence requirements.
Feature scope and the recorded conditional deployment/integration authorization
are preserved. No merge or activation is performed or certified by this report.

Only this report was written. Source and Git/session/deployment state were left
unchanged; no nested agents, long tests or unrelated archive-content review were
used.
