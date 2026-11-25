# Independent final TypeScript client review

Report received from reviewer0 on 2026-11-14. Preserved by lead; subsequent delivery-only refresh is certified separately in `typescript-delivery-equivalence.json`.

Findings: no Blocking, Important or Advisory finding. This committed development client package's source gate is clear. No package release, WebUI merge readiness or cross-repository task completion is implied.

## Reviewer/scope

reviewer0, retained gpt-6.1-sol/xhigh/read_only; live same-session roster and bound current verified, both environment markers absent with trusted binding matching. No overrides/fallback/nested reviewer. Applied all four current mandatory lanes at HIGH risk, reusing unchanged skill/references already read in this context. Read actual client README, docs/development.md and relevant release guide, current backend synchronization procedure, packet/handoff, design clarification and React SDK requirements. No root AGENTS/contributor file was found; the development guide is the repository's contributor workflow. No edits, tests/builds, CI/provider/runtime operations, push or publication performed.

## Exact reviewed range

vpsadmin-typescript-client 2da950a98fa13468b36d03b13fb5e81cca206e0e..6a5227c156aeef89447abb1f2e68988cecb735f4.
Verified merge-base2da950a9, clean tracked/index state and final tree3da81726365cc5988409fa668c19f94a1b0652a1.
Exactly two commits:

- 77e22636c17cb639fa2837239e3d7bf79e1359c6: raw input/provenance/tooling-lock/generator pin records and generated output.
- 6a5227c156aeef89447abb1f2e68988cecb735f4: handwritten packaged runtime/type tests and nine-line developer reference.

Full diff15files,+1557/-237.

## Input/generation/archive identity

Independently compared committed schema/schema.json, schema/provenance.json and schema/tooling.Gemfile.lock with the frozen backend7919441 export: byte-identical, with hashes f919dcebf8ce5453dce6b0eb09e718f72664b5137443bb8e2064ff6452470ca7, d9f839fac6bf45c5d92d7a7a83cc49a5328a5c136bd7e11539b5c955a5208bdd and 2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0 respectively. Prior independent backend export/repeat assessment is reused; no transformed input is substituted.

The complete schema comparison changes only VPS clone/create/index/replace/show/update: additive outputs on clone/create/replace, selected inputs/outputs on index/show, and settings inputs on update. Resource/action inventories are unchanged. The generated set remains677files, no additions/deletions. Every manifest-owned file hash matches its committed Git blob; only the six VPS modules and root schema constant change. All generator tooling hashes match. Generator revision1ef9b204ba45bb261d3334be5c555cc1856b713b/version0.32.2, source digest, Prettier3.9.10/config digest and runtime import are retained. Package/version0.4.0 and actual haveapi-client0.32.0 dependency are unchanged; the Ruby schema/generator identity0.32.2 is distinct from that JS runtime pin.

Independently inspected the named development archive:341450bytes, SHA256fee3800140869c1f721c5a07eda3e438d1a347690dc89aa5f8379a9efc1663bf,1364unique ordinary-file/directory entries with safe package paths. Embedded schema/provenance/exporter lock/generator record/ownership manifest/package.json equal final Git bytes; archived dist bytes equal the inspected built output. No registry artifact is inferred from the unchanged development version.

## All-four-lane assessment

General: generated fields/types/descriptors match the recorded schema and current backend. Initial Index/Show selectors remain optional and descriptors inject no server defaults. Selected queries preserve the explicit policy/status and false boolean. Update override inputs preserve explicit null and numeric types; permission is non-null boolean. Summary members remain optional/nullable by the existing generator's response convention; datetimes stay wire strings, and absent capability is not synthesized as zero/default state.

Architecture/repetition: generation remains owned by pinned HaveAPI, with handwritten package code outside src/generated. The unchanged shared runtime owns primitive/null/path validation and passes through executor errors/metadata. No local enum generator, registry copy, choice shim, provider fork or handwritten generated member was added. Registered/status strings deliberately retain server validation, preserving the raw validators in the schema. The new runtime/type coverage tests the package boundary without reimplementing backend policy or permission checks.

Scope/proportionality: this is the current procedure's required generated synchronization after the user's rebase exposed React's new SDK dependency. It adds the accepted incident contract, without a new API mechanism, runtime dependency upgrade, package bump/release or speculative abstraction. Tests/docs are directly supporting the generated changes. No unnecessary subsystem found.

Risk/compatibility: new inputs are optional so existing callers remain compatible. New clients can read old APIs without sending incident selectors and detect returned capability before enabling new calls. The SDK cannot establish server availability or permission from generated structure. Actual server errors remain errors rather than local “not sent” validation failures. Null resets and false survive the real runtime's JSON/query serialization. Synchronous metadata remains unmodified; absent/null state is allowed by the backend contract, while any supplied malformed receipt remains the consuming application's existing responsibility. Restoring an older candidate requires restoring its input/provenance/generator/output together; this cannot undo writes already accepted by a server.

Representative actual React context was inspected read-only: current getApi uses generated operations through the existing policy executor; VPS list/detail/settings adapters use the new types, omit initial selectors, preserve explicit null/false, and retain the isolated synchronous exception plus supplied-receipt checks. The portable file:packages/*.tgz candidate is an allowed development boundary. This is context inspection only, not a final review or certification of pending React source/tests. Go/Rust candidates likewise remain separate.

## History/generated stream/migration conclusion

The complete series has one final schema/generation stream in77e22636 and one independently reviewable handwritten test/doc commit. There are no superseded pins, fixups, obsolete generated approaches or repeated dependency/generated update streams. The refreshed exporter lock is provenance for the one raw input stream, not a runtime dependency upgrade. Handwritten runtime/package/lock/toolchain/regeneration code is unchanged. No migrations or client persisted-state conversion exist; backend migration versions in provenance are source evidence, not TypeScript-client migrations.

## Documentation: explicit seven-question conclusion

1. README remains the public purpose/install/use entry point and links the development and release guides.
2. docs/development.md is the proper contributor reference/how-to home for incident selector/optional-output/wire/null semantics; the API synchronization process links to its single backend owner.
3. New text remains useful after this initiative and contains no branch-specific execution state. Exact archive/check/head records stay in the session packet/handoff.
4. Prose matches source/tests: optional initial reads, capability checks, null/false preservation, primitive strings with server choices, wire-string datetimes and synchronous outcome limits. It does not claim a live API or published candidate.
5. No documentation move or deletion loses prerequisites, error/retry guidance, permission boundaries or release recovery.
6. Old-API capability ordering and the published-release-before-WebUI-merge rule remain explicit in the owning synchronization procedure; restoring a generated snapshot remains a matched-input operation. No supported path is retired.
7. Working README/guide/API-procedure links retain one authoritative explanation for each contract. Exact development versions serve maintained reproducibility/compatibility pins, not an invented release.

Placement/preservation conclusion: appropriate, no documentation gap requiring correction; no user-visible translations or KB pages/media changed.

## Evidence and limits

Inspected pinned quick log: build, typecheck, strict consumer typecheck, npm15tests/0failures and test:package PASS. Inspected regeneration --check receipt and exact named archive check log; owner reports native0. The packed consumer runs the actual published JS runtime against a local controlled HTTP server, proving omission, selected queries, null/false bodies, primitive/null pre-dispatch refusal, server-error propagation and synchronous metadata without inventing a transaction. It is not a live backend permission/registry/physical-stop test. Full source/input hashes and archive equality are established read-only; no reviewer rerun was launched.

## Verdict

No required source fix; source clearance for2da950a9..6a5227c1. Feature publication/checks may proceed under lead coordination. Final React/Go/Rust packages and their review/checks remain separate. A published TypeScript release containing these members is required before the dependent WebUI merge, with temporary file dependency removed then; no version/tag/publication is authorized here. Backend capability rollout, real CI/runtime/browser/KB acceptance, old-run/claim completion, default-branch integration and lifecycle remain outside this report.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
