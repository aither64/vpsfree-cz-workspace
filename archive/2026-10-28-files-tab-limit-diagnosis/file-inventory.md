# Session Files inventory

Observed 2026-10-28; final metadata check at 14:23:22 UTC. The user's follow-up
authorized read-only metadata inspection of other sessions' public tracking
directories. This supersedes the original investigation's inventory exclusion.
Identity was reverified against this session's exact slug and workspace before
the scan. No peer worktrees, teams, transcripts, private runtime state or file
contents were inspected; no session was changed or cleaned.

## Result

**Nine directories exceed the Files limits: five in `work/`, four in `archive/`.**
All nine exceed 5,000 regular files; the largest three also exceed both 4 MiB
path-metadata budgets. No metadata-only offender was found.

The full metadata pass took 25.8 seconds and examined 381,370 directory entries:
114 `work/` directories with 284,683 eligible regular files, and 260 `archive/`
directories with 58,824. It completed without access errors or time-limit exits.
An additional compact pass recovered the smaller-offender summary, followed by
a metadata-only Markdown/raw-data breakdown for the four archive outliers.

| Root | Session | Files | Logical size | Exceeded budgets | Main contributors |
| --- | --- | ---: | ---: | --- | --- |
| work | `2026-10-17-confctl-rust-rewrite-plan` | 90,735 | 12.87 GiB | Count, traversal metadata, response metadata | `evidence/` 83,733; `.cache/` 6,595. Compiler/tool-source trees, compiled outputs and probe caches. |
| work | `2026-10-24-vpsadmin-haveapi-upgrade` | 80,853 | 5.19 GiB | Count, traversal metadata, response metadata | `package-c/` 64,297; 61,123 files under `node_modules` across the session. Repeated browser comparison environments, SDK build output and Python environments. |
| work | `2026-10-09-evaluate-confctl-rewrite-language` | 63,554 | 3.39 GiB | Count, traversal metadata, response metadata | `evidence/` 63,176. Repeated `.work-cache`, `.core-check-work`, configuration acceptance and Ruby fixture trees. |
| work | `2026-10-27-api-documentation-redesign` | 13,156 | 0.72 GiB | Count | `preview/` 7,773, including `preview/.gems/ruby` 7,691. Baseline/candidate performance source and client trees contribute most of the rest. |
| archive | `2026-10-05-network-ipv4-left-counter` | 10,954 | 0.63 GiB | Count | 6,740 root files; `network-layout-hosted1/` 998. Predominantly JSON, logs, diffs, command exit records, downloaded test artifacts and browser build output. |
| work | `2026-10-22-limit-autostart-alerts-to-boot` | 8,482 | 5.53 GiB | Count | `final-ci-9f9d6139/` 4,428; older CI artifacts 1,397; `async-ci-d4ff05483/` 818. Logs, JSON and status/stdout/stderr evidence from multiple CI attempts. |
| archive | `2026-10-22-codex-thread-retries` | 7,602 | 0.90 GiB | Count | `backend-successor/` 2,244; `backend-browser/` 971; failed-creation recovery fixtures 801; `ui-successor/` 669. JSON, stderr/stdout, source fixtures and browser evidence. |
| archive | `2026-10-12-streamline-vpsadminos-config-imports` | 7,131 | 0.90 GiB | Count | Persistence diagnosis 1,494; final CI observation 1,218; prior CI failures 1,018. Includes 4,366 `.log` files and 1,236 `.txt` files. |
| archive | `2026-10-19-vpsadmin-kernel-cves` | 5,395 | 0.13 GiB | Count | `research/` 3,696, including 3,494 CVE-record files; `assessment/` 1,330; `.gems/` 350. Mainly JSON research records, source excerpts and patches. |

`work/2026-10-20-kernel-check` was just below the cap at 4,987 files; its
traversal/output estimates were 805,430/858,501 bytes, below the byte caps.

## Why the counts are large

These are substantially broader than ordinary tracking notes. The observed
paths and extensions identify retained dependency installations, generated
build products, copied source/test fixtures, downloaded CI artifacts and
research datasets. Several sessions keep multiple independent versions or
baseline/candidate environments, which each contribute their own trees.

Concrete examples:

- The HaveAPI upgrade has 42,333 files in
  `package-c/0.31.0/expiry-paired/` and 21,127 in
  `package-c/0.30.2/mobile-base-comparison/`; the session-wide `node_modules`
  count explains most of its total. It also has 3,697 files under `target`
  and 2,394 under `site-packages` (categories can overlap).
- The confctl rewrite has 18,686 files in
  `evidence/m2/helper-tool-sources-v1/` and 15,422 in
  `evidence/m2/helper-diagnostic-compiler-operation-v2/`. Its extensions include
  3,952 `.o`, 3,127 `.rmeta` and 34,720 `.json` files, consistent with build
  products, compiler metadata and retained tool inputs.
- The language evaluation has separate `tui-configuration-acceptance-v1` and
  `v2` trees with 4,418 files each in `ruby-fixture/`, plus other work/cache
  directories. This proves multiple fixture trees, not byte-identical copies.

**Interpretation:** the evidence fits accumulated development/test material
kept inside the directory that Files recursively inventories. The file kinds
are ordinary for that work; their quantity and repeated environments explain
the failure. Metadata alone does not establish whether every retained copy is
necessary, which exact command created it, or whether any duplication was
accidental. No content hashing or duplicate/provenance investigation was done.

## Archived outliers and current retention

They are not Markdown/history bulk:

| Archived session | Markdown files | `portal.yml` | Other regular files |
| --- | ---: | ---: | ---: |
| `2026-10-05-network-ipv4-left-counter` | 227 | 1 | 10,726 |
| `2026-10-22-codex-thread-retries` | 348 | 1 | 7,253 |
| `2026-10-12-streamline-vpsadminos-config-imports` | 106 | 1 | 7,024 |
| `2026-10-19-vpsadmin-kernel-cves` | 84 | 1 | 5,310 |

The current [storage-retention guide](../../docs/operations/workspace-storage-retention.md)
says new tracking projections retain Markdown and `portal.yml`, but also:
“Predecessor archives retain their recorded policy until compacted.” The raw
data is therefore compatible with historical retained archives. The actual
policy and provenance of each outlier remain **unknown**; no private recovery
receipts or lifecycle history were inspected. These counts do not demonstrate
a current archive lifecycle defect or authorize compaction.

## Method and limits

The scan used `scandir`, regular-file metadata and explicit non-following of
symlinks. It excluded `.git` components and unsafe paths like the portal, counted
relative path bytes for all visited entries before eligibility filtering, and
estimated output with the portal's JSON-path and row-overhead formula.
It did not open file contents or reproduce the portal's per-file open checks.
Consequently, counts establish candidates eligible by path/type, not a successful
HTTP listing under every concurrent permission or lifecycle change.

Totals exceed a budget regardless of traversal order, but no exact first
trigger is claimed for sessions exceeding multiple budgets. Each pass was
bounded and interruptible. The workspace is live, so these are observations,
not an atomic snapshot or permanent counts. The report itself was created
after the inventory and is not included in its totals.

Sizes above are sums of logical file sizes, not disk usage or reclaimable
space. The first pass also summed file `st_blocks`, but that does not account
for filesystem compression, shared extents, snapshots, hardlinks or directory
overhead; no physical-space-recovery claim is made.

The design recommendation remains to return bounded partial listings with a
clear truncation notice. A separate future storage-policy discussion could
address where bulky build/test environments belong; this inventory makes no
cleanup recommendation for particular sessions and performs no cleanup.
