# V1 theme implementation checkpoint

Current verified source: `3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb`.
Independent final review accepted `aeed3a0`; the lead accepted the two-file
V3-R preview correction above it through focused inspection under the narrow-fix
policy. Final real-VPN HTTP/browser verification passed and was accepted by the
lead. The registered preview remains running. See the final V3 section below
for exact source, service and evidence. Publication/CI remain lead/E0-owned;
external VPN-client reachability, human translation approval and production
readiness are not established here.

V2 is folded into V1, with D7/T3/T2/C0/E0 replay equivalence recorded below.
Earlier sections retain their historical checkpoint heads and coverage limits,
including the first accepted V1 checkpoint `c2103bc` atop A1 `d7b90f0`.

## Source boundary and result

One focused V1 commit changes 24 files: layouts and media/comment/sidebar helpers,
CSS, bilingual UI labels, Hugo configuration, `bin/check`, the exact native
`content/_content.gotmpl` archive adapter, and `static/theme/` assets/provenance.
Of 1,457 added lines, 674 are the standard GPL text; CSS is formatted for review.
The owning theme notice records source attribution and copied-image hashes.

The real logo/server photo retain importer-owned legacy upload paths. The theme
copies the actual Tux CTA and three specifically authorized public PNGs; all are
served locally. It uses the measured Arial/Verdana stack without font services.
The original navy palette, 1200/300/900 desktop layout, 162px mobile header,
article spacing, code presentation and keyboard-operable mobile sidebar replace
the generic scaffold. Search is visibly unavailable. English drafts display the
human-review notice; production excludes drafts. Production Discourse embedding
remains disabled.

Author/category/tag/month archives and pagination consume A1's public schema.
Native HTML `.Content`/`.Summary` preserve the source more split and anchors;
107 approved comments retain threading and `comment-ID`, `comments`, `respond`
anchors without a local posting form. Ten full Czech RSS items use the original
GUIDs and dates. Native Hugo 0.167 initially refused HTML; configuration explicitly
permits only the accepted HTML and Markdown content formats. A1's sanitizer
remains the authority for imported HTML/comment safety.

No Czech source, shared data or importer upload was edited by V1. Every emerging
English file was preserved and excluded from V1 staging. The index was empty
and yielded immediately after commit for translation/documentation work. No
database migration, history rewrite, feature push, main integration, firewall,
DNS, nginx or production change occurred.

## Checks and visual evidence

- `nix develop -c bin/check` passed on the final V1 patch with A1's complete corpus
  and concurrent untracked English drafts. It verifies dual production roots,
  reciprocal pairing, draft isolation, deterministic output, all manifest article
  routes/more/comment anchors, author/taxonomy/month archives, ten original feed
  GUIDs/full content, and local rendered image/srcset paths. A temporary draft
  proves media URLs in literal code remain unchanged while image URLs become local.
- Strict native real-corpus builds passed with `--panicOnWarning` and
  `--printPathWarnings`; 125 Czech articles, 6 authors, 9 categories, 32 tags,
  107 comments and all original article routes were exercised. V1-only
  `git diff --check` and staged whitespace checks passed. Imported source CRLF
  and whitespace were not normalized. No hook framework is declared or bypassed.
- All 156 canonical old-blog upload-prefix occurrences were inspected: 81 image
  `src` and 75 link `href` attributes, zero visible/code-text occurrences and zero
  other attributes. The finite renderer rewrites only media-bearing HTML tags,
  preserving source hashes and protected literal code. RSS uses absolute artifact
  host media URLs. Three exact Discourse image GETs were separately authorized;
  all returned HTTP 200/image/png and passed signature/dimension/digest checks.
- Local HTTP responses matched disk hashes for 152 unique referenced assets,
  including linked full images/PDF and the finite theme copies. Every rendered
  image/srcset is local; original YouTube/SuperLectures video iframes remain the
  intentionally supported remote media.
- Actual Chromium desktop 1440×1000 and mobile 390×844 captures cover the home,
  code article and threaded-comment article. Six views reported zero failed HTTP
  requests, broken images, external image/font/style/script requests or document
  overflow. Keyboard Space opened the mobile sidebar. The original and new home
  canvas/sidebar/article widths, title and metadata positions, font sizes and
  content padding match at both viewport sizes.

Side-by-side originals/new renders are beneath `theme-reference/`:

- [Desktop home](theme-reference/compare-home-desktop.png) and
  [mobile home](theme-reference/compare-home-mobile.png).
- [Desktop code](theme-reference/compare-code-desktop.png) and
  [mobile code](theme-reference/compare-code-mobile.png).
- [Desktop comments](theme-reference/compare-comments-section-desktop.png) and
  [mobile comments](theme-reference/compare-comments-section-mobile.png).
- `compare-comments-{desktop,mobile}.png` additionally shows article openings;
  `new-mobile-drawer.png` shows the keyboard-tested drawer. Raw measurement files
  are `reference-metrics.json` and `new-computed-styles.json` in that directory.

Lead inspected the actual desktop comparison and accepted close identity/layout
matching. Explicit differences remain: language/navigation links, localized UI,
disabled-search notice, archive-comment explanation, no local reply form or
email-derived avatar requests, and improved mobile reply indentation. A1 records
omitted WordPress `wptexturize` as an exception for all 125 articles; source-visible
text is preserved, while complete typographic equivalence is not claimed.

## Running real preview

- Czech: <http://aitherdev.int.vpsfree.cz:4567/>.
- English drafts: <http://aitherdev.int.vpsfree.cz:4567/en/>. Coverage is still
  growing; this checkpoint does not claim all 125 English drafts are complete.
- Registered service: `blog-vpn-preview-real`, ID
  `621e26d1-801f-4fbf-b1b7-72441fab0fe3`.
- Registry: `6d35d71b-dca8-43dc-9b68-5f4f0b37af7d`.
- Working directory:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog`.
- Exact registered runtime command:
  `/run/current-system/sw/bin/nix develop -c bin/preview --vpn`.
- The former synthetic VPN service `70dd830c-701f-48ba-9116-341eae1edd67` was
  stopped and retired using ordinary registered commands under the explicit
  preview-update authorization. The original loopback service
  `b0930238-6cc2-4cc0-b511-e1d36c306067` remains untouched. No session was stopped,
  archived or deleted. The real preview stays running and watches source changes.

The preview serves source including ongoing English drafts; it is not a final
immutable artifact receipt. No new Nix artifact was built for this checkpoint;
final source/input/artifact identities must be captured after all intended work
is committed and combined review passes. Local listener/browser success does not
prove a separate VPN client's route through its firewall/DNS path.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.

## V1-L legacy article links

Accepted follow-up `0ba7ca99fe3f58150e82421b7a698869c236aa35`, parent
`2635a3e6606a555442916ba1f3dc71d948dc39dc`, changes only the existing render
partial and `bin/check` (105 added lines). English anchor hrefs with an exact
known Czech article path now use that article's stored absolute `discussion_url`,
preserving query/fragment suffixes. Pre/code regions, comments, prose,
absolute/protocol-relative/unknown/media/query-only/anchor-only links and unmatched
path variants remain outside the correction. Source files/hashes were not changed.

The final check passed for Content, Summary and RSS under production, dual
loopback and VPN static modes, including suffix entities/literal dollar signs
and quote variants. Native RSS normalization of other relative URLs remains
unchanged. All 1,052 Czech production output files were byte-identical before and
after. A snapshot of 125 Czech and 92 English sources contained nine/eight known
anchors respectively; all 51 assertions across three modes passed. The initial
architect observation covered only 45 English drafts/four matching anchors.
Neither observation establishes final 125-English coverage; that check remains due.

Existing VPN responses for `wp-123` and `wp-205` returned 200 with the corrected
Czech destinations. No service was changed or restarted. The correction is to be
folded into unpublished V1 history before final review, with equivalence evidence;
no consolidation or push was performed in this package. Index ownership was yielded
immediately after commit. Lead owns the next allocation and final review.

### V1-L consolidation

The lead authorized the planned unpublished-history consolidation. It completed
with clean tracked files/index, no conflicts and no stash/reset/clean operation.
Final head: `e9c286b2f403603907265ac28f4bd38b3ae00227`.

| Logical commit | Old | Consolidated |
| --- | --- | --- |
| Published initialization | `0354dac281978867ea8c1553b092ce19bccb5ccd` | unchanged |
| A1 import | `d7b90f09e1edd6fb2b032057205c91d6df5c94ee` | unchanged |
| V1 theme | `c2103bcce91d2c93e2d7032c05a92c1375c6693a` | `818202f7b48e8031acb49641360b2402bc4e679b` |
| D7 docs | `2635a3e6606a555442916ba1f3dc71d948dc39dc` | `e9c286b2f403603907265ac28f4bd38b3ae00227` |
| V1-L fix | `0ba7ca99fe3f58150e82421b7a698869c236aa35` | folded into V1 |

`git range-diff d7b90f0..0ba7ca9 d7b90f0..e9c286b` shows only the accepted
two-file correction added to V1, D7 patch-equivalent (`=`), and the standalone
fix removed. `git diff 0ba7ca9 e9c286b` is empty: the entire final tracked tree
equals the tested pre-consolidation tree, both
`db3cf07edd6924544899fe454d5cc7767cc8d151`. D7's old/new stable patch ID is
`f14abbfde5962d8289f6780e2698b1bdfc5c734a`. All 113 untracked English drafts present
at the initial snapshot retained their exact bytes; newly emerging drafts were
untouched. There are no database migrations or dependency/pin update streams.
No builds were repeated for this source-equivalent history change. No push,
default integration, production change or service command was performed. Index
ownership was yielded after recording the result; final 125-English coverage
and combined independent review remain outstanding.

## C0 and final English coverage

Accepted C0 head: `b6b76192c61802c37fbc6cfdc0133c0bec1b3f07`, parent
`c3786b74af9ee9382af4cc44428e7e77965753ea` (the actual final T2 commit).
The commit changes only `layouts/partials/discussion.html`, `hugo.toml`,
`bin/check` and `docs/discussions.md`: 146 additions and one deletion.
Lead directly checked the documentation wording. E0's untracked workflow and
packager were preserved; index ownership was yielded immediately after commit.

Discourse remains off by default. Rendering requires an explicit boolean opt-in,
static production (never `hugo.IsServer`), a non-draft article, the exact CS/EN
production base URL and validated shared HTTPS Czech article identity. JSON-safe
serialization supplies one shared URL to the native embed; no local script asset,
API key, provisioning command or build-time request is introduced. Historical
comments and forum navigation remain independent. The feature documentation owns
the operator prerequisites: installed-version/source-path/category/extraction
checks, public `.org` framing and top-level login/reply behavior, notification
effects and separately approved setup/transition. None has been performed here.

Final `nix develop -c bin/check` passed with C0's isolated local static cases:
default-disabled production, explicit enabled production, both preview environments,
drafts, wrong origins/source URLs, identical language discussion identities and
escaped JSON. The emitted loader was also tested in cached Chromium after replacing
fixture values with synthetic `forum.invalid` and `source.invalid` URLs; all
requests were intercepted and aborted. Each language attempted only the synthetic
embed script. No actual forum URL was opened, and no test server was launched.

Final translation/legacy-link coverage now supersedes the partial observations:

- Exactly 125 Czech and 125 English article files; all English entries remain
  unreviewed drafts without fabricated human reviewer/date fields.
- All 125 translation source hashes match the exact generated Czech files and
  import manifest. Dates, taxonomy associations and source href/src/srcset values
  match; V1/C0 did not rewrite any article source.
- All 250 explicit article paths are unique within the single-origin preview.
- Actual full static renders with drafts included solely for testing passed
  production-host, dual-loopback and VPN contracts: 750 article routes,
  canonicals and reciprocal language links; every English page carries its
  human-review notice, and default embeds remain absent.
- Nine known Czech anchors and nine corresponding English anchors passed all
  three modes (54 assertions). English links use the stored absolute Czech
  destination, while Czech targets remain unchanged. Both reported runtime
  examples were verified earlier on the existing VPN preview.

These draft-inclusive test outputs are not a release artifact. The normal
production check still excludes drafts. No Nix release build, source push,
default integration, forum/live-blog request, service operation or production
transition was performed in C0. No migration or dependency/pin stream was added.
Final independent review and E0 artifact/hosting preparation remain lead-owned
dependencies. V1/C0 fixes remain with implementer1; capacity is free after this
receipt, with no new implementation package assigned.

## V2 localization and final source consolidation

The lead approved the exact English taxonomy labels. V2 changed only
`layouts/partials/term-name.html`, `i18n/en.toml` and `bin/check`: 83 additions
and one deletion. English-only native Hugo i18n keys localize seven category and
two tag slugs; other labels retain their authoritative imported-name fallback.
Existing sidebar, archive and article callsites share that resolver unchanged.
No registry, data/schema changes or Czech prose edits were added.

Focused checks passed all nine category/32 tag labels in both language sidebars
and archive headings, including proper-name fallbacks, and all 125 English article
associations. Before/after checks proved 1,052 Czech production files byte-identical,
860 preview HTML paths unchanged and all 252 article/taxonomy/manifest input hashes
unchanged. English wording was supplied and accepted directly by the lead.

V2 was first committed as `13528a36342b557a61482ac7207d6e5aadc0ac3d` atop
E0 `c4cf0220e313600f568524fc040cd13159669df3`, then folded into unpublished V1
under an explicit exclusive history window. Published initialization and A1 remain
unchanged. The complete old/new mapping is:

| Logical commit | Before this fold | Final |
| --- | --- | --- |
| Published initialization | `0354dac281978867ea8c1553b092ce19bccb5ccd` | unchanged |
| A1 import | `d7b90f09e1edd6fb2b032057205c91d6df5c94ee` | unchanged |
| V1, including V1-L | `818202f7b48e8031acb49641360b2402bc4e679b` | `46286f9c7c9e4d1735ac598fa57d9446d1d992ae` |
| D7 docs | `e9c286b2f403603907265ac28f4bd38b3ae00227` | `57feaa92ceb6ce7fb96d479bb5b5a823a24cd7fd` |
| T3 English drafts | `e8aed2ef787217e8085d782e38a760cd51ddbd90` | `b16c7f46af7424cf3e8d1fcb0ed8227981b71033` |
| T2 English drafts | `c3786b74af9ee9382af4cc44428e7e77965753ea` | `ea8441f2f3cbd01e105798674caf0c3ce132e580` |
| C0 discussions | `b6b76192c61802c37fbc6cfdc0133c0bec1b3f07` | `f464781e488c66a0f4cf61c50eb4249240ad94a3` |
| E0 blog release source | `c4cf0220e313600f568524fc040cd13159669df3` | `aeed3a018d895b797e1b8d9b2863dd20c0dec8e0` |
| V2 correction | `13528a36342b557a61482ac7207d6e5aadc0ac3d` | folded into V1 |

`git range-diff d7b90f0..13528a3 d7b90f0..aeed3a0` shows V1 acquiring the accepted
V2 delta, D7/T3/T2/E0 equal, C0 with only changed check-function placement/context,
and the standalone V2 commit removed. The full supporting output is
[v2-history-range-diff.txt](v2-history-range-diff.txt).

Stable standard patch IDs are identical for both versions of each replay:

| Commit | Stable patch ID |
| --- | --- |
| D7 | `f14abbfde5962d8289f6780e2698b1bdfc5c734a` |
| T3 | `36e2426ebd45aa60e01afa6e2e7ef763f54b7564` |
| T2 | `26240b61866cbec5b119c7a3ec5c50a0f50d5311` |
| E0 | `418d87df2be768ba031eef4357391615ea8b472d` |

C0's standard patch ID changes from `7357a0fd20b5cd233edab75540f652ad2fab417b`
to `70357c433ff440baa863a94bfbc4f14b00d5558b` because the new taxonomy check
precedes its function and call. The old/new zero-context stable patch ID is
identical: `19bcef87a73a724def31ec22ece35967d41f7266`. These were the only
conflicts, resolved through the lead-authorized deterministic check relocation.
The final `bin/check` matches the saved pre-fold file exactly.

`git diff 13528a3 aeed3a0` is empty; both entire tracked trees are
`11ad8cd6f6ed97ecccad1f2ac7f7e3108663cac7`. All 250 article Git blobs and working
file SHA-256 values match the pre-fold snapshot. A1's generated Czech source and
manifest, already consumed by translations, remain intact. No database migration,
dependency/pin update stream, source-content conversion, broad reset/clean/stash,
push/default integration or production/service action occurred in this window.

At the final clean head, the single related known-quick batch passed:
`nix develop -c bin/check` and `nix develop -c bin/check-release` (one offline
packager fixture test). No long Nix artifact build or browser sweep was run before
independent review. The final tracked tree/index are clean and yielded; review
invocation and packet acceptance remain with the lead. Implementer1 retains
V1/V2/C0 findings ownership.

## V3 final VPN usability and V3-R correction

Final source is `3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb`, tree
`b5cc92ab3976a1edef6a945dd0e6e5b0f0c022c7`, directly above reviewed
`aeed3a018d895b797e1b8d9b2863dd20c0dec8e0`. Source/tree/index were clean
before and after the final browser run. No history was rewritten in V3-R.

The first V3 check found that simultaneous loopback and VPN Hugo processes
shared `public/en/`: the VPN English home exposed fixture content and a
`localhost:1314` canonical. The accepted repair changes only `bin/preview` and
`bin/check` (57 additions, 4 deletions). Each invocation now owns a fresh
`mktemp --directory` destination passed to native Hugo; no shared directories
were removed. Explicit `--real-vpn` assertions preserve the separate fixture-only
`--vpn` checks. The lead inspected the exact diff and accepted this direct
correction under mandatory-review sections 9/10, retaining the prior independent
review. Content, source hashes, data, dependencies, pins and migrations are
unchanged.

Only old real-VPN registration `621e26d1-801f-4fbf-b1b7-72441fab0fe3` was
stopped/replaced through registered service commands. The running replacement is:

| Property | Value |
| --- | --- |
| Service | `blog-vpn-preview-real`, `1c3a8df4-d6f2-4245-9fe7-1f3714e8568d` |
| Registry | `6d35d71b-dca8-43dc-9b68-5f4f0b37af7d` |
| Command | `/run/current-system/sw/bin/nix develop -c bin/preview --vpn` |
| CWD | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog` |
| Bind | `172.16.106.40:4567` |
| Observed unique destination | `/tmp/nix-shell.dKvUZf/vpsfree-blog-vpn.od3cRVjl` |

The original loopback service `b0930238-6cc2-4cc0-b511-e1d36c306067` was
untouched. No firewall, default branch, production or session lifecycle action
was taken.

The normal quick check passed before commit, including the regression proving
distinct output directories for loopback and two VPN invocations. After repair,
`nix develop -c bin/check --real-vpn` passed. Explicit HTTP checks used
`curl --resolve aitherdev.int.vpsfree.cz:4567:172.16.106.40 --noproxy '*'`
because local hosts override DNS. Eight endpoints returned 200 without redirects:
both homes, paired wp-615 articles, both ten-item RSS feeds and English Events/
network archives. Advertised canonicals/pairs, no-localhost, noindex, article
draft notice, localized taxonomy and absent production Discourse checks passed;
two representative local media responses matched disk hashes. Exact results and
article paths are [v3-http.json](theme-reference/v3-http.json) and
[v3-spec.json](theme-reference/v3-spec.json).

A fresh Luna/low browser utility passed eight English views in 11.626 seconds:
home, category, tag and long/code article at 1440×1000 and 390×844. All off-origin
requests were intercepted before network; none occurred. Local navigation,
proper-name fallback, paired Czech link, article review notice and keyboard
drawer passed. Mobile code scrolls inside its container; no document overflow,
broken local images or active Discourse was found. Approved remote video embeds
remain a supported exception, not a requirement to contact them during this run.
Evidence: [browser results](theme-reference/v3-browser.json),
[log](theme-reference/v3-browser.log),
[desktop home](theme-reference/v3-en-home-desktop.png),
[mobile home](theme-reference/v3-en-home-mobile.png),
[desktop code](theme-reference/v3-en-code-desktop.png) and
[mobile code](theme-reference/v3-en-code-mobile.png).

The lead separately verified the rooted final Nix artifact
`/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0`; V3 did not
duplicate that build. The lead accepted final local usability. This is local
VPN-listener/browser evidence, not an external VPN-client test, human approval
of translations or production activation/readiness. Implementer1 retains
V1/V2/C0/V3 findings ownership and is free after this receipt. Both previews and
the session remain open.
