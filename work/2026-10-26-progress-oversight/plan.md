# Independent progress oversight and leaner verification

## Goal and decisions

Implement the accepted conversation plan: independent observer0 checks active
work every 15 minutes, challenges waste without adding an approval gate, and
shows a portal warning after the same concern persists across two checks.
New multi-member teams include the observer; existing sessions and Solo opt in.
Use GPT-6.1 Sol/xhigh, read-only development instructions, bounded context,
one check per session and a three-minute check deadline. Quiet healthy checks
must not wake the lead or sustain an idle session. Leads adjust or briefly
justify continuation at the next safe boundary. No reassignment, cancellation
of development work, or waiver of required checks belongs to the observer.

## Repositories and ownership

- dev-workspace: scheduler, compact durable state, reporting/dispositions,
  portal controls, behavioral tests and runtime documentation.
- workspace: team catalog/capacity, verification and lead instructions, matching
  policy checks and the final runtime input selection when needed.

This conversation created a tracking-only initiative through dev-session start
--no-codex. It owns this initiative; no managed team/lead thread exists. The
current lead owns design and implementation using ordinary supported settings.
Mandatory final review and long-check utilities follow the installed site policy.
The two example sessions are read-only investigation sources and remain untouched.

## Compatibility and rollout

Use existing general-purpose roles and same-session delivery. Preserve roster,
lifecycle, submission and Codex protocol formats. Keep progress-specific state
separate and optional; missing observer/state leaves older sessions unchanged.
No database migrations, API/client changes for developed projects, node updates,
Codex upgrade, system configuration deployment or production change is needed.
The user authorized implementation, not default-branch integration or live
profile activation. Prepare reviewed feature branches and a disposable pilot.
Runtime functionality must precede enabling the new catalog defaults. Existing
package-generation and forward-recovery contracts remain authoritative.

## Verification and documentation

Focused fake-clock scheduler/state tests, API/portal interaction tests and team
catalog tests cover behavior. Check restart deduplication, unavailable observers,
idle/lifecycle exclusion, timeout ownership, quiet success, recurring concerns,
lead disposition and old rosters. Use representative excessive-bookkeeping and
justified-long-check scenarios. Complete quick checks, commit, independent final
whole-branch review, then applicable longer checks/pilot. Preserve normal hooks.
Keep command/revision/result/log evidence concise. Runtime behavior belongs in
its session/portal guides; site policy belongs in workspace guidance.
