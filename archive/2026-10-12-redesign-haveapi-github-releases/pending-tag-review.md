# Pending-tag correction: independent final source review

No Blocking, Important or Advisory findings in either complete candidate.
Retained reviewer0, native thread01a1309b-3a6c-7cd2-917f-4426d9b48c52,
turn01a15592-4953-78d1-8237-ffd406b099e1; verified saved actualgpt-6-astra/xhigh,
read-only, exact session identity, no overrides/fallback/nested agent.

Reviewed canonical vpsfreecz/haveapi over SSH:
- Master target refs/heads/master:526648131af45df68c25ac0042a52f22c7a81df5..
  c58704a08451a231fdf6c6123437133422af46dc.
- Release target refs/heads/haveapi-0.29:7fb218e28a86ab1d27de74ccb92c2a45063a4f78..
  355c2990a4bfd3940d3234cb2077ad0127f43551.
Both exact heads clean; bases actual merge bases. Full diffs match packet:
masterd167becfbde081587435ccbf187b990f1d9bbae7be6f72d286babbdadbaae1ec,
release711ac41d8b47839560fa3c9250fe27795cd6ebd8872e46730239ac49783ee758.

All four lanes reviewed directly. GraphQL pending-tag -> databaseId -> REST-ID
sequence matches exact gh2.102.0 implementation. Only explicit null is absent;
errors at either stage stop before creation/upload. The reviewer independently
introspected live schema: Repository.release(tagName:String!) returns Release,
Release.databaseId is Int. Same query resolved published cli/cli v2.102.0 to
ID399674740. A deliberately invalid field returned exit1, confirming GraphQL
semantic errors fail through the shared github_api status check.
Sources: https://github.com/cli/cli/blob/v2.102.0/pkg/cmd/release/shared/fetch.go#L219
https://github.com/cli/cli/blob/v2.102.0/pkg/cmd/api/api.go#L477
https://cli.github.com/manual/gh_api

Nine focused examples cover synthetic REST draft name, existing/new draft,
published release, null,403/404 at either stage and absent post-create lookup.
These model upstream contract, not a captured actual user draft. Creation keeps
--verify-tag; artifact byte comparisons, source/run/hash reuse, approval/secrets,
registry checks, PHP preflight/atomic push and finalization remain intact.
Version0.29.12 metadata/dependencies/bundle/changelog agree; runtime-byte proof
againstv0.29.9 passes with only version declarations different. Existing tests,
Elixir, runtime/API/protocol/state/mixed-version/rollback unchanged. Master0.29.0.

Publisher and CLI/Makefile/workflow consumers retain ownership; github_api owns
two-call JSON/error handling without a new framework/interface/schema/privilege.
Helper/spec/procedure files byte-identical in candidates. Permanent release
procedure explains original tagged-source reruns and new authorized versions for
source corrections. Nearby comment and changelog accurately explain behavior.

Complete new history: masterc58704a only; releasec8cfb16 fix/specs/docs then355c299
version/changelog. Coherent split, no obsolete new approaches/fixups/shims or
repeated pin/dependency/generated-update streams; no pins change. Prior master
and release series are already merged/tagged and consumed by approved runs;
preserve both real source/artifact boundaries. No migrations or transitional
lineage; no migration merged/released/deployed/externally consumed.

Reviewer checked exact-head quick receipts,30normal+30runID123 examples, Ruby lint
243/244files, syntax/whitespace, old repro9/8failures and runtime/history proof.
Both original artifact sets independently rehashed:0.29.10 manifestb0b8600e...,
0.29.11manifest80006e3a986ba713401587f5067c58358f320bf54a681c55d27b31055779dfcf;
source/version/tag/run and all file hashes match. Failure evidence confirms
credentials/registry/PHP steps skipped; exact-version registry checksall404.

Limits/gates: actual pending-draft lookup under an authorized write-capable
identity remains unverified. User's read-only diagnostic is required before any
new tag; public release/schema and mocks do not substitute. Fresh full local and
safe CI still outstanding at review time. New master integration and0.29.12tag
need fresh authorization; human protected environment approval remains mandatory.
Actual OIDC/deploy-key/Packagist use untested; cross-registry partial publication
remains possible. No long tests, source/tracking edits, publication, approvals or
lifecycle actions in this review. Session staysopen.
