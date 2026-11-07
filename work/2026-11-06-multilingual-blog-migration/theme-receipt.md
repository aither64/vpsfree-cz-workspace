# Theme and preview verification

Current B18 verified source: `7fa57c809d828e945b104f5ab3fa74f76a030a51`,
tree `b04e5ee1ffc13882bc04cca7e39328db1f998277`, above accepted E18
`06f88d14c5509281344cd6ae45036ba94a0e2799`. Final review, unique fixture/source
checks and eight focused actual browser captures passed. The parent and lead
inspected the long-scroll gutters/mobile pages; final B18 visual acceptance is
complete. Current VPN snapshot is `ac7cc609`. E18's 125 English reviewed/published
metadata and protected bytes remained unchanged during verification. This source/
native-preview milestone makes no rooted-artifact, publication or production claim.

Prior verified T16 source: `6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344`,
tree `c28f761c78714715a2c22e455782fa325188f12e`. Czech Piwik ID 4 and the
user-supplied English ID 10 apply only to static production output. Final review,
normal/release checks and owner0's rooted build passed. The lead accepted the
eight-endpoint HTTP privacy proof, including actual native Hugo server exclusion
under environment `production`. At that checkpoint real VPN `85ec` and guard
server `1f802` were left open; the T16 section records their exact evidence.
All 250 language files/125 IDs and data remained unchanged. No production
transition or analytics collection is claimed; publication remains lead-owned.

The prior accepted U13 runtime is scoped to
`92ed3dca3120ffa3acae1b6efda6dfa974fb9dce`, tree
`cd8e3e7de8434fefd391e7ccf7706b74801fe019`: twelve same-line form cases passed.
Its exact historical service and source evidence remains below. Configuration
work is separate.

U13 CSS commit `70631dd` keeps search inputs/buttons on one line. Earlier
accepted U12 runtime remains scoped to `b5e3ebe`; the historical receipts below
retain their exact heads and limits. The real snapshot and prior isolated
fixture remain open.

U12 CSS commit `ce0f031` supplies normal-flow mobile expansion. Earlier accepted
U10/S10/L11 runtime remains scoped to `b29f21b`; its broader Pagefind/pagination
proof is retained without another sweep.

U10 navigation commit `c829fbf` contains the left toggle and distinct pagination
states. Earlier U9 browser evidence remains scoped to `f0337fb`, and V3 evidence
to `3aec4d6`; their historical receipts and review boundaries are preserved.

Earlier V3 usability evidence applies to `3aec4d6`, with the lead's narrow-fix
acceptance above reviewed `aeed3a0` preserved below. The preview remains running;
publication/CI remain lead/E0-owned. External VPN-client reachability, human
translation approval and production readiness are not established here.

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

## U9 article alignment and English CTA source checkpoint

Lead accepted `3dff9d7dbf61d7bf7c76e10fd72929711cd2bbf7` directly above
`3aec4d6`, tree `da0b98b03193d87addb67eb4e30662123899a43c`. The focused
five-file commit has 53 additions and 2 deletions: `assets/css/site.css`,
`layouts/_default/baseof.html`, `bin/check`, `static/theme/NOTICE.md` and the
new `static/theme/branding/join-us.svg`. No article, taxonomy, source media,
dependency or migration changed. The clean index was yielded for editorial work.

Pagination is centered and wraps. Scoped rules center `aligncenter` images and
standalone block photos/figures while excluding inline emoji and explicit float
classes. Tables use centered shrink-to-fit boxes with bounded horizontal
scrolling; cell alignment and source HTML are preserved. The final actual
intrinsic-sizing/keyboard/image/icon/browser checks remain due after review.

The English CTA says “Join us”, links to `https://vpsfree.org/registration/`, and
uses a self-contained SVG derivative of the original 150×147 Tux/green-button/
arrow graphic. The English footer links to `https://vpsfree.org/`; the blog logo
retains its language-home target. Czech graphic bytes and destinations are
unchanged. Original PNG SHA-256 remains
`8b73dbbdbc5dfa666196bde128afb12652c0638ede5f9a905e3da7042343f5da`; the SVG
embeds those exact bytes. NOTICE records the derivative/tool/provenance without
asserting a media license. The lead inspected and accepted the native-size
[English CTA capture](theme-reference/u9-cta-english.png) and wording before commit.

`nix develop -c bin/check` passed, including the graphic/source-byte and bilingual
CTA/footer contracts. Focused whitespace, Python syntax and SVG checks passed.
Required baseline desktop/mobile pagination, wp841 image, wp367 table and both
CTA screenshots are saved under `theme-reference/u9-before-*`. The baseline
capture later stalled on a lazy image below the viewport; only that owned capture
browser was stopped and the helper corrected to load images eagerly. No preview
service was affected. No new server, restart, Nix artifact build, push/default,
production or forum action occurred. VPN service `1c3a8df4` and loopback `b093`
remain open. U9 findings and post-review browser verification stay with
implementer1; no additional package is executing.

After both editorial commits, the single final quick batch passed on clean
`f0337fb7eae8797efca9254cd7208949cb0f77e4`, tree
`b80d2261d92efe01c51946f97fec5cd45b32b0fe`: `nix develop -c bin/check` and
`nix develop -c bin/check-release` (one offline packaging test). Source/head/tree
and clean status were unchanged afterward. No browser or long build ran in this
batch; mandatory final review remains the dependency for U9 browser verification.

### U9 final browser verification

After reviewer0 accepted the complete `f0337fb` series with no findings, one fresh
pinned Luna/low utility ran the bounded browser batch. It passed 11 views in
14.074 seconds (exit 0): desktop 1440×1000 and mobile 390×844 Czech/English homes,
English wp841, wp367 and wp828, plus wp847's actual table at 320×844. Explicit
blog-worktree pre/post assertions confirmed exact `f0337fb`, clean source/index
and unchanged source. The utility's incidental subsequent Git command ran from
workspace tracking CWD; the browser script's explicit blog CWD is the source
identity authority. No check was repeated for that unrelated observation.

The target remains service `1c3a8df4-d6f2-4245-9fe7-1f3714e8568d` at
`http://aitherdev.int.vpsfree.cz:4567`, using the already isolated destination.
All off-origin requests were intercepted before navigation; none occurred.
There were zero broken local images, failed local responses, document overflow
or active Discourse embeds. No server, source or artifact build was launched or
changed by this verification.

Measured behavior:

- Pagination rows are centered at x=870 on desktop and x=195 on mobile;
  `flex-wrap:wrap` is active, links remain contained and one current-page marker
  remains. The current controls fit on one row at 390px.
- The wp841 linked screenshot remains 275×157 and is centered at both sizes;
  its local full-image link is preserved. The revised opening is actually served:
  “You can now use passkeys” followed by “As a second factor, vpsAdmin accepts a
  passkey …”. This verifies runtime freshness, not human editorial approval.
- wp367's table shrinks to 454.16px inside the 720px desktop column and fits the
  330px mobile column. Header cells retain centered alignment and data cells
  retain start alignment; native table semantics remain present.
- At 320px, wp847's table stays inside its 260px article column while 401px of
  content scrolls internally. Focusing the actual table and pressing Right Arrow
  moved `scrollLeft` to 40px without moving the page horizontally. wp367's small
  mobile overflow was also keyboard-scrollable.
- wp828's standalone images center while its actual 20px emoji stays inline.
  Temporary browser-only inline-icon/left-float/right-float probes retained
  `inline`/`left`/`right` behavior and were removed from the DOM; no corpus file
  was changed.
- Both CTA images load at native 150×147 with the expected translated alt text,
  registration targets and footer destinations. Keyboard navigation reaches
  each CTA with its 3px focus outline; the mobile drawer operates by keyboard.
  Logo links retain each language's local blog home. External links were checked
  as attributes and were never opened.

Machine evidence: [u9-after.json](theme-reference/u9-after.json) and
[utility log](theme-reference/u9-final-browser.log). Before/after captures include
[pagination before](theme-reference/u9-before-en-pagination-mobile.png) /
[after](theme-reference/u9-after-en-pagination-mobile.png),
[linked image before](theme-reference/u9-before-image-desktop.png) /
[after](theme-reference/u9-after-image-desktop.png),
[table before](theme-reference/u9-before-table-desktop.png) /
[after](theme-reference/u9-after-table-desktop.png),
[keyboard-scrolled narrow table](theme-reference/u9-after-narrow-table-320.png),
[English CTA](theme-reference/u9-after-en-cta-mobile.png) and
[Czech CTA](theme-reference/u9-after-cs-cta-mobile.png).
Additional desktop/mobile captures use the same `u9-before-*`/`u9-after-*` names.
The parent inspected actual image/table/narrow-table/pagination screenshots.

U9 verification is complete. The preview and original loopback service remain
running; source/publication/defaults/production/session lifecycle were untouched.
This proves local preview usability only, with the same external VPN-client and
human-translation/production limits above. Implementer1 retains U9 and prior
findings ownership; capacity is free after this receipt.

## U10 left mobile-navigation source checkpoint

Under the bounded direct lead brief, `957e6f629942dfd14efb759cfb029a0163a86fb9`
adds three and removes three lines in `assets/css/site.css` only, atop `f0337fb`.
Tree: `3b5220a1f3b609afd2f1fa91bb50cef232fee081`. Within the existing
max-width 1199px rule, the label moves from `right:0` to `left:0`, its divider
changes to `border-right`, and the overlaid checkbox moves from `right:4px` to
`left:4px`. The existing checkbox/label, keyboard/focus rules, left drawer,
overlay behavior and desktop rules remain intact. No template or label change
was needed; article/content/media/dependency/migration inputs are unchanged.

Focused owned/staged `git diff --check` passed and the exact one-file diff was
inspected before the ordinary commit. The worktree/index are clean and the
exclusive index window was yielded promptly. No browser, build, service,
publication/default/production or lifecycle action ran. Actual 390px/320px
placement, open/close, focus, unobscured closed-state content and desktop behavior
remain due in the final joint browser batch after search review. Implementer1
retains that U10 verification and findings ownership; previews remain open.

The user then added pagination-state clarity to the same bounded package. The
lead accepted the visual plan, and authorized amending the unpublished commit.
Old `957e6f629942dfd14efb759cfb029a0163a86fb9` / tree
`3b5220a1f3b609afd2f1fa91bb50cef232fee081` becomes
`c829fbf4abcd7f7ab47b44386b3d12ec39090b55` / tree
`ace33dfa22b03275de7418e77a07872bd27c29b5`; parent `f0337fb` is unchanged.
The original sidebar delta is retained exactly and 27 CSS lines add native
pagination-state presentation, for one final one-file commit of 30 additions and
3 deletions. No published history or other source tree was rewritten.

Read-only HTTP inspection of actual first, middle (7) and last (13) pages found
native `aria-current="page"` without href for current items, `aria-disabled="true"`
with no href and tabindex -1 for disabled controls, and real hrefs for usable
pages. No template change was needed. Current pages have a filled navy/white bold
marker (11.75:1 contrast); usable links are dark blue (5.14:1 on white), with
underlined hover/focus feedback and the existing focus outline. Disabled controls
are muted with default cursor and inactive pointer behavior. Centering/wrapping
and native ARIA/link semantics remain. Focused/staged whitespace checks passed;
the clean CSS/index window was yielded. Actual first/middle/last presentation and
390px/320px navigation checks remain in the final joint post-review browser batch.

### U10/S10/L11 accepted preparation — historical plan

Preparation reads D10/D11 and accepted S10 `95a3cae`, without repeating its
source checks. The final L11 head, mandatory review, rooted artifact and free
watcher slot are prerequisites. Lead must separately release exact service
operations. Nothing had run at this preparation checkpoint; execution is recorded
in the following section.

1. Bind the final clean blog head/tree. Recheck the current real-VPN registration
   `1c3a8df4-d6f2-4245-9fe7-1f3714e8568d` before replacing only it through
   `dev-session service stop/run`. New registered command is
   `nix develop -c bin/preview --vpn` in the existing blog worktree; record its
   new ID and unique snapshot destination. Preserve loopback `b093`, all old
   outputs and result links. No session lifecycle action is included.
2. One bounded browser operation covers actual VPN desktop 1440, mobile 390/320:
   first/middle/last pagination states and focus; left toggle/hit area, keyboard
   and pointer open/close, drawer alignment, unobscured closed-state content and
   unchanged desktop; native CS/EN sidebar search, body-term results and correct
   language/root URLs, input/status/More, blank/no-match, one injected local
   Pagefind load failure and reload recovery, plus no-JS fallback. Read wp123's
   English article destination and wp455's mapped KB section/unmapped `#cli`
   href attributes only. All off-origin requests are aborted before navigation;
   no registration, forum or KB target is opened.
3. A single new registered loopback fixture at `127.0.0.1:4568` uses a plain
   `git archive` copy of the reviewed final head under a unique
   `/tmp/blog-u10-fixture.XXXXXXXX`. Only copied `fixtures/content` and
   `fixtures/data` are changed. Keep existing fixture mounts/data isolation.
   From the copy in the cached Nix shell, render Hugo with environment `vpn`,
   drafts, config `hugo.toml,fixtures/hugo.toml`, base URL
   `http://127.0.0.1:4568/` and a fresh destination; run
   `bin/index-search DEST --single-root`; then native Hugo server with the same
   environment/config/base URL/destination, bind `127.0.0.1`, port 4568,
   `--watch=false --disableFastRender --disableLiveReload`. Preserve Pagefind
   output; add no product flag, custom server, cleaning option or renderToDisk.
4. Use copy-only body/title positives and tag/sidebar/comment-only negatives.
   While fixture A serves, edit a paired body token, add one temporary draft
   pair and remove the existing unpaired fixture. Prove A's HTML and search
   remain coherent and old. Stop/re-register only this owned fixture with a fresh
   destination; reload the same browser tab and prove edited/added results,
   absent old tokens/deleted page, and fresh index loading. Authoritative 250
   articles/metadata remain unchanged. The final fixture stays registered unless
   separately authorized otherwise.
5. Serve final immutable artifact bytes through a finite Playwright response
   fixture, avoiding another HTTP server: production English `/search/` with a
   query must show its empty state without requesting missing Pagefind files.
   Parent owns any registered service/copy mutations; one fresh pinned Luna/low
   utility monitors the bounded operation's transferable log/status. Record
   exact source/service/fixture/output identities, screenshots and limits once.

No builds, browser, source/index or service changes occurred during preparation.
Search findings stay with implementer0, rendered-link findings with implementer2,
and U10 navigation/verification findings with implementer1. No optional crawl or
new test framework is proposed.

### U10/S10/L11 final runtime result

After final review and owner0's rooted build/utility-slot yield, the authorized
runtime batch passed at exact clean `b29f21b`, tree `15e46f8`. Explicit blog-CWD
head/status checks and SHA-256 comparison against
[u10-source-before.json](theme-reference/u10-source-before.json) prove all 250
authoritative article files and data remained unchanged. No application source,
index, default branch, production configuration or forum/KB content changed.

Running services under registry `6d35d71b-dca8-43dc-9b68-5f4f0b37af7d`:

| Service | Registration / bind | Source and output |
| --- | --- | --- |
| Real VPN preview | `8990b341-2956-4c6c-a2d8-8bf314c98d7d`, `172.16.106.40:4567` | Existing blog worktree, `nix develop -c bin/preview --vpn`; `/tmp/nix-shell.NRFxdd/vpsfree-blog-vpn.iR0OzDO6` |
| Final synthetic fixture B | `d2293739-8904-46b0-ba1a-2045ff019d5d`, `127.0.0.1:4568` | Archived-copy `/tmp/blog-u10-fixture.iclgei_p`; `/tmp/blog-u10-snapshot.0xY7SWgL` |

The parent first verified old VPN `1c3a8df4` against the authoritative registry,
systemd command/CWD and listener, then stopped only it and registered the new VPN
snapshot. Original loopback `b0930238-6cc2-4cc0-b511-e1d36c306067`, other services,
all old outputs and result links were preserved. Fixture A
`baa40ed2-5dfb-4b11-ba76-2a39de6a05d3` used
`/tmp/blog-u10-snapshot.xkhs61gZ`; it was stopped only for the planned fresh-B
rebuild. The final fixture uses the same native pipeline and explicit reviewed
blog flake for its cached shell, while Hugo/index/server CWD remains the copy.
Both final previews and the session remain open.

Passed behavior, without repeating earlier passed views:

- Twelve navigation views cover first/middle/last pages at 1440/390/320 and the
  desktop/mobile toggle states. Current pages have the filled bold navy marker;
  usable blue links expose keyboard focus; disabled edge controls have no href,
  tabindex -1 and inactive pointer behavior. Rows remain centered and wrap on
  narrow screens. The left toggle and contained checkbox open/close the left
  drawer by Space and pointer; closed-state article content remains unobscured.
- Actual Czech and English sidebar GET searches for `KeePassXC` return the paired
  wp841 article at the correct language's explicit origin-root URL. Blank input
  shows the prompt; `zzqxnomatchneedle` returns zero in both UI and native API.
  Broad `VPS` searches expose More and grow from 10 to 20 results in each language.
- One deliberately aborted local `en_5383bc6.pf_fragment` request produces the
  explicit error, clears results and exposes reload. Same-tab reload recovers.
  A JavaScript-disabled context displays the required fallback.
- Isolated fixture title/body positives match, while sidebar/tag and historical
  comment-only sentinels do not. Copy-only edit/add/remove leaves snapshot A's
  HTML and index old. After the parent's registered refresh into a fresh output,
  the same browser tab reloads and finds the edited/new draft, loses the old token
  and removed result, and the removed HTML route returns 404. New English results
  retain their declared root paths. No fake article entered the real corpus.
- wp123's conference link resolves to the actual local English article. wp455's
  traffic section is `https://kb.vpsfree.org/manuals/vps/traffic#cli_monitor`;
  uncertified API `#cli` remains Czech. These attributes were read without opening
  external destinations.
- Exact immutable artifact
  `/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0` supplied English
  production response bytes through the browser's finite response fixture:
  `/search/?q=VPS` displays the empty state and requests no Pagefind bundle.
  Both real preview feeds retain 200/RSS; the English draft notice and paired
  Czech link remain present.

All browser contexts installed off-origin blocking before navigation. Three
approved YouTube embed requests were aborted before network, giving zero
off-origin page-request egress; no forum, KB or
registration page was opened. No active Discourse, document overflow, broken
local images or unexpected page errors occurred. This is local runtime evidence,
not an external VPN-client test, human translation approval or production rollout.

The last pending phase passed in 29.611 seconds, reusing the prior twelve
navigation views and Czech positive/blank proofs. Machine result:
[u10-runtime-result.json](theme-reference/u10-runtime-result.json); completing
[log](theme-reference/u10-runtime-pending.log) and
[exit status](theme-reference/u10-runtime-pending.exit).
Visual evidence includes [first-page mobile](theme-reference/u10-pagination-1-390.png),
[last-page 320px](theme-reference/u10-pagination-13-320.png),
[left drawer](theme-reference/u10-drawer-open-320.png),
[English More results](theme-reference/u10-search-en-390.png),
[load failure](theme-reference/u10-search-error.png),
[refreshed fixture](theme-reference/u10-snapshot-after.png) and
[empty production English search](theme-reference/u10-production-en-empty.png).
The parent inspected these actual saved layouts; no screenshot-polishing rerun
was made.

Verification corrections and their retained evidence are explicit:

- Archived-copy Nix auto-discovery selected `/tmp` and failed before Hugo. Failed
  fixture `e00d8993` was stopped only through the registered command; the corrected
  launch uses the explicit reviewed blog flake, then native copy-CWD commands.
  A later parent wrapper also used the wrong implicit flake; exact owned Nix PID
  2899587 was stopped before the browser driver began. Its log/status remain as
  `u10-runtime-wrapper-failure.*`.
- The first actual batch's checkbox assertion expected x=4, overlooking the
  native 4px checkbox margin. [Measured bounds](theme-reference/u10-checkbox-diagnostic.json)
  show x=8..38 contained in the visible x=0..40 toggle. Only the helper was fixed;
  passed views were retained in `u10-runtime-final.log` / `u10-runtime-resume.log`.
- Alphanumeric negative `u10nomatchzzqx` produced 47 results in both UI and native
  API, highlighting Czech “u”. Owner0 classified this as pinned-engine token
  interpretation, not stale adapter results. The
  [all-letter diagnostic](theme-reference/u10-search-alpha-diagnostic.json)
  proves native/UI zero; copy-only sentinels were changed using
  [the recorded map](theme-reference/u10-fixture-token-change.json) and a fresh
  fixture baseline. Old registration `2d55f2d8` and its output remain in history.
  No custom normalizer or broader engine-conformance work was added.

Fresh Luna/low observers monitored the initial attempts. When the observer tool
was unavailable for the remaining phase, the lead acknowledged the skill's
visible parent fallback; the parent continued with bounded log/status monitoring
and retained all registered-service/copy authority. No model was substituted.
Owner0 was explicitly told the utility slot was free for CI and no new browser
utility would launch. Search findings remain owner0's, link findings owner2's,
and navigation findings implementer1's. Runtime work is complete; capacity is free
after this receipt. The lead accepted final runtime at exact `b29f21b`; feature
publication/CI remain lead-owned. No default integration or production readiness
is claimed.

## U12/M12 mobile sidebar source checkpoint

The direct lead brief and architect D12 select normal-flow expansion. Commit
`ce0f031a1580e2db6e579ed8afeea3af27d5acf8`, tree
`df6229f9786fd98c947257e2f2591c69cab50537`, sits directly above published
`b29f21b`. It changes only `assets/css/site.css` (3 additions, 12 deletions).
At the existing mobile breakpoint, collapsed widgets use `display:none` and
checked widgets use `display:block`. Removing absolute positioning, viewport
height cap, nested overflow, offscreen transform/visibility/z-index and fixed
width gives natural available-width/height page flow; the article follows the
expanded sidebar. Left native control, focus rules, desktop column and
pagination/search styling are unchanged. No template change was needed.

Before-source captures of actual `b29f21b` at 390/320×844 show 2,858px of widget
content capped in a 682px nested scroll area. After a 600px document scroll, that
area ends at screen y=244 while the main article remains overlaid. Evidence:
[u12-before.json](theme-reference/u12-before.json),
[390px top](theme-reference/u12-before-390-0.png),
[390px scrolled](theme-reference/u12-before-390-600.png),
[320px top](theme-reference/u12-before-320-0.png) and
[320px scrolled](theme-reference/u12-before-320-600.png).

Focused owned/staged whitespace checks passed and the exact CSS-only diff was
inspected. No new mirror test or build ran. An intermediate unpublished local
commit `c1021012a354d151155083cde224b869fcd67a05`, tree
`1de178b06ec863bfbdac05413a8e1d555c2618a6`, was amended in the same exclusive
window to remove its retained 300px mobile width when D12's available-width
clarification arrived. Final history contains one new coherent commit; published
`b29f21b` is unchanged. The clean index/window was yielded to the lead.

Actual revised 390/320, short-landscape, both-language last-archive-to-article
document scrolling, post-scroll open/close, keyboard/focus, local navigation/search
and unchanged desktop checks remain due after joint review/preview refresh.
No article/data/prose/review-state/media/dependency/migration or service change
occurred. Real VPN `8990`, fixture `d229`, loopback `b093` and old roots/results
remain untouched. Implementer1 retains U12 findings and final verification.

### U12/M12/R12 final focused runtime — accepted

Final exact source `b5e3ebe54d9c42ab89142a1bcc50192e580fff10`, tree
`4e5248b97e53b7d34b9bf1a1ccf10d3ace54854d`, passed final review. After owner0
yielded its successful rooted-build slot, the parent verified old VPN `8990b341`
against the session registry, command/CWD and listener, then replaced only that
registration through ordinary registered commands.

| Property | Running real preview |
| --- | --- |
| Registration | `85709a13-baa3-4f4d-a062-72ec39e42f7f` |
| Bind | `172.16.106.40:4567` |
| CWD | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog` |
| Command | `/run/current-system/sw/bin/nix develop /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog -c bin/preview --vpn` |
| Unique destination | `/tmp/nix-shell.NuOzCH/vpsfree-blog-vpn.CUFkuSYJ` |

The focused read-only browser driver passed on its first attempt, exit 0 in
25.432 seconds. Both languages passed 390×844, 320×844 and short-landscape
844×390 cases. Expanded widgets are static, full-width and naturally
2,734.5 / 2,858.25 / 2,590px high, with no maximum height or nested vertical
scrolling. Document scroll reaches the last November 2014 archive link, then
continues into the article; pane scrollTop stays zero. The article follows the
pane, with no overlay, clipped bottom or horizontal overflow. After scrolling,
native Space closes the sidebar, hidden widgets are untabbable, focus returns to
the checkbox and pointer reopening preserves normal flow. Actual archive
navigation works in both languages. Desktop remains a 300px sidebar / 900px
article column with the mobile toggle hidden.

Exactly one English sidebar search smoke (`KeePassXC`) reaches the local English
wp841 result. Actual wp490 and all nine CLI attributes target
`https://kb.vpsfree.org/manuals/vps/api#using_cli`; the two moved destinations are
`https://kb.vpsfree.org/manuals/vps/backups#downloading_backups` and
`https://kb.vpsfree.org/manuals/vps/userns#user_namespace`. Attributes were read
without opening KB pages. No broader Pagefind, API, no-JS, failure, snapshot or
pagination test was repeated.

Off-origin blocking was installed before navigation. One approved YouTube iframe
request was aborted before network, with zero off-origin page-request egress.
There were no broken local images, active Discourse or unexpected page errors.
Explicit blog-CWD pre/post head/status and SHA-256 checks preserve all 250 article
files and data at this revision. No application/index edits, new fixture, extra
build, publication/default, production or session lifecycle action occurred.
The fresh observer interface remained unavailable in this member; the visible
monitoring-skill parent fallback used explicit flake/CWD and cached Node/Chromium,
with no active utility or model substitution.

Evidence: [machine result](theme-reference/u12-runtime-result.json),
[log](theme-reference/u12-runtime.log), [exit](theme-reference/u12-runtime.exit)
and [state/source hashes](theme-reference/u12-runtime-state.json). Captures include
[390px last widget then article](theme-reference/u12-en-390x844-last-widget.png),
[320px keyboard-open sidebar](theme-reference/u12-cs-320x844-open-top.png),
[short landscape](theme-reference/u12-en-844x390-last-widget.png) and
[actual wp490](theme-reference/u12-wp490-cli.png); the complete six-case captures
use `u12-{cs,en}-{width}x{height}-{open-top,last-widget,article}.png`.
The parent and lead inspected actual saved layouts; the lead accepted the result.

The new VPN preview, fixture `d229`, loopback `b093`, all old roots/results and
the session remain open. No external VPN-client, human translation approval or
production-readiness claim is made. U12 findings remain implementer1-owned; link
findings remain owner2's. Capacity is free and no more utility/check/service work
is planned.

## U13 one-line search source checkpoint

Under the bounded direct lead brief, commit
`70631dd0dab3dbc3386a826de6ef95462897b0a6` sits above `b5e3ebe`, tree
`eeb40abb44c022b3cb010e5e132753a4fe1b0409`. It changes only
`assets/css/site.css` (7 additions, 7 deletions). The sidebar previously gave
its input width 100% and the button a top margin; dedicated controls already
used flex but enabled wrapping at the small-screen breakpoint. Both now use a
nonwrapping flex row with an 8px gap, flexible minimum-width-zero inputs and
buttons that retain their size and unbroken labels. Sidebar top margin and the
mobile wrap override are removed. Native form markup, GET/name=q, labels,
Pagefind/no-JS behavior, U12 document flow, desktop columns and pagination are
unchanged. No new prose or template adjustment was needed.

Focused owned/staged whitespace checks passed and the CSS cascade/diff was
inspected before the normal commit. The final source/index are clean and the
exclusive CSS/index window was yielded promptly. No browser, service, build,
article/map/docs/workflow/dependency or production action occurred. Actual
CS/EN sidebar and dedicated-page geometry/input usability/button focus at
320/390 and desktop remain for the focused post-review browser pass; retain
existing broader search proofs. Previews `857`, `d229`, `b093` and all old roots
are untouched. U13 verification and findings remain implementer1-owned.

### U13 final verification preparation — historical plan

Prepared against clean final blog `45d04bc2be31b071cfe4011bab60ddf6d45322f5`,
tree `f5fddf0e2c6ce577fe8f11fa6096718b3807078c`, while joint review is pending.
The session-only helper [u13-runtime.cjs](theme-reference/u13-runtime.cjs) and
[explicit launch plan](theme-reference/u13-runtime-command.txt) are written;
no browser, build or service command was launched. Final review, lead release
and owner0's rooted-build/utility-slot yield remain prerequisites.

The single focused batch measures sidebar and dedicated search controls in
both languages at 320/390/1440px: same row, contained input/button, usable input
width, localized unbroken button, typing and keyboard focus. One positive term
(`KeePassXC`) exercises native sidebar GET submission and the dedicated submit
button, retaining the existing explicit-root English result. A small structural
assertion preserves U12 normal document flow; no sidebar traversal, pagination,
Pagefind API/error/no-JS/snapshot suite is repeated. Off-origin requests are
blocked before navigation. The helper records twelve form captures, result JSON
and exact source/hash pre/post proof.

The parent may later replace only real VPN
`85709a13-baa3-4f4d-a062-72ec39e42f7f`, after authoritative registry/CWD/argv/
listener verification and explicit release. Every Nix command uses the original
blog flake path and explicit CWD, with cached Node/Chromium. No new fixture is
needed; `d229`, `b093`, all old roots/results and the final preview remain open.
One fresh pinned monitor observes the bounded driver, with the skill's visible
fallback if its interface is unavailable; service authority stays with the
parent. These are prepared steps, not runtime evidence.

### U13 final focused runtime result

The D14 hold prevented any launch at the old `45d04bc` preparation checkpoint.
The lead subsequently released independent blog verification at reviewed
`92ed3dca3120ffa3acae1b6efda6dfa974fb9dce`, tree
`cd8e3e7de8434fefd391e7ccf7706b74801fe019`. Owner0's successful rooted build
`/nix/store/wmfrxjri1d8mss04l8n4bz05mm3dpngc-vpsfree-blog-0` and direct utility
slot yield satisfied the final runtime dependency. No configuration action was
included in that release or this verification.

The parent verified old real preview `85709a13-baa3-4f4d-a062-72ec39e42f7f`
against its session registry, systemd command/CWD and exact listener, then
stopped only that registration and launched the replacement:

| Property | Running real preview |
| --- | --- |
| Registration | `7b8d14f8-b374-4d6c-98e7-5017c7a02b28` |
| Bind | `172.16.106.40:4567` |
| CWD | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog` |
| Command | `/run/current-system/sw/bin/nix develop /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog -c bin/preview --vpn` |
| Unique destination | `/tmp/nix-shell.Wz5lmk/vpsfree-blog-vpn.Al83TwJi` |

The prepared read-only helper passed on its first attempt, exit 0 in 9.66 seconds.
Both sidebar and dedicated search forms passed in Czech and English at 320px,
390px and 1440px: twelve form geometries/captures. Inputs and buttons have equal
row positions, remain inside their content widths and retain the 8px gap.
Mobile inputs retain at least 167.03px on the dedicated page and 183.89px in the
sidebar; the desktop sidebar input remains at least 163.89px wide. Button labels
stay unbroken. Typing, Tab navigation and the visible 3px button outline passed.
Native form action, GET method and `name=q` remain intact.

One positive term, `KeePassXC`, submitted through the English sidebar GET form
and dedicated submit button, returned the expected explicit-root
`/two-factor-login-with-passkeys/` result. The small U12 continuity assertion
confirmed static natural-height sidebar flow and article position after the
expanded pane. No full search, sidebar traversal, snapshot, failure/no-JS or
pagination suite was repeated. Off-origin interception preceded every navigation;
there were zero off-origin requests, page errors or viewport overflow.

Pre/post source checks bind exact clean head and unchanged SHA-256 values for
all 250 language files plus data. Article identity comes from the current
`data/migration/source-manifest.json` `cs_file` paths and paired same-folder
English front matter, checking immutable `params.article_id` in both languages;
no historical `wp-*` directory naming is assumed. This was read-only browser
verification, with no application/index edits, additional build, source push,
configuration/API/tracker/default/production or session lifecycle action.

Evidence: [machine result](theme-reference/u13-runtime-result.json),
[log](theme-reference/u13-runtime.log), [exit status](theme-reference/u13-runtime.exit)
and [source/service state](theme-reference/u13-runtime-state.json). The twelve
captures use `u13-{cs,en}-{320,390,1440}-{sidebar,page}.png`, including
[320px Czech sidebar](theme-reference/u13-cs-320-sidebar.png),
[320px English page](theme-reference/u13-en-320-page.png),
[390px English sidebar](theme-reference/u13-en-390-sidebar.png) and
[desktop Czech page](theme-reference/u13-cs-1440-page.png).
The parent and lead inspected actual saved captures; the lead accepted final
blog runtime at exact `92ed3dca`. The observer interface remained
unavailable in this member; the visible permitted parent-monitor fallback used
the explicit original blog flake/CWD and cached Node/Chromium. No utility remains
active; owner0 was directly notified the slot is free and no further utility
will launch.

The final real preview, fixture `d229`, loopback `b093`, all older roots/results
and session remain open. External VPN-client reachability, human translation
approval and production readiness remain outside this result. U13 findings and
follow-up verification remain implementer1-owned; capacity is free after the
receipt, with no further checks or service actions planned.

## T16 production Piwik preparation — English ID pending

Against published `92ed3dca`, six owned paths are dirty and uncommitted:
`hugo.toml`, `layouts/partials/piwik.html`, `layouts/_default/baseof.html`,
`fixtures/hugo.toml`, `bin/check` and `README.md`. The tracked diff is 71 additions
and 5 deletions, plus the new 16-line partial. No index entries were staged.
Czech language configuration uses blog site ID 4; English has no configured ID.
The main websites' IDs 1/6 are not used for the blog. The partial requires a
production environment, a non-server render and a positive configured ID;
synthetic fixture configuration sets both language IDs to zero.

The source snippet was recovered through one authorized read of
`https://blog.vpsfree.cz/`, HTTP 200, 39,749 bytes, UTC
2026-11-07T16:54:09.572077Z–16:54:09.672133Z, SHA-256
`733b92bfec02279058a983099051f025969f05936fe0c6b80e88c44598755ccb`.
Lines 256–268 show `_paq` page views, link tracking, site ID 4, protocol-relative
`piwik.vpsfree.cz/piwik.php`, asynchronous/deferred `piwik.js` and the no-JS
image. The partial preserves these options and fixed endpoint, substituting
only the language ID. No tracker script or collector was fetched or executed.

Focused native HTML-only renders passed 71 documents across production with
isolated English IDs 91/0/-1, preview with 91 and VPN with 91. Production positives
use the expected ID and matching no-JavaScript pixel; unset/zero/negative IDs
omit tracking. Preview and VPN output omit it despite the positive test ID.
A production build of synthetic draft fixtures also omitted both tracker and
pixel on every HTML document. No server was launched: the additional
`hugo.IsServer` source guard remains explicit. Python syntax, TOML parsing and
owned whitespace checks passed. The focused existing check additions retain
the local search-script allowlist and allow only the exact production loader
and matching no-JS pixel; Hugo redirect documents do not use the base layout.

The README's two sentences were contextually accepted by the lead. No analytics
framework, banner, new tracking option, source article/data, deployment/settings,
service, artifact build, publication/default or production action was added.
Normal/release checks and the one final coherent commit wait for the actual
English numeric ID, confirmed sharing of 4, or an explicit Czech-only decision.
That decision remains lead/user-owned; Piwik access/provisioning diagnosis is
architect0's independent package. Existing preview `7b8`, fixture `d229`, loopback
`b093` and all roots remain untouched. T16 implementation/findings ownership is
retained, ready for interim acceptance or parking at this dependency; the index
is empty and available for lead-coordinated work.

### T16 final source checkpoint — CS 4 / EN 10

The user supplied English blog site ID 10; the lead resumed T16 with that
authoritative value. Commit `6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344`, tree
`c28f761c78714715a2c22e455782fa325188f12e`, sits directly above published
`92ed3dca`. Exactly six owned files changed, 90 additions and 5 deletions:
`README.md`, `bin/check`, `fixtures/hugo.toml`, `hugo.toml`,
`layouts/_default/baseof.html` and the new 16-line `layouts/partials/piwik.html`.
No published history was rewritten. The earlier parked preparation above is
historical; its English-ID dependency is resolved.

Both production language roots emit their configured ID and matching no-JS
pixel (Czech 4, English 10). The existing page/link tracking, fixed Piwik endpoint
and loader options are retained. Production environment, non-server render and
positive ID are required; fixture IDs are explicitly zero. The tests continue
to reject unrelated scripts and external images, allowing only the exact
production loader/pixel alongside the existing local search module. The approved
README wording describes that contract without adding a policy or banner.

One final related batch passed on the exact committed source tree, first attempt:
`nix develop` with the explicit original blog flake ran `bin/check` then
`bin/check-release`. Normal checks cover actual CS4/EN10 production output,
alternate positive/zero/negative IDs, preview/VPN/fixture absence, deterministic
dual roots and existing route/content/search/link contracts. The offline release
fixture passed one test in 0.187 seconds. Pagefind's existing Czech stemming note
is unchanged. No analytics script was executed and no tracker/collector request
occurred. The source additionally forces off `hugo.IsServer`; no server was
launched before review, so actual server-runtime verification is not claimed.
The fresh watcher interface was unavailable and the visible permitted parent
fallback monitored the single batch; no utility remains active.

Evidence: [check log](theme-reference/t16-final-check.log),
[exit 0](theme-reference/t16-final-check.exit) and
[source identity/hash snapshot](theme-reference/t16-source-before.json).
Before/after proof preserves 125 immutable IDs, all 250 language-file bytes and
draft states, plus data, environment configuration, assets, lock/dependency,
search/indexing/build inputs against published `92ed3dca`. Python/TOML syntax
and owned/staged whitespace checks passed. No content/review metadata, migration,
dependency update or configuration-repository change occurred. Ordinary hooks
were retained; no hook framework is declared.

The clean source/index window was yielded immediately after commit. Existing
preview `7b8`, fixture `d229`, loopback `b093`, all output/result roots and the
session are untouched and remain open. No browser, final artifact build, source
push/default integration, Piwik administration/settings or production action
occurred. Independent final review and any later artifact/runtime/publication
release remain lead-owned; T16 source/finding ownership stays with implementer1.

### T16 privacy/server verification — historical preparation

After final review, owner0's successful rooted `result-t16`/slot yield and lead
runtime release, replace only current real preview `7b8` through the registered
native VPN command with the explicit original blog flake/CWD. Preserve `d229`,
`b093`, every older output/result and the session.

One separate registered native Hugo server will prove the server guard while
environment is explicitly `production` and language IDs remain 4/10. Recheck
free loopback ports 4570/4571, use the existing two-language production config,
and run in the pinned shell from the exact blog CWD:

```sh
t16_server_destination=$(mktemp --directory /tmp/blog-t16-production-server.XXXXXXXX)
printf '%s\n' "$t16_server_destination"
exec hugo server --environment production --bind 127.0.0.1 --port 4570 \
  --config hugo.toml --destination "$t16_server_destination" --watch=false \
  --disableFastRender --disableLiveReload --panicOnWarning
```

Native multihost serving assigns Czech 4570 and English 4571; verify both exact
listeners/languages and the production environment in argv/logs. No prebuild,
indexer, cleanup, custom server or source/config modification is required. A
single HTTP-only eight-endpoint batch covers both VPN homes/articles/search
pages and both production-server homes. Parse status/language and absence of
Piwik inline `_paq`, tracker scripts and no-JS pixels without executing JS or
requesting images/modules/analytics endpoints. Bind the actual source/ID-language
hashes before/after. Leave the refreshed VPN and separate guard server open.
This is a prepared plan only; no server or HTTP check has run at this checkpoint.

### T16 final HTTP privacy/server proof — accepted

After final review and owner0's successful rooted `result-t16` build at
`/nix/store/5bs03cb3g49iyl4gb81sd6kma06bcmyk-vpsfree-blog-0` and direct slot
yield, the parent performed the exact authorized service operations. Old real
VPN `7b8d14f8-b374-4d6c-98e7-5017c7a02b28` was verified against the session
registry, systemd CWD/argv and exact 4567 listener, then stopped through its
registered command. No other existing service was changed.

| Running service | Registration / bind | Command and unique destination |
| --- | --- | --- |
| Real VPN snapshot | `85ec07f0-0780-4fc7-9739-bc84b32f3642`, `172.16.106.40:4567` | Explicit original-blog `nix develop ... -c bin/preview --vpn`; `/tmp/nix-shell.1OACGY/vpsfree-blog-vpn.yfBFSZgU` |
| Native production-mode guard probe | `1f802dce-e994-4125-9561-c3b8b1241f48`, `127.0.0.1:4570/4571` | Explicit original-blog Nix shell and the exact prepared `hugo server --environment production` command above; `/tmp/blog-t16-production-server.9KLH1OBd` |

Both commands use CWD
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog`.
The production probe used free ports and a fresh destination, with the unchanged
language IDs 4/10 and native two-host configuration: no overlay, prebuild,
indexer, cleaning flag or custom server. Its actual argv and startup log confirm
environment `production`, disk serving, Czech 4570 and English 4571.

One eight-request HTML-only batch passed on its first attempt, exit 0 in 0.175s,
at exact clean `6dae2b1` / tree `c28f761`. Both VPN homes, paired wp841 article
pages and search pages, plus both production-server homes, returned 200 with
the expected language and no redirects. Every response omitted `_paq`, the
Piwik loader/host and no-JavaScript pixel. This directly proves `hugo.IsServer`
exclusion despite positive configured production IDs. The parser recorded safe
HTML facts, body SHA-256, canonical URLs and script references without fetching
those references. Proxies and redirects were disabled. No JavaScript, browser,
asset/image/module or Piwik collector request occurred.

Current manifest paths bind 125 IDs / 250 language files; source/head/tree/data
hashes remained unchanged before/after. No source/index, admin/backend/SSH,
settings, configuration, push/default, production or session lifecycle action
occurred. The known subsecond HTTP batch ran inline under the accepted quick-check
policy; no utility remains active, and owner0 was directly notified the slot is
free. No broader UI/search/pagination/snapshot checks were repeated.

Evidence: [eight-endpoint result](theme-reference/t16-privacy-result.json),
[source/service/argv state](theme-reference/t16-privacy-state.json),
[HTTP log](theme-reference/t16-privacy-http.log),
[exit 0](theme-reference/t16-privacy-http.exit) and
[native production-server log](theme-reference/t16-production-server.log).
The lead inspected the actual result and accepted final privacy/runtime proof.
Both new services, `22b5`, `d229`, `b093`, all older roots/results and the session
remain open. External VPN-client reachability, human translation approval and
production analytics collection are not established here. T16 findings remain
implementer1-owned; capacity is free after this receipt, with no further checks,
source, utility or service work planned.


## E18 maintainer editorial acceptance of current English corpus

User explicitly directed: “you should also mark the english translations as
reviewed, it's fine”. This is maintainer editorial acceptance of the current125,
not a claim of a new human line-by-line review or agent-granted approval.
Commit `06f88d14c5509281344cd6ae45036ba94a0e2799`, parent
`6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344`, tree
`9384504c3cdc39a79a12d6519e062a665a5dad30` changes127paths:125
`content/posts/*/index.en.html` frontmatters plus minimal `README.md` and
`bin/check` expectations (525+/268-). Every English page now has
`draft = false`, `translation_status = "reviewed"`, the exact current paired
whole-CS-file SHA-256, `translation_reviewed_by = "maintainer (chat approval)"`
and `translation_reviewed_at = "2026-11-07T18:02:58Z"`. Article bodies, code
(including raw CRLF), title/date/lastmod/URLs/IDs/byline/GUID/media and all other
metadata remain exact bytes; every Czech file is unchanged. Data, immutable
legacy assets and pins were untouched. B18's disjoint CSS/image/NOTICE changes
were preserved; no whole-tree clean claim.

Source verification compared all125 body/frontmatter invariants and paired CS
bytes against the exact parent, executed existing `discover_articles` and checked
125 unique paired IDs/routes plus original ten-item feed order. Owned127file
bytes equal the committed blobs; staged inventory SHA-256
`9911a83cfd621f5ba111b6070bb3cc77778aa8464d0e6bb054f16acf7303ac1c`.
Normal commit used no bypass; the repository declares no hook framework.
Main applied writing guidance and accepted the two current-corpus README updates;
generic authoring/review policy remains intact.

One fresh pinned Luna/low full-access/never utility ran the established
`nix develop --command bash -c 'bin/check && bin/check-release'` batch to success
(exit0,83.317s). It checked production English Pagefind125 and nonempty search,
125 article routes per language, ten full-content feed items with stable GUIDs
for both languages, synthetic/draft isolation and deterministic output. All owned
hashes and captured B18 peer inputs stayed stable. No check/utility remains.
The first orchestration attempt failed before either check started because
`/bin/bash` was unavailable inside the Nix shell; its receipt is retained.
Diagnosis changed only the launcher to PATH `bash`; no executed test was retried.
No rooted Nix artifact build, browser, server, tracker/script request or remote
network was used. Earlier source/launch preflight mistakes were corrected before
execution (actual peer `NOTICE.md` filename and canonical worktree cwd).

Raw supporting receipts and SHA-256:
- `e18-translation-inventory.json`: `3ab77a07e330313fbb33cececbbc821b6eadafb8deafb0c2ed60062ceb97c20b`.
- `e18-source-check.json`: `fa115e56bbc56b16bc1ad06c9e9e34b0cc11e5c944b67082bc6852efec1ae9cf`.
- `e18-quick-r1.log`: `82e54222382ab286966143ea069f639064048462abf538441ed32321aaccf210`.
- `e18-quick-r1-status.json`: `e86e33c63ef162cc9c4d64d4521e1f976dd755de96e19e20597a5023f146f860`.

Index/shared-check ownership yielded empty directly to owner1 after commit;
B18 dirtyfiles stayed intact. This receipt append is complete and its boundary
is returned. No migrations, new framework or translated prose edits. No feature
or default push, production operation, cleanup or lifecycle action. Lead accepted
E18 source/quick evidence; combined intended-source final review/artifact/runtime/
publication remains with the lead. Owner3 retains metadata finding ownership and
is free after this receipt; no next package is executing.

## B18 continuous rack-photo source checkpoint

Commit `7fa57c809d828e945b104f5ab3fa74f76a030a51`, tree
`b04e5ee1ffc13882bc04cca7e39328db1f998277`, sits above E18
`06f88d14c5509281344cd6ae45036ba94a0e2799`. Exactly three owned files changed:
body declarations in `assets/css/site.css`, new
`assets/images/rack-background.jpg` and existing `static/theme/NOTICE.md`
(13 additions, 1 deletion plus the 907,355-byte image). E18's first check/index
window was respected; owner3 directly yielded it before the one fixture check,
and separately returned this receipt append boundary before this section.

The copied prototype is exactly 3000×1240, SHA-256
`f8e3a64a8be47585ee528889ff3ee185a6c69a2b54e95ebcd294406b08b3ff97`.
Original `foto5.jpg` remains byte-identical at SHA-256
`c12b042763402d09913308e7fb03933e0ec231f916291cbe2d404391fb1bff64`.
The fixed Hugo `resources.Get | fingerprint` image uses its local relative URL
with `repeat-y left top` and `background-size:max(100%, 3000px) auto`, retaining
the navy fallback and all other body/layout rules. NOTICE records source,
crop/384-row smoothstep overlap, encoding/tool version and derivative hash;
the lead accepted the wording and no separate media license is asserted.
No ImageMagick or other build dependency was introduced.

One pinned native Hugo preview fixture render with drafts passed in unique
`/tmp/nix-shell.50ws4s/blog-b18-fixture.r_kb_xd9`. Both `cs/` and `en/` contain
the identical fingerprinted JPEG and CSS referring to its local reachable path;
the byte hash, `repeat-y` and minimum-natural-width sizing match. All preview
HTML inspected remains tracker-free. Machine evidence and protected hashes:
[b18-fixture-result.json](theme-reference/b18-fixture-result.json).
Owned/staged whitespace checks passed before the normal commit; no hook
framework is declared or bypassed. Source/index are clean and the exclusive
index/check window was yielded immediately.

Content, data, all legacy uploads, environment configs, lock/flake, search,
base layout and analytics files stayed unchanged against the exact E18 parent
before/after the check. All 125 English entries remain reviewed and nondraft.
No Pagefind/full-search/normal-release suite was rerun; E18's retained full-check
evidence remains scoped to its packet above. No migration, pin/dependency stream,
source reset, long artifact build, browser, service, push/default integration or
production action occurred. Existing VPN `85ec`, production guard `1f802`,
`22b5`, `d229`, `b093`, old roots/results and the session remain untouched.

Final visual acceptance remains after joint review and explicit runtime release:
actual 1440/1920 exposed gutters below y=2008 and across at least two 1240px joins,
plus 320/390 mobile overflow/background containment and both-language local bytes.
Prototype contact sheets are supporting design evidence, not a browser pass.
B18 fixes, findings and that focused verification remain implementer1-owned.

Prepared helper: [b18-runtime.cjs](theme-reference/d18/b18-runtime.cjs) covers
CS1440/EN1920 at document scroll 900/2100/3300, plus CS320/EN390 mobile, for eight
actual captures. It checks the loaded local image hash in both languages and
privacy/containment; the parent and lead must inspect gutter joins for visual
acceptance. No browser or service is launched before explicit review/runtime
release, and no utility slot is reserved while other assigned work uses it.

### B18 focused native-preview runtime — accepted

After reviewer0's final all-lane pass, the parent verified old real VPN `85ec`
against registry/CWD/argv/listener and performed the authorized refresh. Current
registration is `ac7cc609-7322-4dc8-9693-430482b99fcb`, bound only to
`172.16.106.40:4567`, with CWD the initiative blog worktree and command
`/run/current-system/sw/bin/nix develop /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog -c bin/preview --vpn`.
Its isolated output is `/tmp/nix-shell.mobqij/vpsfree-blog-vpn.yKWveW9y`.

The first stop returned transient session-mutation exit 75; the parent
incorrectly continued and registration `d1e862e8-5a8d-4d1d-80a0-a4f508864ebd`
failed to bind while old `85ec` still served. This was an orchestration error,
not a product defect. The exact old stop was retried and confirmed successful;
only the failed new unit was then stopped through its ordinary registered
command. Both records remain in history and no output was removed. A free-port
and inactive-unit check preceded the corrected registration. No browser had run
during that failure. The [startup log](theme-reference/d18/b18-startup-failure.log)
and state retain the evidence; no private cleanup or lifecycle helper was used.

The first actual browser attempt passed eight captures in 7.139 seconds, exit 0:
CS1440 and EN1920 at document scroll 900/2100/3300 expose both gutters across
joins at y=1240/2480/3720 and below the old y=2008 cutoff; CS320/EN390 confirm
opaque full-width mobile pages without overflow. Four actual image responses
were HTTP 200, the same local fingerprinted URL, 907,355 bytes and exact
`f8e3a64...` digest. Computed repeat/sizing/scroll attachment match the design.
There were no broken images, page errors, active tracking or horizontal overflow;
off-origin blocking preceded navigation and no off-origin request was attempted.

The parent inspected all six desktop and both mobile frames: rack detail remains
upright and inspected wraps have no abrupt cutoff or pale-panel return. The lead
accepted the actual images: [1920 y2100](theme-reference/d18/b18-en-1920-y2100.png),
[1920 y3300](theme-reference/d18/b18-en-1920-y3300.png),
[1440 y3300](theme-reference/d18/b18-cs-1440-y3300.png) and
[390 mobile](theme-reference/d18/b18-en-390-mobile.png).
Other actual frames use `b18-{cs,en}-{width}-y{scroll}.png`; the Czech mobile is
`b18-cs-320-mobile.png`.

Machine evidence: [result](theme-reference/d18/b18-runtime-result.json),
[source/service/argv state](theme-reference/d18/b18-runtime-state.json),
[log](theme-reference/d18/b18-runtime.log) and
[exit status](theme-reference/d18/b18-runtime.exit).
Exact `7fa57c8` / tree `b04e5ee1`, 125 reviewed/published pairs, Czech/body/data,
legacy-photo/config/lock bytes remained unchanged before/after. The observer
interface was unavailable; the visible permitted parent fallback monitored the
bounded run, with no active utility or slot reservation. No full UI/search/
pagination/snapshot suite, artifact build, source edit/push, default integration,
production operation or forum/tracker request occurred. The snapshot source
window is yielded. Current `ac7` plus `1f802`, `22b5`, `d229`, `b093`, every old
root and the session remain open. B18 findings remain implementer1-owned;
capacity is free after this receipt.

## D19: native discussion setup and controlled opt-in

Completed source at blog `5032d82ffd43870aa7e0aa6dd332300e4ce2f3b4`, parent
`7fa57c809d828e945b104f5ab3fa74f76a030a51`, tree
`d157f979c9a189b835b796c9f502d0d68d7b0865`. Only `docs/discussions.md` and the
shared-discussion paragraph in `docs/authoring.md` changed: 181 additions,
32 deletions. Main-context writing review accepted the whole changed prose and
its concrete native-snippet pilot before commit. The source default remains
false; the partial, application code, content, metadata and input pins are not
changed by this commit. No migrations or repeated dependency-update stream.

The guide grounds the native admin host/category/author UI, future root-slug
Czech import namespace and reserved/query exclusions. An English host row with
reject-all `\A(?!)\z` permits CSP framing without English imports. It documents
`.entry-content` extraction, separate visibility settings (unlisted until reply,
not silent), existing RSS/mapping and notification preflight, a one-article
pilot after static public serving, explicit protected-main opt-in and recovery
that preserves topics, mappings and replies. The pilot uses the forum-generated
native script in temporary DOMs of the two production article tabs while source
stays false; the operator's requests can create topics and notifications.

Version-sensitive citations were checked against configured Discourse
`2026.9.1`, source `/nix/store/30w0v0ml6xzhg6vj1zzzk92b77y8xhfm-source`, retained
by `d19-discourse-source`, with exact source NAR
`sha256-j3JjLYNcv3lluoCekyUUKMfkSX/ExeDsa8zrQ+pDrwg=`. This is the fixed-output
source selected by nixpkgs `718f670e845328e9c2cecdd832835712b2cbd065`, not a
claim about the running forum or an independently resolved upstream Git commit.
Source-only cache fetch exit 0/9.3 s; see existing
`d19-discourse-source-fetch.log` and `d19-discourse-source-fetch-status.json`.

Quick checks passed: Ruby 3.4.9 under `nix develop` compiled the documented regex
and accepted all 125 authoritative source paths plus four future slugs; 55
reserved/numeric/nested/query/invalid cases were rejected. Seven encoded/decoded
fixtures exercise the pinned matcher's encoded-OR-decoded contract with Ruby's
standard URI percent decoder; this is not an executed Discourse dependency test.
The English deny-all rule rejected all 193 combined cases. Local checks passed
six document links/two heading anchors, two TOML examples, ten setting names and
the seven initial pinned source paths. The added native-loader citation and
its actual generated snippet/container/iframe behavior received an affected
source-path check. Source false/default, partial and existing `bin/check` bytes
matched the parent; authoring bytes outside the assigned paragraph matched too.
A first link verifier counted an existing inline-code example image as a real
link; excluding code fixed the verifier without a product change. Final staged
inventory was exactly the two owned paths; committed whitespace was clean.
Normal `nix develop -c git commit -F <message-file>` exited 0; this repository
declares no hook framework and no hooks were bypassed. Empty index and owned
committed-byte equality were verified, then the blog index/authoring boundary
was yielded directly to A18 owner0 before this record append.

No whole-site build/render, browser, live forum/API/SSH/account/topic/settings
request, workflow, service change, push or default integration was performed.
Installed version/live overrides/category/user/mappings, extraction of the final
public site, CSP/cookies/concurrent first visits and notification outcomes remain
user-run pilot facts. Independent final review is lead-owned; document/source
checks do not certify those runtime results. All retained roots, services,
fixtures and the session remain open; implementer2 retains D19 findings.
