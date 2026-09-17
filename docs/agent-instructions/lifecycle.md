# Session lifecycle and package transitions

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

An initiative can leave `work/` through an explicitly requested archive or
delete action, or through the enabled automatic archive policy below. Completing
the requested work, answering the current message,
setting a terminal lifecycle, and preparing a handoff all leave the session
open for follow-up conversation. Do not infer permission to archive, delete, or
stop a session from phrases such as "finish the work" or "implement the plan",
and do not schedule delayed cleanup after the current turn.

Enabling `dev-session auto-archive` is standing authorization for its scheduled
worker to archive eligible sessions. Apply tiers in order: explicit
`lifecycle: complete` after 1 inactive day; active sessions with every registered
branch merged after 7 inactive days; active sessions without registered
repositories or owned worktrees after 14 inactive days, archived as abandoned.
The first two tiers retain all normal merge proofs. Already abandoned sessions
require manual archival. A `Keep open` hold prevents automatic archival, and
removing worktrees does not remove the obligations of registered branches.
First enablement, re-enablement, releasing a hold and revival start fresh
inactivity periods. The worker preserves the existing archive checks and
journal recovery. This authorization does not permit an agent to bypass the
worker, abandon other work, delete sessions, or schedule its own delayed cleanup.

Run `dev-session archive <slug> --as-is` for a completed initiative, or add
`--abandoned` when the user explicitly discards the work. Archival is one
deterministic, journaled operation. It verifies that the Codex thread has no
active turn, pending request, or queued message; releases development clusters;
removes clean attached worktrees with non-force `git worktree remove`; retains
branches; writes terminal lifecycle and manifest metadata; moves
`work/<slug>/` atomically to `archive/<slug>/`; commits only that tracking
transition on a compatible shared `master`; and retires the Codex thread, tmux
session, and runtime authority. Preserve unrelated working-tree and index
changes. Resolve any refusal and retry the same command, which resumes its
private journal. The CLI and portal each ask for one yes/no confirmation; they
do not require the slug to be typed.

For a completed initiative, archival fetches each registered feature and
default branch and proves that the exact local and remote feature head is an
ancestor of `origin/<default_branch>`. It refuses unmerged, divergent, missing,
or unprovable refs and reports every offending repository. An interrupted
archive reproves those exact journaled heads before each remaining destructive
phase and verifies the exact projected archive tree and retained thread identity
before committing or retiring runtime state. Pushing, testing, deploying, or
removing a worktree does not satisfy this rule. The merge check is skipped only
for an explicitly abandoned initiative. Coordination-only initiatives with no
registered branches remain valid. Before archiving, remove credentials, caches,
reproducible bulk captures, and other transient outputs; preserve the plan,
state, and intentionally useful evidence.

Follow-up work before merge must reuse the same slug and retained branches. Run
`dev-session revive <slug> --as-is` to restore a prematurely archived
initiative. Reviving commits the move from `archive/<slug>/` back to
`work/<slug>/`, restores the active lifecycle, clears terminal repository
heads, preserves repository, branch, base, and conversation identity, and
starts the exact retained Codex thread. It does not recreate worktrees. The
confirmation uses a stronger warning for an abandoned initiative and is stored
in the revive journal so a retry does not ask again. Recovery verifies the
complete restored tracking tree before committing it. Legacy archives without
`portal.yml` receive a recoverable new shared conversation;
re-adding retained branches reconstructs their registration metadata. Revive
refuses dirty, duplicated, ambiguous, or live state.

`dev-session delete` is the user-directed destructive discard. Agents must not
run it unless the user explicitly asks to delete that session. It requires an
interactive yes/no confirmation; `--force` additionally authorizes dirty
worktree removal and interruption of an active turn. Delete independently
inventories canonical worktrees owned by the exact session, so missing or stale
portal repository registrations do not prevent an explicit discard. It always
refuses symlinks, path escapes, foreign repositories, and ambiguous worktree
entries. Delete releases cluster and runtime state, removes verified worktrees,
retires the Codex thread, and moves tracking plus creation state into private
XDG recovery storage together with the actual worktree identities, branches,
heads, and dirty state. It is journaled and retryable, retains Git branches, and
commits only an already committed tracking deletion. Never-committed tracking
disappears without a Git commit. Unfinished lifecycle journals reserve their
slug; resume the matching `archive`, `delete`, or `revive` command before other
session or cluster mutations, workspace package changes, workspace unregister
or suspension, or Codex reconciliation.
Stable session and cluster commands must verify their originating workspace
package generation after acquiring the shared transition lock. If a command
waited across a successful or compensated package switch, reject it as
superseded and require the stable command to be run again.
When development cluster state exists, package switches and rollbacks require
the target generation to publish the matching state schema, transition policy,
and tracking-size contract, and prove that every existing cluster already has
an explicit recorded socket identity.
Pre-contract cluster state without that identity fails closed and must be reset;
never infer or migrate its ownership during a package transition. This avoids a
race with an old helper that was already waiting on its per-cluster lock.
New helpers create the state directory and record its workspace-scoped socket
identity in one locked initialization step. Ordinary access must reject an
existing state directory without that record. Explicit reset may clean such
state only when the complete runner tuple and its process tree prove ownership;
ambiguous legacy state must remain untouched.
Candidate activation must repeat the same check so a pre-contract installed
switch command cannot bypass it. The one retained password-reset legacy socket
is supported only while its recorded identity and complete owner record prove
the known runner tuple. Other legacy socket state fails closed.
Workspace unregister is refused until that workspace's cluster state is reset.
Never use `delete` as a substitute for archiving completed or abandoned work.
