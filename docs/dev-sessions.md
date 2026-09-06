# Development Tmux Sessions

The user-profile `dev-session` command manages one tmux session per development
initiative. It selects a registered workspace from the current directory; use
`--workspace NAME` before the subcommand to select one explicitly. The session
name is the resolved slug, and the tool follows the workspace layout from
`AGENTS.md`.

## Starting a session

Pass a short name by default:

```sh
dev-session start api-token-rotation
```

This works anywhere under the registered root, including `work/` and
`worktrees/`. From another directory, or whenever you want to be explicit,
name the workspace before the subcommand:

```sh
dev-session --workspace vpsfree-cz start api-token-rotation
```

If only one workspace is registered, it is the fallback outside its root. Once
two or more are registered, an outside call requires `--workspace`.

For a new Codex session, the command asks for the first request before it
creates tracking files or tmux panes. In a script or another noninteractive
shell, put that request in a file:

```sh
dev-session start api-token-rotation --goal-file request.txt --no-attach
```

The request file is required only while creating a shared conversation. An
existing session resumes without asking for the request again.

If a unique existing slug already matches that name, `start` resumes it. If no
existing slug matches, it creates today's slug. On June 6, 2026, a new
`api-token-rotation` session resolves to `2026-06-06-api-token-rotation`.

Use `--new` to force today's slug even when older matching sessions exist:

```sh
dev-session start api-token-rotation --new
```

Use `--as-is` when the argument is already the slug:

```sh
dev-session start 2026-06-06-api-token-rotation --as-is
```

When the workspace portal is available, `--model` and `--effort` select the
initial Codex settings. The browser offers the same choices from the App Server
model catalog.

The first window is named `dev` and contains three panes:

- left: login shell with cwd set to the workspace repository root; the helper
  launches `codex` in this shell, so exiting Codex returns to the shell prompt;
- right top: shell, with cwd set to `work/<slug>`;
- right bottom: shell, with cwd set to `worktrees/<slug>`.

Managed tmux panes and worktree windows receive these environment variables:

- `VPSFREE_DEV_SESSION_SLUG`;
- `VPSFREE_DEV_SESSION_WORKSPACE`;
- `VPSFREE_DEV_SESSION_WORK_DIR`;
- `VPSFREE_DEV_SESSION_WORKTREES_DIR`;
- `VPSFREE_DEV_SESSION_PORTAL_BASE_URL`, the reusable portal origin;
- `VPSFREE_DEV_SESSION_URL`, the resolved link for this session.

Do not use `VPSFREE_DEV_SESSION_URL` as the input for another session. Its
value already contains the current slug. The registry-backed dispatcher passes
the base URL explicitly and exports both values into each managed pane.

`start` creates `work/<slug>/plan.md`, `work/<slug>/state.md`,
`work/<slug>/portal.yml`, and `worktrees/<slug>/` when missing. When
`workspace-portal` is installed, it also creates a Codex App Server thread,
records its ID, assigns the session name, and sends the initial request. It
waits until the App Server has persisted the rollout and verifies the exact
first user message before it opens the terminal Codex client. Once that check
passes, the thread ID is authoritative and the helper resumes that exact
thread while refreshing its working directory and runtime environment. While
an exclusive creation journal
is still `creating` and its initial goal is unsent, the helper reconciles the
unique working directory instead. It resumes the sole candidate, or replaces a
recorded memory-only thread that vanished during an App Server restart. It
refuses multiple candidates and never replaces a ready thread. Before the one
allowed initial `turn/start`, it records a durable attempt marker. A retry of
the same unmaterialized thread fails closed until exact matching history appears
or an App Server restart permits a fresh creation replacement. Existing plan
and state files are never overwritten. New state files begin with exact YAML
front matter containing `lifecycle: active`; that
anchored field is the only lifecycle authority. An
exact slug that is present under `archive/` or active workspace state cannot be
reused. The helper also checks the top-level Git index and history, so removing
an archive from a later checkout does not remove its slug tombstone. It disables
repository-configured process hooks for these read-only checks and fails closed
when the archive history cannot be read.
If a running session was created without a shared portal thread, stop it before
starting the same active slug with portal interaction; the helper refuses to
attach a new browser thread to an old terminal conversation.

```yaml
---
lifecycle: active
---
```

Fill in a substantive plan and initial state and commit them in the workspace
repository before the first project-code commit or external mutation. Keep
active tracking current in the working tree, but do not commit each plan,
review, test/CI, deployment, or status update separately.

Short initiatives normally have only the initial active tracking commit and the
final archive commit. For an initiative that remains unfinished at the end of
an active working day, at most one consolidated tracking-only checkpoint may be
committed for that day when material progress is worth preserving. This is a
ceiling, not a requirement, and inactive calendar days do not count. An
additional same-day checkpoint is reserved for a genuine ownership handoff or
an explicit user request. A pause until a future working day can justify that
day's consolidated checkpoint, but not a second one. Ordinary functional
commits are not tracking-only checkpoints.

## Attaching and syncing

```sh
dev-session attach api-token-rotation
dev-session fork api-token-rotation alternate-approach
dev-session sync api-token-rotation
dev-session stop api-token-rotation
dev-session remove api-token-rotation
dev-session finalize api-token-rotation
dev-session finalize api-token-rotation --check
dev-session reopen api-token-rotation
dev-session list
dev-session current
dev-session url
```

Lookup commands accept a short name when it resolves to exactly one known slug
from `work/`, `worktrees/`, or managed tmux sessions. If multiple slugs match,
the command fails and prints the candidates. Use the full dated slug directly
to avoid ambiguity. The `--as-is` option is only needed when a command must
treat an input as a literal slug before that slug is known to the workspace.

`fork` creates a new dated session with a native copy of the source Codex
conversation. It copies no worktrees, tracking content, artifacts, or
development clusters. Use `--model` and `--effort` to override the inherited
Codex settings.

`sync` creates one managed tmux window for every git worktree under
`worktrees/<slug>/*`. It removes only managed windows whose worktree path no
longer exists, and it leaves user-created windows untouched.

`stop` normally only kills the exact managed tmux session and leaves all files
and worktrees in place. After `finalize` has moved tracking into `archive/`, it
refuses to stop until that exact archive move and its terminal state are
committed.

`current` prints the active slug and nothing else. It resolves the slug from the
managed tmux session environment, the caller's exact managed tmux pane, or a
cwd under `work/<slug>` / `worktrees/<slug>`. It never falls back to tmux's
server-current session when called outside a tmux pane. It exits with an error
when no active session can be found or when those sources disagree. Codex
instances should run it before creating a new initiative slug. The helper
accepts session identity only when both `VPSFREE_DEV_SESSION_SLUG` and the
canonical `VPSFREE_DEV_SESSION_WORKSPACE` match. It filters managed sessions
owned by other workspaces from listing and short-name lookup.

Managed sessions created before workspace identity metadata was introduced are
not adopted automatically. Inspect and stop such a session manually after its
writers are quiet, then restart the same active slug with `start --as-is` so it
receives canonical metadata. Existing symlinked workspace paths are recognized
and normalized automatically.

`url` prints the permanent portal page for the selected initiative. It accepts
the same short-name and `--as-is` forms as the other lookup commands. The page
continues to work after finalization because the portal scans both `work/` and
`archive/`.

`remove` cleans up a development session:

```sh
dev-session remove api-token-rotation
```

It removes clean git worktrees whose `HEAD` is attached to a shared
`refs/heads/*` branch under `worktrees/<slug>/`, removes the empty worktree
group directory, and then kills the managed tmux session when one exists. This
order makes it safe to run from inside its own managed session: the session is
killed only after cleanup has completed. Before removing worktrees, it records
each final `HEAD` and verifies the worktree against the canonical project stored
in `portal.yml`. Branches are kept.
`work/<slug>/plan.md` and `state.md` are kept by default.

Worktrees with changes reported by ordinary `git status --porcelain` are
refused unless `--force` is passed. Detached worktrees and paths outside the
exact initiative group are always refused. Cleanup then delegates removal to
`git worktree remove`; if Git refuses a worktree, resolve the reason and retry.
Branches are retained:

```sh
dev-session remove api-token-rotation --force
```

`remove` is for stopping or cleaning up an active session. It never deletes the
initiative tracking directory. The former `--all` option is intentionally not
supported because completed and abandoned initiatives must retain a durable
record.

## Finalizing an initiative

Use `finalize` only after the initiative is fully integrated and has no
session-owned work, or after it is explicitly abandoned:

```sh
dev-session finalize api-token-rotation
```

Before running it:

- set the lifecycle field in the exact YAML front matter at the start of
  `state.md` to `complete` or `abandoned`; lifecycle-looking text anywhere in
  the Markdown body has no effect;
- for `complete`, merge every registered feature branch's exact final head into
  its configured remote default branch;
- make sure plan and state have an earlier commit under `work/<slug>/`;
- make sure that history includes a commit whose front matter has
  `lifecycle: active` before the terminal transition;
- resolve all review, CI, merge, approval, deployment, and cleanup work owned by
  the session;
- stop shells, editors, builds, and background processes that can still write
  into an initiative worktree;
- remove credentials, caches, reproducible bulk captures, and transient
  outputs, keeping plan/state and intentionally durable evidence.

For `complete`, `finalize` fetches every registered feature branch and default
branch. The local and remote feature tips must be identical, and that exact
commit must be an ancestor of `origin/<default_branch>`. The command reports
all branches whose merge status cannot be proven. A squash merge or partial
cherry-pick does not satisfy this rule. Coordination-only initiatives with no
registered branches remain valid. Legacy live worktrees without `portal.yml`
are inferred from their canonical bare repository and checked as branches, not
treated as coordination-only work. `abandoned` skips only this merge check.
Use `finalize --check` to run the complete preflight without removing
worktrees, changing the manifest, or moving tracking.

`finalize` performs all safety checks before cleanup. It refuses missing
tracking files, an active or ambiguous lifecycle, tracking without a prior
commit, an existing archive destination, mismatched or replaced tmux identity,
worktree changes reported by ordinary `git status --porcelain`, detached
worktrees, worktrees outside the allowed repositories, symlinked
paths or roots, and unknown entries in the worktree group. Cleanup for one slug
is serialized, and every worktree receives the same ordinary cleanliness and
path checks before any is removed. It then delegates each removal to non-force
`git worktree remove`, preserves the branches, and uses a same-filesystem,
atomic no-clobber move from `work/<slug>/` to
`archive/<slug>/`. If Git refuses a worktree for another reason, cleanup stops;
already removed worktrees remain available through their retained branches,
and the command can be retried after resolving the refusal. The helper requires
GNU `mv` with `--no-copy` and `--update=none-fail`; it verifies option support
before removing worktrees.

The per-slug lock serializes `dev-session` commands, not external writers. A
process that writes after the last cleanliness check can still race worktree
removal, so all worktree writers must be stopped before finalization.

The terminal lifecycle and final state do not need a separate commit before
`finalize`; the earlier committed active snapshot is sufficient. The helper
does not stage or commit. Inspect the reported move and commit only the exact
`work/<slug>/` and `archive/<slug>/` paths in the shared top-level repository,
including the final tracking content, as one archive commit. The managed tmux
session remains available for that commit. After the commit,
`dev-session stop <slug> --as-is` verifies the terminal archive and clean
task paths before closing the exact workspace-owned tmux identity it resolves
at stop time.

The portal uses `finalize --prepare` internally before releasing clusters. It
quiesces the terminal client and proves the thread idle while the host
transition gate excludes new mutations. If the later release or finalization
fails, the portal runs `sync` to restore the client.

The public CLI uses that same host-wide gate. It refuses `finalize` while a
vpsAdmin or vpsAdminOS development cluster for the initiative is still present;
reset the reported clusters first. Cluster starts and resets hold the shared
side of the gate for their full command, so none can race the final archive
move.

If an initiative was archived before its branches were merged, reopen it:

```sh
dev-session reopen 2026-06-06-api-token-rotation --as-is
```

The archive move and terminal tracking must already be committed. `reopen`
refuses a conflicting active directory, worktree group, or live session, then
atomically moves `archive/<slug>` back to `work/<slug>`. It changes the
lifecycle to `active`, removes `finalized_at` and stale `final_head_sha` values,
and preserves branch, base, repository, and Codex identity. It is journaled so
an interrupted move can be retried. An explicitly abandoned initiative stays
terminal unless `--allow-abandoned` is supplied.

Legacy archives without `portal.yml` can also be reopened. Add each retained
feature branch with the normal worktree command; the helper reconstructs its
registration from one unambiguous merge base with the configured default
branch. Supply `--base REF` if the intended base cannot be inferred uniquely.
Starting the reopened initiative with an initial request creates a fresh shared
conversation while leaving its existing plan, state, and repository records
unchanged. Reopen records the exact plan and active-state digests until that
conversation is established. Session creation refuses terminal or changed
tracking instead of treating a partial or independently edited directory as a
reopened initiative.

## Worktree helpers

Create a project worktree through the canonical bare repository:

```sh
dev-session worktree add api-token-rotation vpsadmin
```

This uses:

- bare repo: `repos/vpsadmin.git`;
- branch: `<slug>`;
- worktree path: `worktrees/<slug>/vpsadmin`;
- base ref: `origin/HEAD`, falling back to `origin/master`;
- `git fetch origin` before creation.

The helper also records the canonical project identity, GitHub repository,
feature branch, default branch, and starting base commit in `portal.yml`.
Removing an individual worktree or using bulk cleanup records its last commit
before cleanup. Finalization verifies the project identity and records the last
commit of every remaining worktree, so archived pages retain trustworthy
immutable comparison links.

Before fetching or creating a branch, the helper resolves the repository and
requires it to be a bare clone directly under the canonical `repos/` root.
An in-root alias to another canonical bare clone is accepted; a symlink to an
external repository is refused.

Workspace implementation work uses the top-level repository through its
reserved project and worktree name:

```sh
dev-session worktree add api-token-rotation workspace
```

This creates `worktrees/<slug>/workspace` from the top-level repository. The
helper verifies that the worktree belongs to that exact repository and applies
the same cleanliness, attached-branch, final-commit, and non-force removal
checks used for project worktrees. The name `workspace` is reserved for this
repository, so an independent project cannot use it as a worktree alias. Other
non-bare repositories remain refused.

Useful options:

```sh
dev-session worktree add api-token-rotation vpsadmin --base origin/main
dev-session worktree add api-token-rotation vpsadmin --name vpsadmin-master --branch master
dev-session worktree add api-token-rotation vpsadmin --no-fetch
```

Remove a worktree without deleting its branch:

```sh
dev-session worktree remove api-token-rotation vpsadmin
```

Worktrees with changes reported by ordinary `git status --porcelain` are
refused unless `--force` is used. Detached worktrees are always refused. Git
remains the authority for whether its non-force worktree removal can proceed;
resolve any refusal and retry, or use the explicit force option when discarding
the worktree is intentional.

## Runtime ownership

The workspace flake installs the public commands and user systemd units in a
dedicated user Nix profile. A private registry maps workspace names to roots
and hostnames. Per-workspace portal, App Server, authority, and tmux state lives
below `$XDG_RUNTIME_DIR/vpsfree-workspaces/`; the public command derives those
paths and does not require callers to repeat them. Run
`dev-session validate` to validate every persisted portal entry, including its
plan, anchored lifecycle, active/archive placement, and manifest, before
deployment.

Host-specific runtime options are private implementation details fixed by the
dispatcher. Callers can select only a registered workspace, not replace its
runtime paths. The App Server uses the Codex package from the current NixOS
system. `workspace-host` checks its protocol and model catalog before adopting
it and retains one tested Codex store path per application profile generation.
Codex adoption and rollback gate new mutations, quiesce native terminal
clients, verify all threads are idle, restart App Server and portal pairs, and
restore the clients. A compatible system update that finds an active turn is
retried every five minutes. Use `--no-codex` to start a shell in the left pane
instead.

New conversations use GPT-6 Astra with `xhigh` reasoning. When an explicitly
chosen model does not support `xhigh`, its advertised default reasoning effort
is used. An explicit reasoning choice always takes precedence.

`--goal-file FILE` provides the initial Codex request and seeds the Goal
section in a new plan. It is required when a noninteractive caller creates a
shared conversation. `--json` prints the resolved slug, portal URL, Codex
thread ID, and identity-bound tmux attach command. `--exclusive` requires a
goal file and records its digest in a workspace-local creation journal before
creating initiative state. It may resume a manifest
whose creation state is `creating` or `ready` only when the complete request
identity matches. The unique `work/<slug>` directory is used to reconcile one
matching App Server thread, but App Server does not offer an exactly-once
creation key. A pending retry resumes the sole candidate, creates a replacement
when an App Server restart provably left none, and refuses multiple candidates.
It sends the initial goal directly only when metadata identifies the expected
fresh, idle, turnless thread; accepted or ambiguous active turns fail closed.
An incomplete tmux session is replaced only when its creation environment
identifies the exact workspace and slug. The journal remains in
the lock directory after the manifest reaches `ready`, allowing the
HTTP result to be replayed without repeating a known initial turn. The portal
passes a full dated slug with `--as-is`, preserving request identity across
midnight.

The private package implementation requires the authority directory, tmux
socket, Codex command and socket, client version, and portal command to be
present as absolute paths. The registry-backed dispatcher supplies them to
both terminal users and the portal, so they share one command and one session
model.

See [Workspace portal](workspace-portal.md) for the browser interface, manifest
format, security model, private CA, and deployment responsibilities.
