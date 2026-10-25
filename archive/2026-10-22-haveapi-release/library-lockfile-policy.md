# Library lockfile policy: findings and proposed removal

**Accepted for implementation, 2026-10-24:** the user explicitly directed actual
lockfile removal, HaveAPI master integration, backport to 0.30 and release of
0.30.1. Lead accepted this brief's original SHA-256
`95d290d686ab217c6905dbb677e2c1672584cbd92cec80feb4e4631cf17a36b6` without a further
design gate. Owner0 owns the shared worktree from master7ac, Git/shared release
files; owner1 Python, owner2 JS, owner3 Rust. This authority supersedes the
preparation-only and publication-hold wording retained below as history. The
technical contract and required verification remain unchanged. No deployment
or lifecycle action is authorized.

2026-10-24. The user selected **no library lockfiles tracked in Git; application
lockfiles are appropriate**, then explicitly requested that HaveAPI instructions
say so. Owner0's root `AGENTS.md` instruction edit is an independent, separately
accepted package. The removal/workflow design below is **preparation only**,
pending lead routing. Architect has edited only this record and its design link.
It does not authorize additional source work, integration, setup or publication.

## Facts at the reviewed candidate

Inspected HaveAPI `91d4293e0c346f25aa04a6252e2b5ad0f9070263` in our
`haveapi-0-30-1` worktree. No Dependabot YAML exists in that canonical tree.
GitHub automated security updates are a possible source of PRs; current settings
were not read. Retained [PR3 evidence](dependency-refresh-addendum.md) identifies
an advisory-related Markdown/linkify update to the JS lock only. Removing locks
will not guarantee that no dependency/security PR can arise from manifests.
No Dependabot configuration or settings change belongs to this package.

| File | Actual role | Proposed policy |
| --- | --- | --- |
| `clients/js/package-lock.json` | JS library build/test tools plus runtime dependency resolution; 239 external records | Untrack; keep existing ignore rule; resolve a local lock during preparation |
| `clients/python/uv.lock` | Python library's test/runtime environment; 26 external records across supported Python versions | Untrack and ignore locally; prepare before locked checks |
| `clients/rust/Gemfile.lock` | Ruby Rust-generator library/tool dependency graph, including native Fiddle; also embedded generation provenance | Untrack; remove root ignore exception; retain actual locally resolved input for a build |
| `clients/rust/runtime/Cargo.lock` | Private `haveapi-runtime-tests`, `publish = false`; 158 external records | Retain: application/test harness, not a published Rust library |
| `utils/highlight/package-lock.json`, `flake.lock` | Documentation build application and workspace toolchain inputs | Retain unchanged |

Older Ruby/Go clients use ordinary Bundler and ignored `Gemfile.lock`; PHP uses
Composer and ignored `composer.lock`. Their gemspec/Composer dependency ranges
remain the consumer contract. The release manifest already records these
untracked resolved locks alongside tracked ones. Thus retaining exact build
inputs does not require committing them.

Statically inspected original candidate artifacts under
`release-0-30-1-candidate-artifact-download-91d4293e/retained/`. Their manifest
binds source91 and run `40102030371`; each SHA below matches that manifest:

| Artifact | SHA-256 | Locks actually shipped |
| --- | --- | --- |
| npm `haveapi-client-0.30.1.tgz` | `c3327b59f6badc8ec910c36ff74a6b8573a4784d5e06f61ffe637aa235d2a857` | None |
| Python sdist | `9ae8d66e41ecd61c5dd92543b3fcc95e37c56541d92d0970732f32cf469decde` | None |
| Python wheel | `3d44949f4d545c07ea54fbb35229e74a084d5324da89866e6d4d7a91b95eb0c0` | None |
| Rust-generator gem | `e236fe7715fcf48d657fec6bda2a06d19b9a59a77abb45b5f09c4b541170f4ae` | Ruby `Gemfile.lock`, never private `Cargo.lock` |

The Ruby lock shipped with the generator is data, not a RubyGems instruction to
force downstream gem versions. The generator hashes that file into its ownership
manifest (`generator.rb:63`). The npm/Python libraries use their manifest runtime
ranges in downstream installations. Generated Rust libraries use their own
Cargo manifests; the HaveAPI generator does not generate a Cargo.lock. Current
generation docs instruct consumers to commit their lock; update that advice for
libraries, leaving application/harness policy explicit. No downstream repository
edit or regeneration is implied here.

The concrete tradeoff is accepting newly resolved compatible dependencies on a
fresh checkout. Tests and built JS may consequently differ between independent
builds of one commit. Keep exact tools/constraints, actual resolved locks and
original release artifacts as evidence; do not claim commit-only reproducibility.
Nix pins tools, not every npm/PyPI/RubyGems resolution performed by shell hooks.

## Proposed command and compatibility contract

1. **Prepare once with native package managers.** JS uses
   `npm install --no-audit --no-fund`; Python uses `uv sync`; the Rust generator
   uses ordinary `bundle install` with its owning Gemfile/Ruby. These create
   ignored local locks on a fresh checkout and normally reuse compatible ones
   on an existing checkout. Do not add `--upgrade`, alter constraints, import old
   locked versions as new pins, or seed dummy locks. Native gems stay bound to
   the selected Ruby/platform and declared libffi inputs.
2. **Consume that prepared resolution.** Retain Python `uv run --locked` and
   `uv sync --locked` in checks/hooks after explicit preparation. Keep
   `bundle exec`, actual compiler/ES5/declaration/loader tests, and retained
   Cargo harness `--locked` commands. JS's clean-checkout preparation cannot
   start with `npm ci`; after a local lock exists, ci remains valid for replay.
   No update/resolution command runs between a build's prepared-input capture
   and its final checks. Do not run dependency installation with publishing
   credentials or during original-artifact restoration.
3. **Versioning uses prepared local inputs.** Document JS/Python/Rust preparation
   before the maintained `make version`. Preserve its local npm root-version
   update, native `uv lock` and `bundle lock --local` behavior, checking that
   external records remain unchanged. The three local lock updates cease to be
   Git changes: the existing 18 version paths become 15 tracked paths, plus
   CHANGELOG (16 intended tracked metadata paths), subject to owner0's exact
   inventory. No product dependency requirement changes.
4. **Retain Rust packaging/provenance.** Keep the actual prepared Ruby lock in
   the generator gem and retain its ownership-manifest hash. This is build
   provenance, not Git tracking or downstream dependency enforcement. Require
   it explicitly for packaging; do not silently omit it. This avoids changing
   ownership format, generated APIs, model names/routes or existing SDK policy
   solely to stop tracking a library lock. The hash identifies the packaged
   generator input, not necessarily a downstream user's entire executing bundle.

Python CI must prepare with `uv sync` before existing locked commands (both the
check and integration jobs); key its cache from `pyproject.toml`, not a missing
tracked uv.lock. Contributing instructions use the same two phases. Hooks still
fail on an unprepared/mismatched environment rather than installing silently.
Keep Ruff's exact declared constraint and Nix-version comparison. Remove the
now-untracked lock from the hook's tracked-file trigger list, not the hook.
JS shared server CI replaces its initial library `npm ci` with native install;
the highlighter's application ci remains. Existing JS CI already uses install.

## Required release separation

Two existing assumptions must change together; simply deleting files breaks a
clean build and original-artifact recovery:

- `Artifacts#check`/CLI `check-clean` runs before `release-deps`. Make that an
  authored-source/version/changelog/tag/cleanliness check independent of absent
  local library locks. Move the existing JS/Rust lock identity/version checks
  into an explicit prepared-input method/CLI **`check-inputs`**. Require it from
  maintained `make release-check`, `build.sh` before packaging, and manifest
  creation. Source-only workflow preflight remains valid on a fresh checkout.
  This relocates checks; it does not accept mismatched prepared input.
- `Artifacts#verify` runs in a fresh tools-only publishing/restoration checkout.
  It must validate the packaged Rust Ruby lock against the **original retained
  `dependency_locks['clients/rust/Gemfile.lock']`**, not an absent or newly
  resolved checkout file. Pass explicit lock evidence through existing package
  inspection methods: build inspection requires local resolved evidence;
  restored verification requires retained evidence. Enumerate authored Rust
  package files from source and require Gemfile.lock separately. Retain exact
  file set, identity, payload hash, executable, dependency and byte comparisons.
  Missing/malformed retained lock evidence or a mismatched packaged lock fails.

Keep all nine current `dependency_locks` records in release manifests. They
are available after ordinary preparation, including older clients' ignored
locks. Do not replace missing values with null/empty data or resolve anything
to verify a saved release. No manifest schema change or registry/publisher
retry-policy change is needed. Existing published source/tags/artifacts and
their original helpers remain immutable.

## File packages and ownership for later routing

Owner0 retains all current source/Git authority; no removal package starts
until lead routes it. If the lead delegates application edits later, these are
independent boundaries; one owner must own shared release files.

| Package | Exact owned paths and responsibility |
| --- | --- |
| Separate instruction edit | Owner0 only: root `AGENTS.md`, concise library/application rule; independent of removal acceptance |
| Tracking/setup/release coordination | `.gitignore`, `Makefile`, `utils/release/{artifacts.rb,cli.rb,build.sh}`, `utils/release/spec/release_spec.rb`, `doc/agent-instructions/{development.md,releases.md}`; untrack the three library locks while preserving local build inputs |
| JS | `.github/workflows/_ruby-rspec.yml`, `clients/js/{README.md,test/README.md,test/compatibility/build_helpers.spec.cjs}` only where changed setup wording/assertions require it; preserve manifest constraints and graph oracle |
| Python | `.github/workflows/clients-python-tests.yml`, `.overcommit.yml`, `clients/python/{CONTRIBUTING.md,utils/run_ruff.py}` for initial-sync wording; `utils/check.sh` and hook implementation retain their locked checks after preparation |
| Rust | `clients/rust/{README.md,docs/generation.md,docs/releasing.md,haveapi-rust-client.gemspec,spec/unit/dependency_spec.rb}`; enforce required packaging input, clarify local lock and generated-library policy |

For Rust's dependency spec, replace the incidental equality to resolved Fiddle
1.1.8 with: resolved version satisfies the unchanged gemspec requirement,
activated version equals that prepared lock, and it is not Ruby's default gem.
Keep the existing lower-bound negative assertion. Do not force a fresh allowed
resolution to masquerade as 1.1.8.

The disposable version-bump spec copies tracked source today; explicitly copy
the **actual prepared** three local locks into that disposable source as test
inputs. Assert unchanged external graphs (including Python's platform records),
unchanged root/source locks, updated local identities and continued mismatch
rejection. Do not weaken the test by omitting locked inputs or substituting a
handwritten dependency graph. Existing synthetic unit fixtures remain suitable
for isolated parser/error cases.

No generator/runtime/template or dependency-constraint changes are intended.
The old fixed-4dc0 model-equivalence comparison is historical evidence and is
not a comparator for a newly resolved Ruby graph. Do not relax it. Where exact
generator equivalence is needed, use the same qualified local lock as an
explicit input on both sides and compare generated API/runtime bytes; retain
the actual differing build/provenance identities honestly.

## Verification, history and recovery gates

Quick acceptance before committed final review: tracked/ignored classification;
source-only check from a clean fixture without the three library locks;
prepared-input mismatch/missing controls; real disposable make-version graph
preservation; release Ruby/Python helper suites; original-artifact verification
from a fixture without local library locks, including corrupt/missing retained
Ruby-lock negatives; focused changed Rust dependency/package specs and hooks.
Tests must demonstrate genuine prepared locks and cold source behavior. Native
dependency setup is a separate prerequisite, not performed by this design.

After committed full-range independent review, obtain **new affected-candidate
evidence**: clean preparation from the unlocked library manifests, full JS
build/ES5/docs/loader/declaration coverage, Python format/type/unit/integration
and installed wheel/sdist checks, Rust generator/package smoke and runtime
checks as affected by the actual newly resolved inputs. The retained private
Cargo lock remains unchanged; reuse prior compiler/MSRV evidence only with
exact relevant input proof. A single ordinary feature release workflow can
supply the full build/test/package/smoke campaign; do not dispatch duplicate
local and CI campaigns. Verify original new artifacts and lock provenance,
including restored tools-only verification, before candidate acceptance.
91's artifacts remain evidence for 91, not freshness for the changed head.

Implement first on development 0.30.0 source in a new own feature worktree
(proposed `haveapi-library-lockfiles`), based on owner0's fresh master proof and
including the separately reviewed instruction rule. Preserve merged master67,
all required source refs and the published patch91 feature. Consolidate each
unpublished implementation stream before final review. Lead routes checks and
integration under the approved HaveAPI/master scope; this preparation record
does not itself lift the current hold.

Prefer a **separate new patch candidate** from the retained pre-version source
`8591394e13144431b27ecb366aae2b7b77a94e2c`, if owner0 proves it extends the fresh
supported release target. Cherry-pick the accepted instruction/removal commits
with genuine `-x` provenance, then prepare a new final `Version 0.30.1` commit
with lead-owned changelog/date. Do not append changes after an obsolete Version
commit, replay already present fixes, force-push patch91, or rewrite merged
history. If the release target moved, owner0 returns the exact ancestry before
choosing the successor base. Keep patch91 and its artifacts as the old reviewed
candidate, with a clear old/new range and input-equivalence report.

Failures stop the affected setup/test/release phase and retain its resolved
locks and artifacts. No automatic dependency upgrade, weaker test, lost native
input provenance, or rebuilding an already accepted registry version is an
allowed recovery. There is no persisted-state migration or deployment change.
No tags, publication, downstream repository changes or lifecycle action are
authorized by this design.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
