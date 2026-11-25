# Bounded active-session sample

Package E, implementer2, 2026-11-25 approximately 09:55–10:02 UTC. Read-only
sample of three active Full-team sessions, selected for contrasting planning,
bounded runtime correction/rollout, and multi-day runtime recovery scopes.
No cross-session messaging, worktree commands, source-session mutations, telemetry
tools or new timing collector.

## Sensitivity and evidence limits

All three sources were verified ordinary before retaining this report: their
private sensitivity records are absent in the workspace-specific
`sensitive-sessions` directory; installed `workspace-sensitive-sessions.rb`
defines absence as ordinary. Their manifests do not mark them sensitive.
Embedded peer diagnostic material is excluded from this report. Own identity
remained `2026-11-25-team-lead-delegation` / implementer2 throughout.

Sources: existing `codex-teams` rosters, portal `activity-final` snapshots,
session state/package tables, and bounded lead transcript excerpts. Timing is
approximate and snapshots differ by seconds. No clocks are summed or interpreted
as a speedup, utilization target, complete elapsed time or proof of duplication.
Runtime `workingMs` is observed thread work, not a classified breakdown of
reasoning, command execution or substantive engineering. Missing intervals remain
unknown. No exhaustive transcript classification was attempted.

## Working-time context

Minutes, rounded to one decimal. All populated role clocks below report incomplete
coverage and “Some turn time was not observed.” Each role has its own start.

| Source / role | Working | Waiting | Unclassified | Coverage start UTC → snapshot UTC |
| --- | ---: | ---: | ---: | --- |
| backup-disable-design / lead | 24.4 | 5.0 | 0.1 | Nov 25 09:23:06 → 10:00:06 |
| backup-disable-design / architect0 | 10.6 | 0 | 15.0 | Nov 25 09:46:23 → 10:00:12 |
| backup-disable-design / observer0 | 2.6 | 0 | 0.1 | Nov 25 09:38:31 → 09:59:56 |
| pi-message-delivery / lead | 1053.3 | 228.6 | 3.1 | Nov 23 22:59:52 → Nov 25 10:00:22 |
| pi-message-delivery / architect0 | 338.0 | 9.0 | 7.7 | Nov 23 23:02:10 → Nov 25 09:59:55 |
| pi-message-delivery / implementer0 | 594.8 | 8.8 | 35.0 | Nov 23 23:03:55 → Nov 25 10:00:22 |
| pi-message-delivery / implementer1 | 423.1 | 13.3 | 15.4 | Nov 23 23:05:30 → Nov 25 10:00:12 |
| pi-message-delivery / reviewer0 | 87.0 | 3.3 | 6.3 | Nov 24 01:49:10 → Nov 25 10:00:22 |
| pi-message-delivery / observer0 | 78.1 | 0 | 5.3 | Nov 23 23:16:35 → Nov 25 10:00:22 |

Backup-disable-design implementer0–3 and reviewer0 show zero work at 09:54:28,
with no coverage start. This matches their unreleased/unassigned packages; it
does not establish that they should have been executing. Architect coverage
begins at D2 and includes 15 minutes unclassified, so its clock cannot support
a complete D1+D2 comparison with the lead.

For monitor-session-ownership the retained roster/backend is Pi, with no Codex
thread clocks. Comparable runtime timing was not obtained in this bounded read;
working time by role is unavailable. Do not treat that absence as zero.

## Concrete observations

1. **Planning scope explains idle implementers.**
   [backup-disable-design state](../2026-11-25-backup-disable-design/state.md)
   records a design/implementation-plan request, not authorization to implement.
   D2 was dispatched at 09:46:23. Architect completion arrived at 09:56:51.232;
   lead publicly accepted at 09:56:59.273, about eight seconds later. Proposed
   implementation packages correctly remain unreleased. This proves a prompt
   D2 acceptance, not an implementation allocation delay.

2. **There is a bounded example of lead substantive work alongside its owner.**
   In that lead transcript, while D2 design was assigned to architect0, the lead
   wrote the implementation plan at 09:47:42, added UI interaction text at
   09:48:03, refined preservation/cleanup semantics at 09:49:23, and inspected
   transfer confirmation source at 09:52:06. The user then explicitly directed
   “delegate work to team members, do not duplicate their work, just coordinate”
   at 09:52:40. The lead transferred final plan ownership to the architect.
   Earlier D1 also included repeated draft reads at 09:34, 09:35, 09:37 and
   09:38 before acceptance. These are concrete opportunities to narrow lead
   planning/inspection, but targeted source checks can be acceptance work;
   this sample does not quantify wasted time or prove every read redundant.

3. **A short, well-evidenced delegation sequence exists.**
   [monitor-session-ownership state](../2026-11-24-monitor-session-ownership/state.md)
   records architect dispatch 16:35 → design accepted 16:44 → implementer
   dispatched 16:44 → quick-check handoff 17:01 → remediation 17:10 → native
   evidence accepted 17:21 (Nov 24 UTC). Minute resolution cannot establish
   subminute delays; no avoidable allocation gap is demonstrated. Later paired
   configuration/runtime artifacts and helper compatibility create real ordered
   dependencies. No role-clock comparison is available for this source.

4. **Longer lead clocks coexist with appropriate delegation and dependencies.**
   [pi-message-delivery state](../2026-11-23-pi-message-delivery/state.md) spans
   multiple implementation, review, compatibility and deployment phases, so its
   whole-session clocks are not comparable with the planning-only example.
   In the sampled recent lead transcript, the architect supplied routine
   implementation clarifications directly and settled the CLI wire at 09:52:01;
   the CLI owner reported receipt at 09:52:32. The core owner reported a compiling
   checkpoint and an explicit short source/index handoff at 09:53:42. CLI focused
   checks and commit were reported complete at 09:57:40 and acknowledged by the
   lead at 09:57:56. This supports parallel delegated work with a legitimate
   compiling-interface dependency and sequenced mutation window. It does not
   prove all earlier lead time was necessary or duplicative. Public acknowledgment
   is not by itself an exact internal acceptance timestamp.

## Instruction improvements supported by this sample

- Assign substantive implementation-plan authorship with design ownership from
  the start; the lead keeps scope, package allocation, acceptance and user text
  that its retained instructions require. Avoid a parallel technical plan.
- Inspect the owner's completion packet and a bounded set of consequential
  claims for acceptance. If a technical gap remains, return that exact question
  to the owner instead of repeatedly reading incomplete drafts or starting a
  second investigation. Keep necessary independent review intact.
- Record why a package is unreleased: requested scope, unresolved contract,
  permission/recovery invariant or shared-resource conflict. A live roster and
  zero clocks do not create work authorization or independent capacity.
- Prefer direct routine architect/implementer clarification and short explicit
  source/index handoffs once the relevant interface compiles; keep the lead on
  scope, ownership and consequential decisions. Preserve unknown timestamps and
  coverage gaps when assessing dispatch or acceptance delay.

No broad causal claim, timing target or new measurement system is justified by
three selected sessions. This is investigation evidence, not a reviewed product
deliverable. No commits or application-source changes were made for this package.
