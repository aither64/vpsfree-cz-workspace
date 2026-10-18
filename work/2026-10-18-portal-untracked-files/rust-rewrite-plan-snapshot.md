# Rust confctl replacement design

Status: **EXECUTION BRIEF READY — 2026-10-18.** The user authorized the
entire accepted Rust rewrite, testing and feature-branch publication. The accepted
built-in-feature design below remains the implementation contract. Master
integration and production deployment are not authorized.

## Execution coordination status

Identity reverified from the tracking directory; `dev-session current` prints
`2026-10-17-confctl-rust-rewrite-plan` and both environment markers are absent,
consistent with the trusted binding. architect0 owns design/interfaces only;
lead owns plan/state, worktree registration and serialized Git coordination.
Implementer0 owns M0 `tests/compat/core/` and `docs/compatibility.md`;
implementer1 owns M0 `tests/compat/site/`, `tests/compat/helpers/` and optional
`docs/compatibility-site.md`. Freeze executable fixtures before replacement code.

First parallel Rust units are defined in the execution brief below. Lead may
release the isolated foundation subset under the explicit overlap rule below;
replacement behavior still requires M0 acceptance. Shared interfaces and manifests have one writer;
interface changes go through lead. `report_to_lead` is now callable; the earlier
external-lock fallback remains unused. Architect's Nix daemon access is denied;
root-owned verification executes builds/tests and returns logs, without changing
member permissions. This does not block design. No architect application edits.
Lead accepted this execution brief. M0 is still active: lead reports 59 site/helper
cases green and committed, focused native parser/API/operation cases green, and
the immutable Ruby archive frozen. Full 372-case core capture/replay remains
pending. These reported checks are not a full parity claim. Isolated foundation
work can overlap that run; missing behaviors remain gates before replacement.
Architect remains available for design deviations and fixture adjudication.

M0 adjudication **GC-01** is accepted by lead: quick-v2 reproduces Ruby's
`Progress#line` callback crash (confctl exit 1). Rust must complete successful
GC normally and retain genuine GC failures. The narrow exception and required
tests are recorded under CLI parity below; the raw Ruby defect is retained.

## Execution brief — shared interfaces and first assignments

This section freezes implementation direction on 2026-10-18; signatures are
private Rust contracts, not a public SDK. Implementers may add private helpers.
Changes to these shared boundaries require a short lead-coordinated amendment,
not duplicate competing types. Behavior requirements below and the inventories
remain authoritative; these signatures do not waive any parity gate.

### Execution baselines and M0 admission

- Confctl worktree HEAD and origin/master are
  `cc40679d267165aecfa569128438bb55fe910268`, unchanged from planning.
- Site execution baseline is `a4847bd6bbf2a62c107cff30b47452a60548a33e`.
  Relative to V, only staging node1/node2 configs and the dev-workspace lock pin
  changed. Both scripts, feature consumers/settings and the confctl pin are
  unchanged. Do not revert those unrelated baseline changes.
- Worktrees are under this session's `worktrees/<slug>/{confctl,vpsfree-cz-configuration}`.
  Lead owns their registration/hooks/Git state; this brief does not authorize
  touching another session's checkout.
- M0's executable archive is `tests/compat/core/baseline.tar.gz` with immutable
  revision/digest metadata. The shared `--export-baseline DIR` and
  `CONFCTL_RUBY_ORACLE_ROOT` interfaces let site/helper fixtures reuse it.
  Preserve separate raw stdout/stderr/native exit/effect records and explicitly
  normalized presentation snapshots. Do not regenerate expected results from
  the Rust replacement. Production packaging must exclude the archive/Ruby.
- Before substantial replacement, lead accepts executable route/parser cases,
  operation side-effect traces, site semantics and all helper surfaces. A route
  listed only in an inventory is still unverified. The foundation overlap below
  does not satisfy this gate;
  an uncovered behavior remains a gate, never an implicit new Rust default.

**Foundation overlap accepted, 2026-10-18.** Lead may release M1-B private
process/events/timing/terminal library additions while full M0 capture/replay
runs. This is implementation of isolated primitives, not a switch of the
executable or a replacement of command behavior. The immutable archive and
focused evidence permit this independent work; global M0 remains incomplete.

- Implementer1 may add only `src/process/`, `src/events.rs`, `src/timing.rs`,
  `src/terminal/` and dedicated primitive test/harness files. Use the frozen
  `ProcessRunner`/`ProcessSpec`/`ProcessOutcome`, typed event sink, terminal lease,
  input broker and timing-guard contracts below. No adapters, operations, core
  feature services, helper replacements or product CLI routing yet.
- Implementer0 may add the minimum M1-A foundation wiring: Cargo manifest/lock,
  toolchain file, `src/lib.rs`, shared `src/error.rs` and private domain types
  required by M1-B, plus their tests. Keep one writer per shared file; implementer1
  requests missing types/features rather than defining another copy. This early
  subset does not release M1-A parser/selection behavior or `main.rs`/app dispatch.
  M1-B can author its files before the root wiring lands; library compilation
  follows the wiring, without a temporary second Cargo package.
- Existing Ruby source, `bin/confctl`, package/install/default command paths,
  Nix shells/wrappers/hooks, site settings/scripts and M0 archive/harness/capture
  inputs remain unchanged during the oracle run. Do not shadow `confctl` in
  PATH or switch a wrapper to Rust. New test harnesses use explicit paths and
  disposable fake children; they are not installed product binaries.
- Root serializes Cargo/dependency resolution and any verification. Do not
  change the running oracle's checkout inputs, environment or fixture outputs;
  hold overlapping setup/hook/Git operations until its watcher completes.
  Primitive tests check ownership/drain/cancellation/timing invariants without
  claiming CLI parity. Root delegates uncertain builds/checks as usual.
- Full M0 record/replay, gap adjudication and lead acceptance remain mandatory
  before command replacement, adapters/operations or default/package cutover.
  Any new oracle finding can revise these primitives; early work creates no
  presumption that its behavior is accepted. GC-01 remains the named exception.

This narrowly refines the original scheduling gate and leaves all replacement
acceptance criteria intact. No other M1/M2 scope is released by this paragraph.

M0 gen-data transport intervention is accepted: a test-only `RUBYOPT` preload
asserts the locked client's original `https://api.vpsfree.cz` URL, then replaces
only the communicator base URL with the owned numeric loopback HTTP endpoint.
Run actual discovery, auth/challenge/token polling, pagination and GenData code.
Refuse unexpected URLs, redirects or socket destinations outside that exact
endpoint; use fake child programs and fixture credentials. A negative test must
prove an unredirected/out-of-scope request cannot connect. Redact credentials
from traces. Record this intervention in fixture metadata. No production Ruby
or Rust command-line URL option is required merely to support the oracle.

### Toolchain and dependency lock ownership

**Freeze Rust 1.95.0, edition 2024, declared `rust-version = "1.88"`.** Root
reported a successful read-only evaluation of the confctl-pinned nixpkgs
`8b8c811c7c2541c30382c5de7ed26be055569c60`: rustc, cargo, rustfmt and clippy
are all 1.95.0. This is version-selection evidence, not a successful Rust build.
Implementer0 adds those four packages to `nix/flake/mk-confctl-devshell.nix`;
retain existing Ruby/Bundler tooling for M0 and hooks until its owned migration.
Use the same `pkgs.rustPlatform` for `nix/package.nix`. Pin 1.95.0 in
`rust-toolchain.toml`; no new Rust overlay or Nix input is needed. A Nix shell
uses its pinned binaries rather than downloading rustup tools during bootstrap.
The declared MSRV needs its own locked-dependency compile check before claiming
support; if transitive dependencies require newer Rust, constrain the responsible
dependency or explicitly revise the declared floor through lead.

Initial direct selections below were checked against published crate manifests
on 2026-10-18; versions in links are the evidence, not a guarantee of future
latest status. Use compatible manifest requirements with a committed exact
Cargo.lock. Implementer0 alone writes Cargo roots/lock; implementer1 sends needed
features through lead. Resolve the full graph, licenses and advisories before
accepting it. Do not call a selected dependency compiled or audit-clean yet.

| Dependency | Initial release / declared MSRV | Enabled responsibility |
| --- | --- | --- |
| [clap](https://docs.rs/crate/clap/4.6.7/source/Cargo.toml) | 4.6.7 / 1.85 | Static command builder; no automatic version action; explicit compatibility adapter |
| [tokio](https://docs.rs/crate/tokio/1.53.3/source/Cargo.toml) | 1.53.3 / 1.71 | `rt-multi-thread`, `macros`, `process`, `io-util`, `signal`, `sync`, `time`, `net`, `fs`; avoid blocking stdin |
| [tokio-util](https://docs.rs/crate/tokio-util/0.7.20/source/Cargo.toml) | 0.7.20 / 1.85 | `rt` for cancellation; no detached task lifetime |
| [ratatui](https://docs.rs/crate/ratatui/0.30.2/source/Cargo.toml) | 0.30.2 / 1.88 | Disable defaults, select `crossterm_0_29`; inline viewport; add widgets only as used |
| [crossterm](https://docs.rs/crate/crossterm/0.29.0/source/Cargo.toml) | 0.29.0 / 1.63 | Shared terminal backend; no competing input reader |
| [serde](https://docs.rs/crate/serde/1.0.229/source/Cargo.toml), [serde_json](https://docs.rs/crate/serde_json/1.0.154/source/Cargo.toml) | 1.0.229 / 1.56; 1.0.154 / 1.71 | `derive`; JSON `preserve_order` for observed object ordering and retained unknown metadata |
| [thiserror](https://docs.rs/crate/thiserror/2.0.21/source/Cargo.toml) | 2.0.21 / 1.77 | Typed domain/infrastructure errors |
| [rustix](https://docs.rs/crate/rustix/1.1.5/source/Cargo.toml) | 1.1.5 / 1.65 | Unix process groups, descriptors, locking and terminal/input seam; only needed features |
| [chrono](https://docs.rs/crate/chrono/0.4.45/source/Cargo.toml) | 0.4.45 / 1.62.0 | Disable defaults, enable `clock` (includes `now`/`std`); local RFC3339 timestamps, never elapsed durations |
| [tempfile](https://docs.rs/crate/tempfile/3.27.0/source/Cargo.toml) | 3.27.0 / 1.63 | Keep default `getrandom`; owned spool/staging files and test directories |
| [reqwest](https://docs.rs/crate/reqwest/0.13.5/source/Cargo.toml) | 0.13.5 / 1.85 | Async HTTP, explicit Rustls/JSON/form/query features as required by API fixtures; system CA/proxy compatibility is an acceptance check |

Add sha2 and Unicode width/segmentation only when used, after
manifest/MSRV/license checks under the same compiler. Test tooling can reuse the
M0 harness and ordinary Rust tests; assert_cmd/proptest/insta are optional, not
required architecture. A small tested Ruby-glob compatibility adapter owns
pattern semantics; choosing a glob crate cannot redefine them. Use standard
OpenSSH/Git/Nix subprocesses, no SSH library/libgit2/runtime extension dependency.

M1-B dependency follow-up (2026-10-18): the chrono/tempfile releases above are
the latest published manifests observed in this bounded check. Both declare
`MIT OR Apache-2.0`; their direct MSRVs fit 1.88/1.95. Wiring owner implementer0
adds `chrono = { version = "0.4.45", default-features = false, features = ["clock"] }`
and `tempfile = "3.27.0"`, then resolves and records these exact initial releases
in Cargo.lock through root-owned verification. Retain Rustix 1.1.5 with
`process`, `event`, `pipe`, `termios`, `fs` and its default `std`. Tempfile's
Rustix `^1.1.4` requirement can share 1.1.5; its `getrandom` requirement spans
0.3/0.4, so verify the actual selected transitive MSRV/license/advisory graph.
No successful resolution/build or whole-graph audit is claimed by this check.

Published safe API coverage for this feature set:

| Rustix feature | Checked API and intended use |
| --- | --- |
| `process` | [`kill_process_group(Pid, Signal)`](https://docs.rs/rustix/1.1.5/rustix/process/fn.kill_process_group.html); signal only an owned child group, then reap it |
| `event` | [`poll(&mut [PollFd], Option<&Timespec>)`](https://docs.rs/rustix/1.1.5/rustix/event/fn.poll.html); input plus cancellation-wakeup readiness |
| `pipe` | [`pipe_with(PipeFlags)`](https://docs.rs/rustix/1.1.5/rustix/pipe/fn.pipe_with.html) returns two `OwnedFd`s; close-on-exec wakeup pipe with bounded writes |
| `termios` | [`tcgetattr`](https://docs.rs/rustix/1.1.5/rustix/termios/fn.tcgetattr.html) / [`tcsetattr`](https://docs.rs/rustix/1.1.5/rustix/termios/fn.tcsetattr.html); save/restore echo for the sole protected-input owner |
| `fs` | [`flock`](https://docs.rs/rustix/1.1.5/rustix/fs/fn.flock.html) and documented `fcntl_getfl`/`fcntl_setfl`; advisory locks and owned-descriptor flags |

Use Tokio's safe [`Command::process_group(0)`](https://docs.rs/tokio/latest/tokio/process/struct.Command.html#method.process_group)
for noninteractive child isolation; an unsafe `pre_exec` closure is unnecessary
for that task. Preserve inherited stdin flags: duplicating an fd does not isolate
its open-file status flags, so do not set nonblocking on a duplicate and leak it
to interactive children. Temporary spool ownership must outlive relay/capture
consumers; returning a bare pathname after dropping its tempfile owner is invalid.

### First independent execution packages

| Package / owner proposed for lead assignment | Exclusive files | Done when |
| --- | --- | --- |
| M1-A / implementer0 | `Cargo.toml`, `Cargo.lock`, `rust-toolchain.toml`, `src/{lib,main,app,error}.rs`, `src/{cli,domain}/`, `nix/flake/mk-confctl-devshell.nix` | M0 parser/selection fixtures pass through Rust; typed requests/errors exported; shared stubs wired, no replacement package cutover |
| M1-B / implementer1 | `src/process/`, `src/events.rs`, `src/timing.rs`, `src/terminal/`, their focused test modules | Fake children prove concurrent byte drain, log failure/cancellation/reaping; timing union/footer and prompt lease tests pass; inline view PTY checks requested through lead |
| M2-A / implementer0 | `src/{nix,inputs,configuration,generation}/`, `src/operations/`, selection/domain additions | Core adapters and operations pass per-command differential cases; owns deploy/rediscover integration call sites |
| M2-B / implementer1 | `src/{runtime_kernels,netboot_inventory}.rs`, `src/remote/`, four `src/bin/` helper files, feature Nix modules | Site/helper oracles match; returns direct typed feature results; owns neither Cargo roots nor operation call sites |
| Next freed slot / explicit lead assignment | `src/vpsadmin/`, `src/operations/gen_data.rs`; later packaging, workflows and site settings/removal | API oracle then full migration/closure gates; assign these files before edits to avoid M2-A overlap |

M1-A creates shared module declarations once, then each owner fills their own
files; no duplicate `Context`, `Machine`, `ProcessSpec`, event or error enums.
Implementer1 owns its public-in-crate exports; M1-A imports them. Main/app own
construction and shutdown, not business logic. Keep the Ruby executable/package
available as oracle until accepted cutover. Intermediate unreachable or typed
unsupported stubs are development scaffolding only and cannot satisfy M4/M5.

### Frozen private interfaces

Use concrete adapters with small generic test seams; do not add a service locator
or generic hook system. `pub` below means exported within the private testable
library, not a supported downstream API. Types live in the owning modules above.

```rust
// cli / domain: argv is never reparsed by operations.
fn parse(argv: Vec<OsString>) -> Result<ParseOutcome, CliFailure>;
// ParseOutcome = Run(Invocation) | Display(CliDisplay); CliDisplay owns streams/status.
// Invocation = GlobalOptions + Action (typed variants for all 30 action leaves).
fn select(inventory: &Inventory, request: &SelectionRequest,
          policy: SelectionPolicy) -> Result<Selection, ConfctlError>;
// Selection retains ordered stable MachineId values; Inventory is immutable.

// process: nonzero child exit is an Ok(ProcessOutcome), not an infrastructure error.
trait ProcessRunner: Send + Sync {
    fn run(&self, spec: ProcessSpec, scope: ProcessScope)
        -> impl Future<Output = Result<ProcessOutcome, ConfctlError>> + Send;
}
// Supervisor::shutdown().await joins every owned child, stdin writer and drain.
// ProcessScope = CancellationToken + TaskId + optional Phase.
// ProcessSpec = program/args/cwd/env + StdinPolicy + stdout/stderr StreamPolicy
//               + redacted_description; argv/paths are OsString/PathBuf.
// StdinPolicy = Null | Bytes | File | Foreground; StreamPolicy = Capture | Forward
//               | CaptureAndForward | Foreground (foreground needs terminal lease).
// Captured = in-memory small bytes or owned spool path, never silently truncated.
// ProcessOutcome = native status/signal + captures + instants + termination cause.

// events / terminal: operation output has explicit stream and reliable delivery.
async fn emit(&self, event: UiEvent) -> Result<(), ConfctlError>; // EventSink
async fn confirm(&self, prompt: ConfirmPrompt) -> Result<bool, ConfctlError>; // Ui
async fn foreground(&self) -> Result<ForegroundLease, ConfctlError>; // Ui
// UiEvent = Output{stream,bytes} | Table | TaskStarted | TaskProgress | TaskFinished
//           | LogAvailable | Diagnostic; domain formatting uses style tokens.
// UI has Idle/Live/Prompt/ExternalChild states and one stdin broker.

// timing: guards record monotonic intervals, not accumulated worker durations.
fn phase(&self, phase: Phase) -> PhaseGuard; // Timing; PromptGuard separately
fn admit(&self, action: &Action);           // after valid parse/availability
fn finish(self, exit: ExitDisposition) -> TimingReport;

// Nix and state: views carry an epoch to reject reuse after feature file changes.
async fn inventory(&self) -> Result<Inventory, ConfctlError>; // NixClient
async fn settings(&self) -> Result<Settings, ConfctlError>;
fn invalidate_configuration(&mut self) -> ConfigEpoch;
fn load(&self, machine: &MachineName) -> Result<GenerationInventory, ConfctlError>;
fn publish(&self, generation: &BuildGeneration) -> Result<(), ConfctlError>;
// GenerationStore owns roots/links; publish current last; never overwrite collision.
fn replace(&self, path: &AllowedRelativePath, bytes: &[u8],
           policy: FilePolicy) -> Result<WriteReceipt, ConfctlError>; // StateFiles

// Built-ins: callers own validation, selection and confirmation.
async fn refresh<P: ProcessRunner>(ctx: &FeatureContext<'_, P>,
    machines: &[MachineId]) -> Result<KernelRefreshReport, ConfctlError>;
fn render(inventory: &Inventory) -> Result<Vec<u8>, ConfctlError>; // netboot_inventory
fn publish(ctx: &FeatureFiles, content: &[u8]) -> Result<WriteReceipt, ConfctlError>;
// KernelRefreshReport has selection-order rows and updated/deleted/unchanged keys.
```

Concrete struct fields are added by their owner from these contracts. Request
variants carry command-specific options/defaults, not untyped global maps.
`Machine` keeps typed known fields plus ordered `serde_json::Value` metadata;
`MachineId` is an internal stable inventory identity, not a renamed display/key.
Keep distinct deploy-per-host and unified/local generation-selector types.
`SelectionPolicy` is an explicit closed enum/struct for existing family policies,
not an arbitrary predicate DSL. Core add/rename/rediscover and deploy call the two
feature services directly.

`ConfctlError` distinguishes usage/config/selection/state/decode/IO/spawn/drain/
child/health/cancel/uncertain-remote errors. Process failures include native status
and log locator but never secrets. Operation adapters decide whether a nonzero
host result is fatal; status/test-connection/SSH/kernel ordinary failures keep
their legacy command policies. `ExitDisposition` is resolved once from the
operation, primary error and M0-confirmed signal policy; it is shared with timing.
Infrastructure failures cannot masquerade as an ordinary failed host.

The event channel is bounded; reliable output/task transitions are acknowledged.
Progress/tail redraws may coalesce; raw log/capture bytes cannot be lost. Spool
and parse child streams independently of UI repaint so a slow terminal cannot
deadlock both child pipes. A log failure cancels/joins owned work and records
secondary failures without replacing an earlier primary failure. Foreground
children get exclusive terminal ownership and inherited descriptors; never
capture an interactive shell behind a running view. Prompts suspend rendering,
use the original stdout even when piped, and preserve blank/EOF behavior.
The live tail sanitizes child control sequences; raw logs/captures retain bytes.
Plain forwarding preserves the command's stream contract. Workers do not invent
cursor control or independently print styled tables.

M1-B may implement independent disk spooling plus an acknowledged bounded event
relay and serialized merged raw-log writes. Drains must not wait on UI repaint;
preserve each stream's byte order without promising deterministic cross-stream
interleaving. Join drains, relay and log writer before success; disk exhaustion,
receiver loss and write failure remain explicit errors, never silent truncation.

**Temporary foreground staging boundary:** inherited descriptors and a terminal
lease do not transfer controlling-TTY foreground ownership. In the unused
additive M1-B library, explicitly reject a controlling-TTY foreground request
before spawn or terminal mutation with
`ConfctlError::ForegroundJobControlUnavailable`. Implementer0 owns adding that
shared variant; do not disguise it as `TerminalBusy`, a child failure or success.
Non-TTY inherited foreground execution may be implemented/tested now. Determine
the actual controlling/input terminal, not merely whether stdout is piped.

Before wiring interactive SSH, CSSH/pager or other interactive product routes,
implement the supported Linux controlling-TTY path: retain the previous foreground
process group, safely attach the child group with `tcsetpgrp`, handle SIGTTOU
during attach/restore, transfer input exclusively, and restore group/termios/UI
on success, failure, signal and cancellation. Exercise an actual controlling PTY
with a child that reads/writes, Ctrl-C and stop/continue behavior, failure during
handoff and shell/terminal usability afterward. Safe API names alone do not prove
this job-control behavior. The temporary rejection must never ship as completion
of the supported interactive command contract; no silent noninteractive fallback.

Shared types now observed in implementer0's additive files remain the boundary:
`domain::ExitDisposition { code: i32, state: ExitState }` with Completed/Failed/
Canceled, and `error::ConfctlError` with separate spawn/drain/IO/event/input/child/
cancel/uncertain-remote variants plus primary/secondary cleanup. M1-B consumes
these, without its own exit enum or mapping every child nonzero to invocation
failure. Final application policy resolves a consistent status/state before
timing freezes; cancellation codes await their command fixtures. These are
source-interface observations, not compile/test acceptance.

`StateFiles` validates feature paths against the real configuration root and
uses checked parent-directory access for atomic same-directory replacement.
Preserve existing permissions; new file permissions follow the M0/umask contract.
File-purpose policies keep kernel JSON, generated Nix, generation directories
and intentionally store-pointing symlinks distinct. `WriteReceipt` records a
completed effect, not a rollback promise. No mixed Ruby/Rust concurrent writers.

### Operation integration and later packages

Deploy: validate -> select managed hosts -> original preview/confirmation ->
refresh enabled non-carried vpsAdminOS subset once -> publish kernel JSON ->
invalidate Nix settings/inventory/build-plan/input caches -> resolve generation
or build -> status/skip-current -> original copy/activate/reboot/health ordering.
Keep confirmed IDs fixed through reevaluation. Explicit runtime update uses all
selected vpsAdminOS (including carried/unmanaged), original preview/prompt, and
does not acquire a timing appendix. Empty explicit selection still saves; empty
deploy subset has no feature effects. Ordinary host failures delete old selected
kernel keys and continue; malformed file/spawn/write/cancellation aborts.

Add/rename/rediscover: publish core cluster list -> invalidate/reload full
inventory -> if enabled render/publish netboot list. Preserve previous core
writes on later failure. Keep the generated list initially. No feature work on
unrelated commands or disabled settings. The detailed compatibility table below
governs literal `error`, trailing-dot normalization and permissive JSON cases.

Remote helper binaries are thin argument adapters over `remote` modules; retain
existing argv/files and target-system packaging. The rollback watchdog must own
its survival after SSH disconnect; never attach it to the operator's disposable
child group. Carrier/netboot scanning, menu/tree rendering, atomic publication
and kexec downloads are real Rust ports, not wrappers around retained Ruby.
The private vpsAdmin HTTP adapter accepts injected base URL/transport for tests,
uses the existing endpoint in normal runs, and models discovered actions,
challenge/token states and pagination explicitly. It shares the sole protected
input broker and redacted diagnostics; no generic HaveAPI SDK is required.

Nix/root wiring and site cutover remain separately assigned packages: export the
two modules/settings, retain public flake outputs and helper invocations, update
minimal/tools shells, remove confctl's Ruby runtime/release machinery, migrate
site pin/settings and remove only its two scripts. Preserve the site's unrelated
Ruby tools. Workflow owner verifies official action refs before editing CI.

### Execution checks and remaining gates

Quick targeted checks: exact M0 parser/stream/exit/effect replay; fake-process
drain/cancel/spawn/log faults; deterministic timing union/footer; kernel/netboot
scenarios; generation round-trip/root/current fault injection; helper and HTTP
fixture tests; format and affected lint. Rust commands use the declared Nix
toolchain and `--locked`. Initial dependency fetch/compile, full Cargo/PTY/Nix/VM
suites and uncertain checks go through root's fresh verification watcher; do not
launch them in a member and then delegate only the wait.

Before cutover: all 30 leaves and four helpers implemented, no stubs/fallback;
M0 differential gaps closed; old/new state and helper matrix; native x86_64 and
aarch64 package checks; live PTY plus piped/error cases; dependency/license and
Ruby-closure audits; generated docs; site paired rollback. Lead obtains final
independent review after completed intended changes are committed and quick
checks pass, then runs long integration acceptance. No production operation or
master integration is implied. Keep the session open.

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
The lead accepted this direction; the user subsequently authorized implementation.

Retain the Rust/Nix/SSH architecture, Tokio process ownership, Ratatui/Crossterm
inline view and Go invocation timing model. First freeze executable Ruby CLI and
effect fixtures. Then implement process/UI and typed domain interfaces, Nix/state
adapters, core runtime-kernel/netboot services and remote operations in separate
file packages. Port all remote Ruby helpers and the data client before packaging
cutover. Differential, PTY, mixed-version and disposable VM gates remain required.

## Accepted planning revision (historical)

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
The lead owns plan/state, Git coordination and verification delegation;
architect0 owns this design and interfaces. Implementers own application edits.
The historical Go session remains read-only reference material.

Planning baseline: canonical `repos/confctl.git`, Ruby `origin/master` observed at
`cc40679d267165aecfa569128438bb55fe910268`. Source files are inspected with
`git show` and a private read-only source copy at
`/tmp/2026-10-17-confctl-rust-rewrite-plan-architect0-confctl`. No refs or worktrees
were changed during planning. The completed inventories supply the exact site and Go
baselines and exhaustive command/script evidence, linked below.

## Proposed package boundaries for lead coordination

| Package | Owning implementation files | Dependencies | Acceptance |
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
- The execution brief selects exact initial toolchain/direct crate versions from
  current manifests; locked transitive compatibility/license/advisory and build
  checks remain required before acceptance.

## Coordination transport

`report_to_lead` is now available and execution milestones were delivered. During
planning the tool was absent. The permitted CLI fallback with unique message id
`architect0-boundaries-20261017-01` could not acquire
`/home/aither/.local/state/dev-workspaces/transition.lock` under this thread's
filesystem permissions, so it sent no report. That fallback is not retried.
This artifact remains the durable design/status source; no permissions were
bypassed.

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
stderr, reorder result sets or suppress error codes in parity tests. The following
lead-accepted exception is explicit rather than a blanket error normalization.

### GC-01: correct the reproduced Ruby progress callback crash

**Accepted intentional parity exception, 2026-10-18.** The M0 quick-v2
`collect-garbage -y alpha` fixture at R exits 1 after printing a GC completion
line because `Cli::Generation#run_gc` reads `progress.line`, which
`NixCollectGarbage::Progress` does not expose. It emits a `NoMethodError` and
worker traceback with a volatile Thread address. Architect inspected the raw
evidence at
[`evidence/m0-core/quick-v2/raw/gc-baseline-line-error.json`](evidence/m0-core/quick-v2/raw/gc-baseline-line-error.json)
and source `lib/confctl/cli/generation.rb:273-370`,
`lib/confctl/nix_collect_garbage.rb`, and `machine_control.rb:129-135` at
`cc40679d267165aecfa569128438bb55fe910268`. This resolves the earlier static
uncertainty. It does not establish that Rust GC is implemented or verified.

The exception removes this accidental callback crash and its traceback, allows
normal completion output and exit 0 for successful GC, and adopts the requested
timing footer. It does not change selected targets, confirmation/yes policy,
Nix/SSH argv, carrier deduplication, concurrency setting, generation-removal
ordering or filesystem effects. No real garbage collection is authorized by the
fixture or this adjudication. Apply the same corrected GC path when invoked
after generation removal/rotation; keep their preceding effects and scopes.

Intended contract:

- Successful GC child exits produce their host progress and a final completion
  summary (recognized `N store paths deleted...` text, otherwise `done`). All
  selected children are joined. With no other invocation failure, confctl exits
  0 and timing reports `completed (exit 0)` in plain and TTY modes.
- A nonzero GC/SSH child result is a failed host, even if it printed a plausible
  success summary. Preserve child diagnostic output and native status in the
  process/log result; print the host failure outcome, finish/join the other
  scheduled host jobs, and fail the invocation with exit 1 and the existing
  failed-host aggregate diagnostic. Timing reports `failed (exit 1)`. Do not
  import the exit-0 policy of test-connection, SSH commands or kernel probes.
- Progress parsing is observational. Unknown or partial lines remain available
  in the log/tail and do not cause a child failure or fabricated success. A
  typed GC progress event retains its source line and optional deleted path;
  the consumer never requires an absent accessor. Summary text is not proof of
  child success. This exception does not authorize unrelated progress changes.
- Spawn, drain, required log or terminal-output IO failures remain invocation
  failures under the shared error/cleanup rules, not fake GC exit codes. An
  injected renderer failure is reported as that infrastructure error; it does
  not erase a prior child failure or pretend completed GC was undone.
  Cancellation retains the independently fixture-qualified signal/exit policy.

Implementer0 retains the Ruby defect fixture/raw bytes as historical baseline
evidence and records GC-01 in project compatibility documentation. Add separate
Rust expectations for successful GC with the triggering summary line, zero
output, mixed progress/unknown lines, and nonzero child exits both with and
without summary text. Include a multi-host success/failure case and a separate
renderer/log fault case. Assert selection/argv/effects and stream destinations,
not only status; plain and PTY checks exercise the same outcome logic. The
comparator may apply only this named case-specific exception; do not replace
all stderr, scrub the traceback from raw Ruby evidence, or require Rust to
reproduce the crash. If normalizing the Ruby snapshot's Thread address for
repeatability, normalize only that address and retain its full diagnostic.

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

## Planning dependency evidence and remaining limits

This historical 2026-10-17 candidate evidence supplements the execution brief's
newer concrete selections. The execution brief takes precedence for versions and
toolchain; neither section claims a successful build or completed dependency
audit. Check locked transitive MSRVs, licenses, advisories and size in M1.

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

Use the execution brief's Rust 1.95.0 toolchain, edition 2024 and declared 1.88
MSRV. Keep `rust-toolchain.toml` and the Nix dev shell consistent; validate the
locked graph on the declared minimum. Commit Cargo.lock, minimize features, audit licenses
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

Commands below are execution acceptance gates. They were not run during the
planning phase; current run evidence belongs to member reports and lead state.
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

The execution brief above controls the first concrete owner/file assignments:
The isolated M1-B/M1-A-wiring subset may start under the foundation overlap
rule. Full M1a behavior follows M0 acceptance, then Nix/state/operations
run beside built-in services/helpers. Move vpsAdmin and packaging into explicitly
assigned freed slots. Do not let both owners edit
`main.rs`, Cargo manifests, root Nix exports or shared terminal/event types
concurrently. Integration changes get an explicit small assigned file package.
No calendar estimate is claimed: M0 parser/API findings and remote-helper size
are the largest uncertainty. Each milestone produces a usable, reviewable slice,
not an all-or-nothing rewrite branch with deferred tests.

## Explicit uncertainties, risks and decisions left for execution

- Exact GLI abbreviations, negative aliases, option ordering, version/help,
  surplus args, signal status and allow_shared spelling
  require executable M0 evidence. Compatibility takes precedence over convenient
  cleanup; unresolved cases cannot silently become clap defaults.
- GC-01 is adjudicated from executable quick-v2 evidence: fix only the accidental
  progress callback crash, retain genuine child/infrastructure failure policy,
  and keep raw Ruby defect evidence separate from intended Rust expectations.
- Direct dependency manifests/MSRVs and the pinned compiler version are checked;
  the locked graph is not yet built/audited. Confirm transitive MSRV, licenses
  and advisories; prove inline Ratatui behavior in a PTY. Keep one UI owner.
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

No unresolved design question blocks M0 or its subsequent M1 assignments. These
are execution acceptance gates under the user's implementation/test/publication
authorization. Production deployment and master integration remain unauthorized.

## Final architect report

**EXECUTION BRIEF READY — accepted by lead; M0 acceptance still pending.**
Isolated M1-B primitives and minimal M1-A Cargo/private-type wiring may proceed
under the recorded foundation overlap rule; executable replacement remains gated.
Rust 1.95.0/edition 2024, declared MSRV 1.88, initial dependency selections,
concrete first-package ownership, shared private interfaces and verification
gates are recorded near the top. The new site baseline preserves the inventoried
script contracts. Built-in opt-in kernel/netboot services remain selected, with
no extension registry/protocol/SDK. The fail-closed M0 gen-data transport
intervention is accepted without adding a production CLI seam.
The later GC-01 adjudication explicitly permits correcting Ruby's reproduced
progress callback crash; all other GC effects and genuine failures remain gated.

Only `design.md` was written by architect0; no application edits, builds, commits,
deployment, merges, roster changes or lifecycle actions. A read-only local Nix
version query was denied at the daemon socket; root's successful pinned-version
evaluation supplies toolchain evidence. Raw fixture/build/CI results remain
owned by implementers and lead. The document whitespace check passes. Architect
remains available for implementation deviations and fixture findings; no further
research or edits are needed until one arrives. Lead owns plan/state, artifact
registration, assignments and serialized Git coordination. The session stays open.
