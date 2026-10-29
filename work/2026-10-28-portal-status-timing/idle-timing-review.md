# Idle timing follow-up review

Review the completed committed runtime display correction at
cc0d452a0653a112c8a013492c1734d9554bb909 on top of reviewed
7d1163585a51da684be0f5cdd500a64822165839, worktree
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-portal-status-timing/dev-workspace.
Read its AGENTS.md, workspace procedures and mandatory-review skill. Use all four
lanes for the bounded display/admission separation. Remain independent/read-only;
write idle-timing-review-result.md. No delegation, builds or live operations.

The user's original task includes fixing Timing unavailable and session status.
Final acceptance preparation found recovery reports idle, executionHeld=true for
the autostart session, while GET activity returns historical timing. Existing
app.js skipped all activity calls while held. Home isolation alone cannot fix
that display. This commit permits read-only activity only after recovery verifies
idle, triggers it on that state transition, and keeps execution admission paused.
The existing HTTP/Chromium/Firefox recovery fixture now expects timing and checks
that native resume/send/queue calls remain absent before the sole explicit original
message. Unavailable/failed/waiting holds still skip activity. No new endpoint,
state format, migration, native arguments or public execution permission.

Quick checks: JS syntax, diff whitespace and focused recovery/retained-input Go
checks passed (4.7 seconds). Browser fixture is deferred until this review.
Native 0.165 prompted utility, 0.164-to-0.165 saved-state upgrade/resume/fork,
namespace and provider routing passed against unchanged code/binaries. Previous
runtime CI40854716525 passed creation/archive/package. Final runtime CI40858490632
is running, not being treated as equivalent to prior code.

Complete runtime series from d0e4318cb1872feb69f3109f032870c310f14bdf:
7d1163585a51da684be0f5cdd500a64822165839 private home/native/package selection
cc0d452a0653a112c8a013492c1734d9554bb909 verified idle historical timing
The display fix is independent and intentionally separate. Prior whole-branch
and schema-62 lineage conclusions apply to unchanged content. No new migrations
or repeated dependency stream in this runtime series. Consumer locks currently
remain at reviewed7d while the already launched old-head build finishes. They
will be mechanically refreshed to this exact final runtime, preserving the
extension and folding each prior pin into one final generated/composition commit.
That mechanical refresh cannot change this runtime source. Please assess final
runtime history/migration coherence and any risk to held-thread execution.

Read-only live corroboration: querying the autostart activity endpoint returned
idle with observed timing; native loaded-thread sets were identical before/after,
and the autostart thread remained absent from both. No resume/turn was sent.
