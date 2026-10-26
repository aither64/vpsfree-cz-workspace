# Direct-run requirement preflight: frozen review fix

Base/reviewed HEAD: `fca837b7be8913d9f79bc79c2437d25a0f5750ba`.

The direct CLI now checks all three gemspecs in both verified source roots before its first child/pilot. `Performance.gemspec(root, path)` owns the existing subprocess evaluation and Ruby/runtime requirement policy. Campaign delegates to that same helper, preserving its public error class. Bundler/Ruby injection variables are cleared at the shared subprocess boundary. No new evidence/schema/proof framework or documentation change; the documented requirement is now enforced by both callers.

Changed five files: `utils/performance_ci.rb`, `servers/ruby/benchmarks/{endpoints,performance_compare}.rb`, `servers/ruby/spec/performance/{runner,release_lineage}_spec.rb`. Delta: 91 insertions, 24 deletions; most production code moves existing policy. Exact frozen SHA256 inventory: `frozen-inputs.json`.

Focused RSpec command (inside the existing benchmark shell and prepared gem home, with normal source/spec load paths): runner spec locations 148, 312, 406, 547, 562 plus release-lineage location145. Result: **7 examples, 0 failures**, seed8208, 5.27s. `specs.log`, `specs.exit=0`. The new regression uses actual temporary gemspec files/subprocesses and covers valid, unsupported Ruby and incompatible dependency requirements in either source; invalid cases never call `child`. Existing Campaign requirement assertions and cheap/expensive direct-run/replay composition, push exception and weekly maintenance boundary remain covered. Controlled composition tests stub the new source requirement boundary explicitly.

Final RuboCop: **5 files, no offenses** (`lint-final.log`, `lint-final.exit=0`). Ruby syntax all5 files and `git diff --check`: pass. Budget SHA256 unchanged `57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050`; fixed reference remains `b85ec364057f536940d689b09e612512ffffaf82`. Full87 worker/runtime gates and old replay/classifier code are unchanged.

No install, setup, smoke, timing, broad suite, project Git mutation or publication. No active process. Frozen pending lead release to Git owner3 and narrow review reconciliation; hosted final-head checks remain outstanding under the lead's existing plan. Existing successful unrelated checks are reused for their original scope.
