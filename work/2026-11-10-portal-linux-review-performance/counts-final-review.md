# Automatic repository counts: independent final review

No Blocking, Important or Advisory findings in the reviewed committed ranges.
The correction is suitable to proceed to the planned package and integration
verification. This review does not claim that the candidate has been deployed
or that its live acceptance has passed.

Reviewer: `/root/counts_final_review`, assigned installed fallback
`gpt-6.1-sol` / `xhigh`. The installed a0nhkz2 runtime catalog selects the
`delegated` team's `reviewer` role with purpose `review` and those settings.
Fallback reason: the threadless initiative has no eligible retained roster and
the previous application reviewer is unavailable. Review performed directly,
without nested agents. Risk: high because the additive browser/API contract
and composed deployment must remain compatible. Lanes: general, architecture
and repetition, scope and proportionality, risk and compatibility.

## Reviewed series and history conclusion

| Repository | Complete base | Complete head | Commits |
| --- | --- | --- | --- |
| dev-workspace | `02881b401955ff0db71bb74f6fb84f6e475a7879` | `4dd6c7577c4e6c6f607f07c5227b553f17975cce` | 1 |
| workspace | `42c76e8cb61e0d2063a3d25b4b448e66abee523f` | `bf0574e49ac555e7eb36afbbbb486828e1c5d7b6` | 1 |
| vpsfree-cz-configuration | `5dcde1ce5210a42e4499dbf1b6badbd1f0aa326c` | `f74dd69e590eb53e79743eed70ca9224e852b3af` | 1 |

Inspected every commit message and each complete base-to-head diff, together
with the adjacent reader, cache, API, browser, tests and deployment consumers.
All three worktrees are clean for tracked files. Their local origin/master
merge bases equal the packet bases; fresh read-only SSH `ls-remote` checks also
returned those bases for remote master during review.

The runtime commit has one coherent purpose: automatic independent counts,
its supporting regression coverage and reference corrections. Browser import
and template version changes are required to deliver that behavior. The two
consumer selection commits are isolated from runtime behavior and unrelated
inputs. Commit messages match their final changes; the configuration message
preserves confctl's generated changelog.

Whole-series conclusion: no obsolete unmerged approach, fixup, abandoned shim
or unapplied intermediate version remains in any current branch. The original
delivery is already in the bases and protected merged history; this review
does not propose rewriting it. **No migrations**: no database, persisted schema,
saved-comparison format or operation-journal change exists in these ranges.
Migration merge/release/deployment/external-use provenance is therefore empty.

Repeated-stream conclusion: each current branch contains only its one final
update. Workspace's nested runtime input and configuration's
dev-workspace/devWorkspace channel are separate consumer streams, each selecting
`4dd6c757` once. There is no redundant unmerged update to consolidate. Earlier
runtime selections reside in already merged master history, rather than being
retained superseded commits in these reviewed ranges.

## Correctness, ownership and risk assessment

- `portal/internal/repository/review.go:556` delegates statistics to one bounded
  Git numstat operation with the metadata view's frozen pair and rename policy.
  The parser clones metadata, matches complete old/new path identities, accepts
  binary records explicitly, and rejects missing, duplicate, malformed or
  negative records. NUL framing preserves tabs/newlines in paths. Existing
  no-fetch, no-external-diff/textconv, command deadline and output protections
  remain on this read.
- `portal/internal/web/repository_review.go:315` reaches counts only after
  registration and scope authorization, binds the snapshot to session,
  repository and scope, and rejects working-change captures. Clients cannot
  choose arbitrary revisions or filesystem paths through this endpoint.
  Existing four-request and four-Git-job admission remain in force.
- `portal/internal/web/repository_review.go:525` and `:564` make overview and
  per-file counts share the existing immutable, bounded single-flight/LRU
  cache. Metadata and preview reads retain their independent paths. Legacy
  rename representations remain in their own cache namespace. The added
  helper has a concrete shared consumer and avoids a second statistics
  implementation or job subsystem.
- `portal/internal/web/static/repository-review.js:493` starts counts for the
  entire committed comparison without requiring previews. Snapshot identity,
  read generation and request tickets reject stale responses; resume retries
  a suspended pending calculation. Failed counts expose an explicit retry.
  Successful counts replace every header, including collapsed files, and
  `assignContent` no longer overwrites them with limited/failed preview data.
  The changed live-browser fixture exercises those cases rather than merely
  checking the exported formatting helpers.
- The runtime owns this capability and its browser consumes the endpoint.
  Source search found no other endpoint consumer in the affected runtime or
  workspace. Workspace retains the direct nested runtime URL; configuration
  retains its existing channel mapping and host-module consumer. Both lock
  diffs select the same revision and NAR hash. Extension `0c7168f3`, native
  Codex, sibling dependencies, follows paths and application user-profile
  ownership remain unchanged. No cross-project interface was moved to a
  consumer or duplicated downstream.

Scope is proportional to the user's explicit requirement to judge changesets
without opening files. It reuses Git, existing caching and request control.
No pagination/editor-retention stage, fetch/maintenance mechanism, new framework
or persistent background job system was added.

Compatibility conclusion: the endpoint is additive and counts use existing
snapshot identity. Browser assets are versioned with the backend. Existing
inline-summary handling remains, older open pages need a refresh for automatic
per-file counts, and working-change captures retain their previous behavior.
No new persisted state affects rollback. The documented older-package inability
to resolve metadata-generation file IDs is an existing baseline constraint and
remains preserved. No coordinated node or daemon upgrade is introduced.
Local host operators are trusted; remote-client validation and authorization
remain applicable and intact.

## Documentation placement and preservation

The README remains the existing entry point and retains its working link to
`docs/workspace-portal.md`. Its repository-review section now states the visible
automatic-count behavior. The portal guide's **Repository comparisons** section
is the authoritative detailed reference for independent counts, failure/retry,
cache sharing, frozen revisions and the additive endpoint. These explanations
remain useful without this initiative's status or private context.

The changed statements agree with the reader, handler and browser, including
the distinction between unavailable totals and a usable file list or preview.
The edits preserve no-fetch behavior, explicit preparation of partial-clone
content, deadlines/output limits, the 5,000-file cap, legacy-link semantics and
the rollback restriction. No document was moved, no old entry-point anchor was
removed, and no supported upgrade/recovery path was retired. No new upgrade
guide is needed because persisted formats and deployment contracts are unchanged.
README and guide repeat only the user-visible summary; specialist behavior
stays in the linked guide. The finished prose is plain, factual and consistent
with the supplied writing guidance.

Individual revisions, execution results and rollback preparation correctly
remain in shared `state.md` / `rollout.md`, with this review as linked evidence.
Configuration receives only its generated input update and no prohibited
release receipt. Documentation placement and preservation are adequate; no
exception or missing operational prerequisite was identified.

## Evidence and remaining limits

Independently inspected the focused parser/real-Git metadata tests, missing-blob
API fixture, frozen summary/count agreement, shared-cache test, browser
suspend/stale/failure/retry checks and preview-count preservation assertions.
Read the packet's successful Nix Go/JS/Playwright evidence and its diagnosed
initial fixture/environment failures. Independently ran `git diff --check` on
all three complete ranges; all passed. No long tests, builds, deployment or
repository/session mutation was performed by this reviewer; the only written
artifact is this report.

Remaining delivery checks are the planned package/integration verification and
candidate live NFS/Linux API acceptance. Automatic numstat still needs local
blobs and may hit the unchanged deadline/output limits on a large or cold
comparison; the explicit error/retry path is part of the accepted contract.
The packet's host timings and memory observations are evidence for those
measured inputs, not universal latency or memory guarantees.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-portal-linux-review-performance/
