# Package-entrypoint Ruby environment follow-up

Status: package fix committed locally as
`bdaed19e901237e05bd0a779f368e76cb311143f` (P), directly after the reviewed
guard commit `7ba361d22a4aac044cb02abf8397800bcf5726bf`. The focused actual
candidate build, both real regressions, source hash recheck, lint, generated man
and ordinary commit hooks passed. Both D consumer adoption commits now select P
locally and pass their 20 mock scenarios/hooks. Publication remains held for
the complete affected review. Final exact-P package/live/VM verification remains
post-review work. Original review/verification manifests and failed attempts
remain unchanged.

## Demonstrated failure and preserved effects

C's actual IRC workflow step runs inside its declared `nix develop` environment.
The helper's first `inputs ls --json nixpkgs` starts the pinned provider's Ruby
3.4.9 with inherited `RUBYOPT=-rbundler/setup`. That preload activates IRC's
`BUNDLE_GEMFILE`/`BUNDLE_PATH`, whose installed gems use Ruby ABI 3.3.0. Startup
raises `Bundler::GemNotFound` before the helper prints its current revision or
attempts an update. The wrapper exits 1; the helper pipeline returns jq's exit 4
because it received no JSON. This is actual local-helper package behavior,
distinct from the earlier fixture-only YAML/JSON activation problem.

The failed clone remains at `a2ab57b8169ad978f6f8542dd19cf5199517b0cb`, with lock
SHA-256 `006122d3d852e2da6eb985f610278ac3680849dda25e59d16fb1dd58318efcfb`
and semantic index SHA-256
`fffe91a9bf40946c79c7085d399a3f4341c13f8b0b0d71938fbbe0245e01b2e6`.
Tracked status is clean and its push URL remains disabled. Only ignored caller
gem/Bundler setup exists. No live updater retry, cleanup or ref mutation was
performed during diagnosis. Original receipt:
`/tmp/flake-update-guard-2026-10-24-C-postreview-1/project-vpsfree-irc-bot/receipt.json`.

## Accepted startup boundary

The lead accepted the architect-backed change to `nix/package.nix`: pass
`--disable=rubyopt` to the packaged Ruby interpreter and retain its existing
GEM_HOME/GEM_PATH/RUBYLIB and runtime PATH setup. RubyGems stays enabled.
RUBYOPT and BUNDLE_* remain in the process environment for ordinary child Ruby
and hook commands. Explicit Bundler loading by user scripts remains subject to
their bundle configuration. This does not claim general environment isolation.

The actual packaged interpreter's help and the
[Ruby 3.4 option reference](https://docs.ruby-lang.org/en/3.4/ruby/options_md.html#label---disable-3A+Disable+Features)
confirm the independent `rubyopt` feature. The guide/manual describe this exact
boundary. The lead directly reviewed the prose and supplied its final sentence.

This is an existing packaging compatibility bug exposed by the new supported
workflow/local-helper use. Its fix stays a separate coherent commit after the
reviewed guard commit `7ba361d22a4aac044cb02abf8397800bcf5726bf`, which remains
a literal ancestor. No migration, persistent format, source policy, CLI status
or guard transaction behavior changes.

## Diagnosis and quick-check evidence

[package-b-ruby-env-diagnosis.json](package-b-ruby-env-diagnosis.json) retains
the exact-wrapper failure and in-memory one-flag prototype. With reconstructed
known exports from IRC's exact shellHook, the unchanged wrapper fails and the
prototype returns one `nixpkgs` JSON row with its complete revision. Under the
same wrapper GEM/PATH/RUBYLIB setup, the parent retains exact caller variables
and its child selects Ruby 3.3.10 and activates IRC's Overcommit 0.69.0 bundle.
No Nix build or actual update was needed for this read-only diagnosis.

An initial child assertion incorrectly expected RUBYOPT text to remain identical
after Bundler activation. Bundler itself prepends its absolute setup path; the
corrected check proves the exact parent variables before spawning and the actual
child interpreter/bundle activation. Both the failed assertion and explanation
remain in the receipt.

The later old-artifact regression attempt is invalid negative-control evidence:
the previously executed output `/nix/store/rl717hygbxjnqf8c43ksn09rkj5zkcfy-confctl`
had disappeared, so both cases failed with ENOENT. Its disappearance's cause is
not established. The failed attempt is retained in
[package-b-env-regression-old.log](package-b-env-regression-old.log) and is not
represented as behavior verification. No obsolete-output retry is planned.

The new package-specific regression spec creates a miniature caller path gem,
Gemfile and Ruby preload. One case checks successful JSON listing without
activating that preload. The other invokes the actual confctl GitCommit path
from a fixture user script, runs a real Git pre-commit Ruby hook and checks
the selected caller Ruby, caller gem path and hook/preload markers. It tests
behavior rather than checking the wrapper's text. Source-binstub-only runs skip
these package cases; package verification supplies CONFCTL_BIN.

Focused RuboCop passed after correcting indentation. Normal man generation
passed, including the lead's final prose, and staged/unstaged whitespace checks
were clean. The candidate artifact operations used the lead's serialized fresh
watchers and frozen
[package-b-env-quick.sh](package-b-env-quick.sh), SHA-256
`180ad0345e3c2d5247187365773264f5db1687ad08d5f5583756e38af141eaf4`.
The first operation retains an owned output link and source/package/log/status receipts under
`/tmp/flake-update-guard-b-env-2026-10-24-1`. No whole suite, integration stage,
live update, publication or machine action is part of that quick operation.

The first actual candidate built as
`/nix/store/4mj5s052ik9317j7ydyh0r97gyz9rv13-confctl`, with its owned output
link retained. Both tests then failed loading `require_all`. The gem is present;
the package starts normally outside the RSpec bundle. Ruby 3.4's
`rubygems.rb:1482` separately loads `ENV['BUNDLER_SETUP']`, independent of
RUBYOPT. The outer `bundle exec rspec` exports that variable, and it activated
the miniature Gemfile before confctl could load its dependencies. The real IRC
shellHook exports RUBYOPT but does not export this separate launcher preload.
With the known actual IRC shell exports, the retained candidate returns 0 and
one `nixpkgs` JSON row/full revision; parent BUNDLER_SETUP is absent.

The lead accepted setting only BUNDLER_SETUP to nil in the regression's simulated
caller environment, with an explanatory comment. This prevents accidental outer
RSpec activation while preserving its real caller preload/Bundler/Git-hook
behavior. Production does not unset BUNDLER_SETUP or any caller environment.
The accepted feature is RUBYOPT startup handling, not isolation from explicit
RubyGems/Bundler activation. Attempt1, logs and out-link remain intact. Root's
fresh watcher ran the same frozen quick script with output
`/tmp/flake-update-guard-b-env-2026-10-24-2`: status 0, two examples and no
failures, source hashes unchanged. Focused lint passed after the fixture
correction.

The successful candidate output is
`/nix/store/5zxmilj7i4783didd7qb63i5g5wyb6ih-confctl`, wrapper SHA-256
`793077a60751d86dc821f83c337be374b2a41f03b01cf104bf0896f3e3fd4d24`.
Its bundled Nix is 2.34.8 at
`/nix/store/azi9n31ia037jml4ibi4nfwz1v4hmrj6-nix-2.34.8/bin/nix`.
The owned `provider` output link and source/package/status/spec receipts remain
under that attempt root. The exact outer log is
[tracking/package-b-env-quick-2.log](tracking/package-b-env-quick-2.log).
The candidate was built from the precommit worktree; its recorded source file
hashes match P's final files. This is focused prerequisite evidence, not a claim
that the final published P artifact/runtime checks have already run.

Ordinary Overcommit Nixfmt, RuboCop and commit-message hooks passed; only a soft
72-column warning occurred and all message lines are within 80 columns. Log:
[package-b-env-commit.log](package-b-env-commit.log). The complete base
`cc40679d267165aecfa569128438bb55fe910268` to P series has two intentional
commits and 22 changed paths. The bounded 7ba-to-P delta is four paths,
119 insertions and one deletion: package wrapper, new regression spec, owning
guide and manual. Full series/path/tree/diff inventory is in
[package-b-final-inventory.json](package-b-final-inventory.json). No obsolete
intermediate packaging commit or migration remains.

## Remaining sequence

All seven consumers repin locally once to P, consolidating their adoption
streams. D's final local heads are
`7b0609cf41fc9fe54b6d09129246ff100fb4197a` (vpsFree) and
`4352f16fb967e3b9da829972c9799157badd0494` (org); each range remains one
workflow-only adoption commit with unchanged deployment-tool flake inputs.
[package-d-branches-final.json](package-d-branches-final.json) labels these local
heads separately from historical prior remote observations. D's 20 scenarios
passed in [package-d-quick-final.log](package-d-quick-final.log); ordinary hooks
passed in its two `package-d-final-commit-*.log` files. All three worktrees are
clean. No final successor has been pushed.

The affected independent review covers all committed fixes/repins before
provider publication followed by consumers and new long verification. Root will
run all seven real nonpublishing patterns at final P, including IRC and both
old config environments/hooks. The existing exported `checks.<system>.rspec`
sets `src = self` and `CONFCTL_BIN` to the same source's actual package, so its
final exact source/input derivation can prove the full final suite without a
duplicate direct source-suite invocation. The older 195-example result remains
historical; the final source adds these two cases. No result is inferred from
unchanged policy files alone. The original review/attempts remain provenance;
no default integration, release, deployment or session lifecycle action is
authorized.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
