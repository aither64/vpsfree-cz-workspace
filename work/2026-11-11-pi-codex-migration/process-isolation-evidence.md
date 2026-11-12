# Process isolation evidence (Package F)

Architect1, 2026-11-11. Bounded investigation/design only. This is the first
assigned package; no prior package was executing. Session/current environment
identity and the same-session roster were verified. Only this file is owned by
this package. Architect0 owns synthesis, architect2 migration, and the lead
owns acceptance and tracking. No application edits, experiments, builds, model
calls, service launches, configuration changes or lifecycle actions occurred.

## Recommendation and settled boundary

Use **one development-session supervisor, one service cgroup and one mount
namespace**, with lead/member worker processes and their local tool children
inside it. This reflects the user's clarified wording, “One session
cgroup/namespace, with team worker processes inside.” The shared portal remains
the control plane; it does not host cross-session agent workers or execute their
local tools. Never use a worker pool shared across development sessions.

```text
existing portal control plane
  -> session A supervisor [service cgroup + mount namespace A]
       -> lead worker -> shell/MCP/tool children
       -> member workers -> shell/MCP/tool children
  -> session B supervisor [distinct cgroup + mount namespace B]
       -> its own lead/member workers and tools
```

Create workers for loaded work, not for every retained or archived conversation.
Retain dormant history and member identity without permanent worker processes.
Any future idle unloading must preserve accepted/uncertain delivery, queues,
goals, pending tools, subscriptions and registered services. It is not session
archival, deletion or authorization to stop the current session.

| Inside each session boundary | Benefit | Remaining obligation |
| --- | --- | --- |
| Supervisor launching SDK-based lead/member workers | Explicit ownership of tools, resources and callbacks; small application-specific transport | Package our worker entry point; preserve identity, recovery and extension behavior. This is not a new general agent server or Codex protocol emulator. |
| Supervisor launching `pi --mode rpc` lead/member workers with a small reviewed first-party extension if needed | Existing process/JSONL bridge; fewer custom transport decisions | Prove extension hooks cover the required identity/tools/auth boundary and durable submission behavior. RPC correlation is not deduplication. |

Compare these two forms in the already-proposed bounded prototype. SDK access
does not justify moving all team conversations into a shared process after the
clarified worker-process requirement. Neither option has measured Pi resource
cost or proven durable admission; the existing admission/recovery gate remains
mandatory. No third-party extension is selected or vouched for here. Any reused
extension needs exact-source, trust, maintenance and behavioral review.

The proposed side-by-side option leaves the **legacy Codex backend shared**,
keeping existing sessions fully workable. This is a disclosed limitation of the
transition recommendation, not target isolation proof or authorization for any
deployment/action or a user-approved exception. Safe per-session Codex rehoming is
**unestablished and separate work**: existing shared homes, native histories,
socket/authority epochs, receipts, provider recovery and tmux cannot simply be
repointed. Do not claim existing Codex isolation is solved.

## What current source establishes

Source D is dev-workspace
[`6587c4c1cedabee95bcc52f4667e7d33e3a82859`][D]. Canonical bare/default blobs,
repository instructions and relevant launcher/service documentation were read.
These are source findings, not proof that an installed package equals D.

- D [`workspace-codex@.service`][codexunit] and
  [`workspace-portal@.service`][portalunit] use workspace instances, `Type=simple`,
  `Restart=on-failure`, `KillMode=mixed` and a 150-second stop timeout.
  [`workspace-host:1769`][launcher] starts the shared native App Server;
  `run_portal:1689` passes that workspace socket to the portal.
- D [`workspace-tmux@.service`][tmuxunit] is also workspace-scoped.
  `workspace-host:2244` runs/observes the shared tmux server. Asking an already
  running tmux server to create a shell does not make that shell a child of a
  new session supervisor or inherit its namespace.
- D [`workspace-session-services.rb:417–445`][services] durably records a
  resource UUID before `systemd-run --user`, then launches a **separate
  `app.slice` service**, with `Type=exec`, `Restart=no`, `RemainAfterExit=yes`,
  `KillMode=control-group` and a 15-second stop timeout. Identity checks at
  lines 677–705 bind manager, invocation and cgroup. This launcher cannot be
  reused unchanged for an exact single-cgroup/single-namespace Pi boundary.
- Its [temporary-service contract][serviceguide] preserves services through idle
  conversations and integration; uncertain shutdown keeps recovery pending.
  New Pi service starts must go through the owning supervisor, while retaining
  registration/retry/stop proof. Existing registry schemas and legacy shutdown
  contracts must remain supported rather than silently changing old entries.
- At fixed Pi [`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`][P],
  [`bash.ts:125–129`][bash] spawns a shell with explicit cwd/env and Unix
  `detached: true`; its cancellation uses process-group/tree killing.
  Detachment/`setsid`, double-forking or reparenting alone **do not escape a
  cgroup or mount namespace**. Processes retain those memberships through
  fork/exec unless explicitly moved or a new namespace is created.

## Practical systemd and host constraints

A service is the natural owner for a durable supervisor. Start the namespace
before its worker children; use one `ExecStart` process ancestry. A scope can
account for already-created processes but does not itself create their mount
namespace. Ordinary descendants require no `Delegate=yes`; delegation is only
needed if the application itself manages child cgroups, which is not proposed.
Systemd owns the service cgroup and its explicit stop policy. Per-worker abort
must not kill unrelated members; explicit session shutdown needs complete
descendant proof. Final policy/recovery details belong to implementation design.

The installed **systemd 260.5** `systemd.exec(5)` documents these important limits:

- User-manager mount namespacing requires the corresponding user-namespace
  capability; modern `PrivateMounts`/`PrivateTmp` settings imply `PrivateUsers`.
  A user service cannot be assumed to have host `CAP_SYS_ADMIN`.
- `JoinsNamespaceOf` can share private temporary directories but **does not
  share the same kernel mount namespace**. Separate units are not equivalent
  to the topology above. `ExecStartPre` mounts also do not carry into a separately
  created `ExecStart` namespace.
- `PrivateTmp=yes` uses host-disk backing and removes its temporary files on
  service stop; `PrivateTmp=disconnected` uses tmpfs. Neither implicitly defines
  a persistent session scratch/recovery policy. `RuntimeDirectory` normally
  disappears on stop and is not a durable recovery store.
- `PrivateMounts` limits mount propagation; it does not make the workspace/home
  inaccessible or isolate network, user identity or every external service.

Declared host source H is vpsfree-cz-configuration
[`e91c8d21055b7110182fd4c531389947f180e359`][H]. Aitherdev
[`config.nix`][hostconfig] declares Nix sandboxing and `trusted-users = [ "aither" ]`
(162–180), user lingering/wheel membership (214–218) and wheel sudo (283–294).
[`hardware.nix`][hardware] declares ext4 root and no swap. D's
[`host-module.nix`][hostmodule] owns proxy/auth/TLS substrate, not a session
namespace launcher or a declared user-namespace permission guarantee.

Narrow read-only metadata observed: `systemctl --version` reports 260.5;
`user.max_user_namespaces=386016`; the optional
`kernel.unprivileged_userns_clone` and AppArmor userns sysctl files are absent;
`findmnt --target /tmp` and `/home/aither` report the root ext4 filesystem with
`rw,relatime`. These observations do **not** prove namespace setup succeeds,
controller delegation, the complete host configuration or quota support.

**Rootless setup remains unverified.** `PrivateUsers` also changes host-root,
setuid/sudo and group-mapping semantics. Verify required Nix socket, repository,
credential-file and development-tool access without printing secrets. If those
workflows require the original host user namespace, a narrow host-managed
system service can create the mount namespace and run the supervisor as the
original UID without granting agents host `CAP_SYS_ADMIN`. That requires an
explicit host-package/permission decision; it is not implemented or approved
here. Do not silently degrade the required boundary if rootless launch fails.
No kernel work or broader hardening project is warranted by this evidence.

## Inheritance, external work and enforcement

Local shell, stdio MCP, compiler and other children spawned inside the boundary
inherit it. New workers must not launch their tools through the shared portal
process. An already-running service reached by RPC does not inherit client
membership. In particular:

- `systemd-run --user` starts work through the user manager, normally outside
  the invoking service; the existing temporary-service launcher demonstrates it.
- Nix clients can remain inside, while daemon builds/substitutions execute under
  the Nix daemon's own ownership/sandbox. Store writes, daemon cache and remote
  builders are not session-private `/tmp` usage or session-cgroup resource use.
- SSH jobs, containers/VMs and existing remote MCP/tmux services likewise need
  their own ownership/accounting. These are delegated external work, not local
  inherited subprocesses. Do not label their costs as captured by the session
  cgroup or claim all host effects are contained.

This is the existing trusted-local-operator model, not a hostile same-UID
sandbox. Writable worktrees/home, permitted manager sockets and trusted Nix
access remain powerful. Explicit process launch routing and correct ownership
enforce the supported topology; they do not prevent a fully privileged operator
from bypassing it. Do not add speculative escape prevention or silently remove
working host administration paths.

| Mechanism | What it establishes |
| --- | --- |
| Cgroup membership, CPU/memory/task/I/O counters | Attribution for members; includes page cache/kernel charges, not just heap. Not a disk-capacity quota. |
| `MemoryHigh/Max`, `TasksMax`, CPU/I/O limits | Actual controls when supported/configured; defaults and parent limits must be checked. No limits are selected here. |
| Mount namespace + session backing paths | A distinct path/mount view and scratch ownership; not a storage cap or host-access sandbox. |
| `TMPDIR` alone | Convention followed by cooperating tools, not isolation or enforcement. |
| Process RSS/PSS | Process-memory observations, separate from charged cache and filesystem capacity. |

## Temporary storage and allocation

Prefer disk-backed session-owned scratch bound into `/tmp` and `/var/tmp` for
the prototype, with `TMPDIR` set consistently. Keep sockets and durable
admission/history/recovery records outside disposable scratch. Preserve scratch
through supervisor failure/restart until its ownership and command effects are
reconciled; retention/removal needs an explicit lifecycle contract. Do not let
unit-stop defaults unexpectedly erase recovery inputs. No cleanup is authorized
by this assessment or its completion.

Report directory `du`/allocated blocks as **observed directory usage**, not a
hard allocation budget. It misses deleted-but-open files, has hardlink/shared
extent attribution caveats, and does not fully allocate filesystem metadata.
Logical file sizes are different again. A bind mount of a directory on the
shared ext4 filesystem does not create a separate allocator: `df`/`statvfs`
there still describes the shared filesystem.

A dedicated filesystem has allocator-level free/used space and can impose its
own capacity. A dedicated tmpfs can bound size/inodes and count open-unlinked
allocations, but consumes memory (and swap where available); it is a different
budget from disk-backed build scratch. Filesystem project quotas can potentially
enforce per-project disk usage, but require supported features, mount policy,
project assignment and privileged provisioning. Those prerequisites are
unverified; per-user quotas would not separate sessions sharing the same UID.
Do not add quotas, per-session loop filesystems or tmpfs sizing as assumed work.
The immediate deliverable is honest accounting; hard disk allocation limits
need a separate explicit requirement and host decision.

## Future package implications and bounded acceptance

These are proposed boundaries for architect0/lead allocation, not released
implementation assignments. Current ownership remains this evidence file only.

| Future owner/deliverable | Files/interfaces and dependency | Acceptance/evidence |
| --- | --- | --- |
| Lead-assigned runtime implementer: session supervisor/worker launcher | D `libexec/workspace-host`, `nix/systemd/`, package entry points and runtime adapter; depends on host privilege choice and backend/durable-admission brief | Two disposable sessions have distinct cgroup/mount IDs; each lead/member/tool descendant shares its own boundary. No dormant-history worker. Record exact source/package/unit identity. |
| Lead-assigned runtime implementer: service/lifecycle integration | D `libexec/workspace-session-services.rb`, session/runtime contracts, service cleanup/readers; depends on supervisor identity and retained schema/recovery design | New registered Pi services launch inside owning boundary; exact-ID retries do not duplicate. Old registrations and writable legacy Codex continue to work. No broad adoption of existing processes. |
| Lead-assigned host owner, only if required: namespace privilege/storage support | D host module and H aitherdev configuration; separate configuration/deployment scope | Required ordinary UID, group, Nix and host-tool access works without weakening boundary. Unsupported setup refuses visibly; no implicit privileged fallback. |

First prototype checks should be a small disposable batch: verify namespace
and cgroup IDs for supervisor, lead/member workers and a shell grandchild;
verify distinct temporary views and crash/restart retention; exercise one
registered service and explicit stop; check Nix-client access while identifying
daemon work as external. Test per-worker cancellation and whole-session teardown
only in authorized fixtures. Include a deleted-open scratch file to distinguish
directory telemetry from allocator usage, and show bind-mount `df` remains
shared. Record CPU, PSS and cgroup anon/file/kernel separately for a few loaded
workers; do not extrapolate thousands of stored histories into live processes.

Longer tests, after committed implementation/review, must cover interrupted
launch/stop, uncertain tool effects, restart/recovery, mixed legacy/Pi operation,
package transitions and representative SDK-versus-RPC history/provider/durable
admission cases. This package ran none of these tests. Package D's existing
[resource measurements](resource-evidence.md) remain the only measured process
costs; no Pi memory saving, throughput or capacity claim is supported.

Checks for this artifact: exact source references and local manuals inspected;
no runtime acceptance claim, independent-review invocation or source commit.
Lead owns state/portal linkage and package acceptance. Remaining blockers are
rootless/full-workflow feasibility, final host permission route and the already
accepted supported durable-admission proof, not further first-pass inventory.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/

[D]: https://github.com/aither64/dev-workspace/tree/6587c4c1cedabee95bcc52f4667e7d33e3a82859
[P]: https://github.com/earendil-works/pi/tree/a22b888a58fe55b668cc45b80749ec88d4eb4ddc
[H]: https://github.com/vpsfreecz/vpsfree-cz-configuration/tree/e91c8d21055b7110182fd4c531389947f180e359
[codexunit]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/nix/systemd/workspace-codex%40.service
[portalunit]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/nix/systemd/workspace-portal%40.service
[tmuxunit]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/nix/systemd/workspace-tmux%40.service
[launcher]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/libexec/workspace-host#L1769
[services]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/libexec/workspace-session-services.rb#L417
[serviceguide]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/docs/dev-sessions.md#temporary-services
[bash]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/tools/bash.ts#L125
[hostconfig]: https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/e91c8d21055b7110182fd4c531389947f180e359/cluster/cz.vpsfree/machines/aitherdev/config.nix
[hardware]: https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/e91c8d21055b7110182fd4c531389947f180e359/cluster/cz.vpsfree/machines/aitherdev/hardware.nix
[hostmodule]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/nix/host-module.nix
