# Isolated Codex creation acceptance needs one metadata home

During portal creation acceptance with Codex 0.154.0, exact-cwd thread/list
recovery lookup exceeded the 60-second CLI deadline against the existing home
with 2,365 threads. The same query also stalled on a fresh owned App Server using
that home. Initialize, loaded/list and loaded metadata reads stayed responsive;
read-only exact-cwd SQLite lookup found no matching fixture thread. A clean
owned metadata home returned the exact filtered lookup in 3.9 ms. This identifies
a history-dependent lookup limitation; its upstream cause was not established.

Use a fixture-owned metadata home for bounded real creation acceptance, with
private symlinks to the existing auth/config when authenticated model access is
needed. Never copy credential contents. Propagate the identical CODEX_HOME to
the App Server, CLI and dedicated tmux/native TUI. During a mixed-home terminal handoff, the first source turn was interrupted
and had no collaboration context. After
aligning homes, the same source completed an ordinary diagnostic request, and
a newly created plan session's initial turn completed successfully.

Preserve the exact receipt/journal across explicit retries; do not allocate a
new thread merely to hide a timeout. Clean only the owned process/socket/home
after collecting sanitized results. The production history lookup latency
remains outside this portal UI change. Related initiative:
work/2026-09-12-portal-review-experience/.

A later question check also showed that a historical rollout's Plan mode is
insufficient to establish the current live mode after private portal/native
reconnection. The actual next turn ran in Default mode and declined the tool.
On that same source, an explicit default-to-plan settings transition emitted
live notifications. An exact observer-shaped thread/resume then emitted no
settings change, both with the interactive owner retained and after its
disconnect. The experiment did not show the passive resume overwriting mode.
Establish live Plan mode through the ordinary settings API before a bounded
request_user_input acceptance probe; retain unsuccessful attempts in results.
