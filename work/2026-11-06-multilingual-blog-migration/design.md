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
