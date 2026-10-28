# Additional user feedback review

Review the committed runtime delta94a98a2a..HEAD in owned dev-workspace worktree.
User found an outbound delivered CLI message in Communication but none in Codex
Sessions. User also requested no message bodies in Settings, only counters.
Design section Follow-up: durable communication in the Codex view records scope.

Use all four mandatory lanes (general, architecture, scope, risk) on this bounded
addition; retain your completed whole-branch feedback review as context. Read
relevant repo AGENTS; remain read-only, no nested agents or long tests.

The existing GET communication view feeds a render-only projection into All and
Sessions. Native history/paging/acknowledgements stay unchanged. Stable IDs,
delivery status, sender/recipient, timestamps; dedup received native client IDs
or recognized exact message envelope IDs. Lead-only projection; member views
retain their own conversation. Safe text rendering. Visible-view polling and
read failures retain prior messages with warning. Settings permissions plus
sent/received counters; received counts delivered entries only.

Quick Node composer contracts pass including pure projection checks for CLI-only
message, incoming dedup, member exclusion, status update and immutable native
rows. JS syntax and diff checks pass. Browser tests extended for actual new
render/fetch/counter behavior; these await your review. Runtime docs updated.
No new migration/state/API or configuration contract. No additional pin stream;
final downstream pins will be mechanically refreshed/consolidated after this
review. Current unmerged history adds one coherent commit for this user feedback.

Separately diagnosed why sender used CLI: trace searched installed communication
files then ran CLI allow/send; no recorded MCP discovery/call. Tool registration
is present. Retained developer rollout records lack session_communication; this
is insufficient to prove exact model-visible updated policy. Do not invent a
policy refresh fix or mutate that session.

## Formatted-message follow-up

Review dc39a627..f199947c4c0d2c5d96f4f663053ff5a592946ef4 in all four affected lanes.
The user reported only tool cards and requested formatted actual message bodies.
The communication GET now adds sanitized HTML using the existing Markdown
renderer; storage remains unchanged. The UI renders message body separately
from delivery status and omits communication tool rows in Sessions. All retains
tool diagnostics alongside the durable messages. Quick Go communication/API
tests and Node composer/projection contracts passed; API test covers Markdown
and script stripping. Browser test asserts formatting, labels, status and no
tool row in Sessions. No migrations. Overall high risk remains from the prior
feature; this bounded addition touches the remote-content rendering boundary.
Read docs/session-communication.md for the reconciled explanation. Final pins
remain mechanical and will be consolidated to this final runtime revision.

## Final pin and history inventory

dev-workspace: 4a002f52c3b55099540aa99708d5fcf29f7b2456..f199947c4c0d2c5d96f4f663053ff5a592946ef4

cc106266 communication: allow user-approved exchanges between session leads
e9153e61 portal: distinguish communication between sessions in the transcript
d0a9c5f6 codex: retain retry proof after explicit recovery sends
fd9128a1 portal: allow dropping pending sends without retrying
f9d8e4fe portal: organize session settings into content tabs
f199947c portal: display durable session messages in the Codex transcript

workspace: 8b44caceadfed7e175cf181f46000334567cb9c3..c4cd85c78a0faebd174435fe442eddd29da7e360

7cbd43d74 workspace: define approved cooperation between session leads
c4cd85c78 inputs: select approved session communication runtime

vpsfree-cz-configuration: 4715580512a4042bea75cb44167efb42b3618f70..ed3b0ea7fef99d82e683aee832ea6663c1c679d7

ed3b0ea7 inputs: set devWorkspace to f199947c

Both deployment pin streams contain one final update selecting f199947c.
Configuration uses the deployed predecessor base to avoid unrelated OS/dependency
updates; upstream was fetched. No migrations or new contracts in the pin refresh.
Composition checker passed, hooks passed, all feature heads published. Please
confirm final history consolidation under general lane; prior substantive reviews
remain applicable. No default branch integration authorized.
