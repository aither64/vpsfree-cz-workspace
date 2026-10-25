# Real Rust profile mount acceptance

Accepted by lead on 2026-10-24. This closes the runtime coverage gap between
server specs with fake optional modules and Rust renderer checks using real
factories but Struct profiles. Neither proves real optional-gem registration
through `Server#documentation_clients` and `Server#mount`.

The current 27-path product packet does not change. Include this pending gate
in the final review packet. Execute against the final committed, reviewed source
before integration. A failure requiring a source correction reopens affected
quick checks and final review. No tag, publication or deployment is authorized.

## Ownership and timing

- Owner1 prepares and qualifies one session-owned combined dependency closure,
  manifest, lock, sanitized launcher and input/payload evidence. No setup/install
  before owner0's final committed yield; execution follows the lead's grant.
- Owner3 authors the session-only Ruby probe after yielding the active hook fix
  and receiving lead's separate probe-authoring grant. Coordinate probe/launcher
  filenames with owner1; neither edits the other's files.
- Owner0 retains all Git. The lead accepts the exact reviewed head, includes this
  gate in the review packet, and authorizes post-review execution. The architect
  changes only this brief and its design link.

Use `work/2026-10-22-haveapi-release/client-example-profiles-rust-mount/` for
`Gemfile`, `Gemfile.lock`, `probe.rb`, qualified launcher, `inputs.json`, runtime
and payload inventories, full logs and `result.json`. These are session-only
verification inputs/evidence, not new product dependencies or shipped fixtures.

## Frozen manifest and dependency graph

Source root is the registered worktree:

```text
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-client-example-profiles
```

Branch: `2026-10-24-haveapi-client-example-profiles`; immutable initial base:
`4dc0f7e11c494d1a0dc852dabcc312411699fcab`. Owner0 supplies the final head/tree;
do not substitute the base or an earlier inventory for the actual candidate.

Minimal new manifest shape (absolute owning paths):

```ruby
eval_gemfile '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-client-example-profiles/servers/ruby/Gemfile'
gem 'haveapi-rust-client', path: '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-client-example-profiles/clients/rust'
gem 'fiddle', '= 1.1.8'
gem 'tomlrb', '= 2.0.5'
```

Retain the qualified **server** locked external graph unchanged, adding exactly
the two qualified Rust external gems above and the local Rust gem. Static lock
comparison found one shared-version difference: server `mime-types-data
3.2026.1020` versus Rust `3.2026.1013`. Select the server version; the graphs are
not identical. No other shared name/version differs. Use only the already
qualified own cached archives, with their retained checksums, dependency edges,
platform and native-input evidence. No network, new versions or unconstrained
resolution. Missing payload/native prerequisites are reported to lead.

The new combined lock must resolve local `haveapi`, `haveapi-client` and
`haveapi-rust-client` to that same final worktree. Do not reuse a lock whose
relative PATH entries now resolve elsewhere. No product Gemfile/lock edits,
ad hoc `RUBYLIB` injection, or combining two component gem homes in `GEM_PATH`.
One independently qualified combined closure owns external activation. Native
gem reuse is subject to owner1's existing checksum/input qualification; it is
not permission to copy an unqualified native installation.

Select Ruby
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`
and Bundler `4.0.23`. Use the retained declared runtime/native environment and
prove nondefault Fiddle `1.1.8`. Owner1's existing
`client-example-profiles-setup-preparation/in_bundle.py` has no combined profile;
provide a separate qualified launcher or extend its session-only inventory.
Clear inherited Ruby/Gem/Bundler settings as that launcher does. Freeze the new
manifest/lock and activate with `BUNDLE_FROZEN=true`, `BUNDLE_IGNORE_CONFIG=1`.

Command contract: qualified launcher -> exact Ruby with Bundler setup ->
absolute `probe.rb`, with `BUNDLE_GEMFILE` set to the new combined manifest.
Owner1 records the actual argv/environment before execution; this brief does
not pretend a launcher or resolved combined lock already exists.

## Required probe matrix

Use real `require 'haveapi'`, DSL resources, registration, mount, Profile and
renderers. Let registration load the optional Rust adapter. No fake modules,
Struct profiles or adapter factory stubs. Do not import the long Rust runner.
Use `Rack::MockRequest` and real contexts; no listener, action execution,
generator generation, formatter, compiler, registry or live-API operation.

1. **Absent and minimal profiles.** In the initial fresh process, an unconfigured
   server hides both Rust variants and has not loaded the optional Rust adapter.
   Then mount configured servers at `/` and `/mounted/api/`, API version `7`,
   using only `rust: { crate_name: 'fixture-client' }`. Prove the real loaded
   server/generator versions match and omission of `generator_version` succeeds.
   The real profile has nil `package_version`. Both renderers emit real code:
   `cargo add fixture-client`, adding `--features blocking` for blocking. Actual
   base/mount URLs survive; no fabricated SDK version, `nil` installation text,
   literal Cargo `latest` version or `haveapi.invalid` reaches output.
2. **Explicit version and source.** Matching explicit generator version and
   `crate_version: '1.2.3'` preserve rendering apart from dependency instructions;
   a mismatching generator version rejects. A Git source with
   `git: 'https://example.test/fixture-client.git'`, `rev: 'a' * 40` and no SDK
   version emits Git/rev with no invented version. Blocking retains its feature.
   Reject malformed or credential-bearing source. These URLs are never fetched.
3. **Legacy controls.** Form a saved snapshot from the same real mounted
   structural description via pure `Snapshot.from_description`, without fetch.
   Save a real TOML config with `crate_name`, `crate_version`, `license = 'MIT'`,
   `edition = '2024'`, `rust_version = '1.95'`, and `rustfmt_version` copied from
   the retained exact selected formatter-version string as inert data. Register actual
   `snapshot_path` plus `generator_config_path`; compare authorized init/action
   output to matching inline explicit identity. Also cover TOML-only automatic
   schema and snapshot-plus-inline identity. Reject snapshot API-version mismatch
   and conflicting legacy/inline identity. Do not execute the formatter.
4. **Authorization and private schema.** Adapt the small real DSL/auth pattern
   in `servers/ruby/spec/client_examples/profile_mount_spec.rb`, excluding its
   stubs: visible action/field/sample, privileged-only action and input/output
   fields, sentinel secret defaults and privileged sample values. Real fixture
   Basic authentication and requests admin -> member -> member must show actual
   Rust code in both variants for allowed samples, and privileged samples only
   to admin. Restricted HTML and authorized help exclude hidden actions/fields
   and all sentinel values. Repeated restricted rendered code stays equal.
   The adapter retains full naming structure but no structural defaults/examples.
   Rendering a forged hidden action/sample against the restricted real Context
   returns a typed limitation without disclosing its sentinel payload.
5. **Atomic real failure.** Configure two versions: valid first Rust profile,
   then `crate_name: 'self'`. This name passes package validation at registration
   but the real adapter rejects it as an unimportable Rust name during mount.
   Assert sanitized `Profiles::Invalid`, `server.app == nil`, and no profiles
   exposed for either version. Also cover unknown selected API-version rejection.

No separately generated SDK or compiler campaign is needed to close this seam.
The existing Rust model-equivalence and renderer compile/runtime matrix remains
mandatory under [its own brief](client-example-profiles-rust-postreview-brief.md).
This probe proves actual local path-gem integration, not packaged installation
or compatibility of the independently published/deployed vpsAdmin SDK.

## Evidence and later 0.30.1 subset

Retain exact final source head/tree, manifest/lock/probe/launcher digests,
complete dependency/native inputs, actual loaded project/external spec paths and
versions, assertion names/results, full output, exit and timing. Check inputs
before and after execution; do not convert an unexpected limitation into a pass.
No cleanup or retry after failure is implied.

After real 0.30.1 version preparation, repeat the minimal-profile/default
generator-version case against the actual prepared source and matching three
local gem versions, plus explicit matching/mismatching generator controls and
nil SDK version/install-output assertions. Bind any version-only lock changes
to the prepared metadata; external dependencies stay fixed. Earlier 0.30.0
execution is not fresh 0.30.1 evidence. Existing compiler evidence may apply only
under the accepted unchanged-input/version-only rules; no new compiler campaign
is added by this mount gate.
