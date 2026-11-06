# 2026-11-06-multilingual-blog-migration

## Goal

I'd like to migrate https://blog.vpsfree.cz from wordpress to a static generator. We should preserve the design, it doesn't have to be 1:1 of course. We must however preserve all content (articles, authors and comments). Existing comments can be added statically, future comments should be provided by discourse that runs at https://discourse.vpsfree.cz. I assume this is supported by discourse? How would it be interconnected? We should also preserve existing article URLs. Both blog and discourse are configured using vpsfree-cz-configuration. I'll be able to give you access to the blog container so that you can extract data. In addition, I would like the blog to support localization in English and Czech, so all existing articles will have to be translated to English. Suggest what static website generator would be appropriate for our usecase and create a plan to implement it. Ask if something is unclear or I forgot to mention it.

## Affected repositories

- A dedicated blog source/content repository, name/location to agree; proposed
  `vpsfreecz/blog`. Keep templates/build contract with content unless a concrete
  need for separate repositories appears.
- `vpsfree-cz-configuration`: existing blog hosting, static artifact selection and
  Discourse embedding configuration. Inspect canonical refs only during planning.
- This workspace: session planning and evidence only. No project worktrees or
  feature branches are required for the current request.

## Approach

This request covers investigation, generator selection and an implementation
proposal. Implementation, extraction requiring private access, translation,
forum writes and deployment follow later direction. The design owner records
the proposed implementation and acceptance checks in [design.md](design.md).

Plan agent-assisted publishing as the expected workflow: repository instructions
and a focused authoring skill covering drafts, technical fact verification,
translations, checks and previews. Provide direct documented commands for human
authors too. Previews must not create or modify production Discourse topics;
future session-owned preview servers use `dev-session service run`.

Recommend Hugo on the verified multilingual and static-hosting evidence. Preserve
Czech article paths exactly and place English counterparts under `/en/`.
Use durable WordPress IDs for provenance, paired translations and a shared
Discourse topic identity. Archive original public comments statically.

Inventory the authoritative database and files after container access is
provided; public samples cannot establish completeness. Preserve source backups
privately in durable operator-managed storage independent of disposable session
artifacts, and generate a public-only projection suitable for Git. Rehearse a
repeatable migration, compare inventories, review English translations, validate
the candidate and prepare reversible deployment before any production switch.

## Decisions

Confirmed by the user in this conversation on 2026-11-06:

- Czech and English versions share one Discourse discussion per article.
- Future commenters use Discourse's existing account/login/registration rules.
- Git/Markdown publishing is suitable; a browser editor is unnecessary.
- AI translation drafts are acceptable with human review before publication.
- Historical reader comments stay in their original language.
- Future articles will normally be written with agents; authoring instructions
  and skills should streamline that workflow and remain human-friendly.
- An easy local preview server is required.
- A dedicated content Git repository is acceptable.
- The new static website will run on the current blog VPS/container.
- The bot may also be updated if needed. User subsequently confirmed feed
  subscriber continuity matters: preserve `/feed/` and stable existing item
  identities. An English feed can be separate.

The recommendation is Hugo. Proposed details for implementation are Czech at
the existing paths with English under `/en/`, a dedicated blog repository and a
public Discourse blog category. Repository name, category and translation-review
ownership can be settled before their dependent steps. No integration or
deployment approval has been given.

## Compatibility and deployment

- Preserve published article URLs, author attribution, original dates, content,
  media and historical comment IDs/threading. Inventory pages, archives, feeds,
  attachments, query URLs and redirects rather than assuming article paths are
  the only public contract.
- Preserve unpublished/private/spam content in private backups without publishing
  it. Do not publish commenter email/IP data, credentials or database dumps.
- Explicit shared Discourse topic IDs avoid per-language topic duplication.
  Topic provisioning is an intentional publication step, separate from static
  builds and previews; runtime behavior must be tested on the installed version.
- Prepare static serving on the same VPS alongside retained WordPress data.
  Keep the public TLS proxy and proxy-only backend network boundary. Preserve
  `/feed/` for feed subscribers; updating the existing IRC bot's configuration
  is explicitly permitted where needed. Verify feed GUID/polling behavior
  to avoid re-announcing the archive. Replace WordPress-specific health
  checks with static-serving checks. Freeze old writes,
  take the final export, validate and switch atomically. Rollback must retain
  new Discourse replies and the article/topic mapping; WordPress rollback must
  not silently resume a competing comment stream.
- No cross-service schema/protocol changes are proposed; no node-wide upgrade is
  expected. Nix module/options and deployed versions remain to verify.

## Documentation

Readers: blog maintainers, translators and operators. Session design and state
hold this proposal and evidence. Future source repository docs should explain
authoring/translations/import provenance; configuration repository docs should
own repeatable deployment and recovery instructions.

Use the dev-session-documentation and dev-session-handoff skills. Planning and
investigation alone do not trigger mandatory final change review. Implemented
code/configuration and completed substantive operating docs will require that
review after commits and quick checks, before long integration tests.

## Testing plan

For this planning request, verify primary Hugo/Discourse/WordPress documentation
and bounded public/configuration samples; record the limits of that evidence.
Do not claim a content inventory or runtime compatibility without private access.

For implementation, require ID/count/content and media reconciliation, all old
article URL checks and comment anchors, local links/assets, localized metadata
and translation completeness, representative mobile/desktop rendering, and a
staged Discourse lifecycle test proving shared topic identity and reply behavior.
Rehearse final export/cutover/rollback and preserve post-cutover forum replies.
