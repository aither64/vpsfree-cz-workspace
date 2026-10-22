# Client fixture lock selection: committed owner receipt

The lead accepted the completed affected general/architecture review at exact
`a8ea3132e7efe601aaa8965afe648459b3dab5c5`, tree
`9a596258d912ca2075c36ded30d11b3984c656ae`: no findings, four-commit history
accepted, no obsolete fixes/repeated streams and no migrations. Source is frozen.
The fresh policy utility owns the separately prepared continuation; the owner
has not retried suites or installed Go fixture dependencies.

## Diagnosis and exact correction

The original post-review batch passed documentation and server RSpec, then
failed Ruby-client startup before any example. The helper discarded non-ready
child output, so its original log only reported `server did not start`.
A no-server nested `bundle check` reproduced the cause: Bundler 4 exported the
client's `BUNDLE_LOCKFILE`; the helper switched only `BUNDLE_GEMFILE` to the
server. Frozen Bundler compared that server Gemfile with the client lock and
exited with `Bundler::ProductionError` before readiness.

Matching server Gemfile/lock selectors passed the Ruby-client dependency check.
The same probe in the ordinary Go gem home showed the separate prerequisite:
server fixture gems were not installed there. These probes were dependency and
environment evidence, not passing suite results.

Fourth commit `a8ea3132e7efe601aaa8965afe648459b3dab5c5` adds exactly
`'BUNDLE_LOCKFILE' => "#{@gemfile}.lock"` next to the existing Gemfile selector
in each of:

- `clients/ruby/spec/support/test_server.rb`
- `clients/go/spec/support/test_server.rb`

There is no production client/protocol, startup/cleanup, parser, gem-home or Nix
source change. This corrects a latent baseline fixture assumption exposed by
Bundler 4; it remains a separate commit from the three dependency streams.
Ruby syntax passed for both files, native RuboCop reported no offenses in two
files, and normal HaveapiI18n/RuboCop/commit-message hooks passed.

An owned-process/listener inspection found no remaining failed fixture.
Recorded runner/step PIDs were absent. Three inaccessible-cwd own processes
were excluded through readable start metadata predating this check by months
or days. No cleanup or signal was needed. Original failure evidence is retained:

- `verification/dependency-refresh/postreview/03-ruby-client-rspec.log`
- `verification/dependency-refresh/ruby-client-startup-process-evidence.json`
- `verification/dependency-refresh/ruby-client-nested-bundle-diagnostic.log`
- `verification/dependency-refresh/ruby-go-paired-lock-diagnostic.log`
- `verification/dependency-refresh/fixture-lock-selector-quick.log`
- `verification/dependency-refresh/fixture-lock-selector-commit.log`

## Complete four-commit inventory

Base remains merged `c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`.
The original three commits remain exact ancestors:

1. `67ecb6797c2794113b078044395d7a2ed54dfda2` — Ruby 3.4 shell selection.
2. `7b7697e5c2dbb82d120cb5fa321d67b489d59a3e` — generated nixpkgs lock.
3. `18331877660ed0f736a25b29914756da89df0df9` — certifi/Ruff/note.
4. `a8ea3132e7efe601aaa8965afe648459b3dab5c5` — paired fixture selectors.

Full diff: seven files, +33/-33. Fixture-only delta: two lines replaced.
No history was rewritten, migration introduced or repeated pin update added.
All four ignored Gemfile lock hashes are preserved. Prior Python package
invariants remain unchanged: lock revision 5, project version 0.29.0 and 25
other package versions preserved.

| Separate evidence | SHA256 |
| --- | --- |
| `fixture-final-series.txt` | `8488710434420b0f098e8c9eccefa397f9978f49a808c003fb0611b9f041ee2c` |
| `fixture-final.diff` | `9b0459920b278d9b5b89ff47bbdad136a7a0e270d2d92e05eab66529ab99d13d` |
| `fixture-only.diff` | `ca48dca25cd68c0e50eedd26e375d688a245175cedd068ee6fd6ec1471f3e4b6` |

These files are under `verification/dependency-refresh/`. Original
`followup-series.txt`, `followup.diff`, `package-inventory.json`, owner receipt
and review files remain unchanged. The two helper lines do not alter successful
documentation/server RSpec source or tool inputs; the lead explicitly retained
checks 01 and 02. No flake, unit or full original review repetition is needed.

## Prepared continuation owned by the fresh utility

Command:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-dynamic-python-api-client/run-dependency-fixture-continuation.py
```

Runner SHA256:
`4c68433c76bb8c4c1812db8f2bc85316e444c82cf71135a784ca0454b0bfce36`.
Nested `prepare-go-server-fixture.sh` SHA256:
`d0c25c22d90df6be793a7d775d8d37cb39a033114c3fef8afdd1c4cb4c579895`.
Both were syntax-checked only by the owner; the lead subsequently launched the
fresh retained-policy Luna/low utility after affected-review acceptance.

The first step prepares the server bundle inside the ordinary declared Go gem
home. It supplies the server Gemfile and server lock together, keeps frozen
mode, and clears Go's contradictory `RUBYOPT` client-bundle preload only for
those explicit setup/load commands. The scoped native-install purity setting
matches the root flake's existing Prism-header build contract. No gem-home
override, dependency resolution upgrade or Nix source coupling is introduced.
All four lock hashes and exact source/claim are checked before and afterward.

The remaining steps are only Ruby-client RSpec, Go RSpec, Python generic/Rack,
standalone package smoke, release metadata check and release tests. Exact-head,
clean-source, held-claim and frozen-lock guards run outside contaminated Nix Ruby
activation before each check. Bytecode remains disabled. New logs and atomic
per-step/overall statuses live under
`verification/dependency-refresh/postreview-fixture-continuation/`; old logs
and statuses are not overwritten. The batch fails fast and does not retry.

The utility owns the process handle and observation; the parent does not poll
alongside it. Any remaining fixture processes/listeners require ownership proof,
not an inference from parent exit. No vpsAdmin, flake or quick-check rerun,
source edit, push, master integration, release or lifecycle action is included.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/>
