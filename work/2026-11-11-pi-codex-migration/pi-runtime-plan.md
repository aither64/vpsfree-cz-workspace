# Initial Pi runtime implementation brief

Package M, architect1, 2026-11-12. Plan only; F completed and accepted before
this assignment. Session/environment/retained workspace-write access verified;
unchanged required guidance and documentation skill reused. Only this file is
owned here. Architect0 integrates it into implementation-plan.md/design.md;
the lead assigns implementers and accepts package release. No implementation,
prototype, runtime test, login, deployment, lifecycle action or commit ran.

## Scope and release boundaries

Integrate/evaluate **new opt-in Pi sessions alongside unchanged Codex sessions**.
One backend per development session initially. Keep the current portal and a
narrow conversation-backend interface; no general agent server, Codex protocol
emulator, conversion, cutover or retirement tooling. Future removal needs code
separation now, not migration implementation. Existing shared Codex execution
remains a disclosed limitation of coexistence, not newly isolated execution.

```text
shared portal -> session service / supervisor [one cgroup + exact mount namespace]
                  -> loaded lead worker -> local tools
                  -> loaded member workers -> local tools
                  -> registered session services
```

Each Pi development session gets its own supervisor and namespace. Workers are
separate processes; dormant histories/retained members require no worker. Keep
the supervisor while owned services or recovery obligations exist; this brief
does not add automatic session shutdown. The portal never spawns Pi tools outside
the supervisor. No worker pool spans development sessions.

Two delivery gates allow an early usable pilot without overstating recovery:

| Gate | Required result | Held capabilities |
| --- | --- | --- |
| **Pilot-ready** | Supported SDK or stock RPC adapter; manual conversation/history/stop; settled session/caller identity, launch permissions, shared auth-directory and honest outcome contracts; process accounting | Lost acknowledgements remain durable **Unknown**, visibly held with no automatic resubmit. Automated team/queue/fallback recovery stays disabled until its stronger contract passes. Daybreak does not block independent seam/UI work or a pilot on an already supported provider. |
| **Automation-ready** | Supported durable request identity, admission/reconciliation and recovery at tested crash boundaries, without a maintained Pi fork; identity and service/command ownership tests pass | No host outbox presented as proof Pi accepted a request; no exactly-once claim for arbitrary external tool effects. Unsupported cases remain held. Full planned team/portal parity is still required for the initial integration's final acceptance. |

The pilot's reduced capabilities must be explicit in its backend capability
result and portal behavior, not silent successful no-ops. Unsupported namespace
or required tool access blocks worker launch even for the pilot.

## Runtime interfaces and invariants

**Launcher and identity.** Prefer a small supervisor subcommand in the existing
Go binary, launching either SDK workers or stock Pi RPC workers. Its private
control channel supports ensure/inspect, worker load/unload, command/service
start, cancel/stop and resource observation; conversation dispatch remains behind
the separate backend adapter. Trusted host authority supplies workspace/session
incarnation, backend, member and package identity. Worker connections inherit a
host-bound identity; prompt arguments/environment cannot choose the sender.

Persist ownership outside scratch: session incarnation, backend, package/store
identity, supervisor generation, boot ID, unit/invocation ID, cgroup path,
supervisor PID/start identity, observed mount-namespace identity, backing paths,
and live worker/command/service handles. Extend existing authority/locking and
package-capability contracts rather than invent a parallel session registry.
PID, pathname or namespace inode alone is insufficient across reuse/reboot.
Verify live identity and expected generation before cancellation or adoption;
stale handles refuse. Namespace identities are observations, not durable handles
to join after restart.

**Restart.** Record launch intent before spawning and reconcile a lost response
using the same operation identity. One owner starts each generation. A replacement
must prove the old invocation's descendants terminated before admitting work;
unknown termination holds recovery. Recreate the namespace over retained backing
paths, publish the new generation only after verifying it, then restore eligible
idle workers. Do not automatically repeat accepted/uncertain prompts, commands
or services. Supervisor failure may terminate all its descendants through systemd;
record interrupted/unknown effects honestly. Portal restart alone must not kill
the independent supervisor.

**Cancellation and services.** Worker/command process handles and process groups
support targeted cancellation, followed by exit verification. A shared cgroup
proves whole-session membership, not ownership of every daemonized descendant
by one worker. Ambiguous survivors keep the affected stop/resource pending;
never retire it or kill another member to manufacture success. An explicitly
authorized whole-session stop can drain the complete service cgroup and verify
emptiness. Tool cancellation does not delete scratch or close the session.

For new Pi registrations, retain the service resource UUID, request digest,
durable-before-launch intent, exact retry and unknown-shutdown semantics, but
route spawning through the supervisor. The existing sibling `app.slice`
`systemd-run` path remains for legacy registrations. Add a versioned execution
kind/handle rather than reinterpret their saved unit identities. Services remain
alive while conversations are idle; worker unload must not stop them. Preserve
existing archive/delete recovery contracts without invoking them in this task.

**Scratch, credentials and accounting.** Resolve two disk-backed session-owned
directories for `/tmp` and `/var/tmp`, keyed by session incarnation; bind them
inside the one namespace and set `TMPDIR` consistently. Keep durable records and
the control socket outside scratch. A unit failure/stop removes its mount view,
not its backing data: retain backing paths until explicit authorized cleanup and
reconciled command/service ownership. Avoid `PrivateTmp`/`RuntimeDirectory`
defaults that erase recovery inputs on stop.

All Pi workers sharing an account use the **same canonical native Pi credential
containing directory**, writable with common lock sidecars and atomic replacement
visibility. It remains outside private scratch and its cleanup scope. Resolve
the same configured store/provider key in SDK and RPC paths; no per-worker OAuth
copies, private snapshots or file-only binds. Provider/account ownership and
initial login belong to the authentication package; this package neither reads
tokens nor imports a rotating legacy Codex grant.

Expose timestamped cgroup CPU, memory/peak (anonymous/cache/kernel separately),
tasks and I/O plus observed backing-directory allocated/logical bytes. `du` misses
open-unlinked allocations; `df` on a bind directory still describes the shared
filesystem. No quota, per-session filesystem or tmpfs budget is introduced.
Local fork/exec descendants inherit membership, including ordinary detached
shell children. Nix daemon builds, shared tmux/remote MCP, SSH and VM/container
work do not inherit it; label external/shared costs as excluded. Preserve normal
Nix client access without claiming its daemon resources belong to this cgroup.

## Implementation packages and file ownership

Paths below are in dev-workspace unless marked H. New paths are proposals for
architect0's final allocation. Each package has **one lead-assigned implementer**;
no member is assigned by this document. Sequence overlapping authority, launcher
and packaging edits under one owner/window. The auth package owns credential
policy/login; the backend-seam package owns neutral conversation types/UI.

| Package / proposed owner | Deliverable and file boundary | Dependencies / acceptance evidence |
| --- | --- | --- |
| M0 / runtime implementer with architect0 decision | Disposable P0 fixture and SDK-versus-RPC decision record; proposed `test/pi_runtime/` fixtures | Accepted source pins and fake auth fixtures. Record Pilot/Automation results separately, exact package/revisions, namespace/tool-access results and unresolved gates. No production state used. |
| M1 / runtime implementer | New `portal/cmd/workspace-portal/pi_runtime.go`, `portal/internal/piruntime/`; integrate `libexec/workspace-host`, `nix/systemd/workspace-pi-session@.service` (new) | M0 launch route and stable authority interface. Two sessions have distinct boundaries; all local workers/tools/services share their own exact boundary. Correct restart/generation/stop holds and resource projection. |
| M2 / worker implementer | New pinned `pi-runtime/` package: SDK entry point **or** first-party RPC extension/adapter selected by M0; necessary private worker transport | M0 supported API choice; backend-seam and auth owners settle message/identity/store references. Manual stream/history/stop and capability reporting work; no cross-session runtime or credential copies. Remove the unused probe alternative from production packaging. |
| M3 / runtime implementer, after M1 | `libexec/workspace-session-services.rb`; `portal/internal/session/{authority.go,recovery.go,runtime-contract.json,service_cleanup.go}`; `portal/internal/web/{session_services,service_cleanup_handoff}.go`; existing `test/dev_session/`, `test/workspace_host/` service tests | M1 handles plus backend authority/schema contract. Pi services launch inside supervisor; old registry fixtures retain their original execution/recovery. Lost-ack retries do not duplicate, ambiguous stops do not retire. Coordinate any additional lifecycle helper change before expanding files. |
| M4 / packaging implementer, after settled runtime | `flake.nix`, `flake.lock`, `nix/workspace-portal.nix`; new worker derivation and focused check wiring; `docs/dev-sessions.md`, `docs/workspace-portal.md` | Selected supported runtime/dependency closure, M1–M3 and compatibility fences. Packaged commands work without ambient npm installs; legacy Codex package/service paths stay supported; incompatible readers refuse new Pi state. |
| H0 / host implementer, **conditional** | `nix/host-module.nix`; H `cluster/cz.vpsfree/machines/aitherdev/{config,dev-workspace-site}.nix` only where needed | Rootless route fails a required capability and lead accepts bounded host route. Narrow host-created mount namespace runs supervisor as original UID; no host `CAP_SYS_ADMIN` granted to agents. Separate configuration review/deployment remains required. No kernel/quota redesign. |

M1 needs only settled launch/identity contracts; independent seam/UI preparation
need not await unrelated provider access. M2 pilot can proceed with safe held
Unknown outcomes; automated dispatch/recovery is not released before its gate.
M3 requires versioned service ownership, not completion of future migration work.

## Finite P0 and verification plan

Use one disposable two-session fixture, one lead and one member each, plus a
local tool and registered service. First try the rootless systemd user-service
route, namespace creation before the single `ExecStart` supervisor. Check UID/
groups, repository access, shared fake credential directory/lock/replacement,
Nix socket and required setuid/sudo tool semantics without weakening policy.
`JoinsNamespaceOf`, separate per-worker units and `ExecStartPre` mounts do not
satisfy the exact-namespace contract. If rootless cannot preserve required access,
stop that route and report the failing capability; test one narrow host-launcher
candidate only when allocated/authorized. No silent unisolated fallback or
open-ended permission research.

Compare SDK and stock RPC using the same small local provider/tool fixture and
pinned first-party integration. Exercise send before/after worker acceptance,
lost acknowledgement, worker death and restart around tool intent/result. A
missing supported admission hook ends the automation probe with a documented
blocker; it does not trigger a fork, monkey patch or host-outbox workaround.
Pilot success requires preserving and displaying Unknown without retry; automation
success requires evidence that supported identity/reconciliation resolves the
specified cases, while genuinely uncertain external effects remain held.

| Check batch | Intent and stopping condition |
| --- | --- |
| Quick, per package | Focused Go `go test -mod=readonly` for changed runtime/authority packages; repository Ruby service/host tests; selected worker type/unit checks in its Nix environment. Fake process/manager tests cover stale handles, duplicate start, held Unknown, capability refusal and legacy schema fixtures. Stop on a failed contract before broader runs. |
| Disposable integration, after committed changes and review | Verify exact cgroup/mount IDs across both sessions; distinct scratch, shared fake auth directory/locks/replacement; foreground and detached child cancellation, ambiguous-survivor hold, authorized whole-cgroup teardown; supervisor/portal restart and preserved scratch; lost service acknowledgement and old-registry recovery. Record observations, not inferred containment. |
| Packaged/longer acceptance | Repository `nix flake check --print-build-logs`, focused installed-package fixtures and SDK/RPC selected-path recovery/provider tests. Measure a few loaded workers' PSS/cgroup counters; verify legacy Codex sessions remain writable. Long/uncertain checks use the monitoring skill; no live deployment is implied. |

Retain exact base/head/package identities, commands/results, ownership/generation
observations and remaining Unknown outcomes in the ordinary review/rollout
evidence. Deployment preparation must preserve both backend readers and recovery;
an incompatible older package is not a rollback strategy. A corrected supported
package can disable new Pi creation while retaining Pi recovery and unchanged
Codex operation. No history conversion or backend reassignment is part of it.

Source basis: accepted [F process evidence](process-isolation-evidence.md),
[authentication evidence](authentication-evidence.md) and [design](design.md).
Pins remain D `6587c4c1cedabee95bcc52f4667e7d33e3a82859`,
Pi `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`, and
H `e91c8d21055b7110182fd4c531389947f180e359`. Source paths checked; no runtime
feasibility, authentication or recovery test is claimed by this planning package.
