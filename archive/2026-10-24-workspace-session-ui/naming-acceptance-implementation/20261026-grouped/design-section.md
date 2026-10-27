## Naming acceptance preparation: managed VM and separate real positive canary

Status: complete bounded design proposal for lead disposition, 2026-10-26.
This supersedes the missing-recipe disposition at line3856 only by specifying
the required implementation. It is not an implementation or execution release.
Architect inspected immutable44a/alhm and selected source documentation only;
no evaluation, build, test, native/provider request or host operation ran.
Owner3 is the proposed implementation owner, alongside the separately released
three Keep-open selector changes. Owner2 retains package/browser preparation;
owner1 retains final source/dependency/consumer binding. Lead serializes their
overlapping runtime work and releases subsequent operations.

### Source findings and minimum committed boundary

The existing tagged tests in
`portal/cmd/workspace-portal/naming_runtime_integration_test.go` enforce actual
UID1000, cgroup v2, immutable manifest/binary/package resources, native/catalog
hashes, denied-dial counter evidence, ordinary continuity and owned stop/join.
Neither the runtime flake nor an accepted retained receipt supplies their
disposable VM, counter or manifest builder. Their factory unconditionally writes
synthetic credentials and loopback-provider configuration. Its denied-network
canary cannot establish a real positive naming result. Transient session scripts
alone are insufficient: new verification logic belongs in committed runtime
test/Nix/documentation source and mandatory review.

One further prerequisite is source-proven. `startUnit` passes
`--workspace-name naming-smoke`, while `privateCase` creates no host registry
entry and its clean environment supplies no host profile selection. Production
`namingProviderArguments` calls the packaged `workspace-host provider native-args`.
`libexec/workspace-provider-sessions.rb:90-91,107` requires that registry entry
and exact selected profile; `libexec/workspace-host:3337` checks the profile.
The CLI requires a nonempty workspace name (`main.go:359`). Thus merely booting
the old fixture in a VM cannot satisfy this path. This is a static fixture
prerequisite finding, not an executed failure or a production defect.

The bounded source package has four owning paths, in addition to the existing
three-selector correction:

1. `portal/cmd/workspace-portal/naming_runtime_integration_test.go`: retain both
   existing tests/assertions; add private registry/profile setup and one
   opt-in `TestRealNamingRuntimeCanary`. Share only existing identity, HTTP,
   process and teardown helpers; use two explicit fixture constructors, with
   common initialization factored only where necessary. No general scenario
   engine, injected production namer, copied naming prompt or production API.
2. New `nix/tests/naming-runtime.nix`: bounded fixture-binary/manifest builders
   and two disposable NixOS definitions, using `pkgs.testers.runNixOSTest`.
   Keep the fixed counter helper and driver scripts here unless their size
   requires an adjacent test-only source file; report that file split to lead.
3. `flake.nix`: export the narrow test constructor
   `lib.mkNamingRuntimeTests { pkgs; package; provenance; }`, bound to this
   flake's `self`. Return only `fixture`, `manifest`, `managed` and
   `realCanaryDriver`. Do not add real inference to `checks`, package build
   phases or default CI. The managed test needs the explicit final composed
   package and genuine provenance; do not invent extension/workspace heads to
   manufacture a generic default check.
4. `docs/codex-package.md`: document the constructor, prerequisites, exact
   selectors, separate synthetic/real claims, safe launch and failure recovery.
   Link from the existing naming release-boundary text; no new operations
   framework or unrelated documentation rewrite.

No change is proposed to `naming_runtime.go`, `session_namer.go`,
`session_name.go`, provider policy, native source, module declarations, catalogs,
production systemd units or ordinary conversation handling. If implementing the
brief needs such a change, return the concrete reason to lead before editing it.

### Immutable selection, build and manifest dependencies

The inspected baseline is runtime `44a483c61d68da59ca915dc5bb4f1a4790a62183`,
tree `3bbfa411eeb6a53be9837ae70effabb0373609dd`, source
`/nix/store/alhmfv9zw2j0p12hifm83vpxw4imzn23-source`. The final fixture must instead
bind the reviewed successor containing all intended test/export corrections.
Use that successor's locked root nixpkgs: presently root edge `nixpkgs_2`,
revision `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`, NAR
`sha256-r2f1oUwixlgq9zOdYLqJLfS/lWBT60/IITjhTKI59JU=`. Do not use ambient nixpkgs
or the separate llm-agents nixpkgs node. The inspected NixOS testing interfaces
provide `runNixOSTest`, `.driver`, fixed driver test scripts,
`virtualisation.additionalPaths`, `sharedDirectories` and `restrictNetwork`.
The Go builder provides `buildTestBinaries`; these are existing interfaces,
not a request to add another VM runner or alter the installed toolchain.

The constructor takes the actual final assembled application derivation from
the accepted workspace package selection, including the actual extension/team
resources. It must assert that `package.src` is this runtime source. The caller
supplies a nonsecret provenance object derived from exact committed consumer
inputs: runtime/provider/extension/workspace heads, protected ancestors and
source/input receipt identities. Heads must be real selected revisions with
ancestry/input proof; syntactically valid dummy hashes are not provenance.
The runtime head must identify `self`; provider remains the actual selected
llm-agents head, currently `ea188d2f072e0ec8d5b71245e228803672801a22`.
Final extension/workspace revisions come from owner0's final receipt, not from
an inferred or stale consumer pin. Preserve protected runtime ancestor9634151
and extension ancestor399c330 exactly as the current validator requires.

Compile only `cmd/workspace-portal` with tag `naming_runtime_integration` into
an immutable Go test executable, using the selected package's Go toolchain,
source, pin check, review assets and exact `package.goModules`. Prefer the
existing `buildGoModule` test-binary support, explicitly reusing `goModules` and
the package's required `postPatch`/`preBuild` inputs. Disable test execution for
this compile derivation, not application checks. Install the test binary only;
do not inherit the application's post-install activation checks/wrappers into
this fixture. Prove the evaluated source/vendor/compiler/tag identities.
No source copy may receive an uncommitted patch; no second hash discovery or
separately selected module set is needed. If an override does not reuse the
expected `goModules`, stop at evaluation and correct the expression before build.

Generate the existing schema1 manifest in a separate nonsecret derivation after
the actual package and fixture output exist. Hash the final installed executable
after fixup, required package files, every installed agent-teams resource, and
required owning sources. Include the new fixture/Nix source and `session_name.go`
within the existing32-source limit; retain the512-package-file bound. Use actual
canonical store paths and actual package derivation, never guessed result paths.
This ordering avoids a manifest/binary self-reference. The manifest generator
must fail on missing resources, mismatched source/provenance or an exceeded bound.
Outside-VM receipts separately bind derivations, complete source/input graph and
manifest hash; the Go validator does not prove Git ancestry or derive provenance.

Keep exact raw0.164 native source10pdz and executable SHA
`d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae`, catalog SHA
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`/62680 bytes,
and client025 unchanged. The package exposes the native child at
`libexec/codex/libexec/codex/bin/codex`; retain actual resolved executable proof.
No custom Codex build, native patch or materialized-resource allowance changes.

### Managed disposable VM and private registry correction

Use a fresh x86_64 NixOS test VM with user `developer`, UID1000, lingering user
manager, unified cgroups and the exact candidate/fixture/manifest closures in
`virtualisation.additionalPaths`. Wait for `user@1000.service` and the user bus;
invoke the immutable fixture as that user with actual
`XDG_RUNTIME_DIR=/run/user/1000` for its systemd control commands. The existing
per-case clean environment retains its private home/XDG directories. Supply
`MANAGED_NAMING_SMOKE_VM=disposable-nixos-user-manager-v1` and all four existing
manifest/package/source/binary variables with generated exact values. Marker
checks supplement real UID/systemd/cgroup/output evidence; they replace none.

The guest's declarative nftables setup owns one private `inet` table with named
counter `denied` and an output chain restricted to UID1000. Permit fixture
loopback traffic except TCP39991; reject that port and deny other UID1000
network egress through the named counter, covering IPv4 and IPv6. The VM also
uses `restrictNetwork = true`. Existing Go probes must prove actual failed dial,
counter increase, zero listener hits and successful mock GET404, then no further
denied packets. Do not reset the counter between that baseline and teardown.
Install only in this guest a fixed no-argument
`/run/current-system/sw/bin/managed-naming-smoke-counter` which executes the
pinned `nft -j list counter inet <owned-table> denied`; reject arguments. Sudo
permits developer to run only that fixed command without a password. No generic
nft/shell sudo grant, host firewall installation or global counter inspection.

For each private case create mode0600 schema1 registry JSON:
`{schema:1,workspaces:[{name:"naming-smoke",root:<actual-private-workspace>,
hostname:"managed-smoke.example.test",aliases:[]}]}`. Its parent and state
directories are mode0700/UID1000. Set `DEV_WORKSPACES_CONFIG` to that file,
`DEV_WORKSPACES_STATE` to that case's state,
`DEV_WORKSPACES_PROFILE` to its existing exact-package profile link, and
`DEV_WORKSPACES_CODEX_PROVIDERS` to a deliberately absent private catalog path.
Assert absence of saved provider state there. These are test data for the real
read-only provider projection, not calls to host `register`, activation or
session creation. Retain nonempty workspace name, exact profile checking and
the existing assertion that no registration marker was created. Update the
fixture comment to distinguish a private registry record from host registration.
No ambient registry/catalog/home may satisfy this setup.

Run two explicit fixture invocations, serially, with `-test.count=1 -test.v`:
`-test.run '^TestManagedNamingRuntimeIntegration$'` and
`-test.run '^TestNativeNamingRuntimeHTTPFailure$'`. Preserve the five managed
subcases: one child/two concurrent slots/third queued; missing home; child loss
without respawn; MainPID TERM; MainPID KILL. Preserve HTTP-listener failure's
worker join before native owner close and ordinary synthetic continuity.
Do not shorten existing150/155-second systemd stop bounds or change the30-second
naming budget. Bound whole invocations, for example20 minutes and5 minutes,
with a finite30-minute driver budget including startup and teardown. Missing
prerequisites, missing tests, skips or cleanup errors fail the gate.

### Separate real positive canary and credential interface

Add `TestRealNamingRuntimeCanary` under the same build tag, run only by an
explicit real-canary selector and opt-in marker. The two existing managed
selectors never enter it. Its constructor shares the validated manifest,
process ownership, ordinary synthetic-control/proxy, HTTP admission and teardown
helpers. It does not call the synthetic naming-home writer and overwrite its
results later: naming uses a separately supplied private fixture home from the
start. Keep the ordinary control explicitly synthetic and label its receipts
accordingly. A real naming mock/provider must not be available as a fallback.

Supported serving interface is `DEV_WORKSPACE_CODEX_HOME` pointing to an existing
absolute private home; production `namingRuntimeEnvironment` supplies it as
native `CODEX_HOME`. Native0.164 accepts its own `config.toml` and auth storage
(`codex-rs/login/src/auth/storage.rs`, `auth/manager.rs`), including a separately
provisioned test account's auth.json. The host provider token-file projection is
another existing product interface, but this bounded canary uses the default
OpenAI provider in a fixture home, with no host provider catalog. Do not assume
`OPENAI_API_KEY` in ambient environment is equivalent: native's default provider
has no `env_key`, and CODEX_API_KEY handling has a caller enablement condition.
Do not introduce a new credential helper or change native/provider auth policy.

Native `model-provider-info/src/lib.rs:430-448` selects
`https://chatgpt.com/backend-api/codex` for its supported ChatGPT auth modes and
`https://api.openai.com/v1` otherwise. Select and record the actual supported
fixture account mode/route without exporting its credential contents; leave
native endpoint overrides unset. Do not assume an API-key account can access
Luna just because a subscription can. Fresh usable fixture auth is a launch
input; unexpected refresh or additional destination requirements stop for lead
disposition instead of silently expanding network or credential policy.

The launch prerequisite is an explicitly supplied, dedicated disposable test
home/account authorized for the real Luna endpoint. It must not be the operator's
production Codex home or a copy of its auth/keys. No such credential or model
access has been established by this design. A supported interface is not an
availability receipt. If the lead cannot supply this owned input, complete the
secret-free build/preparation and report this concrete real-canary blocker;
do not use production credentials or infer success from synthetic tests.

The real driver is built without credentials and runs outside the Nix build
sandbox after separate release. Use the existing QEMU `sharedDirectories`
interface with a runtime-only directory variable, e.g. `NAMING_CANARY_HOME`,
mounted as a fixed guest private native home. Mount only that dedicated directory,
never its parent or the host HOME. Validate canonical directory/UID1000/private
modes, actual mount and declared nonsecret config before starting the test;
the native child opens auth itself. Do not serialize credential values into
Nix strings/store, argv, environment receipts, manifest, driver logs or artifacts.
Do not use the test driver's base64/shell copying function for credentials.
The home is writable for native owned state; keep it private and separately
retained after failures, without exporting its diagnostic database/auth files.

Use a separate fresh VM definition/driver for real mode. Retain the UID/user
manager/cgroup/manifest/native/resource assertions and the blocked TCP39991
probe. Its explicit egress policy differs only as needed for real HTTPS and
the guest's declared DNS resolver; keep forbidden traffic counted and no
unsolicited inbound/host-service access. Bind actual nonsecret provider hostname,
TLS route and allowed destinations in the launch receipt; reject loopback/mock
endpoint configuration for naming. No TLS interception, response substitution
or rewriting to a synthetic provider. Any additional endpoint/credential-policy
requirement returns to lead before widening this recipe. The egress change does
not establish native tool isolation; the prompted contract still permits native
tool availability and makes no claim about their absence/effects.

Start one actual packaged portal user unit using the private registry/profile
setup above, the supplied naming home and existing fixed failure CLI helpers.
Observe its one exact native child, UID/PID/start/group/cgroup, catalog path and
`sessionFlags` origin before admission. Submit one public synthetic goal through
the real `/sessions` form/POST path with no custom name, no attachments, a fresh
request UUID and the installed team catalog. This reaches the actual production
`runPreparation -> namePreparation -> normalSessionName ->
RunPromptedEphemeralTurn`; never inject a `SessionNamer`, copy its prompt into a
test call, or issue a direct ordinary conversation turn as a substitute.

Require the same accepted request/receipt/attempt to acquire a schema-valid
generated base with `NamingOutcome=model` within30 seconds, measured from
admission with a monotonic deadline, and retain the sanitized production
`duration_ms/outcome/category` evidence. The existing worker owns its one30-second
budget, two slots, native willRetry handling, at most two proven-clean fresh
calls and backoff; the driver performs no second request, provider retry loop or
budget reset. Fixed CLI failure prevents starting any development session/team
after naming/reservation; it is not a naming failure and cannot count as full
creation acceptance. Prove no real session was initialized and no naming call
used the ordinary proxy. The resulting name need not match a hardcoded phrase;
it must satisfy the production schema, with no fallback/custom outcome.

### Teardown, launch gates and verification evidence

Both drivers must preserve the fixture's recorded-unit cleanup, worker-before-
child shutdown order, native process-group stop/join and cgroup-empty evidence.
Do not stop a user slice, host service or existing daemon. A test failure still
runs cleanup and records its separate result. If in-guest cleanup cannot prove
all owned processes stopped, retain failure and private state; the outer NixOS
driver must stop/join its owned QEMU process with finite bounds. VM termination
contains the fixture but does not turn a failed native cleanup assertion green.
Never reuse an interrupted guest/test-home result as a clean positive run.
Retain original logs, input manifests and partial receipts; retry requires
diagnosis and a new attempt identity. No session lifecycle or automatic cleanup
of retained evidence is included.

Implementation quick checks are the selected Nix environment's formatting/
syntax and bounded tagged compilation, existing naming/private-state/retry
unit checks, focused fixture-manifest/environment validation, and the three-role
browser selector syntax check. Add meaningful negative checks for wrong manifest
identity/missing private provider setup and for refusing a real selector without
its distinct opt-in/home; they must not launch native/provider during quicks.
Evaluate the fixed output graph and inspect VM UID/sudo/counter/closure and
managed-versus-real separation when lead releases evaluation. No actual VM test
or real provider call belongs in quick compilation or package build phases.

Commit all intended fixture/export/doc/selector changes, then send the exact
series/final diff and quick results to the retained reviewer. The new host-
fixture/credential boundary needs affected general, architecture, scope and
risk review;44's old report cannot cover it. This design record itself is
planning, not a claim of completed-deliverable review. Preserve no-migration
history and prior production compatibility conclusions where inputs are unchanged.

After review and lead release, owner1 binds the final source and final application
dependency derivation, performs the existing required final dependency proof
once, and refreshes coherent published runtime/consumer selections. The hash
remains Fx only if actual module/content proof agrees; no repeated discovery is
called for. Old44/alhm/xcl/source/vendor and client025 native receipts stay
historical. Reuse unaffected client protocol/state results only with actual
unchanged binary/schema/client/scenario inputs; new runtime source is not44.
No reason is introduced to repeat unaffected long native checks blindly.

Freeze an owned nonsecret selection expression that calls the new constructor
with the final package/provenance. Once its identities are accepted, the future
build selections are exactly `fixture`, `manifest`, `managed.driver` and
`realCanaryDriver` from that expression. Record actual JSON outputs/derivations,
retain their closures with ordinary owned roots, and preserve earlier roots.
Building a driver is preparation, not a passing test. Guest images/toolchain
dependencies must use the ordinary declared Nix/cache policy; an unexpected
local kernel/toolchain build stops for diagnosis under verification guidance.
No live helper installation/profile switch is needed.

The output-gated launch is the actual returned driver's
`bin/nixos-test-driver -o <fresh-owned-output-directory>`, first managed, then
separately real with its private-home input present. Use the fixed compiled
selectors above, and `^TestRealNamingRuntimeCanary$` only for the real driver;
cap the latter at5 minutes overall including bounded stop/join. A fresh
policy-selected watcher owns each long invocation; max1 utility remains in
force. Pre/post guards bind exact source, package, manifest, fixture executable,
native/catalog, driver scripts, tools and owned roots. Collect actual exits,
exact non-skipped test identities, sanitized result/timing and teardown proof.
No guessed store path, unbuilt package, missing credential, stale44 label or
successful driver build releases an acceptance launch.

The changes are test/export/documentation only: no persisted-format migration,
production credential relocation, application activation or rollback policy
change. Release still requires the managed checks and real positive result,
plus all previously required package/browser/creation/state/provider gates.
Missing real account/model access is an explicit remaining input dependency,
not permission to weaken either gate. Final source binding/build/publication
remain held until lead accepts this complete source boundary and implementation
is ready for its normal quick/commit/review sequence.
