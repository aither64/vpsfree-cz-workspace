# Final affected review packet — trusted TypeScript release preparation

Status: complete committed intended deliverable; quick checks and normal hooks pass. Ready for mandatory affected final review before new longer artifact acceptance. Both index/worktrees clean; all source/Git windows released.

## Requested result and boundaries

User requested release workflows for haveapi-typescript-client (Ruby generator gem) and vpsadmin-typescript-client (npm generated SDK), using trusted/pending publishers, and explicitly prohibited an actual release. Existing npm spelling was confirmed; no rename. Prepare usable source workflows, local/package validation and setup/recovery guidance. No version bump, tag, registry upload/settings, default integration, deployment or lifecycle action.

Accepted TOP design.md records owner boundaries, official current sources, latest compatible immutable action refs, package/recovery and actual registry limitations. RubyGems supports pending first-gem publishers. Official npm trust requires an existing package; no pending-first-npm upload is claimed. First npm bootstrap/ownership, license selection and external publisher setup are pending maintainer prerequisites. No credential/token fallback is added. The SDK remains private0.0.0/licenseunset; build-only path accepts that state while tag publication preflight refuses it.

## Exact repositories and complete history

Own verified session2026-10-26-typescript-client-generation in /home/aither/workspace/ai/vpsfree.cz. Worktrees at worktrees/<slug>/{haveapi,vpsadmin-typescript-client,vpsadmin}; state/plan/design/handoff in work/<slug>.

HaveAPI base/default029f79b31cec93167f07e43e571c36b5f42d5b80 -> final f02eca2e96d9fa6db6e8cb22a4f1fca7092c5ade, tree64e50969a34f6dd75b8906fe581c45179fdf7f03. Complete five commits:
1.23fb16ec7c693ada6c04528e102fa64538c408b9 shared schema/capture and Rust facade.
2.6a532e4a25947e4f065a77e50dc312146c21dd07 common Go/Rust CLI.
3.4916b44ae030788a53c0514d05642ff97540116a complete modular TypeScript generator.
4.e6d4f797fc92090fff265585196970e6b017003f generated TS adapter/server examples.
5.f02eca2e96d9fa6db6e8cb22a4f1fca7092c5ade independently reviewable release enablement.
The original four commits are untouched since unified-generator-review.md. New commit13paths522+/40- includes exact fifth-gem lifecycle, package inputs/smoke and docs/tests. It intentionally follows functioning generator/server behavior as a separate release capability.

Downstream genuine empty root6c67b3c6e10e4096f6717345026371a89691f62a -> 179a89c7ac3ec7acf630ca99165db811c985e290, treecc62c5608ceed93b995faaa9907c79837cb689a8. Complete two logical commits: initial functioning package95eeff73cda3d69805031caaa3e1f4debb00a7c3, treed920380c62a90e127027461cfc3cfd149ae6094d with final producer pin/digest/ownership identity; separate release automation179a89c7ac3ec7acf630ca99165db811c985e290. Compared to published50a9602, the initial commit differs only tools/generator.json and owned manifest. Commit2 exactly6paths385+/10-. No separate intermediate pin/fixup update retained. Six release paths: .github/workflows/release.yml, tools/check-package.mjs, tools/release.mjs, test/release.test.mjs, docs/releasing.md, README.md link. Package metadata/private/version/runtime/locks unchanged. The independent workflow capability is reviewable/revertible from the initial SDK; no release/state boundary is needed to justify the functional split.

vpsAdmin unchanged898e2881e8230d24fb06baee1c58737ae55e0009 ->7456c7eaae11cee0c76a984b1386a94656510f88, one exporter commit. Its exact-head integration and allCI passed. No new exporter/database work.

Prior unified review explicitly assessed whole4/1/1 history/no obsolete/repeated streams/no migrations and independently recomputed hashes. Preserve old exact ranges and report; assess this final complete5/2/1 history and new release boundaries, not only incrementaldiff. Earlier parser/emitter/runtime/schema/sourceclosure conclusions retained only for proven unchanged scope. Old publication refs are provenance only, not obsolete active history. No migrations/persisted runtime format; no feature released/deployed/externally consumed migration boundary. Repeated initialSDK pins/digest/manifest updates are consolidated into its one initial commit.

## Implementation and consumers

HaveAPI Release::GEMS is the existing inventory owner; it adds the fifth generator, shared-client-first order, all-registry preflight/hash/conflict/confirmation/recovery checks and exact retained artifact inventory. A tenth ignored local component lock is retained/validated in manifests. Source-only check-clean and tools-only retained verification remain usable without installed local component bundles. Original old tags retain their own four-gem helpers/artifacts; no reinterpretation.

Gemspec now packages Gemfile/Rakefile/own gemspec because source digest already includes those bytes, rather than weakening identity. Exact TS and shared Ruby gem content/identity checks and a new isolated extracted consumer bind loaded paths/versions/digests, actual executable offline generate/check, strict emitted modules and published JSruntime0.30.2 prepared before protected phase. No parser/emitter/runtime/shared schema edit. TSgenerator digest f7d79703fbe744cbcc56e57cf256b68c5bd819cf90bfa264aae9b3229c44049c; sharedhaveapi-client0.30.0/caf98b1e2e9a17f26eaae012fbb56808429f47083aac02d08305cd264aee5cc6 and VERSIONsha42659901f3c792eb230cf32b2c844ae738cd6d53dd84c1b7eb434e969b472ec2 unchanged.

SDK workflow uses hosted runner/pinned Nix, exact recorded public producer checkout, offline regenerate--check, build/types/units and one scripts-disabled npm pack. Existing checker accepts that retained archive and runs its real strict/executor consumer. Small receipt binds package/version/source/tag/filename/hash/SRI. Immutable artifactID passed to publish; publish tag-only/canonicalrepo/protectedrelease/job-onlyOIDC/preflight/no install/repack/build/scripts. Sourcepackageversion/private/license/tag/main/identity/hash prerequisites reject invalid publication. No GitHubRelease/disttag/generalrecovery framework or external registry mutation. Original archive retained; failed publish job retry only after registry reconciliation. Missing/expired accepted archive is not rebuilt automatically.

Cross-project consumer is this SDK's exact-source driver, unchanged except final producer/digest/manifest identity. 674 modules/saved schema/provenance/locks must remain byte-identical. Root/source APIs and generated request semantics do not change. Actual release installation order remains shared Ruby client before dependent generator. A same-range old Ruby-client gem lacks shared API; package/source docs are explicit, no fabricated first version.

## Quick evidence and documentation

All source packages complete/committed before final review; normal hooks required. Owner0 combined TSrelease/publisher/registry122/0, final TSfocused22/0,6Rubyfileslint; shell/smokeembedded syntax andmetadata checks pass. Owner3 release4/0 covers13badprerequisites, receiptarchive/source/tag/hashmismatch, linkarchive refusal and ACTUAL extracted inlineworkflowNode GITHUB_OUTPUT exactnewline. Fresh Luna/low actionlint bothworkflowsPASS13s exacthashpre/post; no mutation.

Lead directly applied vpsfree-user-facing-writing to HaveAPI clients/typescript/README.md, development/releases guides and downstream docs/releasing.md/READMElink. Checked placement/commands/actualtrustconstraints. No pending registry identity or firstpublicpackageclaim invented.

Final downstream construction PASS exit0 within60s first-failure bound: exactsource regenerate/check, release4/0, build, two strict typechecks and client4/0. All674TS mode/blob entries and schema/provenance/locks/othernonrelease tracked inputs equal50a9602; lead quick Git comparisons confirm6releasepaths and twoinitialidentitypaths. Manifest differs only generator_source_sha256, new SHA48a6471ce38c767b17b174c76c56add6006350d4b01226542eab3498f2877727; tools/generator.jsonSHAab9587db10abf05e4dc351aaeab164b1302de17463a5c6dce1dbd6938d2a3fc4. All6recorded tooling hashes stillmatch; releasefiles are not among them. Complete proof /tmp/2026-10-26-typescript-client-generation-release-client-proof.json. Both normal temp-F commits passed in declared Nix, no hookframework declared/no bypass.

New extracted TS+shared gem and exact retainednpmarchive acceptance remain UNRUN until final committed review reconciled. Prior public/Basic/token capture,14rendered/22wire, Ruby/Rust extracted and packed SDK acceptance passed at e6d4/50a in65s; original API/emitter/schema/runtime inputs remain unchanged, so no DB/export/renderedwire repetition needed.

## CI and performance limit

Published e6d4/50a prior checkpoint:10HaveAPI workflows passed (including release build/artifacts; protected publish skipped); performance40395934496 failed strict response identity for intentional12bytegenericHTMLprose change vs fae5508a. APIs/OPTIONS unchanged. Architect/lead retained technically correct reviewed sentence, not implied profile availability. A proposed conditionalcopy repair was reversed exactly before commit; no benchmark/comparator/budget/reference change/ref manipulation/ancestor substitute. Original failed run is not a timing regression or measuredpass. Next genuine e6d4->finalreleasecandidate push must be assessed normally. No CIretry/manualcampaign/release initiated. Finalfeaturepublication follows review and boundedpostreview checks.

## Review assignment

High risk because publication authority/OIDC, immutable artifact/recovery boundaries and crossproject packages. Eligible independent retained reviewer0, savedgpt-6.1-sol/xhigh/read_only, no overrides/fallback. Allfourlanes: general, architecture/repetition, scope/proportionality, risk/compatibility. Read SKILL and allfourreferences plus current workspace/repo required guidance. Direct read-only review, no nestedagents/source/recordwrites/builds/tests/CI/fetch/push/registry/lifecycle. Explicit complete5/2/1history/obsolete/repeatedpin/migration conclusion; reuse priorunchangedreview scope, independently assess new code/docs/consumers/limits. Report findings by severity, no sourcefixrequest if none. Lead saves verbatim as release-workflow-review.md.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/
