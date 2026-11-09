# Multilingual static blog migration: proposed design

Architect: `architect0`, 2026-11-06. Initial recommendation and follow-ups are
accepted. D6 below is the current release boundary for theme, import and translation
work; earlier D4/D5 briefs describe completed prerequisites where superseded.
Initial blog-main publication was separately authorized and completed; no further
default-branch integration, branch merge or production cutover is authorized. Architect
edits only this design; lead owns acceptance, plan/state and user writing.

## Recommendation and settled scope

Use **Hugo**, with one small Git repository containing content, templates,
assets, build definition and author guidance. A separate content-only repository
adds coordinated pins/releases without a current access-control benefit; split
later only if editorial permissions or asset volume justify it. The user created
`git@github.com:vpsfreecz/blog.git`; implementer1 confirmed no commits or refs.
It is the selected unified source/content/build repository.

| Generator | Fit for this request |
| --- | --- |
| **Hugo** | Recommended: native multilingual content pairing, explicit translation keys, Markdown and static output suit a bilingual editorial archive. A small custom layout can reproduce the existing design without a client framework. |
| **Zola** | Credible alternative: multilingual files, translated routes and feeds are built in. No requirement here makes it preferable to Hugo. |
| **Astro** | Supports locale routing and is attractive for richer component-driven interaction. This blog currently needs little of that; more application assembly is unnecessary. |
| **Eleventy** | Flexible templates and a bundled i18n plugin; viable, but more site-specific conventions would need assembling for the same editorial result. |

User decisions relayed by lead:

- Preserve original Czech article URLs and the recognizable design. English is
  **https://blog.vpsfree.org/** at its host root, replacing the earlier `/en/`
  proposal. Czech stays at **https://blog.vpsfree.cz/** with existing paths.
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
- Publishing must require no subsequent manual Discourse work. Prefer GitHub
  Actions deployment on the protected publication branch's pushes, independently
  of routine confctl/system deployments. The revisions below supersede the initial
  explicit-topic-ID provisioning and system-pinned content recommendations.
- User supplied the aitherdev SSH key for root access to the existing blog.int
  container and requests internal DNS `blog.int.vpsfree.cz`. Root access is for
  authorized inventory/administration, not the future Actions deployment identity.

## Evidence and limits

The initial investigation consulted seven successful upstream references and a small public sample;
there was no archive crawl, container access, export, build or runtime admin
inspection. One attempted upstream embed-JavaScript source URL returned 404;
the official automatic/explicit-ID examples and controller supplied the evidence.

1. [Hugo multilingual content](https://gohugo.io/content-management/multilingual/):
   language variants and `translationKey` association.
2. [Zola multilingual sites](https://www.getzola.org/documentation/content/multilingual/).
3. [Astro internationalization](https://docs.astro.build/en/guides/internationalization/).
4. [Eleventy i18n](https://www.11ty.dev/docs/plugins/i18n/).
5. [Discourse native embedding](https://meta.discourse.org/t/embed-discourse-comments-on-another-website-via-javascript/31963),
   including automatic creation and “Linking to existing topics”.
6. [Discourse upstream embed controller](https://github.com/discourse/discourse/blob/main/app/controllers/embed_controller.rb):
   inspected current upstream, **not proof of the deployed version**.
7. [WP-CLI export](https://developer.wordpress.org/cli/commands/export/): WXR
   contains content/authors/comments/attachment records, but not site options or
   attachment bytes. It cannot serve as the sole backup.

The category/security follow-up reused [5–6] and read two additional upstream
models (four sources total for that bounded follow-up). Raw upstream `main` was
read directly on 2026-11-06; neither source nor the documentation proves the
installed forum's exact behavior:

8. [EmbeddableHost](https://github.com/discourse/discourse/blob/main/app/models/embeddable_host.rb),
   `record_for_url` and `url_allowed?`.
9. [TopicEmbed](https://github.com/discourse/discourse/blob/main/app/models/topic_embed.rb),
   `import`, `find_remote` and `import_remote`.

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
Record checksums, counts, source versions and snapshot times privately. The user
requests no formal writer freeze: use the captured snapshot and check briefly
for changed/new articles or comments immediately before switching.

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
- Shared article metadata stores one immutable `discussion_url`, normally the
  original absolute Czech permalink. Both language variants use it. Optional
  explicit topic-ID overrides are only for reviewed existing-topic exceptions.
- A public route/asset/feed manifest records legacy paths, article IDs, comment
  anchors and feed identities. Full sensitive source manifests stay private.

Czech and English each live at their own host root. Set routes from the manifest,
not regenerated
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
refresh all original items or announce the archive again. English uses
`https://blog.vpsfree.org/feed/`, replacing the earlier `/en/feed/` proposal.
Inspect the actual old feed and bot deduplication before selecting
serialization; redirecting to a new feed alone does not prove compatibility.

A0 [source inventory](source-inventory.md) now confirms all 125 Czech GUIDs are
unique `https://blog.vpsfree.cz/?p=<sourceID>` identifiers. Preserve each original
value with `isPermaLink="false"`; feed links still use the original slug URLs.
Keep ten full-content items, ordered by original publication time with a stable
ID tie-break. Do not replace GUIDs with slug URLs or translation publication dates.

Accepted English policy: assign each imported article
`urn:vpsfree:blog:wp-<sourceID>:en`, also with `isPermaLink="false"`; do not reuse
Czech GUIDs across languages. Future native articles use the same URN pattern
with their immutable article ID and language. Record per-language `feed_guids`
in shared article metadata. Both feeds use original article publication dates;
translation/review dates are separate metadata. Corrections retain GUID/date,
and only published, human-reviewed translations enter the English feed. The
initial English feed naturally contains the ten newest translated articles;
there is no prior English subscription identity to preserve.

## One Discourse discussion per article

Recommend **native automatic URL embedding**. Both CS and EN set
`window.DiscourseEmbed` with the same production `discourseUrl` and stored
`discourseEmbedUrl` (the original Czech permalink). Discourse creates the missing
topic when the embed first loads, normally on the **first article visit**, not
the first reply. Replies are written on the forum using its login flow. This
needs one initial forum setup, no per-article manual action or CI API key. [5]

Each translation retains its own SEO canonical. Discussion identity is a separate
immutable URL, never `window.location`, an English URL, a preview URL or a URL
with tracking parameters. Preserve its scheme/host/path/trailing-slash convention
and keep it publicly fetchable. The forum can extract the article opening post;
check extraction and links to both translations with the installed version.
Preserve existing discussion mappings when a title or source filename changes.
Verify simultaneous first visits and both language variants produce only one
topic: upstream behavior is evidence, not a deployed-version guarantee. [6]

Configure the production host/path allowlist, category and topic-creation user
once, with permissions only as needed. Inspect existing matching topics and any
feed importer before enabling; avoid two automatic creators. An existing-topic
exception may use `topicId` on both variants instead, never both mechanisms.
An archive crawl can create many topics even without replies, so verify category
notifications and do browser sweeps against a fixture with production embeds
disabled. Preserve existing closed-discussion intent. Provide a forum fallback
link; a direct topic link becomes available through the embed once created.

Automatic publication-hook API provisioning is an alternative if a topic must
exist immediately at publication. It adds credentials, durable mapping and
reconciliation after uncertain responses; it is unnecessary for the selected
native approach. If creation must wait for reader intent, optional click-to-load
embedding can delay it until “Show discussion”, still before a reply. Neither a
custom first-reply service nor click-to-load implementation is proposed now.

### Category and security boundary

Recommend a dedicated publicly readable **Blog** category, selected once as the
blog host's “Post to Category” setting. It is a proposal, not an existing category
claim. The native importer takes the category from the matching host record when
no explicit import category overrides it. Configure the import identity/staff to
create topics and ordinary eligible members to reply, where the installed category
permissions support that split; verify behavior rather than assuming import
validation matches ordinary interactive creation. Keep current signup/login and
moderation rules. The announcements category supplied as a writing reference
does not automatically become the discussion destination. [5, 9]

Allow only the exact `blog.vpsfree.cz` source host and an anchored article-path
rule derived from the actual route inventory, excluding queries and nonarticle
routes such as previews, feeds, administration and assets. Avoid blanket
wildcard domains or private/internal host entries. The inspected host model uses
host equality (no automatic subdomain wildcard), distinguishes nonstandard ports,
and tests a regex against path plus query in encoded or decoded form. Blank path
rules allow every path; regexes are not automatically anchored. This matching
does not enforce HTTPS by itself; our emitted discussion URLs use HTTPS. [8]

This is a **source-URL restriction, not authentication of the requesting website**.
In the ordinary URL-only embed path, the controller checks `embed_url` against
that allowlist before queuing a missing topic. A caller can trigger import of an
allowed public blog article without visiting the blog; it cannot select an
arbitrary off-domain source through that normal path. The inspected controller's
Referer handling supplies presentation/message-target context, not proof of
caller identity. Browser Origin/Referer/CSP behavior must not be presented as a
credential protecting topic creation. Forum reply authentication and category
permissions are separate. This bounded read is not a full endpoint security audit.
[6]

One relevant limit: remote fetching follows redirects/canonical links through
`FinalDestination` with URI validation; the importer only adopts a resolved URL
as the stored embed identity when its host matches the original. That does not
prove every fetched redirect target stays on the allowlisted host. Keep canonical
article endpoints and redirects on the public blog, permit no external/private
import in our setup, and verify redirect/private-address handling against the
installed version before enabling. Do not weaken its network safeguards. [9]

Check logged-out visibility, excluded URL rejection, category selection and
creation/reply permissions, CSP/referrer behavior, mobile navigation and protected
content against a controlled fixture before production setup. Preview
uses a placeholder/link or a dedicated test forum: suppress production embed
scripts entirely in drafts/previews/tests, rather than merely changing their URL.
Build/check commands never contact creation endpoints or require forum credentials.

The English embedding page is on a different registrable domain from Discourse.
Keep the import source restricted to the Czech discussion URL; do not add `.org`
as an import source merely to display the iframe. Verify the installed forum's
separate frame/referrer requirements for both display hosts. Test public iframe
reading from `.org`, cross-site cookie restrictions and top-level forum navigation
for login/reply. Promise no shared `.cz`/`.org` login cookies or authenticated
private iframe. Reuse the public-category/existing-account design above.

## D4 sufficient briefs: inventory, scaffold and internal DNS

These are the currently settled release boundaries for lead allocation. They do
not release full import, translations, production automation or cutover. Members
must read their repository instructions and current applicable workspace
procedures before action; user-facing author guidance follows the writing skill.

### Shared route, content and artifact contract

- Hugo native multihost configuration: `cs` base URL
  `https://blog.vpsfree.cz/`, `en` base URL `https://blog.vpsfree.org/`. Neither
  site's public routes contain a locale prefix. The production artifact has
  separate `cs/` and `en/` document roots, each with its own index, `/feed/`,
  sitemap and self-canonical metadata. There is no cross-language redirect at
  the host root. Later nginx vhosts select the matching root.
  Hugo's feed artifact is `feed/index.xml` within each root: preview and nginx
  must map `/feed/` internally to it with RSS content type, without an HTTP
  redirect. Feed self-links keep `/feed/`; verify both preview language listeners.
- Content bundles: `content/posts/<article_id>/index.cs.md` and `index.en.md`.
  Imported IDs are `wp-<post_id>`; future author-assigned IDs are immutable and
  must not reuse that namespace. Both variants carry the identical
  `translationKey` and `params.article_id`. Each page has explicit `url` (path
  only), title, original publication `date`, relevant `lastmod` and `draft`.
  Czech `url` is the exact exported path; English gets an explicit reviewed
  root-relative path, frozen once published. Hugo language metadata supplies
  language; do not infer identity from translated titles.
- `data/articles.json` is keyed by article ID; minimal shared entries contain
  `discussion_url` (absolute original Czech permalink), `author_ids` and optional
  `legacy_post_id`. `data/authors.json` is keyed by stable author ID with public
  `name` and optional approved public profile fields. Both variants refer to this
  common attribution/discussion metadata. Historic comment data remains in
  `data/legacy-comments/<article_id>.json`; its full importer schema awaits A0.
  Scaffold must tolerate missing optional archive comments without synthesizing
  them. Feed GUIDs and complex source blocks await the real inventory.
- Use reciprocal `hreflang` for existing counterparts and self-canonical URLs on
  each production host. Translation switches link the paired page, not the other
  homepage. Fixtures need no published translation; missing variants are explicit.
  Production builds exclude drafts. Preview serves two local language roots with
  local paired links, identifies its actual URLs and suppresses production
  Discourse scripts regardless of article metadata.
- Provide a pinned Nix/Hugo environment and ordinary documented build/check/
  preview commands; recommended interfaces are `nix build .#site`,
  `nix develop -c bin/check`, and `nix develop -c bin/preview`. Artifact metadata
  records input/source identity and hashes outside the served page roots. Never
  embed private exports, credentials, transient timestamps or Git internals.
  Tool versions and exact multihost output behavior are scaffold checks, not
  assumptions that permit silently changing these route contracts.

### A0 — runtime inventory and recovery inputs, implementer0

Own read-only inspection/export of the authorized existing blog container and
private evidence under this session; publish only a sanitized findings Markdown
file. Verify target/address/WordPress identity, record access confidence, then
inventory exact URLs/feed identities, table/status counts, authors, comments,
assets and content exceptions. Keep raw users/email/IP/password data and spam
private. Capture consistent recoverable DB/files/export inputs without changing
source content/services; report hashes/counts and capture times. No blog source
files or configuration edits in this package. Lead allocates full importer later.

Completed [A0 inventory](source-inventory.md): 125 published posts, six author IDs,
107 approved comments (43 same-post replies), 159 spam comments, 144 attachment
rows, 569 upload files (~50 MB), no draft/private/page rows reported. All slugs
are unique root-level ASCII, all posts have WordPress more markers, eleven have
YouTube/SuperLectures iframes. The five broad shortcode candidates were literal
PDF labels/shell prompts; no active shortcode subsystem is justified by evidence.
Private SQL/files recovery capture passed structural checks but is not an atomic
final cutover snapshot and has not been restore-tested. Full per-article rendering
and public projection remain importer checks; A0 did not generate public content.

### B0 — local dual-host Hugo scaffold and preview, implementer1

Own the initial blog repository scaffold: Hugo config/layouts/CSS, Nix lock/build,
`bin/{check,preview}`, README/initial repository guidance, and isolated synthetic
fixtures. No real article prose, fake translations of existing articles or real
import output. Fixtures are nonpublished drafts, explicitly labelled synthetic;
production build checks prove their exclusion. Cover a synthetic paired page,
missing translation, punctuation/path preservation and optional shared metadata.
Scaffold can proceed against the settled contract without A0's full export.

Acceptance: build both roots; assert correct host canonicals/reciprocal alternate
links and `/feed/` placement, no unwanted `/en/` prefix, draft exclusion and no
production iframe/scripts in preview. Verify a reproducible build and documented
human preview. Register a session preview through `dev-session service run` when
launched. Full import/comment fidelity and real RSS identity validation are later
checks. Long/uncertain builds use the watcher procedure. Return exact commit,
changed files, quick-check evidence, preview URLs and explicit gaps.

Empty remote handling: prepare local orphan feature history with genuine scaffold
content; do not fabricate a baseline/default commit. Native registration may need
the first genuine local source commit. Do not develop runtime tooling to handle
this case. **Do not push any branch to the empty remote**: the first push could
establish its default. Lead will obtain concrete default-initialization/integration
direction after the local deliverable and independent review. Review covers the
entire root commit/series against the empty tree, with no database migrations.

### N0 — internal blog DNS feature, implementer2

Exclusive configuration file boundary:
`configs/internal-dns/zone.vpsfree.cz.`. Add `blog.int IN A 172.16.8.4`, preserving
`$ORIGIN vpsfree.cz.` and `$TTL 1H` conventions; advance the existing SOA serial
monotonically (observed `2026093000`, proposed `2026110600`, recheck before edit).
Implementer2 verified current `int.blog/module.nix` host metadata and IPv4 agree
on `blog.int.vpsfree.cz` / `172.16.8.4`. Do not edit serving modules, public `.org`
DNS, proxies, TLS or Discourse. No generated tracked file is needed.

Checks: materialize `@fqdn@` for both Prague/Brno internal BIND masters, run
`named-checkzone vpsfree.cz.` on each result and `git diff --check`; inspect that
only this record/serial changed. Own the configuration feature-worktree edits and
commit; supply exact base/head/check evidence. Hook/environment registration
failure is owned by implementer2, not permission to bypass hooks. Feature work
needs no merge claim. DNS activation, if directed separately, affects both
authoritative servers and is not authorization for the blog cutover or default
integration. Public `blog.vpsfree.org` DNS/proxy/TLS remains a later prepared
hosting package with fresh runtime evidence and explicit release scope.

## Independent content deployment

Use confctl once to establish static nginx on the existing blog container, its
proxy-only network boundary, deploy-only user, trusted activation helper and
persistent release storage, for example `/var/lib/blog/releases/<release-id>`
with nginx reading `/var/lib/blog/current`. System configuration owns hosting;
it must not pin a blog source revision and claim that pin represents live content.
Content receipts identify the deployed Git SHA, pinned build inputs, artifact
digest, release path, previous release and workflow run separately.

On a protected publication-branch push, GitHub Actions builds/checks with the same
pinned environment as local development and produces an immutable static artifact.
Only trusted publication jobs obtain deployment credentials; PR jobs receive none.
Use a dedicated non-root SSH identity restricted to the exact deployment target
and upload/activation operations, with pinned host identity and no general shell
or forwarding. Target validation checks artifact digest, safe extraction paths,
required files and release identity before an atomic same-filesystem symlink
replacement. nginx only reads releases; uploads never modify the current tree.

Serialize deployments in Actions **and** activation on the target. Under the
target lock, recheck the authorized publication head and current release receipt;
reject an obsolete run rather than overwriting a newer release. Workflow
cancellation alone cannot establish this guarantee. Record and reconcile an
uncertain activation before retrying. Keep a previous validated release and an
explicit rollback command/receipt; rollback of content does not require reverting
the system generation. Use content-hashed CSS/JS assets and retain referenced
older assets at their served URLs across switches, including rollback, so cached
pages remain usable; merely keeping a previous release directory is insufficient.
Legacy media paths retain stable bytes or an explicit compatible replacement.
Activation must also honor existing machine ownership/maintenance coordination
so automated content releases cannot race a confctl change or migration rollback.

Runner SSH reachability to the internal backend is **unknown**. If no suitable
route exists, prefer a small VPS-side pull of the successful CI artifact for the
exact authorized publication head, with the same validation and stale-activation
rules. Do not expose the internal web backend or grant root access to solve this.
Choose push versus pull after checking the existing network/runner capabilities;
both retain automatic publishing without a new CMS or deployment service.

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
and the reviewed publication-branch workflow. Agent authorship does not authorize
a production release. Explain that approved publication pushes trigger Actions,
while first production embed loads create forum topics automatically. Human and
agent workflows require no additional manual forum step.

Translate a representative pilot first, then process the archive in reviewable
batches. Track source content revision/checksum, draft/review status and reviewer
for each translation. Source edits mark the English counterpart stale. Translate
prose, headings, captions and UI strings while preserving technical meaning,
historical facts and executable examples. Historical comments remain untranslated.
English publication requires human review; full bilingual launch requires no
missing or stale reviewed translations. Do not silently show Czech under an
English URL or redirect readers based on browser language.

Translations should match Jakub Skokan/aither's past announcement style; it may
be shared across translated authors while preserving meaning and each original
byline. Leave the original Czech unchanged and invent no first-person facts or
jokes. Lead owns the [editorial voice brief](plan.md), drawing on the supplied
[mailing-list archive](https://lists.vpsfree.cz/mailman3/hyperkitty/list/news-list@lists.vpsfree.cz/latest)
and [announcements category](https://discourse.vpsfree.cz/c/announcements/5);
individual reference posts must have their authors verified. Do not infer that
every post in either collection was written by Jakub.

## D5 sufficient brief: standalone repository authoring

Owner `implementer0` (execution package D0), after accepted A0 and lead release. File boundary is
`AGENTS.md`, `docs/authoring.md`, `skills/blog-authoring/SKILL.md` and the README
entry-point links in the blog repository. No article, translation, template,
importer, command implementation or workflow changes. Implementer1 retains B0
review fixes and preview source ownership. P edits/commits its source and README
preview block first; D0 may draft disjoint AGENTS/docs/skill concurrently, but
must not edit README or touch the index/commit until P finishes its window.

The repository must teach a generic agent or human, starting from an ordinary
clone, how to add an article without this workspace or chat. `AGENTS.md` is the
entry point; the optional skill is a self-contained Markdown workflow any agent
can read, with no registry/platform installation requirement. Put canonical
details in `docs/authoring.md`, linked locally by both. Do not require session
records, private exports, `dev-session` or workspace skills in an ordinary clone.
Workspace-owned previews use registration only when running in this managed
workspace; other users run the repository's ordinary pinned preview command.

Document commands honestly: `nix develop -c bin/check`, `nix build .#site`,
`nix develop -c bin/preview` for real repository content including drafts, and
`nix develop -c bin/preview --fixtures` for the isolated synthetic demo. P owns
that minimal selection change. Explain the still-empty RSS limitation. Show
file-creation/edit steps without inventing a
`new` or `publish` helper. Include a concise inline metadata example, no new real
post or fixture. Cover immutable new article ID outside `wp-`, explicit CS/EN
paths at their separate production hosts, matching translationKey/article_id,
shared authors/discussion URL and `feed_guids`. Preserve original dates and
byline; translated prose must not claim new first-person experiences.

For forward-compatible editorial metadata, document `params.translation_status`
(`draft`, `reviewed`), `params.translation_source_sha256` (source Czech file),
`params.translation_reviewed_by` and `params.translation_reviewed_at` (RFC3339).
Keep English `draft=true` until human review and source freshness are confirmed.
These fields record editorial review; the current scaffold does not enforce them,
serialize feed items or deploy. Preserve original `date`; `lastmod` reflects a
material content change, not an arbitrary build. Source edits require translation
re-review. Manual checks must not be misrepresented as implemented CI gates.

Include standalone style links to the user-provided mailing-list/Discourse
references and the lead's verified examples, summarizing the accepted factual,
plain technical voice in the document itself. No dependency on `plan.md` or
assumption all announcement authors are Jakub. Human review covers translation
meaning, commands/code, links, chronology, attribution and voice. Keep technical
facts and original Czech content intact.

Publication authority is Git repository write access plus its protected branch
policy; an agent cannot grant itself publishing rights. Explain normal branch,
review and authorized push steps, but state that **Actions publishing is not
implemented yet**. A push currently does not promise a live article. This empty
remote must not receive its first branch until lead obtains default initialization
direction. No forum credentials or manual forum step belongs in article writing;
future native embedding handles topic creation after deployment.

Acceptance: a reader can follow only repository files to locate the content/data
files, prepare a draft, inspect local output, check it and understand the current
publication limitation and permission boundary. Check local links and examples
against accepted B0 at `04b6ecc6dd286a4932910c1a8da12a5d28be1df8`; use existing quick
checks, no new command/test framework. A temporary uncommitted draft must appear
in the default real-content preview; do not commit fake real corpus. Lead performs
contextual writing check before D0's commit. After both P and D0 commits and quick
checks, run combined independent final review and capture clean Nix source evidence
for the complete intended head; do not treat P's partial source as that final head.
Return file inventory, exact head, checks and limitations. Full import/feed
rendering/translation production remains outside D5.

## P sufficient brief: VPN preview on port 4567

Owner `implementer1` after lead release/capacity confirmation. Own preview runner/
config, minimal RSS link correction if required, corresponding checks and README
preview section. Coordinate that README edit with D5's implementer0; lead gives
exclusive source/index windows as specified above. Preserve accepted B0 production
and native dual-loopback preview routing. `bin/preview` defaults to real content
including drafts; explicit `--fixtures` selects only isolated fixture content/data.
The requested VPN demonstration uses `--fixtures`, not arbitrary real drafts.
Make this a minimal flag/config selection, not a new preview server/framework.

Read-only host evidence: interface `br0` has `172.16.106.40/24`; configured DNS
servers `172.16.9.90` and `172.19.9.90` both return that address for
`aitherdev.int.vpsfree.cz`. Local `/etc/hosts` instead returns loopback, so it is
not remote DNS evidence. Port 4567 was unoccupied at the check; recheck before
launch. Bind exactly `172.16.106.40:4567` and advertise
`http://aitherdev.int.vpsfree.cz:4567/`. No public exposure or firewall change.
Actual reachability from a VPN client remains a launch-verification result.

Implementer1's temporary native Hugo config check established: removing per-language
`baseURL` keys enables singlehost mode; setting them empty does not. Use a simple
preview-only configuration with the common base URL. Czech home is `/`, English
home/feed are `/en/` and `/en/feed/`, while the existing explicit fixture article
URLs remain at their distinct root paths. This native result is accepted for
this synthetic preview; **do not claim every English page gains `/en/`**. Assert
fixture path uniqueness and correct paired links. Production continues to use
separate host roots. No URL-overlay subsystem or custom preview framework.

Derive feed links from each site's home permalink so all preview/production modes
resolve correctly. Serve both feed endpoints as RSS with internal status-200
rewrites and no Location redirect. Keep noindex and production Discourse scripts/
iframes disabled. Quick checks cover real-content default using a temporary draft,
explicit fixture mode, and existing production/loopback contracts, while preserving
unrelated D0 draft docs. Commit P before handing README/index ownership to D0.
Final clean Nix source evidence and independent review cover both packages together.

Launch via `dev-session service run` only after both packages are done and combined
final review passes, at the exact final reviewed head; no architect launch.
Verify one listener on the exact address/port, both language homes/paired fixture
links, `/feed/` and `/en/feed/` XML/content type and absence of production embeds.
For local HTTP checks, explicitly resolve the advertised host to `172.16.106.40`
to avoid the hosts-file loopback alias. Report service identity, exact revision,
commands, hostname/IP URLs and evidence limits. Use a VPN-side reachability check
where available; local socket/HTTP success alone cannot prove the user's path.
Do not change firewall policy or stop unrelated services to make a check pass.

## D6 released design contracts: recognizable theme and real corpus

User rejected the synthetic shell's visual result and directed actual design,
content import and English drafts. The accepted code review did not establish
visual acceptance. Blog `main` was initialized, with explicit user authorization,
at `0354dac281978867ea8c1553b092ce19bccb5ccd`. Earlier empty-remote/no-first-push
restrictions are superseded: normal feature-branch publication is allowed, but
**no subsequent default-branch integration, branch merge or production transition
is authorized**. No new production WordPress export/write is part of D6.

### V1a — original visual identity, implementer1; sufficient now

Own layouts/CSS/theme configuration, presentation checks/screenshots and
`static/theme/` assets/provenance. Importer0 exclusively owns
`static/wp-content/uploads/`; no overlapping asset/index writes. V1a may start
against existing fixtures and public original theme assets immediately after
lead release; it does not depend on a complete importer or translations.

Architect reference evidence is under `visual-reference/`: homepage, code article
`/devcgprog-utilita-pro-nastaveni-devices-cgroupv2-controlleru/`, and comment article
`/automaticke-rozsirovani-disku-vps/`; desktop 1440×1000 and mobile 390×844 PNGs,
mobile drawer capture, comment-section captures and `computed-styles.json`.
Start with [original desktop](visual-reference/original-home-desktop.png),
[original mobile](visual-reference/original-home-mobile.png) and
[original comments](visual-reference/original-comments-section-desktop.png).
Eight directly inspected URLs comprise these three pages, both Flat stylesheets,
the logo, background photo and CTA image; browser-loaded dependencies were not an
archive crawl. Cached Chromium/Playwright captured real rendered pages. Lead and
architect inspected original desktop/mobile evidence; no new theme acceptance
is claimed. Implementer1 also owns `theme-reference/` captures.

| Original property | Measured contract |
| --- | --- |
| Canvas | 1200px centered at desktop; 300px navy sidebar and 900px white article column. At 1440px, outer margins are 120px. |
| Palette | Sidebar `#16273f`; body/background fallback `#1f3959`; article white; body text `#555`; links `#3699dc`; metadata `#777`; separators `#eee`. Keep original server photo outside the canvas. |
| Logo | Actual `/wp-content/uploads/2014/11/vpsFree-bile1.png`, intrinsic/rendered 230×90; desktop centered at x155/y30, mobile x80/y15 at 390px width. Never replace it with styled text. |
| Typography | Actual live stack `Arial, Verdana, sans-serif`, body 16px/26px; headings Arial/Verdana weight300. No custom webfont faces were loaded or declared in the inspected CSS. Preserve the real stack rather than adding a substitute font service. |
| Article | Desktop padding80px90px; title centered48px/57.6px, 13px lower margin; meta12px/19.5px uppercase with1px letterspacing; body starts30px below metadata. |
| Sidebar | Logo/tagline, actual Tux CTA, search, recent articles, tags, categories, date archives. Widgets25px padding and14px/22.75px type; white links, subdued headings and thin translucent separators. |
| Code | Courier New/monospace15px/15px; background `#f5f5f5`, text `#333`, border `#ccc`, padding12.5px, radius4px; horizontal overflow confined to code. |
| Comments | Preserve dates/names/thread nesting; desktop section90px padding, comment body40px vertical/120px left, metadata11px. Mobile section30px, comment body30px vertical without left indent; don't reproduce the old local posting form. |
| Responsive | Below1200px header becomes horizontal and sidebar widgets use a300px off-canvas drawer. At390px header162px tall, logo stays230×90, article padding30px, titles24px/28.8px, body gap10px. Keyboard-operable toggle and no page overflow. |

Importer supplies byte-preserved logo and background
`/wp-content/uploads/2014/11/foto5.jpg` at legacy paths. V1 owns an actual copied
CTA from `/wp-content/themes/flat/Pridej_se.png` (150×147) under
`static/theme/branding/`, plus theme-specific icons if needed. It may reference
original public upload URLs temporarily while A1 stages local copies; final
preview uses local copies. Preserve provenance/license notices: original local
Flat stylesheet explicitly declares GPLv3-or-later; keep required notices for
derived theme code. Record actual media provenance separately, do not invent a
license for the logo/photo/CTA or redistribute proprietary system font files.

First deliverable: recognizable original palette/logo/background/sidebar and
article layout, with desktop/mobile before/after screenshots. Then layer real
imported bylines, excerpts, taxonomies, archives and comments via A1's interface.
Search must work over public site data or be visibly unavailable until implemented;
do not ship a decorative broken form. Retain small accessible improvements without
changing the recognizable identity. Capture the same viewport/pages and drawer,
code and comment sections side by side after real content arrives. HTTP/build
success alone is not visual acceptance; report remaining differences to the lead.

### A1 — private snapshot to complete public Czech corpus, implementer0; sufficient now

Use accepted captured SQL/uploads locally; no new production query/export/write.
A private disposable MariaDB restore with owner-only Unix socket and no TCP is
permitted as an extraction tool, registered through session services. It is not a
blog runtime dependency. Explicit allowlist queries only; never dump private rows
to tool output. Existing restore confirms125 posts/107 approved comments and
42,996 source whitespace words; raw body hashes verified against the database.

Own `tools/import*` and its bounded fixtures/checks, Czech article files,
`data/{articles,authors,taxonomies}.json`, `data/legacy-comments/`, public import
manifest and `static/wp-content/uploads/`. V1 owns templates/config/CSS/theme
assets. Lead sequences shared index commits. Implement importer as a small Python
conversion/report tool plus a bounded offline formatting adapter if needed, not a
general migration framework or new service.

Settled output interface (supersedes imported Markdown-wrapper proposals):

- `content/posts/wp-<id>/index.cs.html`: native Hugo HTML content with frontmatter,
  faithfully formatted public article body. Fields: `title`, `date`, `lastmod`,
  `draft=false`, exact root-relative `url`, `translationKey="wp-<id>"`,
  `categories` and `tags` **slug arrays**, `params.article_id="wp-<id>"` and
  `params.source_body_sha256` (original raw WordPress body bytes). Preserve original
  dates, code, links, captions, images, tables and Unicode. No separate public
  `source.cs.html`; byte-exact raw bodies remain in private recovery inputs.
- `data/articles.json`: object keyed `wp-<id>`, values `discussion_url`,
  `author_ids`, `legacy_post_id`, `feed_guids={cs,en}`. Preserve exact source Czech
  GUID and accepted English URN. Common author/discussion metadata is authoritative;
  do not copy private author account fields into frontmatter.
- `data/authors.json`: keyed `wp-user-<id>`, with `name` (original public display
  name), `slug` (public WordPress author-archive nicename), optional validated public
  `url`. Retain all six bylines and `/author/<slug>/` routes. Login/email/password/
  IP/roles/authentication data and unrestricted metadata stay private.
- `data/taxonomies.json`: `categories` and `tags` objects, each keyed by original
  slug with `{name}` display label. Observed9 categories/32 tags have no parents;
  retain associations and `/category/<slug>/`, `/tag/<slug>/` archive routes.
- `data/legacy-comments/wp-<post-id>.json`: top-level array sorted by date then ID,
  entries `{id,parent_id,author_name,date,html,author_url?}`. IDs are original
  numeric comment IDs; `parent_id=0` means root; `date` is ISO8601 with the correct
  source timezone/UTC conversion. Exactly107 approved comments, including43 valid
  same-post replies. No spam/unapproved comment, email, IP or unrestricted meta.
  Theme renders `id="comment-<id>"`, threading and `#comments`/`#respond` compatibility
  anchors; no local comment submission form. Plain display names are escaped.
- `data/migration/source-manifest.json`: ordered public list of article ID, Czech
  path/file, raw-body SHA256, complete generated Czech-file SHA256, visible word
  count and concrete conversion exceptions. Include aggregate counts and asset
  digest mapping. No private source paths or SQL. This releases translation batch
  inputs; preserve raw snapshot provenance separately in private receipts.

Formatting: bounded standalone adapter may use pinned matching WordPress7.1.2
`formatting.php` functions such as `wpautop`/`convert_chars`; record source revision/
hash and call only supported pure functions. Never bootstrap `wp-load.php`, source
live config, run plugins or make application/network calls. Do not approximate
`wptexturize` silently; record actual rendering differences for correction. No PHP,
WordPress or database is required to build/serve the resulting blog artifact.

Preserve native `<!--more-->` summary boundaries and insert legacy `more-<id>`
anchors without dropping text; all125 source posts contain these markers. Comments
use a fixed safe HTML/tag/attribute/URL allowlist; remove active scripts/events and
unsafe schemes without discarding visible text. Source article HTML must likewise
not gain active content: retain the11 observed YouTube/SuperLectures embeds through
explicit safe HTTPS iframe hosts/attributes, report unsupported embeds rather than
deleting silently. Do not add a shortcode subsystem: observed matches were literals.
No arbitrary generic `safeHTML` of unvalidated private metadata or comment input.

Copy all569 upload files, exactly50,375,369 regular-file bytes, to unchanged
`static/wp-content/uploads/...` paths; validate safe relative paths/no symlinks and
byte hashes. Preserve144 attachment records' relevant public links/variants, all
image src/srcset references and the PDF; surface missing references. Theme-owned
legacy assets use the disjoint V1 namespace and explicit route compatibility.

First check three representative bundles (long code, media/iframe, threaded
comments), then generate all125 plus manifest. Repeat same input into a fresh
output and require identical bytes; reruns must not overwrite English files,
manual corrections or unrelated theme files. Explicit correction overlays or a
small documented correction map are allowed only for observed exceptions.
Acceptance is125 Czech articles,6 authors,107 approved comments/43 parent links,
all associations/assets, original routes/date/GUIDs and per-article disposition;
private-field scan and source/output comparisons must pass before translations
consume the public projection. Return exact input/output hashes, files and gaps.

### V1b — consume A1 data; same theme owner

Lead explicitly assigns `content/_content.gotmpl` to V1 for a conventional Hugo
content adapter producing author/date archive pages from public metadata and
publication dates. This exact file is outside A1's
`content/posts/*/index.cs.html` ownership; no corpus writes or generic framework.
V1's normal layouts filter/paginate the resulting native archive pages. Preserve
the lead's shared-index order and A1's first commit window.

Native `.Content` renders imported HTML and future Markdown. `.Summary` uses the
preserved more marker. Resolve category/tag slug display names from taxonomy JSON;
render author, category/tag and date archives, pagination and original anchors.
Hugo0.167 requires explicit `security.allowContent` permission for these input
types; V1 reports allowing only `^text/html$` and `^text/markdown$`, retaining
Goldmark `unsafe=false`. That input declaration does not sanitize HTML: A1's
validated public projection remains the authority for native HTML bodies and
approved iframe hosts. Preview checks exclude production Discourse scripts/iframes
while permitting the preserved article-media iframe contract.
Serialize ten full-content RSS items with exact Czech GUIDs and accepted per-language
identities/dates; English production includes only reviewed published translations.
Keep `/feed/` mapping. Approved comments use the explicit array contract above.
Production Discourse writes remain disabled/unreleased; a preview placeholder is
honest until the separate integration package. Validate real corpus rendering and
side-by-side screenshots, not just synthetic fixtures or HTTP responses.

### T1/T2 — English drafts, implementer2/implementer3; dependent release

Begin only after A1 publishes the sanitized125-bundle manifest and lead assigns
disjoint exact IDs. Balance batches by visible word count (~42,996 total), never
share an article between translators. Start with a small pilot (five IDs each),
check technical/source fidelity and voice, then release the remaining assigned
IDs. Lead owns batch allocation and contextual writing checks before commits.

Own only each assigned `content/posts/<id>/index.en.html`; preserve source HTML
structure/code/links/media, translate visible prose/title/captions/alt text, and
choose explicit stable English paths. No Czech/shared metadata/template edits.
Both HTML and new-author Markdown remain supported. Carry the same translationKey,
article_id, original date and source taxonomy slugs; set `draft=true`,
`params.translation_status="draft"`, and `params.translation_source_sha256` to the
manifest's complete generated Czech-file hash. No agent review may set human
reviewer/date or claim human approval. User-reviewed publication is a later action.

Use the self-contained accepted authoring/style instructions and verified aither
references; preserve meaning/bylines/chronology, no invented personal facts/jokes.
Preview includes these real English drafts with a clear unreviewed label; production
excludes them. At125/125 draft coverage, check source hash freshness, code/URL/media
parity, no missing body sections and no route collisions. A source correction
invalidates the affected draft's source hash and requires reconciliation. Human
review before publication remains required; agent quality checks do not replace it.

## D8 source-preparation briefs: discussions and independent releases

These are **source candidates only**, accepted and allocated by lead: C0 to
implementer1 and E0 to implementer0, both with confirmed capacity. Translation
work and its review remain separate. No production
SSH/HTTP/forum requests, settings/topic writes, service changes, default integration
or current-blog transition are authorized. Prepared workflow/configuration remains
disabled. Existing reviewed checkpoints are evidence for their exact revisions.

### Observed constraints and selected mechanism

Bounded inspection used ten primary configuration/build/helper files plus two
small production-layout/config follow-ups and current docs, with no external
research. Current locally retained configuration `origin/master` is
`5941cdb3dda259e91c6a988a7dbf08c84700b326`; inspected blog head is
`2635a3e6606a555442916ba1f3dc71d948dc39dc`. These are inspected source identities,
not deployed-state claims. The newer WordPress configuration has exact-proxy
HTTP/header trust, Unix-socket MariaDB, isolated WP-CLI/cron and outbound/MTA
restrictions; preserve all of them verbatim. Its public proxy still targets port80.
Forum configuration has OAuth/ordinary site settings but no declarative embedding
host/category records. Do not invent Nix options for runtime database settings.

Existing blog builds produce `cs/`, `en/` and schema1 `metadata.json` with input
identities and per-file SHA256 values. CSS is fingerprinted under `/css/`. Local
build metadata may have a dirty/null revision; that remains fine for authoring,
but a deployable artifact must identify the clean exact source commit.

Choose **Actions build plus VPS pull**, avoiding assumed inbound GitHub-runner
access. A protected-main push produces a checked immutable artifact; a later
enabled VPS-side timer retrieves the successful artifact for the exact authorized
head. One small unprivileged helper handles acquisition/validation/activation,
not a general deployment framework. No root CI, inbound backend exposure or new
runner/VPN infrastructure is proposed. Outbound artifact/API access and private
repository read credentials remain runtime gates, not assumed facts.

### C0 — opt-in discussion source, owner implementer1

Files: blog `layouts/partials/discussion.html`, one local embed script if needed,
explicit default-disabled parameter in Hugo configuration, `bin/check` and
`docs/discussions.md`; localized i18n labels only as required. No README/authoring
edits without a later lead window. No configuration-repository/forum edits.

Render the native embed only when all are true: production environment, explicit
`params.discourse.enabled=true`, non-draft article, expected CS/EN production
host and validated shared `discussion_url` on exact `https://blog.vpsfree.cz/`.
Default is false everywhere; preview/draft builds override false regardless of
user parameters. Serialize values safely as JSON, not raw script interpolation.
Use shared `discourseEmbedUrl`, never the current English/preview URL; no API key,
topic provisioning command or request at build time. Preserve historical comments,
disabled-preview explanation and forum navigation fallback. Existing account
policy and publicly readable proposed Blog category remain unchanged.

Local checks cover disabled production, both preview modes, drafts and the
explicit enabled-production rendering with synthetic origins/blocked requests.
Assert identical CS/EN discussion identity and zero forum/network calls while
checking; do not open an enabled candidate against production Discourse. This
source package is independently ready. Enabling it requires later explicit forum
setup approval, deployed-version/path/category/extraction tests, public `.org`
frame/login verification and blog transition approval. Ordinary first-view topic
creation, source-URL restrictions and notification limits remain as documented.

### E0 — artifact and disabled hosting candidate, owner implementer0

Two repositories, one agreed interface. T3 owns the current short blog index
window; C0/E0 may edit their disjoint sources, with subsequent blog commit windows
allocated by lead. E0 exclusively owns its configuration index. Blog files: one
build/check workflow, a minimal release-artifact packager and separate
`bin/check-release`, `docs/deployment.md`, and only necessary `bin/build`/metadata
validation changes. No C0 `bin/check`/Hugo/i18n changes or README/authoring edits
without a later lead window. Configuration files: new
`cluster/cz.vpsfree/containers/int.blog/static-blog.nix`, its disabled import in
`config.nix`, a site-specific pull/activation helper packaged with configuration,
local fixture checks and `docs/operations/blog-static.md`. Helper lives with its
owning configuration; no live-content source pin is required. Do not edit existing
`wordpress.nix`, proxy, DNS, forum, input pins or old health checks in this candidate.

**Artifact:** clean checkout of the exact trusted source SHA, pinned Nix build,
normal quick checks and production draft exclusion. Extend metadata/envelope only
as needed to carry repository, SHA, build inputs, workflow/run/artifact identity,
archive SHA256 and existing file hashes; self-referential hashes are not required.
The VPS independently verifies GitHub repository/branch/workflow/event/run success
and SHA, rather than trusting identity strings inside downloaded content. Reject
dirty/null/mismatched source identities for release only. PR jobs have read-only
permissions/no deployment secrets; untrusted workflow runs cannot publish an
eligible deployment artifact. Protected publication branch and reviewed workflow
are prerequisites. Actions versions must be checked from upstream when actually
implementing the workflow, per verification procedure.

**Expiry/bootstrap:** Actions artifacts are temporary; explicitly configure/document
the repository-supported retention period. Successful VPS downloads retain the
exact archive, extracted current/previous releases and receipts locally, with no
automatic removal in this package. First activation needs one successful artifact
for the current approved main SHA and an existing validated recovery backup.
If that run's artifact is missing/expired on a fresh or recovered machine, remain
inactive (or keep serving the existing release) and report the exact missing SHA.
An operator dispatches/reruns the trusted build for the same authorized SHA, then
the normal pull retries; do not fall back to an older artifact or build on the
production VPS. The read-only pull credential cannot trigger workflows. Rare
posting does not remove locally retained content. Recovery of a lost machine uses
retained archive/receipt backup or that exact-source rebuild; artifact retention
alone is not the backup strategy.

**Hosting:** a single default-off candidate option prepares persistent
`/var/lib/blog/{releases,receipts,assets}` and an unprivileged `blog-release` user,
nginx CS/EN static virtual hosts on IPv4 port8080, and a default-off pull timer.
No PHP location/execution in that listener. If later enabled, permit port8080 only
from the same metadata-resolved proxy IPv4, preserving the port80 protections;
localhost checks use explicit Host headers. Map each host to `current/cs` or
`current/en`, `/feed/` internally to RSS XML, reject unknown hosts and keep metadata,
archives and receipts outside web roots. WordPress80/DB/PHP/cron remain runnable,
unchanged, providing the original rollback target. Candidate enablement itself
still requires deployment approval; importing its disabled module changes no
effective serving/network/unit state.

**Filesystem transaction:** download to a fresh staging location; validate trusted
artifact identity, complete file hashes and required roots/feed files. Reject
absolute/traversing paths, duplicate archive entries, symlinks/hardlinks/special
files and undeclared web payload before extraction into the immutable release.
Never execute downloaded content. Serialize on the target; immediately before
switch recheck current protected-main SHA and previous receipt. A stale run must
not replace a newer activation; Actions cancellation alone is insufficient.
Atomic same-filesystem `current` symlink replacement and a receipt identify source
SHA, artifact digest, input graph, current/previous paths and outcome. Reconcile
link/receipt after interruption before any retry. Failed download/validation never
changes the pointer. Explicit rollback selects a retained validated release and
records its own receipt; it does not change system generation or delete forum data.

Retain fingerprinted `/css/` assets at their served paths independently of the
current pointer (nginx fallback only for that declared immutable asset namespace,
never HTML). Preserve legacy-upload path bytes and reject conflicting reuse of an
immutable path. Current and previous release archives remain intact for rollback;
merely retaining their directories does not make assets reachable to cached pages.
No garbage collector or retention service is needed now.

### Local acceptance and genuine activation gates

C0 renderer tests, E0 artifact packager/validator and disabled module can start
independently after lead allocation. Use tiny local fixture artifacts and mocked
API responses, not production calls or a new test web service. Cover valid release,
missing/expired artifact, wrong repo/SHA/workflow, dirty build, malformed archive,
hash mismatch, stale/concurrent run, interruption around pointer/receipt and
explicit rollback. Nginx fixture checks prove CS/EN roots/feed, no PHP, no public
port exposure and disabled-state preservation of hardened WordPress. Normal local
draft preview must continue to work. Longer config builds follow the watcher
procedure; no target activation or dry-activate against production is included.

Before final candidate checks, E owner fetches/rebases current configuration
outside claims and reconciles the existing DNS feature's old/new ranges with a
patch-equivalence receipt. Its old `133a94b` review/build only certifies its original
base; it is not evidence for the newer hosting candidate. Preserve unrelated
hardening and all required hooks. Final independent review covers actual complete
feature series and migrations (none planned), with no merge permission implied.

Production enabling is blocked on concrete operator facts: GitHub artifact-read
visibility/credential and trusted workflow ID, verified outbound API/download
route, branch protection, retained release backup and recoverable WordPress state,
plus installed machine-coordination admission. The scheduled activation path must
honor authoritative machine ownership/maintenance exclusion; do not invent an
unverified coordinator bridge or substitute a filesystem lock for that ownership.
Until that integration is proven, keep the timer off and treat automatic activation
driver release as blocked, while pure filesystem/validation code remains testable.
No claim is held during this source preparation or while awaiting those decisions.

Actual transition is a later explicit package: provision public English DNS/TLS,
point the public proxy from WordPress80 to validated static8080 and verify both
hosts, aliases, feeds, assets and forum policy. Legacy query/alias routing must be
accounted for from the existing public manifest before that switch; current
artifact/page success does not prove nginx query handling. Rollback restores proxy
port80 and intact WordPress, retaining new static articles/Discourse replies for
reconciliation. No formal writer freeze: use the brief pre-switch change check
already requested by the user. Machine release follows verified effects and
integrated lineage under the installed guide; no lifecycle cleanup is implied.

## D9 sufficient briefs: alignment, English CTA and prose audit

Source-only feature work; no merge, production transition, service replacement or
search implementation is authorized. Existing VPN service stays open. Lead owns
allocation, commit windows and contextual prose acceptance before editorial commits.

### EN repetition audit — implementer2 and implementer3; sufficient now

Keep the exact existing62/63-ID division in `translation-batches.json`. Each owner
reads the full English article and its Czech source context across all assigned
IDs, auditing repeated wording and especially the teaser/first-body-paragraph
transition. Own only assigned `index.en.html` prose plus the existing compact
review record. No changes to Czech bytes, pre/code bytes (including CRLF), URLs,
media/HTML attributes, article IDs, dates, source/review hashes, draft state or
shared files. Source facts, uncertainty, historical viewpoint/bylines and the
established translation voice remain authoritative.

The teaser before `<!--more-->` must make sense in index/RSS contexts; the complete
article includes it and should then develop the point rather than restate it.
For wp841, the two adjacent “You can now use” claims are a concrete review target;
retain the distinction between secure login and passkey-as-second-factor support,
hardware/software examples and all instructions. Editors may rephrase either
side using full context; do not delete every introduction, move/remove the more
marker, hide duplicated blocks with CSS or alter RSS's full-body contract.
Some source repetition is useful context; change only actual awkward duplication.

Evidence: list all inspected IDs, changed IDs and concise reasons; show original
versus revised lead/body for changed articles. Prove all125 remain drafts with
fresh source hashes and protected-byte/URL/metadata parity, plus unchanged Czech
tree. Agent prose audit is not human publication approval. Lead reviews edits in
context before each ordered commit; independent review follows completed changes.
This package is independent of UI/CTA implementation.

### UI alignment and localized CTA — implementer1; sufficient now

Own `assets/css/site.css`, `layouts/_default/baseof.html` (actual CTA location),
one English CTA asset under `static/theme/branding/`, its existing NOTICE,
necessary i18n labels and focused existing checks. No article/source-media edits.
Current `.pagination` is flex without justification/wrapping: center the group
with `justify-content:center`, allow wrapping, retain link/focus/current-page
semantics and ensure narrow screens have no page overflow.

Corpus read found84 article images,79 carrying `aligncenter`, and8 tables.
Center `.entry-content img.aligncenter` with block display and auto inline margins,
including linked images such as wp841's275×157 screenshot. Also center standalone
block photos/figures using scoped structural selectors where needed, preserving
explicit `alignleft`/`alignright` and inline emoji/icons. Do not apply unconditional
`display:block` to every image. Keep max-width100%/auto height and existing alt
text/links/captions. wp367 is a representative image+table page.

Tables currently use full-width `display:block`; use a conventional shrink-to-fit
scrollable box (for example `width:max-content; max-width:100%; margin-inline:auto`
with the existing block/overflow rules), checking actual intrinsic sizing. Center
the table box, not its cell text. Preserve table/caption/header semantics and
source attributes. Horizontal overflow must stay within the table, with usable
keyboard scrolling/focus; if CSS alone cannot achieve that, request only the
necessary render-wrapper/attribute ownership from lead rather than editing corpus.

English CTA visible text is **Join us**, matching existing i18n. Preserve the
original150×147 Tux image/green button identity, Czech original bytes and recorded
provenance. Produce one local English derivative by replacing only the button text
(small self-contained SVG embedding the source raster or existing raster tooling
is sufficient); retain Tux/arrow/geometry, avoid external fonts/resources, keep a
clear accessible `alt="Join us"`. Document derivative/tool/source hash in NOTICE;
do not invent a separate media license. No new design system or asset framework.

Two public read-only pages verified on2026-11-07: `https://vpsfree.org/` links to
`/registration/`; `https://vpsfree.org/registration/` returns200 with Registration
title. English CTA therefore links exactly there; Czech remains
`https://vpsfree.cz/registrace/`. Localize the separate main-site/footer link to
`https://vpsfree.org/` on English. The existing logo is a link to the current blog
home, so preserve that language-specific blog-home navigation; only a logo link
actually targeting the main Czech site would need the `.org` switch. Do not change
translated article external URLs or the shared Czech discussion identity.

Acceptance: before/after desktop1440/mobile390 captures of pagination, wp841
image, wp367/narrow table, and both language CTAs/footer. Check original Czech
graphic unchanged, English text legible at native size, targets/alt/focus correct,
no inline-icon disruption and no viewport overflow. Use existing browser tooling
and offline builds/current service where appropriate; no new server or live-preview
replacement in this design package. HTTP/build success is not visual acceptance.

### Search answer only

The search field is currently disabled; no search code/package is released by
this question. A small static full-text index built from published pages and
queried in the browser is the recommended direction (Pagefind is a reasonable
candidate). Separate language results/URLs, exclude unreviewed drafts from the
public index, and load the index only when needed. It requires no WordPress/search
server; tradeoffs are browser download size and client-side matching. Preview
draft search, indexing details and dependency selection wait for an explicit
implementation request. No further search research is needed for this answer.

## D10 sufficient brief: local Pagefind search and navigation follow-up

The user now authorizes Pagefind implementation; this supersedes D9's
search-answer-only boundary. Lead retains release/acceptance and main-agent UI
wording review. Architect owns this brief only. No merge, current-blog change,
forum request, configuration activation or service replacement is authorized by
this brief.

**Ownership/dependencies.** S10 owner `implementer0` owns the blog's search
template/partial and local JavaScript, article indexing attributes,
`content/search/index.{cs,en}.md`, i18n, `flake.nix`, `bin/build`, one small shared
indexing helper, `bin/preview`, `fixtures/hugo.toml` search-page mounts, affected
`bin/check`/`bin/check-release` assertions,
and concise README/authoring/deployment documentation. CSS search additions may
follow U10's yielded window. `implementer1` owns U10 only: left mobile toggle and
distinct current/disabled/usable pagination controls, preserving centering/wrap;
lead reports that package committed at `c829fbf` and CSS/index yielded. S10 must
preserve those changes. No article prose, translation state, imported data,
configuration, release-driver or admission edits belong to S10. Git windows
remain lead-controlled. This contract is sufficient for lead release; browser
and pinned-package behavior below are implementation checks, not product choices.

### Dependency, content and language contract

- Use `pkgs.pagefind` from the existing locked nixpkgs in both the development
  shell and Nix site derivation: read-only evaluation returned **1.5.2**. Do not
  refresh the lock or add npm/CDN packages. Record `pagefindVersion` alongside
  Hugo in build inputs. Current Pagefind docs describe 1.6.0; use the established
  JS API available in the pinned package, not unverified new UI components.
- Index rendered article titles and full article bodies only. Mark article
  title/body with `data-pagefind-body`; positively restrict selection to article
  pages (`params.article_id`, existing post layout), with explicit exclusion of
  review banners, bylines/navigation/taxonomy, archived comments and discussion
  controls. Do not index list summaries, search pages or arbitrary front matter.
  Preserve all source HTML, anchors, code, protected links and draft flags.
- Run Hugo first, then Pagefind, then the existing complete file/hash metadata
  pass. Production uses Hugo's published output: 125 Czech articles, zero current
  English draft articles. The indexing helper must detect zero eligible articles
  and skip indexing that root; otherwise Pagefind's default whole-body fallback
  when no body marker exists could index the empty site's navigation. Render a
  localized empty search state without importing a missing bundle. No fake
  article/sentinel or change of draft state is needed.
- Production and ordinary two-port preview each index their actual `cs/` and
  `en/` document roots separately, generating `/pagefind/` within each root.
  Explicitly use the document-root URL base `/` for result URLs; never leak the
  build's `cs/` or `en/` directory names into public links.
- Single-port VPN indexes its combined document root once. Pagefind separates
  documents by the existing HTML language (`cs-CZ` and `en`). Both search pages
  load the same origin-root `/pagefind/` bundle and let Pagefind select the page's
  language. Search pages are `/search/` and `/en/search/` on VPN; each production
  language host and ordinary language preview uses `/search/`. Generate these
  from Hugo page links, not string concatenation. VPN English article results
  retain their actual explicit root paths: **do not prepend `/en/`** to them.
  Do not merge language results or change SEO canonicals/hreflang.

Fixture content stays isolated: `fixtures/hugo.toml` may explicitly mount
`fixtures/content` at `content` and only `content/search` at `content/search`.
Retain `dataDir = 'fixtures/data'`; do not mount the real post tree or all real
content. This makes the genuine search UI available in both fixture topologies
without adding synthetic search articles or changing draft flags. Checks must
prove only fixture articles are searchable and both localized search pages exist.

### Small accessible UI and failure behavior

Replace the disabled sidebar input with a labelled ordinary GET search form
targeting that language's dedicated search page (`q` query parameter). Keep Flat
styling, an explicit submit control and keyboard focus. The results page uses a
small local adapter over Pagefind's native JS API; no custom index/engine,
framework, remote search request or new browser package is needed. Load the local
module on the search page when needed, show title links and short excerpts, and
bound result rendering with a simple additional-results control if necessary.
Use text-safe DOM construction; query strings and result metadata must not become
raw HTML. The result status/loading/empty/error state is announced accessibly;
preserve focus and provide a JavaScript-required fallback. Main approves exact
CS/EN labels, empty/error and preview-snapshot wording before commit.

All module/WASM/index requests stay on the served origin. Updating script checks
must allow only the intended local search assets; preserve production-only
Discourse opt-in and zero Discourse scripts/requests in all previews/drafts.
No search history/localStorage/service worker or persistent browser index is
required. Native Pagefind shards carry their own hashes; retain the ordinary
`/pagefind/` bundle, without a version registry or configuration asset-retention
extension. Do not declare its stable entry filenames immutable. An old open tab
can lose its referenced shard after a content release or rollback: catch module,
index and result-load failures, replace stale results with an explicit error and
reload action, and reinitialize from the current page on reload. This limited,
recoverable stale-tab behavior is accepted; error must not look like no matches.

### Preview freshness: explicit coherent snapshots

Keep the native Hugo server and all current binding/topology/fixture rules.
`bin/preview` prepares a fresh isolated destination, renders the selected real
draft corpus (or explicit fixtures) with the same environment/base URLs as its
server, and runs the shared indexing helper before serving. Start native
`hugo server --watch=false` against that destination; retain disabled live reload
and the explicit VPN `--baseURL`. Installed Hugo **0.167.0** help confirms that
it writes and serves disk by default; there is no `--renderToDisk` flag to add.
Do not use `--cleanDestinationDir` in the subsequent server startup, which must
preserve the already generated search bundle. Prove that the pinned server serves
that bundle and renders links consistent with the pre-index build.

This intentionally changes preview from watching edits to a snapshot, keeping
article HTML and search consistent. Print its snapshot status and exact rerun
command (including `--vpn`/`--fixtures` when selected), and show a concise preview
notice that edits require rebuilding the preview. The supported refresh is to
rerun the same preview command and reload the browser: it creates fresh output
and rebuilds both pages and index, removing stale/deleted articles. Do not add a
watcher, partial index patcher, second server or persistent shared output. Normal
clones need only Nix and the documented command. Managed previews retain service
registration/lifecycle guidance; this design does not stop or replace the
existing VPN service. The lead separately coordinates any authorized preview
update. A source edit while a snapshot is served must not silently update only
the page or only the index.

### Artifact compatibility, checks and recovery

The current release packager hashes all regular files under `cs/` and `en/`;
the configuration validator permits Pagefind JS/WASM/data suffixes and validates
the complete declared payload. Include every generated search file before
`metadata.json`, and extend local release fixtures to prove this inclusion and
tamper rejection. Keep metadata schema 1, clean exact-SHA release admission,
ordinary dirty draft previews and disabled activation unchanged. No CI workflow
or target-protocol change is needed unless a concrete existing check proves
otherwise; route such a conflict to lead. Rollback restores the previous entire
site/index artifact. No database, persisted content or account migration exists.
The old WordPress and current default-off hosting/recovery contracts stay intact.

Quick checks: pinned build and normal/release checks; article-marker and indexed
count checks; no production English draft content, fixture, nav/comment sentinel
or private metadata in search; positive CS/EN queries with correct same-language
URLs; graceful empty EN production; generated assets all hashed and releaseable.
Use actual browser API queries rather than grepping compressed index bytes.
Fixture terms should prove body/title inclusion and comment/navigation exclusion.
Build a real draft-preview corpus without changing drafts. Check production-root,
dual-loopback and VPN result routes, including an English explicit root article.

Browser acceptance after implementation: desktop/mobile search and U10 layout,
keyboard form/results/status/reload behavior, no off-origin search requests or
forum access, missing-shard/load-failure state, and no console errors. Verify an
edit/add/remove is absent from the existing snapshot but reflected after the
documented rebuild and reload, with old tokens/removed results gone. Include a
temporary new draft, without committing fake corpus. Prove existing feed/routes,
draft banners and language links still work. Lead schedules registered test
services and required independent final review; long/uncertain Nix/browser runs
use the existing monitoring policy. Do not widen into full prose review.

Evidence: existing `flake.nix`, build/preview scripts, article/base templates,
check/release scripts and default-off static-host validator; local pinned Nix
evaluation and Hugo server help. Official sources (four bounded pages):
[post-build bundle](https://pagefind.app/docs/),
[body selection](https://pagefind.app/docs/indexing/),
[language separation](https://pagefind.app/docs/multilingual/),
[JS API/loading/reset](https://pagefind.app/docs/api/).
Czech search has no stemming in the documented engine; do not promise Czech
morphological matching. Actual pinned browser behavior and snapshot startup
remain to be verified by S10; no current service or production result is claimed.

## D11: English blog and KB link destinations

The user explicitly authorizes changing destinations of blog-article and KB
links in English output to their verified English equivalents. This supersedes
D6's English-to-Czech-only article-link rendering, not source-byte preservation.
Keep Czech/source translations, prose, link labels, code, front matter, dates,
source hashes, media and every other destination (including mailing lists)
unchanged. Resolve links during rendering, offline, using the existing
`layouts/partials/article-html.html`; no mass content edits or online builds.
Main retains meaningful label/copy decisions. No KB writes, production changes,
services or integration are authorized here.

### Sufficient independent inventory and KB mapping briefs

- **L11-I, implementer2, released by lead:** inspect anchor attributes in all 125
  EN article bodies, excluding `pre`/`code` and HTML comments. Own session
  `language-link-review.md` and its compact machine inventory only. Record exact
  raw href, decoded matching form, article ID/occurrence, query/fragment and
  classification (blog article, blog media/archive/unknown, KB, other/protected).
  Match Czech article paths to immutable IDs in `data/articles.json` and actual
  paired Hugo source routes; do not infer translations from title strings.
  Supply distinct KB page IDs and fragment contexts promptly to L11-K. Report
  complete counts and unknowns; no prose rereading, source edits or network crawl.
- **L11-K, implementer3, released by lead:** consume L11-I's
  distinct linked KB targets, inspect only those Czech pages and their evidenced
  English candidates. Own session `kb-link-review.md` and `kb-link-map.json`
  (candidate data, not application source). Use native `kb-page get --wiki cz`
  and `--wiki org`, preserving credentials outside output. Workspace KB guidance
  identifies the invisible `<page>` tag as translation authority: shared value
  derives from the English page ID, while actual Czech/English IDs differ.
  Validate the candidate English page exists and has the matching tag, or record
  the actual language-switch link as authority when appropriate. No title/slug
  guessing, automatic domain substitution or KB-wide enumeration. Preliminary
  architect scan found 39 distinct KB hrefs (including fragments), not 39
  distinct pages; L11-I supplies final deduplicated counts.
- Read-only native confirmation: `kb-page get --wiki cz navody:vps:api` returns
  `<page>manuals:vps:api</page>` (2026-11-07). This establishes that one candidate
  identity only; it does not yet certify the English page or `#cli` section.
  For linked fragments inspect rendered IDs and section meaning in the paired
  pages using only the necessary public KB reads. Equal spelling alone is not
  proof of equivalent sections. Keep missing pages, missing mappings, ambiguous
  matches and unmapped fragments explicit; never discard a fragment to make a
  link appear successful.

L11-K's bounded data interface is schema 1 with `pages` keyed by the canonical
Czech colon-separated page ID. Each verified entry has `target` (exact absolute
English public page URL without query/fragment) and `fragments` (explicit source
fragment to equivalent target fragment). Keep evidence URLs, tag values, observed
date/source hashes and unmatched occurrences in its review record. Do not put
credentials or full wiki pages in the map. An empty fragment needs no fragment
mapping. Optional top-level `aliases` maps an observed source URL path to its
Czech page ID; the root's observed identity is `domů`, with `/` as its alias and
`https://kb.vpsfree.org/home` as the evidenced target. Do not infer aliases from
similar titles or silently treat an unrelated page as a translation. The renderer
owner will copy only accepted entries into `data/english-links.json`; candidate
mapping does not publish or change the KB. This package can proceed independently
of search and the renderer implementation.

### Sufficient renderer contract and ownership

**L11-R, implementer2 after lead accepts L11-I and confirms capacity:** own only
the existing article HTML partial (plus one small adjacent link partial if that
keeps it readable), accepted `data/english-links.json`, link-contract portions of
`bin/check`, and a concise authoring note. S10 owner0 has yielded `bin/check` and
the index after commit `95a3cae`; preserve its search assertions and U10 changes.
L11-K remains read-only mapping evidence; L11-R alone copies accepted data into
the blog repository. Lead owns commit windows. Renderer work may begin against
a small verified map/fixture without waiting for all KB dispositions; final
acceptance requires the complete finite matched/unmatched report.

1. **Blog identity and build availability:** make the exact Czech permalink-path
   to article-ID lookup from `data/articles.json`, then select the currently
   rendered English Hugo article with that immutable ID. Use its actual
   `.Permalink`, not a translated-title slug or `/en/` guess. Cover existing
   root-relative and exact `http(s)://blog.vpsfree.cz` / protocol-relative forms;
   only recognized article paths qualify. In production, an unavailable/draft
   English counterpart falls back to the article's canonical Czech permalink.
   Preview includes drafts and therefore selects the local English page, using
   port 1314 or its explicit single-port VPN root path. No unpublished path may
   be synthesized from a source file. Do not modify shared `discussion_url`.
2. **Blog fragments:** current 55 cross-article occurrences have no query or
   fragment; the two fragment-only links refer to their current page and stay
   unchanged. Preserve query suffixes when mapping an exact article path.
   A fragment-bearing article link may select EN only when that exact target
   anchor is known to exist there (e.g. preserved `more-ID`, historical comment
   IDs and the common comments/respond anchors). Otherwise retain the absolute
   Czech URL and original fragment; do not invent translated heading anchors.
   This conservative fallback also applies to unknown future fragments. No new
   global heading/anchor registry is required.
3. **KB eligibility:** accept only the exact KB authority `kb.vpsfree.cz` on
   normal HTTP(S)/protocol-relative links, without userinfo or an unexpected
   port. Normalize slash/colon page notation and valid percent-encoding once for
   lookup, after HTML entity decoding; malformed/ambiguous input stays unchanged.
   An observed path alias such as `/` takes precedence. Use the verified English
   `target` for an unfragmented link. For a nonempty fragment, require an explicit
   equivalent entry in `fragments`; otherwise keep the complete original Czech
   link and record that occurrence as unmatched. Do not attach the old fragment
   to a different English heading or remove it. KB links remain absolute public
   KB URLs in both preview topologies and production.
4. **Queries and legacy DokuWiki forms:** the complete current inventory contains
   no blog/KB query strings or `doku.php?id=` forms. Do not expand D11 into a
   general legacy-URL converter. Tests must prove a harmless query suffix on a
   recognized path survives unchanged, including order/escaping, and legacy
   `?id=`/`doku.php?id=`, revision/action parameters (`rev`, `do`, export/media)
   remain unchanged unless an exact alias and its semantics are separately
   verified. They are deliberately unsupported matches, not guessed translations.
   An encoded ordinary KB page path can match the same verified page; this must
   not percent-decode or rewrite query values. No broad `.cz`→`.org` replacement.
5. **Exact edit boundary:** retain the existing tokenized HTML traversal and
   `pre`/`code`/comment exclusions. Change only actual navigational `a[href]`
   destination values in English; preserve surrounding text, quotes and other
   attributes. Decode entities for matching, then safely encode a replacement
   exactly once. Unchanged values keep their original bytes; preserved query
   suffixes must not acquire double `&amp;` escaping. Do not rewrite literal URLs,
   `data-href`, script text, media attributes or code. Existing independent media
   localization stays as it was. Taxonomy links, self-fragments, unknown blog
   targets, existing English KB links and all other domains remain unchanged.
6. **One rendering path:** full articles, summaries and full-content RSS all
   consume the same helper. Absolute mapped article URLs work in feeds as well
   as HTML. No network lookups during Hugo/Nix builds or browser navigation
   interception, new runtime service, crawler or translation engine. Main checks
   any meaningful label/copy need; link-only delivery changes no labels.

The source URL-parity check remains valid: all 531 original EN hrefs still match
their Czech originals. **Rendered** English href parity is replaced only by the
finite authorized blog/KB resolution rules above. Do not weaken source/hash/code
checks merely because the permitted rendered destination changes.

### Acceptance, evidence limits and recovery

L11-I's final inventory is 531 href occurrences in 125 EN files: blog 134
(55 article, 75 media, two taxonomy and two self-fragment), with 44 exact article
targets/41 immutable destination IDs; all paired EN sources exist as drafts.
KB has 70 occurrences, 39 exact hrefs, 27 page paths and 13 fragment hrefs
(23 occurrences). No unknown blog destination, current query/legacy-ID form or
English-host link was found. See `language-link-review.md` and its machine
inventories; no further corpus prose audit is needed.

Quick fixture checks cover published EN target, absent/draft EN target fallback,
real-draft previews on both topologies, absolute/protocol-relative/root-relative
blog links, verified KB page/section, root alias, unmapped page/section, encoded
HTML/URL spelling and untouched legacy/action query forms. Preserve all existing
code/comment/literal/data-attribute/quote/query tests, revising only their formerly
Czech-only rendered article expectations. Prove summaries/RSS match article
routing and source/metadata hashes, non-target hrefs and all Czech output remain
unchanged by D11. Build the real corpus and reconcile every eligible occurrence
to mapped or explicit fallback, using the accepted finite KB map; assert each
local English result path exists in that build. Normal search/release checks
remain required, without making D11 depend on production forum tests.

L11-K reports missing Czech pages `informace:openvz`,
`navody:vps:vpsadminos:storage` and `navody:vps:zalohovani`; preserve their original
links rather than guess replacements. L11-K initially rejected infrastructure as
copied Czech prose; K12 corrects that factual finding below. Absent historic fragment IDs likewise remain
unmatched, even if a similarly named current section exists. These are honest
coverage limits, not requests to repair the KB. Final counts and exact fragment
evidence belong to L11-K's completed report.

Final joint review/browser evidence follows the lead's S10/U10 sequence; no new
service or production check is implied. This changes rendered output only, with
no persisted data/schema migration. An ordinary source/artifact rollback restores
the former destinations; saved source bytes and current deployment/admission
constraints remain intact. No current production link update is claimed.

## D12 correction: semantic KB destinations and mobile sidebar flow

The user reports the English wp-490 CLI link still reaches the Czech KB and
requests reevaluation of **all eight fallback hrefs / 18 occurrences**. D11's
requirement that a historical Czech anchor still exist was too strict. This
section supersedes that rejection rule: an equivalent English destination may
be verified from the article's meaning and current KB navigation even when the
old Czech anchor or page has disappeared. Lead chooses normal document flow for
the expanded mobile sidebar to address the reported issue. Both are bounded corrections; Pagefind,
article source/prose/URL bytes, Czech content, metadata, code and other external
destinations remain unchanged. No KB writes, services, production actions or
integration are authorized by this brief.

### K12 evidence package, implementer3, ready for lead release

Update the existing session `kb-link-review.md` with a D12 section and
`kb-link-map.json` candidate. Reuse L11's inventory and accepted 23 page pairs /
nine fragment pairs; do not rescan 531 hrefs or audit 125 articles. Inspect the
surrounding paragraph/link label and only the additional local article context
needed to establish intent for these eight hrefs:

| Czech target | Occurrences / required question |
| --- | --- |
| `navody/vps/api#cli` | Nine in wp-253, wp-264, wp-284, wp-455, wp-474, wp-490, wp-601, wp-709; identify installation, use or general CLI-documentation intent for **each occurrence**, including both in the repeated article. |
| `informace/chat#bouncer` | One; identify the actual bouncer function and current equivalent documentation, not just any IRC page. |
| `navody/vps/datasety#stahovani_zaloh` | One; verify equivalent backup-download instructions rather than general dataset management. |
| `navody/vps/vpsadminos#user_namespaces` | One; verify the user-namespace concept/behavior referenced in context. |
| `informace/openvz` | Two; verify historical OpenVZ meaning without substituting unrelated current virtualization documentation. |
| `navody/vps/vpsadminos/storage` | Two; verify the referenced storage model/operation. |
| `navody/vps/zalohovani` | One; establish the backup operation meant by the historical article. |
| `informace/infrastruktura` | One; verify the content of the previously rejected infrastructure candidate in its article context. |

Use cached/native KB source and current rendered sections first. Matching
translation tags/language switches remain strong evidence, but may now be
supplemented by explicit current KB navigation, a move notice or a limited search
of the English KB for the specific linked topic. Read only plausible pages
discovered that way and verify actual English content, section meaning and the
rendered target ID. A missing source page or old ID is **not** a sufficient
reason to stop. A similar slug/title or mere HTTP 200 is **not** sufficient proof.
Do not redirect the reader to unrelated modern instructions, guess an anchor,
or silently drop the section requirement.

For each occurrence record intent, exact proposed English URL, navigation/search
evidence, relevant section/anchor and a short equivalence rationale; group only
when contexts support the same destination. For `#cli`, a shared parent section
covering installation and usage is acceptable if its actual contents satisfy all
nine contexts. If they require different targets and no such shared section
exists, report that concrete conflict to architect/lead before inventing an
article-specific mapping mechanism. Main accepts semantic mappings and any
visible label implications. If no defensible English equivalent is found after
the bounded checks, record what was checked and the remaining reason; retain the
original only as that evidence-backed unresolved outcome. No mandatory claim
that all 18 can be mapped.

Prefer the existing schema-1 `pages[id].target` and `fragments` for same-page
equivalents. When a verified old fragment now leads to a **different** English
page, allow the narrow optional `pages[id].fragment_targets` map from old
fragment ID to full English URL (including its verified destination fragment).
This explicit map takes precedence over same-page `fragments`; it avoids changing
other links to that source page. New entries must use exact HTTPS
`kb.vpsfree.org` destinations, with no credentials/ports/action queries. Do not
add cross-page machinery if the accepted evidence fits the existing fields.
Keep evidence in the review record, not copied whole wiki pages in application
data. Report candidate hash and revised mapped/unresolved counts covering all 18.

K12's partial evidence corrects the infrastructure rejection: the identical
source is an English Hardware Inventory, not copied Czech prose. Its existing
language switch and content support the English infrastructure URL. Owner3 also
reports that all nine CLI contexts fit `manuals/vps/api#using_cli`. Two verified
cross-page section candidates require the already defined `fragment_targets`:
`navody:vps:datasety#stahovani_zaloh` to
`https://kb.vpsfree.org/manuals/vps/backups#downloading_backups`, and
`navody:vps:vpsadminos#user_namespaces` to
`https://kb.vpsfree.org/manuals/vps/userns#user_namespace`.
These are owner3's evidence-backed candidates pending main/lead semantic
acceptance; they do not broaden the renderer contract or authorize source writes.

### R12 map application, implementer2 after evidence acceptance

Own `data/english-links.json`, only the necessary KB portion of
`layouts/partials/english-link.html` if `fragment_targets` is needed, associated
link checks in `bin/check`, and a concise existing-documentation correction if
it still states the old strict-anchor rule. Apply only main/lead-accepted K12
entries; leave the other accepted pairs and blog availability/routing behavior
intact. A full target must insert a preserved harmless query before its fragment,
encode once and keep the D11 action/revision exclusions. Source article links
are unchanged; summaries, articles and RSS use the same output mapping.

Quick checks explicitly cover wp-490 and every formerly unresolved occurrence,
the nine CLI intents against their accepted target(s), correct existing target
anchors and unchanged non-target destinations. If used, test cross-page fragment
precedence, query ordering/escaping and an unknown fragment retaining its source.
Reconcile the complete original 70 KB occurrences against the accepted map without
repeating KB network calls in builds. Preserve all source/hash/draft checks and
S10 search checks. Main/lead accepts the finite map before commit; index windows
and joint review remain lead-owned. K12 evidence may run in parallel with mobile
CSS; R12 waits only on the mapping decisions it applies.

### M12 mobile flow package, implementer1, independently sufficient

Current CSS at `@media(max-width:1199px)` absolutely positions `.sidebar-widgets`
below the 162px header, caps it at `calc(100vh - 162px)`, adds `overflow:auto` and
slides it offscreen. Replace that mobile-only drawer behavior with collapsed
`display:none` and checked-state normal-flow expansion. Expanded widgets use
available width, natural height and ordinary document scrolling: no fixed or
absolute widget positioning, height/max-height cap, nested vertical scrollbar,
offscreen transform or overlay over article content. The article starts after
the expanded navigation. Desktop's 300px sidebar and existing appearance remain
unchanged; retain the left native checkbox/label control and visible focus.
Hidden widgets must be absent from keyboard navigation. Do not add JavaScript,
a menu framework or scroll-position manager.

Owner1 edits only the mobile CSS rules in `assets/css/site.css`; a minimal native
control markup correction in `layouts/_default/baseof.html` is permitted only
if needed for accessibility. No search layout/API changes. Quick build/checks
preserve U10 pagination distinctions and existing search/links. Browser evidence
must exercise opening at the top, scrolling the document to the **last archive
link/widget**, then onward into the article, and closing/reopening after a page
scroll; test narrow phone and short landscape viewports, keyboard toggle/focus,
both languages and desktop unchanged. Assert no clipped bottom widget, nested
sidebar vertical scrolling or horizontal viewport overflow. Use the existing
authorized preview/test workflow; this design launches/stops no service.

Compatibility/recovery: all changes are static CSS/output mapping; no persisted
schema, content migration or production behavior is activated now. Prior complete
artifact/source rollback restores the previous rendering. Lead retains exact
feature windows, main writing/semantic acceptance and final independent review;
actual preview/browser acceptance follows implemented evidence, not CSS inspection.

## D13 sufficient briefs: dated bundles, workflow proof and WordPress retirement

The user requests human-readable, date-prefixed article folders, asks how the
existing GitHub workflow will be tested, and authorizes removing WordPress from
configuration while retaining its disk data. These are source/preparation
packages only: no default-branch integration, live deployment, data deletion,
service change or cleanup is authorized. Implementer1's independently assigned
single-line search input/button change remains separate; preserve Pagefind
behavior. Lead accepts releases and coordinates overlapping files/index windows.

### B13 dated article directories — sufficient for implementer2

Hugo's current leaf bundles are `content/posts/<directory>/index.cs.html` and
`index.en.html`. Directory names organize source; explicit `translationKey` and
`params.article_id` identify the pair, explicit `url` controls public paths, and
shared data uses article IDs for bylines, discussion and feeds. None must change
when a bundle moves. This repository convention therefore need not use `wp-ID`
as a directory name. Keep those IDs as stable metadata, not as title matches.

Rename all 125 existing bundles to
`YYYY-MM-DD-<english-title-slug>`, preserving all **250 article files byte for
byte**. Take `YYYY-MM-DD` literally from the original Czech frontmatter `date`
calendar portion, without timezone conversion, current dates or rewriting any
front matter. Slug the current English title deterministically: remove straight
and typographic apostrophes, Unicode NFKD-to-ASCII, lowercase, collapse runs of
non-ASCII-alphanumeric separators to one hyphen, trim end hyphens. Do not derive
the folder from public `url`: two current English URL slugs differ from the title
slug and must remain unchanged. The bounded title inventory found 125 nonempty,
unique slugs (longest 77 characters); owner verifies full dated-path uniqueness.
If a normalized dated name collides, append `-<immutable-article-id>` to every
member of that collision group; an empty title slug uses `article-<id>`. Reject
path separators/traversal and unrelated existing directories. Never overwrite
or resolve identity by content similarity. Once assigned, a directory remains
stable through title edits; renaming it again is an explicit editorial operation.

**Files/interface:** owner2 owns the directory moves, path-dependent portions of
`bin/check`, importer and its checks, `data/migration/source-manifest.json`, and
affected README/AGENTS/authoring skill/authoring/migration documentation. No
article bytes or other metadata maps change. Runtime Hugo helpers already use
`params.article_id`; preserve that approach. Tests and ordinary tooling must
discover pairs by frontmatter ID/language with duplicate detection rather than
constructing `content/posts/<id>` or treating `.parent.name` as identity. Human
instructions use the dated title folder and an independently assigned immutable
ID. Approved static image paths keyed by article ID remain unchanged.

The existing migration manifest is sufficient path authority; add no slug
registry. Update only its article `cs_file` paths and corresponding
`generated_files` path keys, retaining all content hashes, counts, routes and
identities. Import projection reads the explicit ID→`cs_file` map from this
repository's source manifest (or a supplied fixture manifest), validates the
path and ID association, and uses those locations in empty-output and in-place
reruns. Do not silently regenerate `wp-ID` folders or infer a new path from a
changed title. An unknown imported ID requires an explicit path assignment
before writing; it must not overwrite another bundle. Preserve the existing
generated-file/manual-edit check and English-file exclusion. No new private
export or WordPress access is needed; test mapping/overwrite behavior with
local fixtures.

**Acceptance/checks:** capture old/new ID+language→file-byte SHA-256 maps and
prove all 250 hashes identical; both languages share each renamed directory.
All IDs, dates, public routes, feed GUIDs, discussion URLs, review/source hashes,
media and approved-comment files remain identical. Update manifest references
and prove every listed hash still matches its moved file. Importer tests cover
same mapped location on repeated/empty-output projection, manual Czech edit
refusal, no English overwrite, invalid/duplicate map refusal and unknown-ID
refusal. Normal build/check/release checks must pass; compare route/feed/link
and paired-page behavior across production/draft preview, with no renamed public
URL. Git should show exact file moves, not translated-content edits. An ordinary
reverse move restores source layout; no on-disk application migration exists.
Lead sequences shared `bin/check`, README/authoring edits and commits with other
packages. This package does not wait for workflow or configuration work.

### W13 existing workflow test strategy — sufficient for implementer0

This is a bounded explanation/evidence task, not authorization for another
workflow or dispatch mode. Current `.github/workflows/build.yml` runs
`nix develop -c bin/check`, `nix develop -c bin/check-release` and
`nix build .#site` for feature pushes/PRs. Only the canonical repository's
protected `main`, outside a PR, packages and uploads `blog-<exact SHA>`; existing
`workflow_dispatch` on that same main is eligible. Permissions are read-only,
checkout credentials are not persisted, and there is no deployment credential
or activation step. Do not weaken those conditions to test on a feature branch.

Owner0 may reconcile a concise test explanation in existing `docs/deployment.md`
and report evidence already obtained; no workflow/script changes are justified
by this inspection. Existing local packager fixtures cover exact clean identity,
dirty/null rejection, deterministic archives, complete hashed Pagefind payload
and tampering/undeclared files. Configuration's mocked acquisition/transaction
tests separately cover exact protected-main/workflow/run identity, missing or
expired artifacts, malformed payload, stale/concurrent requests, interruption
and rollback. Production CLI admission deliberately remains unavailable; tests
do not prove otherwise. Reuse valid results and rerun affected checks only under
normal final verification, not an extra synthetic release system.

**Remaining real GitHub gate:** an ordinary feature push proves the runner/Nix
checks at that feature SHA but deliberately skips trusted artifact upload. After
later explicit main integration approval, a push or separately authorized
existing main dispatch must run at the exact intended protected-main SHA. Record
workflow/run/attempt and final head; verify the actual upload and retention,
download the exact artifact locally, and validate its receipt/archive/input graph
with the existing validator and independent read-only API facts. This proves the
main-only path without activating a VPS. Main protection, workflow ID, retention
policy/artifact visibility and actual run receipts are external facts to verify,
not assumptions or a reason to bypass guards. Running today's older initialized
main would not test the unmerged candidate. No dispatch/push/network operation is
part of the architect's brief execution; lead controls authorized CI execution
and monitoring. Production admission, credentials and transition remain separate
gates. Owner0 reports any concrete uncovered defect before changing workflow
behavior; no new framework or release-eligibility mechanism is released here.

### C13 WordPress source retirement — superseded by D14, not the current target

Observed configuration at `7bab9781d0a5eb1aed5914f0aed99f6d7d491632` imports
`int.blog/wordpress.nix` and the default-off static module. WordPress owns its
nginx port-80 vhost, PHP pool, local MariaDB provisioning, isolated CLI wrappers,
init and five-minute cron timer, plugin/theme/language inputs and WordPress-only
HTTP/firewall/email restrictions. `module.nix` still expects nginx, mysql,
phpfpm, wordpress-init and a local port-80 response. The public proxy still points
at that port. Source removal is authorized; **this candidate alone is not a
deployable static transition** while static serving/admission is disabled.

Owner3 owns only `cluster/cz.vpsfree/containers/int.blog/{config.nix,module.nix,
wordpress.nix}`, its exclusively used `packages/` sources, a small retention-only
module if useful, `tests/blog-static-module.nix`, and existing
`docs/operations/blog-static.md`. Remove the active WordPress import and service,
PHP/MariaDB/cron/wrapper declarations; remove unused site-local package/policy/
theme files after a reference check. Update the module fixture and retire
WordPress-only health checks, including the port-80 check. Do not fabricate a
successful static health check while static serving is disabled. Leave container
ID/address, internal DNS, public proxy, English DNS/TLS, static listener/pull
defaults and admission fence unchanged. Preserve the enabled firewall and the
static candidate's exact proxy-only policy; do not broadly open 80/8080/3306.

C13's pinned evaluation found that the static candidate's virtual hosts previously
relied on WordPress to enable nginx. In `int.blog/config.nix`, set
`services.nginx.enable = config.services.vpsfree-static-blog.enable` so the
default-off state stays off and enabling the candidate enables its web server.
Keep `static-blog.nix` defaults/admission unchanged. Test both composed states;
virtual-host declarations alone do not prove that nginx runs.

Lead released one narrow prerequisite correction in `static-blog.nix`: move
`default = true` from the unknown-host listener entry to
`services.nginx.virtualHosts.static-blog-unknown-host.default`. The pinned nginx
vhost option declares that boolean and uses it to generate `default_server`;
the listen-entry option does not exist. Keep the explicit IPv4 port-8080 listen
address and unknown-host 444 response unchanged. Owner3 makes this a separate
normal-hook fix commit before retirement. The revised fixture must force enabled
nginx unit/config generation, which exposed the invalid option, and distinguish
a disabled module's placeholder localhost vhost from actual nginx activation.
This exception does not enable serving or change the admission boundary.

**Data and ownership:** pinned NixOS modules locate the complete WordPress state
under `/var/lib/wordpress/blog.vpsfree.cz` (including uploads/fonts and secret
keys), and MariaDB state under `/var/lib/mysql`. They reside on persistent
container storage; no dedicated site mount is declared. Preserve those complete
trees and every other existing persistent file, backup, log and container volume
in place. Do not add deletion, truncation, recursive permission/ownership changes,
`tmpfiles` removal/aging rules, state moves, database drops, user-home removal or
garbage collection. Service removal must not run the former init/migration job.
Never expose secret-key/database contents while checking this.

Retain the existing system account/group identities needed to own those files,
without running WordPress or MariaDB: `wordpress` remains a system user in the
nginx group with its existing allocated UID; retain nginx/mysql ownership users
and groups at the same pinned IDs (the inspected module IDs are nginx 60 and
mysql 84). Do not guess a numeric WordPress UID, allocate a different one or
chown stored data. A small explicit ownership-only declaration is preferable to
keeping PHP/database services alive. Check effective old/new user/group settings
and activation/tmpfiles behavior from the pinned modules. Actual on-machine
UIDs, paths and recovery snapshots remain a read-only pre-transition verification
gate; source evaluation is not proof of live data retention.

**Checks/recovery:** module evaluation asserts WordPress sites, PHP pool,
MariaDB service, init/cron/timer and wrappers are absent; retained ownership is
present; disabled static module still has no listener/pull unit activation and
its enabled fixture preserves roots/feed/PHP-denial/proxy-only safeguards and
blocked scheduler. Inspect resulting activation/tmpfiles/service removal paths
for destructive state handling, run formatting/hooks and the required exact
`int.blog` configuration build without activation. Long builds use the existing
monitor policy. No SSH, dry-activation, live stop or deploy belongs to C13.

Before any later approved transition, preserve the exact prior system generation,
WordPress/config source/input graph and complete DB/uploads/secret-key backups;
do the existing brief changed-content check. With WordPress retired, changing the
proxy alone is **not** a rollback: first reactivate the recorded prior system
generation with compatible original MariaDB and retained account IDs/data, verify
WordPress recovery, then restore its proxy path. Retain the old generation/store
closure; no GC is authorized. Static-content rollback still uses its own receipt
and never rolls back Discourse. Document the inactive candidate's missing-serving
condition plainly so source removal is not mistaken for transition readiness.

These packages preserve source/identity and recovery contracts while changing
source organization and future configuration. Main owns user-facing wording,
lead owns semantic acceptance/index sequencing and independent final review.
Architect inspected files and local package definitions only; no runtime or
GitHub-path verification is claimed by this design.

## D14 current transition contract: keep WordPress through static validation

The user's revised sequence is authoritative: keep WordPress, prepare/deploy the
system, test GitHub build and artifact delivery, verify the generated site, then
switch only after a separate decision. This supersedes C13 retirement and any
documentation claiming the initial candidate removes WordPress. U13 search-row,
P13 dated bundles, the valid nginx option fix and W13's distinction between feature
checks and protected-main artifacts remain applicable. This design correction
authorizes source preparation only, not a deployment, default integration,
service operation or public switch by the architect or implementers.

### C14 restored coexistence source — sufficient for implementer3 now

Restore the published `7bab9781` WordPress composition: active hardened port 80,
PHP pool, MariaDB, init and cron, site packages/policies, ownership and original
health checks. Keep the separate static candidate/default-off pull and exact
proxy-only 8080 boundary; public proxy remains on WordPress port 80. Remove the
retirement-only ownership module and nginx-enable conditional introduced by
C13. WordPress again supplies nginx enablement. Do not simplify or downgrade its
existing firewall/header, writable-path, SMTP, DB or cron protections.

Preserve narrow fix `36f1f567`: the unknown-host vhost owns `default = true`,
not its listen entry. The strengthened fixture must evaluate actual nginx
unit/config generation and prove both composed states: disabled static leaves
WordPress effective behavior unchanged; enabling static retains WordPress on 80
and adds the intended 8080 hosts/roots, feed mapping and unknown-host rejection.
Keep scheduled pull blocked and production mutation CLI fenced. Preserve the
original persistent state, container identity/address, proxy, DNS, source pins
and forum configuration. Change no running system.

Owner3 owns the restored `int.blog` source/test paths from C13 and correction of
`docs/operations/blog-static.md`; no release-helper redesign is included. History:
retain published `7bab9781` and prerequisite `36f1f567`; omit obsolete unpublished
`314f3881` from the feature series instead of stacking a revert/fixup. After the
completed old build and a clean owned-tree check, use the lead's narrow feature
rebase/drop window. Preserve prior refs/recovery evidence; no broad reset, clean,
stash or default rewrite. The successful pure build of `314f3881` proves only
that superseded source; its retained output is not evidence for restored C14.
Run affected module/quick checks and exact new-source build/review under the
normal procedure; lead controls when held downstream work resumes.

### W14 documentation correction — sufficient for implementer0 now

Amend unpublished copy-only `45d04bc` atop the same `14da1cf`, retaining its useful
workflow-test explanation while replacing retirement/rollback claims with this
coexistence sequence. Do not rewrite published `b5` lineage or U13/P13 work. Own
only the existing blog deployment guide for this correction; main accepts final
user-facing wording. W14 does not alter workflows, package eligibility, source
identity, publication permissions or dispatch any run.

### Actual network path and operational gates

Actions **builds and uploads an artifact**. The container fetches it over outbound
HTTPS using a read-only artifact credential, then validates/stages it locally.
Actions needs no SSH route to `blog.int.vpsfree.cz`/172.16.8.4; open no inbound SSH,
public backend port or new proxy route for deployment. Actual outbound GitHub API
and signed artifact-storage reachability, credential permissions, protected-main
policy, verified workflow ID and artifact retention/visibility remain unverified.
These are concrete operational prerequisites, not evidence that the existing
disabled pull driver already deploys on push.

Inspected helper behavior is precise: `prepare` calls `acquire` and `stage`,
validates current protected-main/run/artifact identity, and writes an immutable
`releases/<SHA>-<archive-hash-prefix>` tree/archive and receipt. It does **not**
write `current` or activate nginx content. Its filesystem lock is serialization,
not machine admission; any later target-side invocation still needs the normal
explicitly authorized operation and installed machine ownership. `pull`,
`activate` and `rollback` refuse with `machine-admission-unavailable`; there is
no supported bypass flag/environment or permission to call fixture internals.

This distinction exposes the remaining HTTP-staging prerequisite: the 8080
vhosts currently read `/var/lib/blog/current/{cs,en}`, so successful `prepare`
alone does not make the newly staged artifact available there. Before claiming
8080/browser validation, release and verify the existing driver's installed
machine-admission integration for a **content activation on the private static
listener while public traffic remains on WordPress**. That is separate from
public proxy cutover. Do not hand-create `current`, weaken the fence or invent a
coordinator bridge in these source-restoration packages. Pure artifact validation
can proceed independently; the admission prerequisite must be resolved before
operational HTTP activation. No new product preference blocks restored source,
and no further driver implementation is implicitly released by this brief.

### Ordered later rollout and recovery

1. **Prepare and separately approve the system step.** Review/build the restored
   coexistence configuration, retain exact old generation/input graph and complete
   DB/uploads/secret-key backups, and obtain normal machine ownership. The later
   staging configuration may enable the isolated 8080 listener/storage/user while
   keeping WordPress, all its health checks and public proxy unchanged. Verify
   WordPress still serves correctly after that system deployment. Merely writing
   this order does not execute or approve deployment.
2. **Prove the actual Actions artifact.** Feature checks remain useful, but the
   existing release upload accepts only the intended protected-main SHA. Obtain
   separate repository/default integration approval before placing the candidate
   there; do not pretend today's older main tests it. A later authorized push/run
   builds the pinned site and uploads its exact artifact. Record run/attempt,
   source SHA, inputs, hashes and real download/retention evidence. No VPS build
   or SSH push is involved.
3. **Fetch, validate and stage without a public switch.** Under the approved
   target operation/ownership, use the read-only credential and existing `prepare`
   path. Verify complete hashes, routes/assets, feed identities, search index and
   publication exclusions; retain archive/receipt. Resolve the admission gate
   above before activating that exact content for 8080 HTTP/browser checks with
   the intended Host headers. Keep WordPress and public proxy on 80 throughout.
   A missing/expired artifact keeps existing serving unchanged and calls for an
   authorized rebuild of that exact SHA, never selection of an older artifact.
4. **Review the generated-site evidence, then seek separate cutover approval.**
   Verify representative/full-manifest behavior as required, both hosts' routes,
   search, media, comments/feed continuity and reviewed translation policy. An
   artifact that correctly excludes all unreviewed English drafts is a valid
   build test, not proof of a full bilingual launch. English DNS/TLS, legacy
   aliases and forum runtime setup remain their own launch gates. Briefly check
   for changed WordPress content/comments and refresh only if necessary; no
   writer freeze. Only a later approved proxy change sends public traffic to
   static content. WordPress retirement, if still wanted, is a later separate
   step after confidence in the new site, not part of initial preparation.

With WordPress retained and verified, initial cutover recovery can restore the
original proxy path to its still-running port-80 service. Retain the prior system
generation/data for failures requiring system rollback too. Static-content
rollback uses its own admitted transaction and exact receipt; no forum/DB data
is rolled back or deleted. Keep all original backups/owners/store recovery
material and no cleanup/GC. Deployment evidence supplies neither integration nor
session-lifecycle permission. Lead owns later operation approvals, holds and
exact-source acceptance; no operational success is claimed here.

## D15 sufficient source brief: GitHub webhook wakes artifact preparation

The user rejects periodic polling and requests a GitHub notification that causes
the blog container to fetch the artifact. Choose a **native repository
`workflow_run` webhook**, filtered to completion/success of the configured Build
blog workflow. It fires after the workflow, including its artifact upload, has
finished; no new Actions notification job, CI secret or workflow permission is
needed. A direct CI notification has no demonstrated advantage here and is not
selected. Preserve D14's active WordPress/public port-80 service and separate
later cutover. This releases source/test preparation only, not secret setup,
webhook registration, deployment, dispatch, main integration or public switching.

### Exact route and Nix composition

Use `https://blog.vpsfree.cz/_hooks/github/build`, POST with JSON. The public
Prague proxy adds an **exact** location for that path to the existing blog
virtual host, forwarding the unchanged path/body to the existing metadata-resolved
blog IPv4 port **80** with `Host: blog.vpsfree.cz`. Its ordinary `/` location
continues to WordPress. On the blog backend, an exact location in that same
port-80 nginx vhost proxies to **127.0.0.1:8091**, where the receiver listens.
No new backend ingress firewall opening, inbound SSH, public port, certificate
or English-host dependency is required. Preserve the current exact proxy-only
port-80/header trust and all other WordPress restrictions.

The receiver accepts only that path/Host and POST; query strings/other paths are
not alternate endpoints. Pin the upstream Host rather than trusting an incoming
forwarded host. Keep signature/event/delivery headers and raw body intact through
both nginx hops. Bound body size to **1 MiB** at both proxies and receiver, with
short read timeouts and buffered requests; reject unsupported body encodings and
malformed/ambiguous lengths. No request or signature body is logged. The endpoint
is Czech-host control ingress, not a second bilingual article route: no `.org`
hook or redirect is configured. At a later public `/` cutover to 8080, retain the
exact hook route to the port-80 ingress; any eventual WordPress retirement must
preserve that ingress separately.

Add a default-off webhook module beside restored WordPress/static composition.
Enabling it requires the static preparation user/directories/helper and explicit
operator-supplied workflow/repository IDs and secret file paths; it must not
enable the old periodic timer or activation driver. Keep the inactive 8080 site
and WordPress separate. Source defaults remain off. The proxy's exact route can
be prepared independently, but operator registration waits until both deployed
hops and the enabled receiver have been verified.

N15 composition clarification: assert that an explicitly enabled webhook has
`services.vpsfree-static-blog.enable = true`; do not enable that option implicitly
or split its existing account/storage/helper ownership. Require positive integer
repository/workflow IDs and absolute credential-file **strings** outside
`/nix/store`, avoiding Nix path coercion of secrets. Both options remain off by
default. Explicit static enablement prepares its existing private 8080 listener
and storage; it does not populate `current` or change public WordPress routing.

### Receiver and systemd handoff

Use a small Python-standard-library receiver and a systemd `.path`/oneshot worker;
no framework, message broker, webhook SaaS, database or general job engine.
Receiver runs as a dedicated unprivileged `blog-webhook` user, with no artifact
credential and no write access to release trees/current. The worker runs as the
existing `blog-release` user with the read-only artifact credential. Runtime
secrets use systemd `LoadCredential` from operator-provisioned files outside the
Nix store; neither secret bytes nor tokens belong in Nix, command arguments,
environment dumps, logs, URLs, Git or queue records. The HMAC secret and GitHub
read token are separate credentials. Use a small shared-permission notification
directory only for the handoff, not a root/systemctl privilege for the receiver.

Use a root-owned inbox with a dedicated shared group and mode `02770`; only the
receiver and worker join that group. H15/N15 agree on a stable group-writable
queue-lock file and group-readable/writable atomic hints. Runtime hints are owned
by their creating service user, not required to remain root-owned after rename;
setgid inheritance and explicit file modes preserve access across both users.
Do not replace/unlink the stable lock during ordinary queue operations. These
permissions apply only to the inbox, never the separate credential/release trees.

Stable wiring interface for the two owners: `blog-webhook serve` takes
`--listen 127.0.0.1 --port 8091 --inbox /var/lib/blog-webhook`,
`--secret-file <systemd-credential-path>`, `--repository-id <verified-id>` and
`--workflow-id <verified-id>`; `blog-webhook work` takes the same inbox/verified
IDs, `--state-dir /var/lib/blog` and `--token-file <systemd-credential-path>`.
Repository name, workflow path and HTTP route are fixed by this site-specific
tool. These are operator/Nix arguments, never payload values. Owner3 may expose
these settings under the default-off webhook module without changing this
receiver/worker contract. Runtime directory/credential paths contain no secret
bytes. A precise packaging wrapper may invoke the Python file at its Nix path.

Before parsing JSON or accepting a ping, compute HMAC-SHA256 over the **original
request bytes**, require a well-formed `X-Hub-Signature-256: sha256=…`, and use
constant-time comparison. Reject absent/invalid signatures. Authenticate a
GitHub `ping` and acknowledge it without enqueuing. For `workflow_run`, require
`action=completed`, `workflow_run.status=completed`, `conclusion=success`, exact
configured repository identity (`vpsfreecz/blog` and numeric ID), configured
workflow ID/path `.github/workflows/build.yml`, head branch `main`, and originating
event `push` or `workflow_dispatch` in that repository. Failed, queued, PR/fork,
wrong-branch/repository/workflow and unrelated signed events do not trigger work.
Treat the workflow's human name as descriptive, not identity. Validate scalar
types/bounds, SHA syntax and run IDs; malformed payloads fail closed.

Only a compact validated hint (delivery ID, run ID, SHA/attempt when provided)
is persisted, never the raw payload or its URLs. After a durable atomic enqueue,
return 202 promptly, well inside GitHub's 10-second deadline; a disk/enqueue error
returns failure, not a false acknowledgment. Authenticated ignored events return
204 and authenticated registration ping returns 200. Receiver never performs a
GitHub request, builds content, runs a payload-supplied command or waits for the
worker. All executable paths/config arguments are fixed local configuration.

The handoff is a **coalesced wake-up**, not one deployment per delivery. Use one
atomic pending hint and a claimed/in-progress hint under a short local queue
lock; `.path` starts the fixed oneshot. A notification arriving while the worker
runs remains pending and is processed after it finishes. Do not clear a newer
pending marker when finishing an older run. Preserve unfinished work across a
crash/restart or record it as failed for explicit retry; do not lose it after
202. Use bounded state/status files and the existing release receipts, not an
unbounded delivery registry. `X-GitHub-Delivery` is diagnostic/deduplication
context, not authentication; GitHub redelivery reuses it. A failed delivery/work
item must remain retryable with that same ID. Duplicate/replayed valid hints
cannot cause another activation because this worker has no activation path;
existing SHA/archive identity makes repeated successful staging idempotent.
Coalescing may replace diagnostic hint fields, but never the obligation to check
current protected main. Do not suppress a wake-up based on delivery/run-ID
deduplication or run-ID ordering: an old-commit rerun can have a higher run ID.

### Preparation authority, stale heads and recovery

The webhook is only a wake-up. The worker reuses the existing independently
checked GitHub acquisition and archive validator, configured for the single
repository/workflow. Ignore payload download URLs, branch policy assertions,
archive paths and commands. **Every claimed hint attempts acquisition for current
protected `main` through the API**, including an obsolete hint. Record the hint's
staleness for diagnosis, but never return early or restrict selection to its
SHA/run. Thus if a current-B completion is pending and delayed old-A redelivery
replaces it, the worker still selects B, even if an A rerun has a higher run ID.
For the current SHA, require an eligible successful run and exact named artifact
through the existing API checks, safe extraction and all file/input/receipt
hashes. Missing eligible current content is an actionable failed attempt, not
permission to stage the hinted older content.
Recheck protected-main identity immediately before writing the staged release;
if it changed, leave current serving unchanged and wait for the newer completion
notification. A newer successful rerun of the same SHA may satisfy the wake-up
only through independent current-run/artifact validation.

Factor the existing `prepare` orchestration only as needed for this reuse and
pre-stage recheck. Output remains the existing immutable release directory,
archive and receipt; retain successful current/previous archives. Never write
`current`, execute downloaded content, call `_switch_fixtureable`, or invoke
`pull`/`activate`/`rollback`. Those commands still refuse with
`machine-admission-unavailable`. Enabling this system service is a later approved
system deployment under normal machine ownership. Its subsequent configured
artifact download/preparation is non-activating preparation: the selected
coordination guide explicitly permits building/copying artifacts before an
activation reservation. This narrows D14's broad staging-operation wording; it
does **not** treat a filesystem lock as admission or grant any automatic
pointer/system/proxy activation. Runtime installed admission for actual private
8080 content activation remains the concrete separate blocker.

No periodic reconciliation/polling is selected. GitHub does not automatically
redeliver failed webhooks. Keep a compact journal/status outcome for accepted,
ignored/stale, staged and failed work (safe IDs/hashes only). On transient fetch,
validation or disk failure, stop that attempt without an endless path-trigger
loop or clearing a newer hint; preserve an actionable failure. Operators can
redeliver the same GitHub event or explicitly retry the fixed worker/prepare
command after diagnosis. Service crash restart may resume claimed work with a
bounded restart policy; it must not become a timer that polls GitHub. A missing
or expired artifact reports the exact SHA and requires an authorized workflow
rerun/rebuild, never an older fallback. Do not add a scheduled redelivery scanner.

### Packages and stable boundaries

- **H15, proposed implementer2:** configuration-owned
  `tools/blog-webhook.py`, `tests/blog-webhook.py`, and the minimal shared
  prepare/recheck change in `tools/blog-static-release.py` with affected existing
  release tests. Implement receiver, durable coalesced handoff and fixed worker
  interface against injected local fixtures. No Nix/proxy/docs/shared index edits
  outside the lead's window. The worker/receiver executable and modes are local
  interfaces, never derived from the HTTP request. Report exact mode/credential/
  state-directory arguments to owner3 before wiring, within the above contract.
- **N15, proposed implementer3 after C14 acceptance/capacity:** new
  `int.blog/blog-webhook.nix`, its import/composition, exact backend port-80
  location, exact `prg/proxy/config.nix` hook location, module fixtures and
  existing configuration deployment guide. Own options/services/credentials,
  shared-directory permissions and defaults; no receiver code overlap. Hook
  enable defaults false and requires explicit settings. Keep C14's restored
  WordPress and 36f fix. No machine-runtime or credential provisioning is included.
- **W15, proposed implementer0 after lead release:** amend the held unpublished
  deployment-guide copy to describe webhook-triggered target fetch/preparation,
  manual failure/redelivery, no polling and still-blocked activation. No workflow
  source change is needed. Preserve protected-main upload eligibility, feature
  test explanation and main's wording ownership.

The lead accepts releases and sequences config index/commit windows. H15's source
is sufficient independently of C14 completion; N15 composes only after restored
source is accepted. Any actual receiver/worker interface conflict returns to
architect/lead before divergent implementations. No automatic activation package
is released, and no credential or GitHub setting has been written.

### Tests and later operational rehearsal

Quick tests use local synthetic requests, official HMAC test vector and mocked
GitHub/archive responses. Cover raw Unicode/body alteration, missing/bad
signature, size/type/route/method bounds, ping, every event/repo/workflow/branch
filter, forged payload URLs, duplicate/redelivered hints, concurrent enqueue while
processing, crash/failed-work recovery and queue-write failure before ack. Prove
slow acquisition does not delay the receiver, current-head changes reject stale
work, same artifact stages once/idempotently, invalid content never stages and
`current`/WordPress/public routing remain unchanged. Keep the existing activation
fence tests. No live GitHub, forum, WordPress request or credential is needed.
Focused coalescing regression: queue successful current B, replace pending with
delayed signed old A (including a higher-ID A rerun), and prove B is acquired and
staged while A is never staged. Repeat with B/A arriving during an active claim;
completion of that claim must leave the pending wake-up available to acquire B.

Nix fixtures force generated nginx/service configuration: exact endpoint at both
hops, correct Host/body/header forwarding, loopback-only receiver, body limits,
least-privilege credentials/directories, no timer, and default-off behavior.
With candidate services enabled, WordPress80/DB/PHP/cron/health checks remain
intact. A bounded registered local HTTP integration checks real request/ack and
worker handoff; use the existing verification/service policy, no unregistered
server. Independent final review follows committed intended source/quick checks,
then required longer builds/integration under the monitoring policy.

Later operator gates: separately approved coexistence deployment on blog/proxy,
secret/token provisioning and verified IDs; GitHub repository-hook registration
with JSON, SSL verification and only Workflow runs selected; actual signed ping
and real successful protected-main completion delivery after separately approved
integration. Record GitHub delivery/run IDs, timely HTTP result and the exact
locally staged release/receipt. Test redelivery and failure recovery while
WordPress still serves publicly. Do not claim an artifact is HTTP-visible merely
because preparation succeeded: private8080 activation still requires the supported
admission driver from D14, followed by site evidence and a separately approved
public proxy cutover. Preserve original generation/data and all recovery gates.

Official evidence, read 2026-11-07:
[workflow_run repository event/completion](https://docs.github.com/en/webhooks/webhook-events-and-payloads#workflow_run),
[raw-body HMAC-SHA256 validation](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries),
[quick acknowledgment and same-ID redelivery](https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks),
[no automatic retry](https://docs.github.com/en/webhooks/using-webhooks/handling-failed-webhook-deliveries).
Current source and selected coordination guide establish preparation/activation
boundaries; no actual GitHub hook, network, secret or runtime admission has been
verified. These operational facts do not block the bounded source packages.

## D17 bounded Piwik diagnosis and recovery discovery

Read-only milestone, 2026-11-07 17:01 UTC. Architect owns this design/evidence;
no application fix, machine access, account change or deployment is released.
D15 and the independent T16 analytics guards retain their accepted boundaries.
The questions are whether DNS/proxy explains the reported missing UI assets,
which machine/application version actually serves Piwik, and which installed
native account-discovery/recovery interface exists. Do not infer a password-reset
command or replace account hashes from generic advice.

### Observed routing and HTTP evidence

At configuration head `2aa36562503c8e32f02a308bc70bc9260f5ee120`,
`cluster/cz.vpsfree/containers/prg/proxy/config.nix` declares
`piwik.vpsfree.cz` as an alias of the HTTPS `prasiatko.vpsfree.cz` vhost,
forwarding `/` to `http://37.205.15.53:80`. The internal zone also identifies
`prasiatko.int.vpsfree.cz` with that backend IPv4. The registered configuration
tree contains no Matomo/Piwik service/package declaration or prasiatko machine
selector; it establishes proxy ownership, not the backend installation method.

The configured and observed DNS chains differ but end at the same addresses:

- Internal resolver `172.16.9.90`: Piwik → prasiatko → proxy.
- Public resolver `1.1.1.1` and authoritative `ns1.vpsfree.cz`: Piwik → proxy.
- Both views: proxy IPv4 `37.205.14.61`, IPv6 `2a03:3b40:fe:35::1`.

Unauthenticated HTTPS GETs, without executing scripts or requesting a collector,
admin API or settings action, reached IPv4 `37.205.14.61`:

| Resource | Response | Bytes |
| --- | --- | --- |
| `/` | 200, `text/html; charset=utf-8`, title “Sign in - Matomo” | 145925 |
| `/index.php?module=Proxy&action=getCoreJs&cb=d7b6b71c229b22991cf716f5380f4288` | 200, `application/javascript; charset=UTF-8`, JavaScript/jQuery prefix | 1861108 |
| `/index.php?module=Proxy&action=getCss&cb=b2a4a51a6a1b05f84f33911203508b78` | 200, `text/css;charset=UTF-8` | 454930 |

The root advertised those same asset URLs and the reported cache buster. The
JavaScript body SHA256 was
`1779f30a0ac824c16bf4c928379d0a9fb37b6c4c83fd633069768fc032b15261`.
No cookies, session material, account data or response bodies are retained here.
The reported failure is **not reproduced** by this bounded sample; HTTP success
does not establish rendered UI correctness or all JavaScript chunks' health.
DNS selects a host address, not the query-specific asset handler. The observed
CNAME difference therefore supplies no cause for root-versus-asset failure.
The user subsequently confirmed: “it was blocked by ublock origin. so that is
fixed.” Client blocking is the resolved cause of the reported UI failure;
the earlier backend/network possibilities are no longer open work. `$` being
undefined is consistent with blocked core JavaScript. No DNS, proxy or
application source correction is needed; stop asset/network investigation.

Bounded IPv6 follow-up: forcing the known AAAA `2a03:3b40:fe:35::1` for
the same HTTPS root (5-second connect / 15-second total limits, original TLS
hostname) failed immediately with curl exit 7 and no HTTP response. Local
`ip -6 route get 2a03:3b40:fe:35::1` reports “Network is unreachable”. The
workspace cannot perform this IPv6 comparison; the JavaScript probe was skipped
after that failure. This is a local reachability limit, not evidence that the
public IPv6 endpoint or asset handler is broken. No network change was made.

### Version and account interface limits

No backend version is established by this configuration or public HTML. A local
immutable reference package exists at
`/nix/store/gfm623dy8hgzccbsh6if0vnjabihhlwg-matomo-5.10.0/share`:
`core/Version.php` says 5.10.0 and
`plugins/CoreAdminHome/Commands/VersionInfo.php` implements `core:version`.
Its bundled plugin command sources contain no `user:list` or
`user:reset-password`. **This cached package is not evidence of the installed
backend version or its enabled plugins.** Do not bootstrap it against live data.

[Matomo's console guide](https://developer.matomo.org/guides/piwik-on-the-command-line)
documents `php ./console list` and `php ./console help <command>` from the
application root. The [UserConsole plugin](https://plugins.matomo.org/UserConsole)
adds `user:list` and `user:reset-password`; those names are conditional on that
optional plugin actually being installed/enabled. Inspect its exact version,
command implementation and output fields before recommending an invocation.
Do not install it merely to make an assumed command exist, and never print an
unfiltered user record containing email/token/password fields.

Recovery preference is the existing login-page password-recovery flow when the
account's owner can receive its mail, or a confirmed installed native recovery
interface. The [official emergency recovery FAQ](https://matomo.org/faq/how-to/faq_191/)
describes version-dependent database modification, not a universal core CLI
reset command. No such modification, reset message, plugin installation,
account creation or password change is authorized here. Any later recovery must
name the selected account/method and keep new secrets out of argv/logs/chat;
do not silently replace hashes or disable authentication controls.

### Sufficient next read-only package and gates

Lead may allocate one existing implementer a narrow backend-discovery package
after confirming the actual administrative SSH target/account. Known routing
candidate is `prasiatko.int.vpsfree.cz` / `37.205.15.53`; do not invent a confctl
selector or assume an OS, install root, service user or database prefix. First
inspect only OS/service-to-application-path metadata, the public core version
file/package provenance and native command/plugin source. Never dump private
configuration, process environments, complete service credentials or logs with
request secrets. Only then select a supported reader, scoped to login names and
superuser flags, with explicit output projection; if no suitable installed CLI
exists, return that fact and a proposed bounded read-only method to lead.
Command discovery must not run upgrades, cache clearing or scheduled tasks.

The full current `workspace-host coordination guide` was read from selected
package `/nix/store/zmyllqw6x1cxk8vhwliy7r11ykd19cz9-dev-workspace-0.2.0`.
It defines machine claims as deployment reservations around mutation/activation,
not a requirement for ordinary nonmutating inspection. This read-only package
therefore does not need a deployment claim under that guide; lead release and
exact target/scope remain required by D17. A later backend mutation needs its
real ownership/coordination mapping settled first, since no configured backend
selector has been found. Architect performed no SSH. Lead reports that O17's
default `aither@prasiatko.int.vpsfree.cz` attempt failed before authentication
because the required RSA host key was not trusted. Lead released only a lookup
of existing trust for the exact backend IPv4 and one attempt through an already
trusted IP route; no new host trust or guessed user is allowed. If that remains
unavailable, lead will obtain the actual administrative SSH login and trusted
host fingerprint from the user. No successful backend access or account
discovery is claimed by this record.

UI diagnosis is closed by the user's confirmation. Remaining account-recovery
dependencies are trusted administrative access, installed version/native method
and the selected target account. Retain application/database files and current
configuration; no cache deletion, account mutation, schema migration, service
restart or additional backend claim is needed for the current read-only design.
T16's English analytics ID remains unset pending access. Design capacity is
free; further work waits for those concrete discovery facts or lead allocation.

## D18 sufficient brief: continuous rack-photo background

Source baseline is clean blog `6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344`.
The original `static/wp-content/uploads/2014/11/foto5.jpg` is 3000×2008;
body CSS uses it at natural size with `no-repeat left top`, causing the cutoff
at document y=2008. Its SHA256 is
`c12b042763402d09913308e7fb03933e0ec231f916291cbe2d404391fb1bff64`.
The top has a pale panel and the bottom lower rack bays; plain `repeat-y` creates
an abrupt horizontal break. A session-only plain-repeat contact sheet confirms
this. No external image source or service was used.

### Selected tile and source boundary

Use the prototype
`theme-reference/d18/rack-background-cropped.jpg` beneath this session record:
3000×1240, 907355 bytes, SHA256
`f8e3a64a8be47585ee528889ff3ee185a6c69a2b54e95ebcd294406b08b3ff97`.
It keeps the original horizontal perspective, colors and rack detail upright;
cropping omits the pale top panel and a bounded overlap blends the wrap. Most
rows remain unblended, without resizing or a global blur. Original upload and
all imported/hash-addressed copies stay byte-identical.

Deterministic derivation, performed offline with Python standard library and
cached ImageMagick 7.1.2-23: decode the original to 8-bit RGB and crop
`3000x1624+0+384`. For that crop C (height 1624), append unchanged rows
C[384:1240], then 384 blended rows. For each y=0..383, t=y/383,
a=t²(3−2t), and each output channel is Python
`round((1-a)*C[1240+y] + a*C[y])`. Thus the final row reaches C[383] and
repetition continues with C[384]. Encode JPEG with `-strip -sampling-factor
4:4:4 -quality 92`. This is a one-time asset derivation, not a build step or a
new toolchain dependency. Reuse the inspected prototype bytes; record the source,
transform and derivative hash in the existing provenance notice.

The visual comparison is in `theme-reference/d18/comparison-1920.png` (plain
repeat against the initial full-photo blend). The selected cropped candidate's
three-repeat side exposures are `cropped-joins-1440.png` and
`cropped-joins-1920.png` in that directory. Architect inspected both and the full
tile: the cropped version removes the pale-panel interruption, with a smooth
wrap across two joins and recognizable rack appearance. These are prototype
image evidence, not final browser acceptance.

**B18 owner proposed implementer1, pending lead release:** only add
`assets/images/rack-background.jpg`, adjust the body background in
`assets/css/site.css`, and extend `static/theme/NOTICE.md`. Existing CSS is
already evaluated through Hugo `resources.ExecuteAsTemplate` and fingerprinted.
Resolve the new image with `resources.Get "images/rack-background.jpg" |
fingerprint` in that CSS template, then use its root-relative `.RelPermalink`.
Set `repeat-y left top`, retain navy fallback, and use
`background-size: max(100%, 3000px) auto` so normal desktop widths preserve the
original natural-width composition while displays wider than the source cannot
expose a finite horizontal edge. Do not size against document height or add
fixed-background/parallax behavior. Both languages use identical image bytes.
The existing resource pipeline publishes a local content-hashed image URL and
changes the CSS hash naturally; release payload hashing already includes it.

Retain existing source-photo provenance and its license limits; do not assert a
new media license. No layout, content, importer, manifest, legacy asset, tracker,
search, lockfile or configuration edits are needed. Mobile's opaque full-width
page and its current navigation/pagination/search behavior remain unchanged.
E18 owner3 has the first index/commit/shared-check window; B18 uses its own files
and follows E18's yield for conflicting operations. New acceptance assumes all
125 English articles are approved/published by E18, without altering its
metadata or re-auditing translations.

### Checks, compatibility and recovery

Quick checks: diff/whitespace; source/upload and article-byte preservation from
the package diff/hash evidence; one pinned Hugo fixture build to a unique output
in preview mode, with drafts only as fixtures require. Verify both language roots
contain the same hashed JPEG and their hashed CSS refers to its reachable local
path with `repeat-y`; compare the derived dimensions/hash. No Pagefind rebuild,
tracker execution or full-corpus prose/search regression is warranted by these
three presentation files. Existing T16 CS4/EN10 and preview privacy remain intact.

After the intended commits, quick checks and independent review, later real
browser evidence must inspect 1440 and 1920 widths at y>2008 and across at least
two 1240-pixel joins (for example scroll positions 900, 2100 and 3300 on a long page).
Inspect both exposed side gutters for seams/cutoff and the normal rack detail;
do not use only a top-of-page screenshot. A narrow 320/390 check confirms the
full-width mobile page still hides the background without overflow. Both
languages must load the same local asset; previews must retain disabled tracking.
Use the existing registered preview only through the lead's normal refresh
window; architect launches or changes no service. No full-site/tracker/search
test rerun or new server is part of this package.

This is presentation-only, with no persisted format or public article/media URL
change. Recovery is to restore the prior CSS/background reference and remove
only the new derived resource from a future source revision; keep the original
photo, all historical assets and content untouched. No deployment or default
integration is authorized. The user's subsequent request for a production plan,
including webhook and Discourse setup with deployments performed by the user,
is a later lead allocation; it does not expand B18.

## P18 sufficient production-plan preparation (historical planning boundary)

The later user instruction to finish missing source supersedes this section’s
planning-only scope. A18/H18 and D19 below are the current implementation briefs.

The user will perform deployments and all live webhook/forum/credential changes.
Architect owns only this brief and the current rollout section at the top of
[release-preparation.md](release-preparation.md#p18-production-rollout-plan).
Owner0 and owner2 explicitly yielded that record's write window after the E18DNS
append; preserve their receipts. Main retains final user-facing wording and
allocation/acceptance. No project documentation package is needed for this
individual rollout; the plan links the existing owning-project operations and
discussion contracts. No source implementation or production operation is
released by P18, and preparation is not default-integration approval.

The settled order is: finish combined E18/B18 evidence; expose missing admitted
activation/rollback, legacy-query coverage and enabled/TLS configuration; user
backs up and provisions settings, deploys blog/proxy coexistence with WP public;
separately approved protected-main integration produces an eligible artifact;
verify signed webhook delivery and immutable staging; stop at the activation
fence until a supported implementation exists; validate private serving and
rollback; configure/test one native shared-URL discussion flow; perform the brief
WP delta check and deliberate public proxy switch with WP recovery retained.
Keep the embed off through initial switch if final-source extraction cannot be
verified earlier, then enable through the normal reviewed content-release path.

English DNS already exists according to accepted E18DNS receipts; TLS/vhost
serving remains incomplete. All 125 English translations have user approval, so
new rollout gates concern E18's recorded metadata/final artifact, not another
human translation review. CS4/EN10 and preview privacy stay fixed. Current
configuration2aa is reviewed/published but default-off; its build and mocked HTTP
proof do not certify enabled deployment, actual GitHub delivery or machine
admission. Published blog6dae is only the pre-E18/B18 baseline until their final
combined head/evidence is reconciled in the plan.

The user-facing plan names supported confctl build/deploy, fixed systemd retry
and private HTTP commands with their later prerequisites. It gives no fake
activate/rollback command, manual-pointer bypass, secret value, invented workflow
ID or forum runtime claim. It preserves existing data/generations, webhook80
through cutover, explicit failure/redelivery and retained-artifact recovery.
Quick preparation acceptance is a source-to-command/options/route cross-check,
local document links/whitespace, readable ordered gates and no historical receipt
drift. No tests, builds, probes, SSH or independent source review are triggered
by this planning record. Later source packages and operational checks retain
their normal review/authorization requirements. Final exact blog-head update
waits for E18/B18; no other research is needed for this sufficient draft.

## P18 implementation release: hosting and legacy URLs

The user's subsequent instruction to finish missing deployment source supersedes
P18's planning-only boundary. The user still performs deployments/live setup;
default integration remains separately approved. **H18 is sufficient for lead
allocation to implementer3**, independently of publication internals and forum
inspection. Source baseline is configuration2aa; blog E18/B18 final source is
`7fa57c809d828e945b104f5ab3fa74f76a030a51`. New source must preserve its article
bodies and media. Owner3's E18 blog window is complete; lead sequences subsequent
configuration index windows with publication owner0.

Files: new configuration `cluster/cz.vpsfree/containers/prg/proxy/blog.nix`, its
import and moved blog-only vhost block in `prg/proxy/config.nix`; new
`int.blog/legacy-routes.nix` imported by `int.blog/config.nix`; a finite checked
`data/blog-legacy-routes.json`; focused new proxy/legacy module fixtures. Owner3
must not edit `static-blog.nix`, `blog-webhook.nix` or publication Python/tests
(owner0). Configuration operations-guide paragraphs need one sequential window
after both source packages; no overlapping edits. Blog source stays untouched.

The proxy module exposes `services.vpsfree-blog-proxy.enableEnglish` and
`services.vpsfree-blog-proxy.serveStatic`, both false by default. The existing
Czech HTTPS vhost and exact webhook path remain equivalent with both off.
`enableEnglish=true` creates the `.org` ACME/forceSSL vhost with an explicit 503
prelaunch response while `serveStatic=false`. `serveStatic=true` requires
`enableEnglish=true` and sends both hosts' ordinary article paths to existing
blog metadata IPv4 port8080, with each correct fixed Host. The exact Czech
`/_hooks/github/build` remains on port80 with all H15/N15 raw-body/signature limits
unchanged. Switching `serveStatic` off restores CZ WordPress80 and EN503, without
changing certificates, DNS or WordPress. Never expose private8080/8091 broadly.
No `.org` DNS edit is needed; accepted authorities already point to the proxy.

Legacy routing activates only with the existing static backend. Project the540
`legacy_aliases` records from the exact blog source manifest into the finite
configuration JSON, retaining kind/source/target and source-manifest SHA256 for
provenance. This is a bounded migration table, not a blog repository pin/import
or an online lookup. Validate its exact equality against the current manifest
locally before acceptance; future ordinary new posts do not alter these legacy
identities. Category/author/article path changes must update this migration
contract intentionally, not infer destinations from titles.

Use ordinary nginx maps and return-only redirects in the Czech static vhost.
Exact captured request URI forms are the supported migration inputs:125 post
queries,5 old slugs,144 attachment queries,144 attachment permalinks,6 author
queries,9 category queries and107 reply queries. Map only validated strings to
fixed absolute `https://blog.vpsfree.cz` targets, including recorded comment
fragments; never interpolate caller-provided hosts or redirect targets. Consume
the legacy query rather than appending it to the destination. For literal reserved
identity/feed key spellings (detected case-insensitively), unknown/malformed
legacy identity queries must return404 instead of an unrelated homepage; extra
query combinations outside the finite manifest are explicitly unsupported and
must not guess a destination. Retain direct `/feed/` RSS and the conventional
`/?feed=rss2` alias to it. Do not attach Czech legacy aliases to English article
identity; EN uses its explicit English routes. Preserve ordinary static-query
behavior for non-legacy inputs. Percent-encoded key aliases such as `%70` are
outside the captured identity contract and receive ordinary static handling,
never an inferred article redirect; no query-decoding subsystem is added. Test
that boundary explicitly. No PHP execution or runtime rewrite service.

Quick acceptance: generated nginx with all option combinations; default CZ/hook
equivalence; English503 versus separate-host static routing; rejected invalid
option combination; exact540-entry projection/destination tests, query stripping,
fragments and unknown/ambiguous identity404; same-host feed mapping and no open
redirect. Escape/validate JSON-to-nginx values and demonstrate representative
real nginx responses with a registered local synthetic fixture after final
committed review. Longer native builds cover only affected blog/proxy targets.
No remote requests, DNS changes, certificates or deployments during source work.
Rollback is the mode option change described above; all WP/data/old generations
stay intact. This package supplies operator-selectable routing, not activation.

## P18 implementation release: operator-owned content publication

**A18 is sufficient for lead allocation to implementer0.** The lead accepted the
explicit authority change: the installed workspace claim API is bound to local
session manifests/incarnations and deployment reservations; it is not a target
content-service API. Replace E0's unconditional refusal with an operator-installed
publication policy. Do not build a permanent workspace session, remote claim
bridge or general task platform. Session claims still apply to agent system
deployments; the target application's policy and locks do not claim that authority.

Owner0 files: `tools/blog-static-release.py`, `tools/blog-webhook.py`, their existing
Python tests, `int.blog/static-blog.nix`, `int.blog/blog-webhook.nix` and their
existing module fixtures. A small adjacent policy/maintenance helper is allowed
only if it keeps these fixed operations clearer; no arbitrary executable hooks.
No changes to owner3's proxy/legacy/import files or blog corpus/UI. Sequential
operations-guide update follows source agreement. Preserve existing validated
artifact schema, immutable staging and H15 authentication/coalescing behavior.

### Fixed policy, maintenance and generation contract

Add explicit `services.vpsfree-static-blog.publication.enable=false`; enabling
requires static hosting plus verified positive repository/workflow IDs and the
existing separate runtime read credential, shared consistently with webhook
configuration. Publish a root-owned immutable Nix-generated policy through a
fixed `/etc/blog-release-policy.json` reference. It fixes repository/workflow,
state directory `/var/lib/blog`, enabled mode and schema; it contains no secret.
No CLI argument/environment may replace this policy or change mutation roots.
The installed helper checks that its compiled policy identity matches the active
reference. Missing/disabled/incompatible policies and old-generation helpers
refuse publication. Ordinary `prepare` retains its non-activating contract.
Existing prepare/work state/workflow flags may remain for stage-only compatibility;
activating paths reject any disagreement with the compiled policy/root. A disabled
publication option leaves H15 work stage-only. Status distinguishes this from an
enabled but paused publication policy.

Root owns `/var/lib/blog-control` and a stable group-accessible transaction lock
inside it; the `blog-release` service can lock but cannot replace/unlink that
file or write root control state. Use this SAME lock for all pointer transactions
and root maintenance-state transitions, not a check followed by an unlocked
switch. Existing staging may share it briefly; downloads stay outside it.
Control state defaults to paused when absent and stores schema, maintenance state,
accepted policy digest and exact `/run/current-system` identity. A resumed state
survives reboot only with the same enabled policy/system; changed, disabled or
unknown generation remains paused until the operator verifies and resumes it.

Provide fixed root-only `maintenance-enter`, `maintenance-exit` and read-only
`status` operations. Enter waits for an in-flight pointer transaction under the
lock, then atomically persists pause before returning; a still-running download
may finish staging but cannot switch afterward. Exit verifies selected policy,
current system and reconciled receipts under that lock, records the new resumed
identity, then wakes the fixed worker outside the lock. It never accepts an
arbitrary command or path. The worker rechecks authority immediately before
pointer replacement under the lock.

The pinned NixOS supports `system.preSwitchChecks` and runs it before switch
effects, under the native switch-to-configuration lock. Add a read-only check
requiring paused control state when prior publication state exists, including
when the new candidate disables publication. Operator sequence is maintenance
enter, normal confctl deployment/verification, then explicit maintenance exit.
The first installation starts paused; no automatic resume on failed deployment.
Retain the same mandatory enter step before an old-system rollback whose old
generation lacks this check. Do not use `NIXOS_NO_CHECK` or fabricate admission.
Module-disabled behavior adds no publisher units/listeners/users; the guarded
pre-switch check may still protect already-existing publication state.

### Automatic publish, explicit rollback and crash recovery

After opt-in and resume, webhook work independently acquires current protected
main, validates the exact workflow/run/artifact and stages it, then calls the
supported transaction. `pull` performs that fixed acquire/stage/activate sequence;
`activate` can select only a validated staged release still matching current
protected main. Validate repository ID too; payload hints remain diagnostics.
Recheck API head, active policy/system, maintenance and expected prior receipt
at commit. Use one serialized durable pending transaction and atomic pointer
switch, preserving current/previous receipt history and all existing file/hash
validation. Successful duplicate deliveries are idempotent; an old event cannot
select an older source. Keep periodic pull/timers disabled and unneeded.

Paused work must remain recoverable without a path-trigger loop: coalesce it
into a bounded `deferred.json` not watched by systemd.path; remove only the owned
processing marker, preserving concurrent pending work. Each new delivery still
gets durable202 and may add one deferred wake-up. Root resume coalesces deferred
work back to pending under the queue lock and starts the fixed worker. On boot,
one ordinary service start handles retained work; no polling/retry timer. Failure
records, redelivery and crash processing retain H15's bounded semantics. Agree
queue/control lock order and never hold the queue lock while taking the content
lock or running an external command. Test arrivals during pause/resume/switch.

Expose root-only `rollback` to an explicit validated retained release with an
expected-current receipt identity. It first persists pause under the same lock,
then verifies retained archive/payload/receipt and records a distinct rollback
transaction; it does not require that old SHA to equal current GitHub main.
The prior successful validation/retained identity and the operator's exact target
are its authority. Keep automatic publication paused afterward so a queued event
cannot immediately undo rollback. Preserve pending newer work and all releases.
If no prior release exists, report that limit and use the retained WP public
route for first-launch recovery; never invent an empty release. A later explicit
resume permits current-main publication again.

Reconciliation runs under the stable lock before new mutations. Recognized
pending/current combinations complete or record the interrupted outcome without
losing the previous receipt; unknown pointers, corrupt/missing payloads or
incompatible control schema fail closed and keep pause. Do not automatically
follow arbitrary symlinks or delete retained content. Validate exact file sets,
not only each expected file, when reusing a staged release. Preserve old schema1
stage receipts; the new root control record is additive. Earlier refuse-only
generations cannot publish and require paused recovery on rollback.

Quick acceptance: existing validator tests plus fixed-policy/identity/disabled
checks, root-only controls, same-lock maintenance-versus-switch race, changed
generation refusal, first activation, duplicate/stale/concurrent work, interrupted
transactions at both pointer boundaries, exact retained-release corruption/extra
file rejection, rollback pause and resume, no-loss deferred events without spin.
Module fixtures force enabled/disabled units, permissions, active-policy binding,
pre-switch checks and no timer; ordinary root fixture tests never weaken CLI
production checks. After intended commits/quick checks, independent review precedes
registered local HTTP/systemd-style integration and native affected-system builds.
No live GitHub, secret, system deployment or public content mutation is required
to finish this package. Source compatibility/authority change must be explicit
in its documentation and review packet; it is not removal of validation safety.

## D19 sufficient release: native Discourse setup and explicit opt-in

**Sufficient for lead allocation to implementer2.** Lead accepted native setup,
English framing without English imports, future-article paths and the native
unlisted-until-reply default. No new publisher, plugin, forum upgrade, API service,
Nix default-setting block or database migration is necessary. The existing
production-only boolean and shared Czech source identity implement the native
flow. The user operates the actual forum and later changes the boolean through
the reviewed blog release path; source work performs no live requests or writes.

Owner2 files are blog `docs/discussions.md` and the directly related discussion
paragraph in `docs/authoring.md`. Preserve `hugo.toml`'s disabled default and the
existing partial. No setup helper is needed: the supported admin UI exposes the
required fields. Leave `README.md`, `AGENTS.md`, `docs/deployment.md` and configuration
operations-guide reconciliation to A18 owner0. No article bodies/metadata, media,
search, analytics or style changes. Owner1 must yield its runtime/source-hash window
before blog edits. D19 has the first subsequent blog documentation index/commit
window; A18's other blog documentation follows. Lead reviews prose before commit.
The architect retains this design and the session rollout-plan write window.

### Source authority and supported setup

Owner2 realized only the exact configured Discourse source, tag `v2026.9.1`, from
pinned nixpkgs `718f670e845328e9c2cecdd832835712b2cbd065`. Its fixed-output source
is `/nix/store/30w0v0ml6xzhg6vj1zzzk92b77y8xhfm-source`, NAR
`sha256-j3JjLYNcv3lluoCekyUUKMfkSX/ExeDsa8zrQ+pDrwg=`; `lib/version.rb` confirms
`2026.9.1`. This proves configured source, not the deployed version, live overrides
or an independently resolved upstream commit. Preserve a compact source citation
in the guide for version-sensitive regex/framing/default behavior. The operator
checks the actual installed version before following that part of the procedure.

Use `/admin/customize/embedding`. Its allowed-host form supplies `host`,
`allowed_paths`, `category_id`, `user` and `tags` (UI: Allowed hosts, Path allowlist,
Post to category, Post author, Topic tags). The user selects an actual public
category and verifies its ID and ordinary read/reply permissions, plus an existing
appropriate import username; no invented category ID/account. An invalid/blank
category falls back to uncategorized. Preserve signup/login/moderation and existing
unrelated host entries. Configuration `siteSettings` supplies defaults only and
cannot prove effective mutable settings or create these database records.

The final Czech import rule is the root-slug namespace below, with no query,
nested route or reserved root. Encoded spellings follow the native decode behavior
explained below. All125 current shared source paths
fit the lowercase ASCII root-slug grammar. A finite union of125 paths would
break the intended ordinary author workflow when a new post is pushed. Keep new
article paths in this namespace; a future new nonarticle root must be excluded
before it is introduced. These are source import rules, not caller authentication.
Anyone can request import of a permitted public article.

```text
\A/(?!(?:feed|search|author|authors|category|categories|tag|tags|archive|archives|page|posts|assets|images|pagefind|admin|login|logout|robots|sitemap)/|wp-|[0-9]+/)[a-z0-9]+(?:-[a-z0-9]+)*/\z
```

Set this rule on exact host `blog.vpsfree.cz`. The pinned model evaluates Ruby
Regexp against both encoded and decoded path plus query, without implicit anchors.
Consequently the decode behavior can accept encoded spellings that decode to an
allowed slug; the blog's authoritative `discussion_url` remains exact HTTPS
ASCII without query/port/fragment. Do not claim a regex alone forbids every encoded
alias or enforces HTTPS. The source validation, canonical identity and public
HTTPS route are retained alongside the rule.

For `blog.vpsfree.org`, add a separate allowed-host row with the always-failing
Path allowlist `\A(?!)\z`, selecting the same verified category/author for form
validity. In this pinned source, CSP `frame-ancestors` includes every registered
host independently of its path regex (`lib/content_security_policy/default.rb`),
while `EmbeddableHost.record_for_url` requires a path match before source import.
This permits the English page to frame the shared Czech discussion while rejecting
all English import URLs. Keep `embed_any_origin=false` and
`content_security_policy_frame_ancestors=true`; do not disable CSP or use wildcard
origins. Verify this distinction against the installed version and real browser
before enabling. Retain HTTPS origin referrers; no shared CZ/ORG cookie assumption.

### Extraction, visibility and existing discussions

In the embedding editor's crawler settings choose
`allowed_embed_selectors=.entry-content`, with `blocked_embed_selectors` empty
unless an observed extraction defect needs a precise exclusion. Historical
comments, navigation and discussion controls are outside this wrapper. Retain
`embed_support_markdown=false`, `embed_truncate=true`, `embed_full_app=false` and
`embed_set_canonical_url=false`; use the per-host verified author instead of
changing a global fallback identity. Check extracted prose, code, image and link
content from one final static Czech page. WordPress's old markup does not establish
final-site extraction correctness. Setting names are exact pinned-source facts;
no guessed CLI task or fabricated installed option is part of this package.

Retain `embed_unlisted=false` and **`import_embed_unlisted=true`**: imported topics
start unlisted and become listed after a regular reply in the pinned native flow.
`import_embed_unlisted` is a separate site setting, not one of the custom embedding
editor's saved fields. This choice avoids filling ordinary topic lists with the
archive before discussion begins. It is not private access and does not suppress
notifications. Native import does not use `import_mode` and may enqueue alerts.
Inspect category defaults, existing member subscriptions, mailing-list behavior
and forum-to-IRC/webhook notifications before a controlled pilot. Do not crawl,
preseed or mass-open125 articles; never promise a silent bulk archive import or
change global notification/account policy automatically.

The pinned package includes `discourse-rss-polling` (default disabled), with its
admin UI at `/admin/plugins/rss_polling`. Check the actual enabled setting,
configured feeds and existing imported-topic mappings before selecting native
first-view creation as the sole creator for this blog. RSS uses `TopicEmbed` too;
identical normalized URLs often reuse a mapping, but alternate identities or
unmapped ordinary topics can duplicate, and a second importer can update content
or category semantics. Do not call the existing IRC feed poll a forum importer.
Reconcile known matching topics using their exact source identity, never a fuzzy
title match. If an existing discussion lacks a safe native mapping, leave that
source excluded from the pilot until the operator resolves it; do not delete,
replace or duplicate it and do not invent a mapping SQL command. Unknown live
mapping state is an operator preflight fact, not a reason to build another importer.

### Opt-in sequence, checks and recovery

Prepare the forum while the blog boolean remains false. Initially allow only the
exact selected pilot Czech path, using an anchored escaped rule, and retain the
English reject-all row. After H18 cutover, final-source extraction can be tested
against the public static Czech origin; before then WordPress remains public.
An explicitly user-controlled embed request/first visit can create the pilot topic;
record its URL and verify that both languages and concurrent visits use the same
TopicEmbed identity, anonymous read, authenticated top-level reply, CSP/referrer
and cross-site login behavior. Verify notification effects before expanding the
Czech path rule. Private/local previews remain suppressed and must not contact
production Discourse. Do not present a production iframe smoke test as read-only.

When setup, existing mappings and the pilot are accepted, apply the final Czech
namespace rule and change only `[params.discourse].enabled` to `true` in the blog
source through the ordinary reviewed protected-main artifact/publication path.
Keep all existing production/baseURL/draft/server guards. New posts then need no
per-post forum action. The runtime category/author, observed version/overrides,
pilot topic and notification results are user-provided rollout facts, not values
hardcoded in this source package. Listed-on-first-view behavior can be chosen later
by explicitly changing the two visibility settings after notification review.

Quick package checks: source-to-setting/UI citations; Ruby regex compilation and
all125 authoritative paths, a future valid slug, reserved roots, numeric archive,
query/nested paths and deny-all English cases; demonstrate the pinned encoded-and-
decoded matching semantics rather than an inaccurate blanket encoded rejection.
Check local documentation links, TOML example and unchanged false default/partial;
existing synthetic discussion tests already cover the opt-in guards/shared URL.
Do not add redundant tests for a documentation-only patch or rerun all125 prose.
After main's wording check, commit and request the affected independent documentation
review. No forum integration/build/network test is needed to prove these docs;
later user-run pilot is explicitly separate and cannot be claimed from local checks.

Rollback disables the blog embed through the normal content release, or restores
the retained WordPress public route as H18 defines. Preserve every topic, mapping,
new reply and old static comment; do not roll back the forum database. If an import
must be stopped immediately, the user can narrow the affected source-host path
rule through the supported UI while retaining the host row needed for framing.
Keep direct links to existing discussions and record any new articles/replies
that WordPress cannot consume automatically. No data deletion or schema change.

## P18 final source reconciliation checkpoint

A18/H18 configuration source is committed at
`9ea9fbd9f9a436f82249c08d9e3efc485fe8bff8` (tree
`d160b48cd08b5bce350610120732edd068685540`); combined blog/D19/A18 documentation
is `3fb7d25b1ca39dcddf3dcc8a22b2e47bcf0e49a2` (tree
`743521562f0ef6b1e419011e55888ced23637cea`). Lead accepted source, quick checks and
copy; final joint review is executing. Architect reconciled the current P18
runbook at the top of [release-preparation.md](release-preparation.md) against
these committed interfaces and pinned confctl CLI source. The historical receipt
suffix was preserved byte-for-byte. Main owns final user-facing wording.

The ordered path is stage-only coexistence and real eligible webhook delivery,
then an explicitly enabled/resumed backend publication policy for private serving,
then the user's public proxy mode change, followed by the controlled final-page
Discourse pilot and reviewed embed opt-in. Automatic publication is implemented;
review/build/artifact/runtime outcomes and operator IDs/credentials/settings remain
explicit pending evidence. No production operation, source edit, Git/index change
or verification launch occurred while preparing the runbook. Future exact-head
changes require only affected reconciliation; no new design package is proposed.

## A18 review correction: privilege boundary and durable staging

Lead accepted Important findings A18-R1/R2 on unpublished, undeployed
`9ea9fbd9`. Owner0 folds the narrow correction into its owning A18 commit and
reports old/new lineage for affected review. H18/D19 contracts stay fixed.
Verification preparation is parked; no long/integration launch until the
corrected committed source, quick checks and affected independent review pass.
The current P18 runbook awaits the corrected head and these guarantees.

R1: root only owns immutable-policy checks, root control state and the stable
transaction lock. Content trees, assets, archives, receipts, reconciliation and
service-writable inbox paths must never be processed with root file privileges.
Use fixed internal operations in a small forked child that resets groups to the
configured blog-release identity and irreversibly drops GID/UID before touching
those paths. No saved root identity/capabilities, arbitrary command, caller-chosen
UID or production override. The parent accepts bounded status/identity results,
not child paths or executable instructions.

For rollback, root acquires the same transaction lock and persists pause, then
the dropped child validates/reconciles/switches under that inherited held lock;
do not acquire another flock and deadlock. Root waits before releasing the lock.
For maintenance exit, root pauses first, runs content reconciliation/validation
in the dropped child under the same lock and only writes resumed root control
after success. A child failure leaves pause intact. Root status inspects content
through the dropped child too. Root-invoked prepare/pull/activate must either
perform content work under that identity or refuse with a supported fixed-service
route; preserve user-facing fixed controls and report a necessary compatibility
adjustment before finalizing. Credentials are never returned in child results.

The same boundary covers wake_worker: queue manipulation in
`/var/lib/blog-webhook` runs as blog-release, with its fixed inbox group. Root may
start only the existing fixed systemd worker outside the content lock. Queue and
content locks remain unnested. Ancestor/final symlink swaps must not redirect root
chmod/write through assets, receipts, reconciliation or inbox paths. Test outside
root-owned sentinel bytes/mode unchanged, normal rollback/resume, child failure
and inherited-lock serialization; retain exact privilege-proof limits of pure
fixtures until the separately released isolated runtime check.

R2: make payload durability precede a completed release receipt and every pointer
that can select it. After writing each payload file and final mode, fsync that
regular file; fsync the archive; sync the new directory hierarchy bottom-up. Only
then rename the completed tree into releases, sync the releases directory, and
write/fsync the existing atomic staged receipt and its directory. A failed fsync
or incomplete write aborts eligibility before activation. Apply a barrier when
reusing an older validated staged release whose receipt alone does not establish
this ordering; preserve schema1 and old archives rather than guessing durability.
The current/pending/history receipt transaction retains its existing fsync/atomic
replace ordering after the payload barrier. Add focused ordering and injected
flush-failure tests; no power-cut machine, new persistence format, cleanup or
general storage framework is required.

## A18 R1/R2 corrected-source reconciliation

Corrected configuration `15ad7646c369770fbee584c0e248d05ab9a372bc` / tree
`22160d9a56c16ae270b10ef51b4e4403afe8536b` and blog documentation
`82a1ee3c90990e56cfde0da28ababed8f0444441` / tree
`d23e142cee504f6284ed0bbc4b028be6b8935e8c` amend only their unpublished owning
commits on the same H18/D19 parents. Old9ea/3fb recovery refs and substantive
range evidence remain. Lead accepted source/quick/copy for affected review;
review, corrected native builds, fixed-CLI integration and final artifact/CI
remain pending. Architect reclaimed the receipt window and reconciled the
current P18 runbook, preserving its historical suffix unchanged.

The accepted CLI adjustment requires the actual NSS blog-release account for
prepare/pull/activate and rejects root before token/policy I/O. Operators use the
fixed credential-backed pull service; root maintenance/status/rollback perform
content operations in the irreversible fixed-identity child under the inherited
lock. Queue operations use that identity outside the content lock, then root
starts only the fixed worker. Root control operations and content durability
retain the R1/R2 contracts above. Evidence records21 pure release,19 webhook and
six actual namespace cases; those are not a host-systemd or live delivery claim.
No additional source design or runtime action is released by this reconciliation.

## H18 runtime feed correction: current source identity

Accepted configuration `1e840b8056bbc700ca3e9cd832f0d9301da52652`, tree
`6f6d2020345f731370698be3ed2ff7fe25ac637e`, amends A18 on the same H18 parent.
The two-file fix replaces the failing exact feed file alias with
`try_files /feed/index.xml =404` under each existing language root and retains
RSS type. Public feed/API/authority contracts are unchanged. Lead accepted the
focused generated fixture and narrow inspection; prior review applies to
unchanged scope. Predecessor15ad build and failed real-nginx feed evidence remain
scoped history, while all540 unchanged map checks retain their valid evidence.
The exact82a blog artifact is accepted and unchanged. Refreshed final systems,
feed/remaining modes, fixed-CLI integration and final CI remain pending; architect
reconciled current runbook identities and these limits without source/runtime work.

## A18I bounded fixture diagnosis: private path traversal

The one authorized no-server exec/read smoke reproduced a fixture DAC defect:
inside the same user/mount/network+bwrap setup, private `/nix` was root0:group0
mode0700 while host `/nix` was0755. Store/Python/lib descendants were world555.
Root opened libpython and freshly executed Python; an irreversibly dropped
UID/GID3 child failed fresh exec with EACCES. The smoke's intermediate dropped
stat/read rows were lost when exec raised, so those rows are not claimed.
Original receiver failure was loader exit127 before application import/HTTP.
The working six privilege tests used an already-loaded interpreter and therefore
did not establish fresh nonroot exec. No application failure is established.

Lead accepted the smallest fixture-only repair: owner2 sets process umask022
before creating private scaffolding and before bwrap's automatic ancestors, with
readable NSS/CA and traversable namespace paths. Explicit control0750, lock0660,
inbox02770, secret0400 and private-key0600 remain intact. Host permissions,
application policy/UID guards, source package and compiled-policy bytes do not
change; no LD_LIBRARY_PATH or fork/runpy substitute is needed on this evidence.
Owner2 supplies the small patch and full required-path mode inspection to lead
before a registered full retry. Original attempts/smoke remain immutable.
The first corrected attempt stopped at its mode guard with no application/HTTP
probe: bwrap still auto-created private `/nix` as0700 even with setup umask022;
all other reported public ancestors were755. The smallest supported refinement
is `--perms 0755 --dir /nix` before the readonly store bind, explicitly creating
only that fresh sandbox ancestor. Installed bwrap0.11.2 help confirms these
options. Umask022 remains useful for fixture-owned NSS/credential ancestors but
was not sufficient for bwrap's automatic parent. This corrects the earlier
causal inference without modifying any failed result or host path. Another full
attempt still requires lead release.

Full fixed-CLI/HTTP/publication/rollback evidence remains pending; this diagnosis
authorizes no further run or lifecycle action. Raw evidence stays in the existing
`a18-fixed-cli-rehearsal/exec-smoke-*` paths and its receipt append window.

## A18I accepted functional verification checkpoint

Lead accepted the final28 observations at exact configuration1e840 after the
fixture-only mode and result-label corrections. Actual private NSS/fixed CLI,
compiled source/policy and HTTPS acquisition exercised signed delivery, pause,
deferred/newer pending work, resume, current A/B, duplicate identity, root rollback
remaining paused, generation refusal/resume and old-policy rejection. Final state
is paused. The current P18 plan links exact result/source/NAR proof and marks
only feature publication/CI pending locally. Real host systemd.path/credentials/
switches and live GitHub/forum/deployment remain user-run limits. Prior failed
registrations/results remain immutable evidence; no source/runtime action was
performed by architect during reconciliation.

## P18 final local preparation complete

The final user-run plan in [release-preparation.md](release-preparation.md) now
reconciles accepted configuration `1e840b8056bbc700ca3e9cd832f0d9301da52652`
and blog `82a1ee3c90990e56cfde0da28ababed8f0444441`, their native builds,
artifact, scoped nginx/visual/privacy checks and 28-observation fixed-CLI proof.
Both feature heads are published; blog CI run `42411255497`, attempt 1, passed.
Protected-main packaging/upload were skipped with zero artifacts; configuration
has no applicable feature-push CI. Both remote default branches remain unchanged.
Local preparation is complete, ready for user-operated staged rollout.

The user still supplies verified IDs/credentials and branch policy, integrates
the intended source, obtains a protected-main eligible artifact, builds the
enabled configuration revisions, deploys and verifies TLS/private serving/live
webhook delivery, performs forum setup/pilot and chooses the public cutover.
Host systemd/credential/switch behavior and live services remain user-run checks.
No deployment, default integration or lifecycle action is implied. Historical
receipts, failures, recovery refs, roots and registered fixtures remain retained;
the session stays active. This checkpoint supersedes the preceding local
publication/CI-pending status without changing its historical evidence.

## Proposed implementation packages

These broader delivery packages remain the roadmap; D4's A0/B0/N0 briefs above
define the narrower currently sufficient release boundaries. Paths below are
relative to the selected blog repository unless marked configuration. Lead
accepts each release boundary and controls shared index/commit windows.

| Package and proposed owner | Files/deliverable | Dependencies and acceptance/checks |
| --- | --- | --- |
| A — source inventory and importer, `implementer0` | `tools/import*`, importer fixtures, `docs/migration.md`; generated Czech content, authors/comments, legacy assets and route/feed manifest. Private backup stays outside Git. | Authorized access and source snapshot first. Prove counts/status dispositions, author/comment identity, asset hashes and URL coverage; identical rerun and changed-snapshot reconciliation; no secrets in projection. Inventory settles schema before downstream content work. |
| B — Hugo site and build, `implementer1` | Hugo configuration, `layouts/`, CSS, i18n UI, archetypes, pinned build/Nix definitions, build/check workflow and site README. | Accept A's schema and route contract; fixture-based layout may proceed independently of full export. Preserve Flat design features with mobile/keyboard checks; validate routes, archive rendering, locale metadata, feed GUIDs and reproducible artifact. Own build/config files; expose artifact contract to E's separate deployment workflow. |
| C — discussion integration, `implementer2` | Embed partial, immutable discussion-URL metadata/exception map and `docs/discussions.md`; one-time forum setup plan. | Stable article identities; B exposes one agreed partial slot. Prove first-load auto creation and one shared topic under concurrent CS/EN visits, zero preview/build writes, permissions, extraction, login/moderation and controlled archive notifications. Installed-version test and later setup authorization required. |
| D — author workflow and English migration, `implementer3` | `AGENTS.md`, authoring skill, `docs/authoring.md`, thin author commands; English article files and translation review metadata. | Stable A/B interfaces; technical workflow can precede full archive, English work follows content stabilization. A cannot overwrite English. Human command smoke test and agent dry run; reviewed full coverage/source freshness; human language review remains required. Lead owns final user-facing writing under writing skill. |
| E — hosting, Actions deployment and rollout, `implementer0`, after A | Configuration `int.blog/{config.nix,wordpress.nix,module.nix,packages/default.nix}` as needed; nginx/deploy-user/releases/activation setup, separate deployment workflow and rollout docs. `int.vpsfbot/config.nix` only if needed. | B's exact artifact contract; resolve runner reachability, then constrained push or VPS pull. Verify no root/PR secrets, concurrent/stale-run rejection, safe extraction/atomic switch, cached assets and content rollback receipts. Preserve proxy boundary, `/feed/`, static health checks and bot continuity. No proxy/forum upgrade assumed. |

D4 releases bounded inventory/scaffold/internal-DNS briefs for lead allocation.
Full import and production forum behavior retain their dependency gates. Exact
supported tool versions and repository commands/hooks must be fixed from their
own instructions before code edits. No open preference justifies bypassing data
or account checks. Public English DNS/proxy/TLS is required before bilingual
production launch; the initial same-host proxy assumption applies only to Czech.

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
   translations, discussion identities and review. Build the exact pinned output
   before machine ownership. Keep the original DB/uploads and runnable old system
   generation available; record recovery prerequisites and retention window.
   Prepare one-time hosting and the independent content-release mechanism.
2. **Rehearse:** preview read-only content without production forum writes; test
   static serving, feed continuity, stale-run rejection and both content/system
   rollback using nonproduction fixtures.
   Verify actual Discourse version/category/account behavior separately without
   coupling the migration to forum/PostgreSQL upgrades.
3. **Final change check:** use the captured snapshot; immediately before the
   switch, briefly check for new/changed articles or comments. Refresh the export
   and affected artifact only if changes are found; edited/new Czech articles
   need corresponding reviewed English. No writer freeze, service stop or
   read-only WordPress mode is required. This remains a live capture with the
   documented consistency limits, not an atomic database/filesystem cutoff.
4. **Switch:** under later explicit deployment authorization and machine
   ownership, establish nginx's release pointer and static health checks on the
   existing container, then activate the exact validated content release. Preserve
   public proxy/TLS/routes. Enable reviewed production-only automatic embeds.
   Later approved publication pushes use Actions without full confctl deployment.
5. **Verify:** check production homepage, representative/all manifest routes as
   appropriate, bytes/assets, legacy anchors, `/feed/`, language switching,
   anonymous forum reading and account-policy login/reply. Verify bot polling
   does not reannounce the archive. Record source/config heads, complete input
   graph, system store paths, content SHA/artifact digest/current and previous
   release paths, targets and results in separate linked system/content receipts.
6. **Recover if needed:** restore the recorded original serving configuration and
   intact WordPress state for initial migration failure. For a later content-only
   failure, atomically restore the previous validated content release; the NixOS
   generation does not identify or restore live content. New Discourse replies
   remain authoritative in Discourse; do not delete topics or
   roll back the forum database. Preserve links/mappings to those replies during
   rollback. Reconcile any new static articles with restored WordPress content;
   reverting a system generation does not import them into WordPress.

Compatibility: no planned WordPress or Discourse schema/protocol migration.
The new persistent contracts are public URLs/assets/feed identities, Git content
schema, release receipts and article discussion-URL mappings. Old/new serving can
coexist against retained
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

Access, corpus counts and exact Czech feed identities are reported in A0 above;
complete content exception handling, existing forum topic matches,
category/notification settings, deployed forum version, CI-to-backend reachability
and tested recovery readiness remain unverified. The new remote is empty and
initial publication requires explicit direction. English public DNS/proxy/TLS
needs preparation; no such production setup has been performed. Repository and
English host are settled; category/review ownership remain lead decisions as
needed. These facts constrain dependent releases, not the B0 scaffold.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.


## P19 proxy deployment safety: sufficient read-only brief

User constraint: “proxy is serving other websites and we don't want an outage
there. Configuration switches are acceptable, shutting down nginx is not.”
No nginx stop/restart is permitted; only a validated graceful reload. This
supersedes P18's deployment ownership: the team may prepare deployment to
`cz.vpsfree/containers/int.blog` and `cz.vpsfree/containers/prg/proxy` once access
and staging prerequisites are met. The user handles tokens/GitHub settings and
Discourse UI; no declarative forum source, other target or default merge is
implied. Access is not yet verified. Architect owns this read-only brief only;
lead owns the later preflight/deployment allocation. No source fix is presently
justified.

**Settled evidence.** Configuration `1e840b8056bbc700ca3e9cd832f0d9301da52652`
retains `services.nginx.enableReload=true` in proxy `config.nix:127`; the proxy
source delta moves the Czech blog block to `blog.nix` and adds the scoped hook/
English/mode configuration, preserving other vhost definitions. Pinned nixpkgs
`718f670e845328e9c2cecdd832835712b2cbd065`, nginx module lines 1483–1512 and
1590–1646, generates a separate `nginx-config-reload.service`: config changes
trigger that oneshot, which calls `systemctl reload nginx.service`. The actual
accepted proxy system `a2b5d14vj9rkzlm8sv2j5v0kcf9vplc8` has `ExecReload` running
nginx `-c /etc/nginx/nginx.conf -t`, then `kill -HUP $MAINPID`. The main binary is
`/nix/store/smpkfhyjj22b4zy1f0cprzfhr0nimllr-nginx-1.30.6/bin/nginx`.
New ACME dependencies attach to ACME units, avoiding a main-unit change merely
for a new certificate. The reload oneshot waits for certificate paths; a missing
certificate can postpone reload. ACME renewal itself uses
`try-reload-or-restart`; verify the effective nginx unit remains active and
reload-capable. A failed/withheld reload is not permission to restart.

`enableReload` covers config changes only. The compiled main unit has
`X-StopIfChanged=false`, but no reload-on-unit-change or restart prohibition.
Pinned switch-to-configuration source `main.rs:727–754` defaults
`X-RestartIfChanged=true`; with `X-StopIfChanged=false`, a changed unit is still
**restarted**, rather than stopped in the early phase. Package/ExecStart,
environment/dependency or unit changes can therefore violate the constraint.
The accepted default-off build does not establish the live unit or the future
enabled generation's safety. Preserve its complete input/system proof in the
existing [native receipt](h18-refresh-config-build-proof.json).

**Required later preflight and stop condition.** After access is authorized and
verified, retain the actual current system/profile, nginx unit/drop-ins,
executable, config/includes/cert paths and master PID/start time; compare them
with the exact separately built enabled candidate. Inspect all unrelated vhost
blocks and listener/upstream/TLS changes, plus the activation plan's effects on
shared dependencies. Keep the original generation/config and its inputs rooted.
The supported pinned confctl interface is a separate dry activation:

```sh
nix develop --no-write-lock-file --no-update-lock-file -c confctl deploy --generation '<prepared-generation>' cz.vpsfree/containers/prg/proxy dry-activate
```

This copies/selects the named built closure and invokes its native dry action;
it is a later target operation, not something run for this brief. Inspect its
actual complete output against the live state. `--dry-activate-first` alone
proceeds after a successful dry action and does not reject restart plans;
interactive confirmation is separate (`cli/cluster.rb:873–916`, pinned confctl
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`). Reject a plan that stops/restarts
`nginx.service`, disrupts a shared serving dependency, or is ambiguous. Starting
or restarting the separate reload oneshot is not a main nginx restart. Refresh
preflight if the target/candidate changes; do not automatically confirm a switch.
Native config testing must pass before HUP, with the intended certificates
available; missing paths, failed syntax or a skipped reload stop progress.

Before/after the eventual reload, use the existing proxy health checks for
`vpsfree.cz`, `kb.vpsfree.cz`, and newadmin build-info/healthz, together with
representative unchanged vhosts and the intended blog modes. Record TLS/status
and expected content without secrets. Confirm the nginx master PID/start time
stays unchanged, new workers load the intended config and old workers drain
existing connections; inspect reload/error logs. Configuration comparison alone
cannot promise zero outage.

If the live comparison requires a restart, stop the planned switch. The smallest
candidate is the blog-only configuration delta on the proven running input/unit
baseline, preserving nginx binary/environment; any such source adjustment needs
its own lead allocation and affected checks. Do not suppress restart flags or
bypass switch checks. Recovery must also use the validated reload path; retain
and inspect the old generation, and assess any configured confctl automatic
rollback's return switch before using it. No blind full-generation rollback,
nginx restart or data removal is authorized by this constraint.

This pass read local source, existing compiled units and retained receipts only.
No build/runtime-check execution, server/network/SSH, claim, application edit,
deployment or lifecycle action occurred. The brief is sufficient; live comparison remains
the dependency, and architect capacity is free.


## P20 sufficient implementation brief: backend-owned routing

User approved “yup, let's rework it”: both proxy domains forward to blog.int:80;
cutover/recovery and the hook belong to the backend. Lead accepted this topology
and the ordinary outer-proxy logging/limits change. Sole implementer3 owns the
package and both repository source/index windows. This brief releases source
work; later runbook reconciliation follows results. Predecessors are CONFIG
`1e840b8056bbc700ca3e9cd832f0d9301da52652` and BLOG
`82a1ee3c90990e56cfde0da28ababed8f0444441`; their proofs cover predecessor
behavior only. Architect edits design/assigned rollout records, not application
source. P19's no nginx stop/restart constraint on the shared proxy remains.

Current steering supersedes the first P20 source/quick checkpoint at CONFIG
`cba460554c8008a86cc349ef7308cd539ca75848`: the user rejected a temporary EN
proxy option, and lead accepted unconditional CZ/EN vhosts. Reviewer Important
P20-R1 also found internal nginx directory redirects exposing HTTP and internal
ports. Owner3 alone owns both corrections; the exact old review completes before
an affected review of the new committed contract. Existing source/check receipts
remain historical evidence, not certification of these corrections.

### Fixed interfaces and scope

| Layer | Settled behavior |
| --- | --- |
| Shared proxy | CZ and EN vhosts are unconditional: both have HTTPS/ACME and one ordinary `/` forward to metadata-resolved blog IPv4 port80, with fixed matching Host. Remove `enableEnglish`, proxy `serveStatic` and the special hook location; there is no proxy enable or cutover toggle. Obsolete configuration must fail clearly rather than silently change behavior. Backend EN503 handles the prelaunch state. Unrelated vhosts, inputs and nginx service settings stay unchanged. |
| Backend frontend | New small `blog-routing.nix`, imported unconditionally, owns IPv4 `0.0.0.0:80` and separate fixed CZ/EN server names. New `services.vpsfree-static-blog.serveStatic=false` selects CZ WordPress and EN503; true requires existing `enable=true` and selects the static listener for both. No fallback to WP when a selected static release is missing. Port80 remains reachable only from the exact proxy IPv4 plus local checks. |
| WordPress | Keep the existing generated `blog.vpsfree.cz` vhost/key, PHP location/protection rules, package/settings, WP_HOME/SITEURL, cron, database and identities. Move only its serving listener to `127.0.0.1:8081` and adjust trusted local-hop real-IP handling. Frontend uses a distinct vhost key (`blog-front-cs`), avoiding replacement of generated WP location maps. |
| Static content | Existing CS/EN roots and named vhost keys remain on `127.0.0.1:8080`, available for backend-local verification before cutover. Remove the proxy-to8080 firewall grant; no external8080/8081/8091 listener or firewall opening. Preserve RSS `try_files /feed/index.xml =404`, retained CSS and PHP rejection. CZ-only 540-alias maps remain in this layer; no EN aliases or map changes. |
| Hook | Only frontend CZ exact `= /_hooks/github/build` reaches `127.0.0.1:8091` when webhook enable is true, in both route modes. Disabled exact hook and the reserved `^~ /_hooks/` namespace return404, including EN, so these requests never reach WP or static content. Keep backend1MiB/5s/body/header buffering/pinned Host/log suppression. Receiver, worker and HMAC policy remain unchanged. |
| Defaults/rejection | Unknown Host on frontend80 and internal listeners returns444 through explicit default vhosts; never accidentally make WP the public default. EN ordinary traffic returns503 before static cutover. Static PHP requests return404; WP mode retains its intentional PHP behavior/protections. All listeners are explicit IPv4, avoiding accidental IPv6 exposure or port80 collision. |

Use ordinary fixed `proxy_pass` locations without URI replacement: preserve raw
request path/query/body for legacy matching and HMAC. Outer per-language forward
sets fixed Host, `X-Real-IP $remote_addr` and `X-Forwarded-Proto $scheme` (HTTPS
vhost); no untrusted X-Forwarded-For chain becomes client authority. Frontend
trusts X-Real-IP only from the metadata-resolved proxy /32, with recursion off.
Frontend→WP/static fixes the corresponding Host and forwards its resolved
`$remote_addr` as X-Real-IP; set X-Forwarded-Proto to the fixed canonical `https`
on this private hop, not the local HTTP `$scheme`. WP trusts this header only
from loopback, with recursion off, preserving effective client IP and HTTPS
administration. Its old direct proxy trust may be removed now that it cannot
receive external connections. No URL/header chooses an upstream. Review the
actual generated header inheritance so a second generic header include cannot
overwrite these values. The hook uses its existing fixed-Host/raw-body policy.

Set `absolute_redirect off;` on the retained WordPress and both static
vhosts. Nginx-generated directory redirects must use relative Location values,
so the public HTTPS hostname/port survives the loopback hops. Keep explicit
legacy301 targets fixed to `https://blog.vpsfree.cz`; this correction does not
rewrite WordPress application redirects or the captured alias map. Include
focused generated-module and real-nginx slashless-directory coverage for WP
and both static languages. The proxy's one-deployment P19 gate is unchanged.

Outer policy compatibility is explicit: the accepted proxy currently uses
10MiB global body limit, 60s generic proxy timeouts and ordinary `combined`
access logging. Removing its special hook restores those defaults for this
path; backend enforcement remains1MiB/5s. Ordinary combined logging records
request/URI/status/referrer/user-agent, not HMAC headers or request bodies.
Keep credentials/signatures out of URLs and do not add payload/header debug
logging. No new outer hook rule, filter or dedicated logging framework is
required; backend endpoint logging remains suppressed. This settled change is
approved by lead, not an accidental weakening of an unstated contract.

### Ownership and protected boundaries

Owner3 files in configuration: `cluster/cz.vpsfree/containers/prg/proxy/blog.nix`;
backend `config.nix`, new `blog-routing.nix`, `wordpress.nix`, `static-blog.nix`,
`blog-webhook.nix`, `module.nix`; existing `tests/blog-{proxy,static,webhook,legacy}-module.nix`
and `docs/operations/blog-static.md`. Change `legacy-routes.nix` only if strictly
necessary for composition; keep its projection/data and matching semantics
identical. Reuse current fixtures rather than add a new harness. Update the
backend health commands to check public frontend CZ and retained loopback WP
separately; current HTTP-health success must not imply WP recovery was checked.
Proxy's existing unrelated-site health commands stay intact. The existing
legacy-module fixture still expects the obsolete feed `alias`; reconcile it to
the already accepted `try_files` contract when updating that affected fixture.

Owner3 also owns the narrow BLOG `docs/deployment.md` correction for port roles,
backend cutover/recovery and ordinary proxy forwarding. Read BLOG instructions
before that edit; no article/template/assets/IDs/translation/feed/search changes.
No forum source; setup stays in Discourse UI. Configuration publication Python,
compiled-policy/schema/CLI/UID+lock/durability/queue contracts, Actions workflow,
artifact format and inputs remain unchanged. No Hugo builds locally or on the
backend: use the existing accepted artifact for routing fixtures and actual
eligible Actions artifacts for later deployment. No new IDs/secrets are invented.

### Operation, compatibility and recovery

Three independent choices stay clear: static.enable installs storage/internal
serving, publication.enable authorizes content selection only after explicit
resume, and backend serveStatic exposes that selected content on frontend80.
`prepare` still cannot provide a private preview until a valid current pointer
is selected through the installed publication policy. Keep publication controls,
root maintenance, retained-release rollback and all state unchanged. Every
backend generation switch, including route cutover/return, follows the existing
maintenance-enter/check/status and deliberate post-verification resume contract.
No manual symlink/policy bypass or new switching daemon/CLI.

Normal initial sequence: verify the actual old proxy forwards CZ to80; prepare
and deploy backend coexistence with serveStatic=false, checking retained WP and
EN503; then the one shared-proxy change adds EN TLS and ordinary80 forwarding
under P19 preflight. Successful Actions publication can then be checked
locally at8080 with fixed language Host while WP remains public. Once ready,
only the backend serveStatic option changes. Returning it tofalse restores CZ
WP/EN503 without another proxy change. Content rollback independently retains
its pause semantics. Keep WordPress/PHP/MariaDB/data/keys/owners/backups, old
systems, releases and forum replies. No retirement/cleanup belongs here.

This intentionally replaces the unpublished/undeployed predecessor routing
contract and its external8080 verification path. If live inspection instead
finds a proxy pointing at8080 or an unexpected deployed predecessor, stop and
sequence that concrete transition before making8080 loopback-only; do not assume
the normal sequence applies. Pin/source drift and restart-required proxy plans
remain blockers, not reasons to bypass checks. Preserve old/new review ranges
and recovery refs; owner3 inventories obsolete unmerged layout history and lead
chooses consolidation/publication under existing rules.

### Minimum acceptance and checks

Quick batch: normal hooks and the affected existing Nix module fixtures, using
real composition to force nginx/unit generation. Cover default/coexistence,
static selection, unconditional CZ/EN proxy vhosts, webhook off/on and invalid
static-without-enable. Assert fixed host headers/proto/client-IP trust, no public WP collision,
no external internal-port grant/IPv6 listener, exact hook only, generated WP
protections/data/UID/service preservation, unchanged publication policy/helper
bytes and removal of both proxy toggles/special hook. Assert `absolute_redirect off`
on WordPress and both static vhosts, with fixed HTTPS legacy redirects intact. Prove unrelated proxy vhost
configuration unchanged. Projection bytes stay identical; reuse its accepted
540-map evidence where source identity allows. No broad publication test rerun
is needed if its implementation is unchanged; re-run only affected module gates.

After committed-source/affected independent review, build the two exact system
targets and record new source/input/unit/config identities. The native proxy proof
must show EN ACME configured by default; that does not prove a certificate was
issued or that live TLS works. One bounded
registered real-nginx routing batch may reuse the accepted static artifact:
exercise the ordinary outer hop and frontend in both modes, fixed CS/EN Hosts,
WP recovery path, direct/frontend RSS200+MIME, slashless directories through both
public-host routes with no HTTP/internal-port Location leakage, representative query/fragment
aliases and malformed/nonlegacy cases, unknown Hosts/PHP, hook off/on/EN reject,
raw HMAC body/header preservation and backend body limit. Use unchanged accepted
receiver code/synthetic secrets; no live GitHub/forum requests or new full
publication harness. Prove preview checks do not require Hugo or public routing.
Retain predecessor results only for unchanged scope; no claim of deployed
WP/PHP or production TLS from synthetic upstreams. Later live preflight covers
actual WP/client-IP/HTTPS behavior, unit/binary/config comparison, dry-activation
plan, unrelated-vhost health and master/worker continuity under P19. Stop on any
planned shared-proxy nginx restart or uncertain effect.

No unresolved product choice blocks this source package. Access, live baseline,
operator credentials/eligible main artifact and proxy certificate verification
block only subsequent rollout. This design pass performed local reads and this
addendum only, without evaluation/build/server/network/SSH/claim/source mutation.


### P20 native output realization: accepted investigation boundary

The original exact011151f native command returned0, but retained evidence shows
its final9037 blog and5w86 proxy outputs absent locally. Pinned confctl7bee58
requests real builds, then discards their returned JSON and separately evaluates
output paths before creating generation/GC-root symlinks without target-validity
checks. Its exit status and links alone do not certify local realization.
The actual disappearance cause remains unknown; the proof-reader JSON schema
correction is separate. Preserve the raw103.836s result as incomplete evidence.

Lead released owner3 for one realization of only the two already-bound final
derivations, capturing completed JSON and fresh explicit roots, without confctl
reevaluation or source/pin changes. Acceptance requires exact expected outputs,
local validity/NAR and native-root/compiled-content binding. A later pass is
recovery evidence, not proof of the original cause. Recovery/runtime results
remain pending; the one-proxy deployment and P19 no-restart gate are unchanged.
No broader tooling investigation or implementation is part of this package.


### P20 final preparation checkpoint

Lead accepted CONFIG `011151f978eae435e1357ca00611726dbf501943` / tree
`bb194867edee21017186a0af0471905da03869ca` and BLOG
`7b0f3286ee11737e894f022bde0fce742a8a572d` / tree
`e9bce05317dd1f55234779bb1608d4c171a300f7`: final affected review has no
remaining findings; both feature heads are published with remote defaults/HEAD
unchanged. Exact BLOG push CI [42470233945](https://github.com/vpsfreecz/blog/actions/runs/42470233945),
attempt 1, passed checks/release checks/Nix build; trusted-main packaging/upload
were skipped and artifact count is zero. CONFIG has no applicable push CI.
See [final publication proof](p20-final-publication-proof.json).

The earlier output-gap paragraph's recovery/runtime pending state is historical.
The [final native proof](p20-config-build-proof.json) accepts the separately
rooted 21.209-second realization of only the two exact drvs; the original
103.836-second missing-output run remains incomplete and its cause unknown.
[Blog proof](p20-blog-artifact-proof.json) binds all 2397 served files unchanged;
[73 routing observations](p20-routing-runtime/result.json) passed for the
actual adapted nginx/HMAC path. These establish their recorded local scope,
not production TLS/PHP/systemd or a live generation switch. Unchanged A18I
publication evidence is reused only for its identical implementation/policy.

The [current staged rollout plan](release-preparation.md) now uses unconditional
ordinary forwarding for both proxy domains, one proxy deployment under P19's
live comparison/separate dry-activation/graceful-reload gate, and backend-only
cutover/recovery. Internal WP/static ports stay loopback-only; publication
maintenance, UID/lock/durability and recovery contracts are unchanged. The user
handles tokens/GitHub/Discourse UI; team target access, live facts and eligible
protected-main artifact remain later rollout dependencies. Chat proceeds one
small step at a time. The complete prior receipt suffix is preserved, including
failure/recovery lineage and route-coverage limits. No source change, new check,
deployment, default integration or lifecycle action accompanies this checkpoint;
all refs, roots, fixtures and the session remain open. Record ownership returns
to lead for the handoff.


### P21 proposal: synchronous authenticated HTTPS upload

**Status: accepted for implementation.** The user said "ok, well, proceed with
implementation" after the direct-upload proposal and 512 MiB choice. The accepted
release checkpoint below supersedes proposal-only wording in this section. P20 CONFIG
`011151f978eae435e1357ca00611726dbf501943` and BLOG
`7b0f3286ee11737e894f022bde0fce742a8a572d` remain unchanged. This addresses the
user's proposed workflow push through the existing proxy and requirement for a
deployment secret. It replaces target-side GitHub credentials/API acquisition
and webhook notification with one authenticated package upload. No App, OIDC,
new framework, local Hugo build or background deployment queue is proposed.

**Recommended boundary and authority change.** Make the protected-main workflow
with the deployment secret the release authority. It runs existing checks/build,
packages the site, retains its Actions artifact, then uploads as the last
required step. A successful HTTP response means the exact validated release and
its transaction receipt are durable and selected at response time. The workflow
then reports delivery failure directly; it cannot report the overall run already
completed successfully before this final step succeeds.

This deliberately removes independent target verification of repository ID,
protected/current main, workflow event/path/run success and GitHub artifact
identity/digest. A signature proves possession of the deployment key; SHA,
run identity, input graph and source NAR remain authenticated sender assertions,
not independent GitHub evidence. The validator still proves package consistency,
path safety, complete file hashes and fixed repository/workflow names. Anyone
holding the key can authorize a conforming site, including arbitrary site
JavaScript. Protect main/workflow changes and use an Actions environment restricted
to main with the secret available only to the deploy job; PR/other-branch jobs
must never receive it. Protecting main is still an operator setting, not a
property the new target can observe.

The genuine decision for the user is whether this conventional trusted-workflow
boundary is acceptable in place of target-side current-main/API checks. If the
target must independently prove GitHub's current main at commit time, a shared
secret and package metadata alone cannot meet that requirement. Do not describe
this proposal as retaining that guarantee or add another authority system without
new scope. An optional sender-side current-main check narrows stale delivery but
cannot make it atomic with a target switch.

**Small fixed transport.** Propose exact Czech `POST /_deploy/blog`, forwarded
through the same proxy → backend80 → loopback receiver path in either backend
route mode. English, disabled deployment, other reserved deployment paths and
the retired webhook path must not reach WordPress. Send one standard ZIP with
exactly the existing `payload.tar.gz` and `receipt.json`, reusing the current
strict ZIP member checks and schema-1 package. No multipart parser is needed.
Use bounded Content-Length/application-zip handling, reject duplicate identity
headers and unsupported transfer encodings, and cap both compressed/expanded
sizes and file count before staging. Keep metadata outside served roots.

Recommend HMAC-SHA256 with a high-entropy shared key, over a fixed versioned
string binding method, exact path, workflow run number and SHA-256 of the exact
ZIP body. The digest and run number are explicit headers; the target can verify
the header signature before accepting application work, then verify the streamed
body against that signed digest. The existing receipt inside that body binds
source SHA, run ID and attempt. Use constant-time comparison. This keeps the
key off the existing private HTTP proxy-to-backend hop; the public connection
still requires verified HTTPS, no redirects and no insecure certificate option.
A bearer secret over HTTPS is simpler but would traverse that private HTTP hop;
HMAC adds only standard-library signing, not a new authority service.

Store the target key in an external root-owned 0600 file, supplied by
LoadCredential to a fixed `blog-release` upload service. Store the same key in
the main-restricted Actions environment. No key in Nix/store, URL, command-line
arguments, logs or artifacts; no debug HTTP headers/body. Rotate by replacing
both copies in a coordinated pause, without a permanent dual-key mechanism.
The fixed nonroot receiver now has publication authority and content access,
unlike the old notification-only user. It never receives root/systemctl rights,
controls maintenance, chooses arbitrary paths or executes uploaded content.

**Ordering, retry and maintenance contract.** Use authenticated
`GITHUB_RUN_NUMBER` plus receipt run ID/attempt as workflow-local ordering data,
not numeric ordering of run IDs or commit SHAs. Official [variables documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/variables)
states that run number increments per workflow and does not change on rerun;
attempt increments on rerun. Restrict automatic upload to protected-main push
runs and retries of those runs; retain manual artifact builds without silently
authorizing arbitrary manual historical deployments. Fix repository/workflow
identity in policy. Recreating the workflow/order namespace requires explicit
operator reinitialization, not a guessed reset.

Under the existing stable transaction lock, retain the greatest successfully
committed `(run_number, run_attempt)` and its run-ID/source/digest binding in
transaction state. Reject lower order and conflicting reuse; for the same run
number bind run ID/source across attempts. An identical retry succeeds only
when that exact release remains selected. A previously deployed but now
superseded or rolled-back request must not silently select itself again. A
higher accepted order must be durable even if content selection is unchanged.
Carry ordering state through pending/current receipt reconciliation and root
rollback without reducing it; test interruption before/after pointer replacement.
This rejects regressions behind an already committed newer upload. It cannot
know about a newer main commit or workflow that has not successfully arrived.
A stolen key can forge ordering claims; this is not a defense against its holder.

Use one deployment concurrency group and avoid canceling an in-flight upload;
keep concurrency as load control. GitHub's [concurrency documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)
orders waiting jobs by when they enter the group, not workflow dispatch time.
Serialization therefore does not replace the target ordering check. Bound active
upload/validation work; reject busy requests rather than accumulating a queue.

Keep immutable policy/implementation digest, starting-system identity, fixed UID,
root-owned pause state and the same stable lock. Reject paused, disabled or stale
policy/system uploads; recheck immediately before pointer mutation. No automatic
resume, deferred upload or replay after maintenance-exit. Root rollback persists
pause and leaves ordering intact; a queued/retried request cannot undo it. System
switches still require maintenance. Network/body work stays outside the content
lock; validation/staging and commit preserve fsync/retained CSS/media invariants.
Reusing the current API-authorized switch by supplying receipt values as fake
API facts is expressly excluded: add the named upload authority path around the
same transaction primitives and document its changed proof.

Return 2xx JSON with source/release/receipt identity only after durable commit,
or for a verified identical currently selected release; never 202 merely for
acceptance. Reject authentication, invalid/oversized packages and stale/conflict
requests with explicit non-2xx status; paused/busy conditions are retryable.
The client checks both HTTP status and returned identity and uses bounded retries
of the exact same bytes. A lost connection/timeout can occur after commit, so
Actions failure means delivery was not confirmed, not necessarily that serving
is unchanged. Exact retry resolves that ambiguity; root status remains the
recovery path. Once mutation starts, finish/reconcile it even if the client
disconnects; do not promise rollback merely because its HTTP connection closed.

**Size and finite synchronous budget.** Filesystem-only inspection of retained
P20 output `vn73ycqnxdfj9a6flyz87jrbvk2lzrdj-vpsfree-blog-0` finds 2398 regular
files including metadata, totaling 114,380,315 bytes. JPEG/PNG files account for
102,221,554 bytes. These are uncompressed file sizes. Neither the
[artifact receipt](p20-blog-artifact-proof.json) nor owner3's retained evidence
contains an actual full-site transport ZIP/payload size or validation/staging
latency. A18's 6.521575-second, 28-observation rehearsal used tiny synthetic
archives; it is not a full-site timing. No package was generated for this study.

Do not assume the current ordinary outer 10 MiB limit permits this upload.
Plan one exact Czech upload-location allowance, still forwarding to backend80;
backend settings alone cannot overcome an outer 413. The selected 512 MiB body
cap applies only to the exact Czech endpoint at both hops, leaving room for more
images as the site grows. It matches the existing 512 MiB expanded validation
ceiling; unrelated request limits remain unchanged. Measure the actual transport
package and full-size processing cost. Replace the old backend 1 MiB/5-second webhook
budget. Keep the validator's bounded 512 MiB expanded limit and 25,000-file
limit. Current validation holds expanded files in memory and staging/commit
revalidates and fsyncs them; bound concurrent work and check target memory/disk.

The ordinary 60-second proxy read timeout is an idle-read limit, not a total
end-to-end deadline; a synchronous handler producing no response during
validation can hit it. Propose a finite upload-specific budget, initially
180-second proxy read/send limits and a 300-second client total limit, to be
settled by a full-size controlled measurement before deployment. This is not a
latency claim. If that budget cannot be met reliably, report the limit rather
than silently returning early or adding an asynchronous platform. Preserve
ordinary unrelated-vhost limits, fixed Host, secret-safe logging and P19's
live-unit/config/binary comparison, separate dry activation and graceful reload
only. This is an upload-capacity exception, not a return of proxy cutover modes;
it should join the single eventual proxy deployment before any live rollout.

**Candidate implementation package, only after choice.** Prefer one implementer
(available owner3) for both repos and tests/docs: BLOG `.github/workflows/build.yml`,
a small `bin/upload-release` client and existing release checks/docs; CONFIG
`tools/blog-static-release.py`, replace the webhook receiver/module/tests with
the fixed upload endpoint, `int.blog/{static-blog,blog-routing,module}.nix`, the
proxy blog location, affected fixtures and `docs/operations/blog-static.md`.
Retain Actions artifacts and schema-1 package validation. Remove obsolete GitHub
API acquisition/token options, webhook queue/path/worker and manual pull flow;
do not operate two permanent delivery mechanisms. Source is unmerged/undeployed,
so consolidate its obsolete unconsumed approach after review under normal rules.
Preserve old refs, retained artifacts/receipts and documented recovery.

Keep existing root maintenance/status/content rollback and backend serveStatic
cutover. New authority policy/state needs an explicit version/compatibility
boundary: retained schema-1 content releases remain readable for rollback under
P21. Backend `serveStatic=false` restores the retained WordPress route. Old system
generations remain retained, but their activation/control-gate compatibility must
be independently verified before any switch; no P21-to-P20 system switch is
established by pausing. Old helpers must not write the new ordering state or
silently revive the API-pull path.
No deletion or conversion of WordPress, forum data or retained releases is needed.
Operator work becomes the target runtime key, matching protected-main Actions
secret/environment, access/TLS checks and explicit resume; no target PAT/App or
repository webhook setup. Proxy/backend cutover remains separate from upload.

Quick acceptance covers signed/tampered/missing headers/body, size/path/file
validation, exact/conflicting retries, out-of-order attempts, pause/rollback and
crash-order durability, generation refusal, workflow secret/event scoping and
module removal/routing assertions. After committed affected review, one bounded
registered full-size upload through generated proxy/backend config should measure
body size, memory/duration, durable response, timeout/retry and root maintenance
behavior; it reuses the accepted site artifact, not a new Hugo build. Required
native builds bind the changed systems/source; live TLS/systemd/secret tests
remain staged rollout work. This proposal ran only local source/evidence reads,
filesystem size inspection and the two cited official documentation reads. It
appends this design only; release-preparation/source/index/refs/settings and all
services remain unchanged and open.


### P21 sufficient implementation release

The user accepted the changed authority: the main-restricted, secret-bearing
Actions workflow authorizes publication; the target does not independently
verify GitHub current main, run success or artifact API facts. No product choice
remains. Lead allocated **implementer3 as sole complete cross-repo owner** of the
files/tests/docs listed above, including removal of the API/webhook/pull path.
Architect0 retains routine contract clarification; consequential deviations go
to lead. CONFIG011151f/BLOG7b0 are the retained predecessor, not proof of P21.

The fixed interface is Czech `POST /_deploy/blog` through proxy/backend80 to the
nonroot loopback service, in either backend route mode. Upload one bounded ZIP
containing exactly schema-1 `payload.tar.gz` and `receipt.json`; authenticate the
versioned method/path/run-number/body-digest message with the shared-key HMAC
and verify the actual body digest. Use fixed header names/encoding documented
identically by client/server; owner3 may settle those routine details together.
Only this exact endpoint gets 512 MiB at both hops. Expanded validation remains
512 MiB/25,000 files. Keep unrelated limits, secret isolation, bounded concurrent
work, provisional 180-second proxy and 300-second client budgets, and P19's
shared-proxy no-stop/restart gate. These budgets require later measurement.

Keep one publication transaction/state path. Reuse validator, immutable staging,
retained CSS/media, fsync barriers, fixed UID and root maintenance/generation
controls. Persist authenticated committed ordering and its identity binding in
the existing transaction/reconciliation contract, carry it through rollback and
never lower it when changing the selected content. Identical currently selected
requests are idempotent; older/conflicting requests reject. Durable 2xx confirms
the selected release/receipt; a lost reply remains ambiguous until exact retry
or operator status. Paused/stale-system requests cannot publish, resume or enqueue
future work. Concurrency is load control, not proof of current-main freshness.

Retain readable schema-1 packages and old content releases for rollback under
P21, plus backend `serveStatic=false` WordPress route recovery. Advisory D2
clarifies the system boundary: P20 `control_state` (lines 577-585) and
`check_maintenance` (697-707) require schema 1; P21 pause writes schema 2. Pausing
therefore does not establish an ordinary P21-to-P20 system switch. Keep old
systems retained, but independently verify activation/control-gate compatibility
before any switch. No verified P20 switch, converter, dual writer, gate bypass
or extra legacy support is claimed. Old helpers are not supported writers of
new state and must not resume old pull or erase the committed ordering floor.
Remove obsolete receiver/queue/path/worker/pull/token options rather than retain
a second delivery mechanism; preserve prior refs, receipts, roots and services.
Keep root maintenance/status/rollback and backend-only route cutover intact.

Acceptance is the focused quick coverage listed above, normal hooks and a clean
complete cross-repo history/review packet. After final committed affected review,
lead releases required native builds and one bounded full-size generated-route
upload measurement covering durable response/retry/ordering/maintenance. Reuse
the accepted site artifact; no local Hugo build or broad new test platform.
Operator secret/environment setup, TLS/access and live checks remain later work.
This checkpoint releases implementation only: no deployment, default integration,
cleanup or lifecycle action. Source/index work stays with owner3; the rollout
record waits for actual accepted source/results.


### P21 final delivery checkpoint

Lead accepted final CONFIG `10e66efdffc586bdec8af82b3d0e17df59bee2d7` / tree
`02c209571aaa791c29e08fc54d265b1139d2c628` and BLOG
`e1bb2d2b43aeb7361ac72c4c565919f38daabb65` / tree
`1f5798439460b8d2a879976dbbbcf1de1a3e43fd`: review/corrections, native builds,
artifact identity, 45 scoped runtime observations and both feature publications
are complete. [CI 42502157095](https://github.com/vpsfreecz/blog/actions/runs/42502157095)
attempt 1 passed; main-only package/upload/deploy were skipped, with zero
artifacts. [Final publication proof](p21-final-publication-proof.json) binds
unchanged default refs/HEAD, all six recovery refs and the collector/receiver UID
clarification; [verification proof](p21-final-verification-proof.json) remains
immutable. P20's output gap/recovery is historical; P21 needed no realization
recovery. Full-size measurements retain their private-namespace/CA limits.

The [current rollout plan](release-preparation.md) now uses one root-owned
external `/private/blog/deployment-key` and matching `BLOG_DEPLOY_KEY` in the
main-restricted `blog-production` environment, with no target PAT/App/repository
webhook. Provisioning of either copy is unconfirmed. Source defaults remain off;
enabled policy requires explicit resume while WordPress stays public. One proxy transition
carries unconditional EN TLS and the exact Czech 512 MiB/180-second exception
under P19's no-stop/restart gate; backend-only cutover/recovery remains separate.
P21 content rollback and WordPress routing are supported; old system activation
still requires independent control-schema compatibility proof. Historical receipt
bytes, failed evidence, roots, refs and services remain intact/open. Both features
are unmerged awaiting named integration approval; readiness grants no deployment.
Record writes return to lead for a short interactive handoff. No source,
verification launch, network, deployment or lifecycle action accompanied this
reconciliation.


### P22 sufficient rollout brief: team backend, one user proxy activation

**Authorization and ownership.** The user confirms blog access and states:
"I'll just deploy the proxy.prg when you'll tell me -- I expect to do just one
deploy. Otherwise you will handle the transition on your own." Owner3 is the
sole complete CONFIG implementation/execution owner; lead sequences review,
release and user handoff. Architect owns this brief only. User owns GitHub
settings/secrets and Discourse UI; no default integration is approved. Later
steering, "it will reload/restart nginx, that is fine and expected", permits
normal nginx reload **or restart** during the config switch. This supersedes
P19's no-restart/master-continuity gate for P22; keep P19 as historical evidence.
Preserve unrelated sites and verify actual effects, without claiming zero outage
or authorizing prolonged downtime/extra hosts.

**Current evidence and source boundary.** Accepted predecessors are CONFIG
10e66efd/BLOGe1bb2d2b and the P21 proofs. Owner3 reports strict-knownhosts,
BatchMode access to declared `root@172.16.8.4`, hostname `blog.int.vpsfree.cz`.
The key parent `/private/blog` is root:root 0700; deployment-key is a regular,
nonsymlink root:root 0600 file of 128 bytes. These are metadata-only observations:
no key content/hash/signature or matching Actions-secret proof. Remaining exact
system/input, nginx/WP/PHP/database/accounts/data, active publication/control and
recovery facts are owner3's already allocated read-only baseline; do not invent
them from local builds.

The minimal enabled-source package changes only existing
`cluster/cz.vpsfree/containers/int.blog/config.nix`: static `enable=true`,
`publication.enable=true`, `publication.secretFile="/private/blog/deployment-key"`
and `serveStatic=false`. Keep P21 code/protocol, fixed paths/UID, schema-2
control/order/fsync/rollback, existing inputs and all WordPress data intact.
Once baseline shows this composition needs no unplanned migration or conflicting
writer/listener, lead can release that source independently of forum setup,
proxy certificates or actual Actions secret matching. Missing live settings
block activation/resume/delivery as applicable, not this settled source contract.
No pin refresh, frontend/Hugo/forum changes or setup framework is part of it;
concrete baseline incompatibility goes to lead for the smallest necessary delta.

**Build and deployment boundary.** Commit the intended settings, pass affected
quick module/format checks and independent committed review before longer native
verification. Reuse unchanged implementation proofs only within scope. Build the
exact backend and final intended proxy configuration, retain complete source/input
graphs, system/rollback outputs, validity and prior generations. Operator settings
produce new outputs, not the already accepted default-off systems. Acquire and
verify the exact blog machine claim only near the prepared copy/activation batch,
without holding a repository claim for development or deployment. Preserve exact
selector `cz.vpsfree/containers/int.blog`; no extra machine is inferred.

Before switching, reconcile actual old publication/control state and writers,
retain database/uploads/fonts/secret-key/account recovery and a compatible
recovery route. If prior publication exists, require maintenance through its
compatible installed interface; an unexpected schema/writer or missing recovery
proof stops activation, never justifies conversion/bypass. New P21 policy starts
paused. Deploy coexistence, verify frontend80 Czech WordPress, loopback8081
WordPress/PHP/database/cron, English503, closed internal ports, data/accounts and
credential/service health. Preserve working public Czech content; stop and
recover a failed or uncertain switch before continuing.

**One user proxy activation.** Prepare all required proxy changes together:
unconditional Czech/English TLS/ACME, ordinary fixed-Host backend80 forwarding,
and exact Czech upload exception 512 MiB/180 seconds. Backend route modes remain
independent of proxy configuration. No proxy SSH credential/access is assumed.
The user may first need bounded read-only baseline commands and a separate exact
generation dry action; those are preflight, not additional activations. Compare
actual live/candidate unit, binary, drop-ins, config/includes, certificates and
unrelated vhosts; inspect syntax, the real activation/dry plan and recovery effects.
Normal reload/restart is acceptable; record which happened. Block unexplained
unrelated changes, failed syntax/certificate prerequisites or unsafe recovery,
not an expected nginx restart. Verify both language TLS/status and representative
existing-site health afterward. Lead tells the user to perform the one activation
only when the complete candidate and relevant live facts are prepared; do not
promise a second proxy deployment as a routine fix.

**Content and cutover.** Keep backend `serveStatic=false` through policy/resume,
real protected-main signed delivery and private loopback checks. GitHub environment
must restrict `blog-production` to protected main with matching `BLOG_DEPLOY_KEY`;
no PAT/App/webhook. Real main delivery requires separately explicit BLOG/main
integration approval; deployment authority does not supply it. Keep embed off
while user forum setup/pilot remains incomplete; it need not block source or
private content preparation. Confirm exact response/receipt/order, both language
roots/feeds/search/media and current WP delta/backups. Root maintenance surrounds
each later backend generation change. Only after those checks, prepare the
backend-only `serveStatic=true` change with its affected commit/check/review/build
and exact-generation proof, switch, verify public routes plus retained WordPress,
and deliberately resume. No further proxy mode change is required.

Supported recovery is P21 retained-content rollback preserving committed order
and pause, or a compatible backend `serveStatic=false` generation restoring
WordPress/English503. Old systems remain retained, but P20 schema-1 maintenance
cannot be presumed compatible with P21 schema-2 control; independently establish
activation/control compatibility before any old-software switch. Preserve new
articles/forum replies and every old ref/root/fixture. No cleanup or lifecycle
action follows readiness, deployment or handoff.

**Acceptance and claim retention.** Record exact deployed source/system/input
identities, authoritative claim mapping/status, actual switch results, private
and public health, selected content/receipt/order and recovery evidence in the
existing rollout records. After effects are verified, retain deployed machine
ownership until complete deployed lineage (including dependencies) is integrated
into separately approved remote defaults. Then inspect the exact held claim,
reconcile unfinished effects, verify lineage, release and confirm release
promptly under the installed guide; no separate UI acceptance is needed. Missing
merge approval/evidence keeps ownership held and does not authorize integration.
The installed guide read for this brief is dev-workspace
`/nix/store/b83kfhq5zrz88y3isspd8vga0ga36a9m-dev-workspace-0.2.0`.
This pass records design and owner-supplied facts only; architect ran no SSH,
network, evaluation, build, source/index/ref mutation or deployment.


#### P22 accepted baseline and source release

Lead accepted owner3's read-only baseline: selected system and profile agree on
`y50f85…`, generation 16; booted `4nidz…` is older and must remain distinguished.
Reported nixpkgs is `718f670`. Nginx, PHP, MariaDB, WordPress initialization and
cron are healthy; only ports 22/80 listen. No publication policy/control/state,
current pointer/static root, publication users or units exist. Thus no old-writer
or publication migration conflict blocks the four-setting coexistence change.
The protected key metadata above is confirmed. Reported capacity is 4 GiB RAM
with about 3.7 GiB available and 53 GiB disk available; actual upload resource
checks remain part of rollout verification.

Lead released owner3's source package `28af1e1f`: only the four settings in
`int.blog/config.nix` above CONFIG10e66, followed by scoped quick checks, normal
commit and mandatory review before long build. Source preparation does not wait
for backups, forum/UI, proxy facts or the bounded remaining `/etc/confctl`
source/input provenance read. No activation or machine claim is released by
this baseline acceptance.

Before live activation, owner3 must complete and verify protected recovery
material under the later execution release: a successful consistent native
MariaDB backup of the actual WordPress database, site/uploads/fonts and required
secret files with ownership/modes, account IDs, exact selected/profile/booted
system identities and available source/input/generation recovery. Keep private
backup paths outside served roots and Git; record metadata/results only. Verify
backup command success, readable complete database/site archives and integrity,
and a concrete compatible restore procedure/destination using the existing
backup tools. A list of intended paths or old migration capture is insufficient.
Account for writes between database and site capture and refresh the final
article/comment delta before cutover. Missing backup/provenance or an unsafe
restore path blocks activation, not the already released source change. No new
migration, state converter, test platform or proxy no-restart restriction is
introduced; normal nginx reload/restart remains allowed.

#### P22 native dry-switch coverage: bounded source conclusion

The captured [native dry log](p22-dry-plan-capture-native.log), SHA256
`f08ea2a8c451cd3b4eb14126a0405042fe3fe6a15a8aef17865f9ef2cc501217`,
line 80 proves pinned confctl `7bee58a5` invokes candidate
`/nix/store/cqjh12xcn92cvnl7vd4gcv0j341fxd42-nixos-system-blog-26.05.20261026.718f670/bin/switch-to-configuration dry-activate`.
This is already the native NixOS dry-switch interface. It includes active-unit
comparison, rather than only running the candidate's `dry-activate` script.
Pinned nixpkgs source `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`,
`pkgs/by-name/sw/switch-to-configuration-ng/src/main.rs:1136–1320,1941–1955`,
compares currently active/activating NixOS-managed units. The dry branch at
2049–2191 adds dry activation-script requests, prints its action maps, and exits
before applying service jobs. It does not expand the future systemd dependency
transaction; exit zero is not proof that every eventual service action appeared.

This explains the missing nginx/upload lines. Owner3 found nginx's main unit and
binary unchanged, the config-reload oneshot inactive/dead, and upload newly
enabled. Both candidate `multi-user.target.wants` links are present. Active
targets enter the start set but are hidden from ordinary output (1252–1277).
The full switch reloads systemd's unit definitions, refreshes
`sysinit-reactivation.target` (2433–2454), then starts active targets
(2540–2577), allowing systemd to pull new/inactive dependencies. The nginx
oneshot's `ExecStart` requests `systemctl reload nginx.service`; upload starts
through its target dependency. `STC_DISPLAY_ALL_UNITS=1` reveals target names,
not a complete expanded job plan, so repeating the dry run adds no needed proof.

Owner3's retained [trigger comparison](p22-plan-trigger-comparison.txt) and
[tmpfiles delta](p22-plan-tmpfiles.diff) close the concrete bookkeeping questions.
The six added directory/file rules create publication state and the stable
root:`blog-release` 0660 lock; no WordPress/database rule changes. The pinned
tmpfiles module (253–281) reruns `systemd-tmpfiles --create --remove` through
resetup on `sysinit-reactivation.target`, triggered by the tmpfiles directory.
D-Bus main unit/binary and policy/service tree bytes are unchanged; only generated
system-path references change, with `X-ReloadIfChanged=true`. Its reported reload
is a derived config trigger, not an identified daemon/policy migration.

The sufficient preflight is the captured native dry output plus the retained
actual old/candidate unit, dependency, trigger and activation comparison; no
alternative dry command, simulator, old-system build or pin refresh is needed.
Actual switch/effect verification remains owner3's work under lead release and
the held machine claim. Normal nginx reload/restart is permitted by the current
user instruction. This source-only conclusion adds no outage, backup or service
freeze gate and makes no deployment-success claim. Architect changed only this
design note; all prior records, failures, roots and services remain retained.

#### P22 feature publication without merging: sufficient continuation brief

User explicitly requires feature deployment without merging and reports the one
proxy deployment complete. This supersedes the earlier requirement for main
integration before initial content delivery; automatic Actions publication stays
protected-main-only. Lead accepted a one-time operator use of the existing
key-holder authority. Owner3 owns packaging/copy, the ordinary HTTPS upload and
private verification under a bounded lead release; architect owns this note only.
No application, workflow, pin or default-branch change is needed for this phase.

**Exact package and authority.** Use unchanged BLOG `bin/package-release` from a
clean `e1bb2d2b43aeb7361ac72c4c565919f38daabb65` checkout against the already built
`/nix/store/bi18fs5lxknk4j22sahyd8gp2qspwawr-vpsfree-blog-0`.
[Accepted artifact proof](p21-blog-artifact-proof.json) binds source NAR
`sha256-1MyrtJtrF6w9APGC+1Ar+frTj9r+ibmNB1Ewqry+nfc=`, inputs and all 2397 served
file hashes. Package once with `--sha` that exact SHA, `--run-id 42502157095`
and `--run-attempt 1`; select the existing site with `--site` and a fresh private
output directory with `--output`. This is packaging, not a new Hugo/Nix build.
Retain archive/receipt digests and copied client/package identity against that
source. [Actual feature CI](p21-blog-ci-run.json) succeeded for run number **9**,
ID **42502157095**, attempt **1**. Record this as an **operator-local package
associated with that feature run**: CI packaging/deployment were skipped and
[GitHub artifact count](p21-blog-ci-artifacts.json) was zero. Neither receipt
labels nor upload success establish a protected-main or Actions-produced artifact.

**Existing interfaces only.** CONFIG `tools/blog-static-release.py:669–687`
exposes maintenance, status and rollback, with no public stage/activate command.
Use unchanged `bin/upload-release --release <private-package-directory>` through
its fixed verified HTTPS origin `blog.vpsfree.cz`, path `/_deploy/blog`, without
redirects, insecure TLS or a loopback replacement. One fixed privileged process
on blog.int reads the guarded root-owned `/private/blog/deployment-key` only
into memory and invokes the actual client main. Its process-local inputs are
`GITHUB_RUN_NUMBER=9`, `GITHUB_RUN_ID=42502157095`, `GITHUB_RUN_ATTEMPT=1`,
`GITHUB_SHA=e1bb2d2b43aeb7361ac72c4c565919f38daabb65` and `BLOG_DEPLOY_KEY`.
The client's UTF-8 key interface must preserve the file's exact bytes: no strip,
newline removal or replacement decoding. Refuse an incompatible key locally;
never print its contents/hash, signature, environment, request headers or body,
or put the key in shell arguments. A small fixed launcher may read the file and
invoke the unchanged main in the same process; no persistent service, custom
signer, callback publication or new protocol is introduced. Authentication sends
HMAC over HTTPS/private HTTP; the raw key remains on the target. Existing fixed
receiver UID, policy/system binding, package validation, 512 MiB limits, finite
300-second/three-attempt client and durable transaction remain authoritative.

**Finite execution and stop conditions.** Lead accepted owner3's
[post-proxy result](p22-public-after-proxy-result.json): verified CZ/EN TLS,
CZ WordPress 200, EN 503, unsigned Czech upload 401, English upload and retired
hook 404; backend cqjh/CONFIG1649 remains paused/empty and MySQL root 0700.
This proves observed routing, not an independently identified proxy revision.
Before mutation confirm those relevant source/policy/state/package facts still
hold; stop on drift, a conflicting committed floor, credential-policy mismatch
or route/TLS failure. Keep `serveStatic=false`. Root runs selected
`blog-static-release maintenance-exit`, then the ordinary signed upload, then
`maintenance-enter` after success or failure and checks `status`. Client success
must match exact release/source/body/receipt/run identity; a lost reply is
uncertain delivery, not proof of no commit. Inspect paused status and reconcile
through the existing maintenance interface; if needed, resume and retry only
the identical preserved package, never invent another run/attempt or edit state.

The first committed ordering floor is `(9,1)` with the actual run/source/body
binding. Later newly created runs of the same workflow naturally have larger
run numbers; stale reruns and conflicting equal-order packages remain refused.
Rollback retains this floor. Do not reset it or use synthetic run 101. The
unchanged target trusts the authenticated operator assertion and package
consistency; it adds no GitHub API/current-main claim.

While paused, verify the selected receipt/floor and exact served hashes, both
fixed Hosts on private 8080, roots/feeds/search/media and existing finite alias/
rejection contracts. WordPress remains public on frontend80 and retained8081;
private ports remain closed externally. Collect actual upload time/resources
and safe identity evidence without expanding the verification platform. This
phase ends paused with public WordPress intact. Public-only post/comment/media
delta metadata and proportionate backup freshness govern later cutover, not
independent private preparation; no private export or writer freeze is implied.
Owner3's [live aggregate comparison](p22-live-content-metadata.json) reports
125 published posts, 107 approved public comments and 144 attachments matching
the accepted inventory, with no relevant modification/upload timestamp since the
protected 18:19:55 UTC backup. Backup metadata remains unchanged. This is useful
delta evidence, not proof against deletion, preserved-timestamp edits or exact
live body/media differences; it creates no private-content export authority.

**Later cutover and recovery.** After private acceptance and WP delta resolution,
owner3 changes only backend `serveStatic=true`, then follows quick checks, normal
commit, mandatory review, exact native generation/input proof and switch under
held claim4cd. Maintenance brackets the switch; verify actual effects and the
guarded MySQL root0700 postcondition established in P22. No second proxy deploy
is planned. Retain WordPress/data/accounts/backups and compatible coexistence
generation recovery; with no earlier static release, WordPress is recovery.
Content rollback preserves order and pause, and old-software compatibility is
still a separate requirement. Keep Discourse embed default off and existing
Piwik/privacy gates unchanged; user owns forum/UI/settings. Known route inventory
limits remain daily 0/124 and pagination 35/41. No merge is authorized; claim
retention and all existing refs/roots/receipts/services remain unchanged.

#### P22 visible Actions feature delivery: sufficient temporary release brief

User now explicitly chooses “Keep main untouched; use an explicit feature
deployment push” and permits temporarily changing the workflow's main-only
restriction. This authorizes one exact-feature Actions delivery, not a merge,
weaker main protection or arbitrary-branch secret access. Current BLOG
`5d9cd0be0184c67e8d7c1cfbdbbe41da6acd5e48` is the published documentation
descendant; its CI42524935636 passed with packaging/deployment skipped and zero
artifacts. Selected operator content remains e1bb/bi18/floor `(9,1)` with its
distinct provenance. This brief adds no implementation or execution by architect.

**Owner/files and fixed contract.** Owner1 owns BLOG
`.github/workflows/build.yml`, narrowly affected `bin/check-release` guard checks,
necessary deployment-doc clarification, commits/review evidence, deliberate
feature publication and exact CI/artifact evidence. Owner3 owns backend
pause/resume/status, private content verification and recovery under claim4cd.
Lead releases each phase and owns environment-setting coordination. Configuration
cutover99c7 has its separate review; native build/switch remain held until the
Actions upload is accepted. There is no new uploader or cross-owner source edit.

Extend only the existing package, artifact-upload and deploy eligibility:
preserve each existing protected-main condition **OR** admit repository
`vpsfreecz/blog`, event **push**, and exact ref
`refs/heads/2026-11-06-multilingual-blog-migration`, all three together. Parenthesize
the alternatives explicitly. Main dispatch retains its existing packaging-only
behavior; feature dispatch, PRs, other branches/tags and other repositories
cannot deploy or package through the exception. Keep the same workflow path,
action pins, main protection check, `blog-production` environment, environment
secret, job dependency/concurrency, package/client and HTTPS protocol. No manual
signature, secret transfer, target policy change or synthetic run identity.

**Required setting and preparation.** The accepted
[environment proof](p22-github-settings-proof.json) has selected branch policies
with only `main`, and `BLOG_DEPLOY_KEY` present. Before the deliberate push, add
only branch `2026-11-06-multilingual-blog-migration` to that same environment's
deployment branch list, retaining `main`. This temporarily lets workflows on the
exact feature branch receive the existing deployment secret. Do not move/read
the secret, allow wildcards/all branches, change default branch or relax main
protection. Lead handles this concrete user-owned setting after source preparation,
unless an explicitly authorized existing tool performs precisely that change.
Keep publication paused during preparation, checks, committed independent review
and environment setup. Do not publish the exception early as an ordinary CI push:
the approved push is the deployment trigger.

Quick checks cover YAML validity and the actual guard matrix: protected-main
push succeeds; existing protected-main dispatch packages but does not deploy;
the exact repository/feature push succeeds; unprotected main, feature dispatch,
PRs, foreign repositories, other branches and tags fail the relevant exception.
Verify all three gates agree and action pins/client/protocol remain unchanged.
Run the scoped release checks before independent committed review; no duplicate
site build or broader suite is needed before that boundary. The ensuing exact
Actions run supplies checks, native site build, packaging and actual delivery.

**Finite live sequence and acceptance.** After review, environment readiness and
lead release, owner3 confirms the expected selected system/policy, paused
receipt/floor and public WordPress, then resumes immediately before owner1's
deliberate ordinary feature push. A fresh verification utility follows only the
new exact head/run. Keep current/default refs distinct. Use the same workflow's
real new run number **greater than 9**, actual run ID/attempt and actual build
head; never override these to label the old operator package as Actions output.
Bind the genuine retained Actions artifact to its receipt, source/full inputs,
archive/transport identity and client-confirmed durable target response. The
workflow change produces a new source identity even if served file bytes match.

Owner3 pauses after terminal success, failure or uncertain delivery, then records
selected receipt/order and resolves any lost reply using the existing protocol.
Failure is not proof that no commit occurred. A permitted retry must reuse the
exact retained package and current same-run identity rules; no floor reset or
invented attempt. Independently verify the newly selected package's complete
served set/hashes and affected private fixed-host routes, while public Czech
WordPress/English503 and retained recovery remain intact. Record real Actions
job/artifact/response evidence separately from prior operator61038. Only accepted
delivery/private verification releases the later backend cutover phase; no
second proxy deployment or default integration follows from this success.

**Restoration and consumed history.** After successful demonstration, owner1
makes a normal follow-up commit restoring the original main-only workflow gates
and matching tests/docs on the same feature branch. Keep the exact consumed
upload commit as an ancestor, with its immutable run/artifact/source receipts
and rooted content; do not amend, squash away or relabel that deployed identity.
This two-commit exception/restoration records an actually consumed transition,
not an unused final compatibility path; no extra branch machinery is needed.
Apply the required scoped check/review boundary to restoration, then publish it;
its feature CI must skip package/deploy again. Lead coordinates removal of only
the environment's temporary feature allowance, leaving `main` and the secret.
If the demonstration is abandoned, pause/reconcile effects and restore both
restrictions before closing this temporary scope. No further feature pushes are
delivery-authorized while restoration is pending. Retain all original recovery
evidence, operator and Actions releases, refs/services and the held machine claim.

#### P24 release retention: sufficient implementation and verification brief

User requests pruning old release content and clarifies that deployment may
wait for pruning's lock but must not fail merely because of that contention.
This supersedes keep-all-release-payload wording only for the bounded operation
below. It does not authorize pruning Nix roots, Git refs, WordPress, backups,
private operator/Actions package copies or session files/services. Owner3 retains
the complete CONFIG implementation/runtime package and canonical index; source
work starts after lead release of this sufficient brief. Architect changes only
this design. Current accepted Actions content is a66, floor `(11,1)`, paused on
cqjh; owner3 knows two complete releases, so the five-release policy should remove
none of those. No live inventory or deletion was performed for this brief.

**Small interface and scheduling.** Extend the existing fixed-root helper with
`blog-static-release prune [--dry-run]`, and add
`services.vpsfree-static-blog.retention.keepReleases`, positive integer default
**5**, to the existing module/compiled policy without changing persisted schema2.
Install one ordinary daily systemd oneshot/timer when storage and publication
are enabled. Use selected packaged helper, fixed `blog-release` UID/group,
existing filesystem hardening and no credentials/network access; no dependency
that makes upload/activation success depend on prune success. Root invocation
delegates all content inspection/deletion through existing `content_as_release`;
it must not delete as root. No post-upload cleanup hook, queue, daemon or new
lock. Timer/manual actual pruning skips while paused/disabled or either lock is
busy; normal resumed operation must schedule it. Dry-run may explain the keep/
candidate set while paused, but changes no content, control or trash. Report
kept/candidate/retired/deleted keys, skip reason and cleanup failures without
payloads or secrets; do not claim logical byte counts equal freed disk blocks.

**What is retained.** Existing `stage` creates `releases/KEY/`,
`releases/KEY.tar.gz` and `receipts/KEY.json`; completed selections add UUID-named
transaction receipts, while current/pending/order have separate fixed names.
Rank distinct available complete releases by their latest valid **successful
selection** transaction timestamp, with a deterministic tie-break, and keep five.
Use completed activated/rollback/reconciled-activated records, not staging
receipt mtimes or reconciled-before-switch attempts. Retained older schema1
content remains supported; no receipt rewrite/backfill is needed. Always add
the current release, its immediate `previous_release`/`old_pointer` recovery
reference, and the upload-floor release to the keep set. Validate these references;
there is no `current.previous` symlink. Do not recursively pin every historical
previous link, which would defeat retention. An active/pending/uncertain pointer
transaction means **no retirement**; preserve it for existing reconciliation.

Only successfully selected, unprotected old payload directories and matching
archives are eligible. Stage-only releases, `.incoming-*`, unknown/orphan content
and small receipts are left untouched and reported where relevant. Preserve
every per-release/UUID audit receipt, `current.json`, `upload-order.json`, pending
and control state, both locks and all `assets/`. The shared fingerprinted CSS
fallback serves cached pages and remains cumulative. Legacy media remains in
the selected/kept trees; unchanged activation checks still require immutable
paths/bytes and a media superset. Historical receipts do not promise that pruned
payloads remain rollback targets: rollback is supported only for complete retained
releases and must reject a pruned target before pointer change. The retained
floor still rejects stale uploads after rollback or pruning. This bounds completed
payload copies, not total disk use: audit/CSS, uncommitted staging and external
recovery copies remain outside this policy.

**Wait, retire, then delete.** Actual `Publication.lock` and `serialized` use
blocking `flock(LOCK_EX)` today. Preserve blocking acquisition for upload,
maintenance and rollback: no contention timeout, EBUSY, HTTP503 or new retry
outcome from prune lock ownership. Prune alone tries the existing publication
lock and then staging lock nonblocking; if either is busy, release and skip.
This order does not invert an existing nested acquisition: upload releases the
publication lock before staging, then reacquires it for commit. Do not take the
receiver's busy flag. Under both locks do only bounded metadata/path inspection,
selection and same-filesystem renames; do not hash/decompress entire archives,
walk all payload files or recursively delete there. Recheck the selected policy/
system and pause/transaction/current/floor state immediately before retirement.

Retire eligible directory/archive entries into a private, non-served
`releases/.trash` namespace using strict release keys and a simple per-pass
directory. Rename under the locks, fsync changed parents, then release both
locks **before** recursive disk deletion. The directory is a conventional
retirement area, not a new journal/schema/tombstone subsystem. Existing audit
receipts preserve identity. Interrupted tree/archive moves leave only an
unprotected retired payload or matching leftover; the next locked pass can
finish safe retirement, and the next cleanup can retry trash. Never restore a
retired tree automatically, treat it as serving content, or remove a newly
protected active-path counterpart. Missing protected content, malformed/conflicting
references or ambiguous source/destination identity fail closed before new
retirement. After an I/O error stop new moves, retain evidence/remaining entries
and report prune failure; successful publication remains successful.

Use real fixed state/releases/receipts directories and directory-relative,
no-follow operations. Validate exact `RELEASE_KEY` basenames and regular archive/
receipt types; reject symlink roots, traversal, devices and unexpected filesystem
boundaries. Bulk deletion must use fd-safe traversal rooted in the opened trash
directory, never shell globbing or unchecked recursive paths. Symlinks cannot
lead deletion outside that namespace; an anomaly stays retained with an error.
Handle already-removed trash entries idempotently if two prune invocations overlap
after releasing locks; no third lock is needed. Upload may wait briefly for
metadata retirement, but slow/failing deletion occurs outside its critical path.
Existing finite 180/300-second network budgets remain: this removes deliberate
prune contention failures, not a mathematical guarantee against stalled storage
or unrelated network failure.

**Files, compatibility and deployment.** Owner3 owns
`tools/blog-static-release.py`, `cluster/cz.vpsfree/containers/int.blog/static-blog.nix`,
affected `tests/blog-static-release.py`, `tests/blog-upload.py`/module fixtures
and `docs/operations/blog-static.md`. Keep transport/client/Actions and proxy
unchanged; other source files only if this implementation concretely requires
them, through lead. Update documentation's keep-all and rollback promises.
Combine reviewed retention with the already reviewed99c7 backend cutover settings
before the first public switch, avoiding another activation. The helper change
changes the immutable policy/source package, so obtain a fresh exact native
generation/inputs/output proof after quick checks and independent review; retain
99c7/4m7 as predecessor proof, not certification of retention. Pause surrounds
switch and selected-policy resume as before. Timed pruning skips while paused;
after acceptance/resume verify timer scheduling and a safe explicit dry-run/no-op.
With two known releases, do not fabricate production victims to demonstrate
deletion. Keep the P22 MySQL literal-root0700 postcheck, WP recovery and claim
retention; no second proxy deployment or default merge is authorized here.

**Meaningful checks.** Quick fixtures exercise more than five completed releases,
deterministic newest-five selection, current older than five, immediate previous
and floor pins, duplicate transactions, stage-only/incoming preservation, pending
upload/rollback and malformed protected-state refusal. Verify archive and tree
accounting together, retained receipts/control/order/CSS/media byte preservation,
rollback to kept content and refusal for pruned content, plus stale retry/order
behavior. Exercise real filesystem locks in separate processes: a genuine upload
waits for a held prune metadata lock then commits without a lock-caused failure/
retry; prune skips a busy publication/staging lock; slow or failing trash deletion
outside those locks does not block publication. Test interruption between renames
and during deletion, idempotent recovery, symlink/traversal/outside sentinel
protection and fixed nonroot deletion. Module checks cover count/default/disabled
mode, daily timer, UID/hardening, fixed helper and unchanged WP/proxy configuration.

After committed independent review, run the affected native build and one bounded
existing-fixture integration with actual fixed-UID CLI/receiver, synthetic old
releases and contention/deletion failure injection. Reuse existing full-size
upload/route proof where unchanged; no second complete delivery platform or broad
site/CI rerun is justified. Acceptance requires demonstrated disk-payload removal,
protected-state/rollback/order survival and deploy-waits-not-fails behavior,
plus honest limits above. Lead accepts implementation and later live release;
this brief performs neither deletion nor service/source mutation.

#### P25 correction: preserve historical re-staging through commit

Lead accepted this refinement of the released retention package. A previously
successful release can be re-staged under a valid higher upload order; its old
transaction receipts would otherwise let prune retire it between staging and
commit. Upload must hold the **existing staging lock continuously through final
publication-lock acquisition and commit**. Retain the ordinary locked `stage`
wrapper and factor an internal already-locked body to avoid self-relocking.
The initial publication/order check still releases before staging; body receipt
and validation remain outside. Publication is not held throughout staging, so
maintenance can still enter during staging and the final authority check refuses
commit afterward.

This supersedes the prior brief's lock-interleaving rationale. Prune tries both
publication and staging locks **nonblocking**; if staging is busy it immediately
releases publication and skips, never waits or spins while holding publication.
Current maintenance/status/rollback paths acquire publication only, so none
creates a blocking reverse edge. Add a concise implementation comment preserving
that relationship. No new lock, marker or persisted schema is introduced.

Owner3's focused multiprocess checks must hold a historical re-stage before final
commit, demonstrate prune's busy-stage skip releases publication, and allow the
upload to commit on its first attempt. Also demonstrate maintenance-enter during
staging still prevents commit. Broader deletion and deployment-wait checks remain
as specified above. Owner3 received the settled correction directly; no further
source-release or investigation gate is required.

#### P26 independent follow-ups: sufficient source boundaries

P25 live cutover/retention is accepted. Lead may release these small independent
packages while the authoring contract below is investigated. No default merge,
new deployment or repeat proxy activation is implied; future authoring policy
does not integrate this migration. Lead retains the context-owned final prose
pass before commits. Architect owns design only; implementers own source/index.

**Owner1, BLOG favicon and title.** Start from published472 and preserve the
current restored main-only workflow. First identify the old WordPress favicon
through a bounded read-only request to retained WP8081 with the fixed Czech Host,
or an already retained public-asset archive: inspect its icon link and fetch only
the referenced icon bytes. If no declaration exists, inspect its `/favicon.ico`
response. Record source path, MIME/signature, dimensions and digest; refuse an
HTML/error response or an unproven substitute. No private export or new graphic
design. Once identified, copy those bytes to one ordinary `static/` icon path
and add the matching root-relative icon declaration in
`layouts/_default/baseof.html` for both language roots. Existing static asset
propagation supplies the output; no runtime fetch or new dependencies.

Correct only the title word `přihlášování` to `přihlašování` in
`content/posts/2025-03-03-two-factor-login-with-passkeys/index.cs.html`.
Preserve its nonbreaking space, public URL, wp-841 identity, dates, body, authors,
feed GUIDs and translated meaning. Refresh the complete Czech-file digest in
both `data/migration/source-manifest.json` locations (`articles[].cs_file_sha256`
and `generated_files[cs_file]`) and paired English `translation_source_sha256`.
The private original `source_body_sha256` and prior human-review provenance are
unchanged; a mechanical title correction is not a new human-review attestation.
Keep broader proofreading/metadata checker changes for the later authoring package.
Files are the icon, base layout, these two article files and the manifest; no
shared checker edit is required for these small fixes. Quick evidence checks
actual icon identity/type, exact title-only body-preserving diff, both derived
digest bindings and unchanged source-body identity. Normal review precedes the
existing BLOG build/check output proving both icon paths/declarations and title/
canonical URL. No extra test framework or full corpus rewrite.

**Owner0, web link and workspace inventory.** Use isolated session worktrees and
read current repository guidance after the ordinary fresh-ref preflight. Retained
web origin/master307635a has three relevant English references:
`en/hlavicka.html` navigation and feed, and `en/paticka.html` footer. Point them
to `https://blog.vpsfree.org` and its `/feed/`, preserving layout, link attributes
and Czech links. Current source has a pinned flake/dev shell; use it, not the old
ambient `shell.nix` composer-install hook. This is a two-file link change, with
source diff/link checks and normal reviewed package verification; the unrelated
registration/cluster integration suite need not be expanded for it.

The existing workspace feature already lists `blog` at
`docs/agent-instructions/projects.md:53–58`, including its canonical SSH remote,
two hosts and content/build ownership. Verify that committed feature entry and
its ordinary publication status; do not duplicate it merely because shared
master lacks the unmerged change. If current wording needs a narrow correction,
edit only that project-map entry in the workspace feature worktree. Forum/UI
setup remains user-owned; configuration owns hosting. Preserve the shared-master
records and unrelated workspace source/index. Sequence only owner0's own indexes.

**Owner3, dependent CONFIG web pin.** After the exact reviewed web feature is
published, use the existing native channel command
`confctl inputs channel set --commit vpsfree-web vpsfreeWeb <exact-web-SHA>` in
the CONFIG Nix environment. The channel and role/input are **vpsfree-web →
vpsfreeWeb**, a non-flake input currently pinned307635a; do not hand-edit lockfile
or refresh unrelated inputs. `modules/services/vpsfree-web.nix` consumes it;
`configs/webs/default.nix` assigns `vpsfree.org` to `en`, and the configured
consumer is `cz.vpsfree/containers/int.web`. Development vhosts use an explicit
directory override. Preserve all other graph nodes, routing and effective blog/
proxy generation. Check native lock/source scope and hooks, then review before
the affected native int.web build with exact source/input proof. Pinning does not
authorize int.web activation, default integration or another blog/proxy switch.
Retain prior web/input revisions for normal recovery. No new machine claim is
needed merely for feature work/builds.

Packages are independent except CONFIG's exact published-web dependency and
BLOG's shared index: owner1 completes the tiny BLOG package before authoring
source ownership begins. Lead may release the read-only favicon identification
and these bounded source packages without waiting for the broader authoring
design. No source, network, build or runtime action was performed by architect.

P26 favicon identification is now settled by owner1's bounded WP8081 read:
old public `/wp-content/themes/flat/favicon.png`, advertised as shortcut icon,
is PNG16×16,607 bytes, SHA256
`dfe1b759dd6db24982fb4844e514bebf102462ac8f54f16725e12cfea0105fe8`.
Retained bytes are `theme-reference/p26-favicon/favicon.png`. Use those exact
bytes as `static/favicon.png`, shared `rel="icon" type="image/png"` declaration,
and one provenance entry in existing `static/theme/NOTICE.md`; no separate media
license is inferred. The unrelated apple-touch link was not fetched or requested.
This completes the tiny package's asset dependency. The manifest contains two
Czech-file hash references plus the English translation reference: refresh all
three for the title correction. No broader authoring rule change is included.


#### P26 authoring: sufficient implementation and verification brief

Settled source package, subject to lead allocation after the tiny BLOG8e1 review
and build identity window. Owner1 owns BLOG source/index; architect owns this
brief, lead the final context-owned prose pass. Web/workspace/CONFIG work is
independent. No application, build, network or runtime action by architect.

**Files and commands.** Add focused `bin/check-articles`, ordinary
`.githooks/pre-commit`, small CS/EN technical wordlists under `tools/`, and one
blog-specific `bin/observe-publication`. Update existing `flake.nix` devShell,
`bin/check`, `tools/import-wordpress-check`, `AGENTS.md`, authoring skill and
`docs/authoring.md`; adjust README/deployment/migration links or contradictory
sentences only as needed. Keep workflow/client/protocol and application rendering
unchanged except generic check expectations. No lockfile/pin refresh, new editor,
attestation manifest, spelling API, server, token or publication authority.

`nix develop -c bin/check-articles --staged` validates the actual Git index;
plain invocation checks working source, with optional article IDs for focused
proofreading. The hook invokes the staged command through the pinned environment
and reports actionable path/language/field/word diagnostics. Document ordinary
opt-in installation `git config --local core.hooksPath .githooks` and verification
of configured path plus executable hook; do not silently overwrite an existing
hook setup. Once installed, failed checks block commit. Read index blobs with
Git, including staged additions/deletions/renames; do not stash/reset, silently
stage corrections, or accept a working-tree fix absent from the index. Validate
the staged metadata and companion language even if only one file was staged.
No full Hugo/native build in the pre-commit hook.

**Editorial flow and metadata.** The skill accepts either Czech or English as
input, corrects title/prose typos contextually, generates the missing language,
then compares both for meaning, chronology, attribution and archive voice. Keep
commands, code, links, IDs, proper names and factual claims intact; do not guess
private attribution. Finalize Czech as the existing hash source even when
English was supplied first, then record its complete exact-file SHA256 in EN.
Replace human-only review/draft gates and claims that metadata is unchecked.
Retain genuine historical human review; new review fields name the actual agent
identifier and timestamp, never an invented human. Existing `draft`/`reviewed`
translation status semantics suffice: reviewed non-draft EN needs reviewer,
RFC3339 review time and current CS hash; draft pairs may truthfully remain draft.
Every committed real bundle, including drafts, has exactly CS and EN; uncommitted
single-language preview remains supported.

Executable checks cover valid TOML, nonempty title, timezone-bearing original
`date`/`lastmod`, explicit boolean draft, stable matching translationKey/article_id,
one bundle and one supported file per language, shared publication state and
original date, unique explicit host-root URLs, and complete shared metadata.
Require existing public author IDs, nonempty bylines/unique archive slugs, Czech
absolute discussion URL matching the article, and unique immutable CS/EN feed
GUIDs. New IDs stay outside `wp-`; new GUIDs use the documented URNs. Validate
optional taxonomy references. Preserve existing IDs, published paths, dates,
bylines/discussion/feed identity and private source-body digest. Any intentional
historical correction remains an explicit scoped editorial change; no bulk
metadata migration or automatic attribution/date rewrite.

**Spelling is a diagnostic, not proof of language quality.** Use conventional
`pkgs.hunspell.withDicts` with `hunspellDicts.cs_CZ` and `en_US` from the existing
BLOG nixpkgs pin, exposed as `hunspell` in the devShell. These interfaces exist in
retained local nixpkgs source; owner verifies their availability at BLOG's exact
pin in the normal quick environment check, without refreshing inputs. The skill
performs grammatical/semantic proofreading before the command; Hunspell reports
unknown words only and must not silently autocorrect. A small explicit reviewed
technical wordlist handles legitimate names/terms; never whitelist every error
or require corpus-wide spelling cleanup. Check all prose/title of new articles;
for existing articles check introduced prose/title words against the prior Git
version so unchanged legacy noise or a source-hash-only edit does not block.
Exclude code/pre blocks, inline code, URLs, markup/attributes and identifiers,
but include visible link labels and image descriptions. Report unknowns for the
agent to correct or justify with a precise dictionary entry. Do not claim this
proves grammar, translation, language detection or absence of valid-word typos.

**Preserve archive auditing while allowing authored rows.** The importer encoder
is sorted JSON, ensure_ascii=false, indent=2 and final newline. For only the three
shared generated JSON files, audit canonical projections of original rows
against their EXISTING manifest digests: article IDs from manifest.articles;
authors selected uniquely by manifest.archives.authors slugs; category/tag keys
from their manifest archive paths. Require every original selector exactly once,
then hash the original-key/value projection; altered/deleted original content
still fails, while new unrelated entries can pass. All other generated-file,
125-original-article, private source-body, comments/media and optional private
source comparisons remain intact. Do not regenerate original metadata hashes to
bless new rows. Keep the importer's current refusal to overwrite manual additions;
reimport is an archive operation, not the authoring command. General renderer,
search and feed checks derive eligible source counts; the exact historical link
mapping/count audit remains scoped to manifest IDs. Keep intentional unpaired
synthetic/working-preview tests outside commit-ready pair enforcement.

**Publication and observation.** Optional preview uses existing `bin/preview`.
After proofreading and staged checks, future approved non-draft content goes
straight to fresh `main` with ordinary hooks/protections; drafts/preparation stay
on a feature branch. This editorial policy does not merge the current migration,
transfer feature infrastructure to main or grant server/settings changes. Respect
an actual host refusal; do not weaken protections or introduce a feature-CI cycle
as a compulsory step for a routine approved article.

`bin/observe-publication --sha <pushed-SHA> --article <ID>` is a bounded read-only
blog observer, not a publisher or generic poller. Prefer public GitHub REST for
Build blog's exact SHA/workflow path/push/main identity; existing authenticated
`gh` may be used if already available, never require login/new secrets. Bound
requests and the overall wait (default ten minutes); identify run/attempt and
terminal build AND deploy jobs. Skipped delivery is not publication success;
retain failed/unknown outcomes without retrying a push or upload. If API/auth/
rate limits prevent CI observation, check the expected CS/EN public article URLs
with normal TLS and bounded polling. Compare exact built bytes when an existing
artifact with matching source identity is available; otherwise report only the
specified title/content/canonical observations and that deployed commit and CI
are unproven. Site appearance never turns unknown/failed CI into green. The skill
reports the exact pushed SHA, observed run/delivery result or limited fallback,
and any timeout; no automatic resume, rollback or synthetic run identity.

**Acceptance and checks.** Quick focused fixtures demonstrate staged bad versus
unstaged fixed content fails, staged good versus unstaged bad uses the index,
missing CS/EN fails even for drafts, malformed/missing metadata and stale hashes
fail, CS-first/EN-first completed pairs pass, and new rows pass archive projection
while an edited/deleted original row fails. Use real pinned dictionaries on a
known CS/EN typo plus valid technical/code/link/name examples; verify old unrelated
unknown words are not newly demanded. Observer fixtures cover exact run matching,
failed/skipped deploy, timeout/rate-limit and site-only evidence without false CI
success. No live publication needed for these checks. After quick checks, ordinary
commits and mandatory review precede existing `bin/check`, `bin/check-release`
and `nix build .#site` with one new bilingual article fixture, draft exclusion,
unchanged original archive audit and optional unpaired-preview behavior. Evidence
binds exact source, command/results and limits. No new long suite or actual
article publication is needed merely to validate this tooling package. Lead owns
later delivery and normal workflow observation; recovery is reverting tooling
without touching current content, keys, receipt/order state or production services.


#### P26 accepted correction: observe draft feature checks

The existing observer also covers the user's draft-feature flow. Add
`--branch <exact-pushed-branch>`, defaulting to `main`, to
`bin/observe-publication`. Main retains strict successful workflow/build/deploy
and the existing bilingual public-site checks. An explicit non-main branch uses
the same bounded public REST/optional existing-gh observation, matching exact
SHA, branch, repository, workflow path and push event. Report feature CI success
only when the workflow and build succeed and deploy is terminal/skipped;
publication is `not requested (draft feature)`. Unexpected delivery is a policy
mismatch; failed, cancelled, unavailable or unknown CI remains nonzero.

Feature observation bypasses public-article preparation (which rejects drafts)
and makes **zero site requests**, including fallback. API failure or timeout
reports unknown CI without searching for intentionally unpublished content.
Skill/docs pass the explicit feature branch after a draft push and use the main
path after publication. This corrects the earlier main-only observer boundary;
no new poller, workflow/settings change or publication authority is introduced.

Focused checks cover successful feature CI with skipped delivery and zero site
calls, wrong SHA/branch rejection, failed/cancelled/unknown CI, unexpected feature
delivery, and unchanged main skipped-deploy rejection. Owner1 retains the current
source package and ordinary review boundary; lead accepted this interface delta.


#### P26 R2 accepted correction: retained build on deploy-only rerun

For main observation, current workflow and current-attempt deploy must be
terminal/successful. If that attempt contains no build, inspect earlier attempts
of the **same exact run ID** in descending order. Stop at the first actual build,
whatever its outcome; require completed/success plus its actual `Package release`
and artifact-upload steps completed/success. Do not skip failed, skipped,
cancelled, incomplete or ambiguous builds to find an older green result. An
older attempt's overall failure may be its deployment failure and does not
invalidate an otherwise successful build/package.

Retain exact selected SHA/main/push/workflow/repository matching. Validate jobs'
`run_id`, `head_sha` and `run_attempt` against the queried run/attempt; real retained
API jobs expose these fields. Missing or incomplete API evidence leaves CI
unknown, not permission to skip an unexamined attempt. All lookups share the
existing absolute deadline and request bounds. Report prerequisite `build_attempt`
separately from the current deployment attempt. The unchanged deploy/client
already downloads its own run's artifact and verifies source/run/original build
attempt; add no artifact API, downloader, uploader or authority. Feature checks
and zero-site-request behavior remain unchanged.

Owner1's focused regressions cover deploy2 reusing successful build/package1;
a newer failed/skipped/incomplete build preventing reuse of an older success;
absent build, mismatched run/SHA/attempt, unavailable evidence and missing/skipped
package or upload steps not confirming success. Lead accepted this source
correction within the existing owner1 package and normal hooks/review boundary.


#### P27 sufficient source brief: draft, unlisted and published articles

Lead accepted the two-flag/filter approach and announcement-date correction.
Relevant interfaces are settled; no essential investigation blocker remains.
Owner1 may take the complete BLOG package from accepted8b30/treecb728 after lead
allocation, retaining its source/index and active hooks. Lead owns the final
contextual prose pass. Architect performs no application/runtime work. No CONFIG,
proxy, workflow, secret, permission, production action or migration integration
is part of this package; current no-merge direction remains in force.

**One state contract, compatible defaults.** Keep explicit top-level `draft` and
add optional boolean `params.unlisted`, default false. Reject non-booleans,
`draft=true` with `unlisted=true`, or unequal CS/EN states. Derive the state with
this truth table, use one Hugo state partial across templates and the same small
rule in Python consumers; do not create another editable state field or general
state engine. No author-managed `build.list`/sitemap knobs are required.

| draft | unlisted | State and delivery |
| --- | --- | --- |
| true | absent/false | Draft: omitted from production; local/VPN preview, feature-branch CI only. |
| false | true | Unlisted: normal direct URL in production, deployed through main for review, excluded from discovery. |
| false | absent/false | Published: ordinary listed production article, delivered through main. |

All 250 existing imported language files and shared metadata/review/body hashes
remain untouched and published by default. Retain existing public IDs, URLs,
bundles, bylines, discussion identities and feed GUIDs. This is visibility, not
access control: anyone with an unlisted URL can read/share it, Git source remains
public, and noindex cannot compel every crawler or recall previous copies.

**Dates and transitions.** Permit date changes while the prior committed state
is draft or unlisted, including on transition to published. On publication set
the actual announcement time in both languages, so feed/order uses that date.
Once published, ordinary authoring permits only published→published and freezes
that original date. Reject published→draft/unlisted; this prevents a date-reset
loophole without a new history journal. Preserve all existing/imported published
dates. URL/ID/GUID/bundle remain stable through every transition; the dated bundle
name keeps its initial name even when announcement date changes. Update lastmod
for substantive edits/state promotion, not on each build. Re-finalize Czech and
refresh the exact-file English hash after any CS metadata/state/date change;
retain honest existing review semantics and non-draft reviewed-translation gate.

Both languages must have the same state and date; both remain required for draft
commits. Apply the comparison to staged metadata against HEAD, as existing hooks
do. Non-drafts must not have a future announcement date; retain Hugo's normal
production future-date exclusion and do not enable buildFuture there. Add
`--buildFuture` alongside buildDrafts to BOTH local/VPN preview generation and
server invocation so future-dated working drafts remain previewable. Explicit
article publishDate/expiryDate or build/render/list overrides are unsupported
within this finite contract and should be refused rather than creating a second
publication schedule. No such overrides occur in the current corpus.

**Production rendering and discovery.** Use conventional finite template filters,
not an unverified Page.Build accessor. Filter before pagination, first-N limits,
counts and grouping. Unlisted articles remain rendered at their exact CS/EN URLs
with ordinary canonicals and reciprocal language links, but receive localized
visible review banners and `noindex, nofollow` robots metadata. Published pages
keep ordinary metadata. Do not list unlisted URLs in robots.txt or Disallow them
there: compliant crawlers need to fetch the page to see noindex.

Exclude unlisted from homepage/section lists, all author/date/category/tag archives,
recent sidebar links, tag/category counts/clouds, RSS, sitemap and search. The
source-scanning `content/_content.gotmpl` month/author discovery must use eligible
articles rather than every non-draft file; do not generate unlisted-only month
or author discovery. Filter taxonomy memberships/counts and omit empty/unlisted-only
terms from public navigation and sitemap; do not remove shared source labels.
Use a small custom sitemap preserving host/canonical/translation semantics and
other normal routes, with no unlisted URL in loc or alternate links. Structural
empty term pages need not be deleted if they expose no unlisted article/link.

`bin/index-search` independently crawls rendered HTML: omit the
`data-search-article` marker on unlisted pages and their Pagefind body/meta markers;
the existing positive-file-list/zero-article guard must remain. Search-page
availability and test counts use discoverable articles, not every rendered URL.
Previews continue to show/index working drafts as before, but unlisted stays
excluded from discovery and remains directly reviewable. Apply production-style
unlisted exclusion to generated English target maps/recommendations; never add
an unlisted target through automated related navigation. Preserve explicit source
links and code: an author deliberately linking an unlisted URL can disclose it,
which is documented rather than silently rewriting historical prose. Cross-language
links within that same directly opened unlisted pair are intended.

Discourse script/embed eligibility additionally requires published state, even
when the global embed is enabled; unlisted/draft pages must not create topics or
show an invitation implying article discussion is enabled. Keep existing archived
comments intact where present. This does not change Discourse settings or erase
existing topics, notifications, caches or other previously public copies.

**Owned source boundary.** Existing `bin/check-articles`, `bin/check`,
`tools/check-authoring.py`, `bin/observe-publication`, `bin/preview`;
`content/_content.gotmpl`; base/single/list/archive/search templates, RSS,
sidebar/article-html/discussion partials; small state/list partials and sitemap
layout; `i18n/cs.toml`, `i18n/en.toml` and existing CSS only for banner styling.
Update AGENTS, authoring skill/guide and minimal README/discussion/deployment
sentences to describe the actual state flow. Existing indexer behavior should
need no new service or index format. `bin/build`/package metadata hashes ALL
rendered files, including unlisted direct pages; package/receipt schema, complete
file accounting, uploader and target contract stay unchanged. Split expected
rendered versus listed/search/feed counts in checks without weakening the exact
original archive audit. Do not add state fields to every imported file.

**Authoring and observation.** Draft preparation commits/pushes stay on features.
When the user requests an unlisted review or publication, use the existing normal
main path with intended article-only changes, hooks and host protections; review
content is not forced onto a feature merely because it is still being prepared.
On unlisted→published change flags/date/lastmod and refresh CS→EN hashes before
checks/commit. This future editorial policy never merges this migration branch.
The existing observer derives expected state from the exact requested commit,
accepts unlisted on main and checks its banner/noindex/direct-page identity in
both languages; published checks reject lingering unlisted markers/noindex.
Expose a stable rendered state marker for this small comparison if useful. Keep
exact CI/build/deploy and same-run rerun proof, deadline and honest site-only
limits. Feature observation remains checks-only, zero site requests. No extra
poller, authentication or automatic server/pause/settings change.

**Acceptance and checks.** Quick fixtures exercise the state truth table, invalid
booleans/combinations, staged CS/EN mismatch and missing companion, fresh/stale
translation hashes, draft/unlisted date edits and promotion, frozen published
date/state, and future-dated non-draft rejection. Source/ordinary hook checks and
one tiny native-Hugo three-state fixture can settle template APIs before commit;
record actual command/time and keep it bounded. Verify existing published files/
metadata unchanged. Commit, then mandatory independent final review before long
integration checks.

Use the existing bin/check/bin/check-release/native site batch for meaningful
three-state CS/EN fixtures with distinctive titles/terms/months, actual Pagefind
indexes and emitted sitemap/feed HTML/XML. Draft has no production article;
unlisted has exact direct pages, banner/noindex and translation/canonical links,
but zero discovery entries/markers, including mixed and unlisted-only taxonomies,
authors/months, sidebar counts, sitemap alternates and RSS. With global Discourse
opt-in enabled in the fixture, only published embeds. After promoting unlisted
at a recent actual date, the same URLs/GUIDs enter homepage/RSS/search/sitemap,
lose the banner/noindex, and retain dates on later edits. Local/VPN preview still
renders a future draft without production inclusion. Observer fixtures distinguish
unlisted/published state and preserve all P26 main/feature/rerun regressions.
No real article, live upload, server or external request is needed for acceptance.

Evidence binds final commit/tree, focused checks, complete final review, native
Hugo/Pagefind output and unchanged imported corpus. Before any later delivery,
confirm the new renderer is the one carrying unlisted source: older code ignores
this marker and could list it. Source rollback may revert the package before
unlisted content is used; afterward keep the compatible renderer or explicitly
remove the unpublished review content in a reviewed source change. Do not rebuild
unlisted source with old templates. Existing exact-release rollback still restores
its prior complete payload; no runtime schema migration or new recovery mechanism.


#### P29 sufficient rollout contract: reviewed feature delivery before merge

The user authorized switch-over and verification before merging. P25 already made
both blogs static; this package updates their content and activates the English
web links. No default integration, proxy change, workflow/environment exception,
new source or new protocol is needed. Lead launches each released mutation driver;
owner1 owns exact BLOG package/client preparation, owner3 CONFIG/native/copy/dry,
held target ownership and live verification. Architect owns these records only.

**Settled independent BLOG delivery.** Exact reviewed source is
`a24ed26f04ccdbf09684ad8e855c64b37d03aae4`, tree
`0eaf28311e866c2591dc7d71b140edc4202c0724`; accepted native artifact
`/nix/store/sfvxlsvhzcaskhgz4zcc59zr54qmf54i-vpsfree-blog-0` is bound by
[p27-artifact-result.json](p27-artifact-result.json), including its source/input
NARs, metadata digest and all 2399 served hashes. Real push CI is
run42594078633, run_number16, attempt1, same feature SHA/workflow/repository,
terminal success ([run](p27-ci-final-run.json)); packaging/deploy were skipped
and [Actions artifact count is zero](p27-ci-final-artifacts.json).

The unchanged `bin/package-release` accepts a clean exact checkout plus this
native artifact; it does not require an Actions-origin artifact. Owner1 runs its
ordinary local interface with `--sha a24ed26f04ccdbf09684ad8e855c64b37d03aae4`
`--run-id 42594078633 --run-attempt 1`, outside the clean checkout for output,
then records archive/receipt/package identities, full file/hash accounting and
exact source/input bindings in the preparation packet. This is **operator-local
packaging associated with actual CI16.1**, not an Actions-produced/delivered
artifact; the package's conventional artifact_name is not proof one existed.
Package digest is a concrete release input supplied by that packet, never guessed.

The unmodified client uses real GITHUB_RUN_NUMBER=16, GITHUB_RUN_ID=42594078633,
GITHUB_RUN_ATTEMPT=1 and GITHUB_SHA=a24ed26f04ccdbf09684ad8e855c64b37d03aae4.
Only the later authorized fixed root process on blog.int reads the existing
`/private/blog/deployment-key`, validates exact UTF8 roundtrip without stripping,
and invokes the unchanged client with the key solely in private process memory/
environment. No secret contents/hash/signature, argument, environment dump or
shell trace enters evidence. HTTPS uses normal hostname/CA verification to exact
`https://blog.vpsfree.cz/_deploy/blog`; HMAC authenticates the existing method,
path, run number and ZIP digest. No key crosses proxy→backend HTTP. Keep existing
300-second/three-identical-byte-retry client limits; no outer blind retries or
synthetic run numbers/attempts. The receiver proves key possession and package
consistency, not independent protected-main eligibility; this is existing accepted
operator authority, not a new delivery exception.

Owner3's fresh preflight at cleanCONFIG9b0 already confirms heldblog4cd, current
w3/oldsource76d7/policy4nby, selected A66/receiptd5649, floor11.1, RESUMED/no pending,
MySQL0700, retained WP/services/key metadata. Recheck those exact guards and owned
claim immediately before effect; a changed floor/current/policy/system or package
is a concrete drift to reconcile, not permission to invent a higher run. The
successful ordinary upload advances floor to16.1 and selects the new exact
package atomically while **remaining RESUMED**. Do not copy P22's coexistence
pause/resume sequence. No backend generation build/activation is needed for this
content-only step, and w3 must not be relabeled as a9b0 build.

After the durable client result, bind response source/run/attempt/release/body
and current-receipt digest to root status and floor16.1. Verify every2399 declared
file and metadata/input identity in the selected immutable release tree, plus
complete declared set; shared retained immutable assets may legitimately exceed
that set. Bracket this inspection and HTTP checks with matching current pointer/
receipt/floor/policy/system/mode so a concurrent change cannot be certified as the
same selection. Read-only verification needs no maintenance pause. Confirm public
normal-CA CS/EN roots, exact favicon bytes/declaration, corrected passkey title and
unchanged URL, feed/search/article/media/alias samples and private/reserved-route
rejections against the accepted artifact. Check retained WP8081, MySQL0700/PID,
receiver UID/GID, loopback/firewall and timer/control health. Do not run live prune
or a gratuitous rollback test. Three-state capability is proven by the accepted
P27 native fixtures and delivered source/artifact identity; do not publish a fake
unlisted/draft article for a live demonstration. No forum embed is enabled.

On success preserve RESUMED, previous A66 content/receipt and natural monotonic
floor16.1. On lost response/uncertain client outcome inspect the exact original
transaction/status before any retry; client failure alone does not prove the old
selection remained. Conflicting/corrupt state stops further effects. If recovery
is necessary, use the existing root rollback with exact retained A66 key and
fresh expected-current receipt: it pauses before selection, preserves floor16.1,
and requires deliberate verified resume. This recovery pause is justified by the
failure, not routine success. No old-floor reset/reupload, private data rewrite,
backend switch, key rotation or automatic cleanup. The retained WP route remains
a separately prepared compatible system recovery, not an ordinary P20 switch.

**Independent int.web preparation and switch.** CONFIG is exact
`9b0cf03eb51cac24efb1b763b4349fae7c8d704d`, tree
`eb5a392697c74746304ff3206f74725ba3c715a6`, with web input7fec3e3c in the existing
vpsfree-web→vpsfreeWeb mapping. P28's message replay preserves source trees/patches
but is not a new NAR/derivation receipt. Prefer one ordinary fresh native build of
ONLY `cz.vpsfree/containers/int.web` at9b0, allowing normal cached substitution;
record exact source NAR/full graph/effective inputs, generation/system/deriver and
rollback output. Old95b/6vfm remains old evidence; reuse instead requires actual
new-source graph/derivation binding, not tree equality. No blanket blog/proxy
rebuild. The later web pin does not require changing an already suitable w3
content receiver; any concrete backend semantic delta goes to lead first.

Owner3 acquires a separate typedint.web claim with fresh UUID under its released
preparation scope, preserving heldblog4cd; verify mapping once for this intended
batch. Before copy/dry effects, bind actual target/address, selected/profile/live
old system and recovery generation, vhost/PHP/service baseline, certificates and
health. Copy exact prepared output and inspect generation-specific native dry
activation plus relevant current/candidate unit/config differences; a quiet dry
log alone is not full service-diff proof. Expected scope is web root/input
replacement and its ordinary nginx reload/restart; preserve unrelated vhosts,
accounts and services, no proxy, reboot or data migration. Unexpected substantive
baseline/package/activation differences are reported for lead disposition rather
than silently widening the switch.

After a concrete ready packet, lead releases exact int.web activation. Verify
selected/profile system/source/input graph, actual service effects and health,
then normal public HTTPS vpsfree.org rendered RSS/nav/footer links to
https://blog.vpsfree.org(/feed/) and unchanged Czech links/representative vhosts.
Source SSI include bytes alone are not live link proof. Do not submit forms or
trigger unrelated application operations. On failure use the retained exact
int.web generation through normal confctl recovery and verify public health;
retain both attempts and claim while uncertain. Blog delivery can be released
and accepted without waiting for this independent web dry/build packet.

**Release/evidence boundary.** BLOG ready means package digest+exact local inputs,
actualCI16 identity and fresh target guards; WEB ready means exact9b0 native output,
copy/dry/live comparison/recovery+held typed claim. Neither requires new source
review for operational records alone. Owner1 coordinates known-small packaging
inline without idle utility reservation; owner3 uses the ordinary watcher for
long native work. No repeated broad CI/native campaign; source fixes, if needed,
return to lead's normal review boundary. Each final receipt binds observed effects,
all hashes, command outcomes and limits, preserving previous receipts/roots/refs/
backups/fixtures. No operator-created package is relabeled Actions delivery.

Machine claims remain held until effects are verified AND complete deployed
feature lineage/dependencies are integrated under separately explicit approval.
P28 successors require reviewed lineage evidence; old deployed SHAs are not
literally merged merely because trees match. Then inspect authoritative exact
claim status, reconcile uncertainty, release and verify as the installed guide
requires. No current merge approval, release bypass or lifecycle cleanup follows
from this rollout. Remaining preparation outputs are evidence inputs, not open
product decisions; the next observable is owner1's hashed local package and
owner3's separately bound web candidate/ready packet.


#### P30 sufficient brief: explicit Discourse author metadata

Owner1's dependent BLOG package starts from accepted a24. Lead retains source
release and the final contextual prose pass. Scope is head metadata, one small
mapping, focused checks and authoring/discussion instructions; no forum/API call,
embed enable, source publication, live upload, CONFIG/web change or merge is
released by this brief. Architect append preserves prior records.

**Source contract.** Pinned Discourse v2026.9.1 at retained
`/nix/store/30w0v0ml6xzhg6vj1zzzk92b77y8xhfm-source` parses the first
`meta[name=discourse-username]`, falling back to `meta[name=author]` only if the
former ELEMENT is absent (`topic_embed.rb:249–251`). It strips content and queries
`username_lower` without lowercasing it. `import_remote` prefers that found user
over the retrieval fallback; a host's explicit Post author overrides again in
create/update. `lib/topic_retriever.rb:38–41` supplies the normal fallback from
`embed_by_username`, then site-contact username, then system user. These are
source facts, not proof of installed forum settings/account existence.

**Data and exact user mappings.** Add `data/discourse-authors.json`, a plain
optional author-ID→lowercase forum-username object, rather than adding fields to
`data/authors.json`. Existing original-row digests and whole-row staged byline
immutability must remain unchanged. User confirmed:

| Existing author ID / public name | Article count | Forum username |
| --- | --- | --- |
| wp-user-1 / Petr Krčmář | 38 | krcmar |
| wp-user-3 / Pavel Šnajdr | 38 | snajpa |
| wp-user-6 / Jakub Skokan | 46 | aither |
| wp-user-9 / Martin Myška | 1 | martyet |

Jiří Medvěd/wp-user-2 and Jakub Jirůtka/wp-user-8 each have one article and remain
unmapped, using the normal forum fallback. All125 current articles have exactly
one author. User also confirmed Michal Janoušek=KerryCZE, canonically `kerrycze`
for this parser; no matching author record exists in current public metadata.
Do not invent an unused row/map key or reattribute any article. Preserve that
confirmation here for a future real authored record. No WordPress slug/name
inference or network identity lookup. No generic admin username has been supplied;
it belongs to the forum's normal topic-creation setting, not this map.

**Rendering and multi-author behavior.** In article heads only, emit one
`author` meta tag containing the truthful public names from shared author_ids in
existing order (join multiple names consistently), and one `discourse-username`
tag. For a single author with an explicit mapping, its content is that username.
For unmapped or multi-author articles, emit empty discourse-username content:
the pinned element-presence precedence prevents a display name from accidentally
selecting a forum username, leaving the existing global fallback in control.
A short template comment and docs sentence explain this deliberate empty tag.
Do not pick the first author or invent coauthored forum ownership. Both languages
use identical shared identities. Hugo context-aware escaping must handle names
and attributes; never use safeHTML/safeHTMLAttr or concatenated raw head markup.
No metadata on homepage, archives or search; metadata itself is inert and does
not enable embed/topic creation on drafts/unlisted/previews.

**Checks and files.** Owner1 owns the new mapping, `layouts/_default/baseof.html`
(with one small partial only if that is clearer), `bin/check-articles`, existing
`tools/check-authoring.py`/`bin/check`, `docs/discussions.md`, `docs/authoring.md`
and the related short skill instruction. Read mapping through the existing
staged Source interface, validating an object with unique keys, keys in actual
authors, and nonempty trimmed lowercase string usernames without whitespace or
control characters. Absence is optional/no mapping; omission expresses fallback,
not blank/null map entries. Do not validate live account existence or impose
unverified forum length/account-policy rules. Duplicate target usernames may be
intentional user mappings; do not infer one-to-one ownership. Do not weaken
original import projection, existing names/slugs, shared article rows, source
bodies/reviews/dates/URLs/GUIDs or translation hashes; all250 files remain intact.

Correct the existing guide's advice to fill per-host Post author: user leaves it
blank, including the English framing-only host, and sets the ordinary global
Username for topic creation to their chosen fallback admin. Keep category/host/
path/source-URL/CSP and pilot boundaries unchanged. Explain confirmed mapping,
multi/unmapped fallback and adding a real future author's explicit username in
the authoring flow. Changing this metadata does not retroactively prove or repair
existing topic ownership; preserve existing discussions and verify intended
identity during the separately authorized pilot, without mass retrieval/import.

Quick focused fixtures cover valid/staged mappings, unknown IDs, duplicate keys,
invalid/uppercase/blank values and staged-invalid versus unstaged-fixed behavior.
One bounded real Hugo head fixture exercises both languages, single mapped,
unmapped and multiple authors, special-character name escaping, exactly one of
each meta tag, and absence on nonarticle pages. Confirm truthful visible bylines
and unchanged draft/unlisted/embed guards. Reuse existing test harnesses and
missing-map fixture support; no new identity service or test platform. Verify
original corpus/metadata bytes and audit compatibility, then normal hooks/commit
and mandatory review before the existing full bin/check/release/native build.
Lead's current release may hold source commit/publication until its stated gate;
this brief defines checks, not additional authority.

Compatibility is additive HTML plus optional map. Removing the map falls back
normally while preserving author names; reverting the whole feature restores
the previous no-author-meta behavior. Host overrides/global fallback remain user
settings and are never changed automatically. Embed opt-in and live publication
remain separately settled actions. Known original mappings are sufficient now;
only forum setting/account/pilot facts remain operational dependencies, not a
reason to invent missing author data or block the structural source package.


#### P30 sufficient CONFIG addendum: declarative Discourse embedding defaults

Settled source package for retained owner3 after lead allocation, independent of
owner1's BLOG metadata work. Only CONFIG
`cluster/cz.vpsfree/containers/discourse/config.nix` changes: extend the existing
`services.discourse.siteSettings` attrset, retaining all unrelated configuration,
input pins, administrator definition and secret-file references. No new module,
provisioner, database migration, API, secret, UI mutation or deployment is needed
to prepare this source. Source release/commit/native work remains lead-owned.

The machine selects `nixos-stable`; current CONFIG locks nixpkgsStable to
718f670e845328e9c2cecdd832835712b2cbd065. The retained nixpkgs source
`/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source` owns the ordinary Discourse
module and `nixos_defaults.patch`. Its siteSettings option generates
`/run/discourse/config/nixos_site_settings.json` on service preparation, loaded
as defaults by SiteSetting. Pinned v2026.9.1 source confirms these exact first-
and second-level keys (UI area labels are not the Nix categories):

```nix
posting = {
  allowed_embed_selectors = ".entry-content";
  embed_any_origin = false;
  embed_set_canonical_url = false;
  embed_unlisted = false;
  import_embed_unlisted = true;
  embed_truncate = true;
  embed_support_markdown = false;
};
embedding = {
  blocked_embed_selectors = "";
  embed_full_app = false;
  embed_by_username = config.services.discourse.admin.username;
};
security.content_security_policy_frame_ancestors = true;
```

The admin reference currently resolves to the existing configured `admin`; it
implements the user's requested fallback without inventing an account or adding
a map entry. This supersedes the preceding BLOG brief's unspecified fallback.
Configuration alone does not prove that the installed account exists/works.
Keep four exact original-author mappings; no synthetic Michal author. Both
languages retain the identical Czech discussion_url and one shared topic.

These are declarative defaults, not forced DB reconciliation. The module docs
explicitly permit UI overrides, and Discourse refresh merges stored values over
defaults. User reports no embedding/site-setting changes; retain this as the
user-supplied baseline, not live proof. No reset/remediation campaign follows.
Owner1 updates the existing BLOG `docs/discussions.md` within its package to
point to these CONFIG defaults and briefly explain precedence. Lead owns the
contextual prose pass. The extraction, visibility and framing values preserve
the accepted policy, including imported topics unlisted until a regular reply.

The host editor stores EmbeddableHost rows separately. Exact Czech/English hosts,
path allowlists, real category selection/permissions, optional tags and blank
per-host Post author remain ordinary UI-owned records. The English reject-all
import row still permits framing; it does not create a second topic. Account
existence and any prior topic/source mappings also remain operator pilot facts.
Do not encode these records as site settings or add automatic host/category/user
provisioning. RSS importer reconciliation, notifications and site comment-count
behavior are outside this CONFIG edit.

Acceptance/quick checks: one-file intended Nix diff, repository nixfmt/ordinary
hooks, actual option evaluation confirming the eleven values and the admin
reference without printing secret-containing aggregate settings. Preserve the
existing security.force_https default and all sibling attrs. Confirm pinned
category/key spelling from source; no new test framework or production probes.
Normal commit and independent final review precede the longer ordinary native
`confctl build cz.vpsfree/containers/discourse` under the retained watcher policy.
Native build is verification, not activation. Owner3 reports exact source/input/
system and check evidence; no unrelated system needs a rebuild for this package.

Later, only if deployment is released: normal claimed Discourse activation and
service-health verification, then verify effective settings/accounts and the
existing narrow pilot before BLOG embed opt-in. Delivering inert BLOG head
metadata and preparing CONFIG source can proceed independently. No schema or
protocol change is introduced. Reverting CONFIG restores old defaults on service
restart but does not erase saved UI values, host rows, topics or replies; do not
claim a system rollback undoes forum content. Current embed remains disabled and
no forum operation or merge is authorized by this brief.


#### P30 sufficient BLOG addendum: English discussion source and forum reply counts

User explicitly chose Discourse reply counts and one shared ENGLISH discussion
source/opening post. This supersedes previous Czech forum-source instructions,
not archive provenance. Owner1 owns one dependent source package from committed
3c48b874, after lead release; existing four author mappings/head metadata remain.
CONFIG's generic settings package is independent. No enable, forum call, topic
migration, deployment or merge is authorized here. Lead owns final prose.

**Shared identity.** Add one small `layouts/partials/discussion-source.html`.
Resolve the actual English page from the article's AllTranslations (including
self), matching params.article_id and posts type; require published state and
canonical HTTPS origin exactly `https://blog.vpsfree.org`. Return its real
Permalink after validating no userinfo/port/query/fragment and the supported
host-root route, otherwise empty. Never translate/guess a slug, substitute CS,
or consult an override map. Both discussion.html and count markers consume this
one result. Current125 EN routes are unique simple root slugs; future existing
checker-approved underscore/nested routes remain supported. Missing/wrong-host/
unpublished EN means no forum request. Existing production/not-server/explicit
boolean enabled/matching current-language BaseURL gates remain necessary.

Keep ALL existing content/data/import digests, dates, IDs, canonical URLs, feed
GUIDs, review hashes and Czech discussion_url rows unchanged. That Czech field
continues to identify original/source navigation for article-html.html rewriting;
it is no longer active Discourse identity. Keep its checker requirement and new
CS route policy, documenting the distinct purpose. New authoring supplies the
ordinary paired EN URL; no new per-row discussion field or duplicated EN map.
README, AGENTS, docs/authoring.md and skill must stop claiming that the Czech
field is the runtime discussion source. No renderer provenance rewrite.

**Forum guide.** Invert host roles: blog.vpsfree.org imports EN article paths;
blog.vpsfree.cz has reject-all `\A(?!)\z` for framing only. Both host authors
remain blank, with the same verified category. Use an anchored English rule
matching existing explicit-route grammar (underscore/nesting allowed), excluding
reserved first components already in the checker, cs/en prefixes and generated
year/month archive paths. A concrete rule is:

```text
\A/(?!(?:cs|en|search|feed|author|authors|category|categories|tag|tags|archive|archives|page|posts|assets|images|pagefind|admin|login|logout|robots|sitemap)/|[0-9]{4}/[0-9]{2}/)(?:[a-z0-9]+(?:[-_][a-z0-9]+)*/)+\z
```

The numeric exclusion corresponds to actual content/_content.gotmpl month
archives, not a ban on all numeric/wp-prefixed EN slugs. No new general EN slug
restriction. URLs colliding with generated archive routes are not valid article
routes; fixtures verify that concrete boundary. Preserve existing regex encoded/
decoded/query caveats, exact HTTPS authority and CSP frame-ancestor settings.
Both variants now import the same English article/opening post/source link.
Unknown preexisting Czech TopicEmbed records require operator reconciliation
before enabling; changing source does not merge, retag or delete topics. User
reports untouched settings and our embed remains off; do not claim no historical
forum mappings exist. No automatic reimport/migration or new forum locale setting.

**Byline/client scope.** Count only published article links actually rendered on
home/list/taxonomy/author/month pagination pages. Pass an explicit listing context
to the shared byline from list.html/archive.html; single.html must not launch a
redundant count batch beside its native embed. Replace the published byline's
ambiguous legacy numeric count with a localized plain discussion/Discourse link
to that language's article discussion anchor; eligible listing links additionally
carry the exact shared EN URL and an empty reply-label span. A successful label
is visibly identified as Discourse/forum replies, never an archive or combined
total. Keep historical comment bodies/anchors and ordinary access; draft/unlisted
pages gain no forum invitation, count marker or request. Off/preview/server/
wrong-origin pages have no count client/markers. No-JS/error/unknown stays a usable
plain link. No fabricated zero/loading number or mandatory layout spinner.

Use a small local fingerprinted `assets/js/discourse-counts.js`, loaded once with
defer on eligible listing pages, following existing hashed asset conventions.
No full-site enumeration or search/sidebar follow-up. Deduplicate explicit DOM
markers; at most one asynchronous JSONP GET after page load to the literal
`https://discourse.vpsfree.cz/embed/count`, with one fixed callback identifier
and repeated embed_url[] parameters built using URL/URLSearchParams. No arbitrary
endpoint/callback from HTML, retry, polling, local storage or credentials/API key.
Cap the one batch (50 unique displayed URLs and 8KiB encoded request URL suffice
for current pagination); if exceeded leave plain links, do not split into more
requests. Five-second client deadline, script error, absent/malformed callback or
CSP failure leaves links alone; late/duplicate callbacks are inert. A no-op fixed
callback may remain after timeout so an already fetched late script cannot cause
an uncaught missing-callback error. This is finite UI waiting, not a guarantee of
network cancellation or forum latency. No measured latency is claimed.

Pinned EmbedController#count:145–166 removes terminal #discourse-comments, then
one trailing slash from requested URLs; returned key is normalized URL, except
it appends #discourse-comments when the normalized URL was not in the request.
Therefore keep the exact canonical EN URL for association, but request its
single-trailing-slash-stripped form, and accept ONLY that exact normalized key
for each known DOM group. Both languages bind the same key even though their
local link hrefs differ. Stock count.js cannot do this correctly for translated
hrefs, hence the tiny adaptation rather than its unchanged loader.

Response is `{counts: {url: localized_reply_phrase}}`, not numeric counts.
Accept only own-property string values for requested keys, with a small reasonable
length bound; display via textContent only. Never innerHTML, evaluate response
strings, parse numbers, add legacy counts, rewrite hrefs or accept extra keys.
Known explicit zero phrase is displayable; an omitted key is unknown/not visible,
not zero. Endpoint uses posts_count minus opening post and guardian visibility;
it does not enqueue topic creation. Its semantics need not exactly equal visible
regular comments after moderation. Current-user effective locale wins; otherwise
anonymous locale follows enabled preferences/default. Native `tl=cs/en` is only
honored with set_locale_from_param=true, which defaults false. Do not promise
page-language phrases or mutate this global setting: localize the static forum
context in BLOG i18n, display the returned phrase unchanged, explain upstream
locale in docs. No guessed plural rules or localized integer parsing.

JSONP intentionally executes JavaScript from the same fixed forum origin already
trusted by native embed. Payload shape checks/textContent prevent data-to-HTML
injection, not execution of a compromised trusted endpoint. No wildcard CSP,
unsafe-eval or CORS/proxy workaround; preserve existing policies and treat blocked
script as plain-link fallback. HTTPS exact origin only; never load remote count.js
or script URLs supplied by a response. Count stays behind the SAME embed opt-in,
so this package generates no forum traffic while current production setting is
false. The later opt-in pilot should include one listing per language.

**Files/checks/release.** Owner1 owns the helper, discussion/byline/list/archive/
single/baseof integration as needed, one JS asset, i18n/cs.toml and en.toml,
existing bin/check/check-authoring fixtures, and concise discussions/authoring/
skill/README/AGENTS corrections. bin/check-articles changes only if needed for
an actually identified route collision check/message; preserve original-field
and archive audit invariants. No CONFIG, pins, workflow, packager or content edits.
A tiny JS execution fixture under tools (Node built-in vm/assert plus stub DOM,
no browser framework or npm dependencies) may use dev-only Node from the existing
nixpkgs pin if no declared interpreter exists; no lock/runtime package change.

Quick acceptance: synthetic real-Hugo CS/EN pair resolves identical EN source;
self/matching-ID/missing EN/wrong canonical, underscore+nested routes, every
existing disable/state gate, list-only markers and no marker on unlisted/draft/
nonarticle entries. Keep original bytes/audits and four author metadata checks.
One executable DOM/request fixture covers multiple/duplicate links → one request,
EN mapping independent of href, normalized returned keys, localized/zero phrase,
missing/restricted/extra/malformed results, literal HTML-like text, deadline/error/
late callback and no retry. No live forum or network needed. Normal hooks and
separate coherent count/source commit, combined intended BLOG final review, then
existing full checks/native build under watcher rules; no broad new campaign.

Compatibility is optional additive client plus changed pre-enable forum source.
Old archive data and disabled builds remain usable. Turning opt-in off removes
traffic; rolling code back does not undo any future forum topics and could switch
source back to Czech if enabled, so any later rollback must keep embed off until
identity is reconciled. Existing topic/account/category/installed-settings pilot
facts are deployment dependencies only. Sufficient for source release now; no
unresolved design prerequisite blocks owner1.


#### P30 full-app delta: supported source switches and live compatibility limits

User chose replying directly on the blog. Owner1's existing BLOG package adds
boolean `fullApp: true` to the JSON-serialized DiscourseEmbed object in
`layouts/partials/discussion.html`, updates its exact payload assertion in
`bin/check`, and corrects the mode/pilot text in `docs/discussions.md`. Owner3's
existing CONFIG package changes only
`services.discourse.siteSettings.embedding.embed_full_app` to true in
`cluster/cz.vpsfree/containers/discourse/config.nix`. Lead releases implementation.
Do not alter source under the running false-mode41ca build: first join it, retain
its actual evidence, then normal hooks/commit amendment or successor and new
review/native identity. Old successful native evidence never certifies the new
flag. English identity, mappings, counts, historical corpus and embed opt-in
remain unchanged; `hugo.toml` still has enabled=false.

Pinned v2026.9.1 native embed.js supports fullApp, sends full_app=true, uses
scrolling=yes, default height600px and lazy iframe loading. Use these defaults;
no custom resizing, login widget, cookie/session bridge or new client options.
EmbedController redirects a visible mapped topic to its normal URL with
embed_mode=true only when both server setting and client request are enabled.
An unmapped source still follows native topic retrieval/loading. Native reply
UI checks user and normal posting permissions. Existing sign-in flow defaults
true and can use a top-level login tab/Storage Access API; those upstream flows
are not proof of browser authentication or a new BLOG poller.

Two concrete limits must remain explicit, with material policy resolution via
lead before any live pilot/enable claims:

- Full-app `lib/embed_mode_handler.rb` removes X-Frame-Options only when the
  parent referrer matches EmbeddableHost.record_for_url, including allowed_paths
  (or embed_any_origin, which must remain false). The current Czech reject-all
  framing row therefore works for the classic embed CSP but BLOCKS full-app
  framing. Both hosts being in frame-ancestors alone is insufficient. Do not
  silently broaden Czech import paths or claim that this two-flag change solves
  both-domain framing. Guide must distinguish this unresolved full-app condition
  from the earlier classic-only host recipe until lead settles it.
- Pinned same_site_cookies defaults Lax, and auth/session cookies honor it.
  forum.vpsfree.cz here means the actual discourse.vpsfree.cz origin: Czech blog
  is same-site, English .org is cross-site. Under unchanged Lax, .org iframe
  authentication is not supported merely by logging into a top-level tab;
  upstream embed-auth-flow explicitly assumes same-site or SameSite=None.
  Actual installed value is unverified. Preserve cookie/security settings;
  source tests cannot waive this or browser third-party-cookie restrictions.

The narrow two-flag source preparation is independent of deciding those live
policies; it introduces no database/schema migration or topic rewrite. Keep
CSP, embed_any_origin=false, exact origins/referrers, category permissions and
normal top-level forum access. No source-field mass edit or automatic topic
repair. CONFIG defaults remain subject to saved UI overrides.

Quick verification reuses existing tiny Hugo cases: enabled production payload
contains boolean fullApp=true with the same English identity in CS/EN; disabled,
server, preview, wrong-base, draft/unlisted and missing-EN outputs remain inert.
Retain count fixture success for unchanged client scope. CONFIG normal nixfmt/
hooks and scoped setting evaluation verify true without reading secret fields.
Review final changed heads before the required ordinary native builds. No new
browser platform or live/forum test in source preparation.

After separately resolved host/auth policy and explicit deployment release,
activate reviewed CONFIG and verify effective setting before BLOG opt-in. Pilot
one shared English source from both blog domains: anonymous rendering, normal
login transition, actual inline reply with ordinary account permissions, same
topic identity, CSP and cookie-restricted-browser behavior, plus working top-level
forum fallback. Actual replies/topic creation require that operational release;
no source/native result proves them. User's chosen inline UX remains pending this
pilot, especially .org. In mixed deployment either missing switch retains classic
embed behavior; both true selects full app. Reverting either switch reverts mode,
not topics/replies, and keeps the same English source. Disable BLOG opt-in for
recovery when framing/auth is uncertain. No deployment, UI mutation or merge is
implied by this source-only brief.


#### P30 full-app resolution: native host rules and cross-site session cookies

Lead accepted the smallest native host-policy change for user's inline-reply
choice. This resolves the preceding full-app note's pending host/cookie design;
its source/build sequencing and live-pilot limits still apply. Both exact blog
hosts need article-path allowlists because native full-app checks the parent
referrer against allowed_paths. Keep the accepted EN underscore/nested rule;
use the existing CS root-slug namespace rule for blog.vpsfree.cz:

```text
\A/(?!(?:feed|search|author|authors|category|categories|tag|tags|archive|archives|page|posts|assets|images|pagefind|admin|login|logout|robots|sitemap)/|wp-|[0-9]+/)[a-z0-9]+(?:-[a-z0-9]+)*/\z
```

This supersedes CS reject-all framing-only instructions. Keep blank host authors,
verified category, exact HTTPS hosts, native referrer policy and frame-ancestors;
embed_any_origin remains false. Both BLOG variants still pass only the actual
shared EN canonical to embed/count, producing one topic during normal browsing.
Native allowlists now permit manual/external Czech-source imports too, which can
create another topic. State that limit plainly; no claim of server-enforced
EN-only identity, no dual RSS importer, no plugin/proxy/custom source gate. Before
later enable, reconcile existing source mappings without deleting topics/replies.

Add one standard CONFIG setting alongside embed_full_app=true:
`services.discourse.siteSettings.security.same_site_cookies = "None";`.
Pinned config/site_settings.yml places it in security, with exact enum values
Lax/Strict/Disabled/None. None is necessary for ordinary cross-site iframe
sessions on blog.vpsfree.org; do not choose Disabled. This intentionally changes
the forum-wide SameSite cookie policy, not only the blog. Existing Discourse
module derives security.force_https=true from configured enableACME=true;
DefaultCurrentUserProvider and DiscourseCookieStore consequently emit Secure
session/auth cookies (auth token remains HttpOnly). Verify those effective values
when later authorized; do not read token values. Do not add a duplicate force_https
override, change cookie domains or relax CSRF/origin/CSP protections.

Native embed_full_app_signin_flow defaults true and stays unchanged. Its own
source assumes same-site or SameSite=None, then uses normal user-driven login/
Storage Access API where supported. ApplicationController's existing CSRF token
protection and BAD CSRF refusal remain intact. SameSite=None permits eligible
cross-site use; it does not override browser third-party-cookie blocking or grant
storage access. Full-app success on .org remains an actual browser-pilot fact.
Retain top-level forum navigation for blocked/denied login, and document that
sign-in may open a tab even though writing can remain inline once authenticated.
No custom authentication, browser-setting workaround or CORS change.

Final small ownership: owner1 discussion.html adds fullApp=true, bin/check's
existing exact payload fixture includes it, docs/discussions.md changes both
host rules/mode/pilot wording and explains cookie/fallback limits. Owner3's same
config.nix package changes embed_full_app and adds same_site_cookies only after
joining false-mode41ca native work. No edit under its running build; preserve
that receipt as false-mode evidence, then normal hook/commit/review and the new
native identity. Lead prose pass/release retained. Existing EN helper/count/maps
and disabled Hugo opt-in are untouched.

Quick CONFIG evaluation checks embed_full_app=true, same_site_cookies="None"
and inherited force_https=true without dumping secret attrs. BLOG tiny fixture
checks real boolean fullApp and all existing disable guards; no new auth test
platform. Native/source tests establish wiring only. Later authorized operator
pilot verifies actual framing, anonymous/read state, login plus inline reply on
both domains, same English topic, and top-level fallback under blocked cookies.
Do not enable publicly before that accepted result. Reverting the mode leaves
forum topics/replies intact; reverting cookie policy to Lax can make .org iframe
sessions unavailable and UI overrides can outlive a system rollback. No runtime,
UI, topic, deployment or merge action is authorized by this design. No further
product decision is required to prepare this conventional source package.


#### P31 sufficient operations brief: inert metadata delivery, then one EN pilot

User reports Discourse deployed and pilot hosts configured. Treat that as user
report until owner3's read-only proof, not permission for another deployment or
settings change. Owner1 prepares one exact existing package/client/driver; lead
launches the released mutation after concrete guards; owner3 owns fresh BLOG
baseline/heldclaim and forum/post-delivery verification. Architect records only.
No source edit, rebuild, new CI, global enable, merge, web.int, system switch,
account/cookie reset, importer or topic migration. Forum authentication and actual
inline posting remain the user's browser operation, not an agent-authored reply.

**Independent BLOG delivery.** Accepted final head
985d4eaa74309b219a762dcc02316df4a350065d/tree774efe50f4f24f5cf9945fa7b0271fec443ac54b
and `/nix/store/ysy4gaydzzh17z07xyrdnl2vky3in38k-vpsfree-blog-0` are bound by
p30-artifact-result.json, p30-output-head-proof.json and native/review receipts:
2399 served hashes, metadata SHA256
487527c20c60a5eaed61112315a27efbec084abc428f5ea7820366b73a352af9, all250 article
heads verified, protected corpus unchanged, Hugo enabled=false and zero production
count markers. Real successful feature push CI42613369754 is run17/attempt1;
package/upload-artifact/deploy skipped, zero Actions artifacts. Package this exact
local native artifact with unchanged bin/package-release and real identities;
record archive/receipt/ZIP hashes and bytes in owner1's preparation packet.
It is operator-local associated with actual CI17.1, never an Actions artifact.

Reuse P29's finite fixed driver/auth process, updating ALL concrete old/current/
new identity guards, not the uploader protocol. Current accepted P29 selection is
a24ed26f04ccdbf09684ad8e855c64b37d03aae4-4050259213d48748, receipt
64d240fd7e1c5d56c028e4113633657b73b94843ac69d9c9b9f18092b40a31e8, floor16.1
(run42594078633), body
0fbcba40ea03eaae82a8538d4ee3bc873831674a9c8a7cca5e878b0f48980a69. Owner3 freshly
binds held blog4cd, intended current CONFIG mapping proof, actual w3/76d7/policy4nby,
RESUMED/no pending and current receipt/floor; current CONFIG source must not be
mistaken for a newly activated backend generation. Drift stops effects until
reconciled. Keep retention lock behavior and WP8081/MySQL0700/backups/old roots.

After lead accepts concrete package/driver/preflight, copy exact bytes using
existing strict trusted BLOG access and run the unchanged client once. Its fixed
root process reads existing key only into authentication memory/environment,
never prints key/signature, strips bytes or exports secrets. Normal CA+hostname
HTTPS to blog.vpsfree.cz/_deploy/blog, real17/42613369754/1/985d identity, existing
300s/at-most-three-identical-byte client retries; no outer blind rerun. Successful
selection advances floor17.1 and remains RESUMED; no routine pause/resume. Bind
durable response/current receipt/pointer/body/source/order and full2399 declared
file/hash set plus metadata/input identities. Bracket read-only verification with
matching policy/system/current/floor/mode. Public checks compare both pilot pages
and root/favicons to built bytes, correct author tags, sharedEN source and continued
absence of embed/count scripts. No forum request is needed to publish this inert
release. Preserve prior16.1 package/receipts/recovery and normal timer health.

Lost reply requires exact original transaction/status reconciliation before any
retry. Do not invent a higher run/reset floor or assume failure kept old content.
If actual content recovery is required, existing root rollback to retained a24
uses expected-current receipt, pauses and preserves floor17.1; verified deliberate
resume follows. No rollback rehearsal, live prune, backup extraction or cleanup.

**Forum proof and the one pilot.** Pilot is actual article wp-841:
EN `https://blog.vpsfree.org/two-factor-login-with-passkeys/`, paired CS
`https://blog.vpsfree.cz/dvoufaktorove-prihlasovani-s-passkey/`. Both delivered heads
must show truthful author Jakub Skokan and discourse-username=aither. Expected
shared source is the exact EN URL, never the Czech provenance URL.

Owner3's p31-forum-local-trust.json proves an existing known-host entry for
`discourse.vpsfree.cz`, not the raw IP. Use ordinary hostname access with strict
host-key checking/batch authentication, verified declared address37.205.13.116
and finite bounds; no keyscan/accept-new/trust edits. That receipt does not prove
remote authentication. If accessible, read running/profile/source/service and
only whitelisted nonsecret default/DB-override settings, the two host rows,
category public-read/member-reply permissions, blank host authors, and pilot
account/mapping metadata through ordinary existing local access/SELECTs. No
secret-file dump, private user fields, content bodies or write-capable repair.
Native7w1/source0488276 proves built defaults only; actual live identity may differ.
Required pilot settings include full-app=true, same_site_cookies=None,
force_https=true, protected CSP/any-origin=false, body extraction, configured
fallback and accepted unlisted-import policy. Record actual overrides separately.

Check exact normalized EN and pairedCS TopicEmbed identities (and trailing-slash
variants), including conflicting/deleted mapping if present, with topic/category/
owner IDs only. No broad enumeration. Reuse a safely matching existing English
topic; an unexpected owner, conflicting Czech discussion or ambiguous source is
not permission to rewrite ownership/create replacement. Lead/operator resolves
that concrete conflict first. Check no second blog RSS importer will race it;
retain notification implications. Public /embed/count may show visible known
mappings but absent keys do not prove absence; /embed/info requires an API key,
and /embed/comments can create topics, so neither is a read-only shortcut. If
strict existing access fails, one focused operator request asks for the relevant
settings/host/mapping confirmation through their ordinary admin UI/console.
No credential request or new access platform; BLOG delivery proceeds independently.

Once metadata delivery and forum/mapping conditions are accepted, the lead may
provide this exact native console snippet for ONE English pilot, then the same
snippet on its paired Czech page. It changes only the current tab. Do not run it
on indexes/other articles; scroll to the discussion to trigger native lazy iframe.
The first load can create one English topic and notifications; it is an explicit
pilot effect, not a read-only page check. Let first EN creation settle before CS.

```javascript
(() => {
  const source = 'https://blog.vpsfree.org/two-factor-login-with-passkeys/';
  const here = location.origin + location.pathname;
  const allowed = [source, 'https://blog.vpsfree.cz/dvoufaktorove-prihlasovani-s-passkey/'];
  const target = document.querySelector('#respond');
  if (!allowed.includes(here) || !target ||
      document.querySelector('#comments')?.dataset.discussionUrl !== source ||
      document.querySelector('meta[name="discourse-username"]')?.content !== 'aither' ||
      document.querySelector('#discourse-comments, #discourse-embed-frame')) {
    throw new Error('Wrong pilot page, missing reviewed metadata, or embed already present');
  }
  const container = document.createElement('div');
  container.id = 'discourse-comments';
  target.appendChild(container);
  window.DiscourseEmbed = {
    discourseUrl: 'https://discourse.vpsfree.cz/',
    discourseEmbedUrl: source,
    fullApp: true
  };
  const loader = document.createElement('script');
  loader.async = true;
  loader.src = 'https://discourse.vpsfree.cz/javascripts/embed.js';
  document.head.appendChild(loader);
})();
```

No API key, custom login or source opt-in change. Reload removes the injected DOM,
not a created topic. User checks one shared topic URL, aither attribution, English
opening excerpt/source link, body/media extraction, normal anonymous access,
login transition and their own authorized inline reply from both domains. Keep
top-level forum fallback for blocked cookies; SameSite=None/native source tests
do not prove browser authentication. Owner3 may verify the resulting public topic
and exact mapping metadata read-only after the browser effect. Do not mass-open
archives, post for someone else, force ownership or delete the pilot to hide it.
Current source/global counts remain false; separately reviewed enablement with
updated production assertions is a later package, not part of this pilot.

Sufficient preparation is settled now. Concrete package digest, fresh live BLOG
state and live forum/mapping facts are execution inputs owned above, not reasons
for new design/testing phases. Report proof versus user report versus untested
browser outcomes distinctly. No new Discourse activation/merge is implied.


P31 lead clarification: server readback and p31-forum-readonly.sh are OPTIONAL
for diagnosis, not pilot acceptance gates. Accept the user's deployment/host
setup reports as operator facts, explicitly leaving unobserved settings/source
identity unverified. After metadata delivery, ask only whether the passkey article
already has a Czech or English Discourse topic (URL if present). If the user
reports none, proceed with the one English native browser pilot; existing or
unknown topics require focused operator UI reconciliation, not DB absence proof.
The browser pilot establishes effective framing/login/reply behavior. This
supersedes the preceding brief's mandatory settings/readback wording; no SSH
retry, access provisioning or agent topic creation follows.


P31 pilot 404 diagnosis (source facts, cause not yet observed): pinned full-app
comments returns 404 for a mapped missing/deleted or guardian-inaccessible topic;
invalid host/path is 400, while no mapping returns loading200 with native30s
refresh. Guardian permits direct unlisted topics in public categories, so
import_embed_unlisted alone is not the cause and listing changes are unwarranted.
Comments selects the oldest normalized HTTP/HTTPS mapping; public count uses the
exact requested key and cannot prove absence. Native anonymous cache stores only
200 responses. Next evidence is the existing pilot topic URL/category in admin
UI and direct logged-out visibility; no recreate/reimport/delete, cookie/CSP
change or source patch before resolving that concrete branch.


#### P31 confirmed correction: host matching after URL normalization

Lead accepted owner3's actual read-only proof: TopicEmbed1→topic374 is active and
undeleted, category=-1, visible=false; both host rows select public Blog10. Their
single-backslash anchored path rules require a terminal slash. Six running source
files match the pinned code and uncategorized_category_id is -1. This confirms
the mechanism: TopicEmbed.import normalizes away the terminal slash (:72), then
looks up the host (:81); matching fails, category:nil falls back to -1. The earlier
slash-required host-rule design was wrong. Unlisted state is not this failure.

Proposed exact pilot path corrections (ordinary host editor; writes still need
lead/user release) accept both the canonical and importer-normalized forms:

```text
blog.vpsfree.org: \A/two-factor-login-with-passkeys/?\z
blog.vpsfree.cz:  \A/dvoufaktorove-prihlasovani-s-passkey/?\z
```

Keep category10, blank host authors, exact hosts and all security/settings intact.
Separately propose the normal existing-topic move of topic374 to Blog10, preserving
TopicEmbed1, shared English source, author, posts/replies and visible=false.
Changing the host rule alone does not repair the existing category. No delete,
reimport, replacement topic, owner rewrite or listing toggle. User authorized root
QUERY only; this note authorizes no runtime write or retry of the import endpoint.
After an explicitly released repair, read back the two rules and topic/category/
mapping/visibility before resuming the same browser pilot.

Bounded source follow-up for owner1 after lead allocation: correct the published
BLOG docs/discussions.md broader CS/EN article rules too, keeping their existing
namespace restrictions while allowing optional terminal slash. Reserved-root,
numeric-CS and generated-month-archive exclusions must match both `/` and end of
string, so slashless reserved paths cannot slip through. Preserve canonical
article URLs and discussion-source.html's canonical validation; no corpus/checker
schema/client change is needed. Update retained operator setup instructions under
lead-owned record scope. Add a focused executable regression using the actual
published regexes and Ruby's native matching: pilot canonical and normalized
paths both select the same host/category; valid EN nested/underscore paths remain
accepted; roots, reserved paths with/without slash, queries, numeric CS and actual
month archives stay rejected. Test the importer order (normalize then host match),
not only the initial canonical request. No full forum test platform or new build
campaign. Source fix/review and runtime repair are distinct releases; no source
implementation or runtime mutation has occurred in this correction.


#### P32 all-article enablement and normal main delivery — sufficient brief

User confirms both browser pilots work and requests embedding on all articles
and integration. Lead accepts BLOG→main and CONFIG→master; web.int deployment
stays excluded. P29/P31 public switchover and the browser pilots satisfy the
previous switch-and-verify-before-merge requirement. The selected delivery is
ONE ordinary protected-main Actions push, after the source checks below and
host widening. No preliminary operator upload, workflow exception or new gate.
This supersedes the earlier proposed P32 enabled-feature-upload-before-merge
order. Current live BLOG remains 985d/operator17.1 until actual new delivery.

**Source package: settled, independent and ready for lead release to owner1.**
Baseline is clean BLOG620f14cc96cdc14792a9e26ed3de204f90aa04bb,
tree014c8dec9662a12866e75afebcc1a0b8e09ca114. Owner1 owns its source/index/commit
window; lead retains the final contextual prose pass. Files:

- `hugo.toml`: change only explicit boolean `params.discourse.enabled` to true.
- `bin/check`: update `check_search_script`, `check_roots` and their affected
  callers to distinguish production-enabled output from isolated preview output.
  Keep a finite script inventory: existing Piwik, existing search module only on
  search pages, one native inline embed loader only on eligible article pages,
  and the fingerprinted deferred/SRI count script only on eligible production
  listing kinds. Reject unexpected scripts; do not merely ignore Discourse text.
  Validate decoded payload equality: fixed forum origin, boolean `fullApp:true`,
  and the exact matching published EN canonical derived from source article
  identity/URL, for BOTH rendered language variants. Require the comments target
  and forbid listing-count scripts/markers on article pages. For listing markers,
  require eligible rendered article identity, its paired EN source and unchanged
  local `#comments` link. Roots/search/redirects must not acquire article embeds.
  A count script on an empty eligible listing is harmless; the existing client
  performs no request without markers. Production synthetic tracking fixtures
  must explicitly permit the expected listing script, not bypass script checks.
- Minimal matching prose in `README.md`, `AGENTS.md`, `docs/authoring.md` and
  `docs/discussions.md`: describe the enabled production default and retained
  suppression elsewhere, remove the now-obsolete disabled-output assertion
  instruction. Keep setup/pilot instructions useful for a fresh installation
  temporarily configured false. Distinguish Discourse enablement from the
  separate target-publication default-off contract; do not rewrite that contract
  or turn these project docs into a session deployment receipt.

Keep templates/client, author map, content/data/import hashes, public URLs,
feed GUIDs, package metadata contract, pins and workflow unchanged. Preserve
production exact-origin, Hugo-server, preview/VPN, draft/unlisted, missing or
invalid EN counterpart guards; no wider permission from the flag. Existing
`check_discussions` already exercises both modes, shared EN/fullApp payload,
author metadata and state/origin isolation. Reuse it and the JS DOM fixture.
If an actual implementation defect requires another file, report the concrete
boundary change to lead rather than expanding this package speculatively.

Quick boundary: ordinary staged article hook, Python syntax, existing tiny
real-Hugo discussion/tracking/script checks plus the Node count fixture; add only
focused negative assertions needed to prove the changed production inventory
rejects a wrong source/fullApp value or script on the wrong page. Reuse native
`tools/check-discussion-paths.rb` against the unchanged guide rules when touching
that guide. Commit intended files with hooks; independent final review follows.
Then run the established `nix develop -c bin/check`, `nix develop -c
bin/check-release`, `nix build .#site` and exact feature push CI, under the ordinary
watcher/ownership rules. No forum calls in these checks. Native output must bind
exact final source/input/NAR and all served hashes; enabled output file totals
are observed, not forced to the old 2399. Reuse prior evidence for unchanged
scope honestly. No extra test platform or corpus-wide language work.

**Independent operations: owner3 prepares; lead releases effects.**
Widen ONLY `allowed_paths` on existing host1 `blog.vpsfree.cz` and host2
`blog.vpsfree.org`, before any enabled public payload can arrive. Exact desired
rules are the two normal-operation Ruby expressions in BLOG620f
`docs/discussions.md` (EN first in the guide); copy their actual bytes, not a
reconstructed variant. They end in optional `/?\z` and exclude reserved roots
at either slash or end. CS retains its root-slug/numeric/wp exclusions; EN retains
supported underscore/nested routes and calendar-month exclusions.

Prepare one ordinary installed Discourse Rails runner/app wrapper, using its
existing service user/environment/application and `EmbeddableHost` model, or
normal staff UI. No raw SQL writes or new installed service/tool. Before release,
owner3 records exact invocation and guards: fresh exact host IDs/names, current
pilot regexes, category10/blank user, unrelated host rows/tags preserved, public
Blog10 and existing TopicEmbed1→topic374 healthy. In one model transaction lock
both rows, verify expected current values, `update!` only `allowed_paths`, and
read back. Allow an already-identical desired value as no-op; any other drift
stops before mutation. Model validations remain active. Preserve all settings,
topic/mapping/owner/posts and the actual pre-write listed/unlisted state (do not
force false if the user's pilot reply legitimately changed it). Read back only
those invariants after commit; timestamps may change normally. Unexpected or
uncertain outcome is reconciled before any retry or main push. Host-rule rollback
restores the captured pilot expressions through the same model boundary; it
never deletes hosts/topics or resets settings. No seeding, archive opening,
reimport, automatic reply, notification/auth change or source-host migration.

**Delivery, verification and integration order.**
Owner1 supplies final reviewed source/native/feature-CI identity; owner3 supplies
host readback and fresh BLOG current/floor/RESUMED/policy guards. Host expansion
and final source readiness precede the protected-main push. The unchanged
`.github/workflows/build.yml` packages on protected main, then deploys only on a
protected-main PUSH via blog-production and the unchanged authenticated uploader.
Lead confirms final approval/lineage and launches integration; release the short
repository claim after FF/push/remote proof, before observing Actions. Observe
that exact main SHA/run/attempt and required build/package/artifact/deploy result
with the existing observer (including its accepted same-run deploy-rerun rules).
This is a genuine Actions artifact, unlike prior operator-local17.1. Do not
invent a run number or claim selected content from CI alone; bind target response,
current receipt/release/body hash and monotonic order to the actual new run.
Healthy existing w3/4nby remains RESUMED; no artificial pause/resume/backend switch.

Post-delivery owner3 verifies normal-CA public roots and paired existing pilot
HTML, exact EN/fullApp payload, author metadata, listing markers and fingerprinted
count asset, full served manifest hashes at the backend, fresh current/floor and
receiver/retention health. Ordinary raw HTML/hash checks execute no embed. Use
only the already-mapped pilot for any live iframe follow-up; no crawling to
create topics. Existing pilot success is user browser evidence, not a universal
cookie guarantee. Count error/unknown still leaves a plain link and never a
fabricated zero. Record final source/run/deployed identity and any genuine gap.

Prepare BLOGmain and CONFIGmaster independently from fresh defaults with hooks
and complete final base-to-head/history review. Owner3 owns CONFIG rebase and
lineage evidence; unrelated CONFIG drift does not block owner1 coding. Review
any final refreshed shape, preserving required consumed refs and exact old/new
ranges, range-diff/equivalence and migration conclusions. Do not relabel consumed
BLOG0354/A66/a24/985d or CONFIG76d7/0488 as a new source, nor assert literal
ancestry for an equivalent successor. CONFIG integration implies no web.int,
backend or Discourse system activation. For reused native results, require
actual derivation/input binding, not tree equality alone. FF-only integration
claims cover only fresh target check/merge/hooks/SSH push/remote proof; release
before waits or record work. No source merge before its final checks/review.

Keep current17.1 and earlier selected release roots, receipts, WP8081/MySQL0700,
keys/backups and schema2 recovery. On uncertain upload inspect current/floor;
never substitute a new payload into an old order. Existing rollback selects a
retained release, pauses and preserves the greatest floor; explicit normal
resume binds the selected policy afterward. Forum topics/replies survive blog
rollback. A later corrective upload needs a newer authorized actual order.
Retain machine4cd until verified deployed lineage is integrated under the
installed coordination contract. No session cleanup/lifecycle action follows.

No design blocker remains for source release. Concrete app-wrapper invocation,
fresh baselines, final hashes, rebase equivalence and actual CI identities are
owned execution inputs, not another design phase. Lead owns state/portal updates;
this append records the bounded technical contract only.


#### P34 localized count phrases — sufficient source brief

Lead accepts a small version-bound phrase adapter instead of forum-wide CORS or
locale/auth changes. User requests localized index replies; the independent
legacy-comment cleanup is already committed at BLOG297991333afcd4fca50609a7504a15352bc57607
(parent live/integrated c900). Owner1 owns the dependent count source package;
lead owns the final wording pass and release. Current Actions20.1 remains live.

Pinned Discourse30w0 v2026.9.1 `EmbedController#count` passes integer
`posts_count - 1` (or zero for its missing-topic branch) to
`I18n.t("embed.replies", count: ...)`. The inspected translations are exactly:
`server.en.yml:676`: one `%{count} reply`, other `%{count} replies`;
`server.cs.yml:559`: one `%{count} odpověď`, few/many/other `%{count} odpovědí`.
In particular, upstream's Czech few form is `odpovědí`, not `odpovědi`.
No numeric API is claimed. These two known formats permit unambiguous extraction
of their complete ASCII integer; arbitrary localized responses are unsupported.

Files: `assets/js/discourse-counts.js`, `tools/check-discourse-counts.js`, and the
reply-count paragraph in `docs/discussions.md`. No template, corpus, byline,
translation-data, CONFIG, pin, protocol or dependency change is needed. Reuse
existing `<html lang="cs-CZ">` / `<html lang="en">` to select output; unsupported
page language leaves the existing plain link and makes no new kind of request.
Keep one same fixed-origin JSONP batch, the normalized shared EN keys, current
identity/size/deadline checks, and local links. Do not add `tl`, CORS, cookie,
credential, account or forum-default changes.

For each own-key string response, accept only an exact WHOLE phrase consisting
of canonical ASCII decimal `0` or a nonzero digit followed by digits (maximum
16 digits), one ordinary space, and one of the four exact native units above.
Require the complete match to equal the original string; do not trim it (JS `$`
alone can allow a trailing newline). Convert only the captured integer and
require `Number.isSafeInteger(n)` and `n >= 0`; MAX_SAFE_INTEGER is the bound.
Require native singular `reply`/`odpověď` iff n==1, plural `replies`/`odpovědí`
otherwise. Reject leading zeros, sign, decimal/grouped/localized digits,
exponent, suffix/prefix text, whitespace variants and out-of-range numbers.
Never use parseInt on a native phrase or guess a unit/language. Missing,
malformed, unfamiliar locale/customized phrases and changed upstream formats
leave that article's usable plain discussion link, not a fabricated zero.

Format the recognized value into the PAGE language using one tiny finite map:
English 1→`reply`, others→`replies`; Czech 1→`odpověď`, 2..4→`odpovědi`, all other
nonnegative integers→`odpovědí`. This Czech rule applies to exact integers 2..4,
not numbers ending with those digits. Keep the existing localized discussion
label and set only the existing reply span via textContent, e.g.
`Diskuse na Discourse: 0 odpovědí` / `Discourse discussion: 0 replies`.
No extra Intl dependency/framework is needed for these two integer languages.
This covers an English-preference logged-in reader on Czech blog and the reverse
without touching their session; other forum-language phrases deliberately fall
back. If Discourse translations change, the count label may disappear until
this explicit adapter is updated; ordinary discussion navigation remains.

Quick acceptance uses the existing offline Node DOM fixture executing the real
client. Test both page locales against BOTH accepted native phrase languages,
counts 0/1/2/4/5/11/21/22 and safe-integer boundaries, plus unknown locale/custom
text, malformed singular, negative/grouped/decimal/leading-zero/trailing-newline
and HTML phrases. Confirm exact expected output, zero versus omitted unknown,
unchanged links, textContent only, same deduplicated batch and unchanged
caps/deadline/error/late-callback behavior. Replace prior fixture strings which
were merely passed through (`3 odpovědi` is not the pinned native CS few form).
Existing integration invokes this fixture; retain the normal hook, syntax/diff
checks and existing source/head/Hugo guards rather than adding a new renderer or
browser platform. Commit separately from the accepted comment cleanup; provide
final diff/quick evidence to lead for independent review before ordinary full
`nix develop -c bin/check`, release checks/native build and exact feature CI as
required for the final combined deliverable. No live forum calls in fixtures.

No source-release blocker remains. This revises the old lead-owned no-parsing
constraint only for the two explicit version-bound formats, preserving forum-only
counts and unknown handling. Fresh final source identity/review still precede any
new main push, which is a publication boundary; P32 merge approval and released
machine claims are not reused. Deployment/integration authorization remains with
lead. Recovery is the ordinary previous-content release path; forum topics,
mappings and settings are unchanged. No settings deployment is required.


#### P35 WordPress removal inventory and proposed plan — PLAN ONLY

User requests finding the old WordPress implementation and showing what would
be removed. No implementation, deployment, merge or on-disk purge is authorized.
Read-only baseline: CONFIG HEAD and freshly fetched canonical SSH origin/master
are both `4771ff84e56de349bdde71bc221c62ccd4190f1b`, tree
`b6f1a48773a20927bec8dab78306bde5788a07af`; worktree is clean. Remote HEAD is
master. Applicable workspace procedures and CONFIG AGENTS/README/owning
`docs/operations/blog-static.md` were read/reused. No eval/build/test or target
connection was made. All line anchors below refer to this baseline.

Proposed scope: **68 CONFIG files removed, seven CONFIG files changed**, plus
one small dependent BLOG documentation correction. One retained CONFIG owner
(owner3, if lead allocates later) can own the complete implementation/test/docs
package; BLOG docs stay with owner1 and lead's prose pass. This plan does not
release either package.

**REMOVE — WordPress application and service definitions**

Let `S = cluster/cz.vpsfree/containers/int.blog/` within CONFIG.

| Exact path / anchor | Proposed removal and evidence |
| --- | --- |
| `S/wordpress.nix:20` (entire file, after transfers below) | Sole `import ./packages` caller. Remove WP site/package/plugin/language configuration, generated WP vhost/FastCGI, database provisioning and WP-specific controls. |
| `S/packages/default.nix:4` | WP7.1.2 override/hash; MU policy installation; Akismet5.7, Disable Gutenberg3.3.2 and Open Graph3.4.0 fetches; core/plugin Czech translations; Bootstrap3.4.1 fetch; Flat6.6.6 and TwentyTwentyFive theme composition. |
| `S/packages/vpsfree-policy.php:1`, `S/packages/flat-cs_CZ.mo`, entire `S/packages/flat/` | Delete these with `default.nix`: **67 tracked package files total**, comprising three top-level files and all64 Flat files (PHP, translations, CSS/JS, images, fonts/maps). No partial theme residue. |
| `S/wordpress.nix:24` and `:279` | Remove `wp-blog`, its isolated implementation/config paths, and `wp-blog-core-update-db` from the selected system. No separate tracked update script/patch stream was found. |
| `S/wordpress.nix:194`, `:196`, `:284` | Remove local WP database declaration and skip-networking setting, WP-generated MariaDB/PHP-FPM/init service, cron service and five-minute timer. Do not disable unrelated PHP/MySQL services elsewhere. |
| `S/wordpress.nix:237` | Remove WP loopback8081 vhost and its WP PHP/admin protections together; retain the static PHP denial in `static-blog.nix:70`. |
| `S/wordpress.nix:165` | Stop creating the two WP-user SMTP OUTPUT chains/rules and remove WP-specific mail assertions. Their exact old teardown needs the transition handling below; do not flush unrelated firewall rules. |

Tracked-repository reference search finds no consumer of this package tree
outside `wordpress.nix`. `overlays/default.nix:1` loads `overlays/packages.nix`,
which contains no WordPress override; **neither overlay nor shared packages,
flake pins or daily input updater needs editing**. Vendored theme code is
WordPress-only source, not the current Hugo runtime asset source.

**CHANGE — seven existing CONFIG files**

| Exact path / anchor | Proposed change |
| --- | --- |
| `S/config.nix:6`, `:13` | Remove WP import and obsolete `serveStatic=true`. Keep static storage/publication explicit true and exact runtime deployment-key path. Keep dormant ownership declarations described below here, with no WP service/package or data-writing activation. |
| `S/blog-routing.nix:45`, `:69`, `:86` | Remove `serveStatic` option and WP/8081 fallback/default vhost. Route BOTH fixed language Hosts to loopback8080 when `enable=true`; when false, return503 for both. Missing enabled content remains404, never implicit WP fallback. Keep unknown-host444 and reserved upload/hook exclusions. |
| `S/blog-routing.nix` (transfer from `wordpress.nix:110`, `:156`, `:159`, `:237`) | Own `services.nginx.enable=true`, `enableReload=true`, firewall enabled/iptables selection, exact proxy IPv4 /32 TCP80 allowance, proxy-metadata IPv4 assertion and no-broad-port80 assertions. Existing static/routing checks continue protecting private8080/8091; old8081/3306 remain closed with no listeners. Without this transfer deleting WP would remove nginx enablement and the backend's allowed ingress. Retain only the bounded two-chain SMTP teardown for the removal transition; do not recreate chains or reference a WP process. |
| `S/module.nix:36`, `:45`, `:52`, `:59`, `:91` | Remove MySQL/PHP-FPM/WP-init health requirements and WP8081 curl check. Keep nginx and selected Czech frontend check; replace the removed HTTP check with the equivalent fixed-Host English frontend check. Preserve container29942, address/target172.16.8.4, tags, logging/monitoring metadata. |
| `tests/blog-static-module.nix:5`, `:45`, `:88`, `:109`, `:131`, `:214`, `:378` | Replace WP baseline/preservation assertions with no-WP-runtime and retained-ownership assertions; cover static enabled and disabled503 modes, real generated nginx/unit/activation text, transferred exact firewall trust, feed/media/security and unchanged publisher policy/control contracts. Remove expected8081 and old selector assumptions, not the tests. |
| `tests/blog-upload-module.nix:83`, `:99`, `:151` | Replace WP-state equality with absent WP/MySQL/PHP runtime in both storage/publication modes plus preserved publisher identities/firewall. Keep all key/route/credential/service/retention checks. |
| `tests/blog-legacy-module.nix:11`, `:51`, `:61` | Remove WP import and WP/MySQL assertions; compose the ordinary new routing/static modules. Keep generated nginx and exact540-alias, feed/PHP-denial and no-Czech-aliases-on-English coverage. |
| `docs/operations/blog-static.md:10`, `:171`, `:178`, `:180`, `:253`, `:272` | Describe static-only routing and503 unavailable mode; replace current WP fallback/runbook with retained-static-release recovery and the ordered retirement below. Preserve version-scoped old coexistent-system recovery and schema restrictions explicitly rather than claiming old configurations never supported WP. |

The table has eight rows because the routing file has two concerns; it names
**seven distinct modified CONFIG paths**. Dependent documentation only:
BLOG `docs/deployment.md:88`, `:115` currently promises `serveStatic=false` WP
recovery; update its current-hosting description/link when the new CONFIG is
actually supported, preserving the historical schema2/old-system applicability.
No BLOG template, corpus, client, workflow or package change is needed here.

**KEEP — serving, publication, public history and retained state**

- `S/static-blog.nix:9`, `:21`, `:47`, `:65`, `:99`, `:130`, `:147` stays:
  `/var/lib/blog/current/{cs,en}`, retained fingerprinted CSS, immutable policy,
  pre-switch maintenance, blog-release identity/tmpfiles and daily keep5 prune.
  `S/blog-upload.nix:17` and `tools/blog-upload.py` stay, including exact Czech
  upload route, nonroot receiver and external credential. Keep
  `tools/blog-static-release.py:678` CSS and `:689` legacy-upload immutability.
- `S/legacy-routes.nix:3` and `data/blog-legacy-routes.json` stay byte-identical:
  all540 public legacy aliases, exact identity-query404 behavior, feeds and
  original permalink compatibility survive WordPress removal. Keep
  `tests/blog-legacy-projection.py`, `tests/blog-static-release.py`,
  `tests/blog-upload.py` and `tests/blog-proxy-module.nix`.
- `cluster/cz.vpsfree/containers/prg/proxy/blog.nix:11` stays: TLS/ACME, both
  public hostnames, fixed headers and backend80/exact upload exception. No
  proxy/web.int/Discourse deployment, settings or host/mapping changes required.
- Hugo's own `static/wp-content/` (569 tracked files), copied favicon/theme
  assets and `static/theme/NOTICE.md` stay. `bin/build`/flake has no CONFIG WP
  package input. The historical `/wp-content/uploads/` path is a static media
  URL, not evidence of a running WP dependency. Preserve public bylines,
  imported comments, URLs, author/translation audits and provenance/licensing.
- Keep shared `modules/system/phpfpm-session-cleanup.nix` and its module-list
  entry: it serves int.kb/int.utils/vpsfree-web, not this blog. Keep all shared
  PHP/MariaDB packages/modules and other hosts unchanged. No blog-specific
  backup job or logrotate rule is declared in the inspected site/base imports;
  generic nginx logs/journals and any external backups are not purge targets.

Persisted data is deliberately outside source removal: preserve
`/var/lib/mysql` (last accepted mode0700), all
`/var/lib/wordpress/blog.vpsfree.cz/` including uploads/fonts and secret-keys.php,
all backups, old store/system roots, `/var/lib/nixos` UID/GID maps, publisher
state/control/locks/receipts/floor and `/private/blog/deployment-key` untouched.
Retain inert `wordpress` and `mysql` Unix identities and mysql group alongside
nginx/blog-release: same declarations/IDs/group/home semantics as the predecessor,
no invented dynamic UID, no login enablement, no recursive chown/chmod or fresh
state-directory tmpfiles. The pinned Nixpkgs WP module creates a dynamic
wordpress system user in nginx's group; mysql uses ids.uids/gids.mysql (84 in
this pin). `nixos/modules/config/update-users-groups.pl:134,:270` removes former
declarative accounts even with mutableUsers=true, so simply dropping service
modules is not enough to preserve named ownership. Its UID map does not replace
keeping the identity while recovery data remains. WP's recursive upload `Z`
tmpfiles and MySQL data-directory mode rules disappear with the services; do not
copy those back as a new data migration.

**Compatibility, checks and proposed rollout — future authorization required**

1. Implement the bounded package only after plan approval, on fresh source with
   ordinary hooks. `serveStatic` removal is intentional source-option change;
   update every local caller in the listed paths. `enable` and publication
   defaults remain false, machine opt-ins remain true. Old and new complete
   system generations retain separate configurations; the public proxy/client
   contract and schema2 state remain compatible. No DB migration or deletion.
2. Quick checks: reference/dead-caller scan, formatting/hooks and the three
   existing Nix module fixtures against the locked stable input. Assert no WP
   site/FastCGI/cron/init/MariaDB runtime or8081 listener, unchanged account
   metadata, explicit nginx/firewall and correct503/static/404 modes. Inspect
   generated activation/tmpfiles for no retained-data deletion or permission
   broadening. Keep finite legacy projection and receiver/release tests; any
   long check uses the ordinary watcher. Independent final committed review
   precedes longer/native verification. Build **only int.blog** natively with
   `confctl build cz.vpsfree/containers/int.blog`, inspect closure/system diff
   and dry activation; no broad fleet rebuild or fresh upload benchmark needed
   for unchanged publisher code. Reuse exact relevant successful evidence only
   with its actual inputs, never by assumed tree equality.
3. Before any later deployment: fresh machine claim; fresh current/static
   receipt+floor and ownership baseline; verified complete retained previous
   static payload plus independent backups of old DB/site and rooted compatible
   systems. Runtime facts such as external backups, live ownership, permissions,
   unexpected DB users/jobs and selected generation are later read-only preflight
   inputs, not unknowns blocking this requested plan. Do not assume source
   absence proves the live host has no manually installed consumer.
4. Prepare build/copy/dry diff before activation. Expected retirement is only
   WP cron/init/PHP-FPM and local MySQL; verify no remaining WP worker needs its
   SMTP restriction. Enter publication maintenance, preserve exact current and
   floor, then activate static-only backend with nginx graceful reload and
   unchanged proxy trust. Pinned firewall reload uses the **new** config's
   extraStopCommands, so deleting both old snippets could leave their two
   OUTPUT chains/hooks behind: retain their exact existing idempotent teardown
   in the new routing transition, no broad flush or new chain. Old rooted
   generations can still recreate their original restrictions on recovery.
5. Verify both public languages/static hashes/feed/media/legacy redirects,
   no PHP execution, no8081/3306 listeners, intended units retired, account and
   data ownership/modes unchanged, receiver/current/floor/control coherent,
   timer/policy guard intact. New system identity requires explicit
   maintenance-exit even if helper/policy bytes match; successful resume changes
   no content/order. Do not mutate forum topics by crawling enabled articles.
   Integration and machine release follow separately authorized ordinary rules.
6. First recovery is the retained complete static release through existing
   guarded rollback (pauses, preserves maximum floor, then explicit resume).
   If system-level recovery is needed, use a retained compatible schema2
   generation with all its inputs/data; that restores its configured route,
   not automatically WordPress selection. WP routing requires that old
   configuration's own selector, not the new removed option. Preserve the
   old schema1/2 activation restrictions; don't run incompatible old writers.
   Check old MySQL/tmpfiles effects before reactivation: the pinned generic
   data-directory rule is0755, which must not silently widen the accepted0700
   retained state. No DB/forum rollback, reimport or deletion is part of content
   recovery. If no valid static release remains, fail unavailable and restore a
   backed-up static payload through normal authority; no phantom WP fallback.

A later **optional data purge** would need its own explicit approval, exact
inventory/backups/retention decision and acknowledgement that WP recovery is
being retired. Only then consider old DB/site/log/backup data, dormant accounts
or obsolete system roots. This plan authorizes none of it; no deletion/cleanup,
service stop, source edit, commit or review invocation was performed. Findings
are sufficient for user inspection now; only future live preflight facts remain.


#### P36 complete Czech typo audit — sufficient read-only package

Baseline BLOG63e08c7a1c6a3b4136197e2ec27836619563668b,
tree0475b8b90300be21b2c0862d5a74da15fdc990b8. Read AGENTS, repository
skills/blog-authoring/SKILL.md and docs/authoring.md; reuse the workspace
documentation/verification/writing procedures. User asks to correct the known
Passkey typo and audit all Czech articles; English translations are trusted.
No stylistic modernization, fact-checking campaign or English prose edits.

Inventory was derived from the baseline's tracked Git blobs, TOML IDs/states
and HTML-visible prose, not the old manifest's original-source word counts:
125 distinct Czech articles, all published; no article drafts, unlisted or
future entries. All are index.cs.html. Excluded separately:
content/search/index.cs.md (UI page, no article ID);
fixtures/content/posts/synthetic-pair/index.cs.md and
fixtures/content/posts/synthetic-unpaired/index.cs.md (synthetic draft fixtures).
Historical comments/data are not article prose and are outside this audit.

The table below exhaustively assigns all125 article IDs/paths exactly once.
Body-word weights include decoded visible text and image alt, exclude
pre/code/script/style, URL/email tokens and digit/underscore tokens, using the
existing checker's Unicode word-token convention. Counts are workload estimates,
not coverage proof or replacements for reading the source. Body total40886;
title-inclusive weights: implementer0 13895/41 articles, implementer2 13932/42,
implementer3 13935/42. Greedy descending-weight assignment bounds imbalance to
40 words. Table order within each partition is chronological path order.

**Owners / release.** Lead may release owner2/3 read-only partitions now;
owner0 takes its partition only after its independent navigation separator
package is accepted. Architect owns this brief only. Owner1's known wp-841
technolgii→technologii correction is independent and already has direct binding
clarification; owner3 still reads the rest of wp-841, reporting that known word
as already assigned, not another proposed fix. The baseline is frozen: read
with git show of that exact SHA if current source changes. Do not mutate Git,
fetch, checkout, edit source, install hooks or run tests/builds/network/forum/
runtime operations during this audit.

**Audit contract.** Read EVERY assigned title and visible Czech prose passage
in full context, including headings, lists, tables, captions, alt text and
visible link labels/tooltips. Use original HTML as needed to distinguish code,
links, quoting and prose; do not proofread a stripped word list alone. Flag only
spelling or obvious accidental typographic errors. Preserve technical terms,
proper names, intended historical quotes, commands/code, dated facts, links/
anchors, attribution, dates/lastmod, media and comments. Do not silently convert
valid-word preferences into corrections. Uncertain items may be reported as
uncertain, never applied. No broad grammar/style renewal or translated-title
rewrite.

Optional Hunspell aid uses the existing pinned Czech dictionary and exact
tools/spelling-cs.txt allowlist, without changing that list: full assigned
visible title/prose tokens may be fed to hunspell -l -i UTF-8 -d cs_CZ in the
already available repository environment. The normal bin/check-articles
subtracts HEAD's old tokens and checks only new/introduced words, so running
it on unchanged files does NOT audit the corpus. No new checker, persistent
extraction tool or dependency; if pinned tooling would require forbidden
build/network work, continue contextual reading and report the diagnostic gap.
Unknown words are leads, not corrections; correct dictionary words can still
be typos in context. A successful dictionary check is not reading coverage.

**Deliverable / acceptance.** Each auditor reports baseline, every assigned ID
as read (including no-findings articles), counts and a compact candidate table:
ID, exact path/line at baseline, before→after, enough sentence/paragraph context,
reason and confidence. Separate uncertain/intentional technical-word observations
from clear candidates. Do not claim unread articles checked or treat snippet
sampling as complete. Deliver findings to lead through normal reporting; no new
audit framework or source writes. Lead reconciles duplicate/stale candidates,
performs the final direct user-facing prose pass and authorizes exact edits.
Only then does one assigned implementer make a coherent accepted correction
batch, sequencing index/commit/shared manifest ownership. Independent reading
can continue while the known fix/navigation package is delivered.

**Legitimate correction bindings (already sent to owner1).** For each approved
imported CS edit, preserve exact original line endings/markup except the stated
typo. Recompute SHA256 over COMPLETE current Czech file bytes. Update only its
English params.translation_source_sha256 and the two existing manifest slots:
articles[matching article_id].cs_file_sha256 and generated_files[actual cs_file].
With CS itself, a one-article correction needs three files. There is no current
tracked English-full-file hash ledger to invent or update. Keep trusted EN
title/body byte-identical, dates/lastmod/state/URL/ID/feed/byline/taxonomy unchanged.
Preserve params.source_body_sha256 in both languages and the manifest's original
source_body_sha256, visible_word_count, conversion evidence and shared projection
digests. Raw-private import hash never becomes an editorial source hash.

Preserve genuine maintainer translation_reviewed_by/at history for unchanged
English. The correcting agent actually checks that the typo leaves its intended
meaning consistent with trusted English and records current actor/date plus
that narrow recheck in ordinary commit/evidence; do not redate an old human
approval or claim a new human translation review. bin/check-articles:181–192,
243–251 and tools/import-wordpress-check:185–210 enforce current-file/raw-source
distinction. The optional private --source import audit additionally compares
original visible body text: an editorial body correction intentionally differs.
Keep that audit and raw source unchanged; do not assert fresh raw-source parity,
rewrite provenance or rerun the importer over the corrected corpus to hide it.

After authorized edits: owned staged diff, byte-level preservation of English
prose and protected metadata, exact current-CS bindings and ordinary staged
article hook. Use existing public import audit/source checks and final review/
publication procedure appropriate to the accepted batch; no new tests mirroring
a typo. Lead owns approval/integration/push/CI observation; an article main push
can publish. Audit authorization itself grants none of those effects. Ordinary
revert of a correction must restore its matching derived hashes together; no
database/schema/server recovery change. No independent architect proofreading
has been performed; the table is inventory and allocation only.


**implementer0 partition (41 articles; 13895 title+body words)**

| Stable ID | Czech source path | Body words |
| --- | --- | ---: |
| wp-74 | `content/posts/2015-05-27-talks-for-docker-fans/index.cs.html` | 224 |
| wp-82 | `content/posts/2015-05-29-the-lasting-effect-of-conferences/index.cs.html` | 266 |
| wp-100 | `content/posts/2015-06-08-we-spoke-at-cryptofest-video/index.cs.html` | 171 |
| wp-139 | `content/posts/2015-10-26-vpsadmin-mount-changes-and-the-remote-console/index.cs.html` | 415 |
| wp-156 | `content/posts/2015-10-27-replacing-a-servers-motherboard/index.cs.html` | 325 |
| wp-137 | `content/posts/2015-11-03-99-986-availability/index.cs.html` | 357 |
| wp-205 | `content/posts/2015-11-20-we-didnt-win-kristalova-lupa-yet/index.cs.html` | 189 |
| wp-210 | `content/posts/2015-11-24-we-have-about-a-thousand-ipv4-addresses-left/index.cs.html` | 319 |
| wp-249 | `content/posts/2016-01-19-lupa-cz-wrote-about-us-and-says-we-are-unique/index.cs.html` | 80 |
| wp-269 | `content/posts/2016-02-15-come-and-see-us-at-installfest-5-and-6-march/index.cs.html` | 160 |
| wp-326 | `content/posts/2016-05-02-migrating-a-vps-between-providers/index.cs.html` | 209 |
| wp-347 | `content/posts/2016-05-17-we-support-an-internet-without-bureaucratic-censorship/index.cs.html` | 141 |
| wp-362 | `content/posts/2016-06-07-arch-linux-update-and-void-linux/index.cs.html` | 110 |
| wp-387 | `content/posts/2016-06-27-1000-members-means-we-have-not-messed-anything-up/index.cs.html` | 310 |
| wp-390 | `content/posts/2016-08-04-join-us-on-irc-at-freenode-net-vpsfree/index.cs.html` | 124 |
| wp-403 | `content/posts/2016-09-05-when-disks-fail-our-nas-gave-us-trouble/index.cs.html` | 236 |
| wp-408 | `content/posts/2016-09-21-why-we-want-a-20-gigabit-network/index.cs.html` | 461 |
| wp-443 | `content/posts/2016-10-03-we-are-going-to-linuxdays-come-and-see-us-there/index.cs.html` | 73 |
| wp-465 | `content/posts/2016-11-22-the-first-vpsfree-hackathon-come-and-work-on-networking/index.cs.html` | 335 |
| wp-493 | `content/posts/2017-03-13-our-first-trip-abroad-linux-tage-in-chemnitz/index.cs.html` | 437 |
| wp-516 | `content/posts/2017-05-29-linux-distributions-debian-and-ubuntu-lead-alpine-is-climbing/index.cs.html` | 224 |
| wp-521 | `content/posts/2017-06-26-what-is-a-reverse-dns-record-ptr-and-how-do-you-set-it/index.cs.html` | 473 |
| wp-529 | `content/posts/2017-09-05-vote-for-our-linuxdays-talks/index.cs.html` | 529 |
| wp-536 | `content/posts/2017-09-11-vpsadmin-v2-9-brings-simple-vps-monitoring/index.cs.html` | 170 |
| wp-539 | `content/posts/2018-03-06-we-introduced-vpsadminos-a-system-for-running-containers/index.cs.html` | 118 |
| wp-547 | `content/posts/2018-05-21-were-moving-from-openvz-to-vpsadminos-and-launching-a-test-environment/index.cs.html` | 289 |
| wp-560 | `content/posts/2018-10-01-come-to-linuxdays-this-weekend-well-be-there/index.cs.html` | 178 |
| wp-573 | `content/posts/2018-10-23-vpsadminos-networking-changes-downloadable-iso-backups-and-cgroups/index.cs.html` | 358 |
| wp-576 | `content/posts/2018-11-01-try-cloning-production-vpses-to-the-vpsadminos-test-environment/index.cs.html` | 248 |
| wp-597 | `content/posts/2019-05-02-terraform-provider-for-vpsadmin-automate-infrastructure-management/index.cs.html` | 164 |
| wp-615 | `content/posts/2019-10-29-vpsadminos-development-nfs-on-staging-the-overlay2-driver-for-docker-and-more/index.cs.html` | 1940 |
| wp-621 | `content/posts/2020-01-13-vpsadminos-in-production-in-prague/index.cs.html` | 133 |
| wp-629 | `content/posts/2020-03-03-lets-encrypt-is-revoking-three-million-certificates-check-yours/index.cs.html` | 301 |
| wp-653 | `content/posts/2020-04-02-expanding-meet-vpsfree-cz-with-two-new-servers/index.cs.html` | 277 |
| wp-667 | `content/posts/2020-06-26-datacentre-news-what-were-doing-now-and-planning-next/index.cs.html` | 619 |
| wp-692 | `content/posts/2020-10-12-vpsadmin-updates-default-vps-features-and-oom-reports/index.cs.html` | 352 |
| wp-717 | `content/posts/2021-03-18-we-can-allocate-a-dedicated-64-ipv6-block-to-each-server/index.cs.html` | 148 |
| wp-738 | `content/posts/2022-02-15-vps-start-menu-an-alternative-to-the-grub-bootloader/index.cs.html` | 212 |
| wp-762 | `content/posts/2022-07-13-more-powerful-servers-to-counter-rising-energy-prices/index.cs.html` | 689 |
| wp-773 | `content/posts/2022-10-07-were-upgrading-almost-all-our-hardware-to-save-energy/index.cs.html` | 867 |
| wp-805 | `content/posts/2023-04-24-vpsadmin-news-ssh-host-keys-template-changes-and-cgroups/index.cs.html` | 370 |

**implementer2 partition (42 articles; 13932 title+body words)**

| Stable ID | Czech source path | Body words |
| --- | --- | ---: |
| wp-8 | `content/posts/2014-11-10-we-have-marked-the-centos-7-template-as-stable/index.cs.html` | 60 |
| wp-37 | `content/posts/2015-03-09-we-attended-installfest-2015/index.cs.html` | 717 |
| wp-61 | `content/posts/2015-05-06-distributions-running-at-vpsfree-cz/index.cs.html` | 107 |
| wp-94 | `content/posts/2015-06-09-we-have-three-new-servers-in-our-prague-rack/index.cs.html` | 170 |
| wp-112 | `content/posts/2015-09-14-how-to-repair-a-broken-vps/index.cs.html` | 138 |
| wp-119 | `content/posts/2015-09-21-we-are-going-to-linuxdays-2015-come-and-see-us/index.cs.html` | 125 |
| wp-133 | `content/posts/2015-10-20-we-keep-growing-three-years-in-numbers/index.cs.html` | 74 |
| wp-151 | `content/posts/2015-10-29-we-are-going-to-openalt-come-for-a-coffee/index.cs.html` | 175 |
| wp-174 | `content/posts/2015-11-04-connect-your-servers-with-a-gre-tunnel/index.cs.html` | 227 |
| wp-215 | `content/posts/2015-11-30-launching-support-for-kvm-virtualization/index.cs.html` | 151 |
| wp-229 | `content/posts/2015-12-14-a-christmas-present-weve-doubled-disk-space-to-120-gb/index.cs.html` | 257 |
| wp-253 | `content/posts/2016-01-25-vpsadmin-2-1-0-the-vps-console-in-your-terminal/index.cs.html` | 142 |
| wp-275 | `content/posts/2016-02-22-most-members-join-through-a-personal-recommendation/index.cs.html` | 310 |
| wp-279 | `content/posts/2016-03-08-installfest-went-very-well-take-a-look/index.cs.html` | 244 |
| wp-284 | `content/posts/2016-03-21-download-backups-from-the-command-line/index.cs.html` | 231 |
| wp-308 | `content/posts/2016-04-19-haveapi-fs-mount-your-api-as-a-filesystem/index.cs.html` | 296 |
| wp-316 | `content/posts/2016-04-25-ddos-attacks-most-often-target-teamspeak/index.cs.html` | 494 |
| wp-358 | `content/posts/2016-05-31-weve-added-alpine-linux-3-3-and-slackware-14-1/index.cs.html` | 163 |
| wp-378 | `content/posts/2016-06-22-vpsadmin-has-learned-english/index.cs.html` | 114 |
| wp-381 | `content/posts/2016-06-23-1000/index.cs.html` | 403 |
| wp-406 | `content/posts/2016-09-12-our-first-server-with-ssds-and-512-gb-of-ram/index.cs.html` | 352 |
| wp-433 | `content/posts/2016-09-26-20-gigabits-is-coming-this-year/index.cs.html` | 283 |
| wp-460 | `content/posts/2016-11-10-outages-and-systemd-services-that-fail-to-start/index.cs.html` | 127 |
| wp-474 | `content/posts/2016-11-28-vpsadmin-can-upload-ssh-keys-to-vpses/index.cs.html` | 200 |
| wp-552 | `content/posts/2018-07-09-vpsadminos-status-report-what-we-are-working-on/index.cs.html` | 347 |
| wp-557 | `content/posts/2018-09-03-vpsadminos-installation-updates-deployment-and-networking/index.cs.html` | 335 |
| wp-588 | `content/posts/2019-02-28-a-summary-of-saturdays-annual-meeting-todo/index.cs.html` | 684 |
| wp-610 | `content/posts/2019-06-11-revising-distribution-templates-opensuse-slackware-and-void-linux-on-staging/index.cs.html` | 602 |
| wp-636 | `content/posts/2020-03-16-it-problems-because-of-coronavirus-we-can-help-get-in-touch/index.cs.html` | 182 |
| wp-639 | `content/posts/2020-03-17-were-launching-video-calls-at-meet-vpsfree-cz-free-and-without-registration/index.cs.html` | 207 |
| wp-678 | `content/posts/2020-08-17-memory-management-on-vpsadminos/index.cs.html` | 1400 |
| wp-681 | `content/posts/2020-09-10-choose-your-datacenter-carefully-it-could-be-a-partner-for-life/index.cs.html` | 465 |
| wp-695 | `content/posts/2020-11-24-test-support-for-new-lets-encrypt-certificates-at-test-vpsfree-cz/index.cs.html` | 209 |
| wp-709 | `content/posts/2021-02-18-vps-rescue-mode-boot-a-recovery-operating-system/index.cs.html` | 262 |
| wp-713 | `content/posts/2021-03-08-were-halfway-through-the-vpsadminos-migration-brno-is-next/index.cs.html` | 368 |
| wp-722 | `content/posts/2021-09-20-the-first-vpsadminos-server-in-brno/index.cs.html` | 168 |
| wp-746 | `content/posts/2022-06-03-post-mortem-a-few-words-about-the-outage/index.cs.html` | 994 |
| wp-811 | `content/posts/2023-07-10-automatic-vps-disk-expansion/index.cs.html` | 322 |
| wp-824 | `content/posts/2024-01-15-weve-replaced-lxcfs-with-kernel-virtualization/index.cs.html` | 433 |
| wp-828 | `content/posts/2024-07-31-prometheus-metrics-and-node-load-heatmaps/index.cs.html` | 452 |
| wp-835 | `content/posts/2024-08-19-primary-dns-servers/index.cs.html` | 310 |
| wp-847 | `content/posts/2025-05-16-linux-distributions-users-most-often-switch-to-rocky-linux-and-nixos/index.cs.html` | 357 |

**implementer3 partition (42 articles; 13935 title+body words)**

| Stable ID | Czech source path | Body words |
| --- | --- | ---: |
| wp-15 | `content/posts/2014-11-10-how-we-build-operating-system-templates-for-vpses/index.cs.html` | 209 |
| wp-24 | `content/posts/2014-11-13-backups-at-vpsfree-from-rsync-to-zfs-snapshots/index.cs.html` | 355 |
| wp-51 | `content/posts/2015-04-07-we-supported-ctu-students/index.cs.html` | 1055 |
| wp-84 | `content/posts/2015-06-02-we-supported-volunteer-firefighters-by-hosting-the-dh-cz-portal/index.cs.html` | 277 |
| wp-107 | `content/posts/2015-08-12-nominate-vpsfree-cz-for-kristalova-lupa/index.cs.html` | 73 |
| wp-114 | `content/posts/2015-09-16-we-are-in-the-kristalova-lupa-awards-vote-for-us/index.cs.html` | 78 |
| wp-123 | `content/posts/2015-10-14-we-were-at-linuxdays-2015-photos-and-video/index.cs.html` | 380 |
| wp-191 | `content/posts/2015-11-11-we-brought-coffee-and-logo-stickers-to-openalt/index.cs.html` | 304 |
| wp-69 | `content/posts/2015-11-16-where-are-we-from-far-beyond-prague/index.cs.html` | 179 |
| wp-244 | `content/posts/2016-01-28-how-to-use-256-gb-of-ram-in-a-server/index.cs.html` | 249 |
| wp-264 | `content/posts/2016-02-10-vpsadmin-v2-2-0-setting-maintenance-windows-for-vpses/index.cs.html` | 225 |
| wp-291 | `content/posts/2016-03-23-the-latest-docker-1-10-now-runs-everywhere-here/index.cs.html` | 132 |
| wp-299 | `content/posts/2016-04-18-the-beginnings-of-vpsfree-cz-how-i-gave-a-server-to-a-stranger/index.cs.html` | 87 |
| wp-333 | `content/posts/2016-05-05-new-distributions-devuan-fedora-23-and-opensuse-13-2/index.cs.html` | 256 |
| wp-343 | `content/posts/2016-05-16-why-we-do-not-enable-swap-on-vpses/index.cs.html` | 206 |
| wp-367 | `content/posts/2016-06-13-distributions-a-year-on-debian-ubuntu-and-centos-lead/index.cs.html` | 212 |
| wp-397 | `content/posts/2016-08-16-share-code-snippets-at-paste-vpsfree-cz/index.cs.html` | 113 |
| wp-448 | `content/posts/2016-10-18-haveapi-has-a-new-web-interface/index.cs.html` | 152 |
| wp-450 | `content/posts/2016-10-24-the-dirty-cow-bug-under-openvz/index.cs.html` | 180 |
| wp-455 | `content/posts/2016-10-25-vpsadmin-v2-5-0-private-ip-addresses-and-an-improved-traffic-overview/index.cs.html` | 262 |
| wp-470 | `content/posts/2016-11-24-haveapi-v0-7-blocking-actions/index.cs.html` | 123 |
| wp-481 | `content/posts/2016-12-07-how-did-our-first-vpsfree-hackathon-go/index.cs.html` | 316 |
| wp-490 | `content/posts/2017-02-13-vpsadmin-v2-7-0-payments-emails-and-two-playground-vpses/index.cs.html` | 479 |
| wp-500 | `content/posts/2017-03-29-vpsadmin-2-8-0-improves-outage-reporting/index.cs.html` | 233 |
| wp-506 | `content/posts/2017-05-03-we-support-alpine-linux-and-host-its-main-mirror/index.cs.html` | 460 |
| wp-564 | `content/posts/2018-10-15-our-new-servers-are-fully-patched-against-known-cpu-bugs/index.cs.html` | 161 |
| wp-580 | `content/posts/2019-01-28-our-first-10-years-are-behind-us-with-plenty-more-to-come/index.cs.html` | 602 |
| wp-592 | `content/posts/2019-03-01-were-heading-to-installfest-come-for-coffee-and-a-new-switch/index.cs.html` | 141 |
| wp-601 | `content/posts/2019-05-22-two-factor-login-to-vpsadmin-for-better-security/index.cs.html` | 162 |
| wp-606 | `content/posts/2019-06-04-six-months-of-vpsadminos-development-closer-to-launching-a-production-server/index.cs.html` | 1300 |
| wp-625 | `content/posts/2020-02-28-migrating-our-infrastructure-to-20-gigabits/index.cs.html` | 448 |
| wp-646 | `content/posts/2020-03-18-the-first-day-of-video-calls-at-meet-vpsfree-cz/index.cs.html` | 323 |
| wp-651 | `content/posts/2020-03-30-what-next-for-meet-vpsfree-cz-new-software-and-hardware/index.cs.html` | 291 |
| wp-662 | `content/posts/2020-06-04-lets-move-to-ipv6-together-we-need-it/index.cs.html` | 373 |
| wp-702 | `content/posts/2020-12-09-linux-distributions-ubuntu-grows-faster-than-debian-nixos-gains-popularity/index.cs.html` | 316 |
| wp-730 | `content/posts/2021-12-13-migrate-to-vpsadminos-time-for-current-virtualization-and-a-new-kernel/index.cs.html` | 333 |
| wp-759 | `content/posts/2022-06-08-infrastructure-status-at-status-vpsf-cz/index.cs.html` | 169 |
| wp-792 | `content/posts/2023-01-05-linux-distributions-rocky-linux-grows-quickly-slackware-disappears/index.cs.html` | 351 |
| wp-807 | `content/posts/2023-04-27-devcgprog-a-utility-for-configuring-the-cgroupv2-devices-controller/index.cs.html` | 859 |
| wp-815 | `content/posts/2023-12-19-we-have-discourse-come-and-talk-mailing-lists-have-had-their-day/index.cs.html` | 413 |
| wp-821 | `content/posts/2023-12-30-single-sign-on-in-vpsadmin/index.cs.html` | 657 |
| wp-841 | `content/posts/2025-03-03-two-factor-login-with-passkeys/index.cs.html` | 134 |


#### P37 receiver generation binding — sufficient request-scoped fix proposal

**Status / ownership.** Source investigation and design only; lead accepts release
and assigns one free retained implementer (owner3 is the natural CONFIG owner).
P36 article publication remains independent. Baseline CONFIG is clean
25b2f5f8fad767474fa8180fa0b63b1b3e7278e4. No source/runtime action, check,
build, SSH or network call was performed for this design. The later user/lead
steering supersedes the initial automatic-restart hypothesis: preserve the
in-flight authority check, scope its lifetime to one admitted upload.

**Cause and purpose.** tools/blog-upload.py:162 creates one Publication at
process startup; Handler:112/130 reuses it for every request. Publication in
tools/blog-static-release.py:754 captures /run/current-system once; identity():773
rejects a different selected generation. A caught Paused becomes HTTP503 while
the service remains healthy, so Restart=on-failure cannot repair this condition.
The retained read-only/restart receipts show PID40101 predating the system
transition, current/control both yyf2 with policy6c314, then PID43147 and unchanged
selection/control/floor after the normal restart. The actual Python heap and
first failed HTTP status were not captured; source, PID timing and successful
exact-package retry establish the failure mechanism without pretending those
missing observations were measured. See the existing generation-identity note
and p36-receiver-identity-readonly.json / p36-receiver-restart-result.json.

Pinned nixpkgs718f670, local source z40fynbhnw0d06q05mw2mznn49h1y9pk-source,
nixos/lib/systemd-unit-options.nix:315,548 restarts on changed triggers/unit
(default restartIfChanged=true), not arbitrary system generation changes.
blog-upload.nix:38 has no generation trigger. activation-script.nix:74–79 sets
/run/current-system after activation snippets. This explains survival with
unchanged helper/unit/policy; no synthetic self-toplevel dependency, direct
activation restart, path watcher or new service is needed for the chosen fix.

The useful guard is operation continuity, not a new authentication boundary:
request A can receive its body or stage outside the publication lock while root
pauses, switches from system A to B under the same policy, verifies and resumes
B. Policy equality plus CURRENT control alone would then admit A's already
underway work. A request-local generation snapshot rejects it at the next
existing authority check. The lifetime-wide snapshot wrongly rejects even NEW
requests admitted after B is resumed. Preserve the snapshot check itself and
all policy/control checks. It is not a monotonic history detector: an unobserved
A→B→A or same-generation pause/resume is not newly distinguished by this fix;
do not claim otherwise or introduce a new epoch/schema for this package.

**Exact three-file boundary / interface.**

- tools/blog-upload.py: Server stores a small Publication factory, not a live
  process-wide operation. Production passes the existing release.Publication
  constructor; retain startup policy validation. After successful authentication
  and acquisition of the existing busy slot, create ONE local Publication,
  call allowed(), then read/hash the body and call upload() on THAT SAME object.
  Capture precedes body receipt, not merely upload()/staging/commit. Do not
  recreate or refresh it at later checks, mutate a shared started_system, or
  resolve the active helper dynamically. Keep fixed compiled policy, service
  UID, credential handling, endpoint/HMAC/framing, limits, serial busy handling,
  error handling and durable 200 response contract. A tiny injectable callable
  permits the existing offline handler fixtures; it is not a plugin API.
- tests/blog-upload.py: adapt existing handler fixture to the factory and add
  the concrete same-server transition regressions below. Use existing fixture
  paths/real Publication implementation, not a duplicate model of authority.
- docs/operations/blog-static.md: describe per-upload capture, normal upgrade
  pause→switch→verify→explicit resume, why an in-flight request can fail/retry,
  and why an unchanged surviving receiver now accepts subsequent requests.
  Retain the policy-change refusal, pre-switch gate and older-version manual
  restart diagnosis. No change to tools/blog-static-release.py, module options,
  pinned inputs, BLOG client, workflow, schemas, database or forum is needed.

**Acceptance / focused quick verification.** Existing offline fixtures should
exercise the actual Handler and real Publication with one persistent server
state/factory and synthetic credential, without opening sockets:

1. Admit/publish under A; root pause, select B with unchanged policy, explicitly
   resume through a fresh B helper; a NEW request on the SAME server succeeds
   and its receipt binds B, without resetting server state or restarting it.
2. A request captures A before its body read; during the read complete
   pause→B→resume. Its later upload rejects with503 and leaves current receipt,
   pointer and ordering floor unchanged. A subsequent identical request is a new
   admission and can succeed under B. This catches too-late capture and reuse.
3. Change/resume generation during staging: retain the original request object,
   reject before pointer/floor advancement. Preserve existing final-barrier
   generation and paused-stage cases; cover policy replacement even for a fresh
   request so an old compiled helper cannot adopt a new active policy.
4. Paused/mismatched control still refuses; invalid auth and busy requests never
   create an operation/read a body. Retain identical retry, lost-response,
   ordering, rollback and crash-reconciliation coverage already present.

Run the two existing Python suites (tests/blog-upload.py and
 tests/blog-static-release.py) in the declared environment, ordinary formatting/
hooks and owned diff inspection. Keep quick tests offline and bounded; no new
VM/browser/service framework. Commit the complete three-file package, obtain
independent final review, then run the required affected int.blog native build
through the ordinary watcher. Existing module-mode evaluation is useful to
confirm generated credential/confinement and source-package composition; no
proxy/full-size upload rerun is justified by this request-lifetime change.
Native evidence must bind final source/input/system and generated unit, not
reuse the old yyf2 identity. Source tests prove the handler lifetime; native
build proves packaging, neither alone proves a live authorized transition.

**Compatibility / rollout / recovery.** Schema2 control/receipts and retained
schema1 content are unchanged, as are floor, current selection, locks and
reconciliation. The existing implementation digest includes blog-upload.py,
so this first corrected deployment changes policy/source package/ExecStart and
normal NixOS unit-change restart applies. Root maintenance remains mandatory;
never auto-resume or auto-adopt a changed policy. Build/copy/dry preparation and
any later deployment require the normal separate lead release/claim; this brief
provides none. When authorized, record selected system, PID, policy/control,
current receipt/floor and no pending transaction before/after the switch;
explicitly resume the verified new system and observe the next authorized
ordinary upload. Do not publish artificial content merely to test restart.
Future same-policy system transitions can leave the process running: resumed
B is accepted by fresh requests, underway A stays rejected. Helper/policy
changes still require the selected normal unit; a stale helper fails closed.
Rollback to compatible old code preserves state but restores the old lifetime
limitation: verify/restart that normal receiver after selection if necessary,
then explicitly resume; never reset floor, remove guards or alter credentials.
Retain previous static release, rooted systems, receipts and all recovery data.

**Release conclusion.** Relevant contracts are settled; no essential open fact
blocks this narrow implementation after lead acceptance. Actual checks and
runtime proof remain future evidence. Architect returns the append window;
lead owns package allocation, state/prose and integration/deployment authority.


#### P37 SUPERSEDING final brief — remove redundant cached generation equality

**Accepted final contract.** This supersedes the request-scoped factory proposal
at design.md:5874, including its in-flight cancellation rationale, corresponding
fixtures and routine old-version restart instruction. That earlier text is
retained as investigation history, not the implementation contract. Lead accepted
the necessity reassessment: no concrete harmful state was identified that the
cached generation comparison uniquely prevents after root explicitly resumes the
new generation under the same immutable implementation-bound policy. Same-system
pause/resume and an unobserved A→B→A already disprove a general cancellation claim.
No factory, generation epoch or automatic restart mechanism is required.

**Owner / exact three-file deliverable.** Owner0 revises the unmerged bf37
package after retaining its original proof reference; lead releases the revision.
Independent review and native verification have not started. Against original
CONFIG25b2, the final change is limited to:

- tools/blog-static-release.py: remove only Publication.__init__'s
  started_system cache and identity()'s equality test against that cache. Keep
  selected-system strict resolution/is_dir validation and the returned CURRENT
  policy_sha256/system identity. Preserve compiled-policy/active-policy matching,
  schema/ownership checks, root-owned control.system and control.policy_sha256
  equality, paused state, pre-switch gate, transaction/staging locks, admission
  rechecks, reconciliation, immutable assets, order/floor and durable response.
- tests/blog-upload.py: focused behavior coverage below using the existing actual
  Handler/Publication fixtures. No factory API or duplicate authority model.
- docs/operations/blog-static.md: describe the corrected current contract and
  supported pause→switch→verify→explicit resume sequence. Pause blocks commits
  while paused; it does not permanently cancel admitted requests after explicit
  resume. Remove the former unconditional claim that a staging request can never
  commit afterward. Keep historical manual-restart recovery in the existing
  session note, not as a routine step in the new guide. Policy/helper changes
  still require the ordinary selected unit update; an old compiled helper cannot
  adopt a changed active policy. Credential rotation retains its existing pause
  and normal credential/unit procedure. No new epoch or cancellation promise.

Restore tools/blog-upload.py exactly to the original CONFIG25b2 bytes; it must
have no final delta. Server continues to hold one Publication. No module/options,
protocol, schema, pinned input, BLOG workflow/client or publication scope changes.

**Why remaining checks suffice within the supported contract.** allowed()
checks current policy/system against root's explicit resumed control, including
under the transaction lock in upload(); _switch() checks authority again before
creating the pending/pointer transaction. With unchanged policy and resumed B,
conforming work admitted under A may finish under B. Order/floor guards still
reject superseded content and the resulting receipt records B. A transition to B
without matching explicit resume still refuses. Changed active policy still
rejects the old compiled helper. No guard is removed from these paths apart from
the redundant historical process-generation comparison.

**Acceptance / evidence.** On one retained Server/Publication, verify A→B with
unchanged policy rejects while paused or while control remains bound to A, then
accepts NEW requests after a fresh root helper explicitly resumes B. Also verify
requests spanning body receipt and staging can succeed after that explicit
resume, with correct B receipt, selected content and monotonic ordering floor.
Retain supersession/conflicting retry assertions, stale-policy rejection even
after resume, and the existing cross-generation-without-resume refusal. Keep
existing lock, crash/reconciliation, rollback and paused-stage cases. No new
sockets, service or test framework is needed. Reconcile obsolete factory tests
and claimed cancellation behavior; do not weaken still-applicable assertions.
Run focused cases and existing tests/blog-upload.py plus
 tests/blog-static-release.py in the declared environment, ordinary hooks and
owned diff checks. Preserve bf37 evidence under its actual identity; new results
must identify the revised final head. Then normal commit/final independent review
precedes the affected int.blog native build. No test, native or runtime action
is authorized to the architect by this addendum.

**Compatibility / release boundary.** Existing control/receipt schemas and
content/recovery formats stay unchanged. Modifying the helper changes the
implementation-bound policy/source/ExecStart, so the first corrected deployment
uses the normal unit update under root maintenance, followed by verification and
explicit resume. Subsequent same-policy system upgrades need no receiver restart
solely because the system path changed. Preserve selected release, maximum floor,
receipts, rooted systems and recovery data. Older software remains readable-state
compatible but has its historical cached-generation limitation; its incident
workaround remains in the existing note. No runtime, merge, pin or native action
is released here. P36 delivery stays independent. Relevant source contract is
settled; lead owns release, source allocation and later operational authority.
Architect returns the append window after reporting this exact anchor.
