# H0: host-created Pi session boundary

HOST-DESIGN, architect1, 2026-11-12. Lead allocated design only after M/F
acceptance; this file is the sole edit boundary. Implementer3 owns the future
H0 source package after lead release. Architect0 owns synthesis/technical
acceptance; architect2 owns P2 backend authority. Required guidance, the own D
worktree instructions and accepted main/M/N/O/current design were read/reused.
No privileged probe, application edit, installation or activation ran here.

## Decision and sufficient release

Use **a root-owned systemd system-service template**, with PID1 creating the
mount namespace before executing a fixed bootstrap **as the configured owner**.
The bootstrap then execs the exact retained user-profile application supervisor.
All loaded lead/member workers, local tools and registered Pi services descend
from that supervisor in the same service cgroup and exact mount namespace.
The payload retains the original host user namespace, UID, primary group and
normal supplementary groups. Agents receive no ambient mount-administration
capability. Ordinary authorized setuid/sudo behavior is preserved, not bypassed.

Use a small installed command to manage only this template's instances; no
root daemon, generic privileged argv executor or broad systemd authorization
grant. Root never sources or executes user-profile scripts. This is the
existing trusted-local-operator model, not a hostile-user sandbox. Remote
browser/model input remains untrusted and must pass existing host authority.

**Independent release:** H0 helper/module/bootstrap and fake-manager tests can
be implemented from this brief without a live host installation or Pi model.
P2 authority types/readers remain independent of the concrete launcher. H0 must
not edit native conversation schemas, fabricate Pi acceptance, change Codex,
add migration tooling or switch the default backend. Launch-ready remains
blocked until the separately authorized installed fixture proves tool semantics.

## Installed shape and paths

Proposed module: `services.dev-workspaces.piRuntime.enable`, default false.
It uses the existing configured owner and that owner's actual home/primary
group; no inference that every home is `/home/<name>`. Its `stateRoot` defaults
to `<owner-home>/.local/state/dev-workspaces/pi-runtime-host`, with a normalized
absolute override for installations using another state location. The root is
owner-managed disk storage, separate from the system module and credentials.

Each development-session incarnation gets one persisted random UUID
`instanceId`. Never reuse it for another incarnation or workspace. Fixed paths:

```text
<stateRoot>/instances/<instanceId>/
  launch.json             current immutable launch request, outside scratch
  launch.lock             shared per-instance serialization lock
  receipts/               retained launch/stop evidence; helper-owned host.json
  package-root            retained Nix GC root for the requested app closure
  control.sock            supervisor channel, outside scratch
  tmp/                    bind source for /tmp
  var-tmp/                bind source for /var/tmp
```

P3 prepares owned paths and writes the launch request durably before start.
The installed helper/bootstrap validate ordinary ownership, canonical expected
paths and schema; reject wrong scope, missing input or concurrent replacement.
No arbitrary caller-supplied mount target/source is accepted. Keep request and
receipt sizes bounded. Do not expand these checks into hostile-operator inode
graphs or a new state registry: launch evidence belongs to the application;
systemd owns actual execution, and P2 owns session authorization.

The template `workspace-pi-session@.service` is installed by the **host module**,
not copied into the user manager. Minimum property contract:

| Property | Required behavior |
| --- | --- |
| `User=<owner>`, normal primary group/initgroups | PID1 establishes the owner's normal host group set before the fixed ExecStart; requests cannot override UID/groups. |
| `PrivateUsers=no`, `PrivateMounts=yes` | Keep the original host user namespace; create the exact session mount namespace in the system service. |
| `BindPaths=<stateRoot>/instances/%i/tmp:/tmp` and corresponding `var-tmp:/var/tmp` | Fixed instance-derived disk backing. `PrivateTmp=no`; no stop-time scratch deletion or ephemeral `RuntimeDirectory` ownership of recovery data. |
| `Type=exec`, `Restart=no`, `KillMode=control-group`, `SendSIGKILL=yes`, `TimeoutStopSec=15s`, `Delegate=no` | One supervisor ancestry; no automatic new invocation/replay. Explicit whole-session stop drains this unit. `Type=exec` proves entrypoint exec, not supervisor readiness. |
| Fixed immutable host-bootstrap ExecStart with `%i` only | No `+`/`!` privilege prefixes, root ExecStartPre application hook, shell-evaluated request, or caller-selected root executable. Bootstrap/application executes after UID/group setup. |

Do not add `NoNewPrivileges=yes`, `nosuid` changes or capability restrictions
that break the required host sudo path. Do not grant ambient/effective mount
capabilities to the ordinary worker. Leave other namespaces unchanged; no
`JoinsNamespaceOf`, per-worker units or nested cgroups. Record relevant actual
unit properties at acceptance, since a template declaration alone is not proof.

## Public authority path and frozen helper API

The application path is existing authenticated resolver/admission → P2 trusted
Pi session binding → P3 runtime controller → installed host helper. The helper
is not an HTTP endpoint or model tool. Per-worker/tool **cancel** goes through
the verified supervisor channel; it never becomes a privileged whole-unit kill.
Only an explicitly authorized whole-session **stop** uses the helper stop verb.

Install immutable `workspace-pi-host` through the host module, with a narrow
sudo rule for the configured owner to execute **that exact store executable**
as root noninteractively. Its parser accepts only the fixed verbs below; no
shell, raw unit name, arbitrary systemctl flags, environment or executable argv.
Use configured absolute systemd/tool paths and a controlled environment. The
rule does not grant unrestricted `systemctl`, `systemd-run` or manage-units
polkit access. This host installation is a prerequisite, not permission to
apply the rule now. Existing broad administrator rights remain outside H0.

```text
workspace-pi-host start   --instance UUID --request UUID --digest SHA256
workspace-pi-host inspect --instance UUID --request UUID --digest SHA256
workspace-pi-host stop    --instance UUID --request UUID --digest SHA256
                         --boot-id UUID --invocation-id HEX32
```

All helper operations derive the fixed template name from the validated instance
UUID. New requests load only its fixed `launch.json`; retained requests first
match the helper receipt, as specified below. Bind request/digest to the expected
scope and reject unknown versions. No process discovery/adoption by slug or PID.
`inspect` is read-only and never starts, stops, retries or repairs a unit. Root
can read request JSON as bounded data; no Ruby/shell/user-code evaluation occurs.

The immutable request carries the exact v1 fields below. Its digest is supplied
separately, never embedded in the bytes being hashed. P2 retains its own schema/API
ownership; this launch projection has no native conversation IDs. The bootstrap
uses the fixed, capability-checked supervisor entrypoint and arguments below,
not an arbitrary command array in the request.

Replies are bounded JSON: schema, outcome (`starting`, `running`, `stopped`,
`rejected`, `unknown`), instance/request/digest/runtime generation, host contract
identity, app store root, unit, boot ID, invocation ID, ControlGroup, systemd
job/active/substate and error code. Live observations add main PID/start identity.
Unknown/unavailable fields stay absent; they are not zero/success. Private
identity/path fields go to the controller, not straight into the public portal.

Serialize request publication and every public helper verb, including read-only
`inspect`, using `launch.lock` EX|NB, with one documented lock order after existing
session/package admission. Never invoke Inspect while holding that lock.
Publication releases the lock before invoking the helper, which reacquires it and checks the
exact request/digest. Freeze `launch.json` while a start/stop job, live invocation
or uncertain outcome exists. The bootstrap reads that frozen request; do not
make it wait on a lock held by a caller waiting for readiness. Failed/unknown
start never permits replacing the request. Same-ID retries inspect the same
unit/invocation; changed payload or another generation refuses. A terminal
request cannot silently be replayed as a fresh launch.

The first supervisor handshake on the private channel echoes scope, request,
generation, exact app root, host contract, boot/invocation, PID/start identity,
cgroup and mount/user namespace observations. P3 compares it with independent
systemd/process observations before marking ready or loading workers. This is
execution identity, not a new prompt receipt namespace. Stale/wrong-generation
connections cannot authorize cancel or service start.

`stop` rechecks boot/invocation and the current request under the same lock
immediately before stopping the fixed unit. Mismatch refuses; never stop a
replacement invocation. After native stop, verify terminal job/unit state and
the owned cgroup empty/absent with preserved ownership evidence. A timeout,
observation failure or ambiguous survivor returns Unknown and keeps recovery
held. Missing unit metadata alone is not stop proof. Worker cancellation keeps
the M brief's targeted-handle and ambiguous-survivor rules; no whole-unit kill
to make an individual cancel appear successful.

### Frozen v1 interop details

Architect2 confirmed the scope projection; P3's owner confirmed no collision
with an existing launcher/manifest contract. These are H0 launch contracts,
not changes to P2 storage. `launch.json` is a UTF-8 JSON object, at most 64 KiB,
with exactly the following fields (snake_case); reject duplicate/unknown keys,
nulls, trailing JSON and wrong scalar types:

```text
schema: 1
host_launcher_contract: 1
scope: {
  workspace: canonical absolute workspace path
  slug: validated development-session slug
  session_incarnation: 64 lowercase hex characters
  backend: "pi"
  backend_contract: 1
  binding_revision: positive uint64
}
instance_id: lowercase UUID
request_id: lowercase UUID
generation: 64 lowercase hex characters
app_store_path: canonical absolute /nix/store package root
profile_path: normalized absolute configured user-profile path
profile_generation: nonempty bounded string identifying the admitted profile generation
replaces_request_id: lowercase UUID (omitted on first launch; required on successor)
```

String limits are 4096 UTF-8 bytes, with no NUL/control characters; UUID fields
use the same strict lowercase UUID form as the CLI. `generation` is P3/P2's
execution generation, not another UUID or a new submission identity. P3 derives
profile identity under the existing transition lock; H0 records/compares it but
does not resolve a moving profile to choose an executable. P3 validates `scope`
against durable P2 state before publication. `binding_revision` is the authorized
launch snapshot: later valid member updates do not rewrite this request or mint
a new receipt; P3 checks current binding independently for dispatch.

**Byte/digest rule:** `request_sha256` is lowercase SHA-256 of the complete exact
frozen `launch.json` byte sequence, including whitespace and any final newline.
There is **no digest field in launch.json and no canonical reserialization**.
The publisher writes once, fsyncs and hashes those bytes; helper, bootstrap and
supervisor hash the bytes they actually read. CLI `--digest`, replies and
handshake carry that hash. Semantically equivalent reformatting changes it and
refuses under the original request ID. Add one checked-in byte fixture with a
known hash used by each language implementation. Do not hash a parsed object.

The application capability lives at
`<app_store_path>/share/dev-workspace/pi-runtime.json`, separate from the legacy
strict `package.json`. It is immutable, bounded at 4 KiB, and has exactly:

```json
{"schema":1,"host_launcher_contract":1,"launch_request_schema":1,"handshake_schema":1,"supervisor_entrypoint":"bin/workspace-portal","supervisor_command":["pi-runtime","supervise"]}
```

All values above are fixed v1 constants, not configurable executable/argv
fields. Unknown keys or values refuse. P7 owns production emission/wiring;
H0 tests use a fake immutable package. P0 `pi-runtime/upstream.json` is dependency
input only and must not be treated as this capability manifest. The fixed host
bootstrap, already running as the configured owner, validates that manifest and
execs this argv directly, with no shell:

```text
<app_store_path>/bin/workspace-portal pi-runtime supervise
  --launch-request <stateRoot>/instances/<instance_id>/launch.json
  --instance <instance_id> --request <request_id> --digest <computed request_sha256>
```

The supervisor re-reads/verifies the same bytes and reports the computed digest
in its v1 handshake before accepting work. P3 implements this entrypoint; H0
owns validation/exec fixtures only. The app package contains the selected worker
and dependencies; H0 does not choose SDK/RPC or mutable resource defaults.

**Helper receipt and rearm:** accept implementer3's proposed bounded execution
receipt. The helper alone writes `receipts/host.json` (schema 1, root-owned
mode 0600; maximum 1 MiB) using atomic replacement and file/directory fsync under
`launch.lock`. It contains `schema`, `instance_id`, `current_request_id` and
`requests`, a map keyed by request UUID. Each entry preserves the digest, scope,
generation, app/profile identities, phase and available native identity/proof.
This single record makes head/receipt publication atomic; it is execution
evidence, not a second session authority or transcript store. Capacity exhaustion
refuses safely; H0 never silently prunes or deletes old receipts.

Phases are `starting`, `running`, `stopping`, `terminal`, `unknown`. Persist the
new `starting` entry/current pointer **before** the native start call. Once an
entry exists, same-ID start reconciles/returns it and never calls start again.
A lost reply or interrupted start whose effects cannot be proved remains
Unknown, including the conservative crash window before the manager call.
Actual public outcomes are `starting`, `running`, `stopped`, `rejected`, `unknown`.
The implemented helper has no `not_started` outcome; the earlier proposed
pre-call-rejection alternative is superseded. A rejected request, absent unit or
nonzero systemctl exit does not supply terminal drain proof for succession.

Successor admission requires a stopped/terminal receipt with complete `exited`
or `stopped` drain proof binding boot/invocation/cgroup, recorded no job/terminal
unit state and empty/absent owned cgroup. Preserve timestamps and error
codes as evidence; helper inspection remains read-only, with reconciliation
writes confined to explicit start/stop retries. Terminal same-ID replay returns
its prior terminal receipt, **never relaunches**.

Lookup order matters: under the lock, check a retained request ID and its digest
in `host.json` before requiring the current `launch.json` to match it. A prior
terminal request must remain replayable after a successor has replaced that
file; return its saved result without touching the successor. A digest mismatch
always refuses. Only a genuinely new request reads/adopts the current descriptor.

A successor requires a new explicit request UUID **and** generation, matching
stable instance/workspace/slug/session incarnation/backend contract, and
`replaces_request_id` equal to the helper's current terminal request. Under the
lock, recheck positive old drain and absence of native Unknown/in-flight work
before accepting the successor. P3 also rechecks lifecycle/package authority
and unresolved tool effects; native drain never clears those holds. Preserve
old entries and the same scratch roots. A changed digest under any retained ID,
skipped predecessor, still-live old invocation or uncertain observation refuses.
No public reset/rearm/delete verb or receipt editing workaround is introduced.

The [accepted P3 successor contract](design.md) distinguishes saved receipt
evidence from fresh native observation. Under ordinary P2 admission/P3 runtime
serialization, P3 calls H0 Inspect **before** taking launch.lock. Terminal Inspect
returns saved evidence; it does not certify a fresh systemd unit/no-job state.
Require current boot equality and fresh positive owned cgroup-empty/absent proof.
Under launch.lock, revalidate the captured immutable terminal tuple, exact old
descriptor and current boot/cgroup proof, without another helper call or private
host.json read. Publish exact prepared successor bytes, then release launch.lock
before H0 Start. Start performs its fresh native unit/job/invocation/drain gate
under its own lock. Refusal or uncertainty after publication holds the exact
prepared pointer/request/generation; no descriptor rollback, pointer restoration
or replacement request. This adds no H0 API, outcome or source allocation.

## Profile, storage and recovery compatibility

The host module installs only the template, helper, unprivileged bootstrap and
policy. The user-profile application still deploys separately. Under existing
transition locks, new start captures and validates the selected immutable app
store path/manifest and launcher capability; the bootstrap executes that path,
never whatever a moving profile symlink later names. Inspect/stop and recovery
must support retained generations. Preserve the app closure/GC root and launch
evidence while work is live or unknown; do not add garbage collection to H0.
An incompatible host/app contract refuses before launch. A package switch cannot
relabel existing workers or erase recovery obligations; P2/P3 retain their
existing admission and forward-recovery rules.

Scratch backing remains stable for the session incarnation across invocations.
Exit removes the mount view, not backing data; no helper operation deletes it.
Canonical native Pi credentials remain visible through the **same containing
directory** outside scratch, including locks and replaced files. Because H0
does not mask home, no credential copy or file-only bind is needed. Per-member
history/settings/resource paths stay under P3's private member roots; H0 neither
chooses models nor writes credentials. Nix clients inherit the boundary while
daemon builds remain external accounting. Report cgroup usage and directory
usage honestly; no quota engine, new filesystem or memory budget is introduced.

## Files, dependencies and checks

**H0 source owner: implementer3 after lead release**, in this session's D
worktree, investigated base `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.

| Owned source/deliverable | Boundary and acceptance |
| --- | --- |
| New `nix/pi-runtime-host.nix`; small import in `nix/host-module.nix` | Isolated opt-in host module/template/policy. Preserve existing nginx/auth/TLS reconciliation. Disabled option produces no Pi host unit/policy. |
| New `nix/pi-runtime-host-package.nix`, `libexec/workspace-pi-host`, `libexec/workspace-pi-session-entry` | Immutable separately packaged host tools; fixed-verb parser/systemd adapter and unprivileged manifest bootstrap. No changes to `workspace-host` or root execution of user application code. |
| New `test/pi_runtime_host_test.rb` and isolated fixture support; new `nix/tests/pi-runtime-host.nix` | Fake-manager/process/package fixtures first; disposable installed test definition only, no live host fixture. Follow repository Nix/Ruby conventions. |
| New `docs/pi-runtime-host.md`; pointers in existing guides handed to their owners | Installed prerequisite, private API, generation/recovery/Unknown rules and explicit scope limits. No claim installation occurred. |

P3/implementer1 owns supervisor, `workspace-host` calls, application launch
records/GC-root handling and worker/service cancellation. P2/architect2 and its
implementer own authority/version fences. The packaging owner wires top-level
flake exports/checks and application manifests; H0 supplies importable modules
without taking that shared edit window. P2/central CLI/web files remain untouched.
Conditional later site enablement is limited to H aitherdev `config.nix` and
`dev-workspace-site.nix` plus the normal selected-input change, only if needed
and allocated. No configuration checkout edit, pin update or activation now.

Quick fixtures must cover invalid IDs/verbs/paths, disabled/unsupported contract,
wrong scope or request digest, duplicate starts/lost replies, frozen descriptor
and concurrent generation change, stale invocation stop, manager unavailability,
and empty-versus-unknown cgroup observations. Assert exact systemd argv/property
construction and that application exec occurs in the unprivileged entrypoint.
Use fake app manifests/credentials and no user/system manager mutation. Run the
focused Ruby test in D's Nix environment and module evaluation/unit generation
checks; actual check wiring follows the packaging owner's window.

After committed implementation and required review, a fresh watcher runs the
authorized disposable installed fixture: two simultaneous units, lead/member/
tool/service descendants; exact distinct mount/cgroup boundaries; host-equal
user-namespace identity, UID/groups and sudo-wrapper behavior up to the
noninteractive authentication boundary; zero ordinary-worker ambient mount
capability; shared fake auth directory/lock/replacement; scratch preserved and
rebound after explicit fixture stop/restart; stale stop unable to affect a new
invocation; independent post-stop empty-cgroup proof. No passwords, privileged
payload, real login/model or production workspace is needed. Record limitations
separately if the VM fixture cannot prove a required host-specific tool property.

**Stop/go:** generic implementation can proceed with fake interfaces now.
Installed Launch-ready requires the concrete permission/containment proofs;
unsupported host policy or profile fencing stops that dependent lane, not P2 or
neutral UI work. This brief authorizes no service action, machine reservation,
host installation, user-profile activation, integration or session lifecycle.

## Evidence

The decisive prior fixture is implementer1's D commit
`ab9ce9234fe2b1f80367b7bb1836a81925b2a034`,
`test/pi_runtime/containment.mjs`, command from that D checkout:
`nix develop --command node test/pi_runtime/containment.mjs . .`.
Its [receipt](p0-containment.json) and [summary](p0-evidence.md) report both
simultaneous rootless units successful for containment, scratch and Nix/repo
access, but supplementary groups overflow and sudo rejects root/setuid ownership
before authentication. Restart rebind and post-collection empty-cgroup proof
were not claimed. This is attributed peer evidence, not a rerun by architect1.
The selected H0 direction addresses that failure; it is not itself verified.

See [M](pi-runtime-plan.md), [main implementation plan](implementation-plan.md),
[current design](design.md), [F source evidence](process-isolation-evidence.md)
and [P2 boundary rationale](backend-evolution-boundaries.md). Lead release and
architect0 acceptance follow this sufficient brief; no optional host inventory
or further rootless variant is required first.
