# Status metrics test compatibility final review

No Blocking, Important or Advisory findings. The status-only committed change
and complete three-commit branch pass this focused final review. Prior guard,
scope/risk and other-repository conclusions remain unchanged. Complete status
workflow verification and exact final publication/CI evidence remain separate
gates; this report grants no default-branch integration or deployment approval.

## Identity and exact scope

Verified bound `dev-session current` returned
`2026-10-24-flake-update-downgrade-guard-replacement`; both session environment
variables are absent and the trusted workspace/thread binding matches. Live
same-session roster: `reviewer0`, thread
`01a16da6-4cc0-7fd1-8b85-0933235d3dd0`, purpose `review`, ready,
`gpt-6.1-sol` / `xhigh`, `read_only`. No overrides, fallback, nested agents or
authorship of implementation changes.

Applied the mandatory review skill's general and architecture/repetition lanes,
reusing unchanged guidance already read in this context and the prior reports.
Only vpsf-status was reviewed in this turn. No source/ref edits, test/build
launches, publication, claims, lifecycle, merge or deployment actions occurred.
The independent D watcher was untouched. Only this new review report was written.

Repository: `git@github.com:vpsfreecz/vpsf-status.git`, target `master`, worktree
`worktrees/2026-10-24-flake-update-downgrade-guard-replacement/vpsf-status`.

- Base: `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb`.
- Literal reviewed parent: `6b5e8a6089926112bfbb63a45413b886ee56e549`.
- Reviewed local final head: `d4c816bbf7ad22b9b2dcb424c1f316b1d0b6c6aa`.
- Complete series: `ebb7e6a2252f5a7f61d06a5935bb4c88a6c1964e` (guard adoption),
  `6b5e8a6089926112bfbb63a45413b886ee56e549` (vendor-hash updater fix),
  `d4c816bbf7ad22b9b2dcb424c1f316b1d0b6c6aa` (metrics test compatibility).

Independently verified exact HEAD/parent, clean Git status, base ancestry,
complete ordered series/messages, full final paths and new-only diff against
`package-c-status-metrics-inventory.json`. Read the complete final diff and
range-diff under `review-status-metrics/`. The first two commits are literally
unchanged. The new delta is only `app_routes_test.go`, 12 additions/2 deletions;
production code, workflow/provider R selection, docs, module files, package
definition and lock are unchanged from the reviewed parent. The test-file hash
matches the inventory.

## Test correctness and proportionality

Inspected `app_routes_test.go:1129`, the route/request/scrape/assertion helpers,
`app.go` metrics registration, `exporter.go` and `cache.go`. Also read the local
Prometheus 1.23.2/1.25.0 handler source and 1.25 changelog. Version 1.25 adds
negotiation `Vary` headers inside the exporter handler itself. The retained
failed log shows the old test rejecting `[Accept Accept-Encoding]`; the original
test is byte-identical at the branch base and reviewed parent. This establishes
a pre-existing test assumption exposed by the dependency update, rather than a
guard regression or a production cache defect.

The replacement compares routed `Vary` values with a fresh handler from the
same exporter, using the same method, target and default request headers. Exact
slice equality detects route additions, duplicates and removals while permitting
the delegated exporter's legitimate negotiation behavior. This does not merely
delete the failing assertion. The empty `Cache-Control` assertion remains.

The added gauge checks use existing helpers to scrape through the real routes,
parse the metric family and assert type/help/unlabeled value. The fixture fixes
`app.now` at `fixedNow`; the route cache is shared on the same application and
its TTL is one second. Changing the gauge from the fixture's initial 1 to 0 and
then back to 1, without advancing that clock, detects stale response reuse
within the TTL. It needs no sleeps or timing thresholds. Each test owns its
exporter/registry, so the mutation does not change another test's global state.

Using the same exporter as the header baseline is appropriate delegation at
this boundary; the independent gauge-content assertions cover freshness.
Existing metrics/schema and surrounding cache/gzip checks remain intact. The
`slices` import is supported by the repository's Go 1.25 minimum. The small
change uses established helpers and introduces no duplicated parser, cache
implementation, framework or new production contract. No further abstraction,
documentation change or broader review is needed for this test-only correction.

## History, pins and migrations

Three logical commits are justified. Guard adoption and the independent
baseline vendor-hash defect keep their prior ownership. The third commit fixes
an independently existing metrics-test compatibility assumption, proven present
at the base; it is not a repair of code/tests introduced by either preceding
commit. It is independently meaningful and its message explains both the
negotiation issue and strengthened freshness check.

No obsolete approach, transitional shim, fixup, redundant repair or repeated
pin-update history remains in this complete range. The single final workflow
tool selection remains provider R
`5436d3d7c36d3d5174eab3c44e3578830749d3db`; the new commit introduces no pin
stream or dependency update. Generated flake/Go/vendor changes in the failed
disposable workflow are execution provenance, not additional feature commits
or integrated/deployed lineage.

**No migrations.** The final feature range has no schema/persisted-format
transition; the new delta changes only a test. No release, deployment or
externally consumed runtime-state boundary requires retaining an intermediate
test, migration or repair version. The original failed checkout and its generated
commits remain preserved rather than overwritten or treated as successful proof.

## Evidence and next verification

Read both focused logs: all eight selected cache/gzip/metrics tests passed on
the pinned Prometheus 1.23.2 graph and on the separate diagnostic fixture using
the failed candidate's exact 1.25.0 dependency graph. Inspected the ordinary
Lefthook commit log: gofmt and i18n checks passed. The reconciliation receipt
separates successful guard/Go/vendor stages from the failed test stage and
records no publication or remaining owned process. The correction's test hash
and dependency-input hashes bind the candidate fixture; it does not mutate the
original failed attempt. I launched no redundant checks.

Next: publish only the authorized status feature successor, collect exact remote
proof, then run its complete workflow in a fresh nonpublishing root/manifest
bound to this final source and provider R, retaining required tests/build and
committed-lock validation. Focused compatibility passes are not the full
workflow result. Prior successful other-project patterns remain subject to
their exact-source/input evidence; no all-eight review or verification rerun is
requested here. Other active verification and final CI readiness remain with
the lead. No remediation or further review rerun is requested by this report.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/>
