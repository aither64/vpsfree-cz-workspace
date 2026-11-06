# T2 English translation batch evidence

Owner: `implementer2`. Lead accepted the completed batch on 2026-11-06.
This records completed source work and agent checks; human editorial review and
publication remain pending. C0 owns subsequent aggregate checks and the index.

## Exact source and committed scope

- Repository: `vpsfreecz/blog`, local branch
  `2026-11-06-multilingual-blog-migration`.
- Parent: `e8aed2ef787217e8085d782e38a760cd51ddbd90`.
- Accepted T2 commit: `c3786b74af9ee9382af4cc44428e7e77965753ea`,
  `content: draft 62 English archive translations`.
- The earlier reported `c3786b751ffacb2109d9db19de9849bfd0577146` was a
  transcription error, explicitly corrected and discarded. Verification used
  the actual accepted commit; the lead independently checked it with Git.
- Exact scope: 62 new `content/posts/<id>/index.en.html` files, 2,220 inserted
  lines, translating 21,468 source words. No Czech/shared data/template edits.
- Source snapshot: `20261106T211556Z`. Complete public source manifest:
  `data/migration/source-manifest.json`, SHA-256
  `e3c56173acbc2dd018da1d7ce5cd8b73d52e5ef83847a0353b17b107e5a36ab4`.
- No migrations, input updates, superseded T2 commits or history rewrite.
  No push, default initialization/integration, production action or service
  change was performed by T2.

Assigned IDs, matching `translation-batches.json`'s `implementer2` batch:

```text
wp-24 wp-37 wp-51 wp-61 wp-74 wp-82 wp-84 wp-100 wp-112 wp-114
wp-119 wp-137 wp-139 wp-151 wp-210 wp-215 wp-244 wp-249 wp-253 wp-269
wp-275 wp-279 wp-291 wp-308 wp-326 wp-343 wp-378 wp-387 wp-406 wp-433
wp-443 wp-450 wp-455 wp-460 wp-465 wp-470 wp-474 wp-490 wp-500 wp-521
wp-529 wp-536 wp-552 wp-580 wp-588 wp-601 wp-610 wp-615 wp-625 wp-629
wp-636 wp-651 wp-653 wp-681 wp-695 wp-709 wp-717 wp-792 wp-805 wp-807
wp-811 wp-815
```

## Exact inventory digest

Final SHA-256:
`ff6ebefe2f8377ca62796917283ededb2caa54ec29e64a5d2ad9de81665d4ce3`.

The digest covers a JSON array of 62 objects containing `path` and `sha256`.
Paths are repository-relative `content/posts/<id>/index.en.html`, sorted in
ASCII order. Each hash covers the file's raw bytes. Encode using Python
`json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(',', ':'))`
followed by exactly one LF, then hash those UTF-8 bytes. The committed files
are the durable inventory source; `/tmp/blog-t2-inventory.json` was the local
working copy. Every staged blob, committed blob and final owned working file
matched this digest's individual hashes. The commit's changed-path list was
exactly these 62 paths. The index was empty when yielded to the lead.

## Completed checks and limits

Every full Czech source and public author mapping was read. Each full English
body was translated and compared for semantic omissions, chronology, first-person
claims and source-era technical meaning. The lead read all 62 full English bodies
and accepted the contextual wording, including the requested corrections to
`wp-815`, `wp-465` and `wp-500`.

Final local batch checks passed for all 62:

- Actual complete Czech-file SHA-256 equals the manifest's `cs_file_sha256`
  and English `translation_source_sha256`; the raw body hash was not substituted.
- Original `date`, `lastmod`, taxonomy slugs, `translationKey`, `article_id`
  and source provenance remain unchanged. Every English file has `draft=true`
  and `translation_status="draft"`, with no human reviewer or review timestamp.
- Ordered HTML structure, machine attributes, comments and original `more-*`
  anchors match. Human-readable alt/title translations are allowed; URLs,
  media targets and other machine attributes are preserved.
- Ordered `href`, `src`, `srcset` and `poster` values match, and complete
  protected `<pre>`/`<code>` spans match raw source bytes.
- Numeric values match after English decimal/percent formatting. The approved
  `wp-500` prose word `twice` is explicitly equivalent to source `2x`.
- Newly introduced unprotected EOF blank lines were removed. Each owned file
  ends with one LF; protected code was not normalized.

Before commit, a global source check covered all 125 Czech/English pairs:
complete source-file/manifest/translation hashes, draft state, absence of human
reviewer/date, matching IDs and explicit root-relative English routes passed.
There were no English route collisions across the 125 files then present.
This was source validation, not a Hugo build, rendered-page check or final
aggregate acceptance. C0 owns aggregate checks; no extra shared build was run
for this evidence. Temporary check helpers were outside the repository.

The ordinary commit ran through `nix develop -c git commit -F` with no hook
bypass. Repository instructions declared no hook framework, and no framework
configuration was found. No whole-worktree cleanliness claim was made; other
owners' work was preserved.

## Raw-byte whitespace classification

All **31 `<pre>` blocks and 50 `<code>` spans** were compared as complete
ordered byte strings using `read_bytes()` and byte-pattern extraction, without
text-mode newline conversion. All matched the Czech source; no protected-code
repair was necessary.

Of those protected spans, **25 `<pre>` blocks contain source-identical CRLF**.
The staged diff check reported **154 trailing-whitespace locations**, all inside
those exact source-identical blocks. Every diagnostic was mapped to its staged
file/line and checked against the raw protected source span. There were no other
diagnostics or remaining EOF findings.

| Article | Protected CRLF blocks | Diff-check line diagnostics |
| --- | --- | --- |
| `wp-308` | 9 | 87 |
| `wp-521` | 3 | 14 |
| `wp-610` | 7 | 16 |
| `wp-615` | 2 | 11 |
| `wp-807` | 4 | 26 |
| Total | 25 | 154 |

These are inherited A1 source-fidelity exceptions, not new prose whitespace.
The code bytes remain unchanged. `/tmp/blog-t2-diff-check.txt` held the local
diagnostics; this record retains the classification and counts.

## Preserved source quirks and editorial boundary

- `wp-24`: `ZPS` remains in the quoted source thread title.
- `wp-84`: the source spelling `PostgresSQL` remains.
- `wp-139`: the statement says five mount states while the list has six entries;
  both remain as written in the source.
- `wp-490`: the protected release-note URL remains
  `http://https;//projects.vpsfree.cz/vpsadmin-doc/releases/v2.7.0/`.
- `wp-521`: the historical PTR explanation and one-record claim remain;
  translation did not turn into a technical update.
- `wp-210`: Czech long-scale `79 kvadriliard` is English short-scale
  `79 octillion`, preserving the value.
- Original relative Czech URLs remain for V1's output handling. Source-era
  security/version claims, plans, opinions, uncertainty and authored asides were
  preserved. Existing English titles/UI strings and code remain intact.
- Meaningful Czech alt/title prose was translated; empty or identifier-only
  media labels were retained without inventing descriptions.

Agent fidelity/style checks and the lead's contextual wording acceptance do not
constitute human editorial review. All 62 translations remain drafts, excluded
from production publication under the agreed contract. Final independent change
review waits for C0/E0 source completion and aggregate evidence; human editorial
approval is a separate later gate. Implementer2 retains ownership of T2 findings.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.
