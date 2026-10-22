# 0.29.10 verification before tagging

Exact tested head: b27a031fa03d8d985a3abd2679ce2fc14fe53602.
Base: 784e113c216b16586c482e710ee4a0e0a04e6f8e (v0.29.9).

Independent retained review accepted all four lanes, final history and no-migrations
conclusion before long checks; see release-review.md. A fresh Luna/low utility
ran release-verify-all.sh to completion: local 0, CI 0, wrapper 0 (about 3 minutes).

Local results: server 365 examples; Ruby client 47; Go generator 9; JavaScript
43 tests; PHP 51 tests/144 assertions. All passed. Release helper suite (21),
i18n health, clean package build, manifest/checksums, npm tarball and all three
extracted Ruby libraries passed. Local manifest source matches this head,
version 0.29.10, run_id local. Existing 0.29.9 tests/runtime behavior are retained.
Quick checks also passed with GITHUB_RUN_ID=123, RuboCop (244 files), actionlint,
shell syntax and whitespace. Generated PHP test cache removed; worktree clean.

| Workflow | Run | Result |
| --- | --- | --- |
| clients/go RSpec | [39291064703](https://github.com/vpsfreecz/haveapi/actions/runs/39291064703) | success |
| RuboCop | [39291064490](https://github.com/vpsfreecz/haveapi/actions/runs/39291064490) | success |
| i18n health | [39291064663](https://github.com/vpsfreecz/haveapi/actions/runs/39291064663) | success |
| clients/php PHPUnit | [39291064695](https://github.com/vpsfreecz/haveapi/actions/runs/39291064695) | success |
| servers/ruby RSpec | [39291064651](https://github.com/vpsfreecz/haveapi/actions/runs/39291064651) | success |
| clients/js tests | [39291064610](https://github.com/vpsfreecz/haveapi/actions/runs/39291064610) | success |
| clients/ruby RSpec | [39291064691](https://github.com/vpsfreecz/haveapi/actions/runs/39291064691) | success |
| release | [39291064579](https://github.com/vpsfreecz/haveapi/actions/runs/39291064579) | success |

These branch runs did not publish. The tag run must build its own immutable
artifact set with its own run ID; no local or branch-run files are substituted.
Actual registry OIDC, PHP deploy-key writes and Packagist indexing remain to be
exercised after human environment approval.

Evidence: release-verification.log/status, release-verification-wrapper.log/status,
release-ci-watch.log/status, release-ci-results.json and per-run release-ci-*.log.
