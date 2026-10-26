# Verification preparation

Prepared by implementer0 on 2026-10-24. Dependency setup window is relinquished.
The lead accepted final independent review with no findings and authorized the
revised serial batch. Fresh operation-scoped watcher `final_suites_watcher`
completed it successfully in 32 seconds, exit 0. The utility slot is relinquished
for benchmark verification. It performed no CI monitoring or retries.
The revised batch is bound to reviewed head
`b85ec364057f536940d689b09e612512ffffaf82`, Git tree
`aaa082cae86f0a24559333213ab959729fb37494`, in
[the prepared source/input receipt](post-review-prepared-inputs.json).

## Completed post-review result

- Full server suite: 465 examples, 0 failures, seed 37216.
- Full Rust generator unit suite: 147 examples, 0 failures, seed 46673.
- Documentation highlighter and tab asset checks: passed.
- [Complete combined log](post-review-suites.log), [exact exit status](post-review-suites.exit),
  [post-command source/input and result receipt](post-review-results.json).

The exact reviewed HEAD/tree remained unchanged, the worktree/index remained
clean, and every prepared manifest/local-lock hash plus JavaScript source/dist
hash matched after execution. No source/Git/index mutation or dependency install
was performed. Full server output includes the exception-mailer fixture's
deliberately raised diagnostic; its suite still finished with zero failures.
No benchmark, CI, deployment, release or integration result is claimed here.

## Prepared inputs

The approved command ran once in a fresh pinned `gpt-6-luna`/`low` watcher:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c 'cd clients/js && npm install --no-audit --no-fund && npm run build'
```

It passed in 20 seconds, installed 215 packages and generated the JavaScript
bundle/declarations. The flag suppresses redundant dependency installation in
the already prepared top-level shell; it disables no checks.

- Start HEAD: `de799b595d04e880d092b3e5ef47bce2f4587130`.
- End HEAD: `50792e1dee743558e69423e1555816e450cfe6c7` after concurrent package D commit.
- [Full command output](js-preparation.log); [exit status](js-preparation.exit).
- [Before inventory](js-preparation-before.json); [after inventory](js-preparation-after.json).
- [Runtime store paths and complete npm tree](verification-runtime-and-npm-tree.txt).

All 47 tracked `clients/js/dist` files reproduced exactly. Recorded JavaScript
build sources, Nix inputs and Ruby locks remained byte-identical. The worktree
was clean afterward. Only the new ignored npm lock changed the input inventory.
Despite the broad ignore rule, the repository currently tracks its JS dist
files; future builds must preserve or report any drift rather than discard it.

`clients/js/node_modules`, `clients/js/build` and the local library npm lock are
ignored disposable inputs owned by this session's HaveAPI worktree. Existing
ignored top-level/server/Rust gem homes and locks remain prepared. No tracked
dependency, source or Git/index mutation was made by this preparation package.

Retained lock SHA-256 values:

| Local input | SHA-256 | Retained copy |
| --- | --- | --- |
| `Gemfile.lock` | `0a48c3e68d0b78caf945cb5a0430d13841ee140eb1bdca5734d823617a42afe6` | [root bundle](verification-Gemfile.lock) |
| `servers/ruby/Gemfile.lock` | `fdc5129f60f9ed2f6a56fbf7f9483af5d6a003fedb13a93e895e9cab87193b52` | [server bundle](verification-servers-ruby-Gemfile.lock) |
| `clients/rust/Gemfile.lock` | `53b94ab0ef92f5dccfd413eb1e313ed65868f1e2ba41af8b95ce6e62ae8d447f` | [Rust generator bundle](verification-clients-rust-Gemfile.lock) |
| `clients/js/package-lock.json` | `67db5e891ea2e1b3e66bae8ffa38e05c1129863ae6203e4495261d6a51847f12` | [JS resolution](verification-clients-js-package-lock.json) |

`flake.lock` SHA-256:
`a52bdf3a3b9a069175d3af298234c3cf7adeba54540833eed6ad902e9ccc0a64`.
Its nixpkgs revision is `02c087f3fe673c9e317f206a627cb6b910336dbe`, NAR hash
`sha256-IoNisKcGbUjdd45qCqywGMCYmZ5EnkxezvLII0FWwNA=`.
The resolved top-level tools include Ruby 3.4.11, Node 24.21.0, npm 11.19.0,
rustfmt 1.10.0, PHP 8.3.35 and Python 3.11.17. Complete exact store paths are
retained in the runtime receipt above.

## Exact proposed post-review checks

From the HaveAPI worktree root, with a fresh final head and the retained inputs:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c 'make doc && cd servers/ruby && bundle exec rspec'
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make test-rust-unit
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make test-documentation-assets
```

The lead refined this to one fresh operation-scoped watcher with this serial,
stop-on-failure command, avoiding duplicate execution of the server subset:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c 'make doc && (cd servers/ruby && bundle exec rspec) && make test-rust-unit && make test-documentation-assets'
```

The pre-launch check passed for exact HEAD/tree, clean source and every prepared
manifest/local-lock hash, plus the prepared JavaScript source and dist hashes.
On a subsequent run, check these again against the prepared receipt. Stop and
collect evidence on failure; do not rerun or edit source without diagnosis and
coordination with the owning package. Retain full logs, exact exit status and
post-command worktree state.

The server suite needs the prepared JS TypeScript compiler, Node declarations
and emitted client declarations, plus the Node/Python/PHP/Bash tools in the
top-level shell. It includes packaged-server documentation checks, so `make doc`
must precede it. No Python venv is needed for ordinary server spec discovery.

`make test-rust-unit` clears Bundler runtime variables and sets the separate Rust
gem home/path and Gemfile. The suite uses rustfmt but invokes no Cargo build or
listening server. Do not substitute ambient Ruby for the Nix interpreter.

The prepared JS build/declarations have already passed and reproduced tracked
outputs exactly. The full server suite includes all client-example and
documentation specs, so `make test-documentation` would repeat that subset and
is unnecessary in this batch. `make test-documentation-assets` executes the
highlighter and tab Node checks. They read checked-in assets and do not require
`utils/highlight/node_modules`. The separate asset reproducibility workflow
installs those dependencies and runs `npm run check`, which is outside this
requested batch. The supplemental `make test-documentation-python` requires a
prepared Python environment and is likewise outside the requested batch.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/>.
