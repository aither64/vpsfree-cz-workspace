# Profile simplification dependency and verification plan

This package prepares isolated dependencies and commands for base4dc0, not a
release or default integration. New source is still being authored. The setup
operation only guards immutable installation inputs, copies qualified ignored
locks and installs their exact frozen dependencies. It does not establish
functional source readiness. Source owners decide when their interfaces are
stable enough for the focused checks.

The exact baseline765-file mode/blob/SHA inventory is baseline.json. Installation
inputs and retained-lock qualification are installation-inputs.json and the two
Go qualification receipts. Root/server lock candidates are from the immutable
previous own dependency tree; the Go-unit candidate is from own followups. The
dedicated Go acceptance lock is from the earlier same-session HaveAPI tree.
Its Gemfile/gemspec/version/.ruby/flake.lock match, while flake.nix differs only
by the subsequently added libffi packages. Historical native/tool equality is
not claimed. No installed gems are copied or shared across worktrees.

## Exact setup boundary

One fresh policy-resolved Luna/low utility owns setup.py. The parent checks the
actual persisted turn context and payload hashes before opening its explicit
launch gate. Parsed declared default-shell exports supply Ruby3.4.11, the same
Ruby default-gem directory and native compiler/libffi tools. No automatic shell
hook or eval is used. Exact Bundler4.0.23 is installed with `gem install --norc
--no-document bundler --version 4.0.23`; each own gem-home/bin precedes PATH.
Inherited component Bundler/Gem/Ruby variables are cleared. Workspace CLI calls
use a separate clean environment. HOME and CODEX_HOME are preserved.

The own server home is new-root/.gems, matching the existing Rust fixture child
launcher. Go-unit uses new-root/clients/go/.gems; Rust uses
new-root/clients/rust/.gems. Each profile has separate own .bundle config/cache/
spec directories. The optional Go acceptance manifest uses the new server home plus the new Go
home through GEM_PATH after their frozen installs, with separate Bundler config.
Its older lock selects JSON3.1.0 from the Go home, while the server uses2.21.2.
The ignored root lock is preserved for tooling consistency; no extra root
development bundle is installed because server already supplies Ruby style.

Only frozen bundle installs get NIX_ENFORCE_PURITY=0: direct export otherwise
retains derivation purity and strips Prism's valid absolute local headers. This
is the existing root-flake accommodation, not a source or dependency change.
Third-party activation checks Bundler, RSpec, parser/native libraries and own
nondefault Fiddle1.1.8 for Rust, plus local project Bundler spec/path/version.
It does not require unfinished HaveAPI modules. Native feature records keep
relative entries raw/unmapped with builtin status unproven.

Go's accepted exact documentation lock has55 known external records and blank
CHECKSUMS. Before accepting its bundle, setup maps EVERY record to an original
gem in the two new own caches or its exact separately fetched evidence payload,
and compares actual SHA256 with a nonblank
checksum in the qualified server/Go-unit locks. Source/version/platform and
dependency edges must match. The initial strict guard stopped on the missing root-cache JSON archive. A full
read-only inventory identified JSON3.1.0 in the new Go cache and net-pop0.1.2
as a bundled Ruby library lacking an archive. Lead authorized only that exact
qualified original archive GET into new evidence; no install or resolution. The first reconciliation watcher exited without executing its command after
misreading the parent-only identity gate; that startup refusal is preserved. A
fresh corrected watcher then fetched the exact archive and passed55 payloads.
Frozen Bundler rejected the old blank CHECKSUMS. Lead authorized filling only55
verified external hashes in the new ignored lock: original17738 preserved, new
SHA9854dbae73d4b299a255042bdb562f4ab56475c950ba0076cdf708e3d4b883c0,
all nonchecksum bytes/records equal. A subsequent check found the exact selected
Git store binary absent, separately recorded from dependency graph failure. The
lead-granted same locked tools realization restored original paths/hashes, then
frozencheck/thirdpartyactivation passed in73.01s. All55 payload hashes and166
installation inputs stayed unchanged. No gem install was repeated for recovery. No local resolution/fallback, unknown install,
checksum invention or lock rewrite occurs. All original logs/evidence survive.
First failure or immutable-input drift stops the single batch without retry.

## Commands and phase separation

commands.json gives exact argv/cwd/profile/owner and phase. Once dependency
readiness succeeds, in_bundle.py selects only that own frozen environment.
Place `--cwd` before the profile, for example:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/client-example-profiles-setup-preparation/in_bundle.py --cwd clients/rust rust -- bundle _4.0.23_ exec rspec spec/unit/documentation_spec.rb spec/unit/documentation_factory_spec.rb spec/unit/model_spec.rb spec/unit/model_equivalence_spec.rb spec/unit/documentation_harness_spec.rb
```

Known short: source syntax/style, focused server profile/mount/structural/HTML/
auth checks, Go pure adapter units and standalone DSL checker, Rust pure docs/
factory/model/equivalence/harness units. They run inline only after their owners
yield stable interfaces and dependency readiness. Owner0 must run the documented
`make doc` prerequisite before Ruby server specs; this copies shared docs and
renders json-schema.html into the new own server/doc directory, so retain its
generated-file inventory rather than mislabeling it source drift. Go actual-DSL
checks wait for owner0's shared implementation. No Go spec_helper is selected
for pure units because it starts a test server. No Rust generator_spec is in the
pure batch: it invokes actual formatter/generation.

After all intended source/docs commits and retained independent final review,
fresh watchers own packaged-server HTML checks, actual rendered Go compile/run,
Rust async/blocking rendered compile/run and generation-equivalence. Keep base
and candidate generation input/config/formatter and complete output inventories;
compare source contents, ownership manifests and public names/runtime, not only
a compiler exit. Distinguish generated fixture SDK validation from installing a
real published SDK; neither proves current external vpsAdmin SDK compatibility.
No external package-version lookup is needed for omitted versions.

The Rust documentation runner currently requires an independent1.95 Cargo/
rustc and executes both modes under development and MSRV. Retained MSRV proof
may only cover unchanged complete runtime/compiler/input graphs; a new rendered
program or changed generated bytes needs its affected1.95 check. Use the runner
as documented rather than silently skipping its MSRV loop. Provide fresh own
Cargo home/target/cache and new evidence paths under a separately reviewed long
batch; do not borrow old mutable caches. No Cargo/npm setup or downloads are in
this Ruby setup grant. No broad make release-deps/full release build is planned.

## Input and tool evidence

retained-tool-input-facts.json preserves same-flake historical recursive roots
(2067 root derivations and1377 MSRV derivations), selected tool derivations/
outputs, actual formatter identity rustfmt1.10.0 and current binary-file hashes.
The Nix package path includes1.99.0; that is not the formatter's reported version.
These are retained facts, not a fresh build or complete new Nix evaluation.
Setup records selected exports and executable paths/hashes again. The complete
existing graph is referenced, not replaced by a guessed direct dependency list.

All long/uncertain operations require fresh watchers with absolute owning-root
AGENTS/development/verification/monitor/Rust-packaging guidance, exact frozen
command/input hashes, owned logs and terminal process identity. Unexpected local
Linux-kernel builds stop for investigation; no quiet timeout is invented. The
lead coordinates future slots. No build/test/CI/push/release/default integration
or cleanup is authorized merely by preparing this plan.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
