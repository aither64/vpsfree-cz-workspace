# React generated-SDK rebase — final independent affected review

Report from reviewer0, preserved by lead on 2026-11-14. This report covers the original reviewed range; remediation requires separate lead closure.

One Important finding, REACT-R1; no Blocking or additional Important findings. Lead accepted R1 and assigned owner2. The original reviewed source still requires that narrow correction; this report does not certify any successor or remediation. All four assigned lanes are complete.

## Finding

**REACT-R1 — Important, risk/compatibility and architecture integration: failed verification after an accepted settings write releases main's durable replay guard.**

Repository `vpsadmin-webui`, application commit `2202f08049fa254b6d3f029544c8c67b3834798a`, frozen head `5ffdb67df9d31de8a2de0952c73b92c9a234b424`:

- `src/pages/app/vps/VpsIncidentSettingsForm.tsx:51-54`: after `updateVps` succeeds without action-state metadata, mismatching/missing selected-type readback throws plain Error. A rejected verification GET, such as403 after a concurrent owner/access change, escapes as that read's HaveApiError.
- `VpsIncidentSettingsForm.tsx:72-76`: the error is passed to `settleLocalLock`; the retained draft remains dirty and Save has no independent unresolved-outcome condition.
- Current main's `src/lib/api/apiErrors.ts:126` classifies neither plain Error nor ordinary authoritative4xx read rejection as an ambiguous mutation. `src/components/layout/useLocalMutationLocks.ts:399-434` therefore removes the accepted write's durable generation instead of retaining its uncertainty guard.

The user can retry or perform another VPS mutation after the write was accepted but its result was not verified. This contradicts the reload-before-retry/readback contract and can overwrite concurrent administrator changes. The existing failure-render test mocks Chrome settlement and only checks error text/draft preservation, so its pass does not establish durable nonreplay behavior.

Smallest required outcome: classify every failure of this post-success verification stage through the existing uncertain-mutation boundary, preserve the exact durable generation and draft, and require the requested VPS identity as well as selected type/settings. Main's `updateIpAddress` at `src/lib/api/ipAddresses.ts:136-149` already demonstrates using existing MissingActionStateError for failed synchronous ownership verification. No new framework, global policy or transport is needed. Meaningful focused proof should cover mismatching readback and read4xx preserving the actual durable lock/nonreplay behavior, requested-ID mismatch, and exact selected-type success. Lead owns step9 inspection of the assigned narrow fix. I have not inspected or tested WIP remediation.

## Identity, settings and reviewed range

Trusted bound tracking-CWD current matched `2026-10-30-oomd-abuse-policy`; both DEV_SESSION markers were absent with no conflict. Live same-session roster verified reviewer0 ready / review purpose / read_only / gpt-6.1-sol / xhigh. Retained settings unchanged; no fallback or nested reviewers. Read mandatory-change-review plus all four current lane references and applicable unchanged workspace procedures; read repository AGENTS, design handbook/relevant REQ-051 and workflow/contracts, localization procedure, SDK/packaging references and incident work-log context. Previously reviewed SDK/backend and unaffected UI facts are reused proportionately, not treated as certification of this substantive rebase.

Exact complete range: `88ac13b89d6421c914cd57e18153de1fee6fc7b7..5ffdb67df9d31de8a2de0952c73b92c9a234b424`, tree `20e4583fe57fd2d02505b23614cac653290e5993`, branch `dev/oomd-abuse-policy`, existing PR115. Exact head/tree/merge base and initial clean status independently matched. After owner edits were authorized I continued against immutable original Git objects, not successor working-tree source. No tests, builds, check scripts, CI/provider queries, publication or file edits were performed.

## Lane conclusions

**General.** Compared requested default-branch rebase/localization scope with the41-file +1265/-45 final diff, delivery milestones and complete three-commit series. Most source is the previously accepted selected-type feature; new work integrates main's generated SDK and page conventions rather than treating the rebase as patch equivalence. Six substantive conflict areas were inspected: API contracts, requirements, VPS adapter, list page, layout and mobile list. Main's create toolbar, partial generated relations and disk-risk badges remain. Adapter, helper, rendered/filter tests and prepared E2E source meaningfully cover selector omission, explicit selection, null resets/false, primitive validation/no-send, normal server refusal, old-API hiding, selected-type isolation, role visibility, escaped labels and rapid/external filters. R1 is the remaining correctness/coverage exception.

**Architecture/repetition.** Backend owns registration/counting/authorization and localized stored report text; generated SDK owns paths/types/input validation; HaveAPI0.32.0 owns XHR/decoding; WebUI owns request policy, narrowing, receipts and presentation. New calls use `getApi().vps.index/show/update`; no raw transport, copied SDK, production cast fallback, BFF route or provider correction was added. VpsIncidentSettings derives from the generated input. Output guards extend main's existing boundary for all19 selected summary members without inventing defaults. List/detail/settings are the actual consumers, and desktop/mobile share the same indicator/card/settings logic. Finite status presentation is not a second registered-rule authority. R1 identifies where the preserved form needs to integrate with main's newer uncertainty classification rather than change that shared infrastructure.

**Scope/proportionality.** Current user scope requires adaptation to current default SDK architecture; the ordinary report localization remains backend-owned and adds no React locale field or new flow. This branch adds no rule builder, second production type, counting engine, transport or authorization subsystem. SDK HTTPS selection uses ordinary npm/Nix inputs with compact provenance and existing packaging. Synthetic second-rule fixtures remain tests. The retained narrow filter correction follows existing flushSync/latest-request conventions rather than replacing pagination/router internals. No unnecessary subsystem or speculative hardening found.

**Risk/compatibility.** Initial reads omit new selector/filter parameters; subsequent reads carry a returned supported selected key. Missing capabilities hide new UI instead of implying zero counts. Adapter preserves null limit resets and false enforcement. Server choice/authorization refusal remains authoritative; generated members do not grant permissions. Only valid isolated incident settings receive the added synchronous receipt exception; selector-only, malformed/mixed successes and unrelated updates retain strict guards, including malformed supplied receipts. Administrator mode plus actual admin role gates editor/filters; list requests retain owner scope. Submitted mutation data is snapshotted, and current gates/preflight/generation interfaces are retained, subject to R1's post-success verification defect. Shared stop permission/cooldown/outstanding action remain distinct from selected counts/limits/warnings. History links retain VPS/type context and labels render as text. No new client-side timer or frontend enforcement is introduced.

Rapid filters preserve the latest requested URL, flushSync navigation, effective limit, page1/cursor reset and external/Back adoption. Smart-filter signature/normalization includes incident filters; Clear clears both existing and new filters together. Empty results retain the selected capability instead of losing the controls. Current main's unrelated request/error/narrowing behavior is preserved.

## Dependency identity and exact evidence boundary

Independently compared manifest, both changed npm lock records and `packages/vpsadmin-typescript-client-development.json`: all select the same immutable SDK-owned HTTPS artifact at `6a6ca3613ce947a1393597d5ddcbc78294f6b12d`, packed source `6a5227c156aeef89447abb1f2e68988cecb735f4`. Local retained archive is341450 bytes, SHA256 `fee3800140869c1f721c5a07eda3e438d1a347690dc89aa5f8379a9efc1663bf`, and SHA512 equals lock integrity `sha512-CyHADzgOATfImrb71IBAQiZ37QBbZ4ZSaObiOzhDZ6dZi5IVMZhW0iY7BF4bT0mzoZk8BXx/i7eybfa8GiqZlQ==`. All1364 installed SDK files match that archive byte-for-byte. This reuses my independently reviewed SDK source and lead's separate delivery equivalence; I made no network request.

API input is reviewed7919441, raw schema `f919dcebf8ce5453dce6b0eb09e718f72664b5137443bb8e2064ff6452470ca7`, generator1ef9b204/0.32.2; consumer runtime remains HaveAPI0.32.0. Exactly the root lock record and SDK package record change; BFF, flake lock, shared SDK policy/error files and all other package records are unchanged. Frontend hash is `sha256-Q1gWCIYoWlM0eiagOEcIDNBTRvocm5urw64AkCLBlTc=`. No custom fetch pipeline or retained local archive path exists in committed selection.

This is an accepted development input, not a registry SDK release. Before any future WebUI merge, the published registry SDK prerequisite must be satisfied and manifest/lock/provenance/hash updated together. Compatible backend deployment/capability remains a separate gate. Rolling back the UI/package set does not reverse server settings already written.

## Whole-series, repeated-stream and migration conclusion

Complete series independently inspected:

1. `c255afdbe8f8563b08b2234f4873ec307d478bcb` — SDK dependency/provenance, ordinary lock/cache hash and owning SDK/packaging reference.
2. `2202f08049fa254b6d3f029544c8c67b3834798a` — selected incident feature, SDK integration, contract/copy and focused tests.
3. `5ffdb67df9d31de8a2de0952c73b92c9a234b424` — separately reviewable historical visual/evidence documentation and two capture-only scroll lines.

This split is coherent: provider input precedes consumer, and historical media/evidence is separate. One final SDK update stream exists. No superseded local-file dependency, obsolete OOM-prefixed implementation, intermediate pin/update stream, fixup history, shim or abandoned migration remains. This is substantively rebased source, not a claim of patch equivalence to `40653dff..9e7dd95d`; old source/ref/evidence remain historical. Consolidation/history is satisfactory apart from the required R1 source correction to be folded/verified separately.

**No migrations** in this repository/range. No React database or persisted-format conversion, transitional migration lineage or client/node protocol update is introduced. Backend migration review remains separately owned and is not certified by this UI review.

## Documentation placement/preservation — seven questions

1. **Reachable entry points:** root README links the design handbook, requirements and work log; handbook links API contracts, SDK provenance and packaging. REQ-051 links the incident change record; its image link reaches historical capture provenance.
2. **Audience and home:** behavior/permissions/selected receipts live in `docs/design/API_CONTRACTS.md`, `REQUIREMENTS.md`, `WORKFLOWS.md` and `EVIDENCE_MATRIX.md`; contributor input/release/rollback facts live in `HAVEAPI_CLIENT.md` and `PACKAGING.md`; exact execution/failures/media remain under the repository-permitted dated `docs/work-log/2026-10-30-incident-escalation.md` and screenshot README, with raw receipts in session tracking.
3. **Useful lifetime:** current references explain supported contracts independent of private session context. Temporary artifact selection is explicitly labeled development with a clear retirement condition; individual chronology stays in its dated home. Published baseline provenance is retained and labeled historical rather than current selection.
4. **Source/evidence fidelity:** omitted selectors, server choices, null/false and historical-vs-current evidence are accurately described. R1 is the exception to the claimed durable lock/readback safety and must be corrected; the existing88-test pass does not discharge it. No build/browser/deployment result is invented.
5. **Preservation:** conflicts preserve independent main handbook contracts and UI behavior. Existing SDK registry baseline provenance, anchors, authentication/request-policy limits, packaging prerequisites, separate BFF graph, uncertain-write warnings and rollback limits remain; no consequential instruction is moved away or dropped.
6. **Applicability/rollback:** development archive may be used now; registry artifact is mandatory before merge. Old APIs/capability checks and matching backend support remain explicit. Packaging restores the matching source/manifest/lock/hash set; frontend rollback leaves backend settings/audit intact. No supported upgrade path is retired or extra state migration assumed.
7. **Authority/links/prose:** backend remains authoritative for escalation and stored localization, SDK guide for selected input, packaging guide for cache/source boundary. Public guides do not require private records for supported usage. Existing anchors/local links remain. EN/CS feature catalogs and their reviewed copy are unchanged from the prior shared implementation; this rebase introduces no new translation behavior. KB impact ownership remains explicit and no KB/capture certification is claimed.

Placement/preservation is satisfactory, with R1 as the functional fidelity exception. No unrelated documentation restructuring is needed.

## Quick evidence, history reuse and remaining limits

Inspected native logs and receipts rather than running checks: corrected typecheck and seven files/88tests pass; E2E core types, lint, formatting, design/structural/component/UI-string/mutation audits pass with no new exception. Actual readback/lock integration remains the R1 gap. Retained initial nullable-typecheck failure and local-file Nix prefetch failure remain failures, followed by the corrected source/HTTPS input.

Independently matched recorded checked source hashes to the frozen original Git blobs. Prefetch and source-contents native receipts support their stated scope; final source-contents derivation is recorded as `/nix/store/gi2gzck9amk337wkhb4i5kxrriqrhmbk-vpsadmin-webui-source-contents.drv`. Neither proves a full frontend package build. The documented six bundled WASI optional-package warnings remain bounded by the pending actual build.

All four PNGs and their README are independently byte-identical to old9e7. They retain exact historical fixture/source distinctions and prior failed/scoped browser results, not current main integration or real backend appearance proof. Prior hosted/full-suite/browser results do not certify this rebase. No new full build, browser, runtime, exact-head hosted CI, production authorization, real backend accounting/transfer/mail/physical-stop acceptance or deployed capability is certified. Pending publication/PR update, required SDK registry replacement before merge, backend host acceptance and separate KB work remain outside this source verdict.

Disposition: complete original-range four-lane review; R1 is the only required correction. Publication remains held pending lead's narrow-fix verification. No successor source clearance, merge/deploy or session lifecycle action is authorized by this report.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
