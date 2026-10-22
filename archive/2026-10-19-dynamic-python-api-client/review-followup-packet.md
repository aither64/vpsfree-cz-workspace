# Affected-lane final review follow-up

Original independent review: [review.md](review.md), exact head 05e6236, full
original report in conversation. Same retained reviewer0 Sol/xhigh/read-only.
Complete corrections committed/folded and final quick checks pass. Ready to
assign affected review at exact head below; no live integration launched.

Lead accepted all R1–R5, no waiver. Source corrections committed and consolidated;
no migrations or published consumer/state boundary introduced.

## Affected scope

- General and risk/compatibility: GET lossless representation boundary, actual
  DELETE JSON semantics, wire-order preservation and updated public docs.
- Architecture/repetition limited to ownership of new GET representability
  rules; no separate confirmation review of the exact requested auth extraction.
- Scope lane limited to checking proportionality of new query guards/helpers;
  no new generalized framework or server/protocol extension requested.
- Whole updated branch history/consolidation and migration conclusion required.
- Unchanged package/release implementation accepted by original full review;
  no need repeat those lanes/content absent related change.

R5 no-show binding is a direct narrow correction, lead inspected source guard
and focused tests; reviewer may inspect its final folded diff as context, no
new design/association inference introduced.
R1 ordered transport, R2 server-authoritative DELETE branch, and R3 exact shared
auth helpers are likewise directly inspected/tested requested corrections; no
standalone rerun merely to confirm them. Their interactions with the changed GET
boundary and updated whole history remain context for the affected review.

## Remediation acceptance

R1: `urlencode` ordered pair sequence into ASCII raw query; HTTPX URL.copy_with
changes query only, no QueryParams regrouping. Both facades exact bytes, escaping,
mounted path tests; actual Rack parses two original rows/values.

R2: DELETE follows POST/PUT JSON body, with namespaces+metadata. Actual current
and released server consume body. Named list requires object root/namespace.
Prepared real generic server DELETE echo and metadata regression both modes.

R3: existing ClientState `_prepare_challenge` owns next-step token requirement,
private field stripping and nonce install; `_continuation_params` owns nonce
currentness, override rejection, copied token merge. Both called under existing
mutation gate. Shared parsing remains unchanged, no I/O or public API added.

R4: exact [design.md](design.md) GET correction section. Permit described scalar
coercions/nulls, nonempty mappings, scalar string arrays, dense flat equal-key
rows with canonical shared field order. Reject lossy sparse/nested/empty shapes,
bracket/empty key components, Custom numeric/bool/nested-null leaves (top-level
nullable Custom None remains advertised scalar null). Empty structural wrappers
may omit, supplied empty values cannot disappear. JSON retains expressive data.
No JSON-stringified Custom/indexed array protocol/method override. Tests require
local rejection before action HTTP and real Rack parsed wire assertions.

R5: only ordinary same-resource output with inherit_context=True carries original
bound_args/path_params when no show action exists; associations remain unbound
without known identity, no guess from returned id fields. Positional/named/
unbound/association cases covered.

Advisory: README states only literal Custom accepts arbitrary finite JSON;
unknown parameter type names reject. Lead writing pass preserves exact facts.

## Quick evidence before commits

- Declared Python check.sh: Ruff38 format/lint, strict mypy18, 261 unit tests
  pass in 1.09s.
- Actual bundled Rack parser/wire tests 46 pass in 7.92s, no API server.
- Runtime owner C65 focused plus changed-core raw-query paired2 pass; core/D159
  focused, owned Ruff/mypy clean.
- Generic real server now 13 collected cases only, Ruby shim syntax/RuboCop
  clean. No live generic/vpsAdmin/package smoke run before rereview.
- Fresh policy watcher performed server dependency setup only (bundle install/
  check 25s, exit0), no tests/server/deployment. Committed parser helper uses
  declared server BUNDLE_GEMFILE, not local global gems.

## Final inventory

Base/fetched origin/master: `c58704a08451a231fdf6c6123437133422af46dc`.
Final head: `62a689366e1429f47030ba60534c7ba7b7f96749`.
Tree: `a4d1c62bb1995342cd1d350810177ef7ea094ed8`.
Worktree unchanged: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi`.

Seven commits:

1. `ea6778f15ea3bb344d611adc9a0247557c8edd23` package/docs/harness.
2. `1a2b0a93e1f6b979a51286c3c114babb3e448657` core R2/R4 folded.
3. `190f8c9f442f0cdad243cf744b1581890104e872` response/paging/operations R5 folded.
4. `2163881fae62258a7c4e6d5eb7acf81850d475ba` facade/auth/transport R1/R3 folded.
5. `3041349ea8e75400edea8204b940abb10153c7c6` vpsAdmin bridge unchanged patch.
6. `e47f7301b6f243f3edca6b9995b6ab93cf027ac2` examples/fixture unchanged patch.
7. `62a689366e1429f47030ba60534c7ba7b7f96749` release/PyPI unchanged patch.

Complete base diff: 62 files +10460/-17. Original reviewed 05e6236 to new head:
15 correction/docs/test files +944/-67; no release/package-metadata change. Lead
inspected exact series and correction stat, diff check/clean worktree/index and
empty migration/schema path inventory. Reviewer inspect complete final series
and correction diff directly for explicit updated history/migration conclusions.

Final exact-head aggregate: declared check.sh Ruff38/mypy18/261 units (1.39s),
bundled actual Rack parser/wire 46 pass (8.22s), Ruby shim syntax/RuboCop pass.
No live generic/vpsAdmin, standalone package smoke or CI yet. No upstream rebase
needed after SSH fetch; base matches. All normal hooks pass/signatures enabled.

Known owner correction commits before fold: core b1b4bdd, response e7dc5f5,
C 30dd87c, package/docs/harness e72cea03. Pre-fold complete tree
`a4d1c62bb1995342cd1d350810177ef7ea094ed8`; four-way fold had no content
conflicts. Exact final tree equals complete pre-fold tree, no added content.
Original reviewed ref `2026-10-19-dynamic-python-api-client-original-review` and
pre-fold ref `2026-10-19-dynamic-python-api-client-before-review-fold` retained.
Normal historical config signatures inspected/signed, no hooks bypassed. Last
three streams stable-patch-ID equivalent to reviewed bridge/examples/release.
No repeated pin/version/generated streams, no migrations or supported old feature
state. No feature merged/released/deployed/externally consumed. Four corrections
folded into owning logical commits, no fixup/obsolete history retained.
