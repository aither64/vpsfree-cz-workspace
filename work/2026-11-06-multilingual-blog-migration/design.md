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
