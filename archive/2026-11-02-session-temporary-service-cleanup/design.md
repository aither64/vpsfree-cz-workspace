# Session temporary service cleanup

**IMPLEMENTATION AUTHORIZED / NOT YET VERIFIED — 2026-11-02.** The user directed
implementation and allowed aitherdev deployment through vpsfree-cz-configuration.
Default-branch integration and session lifecycle actions remain unauthorized.
The execution contract below supersedes provisional API/storage choices in the
earlier proposal. Architect work remains design-only; implementers own code.
Scope amended by the user: "let's not handle existing unregisteredservices."

Additional implementation/deployment authorization, 2026-11-03: the user accepted
[machine reservations without a packaged catalog](machine-identity-proposal.md).
The [machine-identity execution contract](#machine-identity-execution-contract)
below governs its separate implementation packages. Default-branch integration
remains unauthorized. No target identity probes or confctl changes are included.

## Frozen execution contract (implementation kickoff)

Reconciled against feature base `c2182254d29c4175c3e9fe4267e5a92dd1da6b79` in
`worktrees/2026-11-02-session-temporary-service-cleanup/dev-workspace`. The relevant
archive/delete order and reader boundaries match the inspected installed source:
fresh archive still prunes at `libexec/dev-session:2134` before journal creation;
delete already publishes its removal journal before worktree removal. No scope
expansion is needed. Use `nix/workspace-portal.nix` for packaging (there is no
`nix/package.nix`). This section freezes A/B interfaces; implementation-private
details may vary without changing the persisted/public contracts or invariants.

### State and ownership (A owns the writer and shared Ruby validator)

Implement `libexec/workspace-session-services.rb`, module `WorkspaceSessionServices`.
Use the existing workspace ID formula: basename + `-` + first 16 SHA256 hex digits
of the canonical workspace root. All JSON below is strict, atomically replaced,
fsynced, private mode 0600, with owner-only directories and ordinary symlink/path
validation. UUIDs are lowercase canonical UUID strings; lifecycle IDs remain the
existing 64 lowercase hex characters. Bound registry/projection to 1 MiB and 256
resource records; refuse new launches before those bounds, never truncate ownership.

| File | Frozen schema-1 fields |
| --- | --- |
| `worktrees/.locks/<slug>.services-registration.json` | `schema`, `workspace`, `slug`, `registry_id` (UUID), `retained_thread_id` (nullable), `tracking_identity` (`dev`, `ino`), `state` (`initializing` or `ready`), `created_at`. First-registration marker only; no coverage/audit semantics. |
| `<state-root>/session-services/<workspace-id>/<slug>.json` | `schema`, same ownership fields, `revision` (monotonic integer), `activity_token` (UUID), `resources` (array). Each resource: `id`, `label`, `unit`, `description`, `argv`, `cwd`, `request_sha256`, `phase`, `created_at`, `updated_at`, `boot_id`, `manager_uid`, `manager_control_group`, `expected_control_group`, `invocation_id` (nullable until observed), `control_group` (nullable until observed), `stopped_at` (nullable), `retired_at` (nullable), `error` (nullable `{code,message}`). No persisted arbitrary environment dump. |
| `worktrees/.locks/<slug>.services-cleanup.json` | `schema`, `workspace`, `slug`, `registry_id`, `retained_thread_id`, `tracking_identity`, `operation` (`archive` or `delete`), `operation_id`, `mode` (archive policy, otherwise null), `force` (delete boolean, otherwise null), `automatic` (boolean), `resource_ids` (sorted frozen UUIDs), `phase` (`services_pending` or `services_stopped`), `created_at`, `updated_at`. Maximum 64 KiB. This is a subordinate lifecycle prelude, not a new public lifecycle command. |

Resource phases: `starting`, `running`, `stopping`, `retired`. Observation failure
or failed application exit does not retire a record; record a safe error/live state
in the projection. `retired` requires verified empty cgroup, settled jobs and
removed transient unit. Resource IDs and generated unit names are never reused.
This makes a separate revival epoch unnecessary: retain the registry identity and
old retired records, and allocate new UUIDs for new launches after ordinary revival.
The existing root plus tracking-directory identity binds the session; archive/revive
rename preserves that directory. A different root/incarnation must not inherit
retained entries, including retired ones. Successful delete transfers marker/registry to its
existing private removal recovery before clearing active ownership; retry uses the
same journal. Do not introduce a new history collector or quota eviction policy.

First launch writes an `initializing` marker, then registry/launch intent, then
durably changes the marker to `ready`, then contacts systemd. Both files absent
means an untouched session. Either present establishes expected registration;
a missing counterpart, identity mismatch or corrupt state refuses destructive
cleanup. A failed first initialization may complete the same marker's empty
registry only while it still says `initializing`, which forbids a systemd attempt.
A `ready` marker never resets or repairs a lost registry as empty. Reuse any
existing valid initialized registry instead of replacing it. No unit scan/adoption repairs loss.
All service-only scratch files remain inside ordinary session-owned file boundaries.

Generate `workspace-session-<resource UUID>.service` and a nonsecret Description
binding `registry_id` + resource ID. Enforce Type=exec, Restart=no,
RemainAfterExit=yes, Slice=app.slice, KillMode=control-group, SendSIGKILL=yes,
TimeoutStopSec=15s.
Do not auto-collect before cleanup. Existing stop design remains: bounded native
TERM→KILL, job/unit identity and descendant-cgroup proof, then exact unit retirement.
A missing unit with unobserved cgroup after an uncertain launch is not enough proof;
positively reconcile native ownership/absence or leave registered state blocked.
Bound systemd calls/observation to at most 20 seconds per resource and report partial
progress. No process/port matching, custom stop hooks, external routing or discovery.

Fast-exit clarification: before contacting systemd to launch, obtain the user
manager's `ControlGroup` with argument-free `systemctl --user show`, and durably
record `manager_control_group` plus `expected_control_group`: normalized manager
root + `/app.slice/` + the generated unit name. Support the local unified cgroup-v2
hierarchy; unavailable or unsupported placement refuses launch. Every nonempty
observed unit `ControlGroup` must equal that expected path. Keep observed
`control_group` nullable; never rewrite the expected path from an unexpected result.
This allows recursive empty/absent proof for an accepted fast-exiting service
whose cgroup disappeared before its first observation. It does not prove that an
uncertain start request has settled: pending jobs, late launch producers, missing
manager or unresolved request outcome still block retirement. Retain boot/UID,
unit Description/InvocationID and native job proof. No Freeze or wrapper protocol.
Source: systemd **v260.5**, `src/core/cgroup.c:unit_default_cgroup_path`,
`src/basic/cgroup-util.c:cg_escape/cg_slice_to_path`, and
`src/core/dbus-manager.c` expose this placement and Manager.ControlGroup; installed
`systemctl(1)` and `org.freedesktop.systemd1(5)` confirm the read interface. The
fixed unit prefix needs no cgroup escaping. These are source proofs, not live tests.

Keep exact recorded InvocationID equality for every loaded-unit observation,
including inactive/failed. Inspected systemd v260.5 `service.c:service_set_state`,
`service_enter_dead` and `service_reset_failed` do not clear it; `service_start`
allocates the next ID through `unit_acquire_invocation_id`, and `unit-serialize.c`
preserves/restores it. `dbus-unit.c` exposes that field directly. There is no
source-supported terminal empty/zero exception. Unit unload/not-found remains
the separate settled-job/expected-cgroup absence proof, never an ID rewrite.
Check retained-ID terminal success, loaded empty/zero/changed-ID refusal and
post-stop not-found in focused/native fixtures. `SERVICE_EXITED` explicitly
prunes its cgroup (`service.c:1374`), corroborating the fast-exit path above.

### Native Job formatting clarification (260.2 fixture failure)

At runtime `7302f4dc961ded7c768733e25ec39e3c603e093b`, `snapshot` invokes
`systemctl --user show UNIT --property=... --property=Job ...`, retaining property
names. The VM log records systemd **260.2** and the first registered launch's
`service manager job state unavailable`; it does **not** capture the offending raw
`show` value (`tracking/runtime-ci-7302f4dc/failed-archive-job.log:3644,5586–5593`).
Root nixpkgs `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4` selects v260.2; its systemd
patches do not alter the following formatter/getter paths. Independently checked
official v260.2 commit `f1d0952a125b96b7ab2f1ff29a87448ade8ac29b` and the retained
files under `tracking/runtime-ci-7302f4dc/systemd-source/`:

- `src/core/dbus-unit.c:254–276,958`: `Job` is `(uo)`; no job returns `(0,"/")`.
- `src/systemctl/systemctl-show.c:1228–1240`: positive ID prints decimal;
  zero passes NULL to the value printer.
- `src/systemctl/systemctl.c:581–603`: explicit `--property` enables SHOW_EMPTY.
  `src/shared/bus-print-properties.c:27–40` therefore prints **`Job=`** for zero.
  The actual command needs no additional `--all`; it must not use `--value` here.
- `systemctl-show.c:2368–2374` reports an absent requested property only at debug
  level, without inventing an output line. Absence is not a zero-job observation.

A's minimal fix: after key/value decoding, normalize exactly
`values.key?('Job') && values['Job'] == ''` to internal `'0'`; preserve existing
explicit `'0'` acceptance. Positive canonical decimal (`\A[1-9][0-9]*\z`) is a
known pending job, never settled. Missing/null/bare `Job` without `=`/whitespace/
malformed text remain unknown and fail safely; no `to_s`, stripping or nil fallback.
No API/schema/dependency or command-flag change. Keep strict loaded InvocationID
equality, uncertain/unloaded launch refusal, native-job/expected-cgroup absence
proof and all original recovery/receipt behavior unchanged. This fixes a proven
source-contract mismatch without claiming the failed VM's unrecorded raw value.

The getter, Job formatter, value printer and explicit-property flag block are
identical in v260.5 commit `84ff4f0dff41c26472cd48c4c4955c2d77f5ac08`; the earlier
260.5 identity/cgroup evidence is not a claim that the VM runs that version.
Focused fixtures use raw `Job=` by default and cover explicit zero compatibility,
omitted/null/bare/malformed refusal and positive-job blocking, including not-found
and uncertain launch. A owns parser/tests/commit; the existing native archive
fixture supplies subsequent 260.2 execution proof. No live probe was performed.

### First-root admission correction (R2, final-review narrow remedy)

Rootless ordinary sessions may register services, but cannot later create their
first Codex root while registration remains. Use one strict read-only admission
helper: no registration returns; validated marker with `retained_thread_id:null`
refuses; the same nonnull root returns; corrupt/missing/changed ownership raises.
Do not distinguish live, retired, empty or initializing records, rewrite ownership,
or add a transition schema. A owns this helper and the following Ruby call sites.

At `85760a7a`, insert in `Runner#start`'s first creation→slug EX lock block after
`guard_portal_preparation_reservation!`, before `select_sensitivity!`, receipt,
revive-runtime or creation-journal preparation; apply only when `run_codex` is true.
This covers CLI/preserved tracking, portal/plan/direct-team starts, creating-root
recovery and the legacy revival subordinate start. Earlier direct-team recovery
helpers only read journals. `create_portal_thread` at 1162/1195 is too late.
Fork uses a separate destination: call the same helper in both destination lock
blocks (initial admission before sensitivity/receipt at 1471, and recheck before
fork-journal/provider/native effects at 1555). Never gate its unchanged source root.
Portal creation dispatches these Ruby commands; no Go registry reader is needed.
Resume requires a retained root, attach retains it, and ordinary rootless revival
skips `start` (`revive_with_access`), so those paths retain existing behavior.

Document the supported order: create a conversation before registering services
if that session needs one. Existing rootless registration remains useful for CLI
services and authorized stop/archive/delete. Stop/retirement/archive/revival keep
metadata and cannot make first-root start admissible; use a separate conversation
session when needed. Do not advise deleting records or a session to bypass refusal.
Fixtures cover live and retired refusal with tracking/registration bytes unchanged
and no sensitivity, receipt, creation/start/fork/provider or native mutation;
continued authorized cleanup; absent registration and same-root admission; fork
destination/source distinction; and rootless archive/revival remaining rootless.

### CLI, locks and the Ruby seam

Freeze public verbs `service run`, `service list`, `service stop`, with the proposal's
session arguments. `run` also accepts optional `--id UUID` for exact-request replay;
without it allocate an ID before intent. Reusing an ID with a different label/cwd/
argv digest refuses; an existing attempted launch is reconciled/reported, never
blindly relaunched. `list --json` is the portal interface. `run`/`stop --json` may
return that same projection after the action. No inventory/adoption/restart API.

Use transition SH with post-acquisition generation validation, then existing
creation and session EX locks for run/stop/lifecycle writes. A's Runner integration
owns lock acquisition; the service Store does not nest those locks. `list` uses
existing session observation SH nonblocking admission and a bounded read. Exit 75
means busy (no JSON); malformed ownership/state returns nonzero; transport/native
status failure with intact registry returns known membership and unknown live state.
Archive/delete may call the Store while already owning their lifecycle locks.
Reads never initialize records or write reconciliation/progress/activity metadata.

Shared Ruby seams (A implements; B calls the pure validator from workspace-host):

- `WorkspaceSessionServices.paths(workspace:, state_root:, slug:)` returns marker,
  registry and prelude paths; path computation never creates them.
- `WorkspaceSessionServices.requirements(workspace:, state_root:)` returns
  `{required: Boolean, pending: Array}` after strict file/identity validation.
  `required` means any retained registration in the marker/registry namespaces,
  including initializing, empty and fully retired records; unknown state raises.
  `pending` contains validated prelude slug/operation/ID summaries.
  Marker/registry presence must be checked in both directions, not one glob only.
- `WorkspaceSessionServices::Store.new(workspace:, state_root:, slug:, runner:)`
  uses the existing command-runner interface. Public collaborators:
  `run!(id:, label:, cwd:, argv:)`, `stop!(id:)`, `public_status`,
  `prepare_cleanup!(operation:, operation_id:, mode:, force:, automatic:)`,
  `cleanup!`, `verify_clean!`, `handoff_cleanup!(journal:)`.
  Runner supplies verified session identity; Store never invents it from slug/CWD.
  Internal method decomposition is A's choice; keep paths/requirements/public JSON stable.

### Public JSON (A emits; B consumes without reading private registry)

`list --json` returns exactly this schema-1 envelope (optional values use null):

```json
{"schema":1,"workspace":"/canonical/root","slug":"SLUG","registryId":null,
 "registered":false,"count":0,"countKnown":true,"observedAt":"RFC3339 UTC",
 "services":[],"history":[],"cleanup":null,"notice":null}
```

Each `services`/`history` row has `id`, `label`, `phase`, `state`, `observedAt`,
`retiredAt`, `error`. `state` is `starting|running|exited|failed|stopping|stopped|unknown`;
it is an observation, not readiness or permission to prune. `error`/`notice` are
null or `{code,message}` with bounded, explicitly safe messages (not raw stderr).
`cleanup` is null or `{operation,operationId,phase}` from the verified prelude or
matching active lifecycle. `services` contains nonretired entries; `history`
contains retired entries and does not contribute to `count`. An intact registry
means `countKnown:true` even if unit observations fail. No marker/registry gives
the empty envelope without probing systemd. Known-state corruption is an error,
not empty JSON. Busy/read failure makes B preserve a visibly stale snapshot or
show unknown, never synthesize zero. Do not expose argv/cwd/unit/cgroup/environment.
B wraps the call in existing exact-session/profile/incarnation checks before and
after reading, like coordination; uses the same accepted snapshot for page/count.
Archived sessions return retained history without probing retired units.

### Lifecycle handoff and package compatibility (A/B joint contract)

For fresh archive, after normal authorization/preflight and the final automatic
eligibility check, allocate/reuse the accepted operation ID, publish/fence the
prelude, stop/verify all entries, and mark `services_stopped` **before pruning**.
Then create the unchanged ordinary archive journal/sidecar with that exact ID.
Delete uses its already published removal journal ID and guards first file removal.
After validating matching ordinary journal identity, remove the prelude; that
journal retains admission ownership. A crash between journal publication and
prelude removal permits both only when operation/ID/mode agree and deletion's
force setting follows its existing authorized false→true retry rule. A prelude
alone resumes via the original archive/delete command, retaining saved policy.
No service state means the old path without a prelude. Validate known registrations
and require verified retired state before every remaining destructive phase on retry.
Old journals keep their exact schemas, phases and sealed file/Git proofs; add no
fields to them and do not rerun an older tracking prune. They receive only the
registered-resource guard before any remaining deletion. No unregistered-resource gate.

A wires prelude ownership into Runner conflicts/admission, archive-check and
automatic-worker own-operation recovery. B wires it into Go PendingLifecycle/
Progress/receipt identity and host unfinished-operation scanning. Do not append a
second mapping for archive/delete to `lifecycleJournals` (the current contract
requires unique command mappings). Treat this suffix explicitly, like the existing
archive-cleanup sidecar; pending+ordinary same-ID is one operation. Prelude progress
evidence excludes `phase`/`updated_at` and deletion's authorized `force` upgrade;
other immutable identity must remain stable.
Creation, revival, cluster/provider admission and package paths must honor its
pending fence; ordinary status reads may show it, never finish it. Publish the
existing coordination lifecycle fence atomically with prelude intent using the
existing bind callback; preserve worker ownership before stopping on automatic runs.

B adds runtime keys `sessionServicesStateSchema: 1` and
`sessionServicesLifecyclePolicy: 1`. Host selection **and candidate activation**
call A's strict requirements validator: pending preludes block package transition;
any retained registration requires both matching keys, including fully retired
records; unknown/missing known state refuses. No registration records means no
gate. Preserve post-lock stale-generation refusal and selected recovery
paths; do not select an incapable package or delete evidence to escape uncertainty.

**Final-review correction at `85760a7a` (R1 accepted by lead):** retirement proves
native shutdown, not that a
predecessor can preserve registration metadata during later lifecycle operations.
At `c2182254`, `dev-session:preserve_removed_state!` moves tracking/team/creation,
but knows neither service path. Its delete therefore leaves marker/registry while
removing work/archive tracking; the next capable `load_state` calls
`tracking_owner` and refuses the orphan. Forward-only profile history does not
prevent selecting an incapable forward package. Require the existing capabilities
for all registration records instead of adding an old-delete reconciler or schema.
Stopping or archiving does not remove this requirement. A separately authorized
ordinary delete through a capable executor already transfers retired evidence to
its private removal recovery and clears active registration; only after its existing
journal finishes can absent active registration remove this gate. Retained completed
removal evidence stays intact. Recovery uses a capable forward package and the
original journal, never deletion of metadata or inferred tracking ownership.
A owns the validator; B keeps both host preparation/activation consumers and docs
consistent. Focused fixtures must reject an incapable predecessor before a retired
session's delete can be dispatched, retain the gate after capable archive/revive,
and prove capable delete/interrupted transfer preserves recovery evidence and leaves
no active registration after completion. Preserve absent-state acceptance and
missing/corrupt-state refusal. No live lifecycle experiment is required for design.
A folds the service `activity_token` into the existing auto-archive
`dimensions.activity`; do not add a `services` dimension or change the Store
allowlist/schema. With no registration, keep native `activityToken` byte-for-byte.
With a validated nonnull service token use SHA256 of JSON
`["session-services-activity-v1", native_activityToken, service_activity_token]`.
Only emit that dimension when both observations are known. On registry failure,
omit its replacement, preserve the prior dimension through the existing merge,
and retain the `services` unknown-dimension diagnostic that blocks eligibility.
Native activity unknown retains the existing continuity-loss/grace behavior.
Keep snapshot `activity_token` and `last_activity_at` as native observations.

Service token changes only on admitted new launch; stop, retirement and reads
retain it, including fully retired registries. The predecessor at `c2182254`
strictly validates dimension keys but accepts this activity digest. Its next scan
replaces the combined digest with its native token, starting fresh inactivity
grace through existing `Policy.observe`; it does not reject persisted state or
become eligible early. No new package gate, coverage marker, schema migration or
old-reader rescue is needed. This observation-format compatibility does not waive
the registration preservation capability gate above. Verify new persisted observations with the exact predecessor Store
for absent/registered/retired fixtures, predecessor fresh-grace behavior, unchanged
absent fingerprints, launch/native-activity resets, stable stop/read/retirement,
and unknown-registry refusal. Reset unpublished disposable development fixtures
containing the rejected extra dimension; they are not a supported migration.

### Receipt handoff clarification (source-derived A/B integration)

Go `LifecycleProgress.Evidence` hashes immutable journal content; prelude and
ordinary journal necessarily differ. Allow exactly one forward **archive** receipt
promotion when its captured phase is `services_pending` or `services_stopped`:
same operation/ID/archive mode, explicit retained-root equality (including absence),
and fresh proof of its already accepted v2 target. Prefer saved JournalTargetID /
location, otherwise original TargetID / location; sample the current directory
using the accepted location, preserving proof across the work→archive rename.
An absent/unverifiable accepted target cannot be invented or rebound for promotion.

While a prelude exists, require its full immutable evidence to match the saved
prelude receipt. After it disappears, the exact proof above permits promotion
without requiring a poll to have observed both files. Whenever ordinary journal
exists, select its evidence **and ordinary phase** as primary, validating any
coexisting prelude's ID/mode/root and authorized delete force upgrade. Carry
additional prelude evidence only in the in-memory reader result if needed. This
keeps delete and old-journal cleanup on their already accepted ordinary evidence.
Service cleanup detail remains available in the Services projection.

Persist ordinary evidence and phase together through existing receipt CAS; subsequent
ordinary evidence changes still refuse. No ordinary→prelude downgrade, repeated
ordinary-hash exception, new receipt schema or changed completion/revival proof.
Use one predicate at `operation_state.go`, `lifecycle_target.go`,
`observation_receipts.go` and `server.go` strict-comparison sites. Capture old phase
before updating progress; execution guards need that captured receipt or already
promoted proof. Read-only observation may validate the same handoff but never save
or retry it. Existing missing-journal recovery and delete false→true force remain.
Verify missed overlap, changed overlapping prelude, same directory after rename,
root/target/ID/mode substitution, a second ordinary hash change, and old delete force.

### Execution ownership and checks

A: new Ruby owner; `libexec/dev-session`, `workspace-archive-check.rb`,
`workspace-auto-archive.rb`; focused Ruby tests/aggregator; `docs/dev-sessions.md`
and `docs/session-archive-recovery.md`. B: portal/service projection and nested
Resources/counts; `libexec/workspace-host`, Go lifecycle/status readers,
`portal/internal/session/runtime-contract.json`, `nix/workspace-portal.nix`, host
tests, `docs/workspace-portal.md`/host docs and VM fixture. B does not edit A's
Ruby owner or lifecycle Runner; A does not edit B's host/Go/Nix files. B may begin
service-reader work from this contract now; surface a contract mismatch to lead
and architect before making incompatible shared changes.

Quick commands, from the feature root and using its Nix shell (run only relevant
focused files; these are a verification plan, not checks performed by architect):

```sh
nix develop --command ruby -Itest test/dev_session/session_services_test.rb
nix develop --command ruby -Itest test/dev_session/archive_check_test.rb
nix develop --command ruby -Itest test/dev_session/archive_cleanup_test.rb
nix develop --command ruby -Itest test/dev_session/deletion_lifecycle_test.rb
nix develop --command ruby -Itest test/workspace_host/profile_transition_test.rb
nix develop --command node --check portal/internal/web/static/app.js
nix develop --command node --check portal/internal/web/static/coordination.js
nix develop --command go -C portal test -mod=readonly ./internal/session ./internal/cluster
```

Use focused `go ... ./internal/web -run PATTERN` for affected existing/new browser
fixtures; its unbounded suite and unknown-duration batches use the required watcher.
Register new Ruby tests in the existing test aggregator so exported shards cover
them. After committed quick checks and mandatory review, the focused long batch is
`nix build --no-link --print-build-logs .#checks.x86_64-linux.package
.#checks.x86_64-linux.host-package-contract .#checks.x86_64-linux.session-archive-lifecycle`
(one command, through the required watcher). Package verification already depends
on `ruby-verification` and runs Go/JS checks; use the separately exported Ruby
check only for diagnosis or exact derivation/input reuse, not a duplicate campaign.
The existing VM must prove real user-unit descendants, start/stop interruption,
pre-prune ordering and old-format recovery. Do not replace its native proof with
fake-command unit tests or point it at live workspace services.

### Exact installed-package fixture invocation (prepared, not executed)

Use the existing `nix/tests/session-archive-lifecycle.nix` with its `devWorkspace`
argument bound to the exact deployed **site package**, then run its ordinary driver
afresh. This verifies installed bytes in an isolated VM; it does not exercise the
live host's user manager. `test/archive_acceptance.py` instead prepares historical
manifestless-repair fixtures, hardcodes an older native version and has no service
scenarios; it is not this rollout's acceptance entry point. No new harness is needed.

After final review/source correction, set these from the final rollout receipts.
The runtime revision must be committed and match the installed package's input
graph; do not substitute a moving checkout HEAD or generic package for those bytes.
Driver preparation can precede activation; run it after confirming selected-package
equality following the authorized system/profile switch. Both steps use the required
verification watcher, with exact output paths and logs recorded by the lead.

```sh
export SESSION_RUNTIME_SOURCE=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/dev-workspace
export SESSION_RUNTIME_REV=EXACT_DEPLOYED_40_HEX_RUNTIME_REVISION
export SESSION_INSTALLED_PACKAGE=/nix/store/EXACT_VERIFIED_SELECTED_SITE_PACKAGE
SESSION_FIXTURE_DRIVER=$(nix build --no-link --print-out-paths --print-build-logs --impure --expr '
  let
    runtime = builtins.getFlake ("git+file://" + builtins.getEnv "SESSION_RUNTIME_SOURCE"
      + "?rev=" + builtins.getEnv "SESSION_RUNTIME_REV");
    pkgs = import runtime.inputs.nixpkgs { system = "x86_64-linux"; };
    fixture = import (runtime.outPath + "/nix/tests/session-archive-lifecycle.nix") {
      inherit pkgs;
      self = runtime;
      devWorkspace = builtins.storePath (builtins.getEnv "SESSION_INSTALLED_PACKAGE");
    };
  in fixture.driver')
SESSION_FIXTURE_DIR=$(mktemp -d /tmp/session-services-installed.XXXXXXXX)
(
  cd "$SESSION_FIXTURE_DIR"
  TMPDIR="$SESSION_FIXTURE_DIR" LOGFILE="$SESSION_FIXTURE_DIR/driver.xml" \
    "$SESSION_FIXTURE_DRIVER/bin/nixos-test-driver" \
    -o "$SESSION_FIXTURE_DIR" --junit-xml junit.xml
)
```

Source basis: runtime `e29d4d83` lifecycle VM accepts `{pkgs,self,devWorkspace}`;
its pinned nixpkgs `nixos/lib/testing/driver.nix` exports `.driver`, and
`nixos/lib/test-driver/src/test_driver/__init__.py` accepts the flags above and runs
the supplied script without interactive mode. Recheck corresponding source after
the pending harness fix; no implementation change is needed for this invocation.
All lifecycle targets live inside the VM: user `developer` UID 1000, workspace
`/home/developer/workspace`, private state/origins, workspace name `fixture`, and
`/run/user/1000/dev-workspaces/fixture` sockets. No real workspace mounts, production
credentials, real-session slugs or host user-unit cleanup are part of the fixture.

Required evidence from that run: three registered main/stubborn-descendant/fast-exit
entries; stopping proof while scripts/assets still exist; mismatch refusal before
prune followed by the same receipt/prelude retry; units/cgroups gone; archived
history and no restart on revival; CLI delete's preserved files on failure and
retired evidence transfer on retry; automatic cleanup; unrelated unregistered guest
sentinel survives. Existing worker-interruption and portal-restart cases retain
operation identity. The native harness does not inject every lost launch reply or
cut execution midway through every service write; focused Ruby interruption proofs
remain complementary evidence, not claims about additional native cases.

Separately record actual deployed system/profile store-path equality, selected
runtime capabilities, authenticated portal/router/coordinator health and retained
Codex/tmux continuity. Read-only browser checks on this session cover Resources
subtabs/deep links/back-forward, resource counts matching pages with zero/unknown
distinction, Team including lead/retained members, and safe service/error rendering.
Positive service/error data comes from the disposable fixture, not live launches.
The existing browser helper tests archive/revive/retry; component UI tests and a
read-only usability check cover Resources/Team interaction. Do not enable live
automatic archival or retry lifecycle operations as a usability probe.

The driver context releases guest machines/networks on exit. Capture its exit and
cleanup outcome; after interruption, reconcile only this driver's exact processes
and run directory before deleting disposable data. Keep failed logs/evidence; after
successful verification retain compact receipts and remove only the recorded owned
`SESSION_FIXTURE_DIR`. No store GC, global unit globs, real-session cleanup or machine
claim release is implied. Actual configuration guidance is its AGENTS.md, README
and `docs/operations/aitherdev-disk-retention.md`, together with the selected
`workspace-host coordination guide` and config-pinned confctl source.

### Installed health and usability evidence (prepared, not executed)

Source anchors at `3d76f527a6b88e9d32c202f729a1a0d673b341f2`:
`nix/host-module.nix:638–673` (TLS/Basic Auth → router),
`portal/cmd/workspace-portal/router.go:82–125` (exact host → portal socket),
`portal/internal/web/server.go:952,1379,2043,2314` (health/details/session/team GET),
`portal/internal/web/coordination.go` and `libexec/workspace-coordination-host.rb:84`
(read-only exact-session coordination), and `docs/workspace-portal.md:312–358`.
These commands are for the lead after the authorized switch, using the deployment
operator's existing environment. Compare paths with exact prepared rollout outputs;
active unit state alone is not application readiness or conversation continuity.

```sh
set -o pipefail
readlink -f /run/current-system /nix/var/nix/profiles/system /home/aither/.local/state/dev-workspaces/profile
systemctl --user show workspace-router.service workspace-coordinator.service workspace-portal@vpsfree-cz.service workspace-codex@vpsfree-cz.service workspace-tmux@vpsfree-cz.service --property=Id,LoadState,ActiveState,SubState,Result --no-pager
SESSION_VERIFY_SLUG=2026-11-02-session-temporary-service-cleanup
SESSION_PORTAL_ORIGIN=https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz
dev-session --workspace vpsfree-cz coordination status "$SESSION_VERIFY_SLUG" --as-is --json --portal |
  jq '{schema, revision, suspended, owners: [.owners[] | {slug, observationIdentity}], heldMachines: ([.reservations[] | select(.state != "requested" and .state != "released") | .machine] | unique)}'
```

The following HTTPS GETs use the existing supported Basic Auth entry. `--user aither`
prompts for the password on the terminal; enter it privately using the operator's
existing credential access. Do not place a password in argv/environment/notes, read
it into captured output, enable curl tracing, export browser cookies or bypass TLS.
The public CA path is documented by the host module. No request was made here.

```sh
curl --fail --silent --show-error --max-time 30 --cacert /var/lib/dev-workspaces/public/ca.pem --user aither "$SESSION_PORTAL_ORIGIN/healthz" | jq -e '.ok == true'
curl --fail --silent --show-error --max-time 30 --cacert /var/lib/dev-workspaces/public/ca.pem --user aither "$SESSION_PORTAL_ORIGIN/api/sessions/$SESSION_VERIFY_SLUG/coordination" |
  jq '{schema, revision, suspended, owners: [.owners[] | {slug, observationIdentity}], heldMachines: ([.reservations[] | select(.state != "requested" and .state != "released") | .machine] | unique)}'
curl --fail --silent --show-error --max-time 30 --cacert /var/lib/dev-workspaces/public/ca.pem --user aither "$SESSION_PORTAL_ORIGIN/api/sessions/$SESSION_VERIFY_SLUG/details" |
  jq '{observationIdentity, clusterCountSnapshot, serviceCountSnapshot, teamCount, servicesKnown}'
curl --fail --silent --show-error --max-time 30 --cacert /var/lib/dev-workspaces/public/ca.pem --user aither "$SESSION_PORTAL_ORIGIN/api/sessions/$SESSION_VERIFY_SLUG/team" |
  jq '.roster | {rootThreadId, revision, count: (1 + ([.members[] | select(.state != "removed")] | length)), members: [.members[] | {address, threadId, state, model, reasoningEffort, access}]}'
```

Require successful command/HTTP status and valid expected fields; retain only these
safe projections. Health proves the authenticated nginx/router/portal path. The
coordinator unit plus matching CLI/HTTPS status proves its available reader path,
not execution of a queued job. Compare root/member thread IDs and saved settings
with the pre-switch same-session receipt; do not create turns, attach new sessions,
change the roster or restart anything to establish continuity.

Existing pinned Playwright runs inside the disposable VM via
`test/archive_lifecycle_browser.cjs`; its fixture origin/credentials and mutating
archive/revive/retry actions make it unsuitable for the live session. There is no
existing live authenticated Resources/Team browser runner. Component coverage is
already in the package check; its focused commands are
`nix develop --command node --test portal/internal/web/resources_browser_test.cjs portal/internal/web/coordination_browser_test.cjs`
and `nix develop --command go -C portal test -mod=readonly ./internal/web -run 'Test(Resource|Resources|TeamCount|OperationsNavigation)'`.
Do not repeat successful unchanged checks merely for this support brief.

Remaining manual evidence: in the existing authenticated browser, open this exact
session's `/#resources`, then Clusters → Reservations → Services; test Back/Forward,
reload and direct `/#clusters`, `/#reservations`, `/#services`, and keyboard
Left/Right/Home/End. Confirm one sidebar entry, matching owned-resource counts,
hidden confirmed zeros, and preserved unknown/stale indicators. Team `(N)` must
equal lead plus retained nonremoved members, including idle members; retain the
same lead/member conversations. Inspect Services without starting/stopping anything;
positive/error/retired rows are fixture evidence when absent live. Verify controls
on existing cluster/reservation pages remain visible, without activating them.
Record observed usability separately from component/VM results; do not claim a
live browser pass from curl, Node fixtures or a health response.

#### Bounded automatic browser feasibility (source-only support)

The fixture's existing root nixpkgs input (`a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`)
resolves to these exact declared tools; read-only evaluation performed, no build:

```text
node: /nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node
Playwright module: /nix/store/2xc3ahwfjaa3k3wpn4gslgws25swsyd7-playwright-core-1.59.1
Chromium: /nix/store/789yhb4v2kq51jwl4acmmjvxs7mfrlhv-chromium-152.0.7977.75/bin/chromium
```

They are already dependencies of `session-archive-lifecycle.nix:32–43,64–66`;
use the final matching driver/input preparation, not an extra browser install.
Host-module source gives `aither` membership in `workspace-portal-owner` and the
existing password file root:owner-group 0640 (directory 0750); its public CA is
0644 (`nix/host-module.nix:169,214–218,247–264,393–395,587`). No credential was read.
An anonymous pipe on inherited FD 3 is feasible: a file-reading child feeds Node,
Node reads `fs.readFileSync(3, 'utf8')` and closes FD 3 before browser launch; only
in-memory `httpCredentials: {username:'aither', password, origin: exactOrigin}`
receives it. Run as unprivileged aither, disable debug/traces/HAR/video, do not
export storage/cookies or print headers/exceptions containing credentials.

**Recommendation: retain the manual browser gap under the current boundary.**
Two source facts prevent certifying a direct one-off live invocation here:
(1) the fixture uses `ignoreHTTPSErrors:true`; the host publishes a CA but does not
establish Chromium trust for this operator. Playwright's context has no server-CA
file option; Node's CA environment is not proof of Chromium trust. Existing browser
trust may suffice, but was not inspected or tested. Do not substitute TLS bypass.
(2) pinned Playwright `types/types.d.ts:4039` and
`lib/server/chromium/crNetworkManager.js:297–304` show redirected requests bypass
the user route handler. An origin/path/method allowlist followed by `route.continue()`
therefore does not establish the requested strict boundary across redirects.
Origin-scoped auth prevents credential forwarding, not the redirected HTTP request.

`serviceWorkers:'block'`, pre-page `context.routeWebSocket(...)` without connecting
to the server, and aborting non-GET/HEAD requests are supported. A future approved
one-off would also need proven CA trust and redirect interception/rejection before
the next network request; adding a CDP/HTTP response relay or NSS setup now would
exceed this small source-support task. No new harness is proposed. If those bounds
are later supplied, use one ephemeral context, a fixed timeout, only this session
page/static assets and reviewed own-session GET endpoints, then tab/hash/history/
keyboard assertions and counts against the same responses. Expect Team (6) only
while the unchanged roster remains lead plus five retained members. Positive/error
service rows remain VM evidence. No credentials, browser, request or probe ran here;
this gap does not hold the source/native pipeline or change deployment authorization.

### Capacity retry operational diagnosis (2026-11-03)

See [capacity-retry-diagnosis.md](capacity-retry-diagnosis.md) for bounded evidence
and source/test citations. This is separate from service cleanup and CI. Installed
package `0q7rc75dh4mjrxpb37m1hchfwcbmpa7a` records native `serverOverloaded` for lead
turn `01a19de7-008c-7513-b64f-9e649c4db784`, with the exact reported capacity text.
The classifier recognizes it and session capacity retry is enabled. The turn had
74 distinct native inputs and 73 retained accepted steer receipts. Installed
admission retention caps snapshots at 64; removing a current-turn contributor
sets `Handled` and invalidates its aggregate proof. That handled-turn gate prevents
later retry scheduling. The observed ledger retains the expected recent suffix,
no failed-turn proof/chain/pending UUID, and the failed-turn handled watermark.

This is documented fail-safe retention behavior, not a proved text-matcher defect.
Later `manual_input` is not the original reason. Exact first eviction timing and
count-versus-byte pressure are not retained; do not invent them. Saved native
model/effort/provider remain `gpt-6.1-sol` / `high` / `codex-lb`. No policy/settings,
records or replay changed. Existing tests cover atomic contributor retirement,
nonrevival of suppressed proof, and eligibility of later independent managed turns.
Natural milestone completion into separate turns can avoid accumulating so many
steers, subject to all ordinary proof/admission gates; it does not rearm this turn.
The diagnosis alone released no implementation. The user's subsequent direction
that input volume must not invalidate capacity retry is addressed separately below;
it does not change the diagnosis or authorize replay of this already-handled turn.

### Capacity retry correction: compact current-turn authority

**LEAD ACCEPTED / IMPLEMENTATION ASSIGNED A / NOT IMPLEMENTED — 2026-11-03.** Separate coherent
runtime change after `5b4b711748343f4ffe88b96c50d88a9f98eeb04d`; do not fold it into
the service-cleanup commits or B's native fixture correction. One implementation
package, released to A by the lead. No model/provider/effort changes, original
prompt replay, reason-visibility UI, or policy/backoff/quota changes.

**Requirement and authority.** An otherwise eligible active turn must retain retry
eligibility for any number of accepted managed inputs. Keep the existing 64-entry
budget for outstanding admission/reconciliation records; accepted history must
leave that budget through lossless compaction, never current-turn eviction.
`ReadTurnContext` already proves the actual model, effort, mode and native policy.
It explicitly does not prove provider, instructions or application context. Reuse
the existing managed `Binding`/epoch/socket identity for those, rather than saving
another complete instruction copy per accepted steer. Still account for every
native user item: otherwise an external writer's input/context could silently gain
our managed execution authority. This is provenance checking, not prompt replay.

**Small persisted extension.** Keep ownership in `internal/turnretry`, in the same
private, atomically replaced retry record and under the same admission lock.
Add schema 2 with one optional `managedTurn` object (JSON names below):

| Field | Meaning |
| --- | --- |
| `version: 1`, `turn`, `epoch`, `bindingDigest` | Exact native turn and existing managed authority; scope/root/socket/incarnation remain in the enclosing record and binding. |
| `count`, `digest`, `lastUserItemId` | Verified chronological native user-item prefix: nonnegative count, SHA256 chain, final native item ID; empty prefix has the defined seed and no final ID. |
| `additionalContext` | Existing application-context map, merged once with the existing conflict and size rules. No per-input instruction copies or growing ID list. |

Use the existing SHA256/JSON conventions, not a new cryptographic primitive.
Define the seed as SHA256 of the JSON array
`["managed-turn/v1", scope, epoch, bindingDigest, turn]`. Each step hashes the JSON
array `["managed-turn/input/v1", previousDigest, nativeItemId, clientUserMessageId,
textDigest]`; count and last ID must agree with that prefix. Use canonical Go
struct/array encoding, lowercase hex, and fixed fixtures. The empty native client
ID is retained as empty in this hash; it may match only the existing unique
`initial` admission by exact text digest. No text is added to this record.
Reference the one existing binding; do not infer or reconstruct a lost binding
from current defaults. Native context is captured through the existing exact
reader when forming the final executed snapshot. Pending retains its existing
immutable full snapshot; the aggregate is never a replacement delivery receipt.

**Atomic acceptance and compaction.** Keep pre-send capture and exact generic
receipt reconciliation in their present order. A receipt binds an admission to
its exact turn as today. Compact only after native history also identifies the
item by exact client ID/content (or the existing initial exception), matching its
saved epoch, binding, provider, policy, instructions and context. Native acceptance
can itself bind a queued/initial admission; enqueue-time defaults cannot prove
execution settings. Fold in native chronological order, not receipt arrival order.
In one `Transaction.Save`, extend the prefix, merge context and remove precisely
those consumed source snapshots. Before that save they remain protected. If it
fails, the durable originals remain and the cursor cache must be discarded.
An accepted reply whose item is not visible yet remains a bound, protected
snapshot; missing history is not proof that it was unsent.

This handles delayed receipts without tombstones: generic UUID reconciliation
still runs before capture; a recovered accepted UUID whose snapshot was compacted
returns its original receipt and cannot be admitted/folded again. If the snapshot
survived a failed save, exact native matching folds it once. Never recapture old
accepted input under today's settings. Preserve the existing prepared-plan and
uncertain-submission exceptions exactly. Automatic accepted-result bookkeeping
and charge settlement remain authoritative even while its new result-turn proof
is incomplete; reserve room before dispatch and retain the exact result admission.
Do not suppress an accepted result merely to fit another repeated settings copy.

**Incremental native reader.** Add a narrow runtime-local reader via the already
exported `Client.Request("thread/items/list", ...)`, with exact `threadId`, `turnId`,
`sortDirection:"asc"`, bounded `limit` and returned opaque cursor. No codex-web
source/dependency update. Validate required data, exact turn/item IDs, text input
normalization, page bounds and cursor progress as in its current item reader;
never hash rendered/display text. Malformed or unsupported input is not absence.
Only the unverified suffix needs admission matching. On a fresh reader, stream
from the beginning, recompute the saved prefix's count/hash/final ID and require
equality before accepting any suffix. Thus restart needs no retired snapshots.
Changed/truncated/reordered prefix fails closed; it is never treated as a new
empty turn. A delayed old-turn receipt cannot replace the latest turn's authority.

Keep the traversal cursor and at most one bounded page in the existing long-lived
workspace client, scoped to exact state prefix, thread/turn, socket identity and
native metadata/rollout identity. They are acceleration hints, not authority.
Invalidate on mismatch, read/reset error or failed save. For an active tail retain
the input cursor of its last page and recheck that bounded tail before advancing;
do not invent a cursor from an item ID. Discarding a cache entry/restarting merely
requires incremental prefix replay. No durable opaque cursor or new scanner store.

Advance evidence during the existing admitted scheduler step for active turns as
well as failed turns, and opportunistically before new capture/after receipt
binding under the existing transaction. A small `Backend.AdvanceProof` seam may
share that reader with `Prove`; it grants no native mutation authority. Keep the
existing two workers, deadlines and lock order. Exhausting a page/time work budget
returns retriable incomplete progress, saves valid folded evidence, leaves
`Handled` unchanged and does not mark the idle token settled. Next admitted step
continues. Remove the 256-page terminal proof cutoff; there is no total-page or
total-input eligibility limit. Before scheduling, finish the latest failed turn's
suffix and form the existing executed proof from the binding, merged context and
exact native context. Recheck all existing execution gates before dispatch.

For an otherwise eligible turn, an unverified current-turn snapshot must never be
evicted to admit another input.
If native evidence cannot catch up and protected records fill the existing budget,
refuse fresh admission before sending, preserve evidence and let checking continue;
do not consume the turn. Obsolete accepted turns may still retire under the old
rules, and unresolved queue/UUID records stay protected. Shared context remains
subject to existing representability/conflict limits: arbitrarily many identical
managed steers do not grow it, but incompatible or genuinely unbounded new context
cannot be replayed as one bounded native request. This is distinct from input count.

**Already-handled active-turn exception (2026-11-03 clarification).** Ordinary
manual work must not fill the retry budget with proof that is permanently forbidden
to authorize continuation. If the exact nonempty current turn already equals the
durably saved `Handled` watermark, permit the existing oldest accepted-bound
retirement for count/byte pressure. Retire only a snapshot with that exact turn,
different from the incoming ID, not `Proven`/`executed`, and not protected by the
existing Pending/unbound rules. Preserve `Handled`, epochs and every Pending,
unaccepted, uncertain or unbound tuple; do not construct/extend compact authority
for the handled turn. This is retirement of unusable evidence, not compaction or
permission to suppress an otherwise eligible turn to make space.

Use the ordinary admission transaction's durable state after cancellation has
been saved and the exact current turn observed. `Cancelled`, `manual_input`, an
absent binding or a temporarily incomplete native read alone cannot trigger this
exception. At base `5b4b7117`, `captureRetry` saves `Cancel("manual_input")` before
the uncertainty check and current-turn read (`turn_retry.go:154–183`); `Cancel`
does not generally mark the current turn handled (`state.go:162–170`). In contrast,
`InvalidateSettings` explicitly sets the observed turn's watermark and advances
the epoch before the settings RPC (`state.go:175–187`, `turn_retry.go:588–609`).
Later warm binding promotion must not clear that watermark. Receipt-first replay
still returns an accepted retired UUID without recapture under a newer epoch.

Add focused fixtures for an upgraded already-handled turn with missing first
contributors, and a same-active-turn settings intent followed by warm binding:
accept more than 64 further steers (also byte pressure/restart), keep storage
bounded through accepted-bound retirement, and never schedule continuation when
that turn later fails. Assert no prefix reconstruction, unchanged watermark and
immutable uncertainty; protected-only pressure still refuses before sending.
Contrast `Cancelled/manual_input` without `Handled == currentTurn`: it must retain
all current-turn evidence or refuse fresh admission, never retire it. A later
independent eligible turn must still establish proof and retry normally.

**Obsolete executed-proof retention (2026-11-03; lead accepted, assigned A).**
Compaction removes source admissions, so executed cached proofs can no longer rely
on source retirement to remove them (`5b4b7117 state.go:506–529`). On a successful
fresh native latest-turn observation `T`, under ordinary admission, filter only
snapshots satisfying `T != "" && p.Turn != "" && p.Turn != T &&
(p.Proven || p.Origin == "executed") && !protectedSnapshot(p)`. This is retirement
after authority advances, not pressure eviction. Preserve current-turn proof,
Pending's full copy and protected sources, unbound/uncertain admissions, `Handled`,
epochs, compact authority, charges and UUIDs. A saved receipt's turn, an empty or
failed native read, or pressure alone does not establish the latest-turn authority.

Use one state filter from the existing `Controller.Step` successful-observation
path before proof/admission, and `captureRetry` after its ordinary cancellation
save/uncertainty check and successful latest-turn read, before new snapshot capacity
checks. Save a changed filter atomically through the existing transaction before
dependent admission/dispatch; a save error aborts that work and cannot publish a
new reader hint. Do not tie cleanup to successful compaction, a nonhandled turn,
or absence of legacy proof. Keep receipt-only/uncertain early paths unchanged.
An old protected proof becomes removable only after ordinary Pending replacement
or clearing and a subsequent fresh observation. No new collector, field or cap.

Fixtures must sustain more than 64 independent/automatic turns after compaction,
including large repeated proofs, without growth in orphaned proof count/bytes.
Assert all three Pending protection matches (pending ID, snapshot ID, snapshot
turn), its immutable copy, current-turn proof and unbound records survive; charges,
UUIDs and watermarks do not change. Cover empty/error observations, save failure
and restart, later retirement after ordinary Pending release, and no rearming or
dispatch merely because obsolete evidence was removed.
Use existing state/controller fixtures for many-turn retention; no additional
large wire campaign is needed. Preserve the actual 205-large one-off verification
receipt; permanent volume cases remain 205-small/65-large as directed by the lead.

**Cancellation and compatibility.** Settings intent still advances the epoch
before native mutation and consumes the old turn; clear its compact authority
without changing any immutable Pending tuple. Preserve provider/socket changes,
Stop/disable, manual/new queue cancellation, recovery/queue holds, enrollment,
Handled/baselines, quota and idempotent UUID behavior. Never rearm the diagnosed
handled turn. Independent native writers remain outside the admission fence:
observed unknown input blocks retry; no client can promise absence of a concurrent
external writer because the native protocol lacks atomic compare-and-start.

Read strict schemas 1 and 2; only an ordinary admitted save upgrades a valid
schema-1 record. Keep Snapshot/Pending formats, hashes, IDs, charges, policy-sidecar
schema and recovery tuples unchanged. Retained complete schema-1 contributors can
be compacted by the same exact native proof; missing/handled evidence cannot be
recreated. Existing valid executed/Pending proof retains its old recovery path.
Do not bulk rewrite records or use current settings to fill missing admissions.

Publish `turnRetryManagedTurnProof: 1` for schema-2 read/write and this compaction
contract. Retain `turnRetryStateSchema: 1` as the predecessor-reader compatibility
declaration: changing it to 2 would make the installed host refuse the upgrade
before the dual reader can run (`workspace-host:3054`). Extend the existing
presence-based retry package guard to require both declarations whenever any retry
JSON exists, including cancelled/legacy/malformed records; no new marker, inventory
or Ruby payload migration. New selection and candidate activation enforce this;
the predecessor host can admit the dual-reader candidate through its original
schema-1 check. A predecessor strict reader rejects schema 2 and must never be
selected to manage it. Recovery is forward with a compatible package; never erase
retry state to pass a package check. Existing policy/lifecycle/provider capabilities
and generation fences remain independent and unchanged. This conservative gate
also applies to retained schema-1 retry records after selecting the new runtime.

**System-first upgrade feasibility (source-only, 2026-11-03).** The new capability
does not require a bridge package or reversing the accepted system/profile order.
At `5b4b7117`, `nix/host-module.nix:74–85,589–617` activates only the root-owned
TLS/auth substrate reconciler; it neither selects the application nor calls
`workspace-host`. A system-generation change can trigger the existing user
`workspace-codex-reconcile.path`, whose service invokes
`%h/.local/state/dev-workspaces/profile/bin/workspace-host reconcile-codex`.
That is the still-selected predecessor. Its `@system_codex` is its own packaged
Codex (`workspace-host:392`), not a newly installed system workspace application.
`reconcile_codex`/`reconcile_codex_update` (`2187–2248`) do not call the retry
capability guard. Selected `0q7` confirms the same paths at wrapped-host
`391,2186–2218`; its retry guard at `3020–3029` still checks only schema 1.

Ordinary profile `switch` then runs the selected host's `prepare_profile` and
`activate_candidate`, checking the **candidate** (`640–697`), selects that package,
and invokes its own activation (`730–740`). Only then does new `_activate` check
its own `package_root` (`1135–1142`), which advertises both retry capabilities.
Prepared legacy activation delegates to the same candidate path; explicit
bootstrap prepares/checks its exact candidate and is not a NixOS activation hook
(`workspace-coordination-host.rb:470–480,517–544,783–853`). No bootstrap is needed
or authorized here. Aitherdev config `59d12a3b`, `config.nix:19,106,109,224`, imports
the host module and a separate Codex package without installing the user app.
Keep system activation first, ordinary claimed user-profile switch second, and
all existing pending-operation/forward-recovery checks. This is caller-path proof,
not an executed activation or a waiver of the original deployment verification.

**A's complete package and verification.** Own `portal/internal/turnretry/{state,
store,controller}.go`, `workspacecodex/turn_retry*.go` and the small client reader
state, affected focused tests/mocks, `session/runtime-contract.json`, the existing
`libexec/workspace-host` retry guard and `test/workspace_host/profile_transition_test.rb`,
plus `docs/turn-retry-recovery.md` and necessary existing retry documentation.
Lead explicitly transferred the now-idle host-contract lane from B to A; no UI/extension/config pin
or codex-web work is required. Keep this a separate feature commit/deliverable.

Required regressions: 65/74/200+ accepted steers and repeated large identical
instructions/context remain bounded and eligible; more than 256 native pages
complete across deliberately tiny batches; restart mid-prefix and after compaction
loses no authority. Cover queue/initial/automatic contributors, delayed and replayed
receipts, save failure on either side of folding, and exact prefix corruption,
unknown input, changed text/order/turn/binding and malformed cursor responses.
Verify pre-send pressure refusal preserves current authority; distinct context
conflicts remain refusal. Settings/provider/socket changes, Stop/disable, queued
work, recovery holds and unsupported failures still prevent dispatch. Capacity
failure yields one continuation with the exact original model/effort/mode/policy
and context; a lost acknowledgment/restart settles the same UUID once and charges
once. Exercise old schema-1 uncertain tuples, already-handled failure, valid legacy
proof conversion, strict old-reader rejection, predecessor-host candidate admission
and new-host refusal of an incapable target without changing retained bytes.

Quick commands, run by A later in the repository Nix environment:
`nix develop --command go -C portal test -mod=readonly ./internal/turnretry ./internal/workspacecodex`
and `nix develop --command ruby test/workspace_host/profile_transition_test.rb`.
Use the README's absent test provider catalog for affected portal tests, then the
existing Go/Node shipped retry/browser suite. After commit, quick checks and
independent review: `nix flake check --print-build-logs` under the normal watcher
policy; retain original service-cleanup VM obligations separately. Exercise the
new reader against the pinned native protocol in disposable existing fixture
tooling, including multiple pages and same-UUID retry; no live-session reproduction.
No checks or implementation were run by the architect for this design.

Source anchors at the stated head: `workspacecodex/turn_retry.go:154,257,283,325,369,391,535`;
`workspacecodex/turn_retry_proof.go:38–173`; `turnretry/state.go:435–529`;
`turnretry/controller.go:145–237`; `web/turn_retry.go:113–146,247`;
`turnretry/store.go:148–285`; `libexec/workspace-host:3049–3059`.
Pinned codex-web `d3a29bee90ef`: `codex/turn_context.go:14–95`,
`codex/client.go:2338–2420`, `codex/thread_page.go:377–419` and
`test/codex_protocol_contract.py:329–331`. These establish available interfaces;
new compaction, cursor replay and mixed-version behavior remain implementation
verification obligations, not claims of completed testing.

## Recommendation and supported boundary

Add one local temporary-service owner to reusable `dev-workspace`: a public
launcher that durably registers each service before starting its systemd user
unit, and an archive/delete cleanup gate that stops and verifies every registered
unit before deleting any supporting files. Future previews and candidates use
the same launcher, including new launches in existing sessions. A service can
remain available after feature integration and through idle conversations until
its session is explicitly archived or the enabled automatic worker archives it
under its existing policy.

This covers registered local transient systemd **user services and their native
cgroup descendants**. Existing unregistered services are excluded: no inspection,
discovery, adoption, cleanup or new archival gate for them. Commands that
deliberately escape into another unit/cgroup, remote servers, containers with an independent
lifecycle, persistent system services and production services are outside this
launch contract and do not acquire a new reconciliation gate. Existing development
cluster ownership remains separate. Do not kill by port, PID, pathname or a
matching name. The trusted local operator boundary remains unchanged; this is not
containment against a hostile operator.

## Evidence

Identity was verified with `dev-session current` and both environment markers:
`2026-11-02-session-temporary-service-cleanup`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. The same-session roster retains
architect0 as Astra/xhigh, workspace-write. Its exact
`worktrees/.locks/2026-11-02-session-temporary-service-cleanup.creation.json`
records `state: ready`, `schema: 3`, `provider: codex-lb`; settings were unchanged.

`workspace-host status` and `workspace-host coordination guide` select:

- Package: `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
- Derivation: `/nix/store/2jvhgyq2ilxa4cprlswc7fwh93b3snpx-dev-workspace-0.2.0.drv`.
- Exact derivation `src`: `/nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source`.

Paths below are relative to that immutable source. Its `libexec/dev-session`
matches installed `libexec/workspace-portal/.dev-session-wrapped` except for the
packaged Ruby shebang. This identifies the inspected implementation without
assuming that the canonical repository's current HEAD is the deployed revision.

| Evidence | Consequence |
| --- | --- |
| `libexec/dev-session:2041`, `archive_with_access` | Explicit, strict and automatic archive converge here. Fresh archival calls `WorkspaceTrackingSummaries.prune(..., apply: true)` at line 2134, **before** `prepare_archive_journal!`. Cleanup added only to a later journal phase is too late. |
| `libexec/dev-session:9341`, `quiesce_explicit_archive!`; `:9392`, `quiesce_and_require_idle!`; `:7000`, `retire_session_runtime!` | Current shutdown concerns Codex clients, native/team conversations and trusted tmux identity. It does not inventory independent user services. |
| `libexec/workspace-tracking-summaries.rb`; `libexec/workspace-archive-cleanup.rb` | Tracking pruning removes non-Markdown/non-portal files; cleanup inventories and removes owned checkouts. Neither is a temporary-service owner. |
| `libexec/dev-session:2463`, `delete_with_access` | Delete has its own journal and removes worktrees before runtime retirement; it needs the same service gate. |
| `portal/internal/web/archive_worker.go:77` | The portal already launches an independently supervised transient user service using `systemd-run`, `Type=exec`, `RemainAfterExit=yes`, and `KillMode=control-group`. Reuse this native mechanism, not the archive worker's authorization or unit. |
| `docs/session-archive-recovery.md`; `docs/dev-sessions.md` | Existing archive/revival policy, saved operation identities, package exclusion, automatic eligibility and deferred tracking synchronization must remain authoritative. |
| `libexec/workspace-host:3082` and `portal/internal/session/runtime-contract.json` | Package selection already checks capabilities against retained archive state; extend that boundary for service ownership and pending cleanup. |

The HaveAPI incident is supplied evidence, not a live finding from this session.
It includes `haveapi-doc-language-preview-20261101.service` and all three
candidate units (`candidate`, `nov2-candidate`, `cachefix-candidate`). Their
reported independent user-service lifetime and lack of `PartOf`/`BindsTo` explain
why terminal/agent retirement does not stop them. Their launch scripts, preview
source and ignored gem dependencies are vulnerable to the existing prune/removal
order. No originating-session files, units or transcript were inspected. Under the
user's amended scope these existing unregistered examples remain outside the
cleanup guarantee and untouched; they do not block this feature's archive path.

## Proposed API and ownership record

Exact spelling and timeout defaults below are proposed, not tested interfaces:

```text
dev-session service run SLUG --as-is --name LABEL --cwd PATH -- COMMAND ARG...
dev-session service list SLUG --as-is --json
dev-session service stop SLUG --as-is --id RESOURCE_UUID
```

`run` is the normal launch path, including experimental candidates. The CLI
returns an opaque resource ID and exact generated unit name. Labels are display
metadata, not identities; repeated launches create separate resources. `list`
reports saved ownership and fresh status without mutating it. `stop` uses the
same stop verifier as archive. There is no generic unregister-live-service or
arbitrary shell cleanup-hook API. There is no inventory/adoption command.

Use one bounded, private, atomic JSON registry per session under the existing
user-state root, for example `session-services/<workspace-id>/<slug>.json`,
outside pruned tracking and worktrees. Proposed schema 1 contains:

- Exact workspace root, slug, retained root/creation identity where available,
  a fresh resource epoch and binding to the verified current session incarnation.
  Use existing lifecycle/creation identity checks; slug or CWD alone is insufficient.
- Per resource: UUID, label, generated exact unit, local user-manager identity,
  ownership nonce, launch intent, boot ID, observed InvocationID and ControlGroup,
  bounded stop policy, phase and last bounded diagnostic. Keep commands/environment
  private; do not copy secrets into tracking or public status.
- When cleaning: lifecycle kind, exact operation ID and saved archive mode,
  frozen resource IDs, phase and per-resource stop/removal results. This is a
  service cleanup prelude to the existing lifecycle, not a second archive engine.

On the first managed launch, publish a small durable registry-ID reference in
retained session metadata, then create the matching registry and launch intent
**before** contacting systemd. This reference records only that managed
registration exists; it says nothing about other services. A crash between these
writes leaves a recoverable incomplete registration, never permission to launch.
Choose the exact metadata location during implementation and retain it through
archive/revival; do not infer a missing reference from a session's age.

Serialize launch, stop and lifecycle admission using the existing transition →
creation → session lock order and post-lock generation checks. Pending cleanup rejects new
launches, even after an interrupted archiver releases its OS locks. A timed-out
start is uncertain: reconcile the exact nonce/unit/job under the original resource
ID; never launch a replacement merely because its reply was lost.

Prefer `Type=exec`, `Restart=no`, `KillMode=control-group`, `SendSIGKILL=yes`,
`RemainAfterExit=yes` and a bounded `TimeoutStopSec` (proposed 15 seconds).
Retaining the transient unit until explicit cleanup makes short-lived/failed
launches observable. Do not enable it at login, add activation units, or let a
caller override ownership, restart or cgroup properties. Allocate unique unit
names and attach the ownership nonce when launching; verify live properties
against the durable record. No dependency on terminal or portal lifetime is
needed. Ordinary forks, daemonization and grandchildren remain in that cgroup;
escaping into another manager resource is outside the contract.

## Archive/delete sequence and failure contract

1. Run current authorization, ownership, claims, journal and archive-readiness
   checks. Add registered-resource validation to read-only `archive-check`, without
   stopping anything. No registry and no registration evidence means no managed
   resources and no new blocker. Automatic scans retain existing eligibility/holds.
2. Under lifecycle admission, freeze launch admission and durably bind the service
   cleanup prelude to the exact accepted archive/delete operation and resource set.
   Publish it **before any service stop or tracking prune**. Preserve existing
   explicit agent quiescence and automatic idle requirements. All conflicting
   lifecycle, creation, revival and package paths must recognize this prelude as
   pending even if the ordinary archive journal has not yet been written. Sessions
   with no managed resources continue the ordinary path without a service prelude.
3. For every registered resource, including failed/starting candidates, reconcile
   its exact identity and outstanding start/stop jobs. Request native service stop;
   systemd sends the graceful signal to the cgroup and escalates to SIGKILL after
   its timeout. Bound the observation wait as well (proposed another 5 seconds).
   Do not substitute process-group killing or a PID-file check.
4. Prove no pending activation/start job, a terminal unit state, and an empty or
   removed recorded cgroup including descendants. A successful `systemctl` exit,
   absent MainPID, closed port or `ActiveState=failed` alone is insufficient.
   Changed InvocationID, manager identity, unknown job state, permission failure,
   lingering descendants or a timeout blocks file deletion. A still-busy kernel
   task remains a blocker even after SIGKILL. Record which owned services stopped;
   leave other sessions and registered-service-dependent files untouched.
5. Release only the exact owned transient unit state (including failed-state reset
   when needed) and verify it unloads without activation sources. No unlinking
   systemd's private unit files or global `reset-failed`/journal vacuum. Preserve
   compact private stop evidence; system journal retention follows host policy.
   Recheck the complete frozen set immediately before the first file deletion.
6. Mark service cleanup verified, then prune tracking, prepare/seal the existing
   archive inventory and continue normal cluster, worktree, tracking and runtime
   phases. Delete calls the same gate before its first worktree/file removal.
   Existing ownership, exact-head and recovery checks remain in effect; `--force`
   cannot bypass unproved service shutdown.

New service-created scratch files should live inside the owning session's existing
tracking/worktree boundaries and use their ordinary removal policy. The API does
not grant arbitrary external file deletion. Ordinary tracking/worktree pruning
remains unchanged, including files used by unregistered services. Markdown/portal
retention and committed-only worktree restoration remain unchanged. No attempt
to preserve a temporary server's in-memory fixture state.

Every step is retryable under the original operation ID. A crash after stop but
before its progress write requires fresh manager/job/cgroup proof, not a second
launch. A unit name reused for another invocation refuses. A lost manager/reboot
must be positively reconciled with the recorded boot, unit and cgroup evidence;
connection failure is not absence. Partial cleanup keeps the operation pending
and recovery files intact. Retry never restarts services to compensate for failure.

## Existing sessions, revival and rollback

Initialize registration lazily at the first managed launch in any session. A new
or old session that never used the launcher needs no service record, migration,
audit or confirmation. Archive/delete proceeds under its ordinary rules. Only
future launches through the API become managed; other services remain untouched
and outside the guarantee. Forks do not inherit another session's registrations.

Distinguish absence from loss: a registry-ID reference or pending lifecycle/launch
evidence proves that registration is expected. A missing, corrupt or mismatched
registry in that case blocks file deletion until the original registered state is
recovered. So does uncertainty about a registered launch or stop. An untouched
old session has no such evidence and gains no blocker. Do not discover units to
fill missing records, and do not turn the registration reference into a claim
about all services belonging to a session.

Preserve all predecessor archive/removal/revival journal formats, saved policies,
sealed tracking checksums, recovery snapshots and committed-head proofs. Add the
registered-resource guard before any *remaining* file deletion without rewriting
old evidence; no registered state means no added recovery obligation. Files already
removed by an old executor cannot be retroactively protected. Completed archives
are not reopened or backfilled. Revival never restarts temporary services; retain
completed registration/stop evidence and use a fresh resource epoch for subsequent
managed launches. Sessions without registrations retain their original revival
and file-restore behavior without an audit gate.

Advertise service state/cleanup support in the runtime contract and check it in
both package selection and candidate activation, following existing capability
checks. New launch/prelude state must survive a compatible package switch; service
registration neither stops nor restarts previews during ordinary activation.
Pending cleanup already excludes package mutation. A target must advertise the
existing service state and lifecycle capabilities whenever any registration
records remain, including fully retired records: it must preserve them through
archive, revival and deletion. Absent registrations require no new capability.
Never discard evidence to pass the check. Recover forward with a capable package;
completed capable deletion retains its evidence in ordinary private removal
recovery and clears active registration. First-upgrade and rollback
tests must include stale pre-upgrade commands waiting on locks. No database/API/client/protocol migration,
fleet coordination or system configuration change is indicated; the persistent
change is local runtime state and its package compatibility contract.

Explicit archive approval covers this necessary temporary-service cleanup for
that session. Automatic cleanup occurs only inside its already enabled worker's
authorized archive operation; preserve the 1/7/14-day policy and Keep open hold.
Managed service launches should reset inactivity through the existing
semantic observation mechanism; status polling and service uptime should not.
Ordinary completion, merge, review, handoff or release of a machine never triggers
service cleanup or session closure. Delete retains its separate exact user approval.

## Proposed portal resources and Team count

Per the user's amendment, replace the separate Clusters/Reservations entries and
proposed Services entry with one **Resources** sidebar entry (label for lead
acceptance). Its page has **Clusters / Reservations / Services** subtabs, using
existing tab, card, badge and notice styles. Preserve current cluster/reservation
controls. Services remains visibility-only; no new resource manager or dashboard.

Show three compact, distinguishable icon/count indicators inside the sidebar
entry, with per-kind accessible names/tooltips and existing icon styling. Hide
each confirmed zero; when all three are confirmed zero show no indicators, but
keep Resources available. Unknown/busy/unavailable is not zero: show a per-kind
unknown marker or visibly stale last-known count with its age/tooltip, including
when the last known value was zero. Do not sum unlike resource kinds.

| Indicator | Authoritative count and page relationship |
| --- | --- |
| Clusters | Existing provider-owned clusters confirmed by `found`, including stopped clusters with retained state; not configured provider definitions, VMs, endpoints or only running clusters. Match the current cluster cards, excluding retired history. `InspectContext` synthesizes unavailable cards on errors, so raw `len(.Clusters)` is not proof: preserve presence/count certainty separately and do not count a diagnostic placeholder as a confirmed cluster. |
| Services | Current, not-yet-retired resource IDs in the registered-service reader: include starting, running, exited/failed and stopping/uncertain cleanup entries until verified retirement. Match the current Services list; put retired records in historical evidence outside the count. Registry membership supplies the count without a live unit scan; a unit-status failure need not invalidate known membership. Lost/corrupt expected registry makes membership unknown. No registry/registration evidence means zero. |
| Reservations | Distinct canonical machines currently held by this exact session incarnation, matching the existing Reserved machines section and complete `reservationHolders` summary. Include held claims and legacy review/recovery holds, deduplicating aliases/records. Requested/waiting claims own nothing and do not increment this count; they remain visible separately. Released/canceled history and repository-only claims do not count. Tooltip identifies the count as held machines, not requests or claim records. |

Team becomes **Team (N)**, including the lead: its current Members table renders
a lead row plus every retained roster member whose state is not `removed`.
Use that same roster projection, including idle, creating, failed or archived
retained members; do not use `readyMembers` or running-agent counts. Exclude removed
history and utility watchers/temporary reviewers outside the roster. A known solo
session shows Team (1); retain the current absence of Team navigation for a
threadless session. The parenthetical is never suppressed as a resource-zero
rule. A failed roster read shows unknown or a marked stale count, not inferred 1.

Retain `#clusters`, `#reservations` and proposed `#services` as child deep links:
hash handling selects Resources and the indicated subtab. `#resources` opens
Clusters by default. Reuse the Settings nested-tab/history pattern, preserving
reload, back/forward, query parameters, keyboard focus and panel ARIA relationships.
Update coordination's visibility check/event handling for the nested Reservations
panel; do not break existing controls or links from Workspace operations.

Source anchors under `portal/internal/web/` in the inspected immutable package:
`templates/session.html:25`–`:28`, `:69`, `:236`, `:338`–`:360`; `templates/clusters.html`;
`static/app.js:3042`–`:3113` (nested Settings/hash navigation) and `:4028` (details
refresh); `static/coordination.js:42`–`:64` and `:229` (held-machine count/refresh).
`portal/internal/cluster/status.go:189` distinguishes found/error results;
`libexec/workspace-coordination.rb:1550`–`:1604` builds incarnation-bound held-machine
summaries before limiting history. `portal/internal/web/coordination.go:15`
documents read-only GET.

Add current counts plus known/stale metadata to initial/session-details projections
for clusters, services and Team; reuse coordination's existing session-scoped GET
and complete holder summary for reservations, not truncated claims/history arrays.
Keep the existing bounded, visibility-aware refresh/cancellation loops; no new poller.
Apply each count with its corresponding accepted page snapshot, including deferred
Team updates during editing. Resource counts should refresh while another session
subpage is visible. Check exact workspace/session/incarnation and registered ownership;
bounded shared/nonblocking reads respect lifecycle fences and never initialize
records, wake/revive services, retry cleanup, write activity or reset inactivity.

Services shows label, lifecycle phase, observed unit state/time and bounded safe
diagnostics; running is not HTTP readiness. Unknown observations stay explicit.
Archived stop/removal evidence is historical, outside current counts, with no live
probing of retired unit names. Allowlist the public projection: no commands,
environment, credentials, raw helper output or logs. Cleanup failures identify the
registered service and pending operation, pointing to existing explicit lifecycle
recovery; reading never retries it. Existing unregistered services remain invisible
and uninspected. Defer preview links: no browser URL contract exists, and workspace
localhost is not automatically browser-reachable. No discovery, proxying, routing
or network exposure. Service Start/Restart/Stop/log streaming remain separate
choices. Lead owns final wording; no KB or site runtime change is indicated.

## Alternatives and implementation packages

A session target/slice with `PartOf` can group units, but it does not durably record
registered ownership, uncertain launches or verified shutdown before file removal.
It is unnecessary for the initial implementation. Name/path/port scans cannot
safely distinguish another session or a durable service. Manual cleanup reminders
leave the reported failure intact. A general resource-plugin framework or remote
server orchestration is outside this change.

Everything functional belongs to `dev-workspace`. No HaveAPI, codex-web,
vpsFree extension runtime or production configuration change is indicated.
Update generic session/launch instructions so agents use the supported launcher
for every preview/candidate. A short workspace procedure pointer may be useful;
do not duplicate the implementation in site code.

Proposed implementation boundaries, after user authorization:

| Package | Files and dependencies | Acceptance |
| --- | --- | --- |
| A: service owner and lifecycle integration, one implementer | New `libexec/workspace-session-services.rb`; `libexec/dev-session`; `libexec/workspace-archive-check.rb`; focused `test/dev_session/*` and service tests. Own CLI, registry, locking, stop proof, pre-prune integration and bounded public status projection. | No admitted launch can escape the durable inventory; all file deletion waits for verified complete cleanup; uncertainty remains recoverable; status reads have no lifecycle side effects. |
| B: compatibility, portal resources/counts, documentation and packaged fixtures, second implementer | `libexec/workspace-host`, `portal/internal/session/runtime-contract.json`, necessary Go lifecycle/status readers; `portal/internal/web/server.go`, `templates/session.html`, new service template, `static/app.js`, `static/coordination.js` and minimal existing stylesheet changes; cluster reader's presence-summary metadata in `portal/internal/cluster/status.go`; owning Nix package expression if needed, `nix/tests/session-archive-lifecycle.nix`, focused portal/host tests; `docs/dev-sessions.md`, `docs/session-archive-recovery.md`, `docs/workspace-portal.md`. Depends on A's frozen state/prelude and public reader contracts. | Selection/activation/refusal and old-format recovery agree; CLI/browser/worker expose the same blocker and resume the same operation. Resource/Team counts match their authoritative page snapshots; nested navigation preserves existing controls/links. Services rendering remains read-only, authenticated, session-bound and distinguishes historical from observed state. |

Lead serializes overlapping reader/test edits and Git operations. Package B's
fixture design and docs can proceed once the record and recovery interfaces are
settled; do not force parallel edits to the lifecycle owner. Exact file additions
are implementation decisions, not authorization to broaden scope.

## Verification brief

No runtime checks were run for this proposal. Later, use the repository's Nix
environment and disposable state; never point lifecycle tests at this workspace
or the supplied HaveAPI units.

Quick component checks should cover:

- Multiple previews/candidates, a fast-exiting launcher, ordinary grandchildren,
  another session's unit and a durable unrelated service; only owned resources stop.
- Lost launch replies, archive versus launch races, late jobs, reused names or
  InvocationIDs, missing/corrupt known registry and manager-unavailable failures.
- Graceful stop and ignored SIGTERM, bounded forced stop, residual cgroup members;
  assert tracking scripts/assets and worktree dependencies still exist on failure.
- Interruption before/after intent, launch, stop, unit unload, prune and main-journal
  handoff; exact retry, no duplicate launch, unchanged old journal policy.
- Old/new sessions without a registry continue ordinary archival; no service
  discovery/adoption occurs and unregistered fixtures remain untouched. Future
  registered launches in an old session receive the full cleanup guarantee.
- First-registration interruption, known registry loss, all registered candidates,
  revival without service restart, and unchanged automatic holds/eligibility.
- Compatible upgrade and refused rollback, candidate activation, waiting stale
  commands and pending old archive/delete/revival formats.
- Focused portal reader/template/browser fixtures: no-registry empty state,
  multiple registered candidates, stale/busy/unknown status, cleanup failure and
  archived evidence; safe text rendering, secret exclusion and session isolation.
  Verify mixed/zero/unknown resource indicators; stopped versus absent clusters and
  unavailable placeholders; active versus retired service records; distinct held
  machines versus waiting/released/repository-only claims and truncated history.
  Verify Team includes lead/nonremoved members in every retained state, excludes
  utilities/removed history, handles absent versus unreadable roster, and updates
  with its table. Check old child links, nested keyboard navigation, reload/back/
  forward, compact sidebar/accessibility, existing controls and hidden-page pause.
  Repeated count/status reads must not mutate state/inactivity or inspect
  unregistered/retired units; stale responses must not cross session incarnations.

After committed implementation, quick checks and mandatory independent review,
extend and run the existing `session-archive-lifecycle` NixOS VM check with real
systemd user units and cgroup descendants. Exercise CLI, browser worker, automatic
archive, delete and interrupted retry; prove all owned units/cgroups disappear
before the first artifact/worktree removal while unrelated fixtures stay running.
Run applicable host package-contract checks for compatibility. Use the required
verification watcher for long checks; stop on identity uncertainty, file deletion
before verified stop, unrelated-unit effects or timeout overruns. Deployment, if
later authorized, additionally requires a fresh disposable installed-package
archive/revive check. None of these proposed checks authorizes live cleanup now.


## Machine-identity execution contract

**LEAD ACCEPTED / A+B IMPLEMENTATION RELEASED — 2026-11-03.**
The full contract, active-binding drift clarification and local-input review /
publication choreography are accepted. A's complete runtime package is released
on `d187`; B's complete extension package is released on `e4e`. B's consuming
workspace package is also **released**: its four source paths are staged and quick-
checked, awaiting A's immutable runtime input. Implementation and verification remain
with their assigned owners; architect provides only requested seam support.
User: "roger that, so let's implement your proposal and include it in your work,
deploy it when done". Architect does not edit application code.
This is a separate feature/commit stream
from the three service commits and capacity correction. No default integration,
claim acquisition, deployment execution or session lifecycle action follows from
writing this contract. The rationale and rejected alternatives remain in
[machine-identity-proposal.md](machine-identity-proposal.md); this section supersedes
its illustrative request/format choices.

### Identity, display and request

One pure runtime-owned derivation, used by claims, conflicts, compatibility,
profile ownership and projections, consumes one of these exact structured values:

```json
{"kind":"repository","origin":"github.com/vpsfreecz/vpsfree-cz-configuration","name":"cz.vpsfree/machines/aitherdev"}
{"kind":"shared","id":"operator-chosen-stable-shared-label"}
```

`origin` is **only** the existing `RepositoryIdentity.identity`/`remote_identity`
result. Reuse its canonical direct SSH-origin checks, registered repository proof,
GitHub case and `.git` normalization. Never derive identity from a local registration
name, checkout/common Git directory, branch, commit, workspace or session. Those
remain source/admission evidence. A confctl result's exact configured `name` must
equal the requested exact selector. No glob, hostname, DNS/PTR, IP, SSH target or
physical identity inference. Names stay case-sensitive; no FQDN/IDNA branch.

If `metaConfig.labels` contains `dev-workspace.lock-id`, its value must be a string
and takes precedence. An absent label yields the repository tuple. Explicit null,
empty or malformed labels refuse rather than falling back. Name/selector and shared
ID: valid UTF-8, 1–256 bytes, no control characters or leading/trailing whitespace;
compare exact strings, never silently trim/case-fold. Origin retains its existing
validator. Shared IDs are configuration-owned, never supplied as a claim override.

Internal resource: `machine:logical:v1:HEX`, where HEX is SHA256 of the runtime's
canonical compact JSON for `["machine-identity",1,identity]`. Store structured fields
and derive this key; do not parse display delimiters. Human identifier uses **single
colons**: `machine:E(origin):E(name)` or `machine:shared:E(id)`. `E` preserves ASCII
letters/digits and `._~/-`, percent-encodes every other UTF-8 byte with uppercase hex
(including `%` and `:`). Thus the accepted ordinary example is exactly
`machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev`.
Display is not a claim input or parser authority. Duplicate resolved identities in
one request refuse; aliases in separate requests contend.

Keep schema-1 string requests unchanged. Add strict schema-2 requests with the same
five top-level fields and typed machines; `repositories` keeps its existing meaning:

```json
{"schema":2,"requestId":"11111111-1111-4111-8111-111111111111",
 "label":"Deploy configured target","repositories":[],
 "machines":[{"repository":"vpsfree-cz-configuration","selector":"cz.vpsfree/machines/aitherdev","adapter":"confctl"}]}
```

`repository` is a registered session repository, `adapter` an installed immutable
protocol-1 adapter ID; neither is executable input. Keep existing request bounds
(16 KiB, 512-byte label), UUID, owner, generation, suspension, capacity and fencing
checks. Missing/extra fields, unsupported adapter, ambiguous selector and malformed
metadata refuse without a claim. Use the existing `acquire`, `claim-status`,
`cancel-claim`, `release` CLI; no new launcher/worker or per-machine enrollment.

### Local resolver and source proof (A consumes, B implements)

Add protocol-1 operation `resolve-machine` to the existing immutable adapter:

```json
{"schema":1,"operation":"resolve-machine","selector":"cz.vpsfree/machines/aitherdev",
 "source":{"path":"/owned/canonical/repository.git","revision":"EXACT_40_HEX_COMMIT"}}
```

Strict success response:

```json
{"schema":1,"name":"cz.vpsfree/machines/aitherdev","sharedLockId":null}
```

Runtime supplies canonical source path and the committed head of the registered
feature branch, never a caller path. Missing branch/commit/flake refuses; no fallback
to master. The adapter reads that immutable Git revision. Do not create coordinator
checkouts, retained deployment artifacts or a source registry for this operation.
B uses a bounded projection of existing `confctl.machines` through `nix eval`,
selecting the exact attribute and returning only `name`/the optional label. Pinned
confctl already exports this data; do not invoke `MachineList.new` here because its
flake implementation builds `confctl.machinesJson`. Disable import-from-derivation,
lockfile writes and online fetching for resolution; missing local locked inputs
require ordinary input preparation before acquisition. No `nix build`, generation
build, copy, `inspect_machine`, SSH, credentials or target/native probe. Logical
resolution is independent of spin/carried-machine activation support; it does not
expand the retained executor's supported standalone-NixOS/no-reboot operations.

Use the existing bounded `Command` runner and private diagnostics. No full evaluated
metadata, environments or command output in claims/portal. Preserve all old adapter
operations/strict artifact formats. A/B share frozen response fixtures; duplicate,
missing, oversized, invalid UTF-8 or wrong-name results fail closed. An absent label
is represented as null in the response; B rejects a present null label first.

Resolve outside the ledger mutex under ordinary generation/session/preparation
admission. Extend the existing local proof with the selected branch/ref and commit
identity; recheck bounded local registration/Git/ref metadata under the existing
mutex before publishing. No external command or Nix evaluation under that mutex.
Use existing Git/ref proof conventions, including packed refs; a source move during
resolution refuses/retries before admission. Concurrent commit changes never become
part of the portable machine key.

### Durable claim and grant/revalidation boundaries (A)

Retain the existing `claims.json` path, atomic write and bounds. Read strict envelope
schema 1 and 2. Write schema 2 atomically only when first admitting a typed request;
copy existing records unchanged. New typed records retain all existing fields and
add `machineBindings`, in request order, each exactly:
`{repository,repositoryOrigin,selector,adapter,sourceRevision,identity}`. No new registry.
`repositoryOrigin` retains source provenance even when `identity.kind` is shared. `identity`
is the structured value above; `sourceRevision` records initial resolution evidence.
Derive primary resources/display from it and validate their consistency with the
saved resources. Schema-1 records have no added fields; legacy ledger, reservations,
job snapshots, attempts, receipts and their immutable payloads remain unchanged.

Exact request-ID retry returns its saved result **before** source resolution, even
after release or clone removal; changed input/owner refuses. It never rebinds.
Waiting grants re-resolve the current registered source outside the mutex and
recheck the local proof inside it. Compare the resolved canonical origin, exact
name, shared-label choice, adapter and resulting resource to the frozen binding;
identity/mapping drift leaves the request waiting, with the existing cancel-and-
reacquire recovery. A newer commit with the same logical mapping is allowed; the
initial source revision remains audit evidence and is not silently rewritten.
Routing/OS-hostname changes alone do not change this logical mapping.

**Fresh-acquire drift guard (lead clarification, 2026-11-03):** after the ordinary
saved-ID check and local proof recheck, but before inserting a fresh record, inspect
all existing `held`/`waiting` bindings under the same ledger mutex. Source pair is
exactly `(repositoryOrigin, selector)`; resolved `name == selector` is already
required. For every same-pair active binding, require both:

```text
old.adapter == incoming.adapter
policy_equivalent(resource(old.identity), resource(incoming.identity))
```

Otherwise refuse with code 3 without creating a claim, sequence or notification.
Apply across all owners, clones and registered workspaces in this coordinator,
including the same owner. Repeat at grant admission (excluding the record itself,
whose frozen-mapping check remains mandatory). Concurrent different resolutions
therefore cannot each publish a different lock. A mere changed label must not turn
an existing hold or waiter into an independently grantable new hash.

An explicitly approved/installed compatibility bridge may make the resources
equivalent; ordinary conflict/fairness then applies and the old record remains
unchanged. It never grants the requester another owner's hold. Adapter **ID** drift
still refuses while a same-pair binding is active; resource aliases do not certify
adapter replacement. A new executable/package implementing the same adapter ID and
protocol is not an ID change; ordinary candidate/source/mapping validation governs
it. After canceling old waiters or reconciling effects and releasing old holders,
terminal typed history does not block a fresh identity or adapter ID. It still
requires the schema-2 reader capability. Do not release merely to satisfy this guard.

For active schema-1 claims/legacy jobs/reservations, obtain the source pair and
adapter from their preserved catalog/retained target mapping, with existing strict
recovery validation. Do not synthesize machineBindings or infer physical identity.
A schema-2 resolution for a source pair still accepted by the legacy catalog must
also remain equivalent to that legacy alias, even with no active old record;
otherwise a later schema-1 acquire could bypass it. That case needs an explicit
bridge before the new shared label is admitted. Terminal records otherwise provide
no ownership. Different source pairs are not equated by this guard: intentional
cross-repository/name overlap still requires the configured shared ID/explicit
bridge, never a hostname comparison or inferred rename.

Held ownership does not follow a changed label/origin/selector. For ordinary
cooperative commands add read-only `coordination verify-machine SESSION --as-is
--id UUID --repository NAME --selector EXACT --json`: resolve current committed
metadata and require an exact owning held binding (the adapter comes from it),
including current generation/incarnation and no fence. Return bounded
`{schema:1,claimId,resource,identifier,sourceRevision}`; no grants, retries or state
writes. Run it once for the intended committed deployment batch, not before every
confctl command. Profile admission uses the same proof under its existing locks.
This is a local logical check; arbitrary commands remain cooperatively governed.
New source with unchanged identity may deploy under the same hold; actual build,
artifact/live-state/recovery checks remain the normal deployment workflow's job.

Error categories reuse existing exit codes: malformed/unsupported input 2;
changed local source/mapping 3; wrong owner/origin/admission 4; corrupt persisted
state, incompatible candidate or unresolved recovery 5; existing transient resource
wait 75 where applicable. Failures do not release, rewrite or retarget ownership.

### Legacy equivalence, profile mapping and package compatibility (A/B)

Keep the existing schema-1 `coordination.json` and legacy catalog entries intact
for first upgrade and retained operations. Its strict predecessor reader rejects
extra fields, so use one **immutable package policy**, not a mutable registry:
`share/dev-workspace/machine-identity-policy.json`, supplied by optional
`lib.mkPackage` argument `machineIdentityConfig` (generic and extension pass-through).
Strict shape: `{schema:1,profileTarget:identity-or-null,legacyAliases:[{resource,identity}]}`.
The resource is an exact previously supported `machine:...` key, never an address.
One resource cannot map to different identities. Several known aliases may map to
one identity. Reject cycles/ambiguous remappings; no guessed equivalence. Defaults
for an unchanged legacy configuration derive its existing catalog machine IDs and
profile target from configured repository remotes and exact selectors. New ordinary
machines never need entries here or in the catalog.

For this upgrade B supplies the default aitherdev repository tuple as profileTarget
and maps `machine:vpsfree:aitherdev` to it, retaining the old names/ID/aliases,
selector, repository and adapter in the legacy catalog for old/recovery readers.
Call that table compatibility-only in policy/docs; do not add future machines to
it. Normal profile-host configuration is one logical identity, not an all-machine
inventory. A shared profile target uses the exact same configured shared ID;
source resolution must agree. Current and candidate profile identities must remain
equivalent during a switch, even when the current package has only the old catalog.

Canonicalize machine resources through this policy **at conflict comparison**, in
both directions across new claims, old held/waiting claims, claimed/running/uncertain
jobs and unreleased legacy reservations. Do not rewrite saved keys/payloads or add
multiple reservation rows per alias. New grants, legacy grants and fairness must
use the same equivalence. Explicitly validate existing ownership before switching;
a discovered collision refuses and retains both original authorities for recovery.
Candidate compatibility preserves every bridge needed by retained ownership/recovery
or by legacy names it still accepts. Missing/changed mappings refuse; no release or
evidence deletion to make upgrade succeed. Ordinary status/counts project one
canonical machine per equivalence class and use the safe identifier/short name;
portal claims keep their existing string-array public projection, not typed objects.

Changing origin/name/override is a deliberate namespace change. Retain a stable
shared ID, or explicitly bridge exact old/new identities through this same finite
compatibility policy before using the new name. Initial installation of a shared
ID on a legacy target also needs its bridge before claims can use it. This rare
rename/intentional-overlap operation is distinct from adding a normal new machine.
No hostname scans, inferred rename or dynamic alias collector.

Add separate `share/dev-workspace/machine-claim-contract.json`:
`{schema:1,claimRecordSchemas:[1,2],machineIdentityVersion:1,resolverProtocol:1}`.
Keep existing claim/coordination/repository capability descriptors unchanged as
supported predecessor contracts, so an old selected host can admit the first new
candidate. The candidate repeats its own checks. Strict old readers cannot load
typed records, including terminal history: require the new capability whenever
schema-2 claim state exists, not merely while a claim is held. Never erase terminal
records or downgrade the envelope to evade this. A purely old/absent store does
not impose that new reader gate; its actual mappings/recovery must still survive.
An active dynamic profile/bridge not representable by a predecessor also refuses
that candidate. Capable candidates validate active identity/adapter/policy mappings;
malformed state refuses. Existing forward-only profile recovery remains unchanged.

First rollout uses the **old schema-1 aitherdev claim**: old selected host must read
the candidate's unchanged legacy catalog/contract, and the new candidate must
recognize that exact held key through the bridge. Preserve authorized system-first,
ordinary user-profile-switch-second ordering. Admit schema-2 requests only after
selection. No native identity upgrade, bootstrap bypass or new rollback workflow.
The coordinator remains global only within its existing shared per-user state root.
Intentional cross-repository overlap needs the same shared label in all configs;
accidental different logical identities are not detected, as the user accepted.

### Complete packages, dependencies and acceptance

| Owner/package | Files and dependency | Required outcome |
| --- | --- | --- |
| A: generic runtime | `libexec/workspace-coordination-claims.rb`, `workspace-coordination.rb`, `workspace-coordination-host.rb`; a small helper only if it keeps the one identity function shared; `nix/workspace-portal.nix`, `flake.nix`, focused coordination/admission/host fixtures and `docs/coordination{,-operations,-legacy}.md`. Any necessary `workspace-host` edit waits for A's current retry-review fix lane to finish. | Typed requests/reader/capability, source proof, shared derivation/conflict aliases, safe existing projections/counts, verify-machine and exact profile admission. No deployment executor expansion. Separate coherent machine-feature commit after the capacity fix. |
| B: extension | Fresh correctly registered `vpsfree-dev-workspace` checkout after lead's guidance/fetched-target check; `lib/workspace_confctl_adapter.rb`, `bin/workspace-confctl-adapter` if needed, `flake.nix` argument pass-through, `test/workspace_confctl_adapter_test.rb`, `docs/workspace-confctl.md`. | Exact resolve-machine protocol and metadata projection with no build/copy/probe. Independent from A after this interface freezes; retain original adapter behavior and artifacts. |
| B: consuming workspace, serialized after extension | Existing workspace feature checkout; package composition/config, `docs/coordination.md` and narrowly applicable deployment policy/selection checks. | One-time profile/legacy policy, catalog reclassified as compatibility-only, no new-machine catalog requirement. Preserve nested runtime override and all unrelated inputs. |
| Lead/integration package | Publication, final workspace runtime+extension selection, configuration channel pins and review/rollout receipts. | Pin actual published final source only, one final update per dependency stream; matching nested runtime and config channel through `check-dev-workspace-deployment`. System/profile deployment remains feature-only until separate default integration approval. |

A and B use identical protocol/key vectors before integration. Source-target
freshness/worktree registration and Git operations stay with the lead/implementers;
architect performed only source reads and design writes. No new repo `confctl`,
CMDB, mutable identity store, worker, dashboard or portal auth/protocol dependency.
The runtime owns lasting identity/recovery documentation; extension links its
resolver implementation to that contract; workspace owns the concrete legacy map.

**Source/review/publication order:** B quick-evaluates the consuming workspace's
new `machineIdentityConfig` against explicit exact local runtime and extension
input overrides, recording their committed heads and effective input paths. Do
not evaluate the new argument against the old published provider or write temporary
pin commits. A/B commit all substantive runtime, extension and workspace-policy
source; complete quick checks and mandatory review of that exact local composition
before publishing branches that trigger long CI. Then publish the reviewed final
provider heads and generate only the final runtime/extension/configuration pins.
Use the installed deployment verifier plus the existing strong source-NAR/full-input-
graph equivalence certificate to connect final published composition to reviewed
local inputs. A substantive graph/source difference returns to affected review;
publication is not proof of equivalence or default integration approval. Long checks
remain after review. B's adapter API and its independent package are unchanged.

Focused disposable cases: same target via two registered repository aliases,
SCP/SSH origin spelling, clones/worktrees/branches and workspaces contend; unrelated
repos with `vps` separate; exact shared labels contend cross-repo; duplicate OS names
with distinct configured names separate. Check percent/delimiter/Unicode vectors,
malformed labels, unsafe/mismatched origins, absent exact selectors, no default-
branch fallback, changed ref during resolution, waiting metadata drift, same-key
new commits and released retry with missing clone. Add fresh-acquire races where
the same source pair changes absent→shared, shared→different-shared or shared→absent
while the prior binding is held or waiting: refuse before inserting new state.
Cover both owners and same-owner acquisition, adapter-ID change with unchanged key,
and a compatible same-ID adapter package update. An explicit bridge produces normal
contention, never parallel ownership. Cancel/release to terminal state, then prove
a fresh typed request with changed identity is allowed when no accepted legacy alias
or other active binding conflicts; retained history still rejects incapable packages.
Cover the legacy accepted-alias rule with and without an active legacy hold, and
source-pair distinction without physical/name guessing. Prove held/waiting/legacy job
and reservation conflicts in both directions, fairness, unchanged stored old payloads,
profile ownership through the old key, candidate bridge loss/collision refusal,
schema-1 admission into the new package and schema-2 terminal-history forward gate.
Status/Resources counts must deduplicate aliases and remain read-only.

Runtime quick commands in its declared Nix environment: focused
`ruby test/coordination_claims_test.rb`, `ruby test/coordination_admission_test.rb`
and affected `test/workspace_host_test.rb` cases; add existing coordination/recovery
cases touched by conflict normalization. Use `nix develop --command ...`, and the
existing `test/run_ruby_suite.rb` batch/shard runner when broader coverage is needed.
Extension: run `ruby test/workspace_confctl_adapter_test.rb` with its pinned Nix
Ruby/test dependencies (derive shell/check invocation from the refreshed flake).
Assert the resolver never invokes build/copy/inspect/SSH and the ledger mutex is
not held during evaluation. Add a disposable flake with the real confctl output
shape to verify local evaluation and source pinning without a machine.

After complete commits/quick checks and mandatory review: run affected exported
runtime Ruby shards, extension packaged Ruby checks and host package-contract check;
reuse existing disposable coordinator/profile fixtures for old→new activation,
interruption and forward recovery. Preserve original session creation/collection,
service/capacity and installed-candidate verification requirements for the combined
release; no new live-machine/native-identity campaign. Long batches use the existing
watcher policy. Build/copy before machine ownership; verify system and profile with
the original rollout procedures. Keep uncertain effects held, release only after
verified deployment and complete approved integrated lineage, and never infer
integration or lifecycle permission. No tests/builds/live probes were run by architect.

Source anchors: selected `0q7rc75dh4mjrxpb37m1hchfwcbmpa7a` guides; runtime source
`workspace-coordination-claims.rb` request/record validation, `acquire_claim`,
`tick_claims_ready`, `profile_claim!`; `workspace-coordination.rb:117–125,672–891`
and portal projection at `:1565–1610`; `workspace-coordination-host.rb:484–516`;
`nix/workspace-portal.nix:173–193` strict catalog. Extension baseline
`e4e7e95ed39bf514b33f8f8ae61ba9868de060ae` adapter/docs. Confctl
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`,
`nix/flake/mk-confctl-outputs.nix:171–228,505–515` exposes machines with names/meta;
`lib/confctl/nix_flake.rb:28–30` builds machinesJson, which the new resolver avoids.
Current selected instructions/retained roster were reread; saved settings unchanged.


## Staged post-review verification commands

**PLAN / NOT EXECUTED — 2026-11-03; lead accepted the selection.** This supplements
the existing rollout, without changing its current status or deployment gates.
A owns the released native fixture addition below as intended source before final
substantive machine review. Finish runtime/extension/workspace-policy commits,
quick checks and that review before these long batches or CI-triggering publication.
Keep downstream final pins and expensive site application/system/installed-driver
preparation held until the exact runtime checks below pass. Use a fresh authorized
verification watcher; no tests, builds or connections were performed by architect.

Set task variables from final reviewed commit receipts, not the presently mutable
worktree heads. `SESSION_RUNTIME_SOURCE` and `SESSION_EXTENSION_SOURCE` are this
session's existing checkouts; `SESSION_RUNTIME_REV` and `SESSION_EXTENSION_REV` are
full committed reviewed SHAs. The following local references do not update locks:

```sh
export SESSION_RUNTIME_SOURCE SESSION_EXTENSION_SOURCE SESSION_RUNTIME_REV SESSION_EXTENSION_REV SESSION_VERIFY_OUT
export SESSION_RUNTIME_REF="git+file://$SESSION_RUNTIME_SOURCE?rev=$SESSION_RUNTIME_REV"
export SESSION_EXTENSION_REF="git+file://$SESSION_EXTENSION_SOURCE?rev=$SESSION_EXTENSION_REV"
```

For Go source tests, use the runtime checkout only while its HEAD and clean source
match SESSION_RUNTIME_REV. Record exit status, exact inputs and bounded logs in the
existing verification/rollout receipts. SESSION_VERIFY_OUT is a fresh session-owned
output directory allocated by the executing owner; its absent-providers.json must
not exist. Never use production sockets, credentials, workspace state or settings.

### 1. Two existing optional Playwright consumers

A normal package pass skips these consumers. Their `.cjs` programs depend on the
Go-created HTTP/TLS fixtures; do not invoke Node alone. Use the runtime's pinned
Nixpkgs, Go/Node/Git and `playwright-test` module tree, not only `playwright-driver`
(which is playwright-core). Chromium runs from the matching browser tree. This
transient shell expression is dependency selection, not a new test harness:

```sh
nix develop --impure --expr '
  let f = builtins.getFlake (builtins.getEnv "SESSION_RUNTIME_REF");
      p = import f.inputs.nixpkgs { system = "x86_64-linux"; };
  in p.mkShell {
    inputsFrom = [ f.devShells.x86_64-linux.default ];
    NODE_PATH = "${p.playwright-test}/lib/node_modules";
    PLAYWRIGHT_BROWSERS_PATH = "${p.playwright-driver.browsers-chromium}";
  }' --command bash -c '
  set -euo pipefail
  cd "$SESSION_RUNTIME_SOURCE"
  test "$(git rev-parse HEAD)" = "$SESSION_RUNTIME_REV"
  test ! -e "$SESSION_VERIFY_OUT/absent-providers.json"
  export PORTAL_BROWSER_TEST=1
  export DEV_WORKSPACES_CODEX_PROVIDERS="$SESSION_VERIFY_OUT/absent-providers.json"
  export PORTAL_RETRY_BACKEND_OUTPUT="$SESSION_VERIFY_OUT/retry-backend"
  export PORTAL_RETRY_SCREENSHOTS="$SESSION_VERIFY_OUT/retry-activity"
  go -C portal test -mod=readonly -count=1 -timeout 12m \
    -run "^TestRetryBackendBrowser$" -v ./internal/web
  go -C portal test -mod=readonly -count=1 -timeout 5m \
    -run "^TestQuestionBrowser$/^retry_activity_browser_test[.]cjs$" -v ./internal/web
'
```

Require four backend subtests (desktop/mobile × root/member), the backend's complete
32-case manifest, and the activity subtest's desktop/mobile evidence. Backend uses
the real runtime retry HTTP/state implementation with a synthetic native transport;
activity is presentation coverage. Neither is the native API proof below. Fixture
TLS bypass is confined to generated local test servers; it is not a live-browser
recipe. The pinned playwright-test wrapper itself references its declared browser
closure; allow ordinary Nix realization, no npm/browser downloads or new install.
Expected warm execution 3–8 minutes plus missing dependency realization; per-backend
case already has an 80-second context. Any missing dependency, selected-test skip,
failed assertion or incomplete manifest fails this batch; preserve diagnostics.

### 2. Runtime package and existing native VMs

One batch (or the exact corresponding CI jobs) covers the combined release:

```sh
nix build --no-link --print-build-logs \
  "$SESSION_RUNTIME_REF#checks.x86_64-linux.package" \
  "$SESSION_RUNTIME_REF#checks.x86_64-linux.host-package-contract" \
  "$SESSION_RUNTIME_REF#checks.x86_64-linux.session-creation" \
  "$SESSION_RUNTIME_REF#checks.x86_64-linux.session-archive-lifecycle"
```

`package` already depends on the complete unique Ruby-shard aggregate and runs
Go/Node checks. Confirm A's new coordination/profile tests belong to that aggregate;
do not run another full Ruby campaign after the same derivations pass. Host contract
checks packaging; existing Ruby admission/profile fixtures prove logical claim,
legacy bridge, capability and interruption decisions. These are not remote-machine
identity checks. Archive VM supplies actual systemd launch/descendant/fast-exit and
archive/delete/revival proof, including the previously failing native scenarios.
Creation VM preserves creation/native/settings continuity and adds the next four
assertions. Both need KVM. Expected warm package 8–15 minutes; each existing VM
roughly 5–20 minutes after dependencies. These are planning bounds, not guaranteed
measurements. On material overrun request one phase checkpoint; stop/escalate on a
real failed assertion, live/unowned target, unintended kernel build or escaped
fixture mutation. No automatic retry of failed native checks without diagnosis.

**Released missing regression, A-owned:** current `test/creation_transport.py`
only initializes then reads thread/list or thread/read; no existing invocation
proves ascending thread/items/list. Add a small lasting proof mode there and one
case in `nix/tests/session-creation.nix`; extend the existing browser helper only
as needed for ordinary managed input. Reuse `test/creation_model.py`'s hold-turn
boundary, actual pinned Codex 0.165.0 and pinned codex-web d3a29bee90ef client.
Do not repurpose historical `archive_acceptance.py` or create another harness.

1. With a few ordinary accepted managed inputs in one active turn, assert the
   real response to `{threadId,turnId,sortDirection:"asc",limit:64}` has the exact
   turn/item/user-ID/clientId/content shape the reader consumes. This closes the
   synthetic-DTO versus pinned-native shape/filter gap.
2. Page that same small turn with limit 1 or 2 and nextCursor; its chronological
   IDs must equal the complete read, with no duplicate/omitted IDs or other-turn
   items. This proves native order/filter/cursor semantics without a volume campaign.
3. Append one accepted managed steer at the active tail and replay the saved last
   page/cursor. Old prefix must remain stable and new input appear exactly once,
   including the exhausted-tail boundary used by the reader's page rewind.
4. Wait for real nonempty persisted managedTurn authority, restart only the
   disposable portal with existing `restart()`, then observe/append a managed input.
   The actual wrapper must replay the saved prefix and extend its count/digest
   once, with no Handled/duplicate continuation. Reconnecting a transport alone
   does not prove loss/reconstruction of the Go reader's process-local hints.

Three/four managed inputs suffice; existing synthetic 205-small/65-large/261-page
cases retain their separate volume/recovery role. Do not manufacture retry records
or native history. Unhold inference and preserve ordinary settings/unique-send
assertions. This regression is intended source, **not yet claimed as implemented
or passing**; it must be included in A's source/history and final review packet.

### 3. Extension and composed-package checks, then final preparation

After runtime acceptance, use the exact reviewed local runtime override until
published final pins exist; do not mutate the extension's lock just for testing:

```sh
nix build --no-link --print-build-logs --no-write-lock-file \
  --override-input dev-workspace "$SESSION_RUNTIME_REF" \
  "$SESSION_EXTENSION_REF#checks.x86_64-linux.tests" \
  "$SESSION_EXTENSION_REF#checks.x86_64-linux.organization-source" \
  "$SESSION_EXTENSION_REF#checks.x86_64-linux.rejects-invalid-site-config"
```

The declared `tests` runs adapter regression and the real offline immutable-flake
resolution case plus normal migration Ruby checks. Flake evaluation asserts the
host-path contract. Expected 2–10 minutes warm; stop at first actual failure and
preserve its exact source/dependency receipt. These checks exercise local metadata,
not target deployment. After pure final published pins and their installed verifier /
source-NAR/full-input-graph certificate, run the existing extension `package` and
`package-metadata` checks with that same effective runtime, and the prepared site
package/checker already required by rollout:

```sh
nix build --no-link --print-build-logs --no-write-lock-file \
  --override-input dev-workspace "$SESSION_RUNTIME_REF" \
  "$SESSION_EXTENSION_REF#checks.x86_64-linux.package" \
  "$SESSION_EXTENSION_REF#checks.x86_64-linux.package-metadata"
```

Bind these exact local refs to final published NAR/input identities first. Package
wrapping cannot be certified by adapter unit tests alone. Then prepare final system/site artifacts and the
installed-package VM driver outside ownership, following the existing commands in
rollout and this design's installed-fixture section. No old EE3 artifact certifies
the new combined source merely because its output previously existed.

**No extension host-migration VM for this boundary.** Current extension diff is
adapter/test/docs/flake pass-through; generic `nix/host-module.nix`, host paths and
runtime-authority corpus are unchanged. The extension VM moves/reconciles/reverses
host namespace password/auth/PKI/TLS/router paths; new retry/service/claim records
do not alter that contract. Retain ordinary migration Ruby and host-path/package
metadata checks. Reconsider only if final reviewed diff changes that actual host
migration boundary. Similarly, unchanged substrate idempotency is not proof of
profile claim compatibility: the affected profile cases are in the package's Ruby
fixtures. Do not add a blanket host-migration/namespace campaign for dependency churn.

Reuse earlier successes only with the required unchanged tested source, complete
inputs and exported derivation/output receipts (including aggregate shard coverage);
Git/tree equality alone is insufficient. Local and CI execution of the same required
check need not be duplicated when exact evidence is available. The selected installed
site package still needs the already planned disposable verification after authorized
system/profile switch, plus bounded Resources/Team usability/health evidence. No
real-session lifecycle action, foreign service cleanup or new machine probe is added.

Anchors: runtime `flake.nix:93–130`, `nix/workspace-portal.nix:310–343`,
`portal/internal/web/retry_backend_browser_test.go:1196–1262`,
`question_browser_test.go:124–129,270–294`, `turn_retry_reader.go:178–216`,
`test/creation_transport.py`, `test/creation_model.py`, creation VM `:167–194`;
pinned nixpkgs `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`
`pkgs/development/web/playwright/driver.nix` installs @playwright/test and browsers;
extension `flake.nix:38–39,318–323,425–474`, `nix/tests/host-migration.nix` and AGENTS.


## Fresh deletion recovery-location validation order

**SOURCE-VALIDATED BOUNDED FIX BRIEF — 2026-11-03; implementation owned by A.**
Inspected clean runtime `ad0770a8ce6bb3b70645dc196386106a049072e8` (activity
fixture fixup over published 5f7). Lead/A report CI Check41691994729 stopped
before either VM: the two existing bad-recovery-root tests now encounter M1's
strict coordinator ENOTDIR before the intended DevSession location diagnostic.
Keep M1 unchanged: only ENOENT proves absence; no rescue-to-empty or relaxed test.

Inside `Runner#delete_with_access`'s existing creation then exclusive slug locks,
immediately **after** `reject_conflicting_lifecycle_journal!` and **before**
`coordination_store.require_lifecycle_idle!`, use this bounded fresh-only preflight:

```ruby
unless path_exists?(lifecycle_journal_file(slug, 'delete'))
  tracking = validate_removal_tracking!(slug)
  validate_removal_recovery_location!(slug, tracking)
end
```

The ordinary removal-journal path is the predicate, not `@lifecycle_access[:journal]`
(which can identify only a services prelude), journal contents, or a new loader.
`path_exists?` uses lstat and rescues only ENOENT; present invalid/symlink journals
are never treated as fresh. Keep the existing strict loaders and their refusals.
Do not add an early `load_removal_journal`: it validates recovery via
`removal_recovery_root`, which can mkdir/chmod. Its existing calls, including in
`failed_creation_start_context`, remain in their current order.

`validate_removal_tracking!` chooses exactly one active/archive root and only
checks it (`ensure_directory!(..., create: false)`). Passing `work_dir` alone
would miss archived tracking. The location validator only derives/reads paths
and invokes the existing cluster `cleanup-paths` inventory contract; it does not
reset clusters or touch services. Ordinary lock/journal-directory setup already
precedes this point; this is not a claim that command entry writes no lock files.
The new preflight adds no recovery directory, journal publication, coordinator
write, retirement, stop or deletion before invalid-location refusal. The path
helper's ensure-directory calls find the journal root already established by the
existing access/conflict path. Preserve missing-prelude fast refusal and every
conflict guard ahead of this new check.

Retained ordinary deletion journals bypass the new preflight, including retries
after tracking has moved to private recovery. Preserve coordinator idle/capacity
ordering, exact operation/force recovery (including the existing force upgrade),
`prepare_removal!` publication and its later tracking/location validation without
moving or removing any of them. No format, capability, migration or recovery
policy changes; this restores validation precedence for fresh invalid locations.

A's focused acceptance: retain the exact Error class/message and untouched
creation/tracking assertions in `deletion_recovery_test`'s two failing cases
(:343/:373), plus the existing nested tracking/worktree/cluster cases. Add one
archived-tracking nested-root case and prove invalid location reaches neither
coordinator admission nor removal publication; preserve bytes and absence of new
recovery data. Exercise retained-journal retry after tracking move, original
operation/force checks, services-prelude-only versus ordinary-journal freshness,
invalid/conflicting prelude refusal, and unreadable coordinator state with a valid
location. Use existing fixtures; no new lifecycle harness.

Suggested focused commands in the repository Nix shell: `ruby test/dev_session/deletion_recovery_test.rb`, `ruby test/dev_session/deletion_safety_test.rb`, `ruby test/dev_session/lifecycle_access_test.rb`, `ruby test/dev_session/session_services_test.rb`, and `ruby test/machine_identity_test.rb --name '/retained_file|genuine_absence/'`.
Add `deletion_lifecycle_test`'s archived-session and retained-journal retry cases
as needed for that file's assertions. Use the normal watcher for any batch of
uncertain duration. These commands are planned, not run by architect.

After A commits the exact core delta and focused checks pass, lead uses the same
reviewer for affected general/risk lanes. No repeat whole-machine design review
or new native scenario is required by this ordering correction. Existing exact
runtime package/archive/creation acceptance remains required before downstream
pins or deployment; earlier pre-VM failures prove no native success. No actual
session deletion, service action or deployment is authorized by this brief.

Source anchors at ad0770a8: `libexec/dev-session:2489–2504,6216–6242,6484–6533,
6535–6553,6554–6600,6601–6699,7233–7244,7459–7465,8314–8331,8432–8438`;
`libexec/workspace-coordination.rb:158–176`; existing recovery/safety/services
fixtures cited above. The selected session/environment and retained
Astra/xhigh/workspace_write roster match; settings unchanged.


## Confirmation fixture ambient-runtime incident: static effect bound

**STATIC FINDING / FIXTURE BRIEF — 2026-11-03.** Architect ran no test, live
request, thread inventory, service action or cleanup. Current identity/env match;
retained settings unchanged. Keep the accepted four-line production preflight
unchanged. The follow-up changes only the affected fixture's native boundary,
with lead acceptance before A resumes implementation/verification.

Evidence separates two executions. `deletion-preflight-quick/manifest.json`
binds HEAD ad0770a8 and staged tree c681b7bfb11e25540e2d476c5c67d30df164f819;
`run.sh` selects the existing five-file component batch through dev_session_test.
`launcher-result.txt` records 18:45:28–18:46:20 UTC, exit 1; `related.log` has
111 tests / 1214 assertions, one confirmation-test failure. Its CLI stderr was
captured in StringIO and not printed: the first invocation's exact native-helper
argv/error/guard branch are **not retained**. The later reproduction is not proof
of the first branch or proof that the first made no native call.

`deletion-preflight-cli-diagnostic.log` records the second, bounded diagnostic:
19:48:13 (log clock), 1 test / 5 assertions / exit 1. Its accepted-confirmation
path invokes installed `0q7.../bin/workspace-portal thread retire` with `--cwd`
under its disposable work/demo, `--workspace` that disposable root,
`--user-state-root` its .xdg-state/dev-workspaces, and **the inherited live socket**
`/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock`; no --thread-id or --force.
It reports `delivery stage=submission-transaction ... failed=true` then
`find session conversation: submission fence exists without its migration journal`.
The rejected-confirmation path returns before this invocation.

Provenance: selected package
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`, deriver
`2jvhgyq2ilxa4cprlswc7fwh93b3snpx-dev-workspace-0.2.0.drv`, env.src
`/nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source`. Its Go-modules deriver
postPatch checks codex-web d3a29bee90ef00a08816920408c596152339a637. Installed
`share/workspace-portal/codex/{client,submission_database,submission_migration}.go`
match those exact Git objects by SHA256. This uses retained immutable source,
not a contemporary branch or an experiment against the selected manager.

For the **second invocation**, main.go:55–86 derives disposable JSON/SQLite
paths from the socket hash but keeps socket+.submission-attempts-v3.json as the
legacy import path. Codex constructor client.go:923–970 allocates state only;
Ensure/dial begins at :973. Runtime client.go:584–600 first calls
ThreadOperationAttempt for the empty thread ID, before target discovery.
Codex client.go:3363–3371 enters submissionTransaction; database.go:58–105 opens
the database before running its operation callback. Migration.go:115–191 sees
schema-4 predecessor fence with no corresponding disposable migration journal
and returns the exact diagnostic. Therefore this recorded invocation reaches no
native connection, initialization RPC, target resolution, retirement operation
record, interrupt, archive or continuation. No import or fence/ledger rewrite is
reached on that branch. The later native retirement stages are not involved.

This is **not zero filesystem interaction**. Database.go:114–154 can create the
disposable submissions directory/SQLite file, WAL/schema before refusal.
Migration.go:86–113 mkdir/checks predecessor parents, opens O_CREAT|O_RDWR .lock
files and flocks them, including the live-adjacent legacy .lock, then reads the
legacy fence. Historical lock preexistence is unavailable; possible creation of
that empty lock is the bounded live metadata effect, plus read/access metadata.
No lock contents are written. Deferred release closes both predecessor descriptors;
the database error branch closes SQLite; threadCommand's deferred Client.Close
runs before main exits 1. Successful process termination leaves no held process
locks. Do not remove the live lock or edit the fence. The disposable Ruby removal
journal had reached thread_retiring; its recovery data and possible SQLite files
were within the test root. Existing Dir.mktmpdir block cleanup removed the root;
there is no retained DB specimen to assert its exact contents. First-invocation
branch uncertainty remains as above; current conversation activity is not evidence
about historical effects on any other thread.

Minimal fixture correction: both CLI instances must use an explicit fixture-only
environment, with no ENV.to_h merge. Existing CLI#runner/runner_for seam can supply
NullTmux and temporary state; use an absolute controlled local portal stub and an
absent socket below the disposable root if exercising retirement. Assert the
stub's cwd/workspace/state/socket arguments and reject unexpected operations;
never delegate to installed workspace-portal or a native client. Negative answer
must leave tracking and call log untouched; positive answer invokes the controlled
retirement at thread_retiring while tracking still exists, then completes ordinary
fixture removal. Existing retirement/recovery tests keep their native-order role.
An XDG-only environment does prevent lookup here (executable_in_path returns nil
for absent PATH, and no socket is selected), but by itself skips the retirement
branch; do not describe that as proving the native-boundary/order assertion.
No ambient-environment framework, production permission relaxation, M1 change,
fence bypass, replay or new native campaign. A owns the narrowly scoped fixture
change; same committed affected general/risk review covers it with the preflight.
Lead decides resumption with the explicit first-invocation evidence limit retained.

Evidence SHA256 (session-relative paths):
- diagnostic log: 75f483388f20e74dddef50053bdc9dae32e0849f2efc8e4afb73f2d4d6d0e87c
- quick/related.log: bcb42cf717200f1b0bccee81dda520a6531e8d14e141229bed4bb1cb59d92682
- quick/manifest.json: 053360a29743a5327894abd13794caf25001c98ba3128cf8ce7a13eb5e5c9637
- quick/launcher-result.txt: 2e256c75bae69dc88ab0a15a4943c56534ddc953230ae745367e6d3f8186d755
- quick/run.sh: 76705c32f77657ca244233a5e463497f84a0fc6d32cba4231b5cda50441d7d53
Here quick/ means deletion-preflight-quick/. Installed codex file hashes:
client.go 4d1fb7cbd53a9212653b38d1523daabdea5e6eae195a912c07d1323c605f7e57;
submission_database.go ad843c381092767d0bacdeca66ce29f0a3fa98641e0f02f8f0fc1cad62c0f1db;
submission_migration.go 2ac424fffdd09ec39c919221cf8eb9dd428046c4ee80b615776283ef444cdbe8.


## Lifecycle cancellation clears dependent compact turn authority

**BOUNDED SOURCE-VALIDATED FIX BRIEF — 2026-11-03; A owns implementation after
lead acceptance.** Baseline clean runtime
`1e138a552c1cc355d0b05a9d47a25d8e391aa85c`. Retained raw archive evidence:
`runtime-postreview-1e138a55/archive-job-126162806656.raw.log`, SHA256
`7ae4e2891a42ee29a8b4d25fd481834ae442e21afe87f2ddb9ad4a073ac7cfaa`.
Lines 4537–4538 show the disposable VM's installed 6625... package failing
`recovery --operation cancel-retries` with `managed turn authority is invalid`
during the held-turn archive/restart fixture. The preceding poll assertions are
not the producer failure. No live operation or new check was run for this brief.

At `portal/internal/turnretry/store.go:332–383`, CancelSession calls
`State.Cancel("lifecycle")`, clears Binding, reconciles uncertain delivery when
possible, then saves. Its new compact ManagedTurn still refers to that binding.
The validator at `managed_turn.go:40–49` correctly refuses this inconsistent
pair. Minimal production delta: add **`t.State.ManagedTurn = nil` immediately
alongside `t.State.Binding = nil`**, inside the same existing per-thread admission
lock, before existing uncertain reconciliation and the existing single Save.
No new helper, record field, schema/capability or migration. Keep generic
`State.Cancel` unchanged: ordinary managed input also uses cancellation without
revoking the loaded binding. Do not call InvalidateSettings (which advances epoch)
or weaken validation to accept compact authority without its binding.

This boundary discards eligibility authority, not submission recovery evidence.
Keep Pending.ID/action/failure/immutable snapshot/result, all source snapshots,
quota UUIDs/charges, epoch, preferences, enrollment and failure watermarks under
their original rules. The additional assignment changes none of them. Existing
Cancel may clear a non-uncertain Pending or consume its accepted ResultTurn;
existing Accepted reconciliation may add result evidence, update Handled and
anchor an accepted charge. Preserve those semantics exactly, not a new reset.

For an uncertain submitting/reconciling tuple, cancellation retains the tuple and
Cancelled=true. Reconcile an exact accepted receipt with existing Accepted logic;
positive NeverSubmitted may clear Pending; unknown/error/no backend leaves the
original tuple uncertain and returns the existing lifecycle blocker **after
saving cancellation**. Neither path sends a continuation, creates a UUID, resumes
work or restores Binding/ManagedTurn. Pending's self-contained immutable snapshot
validates independently of the current binding. Repeated cancellation/restart can
settle that same receipt without duplicate execution or quota charging.

The existing Save validates before creating/replacing its file, then fsyncs and
atomically renames one complete record (`store.go:283–327`). Persist cancellation,
Binding=nil and ManagedTurn=nil together; never save an intermediate unbound
compact record. The observed validation failure therefore did not persist that
invalid pair. A later I/O failure propagates unchanged; recovery reloads the
complete old/new record under existing locks, retaining exact uncertain receipt
handling. There is no all-session transaction: already saved members remain
cancelled if another member fails, and retry is idempotent. Corrupt retained
records continue to refuse on load; do not invent a repair reader. Old schema-1
records without compact proof follow their existing ordinary save/upgrade path.
Process-local reader hints cannot restore authority: their key includes both
Binding and ManagedTurn, and no implicit rebind is added on archive/revival.

A's package is the one production assignment in `store.go` plus existing
turnretry fixture regressions (prefer `state_test.go`'s
TestLifecycleCancellationPreservesUncertainIdentityAndCancelsOtherThreads and
`managed_turn_test.go`'s managedState/managedAdmission helpers). Add compact proof
through the actual fold helper, save it, then call the Store API; do not only test
an in-memory Cancel method. Focused acceptance:

- Bound compact proof with no Pending and with scheduled work: cancellation
  succeeds; reload validates with both authority fields absent, cancelled/deadline
  behavior intact, and no unrelated epoch/quota/Handled/snapshot change.
- Compact proof plus uncertain Pending: no backend or unknown/error outcome
  returns the original blocker while saving a valid cancelled record; UUID,
  immutable snapshot and charge remain exact. Other retained members still cancel.
- Restart from that record, then exact accepted receipt or positive NeverSubmitted:
  existing settlement succeeds, no fresh Continue call, UUID replacement, duplicate
  charge or authority resurrection. Repeat cancellation remains safe.
- Strict validator still rejects a fabricated ManagedTurn with nil/mismatched
  Binding. A failed pre-publication save leaves valid original bytes; any existing
  atomic-write failure seam may be reused without a new fault framework.

Run focused turnretry lifecycle/managed/recovery tests in the declared Nix shell,
then its ordinary package tests once relevant inputs change. Example narrow
selection: `go -C portal test -mod=readonly -count=1 -run 'LifecycleCancellation|ManagedTurn|Recovery' ./internal/turnretry` (keep this
as one shell command). The actual existing archive VM remains the native
acceptance after committed affected review; no new VM scenario/campaign is needed.
Keep the existing watcher on unchanged fast/creation work. Publication, final pins
and deployment remain lead-controlled and gated by exact reviewed/check results.

Other exact anchors: `state.go:163–187,374–428` (Cancel/settings/Accepted),
`controller.go:100–137` (receipt-only cancelled reconciliation),
`cmd/workspace-portal/recovery.go:32–53` (lifecycle bridge),
`codex_provider_scoped.go:183` (same Store consumer),
`workspacecodex/turn_retry_reader.go:37–40` (hint key). No changes to those
interfaces, original recovery, service cleanup, M1, or the earlier fixture fix.


## Native creation prefix stall: bounded diagnostic contract

**DIAGNOSIS BRIEF / NO PRODUCTION FIX SELECTED — 2026-11-03.** Exact failed
source `1e138a552c1cc355d0b05a9d47a25d8e391aa85c`, run 41706416665 attempt 1,
creation job 126162807114. Raw session evidence
`runtime-postreview-1e138a55/creation-job-126162807114.raw.log`, SHA256
`cdaefb2d77519a9a21f35c76af266f1d995439f4f170d9fbbf2947878691ca46`, independently
matched. Local a5d47d22 only changes cancellation owner/tests, not this fixture or
reader. A's saved exported-artifacts inventory reports zero artifacts; do not
assume the old CI runner filesystem or copied guest output remains retrievable.

At raw lines 4510–4527 the fixture has accepted a normal managed send and steer
for expected turn `01a1a2f9-7982-7893-b241-8b1033bae1f7`, then the first
prefix_proof guard fails `managedTurn.turn == expected && managedTurn.count == 2`.
The two input UUIDs are `30af32bc-927e-46b9-a657-e7b4ee0f2628` and
`b98f8f3e-a001-4125-b764-28a23566c23c`. Receipt consistency assertions passed by
execution order; their raw bodies and native item IDs were not printed. State,
managedTurn, turn and count are readable at the shown failures, but their actual
values are absent. Timeout is 900.09 seconds. Do not infer count=1, a wrong turn,
malformed native response or missing binding from this evidence.

`nix/tests/session-creation.nix:203–212` invokes items-proof only after that
state guard. Therefore asc shape, tiny-page order/cursor, appended tail and actual
portal-process restart assertions were **not reached**. The generic unavailable
retry log (`portal/internal/web/turn_retry.go:136`) omits the underlying exception.
`creation_model.py:99–103` holds inference; the subtest finally releases hold-turn
before the top-level exception diagnostics. Those diagnostics print naming/model
and creation checkpoints, not the failed compact tuple. A failure snapshot must
be taken inside prefix_proof while the same hold is still present.

Source allows several distinct paths, none established as this failure's cause:
post-receipt AdvanceProof errors are optional/ignored (`turn_retry.go:371–376`);
active scheduler proof errors return without consuming the active turn
(`turnretry/controller.go:229–244`); the reader checks binding/epoch/socket/policy,
provider, exact metadata, native response shape, prefix and remaining snapshots
(`turn_retry_reader.go:78–99,118–275`). An accepted steer alone does not establish
that its native history item has been folded. Preserve all those checks.

**Smallest next source package, A-owned after lead acceptance:** extend only the
existing creation VM and `test/creation_transport.py`, reusing their initialize/
read-only RPC connection; no production telemetry or new harness. First use any
already retained exact-run artifact, but the inventory currently provides no
actual tuple. Add a bounded prefix-diagnostic mode/projection independent of
compact-state readiness; do not make the existing items-proof pass early.

- Emit one initial guard-mismatch summary and one final failure summary, not a
  full record or every-poll dump. Preserve the original predicates and timeout.
  Keep diagnostic collection before the subtest finally removes hold-turn.
- State projection: expected thread/turn/count and accepted client IDs/text hashes;
  actual schema/epoch/phase/reason/handled/cancelled, Binding presence/epoch/digest,
  ManagedTurn presence/turn/count/lastUserItemId/digest/bindingDigest, Pending
  presence/ID/resultTurn, and bounded snapshot ID/turn/origin/epoch/proven/
  textDigest/bindingDigest. Include file-read/error category and observation time.
  No options, context, instructions, prompt text, environment, credentials or
  entire retry JSON. Retain private data only under existing fixture ownership.
- On the same disposable guest thread/socket, use existing read transport for
  native thread/read and **one** `thread/items/list` request with the production
  `{threadId,turnId,sortDirection:"asc",limit:64}`. Project actual turn IDs/status
  and response envelope/key/type presence, up to 64 entry turn/item/client IDs,
  content kinds and text SHA256/length. Report nextCursor type/presence/length/hash,
  not opaque contents. Record RPC stage/error code/type without raw error payload.
  Observe shape before asserting it so a malformed response leaves useful evidence.
- Bound diagnostics with an explicit short timeout (proposed 10 seconds) and size
  limits; a diagnostic failure records its category and preserves the original
  test failure. Existing proof RPC assertions remain strict. No other-thread
  inventory, send/resume/settings/queue call or retry-state mutation is added.
  Save summaries under existing /tmp/creation-evidence and print their bounded
  JSON so failure logs retain them even when no CI artifact is exported.

This evidence separates the next decisions: differing actual turn identifies
identity/turn-transition disagreement; differing count with matching expected
native users directs investigation to folding/admission/progress; absent native
users or mismatched IDs/text hashes directs it to native delivery/fixture timing;
invalid asc envelope/filter/order identifies the native reader contract seam.
If those all match but proof still stalls, narrow the next inspection to the
specific remaining binding/progress gate shown by state. Do not select a
production correction or change timing on speculation. Observer diagnostics must
not manufacture authority or call the production proof mutator to force success.

After A's diagnostic-only committed/quick-checked delta and required affected
review, run the same existing creation acceptance once through the normal watcher;
no new job, input-volume campaign, timeout increase, assertion removal or synthetic
compact record. Require all four already accepted native assertions on success.
On failure preserve the new projection, then obtain a source-backed defect/fix
brief before retrying. Cancellation fix/review remains independent; publication
and deployment keep the existing lead gates. Architect made only this design
write, with no tests, VM/GH requests, native calls or application edits.


## Rootless stop skips only absent-root recovery calls

**BOUNDED SOURCE-VALIDATED FIX BRIEF — 2026-11-03; A owns implementation after
lead acceptance.** Clean source `9acfcf4d3138a94b40f11f9670fb14a549e29740`,
run 41715271008 attempt 1, archive job 126193509103. Independently matched
`runtime-postreview-9acfcf4d/archive-failed.log` SHA256
`dba182af414ec28cd8191655497b5f62c4147118a22ea79fcf82c8937c529b4e`.
Lines 6204–6210 show the disposable VM confirming stop for
2026-11-02-service-automatic, then installed ff8... recovery cancel-retries
receiving `--thread-id ''` and refusing `exact recovery identity is required`.
The fixture starts this session with --no-codex (:425–431), then launches a
registered preview. Earlier held-turn archive/cleanup progressed past the prior
bug by execution order; this remains a failed complete archive check.

Exact cause: `Runner#stop` (:1807–1817) checks `if session.codex_thread_id` twice;
Ruby empty strings are truthy. Native tmux parsing preserves the empty field
(:704–718), while common test doubles default to nil. The Go recovery bridge
(:26) correctly rejects empty thread before creating its client or operating on
recovery state. Do not change that validator or infer a root from another source.

Minimal caller change, only inside stop after existing ensure_managed_session!:
retain the returned session's `thread_id = session.codex_thread_id`, and guard
both existing recovery calls with `thread_id && !thread_id.empty?`. Keep order
cancel-retries → close_session! → stop for every nonempty ID. Alternatively repeat
the exact nil/empty predicate at the two existing sites; no shared helper is
needed. Do not strip/normalize IDs, rescue failures, bypass close_session!, or
apply a broad cleanup across unrelated callers. This is call admission, not a new
ownership or rootlessness classifier.

Known-root loss still refuses before either recovery or close: select_tmux loads
retained authority (:3209); ensure_managed_session! invokes
validate_authority_session! (:8752–8788), which compares the exact live root,
socket and version against a recorded Codex tuple. Replacing that known live
root with nil or empty therefore raises `live Codex session does not match
trusted authority`. Partial/empty retained Codex authority itself also refuses
(:3278–3305). If a configured authority is absent, the existing retirement path
still refuses untrusted closure; do not replace that check with the new guard.

For the genuine rootless shell, authority deliberately omits the Codex tuple
(:3322–3329). Both native recovery calls are skipped; close_session! still verifies
tracking, retirement identity, idle/team conditions, exact tmux creation token,
conditional kill, absence after kill and authority retirement (:9279–9308).
Its native quiesce already uses the same nil/empty predicate (:9464). Nothing
here stops or unregisters preview services: the existing later archive cleanup
owns those resources and the existing native fixture must still prove it.

A package: the two local stop guards (optional one local root variable) and
focused existing Ruby fixtures, preferably `test/dev_session/tmux_runtime_test.rb`.
Use explicit disposable env/state, existing ManagedTmux and an absolute local
portal stub with an absent socket below the fixture root; no ENV inheritance or
installed helper/native socket. Acceptance cases:

- Valid shell authority with root nil and with root '': stop closes only the
  owned fake terminal, makes no recovery call, and preserves ordinary tracking.
  A stub tripwire fails if either empty/nil case reaches native recovery.
- Valid nonempty matching root: exact ID reaches cancel-retries before closure
  and stop after closure, once each; existing idle/refusal/kill safeguards remain.
- Seed authority with a valid nonempty root, then make the live fake root nil or
  empty without rewriting authority: refuse before recovery/kill and preserve
  authority bytes. This is distinct from the rootless case.
- Keep existing active-root refusal and replacement/kill-boundary tests. Preserve
  Go's empty-identity rejection; no new broad lifecycle fixture or VM scenario.

Focused checks after release: repository Nix shell Ruby tmux_runtime_test and
existing stop-confirmation selection, with bounded stderr retained and no live
backend. After exact committed/quick-green affected general/risk review, the
existing archive native acceptance must complete through rootless stop and
registered automatic cleanup. Same watcher retains fast/creation ownership;
publication/deployment stays lead-controlled. No schema, quota, UUID, recovery,
service registration or package compatibility change. Architect performed only
static source/log reads and this design write; no test, CI poll or lifecycle action.


## Native creation prefix: advance one held response after each accepted steer

**SOURCE-VALIDATED FIXTURE BRIEF — 2026-11-03; A owns implementation after lead
acceptance.** Runtime evidence is exact 9acfcf4d3138a94b40f11f9670fb14a549e29740,
run 41715271008, attempt 1. Independently matched files under
`runtime-postreview-9acfcf4d/`: `creation-prefix-diagnostics.jsonl` SHA256
`030de1d24b55e29ad7cc8ea948e1408a0eebbf740dd0188baa77739c30565ac3` and
`creation-failed.log` SHA256
`6c073ceafe5cad14f2f50d8991ed42ab9d6c767ede62fe25f0f5e18b312b6da6`.

Both diagnostic captures have current turn
01a1a32f-cba6-7e82-99b3-9986ee4dfc10, ManagedTurn count1 and native asc total1.
The sole native item 01a1a32f-cbf8-7b83-9552-fb7f6dae9099 matches the initial
client UUID 3eb79404-021a-48a4-a420-7885e1852a15 and expected text digest.
Accepted steer 47e7f921-8408-4293-80a2-f034433065e2 remains an unproven snapshot
with exact expected text, current turn, epoch1 and matching binding digest.
Handled is the previous turn, Pending is absent, and native current status is
inProgress. Thus the saved prefix matches available history; these observations
do not establish a folding, binding or unknown-input defect.

The exact native source is now available for this conclusion. The failed log
(:748, :2035) names native package 94pabrw3ff2xy0kg05rgxjch2p1g6ids-codex-0.165.0.
Its c1ql1zd4dph4f28wrlx98ilkr1m3v4dg derivation selects source
j4xcz959sk3k5isb6q29gpyivjym37j9-source, official rust-v0.165.0. The absent local
source and unavailable upstream tagged raw URLs were not replaced by another
release. Read-only retrieval of the existing cache.nixos.org NAR
`nar/1ygyns7gvqzw2dww6344vllq1x9dql6ih6wc6x4c4rhysk0fklvg.nar.zst` was decoded
in memory and independently matched to the fixed-output SHA256
`b9PpwNQeZsJIN4wbGA3FLfWAKd2EDMN5E/zj/Y62/vk=`. No realization/build/store write.
Runtime and selected-package llm-agents/codex-web lock nodes also match.

Exact source anchors below are relative to that verified archive's codex-rs/:

- app-server/src/request_processors/turn_processor.rs:1045–1103 passes exact
  expected turn and client UUID to steer_turn; accepted submission returns its
  turn identity. Pinned codex-web d3a29bee90ef client.go:5381–5405 treats that
  response as acceptance; it does not claim the input is already in history.
- core/src/session/turn_input.rs:843–928 validates the active turn, appends the
  user input to its pending queue, then returns acceptance. input_queue.rs:373–386
  appends/notifies; it does not publish the user item to history.
- core/src/session/turn.rs:465–495 drains pending input and records it before the
  NEXT model request. :579–590 awaits the current sampling response; :606–621
  enables draining and keeps the same turn going when pending input exists.
  :950–1001 records accepted pending inputs through run_hooks_and_record_inputs.
  No additional tool invocation is needed to force that continuation.

Fixture cause: creation_model.py:100–104 withholds even HTTP200/SSE while
hold-turn exists. session-creation.nix:383–401 accepts the steer and waits for
its persisted/native prefix while leaving that response held. It prevents the
native loop step that publishes the steer. The runtime reader correctly retains
its snapshot until a native item exists (turn_retry_reader.go:255–272). This
source-backed ordering explains the observed wait; it does not prove the later
pagination/cursor/restart assertions pass.

Smallest correction is confined to existing test/creation_model.py and
nix/tests/session-creation.nix. Keep hold-turn active, but let the fixture grant
ONE response permit for an exact existing request index, using a disposable
control file such as release-turn-<index>. Only that handler consumes it and
leaves its hold; the next request remains held. Keep ordinary hold-turn behavior,
naming and archive fixtures unchanged when no exact permit exists. No timed
remove/recreate of a global hold, free-running response budget, new model API,
tool call or native/portal production change is needed.

In the existing four-input case, select the held request from requests.jsonl
using its unique initial fixture text and index (not the latest unrelated row).
After each successful exact-UUID/same-turn steer receipt, permit that request
once. Wait for a later request for this same marker whose input contains the
new exact steer text; the still-present hold keeps that next response blocked.
Then run the unchanged native/persisted prefix proof and retain that request's
index for the next step. Repeat for counts2 and3, restart only the portal as
already specified, then repeat for count4. Request-body evidence stays inside
the disposable guest; print only bounded indexes/IDs/counts/digests. Finally
remove only this case's hold/permit controls so the existing completion checks
can run. Preserve initial/failure projections and diagnose before another rerun.

Acceptance retains all four goals: real asc envelope/turn filtering; limit1
pagination with exact chronology/no duplicates; appended same-turn users and
previous tail-cursor behavior; fresh portal PID replaying the durable prefix and
extending it exactly once. Every accepted UUID appears once in the expected
turn, no additional turn appears, model/provider/effort remain fixed, and all
unknown-input/settings/admission/receipt checks remain unchanged. A native next
request missing the steer, turn completion/change, or unchanged prefix after
that request is a new failure requiring its actual diagnostics, never permission
to synthesize authority, relax an assertion, resend, or increase the timeout.

A's package is this fixture-only delta and its focused syntax/control checks,
kept separate from the completed rootless-stop correction. Preserve prior
failure evidence. After committed quick-green affected review, use only the
existing `nix build .#checks.x86_64-linux.session-creation --print-build-logs`
under the established watcher/lead batch; no extra native job or volume campaign.
The source test already owns all required assertions. Expected duration remains
the existing creation check (roughly15–25min); stop on its first failure and
return the new bounded projection. Shared archive-model use requires reviewing
unchanged no-permit behavior, not broadening the production patch. Publication,
pins and deployment remain lead-controlled. Architect ran no tests/native calls,
CI polling or lifecycle action and wrote only this design addendum.


## Installed SITE service details failure: diagnostic-only package

**COMPLETE BOUNDED BRIEF — 2026-11-04; no producer correction selected. A owns
implementation after lead release.** Deployed runtime is
0872c5079396fa5763f3ae8d9a30b506010106d1; composed SITE package is
/nix/store/hyjxg06wbz3z7jm62338a3s3s18hn66w-dev-workspace-0.2.0 (deriver ybdakl5l...),
with workspace684ac/configab447/system96304 recorded in rollout.md. Installed
verification driver gjxmkhi8.../k30a04... failed once, exit1 after1076.437336s;
its processes settled and QEMU cleanup was logged. Health/continuity success is
separate from this failed verification. Machine claim5af5ab4e-b640-41b2-a8d0-
3284c0955ba9 remains held; no integration, release, rollback or lifecycle action.

Evidence: deployment-0872/installed-driver/command.log SHA256
7396fb17a83b62c924e7a363618ca3791a2f6b43d47c066edf0c38a3a47444c9, independently
matched. Compiled test-script:326–330 first passes CLI count3/len3, then its
single details GET returns servicesKnown=false/countKnown=false/value0 and fails.
The CLI read takes6.92s (:3134); details portal_read r0000000000000022 records
5701.07ms with repo_validate200.73ms/repo_status464.37ms and minor earlier stages
(:3137/:3248). Named stages sum666.35ms;5034.72ms remains unmeasured. This strongly fits the5s service
producer deadline, but neither timing nor HTTP200/category=ok proves that branch.

A's completed inventory, deployment-0872/installed-driver/readonly-inventory.json
(SHA256a231d06b0957de5bd82c887b81e2c5fd81cbd567a7bde584f553cada815fd64e), found
no child exit/context/parse/stderr evidence, HTTP headers or exported service state. Retained /tmp/session-services-installed.5icz_0kq
contains .keep, driver.xml (SHA2567cc9e22e40e21c8a4a54e4bfbc6e94de86e1eafa564814ed8b97567e86f6ec52)
and junit.xml (SHA25681f0d62a33f89886ea9c24b17e1bde3ae23e33468d8ea071d041d98f2e318b93;
9cases/1failure). The exact driver expression imports0872's existing archive test
and substitutes only SITE devWorkspace. No generic compiled-driver byte equality
is claimed. Generic0872 archive success retains its original generic scope.

Missing decisive fact: did the service helper actually hit its deadline/cancel,
fail to start/exit, fail strict projection decoding, or lose identity/admission?
This determines whether to correct producer work/admission/encoding, or establish
a fixture/environment issue. No source or current evidence justifies a timeout
increase, fixture retry-to-green, count relaxation or claimed SITE catalog defect.

Source contract at0872:

- session_services.go:57–99 checks profile/incarnation, runs stable dev-session
  with explicit --workspace fixture, cwd and DEV_WORKSPACES_STATE, then strictly
  decodes/revalidates. Its captured4096-byte stderr and all specific errors are
  discarded. loadServicePage:160 drops the error, causing the unavailable result.
- coordination_cache.go:13–17,63–155 supplies a5s shared producer,2s success TTL,
  bounded flights/bytes and identity revalidation. Cancellation can replace the
  underlying error. processgroup.Run kills the client group and bounds pipe wait.
- workspace-host:1487–1521 adds exact generation/profile and shared transition
  admission; dev-session:9815–9835 classifies service list as read-only, and
  workspace-session-services.rb:275–289 uses a nonblocking shared session lock.
  SITE extension catalog entries enter wrapper arguments; this path invokes no
  machine resolver, adapter deployment, target discovery or network probe.
- Ruby public_status:467–499 preserves known membership when an individual native
  observation fails (row state unknown). Its native work budget is20s (:650–666).
  Such a row failure alone cannot explain an entirely absent Go projection.
- Existing read_diagnostics.go has fixed stages/categories and numeric timing;
  services are not measured and their dropped error leaves HTTP200 category=ok.

A's minimal diagnostic-only delta belongs in session_services.go and its existing
Go tests, with the smallest necessary extension of read_diagnostics.go/tests and
nix/tests/session-archive-lifecycle.nix. If diagnostic documentation changes,
update only the existing read-diagnostics paragraph in docs/workspace-portal.md.
No Ruby/status schema/CLI flag/cache-policy/native-client/UI control change.

Record fixed safe service stage/outcome before coarse error conversion, plus
numeric elapsed milliseconds, exit code when available and stdout/stderr byte
counts. Distinguish identity-before, helper-start, helper-deadline, helper-canceled,
helper-exit, output-limit/projection-invalid, cache/wait and identity-after.
For context failure, record actual producer context state at the helper boundary;
do not infer it from duration or expose raw error text. Preserve that measurement
when the cache replaces an error. Add services timing and dependency-failure
classification to the existing read trace; shared-flight/cancellation semantics
stay unchanged. Use fixed vocabulary and existing logging ownership, not a new
logging subsystem. Avoid per-row/success heartbeat logs or payload retention.

Implementation clarification: the shared producer uses the cache parent context
and can fail after its originating HTTP waiter has departed. Keep one separate
lastServiceLog atomic timestamp inside existing readDiagnosticState for fixed
portal_service_read identity/helper/projection failures, at most1/sec. Coarse
cache/wait outcomes remain on the existing per-request trace. This prevents a
coarse portal_read record from consuming the producer diagnostic's sampling slot;
it does not promise every concurrent failure survives sampling. The two streams
are independently bounded (combined at most2 records/sec); document that change.
The correlation identifies the request that started the shared flight, not all
its waiters. Preserve actual producer context classification before conversion,
without changing cache lifetime/errors/cancellation or adding persistent state.
Focused regressions cover a departed waiter followed by producer failure, separate
coarse/producer sampling, producer rate limiting and absence of secret canaries.

Never log raw stderr, stdout JSON, argv, environment, labels, paths, unit/cgroup
names, native IDs, private registry data or credentials. Existing HTTP correlation
and fixed metadata suffice. The single failing VM assertion should retain only
its HTTP status/X-Portal-Read/Server-Timing, selected count/known booleans and the
corresponding bounded safe diagnostic. Keep its original condition and one GET;
no polling/retry, new harness, service launches or extra input campaign. Existing
fixture cleanup remains its owner; do not alter this real session or host state.

Focused quick acceptance: existing service-reader/read-diagnostic fixtures cover
successful known count, busy/nonzero helper, actual canceled/deadline context,
malformed/oversize projection, identity change, and shared-reader behavior.
Confirm fixed stage/outcome/numeric fields survive the real error conversion;
secret canaries in stderr/JSON/env never appear in diagnostics or response.
Use the repository Nix shell and existing Go test entrypoints, including
`go test -mod=readonly ./internal/web -run 'TestService|Test.*ReadDiagnostic|TestCoordination'`
from portal/, plus syntax/evaluation checks for the touched existing VM fixture.
No5s/20s/TTL/byte bound, ownership/count assertion or native expectation changes.

Shortest sequence: A commits this complete diagnostic-only package, passes
required quick checks, then lead obtains affected committed review before any
long observation. Keep deployed0872/SITEhyjx and its held machine unchanged while
collecting diagnosis. After release, compose the exact diagnostic runtime with
the same recorded SITE inputs via explicit local overrides and build the existing
archive driver against that exact candidate; preserve source/NAR/derivation/input
receipts. One existing VM observation may diagnose the candidate without deploying
it first. Label it diagnostic candidate evidence, NOT installedhyjx verification,
not proof that downstream pins advanced, and not acceptance of the failed run.
This avoids a diagnostic-only production rollout and speculative pin stream.

Allow roughly the existing18min installed-driver duration; stop at its first
terminal result. A classified failure supplies the next bounded correction brief.
A nonreproducing pass describes only that attempt and leaves the original branch
unproved; no automatic second attempt. Once a correction is justified/reviewed,
lead owns required final checks/publication/pure matching pins and ordinary
system-then-profile deployment under the retained claim, followed by actual
selected-path equality and exact installed verification. Existing successful
checks are reused only for their certified unchanged inputs. No new installed
package or successful final verification is presumed. Historical ambient first-
invocation effects remain UNKNOWN independently. Architect performed source/
retained-log reads only and wrote this addendum; no tests/builds/native probes.


## Service details deadline: correct the fixture to test the supported fallback

**BOUNDED DECISION / IMPLEMENTATION BRIEF — 2026-11-04; pending lead acceptance.**
The diagnostic-only seventh commit2b23f9765410bcb0985dbdd57411de00479bc0d0 is
unpublished/unselected; the first six commits through deployed0872 remain exact
protected ancestors. The one reviewed candidate0dn/driverw83 VM failed after
1012.294753s. All owned processes settled. Live0872/SITEhyjx remains selected.
This is classified diagnostic evidence, not an installed verification pass.

Exact evidence: deployment-0872/installed-driver/diagnostic-2b23f976/command.log
SHA256d58443bf453f4a6122dfc9c66ac6c729862aa8cd0c68ba2e90aeeeba9713f82c;
readonly-inventory.json SHA25638606f21c8d34858c8a517eb0300fd94a77d4b0c5b068a4f789d0c664a8a9e44.
Safe projection at3131/correlationr0000000000000022 reports actual producer
stage=helper/outcome=deadline,5023.23ms,exit=-1,stdout=0,stderr=0. Services timing
is5024.06ms, response total5582.32ms. HTTP200 returns servicesKnown=false and
count{known:false,stale:false,value:0}. Preceding CLI list succeeds in5.70s and
passes count3/len3 by execution order. Its raw rows were not retained. Compiled
assertion360 fails; original19tail statements364–382 remain present but were not
executed. Deliberate InvocationID corruption had NOT happened. Other earlier
helper deadlines/canceled waiters do not locate startup/admission/native costs.
The original0872 failing branch and why the child exceeds5s remain unproved.

Decision: this attempt demonstrates the supported whole-reader deadline fallback.
Correct the fixture's unconditional one-GET-success assumption; no producer or
latency correction is justified by this evidence. docs/workspace-portal.md:346–362
separately defines readable returned registry membership with unknown per-unit
state, and initial whole-reader failure with unavailable status/unknown count.
The latter is what occurred: Ruby had returned no projection when Go's existing
5s producer deadline ended. A readable registry in another CLI invocation is not
an accepted portal projection. Ruby's20s native-work bound is an independent
ceiling, not a promise that the portal waits20s. Preserve both bounds, strict
registry/ownership/JSON checks, process-group cancellation and cache behavior.
This accepts no guarantee of timely positive live rendering in every environment;
it does not claim that the unexplained latency is fixed or that arbitrary
unknown responses should pass native acceptance.

A's smallest complete package:

1. In existing nix/tests/session-archive-lifecycle.nix, retain strict native CLI
   proof before the single details GET: countKnown=true, registered=true, count3,
   exactly three distinct current IDs/labels main,candidate,fast, and public-field
   privacy. Row observation state may legitimately be unknown. Do not substitute
   private registry data, change launched resources or add native probes.
2. Validate exactly one of two outcomes from that existing GET. Success requires
   servicesKnown=true, known=true/value3 and exactly the three expected public
   rows, with existing HTML privacy checks. The fallback requires HTTP200,
   servicesKnown=false, known=false/stale=false/value0, visible unavailable/unknown
   presentation (not the confirmed-empty message), no fabricated current rows,
   and the SAME response correlation's actual helper/deadline record from the
   existing safe diagnostic. Timing alone, missing sampled evidence, cancellation,
   nonzero exit, invalid projection or identity/admission failure do not satisfy
   this fallback branch. Do not require incidental bytecounts/exit-1 to be stable;
   actual context deadline is the admission fact. Preserve numeric diagnostics.
3. Reuse the existing bounded diagnostic projection/parser; return its safe value
   for the assertion as needed. No new endpoint/helper protocol, extra GET,
   wait-until-success, sleep, retry or timeout change. Keep failure evidence.
   Both accepted outcomes continue into ALL19 original tail statements in their
   original order. No early return, exception swallowing or reduced subtest scope.
4. Strengthen existing portal/internal/web/session_services_test.go to require a
   successful THREE-row public helper through the actual service/details render
   path, exact known count3/IDs and privacy, including one unknown unit row with
   known membership and retired history excluded from count. Keep actual bounded
   helper deadline -> unavailable/unknown coverage and existing foreign/private/
   malformed/oversize/identity-change rejection. Existing Resources browser checks
   must retain unknown/stale versus confirmed-zero behavior. This supplies mandatory
   positive portal projection/rendering proof separately from native timing.
5. Clarify only the existing temporary-service-status documentation paragraph:
   known membership requires a successfully returned/validated projection; a
   whole-helper deadline retains explicit unknown or stale UI state. Lead owns
   final user-facing wording. No new latency SLO, polling policy or product control.

Native acceptance still proves every candidate, cgroup descendants and fast exit;
intentional InvocationID mismatch refuses before supporting-file deletion;
original operation/prelude/receipt IDs survive retry; graceful/forced native stop,
unit/cgroup disappearance, retained evidence, foreign-unit survival and revival
without restart remain exact. CLI positive membership/privacy and Go positive
three-row rendering are required, not replaced by the fallback. If the fallback
is exercised, state explicitly that native portal positive rendering was not
observed in that VM. The cleanup proof is not a performance benchmark.

Quick checks in the repository Nix environment: existing Go Service/read-diagnostic
and Resources browser suites, VM Python/Nix syntax checks and the same scope check
that verifies all19 original tail statements remain reachable on both branches.
Exercise both count branches and reject an uncorrelated/missing/nondeadline safe
record using the existing fixture seam; no running services/new harness needed
for these focused logic checks. Existing secret-canary and strict decoder tests
remain. No new broad timing/input campaign, source-cost profiling or native probe.

History/delivery: A may consolidate the unconsumed seventh diagnostic+fixture
work into one coherent successor, retaining exact2b/artifact/review evidence and
old/new delta; do not rewrite any of the deployed first six. Complete source,
quick checks and affected committed review precede publication/long checks.
There is no second unchanged2b VM. Use the existing required final-runtime checks
(including archive through the19tail) after review; reuse older successes only
where exact required derivation/input receipts allow it. No extra diagnostic VM
is needed for this contract decision. Final source publication, pure matching
workspace/configuration pins and NAR/input certification remain lead-owned.

Prepare the resulting exact SITE package/system/driver normally, preserve the
current held claim, and follow the original system-then-profile rollout contract
where outputs change. Only after actual final selected-path equality run the
existing exact installed driver and require all lifecycle assertions to finish.
A corrected fixture/candidate result cannot certify the currently selectedhyjx
run retrospectively. Machine remains held until verified deployment and approved
integrated lineage; no default-branch approval, release or real-session lifecycle
is supplied here. Historical ambient first-run effects remain UNKNOWN separately.
Architect changed only this design note; no source/test/VM/build/native action.

## Resources subtab badges: final-head verification and deployment delta

**BOUNDED PLAN — 2026-11-04; for lead acceptance.** This later UI addition is
commit `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7`, directly above deployed
`95a53aedbb6f530c093b35a9c6cea5879d455cb2`; preserve all seven deployed ancestors.
It changes only `portal/internal/web/static/app.js`, the session/index/automatic-
archival templates, `resources_test.go` and `cluster_controls_browser_test.cjs`.
Existing public count snapshots/events update every badge copy; subtab zero stays
visible, sidebar zero suppression and unknown/stale semantics stay unchanged.
There is no count-reader, API, polling, schema, host, extension or lock change.
This delta selection supersedes the earlier combined-feature verification batch
only for this six-file addition; any wider change requires reassessment.

Evidence already available: `resources-badges/receipt.json` (SHA256
`a8551b15a17dbfb219e8b4c872b6d7448427e7d097f30798c6d18566591b2f7d`)
binds tree `a542ac38715b6dd3c990c9858007a4345f880f19`, source `4vkb...`,
NAR `sha256-pDaBIdK6uFgVq0Gw7arQLjvIjKsGrKg33IFmwmxnOoo=`, unchanged nine-node
runtime lock graph, tested/committed diff equality and the following passes:

```sh
# Already run by B in the pinned Nix environment; do not repeat unchanged passes.
go -C portal test -mod=readonly ./internal/web -run 'Test(Resource|BrowserAsset|OperationsNavigation)'
node --test portal/internal/web/resources_browser_test.cjs portal/internal/web/coordination_browser_test.cjs portal/internal/web/read_cycle_browser_test.cjs
PORTAL_BROWSER_TEST=1 go -C portal test -mod=readonly -count=1 -timeout 5m \
  -run '^TestQuestionBrowser$/^cluster_controls_browser_test[.]cjs$' -v ./internal/web
```

Go passed in 0.205s; Node passed 35/35 without skips; browser passed in 31.25s
(48s launcher elapsed). `resources-badges/browser.sh` selects pinned Go/Node,
`playwright-test` and both Chromium/Firefox browsers. This consumer needs the full
`playwright-driver.browsers`, not the Chromium-only closure from the earlier retry
consumer plan. It uses the actual Go template/scripts/styles with controlled API
responses, not production native data. Existing tests cover initial/refresh counts,
failure→stale→zero→recovery, reservation deduplication/excluded states/incarnations,
keyboard/history and badge geometry. Four 1280/375 screenshots are retained;
architect visually inspected the Chromium desktop/mobile pair, including all three
badges and the mobile wrap. Fixture TLS bypass is confined to its disposable origin.
This is real browser fixture evidence, not a live selected-portal browser pass.

**Review and runtime batch.** Lead obtains the same reviewer's affected final UI
review of committed `95..3bb` before publication/long work. If unchanged and accepted,
publish that exact eighth head once and require its ordinary Check workflow to
finish `fast`, `archive` and `creation` successfully. `.github/workflows/check.yml`
already schedules all three for feature pushes: do not disable them or replace
them with 95's results. Fast evaluates all checks and builds non-VM checks including
package and host-package-contract; archive/creation run their existing VM checks.
No duplicate local archive/creation run or optional retry-browser campaign is needed.
No manual host workflow: its host-module/recovery VMs are scoped to dispatch/master
and this delta changes no host boundary. Expect the existing CI-scale batch (roughly
20–30 minutes, cache-dependent); actual failure stops dependent pin/preparation work.
Investigate its evidence before any rerun. Expensive site/system preparation stays
behind the exact runtime gate; no new test job or campaign is introduced.

**Extension and composition.** Extension remains exact `f8da821e3c76e26e73aa9d89a712eab0e0faa319`.
Its AGENTS/README require normal fast migration and host-path contracts, but reserve
`host-migration-test` for changed migration/host-state compatibility. Keep those
normal checks; neither that VM nor the full unrelated 21-suite extension three-check
campaign is required by this badge delta. Do not describe the old f8da+95 campaign
as a pass against 3bb. A small existing-file migration run can preserve the required
normal check without running KB/provider/adapter suites again. Using the immutable
`SESSION_RUNTIME_REF`, `SESSION_EXTENSION_REF` and clean matching checkouts defined
in the earlier staged plan, the source-derived invocation is:

```sh
nix develop --impure --expr '
  let r = builtins.getFlake (builtins.getEnv "SESSION_RUNTIME_REF");
      e = builtins.getFlake (builtins.getEnv "SESSION_EXTENSION_REF");
      p = import e.inputs.nixpkgs { system = "x86_64-linux"; };
  in p.mkShell {
    packages = with p; [ bash coreutils git jq nix openssl ruby tmux util-linux ];
    DEV_WORKSPACE_RUNTIME_CONTRACT = r.lib.runtimeContract;
    RUNTIME_AUTHORITY_CORPUS = r.lib.runtimeAuthorityCorpus;
  }' --command bash -c '
    set -euo pipefail
    cd "$SESSION_EXTENSION_SOURCE"
    test "$(git rev-parse HEAD)" = "$SESSION_EXTENSION_REV"
    unset RUBYOPT RUBYLIB GEM_HOME GEM_PATH BUNDLE_GEMFILE BUNDLE_PATH MIGRATION_HELPER
    export LANG=C.UTF-8 LC_ALL=C.UTF-8
    export GEM_HOME=$(ruby --disable-gems -rrubygems -e "print Gem.default_dir")
    export GEM_PATH="$GEM_HOME"
    ruby test/migration_test.rb
  '
nix build --no-link --print-build-logs --no-write-lock-file \
  --override-input dev-workspace "$SESSION_RUNTIME_REF" \
  "$SESSION_EXTENSION_REF#checks.x86_64-linux.package-metadata"
```

The migration test uses disposable roots/tmux and the final contract/corpus; it
does not migrate the host. The package-metadata check builds normal/compatibility
packages and exercises catalog/router/namespace/layout assertions; evaluation also
asserts extension migration paths equal runtime host paths. Preserve all declared
package check/install-check dependencies. No private helper invocation is added.
Budget a bounded minutes-scale migration check and cache-dependent package batch;
stop at failure or an unexpected kernel build and reassess, not expand automatically.

After actual publication, make pure final workspace/config pins through the existing
nested runtime input and confctl channel. Preserve extension/follows/sibling inputs;
run `bin/check-dev-workspace-deployment --workspace-root PATH --configuration-root PATH`.
Retain the installed verifier, strong mechanical certificate, complete source/input
graphs and actual NAR/deriver receipts. Build the actual final workspace
`#vpsfree-dev-workspace` plus its existing `deployment-contract`, `agent-team-policy`
and `cluster-provider-composition` checks (and any other mandatory changed-input
checks selected by that consumer). These exercise SITE wrapping and composition.
Do not substitute a generic package pass. Runtime `nix/workspace-portal.nix:310–344`
keeps its Ruby aggregate, Go and Node checkPhase; `nix/ruby-checks.nix` filters out
these UI files. Reuse a successful Nix check only with matching actual derivation
and input receipts; otherwise let the selected build run its normal dependency.
Unchanged bytes/tree equality alone cannot certify an old output. Omitted unrelated
campaigns are explicitly not required for this delta, not falsely reused passes.

**Deployment and installed evidence.** Retain 95's actual installed system240g /
SITE9f239 / driverdiws evidence: 11 subtests, JUnit12/12, native portal POSITIVE3 and
all19 cleanup/recovery tails passed, with settled effects. That establishes the
protected 95 native boundary only. A new Git input can change package/system outputs
even when host-module bytes do not change. Prepare actual final outputs normally;
reuse an old artifact only if its derivation and complete inputs really match.
Keep the ordinary system build/copy → dry-activate/no-reboot switch with existing
health/auto-rollback → user-profile `switch --source` ordering and exact claim/session
admission. Use the existing rollout commands and forward-only profile recovery;
never hotpatch assets, bypass pins or invoke private activation helpers.

After exact selected-path equality, verify authenticated TLS health, own-session
details/coordination/Team, saved thread/roster/settings continuity and all expected
units. Check the actual served v67 asset/template and Resources badges against
those same count snapshots, including confirmed-zero child badges and unchanged
sidebar suppression. Complete desktop/mobile own-session read-only navigation,
refresh, keyboard and Back/Forward evidence in the existing authenticated browser;
do not activate cluster/reservation/lifecycle controls or launch a service for UI
proof. No maintained live read-only browser runner was established by the earlier
support investigation: keep this manual evidence explicit if that remains true.
Curl/fixture screenshots are not substitutes for an unperformed live browser step.
Positive/stale/error states absent from this live session remain fixture evidence.

No additional installed archive VM is required for this UI-only delta: final-head
generic native CI, actual composed-package checks and selected-UI/health verification
cover its affected boundaries while retaining the honestly scoped 95 installed proof.
Do not claim an installed 3bb lifecycle pass or prepare another driver by habit.
Reopen that decision if review changes a service/status/lifecycle/host/adapter contract
or composition instead of this frozen six-file scope. New failed/uncertain effects
block acceptance; the machine stays held until verified deployment and separately
approved integrated lineage. No merge, release or session lifecycle approval is
supplied here. Architect performed source/evidence inspection and this design write
only; execution and final evidence acceptance remain with lead.

## Consumer instruction check: preexisting mismatch exposed by badge preparation

**LEAD ACCEPTED BOUNDED FIX — 2026-11-04; B reads this brief before editing.** The original
local936/f8/3bb composition batch exited1 after13m02 (10:13:00–10:26:02UTC).
`site-artifact-prep-3bb/site-build.log` SHA256
`5e365cd0e25ded34115d31ff88add049053a3ef7401676de8e8b3fdda2ed23e5`, independently
matched, records the instruction check's actual0.062096s,10runs/169assertions,
2failures at126–145: AGENTS16776bytes exceeds the existing16384byte core budget;
the policy assertion still expects `automatic release for all deployed physical machines`.
The later whole-document no-`aitherdev` assertion is masked by that first policy
failure; it also conflicts with the accepted configured-machine example.

Failed derivation `7szz3fl52kchvyhr58h6kjp509wl77jh-workspace-agent-instructions-tests.drv`
is retained in `site-artifact-prep-3bb/failed-agent-instructions-derivation.json`.
Its buildCommand runs Ruby over `/nix/store/r9c6kn2cg02w0xmbwc5762a5fs37478r-source`;
NixJSONv4 `inputs.drvs` contains only stdenv, Ruby3.4.9 and bash, with workspace
source/standard builder scripts as `inputs.srcs`. No runtime3bb or browser helper
is a direct test dependency. This is a workspace instruction/test defect, not
evidence of a badge or selected-runtime behavior regression.

Independent byte comparison with retained95 workspace source
`/nix/store/0ij3cr0ar0q5x5wxig8siwmsvzfd4a68-source` confirms identical AGENTS,
test and coordination documents (16776/8869/10632bytes respectively).
B's source provenance identifies915645's420byte service-route/pointer addition
over b8b's16356byte AGENTS, and policy48b23aa's owner-release wording/configured
example with the test unchanged. Thus both semantic mismatches predate badge pins.
No old95 same-check derivation/pass was retained; do not claim it passed, reuse an
unrecorded derivation, or call the full13m02 an instruction-test duration.

Smallest owning package: B changes only workspace `AGENTS.md` and
`test/agent_instructions_test.rb`. Keep the16KiB assertion and all unique rules.
Concisely retain the new service-operation route and launcher requirement; remove
their duplicated completion/handoff wording already covered by the adjacent
lifecycle rule, then compact repeated routing/plan/review boilerplate as needed
for useful headroom. Do not truncate, omit obligations, move them to an unread
document, increase the budget, or redesign discovery. Preserve explicit full-read
routes, existing settings/team ownership and integration/lifecycle authorization.
The current `docs/coordination.md` policy is correct and needs no semantic rewrite.

Preserve this inventory of unique core obligations during concision:

- Every mandatory procedure route, full-read requirement, context-loss reread,
  unreadable-guidance stop and repository-instruction precedence.
- Canonical bare-clone/worktree/tracking layout; exact current/env/thread binding;
  stop on conflict; no access to another session's private ownership.
- Shared-master/index protection; SSH remotes; hooks; feature publication;
  initial tracking and cadence; exact-final-head completion; separate explicit
  default integration and deployment authorization; no destructive Git shortcuts.
- The `dev-session service run` requirement for every new session-owned local
  temporary server/preview/candidate and its lifecycle-procedure link; authorized
  cleanup only; no archive/delete/stop inferred from completion/handoff; original
  journal, package-generation, ownership and recovery boundaries.
- Saved team/model/effort/access/instructions; role ownership and live roster
  checks; no unauthorized team changes; design before implementation; utility
  watcher ownership; exact-pair cross-session communication authorization.
- Nix/tool/hook conventions, bridge default and kernel-build escalation;
  credential secrecy, exact production-KB approval and session-owned staging.
- Documentation/handoff/writing skills; phase/progress reporting; complete
  history/migration readiness review; compatibility, rolling/rollback and
  vpsAdminOS coordination rules; precise unmerged-migration/schema assumptions.
- Independent committed quick-green-before-long review, substantive-doc scope,
  planning-only exemption, saved reviewer policy; authoritative machine-retention
  routing; storage-retention warning and preservation of committed Git heads.

Repair the policy test against its current contract: locate one nonempty Machine
retention section, retain canonical runtime-policy and installed-guide references,
and assert owning-agent release after verified effects plus integration of the
complete deployed lineage into approved remote defaults. Failure/uncertainty or
missing integration proof retains ownership; deployment alone does not authorize
integration. Apply the no-site-host assertion to that generic policy section,
not to the valid configured examples elsewhere. Keep the operations/recovery link,
cross-procedure routing and independent lifecycle-approval assertions. Do not drop
assertions merely to turn green or reintroduce automatic-worker release wording.
Runtime3bb `docs/coordination.md#machine-retention` remains the authoritative owner:
normal explicit release, no background timer, original recovery, fresh later claim.

The existing failed run is sufficient red evidence. After the narrow edit, run
`ruby test/agent_instructions_test.rb` in the repository's declared pinned Ruby/Nix
environment, plus normal formatting/diff checks; report the resulting byte count
and all10tests passing. No second unchanged red run or new harness is needed.
Commit the complete two-file correction, then obtain affected independent
instruction/test review before resumed packaged work: this is substantive source,
not a purely mechanical pin refresh. Preserve existing reviewed runtime/UI history;
no repeat full runtime/extension/browser/native campaign follows from this fix.

After acceptance, build the exact final workspace `checks.x86_64-linux.agent-instructions`
and finish the existing stopped consumer/SITE batch. Reuse migration43/829 and
package-metadata only for their recorded exact inputs/derivations; completed
deployment/storage/tracking outputs retain their own bounded evidence. SITE,
agent-team-policy and cluster-provider outputs not valid after the stop are not
passes. A valid Nix output receipt requires a real NAR identity, not merely a
successful `path-info` process returning null. The workspace source change requires
fresh final source/certificate/composition receipts; assume neither identical
artifacts nor another runtime change. Stop on an actual failure and diagnose it.
This addendum authorizes no publication, pin/copy/activation, machine release,
default integration or session lifecycle action. Architect inspected source and
retained evidence only and wrote this note; B owns implementation after lead release.

B's completed evidence index is `site-artifact-prep-3bb/failed-batch-receipt.json`
(SHA256139f07ebdf7cafe1e9342f12ea76c43b276eb1012d82a89addd25eab76b1d7e8),
with `provenance.json` (SHA2565369476e7b7864f9bc807f2ed2a777f7367862420a008904def47cdedbc5d8ad).
Exact assertion source lines are11 (budget),47 (old phrase),50 (masked global
hostname assertion); earlier approximate handoff line numbers are superseded.

## Publication outage: exact local artifacts may precede feature publication

**BOUNDED ORDERING DECISION — 2026-11-04; execution remains lead-owned. YES.**
Feature publication is still required by default, but the settled contracts do
not make publishing the consuming workspace/configuration feature commits an
activation prerequisite. `docs/agent-instructions/deployment.md` permits building
and deploying the initiative's configuration worktree/feature branch; the runtime
README and selected ordinary host workflow support `workspace-host switch --source`
from a local checkout. Their published-upstream selection requirement still holds:
runtime3bb and extensionf8 are already published. This only removes the earlier
session-imposed publication-before-copy/cutover ordering during the GitHub outage.
It does not authorize a different source, bypass a native refusal or waive checks.

The fixed candidate is committed/reviewed LOCAL workspace56dd and config2fe, bound
by the retained immutable source/NAR/full-input/matching receipts (including99c72).
Config systemg1xc and its printed generation2026-11-04--11-11-29 are prepared;
SITEgh92/myjy remains unaccepted while B's original checkPhase is running. Record
the actual completed receipt, not a predicted pass. Only already-valid exact
artifacts may enter ordinary copy and non-selecting preflight, including the
established system dry-activate once that configuration's checks are complete.
System cutover and profile selection wait for all required final checks, including
B's SITE/consumer batch, and actual outputs matching the fixed reviewed inputs.

Use the existing local checkouts/immutable outputs and ordinary confctl and stable
workspace-host commands. No unpublished GitHub URL, remote latest lookup, alternate
pin, hotpatch or private activation path. Preserve exact clean committed source,
local Git refs, NAR roots, complete closure/input receipts and original recovery
artifacts while publication is unavailable. Stable profile preparation/activation
must pass its usual source, generation, lifecycle, capability and machine-claim
checks. If an ordinary path actually requires unavailable remote evidence, stop
that path; this decision supplies no fallback around its refusal.

Under existing exact held claim5af5, retain system copy/preflight → dry-activate →
no-reboot system switch with existing health/auto-rollback → ordinary user-profile
switch from the exact local workspace source. Verify selected system/SITE equality,
authenticated health, thread/settings continuity and the released read-only UI
evidence afterward. Preserve forward-only profile recovery and reconcile any
unfinished effects before further action. Current installed95/SITE9f/system240g
is unchanged by this design note.

Mark local56dd/config2fe publication (and any consequent final-head CI) pending;
publish those exact feature heads once GitHub recovers, reconciling uncertain push
effects normally. Never call them published, integrated or fully ready meanwhile.
The user has deferred merges: no default integration is authorized. Verified local
deployment alone cannot release the machine; keep ownership until its complete
deployed lineage has the separately approved remote-default integration evidence
and all normal release conditions hold. No session lifecycle action is authorized.
Architect only recorded this ordering decision; no build, network/SSH, pin, claim,
copy, activation or live verification was performed.

## Selected badge UI: bounded operator diagnosis after attempt2

**STATIC FINDINGS / OPERATOR PLAN — 2026-11-04; no product correction proved.**
The deployed myjy/g1 system/profile has passed the reported health, continuity and
source/package gates. The separate UI attempt failed; it is not a UI acceptance
pass. Independently matched `resources-badges/operator-prep/operator.cjs` SHA256
`35ede54eff471861f83bd9a24b6c26ed04c8d3a6804d8d1796efc27054cff8c0`, and
`deployment-3bb/ui-attempt2/{status.json,command.log}` hashes
`115bc86190ce65822e18f312c994447a3b3de8ad5086e187bd96b598b6fcf433` /
`263aba0a553d6900368fa30aa334e4a92bf35552e7f2ec7e291a37e262191a52`.
Exit1/28.589886s and settled process group are recorded. Native redirect guard
passed; allowed50/blocked79/WS0/snapshots0 and broad own-session-navigation stage
do not identify a failed locator, response, script dependency or count assertion.

Exact immutable4v source narrows the proposed avenues:

- No member-query expansion is justified. The operator navigates the own root
  page without a query. `server.go:1307–1328` sets SelectedMember only from a
  nonempty request member query; `static/app.js:43` therefore emits queryless
  details for this root page. An unexpected member value would be diagnostic
  evidence to explain, not authority to widen the allowlist.
- The required tablist label/button IDs match `templates/session.html:73–76`.
  Operator expected v67 SHA2569c427fff… matches immutable app.js exactly. This
  validates those expectations, not what attempt2 actually received/rendered.
- Startup awaits `/codex/assets/conversation.js?v=26` (app.js1516), and its other
  top-level module imports are within the already allowed public asset namespaces.
  No necessary new API/startup authority was established. Blocked unrelated widget
  reads are expected under Resources-only scope; their aggregate count is not
  proof of a broken dependency. A script/asset failure remains possible but unproved.
- A concrete operator assumption is unsupported: selectAll167–175 requires a NEW
  successful coordination response for every Reservations click. coordination.js
  resumes/render-reuses its accepted lastPayload, starts a read only when paused,
  otherwise retaining the active read/5s completion-based timer (10s read deadline).
  Tab entry promises neither a new request nor a fresh successful response. This
  can reject valid retained presentation; it does not establish attempt2's cause.

A owns the smallest one-off diagnostic change already released by lead: preserve
35ede/original failures, add fixed stages before goto/tablist/each tab, keyboard-
history, reload/read wait, evidence and each count/geometry check. Preserve the
first whitelisted operator error label instead of catch164's undifferentiated
boolean; classify browser failures with fixed categories, never raw exception text.
Keep safe reader status/counts, v67 boolean and snapshot lengths. Categorize blocked
requests into fixed own-reader-query/other-own/global/foreign/method/asset buckets;
never retain arbitrary URL/query/header/body/context values. Capture only the
Resources tab strip on failure if it exists; otherwise report absent/hidden booleans,
not a full page/transcript screenshot. Same TLS/credential/redirect/route bounds.

Recommended narrow oracle correction, conditional on lead acceptance: navigation
must not require a new coordinator response per tab click. Arm the existing exact
own details and coordination response observations before the existing reload,
capture their bodies/identity asynchronously, and require one accepted successful
observation of each for that viewport's evidence. Wait for those capture tasks and
the corresponding public badge presentation, not a newly invented tab-triggered
request. Keep final positive reader/identity/v67/reservation-membership checks,
initial/accepted-snapshot provenance, unknown versus stale versus zero, child/sidebar
agreement and geometry. No extra GET, blind retry, sleep, enlarged timeout or API
allowlist is needed. Do not replace the error with a fabricated compact snapshot.

Keep existing keyboard/history actions and desktop/mobile navigation in this
diagnostic pass: no evidence yet justifies removing them to hide the failure.
Their unchanged fixture pass remains separate evidence. The next shortest proof is
one main-released bounded operator observation with these safe stages (and the
oracle correction only if accepted), not another build/VM/extension campaign.
An asset/script, identity or rendered-count discrepancy is a real finding requiring
its own explanation; the instrumentation must not reclassify it as success.
No application source, pins, services or lifecycle change follows from this note.
The user's later four-master integration/release authorization remains lead-owned
and waits for actual verification and normal ownership/integrated-lineage proof;
it does not authorize session cleanup. Architect performed static/evidence reads
and this design write only, with no browser/password/network/test/live action.

## Workspace integration baseline: equivalent deployed feature successor

**BOUNDED DISPOSITION — 2026-11-04; for lead acceptance before B rewrites.**
The selected myjy package's `workspace-host coordination guide`, Machine retention
and Reviewed rebase lineage sections, explicitly permit an independently proven
equivalent successor to establish deployed feature lineage. A substantive successor
requires a new verified deployment. This is a lineage route, not a claim that two
Git sources, NARs, derivations or installed outputs are identical.

Preserve deployed workspace `56ddf50963e8c3e8b01ec3836026b87f04c14afb`, its old base
`b8b54c3c10384ab0f66336161927f3b95ac16e7a`, all retained refs/reviews and rnii/wx37/
myjy source/output receipts. The fixed new base is
`c2ebca4976eca074213872fcea074c719c42bccd`, containing reported remote08ec23ca.
Lead/B report all other baseline paths as tracking; architect inspected only the
two relevant committed procedure diffs, not other sessions' tracking. They add
three project-map lines for generated Rust/TypeScript clients and six lines routing
vpsAdmin API/HaveAPI generator changes to existing client synchronization guidance.
These are real instruction changes, not tracking-only; their condition does not
apply to this runtime/badge initiative. No Rust/TypeScript checks are induced here.

Rebase only the existing ordered three commits (b4714646, d225a8e8, 56ddf509) onto
that one fixed base, outside claims and with ordinary hooks. Preserve their split,
dependency stream and every original ref; no edits or conflict resolutions are
included in this brief. New base→head must reproduce exactly the eight reviewed
feature blobs/modes: AGENTS.md, config/{coordination,machine-identity}.nix,
docs/agent-instructions/lifecycle.md, docs/coordination.md, flake.{nix,lock}, and
test/agent_instructions_test.rb. B's object-only prospect59ac09ab is supporting
evidence, not the resulting head. Independently reconstruct the expected new tree
from c2eb plus those eight old-head entries and compare the actual final tree;
retain ordered stable patch IDs and range-diff for both exact ranges. Stop on any
unexpected path/mode, patch difference, conflict, changed lock or moved baseline.

After quick checks, the same reviewer covers affected General/Risk plus complete
three-commit history and migration lineage. Explicitly assess the two upstream
instructions' applicability and changed packaged source references. Bind the old
accepted report and old/new base/head ranges, reconstruction, patch IDs, checks and
migration conclusion in existing review/integration receipts. No new migration is
introduced; supported service/retry/claim state and original recovery remain those
of the unchanged deployed runtime. A main-agent certificate alone does not replace
independent assessment of this instruction baseline. Existing four-master approval
survives only the demonstrated clean equivalent refresh; material edits return to
scope/review/approval assessment.

The minimum new-head verification is deliberately consumer-scoped:

- Quick: run `ruby test/agent_instructions_test.rb` in the retained pinned Ruby/Nix
  environment, plus `git diff --check` on the exact new range. The test directly
  reads the changed verification procedure and routed procedure set.
- After review, build exact-final-source `#checks.x86_64-linux.agent-instructions`
  and `#checks.x86_64-linux.tracking-source` with ordinary `nix build --no-link
  --print-build-logs --no-write-lock-file`. The latter proves the refreshed source
  filter still excludes work/archive; this is a small check batch, not a SITE build.
- Run the existing `bin/check-dev-workspace-deployment --workspace-root PATH
  --configuration-root PATH` against the final checkouts. Preserve exact runtime3bb,
  extensionf8, configuration2fe and all locked input paths/identities. Record the
  new full Git and filtered-source NARs, complete graph and prospective SITE
  derivation/input references through normal evaluation, without selecting it.
  Verify that retained package policy, contracts, assets, host paths and executable
  inputs are unchanged; isolate changed workspace-source references and prove the
  referenced update-codex skill contents unchanged. flake.nix:22–30 filters only
  work/archive, while its skill override references workspaceSource: notes/docs can
  therefore change package paths even without changing feature behavior.

The final workspace has no workflow added by this delta; any ordinary publication
or hook check actually configured for its final head must still finish. Old runtime
3bb CI remains exact runtime evidence. No repeated runtime CI, native archive VM,
extension migration/389-test campaign or browser fixture is required solely by this
baseline. Unchanged deployment-contract/storage/team/cluster tests and SITE build
are not new results: their prior successes retain their original derivation/input
scope. Their exported derivations can change through the aggregate workspaceSource;
do not label those changed derivations cached passes or reuse old output identity.
For this equivalence-only integration, building/deploying a prospective SITE is not
required if independent review and the complete source/input certificate establish
that no executable/composition behavior changed. Any unaccounted consumer, contract,
skill or graph difference stops that conclusion and selects its affected normal
checks; a substantive replacement requires a new verified deployment.

Complete the already-required actual myjy UI verification independently; moving a
feature ref cannot change its immutable served3bb assets. On accepted equivalence,
record 56dd→new-final as equivalent integrated feature lineage, never literally
merged ancestry or a newly installed package. Capture the final comparison, publish
the refreshed feature with original refs retained, and obtain fresh remote-default
proof after the lead's ordinary approved fast-forward integration. A stale target
returns to unlocked preparation. Shared-master integration takes its one repository
claim then the nonwaiting tracking lock; release before records/CI. Machine5af5
stays held until verified effects/UI and all four deployed lineages are integrated;
then the lead follows the selected guide's ordinary status/release/result checks.
No session lifecycle action is authorized. Architect only read procedures/source
and saved this plan; no rebase, check, evaluation, build, claim or live action ran.

## UI attempt3: scope reader outcomes to the capture that owns the request

**OPERATOR-ONLY CORRECTION — 2026-11-04; A owns implementation after lead release.**
Actual operator d92b763b1f2e27417659ab9cbdec4c0a1eb6415f7303005ea555aa79284a5094
and `deployment-3bb/ui-attempt3/{command.log,status.json}` are bound by hashes
0a9bcc964b058518c9bbfeb227e3ee3ad0488d717cb40faf4bf623364e54b036 /
d32bc65b072b8fb2f46fff2adadef7d3ae9bbd04c3b68097a9d075236011d131.
The attempt settled exit1/25.339014s, native guard passed, final accepted arrays
each contain one observation, v67 is exact, and last reader statuses are 200.
Its terminal failure is reader-evidence with first reader-status. The Resources-
only crop shows visible 0/1/0 badges. These are partial evidence, not a UI pass.

Source establishes two accounting defects: readerFailure is global and survives
both observed/pending resets; the response handler binds to mutable observed at
response time. Thus preliminary failures stay sticky, and old in-flight responses
can enter a later capture. reader-status establishes at least one watched non-200
response, but its endpoint/status/phase is not retained. Neither cancellation nor
a Basic-auth 401 challenge is proved. Last200 cannot reconstruct earlier outcomes;
attempt2's cause also remains unknown. Do not add a blanket 401 exception.

Use the existing Playwright request/response/requestfailed events, with one small
capture object per viewport's initial/navigation phase and final reload phase:

- At request start, bind each exact already-allowed reader/asset Request object to
  the active capture (a WeakMap suffices). Response/body/failure callbacks retain
  that object; never consult a later mutable capture to decide ownership. Existing
  response waits must require the same final capture as well as exact path/200.
- Each capture owns its accepted arrays, body-task set and fixed numeric outcome
  summary. Keep endpoint kind, phase, request ordinal, status counts and first
  non-200/failure category; no URLs, credentials, headers, payloads or raw errors.
  Distinguish a response status from requestfailed/transport cancellation. Do not
  rename a non-200 as canceled or an observed 401 as a proved authentication retry.
- Preliminary/history outcomes remain recorded. They do not veto a later complete
  final sample merely because the page was deliberately reloaded. A successful
  final sample does not certify those earlier requests. Parsed identity, v67 hash,
  shape or reservation-membership violations remain fatal across captures; this
  change scopes transient transport/status outcomes, not semantic trust failures.
- Final evidence still requires successful own details and coordination bodies,
  correct session observation, exact served v67, and accepted count projections
  from requests STARTED in that final capture. An old response cannot satisfy it.
  Every non-200 or transport/body failure belonging to the final sample fails it,
  even if a later response is 200. Missing/unknown completion is not success.

Closure is explicit and bounded: once required final observations are available,
seal admission of new requests to that evidence sample synchronously. Settle all
requests already assigned to it and their body tasks under the existing bounded
wait budget; also drain already-started older body tasks before the verdict so a
known semantic violation cannot arrive after acceptance. Requests started after
the cutoff share no new settling allowance: closure uses one existing 15000ms
reader budget starting at seal, never reset per request/body/callback. This is not
a deadline from capture creation; existing navigation20000ms and earlier per-step
reader waits remain unchanged. Requests started after
the cutoff are outside this finite sample and must not mutate its arrays/verdict.
Do not stop application polling, issue another GET, extend timeouts or wait forever
for an empty network. If the existing deadline leaves an included request/body
unsettled, fail with a fixed incomplete category. Then compare DOM against that
sealed accepted history and take the existing crop. A concurrent later render
that cannot be justified by that history fails the ordinary count comparison;
do not manufacture a matching snapshot. Retire the capture before the next
viewport/navigation; older callbacks can update only their retained summaries.

A's bounded pure handler checks must cover initial non-200→final valid200 with
the earlier numeric status retained; late old response after reset cannot poison
or satisfy final evidence; final non-200/cancellation/unsettled body still refuses;
and parsed identity/hash/membership failures remain fatal. Exercise closure with
an already-admitted body finishing late and a post-cutoff request, without browser,
credentials or network. Preserve exact d92 and attempt3 evidence. No route/auth/TLS,
deadline, count, geometry, keyboard/history or desktop/mobile requirement changes.
After lead inspects the operator-only correction and quick evidence, one explicitly
released bounded live attempt can establish the actual selected UI result. No new
product source, package, pin, CI/VM campaign or deployment follows from this fix.
Architect read only own static artifacts/operator/crop and wrote this addendum;
no browser, password, test, network, claim or lifecycle action was performed.

## Postmerge creation failure: fork effort evidence boundary

**STATIC DIAGNOSIS / BOUNDED NEXT PACKAGE — 2026-11-04.** Runtime master run
41832349175 attempt1, exact3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7,
creation job126582416616 failed; fast/host/archive and extensionf8 Check passed.
Retain `integration-3bb/postmerge-ci/result.json`, failed job log (plain UTF-8/BOM
despite its .zip suffix) SHA256c7b753b9a322db1d1904b6855263c7d15f1f3ef4a51c7ec80d0ac33b7225f687,
and full runtime log d7fc843f770dc972839bc86136c1bf261c8509c5585fb39f77be6b4d98c4c612.
Raw4856–4867 records actual `medium` versus expected `high`, from
`test/creation_acceptance_browser.cjs:114`, called264 for `fork explicit` with
provider alternate. Its follow-up completed with the expected model reply; this
is a settings assertion failure, not a timeout or established infrastructure loss.
The native four-input prefix and actual portal restart passed earlier in this
same run (raw4647, PID1386→3821). Later creation scenarios were not completed.
The feature-run41807690915 pass remains prior evidence, not a substitute.
A's final `failure-inventory.json` (SHA2566cb86e5d5981d57a4163f81a1d181823ebea8f62d50ba815368e04fbf503c5dc)
binds failed creation drv bx87y8azf3gc086dmhpxbg41xz8xxawf, exactly the derivation
in the feature-pass validation receipt. Identical derivation does not erase this
failed execution or establish its cause.

Exact worktree/immutable4v/local p20 browser fixture SHA256 is
3f8710c4acdf04afac94cd59a933fcc5b7658d60274b12cd7bf2b7c2ae3feb5f (A's inventory).
Source sets high at56–64, reads the actual fork POST at260, and reads the fork
before follow-up at70. Neither settings tuple is retained. The failed record is
saved before follow-up; the transcript is saved at117, after the failing assertion.
A's bounded inventory found no admitted fork settings or before-follow-up tuple
in retained artifacts. VM copy messages do not supply their underlying files.
Model-refresh decode warnings and subsequent canceled reads do not prove causality.

There is a concrete source seam to test, not an established cause for this run:
`static/app.js:2597–2601,2901–2953` reloads provider-specific models asynchronously;
fork is a destination but is excluded from the managed creation selection branch.
`applyCurrentSettings:2850–2873` passes only plan forms as pending overrides to
`effortSelectionForModelRefresh:1444`, so fork effort can be repopulated from live
source settings rather than a deliberate draft selection. Existing provider tests
stub populateEfforts/applyCurrentSettings and do not establish end-to-end preservation.
The server copies submitted effort into its creation request (server.go3684), and
Ruby passes it to the existing settings resolver; changing either owner now would
guess which stage lost high. Do not relax high, add sleeps, or reselect settings
immediately before submission to hide a possible user-visible race.

Smallest A-owned next patch is diagnostic/assertion-only in the existing
`test/creation_acceptance_browser.cjs`: retain a fixed settings projection at the
end of settings(form), from the actual accepted POST, from followup's existing
before read, and from the completed thread before assertions. Include only
provider/model/reasoning effort and fixed stage; no prompts, tokens, arbitrary
headers or new APIs. Persist it before an assertion can throw. Assert that the
serialized fork requested the fixture's gpt-5.5/high/alternate selection. Keep
the original post-follow-up high/model/unique-message/native expectations intact.
This distinguishes DOM/serialization loss from admitted/native restoration loss
and a later follow-up change without extra native reads or model requests.

Do not expand into a separate delayed-model or browser campaign at this point.
The existing creation VM, with this missing fixed projection and immediate request
assertion, is the smallest controlled proof that distinguishes the actual stages.
The asynchronous source seam above is an investigation lead, not a production-fix
release or a claim that a different reproducible draft issue caused this failure.

Quick selection: pinned Node syntax check of the changed acceptance script and
focused review of the fixed projections/assertion ordering; no unrelated provider
suite is needed for this one-file diagnostic patch. Commit only that bounded final
patch, then same reviewer affected General/Risk review before one existing
`#checks.x86_64-linux.session-creation` attempt. Normal final-head CI remains
required; no unchanged3bb rerun-to-green or additional campaign. Preserve all eight
master commits and old receipts; append any correction, never rewrite them. A
fixture-only change does not require new deployment/pins. A proved product change
would need its own reviewed source/check/deployment scope and fresh machine claim.
The old claim is released; no live ownership or session lifecycle permission exists.
Keep actual deployed3bb/f8/56dd(myjy)/2fe and integrated12a3 equivalent lineage
unchanged. New test/source derivations are fresh evidence, not hypothetical artifact
equivalence. No downstream pins, system/profile build or rollout is induced solely
by this fixture-only follow-up.
Architect performed static source/log analysis and this design write only.
