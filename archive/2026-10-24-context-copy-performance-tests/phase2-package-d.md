# Phase 2 package D

Committed as `e98e704e926961bc6d8e4a12ee15c77c1380e7a8` in the granted D
window. Exactly the nine owned files below were staged; C files were preserved.
Normal pre-commit and commit-message hooks passed with final message lines at
most72 columns. The index is empty and D relinquished the Git window. No fetch,
push, rebase, dependency installation, workflow dispatch or campaign was run.
Final source reconciliation with C remains before whole-branch review.

## Owned files

- `.github/workflows/servers-ruby-performance.yml`
- `utils/performance_ci.rb`
- `servers/ruby/spec/performance/event_baseline_spec.rb`
- `servers/ruby/.gitignore` — lead-approved exact `doc/performance.md` rule
- `Makefile`
- `doc/performance.md`
- `doc/agent-instructions/development.md`
- `doc/client-examples.md`
- `README.md`

The shared performance guide is authoritative; its copied server-doc version
is ignored and never staged. Existing opt-in documentation benchmark unchanged.

## Behavior

The resolver reads structured event JSON and Git objects, selecting full exact
SHAs before path relevance. PRs use head/event-base merge-base, feature pushes
use whole-feature merge-base against captured default, default pushes use event
before/after, schedule uses event default SHA vs immutable accepted b85 reference,
and manual uses a complete explicit pair or captured default vs b85. Weekly
always requires that fixed baseline. Missing/zero/unavailable/unrelated/equal
comparisons block; no same-head fallback. Relevant source/dependency/budget/docs/
workflow paths run; valid irrelevant pushes/PRs explicitly succeed without work.

The hosted Ubuntu workflow has contents-read only, no secrets or PR comments,
ordinary PR events and persist-credentials false. It uses the three current
official immutable action refs recorded in [upstream preparation](workflow-preparation.md).
Schedule is Sunday03:00UTC, quick/weekly hard limits10/30min, artifacts30days.
Stable `Performance gate` requires successful job status AND explicit compared
or no-work output; failure/cancel/skipped/missing outputs fail. Evidence is
initialized before checkout so early failures can retain a receipt.

The wrapper exports both exact source trees and runs the neutral candidate
checkout harness with the agreed C run CLI. No worker mode is used by D. Archives,
Git trees, selection/ancestry, matched config/evaluated gemspec dependency
manifests, resolved root/server/(weekly Rust) locks, flake graph, shell derivation/
requisites, runtime and process logs/exits are retained. Isolated gemspec and
worker invocations clear inherited Bundler/Ruby load environment. The runner's
actual loaded gem graph/ABI/source validation remains C-owned.

Exit/report/source binding preserves 0pass/1regression/2inconclusive/3error;
unknown or missing outcomes block. No automatic retry, reference or budget
update. Manual weekly dispatch may be refused until the workflow exists on
default; preserve any refusal and disclose local-only weekly verification.

## Focused evidence

- 22 focused examples passed in about1.5s: PR head selection, multi-commit default
  batch, feature/new branches, missing/manual/scheduled cases, ancestry,
  relevance, real error CLI, actual aggregate shell status/outcome handling and
  subprocess runner exit/report propagation for all four codes.
- Both changed Ruby files pass syntax and RuboCop.
- Workflow YAML properties, every embedded Bash block and guide relative links/
  anchors pass. No actionlint executable exists in the prepared environment;
  no dependency installation was attempted for that tool.
- A read-only actual resolver CLI invocation against available Git objects
  selected exact original event before/after correctly. It performed no Git
  mutation or network request.
- Isolated weekly dependency/gemspec compatibility passed between the exact
  retained b85 source export and current candidate inputs; no workload ran.
- C `endpoints.rb --help` matches the exact documented run/compare flags.
  Make dry runs produce those exact commands. No alternate CLI introduced.
- `make doc`, generated-copy exclusion and `git diff --check` pass.

Prepared quick check command from HaveAPI root:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --command bash -lc \
  'ruby -c utils/performance_ci.rb && ruby -c servers/ruby/spec/performance/event_baseline_spec.rb && bundle exec rubocop utils/performance_ci.rb servers/ruby/spec/performance/event_baseline_spec.rb && make --silent doc && cd servers/ruby && bundle exec rspec spec/performance/event_baseline_spec.rb'
```

The flag skips shellHook dependency installation only. Long complete quick/
weekly comparisons and hosted verification remain after committed final review,
launched by a fresh lead-coordinated verification watcher. Detector calibration
and runner source changes belong to C. No deployment, merge or lifecycle action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/
