# Codex runtime package

Use the [runtime update skill](../skills/update-dev-workspace-codex/SKILL.md)
for a version upgrade. It delegates protocol and catalog maintenance to the
selected codex-web source's update skill.

`lib.mkCodexPackage { pkgs; codex; }` assembles a complete runtime package from
an already selected upstream Codex output. It copies the native executables
without rebuilding Rust, changing their ELF interpreter or RPATH, or stripping
store references. The supported host platform is `x86_64-linux`.

`lib.mkPackage` uses this helper once for the workspace's bundled Codex.
System configurations can pass their selected Codex output to the same helper.
Each consumer supplies its own `pkgs`, so equal Codex versions can have different
dependency closures.

## Upstream packaging and removal

The helper is a downstream workaround for missing complete-package metadata
and resources in the selected llm-agents output. It leaves Codex Rust code
unchanged. The complete-package layout is required by the upstream native daemon. See
[llm-agents issue #9887](https://github.com/numtide/llm-agents.nix/issues/9887),
[the proposed complete-layout packaging in PR #9889](https://github.com/numtide/llm-agents.nix/pull/9889)
and [Codex issue #48050](https://github.com/openai/codex/issues/48050).

Remove the helper only when the selected llm-agents Codex output itself provides
a complete, daemon-copyable package with materialized helpers. Both workspace
and system consumers must use that output directly and pass the existing
normal-startup, resume/fork, manifest/helper/copy and closure-retention checks.
Issue closure or a newer CLI version alone is insufficient. Migrate both
consumers before removing the helper. Preserve retained roots and their
dependencies, and keep the regression coverage.

## Runtime layout

The package has these paths:

```text
bin/codex
bin/codex-code-mode-host
bin/logs_client
share/                           upstream shell completions
libexec/codex/
  codex-package.json
  bin/codex                      native executable
  bin/codex-code-mode-host        native executable
  bin/logs_client                 native executable
  codex-path/rg
  codex-resources/bwrap
```

The public Codex launcher forwards arguments to this output's native entrypoint
and puts bubblewrap on `PATH`. The helper commands and completions keep their
existing public interfaces. Missing required executables fail assembly.

The manifest contains `layoutVersion = 1`, the input's `version`, the host Rust
`target`, `variant = "codex"`, `entrypoint = "bin/codex"`,
`resourcesDir = "codex-resources"` and `pathDir = "codex-path"`. This follows
the [upstream package layout](https://github.com/openai/codex/blob/rust-v0.164.0/scripts/codex_package/README.md).

The runtime root retains resources supplied by the input. File and directory
links are dereferenced during copying; no symlinks remain anywhere below
`libexec/codex`. Public links outside that root are allowed. Ripgrep and Linux
bubblewrap are regular files at the paths above so the native daemon can copy
the runtime root without links that escape its package.

## Daemon selection and dependency retention

The selected llm-agents package patches native daemon installation to use its
original immutable Nix-store runtime in place. It disables upstream release
updates for that selection and attempts to register a native daemon GC root.
The assembled executable retains the original package's embedded store reference,
so Nix retains that package and its dependencies as part of the assembly closure.
The native daemon can therefore execute the original output rather than the
materialized assembly. Check its actual executable independently.

Retained daemons from older package generations can still use runtime copies
under `$CODEX_HOME/packages/app-server-daemon/`. These copies retain their ELF
interpreter, libraries and embedded store references. Copying files into
`CODEX_HOME` does not create a Nix GC root.

Workspace activation retains the selected assembled Codex output through
`~/.local/state/dev-workspaces/codex/current` and
`~/.local/state/dev-workspaces/codex/generations/<generation>`. A deployment
using a different user namespace has the same paths under its selected state
root. System generations independently retain the system Codex package and its
closure. Retain both sets of roots when using system and workspace commands.

Keep retained workspace Codex roots and system generations while a daemon copy
may depend on them. Before pruning a generation, establish that its closure is
unused or retain that exact assembled output through another GC root. Inspect
the output and its dependencies without running garbage collection:

```sh
assembled=$(readlink -f "$workspace_package/libexec/codex")
nix-store --query --references "$assembled"
nix-store --query --requisites "$assembled"
```

Here `workspace_package` is the selected workspace application output. For a
system-only consumer, inspect its assembled Codex output directly.

The package pin selects the workspace's explicit App Server and terminal pair.
Retained native daemon state or an already-running daemon can still select a
different executable. Check its version and store identity separately from the
public command's `--version`; assembly alone does not establish what is running.

## Verification and recovery

The `codex-package` flake check verifies the manifest, executable bytes and
native identity, completions, launcher targets and input/output version. It
also covers materializing file and directory links and rejecting a missing
required executable. Native daemon startup and persisted-state compatibility
need separate probes with a private disposable `CODEX_HOME`.

Workspace recovery remains forward-only: repeat an interrupted supported
`workspace-host switch` or select a corrected newer package. Preserve transition
journals and retained Codex roots. See the [portal recovery guide](workspace-portal.md#user-profile-state)
for the supported entry points. System recovery uses its retained system
generation; whether an older Codex can read newer state must be established
separately on disposable state before using that recovery path.

Workspace package switches compare the candidate's resolved native executable
and launch contract, rather than its CLI version string or package path. With
the live-switch contract, an unchanged native invocation preserves the running
App Server and terminal clients. The initial cutover from an older package and
any changed invocation require idle sessions; see
[switching while threads are active](workspace-portal.md#switching-while-codex-threads-are-active).

## Session naming release boundary

The portal's session namer uses a portal-owned, naming-only App Server with
exact Codex 0.164.0 and `gpt-6-luna`/`low` through codex-web's
`RunPromptedEphemeralTurn`. The package installs codex-web's derived Luna catalog
as
`share/workspace-portal/codex-models.json`. The
[preparation contract](session-preparations.md#naming-and-reservation) defines
the fixed restrictions, disabled Responses Lite mode and startup
catalog checks, and links to codex-web's exact metadata contract. A startup CLI
override selects the native static models manager for this child; the ordinary
App Server retains its dynamic catalog. The helper checks the immutable file
and startup `sessionFlags` origin before inference. It does not patch Codex or
rewrite shared Codex home.
Naming instructions tell the model to treat the request as data and avoid tools,
files, commands, browsing, delegation and questions. The private call retains
its fixed restrictions and rejects interactive requests, but native tools can
remain available. The prompted contract makes no guarantee about native tool
registration, tool attempts or their effects. Global user instructions remain
trusted serving-instance policy. CodeModeOnly models are unsupported because
yielded cells can survive completed turns without a supported scoped stop/join
operation. Codex-web's strict `RunEphemeralTurn` API retains its separate
supported 0.163 contract. Both releases use identical immutable Luna catalog
bytes, which do not establish native version or tool isolation.

Before enabling a candidate deployment, run the codex-web protocol corpus and
fixed restriction-key/type validator against that candidate's generated App
Server schema and `core/config.schema.json`. After mandatory review, run the
tagged exact-binary mock-provider fixture described in codex-web's technical
reference. Record the exact native binary hash, assembled package/profile and
supported catalog metadata, actual advertised tool schemas, dispatch behavior,
question rejection and ephemeral teardown evidence. Include the startup
catalog path/origin, local-only child launch and actual managed-service
start/loss/stop/forced-exit checks with ordinary-daemon continuity. The real
positive naming canary must use this same child, packaged instructions and model,
and obtain a valid result within the thirty-second budget. Missing prerequisites or unsupported
behavior block release. Naming errors must stop preparation before reservation
and preserve the request for retry or a custom name.
The [managed fixture and separate real canary](#naming-acceptance-fixtures)
below cover the packaged naming path with disposable state.

The child reads the existing host-selected account/provider configuration and
uses the pinned version's local-only launch marker; credentials are not copied
into a new home or passed in argv. The portal owns its process group and join,
including early child exit and portal failure. Native ephemeral storage excludes
resumable conversations but its separate SQLite diagnostics can retain input
and identity in plaintext. The existing local logger remains enabled, and its
periodic pruning does not guarantee an erasure deadline. See the
[preparation contract](session-preparations.md#naming-and-reservation) for runtime
ownership, naming-input bounds and native logging semantics.

MCP names are captured once per bounded naming call. Pause/stop naming through
the existing portal service or supported package transition before changing MCP
configuration. Finish that reconfiguration while no naming call is active;
fresh calls capture and disable all literal names then present. This support
condition does not include deliberate administrator reconfiguration during a
call. Use the existing service/package procedures, without a global config
lease or another process manager. Package-generation cancellation must prevent
the old worker from publishing a name or reservation.

## Naming acceptance fixtures

`lib.mkNamingRuntimeTests { pkgs; package; provenance; }` returns `fixture`,
`manifest`, `managed` and `realCanaryDriver`. Pass the final assembled workspace
package, including its extension and team resources, and the runtime's locked
root nixpkgs. The package source must match this runtime's committed source.
The constructor is separate from default checks, CI and application build phases.

`provenance.heads` requires the actual `runtime`, `provider`, `extension` and
`workspace` revisions. `protectedRuntimeAncestor` and
`protectedExtensionAncestor` retain their consumed lineage;
`inputReceipts.source`, `.inputs` and `.ancestry` are the SHA-256 identities of
the approved external receipts. The caller supplies and verifies those receipts
and ancestry. The fixture checks explicit identities and resource hashes; it
does not establish Git ancestry. Do not substitute example or guessed revisions.

`fixture` compiles only the tagged portal test binary with the selected package's
Go compiler, `goModules`, pin check and review assets. Its build runs no tests or
native process. The separate schema1 manifest hashes the installed fixture
after fixup, actual package resources, all installed team resources and owning
sources. Before building, inspect `fixture.fixtureContract` and prove its
source, compiler, vendor derivation and tag equal the accepted selection.
The source and package bounds remain 32 and 512 files respectively.

Freeze a nonsecret selection expression using the final package and provenance.
After review and separate build release, its only build selections are
`fixture`, `manifest`, `managed.driver` and `realCanaryDriver`. Record their
actual output/derivation identities and retain their closures. A built driver
does not prove acceptance. Run each returned driver's `bin/nixos-test-driver`
with `-o` and a new owned output directory, through a fresh verification watcher.

The managed driver uses a disposable NixOS VM, UID1000, a lingering user manager
and cgroup v2. It invokes `^TestManagedNamingRuntimeIntegration$` and then
`^TestNativeNamingRuntimeHTTPFailure$`, each with count1 and verbose output.
The five managed subcases retain two concurrent naming slots, queued successors,
missing-home and child-loss refusals, MainPID TERM/KILL and ordinary synthetic
continuity. Both invocations use synthetic provider traffic. A fixed guest-only
sudo helper reads the owned nftables counter; actual failed TCP39991 dial,
counter increase, zero listener hits and successful mock GET404 are required.
Other developer egress is denied. No host firewall or installed workspace is used.

Each case creates its own mode0600 schema1 workspace registry, mode0700 state
and an exact-package profile link. The provider catalog and saved provider state
must be absent. This supplies the real read-only provider projection without
host registration, activation or a registration marker.

The real driver is separate and runs `^TestRealNamingRuntimeCanary$` only.
Its explicit launch inputs are `NAMING_CANARY_REAL=disposable-real-luna-v1`,
`NAMING_CANARY_HOME`, `NAMING_CANARY_ACCOUNT_MODE` (`chatgpt` or `apiKey`) and
`NAMING_CANARY_PROVIDER_HOST` (`chatgpt.com` or `api.openai.com`, respectively).
The home must be a dedicated disposable test account with authorized Luna
access, canonical and owned by UID1000, mode0700, with mode0600 `auth.json` and
the following nonsecret `config.toml` bytes:

```toml
model_provider = "openai"
model = "gpt-6-luna"
model_reasoning_effort = "low"
```

Credentials are provisioned separately. Never read or copy production auth or
keys, put credential values in Nix/store/argv/receipts, or use ambient API-key
variables as a substitute. The runtime-only shared-directory mount exposes only
that home at `/run/naming-canary-home`; native opens auth itself. The fixture
checks private modes, the actual mount, exact nonsecret configuration and native
account type without exporting account details. Missing opt-in, usable home,
account access or route blocks the real gate. This interface alone establishes
none of those launch prerequisites.

The real guest permits HTTPS only to the declared provider hostname's resolved
public addresses and DNS only to its declared resolver. It records the selected
route and addresses, keeps the blocked-port counter probe, and rejects endpoint
overrides or mock naming fallback. Unexpected refresh or destination needs
require diagnosis and a new reviewed launch policy before widening access.

The canary submits one synthetic goal through the packaged portal's real form
and POST path, installed team selection and production naming worker. The same
request/receipt/attempt must gain a schema-valid base with `NamingOutcome=model`
within the original thirty-second admission budget, with sanitized production
timing/outcome/category evidence. It adds no retry or second request. A fixed
failing initialization CLI prevents creating a real session or team after
naming/reservation. The ordinary continuity control stays synthetic; the result
does not establish full creation acceptance or native tool-effect isolation.

Managed invocation budgets are twenty and five minutes within a thirty-minute
driver limit. The real driver has five minutes overall. Existing 150/155-second
stop/join bounds remain separate from the naming budget. Missing tests, skips,
failed assertions or cleanup errors fail the gate. Each driver stops and joins
only its own unit/process groups and QEMU instance. A containment shutdown does
not turn failed native cleanup green. Retain failed state, the dedicated home,
partial receipts and original logs without exporting auth or native diagnostic
databases. Diagnose before a fresh attempt; never resume an uncertain result.
Workspace recovery remains forward-only and no session lifecycle action follows.
