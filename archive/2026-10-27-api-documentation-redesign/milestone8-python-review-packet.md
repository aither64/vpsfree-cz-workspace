# Final M8 supplemental Python correction: affected review

The intended correction is committed, quick checks pass, and history is folded
into the original three groups. This is a related affected review under the
mandatory-change-review workflow before remaining long acceptance. Review the
actual one-file delta and history correspondence; preserve the earlier reviews'
actual scopes. Do not repeat the product/risk review merely to confirm this fix.

Session `2026-10-27-api-documentation-redesign`, workspace
`/home/aither/workspace/ai/vpsfree.cz`; HaveAPI worktree
`worktrees/2026-10-27-api-documentation-redesign/haveapi`, branch of the same slug,
SSH origin `git@github.com:vpsfreecz/haveapi.git`.

## Exact committed range and history

Base: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
Final clean HEAD: `fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413`.
Final tree: `0e72671b95ef3d0893eb83271c4ef2b78993d57a`.

| Group | Complete final commit |
| --- | --- |
| Core | `51073383f063abbc24bf19ca669b9b6e46bb9555` |
| Optional OAuth | `2462dfbac4921e15619ce17736bde9931f6d3fac` |
| Performance | `fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413` |

Affected review delta: previously reviewed/published
`5114746f3a9f87e91c704147c0d99dd4f0d32f02` to finalfb07, exactly
`servers/ruby/test_support/dynamic_python_login_spec.rb`, +3/-11.
Owned SHA256 `bd962c27dafde9e9db18b67169e60096b12d4007e8ff528f4d78b1bd58be52e0`.
All907 other native entries/modes/blobs are unchanged. Full base-to-head inventory
is148paths,+11467/-1282, native count908. The path was unchanged fromf6 at511;
the new fullset is precisely old147 union this one spec, with no removals.

Accepted correction sidecar `da1e8186dc5582b198b6838844d6a50ac07bc0ab` has the
same tree and empty diff to final, but is outside final ancestry. All three
original feature messages remain verbatim. Old Core9508921c, Optionalbdff6c39
and Performance511 each differ from their corresponding new group by the same
one-file binary/full-index patch SHA256
`f133e9129604f6dcef06b1d4e20b5fcad2e3714c96ac3e93fecb1950ec965257`.
Final f6 aggregate is byte-identical to acceptedda1, SHA256
`f468f0edc893f2899604aa88040f7a6e59bb09869a39c49528413f80eccd73c0`.
Main independently verified these identities, ancestry/messages and clean HEAD.

Fold proof and full148 inventory: `history-m8-python-fold-20261029t014637z/receipt.md`,
`final-lineage.json`, `scoped-reuse.json`, range-diff/series/path records. Original
failed147-count proof was retained; only the ignored proof guard was corrected
to148 plus exact pathset equality after main independently confirmed the delta.
No source change, recommit or repeated hook/test resulted from that proof fix.
Unique reviewed511/acceptedda1 recoveries and all earlier d67/e5ea/24ec/other refs
remain. No obsolete sidecar/fixup is retained in final ancestry.

Earlier review chain: full four-lane product/history f6..b869 in
`milestone8-final-review.md`, its requested R3 narrow renderer fix and main step9
reconciliation to e5ea, then completed e5ea..511 general/architecture/scope review
in `milestone8-ci-review.md`. This assignment changes no accepted product,
authentication/provider/config/schema/runtime/fixture/asset contract. Explicitly
reconcile final whole-history/migration/update-stream conclusions using the
bounded correspondence: no migrations or dependency/channel/input/version streams
are introduced; no nonancestor is called literally merged/deployed.

## Problem, correction and preserved contracts

Exact511 release40796243237 ran the full maintained suite, then supplemental
`test_support/dynamic_protocol_spec.rb` and `dynamic_python_login_spec.rb` failed
7/2 seed2782. Both sync/async expectations still required environment-fed
fixture-user/fixture-password/all while accepted M8 rendered user/secret/scope
and required lifetime fixed. Raw completed CI logs and command scope are in
`verification/current-CI-511/receipt.md` and its retained release step8 log.

The correction removes the obsolete HAVEAPI_AUTH/SimpleNamespace/eval shim;
`ast.literal_eval` reads the actual begin_token_login argument, enforcing a
literal-only input map. It checks exact public user/secret/scope/fixed values
and requires a successful description envelope before using its response.
Both renderers still exercise the real Python parse_description/build_request,
exact token request body and mounted URL, required/include-fixed lifetime,
optional interval and missing-lifetime ValidationError. Process failure must
remain fatal; failed envelopes cannot count as success. Independently assess
these claims from the test, owning renderer/fixture and native encoder context.

No new test framework, skip, fallback, installation, environment/input repair,
fixture relaxation, feature or runtime change. No documentation edit is useful:
this updates an internal oracle to the already documented public literals;
shared packaged11 docs and generation inputs are unchanged.

## Actual checks, boundaries and reviewer

Owner1 receipt `verification/python-supplemental-511-20261029/receipt.md`:
existing two-spec supplemental command, seed2782,7/0 (8.95s+1.21s load), scoped
RuboCop1 clean, whitespace clean. Existing prepared Python .venv/rooted3.11.17,
immutable Ruby3.4.11/frozen server bundle; no setup/install/graph changes.
Normal mandatory HaveapiI18n/RuboCop/message hooks pass. Checked/staged/committed
owned bytes are identical. Final folded package/profile quick10/0 seed50232,
exit0/6.271s once; all three ordinary commit hooks pass.2148 protected inputs,
root/server/Rust/Python locks,23roots, flags and908 physical source modes/hashes
preserved; original/scratch indexes and statuses clean. No active utility/test.

Existing actual511 Go32, TS28/44requests, Rust208 dev1.99/MSRV1.95 root+mounted,
allclient214 and ordinary CI results retain their execution labels. Browser and
installed matrices retain e5ea and a06b-built artifact provenance. Reuse requires
their unchanged affected source/input scope; this is no freshfb07 execution or
whole-Git gem/NAR/derivation equivalence. Full final release/artifact acceptance,
SINGLE directf6-to-final performance and peer actual HTTPS/OAuth/deployment remain
pending. No default integration, release or production authorization exists.

Risk MEDIUM for this cross-language verification delta; no production risk
boundary changes. Lanes: general, architecture/repetition, scope/proportionality.
Selected retained reviewer0 is ready, independent, review-purpose/read_only,
saved gpt-6.1-sol/xhigh, native01a18193-44f5-7741-8b6e-6893a0e7f14d. No override
or fallback. Read mandatory-change-review and all selected lane references plus
applicable workspace/repository guidance. Perform review directly, no nested
agents, tests/builds/network or mutations. Report serious concrete issues from
any lane. Return findings, exact range/identity/model/effort, distinct lane and
whole-history/migrations/update-stream conclusions and residual limits. Return
the report to main; do not write files. Main records reconciliation and next gates.
