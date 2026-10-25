# Package 2: Go documentation examples

Status: owning source committed as `062fad3` with declared hooks passing;
bounded acceptance-environment fix awaits consolidation, final independent review
and longer acceptance. No integration, publication or deployment.
Implementer2 verified session identity/environment and roster workspace_write.
Application design follows `api-doc-contract.md`; no Git/index/hooks mutated by
implementer2. Lead completed the prose pass on docs and user-visible strings.

## Owned files

- `clients/go/lib/haveapi/go_client/documentation.rb`: pure generator-owned
  adapter; full saved SDK mapping, visibility and compatibility checks, literals,
  complete Go programs and explicit unsupported-result limits.
- `clients/go/lib/haveapi/go_client/generator.rb`: additive offline constructor.
- `clients/go/spec/support/documentation_fixture.rb`: saved schema fixture source.
- `clients/go/spec/unit/documentation_spec.rb`: pure capability and safety specs.
- `clients/go/spec/documentation_acceptance.rb`: separate longer acceptance runner.
- `clients/go/docs/documentation.md` and `clients/go/README.md`: profile/mapping/
  capability documentation and entrypoint.
- `servers/ruby/lib/haveapi/client_examples/go_client.rb`: thin profile-gated bridge.
- `servers/ruby/spec/client_examples/go_spec.rb`: standalone-server bridge specs
  using an adapter double; no optional generator dependency.

## Public seam and compatibility

`Generator.from_description(description, dst, opts)` is additive. It configures
ordinary module/package options and constructs `ApiVersion` from already-loaded
schema data. It performs no discovery or writes. Existing
`Generator.new(url, dst, opts)` still constructs the communicator, authenticates
with supplied Basic credentials, describes the selected API version and uses
the same generation options. Both have focused regression checks.

The serving adapter always uses `ApiVersion.new(description)`, never either
Generator constructor. It neither reads files nor invokes generation, formatters,
compilers or network operations. Profiles remain optional and startup loading/
exact generator-version checks belong to implementer0's shared loader.

Saved route paths include the server's mount root and `/vVERSION` segment.
Generated Go requests concatenate `Client.Url` and the saved path, so example
`client.New` receives the API origin. Using the context's mounted base would
repeat its root. Regression checks verify origin initialization, ordered nested
path arguments and a stale changed-mount limitation. No Context ABI changed.

Object/hash inputs and object/list outputs preserve null/omission/false/zero.
Every allocated input selects zero fields before supplied setters. Empty requests
allocate input without creating an unused Go variable. General Custom and list
input remain unsupported. Scalar null output gets a limitation because the
existing scalar output type collapses null into zero. Resource output uses
visible associated show schemas, partial field access and nil guards. Lists
access common documented fields, including common nested associated fields.
API-failure and transport-error branches remain separate. Basic/existing token/
existing OAuth2 examples use environment placeholders. Operation status is shown
only with compatible visible metadata, route and fixed generated state members.
No schema/protocol/persistent-state migrations or downstream changes.

## Quick evidence

All commands ran from the repository root in the declared root Nix environment
with prepared bundles and `HAVEAPI_RELEASE_TOOLS_ONLY=1` (no dependency installs).

- Go component bundle: `BUNDLE_GEMFILE="$PWD/clients/go/Gemfile" bundle exec rspec
  -I clients/go/lib clients/go/spec/unit/documentation_spec.rb`: **26 examples,
  zero failures**, about 0.12 seconds test execution.
- Server component bundle: `BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile" bundle exec
  rspec -I servers/ruby/lib servers/ruby/spec/client_examples/go_spec.rb`:
  **4 examples, zero failures**; no Go generator loaded.
- Server bundle RuboCop on all seven owned Ruby files: **7 files, no offenses**.
- `ruby -c clients/go/spec/documentation_acceptance.rb`: Syntax OK.
- Owned tracked diff whitespace check: clean.

Earlier combined command accidentally scoped BUNDLE_GEMFILE only to the first
command, so a following RSpec invocation selected the root bundle and could not
load require_all. Separate per-component invocations fixed the command; no source
or dependency workaround was needed. Project instructions show separated commands.

## Longer acceptance prepared, not executed

Run after final committed-deliverable independent review using a fresh policy
watcher, with no concurrent dependency-home installation:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c \
  'BUNDLE_GEMFILE="$PWD/clients/go/spec/documentation.Gemfile" bundle exec ruby \
    clients/go/spec/documentation_acceptance.rb'
```

The committed harness writes a saved JSON fixture, generates the real SDK through
`from_description`, loads the corresponding configured profile and extracts real
server-renderer programs. Sixteen programs cover init, Basic/token/OAuth setup,
complete auth+action composition, nested mounted paths, null/zero/false/omitted/
empty input, hostile source literals, list/associated output, API failures,
query encoding and action-state status. Go download/toolchain acquisition is
disabled. A disposable localhost server records actual requests and checks
request values and outputs. Auth-call composition joins exact rendered import/
function sections, deduplicating identical initialization, without rewriting
calls or field names. Generated SDK files are never hand-edited.

Metadata retains the existing sample wire shape: advertised setter guidance is
commented and schema-mapped; ordinary examples do not invent metadata payloads.
The harness compiles generated metadata APIs; no ordinary sample is expanded
with a new metadata DSL. The full server's HTML/package checks remain shared
implementer0/lead work. No longer Go execution evidence is claimed yet.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

## Acceptance environment correction

Read-only probing confirmed that the old server-bundle command loaded the Go
VERSION constant through the harness's injected checkout load path while
`Gem.loaded_specs['haveapi-go-client']` remained absent. The Go-only component
bundle activates the generator specification but excludes WEBrick. This was a
harness-environment gap; production profile validation was not changed.

The harness now uses the test-only `clients/go/spec/documentation.Gemfile`, owned
and prepared by implementer0, to activate the server, Go generator, Ruby client
and WEBrick together. It no longer changes the Ruby load path. Its
`--check-environment` mode checks actual activated gem specifications, verifies
Go spec/version equality and runs the real profile registration/mount using a
disposable local JSON fixture. This mode creates no HTTP listener, generated
source or compiler process. The old server-only bundle is explicitly rejected
by the preflight (known-quick check passed). Harness syntax and RuboCop pass.
The updated Verification section received the lead's final prose pass.

Positive dedicated-bundle preflight passed with exit0 after implementer0 wrote
the manifest. It activated haveapi and haveapi-go-client 0.30.0, and the real
profile loader accepted the fixture. Bundler's quick execution created a local
documentation.Gemfile.lock from installed dependencies; implementer0 owns its
ignore policy and it is not a new permanent lock stream. Full Go execution
remains held for final committed-deliverable review.

## Final review I3: required metadata limitation

Reviewed `api-doc-final-review.md` I3. Lead explicitly granted narrow remediation
and directed saved OR authorized-live required global/object input metadata to
produce a generic limitation for every expected sample outcome. The fixed example
DSL cannot provide metadata, so no value/key/channel was invented. Source reads
only the existing required flags during compatibility checking; optional metadata
comment guidance and metadata-free examples remain executable.

Changed application paths: `clients/go/lib/haveapi/go_client/documentation.rb`,
`clients/go/spec/unit/documentation_spec.rb`, and
`clients/go/docs/documentation.md`. The new user-visible reason is the existing
Rust wording: "This action requires metadata that is absent from the sample."
A short project-doc sentence records this supported boundary.

Focused real-ApiVersion checks: **36 examples, zero failures** (ten added cases).
They cover both global/object metadata roles, both expected statuses, hidden saved
requirements, authorized-live schema drift, optional advertised guidance and no
metadata controls. RuboCop checks the two changed Ruby files. No serving I/O,
compiler, generator/runtime behavior, long run or Git/index operation was added.
Lead owns final prose acceptance; implementer0 owns hooked fixup/fold into the
Go source commit and resulting exact-head review evidence.
