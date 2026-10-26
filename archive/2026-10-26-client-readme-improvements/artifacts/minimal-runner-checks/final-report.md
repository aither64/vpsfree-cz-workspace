# Minimal runner package: frozen handoff

Session `2026-10-26-client-readme-improvements`, implementer1. Session current and both environment bindings match. Project HEAD before runner commit: `37520c4d2712df0947f59391903f55736868c25c`. All shared Git operations remain implementer3's; no staging, commit, fetch, push, or project ref/index changes by implementer1.

## Frozen files

Owner1: `utils/performance_ci.rb`, `.github/workflows/servers-ruby-performance.yml`, `servers/ruby/benchmarks/{endpoints,performance_compare}.rb`, `servers/ruby/spec/performance/{runner,comparator,release_lineage}_spec.rb`, `doc/performance.md` (lead final prose pass preserved). Owner0's separately frozen `event_baseline_spec.rb` joins this package. No Makefile change. File SHA256 inventory and actual benchmark input hashes are in `frozen-inputs.json`.

Existing branches compare exact event before/after, including the narrow quick nonancestor push exception; new branches use captured-default merge-base. The workflow obtains missing exact push objects without a fallback. The conventional single benchmark bundle runs outside Bundler. Raw contributor flakes remain source provenance, while actual benchmark Gemfile/lock/shell bytes and hashes bind consumed inputs. All other declarations and existing JSON/maintenance normalization remain strict. Historical schema2 replay follows its existing path. No rejected preparation/proof subsystem returned.

## Checks and evidence

- Owner0: exact event-selection/Campaign forwarding file, 52 examples / 0 failures, lint clean (separate owner0 report).
- Fresh pinned Luna/low watcher ran `checks.sh`, ~64s. `smoke.exit=0`: exactly ONE untimed normal-request smoke per source, 14 quick workloads each, for fixed `b85ec364057f536940d689b09e612512ffffaf82` and candidate `37520c4d2712df0947f59391903f55736868c25c`. Both showed 116 loaded source files and exactly 87 calibrated activated gems under `/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`. Each request validated, source loaded paths/hashes matched exact exported Git objects, fixtures closed. No timing or eager graph activation.
- `checks.sh` focused comparator + release replay + seven runner examples: 48 examples, 47 pass, one controlled malformed-source fixture failed because new runtime guard ran first. Retained `specs.log/specs.exit=1`. The fixture now stubs only the runtime boundary; `affected.log/affected.exit=0`: 2 examples / 0 failures. This includes the explicit changed-Ruby/unavailable-dependency negative.
- A command filter mistake selected zero examples once (`filtered-empty.log`); this is not pass coverage. Corrected location-based execution produced the above 2-example result.
- Final actual Campaign declaration validation initially exposed that unloaded Rake is absent from the calibrated activated graph. Corrected requirement checks to validate the actual RubyGems-selected installed tool spec. No budget/graph change. `dependencies-before-fix.log` retained; `dependencies.log/dependencies.exit=0`: 1 new requirement example / 0 failures (supported, unsupported Ruby, unsupported dependency), then actual declaration equality/Ruby+gem requirements passed for both exports, including differing contributor flakes and existing JSON declaration normalization.
- `maintenance-inputs.log/maintenance-inputs.exit=0`: 1 affected existing example / 0 failures, covering conventional benchmark inputs with proven own-version normalization as well as old library-lock inputs.
- Final focused RuboCop: 6 files / no offenses, `lint-frozen.log/lint-frozen.exit=0`. Ruby syntax: all 7 changed Ruby files pass (includes owner0's file). `git diff --check` passes. YAML parses; all 10 workflow/doc shell blocks pass `bash -n`. No imported action ref, hard 15/45-minute timeout, timing policy, retry policy or reference change.
- Budget byte equality to `cb43ae23` verified; SHA256 `57b8d4725e76c4552e6cb2eb54982cd8d406bd2415eb99e51cb43049bae3a050`, fixed reference `b85ec364057f536940d689b09e612512ffffaf82`.

## Stop and remaining work

All package edits are frozen. No active watcher/build/install/request process. Lead may release owner3 commit and fresh independent final review. Actual final-head hosted quick and release CI remain outstanding and must follow commit/review; no measured campaign was run locally. Weekly selection and maintenance behavior have deterministic coverage; no weekly timing run is claimed. No deployment, publication, integration, resource or lifecycle action by this package.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-client-readme-improvements/
