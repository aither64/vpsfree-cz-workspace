# SQLite performance package

Committed at `610da4e3212e66fac026eb94eedb55abf6d3c66a`, parent
`b85ec364057f536940d689b09e612512ffffaf82`. Two exclusive files:
`servers/ruby/test_support/performance_sqlite_fixture.rb` and
`servers/ruby/spec/performance/sqlite_spec.rb`. No production source change. Normal Nix/Overcommit hooks passed without warnings;
[commit log](api-performance-sqlite-commit.log). Index empty and Git window relinquished.

The fixture provides `HaveAPI::PerformanceFixtures::SQLite.cases(profile:)`,
`build(case_spec)` and the shared scenario interface from the READY phase 2
brief. Each scenario owns a named abstract ActiveRecord base, in-memory SQLite
connection, model/resource namespace and SQL subscription. It never establishes
or replaces an unrelated global Base connection. `close` unsubscribes, removes
only that pool and releases its namespace; another scenario remains usable.

`call` makes an actual Rack request with in-memory Basic credentials. It disables
the owned connection's query cache and counts only actual SELECT/INSERT/UPDATE/
DELETE events from that pool while the request is active. Schema, transactions,
seed/setup and later validation are excluded. Counter records are preallocated by
`reset!`. Every response, operation count and complete identity is validated after
measurement using C's `HaveAPI::Performance::Identity.json` helper.

Quick cases are scalar `sqlite.page` (128 rows, page32) and nested
`sqlite.includes` (32 rows, include_depth2, default admin). Weekly retains these,
adds page32 over 10000 rows and includes32/128/1024 for explicit admin/member
users. The includes case is unpaginated: it never sends an invalid limit1024.
Deterministic specs also cover direct includes, whose associated Show output has
only scalar fields, rather than relying on the known missing default preload of
an unresolved nested association. The original default-reflection finding stays
source-based in [existing findings](api-performance-existing-findings.md).

Associated Show validation/authorization happens once per associated row, with
no fixture-side `find` in authorization or preparation. Associated Show execution
raises if called, preserving the adapter's serialization contract. Member rows
can deny entire groups/accounts and hide secret fields. Same-app admin/member/
admin requests prove restrictions do not survive into another request.

## Measured counts and quick checks

- Fixed page32 at table sizes32/128/1024/10000: queries1, auth1, exec1.
- Explicit direct includes: queries2, auth1+rows, exec1.
- Explicit nested includes: queries3, exec1; admin auth1+2*rows, member
  auth1+rows+ceil(rows/2). Member32 therefore requires49 checks, admin32 requires65.
- Query count is constant while per-row authorization remains required.
- 17 focused examples pass (seed8290, 4.48s); both files RuboCop clean; whitespace
  check clean. Tests cover real nonzero cursor behavior, fixed page work,
  include sizes1/32/128, output1024, wrong response/index, reset/record completeness,
  user isolation and connection ownership/teardown.
- Prepared environment only; no gem installs, source checkout replacements or
  long suites/campaigns. `make doc` synchronized docs before server specs.

[Bounded calibration](api-performance-sqlite-calibration.json) retains two warmups
and three one-request trials across16 shapes, raw wall/CPU/allocation results,
response identities, counters, separate SQL traces, exact runtime/gem/input graphs
and calibrated/final fixture hashes. Timings are small calibration observations,
not a timing campaign or a production/DB latency claim. Runtime is Nix Ruby3.4.11,
ActiveRecord8.1.4 and sqlite3 2.10.1. Fixed page32 median is2620 allocations at
every measured table size; nested admin rows32/128/1024 medians are11445/41877/
327979, member7972/27924/216172. This is expected work proportional to output.

The fixed-page spec permits128 extra objects per request between small and large
tables, based on observed zero growth and fixed VM bookkeeping slack. C owns
reference-budget JSON and the reviewed25%+32 headroom calculation; no fixed
ceilings or automatic budget update are written by B. Lead received the artifact
and relayed it to C; direct C interface message succeeded with sender implementer1.

Final independent branch review and longer campaigns remain lead-coordinated.
Session stays open; no merge, deployment, release or lifecycle action occurred.
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/>.

Logger followup is resolved without a B source change or new commit. Worker
pre-load RACK_ENV=test is the accepted policy; C owns the actual-worker startup
regression. The ineffective temporary local logger assignment was removed, and
bounded equivalent allocations/identities/counters reconcile calibration hashes.
See [logging boundary evidence](api-performance-sqlite-logger.md).
