# Exact-session development cluster stop/release preparation

Prepared read-only by implementer6 on 2026-11-03. This is preparation, not an
executed shutdown. The user directed WebUI merge first, then stop and release
this session's existing development cluster. The parent owns execution after
successful WebUI/main integration and terminal verification operations. The
session remains open; no archival, session stop, cleanup or production action
is included.

## Verified current effects

`dev-session current`, both environment bindings and live roster61 match
`2026-11-01-typescript-client-migration` in
`/home/aither/workspace/ai/vpsfree.cz`. Implementer6 retains
`gpt-6.1-sol`/xhigh/workspace_write; no settings changed.

At 2026-11-03T21:56:37Z, the public provider status exited0: schema2,
found=true, running, ready=true, single/bridge, actions `[stop, release]`.
No maintenance metadata is present. The exact applied envelope is version1,
workspace/slug match, pending=null, SHA256
`91842caad08e21eb6aabe31a889c9c8e75f4dbb3264b7fc12fb28c80d1ba180b`.
This establishes available provider controls and no pending applied operation;
it is not a global process or CI inventory.

Owned state is
`.dev-clusters/vpsadmin/clusters/2026-11-01-typescript-client-migration/`, a
non-symlink directory owned by uid1000. The recorded socket is
`/tmp/vpsfree-devcluster-2390ddf185e2`, present and owned by uid1000.
Runner3399167 has start ticks31781317, uid1000, PGID/SID3399167, executable
`ruby`, CWD the workspace root, boot ID
`8f3d3e6c-c527-42bd-aad9-bd1ef3fd7c3d`. Its exact `--sock-dir`, `--state-dir`,
`--pid-file` and `--ready-file` pairs match this cluster. The identity was
revalidated after the bounded inspection.

Only that runner's recursive descendants were inspected:38 descendants, with
these four direct QEMU children (PID/start ticks):

- services3405321/31787756;
- dns-primary3408969/31790785;
- dns-secondary3410061/31791360;
- node13410145/31791462.

Existing images are services-root12884901888, dns-primary-root2582642688,
dns-secondary-root2582642688 and node1-tank21474836480 bytes. Their contents
were not read. Public readiness and live owned QEMU processes are the present
observations; no guest SSH/API or fresh in-guest activation check was performed.

The selected result remains
`/nix/store/xl48by018w2035nwqv5q7sc4xkr7b66j-os-test-vpsadmin-devcluster-2026-11-01-typescript-client-migration.json`.
Its WebUI source label is clean worktree4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e,
not the later follow-up candidate. The prior accepted activation/source proof
remains in [preview acceptance](devcluster-preview-acceptance.md) and its JSON:
API610a96, OS staging5918f94e, active frontend
`/nix/store/p5spjawkxdki3rjzznvrxp6fh9vfry33-vpsadmin-webui-frontend-1.0.0`
and BFF
`/nix/store/lwwafhip9lz8jv4b9r6xhm164svchacz-vpsadmin-webui-bff-0.1.0`.
No preview update is necessary to shut it down. Original source, package,
unknown-metadata and toolchain limits remain historical evidence after release.

## Parent execution after merge

CWD for the standard CLI is `/home/aither/workspace/ai/vpsfree.cz`, with the
verified exact DEV_SESSION_SLUG/DEV_SESSION_WORKSPACE binding. Recheck current
identity and public filtered status before execution; the recorded process
identities are a snapshot, not authority to signal a later reused PID.

Normal public stop argv:

```sh
vpsadmin-devcluster stop 2026-11-01-typescript-client-migration
```

Stop retains configuration, credentials, persistent disks and applied/source
roots. It removes readiness/PID through runner shutdown and removes the transient
result-config root after runner exit. The bridge remains the host's shared br0;
only this cluster's guest attachments/processes are stopped. Do not delete or
reconfigure br0.

There is **no separate public CLI release verb** or `dev-session cluster release`
command in this installed package. The standard public Release is the exact
session portal cluster card, or its documented HTTP operation:

```http
POST https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/api/sessions/2026-11-01-typescript-client-migration/release-cluster
Origin: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz
Content-Type: application/json

{"kind":"vpsadmin"}
```

A parent command equivalent to that public operation (prepared, NOT executed):

```sh
curl --fail-with-body --silent --show-error --max-time 190 \
  --header 'Origin: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz' \
  --header 'Content-Type: application/json' \
  --data-binary '{"kind":"vpsadmin"}' \
  'https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/api/sessions/2026-11-01-typescript-client-migration/release-cluster'
```

The normal portal Release internally dispatches the registered provider's
`reset <slug>` implementation: it stops/reaps the exact owned runner and socket
processes, then deletes this cluster's socket directory and cluster directory,
including disks, per-cluster config/credentials and retained roots. This is a
material documented effect of Release, not a nondestructive reservation release.
Do not invoke reset or a private lifecycle helper directly. The user's explicit
stop/release direction is the authority for the public Release, after merge.
A single Release includes stop; a separate successful Stop followed by Release
makes the requested two milestones explicit. Neither command authorizes
workspace-wide certificates/SSH deletion, state of another cluster/session,
store GC, worktree removal or any session lifecycle action.

No separate coordination-machine release is implied by this provider operation.
If the parent has a separately recorded held claim, only its exact claim/status
and original recovery procedure can determine its release; do not invent a
claim from this virtual cluster or use `ReleaseAll`.

## Completion and refusal boundaries

The normal shutdown has concurrent guest shutdown/reaping budgets120+10+20=150
seconds. The public portal Stop/Release deadline is180 seconds. Allow roughly
seconds to three minutes per operation, without treating elapsed time as proof
of failure. Parent fresh Luna may observe the independent native/public result;
no watcher or command was started here.

After Stop expect native exit0 and filtered found/stopped, ready=false, retained
disks/config/applied selection, and disappearance of the positively bound runner
and four guests. A stale result marker alone is insufficient. After public
Release expect HTTP200 `{"ok":true}`, filtered found=false and absence of this
exact cluster directory and recorded socket, plus no surviving positively bound
runner/guests. Do not call `urls` or `config` to verify absence: those can create
state. Status JSON must be captured in memory and projected to safe fields,
never dumped; it includes development account secrets.

Busy provider exit75, concurrent portal mutation, unfinished lifecycle journal,
package-generation mismatch, pending maintenance, unsafe state/socket identity,
or any uncertain native effect is a refusal/reconciliation boundary. Never
force, hand-edit state, signal processes, use another generation or retry a
mutation blindly. Browser/client disconnection does not cancel admitted work;
refresh exact-session status first. Pending maintenance permits only Stop and
blocks Release. A failed/lost Release may have partial effects: retain original
response/native evidence and inspect the same exact paths/identities before any
standard retry. Historical isolated API2 uncertainty remains unrelated.

## Authority and preparation limits

Read workspace lifecycle/coordination and the selected package's coordination
and recovery guides. Provider README read in full:
`/nix/store/9019d7wm0c40q59vrnlf1clwp7q00xrd-vpsfree-dev-workspace-tools-0.1.0/share/vpsfree-dev-workspace/dev-clusters/vpsadmin/README.md`.
Public CLI help and directly implicated provider `bin/devcluster`/shared
`lib/runtime.sh`/`lib/shutdown.json` confirm stop and ownership behavior.
Selected runtime package:
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
Its installed-source guide is
`/nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source/docs/workspace-portal.md`,
complete Development cluster controls and Cluster provider status and shutdown
contract sections. Direct route/client/cluster implementation confirms the
public POST, Origin requirement, fresh action/status validation, nonblocking
provider lock and180-second completion boundary.

Preparation deviation: the first standard status JSON was accidentally printed
unfiltered and includes seeded development credential fields. Those values are
excluded from this record and subsequent reports; later status was projected in
memory. No rotation or other unrequested credential mutation was attempted.
An unsupported `dev-session cluster --help` discovery returned unknown-command
without mutation. No actual Stop/Release/reset/urls/config, signals, source/Git
mutation, guest SSH/network API/build/install/download or cleanup ran.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
