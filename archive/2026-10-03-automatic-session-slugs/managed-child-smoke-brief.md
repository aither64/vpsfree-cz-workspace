# Prepared managed naming-child smoke

Status: source-backed implementation/verification brief, not an executable
fixture or a test result. Prepared by architect0 on 2026-10-04. Only this record
and the linked design supplement were changed. The selected static child is
present in the working source; the final assembled package is not yet frozen.
The older ca/42/2e/f5 package cannot establish these properties.

## Selected fixture boundary

Use a disposable NixOS VM with a real systemd **user** manager, the exact final
assembled workspace package, and private synthetic Codex homes. Reuse the
`pkgs.testers.runNixOSTest`/normal `developer` user approach in runtime
`nix/tests/host-module-idempotency.nix`; that existing test actually boots a VM,
but currently runs a fake router and has no portal/native-child fixture.
Its previous pass does not cover this change. A small session-owned VM wrapper
and a tagged runtime command-package fixture are the missing implementation.
No product flags, registration API, process manager or daemon-state framework
are needed.

A host `systemd-run --user` unit does not inherit the invoking harness's network
namespace. Do not reuse the native fixture's caller-side `unshare` command and
assume it confines a host user service. The VM is the selected finite way to
avoid that gap. After boot, its root fixture installs an inet output chain for
the disposable developer UID, before any native process starts: first count/drop
one reserved loopback TCP canary port, then allow other loopback traffic, then
count/drop all remaining IPv4/IPv6 output from that UID. Check that portal,
native children and ordinary fixture processes actually have that UID. This
keeps unrelated root VM boot services out of the assertion. The Nix VM driver
uses its test channel, not an outbound provider connection. Complete a bounded
owned `net.Dialer.DialContext` to the blocked loopback canary before taking the
fixed counter baseline; no shared HTTP transport or pending dial. Mock listeners
must use other ports. All provider endpoints are literal loopback. No real account,
host HOME, registration, workspace or credential is mounted into the VM.

Run the test driver, mock HTTP provider and ordinary native AppServer outside
the portal's disposable unit. The driver owns and joins them independently.
The portal unit alone owns its naming child. A failure must not make the
fixture kill a broad user slice or the ordinary server to obtain a clean result.

## Candidate guards and future entry points

The coordinator freezes a manifest before execution containing:

- Canonical final assembled package store path, its derivation/source provenance
  and exact provider/runtime/extension/workspace heads. Preserve consumed 4ef/399
  ancestry. Do not discover a candidate from a mutable installed profile or an
  older `/tmp/*final-package-path` file.
- SHA-256 of `bin/workspace-portal`, packaged user-service template,
  `share/dev-workspace/package.json`, installed team catalog/resources,
  `share/workspace-portal/codex/ephemeral_policy.json`, runtime-contract JSON,
  and the reviewed fixture binary/source. Check these again inside the VM.
- Resolved native executable
  `libexec/codex/libexec/codex/bin/codex`, its frozen ELF digest and version
  `codex-cli 0.160.0`; unchanged selected native source identity. Validate the
  complete assembly using the existing package checks, rather than inferring
  source equivalence from version alone.
- Full `share/workspace-portal/codex-models.json`, 472512 bytes, SHA-256
  `fd219bd9f061278275f528939f82f54d2eb97df4b25c23b022adbe48813d920b`.
  Resolve links and require the same read-only original resource consumed by
  the helper. Never write or filter this catalog.

Proposed owning additions, to be implemented and independently reviewed first:

1. Runtime `portal/cmd/workspace-portal/naming_runtime_integration_test.go`,
   build tag `naming_runtime_integration`, with
   `TestManagedNamingRuntimeIntegration` and
   `TestNativeNamingRuntimeHTTPFailure`. These names are proposed, not existing
   runnable selectors. Keep shared fixture helpers local to this file/package.
2. Session `managed-child-smoke.nix`, taking explicit `runtimeSource`,
   `packageRoot`, `fixtureBinary`, and `manifestFile` inputs. It imports the
   reviewed runtime's locked Nixpkgs, boots the normal-user VM, includes the
   candidate closure and reviewed test binary, starts its user manager, installs
   the loopback-only policy, and runs those two selectors as `developer`.
   It must not run workspace-host registration/activation or profile switches.

Prepared commands once those entries exist (all placeholders are frozen inputs):

```sh
# Owning runtime worktree, compile only; no native test execution before review.
nix develop .#packages.x86_64-linux.dev-workspace -c sh -c 'cd portal && go test -mod=readonly -tags=naming_runtime_integration -c -o /tmp/automatic-session-slugs-managed-child.test ./cmd/workspace-portal'

# Existing focused synthetic checks; parent selects/runs after implementation.
nix develop .#packages.x86_64-linux.dev-workspace -c env -u PORTAL_BROWSER_TEST sh -c 'cd portal && go test -mod=readonly -race ./cmd/workspace-portal -run "^TestNamingRuntime" -count=1'

# From coordination workspace; proposed VM wrapper, after committed quick+review.
nix-build work/2026-10-03-automatic-session-slugs/managed-child-smoke.nix \
  --argstr runtimeSource /nix/store/REVIEWED-RUNTIME-SOURCE \
  --argstr packageRoot /nix/store/FINAL-ASSEMBLED-PACKAGE \
  --argstr fixtureBinary /nix/store/REVIEWED-FIXTURE/managed-child.test \
  --argstr manifestFile /nix/store/FROZEN-SMOKE-MANIFEST.json
```

The wrapper must put the actual candidate closure in the VM, not rebuild an
unrelated generic runtime package as its stand-in. The fixture binary can be
built from the reviewed runtime Go package and imported as a store input by the
coordinator. Require that source/package provenance agree before the owning
HTTP-error case is accepted. VM/build/native execution is a long check assigned
to a fresh Luna/low watcher after review. Stop unexpected local kernel builds
under the workspace verification procedure. Nothing above has been executed.

## Private portal setup and exact launch

For each case, the driver allocates a new mode-0700 root `R` owned by the VM
user. Create `R/workspace/{work,archive,worktrees}`, `R/authority`, `R/state`,
`R/runtime`, `R/home`, private XDG directories, `R/naming-home` and
`R/ordinary-home`. User state must be outside `R/workspace`, as enforced by
`modelSessionName`. Create `R/transition.lock` mode0600 and a private symlink
`R/profile` to the canonical candidate package. Leave its identity unchanged.

Populate each Codex home with synthetic-only `auth.json`:

```json
{"auth_mode":"apikey","OPENAI_API_KEY":"synthetic-fixture-only"}
```

Use a small private `config.toml` with `model_provider = "openai"`,
`model = "gpt-5.5"`, `model_reasoning_effort = "low"`, and
`openai_base_url = "http://127.0.0.1:<owned-port>/v1"`. Give the two homes
distinct mock listener ports so their inference observations cannot be confused.
No custom provider, catalog rewrite, live token or serving-config copy. Leave
the full restriction matrix to the native isolation fixture; this fixture
checks the actual naming request's model/effort, empty Direct tools, structured
output, `store:false` and `stream:true`.

Start the ordinary pinned native AppServer against its synthetic home and an
empty cwd. Its ordinary launch has no static-catalog override. Put a private
UDS WebSocket forwarding proxy at `R/runtime/ordinary.sock`, forwarding to the
ordinary native socket. Reuse the bounded transport pattern from codex-web
`codex/ephemeral_integration_test.go:proxy`, recording only client identity and
method/owned synthetic IDs. This is needed to prove **no attempted routing** of
the naming client to the ordinary socket, even if a wrong route would fail
before HTTP inference. Do not replace the ordinary server with a fake.

Write an executable private `R/fail-dev-session` whose only behavior is fixed
exit status 73. It must never invoke the real CLI or log goal/arguments. Supply
`--gh` and `--tmux` as private failing helpers too. This intentionally bounds the
test at preparation/naming and prevents creation of development sessions. Do
not claim successful downstream initialization; a frozen team's later live
availability validation or this stub may intentionally fail after naming.

Launch the **packaged** portal with the following argv under the disposable
unit (the driver passes an argument vector, not interpolated shell text):

```text
<package>/bin/workspace-portal serve
  --unix-socket R/runtime/portal.sock
  --workspace R/workspace
  --base-url https://managed-smoke.example.test
  --dev-session R/fail-dev-session
  --authority-dir R/authority
  --user-state-root R/state
  --package-root <canonical-package>
  --workspace-name naming-smoke
  --registration-marker R/runtime/registration.json
  --host-profile R/profile
  --transition-lock R/transition.lock
  --codex-socket R/runtime/ordinary.sock
  --codex-version 0.160.0
  --gh R/fail-helper --tmux R/fail-helper
```

Use an explicit clean environment (`env -i` or equivalent argv) with private
HOME/XDG paths, bounded PATH of fixture tools, `CODEX_HOME=R/ordinary-home` and
`DEV_WORKSPACE_CODEX_HOME=R/naming-home`. No inherited session variables, tokens,
proxies or host auth. The ordinary native server has its own explicit clean
environment and the pinned remote-control-disabled marker. Production itself
sets the marker for the naming child. Start the user manager through the VM's
normal `loginctl enable-linger developer` and `user@<uid>.service`; the fixture
driver's systemd calls use `/run/user/<uid>` and its user bus. The portal's own
XDG paths remain private.

Create a unique transient user unit using `systemd-run --user` with
`Type=simple`, `KillMode=mixed`, `TimeoutStopSec=150s`, `SendSIGKILL=yes`,
`Restart=no`, `UMask=0077`, and the argv above. The first three properties match
`nix/systemd/workspace-portal@.service`. `Restart=no` is a deliberate fixture
override so a forced main-process failure cannot replace the process under
observation. This proves cleanup of one lifetime, not production restart policy.
Do not install or start the workspace template: it invokes registered host
state. Do not add tmux/Codex workspace dependencies to the disposable unit.

`web.New` validates canonical package/marker/socket paths and real installed
team resources (`server.go:319-386`), but does not read a registration marker
on this path. **Leave `R/runtime/registration.json` absent.** Its required name
and adjacency are satisfied; no invented registration payload is needed. The
private profile symlink is the real supported generation identity
(`readHostProfileIdentity`), not a fabricated receipt. The transition file is
real and existing. If the frozen final source changes this contract, stop and
revise the fixture rather than bypassing validation.

Use GET `/healthz`, then GET `/` over the private HTTP UDS with Host
`managed-smoke.example.test`. Parse the returned form for exact creation_date,
catalogDigest and selected team. POST `/sessions` with those values, a fresh
UUIDv4 `clientRequestId`, synthetic `goal`, and empty `name`, using
`Content-Type: application/x-www-form-urlencoded`, `Accept: application/json`
and `Origin: https://managed-smoke.example.test`. Omit model/effort and upload
fields. Require 202 and matching request/receipt identity. Poll the returned
status URL or `/api/session-creations/<id>`; never invent receipt/preparation
records. Read only generated private preparation JSON for `base` and
`namingOutcome`: `R/state/portal/<workspace-basename>-<first8-sha256-bytes-hex>/`
`session-preparations/<id>.json` (or terminal mappings), per
`internal/userstate` and `preparation_store.go`. No state mutation by the test.

## Native transport and finite cases

The mock uses the existing native fixture's exact built-in Responses transport:
426 only for a real WebSocket Upgrade, plain GET404, actual POST `/v1/responses`,
then native SSE `response.created`, assistant `response.output_item.done`, and
`response.completed` events. Return a valid hyphenated name such as
`{"name":"verify-managed-child"}`; ordinary controls return a different fixed
answer. This proves the supported HTTP fallback lane only. It does not replace
the unchanged-transport real-provider positive canary.

Before admission in successful cases, find the sole `naming-*` directory only
under this fixture's private runtime parent. Require the native child PID/exe/
argv and cgroup identity; do not infer readiness from a socket pathname. A
bounded private initialize/config-read probe must show the original catalog
path and `origins["model_catalog_json"].name.type == "sessionFlags"`; close
the probe before naming. Do not start an extra utility thread as readiness.

| Case | Trigger and required observations |
| --- | --- |
| One child, two slots | Admit three fresh requests with distinct goals. Barrier the first two decoded native naming POSTs before completing either. Require one native app-server PID for the whole portal lifetime and no more than two simultaneous utility POSTs. Release responses promptly so all three finish naming within their unchanged individual ten-second budgets; the third starts only after a slot frees. Inspect model outcome and exact distinct generated bases. A scheduler-delayed third request alone is not positive semaphore evidence; combine this observation with the existing owning two-slot unit test. |
| Startup unavailable | A fresh portal unit gets a nonexistent absolute `DEV_WORKSPACE_CODEX_HOME`; keep its ordinary home/socket healthy. Require the fixed unavailable category, no native naming child/inference, generated `namingOutcome=unavailable`, and exact fallback for goal `Fallback smoke request` → `fallback-smoke-request`. Ordinary proxy must observe no naming client, thread/start or turn/start attributable to this request. Ordinary control turn succeeds. |
| Native loss | After ready, kill only the captured naming child within this fixture's unit and await its exit. Admit one request: deterministic fallback, no restart/adoption and no ordinary routing. Do not accept model outcome. The portal and ordinary server remain usable. |
| Graceful main signal | With two actual provider POSTs held, send TERM to the portal MainPID only using `systemctl --user kill --kill-whom=main --signal=TERM <unit>`. Require stopped admissions, observed provider cancellation/connection closure, no committed cancellation fallback/new slug, and no live naming descendants after portal exit. Preparation may be paused/failed by the existing close behavior; do not demand a new state. Ordinary control turn succeeds afterward. |
| Forced parent death | With an actual held native request and recorded child identity, send KILL to MainPID only. Require systemd's remaining cgroup cleanup within the existing 150-second stop allowance (plus bounded observation overhead), no old child/group remains, and ordinary continuity. Do not kill the child/group yourself before taking this result. |

Record systemd MainPID/ControlGroup and PID start times before faults. Verify
the real native executable's digest through `/proc/<pid>/exe`; count app-server
children rather than the transient version probe. Require the unit cgroup to
be empty/removed and recorded PID identities gone. Subscriber removal, an
unlinked socket, parent exit, or an empty portal scratch directory alone is
insufficient. These checks do not require deletion of upstream stale socket
artifacts after forced death.

## HTTP failure: smallest missing owning extension

There is no supported external packaged CLI operation to close the live HTTP
listener. Removing its Unix pathname does not close the bound listener; a
non-socket planted before startup exercises listener construction failure only.
Do not add a product test flag, signal behavior, or ptrace fault mechanism.

Extend the existing `TestNamingRuntimeHTTPExitKeepsChildForWorkerCleanup` shape
with tagged `TestNativeNamingRuntimeHTTPFailure`: use real
`startNamingRuntime(candidate, ...)`, a real `portalweb.New` configured exactly
as above, the ordinary client, the normal naming adapter, and an owned Unix
listener passed to current `servePortalHTTP`. After a genuine native naming
POST reaches the mock barrier, close that listener from the test owner. Require
the non-ErrServerClosed serve error, application.Close worker completion while
the native child remains alive, then the same deferred child.Close/join order
as production. Observe native cancellation before child teardown, no live owned
processes afterward, and ordinary continuity. A narrow event observation in
the fixture may check liveness at close completion; no injected SessionNamer
or synthetic child substitutes for this case.

This is actual native HTTP-failure integration through the production function,
compiled from reviewed source. It is explicitly **not** an externally forced
HTTP failure in the packaged executable. The packaged signal/forced-parent
cases plus this owning case are the selected finite coverage; requiring that
last failure inside an unmodified packaged CLI would need a different fault
injection boundary. Source equivalence is checked through the frozen manifest.

## Ownership, result and remaining gates

On any fixture failure, record the failure and bounded fixed diagnostics first.
Then stop only recorded fixture units, wait for their cgroups, close/join the
ordinary server/mock/proxy, and remove only the fixture's own disposable root
after process ownership is accounted for. The VM runner is the final boundary
if its driver crashes. No delayed cleanup job and no lifecycle command for this
development session. A forced-parent cleanup failure stays a failure even if
the fixture's emergency stop later removes the child.

Persist only manifest hashes, case results, native/method counts, fixed error
categories and cleanup identities. Do not dump provider bodies, auth/config,
prompts, native logs or database contents. The fixed denied counter must remain
unchanged after the completed negative control; unexplained egress is failure.
The managed smoke does not alter or waive the native fixture's strict SQLite
persistence assertions. Logging choice, full isolation proof and the actual
model canary remain separate release gates; a green process-lifetime result
cannot activate model naming while those are unresolved.

This verification addition changes no host migration/schema/receipt contract.
It does not require repeating Chromium, old-reader or unrelated migration
checks unless their owning behavior changes. Final package/resource hashes and
affected-lane review must include the new fixture and current child source.

## Coordinator correction after source review (2026-10-04)

The fixture creates a private per-case `R/runtime/ordinary.sock` symlink to its
observed harness proxy and uses that alias in both the packaged CLI and owning
HTTP client/config. The absent `R/runtime/registration.json` has the same
canonical lexical parent, as required by current web.New. Ordinary native/proxy
ownership and routing observations remain outside the portal unit. No marker
is fabricated and production validation is unchanged. Formatting and tag
compilation pass; actual native/VM execution remains pending.
