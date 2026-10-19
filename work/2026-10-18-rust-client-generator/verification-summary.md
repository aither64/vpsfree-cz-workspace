# Rust generator and actual client verification

Implementation, independent review and final branch/provenance reconciliation
are complete. All local gates and remote CI passed. API target 7.0,
public capture SHA 70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d.
The snapshot has 152 resources, 524 actions and 8720 parameters; plugin completeness is
unknown. It was not replaced or combined with local authenticated metadata.

| Gate | Evidence and result |
| --- | --- |
| Independent review | final-review.md and final-review-delete.md; initial two Important findings fixed, correction review no new findings |
| Runtime | corrected-acceptance/runtime.result.json; default/blocking tests and strict Clippy passed |
| Actual client | corrected-acceptance/client.result.json; both features, examples/tests/docs and Cargo package passed |
| MSRV | corrected-acceptance/msrv.result.json; exact Rust 1.95.0, same lockfile, both feature sets passed |
| Packaged generator | corrected-acceptance/generator-package.result.json; extracted gem generated identical Rust source and ownership manifest (686 Rust files) |
| Generic real/scripted API | fixture-final-checks/generic.result.json; root and mounted paths, both transports, strict DELETE JSON and GET control, auth steps, errors and partial fields passed |
| Actual vpsAdmin | vpsadmin-token-prereq/watcher-result.txt; 2 tests passed against a disposable source fixture, including VPS update, paging, nullable DNS TTL, Custom JSON and token request/use/renew/revoke |
| Public read-only smoke | live-public-recheck/watcher-result.txt; async and blocking public_stats HTTP 200, no auth or mutations |

Result paths in this table are relative to `artifacts/`. Exact source heads,
commands, timing and full logs are retained alongside each result. The public GET
smoke preceded the DELETE-only classifier correction; its code and method are
unchanged, so it was not repeated just for that correction.

Real generic acceptance exposed a DELETE encoding defect: the server reads JSON
for DELETE, and the runtime initially used query parameters. Corrected shared
classification and copied runtime received affected-lane independent review and
fresh runtime/client/MSRV/package/real-server verification. No server change,
retry/fallback or schema expansion was introduced.

Several fixture assumptions were corrected against canonical code/tests:
required empty strings, Ruby constant/action naming, path ampersand escaping,
short MariaDB socket paths, valid DNS ownership, allowed WebUI namespace and
node availability needed by enabled login notifications. Exact input/metadata
and all token assertions remain. No production mutation, credentialed production
request, release, registry publication or default-branch merge occurred.

Final heads: HaveAPI 9e4c29a0412a25256ce944641f60ba13e9f03c2b and
client 62753f006d7bd3e5befe1033c49a2c630ca3ff02. The final history addendum
(final-review-history.md) accepts three/two logical commits, clean upstream
rebase equivalence and scoped reuse of exact component, lock and Nix inputs.
Both feature branches are published; client main is the neutral empty root.
All five exact-head HaveAPI CI workflows and the client workflow passed. The
client run includes async, blocking, MSRV and regeneration jobs. HaveAPI release
publication was skipped on the feature branch. Exact run links, heads and job
conclusions are retained in [the CI result](artifacts/final-ci/final-summary.json).
No authorized workflow remains active. The initiative is ready, awaiting merge
approval, and stays active until explicitly authorized integration meets the
workspace completion criteria.
