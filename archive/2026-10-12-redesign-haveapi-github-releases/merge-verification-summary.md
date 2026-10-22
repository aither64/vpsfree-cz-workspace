# Refreshed verification before approved master integration

Repository: vpsfreecz/haveapi. Target: refs/heads/master.
Base: cb3f39f75e8a63416388d24293f936d1db97162b.
Tested head: c14e7d3158b91c134c2817b489cd29772fc09f82.

The clean rebase preserves both reviewed patches exactly; see
merge-rebase.range-diff. Refreshed retained independent review followed quick
checks and preceded long checks. It accepted this exact range with no findings,
including whole-history consolidation and no-migrations conclusions. See
merge-review.md and merge-review-receipt.json.

Quick checks: metadata, 21 helper examples normally and under GITHUB_RUN_ID=123,
RuboCop 243 files, shell syntax and Git whitespace, all passed. A fresh Luna/low
utility ran merge-quick.sh; merge-quick.status is 0.

Full local verification: another fresh Luna/low utility owns merge-verify-all.sh
for this exact head. Local exit status is 0 (merge-verification.status).
Release metadata/helper checks, i18n health, clean package build, full component
tests, npm tarball loading, manifest verification and extracted Ruby libraries
passed. Counts: Ruby server 355, Ruby client 47, Go generator 9 examples;
JavaScript 43 tests; PHP 51 tests/144 assertions. The new dist manifest explicitly
records source c14e7d3158b91c134c2817b489cd29772fc09f82 and version 0.29.0.
Old local artifacts remain in artifacts-cb256a87539c/. The PHP test cache generated
by this run was removed, and the feature worktree is clean.

## Safe Actions on the exact head

| Workflow | Run | Conclusion |
| --- | --- | --- |
| release | [39278682776](https://github.com/vpsfreecz/haveapi/actions/runs/39278682776) | success |
| i18n health | [39278682753](https://github.com/vpsfreecz/haveapi/actions/runs/39278682753) | success |
| RuboCop | [39278682772](https://github.com/vpsfreecz/haveapi/actions/runs/39278682772) | success |
| clients/js tests | [39278682743](https://github.com/vpsfreecz/haveapi/actions/runs/39278682743) | success |
| servers/ruby RSpec | [39278682860](https://github.com/vpsfreecz/haveapi/actions/runs/39278682860) | success (Ruby 3.2/3.3/3.4) |

The release run passed maintained-package tests/build, immutable artifact
retention and verification. Publication was skipped. Initial runner queueing
delayed all five jobs; no failed check was retried or dismissed.
All five workflows completed successfully before integration submission. The
aggregate wrapper exited 0 after 1614 seconds (26m54s), reporting local and CI
exit statuses 0. No verification operation remains active.

Evidence: merge-quick.log/status, merge-verification.log/status,
merge-ci-runs.json, merge-ci-results.json when complete, merge-ci-watch.log/status
and merge-verification-wrapper.log/status. Detailed per-run logs use merge-ci-*.

Only the master merge is authorized by the user's "yes, merge it" instruction
on 2026-10-19. No version tag, registry publication, PHP mirror write or
release-line integration is included. Runtime APIs, persisted formats and library
versions are unchanged. Actual trusted authentication, PHP key push rights and
Packagist indexing remain first-authorized-release checks, as documented.
