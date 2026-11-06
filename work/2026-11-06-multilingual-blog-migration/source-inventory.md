# Blog source inventory

Public-safe aggregate findings from A0, implementer0, 2026-11-06. No raw user,
comment or post records, credentials, private content, addresses or dumps are
included here. No application, configuration, database or service changes were
made. No scaffold/importer edits or commits were made.

## Access and evidence

- `dev-session current`, both environment identity values and the same-session
  roster matched `2026-11-06-multilingual-blog-migration`.
- Target mapping came from the canonical configuration clone, retained
  `origin/master` at `85b38f1cd07d6b3a0fde3eefd32258f747e757e5`,
  `cluster/cz.vpsfree/containers/int.blog/module.nix`. DNS was not required.
- Root SSH reached hostname `blog`. The initial strict connection stopped before
  authentication because the host was unknown. Following the lead's explicit
  ordinary `accept-new` clarification, the new host key was enrolled; all later
  connections enforced the recorded key. No changed key was overwritten and host
  checking was not disabled. ED25519 fingerprint:
  `SHA256:PGUTWywjvZb2q5oaeaU0xWHFJp8Ara4ZY4z7sdq3lLk`.
  Confidence is configured mapping plus TOFU plus runtime hostname, **not an
  independently authenticated host-key comparison**.
- Runtime system:
  `/nix/store/y50f85i2dgycjk5kpbgwxd8ww2j9f0n4-nixos-system-blog-26.05.20261026.718f670`.
  WordPress **7.1.2** was confirmed with the isolated `wp-blog` wrapper's
  pre-bootstrap `core version` command under the `wordpress` Unix user, skipping
  plugins/themes. An initial root invocation refused; `runuser` resolved it
  without `--allow-root`. MariaDB reports **11.4.12**.
- Aggregate SQL used `SET SESSION TRANSACTION READ ONLY` and
  `START TRANSACTION WITH CONSISTENT SNAPSHOT`. Initial aggregate snapshot time:
  **2026-11-06 21:13:42 UTC**. Public feed was read through local backend HTTP
  with the expected Host/forwarded-HTTPS headers. No admin endpoints were used.

## Corpus

| Item | Observed result |
| --- | --- |
| Published posts | **125**, all password-free; no draft/private/page rows in the post-type/status inventory |
| Revisions | **422**, retained privately |
| Public-post authors | **6**; **9** registered users overall, full records retained privately |
| Approved comments | **107**, all on the published posts; **43** replies with valid approved same-post parents |
| Spam comments | **159**, excluded from future public projection |
| Comment metadata | **961** rows, private unless a later explicit allowlist requires something |
| Attachments | **144**: 89 JPEG, 54 PNG, 1 PDF |
| Active uploads | **569** regular files, 93 directories, no symlinks; **50,375,369 bytes** including directory metadata |
| Database | **12 InnoDB tables**; allocated data 5,488,640 bytes plus indexes 688,128 bytes |
| Taxonomy | 9 category terms, 32 tag terms; every published post has 1–3 category assignments |
| Publication dates | November 2014 through May 2025; no blank titles/content, zero UTC dates or future publication dates |

All published posts currently have open comment status. This is source state,
not a decision to retain a local commenting service. Public author display names
were not email-shaped; their exact fields still need an explicit projection
allowlist. User logins, email, password hashes, registration/authentication data,
comment email/address fields, spam and unrestricted metadata must remain private.

## URL, feed and rendering constraints

- Site/home is `https://blog.vpsfree.cz`; locale `cs_CZ`; timezone `Europe/Prague`.
  Permalinks are `/%postname%/`. All **125** post slugs are nonempty, unique,
  root-level ASCII with no percent escapes; decoding creates no collisions.
- All **125** post GUIDs are unique HTTPS URLs on the canonical Czech blog host
  using `?p=<source ID>`. They are **identifiers distinct from slug permalinks**.
  Preserve these exact GUIDs in the Czech feed to avoid presenting the existing
  archive as new articles. Do not synthesize GUIDs from the new canonical path.
- Live `/feed/` returns **10** items, all with full content and unique GUIDs;
  every item has `isPermaLink="false"` and the source-ID query GUID. Response
  size was **52,987 bytes**. Options agree: `posts_per_rss=10`,
  `rss_use_excerpt=0`. Existing IRC bot consumption is recorded in
  [configuration-findings.md](configuration-findings.md).
- Active theme is Flat. Active ordinary plugins are Akismet, Disable Gutenberg
  and the Facebook/Open Graph tags plugin. Package versions come from the
  configuration findings; active plugin selection was confirmed from runtime
  option allowlists. Upload paths use year/month directories.
- No block-editor markers were found in published bodies. **11** posts contain
  iframes; observed iframe source hosts are YouTube and SuperLectures. **54**
  posts contain image tags; no direct `<video>`/`<audio>` tags were observed.
  All **125** contain a WordPress `<!--more...` marker.
- The first broad shortcode-shaped scan matched five posts. Follow-up parsing
  found literal `[PDF]` labels and root shell prompts, with no proven active
  shortcode syntax. Do not introduce a shortcode subsystem based on that count.
  Media references, legacy embedding markup, links and code formatting still
  require per-article validation during the later importer package.

The architect's agreed future schema uses `wp-<post_id>` as stable identity,
the original resolved Czech path, English at the `blog.vpsfree.org` root, and
`discussion_url` equal to the original absolute Czech article URL. English feed
identity and publication policy remain design decisions; observed Czech GUIDs
must not be silently repurposed as English publication identities.

## Private recovery capture and consistency limits

A private recovery copy was streamed over SSH directly into durable owner-only
operator storage outside Git and disposable session directories. The exact
location was reported privately to the lead, not placed in this public-safe
record. Directories are mode `0700`; SQL, archive and manifest are `0600`.

- Full `wordpress` database dump: **2,840,321 bytes**, using
  `mariadb-dump --single-transaction --quick --skip-lock-tables` with routines,
  events, triggers and hex blobs. All users, revisions, spam and metadata remain
  in this private recovery artifact. Twelve table definitions and the successful
  dump completion marker were checked without printing content.
- Active uploads plus private secret-key state archive: **49,047,084 bytes**.
  Historical inactive uploads backup directories were excluded. The archive has
  663 safe relative members, including 570 regular files; gzip integrity and
  active-tree/key-state presence were checked. Secret contents were never
  displayed or inspected.
- SHA-256 values and capture metadata are in the private manifest. Upload-tree
  path/type/size/modification/change metadata hashes matched before and after
  extraction. No remote file was created; no writer freeze or service restart
  was requested.

The database snapshot is internally consistent because all tables are InnoDB.
Unchanged upload metadata is useful evidence, but it does not establish an
atomic database/filesystem cutover point. Before final publication, establish a
content-write cutoff and capture a new final snapshot; retain this recovery
copy and the old system generation through rollback. No restore was executed.

## Handoff

A0 is ready for lead acceptance. Its sole coordination output is this
uncommitted findings file; no public corpus has been generated. Architect0 owns
the public allowlist/schema and design; lead must separately allocate the
importer after accepting or explicitly parking A0 and confirming capacity.
Private recovery paths/content must not enter the future public repository.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/)
