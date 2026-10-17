# Rust confctl replacement design

Status: **DESIGN COMPLETE — reconciled with both completed inventories.**
Planning only: this is an implementation proposal, not permission to implement,
merge or deploy.

## Recommendation and implementation order

Build an idiomatic Rust orchestrator around the existing Nix/SSH contracts, with
Tokio for owned asynchronous processes and Ratatui/Crossterm for one inline live
view. Replace the two site Ruby scripts with one separately packaged Rust
executable using a small versioned JSON protocol. Preserve current generation
files, GC roots, profiles and netboot data; adopt the Go invocation timing report.

Start by freezing an executable Ruby CLI/effects fixture contract, including
every option default, stdout/stderr route and exit code. Then implement shared
types/process/UI interfaces, Nix and state adapters, remote operations, and the
site extension in parallel file packages. Port all remote Ruby helpers and the
data-generation client before switching packaging. Finish with differential,
real PTY, mixed-version and disposable VM acceptance; replace the default only
after those gates. Full package dependencies and checks appear below.

These architectural directions have been accepted by the lead as planning
recommendations, subject to source reconciliation. They do not authorize the
future implementation or cutover. The current phase is lead acceptance and planning handoff.

## Scope and evidence

Replace confctl's Ruby implementation with Rust while retaining command meaning,
results, live logs, progress, colors and readable formatting. Replace the
configuration repository's Ruby confctl extensions through an explicit executable
protocol and adopt the useful invocation timing behavior from the Go experiment.
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
| E: extension protocol and site port | `crates/confctl-extension-protocol/`, `src/extensions/`; site `extensions/confctl-site/` | A/B and inventoried hooks | All site scripts map to concrete requests/actions; no Ruby runtime |
| F: packaging, documentation and CI | `Cargo.toml`, lock/toolchain files, `nix/`, `.github/`, `docs/`, `man/` | Staged A–E outputs | Reproducible packages; format/lint/test and VM gates; closure audit |

Freeze shared interfaces first. Assign different file sets to implementers;
serialize manifest/Nix root edits and integration through the lead. The final
milestone table below splits these coarse boundaries into accepted slices.

## Consequential proposed decisions

- One Rust application with private modules, several small remote helper binaries,
  and only a small public extension protocol crate if shared by the site port.
- Subprocess extensions instead of Rust dynamic linking or embedded Ruby. Confctl
  owns prompts, terminal rendering, machine selection and privileged operations.
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
script matrices are part of this brief; the final sections record concrete wire
examples, compatibility exceptions, implementation packages and acceptance gates.

## Architecture and Rust interfaces

Use a Cargo workspace with the application at its root (`src/lib.rs`, a thin
`src/main.rs`, and private implementation modules). The library exists for
integration testing, not as a promised public Rust API. Put the shared wire types
in `crates/confctl-extension-protocol`; publish/version that crate only if an
external consumer needs it. Site code stays in the configuration repository and
depends on an exact released protocol crate or a pinned source revision. Do not
turn every module into a crate or port the Ruby class hierarchy.

The main data flow is:

```text
argv + static extension manifests
  -> clap command tree -> typed request + selection
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
and log reference), decode, health failure, extension failure, cancellation and
uncertain remote outcome. Attach context at adapter boundaries. Preserve the
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
`unwrap`/`expect` on configuration, protocol or process inputs. Treat programmer
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
`build.<machineKey>.{toplevel,autoRollback}`. The exact output shapes and
`lib.mkConfctlOutputs`, module names and extra module arguments remain stable.
Do not regenerate flake keys with a subtly different Rust escaping algorithm;
consume the authoritative mapping. Preserve custom metadata for `ls`, filters,
site extensions and health command interpolation.

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
pin and site extension package on one tested compatible pair. Retain a separate
old configuration checkout/environment for rollback; do not leave two active
extension mechanisms in the production default shell.

Order: prove local state round trips and isolated CLI/extension fixtures;
package core/helpers and site extension; test a disposable carrier/NixOS/
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
migration. The new extension protocol is intentionally a new public boundary;
old in-process Ruby plugins require a port. The Go experiment's extension SDK is
not selected as a supported Rust wire contract merely because it exists.

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
selected machines, prompts, file mutations and hook ordering. Cover every row of
the 29-leaf matrix, the site leaf and four helpers. Make `tests/compat/cases.json`
(or equivalent checked-in manifest) require an owning case for every route and
option, with baseline revision and any narrowly approved variation. Completion
means all intended rows covered, not just successful `--help` snapshots.

| Families (all leaves listed in inventory) | Result/effect oracle and required edge cases |
| --- | --- |
| init/add/rename/rediscover | Exact allowed initial files, generated names/content/modes, rename behavior, sorted discovery, hook after core write |
| inputs root/channel/machine | Selected root inputs, shared-input refusal, lock/original-reference preservation, commit/editor/changelog behavior, no cached fallback accepted as success |
| ls/build | Selection and columns; build grouping, matching generation reuse, current/roots; empty and excluded-state cases |
| deploy/health/status | Every action and copy-only/one-by-one/interactive/reboot/rollback branch; hook before lookup/build; skip-current and missing-generation prompts; failed-host versus invocation outcome |
| changelog/diff | Role union/order, downgrade direction, missing metadata/offline behavior, pager, retrieval failure results |
| test-connection/ssh/cssh | Root/port/config/quoting/input; zero-argument SSH edge; interactive versus command mode; parallel completion-order output and aggregation; remote failure may still exit 0 |
| generation ls/rm/rotate/collect-garbage | Local/remote defaults, distinct unified versus per-host selector semantics, retention/current preservation, affected carrier GC and errors |
| gen-data vpsadmin all/containers/network | Authentication challenges, protected prompts, pagination, container/node and network output, atomic `.new` replacement and all-operation ordering |
| site runtime-kernels update + hooks | Explicit and deploy scopes differ; nonfatal probe errors remove selected stale keys; full site scenario table applies |
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

Allowed rewrite differences are implementation language, new extension source
API, requested timing appendix and similar terminal appearance. Atomic publication,
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

## Extension protocol and site replacement

Use one configuration-owned package at `extensions/confctl-site/`, with
`src/{main,runtime_kernels,netboot}.rs`, `Cargo.toml`, committed `Cargo.lock`, and
`package.nix`. Core owns `crates/confctl-extension-protocol/`, `src/extensions/`
and the authoritative `docs/extensions.md`. Site docs link that contract and
explain its concrete handlers. Rust's native ABI is not a plugin boundary;
subprocesses also permit future extensions written in another language without
exposing private core modules.

Add an optional `extensions = [ siteExtension ];` argument to
`lib.mkConfigDevShell`. Nix builds the extension and a static JSON registry with
absolute store executable paths, schema version, command declarations, hooks,
order and requested capabilities. The shell's confctl launcher supplies the
registry path. Help/command discovery reads data only: no extension execution,
Nix inventory evaluation, PATH scanning, Cargo download or runtime compilation.
Core and site package pins are tested together. Development registry overrides
must be explicit operator input, never an implicit search of arbitrary `scripts/`.

Illustrative registry entry (proposal; field names frozen in M1):

```json
{
  "schema": 1,
  "id": "vpsfree-site",
  "protocol": {"major": 1, "minor": 0},
  "executable": "/nix/store/<site-package>/bin/confctl-site",
  "commands": [{"path": ["runtime-kernels", "update"],
    "handler": "runtime.update", "arguments": [{"name": "machine-pattern", "required": false}],
    "option_set": ["show-trace", "attribute-filters", "tag-filters", "yes"]}],
  "hooks": [{"event": "deploy.prepare", "handler": "runtime.prepare", "order": 100},
    {"event": "rediscover.after-write", "handler": "netboot.rediscover", "order": 100}],
  "capabilities": ["inventory", "select", "machine-exec", "prompt", "render", "workspace-files"]
}
```

The executable is trusted code running as the operator, **not a sandbox**. Its
capability list narrows host services and catches mistakes; it does not prevent
arbitrary OS calls. Registry validation rejects duplicate IDs, core/extension
route collisions, unknown option sets/hooks, incompatible major versions and
missing required capabilities before mutations. No dynamic library loading,
in-process Ruby, autoloaded old scripts or arbitrary object callbacks remain.
Detect legacy regular files in the old scripts directory and stop operational
commands with migration guidance instead of silently skipping their hooks. Help
can explain the problem without executing them. Keep old scripts only in the
retained old revision/environment.

Proposed transport is JSON-RPC 2.0 messages, one compact UTF-8 JSON object per
line, over child stdin/stdout. stderr is diagnostic output captured by the host,
never a terminal handle. `initialize` negotiates protocol major/minor and the
capabilities; reject major mismatch before invoking a command or hook. Additive
minor fields may be ignored only when specified as optional; unknown methods,
enum values and required capabilities fail. IDs distinguish host invocation and
extension service calls. One invocation owns one extension child and its service
requests; no persistent daemon or cross-invocation state is required.

Set explicit bounded defaults at M1: 1 MiB per frame, 16 MiB total in-flight
payload, bounded concurrent service requests, and paginated/projected inventory
responses. Large process captures use host-owned handles/chunks; never put an
unbounded log in a JSON response. `uname -r` results fit the ordinary bounded
capture. A frame-limit violation is an extension error, not truncated success.
Startup negotiation has a bounded timeout (proposed 5 seconds); commands/hooks
have no new arbitrary overall or kernel-probe timeout. Preserve existing SSH
options and allow cancellation of a stalled probe. Extension output may not
write raw stdout beside protocol frames.

Minimal services needed by these two scripts:

| Service | Contract |
| --- | --- |
| `machines.select` / `machines.inventory` | Ordered typed machine records, metadata projections, exact host selection rules; inventory can explicitly refresh after rediscovery; no hidden managed/runnable filter |
| `machines.exec` | Machine identity + argv + inherited execution policy; host resolves local/root SSH target; return native success/nonzero separately from spawn/transport infrastructure failure and bounded byte captures |
| `ui.confirm` | Host displays normal configured-column machine preview and existing prompt; honors yes/always policy, suspends live painting and owns input |
| `ui.message` / `ui.table` | Semantic styles and ordered rows, baseline stdout placement; no plugin-supplied terminal escape sequences |
| `workspace.read` / `workspace.replace` | Relative approved paths, original content and checked atomic replacement under the invocation's root/lock; report changed paths and invalidate evaluation caches |
| `format.nix` | Literal value serialization for generated lists; strings escaped as data, never inserted as Nix expressions |

Bind the invocation to a canonical live config root and identity, not the
extension's `/nix/store` source directory. Host-service file paths reject absolute
paths, `..` and symlink escapes. Execute children and Nix with matching cwd/PWD;
no stale registry/root binding can select a different checkout. Full metadata is
available on demand rather than serializing the entire fleet into every frame.

Typed hook contracts:

| Hook | Input | Result and failure |
| --- | --- | --- |
| `deploy.prepare` | Confirmed ordered machine scope, requested generation, **effective** switch action, parsed deployment options, root/invocation identity; runs after consent/validation but before lookup/build/status filtering for every action including copy-only | `Continue` or structured `Abort`; no scope/option mutation. Completed file writes invalidate build-plan/evaluation caches without expanding confirmed scope. Host waits before proceeding. Nonfatal per-host query results remain Continue |
| `rediscover.after-write` | Root/invocation identity and already-written core-list path; fresh inventory service required | Continue after generated file replacement, or Abort with earlier core writes retained; used by add/rename/rediscover |

The Ruby action keyword happens to read `opts[:action]` rather than the parsed
positional action. The new protocol exposes the effective action deliberately;
these site scripts ignore that old keyword. This is a new typed API, not a change
to operator deploy semantics. The old unused `return_value` object chain is not
emulated. Future hooks may add typed results through a protocol revision.

A concrete abbreviated wire exchange for the prebuild kernel hook:

```json
{"jsonrpc":"2.0","id":"host:1","method":"invoke","params":{"handler":"runtime.prepare","invocation":"run-1","root":"/srv/configuration","machines":["cz.vpsfree/nodes/stg/node1"],"generation":null,"effective_action":"switch"}}
{"jsonrpc":"2.0","id":"ext:1","method":"machines.exec","params":{"machine":"cz.vpsfree/nodes/stg/node1","argv":["uname","-r"]}}
{"jsonrpc":"2.0","id":"ext:1","result":{"status":{"exit_code":0},"stdout_base64":"Ni4xMi4zCg==","stderr_base64":""}}
{"jsonrpc":"2.0","id":"host:1","result":{"outcome":"continue"}}
```

Initialization, scoped file read/replace, rendered table and cancellation frames
are omitted here, not optional in the handler. One final invocation response and
successful child exit are both required. Malformed output, crash, unknown service,
failed handshake or Abort fails the parent operation before its next stage. Do
not retry hooks automatically: files may already have changed. On cancellation
stop granting new services, cancel owned process groups, join handlers/readers,
restore terminal ownership, then report effects already completed.

Operator commands retain their current shape:

```text
confctl runtime-kernels update -y -t node 'cz.vpsfree/nodes/*'
confctl deploy -y 'cz.vpsfree/nodes/stg/*'
confctl rediscover
```

These are examples of the proposed installed package, not commands executed in
this session. Option spelling and placement remain governed by the fixture gate.

Per-script migration decisions (full source/effect map is in the site inventory):

- `scripts/discover_netbootable.rb` becomes `netboot.rediscover`: evaluate the
  freshly written inventory; keep enabled non-carried machines of any spin or
  managed state; retain order/header/final newline in `cluster/netbootable.nix`.
  No commit, SSH or added prompt. Preserve partial earlier effects on failure.
- `scripts/runtime_kernels.rb` becomes `runtime.update` and `runtime.prepare`
  sharing one kernel-update function. Explicit command selects all matching
  vpsAdminOS entries, including unmanaged/carried; hook takes only non-carried
  vpsAdminOS from confirmed managed scope. Empty hook does nothing; empty explicit
  command still follows its prompt/header/save behavior.
- Keep ignored `configs/node/kernels.json`, full machine-name keys and unselected
  entries. Strip stdout, split on dots using Ruby's trailing-empty behavior, keep
  first three parts and rejoin. Preserve suffixes, empty successful strings and
  literal `error` sentinel behavior. Captured command failures print errors,
  delete only the failed selected keys and do not fail the command; other errors
  do. No hidden runnable filter, carrier rerouting or new probe timeout.
- Preserve existing permissive JSON behavior, including unselected non-string
  values and zero-machine reserialization; do not silently impose strict
  object-of-strings validation or discard unknown data. Strong typed merge
  validation occurs where actual selected-host updates require it. Record
  malformed-shape fixtures rather than adding an undocumented cleanup migration.
- Atomic replacement and an invocation-owned lock improve partial-write failure
  safety without changing successful bytes/schema. Preserve pretty JSON/no final
  newline. Mixed Ruby/Rust writers still require operator exclusion. Bounded
  scheduling may cap active probes while retaining selected set, result/exit and
  table order; default first implementation can retain one worker per selected
  host, then tune only with evidence. No generic deadline is introduced.
- Keep `configs/node/kernels.nix` live PWD read, manual override precedence and
  `configs/node/base.nix`/PXE consumers. Hook file writes must affect the next
  impure evaluation; cache invalidation and scope retention are release gates.

## Maintained dependency candidates and limits

These are proposed choices, not installed or compiled dependency claims. Primary
repositories/docs were inspected on 2026-10-17. Release lists and maintained
project documentation support candidate selection; maintenance, advisories,
licenses, transitive size and MSRV must be rechecked when locking versions in M1.
Do not infer a latest compatible version from this planning snapshot.

| Candidate | Use and evidence | Constraint |
| --- | --- | --- |
| [clap](https://github.com/clap-rs/clap/releases) | Active release list (observed v4.6.5); built-in derive plus builder API for static extension declarations | Explicit Ruby parser adapter/fixtures; default clap policy is not the contract |
| [Tokio](https://github.com/tokio-rs/tokio), tokio-util | Process/IO/signal scheduling and cancellation; current process docs inspected | Select features; explicit joins/process groups remain application responsibility |
| [Ratatui](https://github.com/ratatui/ratatui), [Crossterm](https://github.com/crossterm-rs/crossterm/releases) | Widgets/inline terminal and backend; inline docs observed at 0.30.2, Crossterm release list includes 0.29 | Real PTY spike required; no fullscreen/raw-mode default |
| [Indicatif](https://github.com/console-rs/indicatif/releases) | Maintained progress alternative with current release history | Not selected alongside Ratatui; avoid two render owners |
| [Serde](https://github.com/serde-rs/serde) + serde_json | Typed JSON state and protocol with bounded decode | Preserve unknown metadata and old field aliases explicitly |
| [thiserror](https://github.com/dtolnay/thiserror) | Domain error enums | `anyhow` only optional top-level context, not core or wire contracts |
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

In the site repository delete only the two migrated confctl scripts after their
handlers are packaged. Keep its other 31 Ruby files, Gemfile/test hooks and tools
mode: they belong to vpsAdmin, services, specs and development tooling. No claim
of a Ruby-free site or fleet follows from a Ruby-free confctl runtime.

`gen-data` needs a small Rust vpsAdmin/HaveAPI client adapter, not a skipped or
Ruby-backed command. Freeze the current client authentication endpoint discovery,
server-specified challenge/protected fields, fixed token lifetime, pagination and
error behavior using a mock HTTP server. Generate identical Nix values for
container/node metadata and IPv4/IPv6 network lists. TLS/proxy/default endpoint
behavior and source client revision are M0 acceptance inputs; do not invent
endpoint paths or add a server migration. Keep credentials out of command logs,
protocol traces and fixtures.

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
4. Extension conformance: static help, version/route rejection before effects,
   malformed/oversized frames, service errors, stdout contamination, child exit,
   cancellation, root/path binding, hook order/cache refresh and nonfatal host
   failures. Both Ruby-to-Rust and Rust-to-Ruby site file round trips.
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
| `.github/workflows/rust.yml` format/lint/unit | Push and pull_request; pinned toolchain; fmt, clippy, locked unit/CLI/protocol tests on Linux | Separate streams and failure logs; no production credentials |
| Same workflow package/platform jobs | x86_64 native and aarch64 native or supported builder; locked Nix package checks | Real architecture execution where claimed; cross compilation alone is not a run |
| `.github/workflows/tests.yml` | Keep self-hosted authorized VM suite path/dispatch model; add Rust/protocol/helper inputs to path filters | Actual suite result evaluation, logs/artifacts on failure/cancel, isolated owned test state |
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
| M1c: extension contract | `crates/confctl-extension-protocol/`, `docs/extensions.md`, protocol fixtures | M0 site contract | Versioned request/result/schema and frame/capability/error rules; host/site owners can work independently |
| M2a: Nix/inputs/configuration | `src/nix/`, `src/inputs/`, `src/configuration/`, owning tests | M1a/b | Inventory/init/inputs/lock/Git effects pass; no accidental input update on build |
| M2b: generations/status | `src/generation/`, status domain/adapter and tests | M1a/b; Nix interface | Round trips, roots/current crash points, family-specific selectors and unknown metadata |
| M2c: presentation | `src/terminal/`, `src/presentation/`, PTY tests | M1a/b | One owner; prompt/pipe/color/scrollback/cancel/live timing acceptance |
| M2d: host extension runtime + site | Core `src/extensions/`; independent site `extensions/confctl-site/` and tests | M1c, M1b, selection/renderer interfaces | Core conformance and site two-script scenarios; prepare writes visible to next eval |
| M3a: operations | `src/operations/{build,deploy,health,ssh,connection,gc,compare}.rs` and owning tests | M2 adapters/UI | All built-in operation fixtures including partial failure/result/exit and scheduling order |
| M3b: remote helpers | `src/bin/` helpers, `src/remote/`, netboot templates/helper tests | Process/state contracts; separate Nix integration owner | Four Ruby helpers replaced, mixed-version protocol/index tests, watchdog disconnect behavior |
| M3c: vpsAdmin/data generation | `src/vpsadmin/`, `src/operations/gen_data.rs`, HTTP fixtures | M0 API fixtures, process/UI | All three gen-data leaves including challenge auth and error/file semantics |
| M4: packaging/docs/CI | Cargo roots/locks, `nix/`, `flake.nix`, workflows, man generation, README/upgrade docs; site flake pin/registry separately | Accepted M2/M3 packages | Locked runtime closure audit, shell modes, helper architectures, docs/workflow drift, no embedded Ruby |
| M5: acceptance and cutover preparation | Integration/PTY/mixed-version tests and dated rollout record | Quick checks + committed independent review | Native VM and operator visual acceptance, exact final compatible pair and retained rollback path; merge/deploy remain separately authorized |

With two implementers, start M1a/M1b after the shared brief freezes; then pair
M2a with M2b, and M2c/core-extension runtime with the site package. M3 remote
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
- Atomic writes improve interrupted-write safety but do not undo earlier hooks,
  remote effects or failed-host kernel deletion. Old Ruby does not honor new
  locks. Exclude concurrent writers and retain closures, not just JSON backups.
- `bundled-confctl` and arbitrary Ruby imports cannot remain source-compatible.
  This intentional extension/package boundary needs clear upgrade guidance and
  consumer inventory; minimal/tools and the actual site's unrelated Ruby tools
  remain supported.
- Source timing behavior is accepted for adoption; exact human visual preference
  still requires a walkthrough of the future Rust implementation. Historical Go
  passes are not Rust test evidence.

No unresolved question blocks completion of this plan. These are explicit gates
for future implementation, not permission to run builds, deploy or merge now.

## Final architect report

**DESIGN COMPLETE — ready for lead acceptance and tracking handoff.** Both
completed inventories are reconciled; all requested CLI, presentation, timing,
Rust architecture, dependency, extension, site migration, Ruby removal,
compatibility, recovery, CI and implementation-package topics are covered.

Only `design.md` was written by architect0. Investigation used immutable source
inspection, historical read-only context and primary dependency documentation.
No project edits, prototype, application tests/builds, commits, deployment,
merges, roster changes or lifecycle actions occurred. Runtime parity and package
claims remain future acceptance gates. The lead owns final plan/state, artifact
registration and serialized tracking commits. No further architect edits are
planned unless the lead identifies a concrete acceptance issue.
