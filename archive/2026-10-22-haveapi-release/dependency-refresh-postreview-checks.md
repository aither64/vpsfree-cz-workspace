# Dependency refresh: post-review affected checks

Preparation only, implementer2, 2026-10-23. **Tested final head: UNSET.**
No setup, test, compiler, generation, network, CI, utility or Git action ran for
this package. [Frozen addendum](dependency-refresh-addendum.md) controls scope.
Owner1 owns all application/source work; owner0 owns Git; lead grants setup and
execution separately after slot handoff. Publication and new default integration
remain held. This record supplies no check or independent-review conclusion.

## Binding, source and tool guard

Canonical root:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-dependency-refresh`.
Base090a is source provenance, not the eventual tested head. Before any later
operation, lead supplies a committed exact head/tree and final-review receipt.
Require that head, clean tracked/index state, and hash every tracked input plus
ignored locks/setup receipts before and after. Stop on drift or first failure;
no automatic repair, retry, cleanup or expanded campaign.

Relevant source: `flake.nix`/`flake.lock`, `clients/js/{package.json,package-lock.json,
gulpfile.js,rollup.config.js,jsdoc.json,tsconfig.json,jsdoc_aliases.js}`, JS
src/dist/test/config files, `servers/ruby/{Gemfile,haveapi.gemspec,lib,spec,
test_support}`, `clients/ruby` path dependency, `doc/*`, `utils/copydoc.sh`, and
`utils/release/{artifacts.rb,npm-consumer.ts}`. Capture complete path/hash
inventories rather than just the listed entrypoints.

Declared shells: component `.#client-js` supplies Node without installers;
`.#server-ruby` supplies Ruby plus Node/PHP but automatically installs Bundler and
the server bundle. Use the declared **top** tools-only shell for the combined
batch, avoiding that automatic installer:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --no-write-lock-file -c bash <approved-session-script>
```

No script is launched by this preparation. Retain exact shell derivation/output,
full resolved Nix input graph, executable store paths and actual Ruby/Node/npm/
Bundler/TypeScript versions in the later receipt. Current pinned nixpkgs is
`02c087f3fe673c9e317f206a627cb6b910336dbe`; Node24 stays selected. Prior setup
reported Node24.21.0/npm11.19.0, not a fresh tool measurement here. Require actual
TypeScript6.0.3, Rollup4.65.0, JSDoc4.0.5, Markdown15.0.3, anchor10.0.0,
linkify6.1.0 and retained declared Node24 types/peer graph. No old node_modules.
Owner1's own frozen install receipt and unchanged manifest/lock/integrities must
bind the eventual candidate; recheck `npm ls`/module realpaths in that environment.
Do not start another npm installation merely because this is a new check phase.

## Smallest own server Ruby prerequisite — separate setup grant

[Read-only input comparison](dependency-refresh-postreview-prerequisites.json)
finds identical server Gemfile/gemspec/version, Ruby-client gemspec/version,
`.ruby-version`, root Gemfile and flake inputs against retained followups.
Its server lock is available, SHA-256
`cec5e86c703239afa8c5914111ec3773ac7b8b485fc8e33cba80872cc51959b5`,
Bundler4.0.23, with x86_64-linux-gnu resolution. It therefore qualifies as the
**proposed frozen lock source**, conditional on the same proof immediately
before setup. Copy that lock only to the own ignored
`servers/ruby/Gemfile.lock`; never copy installed/native gems. No copy occurred.

Own missing `.gems` does not require reinstalling every component. Existing root
deps remain usable read-only through the already inspected
`approved-default-integrations-20261023T195622Z/haveapi-hook-env.sh`, subject to
same root Gemfile/lock, exact selected Ruby/tool and closure proof. The
registration readiness also records read-only followups hook deps. Do not run
`hooks-ready.sh` again (it signs shared hooks), or pass an installer through a
wrapper whose GEM_HOME points at followups. Root RSpec is not the server bundle.
The helper smoke below needs Ruby standard libraries, not a root bundle install.

After owner1 yields the shared slot, propose a fresh setup watcher under the
declared top tools-only shell. Select its exact Ruby3.4 tool/store path from
readiness (prior prepared root was Ruby3.4.11); check equality before install.
Use only these **own** destinations beneath the canonical root:

```sh
CHECK_ROOT=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-dependency-refresh
unset RUBYOPT BUNDLE_BIN_PATH BUNDLER_SETUP BUNDLE_PATH BUNDLE_LOCKFILE
export GEM_HOME="$CHECK_ROOT/.gems"
export GEM_PATH="$GEM_HOME:$(ruby -e 'puts Gem.default_dir')"
export PATH="$GEM_HOME/bin:$PATH"
export BUNDLE_GEMFILE="$CHECK_ROOT/servers/ruby/Gemfile"
export BUNDLE_USER_HOME="$CHECK_ROOT/.bundle/postreview-user"
export BUNDLE_APP_CONFIG="$CHECK_ROOT/.bundle/postreview-server"
export BUNDLE_USER_CACHE="$BUNDLE_USER_HOME/cache"
export BUNDLE_USER_CONFIG="$BUNDLE_USER_HOME/config"
export GEM_SPEC_CACHE="$BUNDLE_USER_HOME/spec-cache"
export BUNDLE_IGNORE_CONFIG=1
```

Use the fresh own `.gems/cache` archive cache and own Bundler user/config paths;
no global config mutation or native bundle borrowing. Normal default gems come
only from the selected Ruby standard gem dir. Ensure the ignored destinations
are new/owned before creation. Freeze a pre-existing destination for inspection
instead of overwriting it.

Once lock/source/platform proof and explicit setup grant exist, the exact narrow
installation payload is:

```sh
gem --norc install --no-document bundler --version 4.0.23
cd "$CHECK_ROOT/servers/ruby"
NIX_ENFORCE_PURITY=0 BUNDLE_FROZEN=true bundle _4.0.23_ install
BUNDLE_FROZEN=true bundle _4.0.23_ check
bundle _4.0.23_ exec ruby -e 'require "rspec"; require "rackup"; require "webrick"; require "require_all"; require "sinatra/base"; require "active_record"'
```

The Prism local-header setting matches the existing top-shell accommodation and
applies only to installation. Record actually resolved dependencies, native
extension/tool identities and lock equality. Do not extend this into Rust setup
or tests. If retained lock/input equality fails, **stop**: lead may instead grant
normal resolution of this own server Gemfile (`bundle _4.0.23_ lock`), retain the
new lock/input graph and then freeze installation. Never silently fall back or
pretend an unresolved lock is frozen. Setup network/native gem compilation is a
separate future prerequisite grant, not authorized by this brief.

## Exact affected batch after final review and separate execution grant

Use the above own server environment with `BUNDLE_FROZEN=true`, Node from the
same top shell, and `CHECK_ROOT` canonical. Own server lock/bundle activation
must pass without install; capture which local HaveAPI/client paths Bundler uses.
Do not use full `make test`, `make release-deps` or release build.

1. Full JS suite, including actual Ruby-server contract tests:

   ```sh
   cd "$CHECK_ROOT/clients/js"
   npm test
   ```

   This runs normal build, compatibility, async/resource/type suites and Mocha.
   `test/helpers/server.js` starts the own Ruby test API via server Gemfile,
   loopback127.0.0.1 with ephemeral port0; readiness/health is real, not fake XHR.
   Contract tests cover CallbackAdapter and AsyncAdapter; their normal after
   hooks stop the server. Retain complete stdout/stderr, counts, exit/timing and
   owned server PID/readiness/exit evidence. Require explicit localhost permission
   in the later execution grant; reconcile owned processes on failure, no blind
   retry or unowned process termination.

2. Real gulp documentation task:

   ```sh
   cd "$CHECK_ROOT/clients/js"
   ./node_modules/.bin/gulp doc
   ```

   Task rebuilds source, invokes actual JSDoc/Markdown plugin, then Action alias
   writer into `html_doc`. Retain all diagnostics and HTML output hashes. Check
   actual Client/Action/Resource pages, navigation, canonical invoke and exactly
   one invoke__anchor. `npm test` also covers real JSDoc repeated headings, links,
   fenced code and bare URLs; this task establishes the public gulp entrypoint.

3. Shared server docs then dynamic-JS compiler specs:

   ```sh
   cd "$CHECK_ROOT"
   make doc
   cd servers/ruby
   bundle _4.0.23_ exec rspec spec/client_examples/dynamic_js_spec.rb
   ```

   `make doc` needs shell `erb`, `cp` and root doc sources. It renders
   `doc/json-schema.erb` to `servers/ruby/doc/json-schema.html`, copies exactly
   the four root Markdown documents (`protocol.md`, `create-client.md`,
   `typed-input-validation.md`, `client-examples.md`) and `protocol.png`.
   No server gem build, JSDoc output or other-component setup is required.
   This obeys the server-spec procedure even though this focused spec principally
   uses dynamic_fixture, real emitted declarations, Node syntax/transpileModule
   and strict TypeScript renderer programs. It does not select Python or optional
   Go/Rust bundles. Keep compiler/Node diagnostics and RSpec seed/count/exit.

4. Narrow isolated npm artifact/consumer smoke:

   Bind `CHECK_ARTIFACTS` to a **new** retained session directory, supplied by the
   lead. Verify catalog version from VERSION and package manifest, reviewed
   entrypoints/files/repository, exact new built dist inventory and clean source.
   Then, with grant for packaging and local consumer install, use normal npm pack:

   ```sh
   cd "$CHECK_ROOT/clients/js"
   npm pack --ignore-scripts --pack-destination "$CHECK_ARTIFACTS"
   cp dist/haveapi-client.js "$CHECK_ARTIFACTS/haveapi-client.js"
   cd "$CHECK_ROOT"
   ruby -r "$CHECK_ROOT/utils/release/artifacts" -e 'HaveAPI::Release::Artifacts.new(ARGV.fetch(0)).smoke_npm(ARGV.fetch(1))' "$CHECK_ROOT" "$CHECK_ARTIFACTS"
   ```

   Preserve exact TGZ/browser SHA-256, tarball SHA-512, pack file inventory and
   manifest/lock/dist/compiler/source binding. This calls existing production
   Artifacts#smoke_npm directly: inspect_npm checks catalog identity, repository,
   main/types, docs/license, nonempty declarations and packed/browser equality;
   temporary consumer installs retained TGZ with scripts disabled and NODE_PATH
   unset, checks actual package-name callback/async exports, then strict tsc with
   noEmit/listFiles. Every declaration must resolve inside installed package or
   selected compiler standard libs, never checkout declarations. Existing
   ignoreDeprecations6.0 remains limited to the accepted node-resolution option.
   Do not use CLI smoke-npm: it first requires a full release manifest/catalog.
   Direct invocation proves only npm artifact/consumer acceptance, no simulated
   whole-catalog verify. VERSION remains0.30.0 while release is held; these are
   development bytes, never replacements for published0.30.0 packages.

   The helper's local npm install also resolves runtime xmlhttprequest (current
   manifest range latest); own cache completeness is **unknown**, not inferred
   from node_modules. Lead must choose an own cache/network prerequisite grant
   before execution. If an offline cache policy is selected, set
   `npm_config_offline=true` and own approved `npm_config_cache`; missing cache
   stops the operation. Do not borrow old node_modules/native packages, skip
   dependencies or replace actual helper behavior with a handwritten consumer.

## Evidence and remaining gates

Retain per-phase command/cwd/complete logs/status/timing, exact final head/review,
input/lock/tool graphs and source/index/dist preservation before/after. Preserve
full diagnostics; no warning filter/skipLibCheck. Gulp/build output may touch
owned ignored build/docs; tracked dist must remain exactly the reviewed bytes.
No automatic cleanup is granted. Final report distinguishes actual local-server
execution, actual gulp docs, strict renderer compile and installed TGZ consumer.

Outstanding now: owner1 frozen yield and utility slot; final commit/review/head;
own server setup grant and activation proof; generated shared docs; chosen
fresh npm artifact directory and consumer dependency/cache policy; explicit
post-review execution/localhost/pack/install grant. Prior receipts establish
context only. No extra Rust/MSRV, publication, CI dispatch or default integration.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
