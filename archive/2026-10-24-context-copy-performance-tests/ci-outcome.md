# Published-head CI outcome

All ten recorded workflows passed for exact HaveAPI head
`b85ec364057f536940d689b09e612512ffffaf82`, push event on branch
`2026-10-24-context-copy-performance-tests`. All 24 jobs completed: 23 succeeded
and the protected publishing job was skipped. No failure, retry, rerun,
cancellation or publication approval occurred. No CI operation remains running;
implementer2 relinquished the utility slot after the watcher returned.

Authoritative combined run/job/step evidence:
[ci-final-results.json](ci-final-results.json). The initial recorded run set is
[ci-published-runs.json](ci-published-runs.json).

| Workflow | Run | Result |
| --- | --- | --- |
| RuboCop | 40134658627 | success |
| clients/go RSpec | 40134658631 | success |
| release | 40134658467 | success; publishing skipped |
| clients/rust | 40134658462 | success |
| clients/ruby RSpec | 40134658634 | success |
| clients/php PHPUnit | 40134658464 | success |
| clients/python | 40134658446 | success |
| i18n health | 40134658534 | success |
| servers/ruby RSpec | 40134658619 | success |
| clients/js tests | 40134658713 | success |

The server RSpec workflow runs unfiltered `bundle exec rspec`, discovering the
new context allocation and real-page isolation regressions. Ruby 3.2 job
`120993505707`, Ruby 3.3 job `120993505589`, and Ruby 3.4 job `120993505616`
all passed, as did documentation-assets job `120993505396`. This establishes
the deterministic identity/allocation thresholds passing on all three supported
CI Rubies. The specs do not print raw allocation counts; local CRuby 3.4.11
calibration remains in [package-c-notes.md](package-c-notes.md).

Rust job `120993504766` passed its generator unit/style, runtime formatting/
feature/lint, and generated client protocol acceptance workflow. Release build
job `120993504980` passed, including maintained package tests/build, artifact
retention and verification. Its `Publish approved artifacts` job
`120994936004` was skipped, preserving the branch build-only behavior.

The authorized bounded final snapshot
[ci-final-snapshot.json](ci-final-snapshot.json) found nine workflows complete
and only the release build still running. A fresh operation-scoped watcher then
observed that exact outstanding run; no duplicate CI observation loop ran beside
it. Pinned catalog `840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`
selected `gpt-6-luna`/`low`, native utility
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`, fresh context, with
`danger-full-access` and approval policy `never`. Its `gh run watch` exited zero;
the release had completed by observation. Raw watcher evidence:
[ci-release-final.json](ci-release-final.json) and
[ci-release-watch.log](ci-release-watch.log).

No source, workflow or Git changes were made for CI observation. CI success is
verification evidence; no merge, deployment or release action was authorized.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/>.
