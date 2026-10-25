# Expanded API-documentation package receipt

Implementer0; session `2026-10-22-haveapi-release`; HaveAPI only. Original release
receipts and root dist artifacts for `08345b2` remain untouched. User approved
implementation; no default integration, release refs, publication or deployment.
All four package prose passes were completed directly by lead before commits.

## Source and ownership

Implemented the frozen api-doc-contract.md: request-local immutable Context,
legacy renderer ABI bridge and stable IDs; startup-only optional Go/Rust profile
registration/validation; filtered mounted HTML panels and overview; File system
renderer/link removal; escaping and authorization regressions; local highlighter
and keyboard/narrow-screen tabs; shared packaging, dependencies and quick CI.
Language owners supplied their exact owned-path commits under my sole index/hook
ownership. No blanket stash, reset or clean. Optional generators stay absent from
the server dependency contract.

Go acceptance uses a separate `clients/go/spec/documentation.Gemfile` activating
local server, Go generator, Ruby client and WEBrick. Its local lock is ignored,
following Go dev-lock policy. The ordinary server bundle cannot activate an
optional Go gem solely by a load path; production spec/version validation remains
strict. Owner preflight proved activated haveapi and haveapi-go-client 0.30.0,
WEBrick 1.9.2 and real Profiles loading without listener or compiler. No install
was necessary. Manifest style passed. Rust acceptance optional evidence retains
snapshot/TOML/actual generated Cargo.lock/ownership/source and exact tool identities
per mount; it refuses mixed existing evidence and retains available failure data.

JS strict renderer specs need Node declarations and built public declarations.
`make release-deps` prepares JS dev dependencies; `make test-documentation` and
full `make test` build JS before server specs. Shared Ruby CI prepares Node24,
npm ci and build first. Test-only @types/node24.19.2 (undici-types7.24.6) does not
become a runtime dependency. Highlighter pins highlight.js11.12.0/esbuild0.28.2
and BSD license. Build disables output template literals to preserve grammar
bytes while avoiding generated trailing whitespace. npm reproducibility check
and worker tests pass. New guide copied by make doc is ignored and packaged.

Official refs checked live: actions/checkout v7.0.1
3d3c42e5aac5ba805825da76410c181273ba90b1;
cachix/install-nix-action v31.11.2
448cde739abec1eaf0646249e3d25bb8d9bc7702;
actions/setup-node v7.1.0
949feb2413d6458794dcd2491c4babbbce0c15c1;
ruby/setup-ruby v1.333.0
e1bd6146574da5e0795075b5319b300edb30c5b0;
actions/setup-go v7.0.0
b7ad1dad31e06c5925ef5d2fc7ad053ef454303e.

## Quick evidence before consolidation

Prepared root Nix environment; HAVEAPI_RELEASE_TOOLS_ONLY=1 avoids setup in
quick and hook commands. All primary and fixup commits ran declared Overcommit
I18n/RuboCop hooks as applicable, all passed. Some commit-msg width warnings were
nonblocking; every mandatory maximum80 line rule is satisfied. During final
history rewrite each resulting logical commit also runs declared amendment hooks
with a temporary message file. Original maintenance -x provenance preserved.

- `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make test-documentation`:
  JS build, **67 examples/0 failures**, highlighter/fallback and keyboard/ARIA
  tests pass. Includes all dynamic, fake-adapter Go/Rust, no-profile, configured
  profile, stale sample, mount, HTML escaping and per-user privacy checks.
- `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make release-check`: valid0.30.0.
- `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make release-test`:
  **78 release specs/0 failures +6 Python tests/0 failures**. These use temporary
  fake registries and isolated test packages, not the retained original dist.
- Asset `npm run check` byte equality, JS syntax, both changed workflow YAML
  parses and diff whitespace checks pass.
- Shared packaging/style: **3 Ruby files/0 offenses**, dedicated Gemfile1/0.
  Actual full server gem packaging test deliberately remains post-review.
- Go owner: **26 pure generator +4 standalone bridge specs/0**, style7/0.
- Rust owner final: **28 adapter/harness +7 standalone bridge specs/0**,
  evidence followup style5/0; earlier full package style7/0.
- Dynamic owner: **15 specs/0**, including10 strict rendered TS programs,
  helper runtime3/3, callback compatibility29 +clobbering7,
  callback/async declarations and built-bundle ESM imports pass; style13/0.

## Post-review commands, not run

All commands start in exact final HaveAPI worktree. Prepare and run through a
fresh policy Luna/low watcher after mandatory final review. Preserve **all** old
dist entries, including .gitignore, under session baseline-artifacts before the
fresh release build; build.sh requires a literally empty dist. Do not mix baseline
08345b2 payloads with the new candidate. Lead owns that preparation/long batch.

Full build/test/package batch:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c 'make release-deps; make release; make test; cargo clippy --locked --manifest-path clients/rust/runtime/Cargo.toml --all-targets --all-features -- -D warnings; ruby utils/release/cli.rb smoke-npm dist; (cd clients/python && uv run --locked python utils/package_smoke.py); ruby utils/release/cli.rb verify dist'
```

Root shell supplies Rust tools; shared RUST_ENV isolates its locked component
bundle and Ruby defaults from user cache. make release runs packaged Rust smoke;
make test already includes generator/runtime/generated protocol checks, so do not
repeat identical Rust runtime checks. Renderer acceptance below is additional.

Dynamic wheel command (repeat with haveapi_client-0.30.0.tar.gz and distinct
output path to prove sdist):

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c 'source_root=$PWD; cd servers/ruby; bundle exec ruby spec/client_examples/dynamic_acceptance.rb --npm-artifact "$source_root/dist/haveapi-client-0.30.0.tgz" --python-artifact "$source_root/dist/haveapi_client-0.30.0-py3-none-any.whl" --typescript "$source_root/clients/js/node_modules/typescript/bin/tsc" --node-types "$source_root/clients/js/node_modules/@types" --output /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/dynamic-acceptance-wheel'
```

Dynamic sdist command, using distinct retained output:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c 'source_root=$PWD; cd servers/ruby; bundle exec ruby spec/client_examples/dynamic_acceptance.rb --npm-artifact "$source_root/dist/haveapi-client-0.30.0.tgz" --python-artifact "$source_root/dist/haveapi_client-0.30.0.tar.gz" --typescript "$source_root/clients/js/node_modules/typescript/bin/tsc" --node-types "$source_root/clients/js/node_modules/@types" --output /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/dynamic-acceptance-sdist'
```

Go preflight and16-program acceptance with dedicated activated bundle:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c 'export BUNDLE_GEMFILE="$PWD/clients/go/spec/documentation.Gemfile"; bundle check; bundle exec ruby clients/go/spec/documentation_acceptance.rb --check-environment; bundle exec ruby clients/go/spec/documentation_acceptance.rb'
```

On a fresh dependency setup use `bundle install` with the same BUNDLE_GEMFILE;
for this prepared checkout local-only resolution/check already passed, no install.

Rust rendered async/blocking acceptance (26 programs per mount, both compiler
selections), independent MSRV paths from api-doc-msrv-readiness.md:

```sh
HAVEAPI_RUST_DOCUMENTATION=1 HAVEAPI_RUST_MSRV_CARGO=/nix/store/rai05nypxnmj22l65nwsk5xjsaq8s4vc-cargo-1.95.0/bin/cargo HAVEAPI_RUST_MSRV_RUSTC=/nix/store/m4hrdkg9ypcw8y1banfc26q3f27kfqvb-rustc-wrapper-1.95.0/bin/rustc HAVEAPI_RUST_DOCUMENTATION_EVIDENCE=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/rust-documentation-evidence nix develop .#client-rust --command ruby clients/rust/spec/documentation/run.rb
```

Do not inherit RUSTC/compiler wrappers overriding development1.99.0/MSRV1.95.0.
Evidence mount directories must not exist; ensure retains inputs on failure.
Lead exact-head guard/wrapper is verify-api-doc-release.sh; it is prepared and
unrun. No compile/run acceptance or new release artifact evidence is claimed yet.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

## Final history and source freeze

Fresh SSH fetch and final `ls-remote --heads origin master
2026-10-22-haveapi-release` both proved target master remains
`a32b15e379f44fc6dae4b15ef4ec17a142e5f465`; remote feature remains original
`08345b2d5ede025972a3daec8b4a373efb51d711`. Expanded branch has not been pushed.

Final base: `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`.
Final head: `607941c035af0c7466cedb5ca6c2d36841ea34a5`.
Final tree: `17916258a4191edd85d5e543356aee2df7efa77e`.
Pre-consolidation head: `6204d0d3dae1c370f0d4ed218ded33adcbaaf6b2`, same tree.
Tree equality and complete binary aggregate diff equality both proved by script;
no rebase conflicts or source decisions occurred. No generated file hand edits.
All 18 resulting logical commits ran declared pre-commit and commit-msg hooks
through hooked amendment from temporary message files; every hook passed.
Final Version commit additionally ran PythonChecks, PHP style and RuboCop.
Some existing width warnings remain advisory (all message lines <=80).
The final commit's full message bytes are `Version 0.30.0\n` (Git pretty output
adds another terminating newline). Exact user wording, no body.

Final post-rewrite `make release-check` passed valid0.30.0; full-range whitespace,
tracked working-tree diff and index diff are clean. Tree-equivalent rewrite did
not justify repeating already-green meaningful quick suites; all final Go/Rust
bounded followups had owner quick/style evidence before consolidation.

All new source precedes version/changelog, old three released maintenance
commits retain exact patch/message and -x provenance. Full proofs are
api-doc-final-provenance.json. All fixups are folded; no fixup/squash subjects,
unused alternatives or unresolved transition commits remain. Source context,
filtered UI, language packages, generated bundle and packaging/CI are distinct
reviewable steps. The metadata commit coherently includes versions, dependency
agreements, tracked Rust lock and approved lead CHANGELOG top7-line expansion.

No database/state/schema migrations exist in this series. The112 changed paths
contain no migration directories, and intended changes preserve protocol and
persistent formats. No new implementation revision has been merged, released,
deployed or consumed downstream. Original feature08345b2 is branch-published,
with retained local/CI release artifacts; its exact refs/evidence remain intact.
Three earlier released maintenance source fixes are retained separately with
provenance; they are not new migration boundaries.

Repeated update streams and dispositions:

| Stream | Final commit(s) | Disposition |
| --- | --- | --- |
| Rust shared release catalog/build/smoke | b3a6a0b1 | One source stream, prior setup/source fixes folded before original review |
| Released server maintenance | 5b5f0c25, dda40adb, 9c4c8a7c | Three separately reviewable exact released behavior/provenance commits |
| Publication tests/docs | 878509d5 | Includes prerequisite prose fixup; catalog source precedes tests |
| PyPA publish action | 1e810107 | Separate single action update v1.14.3 |
| Node test declarations | 593fac92 | One package+lock update, @types/node24.19.2/undici-types7.24.6, no intermediate pin |
| Go adapter/acceptance | 09f6b22c | Dedicated bundle/preflight followup folded into owner source |
| Rust adapter/acceptance | 1f8aac4c | Evidence followup folded into owner source |
| JS helper generated output | 788dde10, 29b0415a | Authored public helper then one corresponding generated bundle/declarations commit |
| Highlighter dependency/generated stream | ee10f589 | One build+lock+license+bundle step, no intermediate pins/assets |
| Shared docs/CI preparation | 5f0e9f96 | Node dependency ordering fix included with owning orchestration; exact current action pins |
| Shared0.30.0 metadata | 607941c0 | One final coherent version/changelog commit, generated version delta distinct from helper-source generation |

Complete final base-to-head series:

- `b3a6a0b1 release: include the Rust generator in shared releases`
- `5b5f0c25 servers/ruby: validate structured API examples`
- `dda40adb servers/ruby: syntax-check generated client examples`
- `9c4c8a7c servers/ruby: render nested PHP example values`
- `878509d5 release: cover Rust publication and publisher setup`
- `1e810107 release: update PyPA publishing action to v1.14.3`
- `f50c540d servers/ruby: remove unmaintained filesystem examples`
- `4337f1a6 servers/ruby: add request-local client documentation context`
- `b495832d servers/ruby: render filtered client documentation panels`
- `593fac92 clients/js: add Node 24 types for documentation acceptance`
- `09f6b22c clients/go: render SDK documentation from saved profiles`
- `1f8aac4c clients/rust: render SDK documentation from saved profiles`
- `788dde10 clients/js: add typed action lookup`
- `29b0415a clients/js: regenerate action lookup bundle`
- `aee69b7b servers/ruby: document maintained dynamic clients`
- `ee10f589 servers/ruby: ship supported highlighting and accessible tabs`
- `5f0e9f96 servers/ruby: prepare and package client documentation`
- `607941c0 Version 0.30.0`

Complete exports: api-doc-history-before.json, api-doc-history-before-series.txt,
api-doc-history-before-diff.patch; api-doc-final-identity.json,
api-doc-final-series.txt, api-doc-final-diff.patch, api-doc-final-names.txt,
api-doc-final-stat.txt, api-doc-final-range-diff.txt, api-doc-final-status.txt,
api-doc-final-provenance.json. Original final.diff/final-history/final-review
receipts remain untouched. Portal comparison captured exact final base/head.

Tracked source clean and index empty. Only preserved generated untracked
clients/php/.phpunit.result.cache and utils/release/__pycache__/ remain; neither
is a deliverable or staged. All owners yielded source/Git; no pending command,
source edit, hook, gem install or npm operation. Git/index/hooks yielded to lead
for read-only final review. No further mutation or push until directed.
