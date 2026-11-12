# Independent final review

## Findings

1. **Important, risk/compatibility: the normal metadata limit can prevent an
   otherwise supported old file link from reaching the legacy fallback.**
   `portal/internal/web/repository_review.go:614` returns immediately when
   `comparisonFiles` fails; the explicit-file legacy lookup begins only at
   line 630. In the reviewed commit `06e4878039505bc46d3939405b5548f785397dbb`,
   4,999 modified files plus one moved-and-edited file produce 5,000 records
   under the old 50% rename policy and 5,001 under the new exact-rename policy.
   The new parser returns `ErrReviewLimit`, so an existing valid old file URL
   receives 422 before the historical representation is attempted. This is an
   old-link compatibility regression inside the former 5,000-file boundary,
   rather than a request to implement stage-2 pagination. Permit the bounded,
   membership-checked legacy lookup for an explicit file ID when the normal
   inventory exceeds its limit, or record an explicit compatibility decision.
   Cover a previously valid legacy inventory whose metadata inventory exceeds
   the limit. A disposable Git fixture independently confirmed 5,001 versus
   5,000 raw records (545,107 versus 545,011 bytes).

2. **Important, general: interrupted deferred summaries do not recover on page
   resume.** In the original reviewed head,
   `portal/internal/web/static/repository-review.js:206` starts an untracked
   summary request. `suspend()` aborts it, and the catch deliberately ignores
   cancellation; `resume()` at line 938 refreshes only repositories with a
   missing or changed pair. Returning to the browser with an unchanged branch
   therefore leaves `Loading totals…` indefinitely. Page visibility changes
   invoke this lifecycle in `static/app.js`.

   **Narrow remediation inspected:** the lead amended the branch to
   `6180d5943ab88d03479960d02357db1cb0af1fd4` while review was in progress.
   Its only delta from the assigned head records pending summary payloads,
   retries them on resume, clears them on a settled result or replacement
   history, and adds a browser regression. Direct inspection resolves this
   finding; executing that live-browser regression remains part of subsequent
   verification. The first finding is still present at this amended head.

No Blocking findings. Important findings require a fix or explicit recorded
decision before long verification.

## Scope, architecture and compatibility

Reviewed the complete assigned base-to-head series and final diff from
`6587c4c1cedabee95bcc52f4667e7d33e3a82859` to
`06e4878039505bc46d3939405b5548f785397dbb`, plus the narrow remediation above.
All four required lanes and their full references were read. Reviewer:
standalone `/root/portal_final_review`, assigned installed-catalog settings
`gpt-6.1-sol` / `xhigh`; no retained reviewer roster was available. Overall
risk is high because durable links and HTTP response contracts change.

The stage-1 scope is proportionate. The owning component is the dev-workspace
portal, with its bundled browser as the HTTP consumer. No codex-web interface,
dependency pin, configuration deployment, process queue framework or persisted
schema was added. Existing cache/coalescing, deadlines, process admission,
file/output caps and per-file batching are reused. Stage-2 pagination,
virtualization and explicit partial-clone preparation remain excluded.

Normal committed inventory is raw tree metadata with exact rename matching;
whole-comparison numstat and similarity matching are removed from that path.
Missing blobs do not prevent ordinary metadata listing. Content identity still
comes from verified object IDs, and membership checks precede content reads.
Missing content and diff errors are isolated to a file. Remote request/session
and snapshot scoping remain in the existing authorization path. No new local
operator containment mechanism was introduced.

Legacy file IDs use a distinct ID namespace and separate transient snapshot,
so an old link does not mutate an open metadata comparison or silently resolve
to another file. The limit exception above remains unresolved. Deferred summary
responses are fenced by generation, snapshot and request ticket. Browser count
aggregation distinguishes pending, binary and limited records and suppresses
partial line totals. Old inline summaries remain accepted. Cached old browser
pages require refresh; asset versions were bumped. Older portal code cannot
resolve the new metadata file IDs after rollback, and this limit is documented.
Frozen comparison revisions and saved descriptor formats remain unchanged.
Staged/unstaged capture code and its immutable-content behavior were inspected
and are unchanged.

## History and migrations

The complete branch contains one logical commit, `portal: load comparison
metadata before file statistics`, including supporting tests, asset versioning
and documentation. That split is coherent and the message explains purpose
and compatibility. No obsolete unmerged approach or separate follow-up fix
commit remains. The amendment retains one commit rather than accumulating a
repair commit.

**No migrations.** There are no database, manifest, saved-review schema or
journal format changes, and no intermediate migration lineage to preserve.
The packet reports no deployed or externally consumed feature versions.
**No repeated update streams:** there are no dependency/channel/input updates,
generated-artifact refresh streams or superseded pin commits to consolidate.

## Documentation placement and preservation

README's existing repository-review section is an appropriate user entry point
and links to `docs/workspace-portal.md`. The portal guide is the authoritative
reference for metadata counts, exact renames, independent summaries, limits,
no-fetch behavior and rollback/link compatibility. These explanations remain
useful after the initiative and do not depend on its private records. Individual
benchmark, design and rollout status correctly remain in initiative tracking.
Documentation and anchors were preserved; no supported upgrade instructions or
recovery prerequisites were removed. Prose generally matches
the source; the old-link claim needs the first finding resolved or narrowed.
Prepared/tested/deployed claims are separated and no deployment is claimed.
No additional documentation structure or version-specific upgrade guide is
needed for this bounded read-only change.

## Verification and remaining limits

Inspected changed and adjacent reader/API/browser code, the complete commit
series, all changed tests and documentation, saved-review scope handling and
request/cache bounds. Base-to-assigned-head `git diff --check` passed. The
Nix browser navigation/helper contract check passed during the lead's narrow
remediation; it does not substitute for the live-browser regression. The
5,000/5,001-record compatibility probe used a temporary repository and removed
it on exit. No source edits, heavy tests, services, deployments or other-session
access were performed by this reviewer.

Broad Go/package checks and live-browser regressions remain to run after finding
reconciliation. Browser coverage should exercise pending file counts becoming
exact counts, binary/limited classification and aggregate completeness, in
addition to deferred-summary cancellation. Existing 5,000-file and output limits,
retained browser editors/content, and bounded legacy similarity timeouts remain
accepted stage-2 limitations. No integration or deployment approval is implied.
