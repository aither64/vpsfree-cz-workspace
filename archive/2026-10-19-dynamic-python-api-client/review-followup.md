# Independent affected review: corrected branch

Reviewer0 completed review 2026-10-20, same retained gpt-6.1-sol/xhigh/read-only
thread and all lane references, no override/fallback/nesting. Lead records this
faithful summary; full report retained in conversation, reviewer wrote no file.

Reviewed base c58704a08451a231fdf6c6123437133422af46dc to head
62a689366e1429f47030ba60534c7ba7b7f96749, tree
a4d1c62bb1995342cd1d350810177ef7ea094ed8. Original full review05e6236 remains
authority for unchanged package/release/bridge/examples content. Examined entire
15-file correction diff +944/-67, updated tests/docs and complete seven commits.

Result: **no Blocking finding, one Important test finding**. GET public contract,
shared ownership, proportionality and updated whole history accepted. Fix F1
directly, no additional confirmation rereview required for exact expected-value
correction.

## Important F1

`clients/python/tests/integration/test_ruby_server.py:160,170-173,191,201-204`
expects tuple rows/nested tuples for new GET/DELETE wire echoes. Python-only
fixture declares hash output, whose ordinary lists/dicts are intentionally
preserved by adaptation. Both mode tests would fail before verifying DELETE.
Pure read-only adaptation reproduction confirms returned rows are list and
tuple comparison false. Change only assertions to original dense_rows/json_rows,
retaining nested empty/list/dict/bool/number/null values. Production unchanged.
Fold into owning unmerged package/harness commit; lead inspect/check directly.

## Accepted affected conclusions

- GET lossless subset is grounded in actual Rack semantics. Guard rejects
  supplied empty containers, sparse/differing-key rows, nested arrays, row
  containers and ambiguous keys; sorted equal-key dense rows round-trip. Typed
  scalars and declared nullable Custom remain distinct from Custom string-only
  nested leaves. Empty structural wrappers may omit without supplied-value loss.
- JSON POST/PUT/DELETE retains expressive values and actual server object-root
  requirement; no indexed-array, JSON-stringification, marker/default insertion,
  invented namespace or method override introduced.
- Ordered URL query construction preserves pair order, escaping and mount/path
  validation. GET guards precede action I/O; DELETE follows JSON metadata branch.
- README/contributor guidance accurately states public boundaries and literal
  Custom vs unknown types. Lasting contracts stay in project docs, decision
  history in session records.
- Unit and real-parser wire coverage meaningful; prepared actual server tests
  have correct purpose but F1 expectations need correction. Bundled Rack test
  uses declared Gemfile, no global dependency assumption.
- Query Custom validation and structural flattening have distinct shared core
  responsibilities, no cross-facade policy duplication or generalized parser.
  Helpers proportional to demonstrated corruption, no vpsAdmin runtime overfit.
- R1/R2/R3/R5 exact narrow fixes were lead-inspected/tested and context for this
  review, not standalone confirmation reruns. No material new auth/binding design.

## Updated whole-history and migration conclusion

Seven commits: ea6778f package/docs/harness;1a2b0a9 coreR2/R4;190f8c9 responseR5;
2163881 facade/auth/transportR1/R3;3041349 vpsAdmin bridge;e47f730 examples;
62a6893 release. Reviewer independently verified exact pre-fold tree equality,
range-diff equivalence of unchanged bridge/examples/release streams. No fixup,
obsolete approach or intermediate encoding/auth behavior in final ancestry.
Dependency ordered split remains reviewable; no new unrelated bundle. No repeated
pin/generated stream: pyproject/uv.lock once, flake.lock unchanged. Backup refs
preserve evidence outside final ancestry. Fold F1 into owner before readiness.

**NO MIGRATIONS:** no schemas/transitional lineage/new persisted server formats;
no feature merged/released/deployed/externally consumed, no supported Python
consumer/pin requires intermediate state. Disposable vpsAdmin DB is test infra.

## Verification and limits

Reported exact-head261 unit/mypy18/Ruff38 and46 bundled Rack cases accepted as
quick evidence. Reviewer ran only tiny read-only adaptation reproduction with
PYTHONDONTWRITEBYTECODE, no setup/server/smoke/CI/write/lifecycle operation. Source
and index stayed clean at exact reviewed head. Live generic/vpsAdmin, standalone
package and exact-head CI still required after F1; end-to-end registry setup/
OIDC publishing and actual node/VPS lifecycle remain outside current evidence.

Lead accepts F1 and grants exact test correction/fold. No further review needed
for only that narrow fix; changed public boundaries would need affected lanes.
