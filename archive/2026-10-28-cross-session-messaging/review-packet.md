# Final review: cross-session communication

User requests user-approved cross-session cooperation, existing leads, no new
role. Approval from either side authorizes both directions; chat approval is
lead policy under the trusted local operator model, not semantic verification.
Runtime grants enforce pair/identity boundaries. No auto forwarding or loops.
User authorized implementation, tracking and aitherdev deployment, not merges.

Review all lanes: general, architecture, scope/proportionality, risk/compatibility.
Risk is high: authorization, durable messages, lifecycle and package transitions.
Use /home/aither/.codex/skills/mandatory-change-review/SKILL.md and every lane
reference. Read workspace AGENTS and relevant procedures and each repository's
AGENTS before reviewing. Remain read-only; do not start long integration tests.
No nested agents. Report concrete findings, accepted boundary, gaps, and explicit
whole-branch history and migration conclusions.

Initiative: 2026-10-28-cross-session-messaging. Shared tracking at
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-cross-session-messaging
contains plan.md, design.md and state.md. Both feature worktrees are under
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-cross-session-messaging.

Review ranges (record exact HEADs in your report):
- dev-workspace: 4a002f52c3b55099540aa99708d5fcf29f7b2456..HEAD, one feature commit.
- workspace: 60ed89b75c44892d4143e0423fa1ab2b0625baca..HEAD, one guidance commit.
Use git log and git diff for the complete series/diffs. No obsolete approaches or
repeated update streams remain. No migrations: additive private schema-1 file;
never merged, deployed, released or externally consumed. No intermediate schema.
Runtime behavior and its tests/docs are one commit because each interface is a
consumer of the same grant/delivery contract. Guidance is independently committed.

Acceptance: allow A-B from A; exchange both ways without another approval; hold
stopped/approval-waiting recipients; resume through ordinary controls; revoke
from B; refuse new sends; no grant inheritance through archive/revive/fork/reuse.
Preserve model, effort, collaboration mode, saved lead policy and current task.
Reconcile uncertain native receipts without duplicate delivery or post-revocation
new sends. Browser grants require ordinary portal origin/authentication policy.

Owners/consumers: generic dev-workspace owns Go service, private store, MCP,
Ruby CLI/lifecycle hooks, portal worker/API/UI and package compatibility checks.
It consumes existing pinned codex-web SendWithOptions/ReconcileSendWithOptions.
Workspace and vpsfree-cz-configuration select matching generic runtime revisions;
no codex-web or extension changes. Runtime docs/session-communication.md owns
behavior, docs/session-communication-upgrade.md upgrade/recovery; README, session
and portal guides link them. Workspace docs/agent-teams.md and AGENTS define the
narrow exception to session ownership rules. No member role changes.

Mechanical deployment pins will be prepared after publishing the reviewed
runtime revision: workspace nested vpsfree-dev-workspace/dev-workspace URL/lock
and configuration dev-workspace channel devWorkspace role. They will retain one
final update per stream and receive final history confirmation. System before
application, no reboot, held aitherdev machine claim. No default integration.

Quick checks passed: focused communication/native/portal/MCP/registration Go
checks; CLI and host reporting transition Ruby tests; Ruby/JS syntax; diff check.
Browser regression added to existing Playwright harness, not yet executed.
Package/native and archive/creation VM acceptance follow this final review.

Reviewer: standalone gpt-6.1-sol/xhigh from installed default delegated team's
review-purpose role, catalog digest
495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7.
Fallback because the registered operational session is threadless with no roster.

## Final mechanical deployment pins

Runtime final e9a5fc729438abbcc84c54af92d04a3f9a2d86fb differs from accepted
d812fe68 only by the requested candidate-upgrade documentation correction.
Full runtime range is still 4a002f52..e9a5fc72, one feature commit.
Workspace final 39e6b7ac61a9c7a10d25a654908283fb99b30eb0: full range
60ed89b75..39e6b7ac6 is the previously reviewed fecd5aed guidance commit plus one
nested runtime URL/lock pin. Configuration final
32f1aee06f9dc6e365e386a75bceb4e43df42dc4: one generated confctl devWorkspace
channel pin from its immediate predecessor 47155805.
Both pins select e9a5fc72, extension and sibling inputs unchanged. Composition
checker passed. No repeated streams, superseded pins, or new migrations.
Confirm whole-branch history and exact composed pin boundary only; mechanical
content is exempt from another full content review. No substantive scope change.

## User-requested transcript follow-up

User explicitly asked for a distinct color in the Codex tab and a filter beside
All/Messages/Team/Activity. Runtime 93bc779241a1e826226a9c338323bb48c09dc585 adds
amber presentation and a Sessions filter, includes incoming envelopes and
outgoing communication tool calls. Uses existing application-supplied opaque
communication metadata; no codex-web change or new dependency is necessary.
Quick TestCommunication and TestShippedBrowserClientMatchesSessionAPI checks,
Node syntax and git diff --check pass. Browser regression now covers colors,
labels and filters as well as grant controls; execution follows review.

Core runtime e1b6dc67 differs from the accepted e9a5fc72 only by the restored
legacy argv guard/absent-contract handling (libexec/workspace-host) and one
policy-2 archive test fixture. Six focused host tests pass, 20 assertions. This
fix came from full package tests, not a new public contract. Prior accepted
capacity fix and narrow documentation correction remain in the same core
commit. Full runtime range 4a002f52..93bc7792 contains two coherent commits:
core communication, and the later explicitly requested transcript presentation.
No new migrations or obsolete approaches. Final pins will select 93bc7792,
consolidated to one update per workspace/configuration stream.

The original independent v2 reviewer completed its reviews but available native
follow-up rejected direct app-server input for v2 agents. A fresh standalone
reviewer of the same installed model/effort is used for this user-added UI
package and final history/pin confirmation. Retain prior reports as evidence;
review the new UI scope, the narrow legacy compatibility correction, and final
complete history/pin streams. Do not repeat previously accepted core code review
unless these diffs create a concrete concern. All four lanes apply to the full
feature; focus new lane work on the changed boundary. Read-only, no nested agents.

Final ranges for supplemental review:
- runtime 4a002f52c3b55099540aa99708d5fcf29f7b2456..93bc779241a1e826226a9c338323bb48c09dc585
- workspace 60ed89b75c44892d4143e0423fa1ab2b0625baca..0d1fb52c589f80fe4fc2f9b49487feaca05d086a
- configuration 4715580512a4042bea75cb44167efb42b3618f70..944d7d3e (resolve full HEAD).
Workspace/configuration pin streams each consolidated to one final update;
intermediate e9/e1 pins were never deployed, released or externally consumed.
Both final locks select 93bc7792 and composition validation passes. Configuration
hook checks passed; generated changelog was consolidated to the complete final
4a002f52..93bc7792 range. No source changes are in progress.
