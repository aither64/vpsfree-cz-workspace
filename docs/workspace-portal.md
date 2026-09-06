# Workspace portal

The workspace portal is the browser view for development initiatives:

```text
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/
```

The former
`vpsfree-cz-workspace.aitherdev.int.vpsfree.cz` address redirects here.

It lists active and archived initiatives that contain `portal.yml`, with the
newest dated sessions first. Each initiative uses full-width tabs for its Codex
conversation, handoff commands, repositories, development clusters, plan,
state, and curated artifacts. It renders Codex output as sanitized Markdown.
An active conversation can receive messages, be interrupted, answer Codex
questions, handle supported command or file-change approvals, and change its
model and reasoning effort. Enter sends a message; Shift+Enter inserts a line
break.

The portal is not a shell or a general file browser. It exposes `plan.md`,
`state.md`, and files explicitly listed in `portal.yml`. Curated artifacts are
limited to plain text, Markdown, JSON, YAML, and passive raster images. Active
formats such as HTML, SVG, JavaScript, XHTML, and XML are refused.

## Starting and attaching to sessions

The New session form accepts a short name and an initial request. It runs the
packaged `dev-session`, journals creation before changing initiative state,
creates a persisted Codex thread, and sends the request as the first turn. A
retry uses the same dated slug and must contain the same request. Completed
requests replay their existing result instead of creating another session or
turn. Creation reports success only after the rollout exists and its first user
message exactly matches the submitted request. The terminal client starts
after that verification, so it cannot race an empty thread.

The terminal command asks for the same initial request before it creates a new
Codex session, then attaches to the persisted thread:

```text
$ dev-session start example
Initial request: Investigate the reported API failure.
```

For scripts or redirected input, place the request in a file:

```sh
dev-session start example --goal-file request.txt --no-attach
```

Without an interactive terminal, a new Codex session requires `--goal-file`.
An existing session that already has a persisted thread can be attached without
another request.

Codex receives the workspace instructions and selects affected repositories.
The terminal and browser share one App Server thread and a dedicated
per-workspace tmux server. Use the registry-backed command for terminal
actions:

```sh
dev-session attach 2026-09-03-example
dev-session stop 2026-09-03-example
dev-session url 2026-09-03-example
```

The full dated slug is accepted directly. You can also use a short name when it
matches exactly one session.

Fork session copies the Codex conversation and selected model settings into a
new session. It does not copy worktrees, tracking files, artifacts, or
development clusters. The equivalent terminal command is:

```sh
dev-session fork 2026-09-03-example alternate-approach
```

The portal discovers attached Git worktrees directly from the workspace and
canonical bare repositories. A worktree therefore appears even when an older
helper did not record it in `portal.yml`. The manifest remains authoritative
when it already contains the repository, and conflicting live metadata is
reported instead of replacing the recorded values.

The Clusters tab recognizes vpsAdmin and vpsAdminOS state owned by the session.
It shows the verified runner state, topology, network, service links, SSH
commands, and development credentials. Release cluster stops the matching
runner and removes its temporary state. The index marks sessions with running
clusters.

Prepare to finish asks Codex to complete work that is already in scope and set
the tracking lifecycle to `complete` only when no work remains. Archive session
first proves that every registered feature head is merged when the lifecycle is
`complete`. It stops the terminal client and proves the shared thread idle while
browser mutations are gated, then releases development clusters, validates and
removes clean worktrees, moves tracking to `archive/`, commits only that archive
move on the shared workspace `master`, and stops the session. If release or
finalization fails, it restores the terminal client. It never pushes `master`.

The page shows attach and conversation controls only when host-only authority
under the private per-workspace runtime directory is ready and matches the live
tmux session, App Server socket, and persisted thread working directory. Stopped,
archived, forged, or stale sessions remain passive. A verified persisted thread
can still provide a read-only transcript after stop, reboot, completion, or
archival.

Terminal and browser sessions use the App Server socket below
`$XDG_RUNTIME_DIR/vpsfree-workspaces/<name>/`. The App Server runs the Codex
package from the current aitherdev system. The user service validates a new
system Codex against the bundled protocol contract and model catalog before it
adopts it. The transition gate blocks new browser and CLI mutations, quiesces
terminal clients, checks every thread for idleness, restarts each App Server and
portal as a pair, and then restores the clients. A compatible update waits on a
five-minute retry timer while a turn is active. An incompatible update leaves
the last compatible store path active. Stored client versions are diagnostic
history and do not invalidate sessions after a compatible upgrade.

`stop`, `remove`, and `finalize` quiesce the managed terminal client and refuse
an active turn. If tmux disappears before authority cleanup, inspect the
session and remove only a validated, idle stale record:

```sh
dev-session recover-stale 2026-09-03-example
```

The local journal provides at-most-once initial-goal delivery. Codex does not
accept caller-supplied idempotency keys for thread or turn creation, so the
helper durably records an initial submission attempt in a temporary schema-2
manifest before calling `turn/start`. A retry against the same unmaterialized
thread fails closed; it does not rely on a briefly stale idle status. Once
history materializes, the retry requires exactly one matching initial user
message. If an App Server restart removes the recorded memory-only thread,
creation-only reconciliation can select or create one exact fresh replacement
and clear the attempt marker.
A crash between recording the attempt and sending it can therefore require an
App Server restart before retrying.

A lost `thread/start` response can race the App Server's in-memory registration
and leave an unprompted orphan. Recovery refuses multiple visible candidates;
restarting the App Server clears such memory-only orphans. This does not resend
the initial goal because initial-goal delivery has its own durable attempt
marker. Completion removes the marker and writes the ordinary schema-1
manifest, so completed sessions remain readable after a rollback. A previous
portal version intentionally rejects an in-flight schema-2 creation; redeploy
the current version to reconcile it.

A ready manifest written by the earlier empty-thread implementation is not
silently adopted when its rollout is still missing. Archive that incomplete
session and start a new one with an initial request.

## Portal manifest

`dev-session start` creates `work/<slug>/portal.yml`. Worktree creation records
the repository identity, branch, GitHub repository, default branch, and initial
commit. Cleanup records final commits, and finalization preserves the same URL
under `archive/<slug>`. The example is the stable schema written after creation;
schema 2 exists only while an initial goal has an unresolved delivery outcome.

```yaml
schema: 1
slug: 2026-09-03-example
forked_from: 2026-09-03-original
codex:
  thread_id: 01a00000-0000-0000-0000-000000000000
  socket_path: /run/user/1000/vpsfree-workspaces/vpsfree-cz/app-server.sock
  client_version: 0.152.1
creation:
  state: ready
  initial_goal_sent: true
  goal_sha256: 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
repositories:
  - name: vpsadmin
    project: vpsadmin
    github: vpsfreecz/vpsadmin
    branch: 2026-09-03-example
    default_branch: master
    initial_base_sha: 0123456789abcdef0123456789abcdef01234567
artifacts:
  - label: Deployment notes
    path: deployment.md
```

The version is informational; thread ID, canonical working directory, App
Server endpoint, and live host authority control access. Do not list
credentials, private keys, caches, or bulk captures. Artifact paths cannot
leave the tracking directory, and symlinks are refused. Unknown fields,
explicit nulls, aliases, duplicate keys, tags, and multiple YAML documents are
invalid.

## Authentication and security boundary

nginx accepts HTTPS only from the WireGuard network and requires Basic
Authentication. It proxies to a group-restricted Host router socket; each
portal listens on a user-private Unix socket. The portal cannot read nginx's
password hash, TLS key, or CA key, and its sockets are not mounted into the
development LXC.

The portal rejects mutations without the exact origin, uses a restrictive
content security policy and sanitized Markdown, and does not expose general
filesystem, shell, or App Server RPC access. Page rendering reads Git worktree
registrations and immutable metadata only from the workspace checkout and
canonical bare repositories; it does not run Git in writable feature
worktrees. Workspace manifests are display metadata; Codex mutations also
check uid-private host authority against tmux and the App Server.

The Basic Auth username is `aither`. Its random plaintext password is stored at
`/var/lib/vpsfree-workspace-portal-password/password`. It is owned by root and
readable only by the dedicated group containing `aither`; the portal services
cannot modify it. NixOS activation derives the root-owned nginx hash from this
file. Neither value enters Git or the Nix store. Browsers commonly cache Basic
Auth credentials until their session is closed.

Portal access grants control comparable to an interactive Codex client running
as `aither`. Keep the password unique, keep the hostname VPN-only, and remove
the private CA from a lost device. Permission approval request types that
cannot be verified through the App Server remain terminal-only.

## Private CA and certificate renewal

The first aitherdev activation creates the CA and leaf directly in root-owned
`/var/lib/vpsfree-workspace-pki`, installs the nginx leaf pair, and exports the
public CA to the user-readable
`/var/lib/vpsfree-workspace-portal-public/ca.pem`.

The NixOS configuration installs the single host-side reconciler. Run it as
root to validate the password and CA state, create missing credentials, or
renew an expiring leaf:

```sh
sudo workspace-portal-substrate-reconcile
sudo systemctl reload nginx.service
```

The unencrypted CA key is protected by root ownership and mode `0600`; the
portal cannot read it. The nginx key is `root:nginx` mode `0640`. Certificates
and keys are switched as atomic versioned pairs. A weekly timer renews a leaf
with less than 30 days remaining, preserves the CA, and reloads nginx. Repeated
deployments validate and reuse existing state.

Copy only the public CA to VPN clients and trust it for TLS. Never copy the CA
key or server keys to a client.

Removing the NixOS configuration does not revoke the CA on clients. To
decommission the portal permanently, remove the CA from every client's trust
store, remove the internal DNS record, and delete the CA state on aitherdev.
If the CA key may have been exposed, stop the portal, remove client trust and
the DNS record, delete the compromised CA state, and redeploy to create a new
CA. Trust the replacement public CA only after checking it on aitherdev.

## Packaging and deployment

The workspace flake owns `packages.x86_64-linux.workspace-portal`.
`vpsfree-cz-configuration` does not consume or pin it. NixOS owns only nginx,
VPN exposure, TLS and Basic Auth credentials, user lingering, and the ordinary
system Codex package. The workspace flake owns the router, portal, session and
cluster commands, and user systemd units.

Deploy the aitherdev substrate and wildcard internal DNS first. This stops the
former system-owned portal runtime; existing portal and terminal sessions are
not migrated. Initiative tracking and project branches remain on disk and can
be reopened from the new runtime.

Register the workspace once and install the user application from the reviewed
workspace feature worktree:

```sh
nix run /path/to/workspace-feature#workspace-host -- register vpsfree-cz \
  /home/aither/workspace/ai/vpsfree.cz \
  --hostname vpsfree-cz.workspace.aitherdev.int.vpsfree.cz \
  --alias vpsfree-cz-workspace.aitherdev.int.vpsfree.cz
nix run /path/to/workspace-feature#workspace-host -- switch \
  --source /path/to/workspace-feature
```

To retire a registered workspace, first finish or stop its sessions, then run
`workspace-host unregister NAME`. The command quiesces its terminal clients,
disables the three instance services, updates the registry atomically, and
restarts the router. It also retires that name's runtime sockets and session
authority before the name can be registered for another workspace root.

The DNS wildcard is `*.workspace.aitherdev.int.vpsfree.cz`; point it at
aitherdev's VPN address. NixOS creates the password, CA, wildcard certificate,
and nginx proxy automatically. `workspace-host status` shows the active user
package, Codex path, and registered workspace URLs.

The first user-profile switch starts the router, App Server, tmux server, and
portal. Start a fresh session for browser or terminal testing. Existing
initiative directories and retained feature branches can be reopened without
preserving their old Codex process or conversation.

Later portal changes need only `workspace-host switch --source PATH`. The
command builds a candidate, checks it against the system Codex, adds a user
profile generation, updates stable commands and units, and restarts the router
and portal as one transaction. It has no nonactivating mode because changing
the stable commands without restarting the services would mix two application
generations. Each profile generation retains the Codex store path it was tested
with. Failed updates restore the preceding profile, Codex root, links, and
services, then remove the rejected profile generation so rollback cannot select
it later. A failed first installation has no preceding generation to restore;
it leaves the validated candidate installed so the same `switch` can be
retried. `workspace-host rollback` selects the preceding application and Codex
pair and refuses while a thread is active.

This clean-restart release does not make its transient reopened-tracking
metadata readable by the preceding portal generation. Do not roll back between
`dev-session reopen` and successful creation of that initiative's fresh
conversation. If a rollback happens in that window, the plan, state, and
branches remain intact; switch forward to this release and retry the same
session creation request. The provenance fields are removed when the fresh
conversation becomes ready, after which the preceding parser can read the
manifest again.

Before rolling back the NixOS substrate, stop the user layer so two portal
runtimes cannot run at once:

```sh
workspace-host suspend
```

No conversation migration is attempted in either direction. Redeploying the
hybrid substrate and running `workspace-host switch` recreates the user
services. Routine portal iteration does not need a NixOS rebuild or a
configuration input update.

The portal continues serving initiative status when GitHub or the App Server is
temporarily unavailable. Only the affected integration reports an error. The
browser displays the 20 most recent turns; attach from a terminal for older
conversation history.

## ChatGPT desktop and mobile access

The portal works in a macOS or mobile browser once the VPN is connected,
internal DNS resolves, and the private CA is trusted. It does not register its
sessions as native ChatGPT Remote sessions.

Separately, the ChatGPT macOS app can connect to aitherdev over SSH and start
its own remote Codex App Server. ChatGPT mobile can then control those native
remote chats through a paired desktop host. These are a separate session
population from the workspace portal.
