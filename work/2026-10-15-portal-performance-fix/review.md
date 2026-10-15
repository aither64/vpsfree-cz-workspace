# Independent final review

Reviewed the committed deliverable for `2026-10-15-portal-performance-fix`.
Reviewer: `/root/final_review`, standalone catalog fallback, assigned
`gpt-6-astra` / `xhigh`; no retained reviewer roster. All four lanes were read
and applied: general, architecture/repetition, scope/proportionality, and
risk/compatibility. Overall risk is high because recovery admission, protocol
consumers, and deployment composition are affected.

## Findings

No Blocking findings. Three Important findings require a fix or an explicit
recorded decision before proceeding. One Advisory finding is also recorded.
File references below are relative to the named repository at its reviewed head.

### Important I1 — A missing rollout path panics the new activity reader

**General; risk/compatibility.** `codex-web`, commit `f684f843`,
`codex/activity_history.go:135-158`.

`pageFile("")` explicitly returns `(nil, nil)` (`codex/thread_page.go:145`).
`readActivityHistory` therefore passes its error branch, enters cache reset, and
calls `file.Size()` on a nil interface at line 158. A `thread/read` result with
the correct ID and a null or absent path reaches this code through `ReadActivity`.
The protocol permits a null path; the repository's ephemeral fixture also uses
`ephemeral: true, path: nil` (`codex/ephemeral_test.go:113`). Even if the portal
normally selects only persisted threads, the exported HistoryReader option must
not turn an unavailable source into a process panic. A background observation
goroutine does not have the HTTP server's panic recovery.

Smallest remedy: explicitly reject an absent/nonpersistent source before creating
the filesystem-backed cache, returning a descriptive activity-unavailable error.
That does not require adding ephemeral-history support. If existing valid
nonpersistent activity reads must be retained, use a deliberately uncached path
over the isolated reader; do not silently move bulk reads back onto the live
transport. Add a focused nil-path test and retain the existing exact
fresh-unmaterialized-thread exception. This is source-proven; I did not execute a
new Go panic reproduction or edit source files.

### Important I2 — A rejected turn page can permanently hide a new turn

**General; risk/compatibility.** `codex-web`, commit `f684f843`,
`codex/activity_history.go:199-224`.

The `update` closure changes `h.turns` while validating each row, but only appends
new IDs to `h.order` after validating the entire page. An error on a later row
leaves earlier new IDs in the map without an order entry. A subsequent valid
response sees those IDs as existing, so it never inserts them into `h.order`.
All item loading and returned snapshots iterate `h.order`.

Concrete retry sequence: start with a warmed, retained history containing
`old`; receive a head page `[new(valid), old(invalid status)]`; then receive
`[new(valid), old(valid)]`. The first page passes the anchor-ID comparison but
fails `pageTurn(old)` after storing `new`. The next successful read still returns
only `old`, can report complete counts, and can present the old completed turn
as current while `new` is active. Watched histories retain the damaged cache
across the error. This makes a rejected response poison later valid results.

Smallest remedy: validate and normalize the entire page into temporary values,
including duplicate checks, before mutating either map or ordering. Alternatively
discard the affected cache on any page-validation failure. Add a focused test
for a warmed retained cache, rejected later row, then a valid retry, proving that
the new turn appears exactly once with correct counts/current status. No new
protocol or persistence contract is needed.

### Important I3 — Some browser status consumers still treat stale data as live

**General; risk/compatibility.** `dev-workspace`, commit `862c9dcf`,
`portal/internal/web/static/app.js:390-435` and `:3486-3493`.

The backend now deliberately returns the last good snapshot with `stale: true`.
The focused status helper handles this, but `teamWorkPresentation` checks only
the observation timestamp. For a failure shortly after a successful read it
still reports the member as currently working with `stale: false`.
`teamActivityPresentation` marks the statistics partial but continues to label
the row `Active`, `Idle`, or `Sleeping`; that label can persist through repeated
failures. `updateCodexWaitingIndicator` likewise checks the browser receipt clock
without checking `activitySnapshot.stale`, so a newly delivered stale response
can retain its waiting indicator despite the unavailable status label.

Confirmed directly in the repository's Nix environment with the exported JS
helpers: `{stale:true,currentState:"working",observedAtMs:Date.now()}` produced
row `activity: "Active"` and a team banner with `stale:false`,
`label:"implementer0 is working"`. This was a small read-only Node invocation,
not a long suite.

Smallest remedy: propagate the explicit stale flag through the team status
helpers and the waiting-indicator gate. Retain historical counts/times with an
unavailable status; do not discard useful last-good statistics. Add focused
browser contracts for a newly stale snapshot whose observation age is still
inside the freshness budget. The server-side attention path correctly rejects
`Stale`, so I did not find a stale-notification bypass.

### Advisory A1 — Legacy recent transcripts put turn failure before its items

**General; compatibility.** `codex-web`, commit `f684f843`,
`codex/history_reader.go:164-203`.

The new `readRecentThread` appends `pageFailure(turn)` before the ascending item
pages. The existing `transcriptEntries` appends the same turn failure after its
items (`codex/client.go:4073`). Consequently enabling HistoryReader changes the
compatibility `ReadThread` / HTTP `thread` order from `[prompt, response, error]`
to `[error, prompt, response]`. The paged browser path is separate.

Move the failure append after the turn's item loop and check a failed turn with
at least one item. This preserves the stated recent-transcript compatibility
without changing pagination.

## Exact reviewed ranges and history conclusion

| Repository | Base | Head | Complete series |
| --- | --- | --- | --- |
| codex-web | `c9aa6dc2f8cd6e80eeb711a3f9c569e08b7b2016` | `f684f843123aab9fc30e769ddb77b4a5a1ae1326` | `f684f843` |
| dev-workspace | `4e7ff517e1cac52c3cc8bb08f2a6a5ca21d3715b` | `862c9dcf8be8f22fe717df250bf9128e662456e5` | `7b64dc92`, `862c9dcf` |
| workspace | `60fd9da5a6f72d926c97db0f3921f3520eb5ccc9` | `01d1fe0bcad054054d077bfd138a24784de3d9b1` | `01d1fe0b` |
| vpsfree-cz-configuration | `206f3025c0142865ed516283eaf5c2f298a6e6cf` | `f789cd8be941e9e6d0c944c2f24a31c1580f51e5` | `f789cd8b` |

I independently inspected each complete commit series, commit message, changed
file inventory and final diff, and confirmed the worktree heads and merge bases
against the local remote-default refs. The packet's diffs match Git; the workspace
packet merely omits one trailing blank context line. Feature worktrees were clean
at inspection. This is a review of these frozen ranges, not later heads or a
freshness guarantee for remote branches at integration time.

**Whole-branch history is coherent: no obsolete unmerged approaches or redundant
follow-up commits remain in these ranges.** The runtime's catalog/recovery change
is independently separated from its history adoption. The provider's transport,
paging and incremental activity work form the same long-history capability; the
runtime's corresponding pin and adoption are coupled by the new API types and
freshness semantics. Tests/documentation support those behaviors. The final
fixes should be folded into these owning unmerged commits.

**Pin streams are consolidated.** There is one codex-web selection in the runtime
(flake revision, Go module and vendor hash); one matching nested runtime selection
in the workspace; and one generated `dev-workspace` / `devWorkspace` channel
update in configuration. All select the reviewed provider/runtime heads. I found
no retained intermediate updates requiring a release or consumer boundary.
Transitive codex-web changes in the two composed locks are expected; the site
extension revision and follows graph are unchanged. The configuration channel
mapping is present in its `flake.nix`.

**No migrations.** The complete changed-file inventory contains no database or
on-disk format migration and no changed persisted schema. There is therefore no
migration version requiring merge, release, deployment or external-use provenance.
The review does not authorize rewriting previously merged history.

## Architecture, compatibility, and remaining verification

The owning boundaries are appropriate: codex-web owns passive history transport,
item paging and activity projection; dev-workspace owns the process-local catalog,
recovery admission and display freshness. Both runtime client construction sites
receive the shared pool, and the application closes it after its consumers.
The nil-option path retains the existing public client transport. Existing
capability/origin checks remain in the HTTP resolver. Cached recovery-owner
discovery is followed by a direct current manifest, lifecycle-journal, recovery
record and socket-epoch check; cache values are cloned. I found no new remote
authorization bypass within the documented trusted-local-operator boundary.

The two connections and per-request slots bound transport concurrency. Adaptive
item limits retry the same cursor, and the selected websocket dependency exposes
the recognized oversize error. Persisted recovery/activity formats and Codex
version are unchanged. Old/new software therefore has no new state migration;
the matching configuration and composed application selection still need the
documented system-then-profile deployment and coordinator recovery rules.
No coordinated vpsAdminOS fleet update is introduced.

README history guidance and the runtime portal guide describe lasting behavior
in the owning projects; rollout-specific evidence stays in the initiative.
No documentation framework, compatibility shim, or generalized registry is
needed to fix the findings.

I inspected the focused tests but did not independently rerun the full Go suite,
packaged checks, native App Server tests or deployment. Existing synthetic
100,001-turn aggregation coverage is not an end-to-end 100,001-turn backfill.
Post-remediation verification should exercise the actual new HistoryReader path
for cold multi-page progress, fork/revert invalidation, cancellation/retry,
single-item oversize isolation, live watch/send/approval continuity, and stale
team display. The new fork-cache test proves an append but does not exercise a
revert through that cache. The live CPU, latency and ten-minute transport targets
remain unproved. Another initiative's machine reservation must remain respected.

The listed remedies are narrow corrections within the reviewed design. Focused
verification and direct lead inspection can close them under the review skill;
a new design for filesystem-less history or a broader contract change would
require review of the affected lanes. Integration readiness remains conditional
on reconciliation, required checks, current-head history/pin validation, and the
authorized deployment acceptance work.
