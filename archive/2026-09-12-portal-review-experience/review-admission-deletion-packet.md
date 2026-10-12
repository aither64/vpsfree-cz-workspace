# Passive admission and completed-deletion follow-up

Read plan.md and review-final-packet.md for the original user-approved feature
and previously reviewed ranges. This is a focused follow-up on two demonstrated
Important findings from review-final-architecture.md and review-final-scope.md.
All original feature lanes and the prior remediation reviews are complete.
Review the committed delta and its direct interactions; do not restart an
unbounded review of unrelated host features. No tests, edits, Git mutations,
or nested agents. The local operator is trusted; remote clients are untrusted.

Risk is HIGH: concurrent recovery, retained private state, explicit deletion,
protocol reconnection and rollback. Fresh standalone gpt-5.6-sol/xhigh reviewers
cover architecture, risk/compatibility and scope/proportionality. General fixes
were narrow and verified directly; no general rerun merely for confirmation.
The three selected lanes assess the new admission/recovery behavior described
below. Report concrete Blocking/Important/Advisory findings with code evidence.

## Changed behavior

The passive codex-web client bounds connected RPCs at four, including metadata,
history, resume and unsubscribe calls. A fixed four-worker restoration queue is
bound to the connection generation. Disconnect/Close cancels queued work; old
workers cannot publish coverage or watch errors for a newer generation. RPC
timeouts start after admission, while caller deadlines still bound queue time.
Interactive clients retain their existing behavior. No public option or protocol
shape changes. The owning provider is used by dev-workspace's ObserverOnly client;
organization and workspace packages consume the matching pinned provider/runtime.
The protocol coverage scanner recognizes the generation-bound connected helper.

The portal serializes readers of one thread before global history admission,
so duplicate reads cannot consume all four slots while waiting behind one gate.
Gate ownership covers active and cancelled/queued readers and retires at zero.
Existing background coalescing, coverage persistence and all timing semantics
remain unchanged.

A completed deletion supersedes older accepted creation requests. The portal
reuses the existing verified removal recovery marker and checks no destination,
authority or pending journal remains under the runtime lock. Paused/failed
receipts without completed-deletion evidence remain retryable. Retired exact
receipt/binding/evidence files move beside deletion recovery tracking, using
their existing formats. The CLI checks completed deletion/original acceptance
and exact retired IDs under the destination lock (including fork's second lock),
so a queued stale worker cannot recreate an explicitly deleted session after
receipt retirement or name reuse. Fresh IDs accepted after deletion remain valid.
An equal recorded timestamp rejects; one nanosecond after is allowed.
Archive-conflict wording describes the historical event and remains accurate
after revival.

The strict manifests, lifecycle/start/fork journals and removal marker schemas
are unchanged; no new CLI flag, dependency, host configuration or deployment
ordering is introduced. Previous packages ignore additive private recovery files.
Delivery remains provider -> runtime -> organization -> workspace user profile.
The implementation commits/pins are below. Long package/VM/browser/live creation
and profile upgrade/rollback acceptance remains after this review.

## Explicit scope boundaries

The approved plan uses native Git and maintained CodeMirror Merge; no new
dependency in this pass. Historical/offline timing remains unclassified where
coverage is missing. Durable timing records remain with retained conversations,
including archive/delete recovery. Both final reviewers confirmed this ownership
contract. Per-turn disk/inode growth remains a recorded Advisory cost; this pass
does not add unrelated quotas, expiry, or a permanent conversation purge.
No default-branch integration or session archival/deletion is authorized.

## Quick verification

Provider all Go packages pass (codex4.725s). Twenty race repetitions of many-watch
reconnect, queued cancellation/Close, immediate accepted-resume disconnect and
interactive reconnect pass7.995s. The immediate-disconnect case also passed100
repetitions; exact selectedCodex0.154experimental protocol validation passes.

Runtime all Go packages pass against actual provider8377021 (web15.358s). Portal
admission tests pass3 race repeats4.736s, including40 duplicate browser readers
and unrelated worker progress. Creation/removal/archive focused Go races pass
(session1.515s, web12.236s); Ruby38tests445assertions8.915s. These use Ruby-produced
removal markers and cover new/plan/fork x paused/failed, absent/older/unrelated
deletions, held locks, fresh name reuse, queued stale IDs, receipt-only recovery,
second fork lock, timestamp precision and revival notice.

Codex-web's additional functional admission commit remains separate from the
original timing commit because it isolates transport scheduling from timing
accounting. Consumer admission and creation repairs are folded into their
respective feature commits; mechanical dependency updates stay in the pin commits.

## Exact committed ranges

- codex-web: `269962eb65007581ba69c205634f9e6c14cc39d3..83770217d63f2c206689d2c569e1c81950544504`.
  Reviewed delta: `bdd79be2deea3431092b42f15890e95cee40f3a0..83770217d63f2c206689d2c569e1c81950544504`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`.

- dev-workspace: `bcbaf825d71285cbbd05b56e78bc386f2df480bd..c350274225e2886209f4d92e5f01f464bc1caf1a`.
  Reviewed delta: `8760619776cb89936a50d07237a1323b22553bba..c350274225e2886209f4d92e5f01f464bc1caf1a`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`.

- vpsfree-dev-workspace: `c4df3838de8b42083bd43e86bfdff7d45a7e952f..a0d7fdca3ccfe20fa920cfba5e4e880caf9cc1da`.
  Reviewed delta: `db25c77e7d622d71a2e0c9d44b4a20a5aecb27fd..a0d7fdca3ccfe20fa920cfba5e4e880caf9cc1da`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`.

- workspace: `e0d3dee52ac637a96a7d73299aecd753759b484b..ef75f045f1a0a496c23251a25306a98e32438a2f`.
  Reviewed delta: `584ea0f6180cbc82fb8b17047303607259686dbd..ef75f045f1a0a496c23251a25306a98e32438a2f`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`.

All worktrees are clean. Consumer autosquash preserved the tested tree.
Go pseudo-version: `v0.0.0-20260912134208-83770217d63f`.
Fresh vendor hash: `sha256-8NzgurFJHLPL2ITTeXbXuD33afPxj3i+hmQKIQcWOVE=`.
Provider CI passed at the exact final head:
https://github.com/aither64/codex-web/actions/runs/34697189123.
The runtime, organization and workspace pins select this exact dependency chain.
