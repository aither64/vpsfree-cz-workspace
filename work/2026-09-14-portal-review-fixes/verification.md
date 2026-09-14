# Portal fixes: validation and deployment

Deployed to aitherdev from the feature branches on 14 September 2026.

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

## Evidence

- Focused Go, Node and editor regression tests pass, including the real file,
  newline handling, exact line counts and the 2000/2001-line boundary.
- Provider Go race-detector tests pass. A real WebSocket regression rejects an
  old claimed answer when the request ID is reused before the write.
- Browser repository acceptance passes 29 scenarios, including delayed history
  responses, lazy content, collapsible files and bounded editor mounts.
- Question browser acceptance covers recovery, drafts, snoozes, focus,
  attachments and five viewport sizes.
- Chromium and Firefox pass artifact download, hidden-tab timing, navigation
  cancellation and back-navigation recovery checks.
- Runtime packaged checks, the NixOS activation/rollback VM and the workspace
  deployment contract pass.
- An isolated Codex 0.154.0 App Server passes its fresh-thread contract.
- Deployed browser checks confirm the original file's counts, both layouts,
  collapse controls, sidebar settings and safe answer recovery. The answer test
  used isolated HTTP fixtures; no answer was sent to a shared conversation.
- Visual inspection confirms aligned Split context and compact Unified output;
  screenshots are available in the session artifacts.

Provider, runtime and organization CI all pass at the revisions below.

## Revisions

| Component | Feature head |
| --- | --- |
| codex-web | `882c88ccfbebfb646fb2cafbe9bc6790141b2d13` |
| dev-workspace | `b837f0d974a98857daef7e4cc09d8f3039a059a0` |
| vpsfree-dev-workspace | `f6050a4d661be7c923518e0b962a4372ebad7f50` |
| workspace | `1c3f3e156cad0f84090ec1934acbb867eb723345` |

All four mandatory review lanes ran with fresh gpt-6-astra/xhigh reviewers.
Findings and remediation decisions are recorded in state.md and review/.
Feature branches and worktrees remain open for review and integration.
