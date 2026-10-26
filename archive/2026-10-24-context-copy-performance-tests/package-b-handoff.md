# Package B: selective Rust documentation normalization

Implementation committed as `82a7f8880663dfa9d8ad6cd67e981a5842dedf9c`, parent
`5003ded2a47db6b1637a3fef2fdd40474ea7de06`. All three assigned files are committed:

- `clients/rust/lib/haveapi/rust_client/documentation.rb`
- `clients/rust/spec/unit/documentation_spec.rb`
- `clients/rust/spec/unit/documentation_performance_spec.rb`

The adapter shallow-normalizes ancestor maps, preserving `to_s` key normalization
and last-insertion collisions, then recursively normalizes only selected action
or authentication-provider data. Credential selection preserves basic key
presence, public actions, token-before-OAuth preference and normalization of
compared header values. Authentication rendering compares the complete selected
provider description. There is no request cache or dependency on server Context;
mutable duck-typed contexts are read again on every render. Malformed selected
resource/action/auth-render provider shapes yield the existing unavailable
limitation rather than authorization. Basic credential key presence remains
accepted even for nil/false, matching the previous contract.

Both modes have behavioral regressions for mixed keys, collision insertion order,
provider equality, mutable description/sample/header freshness, stale parameter
shapes and frozen-adapter admin/member field/default/sample isolation. Public
render instrumentation counts every recursive normalize call, including scalar
leaves. The work fixture keeps ancestor width and selected inputs fixed while
unrelated nested resources, sibling actions and providers grow from size 1 to 64.
Successful output and limitations must remain identical with identical work.
Saved IR resolution still scans its own actions; this does not establish a bound
on complete rendering time independent of saved model size.

Package D owns durable adapter-guide updates. No schema, migration, persistent
format, client wire contract or deployment change. No deployment or integration
performed. The Git/index window was relinquished with an empty index after commit.

## Verification

- Prepared `nix develop .#client-rust` once through a fresh Luna/low watcher:
  exit 0, 46 seconds. [Setup log](rust-setup.log), [watcher result](rust-setup-watcher-result.txt).
- Focused candidate specs: 56 examples, 0 failures; 0.18 seconds in final run.
  [Candidate log](package-b-candidate-specs.log), [exit status](package-b-candidate-specs.exit).
- RuboCop on all three owned files: 3 files, no offenses. Diff whitespace check
  passed. Normal Nix/Overcommit pre-commit and commit-message hooks all passed
  without warnings. [Commit log](package-b-commit.log).
- Isolated original-adapter proof: obtained only the original adapter source with
  `git show 39909094649b1d14a23f00615775ca7136acf4fd:clients/rust/lib/haveapi/rust_client/documentation.rb`,
  loaded it into a separate Ruby process and ran the new performance spec against
  the unchanged prepared candidate dependencies. No checkout/source replacement.
  Expected exit 1: 8 examples, 8 failures, 9.59 seconds.
  [Baseline log](package-b-baseline-specs.log), [exit status](package-b-baseline-specs.exit).
  Original recursive work counts (small -> large): action+credentials
  404 -> 51,308; full selected-provider authentication 169 -> 19,258;
  stale action limitation 206 -> 25,658; unavailable provider 198 -> 25,650.
  This establishes defect sensitivity, not a measured request-speed improvement.
- Independent final review and long suites/campaigns remain lead-coordinated.

Runtime: `/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`.
Rust component bundle SHA-256:
`53b94ab0ef92f5dccfd413eb1e313ed65868f1e2ba41af8b95ce6e62ae8d447f`.
Flake lock SHA-256:
`a52bdf3a3b9a069175d3af298234c3cf7adeba54540833eed6ad902e9ccc0a64`.
Original adapter SHA-256:
`00583d7b2b4d1f7867b0bf10a8b568f1cdf9fceb749d5d153dd972bad55ca8ea`.

Prepared watcher catalog and native utility, matching the retained catalog digest
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`:

- `/nix/store/l9sc1ksacdkm7iij99ggyg87bqsp9n15-dev-workspace-0.2.0/share/dev-workspace/agent-teams.json`
- `/nix/store/l9sc1ksacdkm7iij99ggyg87bqsp9n15-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`

## Optional combined server/Rust environment

Verified both source libraries load together with the prepared Nix Ruby and gem
homes, including native `fiddle` 1.1.8 and `tomlrb` 2.0.5. From the repository root
inside the prepared top-level Nix environment, the equivalent reusable command is:

```sh
env -u RUBYOPT -u BUNDLE_GEMFILE -u BUNDLE_BIN_PATH \
  GEM_HOME="$PWD/.gems" \
  GEM_PATH="$PWD/.gems:$PWD/clients/rust/.gems:$(ruby -e 'puts Gem.default_dir')" \
  ruby -I servers/ruby/lib -I clients/ruby/lib -I clients/rust/lib \
  -e 'require "haveapi"; require "haveapi/rust_client/documentation"; puts "loaded"'
```

Later code must not invoke Bundler.setup and isolate the combined gems again.
No compiler, Cargo, network acquisition or dependency installation is part of the
adapter's render path.

Session remains open: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/>.
