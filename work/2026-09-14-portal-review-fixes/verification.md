# Portal fixes: validation and deployment

Deployed to aitherdev from the feature branches on 14 September 2026, including
the final mobile heading correction. Reload an open portal page to load the UI.
The Codex process kept running through activation.

The reported `oauth2_config.rb` at commit
`7159fec1390e04156836797cfae1206b99d71531` renders **116 added and 6 removed
lines** in both Unified and Split on the deployed portal. Git supplies changed
line ranges; the editor only adds character highlighting inside those ranges.

Unified is the default. Explicit and saved Split choices are preserved. File
diffs can be collapsed, and diffs above 2000 changed lines load on request.
Explicit file and line links open the requested content.

Repository histories refresh automatically after branch movement; delayed
responses cannot replace newer histories. Open comparisons retain their chosen
revisions until refreshed. Navigation cancels obsolete page reads, while timing
keeps its last value during short recovery after returning to an inactive tab.

Question failures appear inline and retain drafts. An answer is retried once
only after a response confirmed as not sent and restoration of the same question.
Unknown delivery and changed questions are never retried automatically. Snooze
state belongs to each offer, and Refresh question can retry a failed snooze.
Secret answer values remain in memory only.

Automatic archival is under **Session settings** in the left sidebar. The
installed mandatory review instructions use **gpt-6-astra**, with **xhigh**.

The presentation follow-up keeps each file heading visible within the scrolling
comparison, including Unified, Split and full-file views. Linked lines remain
below the heading. While a comparison is open, the session sidebar shrinks to
58px automatically; overview and other tabs restore its normal 250px width.
The file tree stays available, and mobile navigation keeps its existing layout.

Automatic archival uses labelled policy, rule, last-check and conditional
“Not before” values. Readable blockers appear separately; complete CLI diagnostics
are available in a closed **Technical details** section. Failed reads preserve
the last settings, and failed Keep open saves retain the error and confirmed
checkbox value. These changes do not alter archival decisions or stored state.

## Evidence

- Focused Go, Node and editor regression tests pass, including the real file,
  newline handling, exact line counts and the 2000/2001-line boundary.
- Provider Go race-detector tests pass. A real WebSocket regression rejects an
  old claimed answer when the request ID is reused before the write.
- Browser repository acceptance passes 31 scenarios in Chromium and Firefox,
  including delayed history responses, lazy content, collapsible files, sticky headings, linked-line
  visibility and bounded editor mounts.
- Question browser acceptance covers recovery, drafts, snoozes, focus,
  attachments and five viewport sizes.
- Chromium and Firefox pass artifact download, hidden-tab timing, navigation
  cancellation and back-navigation recovery checks.
- Real-template presentation checks pass in Chromium and Firefox, including
  sidebar resizing, keyboard focus and history, mobile/index limits popovers,
  formatted settings, failed reads and failed Keep open saves.
- Runtime packaged checks, the NixOS activation/rollback VM and the workspace
  deployment contract pass.
- An isolated Codex 0.154.0 App Server passes its fresh-thread contract.
- Deployed browser checks confirm the original file's counts, both layouts,
  collapse controls, sidebar settings and safe answer recovery. The answer test
  used isolated HTTP fixtures; no answer was sent to a shared conversation.
- Visual inspection confirms aligned Split context, compact Unified output,
  sticky headers and the compact mobile heading. Updated screenshots are
  available in the session artifacts.

Provider, runtime and organization CI all pass at the final revisions:
[provider](https://github.com/aither64/codex-web/actions/runs/34878642980),
[runtime](https://github.com/aither64/dev-workspace/actions/runs/34888828914),
[organization](https://github.com/vpsfreecz/dev-workspace/actions/runs/34888892734).
The organization run includes the development-cluster check.

## Revisions

| Component | Feature head |
| --- | --- |
| codex-web | `882c88ccfbebfb646fb2cafbe9bc6790141b2d13` |
| dev-workspace | `227bcfc1b989407582d3b022f8b388ac29972c16` |
| vpsfree-dev-workspace | `08d691cfd239260ce5bf7c269a44a49ce8de41e7` |
| workspace | `d53014fd4b589a9de56febfc880aae7c4179b11c` |

All four mandatory review lanes ran with fresh gpt-6-astra/xhigh reviewers.
Findings and remediation decisions are recorded in state.md, review/ and
review-presentation/. The presentation follow-up completed all four lanes;
the bounded CI diagnostic/test correction completed General and Architecture
reruns without findings.

An intermittent history-count fixture failure was investigated from its failed
CI logs and local repetitions. New diagnostics retained a Git object-read error;
automatic commit-graph maintenance ran at the same boundary. This supports, but
does not prove, a maintenance race. Maintenance is disabled only in the disposable
fixture, matching another bulk Git fixture. All 50 subsequent repetitions and
the complete repository suite pass. Production Git configuration is unchanged,
and future failures retain Git's bounded stderr.

Feature branches and worktrees remain open for review and integration.
