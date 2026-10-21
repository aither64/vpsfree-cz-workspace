# Session lifecycle and package transitions

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

Read [coordination](../coordination.md) before a lifecycle/package mutation that
affects queued work or a machine reservation. Running/uncertain operations fence
lifecycle changes. Legacy archive completion automatically releases machine
reservations; that is implementation behavior, not permission to archive or
release a machine. Before any lifecycle action that could release deployed
ownership, satisfy [machine retention](../coordination.md#machine-retention):
integrated deployed feature lineage, user acceptance of the resulting UI/behavior
and explicit direction to release that physical machine. Idle time, feedback,
review, redeployment and turn completion do not supply that direction. Failed or
interrupted archival keeps deployed holds until recovery completes.
Revival does not reacquire released machines or resume canceled work. Deletion
retains its recovery holds. Package candidates must preserve the coordination
contract and retained artifacts; inactivity alone never frees a review reservation.

Sensitive sessions keep these lifecycle and coordination checks, but their
tracking moves stay local and do not require or create Git commits. Preserve
private sensitivity metadata and local exclusions through recovery.

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

Run `dev-session archive <slug> --as-is` for explicit archival. The command
closes the session with neutral `lifecycle: archived`, including unfinished,
unmerged, unpublished, detached or dirty work. It stops owned active agents,
pauses active goals, keeps conversations and queued prompt records, releases
clusters, captures local checkout files and index state in private recovery,
forcefully removes owned worktrees, retains branches, moves tracking atomically
to `archive/`, saves the local transition and retires runtime state. The installed
workspace retries its tracking Git commit independently; network, hook or remote
master failures leave tracking sync pending without reopening the session. It does
not fetch or require merged feature heads. Preserve unrelated shared index and
working-tree changes. CLI and portal each ask for one yes/no confirmation.
Browser archival runs in a separate systemd user service and survives portal
restart. Local file work has no total wall-clock deadline. Inspect pending Git
bookkeeping with `dev-session tracking-sync --status --slug <slug> --json`; the
managed retry timer preserves hooks and the shared tracking lock. Do not edit
receipts or recovery snapshots to clear a pending status.

Automatic archival retains its merge, publication, cleanliness and idle policy.
`--require-merged` requests that completion policy manually; `--abandoned` retains
the explicit discard policy. A retry resumes its journal's saved policy, including
older complete/abandoned operations. Wrong ownership, changed recovery contents,
conflicting operations and actual copy/removal errors still require recovery.
The runtime's `docs/session-archive-recovery.md` owns formats, private snapshots,
retained prompts, target-specific merge proofs and interruption recovery.

Run `dev-session revive <slug> --as-is` to reopen an archived initiative. Revival
restores tracking under `work/`, restores active lifecycle and preserves the
retained repository and conversation identities. Explicit archives recreate their
saved worktrees with staged, unstaged, untracked and ignored files before starting
the conversation. Queued prompts stay held. Revival can proceed before tracking
sync succeeds and coalesces pending bookkeeping to its latest state. Older
journals retain their saved synchronous commit policy. Older complete/abandoned
archives do not gain snapshots. The stronger abandoned warning and accepted confirmations
remain journaled so retries do not ask again. New manifestless revival refuses;
repair historical scope under the separately assigned dated repair procedure.
Unfinished lifecycle journals reserve their slug and must be resumed before
conflicting session, cluster or package mutations.

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
Historic metadata repair is source-only maintenance, with writer exclusions held
across interruption and one standalone recovery file. It has no installed batch
reservation, status decoder or automatic-worker integration. Resume the exact
saved projection inside the re-established window; never expose a partial repair
to ordinary writers. Repair is separate authorization from archive, worker
enablement or conversation retirement. The dated procedure owns tool removal;
the runtime's `docs/session-archive-recovery.md` owns its other temporary readers.
Both inventories include active/archive records and restore/revival paths and
require zero dependent inputs and zero supported reintroduction paths.
Unknown-base schema-1 and schema-2 journals remain supported formats.
