# 2026-07-10-kb-czech-fixes

## Goal

Bring the Czech knowledge base in line with the Czech vpsAdmin interface.
Replace stale English menu entries, form titles, field labels, action names,
error text, and vpsAdmin-specific terminology with the exact Czech wording
shipped by vpsAdmin. Recreate every vpsAdmin-related screenshot represented in
the affected Czech documentation, including screenshots whose English version
is merely old rather than mistranslated. Stage complete pages and their Czech
screenshots in the draft namespace for review before any production-page or
production-media write.

## Affected repositories

- Coordination workspace, for this plan, audit, DokuWiki tooling, local
  previews, draft staging, and state.
- `vpsadmin-kb-captures`, a new standalone screenshot inventory and capture
  repository. Its initiative worktree is at
  `worktrees/2026-07-10-kb-czech-fixes/vpsadmin-kb-captures` and its feature
  branch is `2026-07-10-kb-czech-fixes`.
- `vpsadmin` is read-only source material. The authoritative baseline is
  `origin/master` at `299147166ecb8459c712ed8a5c4dd14f673663fc`.
- `haveapi` is read-only background material. No framework wording was needed
  beyond the vpsAdmin catalogs exposed to users.
- `kb.vpsfree.cz` is the eventual documentation target. This investigation
  made no wiki writes.

The detailed replacement and screenshot inventory is in
`work/2026-07-10-kb-czech-fixes/kb-label-audit.md`.

## Approach

### Inventory and terminology authority

1. Enumerate all accessible pages recursively with the authenticated,
   read-only DokuWiki API (`core.listPages`, depth 10), then read every page.
2. Match likely UI text against both current vpsAdmin localization sources:
   - WebUI gettext catalog:
     `webui/lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.po`;
   - API locale catalogs:
     `api/lib/vpsadmin/api/locales/{en,cs}.yml`;
   - Czech terminology guidance: `doc/i18n-cs.md`.
3. Review unmatched but UI-shaped text manually. This catches renamed labels
   such as old `Parent`/`Create mount`, obsolete error wording, transaction
   terminology, and multi-line navigation paths.
4. Inventory images across all 116 pages, not only pages with stale text.
   Recreate all current vpsAdmin/WebUI, console, and vpsAdmin CLI screenshots
   used by the documentation. Static icons, logos, third-party interfaces, and
   non-vpsAdmin illustrations are excluded.

This expands the draft set from 28 text-affected pages to 30 pages: the two
additional screenshot-only pages are `navody:vps:konzole` and
`navody:vps:kvm-openrc`.

### Draft and media naming

Every source page gets a complete draft copy at:

```text
drafts:2026-07-10-kb-czech-fixes:<source-page-id>
```

For example:

```text
drafts:2026-07-10-kb-czech-fixes:navody:vps:datasety
```

Draft media uses new, create-only IDs:

```text
drafts:2026-07-10-kb-czech-fixes:media:vpsadmin:<topic>:<lang>:<view>.png
```

The eventual permanent ID, written only after non-draft approval, is:

```text
screenshots:vpsadmin:<topic>:<lang>:<view>.png
```

Example Czech/English variants:

```text
drafts:2026-07-10-kb-czech-fixes:media:vpsadmin:datasets:cs:dataset-list.png
screenshots:vpsadmin:datasets:cs:dataset-list.png
screenshots:vpsadmin:datasets:en:dataset-list.png
```

Rules:

- `<lang>` is the stable ISO 639-1 code (`cs`, later `en`), not a runtime
  locale such as `cs_CZ.utf8`.
- `<topic>` is a language-neutral functional area such as `datasets`,
  `ssh-keys`, `networking`, `user-sessions`, or `rescue-mode`; it is not tied
  to a Czech or English page slug.
- `<view>` is a stable semantic description of the UI state rather than a copy
  of an old filename. Scenario code defines execution/display order; order is
  not part of the asset identity.
- Filenames contain no revision counters. Git versions the generated PNG and
  DokuWiki versions the canonical media ID, so a refreshed screenshot does not
  require edits to every page that embeds it. The initial migration still uses
  new media IDs and never overwrites a legacy screenshot.
- Reused screenshots have one owning topic and one media ID. Pages such as
  `informace:novacci` and `navody:vps:sprava` reference the same new SSH-key
  assets instead of uploading duplicates.
- UI screenshots are normalized to PNG. Existing JPEG or PNG media remains
  untouched and available through page history.

Maintain the long-lived inventory as `captures.json` in
`vpsadmin-kb-captures`. It records the legacy media ID, draft media ID,
eventual permanent ID, language, functional topic, source page(s), vpsAdmin
commit, viewport, scenario/checkpoint, driver, fixtures, dimensions, SHA-256,
capture provenance, and review status. The initiative-local
`screenshot-manifest.yml` remains the KB migration map used to build and stage
this draft set.

### Standalone capture repository

`vpsadmin-kb-captures` must be independently runnable. It owns:

- a Nix lock that pins the exact vpsAdmin/vpsAdminOS sources;
- its complete single-node development-cluster definition and seed config;
- `bin/devcluster` lifecycle tooling and ignored repository-local runtime
  state;
- all fixture preparation, browser, console, CLI, capture, and validation
  code.

It must not discover or call a coordination checkout, use an external worktree
layout, or require another repository's helper scripts at runtime. The
coordination repository consumes its manifest and generated artifacts only for
the separate DokuWiki staging workflow.

### Preparation

1. Fetch every affected source page again immediately before editing and fail
   on revision drift instead of overwriting concurrent wiki changes.
2. Prepare one local DokuWiki preview file for each of the 30 draft pages under
   `work/2026-07-10-kb-czech-fixes/kb-previews/`.
3. Apply the page-level replacements from the audit, preserving intentional
   untranslated terms such as `User data`, `Mount`, `Live monitor`, `NAS`,
   `VPS`, `Hostname`, and `Playground`.
4. Recapture the 60 unique vpsAdmin-related screenshots (63 page references)
   through `vpsadmin-kb-captures`. Eight scenarios prepare idempotent fixtures
   and drive the Czech WebUI, the live remote-console iframe, and the real
   `vpsfreectl network top` TUI. Use a non-privileged test account, documentation
   IP ranges, masked TOTP data, and normalized dynamic values. Current
   vpsAdminOS console or CLI screens that remain English are still recaptured
   for freshness and can share the same topic/view naming with later English
   variants.
5. Where an old workflow has changed, update the prose and navigation path,
   not just the label. In particular:
   - old `Parent` becomes the current `Rodičovský dataset` field;
   - old `Create mount` navigation becomes the current `Mount` action;
   - incomplete `Boot from VPS template` becomes the current full form title;
   - session prose uses `relace`, matching current Czech terminology.

### Safe draft media support

`bin/kb-page` currently supports page operations but not media uploads. Before
staging screenshots, extend it with read/write media commands that reuse its
authenticated JSON-RPC client and safety model:

- `media-info --wiki cz MEDIA` and `media-get --wiki cz MEDIA` for read-only
  inspection;
- `media-save --wiki cz MEDIA FILE --create` with MIME/extension validation,
  identity verification, ACL verification, and an existence check;
- optional draft-only `media-delete` for abandoned review captures.

For this initiative, `media-save` is always create-only. It must refuse an
existing ID. Non-draft media IDs require the same explicit approval gate as
non-draft pages. Exercise the implementation first with a disposable media ID
under `drafts:2026-07-10-kb-czech-fixes:smoke:` and remove it after verifying
round-trip bytes and metadata.

### Draft creation and review

1. Save review copies under
   `drafts:2026-07-10-kb-czech-fixes:<source-page-id>` only after checking
   identity and ACL for every exact page and media target.
2. Remove or neutralize each production `<page>...</page>` translation-mapping
   tag in the draft copy so drafts cannot claim the production page's language
   mapping. Add a visible draft note with the source page ID and source
   revision; neither draft-only change is carried into publication.
3. Upload all Czech screenshot revisions to the draft media namespace using
   their manifest IDs, then save each complete draft page with only new draft
   screenshot references. A reviewer must never need access to local files to
   see the proposed result.
4. Fetch every draft page and media object back from DokuWiki; verify the page
   source, image hashes, rendered dimensions, links, and absence of legacy
   screenshot references.
5. Run the mandatory standalone change review on the complete local previews
   and screenshot set. Record the result and disposition of findings in
   `state.md`.
6. Ask for explicit user approval before any non-draft page or media write.

### Publication after approval

1. Copy the approved immutable screenshot files to their new permanent
   `screenshots:vpsadmin:...:cs:...` IDs using create-only writes. Never replace
   or delete a legacy screenshot during publication.
2. Produce publication source from the reviewed draft by removing the draft
   note, restoring the production translation-mapping tag, and rewriting only
   draft media IDs to their approved permanent IDs.
3. Publish in small related batches:
   - membership/profile/session pages;
   - DNS and networking pages;
   - datasets, exports, and backups;
   - VPS lifecycle and recovery;
   - API and terminology-only pages.
4. Fetch each published page and verify the rendered links, image references,
   navigation paths, and exact Czech labels.
5. Preserve draft pages and draft media until the user accepts the published
   Czech set. Cleanup requires a separate recorded decision and does not remove
   any legacy production media.

## Compatibility and deployment

- Documentation-only; there are no schema, API, protocol, persisted-state, or
  configuration changes.
- The capture repository has no deployment component and no GitHub Actions
  workflow. An operator uses its pinned Nix shell and repository-owned
  dedicated cluster, reviews generated artifacts, and invokes the separate KB
  staging workflow.
- Publish only against a deployment that contains the localization baseline
  used for the audit. English-language vpsAdmin remains available, but the
  Czech KB will intentionally describe the Czech interface.
- DokuWiki page history provides per-page rollback. Legacy media is not
  overwritten or deleted, and all new media IDs are immutable, so rollback
  does not depend on reconstructing a previous bitmap.
- Publication is not atomic. Complete and review all local previews first,
  then publish coherent batches so navigation text and screenshots do not
  disagree for long.
- No coordinated vpsAdminOS node update is required.

## Testing plan

- Confirm recursive coverage count and namespace distribution against the
  live wiki immediately before publication.
- Confirm all 30 expected draft page IDs and all manifest media IDs are absent
  before the first create-only write.
- Scan preview source outside code blocks for every stale English string in
  the replacement dictionary; only documented intentional exceptions may
  remain.
- Scan for current Czech spellings and capitalization from both vpsAdmin
  catalogs.
- Visually review every replacement screenshot for Czech labels, current
  layout, legibility, and accidental disclosure of IDs, IPs, hostnames,
  e-mail addresses, tokens, QR codes, or recovery codes.
- Validate screenshot-manifest completeness: 63 references resolve to 60
  unique Czech assets, every asset has a SHA-256 and capture provenance, and
  every new media reference uses the naming convention.
- Fetch every uploaded draft media object and compare its SHA-256 with the
  local manifest before reviewing the rendered page.
- Validate all internal links and media references after draft saves and after
  publication; draft pages must not reference legacy vpsAdmin screenshots.
- Fetch every final page with `bin/kb-page get --wiki cz PAGE` and compare it
  with its approved local preview.
