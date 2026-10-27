# 2026-10-26-typescript-client-generation

## Goal

I wonder about haveapi typescript client. As it is, apparently the user of this client must use findResource and findAction, unlike the javascript client, where the client auto-generates properties for resources and actions. Would it be better if we'd support generating typescript client against concrete API versions, like the client generators for go and rust do it? We'd then have vpsadmin-typescript-client. Would it be more developer-friendly and safe? Intend use of this client is in vpsadmin-webui. Please investigate and make suggestions.

## Affected repositories

- `haveapi`: TypeScript/JavaScript runtimes, Go/Rust generators and schema contracts.
- `vpsadmin-webui`: intended consumer and current API integration.
- `vpsadmin`, `vpsadmin-go-client`, `vpsadmin-rust-client`: API metadata, versioning and generated-client release examples.
- `vpsadmin-typescript-client`: user reports creating `vpsfreecz/vpsadmin-typescript-client`; complete generated private package now implemented in the dedicated worktree and published feature branch.

## Approved default integration — 2026-10-27

User “all right, let's merge it all” authorized all five registered targets.
All five are now integrated via fast-forward ordinary-hook/non-force SSH pushes,
remote heads independently verified, all claims released. Exact default heads are
in state.md. vpsAdmin exporter was patch-equivalently rebased over one disjoint
WebUI dependency update; old/new review binding is vpsadmin-rebase-equivalence.json.
Historical capture provenance and TS generator pin remain authentic/unchanged.
Rust/TS default CI passed, vpsAdmin CI remains running; HaveAPI performance rejects
the intentional12byte HTML identity change and supplies no timing conclusion.
No release, registry change, deployment or lifecycle action authorized/performed.

## Approach

## Performance gate follow-up

User approved implementing the simplified performance plan after observing that
response differences are normal code changes. Cross-revision response content
must never by itself fail or skip comparison. Keep the existing timing and
allocation regression limits (explicit user choice), functional/request-validity
checks and measurement/source/dependency/counter guards. Retain per-revision
canonical response-distribution stability keyed by actual verified source SHA.
Report raw/canonical content changes and bytes-per-request deltas separately.
Keep sample format2 and record actual comparator/policy and consumed sample hashes
without changing historical measurement identity or overwriting old evidence.

Architect0 records the accepted simplified brief; implementer0 owns the bounded
comparator/reporting/tests/docs change through checks/new commit/follow-ups; lead
owns final prose and reviewer0 final independent affected review. After review,
reanalyse the complete retained40529570313 samples once into a new report with
matching budgets. No new measurements, fixture framework/schema migration,
normalization/allowlist, budget/reference/event change or downstream repin.
All five earlier feature histories are merged: preserve them, add one new
performance commit from fresh HaveAPI master and publish the feature. The user
subsequently approved this exact HaveAPI/master integration with “merge it”.
No release, deployment or lifecycle action is authorized.

Implementation is complete at published HaveAPI `4d36efcf`. Focused checks and
independent final general/architecture/scope review passed without findings.
The retained original samples were reanalysed once: all 14 cases passed. All ten
feature CI workflows also passed, including a new measured 14-case performance
comparison of the genuine `18b45aed..4d36efcf` pair. The original failed run remains
unchanged. The user then approved “merge it”; normal fast-forward/SSH integration
18b45aed..4d36efcf is complete, fresh remote proof passed and the claim is released.
New master CI is pending at its first bounded snapshot (seven passes, three active).
[Final evidence](performance-response-feature-ci-result.json).

## Original implementation approach

Implementation authorized by the user after investigation. Implement the HaveAPI TypeScript generator, explicit reproducible schema input/export and the generated package in `vpsfreecz/vpsadmin-typescript-client`. Use this session's dedicated worktrees and published feature branches. Defer WebUI source edits until the user's integration of the HaveAPI 0.30.2 adoption; no integration, package releases, production API calls or deployment authorized here.

| Owner | Expected result / acceptance | Dependencies / checks / status |
| --- | --- | --- |
| architect0 | Accepted generator/exporter/executor contract in `design.md` | Complete; implementation boundaries and auth exclusion settled |
| implementer0 | Saved-schema parser/IR/naming/CLI/output ownership/shared registration | Complete; focused tests/hooks and both review fixes accepted |
| implementer2 | Pure emitter, generated types/runtime and published-runtime wire fixture | Complete; strict consumers/spies/full compile/wire pass |
| implementer1 | Guarded full-plugin mounted fixture export and actual provenance | Complete; 14 safety cases, fresh-DB repeat and final-source export pass |
| implementer3 | Generated ESM package, exact-source regeneration and packed consumers | Complete; construction/type-negative/local/extracted-package checks pass |
| reviewer0 | Independent complete-deliverable/history/migration review | Complete; two Important fixes verified narrowly; no migrations/obsolete history |
| Lead + fresh verification utility | Publish final branches, observe exact CI and assess results | Published; CI observation in progress; owners retain any follow-up fix |
| Future WebUI pilot | One collection read and one write above the upgraded runtime | Waits for separate HaveAPI upgrade integration; no WebUI source edits here |

## Current follow-up

The user approved implementation of the unified generator workflow and generated-TypeScript documentation examples. All three Go/Rust/TypeScript generators must save a portable schema with `fetch`, then generate offline from that file. Capture supports public access, HTTP Basic through environment-held passwords and existing HaveAPI tokens; no separate describe command is requested. Generic generator READMEs must include capture, generation and usage. The top-level README must distinguish the dynamic JavaScript/TypeScript runtime from the new saved-schema TypeScript generator. Ruby-server documentation gains a separately configured generated-TypeScript tab following the existing Go/Rust profile contract.

| Owner | Deliverable and acceptance | Dependencies and checks |
| --- | --- | --- |
| architect0 | Record accepted common capture and generated-TypeScript profile/adapter design at the top of `design.md` | Ready brief before substantive edits; retain complete naming and confidentiality boundaries |
| implementer0 | Shared standard-library snapshot core and lazy authenticated capture in the Ruby client package | Existing format-1 bytes; bounded public/Basic/token OPTIONS; focused unit/failure/secret tests |
| implementer1 | All three CLI integrations, helper compatibility, component dependencies/digests and generic generator/top-level READMEs | Common core API; Go legacy compatibility and real offline generation; lead final prose pass |
| implementer2 | Generator-owned TypeScript documentation adapter and strict rendered-snippet fixtures | Existing IR/naming, public executor/runtime, no runtime changes; unit and actual-snippet compilation |
| implementer3 | Ruby-server TypeScript profile/renderer/HTML integration, then exact downstream driver/pin/regeneration refresh | Adapter interface; authorized current descriptions, private mount model, distinct tabs; downstream follows exact accepted producer |
| reviewer0 | Complete committed affected deliverable and whole-history review | Quick checks first; all four lanes, no obsolete streams/migrations |
| Lead + verification utility | Bounded postreview root/mounted runtime and extracted-package checks; feature publication and exact-head CI | No production API calls, DB/export repeat, registry release, default integration, deployment or lifecycle action |

Shared source edits have one owner; shared Git/index/hooks are serialized. The downstream driver must explicitly load and verify the common Ruby source and expand its cleanliness/digest closure. This is a substantive tooling refresh, not a one-line pin change. Existing schema/provenance bytes and generated request contracts remain fixed. Preserve Go's supported positional command; do not add a new Go output-ownership framework or package registry/source configuration. Current generated-client package remains private.

Accepted final HaveAPI series: (1) shared Ruby schema/capture plus Rust facade/source identity, (2) common Go/Rust CLI workflow and compatibility, (3) one complete modular TypeScript generator consolidating the earlier parser/emitter series and final common integration, (4) generated-TypeScript documentation adapter plus server profile/renderer. Owner1 packaged this series after complete source/prose/check readiness and a coordinated writer pause. Mandatory final review of the complete committed deliverable found no findings, and the four-stage postreview acceptance batch passed. Feature publication and fresh exact-head CI are the current phase. Tests, docs and shared registration go with their owning behavior. Preserve old exact review refs as evidence; there are no released/deployed/externally consumed feature or migration boundaries requiring intermediate source/pin history. The downstream package remains one coherent initial package commit. Final HaveAPI `e6d4f797` and client `50a9602` are published with exact leases/default proof; fresh exact-head HaveAPI CI is being assessed. The unchanged exporter integration CI has passed.

## Trusted-publisher release preparation follow-up

User requested release workflows for `haveapi-typescript-client` and `vpsadmin-typescript-client`, using pending/trusted publishers, and explicitly said not to make a release. They confirmed the existing npm package/repository name; `vpsadmin-client-typescript` was a typo. Prepare and validate source workflows and operator setup guidance only. Implementation/quickchecks/normalcommits are complete at HaveAPIf02eca2e and client179a89c7; mandatory affected final review, requestednarrowfixes and newartifact checks are complete. CorrectedfinalHaveAPI18b45aed/client2dab582 are published/clean and allsevenfinalCIworkflows pass, including14case measuredperformance. Ready awaitingmergeapproval; noactualrelease. No registry account changes, version bump, tag, publication, deployment or default integration is authorized.

Architect0 owns design and confirms current RubyGems/npm trusted-publisher requirements and existing release conventions. Accepted execution boundaries: owner0 adds the TypeScript generator to HaveAPI release tooling; owner3 prepares the downstream npm workflow. Owner1 established that performance failure reflects the intentional genericHTMLdocumentation delta; reviewed source is retained and the original run remains failed without a timing claim. Preserve package identity, shared dependency loading, exact retained artifacts, publication approval boundaries and existing recovery behavior. The downstream package remains private0.0.0 until an explicitly authorized release-preparation change; no license choice is inferred.

## Generated-client README alignment

The user approved the common README plan and explicitly requested implementation.
This milestone is complete, reviewed and published; all13 final snippets compiled,
final Rust/TypeScript CI passed, and no release was made. See the current state
and README review/disposition for exact final heads and evidence.
Readers are developers comparing the Go, Rust and TypeScript SDKs. Each README
will introduce the package, installation and a complete existing-token example
listing the first 50 visible VPSes, followed by separate inspect and hostname-only
rename examples for VPS 123. Use `VPSADMIN_TOKEN`, show ID/hostname/running state,
and preserve each language's actual authentication, errors and optional outputs.
Remove the TypeScript opening dependency/private-publication wording, use truthful
local-tarball installation and move maintainer detail to `docs/development.md`.
Preserve generated code, package metadata, locks, pins and release safeguards.

| Owner | Result and acceptance | Dependencies and checks |
| --- | --- | --- |
| architect0 | Append the settled README design/verification brief | Existing source investigation accepted; brief before source edits |
| implementer0 | Go README and documentation commit | Fresh own worktree; exact code-fence compilation; normal hooks |
| implementer1 | Rust README, including blocking VPS example and current links | Fresh own worktree; async/blocking snippet compilation; normal hooks |
| implementer3 | TypeScript README and linked development guide | Existing own worktree; strict snippet compilation; normal hooks |
| Lead | Common flow and direct final user-facing prose pass | Preserve technical meaning across languages |
| reviewer0 | Independent final documentation and complete-history review | All intended changes committed, quick checks green; general lane |

The default runnable examples are read-only. Rename is a separate intentional
write example; no examples will be executed against an API. Verification uses
disposable compile consumers, link checks and whitespace checks, with a fresh
policy watcher for uncertain compilation. No regeneration, full integration
campaign, release, tag, registry change, merge, deployment or lifecycle action.
Documentation-only changes introduce no migration or runtime compatibility change.

## VPS lifecycle README extension

The user explicitly approved implementation of the lifecycle-guide plan. This
milestone is complete: all38 exact fences compile, independent review has no
findings, allthree featureheads are published/clean, and exact Rust/TS CI passed.
No release was made. Extend
the three generated-client READMEs in one coherent sequence: existing read-only
connect/list, catalogue location/template selection, minimal OR explicitly sized
creation, inspection/rename using the returned VPS ID, separate start/stop/restart
choices, then deletion. Ordinary-member creation needs hostname, chosen location
and OS template; environment sizing, node/pool/owner selection and default startup
stay with the server. The configured alternative shows CPU capacity2, memory
2048MiB, diskspace10240MiB and one IPv4/IPv6 allocation each. Explain allocation
counts, quotas and possible routed prefixes, asynchronous completion and normal
member soft deletion without adding polling or selection frameworks.

Architect0 records the settled appendix before edits; owners0/1/3 own Go/Rust/TS
README technical updates, exact-fence compile checks, normal owning documentation
amendments and review follow-ups. Lead aligns final prose. Reviewer0 performs
final general documentation/whole-history review after all intended amendments
and quick checks. Publish feature branches only with exact prior-head leases and
fresh SSH/default/clean proof; reconcile exact-head CI. All code is illustrative:
no examples execute or contact an API. No generated/runtime/schema/metadata/pin,
release/version/tag/registry/default/deployment/lifecycle changes.

## Decisions

- User now authorizes implementation. Default-branch integration and package releases remain separately approval-bound.
- Investigation findings and plans remain evidence; substantive source/docs/config deliverables require mandatory final review after commit and quick checks.
- User preference: prioritize one API version deployed alongside WebUI. Arbitrary independently upgraded servers are not the primary target.
- Recommended direction: concrete generated async client methods/types with injectable transport; publish version-pinned `vpsadmin-typescript-client` generated offline from an explicit reproducible API snapshot. Preserve generic HaveAPI for dynamic consumers and WebUI's current transport/domain policy.
- Stage adoption with one collection read and one write, then expand after validating compile-time contracts, optional/null semantics, metadata, cancellation, capabilities and uncertain-write behavior.
- Retain WebUI's HaveAPI 0.30.2 adoption owned by `2026-10-24-vpsadmin-haveapi-upgrade`. That replaces custom wire transport with the real npm AsyncClient; our generated facade will layer over the upgraded adapter. Earlier source evidence described cached main before adoption. Do not restore its old transport or modify the upgrade session's owned work.
- Future generator/schema work can proceed independently; WebUI integration should use the accepted upgraded baseline, preferably after it reaches main. Exact baseline and published runtime compatibility must be rechecked at implementation start.

## Compatibility and deployment

The source-only generator is additive and leaves existing clients/runtime behavior intact. vpsAdmin exporter uses separate exact0.30.2 tooling without changing normal API dependency pins. Its complete declared fixture/plugin schema is not a user permission set; generated types remain conservative for omitted/null output. The generated private ESM package pins API7.0 and HaveAPI runtime0.30.2, uses an injected RequestSpec/RequestResult executor targeting an already-versioned base, and performs no HTTP/auth/retry/response decoding. Authentication routes remain explicitly runtime-owned/inventoried.

No production schema, persistent state, daemon protocol, CLI/Terraform or host configuration changes. Tooling rollback selects prior source/artifacts; no deployment planned. WebUI adoption is dependent on the user's separate upgrade integration, not owned/taken over here. Feature publication does not authorize default integration or registry release. New repo publication may bootstrap only the proven empty root as main before feature push; no feature content is placed on default.

## Documentation

Readers: the user and future implementers. Preserve the comparison and proposed design in this session's `design.md`; keep status and source revisions in `state.md` and supporting findings. Lasting contracts are documented in HaveAPI clients/typescript/README.md, vpsAdmin docs/api-schema-export.md and the new client README.md; the lead applied the required direct writing pass before commits.

## Testing plan

Run meaningful generator, type-negative and executor contract checks; prove deterministic generation with explicit input/version/provenance and fail-closed unsupported schema/collision handling. Verify exporter fixtures against controlled loaded schemas and preserve omission/null/metadata/auth boundaries. Require normal hooks and local component checks before final review. Run bounded longer integration/build checks only after independent final review, using a fresh policy watcher. WebUI browser validation waits for the upgraded baseline; no production mutation.
