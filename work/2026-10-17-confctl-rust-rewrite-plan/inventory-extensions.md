# Site extension inventory for the Rust confctl plan

Status: **COMPLETE — final implementer1 evidence package**. Planning and
read-only source inspection only. implementer1 owns this file; the lead owns
tracking, artifact registration and commits. Architect0 owns protocol/design.

## Early findings for architect0

1. There are exactly **two confctl user scripts**, with two hook subscriptions
   and one command: `scripts/discover_netbootable.rb` and
   `scripts/runtime_kernels.rb`. A repository-wide Ruby search found no other
   `ConfCtl` users. Other site Ruby service configuration is a separate concern.
2. `cluster_deploy` is a **prepare hook**, despite its name: after selection,
   validation and confirmation, before either building or looking up a selected
   generation, before already-current filtering, copying and activation. It also
   runs for `--copy-only` and all switch actions. It does not run for standalone
   `build`. Preserve this ordering to make fresh kernel data affect the build.
3. The kernel script owns **persistent build input**, not just presentation:
   ignored `configs/node/kernels.json`. Impure site Nix evaluation reads the live
   checkout through `PWD`; it controls `boot.kernelVersion`. Preserve this file
   path, machine-name keys, merge/delete behavior and live-root association.
4. Ordinary SSH command failures are **nonfatal host results**: print `error`,
   delete that selected host's old value, preserve unselected keys, save and
   continue. JSON/read/write errors and other unhandled failures abort. Do not
   make every failed host abort `deploy.prepare`.
5. Explicit `runtime-kernels update` includes selected unmanaged and carried
   vpsAdminOS entries; the deploy hook excludes carried entries and inherits
   core's managed selection. Neither script adds a runnable-target filter.
6. Rediscover writes `cluster/cluster.nix` **before** invoking the netboot hook;
   the hook must evaluate the new list. `add` and `rename` invoke it too. The
   hook writes tracked `cluster/netbootable.nix`, which configures carrier images.
7. Site `flake.lock` pins confctl **7bee58a5**, while canonical confctl master is
   **cc40679d**. These are distinct source baselines. The extension loader,
   selection/confirmation, SSH and state helpers used here are unchanged across
   them; the prepare-hook body has the same stage and payload at both revisions.

## Sources and inspection boundary

| Label | Repository and immutable revision | Meaning |
| --- | --- | --- |
| V | `vpsfree-cz-configuration` `3ae43f560ec7c0e6400322a5777118232dcdb26b` | Canonical local `HEAD` and `origin/master` at inspection; site inventory baseline |
| C | `confctl` `cc40679d267165aecfa569128438bb55fe910268` | Canonical local `HEAD` and `origin/master`; Ruby rewrite baseline |
| P | `confctl` `7bee58a52372b95c2198ce3f2a719807a3c2c66b` | Exact confctl input locked by V `flake.lock` |

Paths below are relative to the labeled repository. No fetch was performed;
these are locally available source identities, not a claim about current remote
or production state. V/C were inspected through immutable Git archives in
own-session `/tmp` scratch; P through `git show` and bounded diffs. No project
files, refs, worktrees, builds, live machines or lifecycle state were changed.

Session binding was independently verified with `dev-session current`; both
environment identity values match this session and workspace. Required workspace
and repository guidance and the `dev-session-documentation` skill were read.
Reporting tool `report_to_lead` is absent; the lead explicitly selected this
artifact as the reporting fallback. No permissions or reporting fallback retry.

## Concrete path-to-replacement map

These are requirements/recommendations for the architect's selected executable
extension design, not additional accepted protocol decisions.

| Existing source/input | Current invocation and effects | Concrete Rust replacement |
| --- | --- | --- |
| V `scripts/discover_netbootable.rb:3` | `ConfCtl::UserScript.register`; subscribes to `configuration_rediscover`; no CLI command | Configuration-owned Rust executable handler `netboot.rediscover`, statically registered for proposed `rediscover.after-write` |
| V `scripts/discover_netbootable.rb:9` | Fresh full inventory; select truthy `netboot.enable` and non-carried entries, independent of spin/managed/runnable | Host inventory service returning ordered names, custom metadata and carrier identity; handler applies the same predicate |
| V `scripts/discover_netbootable.rb:18` | Overwrite tracked `cluster/netbootable.nix` as a Nix string list with existing generated header | Handler owns same relative output; request host literal-Nix formatting or use an explicitly compatible serializer; preserve evaluated list order and trailing newline |
| V `scripts/runtime_kernels.rb:24` | Register `runtime-kernels update [machine-pattern]`, `--show-trace`, repeated `-a/--attr`, repeated `-t/--tag`, `-y/--yes` | Static command declaration; Rust handler `runtime.update`; host parses options, selects machines, renders confirmation/list and owns terminal |
| V `scripts/runtime_kernels.rb:7` | Subscribe to `cluster_deploy`; filter confirmed managed selection to non-carried vpsAdminOS; skip entirely if empty | `runtime.prepare` handler for proposed `deploy.prepare`, receiving confirmed scope; no second prompt; wait before build/generation lookup |
| V `scripts/runtime_kernels.rb:65` | Load existing state, run `uname -r` per selected machine concurrently, merge successes/delete command failures, print ordered table, write pretty JSON | Shared Rust kernel-update routine behind both handlers; host-owned execution service, ordered result vector, explicit host-failure versus invocation-failure types |
| V `configs/node/kernels.json` (ignored, absent from Git) | Mutable JSON object keyed by full configuration machine name; retained between invocations | Keep path and ordinary JSON object format; do not relocate into private extension state or replace keys with Nix flake keys/carrier aliases |
| V `configs/node/kernels.nix:21`, `configs/node/base.nix:24` | Live JSON read through `PWD`; manual runtime override wins, then JSON, then default kernel; `boot.kernelVersion` consumes result | Retain Nix contract and `impureEval`; set child and Nix CWD/PWD to the live configuration root; invalidate relevant evaluation/build-plan caches after hook writes |
| V `cluster/netbootable.nix`, `lib/netboot-machines.nix:14` | Generated names feed build/APU carrier entries, aliases, tags and PXE overrides | Keep tracked Nix list and downstream schema; do not replace with presentation output/JSON without a separate configuration migration |
| V `flake.nix:164`, `Gemfile`, C `nix/flake/mk-config-devshell.nix` | Site uses packaged confctl and independent Ruby tooling in `mode = "tools"` | Pin Rust confctl and site executable/registry together through Nix; preserve tools mode and Ruby service tests/hooks; no runtime Cargo download/build |

## Invocation, API and observable behavior detail

### Existing extension runtime

C/P `lib/confctl/user_scripts.rb:3` loads every regular file directly inside
`scripts/`, without filtering by extension or sorting `Dir.entries`. It uses
Ruby `load` in the confctl process. There is no subprocess isolation, manifest,
versioned extension API or runtime dependency declaration. Missing `scripts/`
is allowed; a load/setup exception is not caught here. C `lib/confctl.rb:42`
loads/setup scripts before CLI setup; C `lib/confctl/cli/app.rb:536` adds their
commands after builtins. This allows arbitrary Ruby code during startup/help,
even though the two site scripts only register classes at load time.

C/P `lib/confctl/hook.rb:4` registers hook names. Subscribing to an unknown name
raises. Subscribers run synchronously in subscription order; the previous
subscriber's return is supplied as keyword `return_value` to the next. There is
no exception recovery or automatic retry. Neither site script uses that return
chain. Both subscribe to different events, so their relative load order does
not currently affect each other. Proposed deterministic registry ordering is
therefore safe for these two scripts; it is a new generic extension contract.

The required API surface can be much smaller than the Ruby object graph:

| Ruby surface relied upon | Required executable-boundary equivalent |
| --- | --- |
| `UserScript.register`, `setup_cli`, GLI command DSL | Static command/group/option declarations, parser validation and help owned by host |
| `setup_hooks`, `Hook.subscribe` | Versioned named events, explicit ordering and parent-operation completion/failure contract |
| `MachineList.new`, `select`, `map`, `each`, `each_key`, `length`, `empty?` | Ordered inventory/selection records; no implicit managed/runnable filtering |
| `Machine#[]`, `spin`, `carried?` | Full custom metadata with dotted lookup, spin and nullable carrier identity; preserve missing/null/false distinctions |
| `Cli::Command.run`, `require_args!` | Host-owned invocation validation, log/error integration and agreed command exit status |
| `Cli::Command#select_machines` | Shared exact-name/key/glob selection with repeated attribute and tag filters |
| `ask_confirmation!`, `list_machines` | Host prompt and inventory renderer; use configured columns and honor `--yes` |
| `MachineControl.new(machine).execute('uname', '-r')` and result `.out` | Host-owned execution against selected machine identity; argv, raw output, command status and typed infrastructure errors |
| `ParallelExecutor.new(machines.length)` | Concurrent item requests with results rendered in selection order; a finite new limit must be documented as new scheduling policy |
| `ConfDir.path` | Explicit canonical live configuration root, also used as CWD/PWD |
| `NixFormat.to_nix` | Literal Nix string-list formatting, preserving intended values and order |
| `Rainbow(...).bright`, `puts`, `format` | Host-owned styled messages and table primitives, separate from machine-readable protocol |
| Ruby `JSON`/`File` | Extension-owned local state/file I/O with compatible paths/content; atomic replacement is a recommended improvement |

### Netboot discovery

V `scripts/discover_netbootable.rb:7` has no additional confirmation and receives
no selected machines from the parent. It reevaluates **all** inventory after
core rediscovery, keeps `netboot.enable` truthy and `!carried?`, and emits names
in evaluated inventory order. The Nix option is boolean (C
`nix/modules/cluster/default.nix:76`), so literal `true` is sufficient for valid
inputs. NixOS and vpsAdminOS, managed and unmanaged entries remain eligible.
Being a carrier is not the same as being carried.

It prints `replace cluster/netbootable.nix`, truncates/overwrites that file,
writes the exact generated header shown in the existing file, then the Nix
list and a final newline. It does not stage/commit files, query SSH or deploy.
Empty selection writes an empty list. Evaluation or write failure aborts the
parent; it does not undo earlier writes. Core `rediscover` atomically replaces
`cluster/cluster.nix` first (C `cli/configuration.rb:93`, `:299`); `add` and
`rename` call that method. Invalid new machine metadata can therefore leave a
new core list but the old extension list. `rename` does not rewrite kernel JSON
keys; those old keys remain until separately changed or selected.

V `lib/netboot-machines.nix:14` imports the generated list and produces carried
entries with location/name aliases, tags, requested build attributes and
generation retention. It adds `configs/node/pxe-only.nix` for vpsAdminOS.
Concrete importers are `cluster/cz.vpsfree/machines/build/module.nix:37`,
`cluster/cz.vpsfree/machines/brq/apu/module.nix:36` and
`cluster/cz.vpsfree/machines/prg/apu/module.nix:44`. V has 14 generated names,
including NixOS live media. A replacement must not restrict this to OS nodes.

### Runtime-kernel selection, prompts and execution

V `scripts/runtime_kernels.rb:49` accepts zero or one machine-pattern argument.
Selection first uses exact full machine name, then exact Nix machine key, then
Ruby `File.fnmatch?` with extended brace patterns. Attribute predicates are
ANDed string comparisons using `=`/`!=`; repeated tags require all positive
tags and reject all `^negative` tags (C/P `cli/command.rb:163`,
`cli/{attr_filters,tag_filters}.rb`, `pattern.rb`). The script subsequently
filters only `spin == 'vpsadminos'`. It does not call `.managed` or `.runnable`.
Carried entries execute against their own metadata target, not the carrier;
their full synthetic inventory name is also the JSON key.

Without `--yes`, explicit update displays “The following machines will be
queried:” and the normal configured machine table, then the shared confirmation
prompt. V `configs/confctl.nix:4` selects name, spin, node role, host name,
location and domain. `--yes` skips that entire listing/prompt block, not just
input. A negative answer raises `Aborted` before state/network changes. The Ruby
prompt accepts `y`/`n` case-insensitively; despite `[y/N]`, a blank line loops
and EOF raises (C/P `cli/command.rb:73`). Exact prompt-loop quirks are an
explicit compatibility decision for the design, not a reason to add a second
extension-owned prompt. A zero-machine explicit update still prompts unless
`--yes`, prints the kernel header and rewrites state.

The deploy hook instead receives core's confirmed managed-machine list, removes
carried/non-vpsAdminOS entries, and returns without a message or file access if
empty. Otherwise it prints bright “Updating runtime kernel information...”,
runs the same update routine and prints a final blank line. It has no extra
confirmation. C/P `cli/cluster.rb:46` places this before generation lookup/new
build, even when every target is later skipped as already current. It receives
`machines`, `generation`, `action`, `opts`, and the hook's return-chain keyword.
The existing `action` payload comes from `opts[:action]`, although the effective
action is parsed from `args[1]`; the site ignores it. Passing the correct
effective action in the new protocol should be documented as a payload fix.

`State.update` loads JSON **before** network work, starts one worker per selected
machine and waits for all workers. It runs `uname -r` locally when
`host.target == 'localhost'`; otherwise it uses OpenSSH as root, configured
target/port and optional `CONFCTL_SSH_CONFIG`, with shell-escaped remote argv
(C/P `machine_control.rb:125`, `:157`, `:177`). It does not use
`test_connection`'s short timeout options. No whole-operation timeout, execution
limit or cancellation cleanup is declared by this script. New timeout/limit and
child-supervision policies must be named as intentional improvements.

On success, it strips the captured stdout, splits on `.`, takes up to three
components and joins with `.`. Thus `6.12.3-extra.more` becomes `6.12.3-extra`:
this is not semantic-version parsing or removal of suffixes. Ruby drops trailing
empty split components. Empty stdout becomes an empty string and is saved;
synthetic successful stdout equal to `error` is displayed but leaves an old
value unchanged. These edge cases need differential fixtures or an explicit
design deviation. It does not inspect successful stderr as kernel data.

`TTY::Command::ExitError`, including a nonzero SSH exit, is captured per host.
It prints that host as `error` and later prints `Error on <host>: <message>`;
then it deletes that host's previous JSON entry. Selected successes replace
their entries; unselected entries survive, including stale/renamed keys. Even
all captured host failures follow normal successful completion after saving.
Other exceptions, malformed JSON, unreadable files and save failures escape and
abort; no automatic rollback/retry occurs. Error diagnostic order follows
concurrent completion and should not be treated as deterministic. Kernel-table
rows follow selection order regardless of completion order.

### Machine-readable data versus presentation

| Surface | Contract and compatibility consequence |
| --- | --- |
| `cluster/netbootable.nix` | Tracked Nix list of full non-carried machine names; generated header and ordering matter for reproducible diffs; consumed as Nix data |
| `configs/node/kernels.json` | Ignored mutable JSON object: full inventory names to kernel strings; source-controlled file is absent by design; preserve unselected keys and failed-host deletion |
| Host inventory/exec protocol | New typed machine-readable surface; transmit complete metadata and ordered records; separate control frames from stdout/stderr and terminal events |
| Kernel stdout table | Human presentation: `HOST` padded to at least 50 characters, one separating space, `KERNEL`, then ordered rows; no JSON output option in this script |
| Confirmation machine list | Human presentation via shared output formatter and site columns; never parse `confctl ls` text to reconstruct machines |
| Bright message, replacement notice, error paragraphs | Presentation/logging, with host-owned color policy; not protocol messages or success indicators |

V `configs/node/kernels.nix:21` documents that runtime manual overrides win over
JSON and the default kernel. It checks live `$PWD/configs/node/kernels.json`
first, then source-relative JSON, then `{}`. V `flake.nix:160` explicitly enables
impure evaluation. `configs/node/base.nix:35` consumes the runtime choice;
`configs/node/pxe-only.nix:22` consumes the separate boot override/default.
Consequently, a prepare hook must finish its write before the next impure build
evaluation, with stale build-plan/inventory caches invalidated. Keep the
confirmed machine scope fixed rather than expanding it after a refresh.

The current writer uses `JSON.pretty_generate` without a final newline or
atomic rename/lock. It treats only missing files as `{}`. It does not validate
the parsed JSON root/value schema up front; non-object roots may fail later on
string-key updates, while a zero-machine run may simply reserialize them.
Strict object-of-strings validation, atomic replacement and a shared operation
lock are recommended improvements, to be recorded as such. Do not discard
unknown or unrelated state as a migration shortcut. New-process locking cannot
coordinate an old Ruby writer; mixed concurrent writers must be excluded.

## Packaging and Ruby-removal boundary

The architect's chosen subprocess boundary fits both scripts without retaining
Ruby inheritance/GLI/TTY objects. Recommended site layout is an
`extensions/` Rust package with `Cargo.toml`, committed `Cargo.lock`,
`src/main.rs`/handler modules and Nix package/registry files. One executable can
dispatch `netboot.rediscover`, `runtime.update` and `runtime.prepare`. Import
only a public confctl protocol/SDK crate; do not bind site policy to private
core Rust modules. Core owns selection, prompting, terminal and privileged
execution. Site code owns the two generated files and kernel policy.

Use a static, versioned Nix-generated registry with store executable paths and
explicit live configuration-root binding. Help/command discovery should require
no handler startup, Nix machine evaluation, PATH scanning or runtime compilation.
Version both protocol and SDK/package dependencies; pin compatible site/core
artifacts together. Unknown protocol/collision/legacy-script cases need useful
diagnostics before mutation. If legacy `scripts/*.rb` remain after migration,
never silently ignore the missing operational hooks; the design must require
their deliberate removal/relocation and make incomplete migration visible.

Specific packaging changes to plan, not execute:

1. C `nix/package.nix` currently wraps Ruby/Bundler and prepends git, OpenSSH and
   Nix. Its Rust replacement must preserve those external execution dependencies,
   packaged manuals and stable flake package/library entry points.
2. V `flake.nix:164` uses `mkConfigDevShell` **tools mode**, with Ruby 3.4,
   Bundix and bundler-audit. Its `Gemfile` does not depend on confctl. Add the
   site executable and registry through the shell/launcher interface and pin
   the Rust core; keep repository tooling independent from confctl's runtime.
3. Keep Ruby here: V has 33 Ruby files. Two are the confctl scripts; 20 under
   `configs/vpsadmin/api/` belong to vpsAdmin/HaveAPI, one is the network-graphs
   service, one the Discourse plugin, eight are specs/support and one the
   Overcommit Nixfmt hook. None of the other 31 references `ConfCtl`. They are
   not part of a confctl extension rewrite. The existing Gemfile/test hooks
   remain needed; do not delete them merely to claim Ruby-free confctl.
4. Confctl also packages Ruby **remote helpers**: `carrier-env.rb`,
   `build-netboot-server.rb`, `kexec-netboot.rb`, and `libexec/auto-rollback.rb`.
   They are core/helper ownership, not additional site user scripts. Coordinate
   their Rust replacement and compatibility checks with implementer0's/core
   inventory. V `configs/node/base.nix:77` enables kexec-netboot and the carrier
   importers above depend on netboot behavior. Replacing only the CLI would
   not remove Ruby from those helper packages.
5. Preserve V `configs/node/pxe-only.nix:25` machine-image JSON, including
   `inputs-info`, and carrier/netboot/rollback state and remote CLI contracts.
   No extension protocol change alone requires every node/carrier to update
   together. Assert this through mixed old/new helper tests before rollout.
6. Update site README/operator extension instructions with the actual Rust
   command and rebuild/reenter-shell requirements. Current V README describes
   a `shell.nix` shim and generated `./.man`, but V's Git tree has no
   `shell.nix`; C tools-mode code points MANPATH at packaged source manuals.
   Source inspection takes precedence over those stale setup statements.

Switch the operator tool, registry and migrated site source as one compatible
configuration release after acceptance. Preserve both file formats and retain
the previous Ruby tool/source revision for software rollback. Keep old scripts
with that old revision or outside auto-discovery, not live beside the new
registry. Restoring the previous tool/configuration must read the new writer's
files. Rollback does not undo completed file updates, already deployed systems
or deleted failed-host kernel entries. No database migration, public API/client
or Terraform change is required by these two site extensions. No live rollout
was attempted here.

## Differential acceptance scenarios for the implementation brief

These are proposed checks, **not executed verification**. Use disposable source
trees, fake host-service implementations, deterministic clocks/process outcomes
and fixture SSH executables; reserve Nix/VM checks for the later implementation
verification plan. Run the original scripts against the P/C-compatible API as
the behavior oracle, rather than rewriting their policy inside the oracle.

| Scenario | Required observation |
| --- | --- |
| Fresh rediscover; add; rename | Core list becomes visible before exactly one hook; generated netboot list matches each new inventory; no standalone build hook |
| Netboot selection matrix | Include netboot-enabled non-carried NixOS/vpsAdminOS and unmanaged entries; exclude carried/disabled entries; preserve evaluated order |
| Empty netboot inventory | Correct header, empty Nix list and final newline; valid data for downstream imports |
| Discovery evaluation/write failure | Parent fails; earlier core-list/add/rename effects remain visible; no invented rollback |
| Explicit update without pattern | All vpsAdminOS entries, including unmanaged and carried, selected; no hidden runnable filter |
| Exact name, key, glob/brace, filters | Name/key precedence, ANDed attributes, positive/negative tags and repeated options match Ruby; excess args rejected before network/file changes |
| Yes, no, EOF and zero matches | `--yes` skips preview/prompt; decline/EOF prevents update; zero matches still follows explicit command's header/save path; prompt quirks explicitly accepted or changed |
| Deploy switch/boot/test/dry-activate | Hook after validation/confirmation and before build or generation lookup; non-carried vpsAdminOS subset only |
| Copy-only, selected generation, already current | Hook still runs once before later filtering; final inventory remains confirmation-scoped; invalid/declined/empty deploy does not run it |
| Deploy without eligible OS targets | No kernel message, file read/write or host queries |
| Mixed query completion order | Requests may finish out of order; table/state keyed to correct host and table retains selection order |
| Localhost, SSH port/config, carried | Host service reproduces direct-local and root SSH routing/escaping, honors `CONFCTL_SSH_CONFIG`; carried target is not silently replaced by carrier |
| Kernel normalization | Cover normal suffixes, more/fewer than three dot parts, trailing empty parts, empty stdout and literal `error`; compare state and visible values |
| Host exit 1/255 and success stderr | Failed selected host printed/deleted, successful stdout used, success stderr does not become state; unselected entries survive; parent continues after ordinary host failures |
| All hosts fail | Header/errors emitted, selected old keys removed, unrelated keys preserved and normal successful completion after save |
| Missing, malformed, scalar/array JSON | Missing becomes `{}`; malformed read fails without replacement; document explicit strict-shape policy versus Ruby's deferred type failures |
| File permission/rename/write failure | Parent fails, old file retained under proposed atomic writer where possible; completed earlier file effects are not misreported as rolled back |
| Hook-written JSON affects Nix | Next impure build sees the live root's newly written kernel version; no stale store-source read or cached build plan; manual override still wins |
| Ruby ↔ Rust state round trip | Full names, carried synthetic names, unselected keys, pretty JSON and generated Nix remain readable by previous tool/configuration; no schema wrapper inserted |
| Registry/root mismatch or old scripts | Clear migration/version failure before mutation; wrong checkout cannot reuse another root's handler binding; help starts no handler |
| Protocol/output/cancellation failures | Control frames never contaminate presentation or files; host distinguishes nonfatal item errors from invocation failure, owns prompt/terminal, cancels and reaps owned children |
| Packaged site shell | Correct pinned Rust CLI and executable/registry resolved without network compilation; existing Ruby tooling/spec environment still usable |
| Carrier/PXE and older helpers | Netboot imports/aliases/tags and image JSON unchanged; both client/helper version directions meet core compatibility brief |

Compare machine-readable file values, selected identities, command argv,
hook-stage traces, exit classes and error sets directly. Normalize only
presentation choices the user allowed to change; do not normalize away failed
hosts, missing writes, stale input, confirmation or ordering. Error paragraphs'
completion order and cosmetic column/color changes can vary; ordered tables
and state semantics cannot. Test the accepted bounded-execution/timeout/atomic
write policies separately from legacy parity cases.

## Final report to lead

**Assignment complete.** Every confctl Ruby extension at V is mapped above to
invocation, selection/confirmation, side effects, required APIs, proposed Rust
handlers, packaging and acceptance. The critical constraints are prepare-hook
ordering, live ignored kernel JSON, nonfatal host failures and different
carried/managed selection between explicit and hooked updates.

Verification was source-only: immutable V/C archives, P source comparison,
repository-wide Ruby/ConfCtl search, downstream Nix consumers and packaging
inspection. No scripts were executed, so exact GLI process exit codes, network
behavior and Nix results remain future differential/runtime acceptance. No
test/build/deployment claims are made. No project files or commits changed.
Only this assigned tracking artifact was written; scratch copies are in `/tmp`.
Artifact status, revision identities, script coverage and whitespace checks
passed; the cited startup and Nix consumer locations were rechecked.

Historical context read: the prior session's `extension-system.md` (SHA-256
`190276384afad6da7bd1b7110e0b8303c133c6592bb64721a8b70a7aba609fe7`). It already
records similar executable-boundary and hook-stage constraints. This inventory
reconciles its recommendations with V/C/P source; it does not accept that older
Go design or claim its implementation status. No historical worktree/branch
was used or modified.

Remaining design decisions for architect0 are protocol details and explicit
policy for prompt quirks, timeouts/concurrency limits, strict JSON validation,
atomic writes/locking and corrected effective-action payload. These are
recommendations/deviations, not blockers to completing the evidence package.
Lead should register this artifact and serialize tracking/commits; implementer1
did not mutate the manifest/state or retry unavailable reporting transport.

Stable session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-17-confctl-rust-rewrite-plan/
