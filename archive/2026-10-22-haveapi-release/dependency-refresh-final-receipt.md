# Dependency refresh source handoff

All intended source is frozen at base/head `090a188cb4ef3477324718627f4ae3415d1c0975`
in `haveapi-dependency-refresh`, branch
`2026-10-22-haveapi-release-dependency-refresh`. Source ownership is returned to
the lead. No setup, compiler, test or generation operation remains active.
Owner3 must wait for the lead's explicit comparison grant. Owner0 retains sole
Git/index/hooks ownership. Release0.30.1 and new default integration remain held.

The package selects Rollup4.65.0, TypeScript6.0.3, Markdown15.0.3 and anchor10.0.0,
with only JSDoc-scoped direct-reference overrides. Linkify resolves6.1.0. Other
direct dependency ranges and runtime dependencies stay unchanged. The compiler
compatibility setting preserves existing ES5/node10 configurations without
relaxing strict checks. New tests exercise actual JSDoc Markdown/plugin behavior,
repeated independent heading renders and final links/navigation.

## Exact source and output inventory

- `clients/js/README.md` — SHA256 `4e90056eacb5709821497d2fa69f5e1245f557e27cbdb9a3e356a82a9086c8e1`
- `clients/js/package-lock.json` — SHA256 `47b427cc1170c7583c922c5bc924a5fb21eb177fc62875720554c14cc6836408`
- `clients/js/package.json` — SHA256 `d51d94c2c33ff8f631064d095f77f93c5624a2e9c362075251bc37d691723fb5`
- `clients/js/test/README.md` — SHA256 `c0ba78931fc34f5fde68fb2c2ee6d74d5d087bc514021884a47d3a159ca56549`
- `clients/js/test/compatibility/jsdoc_markdown.spec.cjs` — SHA256 `fc82cf4069402b458c2f701f123b674a2c533273b7fe75fe39bcdc1f2695a7bc`
- `clients/js/test/compatibility/module_graph.spec.cjs` — SHA256 `863e266f227fa3adf0f6f9d1ef803c833e7d4f84fcf2fbbd4c87610e4c79a930`
- `clients/js/test/types/callback.tsconfig.json` — SHA256 `db13ae7cec42755f0a667de1e958ad04547b8ba8d7970e5846721c10e57b48f4`
- `clients/js/tsconfig.json` — SHA256 `2be3366bfb01bcbd44ba7d0ca6c7c94549c9479feb24abe997be0d5b2a7b747d`
- `servers/ruby/spec/client_examples/dynamic_js_spec.rb` — SHA256 `8562e3278ce80be15e8342a4b670b0b5924f4f414ed1b211c9779dc09f8410de`
- `utils/release/artifacts.rb` — SHA256 `dee7f9a0c11980dda48e2eb5da23b336c1e850fa2cef9168dac717ab5d3e7c3c`

The inventory contains **10 authored paths**: nine tracked modifications and
one new test. All **47 generated outputs** (bundle and46 declarations) are
byte-identical to090a after both normal builds. There is **no generated delta
or generated commit**. Both final lead-prose hashes match the yielded values.
`dependency-refresh-final-inventory.json` retains every candidate file's mode,
Git blob identity and SHA256, plus original base identities and the47 outputs.

All-file count: **765**. Canonical all-file inventory SHA256:
`3d4002b1fbf484ce93b10311ec7049822e375708b7ca2fd5348cb385568539a2`. Index is empty; `git diff --check` passes.

## Quick evidence

- `dependency-refresh-js-quick.log`:105/0 (compatibility55, async39, resources11),
  strict typecheck/public and deep declarations, ES5 parse, UMD/AMD/CommonJS
  loaders, module graph, bundled helper license, real JSDoc and Markdown checks.
- `dependency-refresh-npm-graph.json`, `dependency-refresh-graph-inventory.json`:
  peer graph exit0, no invalid peers, all locked tarball integrities retained;
 239 package entries plus root, no stale Markdown12/linkify3 runtime chain.
- `dependency-refresh-dist-first.json`, `dependency-refresh-determinism.log`
  and `.json`: two builds match each other and exact090a for all47 outputs.
- `dependency-refresh-release-quick.log`: release-check passed; original
 170-example failure retained for initially absent local prerequisites.
- `dependency-refresh-release-failed-example.log`: subsequent focused failure
  retained for missing own Rust component bundle.
- `dependency-refresh-ruby-style.log`: both changed Ruby files pass style and syntax.
- `dependency-refresh-release-recovery-focused.log`: focused fixture1/0, run once
  after corrected setup. `dependency-refresh-release-recovery-full.log`:
 170/0 plus Python artifacts6/0. Results/commands/timing are in
  `dependency-refresh-release-recovery-result.json`.

The raw outer recovery guard exit98 is retained: the Python tests created one
nonignored bytecode file, with zero changed/removed inputs and unchanged locks.
The lead authorized moving only that exact file into session evidence; its
regular/nonsymlink identity, source-timestamp/size match and preserved SHA are in
`dependency-refresh-generated-cache-relocation.json`. No directories or other
files were removed. Final nonignored inventory now contains only intended source.
No test was repeated for this generated-file relocation.

## Setup evidence and rationale

`dependency-refresh-npm-setup/` retains the isolated fresh Node24.21.0/npm11.19.0
setup. The Rust prerequisite first failed at Prism because the session JSON
export retained derivation-only `NIX_ENFORCE_PURITY=1`; the wrapper discarded
its absolute local include path. The complete cached150-file payload matched
the committed and official gem checksum. `dependency-refresh-rust-bundle-setup/`
retains original scripts/logs/exit5 and bounded diagnosis/official metadata.

The separately granted correction in `dependency-refresh-rust-bundle-recovery/`
passed once in27.93s with `NIX_ENFORCE_PURITY=0` scoped only to frozen install,
matching the root flake's existing local-Prism-header accommodation. Ruby store
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11` and compiler wrapper
`/nix/store/r5ri78axx1qggkjq3vawywlzglg70b5w-gcc-wrapper-16.2.0` were explicit.
Bundler4.0.23, new own/nondefault Fiddle1.1.8 and bundle check passed. No native
borrowing, dependency resolution/change, source/flake/config/lock change or
normal automatic shell hook was used. Fresh utility effective Luna/low/full-access
identity receipts are preserved for both attempts.

Next: lead accepts this inventory, grants owner3's independent read-only check
and coordinates owner0's scoped hooked commit. Retained reviewer0's committed
final review precedes longer JS/server/installed-npm verification. No new
release or default-integration approval is inferred.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
