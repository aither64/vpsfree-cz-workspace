# 2026-09-06-portal-config-deployment-policy

## Goal

Finish the workspace portal as a user-managed, multi-workspace service while
keeping only its privileged HTTPS substrate in the aitherdev NixOS
configuration. Unify CLI and browser sessions, retain system-managed Codex
updates, correct creation recovery and the `xhigh` default, and make initiative
completion mean that every registered feature head is provably merged.

Also provide a safe `dev-session reopen` workflow and use it to restore
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

## Affected repositories

- Coordination workspace (`aither64/vpsfree-cz-workspace`): hybrid user runtime,
  registry and routing, CLI dispatch, lifecycle enforcement and recovery,
  tests, documentation, and durable agent rules.
- `vpsfree-cz-configuration`: privileged nginx/TLS/Basic Auth substrate,
  wildcard workspace domain, user lingering, and removal of system-owned
  workspace application services and packages.

Both repositories use the existing
`2026-09-06-portal-config-deployment-policy` feature branches. Their default
branches must not receive the portal implementation until the user explicitly
requests integration.

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
- Add non-mutating `finalize --check` so the portal proves finalizability before
  releasing clusters. Add journaled `reopen`, with an explicit override for an
  abandoned archive, preserving identities while clearing terminal metadata.
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
- Redefine `dev-session remove` as an explicitly confirmed destructive discard
  that removes a session from active/archive discovery, retires its runtime,
  and clears its creation identity while retaining Git branches. Preserve
  discarded tracking in a private recovery directory and reserve this command
  for direct user authorization; normal completion still uses `finalize`.
- Publish the development-cluster state and cleanup contract in the workspace
  package. Preserve the one proven live legacy password-reset socket, migrate
  only unique process-free stale state to workspace-scoped socket identity, and
  make switch, rollback, removal, and unregister fail closed when ownership
  cannot be proven.
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
- Reconcile only the six user-named unfinished sessions. Stop their old tmux
  clients, create fresh shared threads from the existing tracking, and leave
  the unrelated `34` session untouched. Keep the password-reset dev cluster
  running throughout the cutover.

## Compatibility and deployment

The one-time architecture change is a clean restart, not a compatibility
migration. Deploying the NixOS substrate stops the former system-owned portal,
Codex, and tmux services. The user-profile switch starts a new runtime; old
Codex processes, conversations, and socket metadata do not have to survive.
Initiative tracking, canonical repositories, worktrees, and retained feature
branches remain on disk. The cgroup initiative is reopened under its original
slug and branches, then receives a fresh Codex session if needed.

The unfinished-session reconciliation follows the same clean-restart rule for
conversation state. It does not import old rollouts or infer arbitrary tmux
sessions. Durable tracking and repository state remain authoritative. The six
new conversations start with that existing context, and their old rollout
files remain unbound. The independently running password-reset cluster is not
stopped or recreated.

The follow-up portal changes require no manifest migration and do not change
the Codex package. They are deployed from the unmerged workspace feature
branch through the user-profile runtime. A portal/router restart may briefly
disconnect browser clients, so live deployment requires explicit user approval
after reporting active turns and pending requests; it must not restart Codex or
managed tmux sessions. The unpublished v1 submission ledger is intentionally
not migrated: the new runtime starts with a separate schema-2 ledger. Before
that cutover, audit active turns, pending prompts, browser-local queue/send
receipts, and durable queue/send attempts, and resolve or explicitly discard
every ambiguous submission so the restart cannot duplicate or strand it.

The existing CA remains valid and the Basic Auth password may change at the
architecture cutover. The server leaf is renewed when its SAN set changes.
Unknown workspace hosts remain inaccessible, nginx continues to strip Basic
Auth before proxying, the shared router socket is limited to nginx and `aither`,
and per-workspace application sockets remain user-private.

The workspace user package is deployed from its unmerged feature worktree. The
configuration feature branch is deployed directly to aitherdev. The agent can
deploy aitherdev from that feature worktree; the user owns deployment of the
internal wildcard DNS. Portal iteration afterward requires only
`workspace-host switch`, not a NixOS rebuild. Rollback selects the previous user
profile generation and retains the last compatible Codex store path.

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
