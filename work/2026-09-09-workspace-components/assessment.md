# Workspace component split assessment

The three-component split makes sense. The recommended end state is a reusable
Codex web library, a session application that embeds it, and a workspace
repository containing development records and local policy. Extract the session
application first, then the Codex library. This removes the tooling/data mixture
early and gives the library an actual consumer while its interface settles.

Names below are provisional. This is an evaluation, not an accepted
implementation plan or a deployment instruction.

| Component | Owns | Consumed through |
| --- | --- | --- |
| `codex-web` | Browser conversation UI, Go App Server adapter, conversation HTTP handlers, retry receipts, protocol tests, standalone example | Go module and bundled browser assets; example Nix package |
| `dev-workspace` | `dev-session`, workspace registry, worktrees, lifecycle operations, portal shell, artifacts, repository/CI status, cluster providers, runtime supervision, packaging and host module | User application package, CLI, NixOS host module |
| `vpsfree-cz-workspace` | `work/`, `archive/`, `notes/`, curated evidence, workspace policy and a small declarative tools/configuration reference | Files read by the installed application |

The dependency direction is `vpsfree-cz-workspace -> dev-workspace -> codex-web`.
The Codex library must work without a vpsFree workspace checkout. The session
application must work against a second empty workspace with different paths and
hostnames. Its package source must not include session records.

Current evidence supports these boundaries:

- Workspace baseline: `3580e60bb035c2d0ba5be6f0d2489bbbf30ded3d`.
- Current configuration: `7481618dacab04bfd5b09bc730c373c2d2bf14d7`, verified
  against remote `master`. The canonical bare clone's local `master` is older;
  the assessment uses `origin/master` and that exact commit.
- [The flake](../../flake.nix) exports packages and one app, but no NixOS module.
  [The package](../../nix/workspace-portal.nix) takes `src = self`, combining
  application code with tracked workspace records. Tracking edits therefore
  change the package's source input.
- [The Codex client](../../portal/internal/codex/client.go) is 4,135 lines.
  It already handles much more than rendering: protocol events, questions,
  approval responses, settings, submission attempts, and queue reconciliation.
- [The HTTP server](../../portal/internal/web/server.go) is 2,597 lines and
  [browser script](../../portal/internal/web/static/app.js) is 2,419 lines.
  Both combine conversation operations with workspace/session operations.
- [The host helper](../../libexec/workspace-host) already registers multiple
  workspaces and installs the application into a user profile. It currently
  obtains Codex from `/run/current-system/sw/bin/codex`.
- Both cluster flakes still load `${workspace}/dev-clusters/lib`. Extracting
  the shell commands alone would leave cluster builds dependent on tooling
  files in the records repository.

The Codex library should include the backend integration as well as the UI.
OpenAI documents App Server as the interface for interactive clients with
conversation history, approvals, and streamed events. It supports a shared
terminal client and version-specific generated schemas. This fits the current
portal better than replacing the integration with batch SDK calls.
[OpenAI App Server documentation](https://learn.chatgpt.com/docs/app-server).

Keep the current Go implementation and extract browser code into an ES module
with scoped styles and an explicit mount/unmount interface. An application
provides a conversation identifier, API base URL, and optional actions. This
allows later framework wrappers without requiring a frontend rewrite now.
Package the matching browser assets with the Go HTTP handlers so an ordinary
deployment cannot accidentally combine different API versions.

The public Go surface should separate protocol access from HTTP integration.
The application supplies a resolver that maps its conversation identifier to
an authorized thread, working directory, socket, and allowed operations. The
server validates this mapping for every read, subscription, and mutation.
Absent authorization must deny access. The browser must not select an arbitrary
App Server socket or working directory, or gain unrestricted RPC forwarding.
Keep Markdown sanitization, origin checks, and approval validation in the
reusable handlers, with explicit configuration for the embedding application.

Generic message queues, unknown-outcome receipts, and question state belong
with the conversation adapter. Their storage location and scope should be
configurable and preserve existing retry identities. Session creation,
workspace archival, worktree deletion, and cluster release belong to
`dev-workspace`. The existing workspace lifecycle developer instruction should
be supplied by that application through a policy hook. A library should not
hard-code vpsFree policy, paths, model choices, or client branding.

For example, a rendered plan can expose an action callback. The workspace
application implements "create a session from this plan" and retains the
existing digest and retry checks. The generic component only exposes the plan
and its action. Thread forking has a similar split: App Server mechanics in
the adapter, workspace creation and policy in the session application.

Ship a minimal standalone example that connects to a configured local Codex
App Server and displays an allowed conversation. It should exercise the same
public API as the workspace portal, including sending, streaming, questions,
approvals, and reconnecting. That example is also the test that extraction
removed workspace assumptions.

The session application should initially retain its existing Go, Ruby, and
shell implementation. Repository extraction does not require consolidating
languages or redesigning the lifecycle state machine. Keep vpsAdmin and
vpsAdminOS as optional, shipped providers in this repository. Use the existing
helper/status JSON boundary and add only the configuration needed for provider
selection; a dynamically loaded plugin framework is unnecessary for two known
providers. Cluster package assets come from the installed tooling source,
while project worktrees, certificates, SSH identities, and cluster state remain
under the explicitly registered workspace.

Reusable scripts outside the portal also need an owner. The current `bin/kb-*`,
`lib/kb_*`, and reusable skills cannot remain executable tooling in a repository
whose purpose is session records. For the first split, package them as optional
vpsFree tooling alongside the session application. A later move of KB release
tools to the KB contracts repository can be considered separately. Keep project
policy and local notes in the workspace, and ensure agents can discover skills
from their installed package rather than assume `skills/` exists in this root.

The records checkout keeps its existing canonical path, `.git`, bare project
clones, and worktree layout. `repos/`, `worktrees/`, and `.dev-clusters/` remain
local working data rather than application source. A small flake may pin and
re-export the session tools for convenience, provided it delegates package
construction to the upstream tools flake and never passes its own `self` as
the tools' source. A tiny workspace configuration file can declare the name,
enabled providers, and project catalog. Host registration owns local absolute
paths and endpoints.

For aitherdev, export `nixosModules.host` from `dev-workspace`. The current
configuration already deploys the application through its user profile, but
still implements the TLS/password reconciler, renewal timer, socket groups,
nginx proxy, and related exposure inline. Move these into the module and expose
host facts as options. Optional cluster host configuration can manage a private
bridge/DHCP/NAT network or use explicitly supplied existing bridges. It must
coexist with aitherdev's other VM users.

The following illustrates the desired interface; these options do not exist
yet. `sessionTools` would be the flake selected through confctl's input mapping.

```nix
{
  imports = [ sessionTools.nixosModules.host ];

  services.dev-workspaces = {
    enable = true;
    user = "aither";
    domain = "workspace.aitherdev.int.vpsfree.cz";
    listenAddress = "172.16.106.40";
    allowedNetworks = [ "172.16.107.0/24" ];
    tls.mode = "local-ca";
    auth.mode = "basic";
    clusters.allowedBridges = [ "br0" "virbr0" ];
  };
}
```

The module owns stable host resources. It must not install or restart the
user application on every tools revision, or depend on application CLI flags
and model contracts. A configuration input pin for this host module is
independent of the active application profile. The system closure may include
small host helpers, but should not acquire the portal or Codex runtime through
that module. Routine UI and session changes continue through the user-profile
switch; system deployment is needed only for host setup changes.

Keep hardware, administrator accounts and keys, host addressing, WireGuard
policy, external DNS records, and other unrelated aitherdev services in
`vpsfree-cz-configuration`. Wildcard DNS still needs to point to the host, and
clients still need to trust the local CA. The module can support supplied TLS
certificates too. Preserve current password/CA storage and trust during the
cutover so extraction does not create new credentials.

`nixosConfigurations.example` or a VM example is useful for a dedicated
development host and automated testing. It should compose the same module.
For an existing aitherdev system, an importable module is the suitable public
interface; a complete configuration also makes choices about the rest of the
machine. NixOS modules support this composition through imports and options.
[NixOS module documentation](https://nixos.org/manual/nixos/stable/#sec-writing-modules).

The upstream requested as `numtide/nix-agents.nix` is available at
[`numtide/llm-agents.nix`](https://github.com/numtide/llm-agents.nix).
The first URL returned 404. Numtide updates packages daily and provides a binary
cache. Its documentation explicitly recommends retaining its pinned nixpkgs
for the tested, cached package combination.

Use `inputs.llm-agents.packages.${system}.codex` unchanged. Do not make its
nixpkgs follow the workspace's stable nixpkgs, use the shared-nixpkgs overlay,
or override the Codex derivation if cache reuse is the goal. Configure the
Numtide substituter and public key in the host module. Its Codex package is
source-built by upstream CI, so avoiding local compilation depends on the exact
output being available from the cache.
[Numtide installation and cache guidance](https://github.com/numtide/llm-agents.nix#installation),
[Codex derivation](https://github.com/numtide/llm-agents.nix/blob/main/packages/codex/package.nix).

Let the session application own the selected runtime. Its default Nix bundle
includes the tested Codex output, and both the browser adapter and terminal
clients use that selection. The `codex-web` example can have its own default
package, but the library itself must accept an externally managed connection.
Embedding it in the portal must not start a second competing App Server. Keep
the current per-workspace server topology and one host-owned selection policy
initially; per-workspace version selection would be additional scope.

A daily dependency-update job can propose a fresh Numtide pin, check cache
availability and protocol/behavior compatibility, then publish a tested
application bundle. A lockfile does not refresh itself merely because upstream
updates daily. The runtime adopts a new bundle when sessions permit a safe
transition; busy sessions keep their current process. Retain the preceding
application/Codex pair and its GC roots. The first repository cutover should
keep Codex at the current version, 0.153.4, which also matches the upstream
package inspected on 2026-09-09.

App Server compatibility remains a release requirement. OpenAI marks the
interface/transport experimental. Generated schemas verify the wire shape,
while behavioral tests must cover reconnects, ambiguous sends, approvals,
questions, queues, and simultaneous terminal/browser use. Passing those checks
does not prove that an older Codex can read all state written by a newer one;
verify persisted-state compatibility before promising downgrade support.
[OpenAI protocol documentation](https://learn.chatgpt.com/docs/app-server).

| Alternative | Benefit | Cost | Assessment |
| --- | --- | --- | --- |
| Tools repository plus records repository; Codex stays an internal package | Fastest removal of the tooling/data mixture | Codex UI is not independently consumable | Useful first stage |
| Three repositories; Codex Go library and assets embedded in the session app | Reusable integration with one portal deployment | Public API, releases, and dependency updates require maintenance | Recommended end state |
| Three repositories; Codex UI/backend runs as a separate service | Other backend languages can integrate over HTTP | Additional routing, authentication, state ownership, and version coordination | Consider when a concrete independent consumer needs it |

A fully NixOS-managed application would make installation more declarative,
but routine application updates would again go through a system deployment.
The host module plus independent user application better matches the stated
deployment preference.

The migration can be reviewed in these increments:

1. Export the host module with equivalent behavior and separate package source
   files from session records. This can reduce coupling before new repositories
   are created.
2. Extract tools into their own repository and package all runtime assets,
   including cluster runner libraries and reusable skills. Preserve history in
   the new repository using a disposable extraction clone; keep the existing
   workspace history intact.
3. Prove the installed package works with a minimal second workspace that has
   no tooling checkout. Switch the existing registered workspace to the new
   package while preserving paths, service/socket identities, and URLs.
4. Extract `codex-web`, port the portal to its public API, and run the standalone
   example tests against the same library release. Move the protocol contract
   tests with the adapter; keep workspace lifecycle tests in the session app.
5. Move Codex selection from the system package into the application bundle
   using the same initial version, then add tested dependency updates. Re-run
   package switch, busy-session, compensation, and rollback checks.
6. Remove executable tooling from the records repository only after its
   consumers use the installed package. Update instructions and tool paths,
   and preserve ongoing workspace feature work until explicitly migrated or
   merged.

The difficult migration state is already explicit in the implementation:
`portal.yml`, thread working directories, private authorities, submission
ledgers, lifecycle/creation journals, profile generation identity, and cluster
socket ownership. Preserve their formats and locations for the first cutover.
Run no package transition while an operation journal requires its current
helper. Do not rename the `VPSFREE_*` environment or XDG state paths merely to
match new repository names. Renaming can be a later versioned migration if it
has a practical benefit.

Existing registered `workspace` worktrees still belong to the records Git
repository. Moving tools into a new repository does not change their Git
identity or merge proofs. Keep them intact and reconcile concurrent tooling
branches deliberately. Fresh tools development should use its independent
canonical bare clone and initiative worktree.

No database, vpsAdmin API/client, daemon protocol, or deployed node change is
required by this split. Cluster tests still need to prove that packaged runners
build and operate with their supported project revisions and existing state.
For this assessment, validation was source inspection, upstream documentation,
and remote-ref verification. No code, configuration, or running service was
changed. The first implementation requires mandatory change review before long
integration tests. Repository names, public release/license policy, and the
preferred default TLS mode remain decisions for that implementation.
