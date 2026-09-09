# 2026-09-06-portal-config-deployment-policy

## Goal

Finish the workspace portal as a user-managed, multi-workspace service while
keeping only its privileged HTTPS substrate in the aitherdev NixOS
configuration. Unify CLI and browser sessions, retain system-managed Codex
updates, correct creation recovery and the `xhigh` default, and make initiative
completion mean that every registered feature head is provably merged.

Also provide a safe archived-session recovery workflow and use it to restore
`2026-09-05-cgroup-v1-shared-device-fix` with its original retained branches.

Extend the browser Codex client with plan-mode and queued-message controls, and
reconcile the six named unfinished tmux sessions into the shared browser/CLI
runtime without disturbing their tracking, worktrees, retained branches, or the
password-reset development cluster.

Restore session creation against Codex 0.153.4's structured thread-source
metadata, make explicit session removal remove failed and active sessions from
the workspace namespace, and complete the browser interaction model with a
CLI-like request-input wizard, plan implementation actions, visible steer
receipts, and non-disruptive transcript scrolling. File uploads are deferred.

Prevent agents from closing a conversational session after answering a request.
A terminal lifecycle only makes the initiative eligible for explicit archival;
it does not make an unarchived session read-only or authorize archival or
runtime cleanup. Recover the prematurely archived
`2026-09-07-vpsfstatus-index-stale-2` session under its original slug and exact
Codex thread. Also render GitHub-style pipe tables in chat and artifact Markdown.

Repair the retained password-reset session without changing its conversation,
worktrees, or development cluster. Recognize its verified
`vpsfree-kb-contracts`/`vpsadmin-kb-captures` repository alias, keep any genuine
repository registration conflict local to its session instead of degrading the
whole index, and make conversations longer than ten item pages interactive.
Fresh messages must not scan the complete history. Accepted messages retain a
durable turn receipt for idempotent retry until the browser observes the
matching transcript message and acknowledges it. Before compacting any receipt,
the server must independently prove the exact transcript client identity and
canonical text digest, plus the recorded turn for an accepted receipt;
genuinely uncertain outcomes use cursor-safe streamed reconciliation. Render
structured Codex turn failures as readable errors and show cluster service
destinations as labelled URLs.

## Affected repositories

- Coordination workspace (`aither64/vpsfree-cz-workspace`): hybrid user runtime,
  registry and routing, CLI dispatch, lifecycle enforcement and recovery,
  tests, documentation, and durable agent rules.

The current implementation and review scope is the workspace repository only,
on its existing `2026-09-06-portal-config-deployment-policy` feature branch.
The privileged nginx/TLS/Basic Auth substrate was deployed earlier from an
unmerged `vpsfree-cz-configuration` feature branch; this follow-up neither
changes nor pins that repository and requires no NixOS deployment.

## Approach

- Package the portal, private session engine, public multi-workspace dispatcher,
  cluster helpers, router, and user-systemd units in the workspace flake. Install
  them in a dedicated user Nix profile managed by `workspace-host`.
- Store validated workspace registrations in
  `~/.config/vpsfree-workspaces/registry.json`. Select a workspace from the
  longest matching root or explicit `--workspace NAME`; require the flag outside
  all roots once multiple workspaces exist.
- Run a Host router on a group-restricted Unix socket plus per-workspace portal,
  Codex App Server, and tmux user services. Derive private application runtime
  paths below `/run/user/1000` and reject unknown Host headers.
- Keep Codex sourced from `/run/current-system/sw/bin/codex`. Validate its App
  Server schema and model catalog before adoption, retain a user GC root for the
  last compatible version, and reconcile compatible NixOS updates only after
  active turns become idle.
- Make `vpsfree-cz.workspace.aitherdev.int.vpsfree.cz` canonical. Keep
  `vpsfree-cz-workspace.aitherdev.int.vpsfree.cz` as a redirecting alias and use
  a leaf certificate with both the wildcard workspace SAN and legacy hostname.
- Keep the root-owned unencrypted CA and create a root-owned Basic Auth
  password readable by `aither`. Remove the workspace flake input, CLI wrappers,
  portal package, and application services from the system configuration.
- Keep the new-session default at `gpt-6-astra` with `xhigh` reasoning. Resume
  an already materialized partial creation without consulting or reapplying the
  current catalog; resolve settings only for genuinely new or replacement
  threads.
- For `complete`, fetch every registered repository, require local and remote
  feature tips to agree, and require that exact head to be an ancestor of the
  configured `origin/<default_branch>`. Report all unmerged or unprovable refs.
  Skip merge proof only for `abandoned`; allow registration-free coordination
  initiatives.
- Put merge proof, idle proof, cluster release, worktree cleanup, tracking
  movement and commit, thread retirement, and runtime cleanup in the single
  journaled `archive` command. Add journaled `revive`, with an explicit
  override for an abandoned archive, preserving identities while clearing
  terminal metadata.
- Reconstruct legacy repository registrations from retained branches when
  worktrees are re-added. Use an explicit base when supplied, otherwise require
  one unambiguous merge base with the configured default branch.
- Expose the App Server's collaboration mode and queue APIs in the portal. Keep
  model and reasoning settings unchanged when switching between Default and
  Plan mode. Immediate messages steer the active turn, while an explicit queue
  action appends FIFO work for later execution.
- Allow `dev-session start <slug> --as-is` to adopt committed active tracking
  that predates a portal manifest. Preserve `plan.md` and `state.md` byte for
  byte, create a fresh shared thread, register canonical existing worktrees,
  and make interrupted retries journaled and idempotent.
- Decode both the legacy string and current structured Codex session-source
  forms. Bind creation recovery to the exact workspace portal source and cwd,
  and reject ambiguous or foreign candidates.
- Define `dev-session delete` as an explicitly confirmed destructive discard
  that removes a session from active/archive discovery, retires its runtime,
  and clears its creation identity while retaining Git branches. Preserve
  discarded tracking in a private recovery directory and reserve this command
  for direct user authorization; normal completion uses `archive`.
- Publish the development-cluster state and cleanup contract in the workspace
  package. Preserve the one proven and already recorded live legacy
  password-reset socket. Refuse pre-contract state without an explicit socket
  identity and require reset instead of inferring ownership during a package
  transition. Version that transition policy independently of the persisted
  state schema, and make switch, rollback, removal, and unregister fail closed
  when ownership cannot be proven.
- Present request-user-input as a one-question-at-a-time browser wizard with
  option notes, free-form answers, unanswered confirmation, per-question
  drafts, and CLI-compatible answer encoding. Keep secret drafts memory-only.
- After an approved Plan-mode plan, offer implementation in the same thread or
  in a new named session initialized from the exact approved plan. Keep the
  mode selector in the composer footer and render Plan mode in purple.
- Assign client message IDs to immediate browser input. Show accepted steers in
  a distinct pending-steer area until the matching transcript item arrives.
  Preserve a reader's transcript position unless it was already following the
  bottom, and expose a New output control while detached.
- Keep terminal but unarchived initiatives interactive. Show their terminal
  lifecycle as ready for an explicit archive operation, and use the actual
  archive location rather than lifecycle alone when deciding whether repository
  state is immutable.
- Give terminal and browser callers the same high-level `archive`, `delete`,
  and `revive` operations. Archival uses one explicit confirmation without a
  typed slug; deletion keeps typed-slug confirmation because it is destructive.
  Give the portal a narrowly scoped internal authorization path that is
  accepted only from its own systemd service cgroup.
- State in durable workspace rules that completing a response or preparing an
  initiative for handoff never authorizes an agent to archive or stop it. The
  user must explicitly request session closure; agents must not schedule
  post-turn cleanup processes.
- Recover archived Codex history by exact thread identity with
  `thread/unarchive`, followed by a verified resume. Make interrupted retries
  idempotent, reject ambiguous or foreign identities, preserve the original
  thread ID, and never resend the initial goal.
- Enable Goldmark table parsing in the shared sanitized Markdown renderer and
  style tables so wide content scrolls horizontally in chat and artifact views.
- Reconcile only the six user-named unfinished sessions. Stop their old tmux
  clients, create fresh shared threads from the existing tracking, and leave
  the unrelated `34` session untouched. Keep the password-reset dev cluster
  running throughout the cutover.
- Suppress reasoning transcript entries whose upstream summary is empty. Keep
  non-empty reasoning summaries visible as sanitized Markdown; they are
  user-facing summaries supplied by Codex, not hidden reasoning tokens.
- Replace per-file top navigation with one `Artifacts` tab. Lazy-load the
  selected registered artifact into an inline preview, render Markdown through
  the existing sanitizer, escape structured and plain text, display supported
  images inline, and retain an explicit download action. Keep manifest
  allowlisting, path confinement, symlink rejection, and size limits intact.
- Replace the public lifecycle commands without compatibility aliases:
  `archive`, `delete`, and `revive` supersede `finalize`, `remove`, and
  `reopen`. Each is one journaled, retryable high-level operation shared by the
  CLI and portal. Portal handlers invoke that command instead of reproducing
  lifecycle sequencing in Go.
- Make `archive` an explicit user action with one confirmation and no typed
  slug. Completed archival proves the exact registered feature heads are
  merged, rejects pending Codex work or dirty worktrees before mutation,
  releases clusters, removes worktrees without force, moves tracking, commits
  only that transition on compatible shared `master`, and retires the runtime.
  Explicit abandonment skips only the merge proof.
- Make `delete` the explicit discard path. It retains branches, releases
  runtime and clusters, removes worktrees, and preserves recoverable material
  outside discovery. A committed tracking path receives an exact deletion
  commit; never-committed tracking is deleted without creating a commit.
- Make `revive` restore either a completed or, after a stronger warning,
  abandoned archive. It commits the exact archive-to-work transition, clears
  terminal manifest fields, preserves repository and conversation identity,
  resumes the archived thread when available, and creates a blank shared
  thread only for a legacy archive without retained conversation identity.
  Repository worktrees remain absent until explicitly re-added.
- Sort active sessions by the newest of Codex thread activity and tracking or
  manifest modification times. Load thread metadata once for the index and
  fall back to filesystem activity when Codex is unavailable. Sort archived
  sessions by their tracking or manifest activity time as well, newest first.

## Lifecycle progress and portal status follow-up

- Reject blank or mismatched tmux identities after session removal. Recover the
  stuck `2026-09-08-discourse-disable-chat` archive only after revalidating its
  committed archive, `thread_retired` journal, absent tmux identity, absent
  process, and exact remaining authority record under the transition and
  per-session locks.
- Give archive, delete, and revive one durable operation contract. Make all
  three browser actions asynchronous, expose journal phase, progress, elapsed
  time, paused/failed state, and deterministic retry, and print the same phase
  labels in the CLI. Keep archive confirmation simple and retain typed
  confirmation for destructive deletion.
- Replace the settings dialog with compact model and reasoning selectors beside
  the Default/Plan and Interrupt controls. Show the active turn and elapsed
  time below the transcript.
- Add `All`, `Messages`, and `Activity` transcript views. Keep errors and
  pending interaction visible in every view, preserve independent scroll and
  disclosure state, and render file changes as safe colorized unified diffs.
- Give the top-level session tabs stable fragment URLs and scoped accessible tab
  behavior so nested cluster service tabs cannot interfere with them.
- Resolve each repository's current local branch head and compare it with the
  authoritative GitHub branch head. Show workflow runs only for an exactly
  pushed current revision, and clearly report not-pushed, remote-ahead,
  divergent, and unknown states.
- Replace the flat cluster status credential list with service and account
  groups. Show service URLs in nested tabs, group fields by account, mask secret
  values, retain generic machine access commands, and separate cluster release
  into a footer.
- Make the index HTML filesystem-only. Load exact Codex activity, credential-free
  cluster summaries, lifecycle progress, and repository counts through a
  bounded singleflight status cache, then reorder sessions by resolved activity
  without moving the reader's scroll position. Reconcile additions, completed
  deletions, archives, and revivals only from a complete status listing generated
  after the current HTML, so partial discovery and stale cache entries cannot
  remove cards or trigger reload loops.
- Deliver an initial tmux/index repair first, then the larger interface update.
  Use independent agents for non-overlapping backend changes and integrate the
  shared server, template, JavaScript, and CSS changes in the primary worktree.

## Compatibility and deployment

The current portal changes require no manifest or conversation migration and do
not change the Codex package. They are deployed from the unmerged workspace
feature branch through the user-profile runtime. A portal/router restart may
briefly disconnect browser clients, so audit active turns, pending prompts,
queued messages, durable queue/send attempts, and lifecycle journals
immediately before switching. It must not restart Codex, managed tmux sessions,
or development clusters. If that audit shows work which the switch would
interrupt or make ambiguous, stop and ask the user before deployment.

The existing CA remains valid and the Basic Auth password may change at the
architecture cutover. The server leaf is renewed when its SAN set changes.
Unknown workspace hosts remain inaccessible, nginx continues to strip Basic
Auth before proxying, the shared router socket is limited to nginx and `aither`,
and per-workspace application sockets remain user-private.

The workspace user package is deployed from its unmerged feature worktree with
`workspace-host switch`; no NixOS rebuild or DNS change is part of this
follow-up. Rollback selects the previous user-profile generation only when its
development-cluster contract is compatible, and retains the matching Codex
store path.

An initiative stays active until all registered branches are merged. Pushing,
testing, deploying, or removing a worktree does not complete it. Pre-merge
follow-up work reuses the same slug and retained branches. Exact ancestry means
squash-only or cherry-picked integration does not qualify.

## Testing plan

- Cover workspace registry validation, Host routing, PWD/flag selection,
  profile switching/rollback, user service arguments, and Codex reconciliation.
- Run Go, Ruby, JavaScript, protocol-contract, and Nix package checks, including
  creation recovery and GPT-6 Astra `xhigh` resolver coverage.
- Test finalization with unmerged, merged, divergent, missing, and unprovable
  feature refs; abandoned and coordination-only initiatives; and aggregate
  diagnostics.
- Test reopening current and legacy archives, metadata cleanup, abandoned
  override, dirty/duplicate/live/symlink states, interrupted recovery, and
  retained-branch worktree reuse.
- Test collaboration-mode discovery and updates, preservation of model and
  reasoning settings, queue CRUD/start behavior, notification refresh, and the
  idle/immediate versus active/steer message paths.
- Test adoption of substantive active tracking without a manifest, exact-file
  preservation, interrupted retry recovery, canonical existing-worktree
  registration, and rejection of uncommitted tracking, unsafe worktree
  provenance, or ambiguous bases. Active project worktrees may remain dirty;
  unsafe, detached, and noncanonical worktrees are preserved but omitted with
  diagnostics.
- Test Codex thread-source strings and objects, creation recovery with the
  portal's custom source, and rejection of foreign or ambiguous candidates.
- Test removal of incomplete, active, archived, dirty, clustered, and
  duplicated states, including confirmation, force behavior, recovery moves,
  runtime retirement, and retained branches.
- Test every request-input answer shape, multi-question navigation and draft
  retention, unanswered confirmation, secret handling, and nonblocking
  auto-resolution.
- Test stale-plan rejection, same-thread implementation, named fresh-session
  implementation, steer receipt reconciliation by client ID, and scroll
  following versus position preservation.
- Evaluate and deploy the aitherdev NixOS configuration and verify
  wildcard/legacy TLS,
  VPN-only nginx, credential permissions, lingering, and absence of system-owned
  portal services.
- Run mandatory change review at `xhigh` after quick checks, then full package
  checks. Deploy the configuration feature branch, leave wildcard DNS deployment
  to the user, validate HTTPS and CLI/browser interoperability, then recover the
  legacy cgroup initiative and verify its two exact branch heads and original
  base commits.
- Reconcile the six explicitly named unfinished sessions after deployment and
  verify browser and CLI attachment, portal repository discovery, and continued
  visualization of the running password-reset cluster.
- Test terminal-but-unarchived browser and CLI interactivity, exact-slug
  confirmation for mutating finalization and stop, portal-only internal
  authorization, and rejection from foreign cgroups and non-interactive agent
  processes.
- Test exact archived-thread recovery, identity mismatches, ambiguous and
  already-unarchived retry states, interrupted recovery, and preservation of the
  thread ID without another initial request.
- Test table elements in chat and artifact Markdown, horizontal overflow styles,
  and continued removal of unsafe HTML and JavaScript URLs.
- Test transcript layout with long conversations so Markdown responses keep
  their natural height and cannot overlap adjacent messages. Keep horizontal
  overflow on dedicated table wrappers rather than entire messages.
- Test that command and tool details start collapsed, expanded state survives
  live transcript refreshes, unchanged refreshes retain the existing DOM, and
  transcript scrolling remains under the reader's control.
- Test empty and non-empty reasoning summaries, the grouped artifact preview
  and download paths, sanitization and escaping, image previews, traversal and
  symlink rejection, unsupported types, and size limits.
- Test `archive` completion and abandonment, all preflight refusals, exact
  tracking commits, cluster and runtime cleanup, retry phases, and preservation
  of unrelated shared-workspace changes.
- Test `delete` for committed and never-committed tracking, forced recovery,
  runtime and cluster cleanup, and absence of the retired command names.
- Test `revive` for completed, abandoned, current, and legacy archives, exact
  thread reuse, blank legacy threads, no implicit worktree recreation,
  conflicting state, and interrupted retries.
- Test active-session ordering by Codex `updatedAt`, filesystem fallback when
  App Server is unavailable, and archived-session ordering by activity time.
