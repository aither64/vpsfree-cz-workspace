# Multilingual static blog migration: proposed design

Architect: `architect0`, 2026-11-06. Planning only; no implementation, export,
translation, production write, repository creation, commit or deployment is
authorized by this proposal. Lead owns acceptance, plan/state and user writing.

## Recommendation and settled scope

Use **Hugo**, with one small Git repository containing content, templates,
assets, build definition and author guidance. A separate content-only repository
adds coordinated pins/releases without a current access-control benefit; split
later only if editorial permissions or asset volume justify it. The proposed
repository name `vpsfreecz/blog` is provisional and has not been created.

| Generator | Fit for this request |
| --- | --- |
| **Hugo** | Recommended: native multilingual content pairing, explicit translation keys, Markdown and static output suit a bilingual editorial archive. A small custom layout can reproduce the existing design without a client framework. |
| **Zola** | Credible alternative: multilingual files, translated routes and feeds are built in. No requirement here makes it preferable to Hugo. |
| **Astro** | Supports locale routing and is attractive for richer component-driven interaction. This blog currently needs little of that; more application assembly is unnecessary. |
| **Eleventy** | Flexible templates and a bundled i18n plugin; viable, but more site-specific conventions would need assembling for the same editorial result. |

User decisions relayed by lead:

- Preserve original Czech article URLs and the recognizable design. Recommend
  English below `/en/`; that URL convention remains a proposal.
- Preserve articles, authors and historical comments; keep old comments in their
  original language as a static archive. One future Discourse discussion serves
  both language versions. Reuse the existing Discourse account/signup rules.
- Git/Markdown publishing is suitable. Future articles will primarily be
  agent-authored, with a straightforward human workflow too. AI translation
  drafts require human review. Every existing published article needs a reviewed
  English translation for full bilingual launch; phased coverage needs a later
  explicit decision.
- Serve production from the **same existing blog VPS/container**. Supply an easy
  local preview. Preserve the existing `/feed/` for subscribers; bot configuration
  updates are allowed if needed, but cannot replace feed continuity.

## Evidence and limits

Seven successful upstream references were consulted, plus a small public sample;
there was no archive crawl, container access, export, build or runtime admin
inspection. One attempted upstream embed-JavaScript source URL returned 404;
the official explicit-ID example and controller supplied the needed evidence.

1. [Hugo multilingual content](https://gohugo.io/content-management/multilingual/):
   language variants and `translationKey` association.
2. [Zola multilingual sites](https://www.getzola.org/documentation/content/multilingual/).
3. [Astro internationalization](https://docs.astro.build/en/guides/internationalization/).
4. [Eleventy i18n](https://www.11ty.dev/docs/plugins/i18n/).
5. [Discourse native embedding](https://meta.discourse.org/t/embed-discourse-comments-on-another-website-via-javascript/31963),
   especially “Linking to existing topics”.
6. [Discourse upstream embed controller](https://github.com/discourse/discourse/blob/main/app/controllers/embed_controller.rb):
   inspected current upstream, **not proof of the deployed version**.
7. [WP-CLI export](https://developer.wordpress.org/cli/commands/export/): WXR
   contains content/authors/comments/attachment records, but not site options or
   attachment bytes. It cannot serve as the sole backup.

Public HTML/CSS sampled on 2026-11-06: [home](https://blog.vpsfree.cz/),
[one article](https://blog.vpsfree.cz/linuxove-distribuce-uzivatele-prechazeji-nejcasteji-na-rocky-linux-a-nixos/)
and [Flat stylesheet](https://blog.vpsfree.cz/wp-content/themes/flat/assets/css/main.min.css?ver=1.4.2).
The sample has a left sidebar with logo/tagline, search, recent posts, tags,
categories and archives, alongside a white article column with titles, dates,
bylines and excerpts. CSS provides responsive/off-canvas sidebar behavior.
The sampled article has a root `/slug/` canonical URL, WordPress ID 847 and
`#comments`; the logo uses `/wp-content/uploads/2014/11/vpsFree-bile1.png`.
This is a design reference, not a full content or browser-rendering inventory.

[Configuration findings](configuration-findings.md) are implementer0's accepted
bounded investigation of retained remote default
`85b38f1cd07d6b3a0fde3eefd32258f747e757e5`, without a fetch. They identify:

- `cz.vpsfree/containers/int.blog`: WordPress/MariaDB backend at `172.16.8.4`,
  uploads at `/var/lib/wordpress/blog.vpsfree.cz/uploads`.
- `cz.vpsfree/containers/prg/proxy`: public HTTPS proxy to that backend; preserve
  exact proxy-only HTTP access and trusted client-header handling.
- `cz.vpsfree/containers/discourse`: separate forum with OAuth and custom signup
  policy. Deployed version, category visibility and embed settings are unknown.
- Existing configuration pattern: pinned source input, Nix-built immutable site,
  nginx document root. IRC bot polls `https://blog.vpsfree.cz/feed/`.

## Content, URLs and lossless import

“Lossless” means retaining an authoritative private recovery copy **and** proving
that all intended public content survives the public projection. It does not mean
publishing database internals, drafts, spam, email addresses or client IPs.

After authorized container access, take a consistent database/files backup and
WXR export, including uploads, local theme/plugin assets and configuration needed
to restore WordPress. Inventory post types/statuses, authors, comment states and
parent links, taxonomy, attachment variants, options, shortcodes and redirects.
Keep raw backups and sensitive intermediate data outside public Git/build roots.
Record checksums, counts, source versions and snapshot/cutoff time privately.

Use WordPress post IDs as stable import identities, independent of title or slug.
Export actual resolved public permalinks and rendered content in addition to raw
post bodies: WXR/raw Markdown conversion alone can lose shortcode/plugin output.
Convert supported content to Markdown; retain reviewed HTML where conversion
would alter meaning or structure. Keep code, tables, captions, image alt text,
links, dates/timezones, author attribution and comment order/parentage. Surface
every unsupported block or missing asset as an exception; never silently omit it.

The deterministic importer writes a generated Czech baseline and shared public
metadata. Keep manual corrections as explicit overlays and English files outside
its overwrite boundary. Running the same snapshot twice must produce identical
results; a later snapshot must report additions, edits and removals by stable ID
without erasing reviewed work. Retain the original export separately.

Proposed public source contract, finalized after inventory:

- `content/posts/<stable-id>/index.cs.md` and `index.en.md`, sharing a
  `translationKey`; original article date/byline remain distinct from translator
  attribution and translation review date.
- `data/authors.*`: stable author IDs and existing public profile information.
- `data/legacy-comments/<id>.*`: public historical comments, original IDs,
  timestamps, display names and parent IDs; sanitized markup and safe links.
  Nonpublic moderation states remain in the private recovery archive.
- `data/discussions.*`: one stable article ID to one production topic ID; owned
  by explicit publication provisioning, never regenerated by import.
- A public route/asset/feed manifest records legacy paths, article IDs, comment
  anchors and feed identities. Full sensitive source manifests stay private.

Czech remains the unprefixed default. Set routes from the manifest, not regenerated
slugs, including unusual encoding/trailing slashes. Preserve old article paths as
direct pages; map secondary aliases/query URLs at nginx where needed. Explicitly
inventory author/category/tag/date archives, pagination, attachment pages,
`?p=...`, old slug redirects, `#comment-...` and `#comments`. Preserve established
asset URLs, including `/wp-content/uploads/...`, generated image sizes, `srcset`,
downloads and theme-owned images actually used by content. Hash copied bytes.

Use language-specific self-canonical URLs, reciprocal `hreflang`, language-aware
navigation/feeds and correct document language. English paths must never displace
Czech routes. Reuse the same original-language comment archive on both versions,
clearly labelled, with language markup where known. Preserve original attribution;
do not manufacture Discourse accounts for historical authors/commenters.

Keep `/feed/` as a Czech feed with original item GUIDs (including `isPermaLink`
meaning), links, dates and ordering semantics. Translation publication must not
refresh all original items or announce the archive again. Recommend `/en/feed/`
for English. Inspect the actual old feed and bot deduplication before selecting
serialization; redirecting to a new feed alone does not prove compatibility.

## One Discourse discussion per article

Native embedding is sufficient: it renders replies through an iframe; readers
follow the forum link to log in and reply. Configure each language page with the
same explicit `window.DiscourseEmbed` values: production `discourseUrl` and the
article's `topicId`. The official alternative replaces `discourseEmbedUrl` and
does not create topics. Do not pass both identity mechanisms. [5]

URL-based embedding instead looks up an embed URL and can queue topic retrieval
when no mapping exists. Upstream's explicit-ID path selects the existing topic;
its comment view omits the opening post and hidden/deleted content and limits the
embedded replies. Verify the deployed version's behavior. [6]

The design therefore does **not** equate SEO canonical tags with discussion
identity: each translation keeps its own canonical, while both embed the same
stored topic ID. An English URL, tracking query or preview address cannot select
or create a second topic through our templates. Provide a permanent forum link
even if scripts/iframes fail or the embedded reply limit is reached.

Provision topics separately, by an operator publication command or documented
manual process. Use a service identity with minimal needed permissions and
server-side credentials outside repository/build output. The opening post gives
a short introduction and both article links; the blog remains the article source.
Record the returned topic ID before deployment. Serialize provisioning for an
article; check the mapping first. After a timeout/uncertain creation response,
reconcile the forum result using the article identity/link before retrying; do not
claim an unverified API idempotency guarantee. Build/preview/check commands never
create/update topics and need no production API credentials.

For old articles, provision in a controlled batch after inspecting existing
relevant topics, category notifications and any current feed importer. Reuse an
appropriate existing topic only after explicit mapping review. Avoid duplicate
automatic feed creation and unwanted archive notification floods. Preserve
existing closed-discussion intent unless a later editorial decision changes it.

Reuse existing forum account/registration rules and ordinary moderation,
reporting and anti-spam controls. Select and verify a category readable by the
intended blog audience; don't promise broader signup or anonymous posting. Check
logged-out visibility, allowed embed origins/paths, CSP/referrer behavior and
mobile navigation on the deployed forum. An origin allowlist is not an account
authorization mechanism. Test private/hidden content remains protected. Preview
uses a placeholder/link or a dedicated test forum; it must not write production.

## Authoring and translation workflow

Provide `AGENTS.md`, one reusable authoring skill, and `docs/authoring.md` describing
the **same** small command interface: new article, translation draft, check,
preview and publication preparation. Use ordinary Hugo/Git commands or thin
wrappers; no custom CMS or workflow engine. The human quick start must work
without an agent. A local human preview uses `hugo server --buildDrafts` in the
pinned development environment; agents launch session-owned previews through
`dev-session service run`, following the installed temporary-service procedure.
Keep drafts/private material local; do not expose a draft preview publicly by
default. No preview is launched during planning.

The skill requires factual sources, correct author attribution, preserved links
and code, localized metadata, useful image descriptions, human editorial review
and explicit publication/topic creation. Agent authorship does not authorize a
production release. Publication guidance distinguishes content review, Git
integration, Discourse writes and deployment.

Translate a representative pilot first, then process the archive in reviewable
batches. Track source content revision/checksum, draft/review status and reviewer
for each translation. Source edits mark the English counterpart stale. Translate
prose, headings, captions and UI strings while preserving technical meaning,
historical facts and executable examples. Historical comments remain untranslated.
English publication requires human review; full bilingual launch requires no
missing or stale reviewed translations. Do not silently show Czech under an
English URL or redirect readers based on browser language.

## Proposed implementation packages

These are future allocations using verified same-session members, **not current
assignments or implementation permission**. Paths below are relative to the
proposed blog repository unless marked configuration. Lead accepts each release
boundary and controls shared index/commit windows.

| Package and proposed owner | Files/deliverable | Dependencies and acceptance/checks |
| --- | --- | --- |
| A — source inventory and importer, `implementer0` | `tools/import*`, importer fixtures, `docs/migration.md`; generated Czech content, authors/comments, legacy assets and route/feed manifest. Private backup stays outside Git. | Authorized access and source snapshot first. Prove counts/status dispositions, author/comment identity, asset hashes and URL coverage; identical rerun and changed-snapshot reconciliation; no secrets in projection. Inventory settles schema before downstream content work. |
| B — Hugo site and build, `implementer1` | Hugo configuration, `layouts/`, CSS, i18n UI, archetypes, build/Nix/CI definitions and site README. | Accept A's schema and route contract; fixture-based layout may proceed independently of full export. Preserve Flat design features with mobile/keyboard checks; validate routes, archive rendering, locale metadata, feed GUIDs and pinned build. Own build/config files exclusively. |
| C — discussion integration, `implementer2` | Embed partial, `data/discussions.*`, minimal publication helper and `docs/discussions.md`; explicit forum setup plan. | Stable article IDs; B exposes one agreed partial slot, no overlapping edits. Prove same topic for CS/EN, zero build/preview writes, safe uncertain-create recovery, public/private visibility, login/reply/moderation and no duplicate batch topics. Forum writes require later authorization. |
| D — author workflow and English migration, `implementer3` | `AGENTS.md`, authoring skill, `docs/authoring.md`, thin author commands; English article files and translation review metadata. | Stable A/B interfaces; technical workflow can precede full archive, English work follows content stabilization. A cannot overwrite English. Human command smoke test and agent dry run; reviewed full coverage/source freshness; human language review remains required. Lead owns final user-facing writing under writing skill. |
| E — same-container hosting and rollout, `implementer0`, after A | Configuration `int.blog/{config.nix,wordpress.nix,module.nix,packages/default.nix}` as needed; pinned blog input, static nginx configuration and health checks; rollout/recovery docs. `int.vpsfbot/config.nix` only if needed. | Accepted immutable B output and A/C/D acceptance. Preserve proxy-only access and `/feed/`; nginx/static health checks replace PHP/MySQL assumptions. Rehearse recovery; verify public routes/feed/media and bot polling without old announcements. No proxy or Discourse package upgrade assumed. |

Current boundaries are settled enough for planning. After implementation approval,
A can begin with access; B may start on agreed public fixtures/schema. Import
details, real corpus translation scope and production forum behavior remain
discovery gates for dependent work. Repository location, exact supported tool
versions and concrete commands/hooks must be fixed from their own instructions
before code edits. No open preference justifies bypassing data or account checks.

## Verification, cutover and recovery

Quick checks during implementation: deterministic import fixture/rerun checks,
Hugo build, metadata/route collision checks, public-output secret scan, internal
links/assets, translation coverage/freshness and RSS parsing/GUID comparison.
Small representative visual checks cover homepage, article, images/code,
historical threaded comments, author/archive pages and both languages. These
planning records have no implementation test or independent final-review claim.

After completed commits and quick checks, use mandatory independent final review;
then longer checks cover the complete authoritative URL/asset inventory, all
public content dispositions, browser/mobile/keyboard behavior, forum integration
against a controlled fixture and same-container rollback rehearsal. Long/uncertain
checks use the required utility watcher. Compare full archive counts rather than
inferring completeness from the public sample.

1. **Prepare:** obtain source access; inventory/backup; complete import, design,
   translations, topic mappings and review. Build the exact pinned static output
   before machine ownership. Keep the original DB/uploads and runnable old system
   generation available; record recovery prerequisites and retention window.
2. **Rehearse:** preview read-only content without production forum writes; test
   static serving, feed continuity and rollback using nonproduction fixtures.
   Verify actual Discourse version/category/account behavior separately without
   coupling the migration to forum/PostgreSQL upgrades.
3. **Final snapshot:** announce a short WordPress content/comment write freeze,
   take the final consistent export and reconcile all deltas. An edited/new Czech
   article requires refreshed reviewed English before launch. Rebuild/recheck the
   final artifact. Readers can continue reading during the editorial freeze.
4. **Switch:** under later explicit deployment authorization and machine
   ownership, point nginx on the existing blog container at the prepared immutable
   output and update its health checks together. Preserve the public proxy, TLS,
   host and asset/article routes. Enable the reviewed shared-topic mappings.
5. **Verify:** check production homepage, representative/all manifest routes as
   appropriate, bytes/assets, legacy anchors, `/feed/`, language switching,
   anonymous forum reading and account-policy login/reply. Verify bot polling
   does not reannounce the archive. Record source/config heads, complete input
   graph, deployed store paths, targets and results in the rollout receipt.
6. **Recover if needed:** restore the recorded original serving configuration and
   intact WordPress state. Keep WordPress writes frozen during diagnosis. New
   Discourse replies remain authoritative in Discourse; do not delete topics or
   roll back the forum database. Preserve links/mappings to those replies during
   rollback. Reconcile any new static articles before reopening WordPress editing;
   reverting a system generation does not import them into WordPress.

Compatibility: no planned WordPress or Discourse schema/protocol migration.
The new persistent contracts are public URLs/assets/feed identities, Git content
schema and article-to-topic mapping. Old/new serving can coexist against retained
read-only source data, but WordPress cannot consume new Git articles or Discourse
replies automatically. Exact old package generation/data must remain recoverable.
Do not remove PHP/database data or old assets as part of initial cutover.

Before any integration/deployment, read current repository procedures and selected
package coordination guide. Integration requires separate explicit approval.
Repository merge claims cover only the short prepared merge/push verification;
machine reservations are separate. Release machines promptly once deployed
effects and complete integrated lineage are proven, retaining receipts and the
session itself. No operation in this plan archives, deletes or stops this session.

## Remaining implementation facts

Container access, corpus counts/plugin rendering exceptions, exact permalink/feed
variants, existing forum topic matches, category/notification settings, deployed
versions and backup recovery readiness remain unverified. These constrain effort
and release checks, not the recommendation. Repository name and `/en/` route
convention are proposals. The lead has no unanswered user preference from the
questions asked so far.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.
