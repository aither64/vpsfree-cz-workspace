# Held 0.30.1 worktree: static setup prerequisites

Static preparation only; no language tool/check, require, Nix evaluation/setup,
network/API/CI observation, install, build, test, compiler, Git command/ref mutation
or application/config write. Rust watcher operation was not inspected. Owner1
owns future physical setup; owner0 owns backports/Git/version edits after actual
master integration proof. The held source/artifacts remain untouched.

Scope is the retained `haveapi-0-30-1` worktree under this session. Its held
8270b/tree090a binding is the lead's retained source fact; no new Git check was
performed. Compared only static files here against the retained accepted67
source export `client-example-profiles-commit-retry-20261024T084523Z/04-server-profiles-after.json`
(head 67fcd34ba506264a5c7ee2e8e18a88d221c6f469, tree
80804b1c0c3ed33fc4b086673dbc3618a789cd4f). Exact path/type/owner/mode/hash records
and input comparisons are in [the JSON inventory](release-0-30-1-static-prerequisites.json).

## Actual files present/absent

| Area | Current static fact |
| --- | --- |
| Root | Ignored Gemfile.lock exists: SHA7c48d2c2ecc7dd97ecf37bdcebdd92fc100a3c8f1c8430a28a2ec45ed1d24c80; Bundler4.0.23, ruby/x86_64-linux platform records. No `.gems`, `.bundle`, `.config` or `.npmrc`. |
| Server/Ruby client | No component Gemfile.lock, gem home or Bundler directory. |
| Go | No component or optional documentation lock, `.gems` or Bundler directory. |
| Rust | Tracked lock exists unchanged at7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4. No component `.gems` or Bundler directory. |
| JS/highlighter | No clients/js or utils/highlight node_modules; no JS .npmrc. |
| PHP/Python | No PHP vendor or composer.lock; no Python .venv. |

Ignored classification follows the owning `.gitignore` rules (Gemfile.lock,
.gems, .bundle, node_modules); tracked Rust lock is the explicit exception. No
credential/config values were read. No own installed gemspec metadata exists
because all inspected own gem homes are absent. **Nothing is dependency-ready
merely from this inventory.** The root ignored lock differs from the accepted67
root lock450de01a; preserve it and qualify its graph before any later reuse or
replacement. No root graph equivalence is asserted.

## Dependency reuse applicability

All 22 inspected non-JS inputs equal accepted67 bytes: root/component Gemfiles,
four gemspec/version identities, `.ruby-version`, flake/lock, shared VERSION,
Makefile, tracked Rust lock, Python pyproject/uv lock. The JSON has individual
hashes. This allows later exact input/graph qualification; it does not authorize
using another worktree's writable gem home, copying native extensions or calling
an absent local bundle ready. The selected declared Ruby3.4.11/Bundler4.0.23,
platform, binary/native identities and persistent tool-root binding still need
owner1's patch-specific execution receipts.

JS package.json/package-lock/tsconfig differ from accepted67. The planned
`4dc0 -x` dependency backport will supply the new graph before setup. Do not
resolve/install using the held old JS graph, reuse another node_modules, or
claim old dependencies apply. Compare the actual post-backport inputs first;
then owner1 may prepare the exact frozen own npm graph under a separate grant.
Other dependency/build-source changes must be inventoried after backports too.

## Smallest later setup order

1. After master integration proof, owner0 establishes actual intended backports
   and the patch source inventory. Reprove exact owning Gemfiles/gemspecs,
   `.ruby-version`, flake/lock/system, VERSION and tracked/ignored locks. This
   static held-tree comparison does not substitute for that final binding.
2. Owner1 prepares/rebinds the declared **top tools-only** shell and persistent
   own tool proof. `make version` uses make/shell/coreutils/sed, Node, Ruby,
   Bundler and **uv**; top tools-only avoids automatic shell-hook installs.
   Component shell hooks install automatically and must not be entered as an
   ungranted shortcut. Root hook/release-test dependencies require their own
   qualified environment; absent root .gems does not authorize borrowing one.
3. Before `make version VERSION=0.30.1`, prepare the owning Rust component bundle
   against its current tracked lock. The target calls `bundle lock --local`
   under its own Rust GEM_HOME/GEM_PATH and absolute component BUNDLE_GEMFILE.
   It also calls `uv lock` in clients/python. This needs the declared uv/Python
   tools/cache policy, not an already installed Python .venv. Node only edits
   package/lock metadata here; npm dependencies are not needed just to bump.
   Do not run full release-deps merely to satisfy versioning. No version action
   is authorized by this preparation note.
4. Once owner0 changes versions, rebind local PATH/spec/requirement/CHECKSUMS
   records for server/Ruby/Go/optional/combined bundles to actual0.30.1 source.
   Prepare missing own Ruby-client/server/Go-unit closures and Go optional
   description closure; the latter needs real haveapi/haveapi-client/Go specs,
   dedicated ignored lock and own config. A Rust component bundle alone cannot
   supply the server or combined mount check. Keep recorded external graphs,
   Fiddle1.1.8 and Tomlrb2.0.5; no default/native borrowing or silent resolution.
5. After the actual metadata candidate is committed/reviewed, use only the
   proportional release-check/release-test, authoritative build-only and real
   version-sensitive subset in the controlling brief. Minimum Go/Rust mount
   checks need patch-bound loaded-version/path assertions, without a new
   compiler/listener/MSRV campaign. Owner1 supplies exact commands/environment;
   owner0 preserves hooks and expected version-only changes.

[release-version-sensitive-verification.md](release-version-sensitive-verification.md)
is authoritative for the18 version-target paths, local lock rebinding,
pre-version comparator retention and actual0.30.1 Go/Rust subset. This note adds
no new design scope or execution permission. Native activation and final source
readiness remain UNKNOWN until separately qualified; publication/tagging and
registry/configuration actions are not part of this package.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
