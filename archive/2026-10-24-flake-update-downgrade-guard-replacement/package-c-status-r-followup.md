# Status final R workflow failure

The lead accepted the complete corrected status workflow: exit 0, 39 operations all 0, generated local head `27403b4b607046937a4cf10e17007f7a781fb928`, including ordinary hooks, full Go tests, Nix build and final committed-lock validation. [Hashed final receipts](package-c-final-real-workflow-receipts.json) bind the new source and separate attempt. The original failure remains preserved below.

The final nonpublishing status pattern stopped at workflow step 05, `Run tests`
(`nix develop --command go test ./...`), with status 1. The failing assertion is
`TestRoutesDoNotCacheMetrics` at `app_routes_test.go:1138`: the response has
`Vary: Accept, Accept-Encoding`; the test forbids `Accept-Encoding` as a proxy
for the application route cache. The tools package passed, including the Perl
setter regression. This is neither a guard rejection nor an evidence failure.
The final committed-lock guard, package build and publication were not reached.

Exact candidate Prometheus `client_golang v1.25.0` deliberately adds those two
Vary fields in `prometheus/promhttp/http.go:329-333`; its changelog records this
negotiation enhancement in version 1.25.0, issue 2142. The baseline version
1.23.2 did not add Vary. The updater selected that dependency through its
existing `go get -u -t ./...` behavior. Status's unchanged `/metrics` route uses
the exporter handler directly. Its response cache separately adds
`Vary: Accept-Encoding` in `cache.go:155`, but `/metrics` does not use that path.
The test and production routes are unchanged from the original feature base;
this assertion conflates the header name with the component that added it.

The lead accepted the following test-only correction: retain the empty
Cache-Control assertion; compare routed Vary values with the direct exporter
handler for an identical request, retaining detection of route-owned additions;
verify changing exporter gauge values are immediately visible at the same fixed
clock, within the route-cache TTL. No production behavior, metrics contract,
dependency selection or input pin changes are proposed. No source edit or test was run during initial diagnosis. The accepted correction
is now local commit `d4c816bbf7ad22b9b2dcb424c1f316b1d0b6c6aa`, following the
existing adoption and independent vendor-hash fix as a third logical commit.
Eight focused route-cache/gzip/metrics tests pass with both pinned Prometheus
1.23.2 and the failed candidate's exact 1.25.0 graph in a separate diagnostic
checkout. Ordinary gofmt/i18n hooks passed; only app_routes_test.go changed.
[The complete inventory](package-c-status-metrics-inventory.json) and
`review-status-metrics/` retain the three-commit series and exact delta.
The [focused final review](review-status-metrics-report.md) passed with no findings,
including all three logical commits and retained test invariants. The exact
reviewed head was published through a normal fast-forward SSH push; master
remains unchanged and the worktree is clean.
[Publication proof](package-c-status-metrics-publication.json) and
[the immediate CI snapshot](package-c-status-metrics-ci.json) are retained.
Final-head i18n run 40105130335 passed; Integration 40105130350 was in progress
at observation. Previous R Integration 40102931080 completed successfully. No
superseded active run required cancellation, and no CI wait/rerun/dispatch occurred.
[The new status-only runtime brief](package-c-status-metrics-verification-brief.md)
binds a separate root/driver/manifest; no runtime rerun was launched.

The failed checkout and original receipts remain untouched at
`/tmp/flake-update-guard-2026-10-24-provider-r-1/project-vpsf-status/`.
[Reconciliation](package-c-status-r-failure-reconciliation.json) binds exact
source/driver/receipt hashes, command process groups, logs, HEAD/index/lock and
local commit effects. Two successful local workflow commits explain the
whole-job unchanged=false field:

- `1ef7a3ae184051d967688595b663f48427ba3698`: guarded nixpkgs leaf update,
  only flake.lock; ordinary hook succeeded.
- `8411635e196e0db3dde15c5a29e8ec50a7caa9b9`: Go dependencies and vendor hash,
  only go.mod/go.sum/nix/package.nix; ordinary hook succeeded.

HEAD is the latter commit. Index and worktree match HEAD, with no staged,
unstaged or untracked changes. HEAD/index/worktree lock blob is
`a6224d64b9a4216ecea87d04ee0d80196e658f0c`. External push remains
`disabled://nonpublishing-verification`. A /proc scan finds none of the receipt's
owned process groups or a process with CWD beneath this attempt. No cleanup,
retry, kernel build, provider modification or external publication occurred.

[Exact source/module hashes](package-c-status-r-metrics-source-evidence.json)
retain the static basis. Independent IRC/D/race verification may proceed under
the lead because the provider and safety guard are unaffected; no success is
claimed for the unexecuted final status guard/build/publication stages.
