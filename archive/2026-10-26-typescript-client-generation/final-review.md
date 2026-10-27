# Independent final review — TypeScript client generation

**Result: no Blocking findings; two Important findings require remediation before longer verification.** The lead has accepted both for fixes. This report reviews the original immutable packet heads below; subsequent remediation is not included.

## Findings

1. **Important — reject unsupported GET object-input metadata during generation.** General/risk lanes. HaveAPI parser `257819397309a87d9cbfacd8a01af411e1a329ff`, `clients/typescript/lib/haveapi/typescript_client/ir.rb:99`; emitter `9b7afb2c8a0e2981a48985b2ed79cf2d0b104f0d`, `clients/typescript/lib/haveapi/typescript_client/emitter.rb:100` and `clients/typescript/template/runtime.ts.erb:145`.

   The IR accepts a GET action declaring object-input metadata, and the emitter exposes it under `params._meta`. Required metadata also makes the generated options/params required. The generated runtime then rejects every supplied object-metadata object on GET with “Object metadata query input is unsupported by HaveAPI 0.30.2”. For required metadata, omitting it fails the required-field check and supplying it fails the query check: the generated operation has no successful invocation.

   An in-memory source probe confirmed that a GET action with required object-input `revision: Integer` passes IR construction and emits a required `"_meta": Widget__IndexObjectInput` field. The smallest fix is to reject this unsupported schema combination in IR with its `meta/object/input` path before generation writes anything, keeping the existing runtime safety guard. Add a regression proving the diagnostic and unchanged/missing output destination. Do not add another query encoder or transport implementation. The current vpsAdmin snapshot contains **zero object-input metadata groups**, so its emitted operations are unaffected.

2. **Important — validate nested structural machine endpoints in the snapshot boundary.** Risk/architecture lanes. HaveAPI parser `257819397309a87d9cbfacd8a01af411e1a329ff`, `clients/typescript/lib/haveapi/typescript_client/snapshot.rb:48` and `:108`.

   `from_description` copies nested structural `help`, `path`, `*_path` and `*_url` values without validating them. Later validation checks the envelope source URL and direct authentication provider fields, while IR checks application action paths; neither checks nested association endpoints. A Resource parameter containing `choices.help = "/v1.0/widgets?token=synthetic-marker"` survives `from_description` and successful IR construction unchanged. A caller saving the canonical snapshot can therefore retain a credential-bearing or otherwise invalid machine endpoint despite the specified endpoint-validation boundary.

   This is also a concrete policy divergence from the existing Rust snapshot capture and the new vpsAdmin exporter, which validate structural endpoints during traversal. Restore this validation in capture and saved-snapshot validation, or remove unused capture helpers in favor of an authoritative producer. Allow only the supported `help?method=...` query; reject credential-bearing/query-bearing URLs and unsafe paths. Preserve arbitrary real data under Custom/default objects and validator choice keys. Resource `choices`/association endpoint descriptions remain structural; validator `include.values` choice keys remain data. Add nested endpoint regressions rather than another broad abstraction. The committed vpsAdmin exporter already performs these checks; **no current artifact credential leak was found**.

No additional actionable finding was established in the assigned scope.

## Identity, scope and revisions

Reviewer: retained `reviewer0`, thread `01a177e7-c4ad-7893-b980-0807c3ec58b3`, purpose `review`, saved `gpt-6.1-sol/xhigh/read_only`; no model/effort overrides, fallback or nested agents. `dev-session current` from the bound tracking directory returned `2026-10-26-typescript-client-generation`. Both DEV_SESSION identity variables were absent, and the trusted developer binding supplies the matching absolute workspace/session identity. The live roster confirmed the retained reviewer identity/settings.

Read the complete review packet, plan/state/design, workspace/repository AGENTS and applicable procedures, mandatory-change-review skill and all four references: general, architecture/repetition, scope/proportionality, risk/compatibility. Risk classification is **high** because this introduces a reusable generated public contract and a destructive-test-fixture database boundary.

Reviewed complete series and final source changes:

| Repository | Base | Reviewed head | Series |
| --- | --- | --- | --- |
| HaveAPI | `ec84ec874eb209ab59848873998456293ddf3c52` | `9b7afb2c8a0e2981a48985b2ed79cf2d0b104f0d` | `257819397309a87d9cbfacd8a01af411e1a329ff` parser/orchestration; `9b7afb2c8a0e2981a48985b2ed79cf2d0b104f0d` emitter/runtime/tests |
| vpsAdmin | `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5` | `cfe245130badcf2ac8ad8dd69f758ee4da618430` | One exporter/tooling/documentation commit |
| vpsadmin-typescript-client | Empty root `6c67b3c6e10e4096f6717345026371a89691f62a` | `a914514bf7042c6824335f4341f52e55a6347ff0` | One initial generated-package commit |

The supplied bases are ancestors and the actual merge bases for these ranges. Commit counts are 2/1/1. All three worktrees were clean at inspection; range whitespace checks passed. No fetch, push, integration, production access, implementation mutation or long test was performed by this reviewer.

## Whole-branch history and migrations

- **HaveAPI:** The two final commits separate parser/output orchestration and emitted facade/runtime behavior, with an explicit dependency. Tests, docs and source/version registration support their owning behavior. The final branch introduces one design directly; obsolete parser fixes and intermediate emitter revisions are not retained as follow-up/fixup commits. **No obsolete history, repeated dependency/channel/generated-pin update stream, migration or transitional migration remains.**
- **vpsAdmin:** One coherent export capability, with its isolated bundle, safety checks, snapshot tests and operating documentation. Normal API dependency pins and database schema/migrations are unchanged. Plugin migration versions recorded by provenance are existing migrations applied only to the disposable fixture. **No obsolete history, repeated pin stream, new migration or transitional migration remains.**
- **New client:** The empty root is honest registration provenance, not a preexisting upstream implementation or integrated default. I independently accept the single initial package commit: schema/provenance, exact producer/tool pins, emitted sources, entrypoints, packaging and consumer checks together introduce the first usable API-7.0 package. They have one rollback/review boundary; a separate empty scaffold or unsupported intermediate pin state would add no supported consumer boundary. The large mechanical portion is independently bound/reconstructed as described below. **No obsolete scaffold, repeated pin stream, new migration or transitional migration remains.**

No new migration version needs merge/release/deployment/external-use accommodation. Packet provenance reports no prior release, deployment or external consumption of this generator/package; that is consistent with the source scope and private development package. This review does not establish fresh remote/default or deployed state.

## Architecture, proportionality and compatibility

HaveAPI appropriately owns schema parsing, naming, emission and the generated executor contract. vpsAdmin owns its mounted all-plugin fixture/export process; the generated package owns its captured inputs, exact producer identity and small consumer-facing adapter. Actual imports and manifests use the public RequestSpec/RequestResult contract from exact HaveAPI runtime 0.30.2. The adapter preserves its receiver and calls request directly; it adds no HTTP/authentication/retry implementation. Future WebUI adoption remains deferred, and no other session's sources were inspected.

The shared source generator version 0.30.0, npm runtime 0.30.2, API 7.0, protocol 2.0 and package 0.0.0 are distinct and recorded. Mounted/versioned paths are stripped by validated segments, and documentation correctly requires an already-versioned executor base. Authentication API-root operations remain explicitly inventoried and delegated to the existing runtime. Unknown schema constructs and naming collisions otherwise fail closed.

Input omission, explicit supported null/false/zero/empty values, safe numeric integers and path encoding have owning runtime checks. Response narrowing is confined to data, with metadata/envelope/status preserved; optional/nullable fields and partial associations avoid treating exported declarations as authorization or complete runtime validation. Server authorization remains authoritative. The declared lack of write replay/completion handling is appropriate for this scope.

The exporter rejects inherited database/test/plugin/Bundler configuration before loading the API, and its shell launcher rejects Ruby preloads before starting Ruby. The reviewed bootstrap obtains its database URL only from TestDb's owned automatic temporary instance before SpecDbSetup can reset it. It uses the real API/models/plugin migrations and established fixture setup without importing spec_helper stubs. No production/database migration or persistent application-state change is introduced. The trusted interpreter/PATH boundary and abnormal-termination cleanup limits are documented.

The scope is proportionate: one source generator, one controlled exporter and one generated package; no release framework, alternative transport, runtime API dependency update or WebUI takeover. The snapshot normalization duplication has already exposed the endpoint-check divergence in finding 2; its fix should stay bounded. Project documentation is discoverable and explains lasting executor/type/provenance/ownership/recovery limits rather than relying on session-only rollout notes.

## Verification evidence and limits

Independently recomputed:

- Canonical schema SHA256 `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794`; provenance `4bc121cd724fb0be5019e2347842699b9fab8b9e128f26acfea6d4a6f6614f5a`; exporter lock `223136cd93ebb408cab7ffa12e0a8f573ea4be01bee28211fe58eaa82c94308a`.
- Generator source digest `99617ced2222ad2d47121a60766626ef045e1d7d99c35db7e50d72d0aa863a9e`, root VERSION hash, all recorded downstream tooling hashes, exporter fixture/config hashes, all six plugin source digests and their existing migration inventories.
- Generated manifest SHA256 `dedba3efad4d99175c9790363e99fdb4ec1c327a82300de4fa0c24fdc38a5608` and each owned output file hash.
- Parsed full application inventory: **151 resources / 519 actions**, plus separately excluded **1 authentication resource / 5 actions**. Canonical JSON bytes match the saved schema.
- A pure in-memory run of the exact final IR/emitter in the client's pinned Nix environment reconstructed **all three emitted files byte-for-byte**, without writing output. The same source-only probe confirmed both findings.

Inspected the committed parser/output-safety tests, strict positive/negative type consumers, runtime spies, local package consumers, extracted-package checker and exact-published-runtime wire harness. The packet reports 21 focused generator checks, 14 DB-free exporter checks and successful full package construction/strict compilation/local consumer checks; these reported suites were not redundantly rerun.

Still required after finding reconciliation: the planned independent fresh-database repeat export, actual published-0.30.2 loopback wire harness and extracted npm-package ESM/declaration/consumer check. They were intentionally withheld before final review. No deployed-server permission behavior, WebUI/browser behavior, mixed deployed release pair or production compatibility was verified. The fixture schema describes declared mounted coverage, not object-specific preparation or a live user's capabilities. Registry publication, license selection, default-branch integration and deployment remain separately authorized decisions.

The lead should verify the narrow remediations and refreshed generated source/provenance pins under the skill's narrow-fix policy. A broadened public contract or new encoding design requires the affected review lanes again. This report supplies no integration or release approval.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/
