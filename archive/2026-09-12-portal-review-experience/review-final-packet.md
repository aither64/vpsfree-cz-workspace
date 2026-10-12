# Final cache ownership and scheduling review

Use this packet with plan.md and review-delta-packet.md. The initial full review
and three first-delta lanes are complete; their reports are immutable evidence.
This pass covers the final committed repairs below and their interactions. Inspect
the exact series and final ranges, not uncommitted tracking records. Perform your
assigned review directly; no nested agents, code edits, Git mutations or tests.

General and risk findings about exact plan-journal recovery after source removal
and archived canonical access are directly repaired and verified by focused
regressions. A general/risk rerun is not required merely to confirm those narrow
fixes. Architecture reruns because unified cache ownership and authority-wide
read scheduling add previously unassessed behavior. Scope is the required first
review of the completed remediation design, including the final simplifications.
Both reviewers are fresh standalone gpt-5.6-sol/xhigh. Risk remains HIGH.

## Final repairs

History caches now have read/watch references under the existing short map mutex.
Queued readers pin the same per-thread gate, so last unsubscribe cannot replace
a cache that a reader still uses. Completed unwatched caches retire when the last
reader releases them. Only incomplete, unwatched histories can enter a bounded
eight-entry idle retry list; active reads/watches are never evicted. This preserves
progress after cancelled long backfills without retaining every archived history.
Recorder persistence and summary formats are unchanged by this repair.

The portal shares four cancellable read slots per App Server authority. Background
workers queue one verification/subscription/history operation at a time; their
notifications remain independently subscribed and coalesced. Browser history reads
use the same slots. The four-second worker RPC deadline starts after a slot is
obtained, so queued workers do not repeatedly expire before getting any work.
An established subscription is released if later thread/cwd validation fails.
Noninteractive pages retain their first successful snapshot, without continuous
polling or wall-clock projection. Failed/incomplete initial reads can still retry.

Creation retry no longer duplicates the strict Ruby fork-journal schema in Go.
The portal snapshots and validates fresh requests, then sends immutable validated
receipt/source/goal/settings arguments to the CLI. Ruby owns the exact destination
start/fork journal decision and retains source validation for fresh/no-journal
attempts. Matching destination journals recover without needing a still-live
source. Archived canonical destinations remain visible through exact evidence
or an explicit nonblocking archive notice. No CLI flag or persistent schema was
added. Existing completion evidence and canonical identity checks remain.

## Retention decision to assess

See review-reconciliation.md for the coordinator's evidence-based reconciliation
of the architecture Important/risk Advisory durable-retention finding. Existing
`dev-session delete` archives its Codex thread and preserves tracking/creation
state in private recovery storage; it does not purge the conversation. The approved
feature retains historical timing and archived totals. Timing summaries remain
keyed by their original thread identity, and a reused slug resolves its new
manifest's thread. There is no automatic expiry or quota in this initiative.

The coordinator records per-turn inode/disk growth as Advisory operational cost,
rather than adding a new purge/recovery contract or silently expiring requested
history. Review that conclusion against the actual ownership and recovery code,
not by counting reviewer votes. A concrete data-integrity or supported lifecycle
defect still requires a finding. The local operator is trusted; remote clients
remain untrusted. No new dependency or Codex version is introduced.

## Verification before this review

Root monitor regressions pass three race repetitions:40 concurrent startup workers
share the four-slot bound, queued browser cancellation is prompt, all workers make
progress, and a failed identity check releases observation. Browser unit contracts
pass. The controlled browser fixture compiles with the final API and now also
checks a stable archived snapshot and absence of repeated activity requests;
actual execution remains after review.

Further provider/creation and pin results, plus exact final heads, follow below.
No packaged VM, live creation/browser acceptance, profile switch or rollback has
run. Previous exact-head provider/runtime/organization feature CI was green;
new final-head CI results are recorded separately when available.

## Exact final ranges

- codex-web: `269962eb65007581ba69c205634f9e6c14cc39d3..bdd79be2deea3431092b42f15890e95cee40f3a0`
  Prior delta review to final tree: `4dde3c6aaa1d038c518563762fa7ac480b650cd2..bdd79be2deea3431092b42f15890e95cee40f3a0`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`.
- dev-workspace: `bcbaf825d71285cbbd05b56e78bc386f2df480bd..8760619776cb89936a50d07237a1323b22553bba`
  Prior delta review to final tree: `40837d245e867aa0edd35f59f72b63bba80034d1..8760619776cb89936a50d07237a1323b22553bba`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`.
- vpsfree-dev-workspace: `c4df3838de8b42083bd43e86bfdff7d45a7e952f..db25c77e7d622d71a2e0c9d44b4a20a5aecb27fd`
  Prior delta review to final tree: `4e03a3f0a3fd439ae2c645ab41fa736051c5b8c9..db25c77e7d622d71a2e0c9d44b4a20a5aecb27fd`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`.
- workspace: `e0d3dee52ac637a96a7d73299aecd753759b484b..584ea0f6180cbc82fb8b17047303607259686dbd`
  Prior delta review to final tree: `ea6cc34a303dc2c8d9027f109a2212d1ebea02c5..584ea0f6180cbc82fb8b17047303607259686dbd`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`.

All four intended code/pin worktrees are committed and clean. Final runtime
autosquash preserved exactly the tested tree. Provider CI atbdd79be passed:
https://github.com/aither64/codex-web/actions/runs/34695650528.

Final provider all-Go suite passes; history lifetime/backfill/overlap tests pass
15 race repeats (6.128s), recorder-setup-error ownership3 race repeats, and exact
0.154experimental schema passes. Runtime all Go packages and browser unit pass
against actual bdd79be pin (web13.324s). Creation focused Go race8.136s, Ruby
28runs299assertions5.884s pass. These include source archive/delete at the exact
evidence-write crash, no duplicate initial turn, binding/journal mismatch
rejection, fresh-source validation, and six archive-destination new/plan/fork
combinations with evidence present/absent and pending lifecycle preservation.

Final vendorHash: `sha256-oaihmUfwPnYLdHjYSx2rSZIM57gS7s0t4TwLaIbs5RM=`.
Provider Go pseudo-version: `v0.0.0-20260912130915-bdd79be2deea`.
The final package dependency graph evaluates. All branches remain unmerged.
