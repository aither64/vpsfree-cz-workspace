# Final affected review — trusted TypeScript release preparation

## Findings

Two Important findings at the assigned immutable client revision `179a89c7ac3ec7acf630ca99165db811c985e290`. No Blocking or additional Advisory findings. The lead has accepted both findings and assigned their narrow remediation; this report does not review or certify those subsequent edits.

**R1 — Important — normal package archives always fail the new listing checks.** `tools/check-package.mjs:45–48`, client commit `179a89c7` (general/verification).

The command helper returns stdout unchanged at line 25. Both `tar -tzf` and `tar -tvzf` terminate their normal listings with LF, so `.split('\n')` leaves an empty final element. The `details.every(...)` check rejects that element as a link/special file; the subsequent `entries.every(...)` check would also reject it as an unsafe path. Thus an ordinary valid archive cannot reach extraction, strict declarations or executor acceptance, and both the new workflow's `--archive` invocation and the existing local package check fail. The negative link fixture alone cannot distinguish this unrelated failure from correct link rejection.

Smallest correction: deliberately remove the listing terminator before splitting, retain the type/path/duplicate refusals, and verify that an ordinary valid archive reaches the real consumer. This follows directly from the committed code and standard tar output; I ran no test or package command.

**R2 — Important — a full rerun can replace an accepted tag build after its artifact is lost.** `.github/workflows/release.yml:48–69`, client commit `179a89c7` (risk/recovery).

The build job unconditionally installs, builds, packs and uploads on reruns. `overwrite: false` protects an artifact while it exists, but supplies no memory of an accepted upload after deletion or expiry. Re-running all jobs then rebuilds the same tagged version and creates a new artifact ID and receipt; that replacement can subsequently enter publication. This contradicts the accepted no-automatic-rebuild recovery contract and `docs/releasing.md:85–91`. Even a rerun while the old artifact exists performs the unnecessary rebuild before its upload eventually refuses.

Smallest correction: conservatively refuse tag build reruns before dependency preparation/build/packing, or restore/refuse the original artifact before any build. A conservative refusal is sufficient; no generalized recovery subsystem is needed. Preserve publish-job-only retry against its original immutable artifact ID, failing if missing. Focused coverage should bind the chosen refusal to the actual workflow.

The lead reported R1/R2 accepted and owner3 assigned exactly these narrow fixes. They remain findings against the reviewed original head; the lead will record separate direct verification and closure under the skill's narrow-fix policy.

## Review identity and scope

Reviewer0 performed the review directly and independently, with no nested agents or source/record writes. `dev-session current` returned `2026-10-26-typescript-client-generation`; DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE were both absent and the trusted developer binding matched `/home/aither/workspace/ai/vpsfree.cz`. The live same-session roster confirmed ready reviewer0, purpose review, read_only, saved `gpt-6.1-sol` / `xhigh`, thread `01a177e7-c4ad-7893-b980-0807c3ec58b3`. No overrides or fallback.

Read the complete release packet, current TOP design/accepted release brief, current plan/state, applicable workspace/repository procedures including release instructions, mandatory-change-review and all four lane references. Reviewed the new committed implementation, workflows, tests, package metadata, guides and actual consumers, plus the complete 5/2/1 history. Inspections used read-only Git/file operations and in-memory source hashing/comparison. No tests, builds, compilers, CI, network, fetch/push, registry or lifecycle action was performed.

Exact reviewed ranges:

- HaveAPI: `029f79b31cec93167f07e43e571c36b5f42d5b80..f02eca2e96d9fa6db6e8cb22a4f1fca7092c5ade`; tree `64e50969a34f6dd75b8906fe581c45179fdf7f03`.
- Client: genuine empty root `6c67b3c6e10e4096f6717345026371a89691f62a..179a89c7ac3ec7acf630ca99165db811c985e290`; tree `cc62c5608ceed93b995faaa9907c79837cb689a8`.
- vpsAdmin: `898e2881e8230d24fb06baee1c58737ae55e0009..7456c7eaae11cee0c76a984b1386a94656510f88`, unchanged exporter.

The client was clean at initial inspection. During final immutable-tree/history comparison, status showed owner3's newly authorized R1/R2 changes in four paths; those edits were excluded. All final artifact comparisons used explicit committed revisions. HaveAPI/exporter remained at their assigned clean heads. Prior unified review remains authoritative for the unchanged four HaveAPI commits and unchanged generated/runtime/exporter contracts.

## General lane

The new scope is release-workflow preparation only. The HaveAPI fifth commit adds the generator to coordinated releases, packages every source-digest input, validates retained content/locks and adds an extracted consumer. The client's independent second commit adds build/pack validation, tag publication preflight, an archive receipt and operator guidance. Package version, private flag, license choice, runtime peer, schema and dependency locks remain unchanged. No release, tag, registry configuration or upload was performed.

Docs correctly distinguish RubyGems pending first-gem publishing from npm's existing-package prerequisite. They leave npm bootstrap/ownership, license selection, environment protection and publisher activation as maintainer prerequisites. No invented pending-first-npm or credential fallback appears. R1 means the recorded quick negative checks do not establish positive archive acceptance; that remains a material gap until the valid archive path is exercised after correction.

## Architecture and repetition lane

HaveAPI extends the existing authoritative `Release::GEMS` inventory rather than adding a parallel publishing path. Its actual build, all-registry preflight, matching-version/conflict checks, client-first uploads and final confirmation enumerate that inventory. The new registry endpoint allowlist entry covers the TypeScript gem. Manifest verification retains the tenth component lock and validates it without requiring a locally installed component bundle in the tools-only job.

Gem inspection checks the TypeScript identity/Ruby floor/shared-client requirement, complete expected files and exact bytes; shared Ruby schema/version bytes are checked in the retained provider gem. The extracted smoke loads generator/schema code from the retained gems, clears ambient Ruby/Bundler overrides, compares source identities, runs the packaged executable's generate/check and uses a strict consumer with the prepared published 0.30.2 runtime. Candidate-source identity calculation is explicitly separate from the extracted consumer; it is not a source-loading fallback.

The npm helper stays repository-specific and small. Its receipt binds archive bytes, filename, package/version, source commit and tag; the publish job uses the immutable build artifact ID and verifies that receipt before invoking npm. The exact-source regeneration driver remains unchanged. No new registry/factory or generalized recovery framework was introduced. R2 can be fixed with a simple refusal, preserving this scope.

## Scope and proportionality lane

The fifth HaveAPI commit is independently useful release enablement after the functioning generator; the client's release capability is appropriately separate from its initial usable package. Tests target the owned metadata, content, publication prerequisites and receipt boundaries. Existing release machinery is reused, and no unrelated parser/runtime/framework or benchmark behavior changes were found.

No further hardening subsystem is requested. The two findings concern promised current behavior: usable archive validation and preservation of an accepted artifact. Their narrow corrections are proportionate to the authorized release-preparation scope.

## Risk and compatibility lane

Only the npm publish job receives OIDC; it is restricted to pushed tags in the canonical repository and names the `release` environment. Its preflight requires explicit activation, stable non-placeholder version/tag agreement, matching package-lock identity, intentional public metadata/license/file and ancestry on main. Branch/PR/manual paths cannot publish. The protected step verifies and publishes the retained tarball with scripts disabled, without rebuilding/repacking or installing npm dependencies. Configuring required environment reviewers/tag restrictions and external trust is a documented future maintainer prerequisite, not established by this source review.

HaveAPI preserves its existing protected/tag/release-branch gates and original-artifact recovery. Shared Ruby client is published before dependent generators. Old tagged workflows keep their original four-gem contract; the new five-gem verifier must not reinterpret their manifests. Current source VERSION 0.30.0 is not an authorized or ready release, and satisfying an old same-range Ruby dependency does not manufacture the shared API.

The new package metadata/source identity does not change runtime requests, generated types, captured schema or persisted state. Tools can be rolled back with matching source pins/manifests. No service/node deployment ordering or database upgrade is introduced. R2 is the specific unresolved artifact-recovery risk; no publishing credentials or live publication were exercised here.

## Independent source and artifact comparisons

Confirmed HaveAPI's first four commits are unchanged: `f02eca2e^` is exact `e6d4f797`. The release diff contains the assigned 13 paths; no parser/emitter/shared-schema/runtime or performance implementation changes occur.

Independently recomputed the new TypeScript source digest from committed bytes and canonical shared identity: `f7d79703fbe744cbcc56e57cf256b68c5bd819cf90bfa264aae9b3229c44049c`, matching the downstream pin/manifest. Shared identity remains haveapi-client 0.30.0 / `caf98b1e2e9a17f26eaae012fbb56808429f47083aac02d08305cd264aee5cc6`.

Compared client initial commit `95eeff73` with prior reviewed `50a9602`: only tools/generator.json and the generated ownership manifest differ. All 674 generated TypeScript mode/blob/path entries match. Saved schema/provenance/exporter lock, package metadata/npm lock, flake inputs, public src/index.ts, regeneration driver and source helper match. The ownership manifest differs only at generator_source_sha256. Its SHA256 is `48a6471ce38c767b17b174c76c56add6006350d4b01226542eab3498f2877727`; the pin SHA256 is `ab9587db10abf05e4dc351aaeab164b1302de17463a5c6dce1dbd6938d2a3fc4`. Client commit2 contains exactly the six release paths described by the packet.

## Complete history, obsolete approaches and repeated streams

Explicitly reviewed the final complete 5/2/1 series:

- HaveAPI `23fb16ec` shared schema/capture; `6a532e4a` Go/Rust CLI integration; `4916b44a` complete modular TS generator; `e6d4f797` generated TS documentation; `f02eca2e` coordinated release enablement.
- Client `95eeff73` one complete initial reproducible SDK, followed by `179a89c7` independent release automation.
- vpsAdmin `7456c7ea` one unchanged controlled exporter.

The new release boundaries are coherent and separately reviewable/revertible; no unrelated functional change is bundled into them. The initial SDK remains one coherent package from the genuine empty root, with final producer identity folded into it. The release workflow is correctly separate from that initial package rather than hidden in a mechanical pin commit.

No obsolete unmerged approaches, intermediate scaffolds, flat-output predecessors or redundant fixup commits remain in these reviewed ranges. Old reviewed/published refs remain provenance, not active branch history. No release/deployment/external-consumer boundary requires an intermediate implementation or pin.

No repeated pin/dependency/generated-metadata update stream remains: the SDK source/digest/ownership changes are consolidated in its initial commit, with one final selected producer. HaveAPI's release action installer pin changes are one coherent release-workflow update; component lock retention is part of that release capability. Earlier branch publication/review does not independently justify retaining superseded pins, and none are retained here. The later R1/R2 remediation is outside these immutable ranges and should be consolidated into its owning release commit by the lead/owner as appropriate.

## Migrations and residual acceptance

No migrations. The complete ranges introduce no database schema/seed migration, persisted runtime format or transitional upgrade state. Generated API actions named migrate/migration_plan are existing API operations. There is no merged/released/deployed/externally consumed feature-migration predecessor to preserve. Migration lineage is sound and empty.

R1/R2 require narrow closure before treating release preparation as reconciled. New retained/extracted TypeScript+shared gem acceptance and a positive exact npm archive/strict-consumer check remain unrun and required. Prior capture/rendered-wire/exporter results retain their unchanged input scope and do not certify these new release paths. Future final-head workflows and actual registry trust/authorization remain separately unverified.

The earlier performance run's intentional 12-byte HTML identity mismatch remains a recorded failure, not a measured timing pass. This release diff does not change the benchmark, baseline, budgets, refs or comparator; the next genuine push pair remains pending. No ancestor substitution or baseline workaround is accepted by this review.

This is source review, not artifact/runtime certification or permission for a version/tag/release, registry setting/upload, default integration, deployment or session lifecycle action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/
