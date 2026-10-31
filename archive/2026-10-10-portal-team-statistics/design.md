# Team activity and settings design

The lead owns this design. The accepted plan in plan.md defines product scope.

## Activity

codex-web owns generic thread activity, pagination and item classification.
Extend ActivitySnapshot additively with aggregate sent/received/tool counts,
idle timing, count coverage, and current wait reason/deadline. Preserve existing
latest-turn count fields. Full history is summarized per distinct item ID without
retaining message content. Only own turns contribute after a fork.

The recorder observes item/started and item/completed for sleep and collaboration
waits. An explicit wait is waiting even when native runtime status says idle.
Blocking user requests take precedence in presentation; overlap counts once.
Turn completion clears open wait state. Missing/reconnect evidence remains
unclassified. Ongoing collaboration waits can be restored from native item
status. Sleep history has no lifecycle status: if its turn start was missed,
ambiguous time remains unclassified until fresh native active status establishes
current work. Coverage starts at that boundary; earlier gaps remain unknown. An
observed wait still counts as waiting. Wall-clock work includes ordinary tool execution, excluding explicit
waits; it is not model or CPU time. Idle is bounded by the owning member/thread
creation and removal boundaries. Do not accrue idle after removal.

dev-workspace expands the existing activity monitor to trusted ready member
threads, retaining four-wide RPC admission and per-thread gates. A dedicated
GET /api/sessions/<slug>/team-stats returns lead/member snapshots and per-member
diagnostics. Browser input never selects thread IDs or sockets. Removed members
retain their final snapshot. Held sessions use cold reads and never implicit resume.
Statistics update their own cells, preserving edited roster settings and focus.
Stale observations remain visible but projected timers stop.

## Model choices

Model/effort editing depends on session authorization and catalog validity, not
busy/idle or systemError status. Collaboration-mode controls retain their old gate.
Loaded threads use thread/settings/update and confirm subsequent-turn defaults.
The UI says when saved defaults affect the next turn.

Held/stopped changes remain durable without resume. Member roster is authoritative
for desired member settings; a private root-setting record binds workspace, slug,
root and exact thread identity. Apply retained choices through explicit activation
settings before native queues/goals run. Keep mutation locks and generation checks;
latest saved choices win and stale reads do not undo confirmed edits. Preserve
pending choices on transport failures and reconcile uncertain application.

## Compatibility, deployment and recovery

Preserve lifecycle/recovery/receipt schemas; use additive generic APIs and isolated
private records for optional feature state. Existing records missing new metadata
produce partial snapshots and can be backfilled. Existing forward-only profile
policy remains enforced; recover failed rollout with a compatible newer package.
Keep the selected native Codex unchanged so live-switch compatibility remains
available. Match the runtime selection in workspace and configuration; preserve
extension and unrelated flake inputs. Exact prepared and executed rollout evidence
belongs in rollout.md, not permanent feature docs.

## Acceptance and verification

All retained rows show independent activity and lifetime totals. Sleeping/waiting
never asks for instructions unless a genuine blocking prompt exists. Models can
be saved during active/error/held states and take effect on the next permitted turn.
No stats read, held save or observer activates stopped work.

Quick: focused Go and browser contracts in repository Nix shells, formatting,
protocol request corpus and composition checks. Independent final review includes
whole-branch history, new state/compatibility and documentation. Long checks after
review: packaged flakes and live isolated App Server/browser acceptance, delegated
to the utility watcher. Deploy only the owned composed candidate and aitherdev
configuration, then verify endpoint behavior and preserved runtime generation.

## Verification prerequisite repair

The workspace base already exceeds its 16 KiB core instruction headroom check.
Route branch readiness explicitly to the Git procedure and retain a concise core
summary. Preserve all existing gates in the procedure; no runtime, persisted
state, native policy, profile transition or deployment contract changes. Existing
agent instruction tests provide the quick acceptance check. Independent general
review precedes resuming the composed build.

## Compact-table and reconnect correction

The lead owns this accepted follow-up. No retained team exists for this tracking-
only initiative. Use the existing activity API fields and metadata/settings
endpoints; preserve server-side trust resolution and the read-only team-thread
endpoint while removing its Team UI. Layout has ten columns; roster/access/thread
metadata shares Member. Numeric metrics remain separate and right-aligned. Thread
excerpts use first eight/last four characters, with full title and clipboard value.
Ready members and lead use a bounded shared model-settings popup controller. Team
popup is outside polled roster HTML and its target is fixed until it closes.
Uncertain settings writes reconcile against that target, preserving unsaved drafts.

A fresh native active notification/read or matching work lifecycle event establishes
current work from its observation boundary. In-memory evidence belongs only to
that connection and turn; history HasSleep cannot erase newly established evidence.
Known automatic and blocking waits take precedence, and activity never retroactively
assigns unknown coverage. Native idle during ambiguous sleep does not complete a
turn or ask the user for instructions. Disconnect clears observation evidence.
No migration or native version change is needed; old readers retain the same
activity/checkpoint contract. Rollout/recovery uses the prior compatible live
profile procedure, matching runtime selections and retained deployed source refs.

Quick checks: focused recorder tests, portal/helper tests and JS syntax. Required
final independent review covers the consolidated complete branch series. Longer
checks: packaged flakes, actual browser geometry at 1280 with normal sidebar, popup
target/save/stale/draft behavior, clipboard, add-form layout and selected native
protocol behavior. Live verification reads both named example sessions without
changing settings, starting inference or altering their ownership.


## Other team members working follow-up

Accepted on 2026-10-10: show a compact Codex-panel notice while the focused
member is idle or waiting. Include working, sleeping, waiting-for-team and
unclassified in-progress turns; exclude focused/removed/stopped/blocked members.
List three addresses then the remaining count. Preserve approval/answer requests,
replace idle waiting-for-instructions wording with Idle when others have ongoing
work, and suppress its attention dot. Existing team-stats API is shared with the
Team table every five visible seconds; stale observations after 15 seconds or a
failed read show unavailable status. No wire/persistence/provider change.

Tests cover member selection, automatic waits, blocked members, truncation,
completion, failed/delayed reads, page visibility, Chromium/Firefox and 1280/narrow
layouts. Update owning portal guide; quick checks, committed whole-branch review,
long browser/package/composition checks, then authorized aitherdev deployment.
Retain pins/provenance and branches; no default-branch integration authorization.
