# vpsAdmin Go and Rust documentation configuration

Investigation/design only, 2026-10-23. No application edits, dependency setup,
generation, tests, network requests or deployment were performed. Dependency
refresh 4dc0 and the held HaveAPI 0.30.1 patch 8270b remain independent.

## What the API needs

vpsAdmin already has the right hook: call
`api.documentation_clients('7.0', ...)` inside its existing
`VpsAdmin::API.configure` block in `api/config/api.rb`. That block runs before
`api.mount('/')`. No new configuration framework or resource edits are needed.

| Requirement | Actual state |
| --- | --- |
| HaveAPI support | Inspected vpsAdmin pins `haveapi ~> 0.29.9`, packaged as 0.29.12. The profile API requires 0.30. An API-bundle upgrade is a prerequisite, not authorized implementation here. |
| Go SDK | Real import is `github.com/vpsfreecz/vpsadmin-go-client/client`, alias `client`. The inspected SDK has no retained generation description/pin or local version tags. Exact saved input and a resolvable module version remain unproven. |
| Rust SDK | Real crate is `vpsadmin-client` 0.1.0, source import `vpsadmin_client`. Its saved 7.0 snapshot and TOML are available, but the crate is unpublished. Current HaveAPI always prints a crates.io version dependency; there is no Git/path source override. |

Do not enable a public profile with invented inputs or a misleading install
line. Omit a language until its prerequisites are met. This investigation
does not propose publication or silently add SDK regeneration/HaveAPI changes.

## Concrete configuration

The following shows the existing API exactly, with the unresolved Go values
clearly marked. The data directory is a proposed packaged location, not an
existing directory. Add these statements to the installation's existing
configure block: a second `VpsAdmin::API.configure` call replaces the first.

```ruby
# api/config/api.rb
# Requires an approved HaveAPI 0.30 API bundle and verified local SDK inputs.
VpsAdmin::API.configure do |api|
  sdk_root = File.join(VpsAdmin::API.root, 'doc', 'client-sdks')

  api.documentation_clients('7.0',
    go: {
      import_path: 'github.com/vpsfreecz/vpsadmin-go-client/client',
      module_version: verified_go_module_version, # unresolved, not a real variable
      description_path: verified_go_description_path, # unresolved absolute file
      generator_version: '0.30.0'
    },
    rust: {
      snapshot_path: File.join(sdk_root, 'rust', 'api-7.0.json'),
      generator_config_path: File.join(sdk_root, 'rust', 'generator.toml'),
      generator_version: '0.30.0'
    }
  )
end
```

This illustrates registration, not a ready-to-run current configuration.
Delete the `go:` or `rust:` entry entirely while that language is unconfigured.
There is no setup/unavailable panel for a missing profile: its overview entry
and all initialization/authentication/action tabs are hidden.

The optional runtime Ruby dependencies are `haveapi-go-client` and
`haveapi-rust-client`. They contain the naming/render adapters; this does not
install a Go module or Rust crate on the server. Their installed VERSION must
exactly equal the respective `generator_version`. Both inspected generators
report 0.30.0. Their transitive `haveapi-client` dependency is also0.30.x.

A concrete published-version option for a later evaluation is
`haveapi ~> 0.30.0`, `haveapi-go-client = 0.30.0` and
`haveapi-rust-client = 0.30.0`. On vpsAdmin's Ruby 3.4, that old Rust gem also
needs an explicitly packaged Fiddle dependency: it requires `fiddle/import`
but published 0.30.0 omitted the gem dependency. Reviewed 090a declares
`fiddle ~> 1.1, >= 1.1.8`; prefer a released fixed combination when available.
HaveAPI 0.30.1 is held, so it is not a released pin to use today. An exact
reviewed Git source is possible for isolated development but requires explicit
bundle/Nix packaging work and is not a production-pin recommendation.

## Which settings belong to the SDK

**Go generation** produces the package/module using its generator options.
The existing SDK declares module `github.com/vpsfreecz/vpsadmin-go-client`,
Go 1.16 and package directory `client/`. Its README documents the historical
command `haveapi-go-client https://api.vpsfree.cz ./client`; that does not
retain the exact old schema or generator revision.

**Go documentation** supplies the real import, a module version, and the saved
description object used by the SDK. That JSON must contain resources,
authentication and meta; it is neither an OPTIONS response envelope nor the
Rust snapshot wrapper. The adapter reuses the generator's canonical names and
types. A valid Go pseudo-version is allowed; raw SHAs are not accepted.
No authoritative module resolution was performed, so no version is supplied
above. Do not assume the Rust snapshot matches the older generated Go SDK.

**Rust generation** uses the retained snapshot and this exact
`generator.toml` from the SDK:

```toml
crate_name = "vpsadmin-client"
crate_version = "0.1.0"
license = "MIT"
edition = "2024"
rust_version = "1.95"
rustfmt_version = "rustfmt 1.9.0"
```

**Rust documentation** reads that same TOML with `Tomlrb.load_file` and the
snapshot with API version 7.0. The adapter constructs the generator's validated
in-memory model. It does not invoke generation, Rustfmt or Cargo. Package name
and version come from the TOML; hyphens become underscores in the Rust import.
One profile enables both `Rust (async)` and `Rust (blocking)`.

The truthful consumer dependency for the current unpublished SDK is:

```toml
[dependencies]
vpsadmin-client = { git = "https://github.com/vpsfreecz/vpsadmin-rust-client", rev = "ff876abe17e3301da62c1b6afbda055ec89db9d2" }
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
# Blocking consumers add features = ["blocking"] to vpsadmin-client.
# Tokio can be omitted by an application using only the blocking API.
```

This is consumer guidance, not an accepted profile override. The existing
renderer instead emits `vpsadmin-client = { version = "0.1.0" }` and adds the
blocking feature where appropriate, Tokio for async, and serde_json. No
`git`, `rev`, `path`, alias or custom dependency-text profile keys exist.
The SDK README's version-only installation example is not publication evidence.
Consequently the Rust profile can be registered with these files for inspection,
but its public installation hint is not currently usable as printed. Resolving
that limitation would need a separate decision/scope; publication is not assumed.

## Exposure, compatibility and failures

Profiles are registered before mount, are per API version, and have exact
required key sets of nonempty strings. Files must be trusted absolute local
files. Bad/missing files, missing adapter gems, version mismatch, unknown keys,
duplicate profiles or invalid schemas/config fail startup. Mount also rejects
unknown selected API versions and Rust snapshot version mismatches. Go has no
equivalent snapshot-version field; saved routes and acceptance must establish
its API-version match. The generator version check is not a Git/digest check:
preserve input/source provenance independently.

Saved SDK metadata remains private. Rendering is bounded by the current user's
authorized description and sample. Stale routes/types, missing SDK actions or
unsupported layouts show a limitation. Go handles object/hash input and
object/list output; Custom fields/list input and scalar-null output fidelity
have explicit limits. Rust follows its nullable/Custom/list generated contract
and query restrictions. Existing-token/Basic/OAuth2 examples do not invent
automatic Rust login, challenge handling or operation waiting.

JS/TS callback+async, Python sync+async and Ruby/PHP/CLI/curl/HTTP need no such
profiles. Upgrading HaveAPI brings the newer dynamic variants and removes the
obsolete File system format as well. The Rust snapshot is public-only:
152 resources, 524 actions; plugin completeness is unknown.

The existing Nix `configDirectory` option supplies `api/config/api.rb` at
runtime. `packages/api/common.nix` replaces the package's config directory
with a runtime link; adding a source-tree config alone does not configure a
deployed service. Trusted SDK files can be packaged under the proposed
`api/doc/client-sdks/` path or supplied from immutable site-owned SDK sources.
No site configuration/deployed revision was inspected.

## Representative source-derived calls

These condensed examples use actual SDK names, not captured/rendered HTML.
They were not run. Both call vpsAdmin's existing public Cluster/PublicStats
example; use the base URL without `/v7.0/` because the SDK owns the route.

```go
package main

import (
    "fmt"
    client "github.com/vpsfreecz/vpsadmin-go-client/client"
)

func main() {
    api := client.New("https://api.vpsfree.cz")
    response, err := api.Cluster.PublicStats.Prepare().Call()
    if err != nil { panic(err) }
    if !response.Status { panic(response.Message) }
    fmt.Println(response.Output.VpsCount)
}
```

```rust
use vpsadmin_client::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api = Client::builder("https://api.vpsfree.cz").build()?;
    let response = api.cluster().public_stats().send().await?;
    println!("{:?}", response.output.vps_count);
    Ok(())
}
```

Blocking uses `vpsadmin_client::blocking::Client`, a normal `fn main` and
`.send()?`; construct/use/drop it outside async runtime threads.

## Optional implementation boundaries and gates

Only if later assigned:

1. Owner0 establishes a fresh vpsAdmin base/worktree and owns Git. One available
   implementer owns the cohesive dependency/config/docs/tests package.
2. Author `api/Gemfile`; use `rake vpsadmin:gems:api` to generate
   `packages/api/{Gemfile,Gemfile.lock,gemset.nix}`. That task re-resolves the
   API lock, so review all drift. Other components' separate bundles need not
   move just to enable HTML examples. Do not hand-edit generated gem metadata.
3. Add a non-loaded configuration example and a developer/operator page linked
   from `docs/README.md`; no edit to `api/lib/vpsadmin/api.rb` is required.
   Package immutable SDK files with provenance only once their prerequisites
   are established. Go input recovery/regeneration and Rust dependency-source
   support/publication are separate possible prerequisites, not implicit work.
   Site activation requires the actual deployment owner's configuration scope.
4. Add focused `api/spec/lib/documentation_clients_spec.rb` coverage and
   packaged services-up documentation assertions. `spec/lib` belongs to the
   platform-config topic; preserve full/core exact-once coverage.

Quick checks: Ruby syntax/style; resolved gem versions/input digests; actual
configure-before-mount wiring; valid/invalid profile startup; no-profile
absence in overview and every panel; exact SDK names/variants; authorized
field filtering; public and stale/missing-SDK actions; no private paths/schema
in HTML. Commit all intended work and pass quick checks before independent
full-range final review.

Longer gates after review: API full/core suites in the declared Ruby 3.4 shell,
packaged `services-up` (required after HaveAPI updates), and actual rendered
Go/Rust examples compiled against the exact SDKs, including async/blocking and
truthful dependency resolution. Use disposable local API fixtures for request,
auth, nested path/mount and permission checks; no production calls or schema
refresh. Check declared Rust 1.95 compatibility where relevant. Normal watcher
policy applies; no checks were launched for this investigation.

A later approved deployment installs the bundle/data before enabling profiles.
Mixed workers may temporarily show different docs; no DB/protocol/state
migration or coordinated node rollout is expected. Validate startup before
rollout. Removing a profile hides that language; reverting to HaveAPI 0.29 also
requires removing the new call. Preserve the previous bundle/config/data as a
rollback unit.

## Source evidence

Canonical local objects were used; cached refs do not establish fresh remote
or deployed heads. vpsAdmin local master b4ef8535 is older and was not used.
HaveAPI 090a profile/renderer/adapter files compare unchanged to published b64 and
dependency-refresh 4dc0f7e1. The short name 4dc0 is ambiguous locally; comparisons
used its full hash.

- [vpsAdmin Gemfile](https://github.com/vpsfreecz/vpsadmin/blob/26518b27959eb8a63f3fc0b481720a54aa14e41c/api/Gemfile#L18),
  [packaged lock](https://github.com/vpsfreecz/vpsadmin/blob/26518b27959eb8a63f3fc0b481720a54aa14e41c/packages/api/Gemfile.lock#L63),
  [configuration load](https://github.com/vpsfreecz/vpsadmin/blob/26518b27959eb8a63f3fc0b481720a54aa14e41c/api/lib/vpsadmin.rb#L45),
  [server startup/hook](https://github.com/vpsfreecz/vpsadmin/blob/26518b27959eb8a63f3fc0b481720a54aa14e41c/api/lib/vpsadmin/api.rb),
  [Nix config wiring](https://github.com/vpsfreecz/vpsadmin/blob/26518b27959eb8a63f3fc0b481720a54aa14e41c/nixos/modules/vpsadmin/api-app.nix#L127),
  [package metadata task](https://github.com/vpsfreecz/vpsadmin/blob/26518b27959eb8a63f3fc0b481720a54aa14e41c/tasks/gem_updates.rb).
- [HaveAPI exact profile keys/validation](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/servers/ruby/lib/haveapi/documentation_clients.rb),
  [public usage](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/servers/ruby/doc/client-examples.md),
  [Go adapter](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/clients/go/lib/haveapi/go_client/documentation.rb),
  [Rust dependency rendering](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/clients/rust/lib/haveapi/rust_client/documentation.rb#L71).
- [Go module](https://github.com/vpsfreecz/vpsadmin-go-client/blob/1d9240f3d27b5831baf3694baab5fe06294875d8/go.mod),
  [generation instructions](https://github.com/vpsfreecz/vpsadmin-go-client/blob/1d9240f3d27b5831baf3694baab5fe06294875d8/README.md),
  [actual public-stats action](https://github.com/vpsfreecz/vpsadmin-go-client/blob/1d9240f3d27b5831baf3694baab5fe06294875d8/client/resource_cluster_action_public_stats.go).
- [Rust Cargo metadata](https://github.com/vpsfreecz/vpsadmin-rust-client/blob/ff876abe17e3301da62c1b6afbda055ec89db9d2/Cargo.toml),
  [TOML](https://github.com/vpsfreecz/vpsadmin-rust-client/blob/ff876abe17e3301da62c1b6afbda055ec89db9d2/generator.toml),
  [provenance](https://github.com/vpsfreecz/vpsadmin-rust-client/blob/ff876abe17e3301da62c1b6afbda055ec89db9d2/schema/provenance.json),
  [saved snapshot](https://github.com/vpsfreecz/vpsadmin-rust-client/blob/ff876abe17e3301da62c1b6afbda055ec89db9d2/schema/api-7.0.json),
  [actual output type/route](https://github.com/vpsfreecz/vpsadmin-rust-client/blob/ff876abe17e3301da62c1b6afbda055ec89db9d2/src/generated/resources/cluster/public_stats.rs).
  Snapshot SHA256: `70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`.

