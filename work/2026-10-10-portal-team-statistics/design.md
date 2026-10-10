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
unclassified. Wall-clock work includes ordinary tool execution, excluding explicit
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
