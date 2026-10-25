# Rust library-lockfile support

Source and assigned focused checks are complete and yielded in the shared registered `haveapi-library-lockfiles` worktree,
branch `2026-10-24-haveapi-library-lockfiles`, base
`7ac977a26080d45d44b6608aafad2cadd2ec7f81` / tree
`d92f9ecef3854b11d4f4d26106d524ff2d72758d`. The source root, branch and base
were independently checked after owner0 readiness. Binding/env and same-session
workspace-write access matched. Owner0 retains all Git/index/shared release
files, untracking and ignore-rule ownership.

The five assigned paths are recorded in [source-inventory.json](source-inventory.json);
the [original baseline](baseline.json) and original bytes remain available.
Only the gemspec file inventory and focused dependency/package specs change
behavior. The gemspec keeps `Gemfile.lock` as an unconditional required entry:
it can load without a local lock for fresh Bundler preparation or restored
inspection, while normal RubyGems packaging rejects a missing file. The focused
positive spec builds a disposable gem with the actual prepared lock and checks
its extracted bytes and runtime contents. The negative spec loads a disposable
source without a lock and requires packaging failure.

The Fiddle spec retains the existing supported/lower-bound negative assertions.
Its activation assertion accepts only the actual prepared lock version that
satisfies the unchanged gemspec range, equals the activated version and is
nondefault. No constraints or default-gem fallback changed.

README/generation/releasing describe ordinary local Bundler preparation and
retaining actual resolved build inputs, the required packaged provenance lock,
and the library/application lockfile distinction. Lead prose pass accepted all
three sections unchanged. Private `runtime/Cargo.lock` stays tracked; generation
ownership format, generator/runtime/templates and API remain unchanged.
32 protected Rust/toolchain inputs match the baseline.

The accepted fresh own Rust environment is recorded in
[environment-inputs.json](environment-inputs.json): Ruby3.4.11,
Bundler4.0.23, nondefault Fiddle1.1.8, Tomlrb2.0.5 and both local project
specs0.30.0. The prepared ignored component lock remains
`7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4`.
The saved with-env.py wrapper selects this worktree's own `.gems`, native tools
and Gemfile. It does not install dependencies or borrow another bundle.

Final known quick results (exact rooted argv/cwd/exit/timings in each result):

- [Focused dependency/package spec](01-focused-dependency-after-style-fix.log):
  4 examples/0 failures, seed9208, exit0/1.041s.
- [Explicit root-config RuboCop](02-root-style-after-style-fix.log):
  2 files/no offenses, exit0/3.847s.
- [Gemspec syntax](03-syntax-gemspec-after-style-fix.log): Syntax OK,
  exit0/.098s.
- [Dependency-spec syntax](04-syntax-dependency.log): Syntax OK,
  exit0/.108s. This file did not change after that syntax check.

The first focused run also passed4/0 (seed54371). The original root style check
failed one continued-call indentation in the gemspec; only whitespace was
corrected, then affected checks passed. The original failed style log/result
and pre-fix gemspec are preserved. No rule/config bypass or relaxation occurred.
Packaging tests emit normal Ruby constant-redefinition warnings while loading
disposable copies of version.rb; the version value remains unchanged.

[Final inventory](final-inventory.json) records all5 source hashes, the canonical
files-map digest, actual commands/results and log hashes. It supersedes the
pre-check source inventory only for the gemspec whitespace correction. All3
lead-approved docs and the dependency spec remain byte-identical to that draft.
[Final patch](final.patch) compares only the five owned paths with their baseline.
32 protected inputs and all gemspec requirements remain unchanged.
No generation/Cargo/MSRV/model campaign, dependency installation or Git/index
operation was performed by implementer3. No command remains active. Owner0 owns
the combined source commit and subsequent gates.


Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
