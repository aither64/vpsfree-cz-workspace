# Rust confctl replacement design

Status: **DESIGN COMPLETE — 2026-10-18 revision: built-in features, no user extension API.**
Planning only: this is an implementation proposal, not permission to implement,
merge or deploy.

## Recommendation and implementation order

**Recommend removing user extension support.** The two existing scripts perform
confctl domain work: collecting running kernel versions before deployment and
maintaining a netboot machine list. Implement them as ordinary core Rust services
with opt-in typed Nix settings. This removes the registry, wire protocol, SDK,
capability dispatch, extension subprocess lifecycle and separately packaged site
binary. It retains the useful features, their tests and a small configuration
contract; it does not introduce a generic task or hook DSL.

Preserve `runtime-kernels update`, the existing kernel JSON and generated netboot
Nix list. Keep deployment refresh after confirmation and before generation
lookup/build, with cache invalidation; keep netboot refresh after the core machine
list is written by add/rename/rediscover. Default both features off. The site
explicitly opts into its current paths and automatic stages. Other deployments
acquire no new SSH probes or file writes.

The 2026-10-18 revision supersedes this plan's original executable-extension
recommendation. Both inventories remain immutable historical evidence: their
source observations and parity scenarios still apply, but their proposed
protocol/handler/package mappings are superseded by the built-in feature section.
The lead requested and favors this direction; no implementation is authorized.

Retain the Rust/Nix/SSH architecture, Tokio process ownership, Ratatui/Crossterm
inline view and Go invocation timing model. First freeze executable Ruby CLI and
effect fixtures. Then implement process/UI and typed domain interfaces, Nix/state
adapters, core runtime-kernel/netboot services and remote operations in separate
file packages. Port all remote Ruby helpers and the data client before packaging
cutover. Differential, PTY, mixed-version and disposable VM gates remain required.

## Revision completion

Identity verified from this session directory against the trusted thread binding;
both environment markers are absent. Both inventories and relevant guidance were
rechecked. No source or tool blocker. Proposed settings are
`confctl.runtimeKernels.{enable,stateFile,refreshBeforeDeploy}` and
`confctl.netbootInventory.{enable,outputFile}`. Existing site paths remain
`configs/node/kernels.json` and `cluster/netbootable.nix`; no new site executable.
The lead accepted this core-feature direction. Architecture, package boundaries,
dependencies, CI, milestones and migration guidance are reconciled below. Both
inventory files remain unchanged; no implementation or new source research was
needed for this revision.

## Scope and evidence

Replace confctl's Ruby implementation with Rust while retaining command meaning,
results, live logs, progress, colors and readable formatting. Replace the
configuration repository's two Ruby confctl scripts with built-in domain features
and typed opt-in Nix settings; adopt the useful Go invocation timing behavior.
The lead owns plan/state and commits; architect0 owns this design. No application
edits, builds, deployment or modification of the historical Go session occur here.

Baseline: canonical `repos/confctl.git`, Ruby `origin/master` observed at
`cc40679d267165aecfa569128438bb55fe910268`. Source files are inspected with
`git show` and a private read-only source copy at
`/tmp/2026-10-17-confctl-rust-rewrite-plan-architect0-confctl`. No refs or worktrees
were changed. The completed implementer inventories supply the exact site and Go
baselines and exhaustive command/script evidence, linked below.

## Proposed package boundaries for lead coordination

| Package | Owning files in future implementation | Dependencies | Acceptance |
| --- | --- | --- | --- |
| A: command and domain contracts | `src/cli/`, `src/domain/`, `tests/compat/` | Baseline inventory | Every built-in route/alias/option maps to a typed request and fixture |
| B: execution and presentation | `src/process/`, `src/events.rs`, `src/timing.rs`, `src/terminal/` | Frozen A interfaces | Joined child ownership; bounded live view; cancellation and timing tests |
| C: Nix, inputs and local state | `src/nix/`, `src/inputs/`, `src/generation/` | A and process interface | Existing Nix and on-disk contracts preserved; bidirectional Ruby fixtures |
| D: remote operations | `src/operations/`, `src/remote/`, `src/bin/` helper binaries | B/C interfaces | Deploy, rollback, health, carrier and GC effects match baseline |
| E: runtime kernels and netboot inventory | `src/runtime_kernels.rs`, `src/netboot_inventory.rs`, two typed Nix option modules; site settings only | A/B and inventoried behavior | Both script behaviors covered by direct core calls; disabled defaults have no feature effects |
| F: packaging, documentation and CI | `Cargo.toml`, lock/toolchain files, `nix/`, `.github/`, `docs/`, `man/` | Staged A–E outputs | Reproducible packages; format/lint/test and VM gates; closure audit |

Freeze shared interfaces first. Assign different file sets to implementers;
serialize manifest/Nix root edits and integration through the lead. The final
milestone table below splits these coarse boundaries into accepted slices.

## Consequential proposed decisions

- One Rust application with private modules and several remote helper binaries.
- No user extension API. Core runtime-kernel and netboot services use ordinary
  typed interfaces; site settings opt in. Confctl owns prompts, terminal rendering,
  machine selection and privileged operations.
- Preserve flake generation JSON, directory names, GC root names, Nix outputs,
  remote profiles and auto-rollback handshake; no schema migration by default.
- One process supervisor and one terminal owner. Domain code emits typed events,
  never terminal escapes. Timing is observational and cannot alter Nix operations.
- Final dependency versions require upstream maintenance/MSRV/license validation
  at implementation time; the plan records current primary-source evidence.

## Coordination limitation

The requested `report_to_lead` tool is not exposed in architect0's current tool
catalog. The permitted CLI fallback was attempted with unique message id
`architect0-boundaries-20261017-01`, but could not acquire
`/home/aither/.local/state/dev-workspaces/transition.lock` under this thread's
filesystem permissions. No assignment was sent. This artifact preserves the early
boundaries and decisions for lead inspection; no permissions were bypassed.

## Evidence reconciliation

Both completed inventories have been incorporated. Their exhaustive command and
behavioral matrices are part of this brief; the final sections record concrete
Nix settings, compatibility exceptions, implementation packages and acceptance
gates. Their original extension-mechanism recommendations are superseded.

## Architecture and Rust interfaces

Use one Cargo package (`src/lib.rs`, a thin `src/main.rs`, helper binaries and
private implementation modules). The library exists for integration testing, not
as a promised public Rust API. Core owns the two domain services and typed feature
settings; the site owns only its configuration and data. Do not turn every module
into a crate or port the Ruby class hierarchy.

The main data flow is:

```text
argv -> static clap command tree -> typed request
  -> typed Nix settings + selection (only when the command needs them)
  -> operation service -> Nix / Git / state / SSH / HTTP adapters
  -> typed events -> presentation model -> terminal or plain renderer
                         |                     |
                    timing ledger        sole input broker
  child bytes -> checked command log + command capture + bounded display tail
```

Core type proposals:

| Type | Meaning and invariant |
| --- | --- |
| `ConfigRoot`, `StorePath`, `MachineName`, `MachineKey`, `InputName`, `InputRole`, `GenerationName` | Validated newtypes; never interchange a display name, filesystem escape, flake key, store path and remote target |
| `Machine`, `MachineKind` | Typed known metadata plus retained JSON for custom attributes; direct/carrier/carried are explicit variants with validated references |
| `Selection` | Ordered machine IDs plus typed attribute/tag filters; exact machine name, then flake key, then Ruby-compatible glob resolution |
| `DeployRequest`, `SwitchAction`, `GenerationSelector` | Parsed once; default/switch/boot/test/dry-activate, explicit generation/current/offset selection represented explicitly after validation |
| `BuildGeneration`, `RejectedGeneration`, `CurrentResolution` | Supported state, excluded state with path/reason, and resolved/missing/invalid current pointer are different states |
| `ProcessSpec` | Program `PathBuf`/`OsString`, argv `Vec<OsString>`, cwd, environment changes, input policy, capture policy, operation ID and redacted display description |
| `ProcessOutcome` | Native status or signal, stdout/stderr captures, start/end instants and termination cause; failure is not a boolean |
| `TaskState` | Pending, running, succeeded, failed, skipped, incomplete/cancelled; zero observed activity never implies success |
| `OperationOutcome` | Ordered per-machine effects/results, partial completion and primary error; a view cannot change this result |

Use `Result<T, ConfctlError>` with a `thiserror` enum for parse/selection,
configuration, unsupported state, IO (path and operation), child failure (status
and log reference), decode, health failure, feature configuration/state failure,
cancellation and uncertain remote outcome. Attach context at adapter boundaries. Preserve the
first meaningful operation failure; append drain/log/terminal cleanup failures
as secondary diagnostics. Never replace a child error with an EOF or renderer
error, or report success after a required log write failed. Translate to the
baseline command exit policy only at `main`; do not expose clap's default exit
codes or Unix signal-derived statuses without checking baseline fixtures.

Keep selection, retention, lock graph resolution, Nix string escaping, output
formatting and state transitions pure. Use owned data and small borrowed views;
`Arc` is for immutable machine data and shared handles, not every object.
Boundaries requiring fakes are process execution, HTTP/transport, filesystem
publication and clock; do not add traits for every internal helper. Avoid
`unwrap`/`expect` on configuration, state or process inputs. Treat programmer
assertions separately. Avoid `unsafe` in application code; use maintained OS
wrappers and review any unavoidable platform-specific exception in one module.

### Execution, concurrency and cancellation

Proposed runtime: Tokio with explicitly selected process, IO, signal, time and
runtime features, plus `tokio-util::CancellationToken`. A `RunContext` owns the
token, process supervisor, log sink, timing ledger and terminal session.
Operations own a `JoinSet` (or equivalent scoped owner) and cannot return until
their children and output readers are joined. Parallel copy, checks, SSH and GC
use bounded permits matching current per-command limits; synchronous filesystem
work stays short or runs in a joined blocking worker. Preserve sequential and
`--one-by-one` semantics and deterministic result ordering independently of
completion order.

`ProcessRunner::run(spec, events, cancel)` starts a child, drains stdout and
stderr concurrently as bytes, writes stdin concurrently when required, closes it
at EOF, awaits native status, drains the final output and joins all readers.
Use bounded buffers for UI tails; large captures spool to owned files rather
than RAM. Progress events can coalesce by task ID; completion/error events and
raw log bytes cannot be silently dropped. The log writer establishes one merged
arrival order; no cross-pipe causal ordering beyond that is claimed. A log or
capture failure cancels the operation and remains visible. Bound incomplete
lines and decode incrementally across UTF-8 and escape-sequence chunk boundaries.

On Unix, give noninteractive local children an owned process group, record its
identity, signal that group on INT/TERM, stop scheduling new work, then escalate
after a bounded grace period and reap. `kill_on_drop` is only a last safeguard:
Tokio explicitly documents that dropping a child normally leaves it running and
that deterministic cleanup requires awaiting it
([process documentation](https://docs.rs/tokio/latest/tokio/process/index.html)).
Do not confuse killing local SSH with cancelling a remote effect. Report the
last known remote stage and retain logs; an interrupted activation may have
changed the system. Never kill a remote rollback watchdog merely because its
transport disappeared. The Rust helper must continue rollback on lost
confirmation, tolerate broken logging pipes and be tested across SSH disconnect.
Legacy helper interruption semantics remain a mixed-version test obligation.

Cancellation remains active during a prompt, stalled stdin, output flood,
blocked child input, Nix evaluation and cleanup. No detached `spawn_blocking`
stdin reader is allowed. A single input broker polls the input FD plus a wakeup
FD (through safe Unix bindings), reads only for an active prompt, and can be
joined on cancellation. It does not consume input while interactive SSH or a
pager owns it. Do not read beyond the current answer into a future child's input.
Secrets disable echo only for the prompt scope, restoring the exact termios
state on every exit. The general live view does not use raw input mode.

## Terminal, output and timing contract

Use Ratatui widgets with a Crossterm backend in an inline viewport, not a
fullscreen alternate-screen dashboard. Ratatui documents an inline viewport for
a UI embedded in normal CLI output
([viewport API](https://docs.rs/ratatui/latest/ratatui/enum.Viewport.html)).
This is a proposed fit, not a tested implementation. First prove that redraw,
resize, scrollback retention and prompt suspension work in real PTYs. Use its
Gauge/LineGauge and text widgets; do not run an independent Indicatif redraw
thread beside Ratatui. A small renderer model can fall back to direct Crossterm
commands if an upstream inline limitation is demonstrated, with the same single
owner and acceptance tests.

`TerminalSession` has explicit Idle, Live, Prompt and ExternalChild states. Only
it writes confctl UI bytes or reads operator answers. Operations send events;
they never print or call a prompt library directly. Pausing a live view drains
events and parks painting before a prompt receives ownership. Closing joins
readers, applies final states, paints once, retains that panel, and prints only
omitted task outcomes and a missing/clipped full log locator. Do not replay the
entire header or successful rows. External pager/SSH handoff flushes and restores
the terminal first, then resumes only after that child exits.

| Destination/mode | Required behavior |
| --- | --- |
| stdout and stderr both TTY, `CONFCTL_TTY` enabled | Inline live panel, full machine/input prelude once per build group, bordered tail and task rows; normal results remain in scrollback |
| Either stream redirected, `CONFCTL_TTY=0`, unusable terminal | Plain deterministic output on baseline streams; no cursor motion, hidden-key reader or control sequences except explicit forced color |
| `--color=always` / `never` / `auto` | Always overrides `NO_COLOR`; never disables confctl styling; auto considers actual destination and `NO_COLOR`. Color selection is independent of live-mode selection |
| Child output | Byte-preserving captures/logs; escape/control normalization only in the live display. Do not recolor or modify executed paths or returned child data |
| Pager / interactive SSH | Exclusive terminal and input lease; no simultaneous live repaint or timing footer for interactive SSH/CSSH |
| Error/cancel | Retained full log and per-host effects; restore terminal; final timing report only after all joins and log cleanup |

At a normal 80x24 terminal preserve approximately the Go/Ruby presentation:
compact Command/Started/Elapsed/operation/log information, at least twelve log
rows and at most five progress rows when space permits. Small terminals use the
available height without underflow; excess tasks have an explicit count, with
failed/incomplete tasks prioritized for membership but displayed in registered
order. Known positive totals show bars; unknown/zero totals show activity and
counts without invented percentages. Build row order is Building, Fetching,
optional combined Nix build, then Nix eval. An actual joined build succeeds
before later metadata evaluation; an evaluation failure cannot rewrite that
build outcome. Nix activity parsing is observational and cannot decide success.

Retain bold headings; yellow machines/actions, cyan generations, green success,
red failure, yellow skipped/incomplete. Width calculations use Unicode display
width and grapheme boundaries. Bars/count/detail columns align; narrow terminals
drop bars before hiding result text. Store hashes may shorten only in task
details when necessary; logs/state/argv keep full paths. The live tail is bounded
and does not require loading the whole retained log.

### Adopted Go elapsed-time behavior

Reference: Go experiment `009ca80cfca39634fc72e38b4002108a94194796`,
`docs/live-operations.md`, with private timing implementation to be anchored by
the CLI inventory. Earlier session records are context only; no Go source is
copied or modified by this plan.

Start one monotonic clock at main entry, before operational setup. Admit timing
after valid command/help checks for build, status, deploy, health-check, SSH
command mode, test-connection, collect-garbage, generation rm and rotate
(including runs that do not collect garbage). Live headers show local Started
and whole-second Elapsed across groups; do not reset on view changes.

Record RAII spans for actual evaluation, build (including fetching), copy,
deployment, status checks, reboot wait, health checks, SSH, connection checks and
GC work. For each phase take the union of its intervals, not the sum of parallel
tasks. Prompt intervals have their own union and may overlap background work.
Other is total minus the union of *all* work and prompt intervals. Therefore
phase sums may exceed total but Other cannot become negative. Use `Instant` for
durations and a separately captured local wall clock for RFC3339 start/end;
clock corrections must not change elapsed duration. RAII ends each span once on
success/error/cancel; snapshotting is read-only.

Print exactly one final original-stderr appendix after child/view/log cleanup,
also with piped output. Include command outcome, local start/end, nonempty phases,
prompt wait and prompt/work overlap if any, Other and independent Total;
millisecond precision is retained. The exact grammar comes from the inventory's
Go reference and golden fixture. stdout, child captures and help/version stay
unchanged. This stderr addition is an intentional requested presentation change,
not a new machine-readable API. Do not invent per-path timers or change Nix
arguments, progress producer requirements, retries or log transport to obtain it.

## Nix, persisted state and mixed-version operation

Nix remains the configuration evaluator and builder; Rust is the orchestrator.
Use the existing `nix` and `git` executables instead of reimplementing Nix APIs
or embedding libgit2. Preserve installables rooted at `.#confctl`, including
`settings`, `moduleOptions`, `machineNames`, `machineKeys`,
`machinesJson`, `buildPlan`, `inputs`, `inputsInfo`, and
`build.<machineKey>.{toplevel,autoRollback}`. Existing output fields and
`lib.mkConfctlOutputs`, module names and extra module arguments remain stable;
the two new opt-in settings groups are additive and absent groups mean disabled.
Do not regenerate flake keys with a subtly different Rust escaping algorithm;
consume the authoritative mapping. Preserve custom metadata for `ls`, filters,
the two core domain services and health command interpolation.

Port existing pure evaluation, explicit impure override and legacy NIX_PATH
behavior. Normal eval/build passes no-write/no-update-lock-file protections;
only input update/set may write the lock. Preserve narrowly detected Nix version
fallbacks and buffered stderr/JSON behavior; never retry a general child failure
as an older-Nix compatibility case. Lock graph handling must support aliases,
`follows`, raw sources, shared channel roles and path inputs as documented in
`docs/flake-inputs.md`. Update/set scope, shared-input refusal, changelog
direction, editor invocation, exact staged paths and commit behavior require
fixtures against the Ruby implementation. Do not broaden `git add` or discard
unrelated changes. Cache mirrors are caches, not authorization for input updates.

| Interface/state | Rust obligation | Rollback/mixed-version implication |
| --- | --- | --- |
| `.confctl/generations/<escaped-host>/<name>/generation.json` | Read/write explicit `mode: "flakes"`, ISO8601 date, toplevel, optional old rollback field, inputs and input metadata; accept existing `inputsInfo` alias while writing canonical `inputs_info` | Ruby flake readers must load Rust-created records and Rust must load old ones; no format bump |
| Generation names, paths, links | Keep timestamp names, host escaping, `toplevel`, `auto_rollback`, `<role>.input`, relative `current` link and selection semantics | Changing current is an ordinary build effect; retain old generations for explicit rollback |
| Unknown/corrupt/swpins/missing-mode records | Report path/reason, exclude, leave record and roots untouched; invalid current fails selection/local old removal/rotation; numeric selection fails when excluded records exist | Retained v3 handles old swpins; Rust does not add removed migration commands |
| GC roots | Preserve canonical real-config-path SHA256 namespace (first eight hex chars), login resolution and exact host/generation/suffix names under per-user gcroots | Moving configuration paths changes identity; JSON copies alone do not retain closures |
| `/nix/var/nix/profiles/system` and `confctl-<carried-alias>` | Preserve nix-env profile commands, IDs, link time interpretation and carrier-env callback ordering | Old/new operator tools can manage compatible remote profiles sequentially |
| `/etc/confctl/{inputs-info,configuration-info}.json` | Preserve field names, unknown/missing semantics, revision and dirty state | Old nodes without metadata remain operable and show unknown status; no coordinated fleet upgrade |
| Auto-rollback | Keep stored helper path and `-t TIMEOUT TOPLEVEL ACTION CHECK_FILE`; preserve switching/switched/confirmed file protocol | New CLI can invoke an old generation's Ruby helper; old CLI can invoke a Rust helper if protocol fixture passes |
| Netboot HTTP/TFTP files and JSON | Preserve machines/generations, URLs, MAC mapping, boot files, variants, kernel params, `inputs_info`, atomic root switch and locking | Old kexec client/new server and new client/old server must be tested |
| Logs and mirrors | Keep log location/retention meaning and readable logs; log text is diagnostic, not a deserialization format; caches can be recreated safely | Do not treat diagnostic layout changes as a state migration; never remove roots to clean a cache |

Publish new generation records through a same-filesystem temporary directory,
flush files, atomically publish under the existing timestamp name, install
required roots, then atomically replace current last. Hold an operation lock
under `.confctl` for Rust local mutations. Timestamp collisions must never
overwrite existing records: serialize and choose the next unused timestamp
without inventing a suffix old tools cannot parse. Recover only known staged
work whose ownership is proven; a failed publication preserves old current and
existing roots. A new lock is advisory: old Ruby does not honor it. The supported
contract is sequential old/new tooling, not concurrent writers to one checkout.
Document operator exclusion during cutover and test crash points. Remote profile
mutations likewise serialize per machine; do not claim a distributed transaction.

### Deployment and recovery implications (future work only)

Ship a selectable Rust candidate alongside a separately retained Ruby release
during acceptance, with distinct executable names in test shells. The final
default `confctl` becomes Rust only after parity gates. Keep the configuration
pin and explicit site settings on one tested compatible pair. Retain the old
configuration revision/scripts/environment for paired rollback; the migrated
configuration contains no user scripts. Preserve ignored state and config-root
identity when choosing a rollback checkout, as detailed below.

Order: prove local state round trips and isolated CLI/domain-feature fixtures;
package core/helpers and migrate site settings; test a disposable carrier/NixOS/
vpsAdminOS fleet; stage the configuration shell and metadata-only commands;
then a representative small build and explicitly authorized canary deploy.
Update carrier and kexec helpers opportunistically with their host generations;
the preserved protocol avoids a fleet-wide synchronized update. Operator tooling
rollback selects the retained Ruby environment plus its matching site scripts
and configuration revision. Machine rollback uses retained system generations
and closures independently. Never remove old local/remote roots during the
acceptance window; garbage collection can make rollback impossible.

Rust remote helper packages must be built for the deployed machine architecture,
not accidentally the operator architecture. Prefer helper outputs from confctl's
own supported pinned Rust toolchain for `pkgs.stdenv.hostPlatform.system` rather
than requiring every older per-machine nixpkgs to provide a new enough compiler.
Verify that old and new Nix module entry points can refer to these outputs and
that each helper's Nix closure includes its actual runtime executables. Preserve
NixOS and vpsAdminOS support on x86_64-linux and aarch64-linux; other platforms
need a separate proven support claim.

No database schema, seed, service daemon protocol or Terraform provider change
is required. The vpsAdmin HTTP API is a client-side dependency for data/secret
commands; its authentication and response contract needs fixtures, not a server
migration. User extension support is intentionally removed. The two inventoried
behaviors become built-in opt-in services; arbitrary other Ruby plugins have no
automatic migration. The Go experiment's extension SDK is outside this design.

## Reconciled sources and CLI parity gate

The completed [core inventory](inventory-confctl.md) is authoritative for all
29 built-in action leaves, every registered option/default/negative form, stream
and exit behavior, helper arguments and exact Go timing grammar. The completed
[site inventory](inventory-extensions.md) owns the exhaustive two-script mapping
and differential scenarios. They are part of this brief; their matrices are not
repeated here. Immutable reference set:

| Label | Revision | Meaning |
| --- | --- | --- |
| R/C | `cc40679d267165aecfa569128438bb55fe910268` | Locally available Ruby master |
| V | `3ae43f560ec7c0e6400322a5777118232dcdb26b` | Locally available site master |
| P | `7bee58a52372b95c2198ce3f2a719807a3c2c66b` | Confctl actually pinned by V |
| G | `009ca80cfca39634fc72e38b4002108a94194796` | Published Go experiment; historical automated acceptance, no default merge/deployment; visual walkthrough pending |

No fresh upstream or production identity is claimed. The site inventory checked
that its used extension surfaces agree between P and R.

**M0 must freeze executable fixtures before substantive replacement work.** Run
the retained Ruby package only in disposable fixtures with fake Nix/SSH/Git/API
services. Record argv, environment, independent stdout/stderr, exit status,
selected machines, prompts, file mutations and automatic refresh ordering. Cover every row of
the 29-leaf Ruby matrix, the site leaf promoted to core (30 actions in the Rust
plan) and four helpers. Make `tests/compat/cases.json`
(or equivalent checked-in manifest) require an owning case for every route and
option, with baseline revision and any narrowly approved variation. Completion
means all intended rows covered, not just successful `--help` snapshots.

| Families (all leaves listed in inventory) | Result/effect oracle and required edge cases |
| --- | --- |
| init/add/rename/rediscover | Exact allowed initial files, generated names/content/modes, rename behavior, sorted discovery, enabled netboot refresh after core write |
| inputs root/channel/machine | Selected root inputs, shared-input refusal, lock/original-reference preservation, commit/editor/changelog behavior, no cached fallback accepted as success |
| ls/build | Selection and columns; build grouping, matching generation reuse, current/roots; empty and excluded-state cases |
| deploy/health/status | Every action and copy-only/one-by-one/interactive/reboot/rollback branch; enabled kernel refresh before lookup/build; skip-current and missing-generation prompts; failed-host versus invocation outcome |
| changelog/diff | Role union/order, downgrade direction, missing metadata/offline behavior, pager, retrieval failure results |
| test-connection/ssh/cssh | Root/port/config/quoting/input; zero-argument SSH edge; interactive versus command mode; parallel completion-order output and aggregation; remote failure may still exit 0 |
| generation ls/rm/rotate/collect-garbage | Local/remote defaults, distinct unified versus per-host selector semantics, retention/current preservation, affected carrier GC and errors |
| gen-data vpsadmin all/containers/network | Authentication challenges, protected prompts, pagination, container/node and network output, atomic `.new` replacement and all-operation ordering |
| runtime-kernels update + automatic domain stages | Explicit and deploy scopes differ; nonfatal probe errors remove selected stale keys; full site scenario table applies |
| four remote helpers | CLI, filesystem effects, rollback handshake, carrier callback and old/new netboot consumers |

Clap is a parser implementation, not permission to change behavior. Preserve
options-before-positionals, negative switches, command prefix resolution,
ambiguity and help/completion plumbing where Ruby accepts them. Freeze framework
errors (normally bad command line 64, ordinary failure 1, normal action 0) and
verify signal/OptionParser edges. Do not add a successful `--version` route merely
because clap supports one. Do not add manual-only `deploy --outdated` or resolve
`allow_shared` versus `allow-shared` by assumption; M0 captures actual acceptance.
If both spellings are proposed later, record that as a separate additive change.

Keep confirmations on stdout even when piped. `--yes` suppresses their preview
block too. Preserve explicit y/n acceptance, blank/invalid-answer loops and EOF
failure, including action prompts; no non-TTY auto-yes. Keep different generation
selector algorithms where their ordering differs. Parallel SSH result order is
completion order, whereas kernel tables use selection order. This refines the
architecture's general ordering rule: order is a per-command contract.

Allowed rewrite differences are implementation language, removal of user extension
support with built-in replacements and explicit opt-in settings, the requested
timing appendix and similar terminal appearance. Atomic publication,
joined cancellation and bounded memory are implementation improvements; preserve
successful results and separately test failure behavior. Do not normalize entire
stderr, reorder result sets or suppress error codes in parity tests. The static
GC `progress.line`/`path` mismatch needs one targeted oracle fixture; do not encode
an unproven crash as intended functionality or quietly claim it fixed.

For timing, use the exact G footer grammar in the core inventory: initial/final
LF, `Timing: completed|failed|canceled (exit N)`, local Started/Ended, seen phases
in prescribed order, always Prompt wait/Other/Total, conditional overlap and
conditional overlap note, truncated three-decimal durations. Resolve the actual
Rust executable status before freezing the footer. A footer-write failure makes
an otherwise successful invocation fail with 1, preserves a prior nonzero status,
and is neither retried nor recursively reported. No Rust prototype entrypoint or
130/143 policy is implied by the Go prototype.

## Built-in runtime kernels and netboot inventory

The replacement is two domain services, not an extensibility framework. Core owns
`src/runtime_kernels.rs`, `src/netboot_inventory.rs`, the static CLI declaration,
settings decoding and ordinary operation call sites. They use the existing typed
inventory, process, file-publication and presentation services directly. No user
program can register commands or callbacks; no registry, protocol crate, SDK,
dynamic command tree or separately compiled site binary is planned.

The reusable mechanisms are running `uname -r` against machine identities,
merging kernel state and generating a Nix list from netboot metadata. Site policy
is limited to enabling those features, choosing output paths and enabling the
pre-deploy refresh. Keep the observed selection and normalization semantics as
fixed feature behavior for the initial port; do not generalize them into arbitrary
commands, predicates, serializers or event subscriptions.

### Typed configuration and defaults

Add `nix/modules/confctl/runtime-kernels.nix` and
`nix/modules/confctl/netboot-inventory.nix`, register them in the settings/module
option exports and document them in the generated option reference. The existing
`.#confctl.settings` output gains two additive groups; no new evaluation endpoint
or plugin discovery is needed. Rust readers of older settings default both groups
to disabled. These settings only describe operations; Nix evaluation itself must
never probe SSH, refresh files or run an operator command.

Proposed site `configs/confctl.nix` additions:

```nix
{
  confctl.runtimeKernels = {
    enable = true;
    stateFile = "configs/node/kernels.json";
    refreshBeforeDeploy = true;
  };

  confctl.netbootInventory = {
    enable = true;
    outputFile = "cluster/netbootable.nix";
  };
}
```

| Option | Type/default | Contract |
| --- | --- | --- |
| `runtimeKernels.enable` | bool / false | Enables the built-in update operation for this configuration |
| `runtimeKernels.stateFile` | null or relative-path string / null | Required when enabled; no implicit output path or state migration |
| `runtimeKernels.refreshBeforeDeploy` | bool / false | Requires enable; refreshes once at the existing pre-build deployment stage |
| `netbootInventory.enable` | bool / false | Enables regeneration after add/rename/rediscover writes the core list |
| `netbootInventory.outputFile` | null or relative-path string / null | Required when enabled; contains the generated literal Nix list |

Use strings rather than Nix path values so ignored mutable files are not copied
into the store. Decode to `RuntimeKernelSettings`, `NetbootInventorySettings` and
validated `ConfigRelativePath` Rust types. Reject absolute paths, traversal,
symlink escapes, identical destinations and reserved core files such as
`flake.nix`, `flake.lock` and `cluster/cluster.nix` before feature effects. Require
an existing parent directory; do not create a new site tree implicitly. Resolve
against the canonical live configuration root. These are domain-specific options,
not a generic file-generation DSL or code-execution capability list.

`runtime-kernels update [machine-pattern]` becomes a statically registered core
command with the existing show-trace/attribute/tag/yes options. Help requires no
configuration or execution. Invoking the operation when disabled fails with a
clear enablement message before probes/state access. This adds a visible core
help entry outside this site, but default deploy, build, inventory and rediscover
perform no new kernel probes or netboot writes. Enabling runtime kernels alone
does not enable automatic deploy refresh. Both features stay independent.

### Exact operation ordering and outcomes

**Explicit kernel update:** validate command and enabled settings; evaluate and
select by the existing exact-name/key/glob and attr/tag rules; keep only
vpsAdminOS entries, including unmanaged and carried entries; run the unchanged
confirmation/preview policy; acquire the mutation lock and load the state; run
concurrent `uname -r` requests; join every request; render the ordered table and
error diagnostics; merge and atomically replace the file; invalidate dependent
Nix caches. No hidden runnable filter or carrier-target substitution is allowed.
Zero selected machines still follows the existing prompt/header/save path.

**Deploy:** validate action/options and obtain the usual managed-machine
selection; confirm using the existing preview/yes rules; if enabled, take the
non-carried vpsAdminOS subset of that confirmed scope; if empty, do not read the
state, query hosts or print a kernel banner. Otherwise print the existing bright
banner, run the shared update routine without another prompt and print its final
blank line. Wait for publication and invalidate inventory/build-plan/input
memoization dependent on the changed checkout. Only then look up a requested
generation or evaluate build inputs/build systems, query current targets and
continue copy/activation/reboot/health. Keep the confirmed scope fixed across
cache refresh; do not add newly discovered targets.

This refresh runs for switch, boot, test, dry-activate, copy-only, selected
existing generations and hosts later skipped as already current. It does not run
for standalone build/status/health/SSH, or an invalid/declined/empty deploy.
Inventory/settings evaluation needed for selection may precede refresh; actual
build-input evaluation must observe the published file. Do not move refresh
inside per-host one-by-one execution or repeat it on health retries. That would
change scope/timing and writes relative to the original pre-deploy hook.

**Netboot list:** add/rename/rediscover performs its existing core writes,
including the new `cluster/cluster.nix`; invalidate inventory and evaluate a
fresh full machine list; when enabled, select `netboot.enable == true` and
non-carried entries, without spin/managed/runnable restrictions; retain evaluated
order; print the replacement notice and atomically replace the configured file.
No SSH or extra confirmation is introduced. Evaluation/write failure fails the
parent operation and leaves earlier core writes intact, as today. No automatic
retry or invented multi-file transaction. A rename still does not rewrite stale
kernel JSON keys.

Preserve the kernel policy exactly: successful stdout is stripped, split on dots
with Ruby's trailing-empty behavior, truncated to three parts and rejoined;
suffixes and empty successful values remain. Successful literal `error` leaves an
old value unchanged. Ordinary nonzero command/SSH status prints an error and
deletes only that selected host's prior key; all such failures still allow normal
successful completion after saving. Spawn/infrastructure, malformed JSON and
read/write failures remain invocation failures. No new probe deadline or default
connection-test timeout is introduced. Table order is selection order; error
paragraph order may follow completion. Preserve permissive legacy JSON behavior
and unselected values, including the zero-machine reserialization cases; do not
quietly normalize bad state or add a schema wrapper.

Core still owns terminal/input/log/process cancellation. There is no second
extension child to supervise. Cancel/join probes before return and never publish
an incomplete merge as success. Atomic replacement plus the configuration
mutation lock protects completed publication; old Ruby writers do not honor the
lock, so concurrent old/new writers remain unsupported. Preserve original
successful file bytes/formatting and test interrupted-write failure behavior
separately. Bounded scheduling may change active worker count, not the selected
set or result/exit contract. Reuse existing timing admission; the standalone
kernel command does not gain a new timing appendix by this planning change.

### Concrete source migration and compatibility

| Current source/data at V | Replacement and ownership |
| --- | --- |
| `scripts/runtime_kernels.rb` | Core runtime-kernel service, static CLI action and direct pre-deploy call; remove the script after acceptance |
| `scripts/discover_netbootable.rb` | Core netboot inventory service called by the rediscover owner after its write; remove the script after acceptance |
| `configs/node/kernels.json` | Same ignored JSON file, same full machine-name keys and merge/deletion semantics; explicitly selected by the site setting |
| `configs/node/kernels.nix`, `configs/node/base.nix` | Retain live PWD-based read, manual runtime override then JSON then default, and existing kernel consumer; no forced generic core kernel policy |
| `cluster/netbootable.nix`, `lib/netboot-machines.nix` | Retain tracked generated list and carrier aliases/tags/attributes/PXE consumers |
| `configs/confctl.nix` | Site enables the two typed features and selects its current paths |
| Site `flake.nix`/lock and tools shell | Select compatible Rust confctl/Nix option definitions; no extra package/registry/runtime compilation |

Keep `cluster/netbootable.nix` in the initial migration. A purely Nix-derived list
might remove one generated file, but current carrier declarations consume that
list while contributing to the evaluated inventory; deriving it naively from
expanded inventory risks recursion and changes rediscover/file-diff behavior.
That is a separate possible improvement requiring a deliberate pre-carrier
metadata design and consumer migration, not a simplification needed for this port.

Prepare the new core package and options first. In one reviewed site transition,
update its confctl pin, add explicit settings, remove the two script files and
update documentation. Verify fixtures and live-root file compatibility before
using the migrated shell. Retain data unchanged; do not regenerate or delete the
ignored JSON as an installation step. No feature source, Cargo package, protocol
crate or callback remains in the site repository. Its other 31 Ruby files and
Gemfile/test/tooling remain unrelated and supported.

| Tool/configuration combination | Supported meaning |
| --- | --- |
| New Rust + old config without scripts/settings | Existing core behavior; both new features disabled |
| New Rust + old config with regular legacy script files | Fail operational preflight with migration guidance before mutation; never silently omit their behavior or execute them; help remains available |
| New Rust + migrated site pin/settings/no scripts | Both opt-in services preserve current site operation and files |
| Old Ruby + migrated site | Unsupported: old option definitions can reject new settings, or old CLI can miss refreshes after scripts are removed; no claim of tool-only rollback |
| Retained old Ruby + matching old site revision/scripts | Rollback pair reads retained files written by Rust; preserve local root/path and closures |
| Old/new running nodes and carrier helpers | Existing remote/profile/netboot contracts remain; no fleet-wide coordinated update required |

Rollback restores the matching previous configuration revision, option modules,
confctl pin and Ruby scripts together, then reenters that environment. Preserve
ignored kernel JSON in the same live root (or explicitly transfer it when using a
separate retained checkout); a Git checkout alone does not copy ignored state or
GC-root identity. Restore tracked netboot data consistently and retain closures.
Rollback does not undo successful file updates, failed-host key deletion or
already-deployed systems. No database/API schema migration is introduced.

### Simplification and remaining tradeoffs

The plan removes extension registration/discovery, JSON framing/versioning,
capability services, cross-process rendering/prompts, dynamic help, protocol
conformance tests, SDK publishing and a second Cargo/Nix package/pin. Core
already has the selection/SSH/UI/file services these two features need. Reuse
those directly and keep the new modules small.

The functionality itself still needs code, tests, settings documentation and
compatibility maintenance. Core now owns these features for all users, so false
defaults and negative-effect tests are mandatory. New customization requires an
ordinary core feature change or separate external tooling, rather than arbitrary
user commands/hooks. Accept that limitation deliberately; do not retain an unused
plugin framework or reintroduce it as configurable shell commands. Keeping the
netboot file and existing kernel edge semantics trades some elegance for a
smaller, safer compatibility change.

## Maintained dependency candidates and limits

These are proposed choices, not installed or compiled dependency claims. Primary
repositories/docs were inspected on 2026-10-17. Release lists and maintained
project documentation support candidate selection; maintenance, advisories,
licenses, transitive size and MSRV must be rechecked when locking versions in M1.
Do not infer a latest compatible version from this planning snapshot.

| Candidate | Use and evidence | Constraint |
| --- | --- | --- |
| [clap](https://github.com/clap-rs/clap/releases) | Active release list (observed v4.6.5); static built-in command definitions | Explicit Ruby parser adapter/fixtures; default clap policy is not the contract |
| [Tokio](https://github.com/tokio-rs/tokio), tokio-util | Process/IO/signal scheduling and cancellation; current process docs inspected | Select features; explicit joins/process groups remain application responsibility |
| [Ratatui](https://github.com/ratatui/ratatui), [Crossterm](https://github.com/crossterm-rs/crossterm/releases) | Widgets/inline terminal and backend; inline docs observed at 0.30.2, Crossterm release list includes 0.29 | Real PTY spike required; no fullscreen/raw-mode default |
| [Indicatif](https://github.com/console-rs/indicatif/releases) | Maintained progress alternative with current release history | Not selected alongside Ratatui; avoid two render owners |
| [Serde](https://github.com/serde-rs/serde) + serde_json | Typed JSON state, settings and Nix/HTTP data with bounded decode | Preserve unknown metadata and old field aliases explicitly |
| [thiserror](https://github.com/dtolnay/thiserror) | Domain error enums | `anyhow` only optional top-level context, not domain error contracts |
| [rustix](https://github.com/bytecodealliance/rustix) | Safe Unix bindings for process/input/locking helpers | Confirm needed API/version; platform code stays isolated |
| [unicode-width](https://github.com/unicode-rs/unicode-width), unicode-segmentation | Display width and grapheme-safe clipping | Segmentation version/MSRV review remains M1 work |
| [chrono](https://github.com/chronotope/chrono) | Local timezone/RFC3339 and retained generation dates | `std::time::Instant` owns durations; no wall-clock duration subtraction |
| [reqwest](https://github.com/seanmonstar/reqwest) with rustls | vpsAdmin client and HTTP downloads where needed | Preserve authentication, TLS/proxy and response semantics; no new general HaveAPI SDK required |
| tempfile, sha2, a small glob adapter | Safe staging, existing SHA256 namespace and Ruby-compatible patterns | Candidates not yet audited; glob behavior needs explicit fixtures (slashes/dots/escapes/braces), not blind substitution |
| [assert_cmd](https://github.com/assert-rs/assert_cmd), [proptest](https://github.com/proptest-rs/proptest), [insta](https://github.com/mitsuhiko/insta) | CLI, invariant/property and selected presentation snapshots | Test-only; snapshots do not substitute for process/effect assertions |

Use Rust edition 2024 with a concrete stable compiler pinned by
`rust-toolchain.toml`, `rust-version` and the Nix dev shell once the candidate
set's MSRVs are checked. Commit Cargo.lock, minimize features, audit licenses
against confctl's GPL-3.0-only and produce notices. Avoid an embedded JS/Lua/Wasm
runtime, Rust cdylib ABI, SSH library or libgit2 dependency for this scope. They
add a second contract without solving the observed two-script requirements.

## Full Ruby removal and packaging boundary

Replace application `bin/confctl`, `lib/**/*.rb`, all four installed helpers,
ERB/manual generation and Ruby-owned release/package machinery. Proposed helper
binaries: `confctl-auto-rollback`, `carrier-env`, `build-netboot-server`,
`kexec-netboot`, in `src/bin/` with logic in `src/remote/`. Preserve their existing
public invocations and generated data. `build-netboot-server` needs a real port
of profile scanning, locks, HTTP/TFTP tree generation, menus, variants and atomic
publication; it is not a shell-wrapper-sized task. Replace ERB with small typed
renderers/templates preserving outputs, and generate man/options documentation
from the CLI and Nix option data without Ruby.

`nix/package.nix` becomes `rustPlatform.buildRustPackage` with locked Cargo
sources, installed manuals, wrapper runtime PATH (Nix/Git/OpenSSH and actual
helper tools), separate helper outputs if useful and platform-specific checks.
Update `flake.nix`, `mk-confctl-devshell.nix`, helper modules and autoRollbackFor.
Keep public package/lib/module outputs compatible; new checks can replace Ruby
checks under documented names. The old `bundled-confctl` shell mode cannot keep
its promise of Ruby imports: explicitly deprecate/refuse it with migration
instructions or provide a name alias to tools mode only after callers are
migrated; never pretend embedded Ruby remains available. Minimal/tools modes
remain supported. Retain legacyCompat behavior only where independently needed,
with fixtures; do not remove unrelated exports as collateral cleanup.

Port RSpec application tests to Rust as their owners port behavior; retire the
old suites only after equivalent assertions pass. The external vpsAdminOS test
runner's Ruby/RSpec DSL may remain a **test-only** dependency. Owned runner helper
business logic should move to a Rust fixture binary where practical; do not
rewrite the external framework. Audit runtime package closures independently of
test/dev shells: confctl CLI and new helper outputs must not require Ruby,
Bundler, Gem paths or a hidden Ruby fallback. Old retained generations may still
reference their old Ruby helpers, intentionally for rollback.

In the site repository delete only the two migrated confctl scripts after the
built-in replacements and explicit settings pass acceptance. Keep its other 31
Ruby files, Gemfile/test hooks and tools mode: they belong to vpsAdmin, services, specs and development tooling. No claim
of a Ruby-free site or fleet follows from a Ruby-free confctl runtime.

`gen-data` needs a small Rust vpsAdmin/HaveAPI client adapter, not a skipped or
Ruby-backed command. Freeze the current client authentication endpoint discovery,
server-specified challenge/protected fields, fixed token lifetime, pagination and
error behavior using a mock HTTP server. Generate identical Nix values for
container/node metadata and IPv4/IPv6 network lists. TLS/proxy/default endpoint
behavior and source client revision are M0 acceptance inputs; do not invent
endpoint paths or add a server migration. Keep credentials out of command logs,
HTTP traces and fixtures.

## Verification and GitHub workflows

All commands below are future implementation gates; none was run for this plan.
Use the repository's Nix development environment. Preserve workspace policy:
quick checks and committed deliverable review precede long VM/integration checks;
long/uncertain work uses the designated verification watcher. This planning-only
artifact itself does not trigger mandatory review.

Quick checks per package: `cargo fmt --all -- --check`,
`cargo clippy --workspace --all-targets --locked -- -D warnings`, focused
`cargo test --locked`, Nix formatting, fixture manifest coverage and generated
documentation drift. Full `cargo test --workspace --locked` is a broader gate
when needed; avoid repeatedly running everything for documentation-only edits.

Independent acceptance layers:

1. Pure properties: selection/globs/stringification, distinct generation
   selectors/retention, flake lock aliases/follows, Nix escaping, state publication
   failure points, progress chunk boundaries and interval unions.
2. Differential CLI/effects fixtures: all 29 leaves, all options/defaults/negative
   forms, site cases and helper contracts, exact raw stdout/stderr/exit retained.
   A strict footer splitter permits only the requested timing suffix.
3. Real process/PTY tests: held child visibly updates before exit, flood both
   streams, missing/failing executable, blocked input, slow readers, INT/TERM,
   descendants and no remaining processes; prompt/EOF/echo restoration, resize,
   80x24/tiny/Unicode/forced-color and either stream piped. Compare bytes and
   screen state plus ordering; final-frame snapshots alone are insufficient.
4. Built-in feature contract: disabled defaults cause no probes or generated-file
   writes; explicit enablement/path validation, static help, correct scopes and
   operation order, live-root/cache refresh, nonfatal host errors, joined
   cancellation and atomic publication. Both Ruby-to-Rust and Rust-to-Ruby file
   round trips; paired old/new settings migration and legacy-script refusal. Use
   the site inventory's behavioral cases; its protocol/registry cases are superseded.
5. Nix/package/native VM: x86_64-linux and aarch64-linux packages; isolated
   NixOS/vpsAdminOS deploy, auto rollback, carrier/deploy and carrier/netboot
   suites; old/new CLI-helper and netboot reader/writer combinations. Verify
   native results and no unexpected local kernel build; no production access.
6. Operator acceptance: similar live presentation, prompt flow, visible elapsed
   time and log inspection in the packaged site shell. Automated success alone
   does not establish this visual preference.

Proposed workflows:

| File/job | Trigger and execution | Required evidence |
| --- | --- | --- |
| `.github/workflows/rust.yml` format/lint/unit | Push and pull_request; pinned toolchain; fmt, clippy, locked unit/CLI/domain-feature tests on Linux | Separate streams and failure logs; no production credentials |
| Same workflow package/platform jobs | x86_64 native and aarch64 native or supported builder; locked Nix package checks | Real architecture execution where claimed; cross compilation alone is not a run |
| `.github/workflows/tests.yml` | Keep self-hosted authorized VM suite path/dispatch model; add Rust/feature-option/helper inputs to path filters | Actual suite result evaluation, logs/artifacts on failure/cancel, isolated owned test state |
| Dependency/license job | Scheduled and relevant PR changes; selected advisory/license tool | Reviewed lock/advisory update, documented exceptions rather than blanket ignores |

Retire Ruby rspec/rubocop workflows only when replacement coverage and remaining
file responsibilities are resolved. Check latest compatible imported action refs
from official upstreams when authoring workflows; this plan does not prescribe
remembered versions. Use contents:read, branch concurrency cancellation and
bounded job timeouts. Never cancel unrelated branch runs. Use runner-owned GC
roots/state instead of copying the current broad per-user GC-root deletion into
shared runners. Test fixtures must never invoke real deployment targets through
an accidental PATH or inherited configuration.

## Implementation milestones and independent work packages

Owners below are execution slots for the lead to assign from the retained roster,
not new team members. Shared root manifests/wiring are serialized. Every package
owns focused tests and lasting project docs with its code. Architect owns design
revisions and resolves deviations through the lead.

| Milestone/package | Files and independent boundary | Dependencies | Acceptance/checks |
| --- | --- | --- | --- |
| M0: compatibility contract | `tests/compat/`, fixtures and `docs/compatibility.md`; one owner captures Ruby, another site/helper fixture data | Read-only R/P/V/G baselines | Complete route/option manifest and executable exit/stream/side-effect oracle; discrepancies adjudicated before port |
| M1a: domain/parser foundation | `src/cli/`, `src/domain/`, `src/error.rs`, configuration/selection tests | M0 | Typed requests preserve parser/selection quirks; no CLI policy guessed from clap |
| M1b: process/events/timing | `src/process/`, `events.rs`, `timing.rs`, owning tests | Frozen M1 interfaces (can use fixture types) | Concurrent drains, cancellation and join proofs; exact timing ledger/footer tests |
| M1c: typed feature configuration | `nix/modules/confctl/{runtime-kernels,netboot-inventory}.nix`, settings types, option fixtures and `docs/runtime-kernels.md`/`docs/netboot-inventory.md` | M0 site behavior contract | Disabled defaults, validated paths and explicit enablement; stable internal service inputs/results, no public SDK |
| M2a: Nix/inputs/configuration | `src/nix/`, `src/inputs/`, `src/configuration/`, owning tests | M1a/b | Inventory/init/inputs/lock/Git effects pass; no accidental input update on build |
| M2b: generations/status | `src/generation/`, status domain/adapter and tests | M1a/b; Nix interface | Round trips, roots/current crash points, family-specific selectors and unknown metadata |
| M2c: presentation | `src/terminal/`, `src/presentation/`, PTY tests | M1a/b | One owner; prompt/pipe/color/scrollback/cancel/live timing acceptance |
| M2d: core domain features | `src/runtime_kernels.rs`, `src/netboot_inventory.rs`, focused tests; owner-assigned deploy/rediscover call sites | M1c, M1b, selection/renderer interfaces | Both script scenarios preserved; explicit/deploy scopes, write ordering and cache invalidation; no default side effects |
| M3a: operations | `src/operations/{build,deploy,health,ssh,connection,gc,compare}.rs` and owning tests | M2 adapters/UI | All built-in operation fixtures including partial failure/result/exit and scheduling order |
| M3b: remote helpers | `src/bin/` helpers, `src/remote/`, netboot templates/helper tests | Process/state contracts; separate Nix integration owner | Four Ruby helpers replaced, mixed-version protocol/index tests, watchdog disconnect behavior |
| M3c: vpsAdmin/data generation | `src/vpsadmin/`, `src/operations/gen_data.rs`, HTTP fixtures | M0 API fixtures, process/UI | All three gen-data leaves including challenge auth and error/file semantics |
| M4: packaging/docs/CI | Cargo roots/locks, `nix/`, `flake.nix`, workflows, man generation, README/upgrade docs; site flake pin/settings, script removal and upgrade notes separately | Accepted M2/M3 packages | Locked runtime closure audit, shell modes, helper architectures, docs/workflow drift, no embedded Ruby |
| M5: acceptance and cutover preparation | Integration/PTY/mixed-version tests and dated rollout record | Quick checks + committed independent review | Native VM and operator visual acceptance, exact final compatible pair and retained rollback path; merge/deploy remain separately authorized |

With two implementers, start M1a/M1b after the shared brief freezes; then pair
M2a with M2b, then M2c presentation with M2d core domain features. M3 remote
helpers can proceed beside operation assembly after stable process/state APIs;
move vpsAdmin and packaging into freed slots. Do not let both owners edit
`main.rs`, Cargo manifests, root Nix exports or shared terminal/event types
concurrently. Integration changes get an explicit small assigned file package.
No calendar estimate is claimed: M0 parser/API findings and remote-helper size
are the largest uncertainty. Each milestone produces a usable, reviewable slice,
not an all-or-nothing rewrite branch with deferred tests.

## Explicit uncertainties, risks and decisions left for execution

- Exact GLI abbreviations, negative aliases, option ordering, version/help,
  surplus args, signal status, allow_shared spelling and the static GC mismatch
  require executable M0 evidence. Compatibility takes precedence over convenient
  cleanup; unresolved cases cannot silently become clap defaults.
- Dependency candidates were researched, not locked/built/audited. Confirm MSRV,
  licenses, advisories and Nix availability; prove inline Ratatui behavior in a
  PTY before investing in the renderer. Choose one maintained UI stack.
- vpsAdmin client auth/discovery/pagination/TLS defaults need source/fixture
  qualification; retaining a Ruby fallback does not satisfy completion.
- Old rollback-helper survival after transport loss is not proven by static
  source. Preserve wire compatibility and test both directions; a discovered
  incompatibility must change the rollout contract before cutover.
- Atomic writes improve interrupted-write safety but do not undo earlier feature
  writes, remote effects or failed-host kernel deletion. Old Ruby does not honor new
  locks. Exclude concurrent writers and retain closures, not just JSON backups.
- `bundled-confctl` and arbitrary Ruby imports cannot remain source-compatible.
  This intentional removal of extension support needs clear upgrade guidance and
  paired tool/settings rollback; minimal/tools and the actual site's unrelated
  Ruby tools remain supported.
- Source timing behavior is accepted for adoption; exact human visual preference
  still requires a walkthrough of the future Rust implementation. Historical Go
  passes are not Rust test evidence.

No unresolved question blocks completion of this plan. These are explicit gates
for future implementation, not permission to run builds, deploy or merge now.

## Final architect report

**DESIGN COMPLETE — built-in-feature revision ready for lead handoff.**
Recommend removing extension support and implementing runtime-kernel collection
and netboot inventory as opt-in core services. Registry/protocol/SDK/site-package
work is removed; preserved files, operation ordering, defaults and paired rollback
are explicit. Feature logic, Nix contracts and tests remain maintenance duties.
Both completed inventories are reconciled; all requested CLI, presentation, timing,
Rust architecture, dependencies, built-in feature migration, Ruby removal,
compatibility, recovery, CI and implementation-package topics are covered.

Only `design.md` was written by architect0. Investigation used immutable source
inspection, historical read-only context and primary dependency documentation.
No project edits, prototype, application tests/builds, commits, deployment,
merges, roster changes or lifecycle actions occurred. Runtime parity and package
claims remain future acceptance gates. The lead owns final plan/state, artifact
registration and serialized tracking commits. No further architect edits are
planned unless the lead identifies a concrete acceptance issue.
