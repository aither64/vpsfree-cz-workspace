# Rust generator and actual client verification

## Current integration verification (2026-10-21)

HaveAPI implementation merged ate09142ad241bd63fc4c014ca3afa50ad75106103.
Root READMEfollowup a32b15e379f44fc6dae4b15ef4ec17a142e5f465 subsequently
merged on2026-10-22: oneRustgeneratorclients-list entry, independent general
review/mandatoryhooks passed, no code or build-inputchange. No CI triggered
for README-onlypush; priorimplementationCI below remains correctly scoped.
All six automatic default-branch workflows passed, including the complete Rust
unit/style, runtime fmt/default/blocking/Clippy and generic server acceptance
steps. The release workflow's publication job was skipped (build-only push).
See artifacts/haveapi-default-ci/result.json and
artifacts/approved-default-integration/haveapi-default-remote-proof.txt.

The final extracted-gem/API7 proof passed in29.12s under current HaveAPI
Ruby3.4.11 with the client's own rustfmt1.9.0 explicitly selected. It compares
current package payload, extracted-library ownership, the full manifest/all686
Rust files and read-only --check; artifacts/integration-formatter-acceptance/result.json
and generator-package-formatter-acceptance/result.json. No old archive-byte
reuse is claimed for changed package documentation.

Final client945af6a97717a7a6373507bbc9592d5cd53727c2 CI39600821857 passed
async/blocking/examples/docs/package/MSRV1.95/regeneration with its own unchanged
inputs. Its exact recorded compatible HaveAPI source68cc is publicly retained.
Client main was fast-forwarded to945af6a on2026-10-22 after the coordinator
update enabled ordinary registered-repository claims. Fresh default-branch
CI39739951412 passed all four jobs, observed by a new Luna/low utility. Remote proof and merge
evidence: artifacts/client-default-integration-20261022. No source changes
or test repeats were needed for the unchanged reviewed/verified head.

Final committed affected reviews: final-review-integration-rebase.md and
final-review-formatter-fixtures.md, retained reviewer0 Sol/xhigh/read_only,
all four lanes, no unresolved findings. Complete3+4feature histories are clean;
no obsolete approaches, migrations or repeated update streams.

Failures preserved: initial wrong-cwd launch did not reach software tests;
corrected68cc Ruby generator/package checks failed the exact rustfmt1.9/1.10
guard. Architect Clarification7 led to bounded temporary-fixture/docs correction,
keeping production guard and source bytes. Fresh finale091 tests passed; old
failed receipts were never relabeled. All current receipts bind exact inputs.

No releases, tag, publishing dispatch, registry upload or credential read.
The earlier catalog-authority blocker is resolved through the updated coordinator;
both approved default-branch merges are complete. No releases were performed.

## Historical implementation acceptance (2026-10-19)

The records below bind their historical heads; current baseline verification is
reported above. Original full acceptance remains useful within independently
reviewed unchanged input scopes.


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


## User-focused README follow-up

The later README-only commit c4a0f597cd3602e28ae11846962e2d1e07a0c1ff
refocuses installation and examples on library consumers. General-lane review
found no Blocking/Important issues; one packaged-link Advisory was fixed and
directly verified. A fresh Cargo publication dry-run passed at this clean head
(exit 0, 34 seconds); no upload occurred. Exact-head CI run
[39316994971](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/39316994971)
also passed async, blocking, MSRV and regeneration. The changed README archive
payload was freshly checked; original archive bytes are not reused.

The user selected GitHub Actions trusted publishing. Architect Clarification 6
and trusted-publishing.md describe a separate client workflow change and
registry-owner prerequisites. Workflow implementation is committed at 091bd70 with Actionlint/ShellCheck and
26 positive/negative gate checks passing. Independent four-lane review passed
with no findings; workflow feature push091bd70 is published and exact-head
CI run39318944837 passed all four jobs, confirmed by a fresh watcher; no local
Cargo login or upload, release tag, registry setup or default merge occurred.
