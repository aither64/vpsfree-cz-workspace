# Session identity in a verification watcher

`dev-session current` can resolve the bound session from its tracking directory
when both DEV_SESSION environment variables are absent. The shared workspace
root has no current session, so probing there can report a missing identity even
while the conversation's trusted binding and tracking-directory result agree.

In session `2026-09-30-portal-review-improvements`, two watchers used the shared
root despite an assigned tracking directory. Both stopped before launching
checks. This produced no verification evidence and did not mean the session
binding was lost.

Give a fresh watcher its first shell command and exact tool working directory,
then require the literal slug. Keep the same directory for the parent-written
verification script; the script should also validate identity before touching
worktrees. Never treat CWD alone or missing environment markers as ownership
proof, and do not invent markers to conceal a conflicting binding.

Related initiative: [state record](../../work/2026-09-30-portal-review-improvements/state.md).
