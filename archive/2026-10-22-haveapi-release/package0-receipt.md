# Package0 completion receipt

Final branch: `2026-10-22-haveapi-release`, HaveAPI worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi`.
Prepared for the lead's final independent review; no publication, official
release refs, default integration or deployment performed.

## Exact final range and history

Base and freshly fetched `origin/master`:
`a32b15e379f44fc6dae4b15ef4ec17a142e5f465`.
SSH `git ls-remote origin refs/heads/master` independently returned the same
target after fetch. No upstream rebase was needed.

Final head: `09024e01251a1334780b73f14218266e94706192`.
Final tree: `3bd9df27413a1794bad5d8db27faca551cc3f79a`.

The pre-reorder head `123364c69f1daf562405ecd494ea6575f3515945` has the same tree.
`git diff --exit-code <old-head> <final-head>` passed. The manual interactive
rebase was conflict-free, with hooks enabled, folding both temporary fixups into
their owning source/documentation commits and ordering source before its tests.

| Final commit | Purpose |
| --- | --- |
| `70180e6fb290a59d49ce804bc3ac8417a3276f0a` | Rust release build/catalog/artifact/version/isolated setup contract |
| `c305117fc50274fc9b14e881dd0ba485f9542735` | Preserve released structured examples |
| `19730572d3a15d7d031bc87cac02bfe415ade784` | Preserve native example syntax tests/rendering and server tools |
| `62cb54e4a6c32b65b9d127334b26f0d73765d433` | Preserve recursive PHP example values |
| `db91afadea891520b08d5df47c8ea14fc1ba57bb` | Publication contract, registry/release docs and Rust path triggers; includes lead-approved setup prerequisite |
| `67dd584d3d0a11b132a1f6e754137de675f48001` | Separate upstream PyPA security/action refresh |
| `09024e01251a1334780b73f14218266e94706192` | One coherent shared 0.30.0 metadata/changelog commit |

Preservation provenance in the three messages includes released commits
`9b53aa87aec7a8d9c61eee2716e5520b3ecf743c`,
`fda2e33d32c249310812730b6b3096b99778918d`, and
`f82ca890683d518496fdb57dc1c040589a0d585b`, together with their original source
SHAs. All nine affected server source/spec paths compare exactly to `v0.29.12`.
The released server-shell Node/PHP additions coexist with the root Rust tools.

One shared version stream is consolidated; tracked Rust lock changes contain
only five local-version replacements. No registry dependency/channel pin churn,
superseded source approaches, temporary compatibility paths, or migrations
remain. There are no database migrations in this branch. The three already
released preservation changes remain separately reviewable with their genuine
release/provenance boundary.

Full evidence: [history](final-history.txt), [final diff](final-diff.patch),
[stat](final-diff-stat.txt), [old series](history-before-reorder.txt), and
[reorder range-diff](history-range-diff.txt). Final diff has 39 paths,
1080 additions and 75 deletions. Session comparison was captured for the exact
final base/head.

## Implementation and quick verification

The central GEMS catalog now supplies the fourth gem to builds, inspection,
publication/retries and draft assets. Rust metadata/version/dependency/lock
agreement is enforced. Manifest provenance includes Rust generator/Cargo locks
and cargo/rustc/rustfmt versions. Artifact inspection checks the complete
generator payload against source, including templates/runtime bytes and absence
of harness/fixtures. A standalone extracted-artifact smoke runs offline CLI
generation/check and compares the copied runtime, without checkout code fallback.

Root release preparation/tests/builds use a shared Makefile Rust isolation
expression; component setup and smoke use explicit component-home plus Ruby
default gem paths. Root shell includes Rust compiler/formatter/native tools.
The private runtime harness remains version 0.1.0 with `publish = false`.

Passed before reorder, whose final tree is identical:

- `make release-test`: 78 Ruby examples, six Python artifact tests.
- `make test-rust-unit`: 28 examples.
- Rust launcher contracts: 19 examples across `bundle_activation_spec.rb`,
  `fixture_actions_spec.rb`, and `fixture_contract_spec.rb`.
- After `make doc`, server documentation/examples and native renderer syntax
  specs: 12 examples.
- Own Ruby style/syntax, shell syntax and diff whitespace checks.
- Version bump fixture verifies npm nested dependency bytes, exactly five Rust
  local version substitutions, and preservation of the root lockfile.

At exact final head: `make release-check` and
`bundle exec overcommit --diff origin/master` passed (HaveapiI18n,
PythonChecks, PhpCsFixer, RuboCop). Every original/fixup commit used declared
hooks; no hook bypass was used. One alignment-only hook rejection was fixed
before retry. Commit-message width warnings were advisory; lines obey the
workspace's 80-character limit.

## Diagnosed setup failures and repair

- The initial disposable version regression inherited root `BUNDLE_LOCKFILE`
  under `bundle exec`, redirecting writes to ignored root `Gemfile.lock`.
  Cleared lock/setup variables in Rust commands, restored only that owned
  ignored root lock via `bundle lock --local`, and added a root-lock
  nonmutation assertion. Tracked source/metadata were unaffected.
- Initial component installation reused `~/.gem` and left dependencies absent
  when the existing launcher restricted GEM_PATH. Corrected supported Nix and
  Makefile setup to explicitly use component home plus Ruby defaults, then
  reran the documented `nix develop .#client-rust -c true`. Setup passed in
  13 seconds and all 19 launcher checks then passed without local exceptions.
- RubyGems caches loaded gem specifications; mutable test fixtures now duplicate
  the specification so missing-file tests cannot contaminate later fixtures.

Fresh policy watcher logs: [initial quick setup](package0-quick-deps.log),
[server bundle](package0b-server-deps.log),
[corrected isolated Rust setup](package0-isolated-rust-deps.log).
All watchers used pinned Luna/low utility policy and full-access/never.
No watcher, setup, Git or hook command remains running.

## Recommended post-review batch

Lead should launch a fresh watcher from the canonical HaveAPI worktree, with
exact final head above and the declared top-level Nix shell. Root lint/spec
bundle, JS dependencies, server bundle and isolated Rust bundle are prepared;
remaining component dependencies should still be prepared through release-deps.
No root `dist` release build has been run. Confirm it is empty before starting.

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euo pipefail -c '
  make release-deps
  make release
  make test
  cargo clippy --locked --manifest-path clients/rust/runtime/Cargo.toml --all-targets --all-features -- -D warnings
  ruby utils/release/cli.rb smoke-npm dist
  (cd clients/python && uv run --locked python utils/package_smoke.py)
  ruby utils/release/cli.rb verify dist
'
```

`make release` builds/inspects the full catalog, writes its manifest, and runs
the extracted Rust artifact smoke automatically. `make test` already runs the
Rust unit suite, both runtime feature configurations, and generated-client
acceptance; do not duplicate those same commands. Clippy is the separate check
from the existing runtime guide. MSRV-specific acceptance remains a distinct
existing support check if the lead selects it; the root development compiler is
newer than 1.95. No downstream real-vpsAdmin campaign or registry action belongs
in this batch.

Git ownership returns to the lead for final review. Tracked working tree/index
are clean; only known generated `utils/release/__pycache__/` is untracked and
preserved. No feature push performed, as directed. Session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
