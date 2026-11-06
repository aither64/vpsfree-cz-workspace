# 2026-11-06-multilingual-blog-migration

## Goal

I'd like to migrate https://blog.vpsfree.cz from wordpress to a static generator. We should preserve the design, it doesn't have to be 1:1 of course. We must however preserve all content (articles, authors and comments). Existing comments can be added statically, future comments should be provided by discourse that runs at https://discourse.vpsfree.cz. I assume this is supported by discourse? How would it be interconnected? We should also preserve existing article URLs. Both blog and discourse are configured using vpsfree-cz-configuration. I'll be able to give you access to the blog container so that you can extract data. In addition, I would like the blog to support localization in English and Czech, so all existing articles will have to be translated to English. Suggest what static website generator would be appropriate for our usecase and create a plan to implement it. Ask if something is unclear or I forgot to mention it.

## Affected repositories

- User-created `git@github.com:vpsfreecz/blog.git` for content, templates, assets
  and build contract. Remote was initially empty; user approved one-time main initialization from
  reviewed0354dac. All subsequent work stays on the feature branch; no merges.
- `vpsfree-cz-configuration`: existing blog hosting, static artifact selection and
  Discourse embedding configuration. Inspect canonical refs only during planning.
- This workspace: session tracking plus user-requested minimal blog entry in
  docs/agent-instructions/projects.md; feature edit uses an isolated workspace
  worktree. User originally named vpsfreecz/dev-workspace then confirmed the
  workspace project map after receiving its exact link; no duplicate extension
  project list is requested.

## Approach

Planning is accepted and the user has supplied root container access, the blog
repository, an internal DNS request and the English domain. Proceed with source
inventory, repository preparation/scaffolding under the accepted design brief,
and a minimal internal DNS feature change. User additionally requires standalone
agent/human author instructions inside the blog clone and a VPN preview on
port4567. Add those as separate small delivery milestones. Production cutover, forum writes
and further default-branch integration remain prohibited until user approval. The design owner maintains
[design.md](design.md).

Plan agent-assisted publishing as the expected workflow: repository instructions
and a focused authoring skill covering drafts, technical fact verification,
translations, checks and previews. Provide direct documented commands for human
authors too. Previews must not create or modify production Discourse topics;
future session-owned preview servers use `dev-session service run`.

Recommend Hugo on the verified multilingual and static-hosting evidence. Preserve
Czech article paths exactly at `https://blog.vpsfree.cz/`; English uses
`https://blog.vpsfree.org/` at the host root, replacing the initial `/en/` proposal.
Use durable WordPress IDs for provenance and paired translations. Revise the
discussion recommendation to native automatic URL-based Discourse embedding:
both language versions pass one stable original article URL as discussion
identity, separate from their language-specific SEO canonicals. Loading the
production embed can create the topic before anyone replies. Previews disable
production embeds. Archive original public comments statically.

User follow-up asks for zero manual forum work and site-only deployment on push.
Recommend a GitHub Actions publication pipeline independent of system deployment:
build/check Hugo in the pinned environment, transfer a versioned artifact to the
existing VPS, validate it and atomically select it for nginx. confctl manages the
hosting infrastructure and deployment permissions; it does not need to run for
each article. Runner access to the internal backend is an implementation gate;
use VPS-side artifact retrieval if a suitable restricted upload route is absent.

Use the supplied root SSH access for authoritative read-only source inventory;
public samples cannot establish completeness. Preserve source backups
privately in durable operator-managed storage independent of disposable session
artifacts, and generate a public-only projection suitable for Git. Rehearse a
repeatable migration, compare inventories, review English translations, validate
the candidate and prepare reversible deployment before any production switch.

## Decisions

Confirmed by the user in this conversation on 2026-11-06:

- Czech and English versions share one Discourse discussion per article.
- Future commenters use Discourse's existing account/login/registration rules.
- Future article publication should need no manual Discourse topic provisioning.
- Git/Markdown publishing is suitable; a browser editor is unnecessary.
- AI translation drafts are acceptable with human review before publication.
- Translations, particularly articles by Jakub Skokan/aither, should follow the
  language of his earlier announcements. The user permits adopting that general
  style across authors; preserve each author's attribution, facts and viewpoint.
  Reference collections:
  https://lists.vpsfree.cz/mailman3/hyperkitty/list/news-list@lists.vpsfree.cz/latest
  and https://discourse.vpsfree.cz/c/announcements/5 .
- Historical reader comments stay in their original language.
- Future articles will normally be written with agents; authoring instructions
  and skills should streamline that workflow and remain human-friendly.
- An easy local preview server is required.
- A dedicated content Git repository is acceptable, and has now been created.
- Standalone root AGENTS.md, local author guide and optional readable skill must
  let generic agents/humans work from an ordinary clone without this coordination
  workspace. Git permissions/protected publication branch govern publishing.
- When this batch is ready, leave a registered preview reachable through VPN on
  aitherdev.int.vpsfree.cz:4567. No firewall change requested. Real draft preview
  is the default; isolated synthetic fixtures are an explicit demo option.
- The new static website will run on the current blog VPS/container.
- User explicitly waives a formal content/comment freeze because posting is
  rare. Use the captured snapshot and one brief pre-switch check for deltas;
  refresh export only if changes are found. No service stop/read-only WP change.
- The bot may also be updated if needed. User subsequently confirmed feed
  subscriber continuity matters: preserve `/feed/` and stable existing item
  identities. An English feed can be separate.

Hugo and the blog repository are settled. Czech remains on `blog.vpsfree.cz`;
English uses `blog.vpsfree.org`, with language-specific canonicals/hreflang and
shared Czech discussion identities. Future public .org DNS, TLS/proxy and
cross-site forum display/login checks are required. Add `blog.int.vpsfree.cz`
A record for the verified container address to the internal zone. Blog category
and translation-review ownership remain to settle. Default integration and
production blog cutover have not been approved.

## Compatibility and deployment

- Preserve published article URLs, author attribution, original dates, content,
  media and historical comment IDs/threading. Inventory pages, archives, feeds,
  attachments, query URLs and redirects rather than assuming article paths are
  the only public contract.
- Preserve unpublished/private/spam content in private backups without publishing
  it. Do not publish commenter email/IP data, credentials or database dumps.
- Native auto-creation uses one stable production discussion URL shared by both
  languages. It occurs when the production comments embed loads, not only when
  someone posts. Site builds/previews must not activate production embeds, and
  the installed forum must be tested for duplicate-free shared URL behavior.
- Recommend a dedicated public Blog category, selected once on the embedding
  host record. Restrict normal automatic article imports to exact
  `blog.vpsfree.cz` and anchored published-article paths, with narrow category
  creation/reply permissions under the existing account rules. The native
  restriction validates the article source URL, not an authenticated caller:
  anyone may trigger import of an allowed public article. Do not promise Origin
  or Referer is authentication. Validate source/redirect handling on the actual
  installed forum before enabling; the current upstream review is bounded.
- Site releases live in versioned persistent directories with an atomic current
  pointer and a retained previous artifact. CI uses deployment-only permissions;
  protected publication-branch pushes trigger releases, PR checks get no deploy
  secrets. Serialize activation and reject stale releases. Keep artifact/source
  identities in release receipts. System-generation rollback and content-release
  rollback are separate; preserve both recovery contracts and asset compatibility.
- Prepare static serving on the same VPS alongside retained WordPress data.
  Keep the public TLS proxy and proxy-only backend network boundary. Preserve
  `/feed/` for feed subscribers; updating the existing IRC bot's configuration
  is explicitly permitted where needed. Verify feed GUID/polling behavior
  to avoid re-announcing the archive. Inventory verified original CZ identifiers
  https://blog.vpsfree.cz/?p=<id> with isPermaLink=false; preserve them exactly.
  English /feed/ uses stable language-specific URNs, original publication dates
  and reviewed variants only. Replace WordPress-specific health
  checks with static-serving checks. Do the brief pre-switch delta check,
  refresh export only if necessary, validate and switch atomically. Rollback
  retains new Discourse replies and discussion identities; preserve access to
  those replies without requiring them to be imported back into WordPress.
- No cross-service schema/protocol changes are proposed; no node-wide upgrade is
  expected. Nix module/options and deployed versions remain to verify.

## Documentation

### Translation voice brief

Lead inspected the supplied mailing-list collection and aither's bilingual
[primary DNS announcement](https://discourse.vpsfree.cz/t/primarni-dns-servery-primary-dns-servers/258)
and [initial VPS configuration announcement](https://discourse.vpsfree.cz/t/prvotni-konfigurace-vps-skriptem-cloud-init-a-nixos-initial-vps-configuration-with-script-cloud-init-and-nixos/317).
The general category also contains other authors; identify bylines before using
a post as an aither-specific sample. The mailing-list Guix announcement adds a
longer personal technical example. This is a small evidence sample, not a full
voice analysis of every article.

For the future authoring instructions/skill, use direct, practical English with
familiar technical terms and short purposeful paragraphs. Lead with what is
available or what happened, then explain use, reasons and concrete limitations.
Use examples and headings when the source needs them. Address the reader
naturally; retain first-person experience and occasional informal asides where
they exist in the source. Avoid promotional language, artificial enthusiasm and
generic filler. Match the voice without reproducing spelling mistakes or
awkward English. Do not add opinions, jokes, personal experiences, promises or
new technical claims to imitate personality. Preserve chronology, uncertainty,
authorship, commands and links. Leave the original Czech archive unchanged.
Human review checks both source fidelity and voice before publication.

The standalone authoring skill and guide now carry this guidance; later source
reconciliation documents native imported HTML alongside new Markdown.
Apply the vpsfree-user-facing-writing workflow after technical facts are settled,
using the supplied author samples to calibrate the prose.

Readers: blog maintainers, translators and operators. Session design and state
hold this proposal and evidence. Future source repository docs should explain
authoring/translations/import provenance; configuration repository docs should
own repeatable deployment and recovery instructions.

Use the dev-session-documentation and dev-session-handoff skills. Planning and
investigation alone do not trigger mandatory final change review. Implemented
code/configuration and completed substantive operating docs will require that
review after commits and quick checks, before long integration tests.

## Testing plan

Initial planning verified primary Hugo/Discourse/WordPress documentation and
bounded public/configuration samples. Accepted private snapshot evidence later
established the complete corpus; final source checks/review are in state.md.
Installed forum/runtime compatibility remains separately unverified.

For implementation, require ID/count/content and media reconciliation, all old
article URL checks and comment anchors, local links/assets, localized metadata
and translation completeness, representative mobile/desktop rendering, and a
staged Discourse lifecycle test proving shared topic identity and reply behavior.
Rehearse cutover/rollback, use the brief delta check agreed with the user, and
preserve post-cutover forum replies.

## Current implementation milestone after visual feedback

User rejected the generic scaffold. Rebuild from actual original design: navy
sidebar#16273f, serverphoto background#1f3959,230x90logo, Arial/Verdana,
1200desktopcanvas/300sidebar/900main, centered48pxheadings and measuredmobile
menu/layout. D6contains exact metrics and actual screenshots. Theme asset/code
provenance retained; do not invent font/media license claims.

Import snapshot locally to native Hugo index.cs.html bundles preserving visible
content, rawbody provenance hashes, code/media/moreanchors,125routes/GUIDs,6authors,
107approvedcomments/43threads,569uploads bytes andtaxonomies. Private metadata
remains outsideGit. English translation batches62/63articles are proposed by
wordcount were released against a stable sanitizedCSsource/manifest. All125
complete English drafts are now committed and source-hash/raw-code checked,
with main prose checks and independent source review complete. They remain
drafts awaiting human review, visible in preview with a clear label.

Blog initial main0354dac is user-authorized and verified; no furtherdefault
updates/merges and no transition/currentblog changes until separate approval.


## Reviewed source preparation and remaining activation gates

Recognizable original theme, complete public Czech archive/comments/assets,
125 English drafts, standalone author instructions, local/VPN previews and
production-disabled native Discourse rendering are implemented. Reviewed blog
feature head is aeed3a018d895b797e1b8d9b2863dd20c0dec8e0; source checks and
independent high-risk four-lane review found no issues in the source-preparation
boundary. Translation human approval and user visual acceptance remain distinct.

The independent release source candidate uses Actions builds and target-side
artifact acquisition, preserving current WordPress80 and a separate default-off
static8080 module. Artifacts require clean exact source identity, complete payload
hashes and independently verified trusted workflow/API identity. Current/previous
archives/assets/receipts remain locally retained; expired current-SHA artifacts
require the same-source trusted rebuild, never an older fallback or a VPS build.

Automatic pull/activation/rollback remains unavailable pending an implemented,
verified machine-coordination admission contract. The source CLI refuses and
timer enablement fails evaluation; filesystem fixtures do not replace ownership.
Current protected-branch/workflow credentials, outbound artifact reachability,
retained backup and actual forum/topic/account/frame behavior remain operator
gates. No forum setup, public.org DNS/TLS/proxy change, queryalias cutover or
transition is executed here. The user forbids merges until the last step and
requires explicit approval before touching the current blog.
