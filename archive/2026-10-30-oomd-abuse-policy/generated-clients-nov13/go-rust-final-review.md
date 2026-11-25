# Go and Rust final generated-client review

Report from reviewer0, received 2026-11-14 and preserved by lead. Subsequent narrow G1 remediation requires separate lead closure.

No Blocking or Important findings. Source clearance for the exact completed Go/Rust packages below, with one Advisory and the verification limits retained. This is independent final source review, not release, integration, live-server or overall cross-repository acceptance.

## Findings

**G1 — Advisory, general/risk: new Go test requires a newer standard library than the module declaration.** `vpsadmin-go-client/client/incident_policy_test.go:35`, commit `f36796b9763fdef82aad3b5662265f90e5a027e5`, calls `url.Values.Has`. The installed Go API inventory records that method as added in Go1.17, while `go.mod:3` remains `go 1.16`. Thus the repository test suite will not compile with1.16. Generated library code and existing consumers are unaffected, and the pinned1.26.10 pass is valid. Small optional outcome: replace this presence test with a map-key lookup; no dependency or generator change is needed. I did not run an old compiler or edit the test.

## Identity, settings and exact scope

Bound tracking-CWD `dev-session current` matched `2026-10-30-oomd-abuse-policy`; both DEV_SESSION markers were absent, matching the trusted exact developer binding. Live same-session roster verified reviewer0 ready / purpose review / read_only / gpt-6.1-sol / xhigh; no overrides, fallback or subagents. All four lanes completed after reading mandatory-change-review and its current general, architecture, scope and risk references, applicable workspace procedures, both repository AGENTS and contributor guides, and vpsAdmin's API-schema synchronization procedure.

- Go: `af9a819ca35f6de5556092679b4df7cb72e7aa89..f36796b9763fdef82aad3b5662265f90e5a027e5`, tree `4d261fbd312b30d58cb376f88f90e5dc60801752`.
- Rust: `823a4f8450fce4947310fc81bcdebdca91d9ffae..9157c271b6a5446aaf5e3809a82b5b486441e4fb`, tree `63856abcecf4cd3d3110961b3e9b1dca3c1860cd`.

Both exact heads, trees, merge bases and clean statuses independently matched. Inspected complete series/final diffs, raw inputs, generated sources, serializers/decoders, tests, contributor documentation and native logs. No tests/builds/check scripts/CI or mutations were launched. Prior backend export review is reused; TS and pending React work are context only.

## Four-lane conclusions

**General:** The changes match the user-requested rebase and the current upstream requirement to synchronize all clients with the final API source. Go's13-file +2946/-417 and Rust's15-file +2494/-269 diffs mainly contain saved schema/provenance and conventional generated output; handwritten additions are focused tests and short contributor reference. The raw schema has exactly103 added incident parameter records in six VPS actions, with no removed or modified existing record. Reviewed all19 summary members across Index/Show/Create/Clone/Replace and the8 new inputs across Index/Show/Update. Types, wire names and timestamp strings match the raw contract. The tests exercise supported omission, null/false, isolated ordinary updates, summary decoding, synchronous metadata absence and server refusal rather than claiming server registry acceptance from a successful mock.

**Architecture/repetition:** HaveAPI remains the sole generator/runtime owner. Both clients retain provider `1ef9b204ba45bb261d3334be5c555cc1856b713b` /0.32.2. Independently matched every Go recorded provider-source hash to that own generator checkout; generator configuration/source inventory and generator lock are retained. Go's raw-to-effective structural difference is solely `description.authentication.oauth2.revoke_url`, using the unchanged bounded helper. Its existing origin-trust protections are unchanged. Rust's generated ownership manifest covers688 files, with exact file-set and byte-hash agreement, no additions/removals; copied runtime bytes match maintained HaveAPI source and are unchanged from base. Rust generator/runtime/toolchain identities and configuration are retained. Repeated action declarations are provider output, not divergent handwritten policy. No new enum generator, duplicated registry, transport shim or provider correction was introduced.

Actual Go consumers were derived from canonical repository manifests: Terraform provider `29b47dd96c292dfa35412c8a5f21f8383cf90ddc` pins client `1d9240f3d27b`; vpsf-status `5f6db13103bf652e69b7b879a69e98794075e64e` pins `45a5170b7190`. Representative Terraform Show, Index and Update callers retain selected-input behavior and existing accessors. Their pins are unchanged by this package, so this is no certification of downstream upgrades/tests. Rust's in-repository examples/tests remain on its owned async/blocking interfaces; no downstream pin update is part of this range.

**Scope/proportionality:** The synchronization is necessary because new upstream React uses the generated SDK and the API contributor procedure requires all three clients to be assessed. The package adds no rule builder, production type, provider feature, permissions mechanism, release workflow or compatibility framework. Existing Go scalar-null behavior is documented rather than expanding the generator. Handwritten test coverage is proportionate to the new client-facing fields and existing runtime boundary. No unnecessary subsystem or obsolete implementation remains in either final range.

**Risk/compatibility:** Initial Index/Show calls omit the incident selector, including reads selecting an existing limit. Explicit selector/status/false filters reach the existing encoders; Go's false query representation remains numeric0, Rust's remains textfalse. Both update encoders preserve explicit null resets and JSON false without unrelated input. Rust `InputValue::Unset`/Null/Value, parameter specs and shared protocol enforce primitive/null rules; names/status remain server-validated strings. Unknown registry strings follow the normal server-error path. Optional Rust outputs map absent/null to None. Go retains its documented scalar zero-value conflation for absent/null/false/zero, so callers must not infer capability or authorization from zero values. Generated structure grants no server permission.

Synchronous updates decode without inventing an action receipt; existing Go IsBlocking is nil-safe and Rust optional action_state_id remains None. Async and blocking Rust calls share the inspected preparation/decoding path; no transport/retry/authentication behavior changed. Old APIs require capability gating before new fields are sent; compatible API support must be available before enabling these calls. Source synchronization is not API deployment or package release. Recover by restoring schema/provenance/generator inputs/output together or pinning an earlier client; that cannot undo accepted server writes. No current runtime/deployment ordering defect found inside this boundary.

## Input, whole-history and migration conclusions

Independently verified both committed raw schema/provenance/exporter-lock copies are byte-identical to the reviewed final API7919441 export:

- schema `f919dcebf8ce5453dce6b0eb09e718f72664b5137443bb8e2064ff6452470ca7`;
- provenance `d9f839fac6bf45c5d92d7a7a83cc49a5328a5c136bd7e11539b5c955a5208bdd`;
- exporter lock `2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0`.

Go effective schema is `948586828973a22f614182c4e534bafd5ffa66b4fe9155e76b12ca7b179d492b`. The unchanged projection helper hash is `92a56fbc9056bda008b6e7c7c47c3f6b95f15e665f6158a593f1c93811f0e019`. The Python execution-path/version receipt update records the actual existing shell interpreter, not a shell or dependency upgrade. Rust copied-runtime identity remains `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`.

Go complete series is exactly `356417d8abce2ed2e3a46f1e22f51b6cdd206b5e` generated refresh, then `f36796b9763fdef82aad3b5662265f90e5a027e5` handwritten tests/docs. Rust complete series is exactly `d0f4c3d038151a72714915bccf7afccccb31854d` generated refresh, then `9157c271b6a5446aaf5e3809a82b5b486441e4fb` handwritten tests/docs. Each split is coherent and independently reviewable; messages describe the final outcome/rationale. Each has one final schema/generation stream, with no superseded input, obsolete fixup/transitional history, repeated dependency/pin stream or unused compatibility path. Consolidation is satisfactory.

Go owns684 generated files before/after; Rust owns688 before/after, excluding its ownership manifest. Neither removes/adds generated files. Client module/package manifests, runtime dependencies, generator locks/configuration and shell inputs are unchanged. The refreshed exporter tooling lock is retained raw API input, not an authored client runtime/dependency upgrade. **No migrations in either client range.** Backend migration inventories inside raw export provenance are source evidence, not executable client migrations; no transitional client schema/state needs preserving. No release, deployment or external-state conversion is introduced.

## Documentation placement/preservation: seven questions

1. Reachability/entry points: Go's existing README “Development and regeneration” remains the owning contributor entry point; Rust README links `docs/development.md`. Basic usage/authentication warnings remain accessible.
2. Audience/home: new selector, nullability, capability and response paragraphs belong to SDK contributors/client reference in those existing homes. The shared synchronization/rollback procedure remains authoritative in vpsAdmin `docs/api-schema-export.md#generated-client-synchronization`, linked by both guides; individual execution evidence stays in the session packet/logs.
3. Durable usefulness: guidance describes source behavior without requiring private session context. Go's exact API source revision is generation provenance, not an unverified rollout claim. No temporary branch checklist was added to product docs.
4. Fidelity/evidence: omission/null/false/scalar behavior matches the inspected serializers and native focused results. Guides distinguish saved-input consistency, API freshness, server capability and release/deployment. The packet honestly retains corrected failed invocations and Rust compilation-only attempt.
5. Preservation: no documentation moves/deletions; existing authentication, unsupported Custom-input limitations, uncertain-write/retry warnings, generation ownership and failure prerequisites are preserved.
6. Upgrade/rollback: existing Rust compatibility/release section and shared API synchronization procedure preserve old-server capability gating, client pin recovery, source/input restoration and the limit that client rollback does not reverse server actions. No supported upgrade/recovery path is retired; no new migration or persistent format requires an additional upgrade runbook.
7. Authority/links: linked local guides/input artifacts and the shared synchronization anchor resolve in the inspected sources. Behavior is explained once per owning client, with common workflow linked rather than copied. Existing Go README regeneration placement is a reasonable local-layout equivalent; no unrelated docs restructuring is required. No KB page/media/UI prose is changed here.

Conclusion: documentation placement and consequential preservation are satisfactory, with G1's minimum-test-toolchain caveat above.

## Verification evidence and remaining limits

Inspected existing native logs: Go fresh generation and full-set comparison684files (recorded exit0); `go test ./...` succeeds and Python schema-helper4tests pass in `incident-client-go-quick-fixed.log`. Original two expectation failures remain retained: false query was already0 and body already included empty_meta; only test expectations changed. Pinned Go1.26.10 is the demonstrated compiler, not minimum-Go proof.

Rust quick log supports format/shell/provenance checks and7provenance tests; corrected refusal log has10tests passing; deterministic regeneration is recorded exit0. Original missing-env invocation remains a failure. `incident-client-rust-focused-corrected.log` actually runs3tests,3passed/0failed/0filtered; earlier `incident-client-rust-focused.log` ran0tests/3filtered after compilation and is **compilation-only**. Existing generated dead-code warnings remain. I did not rerun any checks.

Rust full default/all-targets, blocking matrix, docs, package and Rust1.95 minimum-compiler gates have not been established by this package and are not certified. No live API/browser/guest, authorization integration, registry publication or deployed capability acceptance is established. TS delivery certification is outside this new review; React/KB/client publication and broader task completion remain separate gates. No merge/deploy/lifecycle or old-run completion authority is inferred.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
