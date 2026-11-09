# P13 dated bundle relocation receipt

Owner: `implementer2`. D13 and the lead's complete P13 release authorize source
organization only. Main read/accepted the exact README/AGENTS/authoring/skill/
migration wording, including the literal Czech calendar date and lowercase
`YYYY-MM-DD-english-title/` examples, before commit. W13's deployment document
remained outside this commit.

- Base/parent: `70631dd0dab3dbc3386a826de6ef95462897b0a6` (accepted U13).
- Head: `14da1cfc3e7c22380872d0fa1789edea192d0c0a`.
- Tree: `7ca843018f8adac63fe4767fa112e80d100f80aa`.
- Git: **250 exact R100 renames**, comprising 125 CS/EN bundles; nine modified
  tooling/manifest/documentation files; 259 logical paths, 445 additions/271
  deletions. No article-content diff.
- Modified files: `tools/import-wordpress`, `tools/import-wordpress-check`,
  `bin/check`, `data/migration/source-manifest.json`, `README.md`, `AGENTS.md`,
  `docs/authoring.md`, `docs/migration.md`, `skills/blog-authoring/SKILL.md`.
- Complete final staged/committed 259-file inventory SHA-256:
  `c3a1b3409e0ceee086902f25590ee80fc2baf94ba1a36b511ecd8bdba1532b27` (canonical sorted JSON path/raw-SHA array
  plus LF). Each committed blob matched the staged/working file. The rename
  bijection was checked separately with `--find-renames=100%`.

[Exact old/new ID-language path/hash map](article-path-map.json) records every
one of the 250 original SHA-256 values and both paths, plus original CS/EN public
URLs. Map SHA-256: `662c0795b6b1fab4419202acbfffea7f1880ca84aeed6f61bfde23ba50fcfa86`. This is session evidence,
not a new application slug registry. Immutable old/new Git trees and exact rename
records also retain the complete mapping and source bytes.

Folders use the first ten calendar characters of stored CS `date`, without
conversion, then the current EN title with apostrophes removed, NFKD-to-ASCII,
lowercase and collapsed/trimmed non-alphanumeric hyphens. All 125 dated names are
unique/nonempty; no collision suffix was needed (longest title slug: 77).
Collision groups use immutable-ID suffixes for every member; empty title slugs
use `article-<id>`. The title-derived names of wp-137 and wp-381 differ from their
explicit English public URLs; both URLs remain byte-identical. Assigned folders
remain stable through title edits.

All **250 complete article bytes are unchanged**, including frontmatter, dates,
IDs, source/review hashes, draft state, prose, code/CRLF, hrefs and media. Each
pair shares its new directory. The manifest reverse-mapping proof establishes
that only 125 `articles[].cs_file` values and the corresponding 125
`generated_files` keys changed: content hashes, counts, routes and every other
manifest field are equal. Shared articles/authors/taxonomies/discussions/feed
GUIDs, approved comments, static media, runtime helpers, Pagefind source and
Nix inputs are unchanged.

The importer now reads its existing manifest's explicit ID→path assignments by
default, or a supplied `--source-manifest` fixture. It validates ID association,
relative dated paths, real calendar dates and duplicate IDs/destinations; unknown
imported IDs refuse before formatting/output. Existing unrelated bundles refuse,
manual Czech changes retain the prior generated-hash fence, and English files
are never part of the generated set. Empty-output and in-place writes use the
same assigned location. `bin/check` discovers languages by frontmatter ID and
rejects duplicate identities or split bundles, rather than using parent names.
No private export/database/WordPress operation was performed to test this.

| Authorized check | Result / retained local log |
| --- | --- |
| `nix develop -c python3 tools/import-wordpress-check --source .` | exit 0, eight tests plus public125-file/route/107-comment/569-asset checks, 4s; `/tmp/p13-importer-check.log` |
| `nix develop -c bin/check` | exit 0, 53s; `/tmp/p13-check.log`; search, source/hash/draft, link/pair and existing fixtures retained |
| `nix develop -c bin/check-release` | exit 0, one test/1s; `/tmp/p13-check-release.log` |
| Native Hugo production + draft-preview renders | exit 0, 8s; `/tmp/p13-equivalence-render.log` |

A fresh pinned Luna/low operation watcher ran that related batch with explicit
`danger-full-access`/`never`; all operations completed. Owners0/3 received direct
utility-slot-free notice. Focused tests cover mapped fresh/repeated output,
manual Czech refusal, English raw preservation, invalid/duplicate map and unknown
ID refusal, other-bundle preflight and source identity discovery. Earlier inline
focused validation also passed; no failed checks, retries or bypass occurred.

Before/after native Hugo outputs are **byte-identical in full**: all 1,661
production files and 2,110 draft-preview files. This proves unchanged article and
archive routes, paired links, canonicals and full-content feeds without a live
service. Production has ten CS feed items/zero EN; preview has ten of each.
Production CS feed SHA-256 is
`635493e514ae0152020dadbab7eeef1eb6b03babd390e87c5ee95201ce1c97c7`; preview EN feed SHA-256 is
`ca78453c2761b3e25049019d5de77ca2d218abe2c31f75b44c96a09ff14c78fc`. Raw local renders remain at
`/tmp/p13-baseline/` and `/tmp/p13-final/`; no final Nix release artifact or browser
run was performed before mandatory review.

Exact owned staging included 509 old/new path names and excluded W13. Working,
staged and exact committed rename-aware whitespace checks pass with zero
findings; inherited raw source whitespace remains unchanged. Normal
`nix develop -c git commit -F` exited 0. The repository declares no hook framework;
framework configs/core.hooksPath/active non-sample hooks were absent. No hook
bypass. Index verified empty and yielded directly to implementer0 with exact
head/tree; no further P13 source/Git mutation follows that yield. No whole-tree
clean claim is made over W13's independently owned document.

No dependency/pin stream or persisted application migration. Reverse moves and
the prior manifest/tooling restore the old source layout; public routes need no
redirect because they never changed. Lead owns acceptance, independent final
review, later artifact checks/publication. No push/default/rebase/network,
service/live WordPress/private-input/cleanup/production action or human editorial
approval was performed. Retain P13 source-fix ownership; session and previews
remain open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.
